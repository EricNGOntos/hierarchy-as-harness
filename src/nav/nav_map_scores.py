from __future__ import annotations

from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

from knowhere_hybrid import (
    build_content_search_text,
    build_path_search_text,
    build_term_search_text,
    score_rows_hybrid_all,
)


def _children_ids(ts: Any, section_id: str, doc_id: str) -> List[str]:
    children_fn = getattr(ts, "_children_for_section_path", None)
    if not callable(children_fn):
        st = ts.get_structure(section_id)
        rows = st.get("children") or []
        return [str(r.get("section_id") or "").strip() for r in rows if r.get("section_id")]
    rows = children_fn(section_id, doc_id, limit=100000)
    return [str(r.get("section_id") or "").strip() for r in rows if r.get("section_id")]


def _line_content(ts: Any, section_id: str, doc_id: str) -> str:
    """Raw line text for a section node (no truncation)."""
    idx = getattr(ts, "_idx", None)
    b = getattr(idx, "_bundles", {}).get(doc_id) if idx is not None else None
    if b is None:
        st = ts.get_structure(section_id)
        return str(st.get("preview") or "").strip()
    loc = getattr(idx, "_node_to_doc_line", {}).get(section_id)
    if not loc:
        return ""
    _doc, line_idx = loc
    if line_idx < 0 or line_idx >= len(b.lines):
        return ""
    return str(b.lines[line_idx].content or "").strip()


def _ancestor_path_titles(ts: Any, section_id: str, doc_id: str) -> str:
    idx = getattr(ts, "_idx", None)
    if idx is None:
        return ""
    try:
        ancestors = list(idx.ancestor_line_node_ids(section_id))
    except Exception:
        ancestors = []
    titles: List[str] = []
    for aid in reversed(ancestors):
        if not str(aid).startswith(f"{doc_id}:"):
            continue
        titles.append(_line_content(ts, aid, doc_id))
    titles.append(_line_content(ts, section_id, doc_id))
    return " / ".join(t for t in titles if t)


def _self_only_text(ts: Any, section_id: str, doc_id: str) -> Tuple[str, bool]:
    """Return (self_text, has_interstitial_body).

    Interstitial means self_only span contains content beyond the heading line
    itself (structural: more than one line/chunk in the self span).
    """
    self_fn = getattr(ts, "materialize_self_only_chunks", None)
    if not callable(self_fn):
        return "", False
    chunks = list(self_fn(section_id, doc_id) or [])
    if not chunks:
        return "", False
    texts = [str(getattr(c, "text", "") or "").strip() for c in chunks]
    texts = [t for t in texts if t]
    if not texts:
        return "", False
    # Structural interstitial: self span covers more than the node heading line.
    has_interstitial = len(chunks) > 1
    return "\n".join(texts), has_interstitial


def _section_body_text(ts: Any, section_id: str, doc_id: str) -> str:
    """Heading + lines until first structural child (leaf body / parent self span)."""
    text, _ = _self_only_text(ts, section_id, doc_id)
    if text:
        return text
    return _line_content(ts, section_id, doc_id)


def _walk_tree(
    ts: Any,
    doc_id: str,
    root_ids: Sequence[str],
) -> Tuple[Dict[str, List[str]], Set[str], Dict[str, str]]:
    """Return children map, leaf ids, and title map for reachable nodes."""
    children_map: Dict[str, List[str]] = {}
    titles: Dict[str, str] = {}
    leaves: Set[str] = set()
    seen: Set[str] = set()

    def walk(sid: str) -> None:
        if not sid or sid in seen:
            return
        seen.add(sid)
        titles[sid] = _line_content(ts, sid, doc_id)
        kids = [c for c in _children_ids(ts, sid, doc_id) if c]
        children_map[sid] = kids
        if not kids:
            leaves.add(sid)
            return
        for kid in kids:
            walk(kid)

    for rid in root_ids:
        walk(rid)
    return children_map, leaves, titles


def _collect_descendant_leaves(
    section_id: str,
    children_map: Dict[str, List[str]],
    leaves: Set[str],
) -> List[str]:
    out: List[str] = []

    def rec(sid: str) -> None:
        kids = children_map.get(sid) or []
        if not kids:
            if sid in leaves:
                out.append(sid)
            return
        for kid in kids:
            rec(kid)

    rec(section_id)
    return out


def build_score_units(ts: Any, doc_id: str, root_ids: Optional[Sequence[str]] = None) -> List[dict]:
    """Build leaf (+ interstitial self_only) units for hybrid scoring."""
    if root_ids is None:
        root_ids = list(ts.sections_for_doc(doc_id))
    children_map, leaves, titles = _walk_tree(ts, doc_id, root_ids)
    units: List[dict] = []
    seen_unit_ids: Set[str] = set()

    for leaf_id in sorted(leaves):
        content = _section_body_text(ts, leaf_id, doc_id) or (
            titles.get(leaf_id) or _line_content(ts, leaf_id, doc_id)
        )
        path_text = _ancestor_path_titles(ts, leaf_id, doc_id)
        unit_id = leaf_id
        if unit_id in seen_unit_ids:
            continue
        seen_unit_ids.add(unit_id)
        title = titles.get(leaf_id) or _line_content(ts, leaf_id, doc_id)
        units.append(
            {
                "chunk_id": unit_id,
                "section_id": leaf_id,
                "kind": "leaf",
                "content": content,
                "path_text": path_text,
                "path_search_text": build_path_search_text(
                    section_path=path_text, section_title=title or content
                ),
                "content_search_text": build_content_search_text(content),
                "term_search_text": build_term_search_text(content, path_text=path_text),
            }
        )

    # Parents with interstitial self body.
    for sid, kids in children_map.items():
        if not kids:
            continue
        self_text, has_interstitial = _self_only_text(ts, sid, doc_id)
        if not has_interstitial or not self_text:
            continue
        unit_id = f"{sid}__self"
        if unit_id in seen_unit_ids:
            continue
        seen_unit_ids.add(unit_id)
        path_text = _ancestor_path_titles(ts, sid, doc_id)
        units.append(
            {
                "chunk_id": unit_id,
                "section_id": sid,
                "kind": "self_only",
                "content": self_text,
                "path_text": path_text,
                "path_search_text": build_path_search_text(
                    section_path=path_text, section_title=titles.get(sid) or ""
                ),
                "content_search_text": build_content_search_text(self_text),
                "term_search_text": build_term_search_text(self_text, path_text=path_text),
            }
        )
    return units


def compute_map_scores(
    ts: Any,
    *,
    doc_id: str,
    query: str,
    root_ids: Optional[Sequence[str]] = None,
) -> Dict[str, float]:
    """Leaf 3-channel scores + parent max-pool (self_only only if interstitial)."""
    map_scores, _unit_scores = compute_map_and_unit_scores(
        ts, doc_id=doc_id, query=query, root_ids=root_ids
    )
    return map_scores


def compute_map_and_unit_scores(
    ts: Any,
    *,
    doc_id: str,
    query: str,
    root_ids: Optional[Sequence[str]] = None,
    namespace: Optional[str] = None,
) -> Tuple[Dict[str, float], Dict[str, float]]:
    """Return (section map_scores, unit hybrid scores keyed by chunk_id)."""
    if root_ids is None:
        root_ids = list(ts.sections_for_doc(doc_id))
    children_map, leaves, _titles = _walk_tree(ts, doc_id, root_ids)
    units = build_score_units(ts, doc_id, root_ids=root_ids)
    if not units:
        return {}, {}

    ns = namespace
    if not ns:
        import os

        ns = os.environ.get("NAV_MAP_UNIT_CACHE_NS", "").strip() or None

    scored = score_rows_hybrid_all(
        units,
        query,
        path_texts={u["chunk_id"]: u.get("path_text") or "" for u in units},
        content_texts={u["chunk_id"]: u.get("content") or "" for u in units},
        doc_id=doc_id,
        namespace=ns,
    )
    unit_score = {str(r.get("chunk_id") or ""): float(r.get("score") or 0.0) for r in scored}

    map_scores: Dict[str, float] = {}
    for leaf_id in leaves:
        map_scores[leaf_id] = float(unit_score.get(leaf_id, 0.0) or 0.0)

    # Bottom-up parent MAX-pool over descendant leaf units (+ interstitial self).
    def score_node(sid: str) -> float:
        if sid in map_scores:
            return map_scores[sid]
        kids = children_map.get(sid) or []
        if not kids:
            val = float(unit_score.get(sid, 0.0) or 0.0)
            map_scores[sid] = val
            return val
        leaf_ids = _collect_descendant_leaves(sid, children_map, leaves)
        parts = [float(unit_score.get(lid, 0.0) or 0.0) for lid in leaf_ids]
        self_key = f"{sid}__self"
        if self_key in unit_score:
            parts.append(float(unit_score[self_key]))
        val = float(max(parts)) if parts else 0.0
        map_scores[sid] = val
        return val

    for sid in list(children_map.keys()):
        score_node(sid)
    return map_scores, unit_score


def unit_id_to_section_id(unit_id: str) -> str:
    """Map scoring unit id (leaf or `{sid}__self`) to the section on the map."""
    uid = str(unit_id or "").strip()
    if uid.endswith("__self"):
        return uid[: -len("__self")]
    return uid


def select_map_highlights(unit_scores: Dict[str, float], k: int = 6) -> List[str]:
    """TOP-K section ids by unit hybrid score (stable tie-break on unit id)."""
    limit = max(0, int(k))
    if limit <= 0 or not unit_scores:
        return []
    ranked = sorted(
        unit_scores.items(),
        key=lambda kv: (-float(kv[1] or 0.0), str(kv[0])),
    )
    out: List[str] = []
    seen: Set[str] = set()
    for uid, _score in ranked:
        sid = unit_id_to_section_id(str(uid))
        if not sid or sid in seen:
            continue
        seen.add(sid)
        out.append(sid)
        if len(out) >= limit:
            break
    return out
