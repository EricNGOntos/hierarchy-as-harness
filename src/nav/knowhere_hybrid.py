"""KnowWhere-style 3-channel hybrid retrieval (path BM25 + content BM25 + term).

Ported from Ontos-AI/knowhere:
  packages/shared-python/shared/services/retrieval/search/{scoring,lexical_ranker,channels}.py

Reference: https://github.com/Ontos-AI/knowhere
"""
from __future__ import annotations

import os
import re
from typing import Any, Dict, List, Optional, Sequence, Tuple

RRF_K = 60
CHANNEL_WEIGHT_PATH = 1.0
CHANNEL_WEIGHT_CONTENT = 2.0
CHANNEL_WEIGHT_TERM = 1.5
INTERNAL_RECALL_K_MULTIPLIER = 2


def tokenize_for_retrieval(text: str, *, dedupe: bool = True) -> List[str]:
    tokens = re.findall(r"[a-z0-9_]+|[\u4e00-\u9fff]", str(text or "").lower())
    if not dedupe:
        return [t for t in tokens if t]
    seen: set[str] = set()
    out: List[str] = []
    for t in tokens:
        if t and t not in seen:
            seen.add(t)
            out.append(t)
    return out


def tokenize_query_for_ranker(query: str) -> List[str]:
    return tokenize_for_retrieval(query, dedupe=True)


def _space_join_tokens(text: str) -> str:
    return " ".join(tokenize_for_retrieval(text, dedupe=False))


def build_content_search_text(content: str, *, section_summary: Optional[str] = None) -> str:
    parts = [str(content or "").strip()]
    if section_summary and str(section_summary).strip():
        parts.append(str(section_summary).strip())
    raw = " ".join(p for p in parts if p)
    return _space_join_tokens(raw) if raw else ""


def build_path_search_text(
    *,
    source_file_name: Optional[str] = None,
    section_path: Optional[str] = None,
    section_title: Optional[str] = None,
) -> str:
    parts = [
        str(v).strip()
        for v in (source_file_name, section_path, section_title)
        if v and str(v).strip()
    ]
    if not parts:
        return ""
    return _space_join_tokens(" ".join(parts))


def build_term_search_text(content: str, *, path_text: Optional[str] = None) -> str:
    combined = f"{str(content or '').strip()} {str(path_text or '').strip()}".strip()
    return combined


def _get_search_tokens(row: dict[str, Any], *, search_field: str) -> List[str]:
    return [token for token in str(row.get(search_field) or "").split() if token]


def _rank_rows_by_token_overlap(
    rows: List[dict[str, Any]],
    query_tokens: List[str],
    *,
    search_field: str,
) -> List[dict[str, Any]]:
    ranked_rows: List[dict[str, Any]] = []
    query_token_set = set(query_tokens)
    for row in rows:
        tokens = _get_search_tokens(row, search_field=search_field)
        overlap = len(query_token_set.intersection(tokens))
        if overlap <= 0:
            continue
        ranked_rows.append(dict(row, score=float(overlap)))
    ranked_rows.sort(key=lambda row: row["score"], reverse=True)
    return ranked_rows


def rank_rows_by_bm25(
    rows: List[dict[str, Any]],
    query_tokens: List[str],
    *,
    search_field: str,
) -> List[dict[str, Any]]:
    try:
        from rank_bm25 import BM25Okapi
    except ImportError:
        return _rank_rows_by_token_overlap(rows, query_tokens, search_field=search_field)

    corpus: List[List[str]] = []
    ranked_rows: List[dict[str, Any]] = []
    query_token_set = set(query_tokens)
    for row in rows:
        tokens = _get_search_tokens(row, search_field=search_field)
        if not tokens or not query_token_set.intersection(tokens):
            continue
        corpus.append(tokens)
        ranked_rows.append(row)

    if not corpus or not query_tokens:
        return []

    bm25 = BM25Okapi(corpus)
    scores = bm25.get_scores(query_tokens)
    for index, row in enumerate(ranked_rows):
        row = dict(row)
        row["score"] = float(scores[index])
        ranked_rows[index] = row
    ranked_rows.sort(key=lambda row: row["score"], reverse=True)
    return ranked_rows


def rank_rows_by_term_channel(rows: List[dict[str, Any]], query: str) -> List[dict[str, Any]]:
    query_lower = query.lower().strip()
    query_tokens = tokenize_query_for_ranker(query)
    if not query_lower or not query_tokens:
        return []

    scored: List[dict[str, Any]] = []
    for row in rows:
        haystack = (row.get("term_search_text") or "").lower()
        if not haystack:
            continue
        if query_lower in haystack:
            scored.append(dict(row, score=100.0))
            continue
        hit_count = sum(1 for unit in query_tokens if unit in haystack)
        if hit_count > 0:
            scored.append(dict(row, score=float(hit_count)))
    scored.sort(key=lambda r: r["score"], reverse=True)
    return scored


def merge_channels_rrf(
    channels: List[List[dict[str, Any]]],
    weights: List[float],
    top_k: int,
    k: int = RRF_K,
) -> List[dict[str, Any]]:
    score_dict: Dict[str, float] = {}
    row_by_chunk_id: Dict[str, dict[str, Any]] = {}

    for channel_idx, channel_rows in enumerate(channels):
        weight = weights[channel_idx] if channel_idx < len(weights) else 1.0
        for rank, row in enumerate(channel_rows):
            chunk_id = str(row.get("chunk_id") or "")
            if not chunk_id:
                continue
            rrf_score = weight / (k + rank + 1)
            score_dict[chunk_id] = score_dict.get(chunk_id, 0.0) + rrf_score
            if chunk_id not in row_by_chunk_id:
                row_by_chunk_id[chunk_id] = row

    ranked = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)
    results: List[dict[str, Any]] = []
    for chunk_id, fused_score in ranked[:top_k]:
        row = dict(row_by_chunk_id[chunk_id])
        row["score"] = round(fused_score, 6)
        results.append(row)
    return results


def normalize_row_scores(
    rows: List[dict[str, Any]],
    *,
    source_field: str = "score",
    target_field: str = "discovery_score",
    default: float = 0.5,
) -> None:
    if not rows:
        return
    values = [float(row.get(source_field, 0.0) or 0.0) for row in rows]
    min_score = min(values)
    max_score = max(values)
    if max_score <= 0.0 and min_score <= 0.0:
        for row in rows:
            row[target_field] = 0.0
        return
    if max_score == min_score:
        for row in rows:
            row[target_field] = default
        return
    denominator = max_score - min_score
    for row in rows:
        raw_score = float(row.get(source_field, 0.0) or 0.0)
        row[target_field] = round((raw_score - min_score) / denominator, 6)


def _channel_weights() -> Tuple[float, float, float]:
    path_w = float(os.environ.get("NAV_DISCOVERY_CHANNEL_WEIGHT_PATH", str(CHANNEL_WEIGHT_PATH)).strip() or CHANNEL_WEIGHT_PATH)
    content_w = float(
        os.environ.get("NAV_DISCOVERY_CHANNEL_WEIGHT_CONTENT", str(CHANNEL_WEIGHT_CONTENT)).strip()
        or CHANNEL_WEIGHT_CONTENT
    )
    term_w = float(os.environ.get("NAV_DISCOVERY_CHANNEL_WEIGHT_TERM", str(CHANNEL_WEIGHT_TERM)).strip() or CHANNEL_WEIGHT_TERM)
    return path_w, content_w, term_w


def hybrid_search_rows(
    rows: Sequence[dict[str, Any]],
    query: str,
    *,
    top_k: int = 10,
    internal_recall_k: Optional[int] = None,
) -> List[dict[str, Any]]:
    """Run KnowWhere path/content/term channels + weighted RRF over in-memory rows."""
    if not rows:
        return []
    query_tokens = tokenize_query_for_ranker(query)
    if not query_tokens:
        return []

    recall_k = internal_recall_k
    if recall_k is None:
        mult = int(os.environ.get("NAV_DISCOVERY_RECALL_MULT", str(INTERNAL_RECALL_K_MULTIPLIER)).strip() or INTERNAL_RECALL_K_MULTIPLIER)
        recall_k = max(top_k, top_k * max(1, mult))

    rrf_k = int(os.environ.get("NAV_DISCOVERY_RRF_K", str(RRF_K)).strip() or RRF_K)
    path_w, content_w, term_w = _channel_weights()

    path_rows = rank_rows_by_bm25(list(rows), query_tokens, search_field="path_search_text")[:recall_k]
    content_rows = rank_rows_by_bm25(list(rows), query_tokens, search_field="content_search_text")[:recall_k]
    term_rows = rank_rows_by_term_channel(list(rows), query)[:recall_k]

    fused = merge_channels_rrf(
        [path_rows, content_rows, term_rows],
        [path_w, content_w, term_w],
        top_k,
        k=rrf_k,
    )
    normalize_row_scores(fused)
    return fused
