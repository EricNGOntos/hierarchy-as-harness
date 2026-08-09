from __future__ import annotations

from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

from knowhere_hybrid import (
    build_content_search_text,
    build_path_search_text,
    build_term_search_text,
    score_dense_channel,
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
        # Provider-backed spaces expose the title chain directly; without this
        # the path channel would score every unit as empty.
        path_fn = getattr(ts, "path_titles", None)
        return str(path_fn(section_id, doc_id) or "") if callable(path_fn) else ""
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


def _pool_unit_scores_to_tree(
    children_map: Dict[str, List[str]],
    leaves: Set[str],
    unit_scores: Dict[str, float],
) -> Dict[str, float]:
    """MAX-pool globally comparable unit scores onto one document tree."""
    map_scores = {
        leaf_id: float(unit_scores.get(leaf_id, 0.0) or 0.0)
        for leaf_id in leaves
    }

    def score_node(section_id: str) -> float:
        if section_id in map_scores:
            return map_scores[section_id]
        kids = children_map.get(section_id) or []
        if not kids:
            score = float(unit_scores.get(section_id, 0.0) or 0.0)
            map_scores[section_id] = score
            return score
        descendant_leaves = _collect_descendant_leaves(
            section_id, children_map, leaves
        )
        parts = [
            float(unit_scores.get(leaf_id, 0.0) or 0.0)
            for leaf_id in descendant_leaves
        ]
        self_key = f"{section_id}__self"
        if self_key in unit_scores:
            parts.append(float(unit_scores[self_key]))
        score = float(max(parts)) if parts else 0.0
        map_scores[section_id] = score
        return score

    for section_id in children_map:
        score_node(section_id)
    return map_scores


def _score_dense_units_by_doc(
    units_by_doc: Sequence[Tuple[str, List[dict]]],
    query: str,
    *,
    namespace: Optional[str],
) -> Dict[str, Optional[Dict[str, float]]]:
    """Read per-doc vector caches, returning raw cosine scores for global fusion.

    Dense cosine is independently comparable across documents. Partitioning only
    preserves the existing per-doc disk cache; no ranking or normalization occurs
    here. If any partition fails, that whole channel falls back to global BM25.
    """
    dense_by_channel: Dict[str, Optional[Dict[str, float]]] = {}
    for channel, text_field in (("path", "path_text"), ("content", "content")):
        score_by_id: Dict[str, float] = {}
        complete = True
        for doc_id, units in units_by_doc:
            if not units:
                continue
            unit_ids = [str(unit["chunk_id"]) for unit in units]
            scores = score_dense_channel(
                [str(unit.get(text_field) or "") for unit in units],
                query,
                unit_ids=unit_ids,
                doc_id=doc_id,
                channel=channel,
                namespace=namespace,
            )
            if scores is None or len(scores) != len(unit_ids):
                complete = False
                break
            score_by_id.update(
                {
                    unit_id: float(scores[index])
                    for index, unit_id in enumerate(unit_ids)
                }
            )
        dense_by_channel[channel] = score_by_id if complete else None
    return dense_by_channel


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
    map_scores = _pool_unit_scores_to_tree(children_map, leaves, unit_score)
    return map_scores, unit_score


def compute_corpus_map_and_unit_scores(
    ts: Any,
    *,
    doc_ids: Sequence[str],
    query: str,
    namespace: Optional[str] = None,
) -> Tuple[Dict[str, float], Dict[str, float]]:
    """Globally score every unit in the corpus-root navigation space.

    All documents share one BM25 corpus, path/content normalization, channel
    ranking, and RRF pass. Dense vectors are only loaded through per-doc cache
    partitions; their raw cosine scores join the same global fusion. Synthetic
    document and corpus roots are then MAX-pooled from those global unit scores.
    """
    from agent_delivery.code.tool_space import (  # late import
        CORPUS_ROOT_SECTION_ID,
        is_corpus_doc_id,
    )

    valid_doc_ids: List[str] = []
    seen_doc_ids: Set[str] = set()
    for raw in doc_ids:
        doc_id = str(raw or "").strip()
        if (
            not doc_id
            or is_corpus_doc_id(doc_id)
            or doc_id in seen_doc_ids
        ):
            continue
        seen_doc_ids.add(doc_id)
        valid_doc_ids.append(doc_id)

    ns = namespace
    if not ns:
        import os

        ns = os.environ.get("NAV_MAP_UNIT_CACHE_NS", "").strip() or None

    tree_by_doc: Dict[str, Tuple[Dict[str, List[str]], Set[str]]] = {}
    units_by_doc: List[Tuple[str, List[dict]]] = []
    all_units: List[dict] = []
    for doc_id in valid_doc_ids:
        root_ids = list(ts.sections_for_doc(doc_id))
        children_map, leaves, _titles = _walk_tree(ts, doc_id, root_ids)
        units = build_score_units(ts, doc_id, root_ids=root_ids)
        tree_by_doc[doc_id] = (children_map, leaves)
        units_by_doc.append((doc_id, units))
        all_units.extend(units)

    dense_scores = _score_dense_units_by_doc(
        units_by_doc,
        query,
        namespace=ns,
    )
    scored = score_rows_hybrid_all(
        all_units,
        query,
        dense_scores_by_channel=dense_scores,
    )
    unit_scores = {
        str(row.get("chunk_id") or ""): float(row.get("score") or 0.0)
        for row in scored
    }

    map_scores: Dict[str, float] = {}
    doc_root_scores: Dict[str, float] = {}
    for doc_id in valid_doc_ids:
        children_map, leaves = tree_by_doc[doc_id]
        doc_map_scores = _pool_unit_scores_to_tree(
            children_map, leaves, unit_scores
        )
        map_scores.update(doc_map_scores)
        doc_max = max(
            (float(value) for value in doc_map_scores.values()),
            default=0.0,
        )
        root_id = f"{doc_id}:__doc_root"
        map_scores[root_id] = doc_max
        doc_root_scores[root_id] = doc_max
    map_scores[CORPUS_ROOT_SECTION_ID] = max(
        doc_root_scores.values(),
        default=0.0,
    )
    return map_scores, unit_scores


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


def compute_multi_query_map_scores(
    ts: Any,
    *,
    queries: Dict[str, str],
    doc_id: str,
    root_ids: Optional[Sequence[str]] = None,
    corpus_doc_ids: Optional[Sequence[str]] = None,
    namespace: Optional[str] = None,
) -> Tuple[Dict[str, Dict[str, float]], Dict[str, Dict[str, float]]]:
    """Score the map once per query id.

    Returns ``(subgoal_map_scores, subgoal_unit_scores)`` keyed by the same
    query ids. Empty / blank queries are skipped. Reuses the existing single-
    query scorer — no new retrieval channels.
    """
    sub_map: Dict[str, Dict[str, float]] = {}
    sub_unit: Dict[str, Dict[str, float]] = {}
    corpus = list(corpus_doc_ids or [])
    for qid, raw_q in (queries or {}).items():
        key = str(qid or "").strip()
        query = str(raw_q or "").strip()
        if not key or not query:
            continue
        if corpus:
            ms, us = compute_corpus_map_and_unit_scores(
                ts, doc_ids=corpus, query=query, namespace=namespace
            )
        else:
            ms, us = compute_map_and_unit_scores(
                ts,
                doc_id=doc_id,
                query=query,
                root_ids=root_ids,
                namespace=namespace,
            )
        sub_map[key] = ms
        sub_unit[key] = us
    return sub_map, sub_unit


def merge_score_maps(
    per_source: Dict[str, Dict[str, float]],
    *,
    weights: Optional[Dict[str, float]] = None,
    active_ids: Optional[Sequence[str]] = None,
) -> Dict[str, float]:
    """Goal-conditioned merge: ``max_s(w_s · score_s(node))``.

    Sources with non-positive weight are ignored. When ``weights`` is omitted,
    every active source contributes with equal weight 1.0.
    """
    if active_ids is None:
        keys = [str(k) for k in (per_source or {}).keys()]
    else:
        keys = [str(k) for k in active_ids if str(k) in (per_source or {})]
    if not keys:
        return {}
    wmap = {str(k): float(v) for k, v in (weights or {}).items()}
    out: Dict[str, float] = {}
    for key in keys:
        w = float(wmap.get(key, 1.0))
        if w <= 0.0:
            continue
        for sid, score in (per_source.get(key) or {}).items():
            val = w * float(score or 0.0)
            prev = out.get(sid)
            if prev is None or val > prev:
                out[sid] = val
    return out


def select_map_highlights_multi(
    per_source_unit_scores: Dict[str, Dict[str, float]],
    *,
    k: int,
    active_ids: Optional[Sequence[str]] = None,
    weights: Optional[Dict[str, float]] = None,
) -> Tuple[List[str], Dict[str, List[str]]]:
    """Per-source TOP-K union + provenance for ``[Hit:s*]`` tags.

    Each active source contributes up to ``k`` sections (same rescue-K as the
    single-query path). Union order follows the merged weighted unit score.
    """
    if active_ids is None:
        keys = [str(k) for k in (per_source_unit_scores or {}).keys()]
    else:
        keys = [
            str(k) for k in active_ids if str(k) in (per_source_unit_scores or {})
        ]
    hit_sources: Dict[str, List[str]] = {}
    for key in keys:
        local = select_map_highlights(per_source_unit_scores.get(key) or {}, k=k)
        for sid in local:
            hit_sources.setdefault(sid, [])
            if key not in hit_sources[sid]:
                hit_sources[sid].append(key)

    merged_units = merge_score_maps(
        per_source_unit_scores,
        weights=weights,
        active_ids=keys,
    )
    # Rank the union by merged score; keep every sourced hit (must_keep soft).
    ranked = sorted(
        hit_sources.keys(),
        key=lambda sid: (
            -float(merged_units.get(sid, 0.0) or 0.0),
            sid,
        ),
    )
    return ranked, hit_sources
