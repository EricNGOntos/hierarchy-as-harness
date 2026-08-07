"""M4/M5: wave orchestration over a RetrievalPlan.

Execution order = dependency DAG ∩ optional map-locality merge ∩ soft prefer_after.
Soft plan: never clips C*/D*/F* action space — only changes query focus,
bindings, fold weights, and TRACE.
"""

from __future__ import annotations

import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

from nav_illuminate import (
    bindable_retrieval_queries,
    illuminate_from_plan,
    refresh_fold_from_subgoal_scores,
)
from nav_navigate import _fork_nav_state, _merge_nav_state, navigate
from nav_plan import (
    RetrievalPlan,
    ScopeFilter,
    Subgoal,
    bind_slots,
    is_always_active,
    plan_query,
)
from nav_types import NavConfig, NavState, SubgoalResult
from nav_verify import (
    activation_when_holds,
    apply_bindings_from_result,
    build_evidence_text_from_state,
    extract_slots,
    verify_contract,
)

_SLOT_STRIP_RE = re.compile(r"\{\{\s*[^}]+\s*\}\}")


def ready_subgoal_ids(
    plan: RetrievalPlan,
    *,
    satisfied: Set[str],
    activated: Set[str],
    bindings: Dict[str, str],
    attempted: Optional[Set[str]] = None,
) -> List[str]:
    """Subgoals eligible to run now (deps met, bindable, not yet finished)."""
    bindable = bindable_retrieval_queries(plan, bindings)
    known = {s.id for s in plan.subgoals}
    done = set(attempted or ()) | set(satisfied)
    out: List[str] = []
    for sg in plan.subgoals:
        if sg.id in done:
            continue
        if sg.id not in bindable:
            continue
        if not is_always_active(sg) and sg.id not in activated:
            continue
        deps = [d for d in (sg.depends_on or []) if d in known]
        if any(d not in satisfied for d in deps):
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


def beacons_for_subgoal(
    state: NavState,
    subgoal_id: str,
    *,
    k: int,
) -> List[str]:
    """Beacon sections for locality: Hit provenance, else top map scores."""
    sid = str(subgoal_id)
    prefer_docs = {
        str(d).strip()
        for d in (getattr(state, "focus_scope_doc_ids", None) or [])
        if str(d).strip()
    }
    from_hits: List[str] = []
    for section, sources in (state.hit_sources or {}).items():
        if sid in (sources or []):
            from_hits.append(str(section))
    if prefer_docs:
        scoped = [s for s in from_hits if any(d in s for d in prefer_docs)]
        if scoped:
            from_hits = scoped
    if from_hits:
        return from_hits[: max(1, int(k))]
    scores = dict((state.subgoal_map_scores or {}).get(sid) or {})
    if not scores and state.map_scores:
        scores = dict(state.map_scores)
    ranked = sorted(scores.items(), key=lambda kv: (-float(kv[1] or 0.0), str(kv[0])))
    ids = [s for s, _ in ranked]
    if prefer_docs:
        scoped = [s for s in ids if any(d in s for d in prefer_docs)]
        if scoped:
            ids = scoped
    return ids[: max(1, int(k))]


def _ancestor_set(ts: Any, section_id: str, doc_id: str) -> Set[str]:
    rel = getattr(ts, "section_relation_ids", None)
    if not callable(rel):
        return {str(section_id)}
    try:
        ancestors, _desc = rel(section_id, doc_id)
        out = {str(section_id)}
        out.update(str(a) for a in (ancestors or []) if a)
        return out
    except Exception:
        return {str(section_id)}


def _beacons_related(
    ts: Any,
    doc_id: str,
    a: Sequence[str],
    b: Sequence[str],
) -> bool:
    """True if any beacon pair shares ancestry (same local subtree)."""
    if not a or not b:
        return False
    sets_a = [_ancestor_set(ts, sid, doc_id) for sid in a]
    sets_b = [_ancestor_set(ts, sid, doc_id) for sid in b]
    for sa in sets_a:
        for sb in sets_b:
            if sa & sb:
                return True
    return False


def cluster_by_locality(
    ts: Any,
    state: NavState,
    subgoal_ids: Sequence[str],
    *,
    k: int,
    enabled: bool,
) -> List[List[str]]:
    """Union-find merge of same-wave subgoals whose beacons share a subtree."""
    ids = [str(x) for x in subgoal_ids]
    if not ids:
        return []
    if not enabled or len(ids) == 1:
        return [[i] for i in ids]

    parent = {i: i for i in ids}

    def find(x: str) -> str:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: str, b: str) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    beacons = {i: beacons_for_subgoal(state, i, k=k) for i in ids}
    for i, si in enumerate(ids):
        for sj in ids[i + 1 :]:
            if _beacons_related(ts, state.doc_id, beacons[si], beacons[sj]):
                union(si, sj)

    groups: Dict[str, List[str]] = {}
    for i in ids:
        groups.setdefault(find(i), []).append(i)
    order = []
    seen = set()
    for i in ids:
        root = find(i)
        if root not in seen:
            seen.add(root)
            order.append(root)
    return [groups[r] for r in order]


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
    collected_before: Set[str],
    force_llm_extract: bool = False,
) -> SubgoalResult:
    evidence = build_evidence_text_from_state(state)
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
    want_replan = False

    for attempt in range(max_attempts):
        before = set(state.collected_section_ids)

        if last is not None and last.verdict == "WIDEN":
            _widen_scope_filter(subgoal)

        if last is not None and last.verdict == "REBIND":
            # First: re-extract (LLM if verify enabled). If still bad, degrade query.
            re_extract = _verify_subgoal(
                state,
                config,
                subgoal,
                retrieval_query=rq,
                collected_before=before,
                force_llm_extract=True,
            )
            if re_extract.satisfied or re_extract.verdict == "SATISFIED":
                return re_extract, False
            rq = _unbound_retrieval_query(subgoal)

        _set_focus(state, subgoal, rq)
        child_steps: List[Any] = []
        _run_navigate_for_query(ts, state, config, query=rq, steps_out=child_steps)
        if steps_out is not None:
            steps_out.extend(child_steps)
        last = _verify_subgoal(
            state,
            config,
            subgoal,
            retrieval_query=rq,
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


def _execute_cluster_on_state(
    ts: Any,
    state: NavState,
    config: NavConfig,
    plan: RetrievalPlan,
    cluster: List[str],
    *,
    steps_out: Optional[List[Any]],
) -> List[Dict[str, Any]]:
    by = {s.id: s for s in plan.subgoals}
    results: List[Dict[str, Any]] = []
    merge = len(cluster) > 1 and bool(getattr(config, "enable_locality_merge", False))
    if merge:
        parts = [bind_slots(by[sid].retrieval_query, state.slot_bindings) for sid in cluster]
        join_q = chr(10).join(parts)
        before = set(state.collected_section_ids)
        _set_focus(state, by[cluster[0]], join_q)
        child_steps: List[Any] = []
        _run_navigate_for_query(ts, state, config, query=join_q, steps_out=child_steps)
        if steps_out is not None:
            steps_out.extend(child_steps)
        for sid in cluster:
            sg = by[sid]
            rq = bind_slots(sg.retrieval_query, state.slot_bindings)
            result = _verify_subgoal(
                state, config, sg, retrieval_query=rq, collected_before=before
            )
            results.append(
                {
                    "subgoal_id": sid,
                    "result": result,
                    "want_replan": result.verdict == "REPLAN",
                }
            )
        _clear_focus(state)
        return results

    for sid in cluster:
        sg = by[sid]
        result, want_replan = _execute_subgoal_with_verdicts(
            ts, state, config, sg, steps_out=steps_out
        )
        results.append(
            {"subgoal_id": sid, "result": result, "want_replan": want_replan}
        )
        _clear_focus(state)
    return results


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
    wave_idx = 0
    summary: Dict[str, Any] = {"waves": [], "results": {}}

    while True:
        if max_waves > 0 and wave_idx >= max_waves:
            break
        ready = ready_subgoal_ids(
            plan,
            satisfied=set(state.satisfied_subgoal_ids),
            activated=set(state.activated_subgoal_ids),
            bindings=dict(state.slot_bindings),
            attempted=set(state.attempted_subgoal_ids),
        )
        if not ready:
            break
        wave_idx += 1
        clusters = cluster_by_locality(
            ts,
            state,
            ready,
            k=int(config.collect_top_k),
            enabled=bool(getattr(config, "enable_locality_merge", False)),
        )
        wave_detail: Dict[str, Any] = {
            "wave": wave_idx,
            "ready": list(ready),
            "clusters": [list(c) for c in clusters],
            "cluster_results": [],
        }

        if bool(getattr(config, "enable_per_subgoal_illumination", False)):
            refresh_fold_from_subgoal_scores(state, config)

        by_id = {s.id: s for s in plan.subgoals}
        cluster_outputs: List[List[Dict[str, Any]]] = []

        if len(clusters) <= 1:
            for c in clusters:
                cluster_outputs.append(
                    _execute_cluster_on_state(
                        ts, state, config, plan, c, steps_out=steps_out
                    )
                )
        else:
            max_workers = max(1, min(len(clusters), int(config.dispatch_max_workers or 1)))
            forks = [(c, _fork_nav_state(state)) for c in clusters]

            def _run_fork(item: Tuple[List[str], NavState]):
                cluster, child = item
                fork_steps: List[Any] = []
                res = _execute_cluster_on_state(
                    ts, child, config, plan, cluster, steps_out=fork_steps
                )
                return cluster, child, res, fork_steps

            with ThreadPoolExecutor(max_workers=max_workers) as pool:
                futs = [pool.submit(_run_fork, item) for item in forks]
                for fut in as_completed(futs):
                    _c, child, results, fork_steps = fut.result()
                    _merge_nav_state(state, child)
                    state.slot_bindings.update(child.slot_bindings)
                    state.satisfied_subgoal_ids.update(child.satisfied_subgoal_ids)
                    state.attempted_subgoal_ids.update(child.attempted_subgoal_ids)
                    state.activated_subgoal_ids.update(child.activated_subgoal_ids)
                    state.subgoal_results.update(child.subgoal_results)
                    if steps_out is not None and fork_steps:
                        steps_out.extend(fork_steps)
                    cluster_outputs.append(results)

        replan_requested = False
        for group in cluster_outputs:
            for item in group:
                sid = item["subgoal_id"]
                result: SubgoalResult = item["result"]
                state.subgoal_results[sid] = asdict(result)
                wave_detail["cluster_results"].append(
                    {"subgoal_id": sid, "verdict": result.verdict, "gap": result.gap}
                )
                summary["results"][sid] = asdict(result)

                if result.extracted:
                    state.slot_bindings = apply_bindings_from_result(
                        state.slot_bindings, by_id[sid], result.extracted
                    )

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
                state.satisfied_subgoal_ids = set()
                state.attempted_subgoal_ids = set()
                state.activated_subgoal_ids = set()
                state.slot_bindings = {}
                state.subgoal_results = {}
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
