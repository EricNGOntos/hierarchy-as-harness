"""M4/M5: wave orchestration over a RetrievalPlan.

Execution order = dependency DAG ∩ soft prefer_after. Each subgoal runs its own
harvest/navigate so evidence attribution stays per-subgoal. Slot values are
extracted only when a later subgoal references them; checklist acceptance is
owned by ``plan_control``.
"""

from __future__ import annotations

import re
import time
from dataclasses import asdict
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

from nav_navigate import navigate
from nav_plan import (
    RetrievalPlan,
    Subgoal,
    bind_slots,
    plan_query,
    unbound_slots,
)
from nav_types import NavConfig, NavState, SubgoalResult
from nav_verify import apply_bindings_from_result, build_subgoal_result

_SLOT_STRIP_RE = re.compile(r"\{\{\s*[^}]+\s*\}\}")


def ready_subgoal_ids(
    plan: RetrievalPlan,
    *,
    satisfied: Set[str],
    attempted: Optional[Set[str]] = None,
    dropped: Optional[Set[str]] = None,
) -> List[str]:
    """Subgoals eligible to run now (deps settled, not yet finished).

    F1: a dependency only needs to be *settled* (``satisfied`` or ``dropped``).
    Widen leaves a subgoal out of ``attempted`` so it stays ready next wave.
    """
    settled = set(satisfied) | set(dropped or ())
    known = {s.id for s in plan.subgoals}
    done = set(attempted or ()) | set(satisfied) | set(dropped or ())
    out: List[str] = []
    for sg in plan.subgoals:
        if sg.id in done:
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


def _clear_focus(state: NavState) -> None:
    state.focus_subgoal_id = ""
    state.focus_subgoal_need = ""
    state.focus_subgoal_contract = ""
    state.focus_retrieval_query = ""
    state.focus_contract_kind = ""


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


def _wave_subgoal_result(
    plan: RetrievalPlan,
    state: NavState,
    config: NavConfig,
    subgoal: Subgoal,
    *,
    retrieval_query: str,
    new_chunks: Sequence[Tuple[Any, float]],
    collected_before: Set[str],
) -> SubgoalResult:
    """Build this wave's result from *new* chunks only (never the global pool)."""
    return build_subgoal_result(
        plan,
        state.collected_section_ids,
        config,
        subgoal,
        retrieval_query=retrieval_query,
        new_chunks=new_chunks,
        collected_before=collected_before,
        use_llm_extract=bool(config.is_checklist),
    )


def _execute_subgoal_harvest_once(
    ts: Any,
    state: NavState,
    config: NavConfig,
    plan: RetrievalPlan,
    subgoal: Subgoal,
    *,
    steps_out: Optional[List[Any]],
) -> Dict[str, Any]:
    """One harvest() call for this subgoal this wave — no internal retry loop.

    Retry / widen / drop / replan authority belongs to ``plan_control`` across
    waves (see ``nav_control.plan_control``), not to this single call.
    """
    from nav_harvest import harvest

    rq = bind_slots(subgoal.retrieval_query, state.slot_bindings)
    if unbound_slots(rq):
        # F1: deps may be "settled" (satisfied or dropped) without ever
        # producing this subgoal's referenced slot — degrade to a query with
        # the unresolved {{...}} braces stripped rather than stalling.
        rq = _unbound_retrieval_query(subgoal)
    gap_note = str((state.subgoal_widen_gaps or {}).get(subgoal.id) or "").strip()
    if gap_note:
        rq = f"{rq}\n[widen gap] {gap_note}".strip()
    _set_focus(state, subgoal, rq)
    # Always enter at namespace/document root; prior dead-ends stay hidden via
    # subgoal_dismissed_section_ids so the next harvest sees siblings instead.
    before_sections = set(state.collected_section_ids)
    before_len = len(state.collected)
    harvest_result = harvest(
        ts,
        state,
        config,
        subgoal=subgoal,
        entry_scope=None,
        query=rq,
        steps_out=steps_out,
    )
    new_chunks = list(state.collected[before_len:])
    signal = _wave_subgoal_result(
        plan,
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
            "n_policy_calls": harvest_result.n_policy_calls,
            "visited_section_ids": list(harvest_result.visited_section_ids),
            "max_depth_hit": harvest_result.max_depth_hit,
            "reason": harvest_result.reason,
            "widen_gap": gap_note,
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

    ``widen`` = leave the subgoal unsettled for the next wave. Harvest again
    from the root with prior dead-ends dismissed and the last ``gap`` appended
    to the retrieval query. Only ``subgoal_max_attempts`` turns widen into drop.
    """
    del by_id  # reserved for future control context
    from nav_control import plan_control

    decision = plan_control(ts, state, config, plan=plan, wave_outputs=outputs)
    max_attempts = max(1, int(getattr(config, "subgoal_max_attempts", 2) or 2))

    for item in outputs:
        sid = item["subgoal_id"]
        result: SubgoalResult = item["result"]
        sub_decision = decision.per_subgoal.get(sid)
        has_evidence = int(getattr(result, "chars_used", 0) or 0) > 0
        kind = sub_decision.decision if sub_decision else ("accept" if has_evidence else "widen")
        # Circuit breaker: bound widen loops regardless of plan_control.
        if kind == "widen" and int(state.subgoal_attempt_counts.get(sid, 0)) >= max_attempts:
            kind = "drop"

        if kind == "accept":
            result.satisfied = True
            state.subgoal_results[sid] = asdict(result)
            state.satisfied_subgoal_ids.add(sid)
            state.attempted_subgoal_ids.add(sid)
            state.subgoal_widen_gaps.pop(sid, None)
        elif kind == "drop":
            state.dropped_subgoal_ids.add(sid)
            state.attempted_subgoal_ids.add(sid)
            state.subgoal_widen_gaps.pop(sid, None)
        else:
            # widen: keep unsettled; stash gap for the next harvest query.
            note = str(getattr(result, "gap", "") or "").strip()
            if note:
                state.subgoal_widen_gaps[sid] = note

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
    # Checklist mode always harvests + plan_controls (navigate-per-subgoal retired).
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

        by_id = {s.id: s for s in plan.subgoals}
        outputs: List[Dict[str, Any]] = []

        def _run_one(sid: str, working_state: NavState, out_steps: Optional[List[Any]]) -> Dict[str, Any]:
            return _execute_subgoal_harvest_once(
                ts, working_state, config, plan, by_id[sid], steps_out=out_steps
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
                {
                    "subgoal_id": sid,
                    "chars_used": result.chars_used,
                    "gap": result.gap,
                    "extracted": dict(result.extracted or {}),
                }
            )
            summary["results"][sid] = asdict(result)
            if result.extracted:
                state.slot_bindings = apply_bindings_from_result(
                    state.slot_bindings, by_id[sid], result.extracted
                )
            state.subgoal_attempt_counts[sid] = int(
                state.subgoal_attempt_counts.get(sid, 0)
            ) + 1

        control_detail = _apply_plan_control(
            ts, state, config, plan=plan, outputs=outputs, by_id=by_id, steps_out=steps_out
        )
        wave_detail["plan_control"] = control_detail
        replan_requested = bool(control_detail.get("replan"))
        if control_detail.get("done"):
            episode_done = True

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
                # so per-id bookkeeping (satisfied/attempted/dropped/widen gaps,
                # qualified "sX.slot" bindings) cannot be safely carried over —
                # those ids now mean something else. What IS safe and worth
                # keeping is unqualified slot bindings (plain fact values) and
                # every chunk already in state.collected.
                state.satisfied_subgoal_ids = set()
                state.attempted_subgoal_ids = set()
                state.dropped_subgoal_ids = set()
                state.subgoal_results = {}
                state.subgoal_widen_gaps = {}
                state.subgoal_attempt_counts = {}
                state.subgoal_dismissed_section_ids = {}
                state.slot_bindings = {
                    k: v for k, v in state.slot_bindings.items() if "." not in k
                }
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
    summary["dropped"] = sorted(state.dropped_subgoal_ids)
    return summary
