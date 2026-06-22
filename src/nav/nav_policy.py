from __future__ import annotations

import json
import os
import re
import time
from typing import Any, List, Optional

from nav_types import ActionKind, LegalAction, NavConfig, NavState, Projection


def choose_rule_action(
    state: NavState,
    projection: Projection,
    actions: List[LegalAction],
    *,
    step_idx: int,
    config: NavConfig,
) -> LegalAction:
    """Deterministic fallback policy used for cheap debugging and invalid LLM actions."""
    def first(kind: ActionKind) -> Optional[LegalAction]:
        for a in actions:
            if a.kind == kind:
                return a
        return None

    task_type = (state.task_type or "").lower()
    if not state.collected:
        if task_type in ("scope_collection", "regulatory_coverage"):
            act = first(ActionKind.EXPAND) or first(ActionKind.COLLECT)
            if act:
                return act
        act = first(ActionKind.SEARCH) or first(ActionKind.COLLECT)
        if act:
            return act

    if task_type in ("scope_collection", "regulatory_coverage"):
        act = first(ActionKind.COLLECT)
        if act:
            return act
        act = first(ActionKind.BACK)
        if act:
            return act

    if len(state.collected) < 3:
        act = first(ActionKind.COLLECT) or first(ActionKind.SEARCH)
        if act:
            return act

    return first(ActionKind.FINISH) or actions[-1]


def _extract_json_obj(text: str) -> Optional[dict]:
    s = (text or "").strip().replace("```json", "").replace("```", "")
    if not s:
        return None
    if s.startswith("{") and s.endswith("}"):
        try:
            obj = json.loads(s)
            return obj if isinstance(obj, dict) else None
        except Exception:
            pass
    m = re.search(r"\{.*?\}", s, flags=re.S)
    if not m:
        return None
    try:
        obj = json.loads(m.group(0))
        return obj if isinstance(obj, dict) else None
    except Exception:
        return None


def _extract_action_id_fallback(text: str) -> str:
    """Recover action_id from a truncated JSON object; still validated against legal actions."""
    s = (text or "").strip()
    for key in ("action_id", "id"):
        m = re.search(rf'"{key}"\s*:\s*"([^"]+)"', s, flags=re.I)
        if m:
            return str(m.group(1) or "").strip().upper()
    return ""


def _compatible_discovery_action_id(aid: str, actions: List[LegalAction]) -> str:
    """Map habitual Cn collect IDs to Dn when only discovery collect choices exist."""
    normalized = (aid or "").strip().upper()
    m = re.fullmatch(r"C(\d+)", normalized)
    if not m:
        return normalized
    wanted = f"D{m.group(1)}"
    legal = {a.action_id.upper() for a in actions}
    if normalized not in legal and wanted in legal:
        return wanted
    return normalized


def _format_agent_state(state: NavState, step_idx: int, config: NavConfig) -> str:
    """Agent state block so the nav LLM knows what was already collected."""
    lines = ["=== Agent State ==="]
    lines.append(f"Current scope: {state.current_scope or 'document-root'}")
    lines.append(f"Step: {step_idx + 1} / {config.max_steps}")

    collected_sections: List[str] = []
    explored_empty: List[str] = []
    seen: set[str] = set()
    for h in state.action_history:
        sid = str(h.get("section_id") or "").strip()
        if not sid or sid in seen:
            continue
        seen.add(sid)
        if h.get("kind") == "collect" and int(h.get("n_added", 0) or 0) > 0:
            collected_sections.append(sid)
        elif h.get("kind") == "collect" and int(h.get("n_added", 0) or 0) == 0:
            explored_empty.append(sid)

    if collected_sections:
        lines.append(f"Evidence collected: {len(collected_sections)} section(s)")
        for sid in collected_sections:
            lines.append(f'  - "{sid}"')
    else:
        lines.append("Evidence collected: none")

    if explored_empty:
        lines.append(f"Already explored (no new evidence): {len(explored_empty)} section(s)")
        for sid in explored_empty[:5]:
            lines.append(f'  - "{sid}"')

    remaining = config.max_steps - step_idx - 1
    if remaining <= 2:
        lines.append(
            f"Only {remaining} step(s) remaining. Consider FINISH if evidence is sufficient."
        )

    lines.append("=== End Agent State ===")
    return "\n".join(lines)


def choose_llm_action(
    state: NavState,
    projection: Projection,
    actions: List[LegalAction],
    *,
    step_idx: int,
    config: NavConfig,
) -> tuple[LegalAction, dict]:
    from agent_delivery.code.llm_config import make_openai_client, require_llm_env  # type: ignore
    from agent_delivery.code.llm_api_cache import cached_chat_completion  # type: ignore
    from agent_delivery.code.llm_usage import record_usage  # type: ignore

    require_llm_env(context="Nav Agent")
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    model = os.environ.get(config.llm_model_env, "").strip() or os.environ.get("COMPOSE_MODEL", "gpt-4o-mini")
    base_url = os.environ.get("OPENAI_BASE_URL", "").strip() or None
    client = make_openai_client(api_key=key, base_url=base_url)
    agent_state = _format_agent_state(state, step_idx, config)
    action_block = "\n".join(f"- {a.prompt_line()}" for a in actions)

    system = (
        "You are a document navigation agent running an observe-act loop.\n\n"
        "Each step chooses exactly ONE action_id from the legal action list.\n\n"
        "Action semantics:\n"
        "  - C* (COLLECT): adds a section and all descendant content to evidence.\n"
        "  - E* (EXPAND): opens a section to see its children in the next step.\n"
        "  - D* (DISCOVERY COLLECT): collects a section found by bottom-up search.\n"
        "  - S* (SEARCH): keyword search within the document.\n"
        "  - B* (BACK): return to parent scope.\n"
        "  - F* (FINISH): end navigation for this document.\n\n"
        "Rules:\n"
        "  - Do NOT re-collect a section already listed in 'Evidence collected'.\n"
        "  - Do NOT re-explore a section listed in 'Already explored'.\n"
        "  - For [Leaf] sections, prefer COLLECT over EXPAND.\n"
        "  - If evidence is sufficient for the query, choose FINISH.\n"
        "  - When steps remaining <= 2, prioritize COLLECT or FINISH.\n"
        "  - Do not invent action IDs. Use only IDs from the legal action list.\n\n"
        'Return ONLY one JSON object: {"action_id":"C1","reason":"short reason"}\n'
        "Keep reason under 15 words. Reason must be in English."
    )
    user = (
        f"User query: {state.query}\n"
        f"Task type: {state.task_type}\n\n"
        f"{agent_state}\n\n"
        f"=== Actionable Observation ===\n"
        f"{projection.text}\n"
        f"=== End Actionable Observation ===\n\n"
        f"Legal actions:\n{action_block}\n\n"
        'Return: {"action_id":"...","reason":"..."}'
    )

    last_error: Optional[Exception] = None
    for attempt in range(3):
        try:
            cached = cached_chat_completion(
                client,
                purpose="nav_action_v2",
                model=model,
                messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
                temperature=float(config.llm_temperature),
                max_tokens=int(config.llm_max_tokens),
                response_format={"type": "json_object"},
            )
            record_usage("nav", cached.get("usage"))
            text = str(cached.get("content") or "").strip()
            obj = _extract_json_obj(text) or {}
            aid = str(obj.get("action_id") or obj.get("id") or "").strip().upper()
            if not aid:
                aid = _extract_action_id_fallback(text)
            aid = _compatible_discovery_action_id(aid, actions)
            for action in actions:
                if action.action_id.upper() == aid:
                    return action, {
                        "model": model,
                        "reason": str(obj.get("reason") or "")[:300],
                        "raw": text[:500],
                    }
            last_error = RuntimeError(
                "Nav Agent LLM 返回了非法 action_id="
                f"{aid!r}；合法选项={[a.action_id for a in actions]!r}；raw={text[:500]!r}"
            )
            if attempt < 2:
                time.sleep(min(2.0, 0.4 * (attempt + 1)))
                continue
            fallback = choose_rule_action(
                state, projection, actions, step_idx=step_idx, config=config
            )
            return fallback, {
                "model": model,
                "reason": "rule_fallback_illegal_action",
                "raw": text[:500],
                "illegal_action_id": aid,
                "fallback_action_id": fallback.action_id,
            }
        except RuntimeError as exc:
            last_error = exc
            if attempt < 2:
                time.sleep(min(2.0, 0.4 * (attempt + 1)))
                continue
            raise
        except Exception as exc:
            last_error = exc
            time.sleep(min(2.0, 0.4 * (attempt + 1)))
    raise RuntimeError(
        f"Nav Agent LLM 调用失败（model={model!r}，step={step_idx}）：{last_error}"
    )
