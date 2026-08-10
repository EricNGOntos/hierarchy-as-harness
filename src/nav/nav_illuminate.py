"""M3: per-subgoal map illumination + goal-conditioned fold scores.

Pass 0 remains the episode-start raw-query scoring in ``run_nav_episode``.
Pass 1 (this module) re-scores with each bindable subgoal ``retrieval_query``
and merges via ``max_s(w_s · score_s)``. Satisfaction decay hooks
``satisfied_subgoal_ids`` for M5; until then all fold weights stay positive.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

from nav_map_scores import (
    compute_multi_query_map_scores,
    merge_score_maps,
    select_map_highlights_multi,
)
from nav_plan import RetrievalPlan, bind_slots, is_always_active, unbound_slots
from nav_types import NavConfig, NavState

try:
    from agent_delivery.code.tool_space import (  # type: ignore
        is_corpus_doc_id,
    )
except Exception:  # pragma: no cover
    def is_corpus_doc_id(doc_id: str) -> bool:  # type: ignore
        return str(doc_id or "").startswith("__corpus__")


def bindable_retrieval_queries(
    plan: RetrievalPlan,
    bindings: Dict[str, str],
) -> Dict[str, str]:
    """Subgoal id → retrieval_query after slot fill; skip still-unbound queries."""
    out: Dict[str, str] = {}
    for sg in plan.subgoals or []:
        rq = bind_slots(sg.retrieval_query, bindings)
        if unbound_slots(rq):
            continue
        text = (rq or "").strip()
        if text:
            out[sg.id] = text
    return out


def fold_participant_ids(
    plan: RetrievalPlan,
    *,
    bindable: Dict[str, str],
    satisfied: Set[str],
    activated: Optional[Set[str]] = None,
) -> List[str]:
    """Which subgoals currently drive fold merge + Hit provenance.

    Always-active bindable goals participate until satisfied. Conditional goals
    participate only after activation (M5); empty ``activated`` keeps them out
    of the fold so rare forks do not steal display budget up front.
    """
    activated = set(activated or ())
    out: List[str] = []
    for sg in plan.subgoals or []:
        if sg.id not in bindable:
            continue
        if sg.id in satisfied:
            continue
        if is_always_active(sg) or sg.id in activated:
            out.append(sg.id)
    return out


def fold_weights_for_plan(
    plan: RetrievalPlan,
    participant_ids: Sequence[str],
    *,
    goal_conditioned: bool,
) -> Dict[str, float]:
    """Relative fold weights.

    When goal-conditioned folding is on, use each participant's ``budget_share``
    (equal fallback if all zero). When off, every participant has weight 1.0 —
    still a multi-source max, just unweighted.
    """
    by_id = {s.id: s for s in (plan.subgoals or [])}
    ids = [str(i) for i in participant_ids]
    if not ids:
        return {}
    if not goal_conditioned:
        return {i: 1.0 for i in ids}
    raw = {i: max(0.0, float(getattr(by_id.get(i), "budget_share", 0.0) or 0.0)) for i in ids}
    if sum(raw.values()) <= 0.0:
        return {i: 1.0 for i in ids}
    return raw


def _route_hint_hits(
    plan: RetrievalPlan,
    participant_ids: Sequence[str],
) -> Dict[str, List[str]]:
    hits: Dict[str, List[str]] = {}
    by_id = {s.id: s for s in (plan.subgoals or [])}
    for sid in participant_ids:
        sg = by_id.get(sid)
        if sg is None:
            continue
        for hint in sg.route_hints or []:
            section = str(hint or "").strip()
            if not section:
                continue
            hits.setdefault(section, [])
            if sid not in hits[section]:
                hits[section].append(sid)
    return hits


def apply_illumination_to_state(
    state: NavState,
    *,
    subgoal_map_scores: Dict[str, Dict[str, float]],
    subgoal_unit_scores: Dict[str, Dict[str, float]],
    participant_ids: Sequence[str],
    weights: Dict[str, float],
    collect_top_k: int,
    route_hint_hits: Optional[Dict[str, List[str]]] = None,
) -> Dict[str, Any]:
    """Write merged scores / highlights / hit_sources onto ``state``."""
    state.subgoal_map_scores = {
        k: dict(v) for k, v in (subgoal_map_scores or {}).items()
    }
    state.subgoal_unit_scores = {
        k: dict(v) for k, v in (subgoal_unit_scores or {}).items()
    }
    state.active_subgoal_ids = [str(x) for x in participant_ids]

    merged_map = merge_score_maps(
        state.subgoal_map_scores,
        weights=weights,
        active_ids=participant_ids,
    )
    merged_units = merge_score_maps(
        state.subgoal_unit_scores,
        weights=weights,
        active_ids=participant_ids,
    )
    highlights, hit_sources = select_map_highlights_multi(
        state.subgoal_unit_scores,
        k=int(collect_top_k),
        active_ids=participant_ids,
        weights=weights,
    )
    for sid, sources in (route_hint_hits or {}).items():
        hit_sources.setdefault(sid, [])
        for src in sources:
            if src not in hit_sources[sid]:
                hit_sources[sid].append(src)
        if sid not in highlights:
            highlights.append(sid)

    state.map_scores = merged_map
    state.unit_scores = merged_units
    state.highlight_ids = list(highlights)
    state.hit_sources = {k: list(v) for k, v in hit_sources.items()}
    return {
        "n_queries": len(subgoal_map_scores),
        "participant_ids": list(participant_ids),
        "n_highlights": len(highlights),
        "weights": dict(weights),
    }


def refresh_fold_from_subgoal_scores(
    state: NavState,
    config: NavConfig,
) -> Optional[Dict[str, Any]]:
    """Re-merge stored per-subgoal scores after satisfaction / activation changes.

    No BM25 recompute — only fold weights + Hit union change.
    """
    plan = state.retrieval_plan
    if plan is None or not state.subgoal_map_scores:
        return None
    live = bindable_retrieval_queries(plan, state.slot_bindings)
    bindable = {
        sid: query
        for sid, query in live.items()
        if sid in state.subgoal_map_scores
    }
    participants = fold_participant_ids(
        plan,
        bindable=bindable,
        satisfied=set(state.satisfied_subgoal_ids or ()),
        activated=set(state.activated_subgoal_ids or ()),
    )
    participants = [p for p in participants if p in state.subgoal_map_scores]
    if not participants:
        return None
    weights = fold_weights_for_plan(
        plan,
        participants,
        goal_conditioned=bool(
            getattr(config, "enable_goal_conditioned_folding", False)
        ),
    )
    return apply_illumination_to_state(
        state,
        subgoal_map_scores=state.subgoal_map_scores,
        subgoal_unit_scores=state.subgoal_unit_scores,
        participant_ids=participants,
        weights=weights,
        collect_top_k=int(config.collect_top_k),
        route_hint_hits=_route_hint_hits(plan, participants),
    )


def illuminate_from_plan(
    ts: Any,
    state: NavState,
    config: NavConfig,
) -> Optional[Dict[str, Any]]:
    """Pass-1 illumination after a RetrievalPlan is available.

    Returns a TRACE-friendly detail dict, or None when there is nothing to do.
    """
    if not bool(getattr(config, "enable_per_subgoal_illumination", False)):
        return None
    plan = state.retrieval_plan
    if plan is None or not getattr(plan, "subgoals", None):
        return None

    queries = bindable_retrieval_queries(plan, state.slot_bindings)
    if not queries:
        return None

    participants = fold_participant_ids(
        plan,
        bindable=queries,
        satisfied=set(state.satisfied_subgoal_ids or ()),
        activated=set(state.activated_subgoal_ids or ()),
    )
    # Score every bindable query (including inactive conditionals) so activation
    # can reuse BM25 later; fold/Hit use participants only — never fall back to
    # unactivated conditionals stealing display budget.
    from nav_address import uses_document_nodes

    doc_id = state.doc_id
    corpus_ids = None
    root_ids = None
    if uses_document_nodes(ts) and not str(doc_id or "").strip():
        corpus_ids = list(ts.document_ids())
    elif is_corpus_doc_id(doc_id):
        corpus_ids = list(getattr(ts, "corpus_doc_ids", None) or [])
    else:
        root_ids = list(ts.sections_for_doc(doc_id))

    sub_map, sub_unit = compute_multi_query_map_scores(
        ts,
        queries=queries,
        doc_id=doc_id,
        root_ids=root_ids,
        corpus_doc_ids=corpus_ids,
    )
    state.subgoal_map_scores = {k: dict(v) for k, v in (sub_map or {}).items()}
    state.subgoal_unit_scores = {k: dict(v) for k, v in (sub_unit or {}).items()}

    if not participants:
        return {
            "n_queries": len(queries),
            "participant_ids": [],
            "n_highlights": len(state.highlight_ids or []),
            "weights": {},
            "deferred_fold": True,
        }

    weights = fold_weights_for_plan(
        plan,
        participants,
        goal_conditioned=bool(
            getattr(config, "enable_goal_conditioned_folding", False)
        ),
    )
    detail = apply_illumination_to_state(
        state,
        subgoal_map_scores=sub_map,
        subgoal_unit_scores=sub_unit,
        participant_ids=participants,
        weights=weights,
        collect_top_k=int(config.collect_top_k),
        route_hint_hits=_route_hint_hits(plan, participants),
    )
    detail["queries"] = {k: queries[k] for k in participants if k in queries}
    detail["goal_conditioned"] = bool(
        getattr(config, "enable_goal_conditioned_folding", False)
    )
    return detail
