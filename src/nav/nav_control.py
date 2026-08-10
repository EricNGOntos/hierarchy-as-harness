"""Merged check authority (PLAN×NAV fusion): one planner decision per wave.

Before this module, four independent "is it enough?" judges disagreed without
talking to each other (NAV FINISH, depth-0 group_rank, free-text subagent
reports, PLAN contract verify — see docs/audit_plan_nav_overlap.md §1.6).
``plan_control`` is the single authority left standing: it reviews every
subgoal's own newly-collected evidence for the current wave (never the
global pool — see the ``collected_before`` fix in ``nav_orchestrate``) plus a
zero-cost rule signal from ``nav_verify.verify_contract``, and returns one
decision per subgoal plus one global decision. ``REPLAN`` can only originate
here — the old "retries exhausted -> escalate" path is not used on this path.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any, Dict, List, Literal, Optional, Sequence

from nav_plan import RetrievalPlan, Subgoal
from nav_policy import _extract_json_obj
from nav_types import NavConfig, NavState

SubgoalDecisionKind = Literal["accept", "widen", "drop"]
GlobalDecisionKind = Literal["continue", "replan", "done"]

_CONTROL_PURPOSE = "nav_plan_control_v1"
_SUBGOAL_DECISIONS = {"accept", "widen", "drop"}
_GLOBAL_DECISIONS = {"continue", "replan", "done"}


@dataclass
class SubgoalDecision:
    subgoal_id: str
    decision: SubgoalDecisionKind = "accept"
    note: str = ""


@dataclass
class PlanControlDecision:
    per_subgoal: Dict[str, SubgoalDecision] = field(default_factory=dict)
    global_action: GlobalDecisionKind = "continue"
    reason: str = ""
    raw: str = ""


def _digest_evidence(new_chunks: Sequence[Any], *, limit: int) -> str:
    parts: List[str] = []
    total = 0
    for chunk, _score in list(new_chunks or []):
        text = str(getattr(chunk, "text", "") or getattr(chunk, "content", "") or "").strip()
        if not text or total >= limit:
            continue
        take = text[: max(0, limit - total)]
        parts.append(take)
        total += len(take)
    return "\n".join(parts)


def _wave_subgoal_block(
    subgoal: Subgoal,
    *,
    signal: Any,
    digest: str,
    harvest_meta: Optional[Dict[str, Any]],
    attempt_count: int,
) -> str:
    card = subgoal.contract.cardinality
    contract_line = f"{subgoal.contract.kind}" + (
        f" cardinality={card}" if card is not None else ""
    )
    lines = [
        f"[{subgoal.id}] need: {subgoal.need}",
        f"  contract: {contract_line}",
        "  search_space: shared (no per-subgoal scope/anchor)",
        f"  rule_signal: verdict={getattr(signal, 'verdict', '')} "
        f"gap={getattr(signal, 'gap', '') or '-'} "
        f"satisfied={bool(getattr(signal, 'satisfied', False))}",
        f"  attempt: {attempt_count}",
    ]
    if harvest_meta:
        lines.append(
            "  harvest: anchor="
            f"{harvest_meta.get('anchor') or '-'} "
            f"visited={len(harvest_meta.get('visited_section_ids') or [])} "
            f"policy_calls={harvest_meta.get('n_policy_calls', 0)}"
        )
        harvest_reason = str(harvest_meta.get("reason") or "").strip()
        if harvest_reason:
            lines.append(f"  harvest_reason: {harvest_reason}")
    lines.append(f"  new_evidence: {digest.strip() or '(empty)'}")
    return "\n".join(lines)


def _plan_overview_block(plan: RetrievalPlan, state: NavState) -> str:
    lines = ["coverage_checklist:"]
    checklist = list(getattr(plan, "coverage_checklist", None) or [])
    if checklist:
        for item in checklist:
            lines.append(f"- {item.id}: {item.fact}")
    else:
        lines.append("- (none)")
    lines.append("subgoals:")
    for sg in plan.subgoals:
        status = (
            "satisfied"
            if sg.id in state.satisfied_subgoal_ids
            else "attempted" if sg.id in state.attempted_subgoal_ids else "pending"
        )
        lines.append(f"- {sg.id}: {sg.need} [{status}]")
    return "\n".join(lines)


def _control_system_prompt() -> str:
    return (
        "You are the single retrieval-plan controller for one wave of a "
        "hierarchical document retrieval episode. You replace all separate "
        "per-region stop/retry judgments with one decision.\n\n"
        "The plan has a global coverage_checklist (facts that must appear in "
        "episode evidence) and one shared search space. For each subgoal in "
        "this wave you are shown: its need/contract, a zero-cost rule signal, "
        "the harvester's own explanation (harvest_reason), and the evidence "
        "collected THIS wave only (never older evidence from other subgoals).\n\n"
        "=== Per-subgoal decisions ===\n"
        "  - accept: this subgoal's need is covered by this wave's evidence.\n"
        "  - widen: not yet covered, and this region plausibly does not "
        "hold the answer; step out to the parent scope and look again with a "
        "coarser view (handled automatically — you do not name an anchor, "
        "and nodes already reviewed and rejected for this subgoal will not "
        "be shown again).\n"
        "  - drop: not covered and further attempts are unlikely to help "
        "(e.g. evidence is structurally absent, or harvest_reason shows the "
        "search has already reached the document root with nothing found); "
        "stop trying this subgoal.\n\n"
        "=== Global decision ===\n"
        "  - continue: proceed to the next wave with current subgoal set.\n"
        "  - replan: the retrieval plan's decomposition itself is wrong "
        "(e.g. missing checklist facts, wrong dependencies) and needs regenerating. "
        "Only choose this for a structural plan problem, not for an "
        "individual subgoal's evidence gap (use widen/drop for those).\n"
        "  - done: the coverage_checklist is met (or cannot be met "
        "further); stop the episode.\n\n"
        "Return ONLY one JSON object:\n"
        "{\n"
        '  "subgoals": {"s1": {"decision": "accept|widen|drop", '
        '"note": "..."}},\n'
        '  "global": "continue|replan|done",\n'
        '  "reason": "..."\n'
        "}\n"
        "Do not include any explanation outside the JSON.\n\n"
        "IMPORTANT:\n"
        "1. All agent-generated text (note/reason) MUST be in English.\n"
        "2. Keep reason under 30 words; keep each note under 15 words.\n"
    )


def _parse_control_decision(obj: Dict[str, Any], subgoal_ids: Sequence[str]) -> PlanControlDecision:
    per_subgoal: Dict[str, SubgoalDecision] = {}
    raw_sub = obj.get("subgoals") if isinstance(obj, dict) else None
    if isinstance(raw_sub, dict):
        for sid in subgoal_ids:
            row = raw_sub.get(sid)
            if not isinstance(row, dict):
                continue
            decision = str(row.get("decision") or "").strip().lower()
            if decision not in _SUBGOAL_DECISIONS:
                decision = "accept"
            per_subgoal[sid] = SubgoalDecision(
                subgoal_id=sid,
                decision=decision,  # type: ignore[arg-type]
                note=str(row.get("note") or "")[:200],
            )
    global_action = str(obj.get("global") or "").strip().lower()
    if global_action not in _GLOBAL_DECISIONS:
        global_action = "continue"
    return PlanControlDecision(
        per_subgoal=per_subgoal,
        global_action=global_action,  # type: ignore[arg-type]
        reason=str(obj.get("reason") or "")[:300],
    )


def _fallback_decision(
    subgoal_ids: Sequence[str],
    signals: Dict[str, Any],
) -> PlanControlDecision:
    """Deterministic fallback when the LLM call fails or returns malformed JSON.

    Mirrors the pre-fusion rule: satisfied -> accept, retry-family -> widen
    (broaden rather than blindly repeat the same failing anchor).
    """
    per_subgoal: Dict[str, SubgoalDecision] = {}
    for sid in subgoal_ids:
        sig = signals.get(sid)
        satisfied = bool(getattr(sig, "satisfied", False)) if sig is not None else False
        per_subgoal[sid] = SubgoalDecision(
            subgoal_id=sid,
            decision="accept" if satisfied else "widen",
        )
    return PlanControlDecision(per_subgoal=per_subgoal, global_action="continue", reason="fallback")


def plan_control(
    ts: Any,
    state: NavState,
    config: NavConfig,
    *,
    plan: RetrievalPlan,
    wave_outputs: Sequence[Dict[str, Any]],
) -> PlanControlDecision:
    """One LLM call per wave: per-subgoal accept/widen/drop + global signal."""
    from nav_token_budget import nav_token_budget_exhausted

    by_id = {s.id: s for s in plan.subgoals}
    subgoal_ids = [str(item.get("subgoal_id")) for item in wave_outputs]
    signals = {str(item.get("subgoal_id")): item.get("result") for item in wave_outputs}
    if not subgoal_ids:
        return PlanControlDecision(global_action="continue")
    if nav_token_budget_exhausted():
        decision = _fallback_decision(subgoal_ids, signals)
        decision.global_action = "done"
        decision.reason = "token_limit"
        return decision

    digest_limit = max(0, int(getattr(config, "plan_control_digest_chars", 600) or 0))
    blocks: List[str] = []
    for item in wave_outputs:
        sid = str(item.get("subgoal_id"))
        sg = by_id.get(sid)
        if sg is None:
            continue
        digest = _digest_evidence(item.get("new_chunks") or [], limit=digest_limit)
        blocks.append(
            _wave_subgoal_block(
                sg,
                signal=item.get("result"),
                digest=digest,
                harvest_meta=item.get("harvest"),
                attempt_count=int(state.subgoal_attempt_counts.get(sid, 0)),
            )
        )
    user = (
        f"=== Plan Overview ===\n{_plan_overview_block(plan, state)}\n"
        "=== End Plan Overview ===\n\n"
        f"=== This Wave ({len(wave_outputs)} subgoal(s)) ===\n"
        + "\n\n".join(blocks)
        + "\n=== End This Wave ===\n\n"
        "Return the control decision JSON."
    )

    try:
        from agent_delivery.code.llm_api_cache import cached_chat_completion  # type: ignore
        from agent_delivery.code.llm_config import make_openai_client, require_llm_env  # type: ignore
        from agent_delivery.code.llm_usage import record_usage  # type: ignore

        require_llm_env(context="Nav Plan Control")
        model = (
            os.environ.get(config.planner_model_env, "").strip()
            or os.environ.get(config.llm_model_env, "").strip()
            or os.environ.get("COMPOSE_MODEL", "").strip()
            or "gpt-4o-mini"
        )
        key = os.environ.get("OPENAI_API_KEY", "").strip()
        client = make_openai_client(
            api_key=key, base_url=os.environ.get("OPENAI_BASE_URL", "").strip() or None
        )
        # Planner-class call: reuse planner_llm_max_tokens (not navigate's 256).
        # Reasoning models may spend the whole budget on reasoning_content and
        # leave content empty — same recovery path as nav_plan.plan_query.
        max_tokens = max(
            256,
            int(getattr(config, "planner_llm_max_tokens", 0) or 0)
            or int(config.llm_max_tokens or 256),
        )
        cached = cached_chat_completion(
            client,
            purpose=_CONTROL_PURPOSE,
            model=model,
            messages=[
                {"role": "system", "content": _control_system_prompt()},
                {"role": "user", "content": user},
            ],
            temperature=float(config.llm_temperature),
            max_tokens=max_tokens,
            response_format={"type": "json_object"},
        )
        record_usage("nav_plan_control", cached.get("usage"))
        text = str(cached.get("content") or "").strip()
        if not text:
            reasoning = str(cached.get("reasoning_content") or "").strip()
            if reasoning and _extract_json_obj(reasoning):
                text = reasoning
        obj = _extract_json_obj(text) or {}
        decision = _parse_control_decision(obj, subgoal_ids)
        decision.raw = text[:1000]
        # Any subgoal the model omitted still needs an explicit decision.
        for sid in subgoal_ids:
            if sid not in decision.per_subgoal:
                sig = signals.get(sid)
                satisfied = bool(getattr(sig, "satisfied", False)) if sig is not None else False
                decision.per_subgoal[sid] = SubgoalDecision(
                    subgoal_id=sid, decision="accept" if satisfied else "widen"
                )
        return decision
    except Exception:
        return _fallback_decision(subgoal_ids, signals)
