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
    action_block = "\n".join(f"- {a.prompt_line()}" for a in actions)
    history = "\n".join(
        f"- step={h.get('step_idx')} action={h.get('action_id')} kind={h.get('kind')} section={h.get('section_id')}"
        for h in state.action_history[-6:]
    )
    system = (
        "You are a constrained document navigation policy. "
        "Return one JSON object only. You must choose exactly one action_id from the legal action list. "
        "Do not invent paths, tools, or action ids. Keep reason under 12 words."
    )
    user = (
        f"query: {state.query}\n"
        f"task_type: {state.task_type}\n"
        f"current_scope: {state.current_scope or '<document-root>'}\n"
        f"recent_history:\n{history or '(none)'}\n\n"
        f"section_projection:\n{projection.text}\n\n"
        f"legal_actions:\n{action_block}\n\n"
        'Return: {"action_id":"C1","reason":"short reason"}'
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
            for action in actions:
                if action.action_id.upper() == aid:
                    return action, {
                        "model": model,
                        "reason": str(obj.get("reason") or "")[:300],
                        "raw": text[:500],
                    }
            raise RuntimeError(
                "Nav Agent LLM 返回了非法 action_id="
                f"{aid!r}；合法选项={[a.action_id for a in actions]!r}；raw={text[:500]!r}"
            )
        except RuntimeError:
            raise
        except Exception as exc:
            last_error = exc
            time.sleep(min(2.0, 0.4 * (attempt + 1)))
    raise RuntimeError(
        f"Nav Agent LLM 调用失败（model={model!r}，step={step_idx}）：{last_error}"
    )
