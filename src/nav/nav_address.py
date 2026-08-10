"""Production address model for MAP-NAV.

Levels match Knowhere's real keys (see ``document.py``):

- ``NAMESPACE`` — ``(user_id, namespace)`` scope. Not a row; represented as
  empty ``scope`` / empty node id, never a synthetic ``__corpus__:__root``.
- ``DOCUMENT`` — ``Document.document_id``
- ``SECTION`` — ``DocumentSection.section_id``
- ``CHUNK`` — ``DocumentChunk.chunk_id``

Hierarchy comes from the provider's level registry and ``parent_section_id``,
not from parsing magic suffixes out of a string id.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional


class NavLevel(str, Enum):
    NAMESPACE = "namespace"
    DOCUMENT = "document"
    SECTION = "section"
    CHUNK = "chunk"


@dataclass(frozen=True)
class NavAddress:
    level: NavLevel
    id: str = ""

    def __post_init__(self) -> None:
        object.__setattr__(self, "id", str(self.id or "").strip())


def namespace_root() -> NavAddress:
    """Scope handle for a namespace root (not a navigable row)."""
    return NavAddress(NavLevel.NAMESPACE, "")


def is_dispatch_only_level(level: Optional[NavLevel]) -> bool:
    """Document (and namespace) nodes may be entered, not collected as leaves."""
    return level in (NavLevel.NAMESPACE, NavLevel.DOCUMENT)


def _coerce_level(level: Any) -> Optional[NavLevel]:
    if isinstance(level, NavLevel):
        return level
    if isinstance(level, str):
        try:
            return NavLevel(level)
        except ValueError:
            return None
    return None


def _coerce_doc_id(value: Any) -> str:
    if isinstance(value, str):
        return value.strip()
    return ""


def address_level(ts: Any, node_id: str) -> Optional[NavLevel]:
    """Read level from the toolspace/provider registry when available."""
    sid = str(node_id or "").strip()
    if not sid:
        return NavLevel.NAMESPACE
    fn = getattr(ts, "address_level", None)
    if callable(fn):
        level = _coerce_level(fn(sid))
        if level is not None:
            return level
    provider = getattr(ts, "_provider", None)
    fn = getattr(provider, "address_level", None)
    if callable(fn):
        return _coerce_level(fn(sid))
    return None


def is_dispatch_only_node(ts: Any, node_id: str) -> bool:
    """True when the node is document/namespace scoped (DISPATCH only)."""
    level = address_level(ts, node_id)
    if level is not None:
        return is_dispatch_only_level(level)
    # Legacy ToolSpace still uses synthetic suffix ids until that path is retired.
    try:
        from agent_delivery.code.tool_space import is_synthetic_dispatch_only
    except Exception:  # pragma: no cover
        return False
    return bool(is_synthetic_dispatch_only(node_id))


def owner_document(ts: Any, node_id: str, fallback: str = "") -> str:
    """Owning ``document_id`` for a node, without parsing id strings."""
    sid = str(node_id or "").strip()
    fb = str(fallback or "").strip()
    if not sid:
        return fb

    fn = getattr(ts, "owner_document", None)
    if callable(fn):
        got = _coerce_doc_id(fn(sid))
        if got:
            return got

    provider = getattr(ts, "_provider", None)
    fn = getattr(provider, "owner_document", None)
    if callable(fn):
        got = _coerce_doc_id(fn(sid))
        if got:
            return got

    synth = getattr(ts, "_synthetic_doc_id", None)
    if callable(synth):
        got = _coerce_doc_id(synth(sid))
        if got:
            return got

    idx = getattr(ts, "_idx", None)
    if idx is not None:
        loc = getattr(idx, "_node_to_doc_line", {}).get(sid)
        if loc:
            return str(loc[0])

    return fb


def uses_document_nodes(ts: Any) -> bool:
    """True when document ids themselves are map nodes (namespace provider).

    Checks the provider class (not a duck-typed instance attribute) so adapters
    and test mocks do not look like namespace mode by accident.
    """
    provider = getattr(ts, "_provider", None)
    target = provider if provider is not None else ts
    return callable(getattr(type(target), "document_ids", None))
