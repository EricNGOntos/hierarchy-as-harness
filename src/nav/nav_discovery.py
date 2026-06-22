"""Hybrid discovery + LLM rerank for Nav Agent.

Discovery finds candidate sections via KnowWhere 3-channel RRF, then asks the
navigation LLM to pick 1–3 paths. Nothing is injected into the evidence pool
until the agent explicitly chooses a D* COLLECT action.
"""
from __future__ import annotations

import json
import os
import re
from typing import Any, Dict, List, Optional, Tuple

from agent_delivery.code.index_retrieval import Chunk
from agent_delivery.code.tool_space import ToolSpace

from knowhere_hybrid import hybrid_search_rows
from nav_types import NavConfig, NavState


def _discovery_enabled() -> bool:
    raw = os.environ.get("NAV_DISCOVERY_SOFT_SIGNAL", "1").strip().lower()
    return raw not in {"0", "false", "no", "off"}



def _ancestor_node_ids(ts: ToolSpace, doc_id: str, node_id: str) -> List[str]:
    idx = getattr(ts, "_idx", None)
    if idx is None:
        return [node_id]
    try:
        ancestors = list(idx.ancestor_line_node_ids(node_id))
    except Exception:
        ancestors = []
    if ancestors:
        return [a for a in ancestors if str(a).startswith(f"{doc_id}:")]
    return [node_id]


def _nearest_scope_node_ids(ts: ToolSpace, doc_id: str, node_id: str) -> List[str]:
    ancestors = _ancestor_node_ids(ts, doc_id, node_id)
    if not ancestors:
        return [node_id]
    depth = max(1, int(os.environ.get("NAV_DISCOVERY_SCOPE_ANCESTOR_DEPTH", "2").strip() or "2"))
    return ancestors[:depth]


def _split_chunk_text(chunk: Chunk) -> Tuple[str, str]:
    text = str(chunk.text or "")
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    path_text = ""
    body_lines: List[str] = []
    for ln in lines:
        if ln.startswith("[§"):
            path_text = ln.strip("[]").replace("§", "", 1).strip()
        elif ln.startswith("PATH:"):
            path_text = ln.replace("PATH:", "", 1).strip()
        else:
            body_lines.append(ln)
    body = "\n".join(body_lines).strip()
    return path_text, body or text


def _chunk_to_search_row(chunk: Chunk, ts: ToolSpace) -> dict[str, Any]:
    path_text, body = _split_chunk_text(chunk)
    section_id = str(chunk.section_id or "")
    preview = ""
    if section_id:
        try:
            preview = str(ts.get_structure(section_id).get("preview") or "")[:160]
        except Exception:
            preview = ""
    from knowhere_hybrid import build_content_search_text, build_path_search_text, build_term_search_text

    return {
        "chunk_id": chunk.node_id,
        "section_id": section_id,
        "content": body,
        "path_search_text": build_path_search_text(section_path=path_text or preview, section_title=preview),
        "content_search_text": build_content_search_text(body, section_summary=preview),
        "term_search_text": build_term_search_text(body, path_text=path_text or preview),
        "preview": preview[:120],
    }


def _aggregate_section_candidates(
    fused_rows: List[dict[str, Any]],
    ts: ToolSpace,
    state: NavState,
) -> List[dict[str, Any]]:
    task_type = (state.task_type or "").strip().lower()
    is_scope = task_type in {"scope_collection", "regulatory_coverage"}
    ancestor_decay = float(os.environ.get("NAV_DISCOVERY_ANCESTOR_DECAY", "0.90").strip() or "0.90")
    if is_scope:
        ancestor_decay = float(os.environ.get("NAV_DISCOVERY_SCOPE_ANCESTOR_DECAY", "0.55").strip() or "0.55")

    section_best: Dict[str, dict[str, Any]] = {}
    for row in fused_rows:
        sid = str(row.get("section_id") or "").strip()
        if not sid:
            continue
        base = float(row.get("discovery_score", row.get("score", 0.0)) or 0.0)
        preview = str(row.get("preview") or "")
        chain = _nearest_scope_node_ids(ts, state.doc_id, sid) if is_scope else _ancestor_node_ids(ts, state.doc_id, sid)
        if sid not in chain:
            chain = [sid] + [n for n in chain if n != sid]

        for depth, target in enumerate(dict.fromkeys(chain)):
            score = base * (ancestor_decay ** depth)
            prev = section_best.get(target)
            label = preview
            if target != sid:
                try:
                    label = str(ts.get_structure(target).get("preview") or preview)[:120]
                except Exception:
                    label = preview
            if prev is None or score > float(prev.get("discovery_score", 0.0)):
                section_best[target] = {
                    "section_id": target,
                    "discovery_score": score,
                    "label": label,
                }

    ranked = sorted(section_best.values(), key=lambda item: (-float(item["discovery_score"]), item["section_id"]))
    recall_k = max(1, int(os.environ.get("NAV_DISCOVERY_RECALL_K", "10").strip() or "10"))
    return ranked[:recall_k]


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
    m = re.search(r"\{.*\}", s, flags=re.S)
    if not m:
        return None
    try:
        obj = json.loads(m.group(0))
        return obj if isinstance(obj, dict) else None
    except Exception:
        return None


def _llm_rerank_sections(
    state: NavState,
    candidates: List[dict[str, Any]],
    config: NavConfig,
) -> Tuple[List[str], dict[str, Any]]:
    """Ask the nav LLM to pick section_ids from hybrid-recall candidates."""
    if not candidates:
        return [], {}

    legal_ids = [str(c["section_id"]) for c in candidates if c.get("section_id")]
    if not legal_ids:
        return [], {}

    pick_hint = max(1, int(os.environ.get("NAV_DISCOVERY_PICK_K", "3").strip() or "3"))
    if os.environ.get("NAV_DISCOVERY_LLM_RERANK", "1").strip().lower() in {"0", "false", "no", "off"}:
        return legal_ids[:pick_hint], {"model": "disabled", "reason": "llm rerank off"}

    from agent_delivery.code.llm_api_cache import cached_chat_completion  # type: ignore
    from agent_delivery.code.llm_config import make_openai_client, require_llm_env  # type: ignore
    from agent_delivery.code.llm_usage import record_usage  # type: ignore

    require_llm_env(context="Nav discovery rerank")
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    model = os.environ.get(config.llm_model_env, "").strip() or os.environ.get("NAV_LLM_MODEL", "gpt-4o-mini")
    base_url = os.environ.get("OPENAI_BASE_URL", "").strip() or None
    client = make_openai_client(api_key=key, base_url=base_url)

    cand_lines = []
    for c in candidates:
        cand_lines.append(
            f"- {c['section_id']} | score={float(c.get('discovery_score', 0.0)):.3f} | {str(c.get('label') or '')[:100]}"
        )

    system = (
        "You rerank document navigation discovery candidates. "
        "Return one JSON object only. "
        f"Pick up to {pick_hint} section_id values from the candidate list based on query relevance. "
        "Do not invent ids. Keep reason under 15 words."
    )
    user = (
        f"query: {state.query}\n"
        f"task_type: {state.task_type}\n\n"
        "candidates:\n"
        + "\n".join(cand_lines)
        + '\n\nReturn: {"section_ids":["..."],"reason":"..."}'
    )

    meta: dict[str, Any] = {"model": model}
    try:
        cached = cached_chat_completion(
            client,
            model=model,
            messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
            temperature=float(config.llm_temperature),
            max_tokens=min(256, int(config.llm_max_tokens)),
            purpose="nav_discovery_rerank",
        )
        record_usage("nav_discovery_rerank", cached.get("usage"))
        content = str(cached.get("content") or "")
        meta["raw"] = content
        obj = _extract_json_obj(content) or {}
        picked_raw = obj.get("section_ids") or obj.get("section_id") or []
        if isinstance(picked_raw, str):
            picked_raw = [picked_raw]
        picked: List[str] = []
        legal = set(legal_ids)
        for sid in picked_raw:
            sid_s = str(sid or "").strip()
            if sid_s in legal and sid_s not in picked:
                picked.append(sid_s)
        meta["reason"] = str(obj.get("reason") or "")
        if picked:
            return picked, meta
    except Exception as exc:
        meta["error"] = str(exc)

    # Fallback: keep hybrid ordering, no hard score cutoff — just cap presentation width.
    return legal_ids[:pick_hint], meta


def _hybrid_section_candidates(ts: ToolSpace, state: NavState, config: NavConfig) -> List[dict[str, Any]]:
    if state.hybrid_section_candidates:
        return list(state.hybrid_section_candidates)
    pool = ts.leaf_path_search_pool(state.doc_id)
    if not pool:
        return []
    rows = [_chunk_to_search_row(chunk, ts) for chunk in pool]
    chunk_top_k = max(1, int(os.environ.get("NAV_DISCOVERY_CHUNK_TOP_K", "24").strip() or "24"))
    fused = hybrid_search_rows(rows, state.query, top_k=chunk_top_k)
    if not fused:
        return []
    section_candidates = _aggregate_section_candidates(fused, ts, state)
    state.hybrid_section_candidates = list(section_candidates)
    return section_candidates


def _picked_discovery_ids(state: NavState, section_candidates: List[dict[str, Any]], config: NavConfig) -> List[str]:
    if state.discovery_picked_ids:
        return list(state.discovery_picked_ids)
    picked_ids, rerank_meta = _llm_rerank_sections(state, section_candidates, config)
    if rerank_meta:
        state.discovery_rerank_meta = rerank_meta
    state.discovery_picked_ids = list(picked_ids)
    return picked_ids


def compute_discovery_scores(ts: ToolSpace, state: NavState, config: NavConfig) -> Dict[str, float]:
    if not _discovery_enabled():
        return {}

    section_candidates = _hybrid_section_candidates(ts, state, config)
    if not section_candidates:
        return {}

    picked_ids = _picked_discovery_ids(state, section_candidates, config)
    by_id = {str(c["section_id"]): float(c["discovery_score"]) for c in section_candidates}
    scale = float(os.environ.get("NAV_DISCOVERY_SCORE_SCALE", "20.0").strip() or "20.0")
    min_score = float(os.environ.get("NAV_DISCOVERY_MIN_SCORE", "0.1").strip() or "0.1")
    out: Dict[str, float] = {}
    for sid in picked_ids:
        raw = by_id.get(sid)
        if raw is None or raw < min_score:
            continue
        out[sid] = raw * scale
    return out
