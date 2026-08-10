"""M4/M5/M6: wave orchestration over a RetrievalPlan.

Execution order = dependency DAG ∩ soft prefer_after. Each subgoal runs its own
navigate→verify so evidence attribution stays per-subgoal.
Soft plan: never clips C*/D*/F* action space — only changes query focus,
bindings, fold weights, and TRACE.

M6 ``BudgetLedger`` / ``settle_subgoal_evidence`` live in ``nav_compose``
(wired from ``run_nav_episode`` after orchestration).
"""

from __future__ import annotations

import re
import time
from dataclasses import asdict
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

from nav_illuminate import illuminate_from_plan, refresh_fold_from_subgoal_scores
from nav_navigate import navigate
from nav_plan import (
    RetrievalPlan,
    ScopeFilter,
    Subgoal,
    bind_slots,
    is_always_active,
    plan_query,
    unbound_slots,
)
from nav_types import NavConfig, NavState, SubgoalResult
from nav_verify import (
    activation_when_holds,
    apply_bindings_from_result,
    build_evidence_text_from_chunks,
    extract_slots,
    verify_contract,
)

_SLOT_STRIP_RE = re.compile(r"\{\{\s*[^}]+\s*\}\}")


def ready_subgoal_ids(
    plan: RetrievalPlan,
    *,
    satisfied: Set[str],
    activated: Set[str],
    attempted: Optional[Set[str]] = None,
    dropped: Optional[Set[str]] = None,
) -> List[str]:
    """Subgoals eligible to run now (deps settled, activated, not yet finished).

    F1 fix: a dependency only needs to be *settled* (``satisfied`` or
    ``dropped``, never both — see ``NavState.dropped_subgoal_ids``), not
    specifically ``satisfied``. A dropped precursor must not starve every
    downstream subgoal forever. Readiness no longer requires the retrieval
    query to be fully slot-bound either: once deps are settled the caller
    degrades an unbound query (``_unbound_retrieval_query``) instead of
    waiting on a slot that a dropped precursor will never produce.
    """
    settled = set(satisfied) | set(dropped or ())
    known = {s.id for s in plan.subgoals}
    done = set(attempted or ()) | set(satisfied)
    out: List[str] = []
    for sg in plan.subgoals:
        if sg.id in done:
            continue
        if not is_always_active(sg) and sg.id not in activated:
            continue
        deps = [d for d in (sg.depends_on or []) if d in known]
        if any(d not in settled for d in deps):
            continue
        out.append(sg.id)
    return order_ready_by_prefer_after(plan, out)


def order_ready_by_prefer_after(
    plan: RetrievalPlan,
    ready_ids: Sequence[str],
) -> List[str]:
    """Soft ordering: if A prefer_after B and both ready, B before A."""
    ready = [str(x) for x in ready_ids]
    if len(ready) <= 1:
        return ready
    by = {s.id: s for s in plan.subgoals}
    ready_set = set(ready)
    # Kahn over soft edges B -> A when A prefer_after B.
    indeg = {i: 0 for i in ready}
    edges: Dict[str, List[str]] = {i: [] for i in ready}
    for sid in ready:
        sg = by.get(sid)
        if sg is None:
            continue
        for pred in sg.prefer_after or []:
            if pred in ready_set and pred != sid:
                edges[pred].append(sid)
                indeg[sid] += 1
    queue = [i for i in ready if indeg[i] == 0]
    ordered: List[str] = []
    seen = set()
    while queue:
        # Stable: keep original relative order among zero-indegree nodes.
        queue.sort(key=lambda x: ready.index(x))
        node = queue.pop(0)
        if node in seen:
            continue
        seen.add(node)
        ordered.append(node)
        for nxt in edges.get(node, []):
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                queue.append(nxt)
    for sid in ready:
        if sid not in seen:
            ordered.append(sid)
    return ordered


def _set_focus(state: NavState, subgoal: Subgoal, retrieval_query: str) -> None:
    state.focus_subgoal_id = subgoal.id
    state.focus_subgoal_need = subgoal.need or retrieval_query
    state.focus_retrieval_query = retrieval_query
    kind = subgoal.contract.kind
    card = subgoal.contract.cardinality
    state.focus_contract_kind = str(kind or "")
    state.focus_subgoal_contract = (
        f"{kind}" + (f" cardinality={card}" if card is not None else "")
    )
    state.focus_scope_doc_ids = list(subgoal.scope_filter.doc_ids or [])


def _clear_focus(state: NavState) -> None:
    state.focus_subgoal_id = ""
    state.focus_subgoal_need = ""
    state.focus_subgoal_contract = ""
    state.focus_retrieval_query = ""
    state.focus_contract_kind = ""
    state.focus_scope_doc_ids = []


def _widen_scope_filter(subgoal: Subgoal) -> None:
    """Clear scope_filter so the next attempt can look more broadly."""
    subgoal.scope_filter = ScopeFilter()


def _unbound_retrieval_query(subgoal: Subgoal) -> str:
    """Drop unresolved slot braces for REBIND degrade."""
    raw = _SLOT_STRIP_RE.sub(" ", subgoal.retrieval_query or "").strip()
    raw = re.sub(r"\s+", " ", raw).strip()
    return raw or (subgoal.need or "").strip() or subgoal.retrieval_query


def _run_navigate_for_query(
    ts: Any,
    state: NavState,
    config: NavConfig,
    *,
    query: str,
    steps_out: Optional[List[Any]],
) -> None:
    navigate(
        ts,
        state=state,
        scope=None,
        query=query,
        config=config,
        depth=0,
        budget=int(config.map_char_limit),
        steps_out=steps_out,
    )


def _verify_subgoal(
    state: NavState,
    config: NavConfig,
    subgoal: Subgoal,
    *,
    retrieval_query: str,
    new_chunks: Sequence[Tuple[Any, float]],
    collected_before: Set[str],
    force_llm_extract: bool = False,
) -> SubgoalResult:
    """Verify against THIS call's own new evidence only (never the global pool).

    ``new_chunks`` must be the chunks collected since ``collected_before`` was
    snapshotted — mixing in older/other-subgoal evidence here is exactly the
    attribution leak audited in docs/audit_plan_nav_overlap.md §1.4-1.
    """
    evidence = build_evidence_text_from_chunks(new_chunks)
    use_llm = bool(getattr(config, "enable_contract_verify", False)) or force_llm_extract
    extracted, conf = extract_slots(
        subgoal,
        evidence,
        config,
        retrieval_query=retrieval_query,
        use_llm=use_llm,
    )
    # Rule verify always runs; LLM extract is optional.
    outcome = verify_contract(
        subgoal,
        extracted=extracted,
        evidence_text=evidence,
        confidence=conf,
    )
    result = outcome.result
    result.collected_section_ids = [
        s for s in state.collected_section_ids if s not in collected_before
    ] or list(result.collected_section_ids)
    return result


def _activate_conditionals(
    plan: RetrievalPlan,
    state: NavState,
    config: NavConfig,
    *,
    parent_id: str,
    parent_result: SubgoalResult,
) -> List[str]:
    activated_now: List[str] = []
    for sg in plan.subgoals:
        if is_always_active(sg):
            continue
        if sg.activation.on != parent_id:
            continue
        if sg.id in state.activated_subgoal_ids:
            continue
        if activation_when_holds(
            sg.activation.when,
            parent_extracted=parent_result.extracted,
            parent_satisfied=bool(parent_result.satisfied),
            config=config,
            use_llm=bool(getattr(config, "enable_contract_verify", False)),
        ):
            state.activated_subgoal_ids.add(sg.id)
            activated_now.append(sg.id)
    return activated_now


def _execute_subgoal_with_verdicts(
    ts: Any,
    state: NavState,
    config: NavConfig,
    subgoal: Subgoal,
    *,
    steps_out: Optional[List[Any]],
) -> Tuple[SubgoalResult, bool]:
    """Run navigate→verify with RETRY/WIDEN/REBIND. Returns (result, want_replan)."""
    max_attempts = max(1, int(getattr(config, "subgoal_max_attempts", 2) or 2))
    rq = bind_slots(subgoal.retrieval_query, state.slot_bindings)
    last: Optional[SubgoalResult] = None
    last_new_chunks: List[Tuple[Any, float]] = []
    want_replan = False
    # Cross-subgoal report leakage (audit §1.6): each subgoal starts with a
    # clean scratchpad; its own dispatch reports still accumulate across its
    # own retries below.
    state.reports_context = ""

    for attempt in range(max_attempts):
        before = set(state.collected_section_ids)

        if last is not None and last.verdict == "WIDEN":
            _widen_scope_filter(subgoal)

        if last is not None and last.verdict == "REBIND":
            # First: re-extract (LLM if verify enabled) from the SAME evidence
            # collected by the previous attempt. If still bad, degrade query.
            re_extract = _verify_subgoal(
                state,
                config,
                subgoal,
                retrieval_query=rq,
                new_chunks=last_new_chunks,
                collected_before=before,
                force_llm_extract=True,
            )
            if re_extract.satisfied or re_extract.verdict == "SATISFIED":
                return re_extract, False
            rq = _unbound_retrieval_query(subgoal)

        _set_focus(state, subgoal, rq)
        before_len = len(state.collected)
        child_steps: List[Any] = []
        _run_navigate_for_query(ts, state, config, query=rq, steps_out=child_steps)
        if steps_out is not None:
            steps_out.extend(child_steps)
        last_new_chunks = list(state.collected[before_len:])
        last = _verify_subgoal(
            state,
            config,
            subgoal,
            retrieval_query=rq,
            new_chunks=last_new_chunks,
            collected_before=before,
        )
        if last.satisfied or last.verdict == "SATISFIED":
            last.satisfied = True
            last.verdict = "SATISFIED"
            return last, False
        if last.verdict in {"RETRY_SAME_REGION", "WIDEN", "REBIND"}:
            continue
        if last.verdict == "REPLAN":
            want_replan = True
            break
        break

    assert last is not None
    # Attempts exhausted without satisfaction → optional structural replan.
    if (
        not last.satisfied
        and int(getattr(config, "max_replans", 0) or 0) > 0
        and last.verdict in {"RETRY_SAME_REGION", "WIDEN", "REBIND", "REPLAN"}
    ):
        last.verdict = "REPLAN"
        want_replan = True
    return last, want_replan


def _execute_subgoal_harvest_once(
    ts: Any,
    state: NavState,
    config: NavConfig,
    subgoal: Subgoal,
    *,
    steps_out: Optional[List[Any]],
) -> Dict[str, Any]:
    """One harvest() call for this subgoal this wave — no internal retry loop.

    Retry / widen / drop / replan authority belongs to ``plan_control`` across
    waves (see ``nav_control.plan_control``), not to this single call.
    """
    from nav_harvest import harvest, resolve_harvest_anchor

    rq = bind_slots(subgoal.retrieval_query, state.slot_bindings)
    if unbound_slots(rq):
        # F1: deps may be "settled" (satisfied or dropped) without ever
        # producing this subgoal's referenced slot — degrade to a query with
        # the unresolved {{...}} braces stripped rather than stalling.
        rq = _unbound_retrieval_query(subgoal)
    _set_focus(state, subgoal, rq)
    anchor = resolve_harvest_anchor(subgoal, state, config, ts=ts)
    before_sections = set(state.collected_section_ids)
    before_len = len(state.collected)
    harvest_result = harvest(
        ts,
        state,
        config,
        subgoal=subgoal,
        entry_scope=anchor,
        query=rq,
        steps_out=steps_out,
    )
    new_chunks = list(state.collected[before_len:])
    signal = _verify_subgoal(
        state,
        config,
        subgoal,
        retrieval_query=rq,
        new_chunks=new_chunks,
        collected_before=before_sections,
    )
    _clear_focus(state)
    return {
        "subgoal_id": subgoal.id,
        "result": signal,
        "new_chunks": new_chunks,
        "harvest": {
            "anchor": anchor,
            "n_policy_calls": harvest_result.n_policy_calls,
            "visited_section_ids": list(harvest_result.visited_section_ids),
            "max_depth_hit": harvest_result.max_depth_hit,
            "reason": harvest_result.reason,
        },
    }


def _apply_plan_control(
    ts: Any,
    state: NavState,
    config: NavConfig,
    *,
    plan: RetrievalPlan,
    outputs: Sequence[Dict[str, Any]],
    by_id: Dict[str, Subgoal],
    steps_out: Optional[List[Any]],
) -> Dict[str, Any]:
    """Apply one wave's plan_control decision; returns a TRACE-friendly detail.

    F2 fix: ``widen`` is the only "try again differently" decision (no more
    ``reharvest``) and is applied deterministically here, never by the LLM
    naming an anchor — it steps ``state.subgoal_anchor[sid]`` up to the
    parent of whatever it currently is (``nav_harvest.resolve_parent_section_id``).
    Once the anchor is already the document root (``None`` — maximum
    breadth), there is nowhere coarser to go, so widen degrades to a
    deterministic ``drop`` instead of silently repeating the same harvest.
    """
    from nav_control import plan_control
    from nav_harvest import resolve_parent_section_id

    decision = plan_control(ts, state, config, plan=plan, wave_outputs=outputs)
    max_attempts = max(1, int(getattr(config, "subgoal_max_attempts", 2) or 2))

    for item in outputs:
        sid = item["subgoal_id"]
        result: SubgoalResult = item["result"]
        sub_decision = decision.per_subgoal.get(sid)
        kind = sub_decision.decision if sub_decision else ("accept" if result.satisfied else "widen")
        # Circuit breaker: bound widen loops regardless of plan_control.
        if kind == "widen" and int(state.subgoal_attempt_counts.get(sid, 0)) >= max_attempts:
            kind = "drop"

        if kind == "widen":
            current = state.subgoal_anchor.get(sid)
            if current is None:
                # Already at the unrestricted document root: no coarser scope
                # exists to widen into.
                kind = "drop"
            else:
                state.subgoal_anchor[sid] = resolve_parent_section_id(ts, current, state.doc_id)

        if kind == "accept":
            result.satisfied = True
            result.verdict = "SATISFIED"
            state.subgoal_results[sid] = asdict(result)
            state.satisfied_subgoal_ids.add(sid)
            state.attempted_subgoal_ids.add(sid)
            _activate_conditionals(plan, state, config, parent_id=sid, parent_result=result)
        elif kind == "drop":
            state.dropped_subgoal_ids.add(sid)
            state.attempted_subgoal_ids.add(sid)
        # kind == "widen": anchor already advanced above; next wave's harvest
        # reads it back from state.subgoal_anchor via resolve_harvest_anchor.

    if steps_out is not None:
        from agent_delivery.agent.types import AgentStep  # type: ignore

        steps_out.append(
            AgentStep(
                step_idx=len(steps_out) + 1,
                action="plan_control",
                detail={
                    "global": decision.global_action,
                    "reason": decision.reason,
                    "subgoals": {
                        sid: {"decision": d.decision, "note": d.note}
                        for sid, d in decision.per_subgoal.items()
                    },
                },
            )
        )
    return {
        "global": decision.global_action,
        "replan": decision.global_action == "replan",
        "done": decision.global_action == "done",
        "reason": decision.reason,
    }


def _execute_subgoal_on_state(
    ts: Any,
    state: NavState,
    config: NavConfig,
    plan: RetrievalPlan,
    subgoal_id: str,
    *,
    steps_out: Optional[List[Any]],
) -> Dict[str, Any]:
    by = {s.id: s for s in plan.subgoals}
    result, want_replan = _execute_subgoal_with_verdicts(
        ts, state, config, by[subgoal_id], steps_out=steps_out
    )
    _clear_focus(state)
    return {"subgoal_id": subgoal_id, "result": result, "want_replan": want_replan}


def execute_plan(
    ts: Any,
    state: NavState,
    config: NavConfig,
    *,
    steps_out: Optional[List[Any]] = None,
    episode_query: str = "",
) -> Dict[str, Any]:
    """Run dependency waves until idle or ``max_waves``."""
    from nav_agent import AgentStep

    plan = state.retrieval_plan
    if plan is None or not getattr(plan, "subgoals", None):
        _run_navigate_for_query(
            ts, state, config, query=episode_query or state.query, steps_out=steps_out
        )
        return {"fallback_navigate": True}

    max_waves = int(getattr(config, "max_waves", 0) or 0)
    use_harvest = bool(getattr(config, "enable_one_shot_harvest", False))
    use_control = bool(getattr(config, "enable_plan_control", False))
    wave_idx = 0
    summary: Dict[str, Any] = {"waves": [], "results": {}}
    episode_done = False

    while True:
        if episode_done:
            break
        if max_waves > 0 and wave_idx >= max_waves:
            break
        ready = ready_subgoal_ids(
            plan,
            satisfied=set(state.satisfied_subgoal_ids),
            activated=set(state.activated_subgoal_ids),
            attempted=set(state.attempted_subgoal_ids),
            dropped=set(state.dropped_subgoal_ids),
        )
        if not ready:
            break
        wave_idx += 1
        wave_detail: Dict[str, Any] = {
            "wave": wave_idx,
            "ready": list(ready),
            "subgoal_results": [],
        }

        if bool(getattr(config, "enable_per_subgoal_illumination", False)):
            refresh_fold_from_subgoal_scores(state, config)

        by_id = {s.id: s for s in plan.subgoals}
        outputs: List[Dict[str, Any]] = []

        def _run_one(sid: str, working_state: NavState, out_steps: Optional[List[Any]]) -> Dict[str, Any]:
            if use_harvest:
                return _execute_subgoal_harvest_once(
                    ts, working_state, config, by_id[sid], steps_out=out_steps
                )
            return _execute_subgoal_on_state(
                ts, working_state, config, plan, sid, steps_out=out_steps
            )

        # Serial wave execution (parallel fan-out retired with ThreadPoolExecutor).
        for sid in ready:
            outputs.append(_run_one(sid, state, steps_out))

        # Bookkeeping shared by both decision paths.
        for item in outputs:
            sid = item["subgoal_id"]
            result: SubgoalResult = item["result"]
            state.subgoal_results[sid] = asdict(result)
            wave_detail["subgoal_results"].append(
                {"subgoal_id": sid, "verdict": result.verdict, "gap": result.gap}
            )
            summary["results"][sid] = asdict(result)
            if result.extracted:
                state.slot_bindings = apply_bindings_from_result(
                    state.slot_bindings, by_id[sid], result.extracted
                )
            state.subgoal_attempt_counts[sid] = int(
                state.subgoal_attempt_counts.get(sid, 0)
            ) + 1

        replan_requested = False
        if use_control:
            control_detail = _apply_plan_control(
                ts, state, config, plan=plan, outputs=outputs, by_id=by_id, steps_out=steps_out
            )
            wave_detail["plan_control"] = control_detail
            replan_requested = bool(control_detail.get("replan"))
            if control_detail.get("done"):
                episode_done = True
        else:
            for item in outputs:
                sid = item["subgoal_id"]
                result = item["result"]
                if item.get("want_replan") or result.verdict == "REPLAN":
                    replan_requested = True
                # Close the node after attempts (success or exhausted).
                state.attempted_subgoal_ids.add(sid)
                if result.satisfied or result.verdict == "SATISFIED":
                    state.satisfied_subgoal_ids.add(sid)
                    _activate_conditionals(
                        plan, state, config, parent_id=sid, parent_result=result
                    )

        if bool(getattr(config, "enable_per_subgoal_illumination", False)):
            illuminate_from_plan(ts, state, config)
            refresh_fold_from_subgoal_scores(state, config)

        if steps_out is not None:
            steps_out.append(
                AgentStep(
                    step_idx=len(steps_out) + 1,
                    action="plan_wave",
                    detail=wave_detail,
                )
            )
        summary["waves"].append(wave_detail)

        if replan_requested:
            cap = int(getattr(config, "max_replans", 0) or 0)
            if cap > 0 and int(state.replan_count) < cap:
                state.replan_count += 1
                t0 = time.perf_counter()
                new_plan = plan_query(ts, state, config)
                state.retrieval_plan = new_plan
                plan = new_plan
                # A regenerated plan gets fresh subgoal ids (s1, s2, ... again),
                # so per-id bookkeeping (satisfied/attempted/activated, qualified
                # "sX.slot" bindings) cannot be safely carried over — those ids
                # now mean something else. What IS safe and worth keeping (audit
                # §2.4: "don't discard what's already accepted") is unqualified
                # slot bindings (plain fact values) and every chunk already in
                # state.collected — neither is reset here or anywhere else.
                state.satisfied_subgoal_ids = set()
                state.attempted_subgoal_ids = set()
                state.activated_subgoal_ids = set()
                state.subgoal_results = {}
                state.slot_bindings = {
                    k: v for k, v in state.slot_bindings.items() if "." not in k
                }
                if bool(getattr(config, "enable_per_subgoal_illumination", False)):
                    illuminate_from_plan(ts, state, config)
                if steps_out is not None:
                    steps_out.append(
                        AgentStep(
                            step_idx=len(steps_out) + 1,
                            action="replan",
                            detail={
                                "replan_count": state.replan_count,
                                "n_subgoals": len(new_plan.subgoals),
                                "fallback": bool(new_plan.fallback),
                                "seconds": time.perf_counter() - t0,
                            },
                        )
                    )
                continue
            # Cap reached: stop requesting further replans.
            replan_requested = False

    _clear_focus(state)
    summary["n_waves"] = wave_idx
    summary["satisfied"] = sorted(state.satisfied_subgoal_ids)
    summary["attempted"] = sorted(state.attempted_subgoal_ids)
    summary["activated"] = sorted(state.activated_subgoal_ids)
    return summary
