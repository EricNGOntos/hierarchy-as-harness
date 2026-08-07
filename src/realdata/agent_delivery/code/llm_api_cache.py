from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from pathlib import Path
from threading import Lock
from typing import Any, Dict, Optional, Sequence

from .llm_config import load_llm_env

_LOCK = Lock()
_CACHE: dict[str, dict[str, Any]] | None = None


def _append_audit_event(event: Dict[str, Any]) -> None:
    raw = os.environ.get("BODYRICH_LLM_API_AUDIT_PATH", "").strip()
    if not raw:
        return
    path = Path(raw)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"recorded_at": time.time(), **event}
    with _LOCK:
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n")
            handle.flush()
            os.fsync(handle.fileno())


def _cache_enabled() -> bool:
    raw = os.environ.get("BODYRICH_LLM_API_CACHE", "1").strip().lower()
    return raw not in {"0", "false", "no", "off"}


def _cache_path() -> Path:
    raw = os.environ.get("BODYRICH_LLM_API_CACHE_PATH", "").strip()
    return Path(raw) if raw else Path("cache") / "llm_api_cache.jsonl"


def _load_cache() -> dict[str, dict[str, Any]]:
    global _CACHE
    if _CACHE is not None:
        return _CACHE
    path = _cache_path()
    cache: dict[str, dict[str, Any]] = {}
    if path.exists():
        try:
            with path.open("r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    row = json.loads(line)
                    key = str(row.get("key") or "")
                    if key and "content" in row:
                        cache[key] = row
        except Exception as exc:
            print(f"[llm-cache] ignoring unreadable cache {path}: {exc}", file=sys.stderr, flush=True)
    _CACHE = cache
    return cache


def _key(
    *,
    purpose: str,
    model: str,
    messages: Sequence[Dict[str, str]],
    temperature: Any,
    max_tokens: Any,
    response_format: Optional[Dict[str, Any]],
    extra: Optional[Dict[str, Any]],
) -> str:
    payload = {
        "purpose": purpose,
        "model": model,
        "messages": list(messages),
        "temperature": temperature,
        "max_tokens": max_tokens,
        "response_format": response_format,
        "base_url": os.environ.get("OPENAI_BASE_URL", "").strip(),
        "extra": extra or {},
        "cache_version": "bodyrich-chat-v1",
    }
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _usage_dict(usage: Any) -> Dict[str, int]:
    if isinstance(usage, dict):
        prompt = int(usage.get("prompt_tokens", 0) or 0)
        completion = int(usage.get("completion_tokens", 0) or 0)
        total = int(usage.get("total_tokens", 0) or (prompt + completion))
    else:
        prompt = int(getattr(usage, "prompt_tokens", 0) or 0) if usage is not None else 0
        completion = int(getattr(usage, "completion_tokens", 0) or 0) if usage is not None else 0
        total = int(getattr(usage, "total_tokens", 0) or (prompt + completion)) if usage is not None else prompt + completion
    return {"prompt_tokens": prompt, "completion_tokens": completion, "total_tokens": total}


def cached_chat_completion(
    client: Any,
    *,
    purpose: str,
    model: str,
    messages: Sequence[Dict[str, str]],
    temperature: Any = 0.0,
    max_tokens: Any = None,
    response_format: Optional[Dict[str, Any]] = None,
    extra: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    call_t0 = time.perf_counter()
    load_llm_env()
    cache_key = _key(
        purpose=purpose,
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        response_format=response_format,
        extra=extra,
    )
    if _cache_enabled():
        with _LOCK:
            row = _load_cache().get(cache_key)
        if row is not None:
            print(f"[llm-cache] hit purpose={purpose} model={model}", file=sys.stderr, flush=True)
            usage = {
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "total_tokens": 0,
                "cache_hit": True,
                "retry_wait_seconds": 0.0,
            }
            _append_audit_event({
                "run_id": os.environ.get("BODYRICH_LLM_API_AUDIT_RUN_ID", ""),
                "key": cache_key,
                "purpose": purpose,
                "model": model,
                "cache_hit": True,
                "original_usage": _usage_dict(row.get("usage") or {}),
                "billed_usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
                "elapsed_seconds": time.perf_counter() - call_t0,
            })
            return {
                "content": str(row.get("content") or ""),
                "reasoning_content": str(row.get("reasoning_content") or ""),
                "usage": usage,
                "cache_hit": True,
            }

    kwargs: Dict[str, Any] = {
        "model": model,
        "messages": list(messages),
        "temperature": temperature,
    }
    if max_tokens is not None:
        kwargs["max_tokens"] = max_tokens
    if response_format is not None:
        kwargs["response_format"] = response_format
    if extra:
        # Keys starting with "_" are cache-only metadata (e.g. _thinking_mode).
        kwargs.update(
            {k: v for k, v in extra.items() if not str(k).startswith("_")}
        )
    max_retries = max(1, int(os.environ.get("BODYRICH_LLM_API_MAX_RETRIES", "6").strip() or "6"))
    base_sleep = max(0.0, float(os.environ.get("BODYRICH_LLM_API_RETRY_BASE_SECONDS", "0.8").strip() or "0.8"))
    last_error: Exception | None = None
    retry_wait_seconds = 0.0
    for attempt in range(max_retries):
        try:
            rsp = client.chat.completions.create(**kwargs)
            break
        except Exception as exc:
            last_error = exc
            if attempt + 1 >= max_retries:
                raise
            sleep_s = min(20.0, base_sleep * (2 ** attempt))
            print(
                f"[llm-cache] api retry {attempt + 1}/{max_retries} "
                f"purpose={purpose} model={model}: {exc}",
                file=sys.stderr,
                flush=True,
            )
            retry_wait_seconds += sleep_s
            time.sleep(sleep_s)
    else:  # pragma: no cover - loop always breaks or raises.
        raise RuntimeError(f"LLM API failed without response: {last_error}")
    content = (rsp.choices[0].message.content or "").strip()
    reasoning = ""
    msg = rsp.choices[0].message
    for attr in ("reasoning_content", "reasoning"):
        val = getattr(msg, attr, None)
        if val:
            reasoning = str(val).strip()
            break
    if not reasoning and isinstance(getattr(msg, "model_extra", None), dict):
        reasoning = str(
            msg.model_extra.get("reasoning_content")
            or msg.model_extra.get("reasoning")
            or ""
        ).strip()
    usage = _usage_dict(getattr(rsp, "usage", None))
    # Some gateways report reasoning tokens separately.
    raw_usage = getattr(rsp, "usage", None)
    if raw_usage is not None:
        for attr in ("reasoning_tokens", "completion_tokens_details"):
            val = getattr(raw_usage, attr, None)
            if attr == "reasoning_tokens" and val is not None:
                usage["reasoning_tokens"] = int(val or 0)
            if attr == "completion_tokens_details" and val is not None:
                rt = getattr(val, "reasoning_tokens", None)
                if rt is None and isinstance(val, dict):
                    rt = val.get("reasoning_tokens")
                if rt is not None:
                    usage["reasoning_tokens"] = int(rt or 0)
    usage["retry_wait_seconds"] = retry_wait_seconds
    if _cache_enabled():
        path = _cache_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        row = {
            "key": cache_key,
            "created_at": time.time(),
            "purpose": purpose,
            "model": model,
            "content": content,
            "reasoning_content": reasoning,
            "usage": usage,
        }
        with _LOCK:
            with path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
                f.flush()
                os.fsync(f.fileno())
            _load_cache()[cache_key] = row
        print(f"[llm-cache] saved purpose={purpose} model={model}", file=sys.stderr, flush=True)
    _append_audit_event({
        "run_id": os.environ.get("BODYRICH_LLM_API_AUDIT_RUN_ID", ""),
        "key": cache_key,
        "purpose": purpose,
        "model": model,
        "cache_hit": False,
        "original_usage": _usage_dict(usage),
        "billed_usage": _usage_dict(usage),
        "retry_wait_seconds": retry_wait_seconds,
        "elapsed_seconds": time.perf_counter() - call_t0,
        "has_reasoning": bool(reasoning),
    })
    return {
        "content": content,
        "reasoning_content": reasoning,
        "usage": usage,
        "cache_hit": False,
    }
