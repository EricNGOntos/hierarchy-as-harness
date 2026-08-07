from __future__ import annotations

import concurrent.futures
import threading
from typing import Any, Dict, List, Optional, Tuple

from agent_delivery.code.tool_space import (
    CORPUS_DOC_ID,
    ToolSpace,
    is_corpus_doc_id,
    is_doc_root_section,
)
from agent_delivery.code.index_retrieval import Chunk
from path_ledger import doc_id_for

from nav_actions import build_legal_actions, format_actionable_map_observation
from nav_policy import choose_llm_action, choose_rule_action
from nav_projection import build_projection
from nav_types import (
    ActionKind,
    LegalAction,
    NavConfig,
    NavState,
    RegionReport,
)


def _batch_actions(chosen: LegalAction) -> List[LegalAction]:
    batch = (chosen.metadata or {}).get("batch_actions")
    if isinstance(batch, list) and batch:
        return [a for a in batch if isinstance(a, LegalAction)]
    return [chosen]


def _chunk_plain_chars(chunk: Chunk) -> int:
    text = (getattr(chunk, "text", None) or "").strip()
    if not text:
        return 0
    lines = text.splitlines()
    if lines and lines[0].strip().startswith("[§"):
        text = "\n".join(lines[1:]).strip()
    return len(text)


def _estimate_branch_chars(ts: ToolSpace, section_id: str, doc_id: str) -> int:
    """Evidence-sized estimate of hydrating section_id ∪ descendants."""
    sid = str(section_id or "").strip()
    if not sid:
        return 0
    materialize = getattr(ts, "_materialize_leaf_path_chunks", None)
    if not callable(materialize):
        return 0
    try:
        pool = list(materialize(sid, doc_id) or [])
    except Exception:
        return 0
    return sum(_chunk_plain_chars(c) for c in pool)


def _section_has_children(
    ts: ToolSpace,
    section_id: str,
    doc_id: str,
    projection: Any = None,
) -> bool:
    sid = str(section_id or "").strip()
    if not sid:
        return False
    if projection is not None:
        for view in list(getattr(projection, "tree_sections", None) or []) + list(
            getattr(projection, "visible_sections", None) or []
        ):
            if str(getattr(view, "section_id", "") or "") == sid:
                return bool(getattr(view, "has_children", False))
    relations = getattr(ts, "section_relation_ids", None)
    if callable(relations):
        try:
            _anc, desc = relations(sid, doc_id)
            desc = {str(x).strip() for x in (desc or set()) if str(x).strip()}
            desc.discard(sid)
            return bool(desc)
        except Exception:
            pass
    materialize = getattr(ts, "_materialize_leaf_path_chunks", None)
    if callable(materialize):
        try:
            pool = list(materialize(sid, doc_id) or [])
            return len(pool) > 1
        except Exception:
            return False
    return False


def _split_oversize_collect_actions(
    ts: ToolSpace,
    state: NavState,
    chosen: LegalAction,
    config: NavConfig,
    projection: Any,
) -> Tuple[List[LegalAction], List[LegalAction], List[Dict[str, Any]]]:
    """Split a COLLECT batch into (keep_collect, rewrite_dispatch, rewrite_info)."""
    limit = int(getattr(config, "depth0_oversize_char_limit", 0) or 0)
    keep: List[LegalAction] = []
    rewrite: List[LegalAction] = []
    info: List[Dict[str, Any]] = []
    for act in _batch_actions(chosen):
        sid = str(act.section_id or "").strip()
        if not sid:
            continue
        act_doc = doc_id_for(sid) or (
            state.doc_id if not is_corpus_doc_id(state.doc_id) else ""
        )
        chars = _estimate_branch_chars(ts, sid, act_doc) if act_doc else 0
        has_kids = _section_has_children(ts, sid, act_doc or state.doc_id, projection)
        if limit > 0 and chars > limit and has_kids:
            rewrite.append(
                LegalAction(
                    action_id=str(act.action_id or ""),
                    kind=ActionKind.DISPATCH,
                    section_id=sid,
                    label=str(act.label or ""),
                    score=float(act.score or 0.0),
                    metadata=dict(act.metadata or {}),
                )
            )
            info.append(
                {
                    "section_id": sid,
                    "branch_chars": chars,
                    "limit": limit,
                    "from_action_id": str(act.action_id or ""),
                }
            )
        else:
            keep.append(act)
    return keep, rewrite, info


def _estimate_region_chars(projection_text: str) -> int:
    return len(projection_text or "")


def _fork_nav_state(state: NavState, *, doc_id: Optional[str] = None) -> NavState:
    """Copy mutable evidence fields so concurrent subagents do not race."""
    return NavState(
        doc_id=str(doc_id) if doc_id is not None else state.doc_id,
        query=state.query,
        task_type=state.task_type,
        current_scope=state.current_scope,
        collected_ids=set(state.collected_ids),
        collected=list(state.collected),
        map_scores=dict(state.map_scores or {}),
        unit_scores=dict(state.unit_scores or {}),
        highlight_ids=list(state.highlight_ids),
        collected_section_ids=set(state.collected_section_ids),
        blocked_collect_section_ids=set(state.blocked_collect_section_ids),
        action_history=[],
        refusal_events=[],
        reports_context="",
        investigated_section_ids=set(),
        dismissed_section_ids=set(state.dismissed_section_ids),
        collect_confidence=dict(state.collect_confidence),
        explicit_collect_ids=set(state.explicit_collect_ids),
        group_priority=dict(state.group_priority),
        retrieval_plan=state.retrieval_plan,
        slot_bindings=dict(state.slot_bindings),
        subgoal_map_scores={
            k: dict(v) for k, v in (state.subgoal_map_scores or {}).items()
        },
        subgoal_unit_scores={
            k: dict(v) for k, v in (state.subgoal_unit_scores or {}).items()
        },
        hit_sources={k: list(v) for k, v in (state.hit_sources or {}).items()},
        active_subgoal_ids=list(state.active_subgoal_ids),
        satisfied_subgoal_ids=set(state.satisfied_subgoal_ids),
        attempted_subgoal_ids=set(state.attempted_subgoal_ids),
        activated_subgoal_ids=set(state.activated_subgoal_ids),
        focus_subgoal_id=state.focus_subgoal_id,
        focus_subgoal_need=state.focus_subgoal_need,
        focus_subgoal_contract=state.focus_subgoal_contract,
        focus_retrieval_query=state.focus_retrieval_query,
        focus_contract_kind=state.focus_contract_kind,
        focus_scope_doc_ids=list(state.focus_scope_doc_ids or []),
        subgoal_results=dict(state.subgoal_results),
        replan_count=int(state.replan_count or 0),
    )


def _merge_nav_state(parent: NavState, child: NavState) -> None:
    """Merge a forked subagent state into the parent (called under lock)."""
    for chunk, score in child.collected:
        nid = getattr(chunk, "node_id", None)
        if nid is None or nid in parent.collected_ids:
            continue
        parent.collected_ids.add(nid)
        parent.collected.append((chunk, float(score)))
    parent.collected_section_ids.update(child.collected_section_ids)
    parent.blocked_collect_section_ids.update(child.blocked_collect_section_ids)
    parent.investigated_section_ids.update(child.investigated_section_ids)
    parent.dismissed_section_ids.update(child.dismissed_section_ids)
    parent.refusal_events.extend(child.refusal_events)
    parent.action_history.extend(child.action_history)
    parent.collect_confidence.update(child.collect_confidence)
    parent.explicit_collect_ids.update(child.explicit_collect_ids)
    parent.group_priority.update(child.group_priority)
    parent.slot_bindings.update(child.slot_bindings)
    parent.satisfied_subgoal_ids.update(child.satisfied_subgoal_ids)
    parent.attempted_subgoal_ids.update(child.attempted_subgoal_ids)
    parent.activated_subgoal_ids.update(child.activated_subgoal_ids)
    parent.subgoal_results.update(child.subgoal_results)
    if child.reports_context:
        if parent.reports_context:
            parent.reports_context = parent.reports_context + "\n" + child.reports_context
        else:
            parent.reports_context = child.reports_context


def _apply_collect(
    ts: ToolSpace,
    state: NavState,
    chosen: LegalAction,
    config: NavConfig,
) -> Dict[str, Any]:
    """Run one (possibly batched) COLLECT; mutates state."""
    from nav_agent import (  # late import avoids cycle
        _add_scored,
        _collect_subtree,
        _mark_collected_branch,
        _purge_descendant_evidence,
    )
    from nav_compose import evidence_owner_section_id

    detail: Dict[str, Any] = {
        "kind": "collect",
        "section_id": chosen.section_id,
        "collect_section_ids": [],
        "n_added": 0,
        "n_hits": 0,
        "n_purged_descendant_evidence": 0,
    }
    total_added = 0
    total_hits = 0
    total_purged = 0
    sids: List[str] = []
    conf_by_sid = dict((chosen.metadata or {}).get("confidence_by_section") or {})
    for act in _batch_actions(chosen):
        sid = str(act.section_id or "").strip()
        if not sid:
            continue
        # Explicit COLLECT root: record target + confidence from LLM (missing => 0).
        state.explicit_collect_ids.add(sid)
        conf = float(conf_by_sid.get(sid, 0.0) or 0.0)
        state.collect_confidence[sid] = max(0.0, min(1.0, conf))
        # Absorb prior child COLLECTs (e.g. L93) before parent hydrate (L92).
        total_purged += _purge_descendant_evidence(ts, state, sid)
        scored = _collect_subtree(ts, act, state, config)
        # Hydration descendants: confidence stays 0 unless previously explicit.
        for chunk, _score in scored:
            owner = evidence_owner_section_id(chunk)
            if owner and owner != sid:
                state.collect_confidence.setdefault(owner, 0.0)
        added = _add_scored(state, scored)
        cov = _mark_collected_branch(ts, act, state, added)
        total_added += added
        total_hits += len(scored)
        sids.append(sid)
        detail.update(cov)
    detail["n_added"] = total_added
    detail["n_hits"] = total_hits
    detail["n_purged_descendant_evidence"] = total_purged
    detail["collect_section_ids"] = sids
    if sids:
        detail["section_id"] = sids[0]
    return detail


def _format_region_reports(reports: List[RegionReport]) -> str:
    if not reports:
        return ""
    lines = [f"=== Investigate results ({len(reports)} region(s)) ==="]
    for i, rep in enumerate(reports, 1):
        scope = rep.scope or "<unknown>"
        status = "skipped" if rep.skipped else "ok"
        lines.append(f"[region {i}] {scope} ({status})")
        if rep.summary:
            lines.append(rep.summary)
        if rep.collected_section_ids:
            lines.append(
                "collected: " + ", ".join(rep.collected_section_ids[:20])
            )
        if rep.reason:
            lines.append(f"reason: {rep.reason}")
        lines.append("---")
    lines.append("=== End Investigate ===")
    return "\n".join(lines)


def dispatch(
    ts: ToolSpace,
    state: NavState,
    ids: List[str],
    *,
    query: str,
    config: NavConfig,
    depth: int,
    budget: int,
    steps_out: Optional[List[Any]] = None,
) -> List[RegionReport]:
    """Concurrently run navigate() on each region id (fork/merge state).

    Corpus→synthetic-document-root DISPATCH is depth-neutral: the document
    episode starts at depth 0. A direct corpus→real-section DISPATCH already
    descends one in-document level, so it starts at depth 1.
    """
    scope_now = str(state.current_scope or "").strip()
    region_ids = [
        rid
        for rid in (str(x).strip() for x in ids if str(x).strip())
        if rid != scope_now  # never re-enter the current scope (self-dispatch)
    ]
    if not region_ids:
        return []

    group_size = max(1, int(config.dispatch_group_size))
    max_workers = max(1, int(config.dispatch_max_workers))
    child_budget = max(500, int(budget * 0.85))
    merge_lock = threading.Lock()
    corpus_parent = is_corpus_doc_id(state.doc_id)

    def _run_one(rid: str) -> RegionReport:
        child_doc = doc_id_for(rid)
        # Leaving the corpus sentinel switches to the real document state.
        # Only the virtual document root is depth-neutral. Entering a real
        # section directly is equivalent to entering the document and then
        # dispatching that section in single-document mode.
        enter_doc = (
            corpus_parent
            and bool(child_doc)
            and not is_corpus_doc_id(child_doc)
            and child_doc != CORPUS_DOC_ID
        )
        with merge_lock:
            if enter_doc:
                child_state = _fork_nav_state(state, doc_id=str(child_doc))
                child_depth = 0 if is_doc_root_section(rid) else 1
            else:
                child_state = _fork_nav_state(state)
                child_depth = depth + 1
        try:
            report = navigate(
                ts,
                state=child_state,
                scope=rid,
                query=query,
                config=config,
                depth=child_depth,
                budget=child_budget,
                steps_out=None,  # parent records dispatch; child history merges via state
            )
        except Exception as exc:
            report = RegionReport(
                scope=rid,
                summary="",
                reason=f"dispatch_failed: {exc}",
                skipped=True,
                depth=child_depth,
            )
        with merge_lock:
            _merge_nav_state(state, child_state)
            if steps_out is not None:
                from agent_delivery.agent.types import AgentStep

                for h in child_state.action_history:
                    steps_out.append(
                        AgentStep(
                            step_idx=len(steps_out) + 1,
                            action=f"nav_{h.get('kind', 'step')}",
                            detail=dict(h),
                        )
                    )
        return report

    reports: List[RegionReport] = []
    if max_workers <= 1 or len(region_ids) == 1:
        for rid in region_ids:
            reports.append(_run_one(rid))
        return reports

    for start in range(0, len(region_ids), group_size):
        batch = region_ids[start : start + group_size]
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=min(max_workers, len(batch))
        ) as pool:
            futs = {pool.submit(_run_one, rid): rid for rid in batch}
            for fut in concurrent.futures.as_completed(futs):
                try:
                    reports.append(fut.result())
                except Exception as exc:
                    rid = futs[fut]
                    reports.append(
                        RegionReport(
                            scope=rid,
                            reason=f"dispatch_failed: {exc}",
                            skipped=True,
                            depth=depth + 1,
                        )
                    )
    return reports


def navigate(
    ts: ToolSpace,
    *,
    state: NavState,
    scope: Optional[str],
    query: str,
    config: NavConfig,
    depth: int = 0,
    budget: Optional[int] = None,
    steps_out: Optional[List[Any]] = None,
) -> RegionReport:
    """Recursive observe-act loop: COLLECT / DISPATCH / FINISH.

    When enable_recursive_dispatch is False, only depth==0 may DISPATCH; deeper
    regions hard-COLLECT visible nodes or skip on overflow/error.
    """
    from agent_delivery.agent.types import AgentStep

    char_budget = int(budget if budget is not None else config.map_char_limit)
    prev_scope = state.current_scope
    state.current_scope = scope
    collected_before = set(state.collected_section_ids)
    max_steps = max(1, int(config.navigate_max_steps if depth > 0 else config.max_steps))
    report = RegionReport(scope=scope, depth=depth)

    try:
        for step_idx in range(max_steps):
            projection = build_projection(
                ts,
                doc_id=state.doc_id,
                query=query,
                scope=scope,
                config=config,
                map_scores=state.map_scores,
                collected_section_ids=state.collected_section_ids,
                dismissed_section_ids=state.dismissed_section_ids,
                highlight_ids=state.highlight_ids,
                hit_sources=state.hit_sources or None,
            )
            # Experimental non-recursive mode: if a deep region overflows the
            # map budget after folding, skip rather than invent hard truncation.
            if (
                depth > 0
                and not config.enable_recursive_dispatch
                and _estimate_region_chars(projection.text) > char_budget * 2
                and projection.truncated
            ):
                report.skipped = True
                report.reason = "region_overflow_skip"
                break

            actions = build_legal_actions(
                state,
                projection,
                step_idx=step_idx,
                config=config,
                depth=depth,
                max_steps=max_steps,
            )
            if not actions:
                report.reason = "no_legal_actions"
                break

            obs = format_actionable_map_observation(
                projection,
                actions,
                inline_summary=scope is not None,
            )
            projection.text = obs

            group_map: Dict[str, str] = {}
            assembled_preview = ""
            if (
                depth == 0
                and bool(getattr(config, "enable_external_rerank", True))
                and state.collected
            ):
                from nav_compose import build_compose_preview, dedupe_scored

                assembled_preview, group_map = build_compose_preview(
                    dedupe_scored(list(state.collected)),
                    ts,
                    state,
                    config,
                )

            if (config.policy or "").strip().lower() == "llm":
                chosen, meta = choose_llm_action(
                    state,
                    projection,
                    actions,
                    step_idx=step_idx,
                    config=config,
                    depth=depth,
                    max_steps=max_steps,
                    group_map=group_map or None,
                    assembled_preview=assembled_preview or None,
                )
            else:
                chosen = choose_rule_action(
                    state, projection, actions, step_idx=step_idx, config=config
                )
                meta = {"reason": "rule_policy"}

            detail: Dict[str, Any] = {
                "action_id": chosen.action_id,
                "kind": chosen.kind.value,
                "section_id": chosen.section_id,
                "scope": scope,
                "llm_reason": meta.get("reason"),
                "llm_raw": meta.get("raw"),
                "depth": depth,
                "n_legal_actions": len(actions),
                "legal_actions_preview": [a.prompt_line() for a in actions[:16]],
                "projection_chars": len(obs),
            }
            if meta.get("group_rank"):
                detail["group_rank"] = meta.get("group_rank")

            if chosen.kind == ActionKind.FINISH:
                report.reason = str(meta.get("reason") or "finish")
                if steps_out is not None:
                    steps_out.append(
                        AgentStep(
                            step_idx=len(steps_out) + 1,
                            action="nav_finish",
                            detail=detail,
                        )
                    )
                state.action_history.append({**detail, "step_idx": step_idx})
                break

            if chosen.kind == ActionKind.COLLECT:
                keep_acts = _batch_actions(chosen)
                rewrite_acts: List[LegalAction] = []
                rewrite_info: List[Dict[str, Any]] = []
                if depth == 0 and bool(
                    getattr(config, "enable_depth0_oversize_to_dispatch", False)
                ):
                    keep_acts, rewrite_acts, rewrite_info = _split_oversize_collect_actions(
                        ts, state, chosen, config, projection
                    )

                # Oversized branches first: rewrite COLLECT -> DISPATCH.
                if rewrite_acts:
                    region_ids = [
                        str(a.section_id or "").strip()
                        for a in rewrite_acts
                        if a.section_id
                    ]
                    child_reports = dispatch(
                        ts,
                        state,
                        region_ids,
                        query=query,
                        config=config,
                        depth=depth,
                        budget=char_budget,
                        steps_out=steps_out,
                    )
                    for rid in region_ids:
                        state.investigated_section_ids.add(rid)
                    block = _format_region_reports(child_reports)
                    if block:
                        if state.reports_context:
                            state.reports_context = (
                                state.reports_context + "\n" + block
                            )
                        else:
                            state.reports_context = block
                    ddetail = {
                        **detail,
                        "kind": "dispatch",
                        "rewritten_collect_to_dispatch": True,
                        "rewrite_info": rewrite_info,
                        "dispatch_regions": region_ids,
                        "n_child_reports": len(child_reports),
                        "n_child_skipped": sum(1 for r in child_reports if r.skipped),
                        "reports_snippet": (block or "")[:2000],
                        "section_id": region_ids[0] if region_ids else chosen.section_id,
                    }
                    if steps_out is not None:
                        steps_out.append(
                            AgentStep(
                                step_idx=len(steps_out) + 1,
                                action="nav_dispatch",
                                detail=ddetail,
                            )
                        )
                    state.action_history.append({**ddetail, "step_idx": step_idx})

                # Remaining non-oversize COLLECTs (if any).
                if keep_acts:
                    collect_chosen = keep_acts[0]
                    base_meta = dict(chosen.metadata or {})
                    # Drop the original full batch; rebuild from keep_acts only.
                    base_meta.pop("batch_actions", None)
                    if len(keep_acts) > 1:
                        base_meta["batch_actions"] = keep_acts
                    collect_chosen.metadata = base_meta
                    cdetail = _apply_collect(ts, state, collect_chosen, config)
                    cdetail_full = {
                        **detail,
                        **cdetail,
                        "kind": "collect",
                        "rewritten_collect_to_dispatch": bool(rewrite_info),
                        "rewrite_info": rewrite_info or None,
                    }
                    if steps_out is not None:
                        steps_out.append(
                            AgentStep(
                                step_idx=len(steps_out) + 1,
                                action="nav_collect",
                                detail=cdetail_full,
                            )
                        )
                    state.action_history.append({**cdetail_full, "step_idx": step_idx})
                elif not rewrite_acts:
                    # Empty selection — should not happen; fall back to original.
                    cdetail = _apply_collect(ts, state, chosen, config)
                    detail.update(cdetail)
                    if steps_out is not None:
                        steps_out.append(
                            AgentStep(
                                step_idx=len(steps_out) + 1,
                                action="nav_collect",
                                detail=detail,
                            )
                        )
                    state.action_history.append({**detail, "step_idx": step_idx})
                continue

            if chosen.kind == ActionKind.DISPATCH:
                region_ids = [
                    str(a.section_id or "").strip()
                    for a in _batch_actions(chosen)
                    if a.section_id
                ]
                # Non-recursive experiment: deep agents should not see DISPATCH
                # (build_legal_actions gates it); still guard here.
                if depth > 0 and not config.enable_recursive_dispatch:
                    detail["skipped_dispatch"] = True
                    detail["reason"] = "recursive_dispatch_disabled"
                    if steps_out is not None:
                        steps_out.append(
                            AgentStep(
                                step_idx=len(steps_out) + 1,
                                action="nav_dispatch_skipped",
                                detail=detail,
                            )
                        )
                    continue

                child_reports = dispatch(
                    ts,
                    state,
                    region_ids,
                    query=query,
                    config=config,
                    depth=depth,
                    budget=char_budget,
                    steps_out=steps_out,
                )
                for rid in region_ids:
                    state.investigated_section_ids.add(rid)
                block = _format_region_reports(child_reports)
                if block:
                    if state.reports_context:
                        state.reports_context = state.reports_context + "\n" + block
                    else:
                        state.reports_context = block
                detail["dispatch_regions"] = region_ids
                detail["n_child_reports"] = len(child_reports)
                detail["n_child_skipped"] = sum(1 for r in child_reports if r.skipped)
                detail["reports_snippet"] = (block or "")[:2000]
                if steps_out is not None:
                    steps_out.append(
                        AgentStep(
                            step_idx=len(steps_out) + 1,
                            action="nav_dispatch",
                            detail=detail,
                        )
                    )
                state.action_history.append({**detail, "step_idx": step_idx})
                continue

            # Unknown kind — stop.
            report.reason = f"unknown_action:{chosen.kind}"
            break
        else:
            report.reason = report.reason or "max_steps"

    except Exception as exc:
        report.skipped = True
        report.reason = f"navigate_error: {exc}"
    finally:
        state.current_scope = prev_scope

    newly = sorted(state.collected_section_ids - collected_before)
    report.collected_section_ids = newly
    roots = [
        str(h.get("section_id") or "")
        for h in state.action_history
        if h.get("kind") == "collect"
        and int(h.get("n_added", 0) or 0) > 0
        and h.get("section_id")
    ]
    report.summary = (
        f"collected {len(newly)} branch node(s); explicit roots={roots[-8:]}"
        if newly
        else (report.reason or "no new evidence")
    )
    return report


def sort_collected_by_doc_order(
    scored: List[Tuple[Chunk, float]],
    ts: ToolSpace,
    doc_id: str,
) -> List[Tuple[Chunk, float]]:
    """Order evidence by (doc_id, line). Cross-doc when doc_id is the corpus sentinel."""
    idx = getattr(ts, "_idx", None)
    node_map = getattr(idx, "_node_to_doc_line", {}) if idx is not None else {}
    corpus = is_corpus_doc_id(doc_id)

    def key(item: Tuple[Chunk, float]) -> Tuple[str, int, int, str]:
        chunk, _score = item
        cdoc = str(getattr(chunk, "doc_id", "") or "")
        line_ids = list(chunk.line_ids or ())
        if line_ids:
            ln = min(line_ids)
            return (cdoc if corpus else "", ln, ln, chunk.node_id)
        loc = node_map.get(chunk.node_id) or node_map.get(
            str(getattr(chunk, "section_id", "") or "")
        )
        if loc and len(loc) >= 2:
            loc_doc, loc_line = str(loc[0]), loc[1]
            if corpus or loc_doc == doc_id:
                try:
                    li = int(loc_line)
                    return (loc_doc if corpus else "", li, li, chunk.node_id)
                except Exception:
                    pass
        return (cdoc if corpus else "\uffff", 10**9, 10**9, chunk.node_id)

    return sorted(scored, key=key)
