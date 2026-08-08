from __future__ import annotations

import time
import os
import re
from typing import Any, Dict, List, Optional, Sequence, Tuple

from agent_delivery.agent.types import AgentStep, EpisodeResult
from agent_delivery.code.compose_llm import compose_answer_llm
from agent_delivery.code.hierarchical_tools import HierarchicalTools
from agent_delivery.code.index_retrieval import Chunk
from agent_delivery.code.tool_space import (
    CORPUS_DOC_ID,
    Refusal,
    ToolSpace,
    is_corpus_doc_id,
    is_synthetic_dispatch_only,
)
from path_ledger import doc_id_for

from nav_compose import (
    evidence_owner_section_id,
    pack_nav_evidence,
    settle_subgoal_evidence,
    unit_score_for_evidence_chunk,
)
from nav_map_scores import (
    compute_corpus_map_and_unit_scores,
    compute_map_and_unit_scores,
    select_map_highlights,
)
from nav_navigate import navigate
from nav_types import (
    LegalAction,
    NavConfig,
    NavState,
    map_mode_enabled,
)

# Back-compat aliases for tests / callers.
_evidence_owner_section_id = evidence_owner_section_id
_unit_score_for_evidence_chunk = unit_score_for_evidence_chunk


def _chunks_to_retrieved_nodes(chunks: List[Chunk]) -> List[str]:
    seen: set[str] = set()
    out: List[str] = []
    for c in chunks:
        for lid in c.line_ids:
            node = f"{c.doc_id}:L{lid}"
            if node not in seen:
                seen.add(node)
                out.append(node)
    return out


def _dedupe_scored(scored: List[Tuple[Chunk, float]]) -> List[Tuple[Chunk, float]]:
    from nav_compose import dedupe_scored

    return dedupe_scored(scored)


def _add_scored(state: NavState, scored: List[Tuple[Chunk, float]]) -> int:
    added = 0
    for c, score in scored:
        if c.node_id in state.collected_ids:
            continue
        state.collected_ids.add(c.node_id)
        state.collected.append((c, float(score)))
        added += 1
    return added


def _resolve_action_doc_id(action_or_sid: Any, state: NavState) -> str:
    """Prefer section_id prefix; fall back to episode doc_id (never corpus for hydrate)."""
    if hasattr(action_or_sid, "section_id"):
        sid = str(getattr(action_or_sid, "section_id", "") or "").strip()
    else:
        sid = str(action_or_sid or "").strip()
    resolved = doc_id_for(sid)
    if resolved and not is_corpus_doc_id(resolved):
        return resolved
    if state.doc_id and not is_corpus_doc_id(state.doc_id):
        return state.doc_id
    return str(resolved or state.doc_id or "")


def _purge_descendant_evidence(
    ts: ToolSpace,
    state: NavState,
    parent_sid: str,
) -> int:
    """Drop standalone evidence owned by proper descendants of parent_sid.

    When COLLECT parent after COLLECT child (e.g. L93 then L92), child chunks
    are absorbed into the parent hydrate and must not keep a separate bag slot.
    """
    sid = str(parent_sid or "").strip()
    if not sid:
        return 0
    doc = _resolve_action_doc_id(sid, state)
    relations = getattr(ts, "section_relation_ids", None)
    if callable(relations):
        _anc, descendants = relations(sid, doc)
    else:
        descendants = _section_and_descendants(ts, sid, doc)
    descendants = {str(x).strip() for x in (descendants or set()) if str(x).strip()}
    descendants.discard(sid)
    if not descendants:
        return 0

    kept: List[Tuple[Chunk, float]] = []
    removed = 0
    for chunk, score in list(state.collected):
        owner = _evidence_owner_section_id(chunk)
        if owner in descendants:
            state.collected_ids.discard(chunk.node_id)
            removed += 1
            continue
        kept.append((chunk, score))
    state.collected = kept
    return removed


def _env_enabled(name: str, default: str = "1") -> bool:
    return os.environ.get(name, default).strip().lower() not in {"0", "false", "no", "off"}


def _line_order(pool: List[Chunk]) -> List[Chunk]:
    return sorted(pool, key=lambda c: (min(c.line_ids or (10**9,)), c.node_id))


def _collect_by_unit_score(
    pool: List[Chunk],
    state: NavState,
    config: NavConfig,
) -> List[Tuple[Chunk, float]]:
    """Directed hydrate: order/truncate by unit score (single_fact / span)."""
    if not pool:
        return []
    bonus = float(config.read_score_bonus)
    scored = [
        (chunk, float(unit_score_for_evidence_chunk(chunk, state.unit_scores)) + bonus)
        for chunk in pool
    ]
    scored.sort(
        key=lambda item: (
            -float(item[1]),
            min(getattr(item[0], "line_ids", None) or (10**9,)),
            str(getattr(item[0], "node_id", "") or ""),
        )
    )
    k = max(1, int(config.collect_k or 1))
    return scored[:k]


def _collect_subtree(ts: ToolSpace, action: LegalAction, state: NavState, config: NavConfig) -> List[Tuple[Chunk, float]]:
    sid = action.section_id
    if not sid:
        return []
    if is_synthetic_dispatch_only(sid):
        return []
    doc = _resolve_action_doc_id(action, state)
    if not doc or is_corpus_doc_id(doc):
        return []
    materialize = getattr(ts, "_materialize_leaf_path_chunks", None)
    if callable(materialize):
        pool = list(materialize(sid, doc))
        if pool:
            # Contract-driven hydrate when a soft-focus subgoal is active (M5/A3).
            kind = str(getattr(state, "focus_contract_kind", "") or "").strip().lower()
            if map_mode_enabled(config) or bool(getattr(state, "unit_scores", None)):
                if kind in {"single_fact", "span", "comparison", "existence"}:
                    return _collect_by_unit_score(pool, state, config)
                return _collect_in_doc_order(pool, config)
            idx = getattr(ts, "_idx", None)
            if idx is None:
                return _collect_in_doc_order(pool, config)
            scored = idx.search(
                state.query,
                pool,
                min(len(pool), int(config.collect_k)),
                doc_id_filter=doc,
            )
            return [(c, float(s) + float(config.read_score_bonus)) for c, s in scored]
    rc = ts.read_chunks(sid, state.query, doc_id=doc, k=int(config.collect_k))
    if isinstance(rc, Refusal):
        state.refusal_events.append(
            {
                "tool": "collect",
                "section_id": sid,
                "status": rc.status,
                "message": rc.message,
                "available_sections": list(rc.available_sections),
            }
        )
        return []
    return [(h.chunk, float(h.score) + float(config.read_score_bonus)) for h in rc]


def _mark_collected_branch(
    ts: ToolSpace, action: LegalAction, state: NavState, added: int
) -> dict[str, Any]:
    """On successful COLLECT: mark sid ∪ descendants as collected (removed from map).

    Replaces the old covered/collected split — one set only.
    """
    sid = str(action.section_id or "").strip()
    if not sid or not _env_enabled("NAV_FILTER_COLLECTED_SECTIONS"):
        return {}
    doc = _resolve_action_doc_id(action, state)
    materialize = getattr(ts, "_materialize_leaf_path_chunks", None)
    relations = getattr(ts, "section_relation_ids", None)
    pool = list(materialize(sid, doc)) if callable(materialize) and doc else []
    if callable(relations) and doc:
        ancestors, descendants = relations(sid, doc)
    else:
        ancestors, descendants = set(), _section_and_descendants(ts, sid, doc)
    descendants = {str(x).strip() for x in (descendants or set()) if str(x).strip()}
    descendants.add(sid)

    is_full = bool(pool) and all(chunk.node_id in state.collected_ids for chunk in pool)
    if added > 0:
        state.collected_section_ids.update(descendants)
        if len(pool) > 1:
            state.blocked_collect_section_ids.update(ancestors)
    return {
        "collect_full": is_full,
        "branch_selected": added > 0,
        "n_collected_sections": len(state.collected_section_ids),
        "n_blocked_ancestor_collects": len(state.blocked_collect_section_ids),
    }


# Back-compat name used by older tests; prefer _mark_collected_branch.
_update_collect_coverage = _mark_collected_branch


def _collect_in_doc_order(
    pool: List[Chunk],
    config: NavConfig,
) -> List[Tuple[Chunk, float]]:
    """Hydrate the complete branch in document order; COMPOSE truncates later."""
    if not pool:
        return []
    base = float(config.read_score_bonus)
    return [(chunk, base) for chunk in _line_order(pool)]


def _direct_child_ids(ts: ToolSpace, section_id: str, doc_id: str) -> List[str]:
    sid = (section_id or "").strip()
    if not sid:
        return []
    children_fn = getattr(ts, "_children_for_section_path", None)
    rows: List[Any] = []
    if callable(children_fn):
        try:
            rows = list(children_fn(sid, doc_id, limit=100000) or [])
        except Exception:
            rows = []
    if not rows:
        try:
            st = ts.get_structure(sid)
            rows = list(st.get("children") or [])
        except Exception:
            return []
    out: List[str] = []
    seen: set[str] = set()
    for row in rows:
        if not isinstance(row, dict):
            continue
        child_id = str(row.get("section_id") or "").strip()
        if child_id and child_id not in seen:
            seen.add(child_id)
            out.append(child_id)
    return out


def _section_and_descendants(ts: ToolSpace, section_id: str, doc_id: str) -> set[str]:
    """Return {section_id} ∪ descendants (best-effort)."""
    sid = (section_id or "").strip()
    if not sid:
        return set()
    relations = getattr(ts, "section_relation_ids", None)
    if callable(relations):
        try:
            _anc, desc = relations(sid, doc_id)
            out = {str(x).strip() for x in (desc or set()) if str(x).strip()}
            out.add(sid)
            return out
        except Exception:
            pass
    out: set[str] = {sid}
    stack = [sid]
    while stack:
        cur = stack.pop()
        for child in _direct_child_ids(ts, cur, doc_id):
            if child not in out:
                out.add(child)
                stack.append(child)
    return out


def run_nav_episode(
    tools: HierarchicalTools,
    query: str,
    *,
    doc_id: Optional[str] = None,
    corpus_doc_ids: Optional[Sequence[str]] = None,
    budget_chars: int,
    task_type: str = "unknown",
    compose_format_constraints: str = "",
    compose_answer: bool = True,
    policy: str = "rule",
    config: Optional[NavConfig] = None,
) -> EpisodeResult:
    corpus_ids = [
        str(d).strip()
        for d in (corpus_doc_ids or [])
        if str(d).strip() and not is_corpus_doc_id(str(d).strip())
    ]
    episode_doc = str(doc_id or "").strip()
    if corpus_ids:
        episode_doc = CORPUS_DOC_ID
    elif not episode_doc:
        raise ValueError(
            "Nav Agent requires doc_id or non-empty corpus_doc_ids "
            "(eval entry points always pass corpus_doc_ids for task_corpus)"
        )
    from agent_delivery.code.llm_config import load_llm_env, require_llm_env  # type: ignore

    load_llm_env()
    require_llm_env(context="Nav Agent")
    cfg = config or NavConfig(policy="llm")
    if map_mode_enabled(None):
        cfg.map_mode = True
        if cfg.llm_max_tokens < 256:
            cfg.llm_max_tokens = 256
    nav_policy = (policy or cfg.policy or "llm").strip().lower()
    if nav_policy != "llm":
        raise ValueError(
            f"Nav Agent 仅支持 llm 策略（须配置 OPENAI_API_KEY）；收到 policy={policy!r}。"
            "请设置 --nav-policy llm 或删除 NAV_POLICY=rule。"
        )
    cfg.policy = "llm"
    # Tie the large-scope title-only threshold to the real evidence budget
    # (budget_chars x mult): a scope whose full summary map would dwarf the final
    # evidence budget is shown title-only, nudging DISPATCH over broad COLLECT.
    mult = float(getattr(cfg, "scope_inline_summary_budget_mult", 0.0) or 0.0)
    if mult > 0.0 and int(budget_chars) > 0:
        cfg.scope_inline_summary_char_limit = max(1, int(budget_chars * mult))
    # Depth-0 oversize→DISPATCH threshold defaults to the evidence budget.
    if bool(getattr(cfg, "enable_depth0_oversize_to_dispatch", False)):
        if int(getattr(cfg, "depth0_oversize_char_limit", 0) or 0) <= 0:
            cfg.depth0_oversize_char_limit = max(1, int(budget_chars))
    retrieval_t0 = time.perf_counter()
    ts = ToolSpace(tools, corpus_doc_ids=corpus_ids or None)
    state = NavState(doc_id=episode_doc, query=query, task_type=task_type)
    steps: List[AgentStep] = []
    if is_corpus_doc_id(episode_doc):
        section_ids = ts.sections_for_doc(CORPUS_DOC_ID)
        state.map_scores, state.unit_scores = compute_corpus_map_and_unit_scores(
            ts, doc_ids=ts.corpus_doc_ids, query=query
        )
    else:
        section_ids = ts.sections_for_doc(episode_doc)
        state.map_scores, state.unit_scores = compute_map_and_unit_scores(
            ts, doc_id=episode_doc, query=query, root_ids=section_ids
        )
    state.highlight_ids = select_map_highlights(
        state.unit_scores, k=int(cfg.collect_top_k)
    )

    if bool(getattr(cfg, "enable_query_planning", False)):
        from nav_plan import plan_query

        plan_t0 = time.perf_counter()
        retrieval_plan = plan_query(ts, state, cfg)
        state.retrieval_plan = retrieval_plan
        steps.append(
            AgentStep(
                step_idx=len(steps) + 1,
                action="query_plan",
                detail={
                    "fallback": bool(retrieval_plan.fallback),
                    "n_subgoals": len(retrieval_plan.subgoals),
                    "reason": retrieval_plan.reason,
                    "plan": retrieval_plan.to_dict(),
                    "planning_map_char_limit": int(
                        getattr(cfg, "planning_map_char_limit", 0) or cfg.map_char_limit
                    ),
                    "seconds": time.perf_counter() - plan_t0,
                },
            )
        )

    if bool(getattr(cfg, "enable_per_subgoal_illumination", False)):
        from nav_illuminate import illuminate_from_plan

        illum_t0 = time.perf_counter()
        illum_detail = illuminate_from_plan(ts, state, cfg)
        if illum_detail is not None:
            illum_detail = dict(illum_detail)
            illum_detail["seconds"] = time.perf_counter() - illum_t0
            steps.append(
                AgentStep(
                    step_idx=len(steps) + 1,
                    action="illuminate",
                    detail=illum_detail,
                )
            )

    # Top-level: plan orchestration (M4/M5) or classic single navigate.
    if bool(getattr(cfg, "enable_plan_orchestration", False)) and state.retrieval_plan is not None:
        from nav_orchestrate import execute_plan

        orch_t0 = time.perf_counter()
        orch_detail = execute_plan(
            ts, state, cfg, steps_out=steps, episode_query=query
        )
        orch_detail = dict(orch_detail or {})
        orch_detail["seconds"] = time.perf_counter() - orch_t0
        steps.append(
            AgentStep(
                step_idx=len(steps) + 1,
                action="plan_orchestrate",
                detail=orch_detail,
            )
        )
    else:
        navigate(
            ts,
            state=state,
            scope=None,
            query=query,
            config=cfg,
            depth=0,
            budget=int(cfg.map_char_limit),
            steps_out=steps,
        )

    fill = None
    ledger_detail = None
    if (
        bool(getattr(cfg, "enable_subgoal_budget_ledger", False))
        and state.retrieval_plan is not None
        and bool(getattr(cfg, "enable_plan_orchestration", False))
    ):
        fill, ledger = settle_subgoal_evidence(
            _dedupe_scored(list(state.collected)),
            ts,
            state,
            cfg,
            budget_chars=budget_chars,
        )
        if ledger is not None:
            ledger_detail = ledger.to_dict()
            steps.append(
                AgentStep(
                    step_idx=len(steps) + 1,
                    action="budget_ledger",
                    detail=ledger_detail,
                )
            )
    if fill is None:
        fill = pack_nav_evidence(
            _dedupe_scored(list(state.collected)),
            ts,
            state,
            cfg,
            budget_chars=budget_chars,
        )
    scored_chunks = list(fill.scored_chunks)
    retrieval_seconds = time.perf_counter() - retrieval_t0
    composed = ""
    compose_seconds = 0.0
    if compose_answer:
        compose_t0 = time.perf_counter()
        max_ans = min(1024, max(256, int(budget_chars)))
        extra_mh_constraint = ""
        if (task_type or "").strip().lower() == "multi_hop":
            extra_mh_constraint = (
                "multi_hop 约束：fact_1 与 fact_2 必须分别覆盖两跳信息，"
                "final_answer 必须整合二者，任一缺失视为不完整。"
            )
        fc = compose_format_constraints
        if extra_mh_constraint:
            fc = (f"{fc}\n{extra_mh_constraint}" if fc else extra_mh_constraint)
        composed = compose_answer_llm(
            query,
            task_type=task_type or "niche_fact",
            evidence_text=fill.evidence_text or "",
            max_answer_chars=max_ans,
            budget_chars=int(budget_chars),
            format_constraints=fc,
        )
        compose_seconds = time.perf_counter() - compose_t0
        steps.append(
            AgentStep(
                step_idx=len(steps) + 1,
                action="compose_answer",
                detail={
                    "evidence_chars": fill.evidence_chars_actual,
                    "n_chunks_kept": fill.n_chunks_kept,
                    "truncated_last": fill.truncated_last,
                },
            )
        )

    return EpisodeResult(
        representation=f"hierarchical_nav_{cfg.policy}",
        steps=steps,
        scored_chunks=scored_chunks,
        kept_chunks=fill.kept_chunks,
        evidence_text=fill.evidence_text,
        evidence_chars_actual=fill.evidence_chars_actual,
        retrieved_nodes=_chunks_to_retrieved_nodes(list(fill.kept_chunks)),
        composed_answer=composed,
        section_ids=list(section_ids),
        trajectory_length=len(steps),
        truncated_last=fill.truncated_last,
        refusal_events=list(state.refusal_events),
        phase_timings={
            "retrieval_framework_seconds": retrieval_seconds,
            "compose_seconds": compose_seconds,
            "online_response_seconds": retrieval_seconds + compose_seconds,
        },
    )
