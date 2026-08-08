"""One-shot harvest primitive (PLAN×NAV fusion).

Replaces the multi-step COLLECT/DISPATCH/FINISH ReAct loop with a single
policy decision per visible map node: the model returns the union of nodes to
collect and the union of nodes to dispatch to a deeper harvester in one call.
FINISH is implicit — selecting neither collect nor dispatch simply ends this
region; there is no separate round trip asking "are you done?".

Recursion is bounded by ``max_harvest_depth`` and only ever follows an
explicit DISPATCH selection (never a fixed step budget). The map already
folds large scopes to title-only and offers D* ids for internal nodes
(``nav_projection.build_map`` / ``nav_actions.build_legal_actions``), so a
node whose children overflow the display budget naturally nudges the model
toward DISPATCH — no separate "scope overflow" special case is needed here.

Depends only on the existing map/action primitives (``nav_projection``,
``nav_actions``) plus ``nav_navigate._apply_collect`` for hydration — the same
kernel surface ``navigate()`` already uses. No new ToolSpace capability is
required beyond the 5 documented in docs/audit_plan_nav_overlap.md.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence, Tuple

from nav_actions import build_legal_actions, format_actionable_map_observation
from nav_compose import parse_collect_confidence
from nav_plan import Subgoal
from nav_policy import _extract_json_obj  # reuse: same tolerant JSON extraction
from nav_projection import build_projection
from nav_types import ActionKind, LegalAction, NavConfig, NavState, Projection

_HARVEST_PURPOSE_DEPTH0 = "nav_harvest_v1"
_HARVEST_PURPOSE_CHILD = "nav_harvest_child_v1"


@dataclass
class HarvestResult:
    subgoal_id: str
    new_section_ids: List[str] = field(default_factory=list)
    visited_section_ids: List[str] = field(default_factory=list)
    n_policy_calls: int = 0
    max_depth_hit: bool = False
    reason: str = ""


def _actions_by_ids(actions: Sequence[LegalAction], ids: Sequence[str]) -> List[LegalAction]:
    from nav_actions import actions_by_ids

    return actions_by_ids(list(actions), list(ids))


def _harvest_system_prompt(*, dispatch_available: bool) -> str:
    dispatch_rule = (
        "  - dispatch=D*: hand a node's subtree to a deeper harvester before "
        "deciding; use this only when the node's title/summary alone does not "
        "tell you whether the needed evidence is inside — the deeper harvester "
        "will make its own single decision over that subtree.\n"
        if dispatch_available
        else ""
    )
    return (
        "You are a retrieval harvester working on ONE retrieval subgoal inside "
        "a hierarchical document map region.\n\n"
        "In a single response, decide which visible nodes to collect as "
        "evidence for the subgoal below, and (if available) which visible "
        "nodes to hand to a deeper harvester. Selecting neither finishes this "
        "region — there is no separate finish step.\n\n"
        "=== Rules ===\n\n"
        "  - collect=C*: add the node (and its full subtree, when it is a "
        "parent) as evidence for the subgoal's contract.\n"
        f"{dispatch_rule}"
        "  - Use only action IDs shown on a node line. Never invent IDs or "
        "write raw section paths as targets.\n"
        "  - Prefer being decisive: if the visible titles/summaries already "
        "answer the subgoal, collect directly instead of dispatching.\n"
        "  - Provide confidence in [0,1] for every collect id (object map "
        "keyed by action id, or a single scalar when there is exactly one).\n\n"
        "=== End Rules ===\n\n"
        "Return ONLY one JSON object, e.g.:\n"
        '{"collect_ids":["C1"],"dispatch_ids":[],"confidence":{"C1":0.8},'
        '"reason":"short reason"}\n'
        "Do not include any explanation outside the JSON.\n\n"
        "IMPORTANT:\n"
        "1. All agent-generated text (reason) MUST be in English.\n"
        "2. Document content and section titles MUST remain in their "
        "original language.\n"
        "3. Keep reason under 25 words.\n"
    )


def _harvest_user_prompt(
    *,
    subgoal: Subgoal,
    query: str,
    observation: str,
) -> str:
    card = subgoal.contract.cardinality
    contract_line = f"{subgoal.contract.kind}" + (
        f" cardinality={card}" if card is not None else ""
    )
    mentions = ", ".join(subgoal.contract.must_mention or []) or "-"
    return (
        f"Subgoal need: {subgoal.need or query}\n"
        f"Retrieval query: {query}\n"
        f"Contract: {contract_line}\n"
        f"Must mention (if any): {mentions}\n\n"
        f"=== Region Observation ===\n{observation}\n=== End Region Observation ===\n"
    )


def _rule_fallback_selection(
    actions: Sequence[LegalAction],
) -> Tuple[List[LegalAction], List[LegalAction]]:
    """Deterministic pick when the LLM returns no valid ids: one collect else nothing."""
    for a in actions:
        if a.kind == ActionKind.COLLECT:
            return [a], []
    return [], []


def harvest_policy_call(
    ts: Any,
    state: NavState,
    config: NavConfig,
    *,
    subgoal: Subgoal,
    query: str,
    projection: Projection,
    actions: Sequence[LegalAction],
    depth: int,
) -> Tuple[List[LegalAction], List[LegalAction], Dict[str, float], str, Dict[str, Any]]:
    """One LLM call: returns (collect_actions, dispatch_actions, confidence, reason, meta)."""
    import os

    from agent_delivery.code.llm_api_cache import cached_chat_completion  # type: ignore
    from agent_delivery.code.llm_config import make_openai_client, require_llm_env  # type: ignore
    from agent_delivery.code.llm_usage import record_usage  # type: ignore

    require_llm_env(context="Nav Harvest")
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    model_env = config.subagent_model_env if depth > 0 else config.llm_model_env
    model = (
        os.environ.get(model_env, "").strip()
        or os.environ.get(config.llm_model_env, "").strip()
        or os.environ.get("COMPOSE_MODEL", "gpt-4o-mini")
    )
    base_url = os.environ.get("OPENAI_BASE_URL", "").strip() or None
    client = make_openai_client(api_key=key, base_url=base_url)

    dispatch_available = any(a.kind == ActionKind.DISPATCH for a in actions)
    system = _harvest_system_prompt(dispatch_available=dispatch_available)
    observation = format_actionable_map_observation(
        projection, list(actions), inline_summary=projection.scope is not None
    )
    user = _harvest_user_prompt(subgoal=subgoal, query=query, observation=observation)
    purpose = _HARVEST_PURPOSE_DEPTH0 if depth == 0 else _HARVEST_PURPOSE_CHILD

    cached = cached_chat_completion(
        client,
        purpose=purpose,
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        temperature=float(config.llm_temperature),
        max_tokens=int(config.llm_max_tokens),
        response_format={"type": "json_object"},
    )
    record_usage("nav_harvest", cached.get("usage"))
    text = str(cached.get("content") or "").strip()
    obj = _extract_json_obj(text) or {}

    collect_ids = [str(x).strip().upper() for x in (obj.get("collect_ids") or []) if str(x).strip()]
    dispatch_ids = [str(x).strip().upper() for x in (obj.get("dispatch_ids") or []) if str(x).strip()]
    collect_actions = [a for a in _actions_by_ids(actions, collect_ids) if a.kind == ActionKind.COLLECT]
    dispatch_actions = [a for a in _actions_by_ids(actions, dispatch_ids) if a.kind == ActionKind.DISPATCH]
    fallback_used = False
    if not collect_actions and not dispatch_actions and not collect_ids and not dispatch_ids:
        # Genuinely empty selection == implicit finish; not a parse failure.
        pass
    elif not collect_actions and not dispatch_actions:
        collect_actions, dispatch_actions = _rule_fallback_selection(actions)
        fallback_used = True

    confidence = parse_collect_confidence(obj, collect_actions)
    reason = str(obj.get("reason") or "")[:300]
    meta = {
        "model": model,
        "raw": text[:500],
        "depth": depth,
        "fallback_used": fallback_used,
    }
    return collect_actions, dispatch_actions, confidence, reason, meta


def resolve_harvest_anchor(
    subgoal: Subgoal,
    state: NavState,
    config: NavConfig,
) -> Optional[str]:
    """Per-subgoal harvest entry scope: reharvest override > route_hints > root.

    Skips hints already fully collected, and hints outside a declared
    ``scope_filter.doc_ids`` (anchors never cross a subgoal's own document
    boundary once one is declared).
    """
    if not bool(getattr(config, "enable_anchor_entry", False)):
        return None
    override = str((state.subgoal_reharvest_anchor or {}).get(subgoal.id) or "").strip()
    if override:
        return override

    from path_ledger import doc_id_for

    allowed_docs = {d for d in (subgoal.scope_filter.doc_ids or []) if str(d).strip()}
    for hint in subgoal.route_hints or []:
        sid = str(hint or "").strip()
        if not sid or sid in state.collected_section_ids:
            continue
        if allowed_docs:
            doc = doc_id_for(sid)
            if doc and doc not in allowed_docs:
                continue
        return sid
    return None


def harvest(
    ts: Any,
    state: NavState,
    config: NavConfig,
    *,
    subgoal: Subgoal,
    entry_scope: Optional[str],
    query: str,
    steps_out: Optional[List[Any]] = None,
) -> HarvestResult:
    """Anchor-entry, single-decision-per-node evidence harvest for one subgoal."""
    result = HarvestResult(subgoal_id=subgoal.id)
    from agent_delivery.code.tool_space import is_doc_root_section  # type: ignore

    initial_depth = 0 if (entry_scope is None or is_doc_root_section(entry_scope)) else 1
    _harvest_node(
        ts,
        state,
        config,
        subgoal=subgoal,
        node_scope=entry_scope,
        query=query,
        depth=initial_depth,
        budget=int(config.map_char_limit),
        steps_out=steps_out,
        result=result,
    )
    return result


def _harvest_node(
    ts: Any,
    state: NavState,
    config: NavConfig,
    *,
    subgoal: Subgoal,
    node_scope: Optional[str],
    query: str,
    depth: int,
    budget: int,
    steps_out: Optional[List[Any]],
    result: HarvestResult,
) -> None:
    from nav_navigate import _apply_collect  # late import avoids cycle

    max_depth = max(0, int(getattr(config, "max_harvest_depth", 0) or 0))
    show_harvested = bool(getattr(config, "show_harvested_in_map", False))
    projection = build_projection(
        ts,
        doc_id=state.doc_id,
        query=query,
        scope=node_scope,
        config=config,
        map_scores=state.map_scores,
        collected_section_ids=state.collected_section_ids,
        dismissed_section_ids=state.dismissed_section_ids,
        highlight_ids=state.highlight_ids,
        hit_sources=state.hit_sources or None,
        harvested_section_ids=state.harvested_owner_subgoal if show_harvested else None,
    )
    actions = build_legal_actions(state, projection, step_idx=0, config=config, depth=depth)
    actionable = [a for a in actions if a.kind != ActionKind.FINISH]
    if not actionable:
        result.reason = result.reason or "no_legal_actions"
        return

    collect_actions, dispatch_actions, confidence, reason, meta = harvest_policy_call(
        ts,
        state,
        config,
        subgoal=subgoal,
        query=query,
        projection=projection,
        actions=actions,
        depth=depth,
    )
    result.n_policy_calls += 1
    if steps_out is not None:
        from agent_delivery.agent.types import AgentStep  # type: ignore

        steps_out.append(
            AgentStep(
                step_idx=len(steps_out) + 1,
                action="harvest",
                detail={
                    "subgoal_id": subgoal.id,
                    "scope": node_scope,
                    "depth": depth,
                    "collect_ids": [a.action_id for a in collect_actions],
                    "dispatch_ids": [a.action_id for a in dispatch_actions],
                    "reason": reason,
                    **meta,
                },
            )
        )

    if collect_actions:
        conf_by_sid = {
            str(a.section_id): float(confidence.get(a.action_id.upper(), 0.0))
            for a in collect_actions
            if a.section_id
        }
        primary = collect_actions[0]
        primary.metadata = dict(primary.metadata or {})
        primary.metadata["batch_actions"] = collect_actions
        primary.metadata["confidence_by_section"] = conf_by_sid
        cdetail = _apply_collect(ts, state, primary, config)
        new_roots = list(cdetail.get("collect_section_ids") or [])
        result.new_section_ids.extend(new_roots)
        if bool(getattr(config, "show_harvested_in_map", False)):
            for sid in new_roots:
                state.harvested_owner_subgoal[sid] = subgoal.id

    if dispatch_actions and depth >= max_depth:
        result.max_depth_hit = True
        return

    for act in dispatch_actions:
        sid = str(act.section_id or "").strip()
        if not sid or sid == str(node_scope or ""):
            continue
        result.visited_section_ids.append(sid)
        child_budget = max(500, int(budget * 0.85))
        _harvest_node(
            ts,
            state,
            config,
            subgoal=subgoal,
            node_scope=sid,
            query=query,
            depth=depth + 1,
            budget=child_budget,
            steps_out=steps_out,
            result=result,
        )
