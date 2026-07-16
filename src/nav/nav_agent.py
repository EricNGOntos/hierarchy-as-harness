from __future__ import annotations

import time
import os
import re
from typing import Any, Dict, List, Optional, Tuple

from agent_delivery.agent.types import AgentStep, EpisodeResult
from agent_delivery.code.compose_llm import compose_answer_llm
from agent_delivery.code.hierarchical_tools import HierarchicalTools
from agent_delivery.code.index_retrieval import Chunk
from agent_delivery.code.tool_space import Refusal, ToolSpace

from nav_compose import (
    evidence_owner_section_id,
    pack_nav_evidence,
    unit_score_for_evidence_chunk,
)
from nav_map_scores import compute_map_and_unit_scores, select_map_highlights
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
    relations = getattr(ts, "section_relation_ids", None)
    if callable(relations):
        _anc, descendants = relations(sid, state.doc_id)
    else:
        descendants = _section_and_descendants(ts, sid, state.doc_id)
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


def _scope_collect_strategy() -> str:
    explicit = os.environ.get("NAV_SCOPE_COLLECT_STRATEGY", "").strip().lower()
    if explicit in {"line_order", "local_band", "multi_band", "relevance"}:
        return explicit
    return "local_band" if _env_enabled("NAV_SCOPE_COLLECT_RELEVANCE_FIRST") else "line_order"


def _has_explicit_scope_collect_strategy() -> bool:
    return os.environ.get("NAV_SCOPE_COLLECT_STRATEGY", "").strip().lower() in {
        "line_order",
        "local_band",
        "multi_band",
        "relevance",
    }


def _is_scope_outline_query(query: str, task_type: str) -> bool:
    """Legacy keyword OUTLINE detector (retired from active COLLECT path).

    Kept for ablation/tests only. Retrieval no longer branches on task_type or
    these keywords; compose still reads task_type from task data.
    TODO(knowhere-align): replace with query_intent labels if OUTLINE returns.
    """
    if (task_type or "").strip().lower() not in ("scope_collection", "regulatory_coverage"):
        return False
    q = (query or "").strip()
    if re.search(r"主要(条目|内容|项目|章节|部分|要点|事项)", q):
        return True
    if re.search(r"(列举|列出|概述|概括|归纳).{0,20}(部分|章节|条目|内容|要点)", q):
        if not re.search(r"(具体|详细|全部|所有).{0,4}(步骤|内容|要素|条款)", q):
            return True
    if re.search(r"(哪些|包含什么|有什么).{0,10}(部分|章节|条目|内容)", q):
        return True
    return False


def _scope_collect_outline(
    idx: Any,
    pool: List[Chunk],
    action: LegalAction,
    state: NavState,
    config: NavConfig,
) -> List[Tuple[Chunk, float]]:
    """Legacy outline hydrate (ablation only; not called from _collect_subtree).

    Outline mode：对目标 section 的每个直接子节取首 N 行窗口。
    广度优先覆盖所有 child，而非只深入少数。
    """
    action_score_cap = max(0.0, float(os.environ.get("NAV_SCOPE_ACTION_SCORE_CAP", "1.0") or "1.0"))
    action_score = max(0.0, min(float(action.score or 0.0), action_score_cap))
    base = float(config.read_score_bonus) + action_score
    lines_per_child = max(1, int(os.environ.get("NAV_SCOPE_OUTLINE_LINES_PER_CHILD", "3") or "3"))

    bundle = idx._bundles.get(state.doc_id)
    if not bundle:
        return _scope_collect_scored(idx, pool, action, state, config)

    lines = bundle.lines
    levels = bundle.levels_for_tree
    if len(levels) < len(lines):
        return _scope_collect_scored(idx, pool, action, state, config)

    target_sid = action.section_id
    if not target_sid:
        return _scope_collect_scored(idx, pool, action, state, config)

    m = re.search(r":L(\d+)$", target_sid)
    if not m:
        return _scope_collect_scored(idx, pool, action, state, config)
    target_line_id = int(m.group(1))

    sec_start = None
    for j, rec in enumerate(lines):
        if rec.line_id == target_line_id:
            sec_start = j
            break
    if sec_start is None:
        return _scope_collect_scored(idx, pool, action, state, config)

    anchor_level = levels[sec_start]
    sec_end = len(lines)
    for j in range(sec_start + 1, len(lines)):
        if levels[j] <= anchor_level:
            sec_end = j
            break

    child_levels = set(
        levels[j] for j in range(sec_start + 1, sec_end)
        if levels[j] > anchor_level
    )
    if not child_levels:
        return _scope_collect_scored(idx, pool, action, state, config)
    child_level = min(child_levels)

    child_starts: List[int] = []
    for j in range(sec_start + 1, sec_end):
        if levels[j] == child_level:
            child_starts.append(j)

    if len(child_starts) < 2:
        return _scope_collect_scored(idx, pool, action, state, config)

    outline_chunks: List[Tuple[Chunk, float]] = []
    seen_ids: set = set()

    sec_first = Chunk(
        node_id=f"{state.doc_id}:L{lines[sec_start].line_id}__outline",
        doc_id=state.doc_id,
        text=(lines[sec_start].content or "").strip(),
        line_ids=(lines[sec_start].line_id,),
        section_id=target_sid,
    )
    if sec_first.text:
        outline_chunks.append((sec_first, base + 1.0))
        seen_ids.add(sec_first.node_id)

    for ci, child_j in enumerate(child_starts):
        child_end = child_starts[ci + 1] if ci + 1 < len(child_starts) else sec_end
        window_end = min(child_j + lines_per_child, child_end)
        window = [rec for rec in lines[child_j:window_end] if (rec.content or "").strip()]
        if not window:
            continue
        line_ids = tuple(rec.line_id for rec in window)
        chunk = Chunk(
            node_id=f"{state.doc_id}:L{lines[child_j].line_id}__outline",
            doc_id=state.doc_id,
            text="\n".join((rec.content or "").strip() for rec in window),
            line_ids=line_ids,
            section_id=target_sid,
        )
        if chunk.node_id in seen_ids:
            continue
        score = base + 0.9 - ci * 0.01
        outline_chunks.append((chunk, score))
        seen_ids.add(chunk.node_id)

    min_outline = max(1, int(os.environ.get("NAV_SCOPE_OUTLINE_MIN_CHUNKS", "3") or "3"))
    if len(outline_chunks) < min_outline:
        if map_mode_enabled(None) or bool(getattr(state, "unit_scores", None)):
            return _collect_in_doc_order(pool, config)
        return _scope_collect_scored(idx, pool, action, state, config)

    limit = min(len(outline_chunks), int(config.collect_k))
    return outline_chunks[:limit]


def _scope_collect_scored(
    idx: Any,
    pool: List[Chunk],
    action: LegalAction,
    state: NavState,
    config: NavConfig,
) -> List[Tuple[Chunk, float]]:
    ordered = _line_order(pool)
    strategy = _scope_collect_strategy()
    if (
        not _is_scope_outline_query(state.query, state.task_type or "")
        and _env_enabled("NAV_SCOPE_DETAIL_FORCE_LINE_ORDER", "1")
        and not _has_explicit_scope_collect_strategy()
    ):
        strategy = "line_order"
    min_pool = max(1, int(os.environ.get("NAV_SCOPE_LOCAL_BAND_MIN_POOL", "20") or "20"))
    action_score_cap = max(
        0.0, float(os.environ.get("NAV_SCOPE_ACTION_SCORE_CAP", "1.0") or "1.0")
    )
    action_score = max(0.0, min(float(action.score or 0.0), action_score_cap))
    base = float(config.read_score_bonus) + action_score
    if state.scope_evidence_locked:
        base -= max(
            0.0,
            float(os.environ.get("NAV_SCOPE_POST_LOCK_SCORE_PENALTY", "2.0") or "2.0"),
        )

    if strategy == "line_order" or (strategy == "local_band" and len(ordered) < min_pool):
        limit = min(len(ordered), int(config.collect_k))
        return [
            (chunk, base + (limit - rank) * 0.001)
            for rank, chunk in enumerate(ordered[:limit])
        ]

    ranked = idx.search(state.query, pool, len(pool), doc_id_filter=state.doc_id)
    relevance_by_id = {c.node_id: float(score) for c, score in ranked}
    if strategy == "relevance":
        relevance_order = sorted(
            ordered,
            key=lambda c: (-relevance_by_id.get(c.node_id, float("-inf")), min(c.line_ids or (10**9,)), c.node_id),
        )
        return [
            (chunk, base + relevance_by_id.get(chunk.node_id, 0.0))
            for chunk in relevance_order[: min(len(relevance_order), int(config.collect_k))]
        ]

    band_k = max(1, int(os.environ.get("NAV_SCOPE_LOCAL_BAND_K", "8") or "8"))
    band_k = min(band_k, int(config.collect_k), len(ordered))
    context_before = min(
        max(0, int(os.environ.get("NAV_SCOPE_LOCAL_BAND_CONTEXT_BEFORE", "1") or "1")),
        max(0, band_k - 1),
    )
    if strategy == "multi_band":
        anchors_n = max(1, int(os.environ.get("NAV_SCOPE_MULTI_BAND_ANCHORS", "3") or "3"))
        context_after = max(
            0, int(os.environ.get("NAV_SCOPE_MULTI_BAND_CONTEXT_AFTER", "1") or "1")
        )
        selected: List[Chunk] = []
        selected_ids: set[str] = set()
        candidate_anchors = [chunk for chunk, _ in ranked]
        if not candidate_anchors:
            candidate_anchors = ordered
        seeded = 0
        for cand in candidate_anchors:
            if len(selected) >= band_k:
                break
            if seeded >= anchors_n:
                break
            cand_idx = next((i for i, chunk in enumerate(ordered) if chunk.node_id == cand.node_id), None)
            if cand_idx is None:
                continue
            before = min(context_before, max(0, band_k - len(selected) - 1))
            win_start = max(0, cand_idx - context_before)
            win_end = min(len(ordered), cand_idx + context_after + 1)
            if before != context_before:
                win_start = max(0, cand_idx - before)
            before_count = len(selected)
            for chunk in ordered[win_start:win_end]:
                if chunk.node_id in selected_ids:
                    continue
                selected.append(chunk)
                selected_ids.add(chunk.node_id)
                if len(selected) >= band_k:
                    break
            if len(selected) > before_count:
                seeded += 1
        if len(selected) < band_k:
            for chunk in ordered:
                if chunk.node_id in selected_ids:
                    continue
                selected.append(chunk)
                selected_ids.add(chunk.node_id)
                if len(selected) >= band_k:
                    break
        selected.sort(
            key=lambda c: (
                -relevance_by_id.get(c.node_id, float("-inf")),
                min(c.line_ids or (10**9,)),
                c.node_id,
            )
        )
        return [
            (
                chunk,
                base
                + relevance_by_id.get(chunk.node_id, 0.0)
                + (band_k - rank) * 0.001,
            )
            for rank, chunk in enumerate(selected)
        ]
    anchor = ranked[0][0] if ranked else ordered[0]
    anchor_idx = next((i for i, chunk in enumerate(ordered) if chunk.node_id == anchor.node_id), 0)
    start = max(0, min(anchor_idx - context_before, len(ordered) - band_k))
    band = ordered[start : start + band_k]
    anchor_score = relevance_by_id.get(anchor.node_id, 0.0)
    return [
        (chunk, base + anchor_score + (band_k - rank) * 0.001)
        for rank, chunk in enumerate(band)
    ]


def _collect_subtree(ts: ToolSpace, action: LegalAction, state: NavState, config: NavConfig) -> List[Tuple[Chunk, float]]:
    sid = action.section_id
    if not sid:
        return []
    materialize = getattr(ts, "_materialize_leaf_path_chunks", None)
    idx = getattr(ts, "_idx", None)
    if callable(materialize) and idx is not None:
        pool = list(materialize(sid, state.doc_id))
        if pool:
            # Retrieval/evidence assembly is task-type agnostic: always hydrate the
            # full branch in document order. Keyword OUTLINE and scope-only collect
            # paths are retired (task_type remains for compose answer format only).
            if map_mode_enabled(config) or bool(getattr(state, "unit_scores", None)):
                return _collect_in_doc_order(pool, config)
            scored = idx.search(
                state.query,
                pool,
                min(len(pool), int(config.collect_k)),
                doc_id_filter=state.doc_id,
            )
            return [(c, float(s) + float(config.read_score_bonus)) for c, s in scored]
    rc = ts.read_chunks(sid, state.query, doc_id=state.doc_id, k=int(config.collect_k))
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
    materialize = getattr(ts, "_materialize_leaf_path_chunks", None)
    relations = getattr(ts, "section_relation_ids", None)
    pool = list(materialize(sid, state.doc_id)) if callable(materialize) else []
    if callable(relations):
        ancestors, descendants = relations(sid, state.doc_id)
    else:
        ancestors, descendants = set(), _section_and_descendants(ts, sid, state.doc_id)
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
        "scope_evidence_locked": state.scope_evidence_locked,
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
    doc_id: str,
    budget_chars: int,
    task_type: str = "unknown",
    compose_format_constraints: str = "",
    compose_answer: bool = True,
    policy: str = "rule",
    config: Optional[NavConfig] = None,
) -> EpisodeResult:
    if not doc_id:
        raise ValueError("Nav Agent requires a non-empty doc_id")
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
    retrieval_t0 = time.perf_counter()
    ts = ToolSpace(tools)
    state = NavState(doc_id=doc_id, query=query, task_type=task_type)
    steps: List[AgentStep] = []
    section_ids = ts.sections_for_doc(doc_id)
    state.map_scores, state.unit_scores = compute_map_and_unit_scores(
        ts, doc_id=doc_id, query=query, root_ids=section_ids
    )
    state.highlight_ids = select_map_highlights(
        state.unit_scores, k=int(cfg.collect_top_k)
    )

    # Top-level recursive-dispatch navigate (depth 0).
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
