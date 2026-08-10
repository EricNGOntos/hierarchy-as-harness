"""Episode LLM token hard stop (fusion plan §3.6).

One counter, one rule: if cumulative LLM ``total_tokens`` reaches
``RETRIEVAL_NAV_TOKEN_LIMIT``, do not start another nav LLM call; keep
already-collected evidence and return upward (FINISH / done / fallback).

Inside ``nav_token_episode()`` the counter is per-episode (contextvars).
Outside it, usage falls back to the process-global ``llm_usage`` snapshot
so bin scripts that only ``reset_usage()`` keep working.
"""

from __future__ import annotations

import os
from contextlib import contextmanager
from contextvars import ContextVar
from typing import Any, Dict, Iterator, List, Optional

# Plan default for RETRIEVAL_NAV_TOKEN_LIMIT (env name is the source of truth).
_ENV_TOKEN_LIMIT = "RETRIEVAL_NAV_TOKEN_LIMIT"
_DEFAULT_TOKEN_LIMIT = 100_000

# Mutable one-element list so callers can increment without rebinding ContextVar.
_EpisodeCounter = List[int]
_episode_tokens: ContextVar[Optional[_EpisodeCounter]] = ContextVar(
    "nav_episode_tokens", default=None
)


class NavTokenLimit(Exception):
    """Raised when the episode (or process) LLM token budget is exhausted."""

    def __init__(self, used: int = 0, limit: int = 0) -> None:
        self.used = int(used)
        self.limit = int(limit)
        super().__init__(
            f"nav token limit exhausted: used={self.used} limit={self.limit}"
        )


def nav_token_limit() -> int:
    """Always a positive limit: unset / invalid / non-positive fall back to the default."""
    try:
        limit = int(os.environ.get(_ENV_TOKEN_LIMIT, "").strip())
    except ValueError:
        limit = 0
    return limit if limit > 0 else _DEFAULT_TOKEN_LIMIT


def _process_tokens_used() -> int:
    from agent_delivery.code.llm_usage import snapshot_usage  # type: ignore

    total = 0
    for block in snapshot_usage().values():
        total += int(block.get("total_tokens", 0) or 0)
    return total


def nav_tokens_used() -> int:
    ep = _episode_tokens.get()
    if ep is not None:
        return int(ep[0])
    return _process_tokens_used()


def nav_token_budget_exhausted() -> bool:
    return nav_tokens_used() >= nav_token_limit()


def record_episode_tokens(usage: Optional[Dict[str, Any]]) -> None:
    """Add one call's ``total_tokens`` to the active episode counter (no-op outside)."""
    ep = _episode_tokens.get()
    if ep is None:
        return
    try:
        add = int((usage or {}).get("total_tokens", 0) or 0)
    except (TypeError, ValueError):
        add = 0
    if add > 0:
        ep[0] += add


@contextmanager
def nav_token_episode() -> Iterator[None]:
    """Bind a fresh per-episode token counter for the duration of the block."""
    token = _episode_tokens.set([0])
    try:
        yield
    finally:
        _episode_tokens.reset(token)
