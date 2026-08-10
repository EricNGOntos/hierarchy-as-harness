"""Episode LLM token hard stop (fusion plan §3.6).

One counter, one rule: if cumulative LLM ``total_tokens`` reaches
``RETRIEVAL_NAV_TOKEN_LIMIT``, do not start another nav LLM call; keep
already-collected evidence and return upward (FINISH / done / fallback).
"""

from __future__ import annotations

import os

# Plan default for RETRIEVAL_NAV_TOKEN_LIMIT (env name is the source of truth).
_ENV_TOKEN_LIMIT = "RETRIEVAL_NAV_TOKEN_LIMIT"
_DEFAULT_TOKEN_LIMIT = 100_000


def nav_token_limit() -> int:
    raw = os.environ.get(_ENV_TOKEN_LIMIT, "").strip()
    if not raw:
        return _DEFAULT_TOKEN_LIMIT
    try:
        return max(0, int(raw))
    except ValueError:
        return _DEFAULT_TOKEN_LIMIT


def nav_tokens_used() -> int:
    from agent_delivery.code.llm_usage import snapshot_usage  # type: ignore

    total = 0
    for block in snapshot_usage().values():
        total += int(block.get("total_tokens", 0) or 0)
    return total


def nav_token_budget_exhausted() -> bool:
    limit = nav_token_limit()
    if limit <= 0:
        return False
    return nav_tokens_used() >= limit
