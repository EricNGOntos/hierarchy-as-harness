"""Asset SEARCH channel aligned with Knowhere chunk_type filtering.

Harvest may request ``search_assets`` so evidence can be image/table-only.
Candidates are units under a scope whose ``chunk_type`` matches Knowhere's
``image`` / ``table`` vocabulary — same filter as production
``asset_filter_step``, without the VLM/S3 inspector (wired at Knowhere route).
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

from nav_address import owner_document

# Knowhere DocumentChunk.chunk_type values + harvest JSON kind aliases.
_KIND_TO_CHUNK_TYPE = {
    "image": "image",
    "images": "image",
    "table": "table",
    "tables": "table",
}


def asset_chunk_type(kind: str) -> Optional[str]:
    """Map harvest ``kind`` to Knowhere ``chunk_type``, or None if unknown."""
    return _KIND_TO_CHUNK_TYPE.get(str(kind or "").strip().lower())


def parse_search_assets(raw: Any) -> List[Dict[str, str]]:
    """Normalize harvest ``search_assets`` entries to ``{kind,query,scope,asset_type}``."""
    if not isinstance(raw, list):
        return []
    out: List[Dict[str, str]] = []
    for item in raw:
        if not isinstance(item, dict):
            continue
        kind = str(item.get("kind") or "").strip()
        asset_type = asset_chunk_type(kind)
        if not asset_type:
            continue
        query = str(item.get("query") or "").strip()
        scope = str(item.get("scope") or "").strip()
        out.append(
            {
                "kind": kind,
                "query": query,
                "scope": scope,
                "asset_type": asset_type,
            }
        )
    return out


def _provider(ts: Any) -> Any:
    return getattr(ts, "_provider", None)


def _section_ids_under_scope(ts: Any, scope: Optional[str], doc_id: str) -> List[str]:
    """Section ids in ``scope`` subtree (or document/corpus roots when empty)."""
    sid = str(scope or "").strip()
    provider = _provider(ts)
    if sid:
        relations = getattr(ts, "section_relation_ids", None)
        if callable(relations):
            _anc, descendants = relations(sid, doc_id)
            out = [sid]
            out.extend(str(x) for x in (descendants or ()) if str(x).strip())
            return list(dict.fromkeys(out))
        if provider is not None and callable(getattr(provider, "relations", None)):
            _anc, descendants = provider.relations(sid)
            out = [sid]
            out.extend(str(x) for x in (descendants or ()) if str(x).strip())
            return list(dict.fromkeys(out))
        return [sid]

    roots_fn = getattr(ts, "sections_for_doc", None)
    if callable(roots_fn):
        roots = [str(x) for x in (roots_fn(doc_id) or ()) if str(x).strip()]
        if roots:
            out: List[str] = []
            for root in roots:
                out.extend(_section_ids_under_scope(ts, root, doc_id or owner_document(ts, root, "")))
            return list(dict.fromkeys(out))
    if provider is not None and callable(getattr(provider, "all_section_ids", None)):
        return [str(x) for x in provider.all_section_ids() if str(x).strip()]
    return []


def gather_scoped_asset_chunks(
    ts: Any,
    *,
    asset_type: str,
    scope: Optional[str],
    doc_id: str = "",
) -> List[Any]:
    """Units under scope with ``chunk_type == asset_type``, as ToolSpace Chunks."""
    from agent_delivery.code.index_retrieval import Chunk  # type: ignore

    wanted = str(asset_type or "").strip().lower()
    if wanted not in {"image", "table"}:
        return []

    provider = _provider(ts)
    self_units = getattr(provider, "self_units", None) if provider is not None else None
    unit_text = getattr(provider, "unit_text", None) if provider is not None else None
    if not callable(self_units) or not callable(unit_text):
        return []

    resolved_doc = str(doc_id or "").strip()
    section_ids = _section_ids_under_scope(ts, scope, resolved_doc)
    out: List[Any] = []
    seen: Set[str] = set()
    for section_id in section_ids:
        owner = owner_document(ts, section_id, resolved_doc)
        for unit in self_units(section_id) or ():
            if str(getattr(unit, "chunk_type", "") or "").strip().lower() != wanted:
                continue
            chunk_id = str(getattr(unit, "chunk_id", "") or "").strip()
            if not chunk_id or chunk_id in seen:
                continue
            text = str(unit_text(unit) or "").strip()
            if not text:
                continue
            seen.add(chunk_id)
            out.append(
                Chunk(
                    node_id=chunk_id,
                    doc_id=owner or resolved_doc,
                    text=text,
                    line_ids=(int(getattr(unit, "sort_order", 0) or 0),),
                    section_id=str(getattr(unit, "section_id", "") or section_id),
                )
            )
    out.sort(key=lambda c: (min(c.line_ids or (0,)), c.node_id))
    return out


def apply_search_assets(
    ts: Any,
    state: Any,
    config: Any,
    *,
    requests: Sequence[Dict[str, str]],
    default_scope: Optional[str],
) -> Tuple[int, List[Dict[str, Any]]]:
    """Add type-filtered asset chunks to ``state.collected``. Returns (n_added, trace)."""
    from nav_agent import _add_scored

    bonus = float(getattr(config, "read_score_bonus", 0.0) or 0.0)
    trace: List[Dict[str, Any]] = []
    total = 0
    for req in requests:
        asset_type = str(req.get("asset_type") or "").strip()
        scope = str(req.get("scope") or "").strip() or (default_scope or "")
        doc = owner_document(ts, scope, str(getattr(state, "doc_id", "") or ""))
        chunks = gather_scoped_asset_chunks(
            ts, asset_type=asset_type, scope=scope or None, doc_id=doc
        )
        scored = [(c, bonus) for c in chunks]
        added = _add_scored(state, scored)
        total += added
        trace.append(
            {
                "kind": req.get("kind", ""),
                "asset_type": asset_type,
                "query": req.get("query", ""),
                "scope": scope,
                "n_candidates": len(chunks),
                "n_added": added,
            }
        )
    return total, trace
