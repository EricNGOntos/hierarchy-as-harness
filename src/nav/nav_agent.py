from __future__ import annotations

import time
import os
import re
from typing import Any, Dict, List, Optional, Tuple

from agent_delivery.agent.types import AgentStep, EpisodeResult
from agent_delivery.code.budget_eval import evaluate_at_budget
from agent_delivery.code.compose_llm import compose_answer_llm
from agent_delivery.code.hierarchical_tools import HierarchicalTools, ToolHit
from agent_delivery.code.index_retrieval import Chunk
from agent_delivery.code.tool_space import Refusal, ToolSpace

from nav_actions import build_legal_actions
from nav_policy import choose_llm_action
from nav_projection import build_projection
from nav_types import ActionKind, LegalAction, NavConfig, NavState


def _chunks_to_retrieved_nodes(chunks: List[Chunk]) -> List[str]:
    seen: set[str] = set()
    out: List[str] = []
    for c in chunks:
        for lid in c.line_ids:
            node = f"{c.doc_id}:L{lid}"
            if node not in seen:
                seen.add(node)
                out.append(node)
    return out


def _dedupe_scored(scored: List[Tuple[Chunk, float]]) -> List[Tuple[Chunk, float]]:
    best: Dict[str, Tuple[Chunk, float]] = {}
    for c, score in scored:
        prev = best.get(c.node_id)
        if prev is None or float(score) > float(prev[1]):
            best[c.node_id] = (c, float(score))
    out = list(best.values())
    out.sort(key=lambda x: -x[1])
    return out


def _query_tokens_for_compose(query: str) -> List[str]:
    raw = (query or "").lower()
    toks = re.findall(r"[a-z0-9_]+|[\u4e00-\u9fff]", raw)
    return [t for t in toks if t.strip()]


def _prepare_compose_evidence_text(
    query: str,
    evidence_text: str,
    *,
    budget_chars: int,
    task_type: str,
) -> str:
    text = (evidence_text or "").strip()
    if not text:
        return ""
    if os.environ.get("NAV_COMPOSE_CLEAN_EVIDENCE", "1").strip().lower() in {"0", "false", "no"}:
        return text[: max(1, int(budget_chars))]

    tt = (task_type or "").strip().lower()
    keep_path = tt == "multi_hop"
    blocks: List[Tuple[str, str]] = []
    for raw_block in re.split(r"\n\s*\n(?=\[)", text):
        chunk = raw_block.strip()
        if not chunk:
            continue
        lines = chunk.splitlines()
        if not lines:
            continue
        header = lines[0].strip()
        body_lines = list(lines[1:]) if keep_path else [ln for ln in lines[1:] if not ln.strip().startswith("PATH:")]
        body = "\n".join(body_lines).strip()
        if not body:
            continue
        blocks.append((header, body))
    if not blocks:
        cleaned = re.sub(r"(?m)^PATH:.*\n?", "", text).strip()
        return (cleaned or text)[: max(1, int(budget_chars))]

    should_rerank = tt in {"scope_collection", "regulatory_coverage"}
    if should_rerank:
        toks = _query_tokens_for_compose(query)

        def _score_block(block: Tuple[str, str]) -> Tuple[int, int]:
            body = block[1].lower()
            overlap = sum(1 for t in toks if t in body)
            return (overlap, len(body))

        blocks.sort(key=_score_block, reverse=True)

    deduped: List[Tuple[str, str]] = []
    seen_body: set[str] = set()
    for h, b in blocks:
        b_norm = re.sub(r"\s+", " ", b).strip()
        if not b_norm or b_norm in seen_body:
            continue
        seen_body.add(b_norm)
        deduped.append((h, b))

    out_parts: List[str] = []
    used = 0
    for h, b in deduped:
        piece = f"{h}\n{b}"
        add_len = len(piece) + (2 if out_parts else 0)
        if used + add_len <= int(budget_chars):
            out_parts.append(piece)
            used += add_len
            continue
        remain = int(budget_chars) - used - (2 if out_parts else 0)
        if remain > 40:
            out_parts.append(piece[:remain])
        break
    if out_parts:
        return "\n\n".join(out_parts)
    return text[: max(1, int(budget_chars))]


def _add_scored(state: NavState, scored: List[Tuple[Chunk, float]]) -> int:
    added = 0
    for c, score in scored:
        if c.node_id in state.collected_ids:
            continue
        state.collected_ids.add(c.node_id)
        state.collected.append((c, float(score)))
        added += 1
    return added


def _collect_subtree(ts: ToolSpace, action: LegalAction, state: NavState, config: NavConfig) -> List[Tuple[Chunk, float]]:
    sid = action.section_id
    if not sid:
        return []
    materialize = getattr(ts, "_materialize_leaf_path_chunks", None)
    idx = getattr(ts, "_idx", None)
    if callable(materialize) and idx is not None:
        pool = list(materialize(sid, state.doc_id))
        if pool:
            scored = idx.search(state.query, pool, min(len(pool), int(config.collect_k)), doc_id_filter=state.doc_id)
            return [(c, float(s) + float(config.read_score_bonus)) for c, s in scored]
    rc = ts.read_chunks(sid, state.query, doc_id=state.doc_id, k=int(config.collect_k))
    if isinstance(rc, Refusal):
        state.refusal_events.append(
            {
                "tool": "collect",
                "section_id": sid,
                "status": rc.status,
                "message": rc.message,
                "available_sections": list(rc.available_sections),
            }
        )
        return []
    return [(h.chunk, float(h.score) + float(config.read_score_bonus)) for h in rc]


def _search_doc(ts: ToolSpace, state: NavState, config: NavConfig) -> List[Tuple[Chunk, float]]:
    hits = ts.search(state.query, int(config.search_k), doc_id=state.doc_id)
    return [(h.chunk, float(h.score)) for h in hits]


def _query_variants(query: str, task_type: str) -> List[str]:
    variants: List[str] = []

    def add(text: str) -> None:
        q = re.sub(r"\s+", " ", (text or "").strip())
        if q and q not in variants:
            variants.append(q)

    add(query)
    stripped = re.sub(
        r"(请|根据|列出|列举|说明|回答|文中|本条例|本方案|所有|哪些|多少|是什么|分别|以及|包括|中提到的)",
        " ",
        query or "",
    )
    add(stripped)
    for part in re.split(r"[，,；;。?？]|以及|和|与|及|、", query or ""):
        if len(part.strip()) >= 4:
            add(part)
    if (task_type or "").lower() in ("multi_hop", "scope_collection", "regulatory_coverage"):
        add((query or "") + " 相关条款 定义 条件 范围")
    add((query or "") + " 答案 证据 原文")
    return variants[: max(1, int(os.environ.get("NAV_SAFETY_NET_QUERY_ROUNDS", "3").strip() or "3"))]


_HIER_PATH_RE = re.compile(r"层级路径[“\"]([^”\"]+)[”\"]")


def _norm_heading(text: str) -> str:
    text = re.sub(r"\s+", "", str(text or "").lower())
    text = re.sub(r"[：:。；;，,、（）()《》\"“”'‘’._\\-—\\[\\]【】/\\\\]", "", text)
    return text


def _hier_path_parts(query: str) -> List[str]:
    matches = list(_HIER_PATH_RE.finditer(query or ""))
    if not matches:
        return []
    out: List[str] = []
    for m in matches:
        parts = [p.strip() for p in re.split(r"\s*/\s*", m.group(1)) if p.strip()]
        # The first segment is often the document title; keep only section anchors.
        if len(parts) >= 3:
            keep = parts[-2:]
        elif len(parts) >= 2:
            keep = parts[1:]
        else:
            keep = parts
        for part in keep:
            if part not in out:
                out.append(part)
    return out


def _hier_path_leaf_parts(query: str) -> List[str]:
    """Return only the most specific segment of each quoted hierarchy path."""
    matches = list(_HIER_PATH_RE.finditer(query or ""))
    out: List[str] = []
    for m in matches:
        parts = [p.strip() for p in re.split(r"\s*/\s*", m.group(1)) if p.strip()]
        if not parts:
            continue
        leaf = parts[-1]
        if leaf and leaf not in out:
            out.append(leaf)
    return out


def _scope_focus_query(query: str) -> str:
    m = re.search(r"围绕问题[“\"]([^”\"]+)[”\"]", query or "")
    if m and m.group(1).strip():
        return m.group(1).strip()
    return str(query or "").strip()


def _path_anchor_candidates(ts: ToolSpace, state: NavState) -> List[Tuple[str, float, str]]:
    parts = _hier_path_parts(state.query)
    if (state.task_type or "").lower() == "multi_hop":
        # Multi-hop path prompts include both a parent heading and a concrete
        # leaf fact for each hop. Parent headings are useful for navigation, but
        # they can waste the tight b=500 evidence budget; anchor packing should
        # prioritize the most specific leaf facts.
        leaf_parts = _hier_path_leaf_parts(state.query)
        if leaf_parts:
            parts = leaf_parts
    if not parts:
        return []
    bundle = ts._idx._bundles.get(state.doc_id)
    if not bundle:
        return []
    targets = [(_norm_heading(p), p) for p in parts if _norm_heading(p)]
    if not targets:
        return []

    out: List[Tuple[str, float, str]] = []
    for j, rec in enumerate(bundle.lines):
        line_norm = _norm_heading(rec.content)
        if not line_norm:
            continue
        best = 0.0
        best_part = ""
        for rank, (target_norm, raw_part) in enumerate(targets):
            # Last path segment is most specific; give it the strongest weight.
            specificity = 1.0 + (rank / max(1, len(targets) - 1))
            if line_norm == target_norm:
                score = 6.0 * specificity
            elif target_norm in line_norm or line_norm in target_norm:
                score = 4.0 * specificity
            else:
                common = len(set(target_norm) & set(line_norm))
                denom = max(1, len(set(target_norm)))
                score = (common / denom) * specificity
            if score > best:
                best = score
                best_part = raw_part
        if best >= float(os.environ.get("NAV_PATH_ANCHOR_MIN_MATCH", "3.2").strip() or "3.2"):
            out.append((f"{state.doc_id}:L{rec.line_id}", best, best_part))
    out.sort(key=lambda x: -x[1])
    return out[: max(1, int(os.environ.get("NAV_PATH_ANCHOR_MAX_SECTIONS", "3").strip() or "3"))]


def _path_anchor_safety_net(
    ts: ToolSpace,
    state: NavState,
    config: NavConfig,
) -> List[Tuple[Chunk, float]]:
    if os.environ.get("NAV_PATH_ANCHOR_SAFETY_NET", "1").strip().lower() in {"0", "false", "no", "off"}:
        return []
    allowed_raw = os.environ.get("NAV_PATH_ANCHOR_TASK_TYPES", "scope_collection,regulatory_coverage")
    allowed = {x.strip().lower() for x in allowed_raw.split(",") if x.strip()}
    if allowed and (state.task_type or "").lower() not in allowed:
        return []
    materialize = getattr(ts, "_materialize_leaf_path_chunks", None)
    if not callable(materialize):
        return []
    anchors = _path_anchor_candidates(ts, state)
    if not anchors:
        return []
    bonus = float(os.environ.get("NAV_PATH_ANCHOR_SCORE_BONUS", "55.0").strip() or "55.0")
    k = max(1, int(os.environ.get("NAV_PATH_ANCHOR_K", str(config.collect_k * 3)).strip() or config.collect_k * 3))
    all_scored: List[Tuple[Chunk, float]] = []
    for anchor_rank, (section_id, anchor_score, _matched_part) in enumerate(anchors):
        pool = list(materialize(section_id, state.doc_id))
        if not pool:
            continue
        if (state.task_type or "").lower() in ("scope_collection", "regulatory_coverage"):
            focus = _scope_focus_query(state.query)
            if focus and focus != state.query:
                scored = ts._idx.search(focus, pool, min(len(pool), k), doc_id_filter=state.doc_id)
            else:
                # Without a concrete focus question, preserve tree order so b=500
                # starts at the anchored range.
                scored = [(c, 0.0) for c in pool[:k]]
            if not scored:
                scored = [(c, 0.0) for c in pool[:k]]
        else:
            scored = ts._idx.search(state.query, pool, min(len(pool), k), doc_id_filter=state.doc_id)
            if not scored:
                scored = [(c, 0.0) for c in pool[:k]]
        for local_rank, (chunk, score) in enumerate(scored):
            adjusted = bonus + float(anchor_score) + float(score) - (anchor_rank * 0.1) - (local_rank * 0.01)
            all_scored.append((chunk, adjusted))
    return _dedupe_scored(all_scored)


def _multi_hop_path_window_safety_net(
    ts: ToolSpace,
    state: NavState,
    config: NavConfig,
) -> List[Tuple[Chunk, float]]:
    """For path-anchored multi-hop tasks, pack a compact local window per path anchor."""
    if (state.task_type or "").lower() != "multi_hop":
        return []
    if os.environ.get("NAV_MULTI_HOP_PATH_WINDOW_SAFETY_NET", "1").strip().lower() in {"0", "false", "no", "off"}:
        return []
    bundle = ts._idx._bundles.get(state.doc_id)
    if not bundle:
        return []
    anchors = _path_anchor_candidates(ts, state)
    if not anchors:
        return []

    before = max(0, int(os.environ.get("NAV_MULTI_HOP_PATH_WINDOW_BEFORE", "4").strip() or "4"))
    after = max(0, int(os.environ.get("NAV_MULTI_HOP_PATH_WINDOW_AFTER", "2").strip() or "2"))
    max_chars = max(120, int(os.environ.get("NAV_MULTI_HOP_PATH_WINDOW_MAX_CHARS", "340").strip() or "340"))
    bonus = float(os.environ.get("NAV_MULTI_HOP_PATH_WINDOW_SCORE_BONUS", "95.0").strip() or "95.0")
    atom_enabled = os.environ.get("NAV_MULTI_HOP_PATH_ATOM_SAFETY_NET", "1").strip().lower() not in {
        "0",
        "false",
        "no",
        "off",
    }
    atom_bonus = float(os.environ.get("NAV_MULTI_HOP_PATH_ATOM_SCORE_BONUS", "115.0").strip() or "115.0")
    atom_chars = max(80, int(os.environ.get("NAV_MULTI_HOP_PATH_ATOM_MAX_CHARS", "520").strip() or "520"))
    atom_neighbor_bonus = float(
        os.environ.get("NAV_MULTI_HOP_PATH_NEIGHBOR_ATOM_SCORE_BONUS", "108.0").strip() or "108.0"
    )
    atom_min_chars = max(6, int(os.environ.get("NAV_MULTI_HOP_PATH_ATOM_MIN_CHARS", "10").strip() or "10"))

    out: List[Tuple[Chunk, float]] = []
    seen: set[Tuple[int, int]] = set()
    seen_atoms: set[int] = set()
    for anchor_rank, (section_id, anchor_score, _matched_part) in enumerate(anchors):
        loc = ts._idx._node_to_doc_line.get(section_id)
        if not loc or loc[0] != state.doc_id:
            continue
        anchor_pos = int(loc[1])
        start = max(0, anchor_pos - before)
        end = min(len(bundle.lines), anchor_pos + after + 1)
        if start >= end or (start, end) in seen:
            continue
        seen.add((start, end))

        text_parts: List[str] = []
        line_ids: List[int] = []
        for j in range(start, end):
            rec = bundle.lines[j]
            line_text = str(rec.content or "").strip()
            if not line_text:
                continue
            text_parts.append(line_text)
            line_ids.append(int(rec.line_id))
        if not text_parts or not line_ids:
            continue

        if atom_enabled:
            for j in range(start, end):
                rec = bundle.lines[j]
                line_no = int(rec.line_id)
                if line_no in seen_atoms:
                    continue
                anchor_text = str(rec.content or "").strip()
                if len(anchor_text) < atom_min_chars:
                    continue
                seen_atoms.add(line_no)
                is_anchor_line = j == anchor_pos
                atom_chunk = Chunk(
                    node_id=f"{state.doc_id}:MHOPATOM{line_no}",
                    doc_id=state.doc_id,
                    text=anchor_text[:atom_chars].rstrip(),
                    line_ids=(line_no,),
                    section_id=section_id,
                )
                local_distance = abs(j - anchor_pos)
                base_atom_bonus = atom_bonus if is_anchor_line else atom_neighbor_bonus
                atom_score = base_atom_bonus + float(anchor_score) - (anchor_rank * 0.05) - (local_distance * 0.01)
                out.append((atom_chunk, atom_score))

        text = "\n".join(text_parts)
        if len(text) > max_chars:
            text = text[:max_chars].rstrip()
        chunk = Chunk(
            node_id=f"{state.doc_id}:MHOPPATH{line_ids[0]}_{line_ids[-1]}",
            doc_id=state.doc_id,
            text=text,
            line_ids=tuple(line_ids),
            section_id=section_id,
        )
        score = bonus + float(anchor_score) - (anchor_rank * 0.05)
        out.append((chunk, score))
    return _dedupe_scored(out)


def _path_focus_block_safety_net(
    ts: ToolSpace,
    state: NavState,
    config: NavConfig,
) -> List[Tuple[Chunk, float]]:
    """For path-anchored list tasks, retrieve focused local blocks inside the anchored subtree."""
    if os.environ.get("NAV_PATH_FOCUS_BLOCK_SAFETY_NET", "1").strip().lower() in {"0", "false", "no", "off"}:
        return []
    if (state.task_type or "").lower() not in ("scope_collection", "regulatory_coverage"):
        return []
    focus = _scope_focus_query(state.query)
    if not focus:
        return []
    bounds_for_path = getattr(ts, "_subtree_bounds_for_section_path", None)
    if not callable(bounds_for_path):
        return []
    anchors = _path_anchor_candidates(ts, state)
    if not anchors:
        return []
    bundle = ts._idx._bundles.get(state.doc_id)
    if not bundle:
        return []
    node_to_chunk = {c.node_id: c for c in ts._idx.small_chunks if c.doc_id == state.doc_id}
    if not node_to_chunk:
        return []

    levels = bundle.levels_for_tree
    parents = ts._idx._doc_parents.get(state.doc_id, [])
    seed_k = max(1, int(os.environ.get("NAV_PATH_FOCUS_BLOCK_SEED_K", str(config.search_k * 2)).strip() or config.search_k * 2))
    max_lines = max(1, int(os.environ.get("NAV_PATH_FOCUS_BLOCK_MAX_LINES", "12").strip() or "12"))
    max_chars = max(80, int(os.environ.get("NAV_PATH_FOCUS_BLOCK_MAX_CHARS", "900").strip() or "900"))
    bonus = float(os.environ.get("NAV_PATH_FOCUS_BLOCK_SCORE_BONUS", "75.0").strip() or "75.0")
    out: List[Tuple[Chunk, float]] = []

    for anchor_rank, (section_id, anchor_score, _matched_part) in enumerate(anchors):
        bounds = bounds_for_path(section_id, state.doc_id)
        if not bounds:
            continue
        bound_start, bound_end = bounds
        if bound_start >= bound_end:
            continue
        if bound_end <= bound_start + 2:
            bound_end = min(len(bundle.lines), bound_start + max_lines)
        pool: List[Chunk] = []
        for j in range(bound_start, bound_end):
            nid = f"{state.doc_id}:L{bundle.lines[j].line_id}"
            chunk = node_to_chunk.get(nid)
            if chunk is not None:
                pool.append(chunk)
        if not pool:
            continue

        seeds = ts._idx.search(focus, pool, min(len(pool), seed_k), doc_id_filter=state.doc_id)
        if not seeds:
            seeds = [(c, 0.0) for c in pool[:seed_k]]

        for seed_rank, (seed, seed_score) in enumerate(seeds):
            loc = ts._idx._node_to_doc_line.get(seed.node_id)
            if not loc or loc[0] != state.doc_id:
                continue
            seed_pos = int(loc[1])
            if seed_pos < bound_start or seed_pos >= bound_end:
                continue

            start = seed_pos
            parent = parents[seed_pos] if seed_pos < len(parents) else None
            if parent is not None and bound_start <= parent < seed_pos:
                parent_level = levels[parent] if parent < len(levels) else 0
                seed_level = levels[seed_pos] if seed_pos < len(levels) else 0
                # If the seed is a child item, include its immediate heading so list answers keep context.
                if parent_level > 0 and (seed_level == 0 or seed_level > parent_level):
                    start = parent

            base_level = levels[start] if start < len(levels) else 0
            end = min(bound_end, start + max_lines)
            if base_level > 0:
                for j in range(start + 1, min(bound_end, start + max_lines)):
                    lev = levels[j] if j < len(levels) else 0
                    if lev > 0 and lev <= base_level:
                        end = j
                        break
            if end <= start + 1:
                # Some OCR-derived trees mark a subsection title and its body at
                # the same level. In that case, keep a small local run instead
                # of returning the bare heading only.
                end = min(bound_end, start + max_lines)

            block_lines = list(range(start, end))
            if not block_lines:
                continue
            text_parts: List[str] = []
            line_ids: List[int] = []
            for j in block_lines:
                rec = bundle.lines[j]
                line_text = str(rec.content or "").strip()
                if not line_text:
                    continue
                text_parts.append(line_text)
                line_ids.append(int(rec.line_id))
            if not text_parts or not line_ids:
                continue

            text = "\n".join(text_parts)
            if len(text) > max_chars:
                text = text[:max_chars].rstrip()
            chunk = Chunk(
                node_id=f"{state.doc_id}:PATHFOCUS{line_ids[0]}_{line_ids[-1]}",
                doc_id=state.doc_id,
                text=text,
                line_ids=tuple(line_ids),
                section_id=section_id,
            )
            score = bonus + float(anchor_score) + float(seed_score) - (anchor_rank * 0.1) - (seed_rank * 0.03)
            out.append((chunk, score))
    return _dedupe_scored(out)


def _hierarchy_safety_net(
    ts: ToolSpace,
    state: NavState,
    config: NavConfig,
) -> List[Tuple[Chunk, float]]:
    if os.environ.get("NAV_HIER_SAFETY_NET", "1").strip().lower() in {"0", "false", "no", "off"}:
        return []
    pool = ts.leaf_path_search_pool(state.doc_id)
    if not pool:
        return []
    k = max(1, min(len(pool), int(os.environ.get("NAV_SAFETY_NET_K", str(config.search_k * 3)).strip() or config.search_k * 3)))
    bonus = float(os.environ.get("NAV_SAFETY_NET_SCORE_BONUS", "12.0").strip() or "12.0")
    all_scored: List[Tuple[Chunk, float]] = []
    for qi, q in enumerate(_query_variants(state.query, state.task_type), start=0):
        weight = 1.0 if qi == 0 else max(0.45, 0.82 ** qi)
        hits = ts._idx.search(q, pool, min(len(pool), k), doc_id_filter=state.doc_id)
        all_scored.extend((c, float(s) * weight + bonus) for c, s in hits)
    return _dedupe_scored(all_scored)


def _multi_hop_neighbor_block_safety_net(
    ts: ToolSpace,
    state: NavState,
    config: NavConfig,
) -> List[Tuple[Chunk, float]]:
    """Pack local neighboring lines for multi-hop tasks where evidence is adjacent."""
    if (state.task_type or "").lower() != "multi_hop":
        return []
    if os.environ.get("NAV_MULTI_HOP_BLOCK_SAFETY_NET", "1").strip().lower() in {"0", "false", "no", "off"}:
        return []
    bundle = ts._idx._bundles.get(state.doc_id)
    if not bundle:
        return []
    node_to_chunk = {c.node_id: c for c in ts._idx.small_chunks if c.doc_id == state.doc_id}
    pool = list(node_to_chunk.values())
    window_size = max(2, int(os.environ.get("NAV_MULTI_HOP_WINDOW_SIZE", "8").strip() or "8"))
    window_stride = max(1, int(os.environ.get("NAV_MULTI_HOP_WINDOW_STRIDE", "8").strip() or "8"))
    window_pool: List[Chunk] = []
    for start in range(0, len(bundle.lines), window_stride):
        part = bundle.lines[start : start + window_size]
        if not part:
            continue
        window_pool.append(
            Chunk(
                node_id=f"{state.doc_id}:MHOPWIN{start}",
                doc_id=state.doc_id,
                text="\n".join(str(r.content or "") for r in part),
                line_ids=tuple(int(r.line_id) for r in part),
            )
        )
    if not pool and not window_pool:
        return []

    seed_k = max(1, int(os.environ.get("NAV_MULTI_HOP_BLOCK_SEED_K", str(config.search_k * 2)).strip() or config.search_k * 2))
    before = max(0, int(os.environ.get("NAV_MULTI_HOP_BLOCK_BEFORE", "1").strip() or "1"))
    after = max(1, int(os.environ.get("NAV_MULTI_HOP_BLOCK_AFTER", "6").strip() or "6"))
    max_chars = max(120, int(os.environ.get("NAV_MULTI_HOP_BLOCK_MAX_CHARS", "900").strip() or "900"))
    bonus = float(os.environ.get("NAV_MULTI_HOP_BLOCK_SCORE_BONUS", "35.0").strip() or "35.0")
    window_bonus = float(os.environ.get("NAV_MULTI_HOP_WINDOW_SCORE_BONUS", "45.0").strip() or "45.0")

    out: List[Tuple[Chunk, float]] = []
    if window_pool:
        window_k = max(1, int(os.environ.get("NAV_MULTI_HOP_WINDOW_K", str(config.search_k)).strip() or config.search_k))
        window_scored: List[Tuple[Chunk, float]] = []
        for qi, q in enumerate(_query_variants(state.query, state.task_type), start=0):
            weight = 1.0 if qi == 0 else max(0.45, 0.82 ** qi)
            hits = ts._idx.search(q, window_pool, min(len(window_pool), window_k), doc_id_filter=state.doc_id)
            window_scored.extend((c, float(s) * weight + window_bonus) for c, s in hits)
        out.extend(_dedupe_scored(window_scored)[:window_k])

    if not pool:
        return _dedupe_scored(out)
    seeds: List[Tuple[Chunk, float]] = []
    for qi, q in enumerate(_query_variants(state.query, state.task_type), start=0):
        weight = 1.0 if qi == 0 else max(0.45, 0.82 ** qi)
        hits = ts._idx.search(q, pool, min(len(pool), seed_k), doc_id_filter=state.doc_id)
        seeds.extend((c, float(s) * weight) for c, s in hits)
    seeds = _dedupe_scored(seeds)[:seed_k]

    seen: set[Tuple[int, int]] = set()
    for seed_rank, (seed, seed_score) in enumerate(seeds):
        loc = ts._idx._node_to_doc_line.get(seed.node_id)
        if not loc or loc[0] != state.doc_id:
            continue
        seed_pos = int(loc[1])
        start = max(0, seed_pos - before)
        end = min(len(bundle.lines), seed_pos + after + 1)
        if start >= end or (start, end) in seen:
            continue
        seen.add((start, end))
        text_parts: List[str] = []
        line_ids: List[int] = []
        for j in range(start, end):
            rec = bundle.lines[j]
            line_text = str(rec.content or "").strip()
            if not line_text:
                continue
            text_parts.append(line_text)
            line_ids.append(int(rec.line_id))
        if not text_parts or not line_ids:
            continue
        text = "\n".join(text_parts)
        if len(text) > max_chars:
            text = text[:max_chars].rstrip()
        chunk = Chunk(
            node_id=f"{state.doc_id}:MHOPBLOCK{line_ids[0]}_{line_ids[-1]}",
            doc_id=state.doc_id,
            text=text,
            line_ids=tuple(line_ids),
            section_id=seed.section_id,
        )
        score = bonus + float(seed_score) - (seed_rank * 0.03)
        out.append((chunk, score))
    return _dedupe_scored(out)


def _scope_line_safety_net(
    ts: ToolSpace,
    state: NavState,
    config: NavConfig,
) -> List[Tuple[Chunk, float]]:
    if (state.task_type or "").lower() not in ("scope_collection", "regulatory_coverage"):
        return []
    if os.environ.get("NAV_SCOPE_LINE_SAFETY_NET", "1").strip().lower() in {"0", "false", "no", "off"}:
        return []
    pool = [c for c in ts._idx.small_chunks if c.doc_id == state.doc_id]
    if not pool:
        return []
    k = max(1, min(len(pool), int(os.environ.get("NAV_SCOPE_LINE_SAFETY_K", str(config.search_k * 4)).strip() or config.search_k * 4)))
    bonus = float(os.environ.get("NAV_SCOPE_LINE_SCORE_BONUS", "13.0").strip() or "13.0")
    all_scored: List[Tuple[Chunk, float]] = []
    for qi, q in enumerate(_query_variants(state.query, state.task_type), start=0):
        weight = 1.0 if qi == 0 else max(0.45, 0.82 ** qi)
        hits = ts._idx.search(q, pool, min(len(pool), k), doc_id_filter=state.doc_id)
        all_scored.extend((c, float(s) * weight + bonus) for c, s in hits)
    return _dedupe_scored(all_scored)


def _scope_contiguous_block_safety_net(
    ts: ToolSpace,
    state: NavState,
    config: NavConfig,
) -> List[Tuple[Chunk, float]]:
    """For list-style tasks, expand likely heading hits into the following gold-tree lines."""
    if (state.task_type or "").lower() not in ("scope_collection", "regulatory_coverage"):
        return []
    if os.environ.get("NAV_SCOPE_BLOCK_SAFETY_NET", "1").strip().lower() in {"0", "false", "no", "off"}:
        return []
    bundle = ts._idx._bundles.get(state.doc_id)
    if not bundle:
        return []
    node_to_chunk = {c.node_id: c for c in ts._idx.small_chunks if c.doc_id == state.doc_id}
    pool = list(node_to_chunk.values())
    if not pool:
        return []

    seed_k = max(1, int(os.environ.get("NAV_SCOPE_BLOCK_SEED_K", "8").strip() or "8"))
    max_lines = max(1, int(os.environ.get("NAV_SCOPE_BLOCK_MAX_LINES", "14").strip() or "14"))
    bonus = float(os.environ.get("NAV_SCOPE_BLOCK_SCORE_BONUS", "25.0").strip() or "25.0")
    seeds: List[Tuple[Chunk, float]] = []
    for qi, q in enumerate(_query_variants(state.query, state.task_type), start=0):
        weight = 1.0 if qi == 0 else max(0.45, 0.82 ** qi)
        hits = ts._idx.search(q, pool, min(len(pool), seed_k), doc_id_filter=state.doc_id)
        seeds.extend((c, float(s) * weight) for c, s in hits)
    seeds = _dedupe_scored(seeds)[:seed_k]

    levels = bundle.levels_for_tree
    out: List[Tuple[Chunk, float]] = []
    seen: set[str] = set()
    for seed_rank, (seed, seed_score) in enumerate(seeds):
        loc = ts._idx._node_to_doc_line.get(seed.node_id)
        if not loc or loc[0] != state.doc_id:
            continue
        start = int(loc[1])
        if start < 0 or start >= len(bundle.lines):
            continue
        base_level = levels[start] if start < len(levels) else 0
        end = min(len(bundle.lines), start + max_lines)
        if base_level > 0:
            for j in range(start + 1, min(len(bundle.lines), start + max_lines)):
                lev = levels[j] if j < len(levels) else 0
                if lev > 0 and lev <= base_level:
                    end = j
                    break
        for offset, j in enumerate(range(start, end)):
            nid = f"{state.doc_id}:L{bundle.lines[j].line_id}"
            chunk = node_to_chunk.get(nid)
            if chunk is None or chunk.node_id in seen:
                continue
            seen.add(chunk.node_id)
            # Keep contiguous list items ahead of unrelated dense hits while preserving local order.
            score = bonus + float(seed_score) - (seed_rank * 0.05) - (offset * 0.01)
            out.append((chunk, score))
    return _dedupe_scored(out)


def run_nav_episode(
    tools: HierarchicalTools,
    query: str,
    *,
    doc_id: str,
    budget_chars: int,
    task_type: str = "unknown",
    compose_format_constraints: str = "",
    compose_answer: bool = True,
    policy: str = "rule",
    config: Optional[NavConfig] = None,
) -> EpisodeResult:
    if not doc_id:
        raise ValueError("Nav Agent requires a non-empty doc_id")
    from agent_delivery.code.llm_config import load_llm_env, require_llm_env  # type: ignore

    load_llm_env()
    require_llm_env(context="Nav Agent")
    cfg = config or NavConfig(policy="llm")
    nav_policy = (policy or cfg.policy or "llm").strip().lower()
    if nav_policy != "llm":
        raise ValueError(
            f"Nav Agent 仅支持 llm 策略（须配置 OPENAI_API_KEY）；收到 policy={policy!r}。"
            "请设置 --nav-policy llm 或删除 NAV_POLICY=rule。"
        )
    cfg.policy = "llm"
    retrieval_t0 = time.perf_counter()
    ts = ToolSpace(tools)
    state = NavState(doc_id=doc_id, query=query, task_type=task_type)
    steps: List[AgentStep] = []
    section_ids = ts.sections_for_doc(doc_id)

    for step_idx in range(1, max(1, int(cfg.max_steps)) + 1):
        projection = build_projection(
            ts,
            doc_id=doc_id,
            query=query,
            scope=state.current_scope,
            config=cfg,
        )
        actions = build_legal_actions(state, projection, step_idx=step_idx, config=cfg)
        chosen, llm_meta = choose_llm_action(state, projection, actions, step_idx=step_idx, config=cfg)

        detail: Dict[str, Any] = {
            "action_id": chosen.action_id,
            "kind": chosen.kind.value,
            "section_id": chosen.section_id,
            "scope": state.current_scope,
            "projection_chars": len(projection.text),
            "n_visible_sections": len(projection.visible_sections),
            "n_legal_actions": len(actions),
            "legal_actions": [a.prompt_line() for a in actions],
        }
        if llm_meta:
            detail["llm"] = llm_meta

        if chosen.kind == ActionKind.FINISH:
            steps.append(AgentStep(step_idx=len(steps) + 1, action="nav_finish", detail=detail))
            state.action_history.append({**detail, "step_idx": step_idx})
            break
        if chosen.kind == ActionKind.EXPAND:
            state.push_scope(chosen.section_id)
            steps.append(AgentStep(step_idx=len(steps) + 1, action="nav_expand", detail=detail))
            state.action_history.append({**detail, "step_idx": step_idx})
            continue
        if chosen.kind == ActionKind.BACK:
            new_scope = state.back()
            detail["new_scope"] = new_scope
            steps.append(AgentStep(step_idx=len(steps) + 1, action="nav_back", detail=detail))
            state.action_history.append({**detail, "step_idx": step_idx})
            continue
        if chosen.kind == ActionKind.SEARCH:
            scored = _search_doc(ts, state, cfg)
            added = _add_scored(state, scored)
            detail["n_hits"] = len(scored)
            detail["n_added"] = added
            steps.append(AgentStep(step_idx=len(steps) + 1, action="nav_search", detail=detail))
            state.action_history.append({**detail, "step_idx": step_idx})
            continue
        if chosen.kind == ActionKind.COLLECT:
            scored = _collect_subtree(ts, chosen, state, cfg)
            added = _add_scored(state, scored)
            detail["n_hits"] = len(scored)
            detail["n_added"] = added
            steps.append(AgentStep(step_idx=len(steps) + 1, action="nav_collect", detail=detail))
            state.action_history.append({**detail, "step_idx": step_idx})
            continue

    path_focus_block_scored = _path_focus_block_safety_net(ts, state, cfg)
    if path_focus_block_scored:
        anchors = _path_anchor_candidates(ts, state)
        steps.append(
            AgentStep(
                step_idx=len(steps) + 1,
                action="nav_path_focus_block_safety_net",
                detail={
                    "n_hits": len(path_focus_block_scored),
                    "anchors": [
                        {"section_id": sid, "score": score, "matched_path_part": part}
                        for sid, score, part in anchors
                    ],
                    "seed_k": int(os.environ.get("NAV_PATH_FOCUS_BLOCK_SEED_K", str(cfg.search_k * 2)).strip() or cfg.search_k * 2),
                    "max_lines": int(os.environ.get("NAV_PATH_FOCUS_BLOCK_MAX_LINES", "12").strip() or "12"),
                    "score_bonus": float(os.environ.get("NAV_PATH_FOCUS_BLOCK_SCORE_BONUS", "75.0").strip() or "75.0"),
                },
            )
        )
    path_anchor_scored = _path_anchor_safety_net(ts, state, cfg)
    if path_anchor_scored:
        anchors = _path_anchor_candidates(ts, state)
        steps.append(
            AgentStep(
                step_idx=len(steps) + 1,
                action="nav_path_anchor_safety_net",
                detail={
                    "n_hits": len(path_anchor_scored),
                    "anchors": [
                        {"section_id": sid, "score": score, "matched_path_part": part}
                        for sid, score, part in anchors
                    ],
                    "score_bonus": float(os.environ.get("NAV_PATH_ANCHOR_SCORE_BONUS", "55.0").strip() or "55.0"),
                },
            )
        )
    multi_hop_path_window_scored = _multi_hop_path_window_safety_net(ts, state, cfg)
    if multi_hop_path_window_scored:
        anchors = _path_anchor_candidates(ts, state)
        steps.append(
            AgentStep(
                step_idx=len(steps) + 1,
                action="nav_multi_hop_path_window_safety_net",
                detail={
                    "n_hits": len(multi_hop_path_window_scored),
                    "anchors": [
                        {"section_id": sid, "score": score, "matched_path_part": part}
                        for sid, score, part in anchors
                    ],
                    "before": int(os.environ.get("NAV_MULTI_HOP_PATH_WINDOW_BEFORE", "4").strip() or "4"),
                    "after": int(os.environ.get("NAV_MULTI_HOP_PATH_WINDOW_AFTER", "2").strip() or "2"),
                    "max_chars": int(os.environ.get("NAV_MULTI_HOP_PATH_WINDOW_MAX_CHARS", "340").strip() or "340"),
                    "score_bonus": float(os.environ.get("NAV_MULTI_HOP_PATH_WINDOW_SCORE_BONUS", "95.0").strip() or "95.0"),
                },
            )
        )
    multi_hop_block_scored = _multi_hop_neighbor_block_safety_net(ts, state, cfg)
    if multi_hop_block_scored:
        steps.append(
            AgentStep(
                step_idx=len(steps) + 1,
                action="nav_multi_hop_block_safety_net",
                detail={
                    "n_hits": len(multi_hop_block_scored),
                    "seed_k": int(os.environ.get("NAV_MULTI_HOP_BLOCK_SEED_K", str(cfg.search_k * 2)).strip() or cfg.search_k * 2),
                    "before": int(os.environ.get("NAV_MULTI_HOP_BLOCK_BEFORE", "1").strip() or "1"),
                    "after": int(os.environ.get("NAV_MULTI_HOP_BLOCK_AFTER", "6").strip() or "6"),
                    "score_bonus": float(os.environ.get("NAV_MULTI_HOP_BLOCK_SCORE_BONUS", "35.0").strip() or "35.0"),
                },
            )
        )
    safety_scored = _hierarchy_safety_net(ts, state, cfg)
    if safety_scored:
        steps.append(
            AgentStep(
                step_idx=len(steps) + 1,
                action="nav_hierarchy_safety_net",
                detail={
                    "n_hits": len(safety_scored),
                    "k": int(os.environ.get("NAV_SAFETY_NET_K", str(cfg.search_k * 3)).strip() or cfg.search_k * 3),
                    "score_bonus": float(os.environ.get("NAV_SAFETY_NET_SCORE_BONUS", "12.0").strip() or "12.0"),
                    "query_rounds": len(_query_variants(state.query, state.task_type)),
                },
            )
        )
    scope_line_scored = _scope_line_safety_net(ts, state, cfg)
    if scope_line_scored:
        steps.append(
            AgentStep(
                step_idx=len(steps) + 1,
                action="nav_scope_line_safety_net",
                detail={
                    "n_hits": len(scope_line_scored),
                    "k": int(os.environ.get("NAV_SCOPE_LINE_SAFETY_K", str(cfg.search_k * 4)).strip() or cfg.search_k * 4),
                    "score_bonus": float(os.environ.get("NAV_SCOPE_LINE_SCORE_BONUS", "13.0").strip() or "13.0"),
                    "query_rounds": len(_query_variants(state.query, state.task_type)),
                },
            )
        )
    scope_block_scored = _scope_contiguous_block_safety_net(ts, state, cfg)
    if scope_block_scored:
        steps.append(
            AgentStep(
                step_idx=len(steps) + 1,
                action="nav_scope_block_safety_net",
                detail={
                    "n_hits": len(scope_block_scored),
                    "seed_k": int(os.environ.get("NAV_SCOPE_BLOCK_SEED_K", "8").strip() or "8"),
                    "max_lines": int(os.environ.get("NAV_SCOPE_BLOCK_MAX_LINES", "14").strip() or "14"),
                    "score_bonus": float(os.environ.get("NAV_SCOPE_BLOCK_SCORE_BONUS", "25.0").strip() or "25.0"),
                },
            )
        )
    scored_chunks = _dedupe_scored(
        list(state.collected)
        + path_focus_block_scored
        + path_anchor_scored
        + multi_hop_path_window_scored
        + multi_hop_block_scored
        + safety_scored
        + scope_line_scored
        + scope_block_scored
    )
    fill = evaluate_at_budget(scored_chunks, budget_chars=budget_chars)
    retrieval_seconds = time.perf_counter() - retrieval_t0
    composed = ""
    compose_seconds = 0.0
    if compose_answer:
        compose_t0 = time.perf_counter()
        max_ans = min(1024, max(256, int(budget_chars)))
        extra_mh_constraint = ""
        if (task_type or "").strip().lower() == "multi_hop":
            extra_mh_constraint = (
                "multi_hop 约束：fact_1 与 fact_2 必须分别覆盖两跳信息，"
                "final_answer 必须整合二者，任一缺失视为不完整。"
            )
        fc = compose_format_constraints
        if extra_mh_constraint:
            fc = (f"{fc}\n{extra_mh_constraint}" if fc else extra_mh_constraint)
        compose_evidence = _prepare_compose_evidence_text(
            query,
            fill.evidence_text or "",
            budget_chars=int(budget_chars),
            task_type=task_type or "niche_fact",
        )
        composed = compose_answer_llm(
            query,
            task_type=task_type or "niche_fact",
            evidence_text=compose_evidence,
            max_answer_chars=max_ans,
            budget_chars=int(budget_chars),
            format_constraints=fc,
        )
        compose_seconds = time.perf_counter() - compose_t0
        steps.append(
            AgentStep(
                step_idx=len(steps) + 1,
                action="compose_answer",
                detail={
                    "evidence_chars": fill.evidence_chars_actual,
                    "n_chunks_kept": fill.n_chunks_kept,
                    "truncated_last": fill.truncated_last,
                },
            )
        )

    return EpisodeResult(
        representation=f"hierarchical_nav_{cfg.policy}",
        steps=steps,
        scored_chunks=scored_chunks,
        kept_chunks=fill.kept_chunks,
        evidence_text=fill.evidence_text,
        evidence_chars_actual=fill.evidence_chars_actual,
        retrieved_nodes=_chunks_to_retrieved_nodes(list(fill.kept_chunks)),
        composed_answer=composed,
        section_ids=list(section_ids),
        trajectory_length=len(steps),
        truncated_last=fill.truncated_last,
        refusal_events=list(state.refusal_events),
        phase_timings={
            "retrieval_framework_seconds": retrieval_seconds,
            "compose_seconds": compose_seconds,
            "online_response_seconds": retrieval_seconds + compose_seconds,
        },
    )
