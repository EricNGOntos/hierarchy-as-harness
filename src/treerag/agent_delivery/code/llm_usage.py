from __future__ import annotations

from collections import defaultdict
from typing import Any, Dict


_USAGE: dict[str, dict[str, float]] = defaultdict(
    lambda: {
        "prompt_tokens": 0,
        "completion_tokens": 0,
        "total_tokens": 0,
        "api_calls": 0,
        "cache_hits": 0,
        "retry_wait_seconds": 0.0,
    }
)


def record_usage(purpose: str, usage: Any) -> None:
    block = _USAGE[str(purpose or "unknown")]
    if isinstance(usage, dict):
        prompt_tokens = int(usage.get("prompt_tokens", 0) or 0)
        completion_tokens = int(usage.get("completion_tokens", 0) or 0)
        total_tokens = int(usage.get("total_tokens", 0) or 0) or prompt_tokens + completion_tokens
        cache_hit = bool(usage.get("cache_hit"))
        retry_wait_seconds = float(usage.get("retry_wait_seconds", 0.0) or 0.0)
    else:
        prompt_tokens = int(getattr(usage, "prompt_tokens", 0) or 0) if usage is not None else 0
        completion_tokens = int(getattr(usage, "completion_tokens", 0) or 0) if usage is not None else 0
        total_tokens = int(getattr(usage, "total_tokens", 0) or 0) if usage is not None else prompt_tokens + completion_tokens
        cache_hit = False
        retry_wait_seconds = 0.0
    block["prompt_tokens"] += prompt_tokens
    block["completion_tokens"] += completion_tokens
    block["total_tokens"] += total_tokens
    if cache_hit:
        block["cache_hits"] += 1
    else:
        block["api_calls"] += 1
    block["retry_wait_seconds"] += retry_wait_seconds


def snapshot_usage() -> Dict[str, Dict[str, float]]:
    return {purpose: dict(values) for purpose, values in sorted(_USAGE.items())}


def reset_usage() -> None:
    _USAGE.clear()
