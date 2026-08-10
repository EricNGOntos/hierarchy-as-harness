"""M5: mechanical evidence/slot signal, slot extraction, activation predicates.

Soft plan: verdicts never clip the action space — they only drive bindings,
satisfaction marks, fold refresh, and optional replan. Whether a need is
actually answered is decided by ``nav_control.plan_control`` against the plan's
coverage checklist, not here.
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from typing import Any, Dict, List, Literal, Optional, Tuple

from nav_plan import Subgoal
from nav_types import NavConfig, SubgoalResult

Verdict = Literal[
    "SATISFIED",
    "RETRY_SAME_REGION",
    "REBIND",
    "REPLAN",
]

_TOKEN_RE = re.compile(r"[\w\u4e00-\u9fff]+", re.UNICODE)


@dataclass
class VerifyOutcome:
    verdict: Verdict
    result: SubgoalResult
    gap: str = ""


def _tokens(text: str) -> List[str]:
    return [t.lower() for t in _TOKEN_RE.findall(text or "") if t.strip()]


def evidence_chars(text: str) -> int:
    return len((text or "").strip())


def extract_slots_heuristic(
    subgoal: Subgoal,
    evidence_text: str,
    *,
    retrieval_query: str = "",
) -> Dict[str, str]:
    """Deterministic slot fill from evidence (no LLM, no magic thresholds).

    Prefer contract.must_mention hits; else the evidence line with the largest
    token overlap against the retrieval query / need.
    """
    text = evidence_text or ""
    if not text.strip() or not subgoal.produces:
        return {}
    out: Dict[str, str] = {}
    mentions = [m for m in (subgoal.contract.must_mention or []) if str(m).strip()]
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    q_tokens = set(_tokens(retrieval_query or subgoal.need or subgoal.retrieval_query))
    best_line = ""
    best_overlap = -1
    for ln in lines:
        overlap = len(q_tokens & set(_tokens(ln))) if q_tokens else 0
        if overlap > best_overlap:
            best_overlap = overlap
            best_line = ln
    for slot in subgoal.produces:
        name = str(slot).strip()
        if not name:
            continue
        hit_mentions = [m for m in mentions if m in text]
        if hit_mentions:
            if subgoal.contract.kind == "enumeration":
                out[name] = "、".join(hit_mentions)
            else:
                out[name] = hit_mentions[0]
        elif best_line:
            out[name] = best_line
    return out


def extract_slots_llm(
    subgoal: Subgoal,
    evidence_text: str,
    config: NavConfig,
    *,
    retrieval_query: str = "",
) -> Dict[str, str]:
    """Ask the LLM for produced slot values; empty on failure."""
    slots = [str(s).strip() for s in (subgoal.produces or []) if str(s).strip()]
    if not slots or not (evidence_text or "").strip():
        return {}
    try:
        from agent_delivery.code.llm_api_cache import cached_chat_completion  # type: ignore
        from agent_delivery.code.llm_config import make_openai_client, require_llm_env  # type: ignore
        from agent_delivery.code.llm_usage import record_usage  # type: ignore
        from nav_token_budget import nav_token_budget_exhausted
    except Exception:
        return {}
    if nav_token_budget_exhausted():
        return {}

    require_llm_env(context="Nav Slot Extract")
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    model = (
        os.environ.get(config.planner_model_env, "").strip()
        or os.environ.get(config.llm_model_env, "").strip()
        or os.environ.get("COMPOSE_MODEL", "").strip()
        or "gpt-4o-mini"
    )
    client = make_openai_client(
        api_key=key,
        base_url=os.environ.get("OPENAI_BASE_URL", "").strip() or None,
    )
    system = (
        "Extract slot values for a retrieval subgoal from evidence text.\n"
        'Return ONLY JSON: {"slots": {"name": "value"}, "confidence": 0..1}.\n'
        "Use the evidence language. If a slot is missing, omit it.\n"
        "Do not invent facts absent from the evidence."
    )
    user = (
        f"Need: {subgoal.need}\n"
        f"Retrieval query: {retrieval_query or subgoal.retrieval_query}\n"
        f"Slots to fill: {json.dumps(slots, ensure_ascii=False)}\n"
        f"Contract: {subgoal.contract.kind}"
        + (
            f", cardinality={subgoal.contract.cardinality}"
            if subgoal.contract.cardinality
            else ""
        )
        + f"\n\n=== Evidence ===\n{evidence_text[:6000]}\n=== End Evidence ===\n"
    )
    try:
        cached = cached_chat_completion(
            client,
            purpose="nav_slot_extract_v1",
            model=model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            temperature=float(config.llm_temperature),
            max_tokens=max(256, int(config.llm_max_tokens or 256)),
            response_format={"type": "json_object"},
        )
        record_usage("nav_verify", cached.get("usage"))
        raw = str(cached.get("content") or "").strip()
        obj = json.loads(raw) if raw.startswith("{") else {}
        slots_obj = obj.get("slots") if isinstance(obj, dict) else None
        if not isinstance(slots_obj, dict):
            return {}
        out: Dict[str, str] = {}
        for name in slots:
            val = str(slots_obj.get(name) or "").strip()
            if val:
                out[name] = val
        return out
    except Exception:
        return {}


def extract_slots(
    subgoal: Subgoal,
    evidence_text: str,
    config: NavConfig,
    *,
    retrieval_query: str = "",
    use_llm: bool = True,
) -> Tuple[Dict[str, str], float]:
    """LLM extract when enabled; always fall back to heuristic. confidence in [0,1]."""
    heuristic = extract_slots_heuristic(
        subgoal, evidence_text, retrieval_query=retrieval_query
    )
    llm_slots: Dict[str, str] = {}
    if use_llm and bool(getattr(config, "enable_contract_verify", False)):
        llm_slots = extract_slots_llm(
            subgoal, evidence_text, config, retrieval_query=retrieval_query
        )
    merged = dict(heuristic)
    merged.update(llm_slots)
    needed = [str(s).strip() for s in (subgoal.produces or []) if str(s).strip()]
    if not needed:
        conf = 1.0 if (evidence_text or "").strip() else 0.0
        return merged, conf
    filled = sum(1 for s in needed if (merged.get(s) or "").strip())
    return merged, float(filled) / float(len(needed))


def verify_contract(
    subgoal: Subgoal,
    *,
    extracted: Dict[str, str],
    evidence_text: str,
    confidence: float,
) -> VerifyOutcome:
    """Mechanical zero-cost signal: is there evidence, and are declared slots bound?

    It deliberately does NOT judge whether the need is answered — contract kind,
    cardinality and must_mention are conclusions, and ``plan_control`` is the
    single authority that reconciles evidence against the coverage checklist.
    """
    chars = evidence_chars(evidence_text)
    needed = [str(s).strip() for s in (subgoal.produces or []) if str(s).strip()]
    missing = [s for s in needed if not str(extracted.get(s) or "").strip()]

    base = SubgoalResult(
        subgoal_id=subgoal.id,
        satisfied=False,
        confidence=float(confidence),
        extracted=dict(extracted),
        chars_used=chars,
        gap="",
        verdict="",
    )

    if chars <= 0:
        base.gap = "empty_evidence"
        base.verdict = "RETRY_SAME_REGION"
        return VerifyOutcome(verdict="RETRY_SAME_REGION", result=base, gap=base.gap)

    if missing:
        base.gap = "missing_slots:" + ",".join(missing)
        base.verdict = "REBIND" if needed else "RETRY_SAME_REGION"
        return VerifyOutcome(verdict=base.verdict, result=base, gap=base.gap)  # type: ignore[arg-type]

    base.satisfied = True
    base.verdict = "SATISFIED"
    base.gap = ""
    return VerifyOutcome(verdict="SATISFIED", result=base, gap="")


def activation_when_holds(
    when: str,
    *,
    parent_extracted: Dict[str, str],
    parent_satisfied: bool,
    config: Optional[NavConfig] = None,
    use_llm: bool = False,
) -> bool:
    """Evaluate a conditional activation predicate.

    Empty ``when`` ⇒ activate whenever the parent is satisfied.
    Non-empty: prefer full slot-value substring match; optional LLM. No token-bag overlap.
    """
    if not parent_satisfied:
        return False
    pred = (when or "").strip()
    if not pred:
        return True

    values = [str(v).strip() for v in (parent_extracted or {}).values() if str(v).strip()]
    for val in values:
        if val in pred or pred in val:
            return True

    if not use_llm or config is None:
        return False
    if not bool(getattr(config, "enable_contract_verify", False)):
        return False
    try:
        from agent_delivery.code.llm_api_cache import cached_chat_completion  # type: ignore
        from agent_delivery.code.llm_config import make_openai_client, require_llm_env  # type: ignore
        from agent_delivery.code.llm_usage import record_usage  # type: ignore
        from nav_token_budget import nav_token_budget_exhausted
    except Exception:
        return False
    if nav_token_budget_exhausted():
        return False
    require_llm_env(context="Nav Activation When")
    key = (
        os.environ.get("NAV_PLANNER_API_KEY", "").strip()
        or os.environ.get("DS_KEY", "").strip()
        or os.environ.get("OPENAI_API_KEY", "").strip()
    )
    model = (
        os.environ.get(config.planner_model_env, "").strip()
        or os.environ.get(config.llm_model_env, "").strip()
        or os.environ.get("COMPOSE_MODEL", "").strip()
        or "gpt-4o-mini"
    )
    base = (
        os.environ.get("NAV_PLANNER_BASE_URL", "").strip()
        or os.environ.get("DS_URL", "").strip()
        or os.environ.get("OPENAI_BASE_URL", "").strip()
        or None
    )
    client = make_openai_client(api_key=key, base_url=base)
    try:
        cached = cached_chat_completion(
            client,
            purpose="nav_activation_when_v1",
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Decide if a conditional retrieval branch should run.\n"
                        'Return ONLY JSON: {"activate": true|false, "reason": "..."}.'
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Condition: {pred}\n"
                        f"Parent extracted slots: "
                        f"{json.dumps(parent_extracted, ensure_ascii=False)}\n"
                    ),
                },
            ],
            temperature=0.0,
            max_tokens=128,
            response_format={"type": "json_object"},
        )
        record_usage("nav_verify", cached.get("usage"))
        obj = json.loads(str(cached.get("content") or "").strip() or "{}")
        return bool(obj.get("activate"))
    except Exception:
        return False


def apply_bindings_from_result(
    bindings: Dict[str, str],
    subgoal: Subgoal,
    extracted: Dict[str, str],
) -> Dict[str, str]:
    """Write short and qualified ``s1.slot`` keys into bindings."""
    out = dict(bindings or {})
    for slot, value in (extracted or {}).items():
        name = str(slot).strip()
        val = str(value or "").strip()
        if not name or not val:
            continue
        out[name] = val
        out[f"{subgoal.id}.{name}"] = val
    return out


def build_evidence_text_from_chunks(chunks: Any, *, limit: int = 8000) -> str:
    """Concatenate (chunk, score) texts up to a char budget."""
    parts: List[str] = []
    total = 0
    for chunk, _score in list(chunks or []):
        text = str(getattr(chunk, "text", "") or getattr(chunk, "content", "") or "")
        if not text.strip():
            continue
        if total >= limit:
            break
        take = text[: max(0, limit - total)]
        parts.append(take)
        total += len(take)
    return "\n".join(parts)
