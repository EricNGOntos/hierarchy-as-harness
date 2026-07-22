"""Nav COMPOSE packing: parent-scoped rank + one-level indent tree.

Parent sections are path headers only (not competing evidence units).
Child score = own_unit + w_conf * collect_confidence (default w_conf=0.5).
Group order: group_priority (external rank), then max child score, then doc order.

Packing modes (NavConfig.compose_packing_mode):
- waterfill (default): when greedy must drop children, reserve a coverage slice for
  cross-group snippets, then enrich snippets back to full text by rerank.
- greedy: fill full text by group/score until budget (kept for ablation / override).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

from agent_delivery.code.index_retrieval import Chunk
from agent_delivery.code.load_data import line_node_id
from agent_delivery.code.tool_space import ToolSpace, is_corpus_doc_id
from path_ledger import doc_id_for

from nav_types import NavConfig, NavState


@dataclass
class ComposeFillResult:
    kept_chunks: List[Chunk]
    evidence_text: str
    evidence_chars_actual: int
    n_chunks_kept: int
    truncated_last: bool
    scored_chunks: List[Tuple[Chunk, float]]
    dropped_any: bool = False


def _clamp01(x: float) -> float:
    return max(0.0, min(1.0, float(x)))


def _section_doc_id(ts: ToolSpace, section_id: str, fallback_doc_id: str = "") -> str:
    """Resolve owning doc for a section (chunk owner / synthetic / episode fallback)."""
    sid = str(section_id or "").strip()
    if not sid:
        return str(fallback_doc_id or "")
    idx = getattr(ts, "_idx", None)
    if idx is not None:
        loc = getattr(idx, "_node_to_doc_line", {}).get(sid)
        if loc:
            return str(loc[0])
        synth = getattr(ts, "_synthetic_doc_id", None)
        if callable(synth):
            did = synth(sid)
            if did and not is_corpus_doc_id(did):
                return str(did)
    parsed = doc_id_for(sid)
    if parsed and not is_corpus_doc_id(parsed):
        return parsed
    fb = str(fallback_doc_id or "")
    return "" if is_corpus_doc_id(fb) else fb


def evidence_owner_section_id(chunk: Chunk) -> str:
    """Section that owns a hydrated evidence chunk (strip __path/__intro suffixes)."""
    nid = str(getattr(chunk, "node_id", "") or "").strip()
    for suf in ("__path", "__intro", "__outline", "__self"):
        if nid.endswith(suf):
            return nid[: -len(suf)]
    sid = str(getattr(chunk, "section_id", "") or "").strip()
    return nid or sid


def unit_score_for_evidence_chunk(chunk: Chunk, unit_scores: Dict[str, float]) -> float:
    """Map leaf/path materialize ids onto hybrid unit scores."""
    scores = unit_scores or {}
    nid = str(getattr(chunk, "node_id", "") or "")
    if nid.endswith("__path"):
        base = nid[: -len("__path")]
        return float(scores.get(base, 0.0) or 0.0)
    if nid.endswith("__intro"):
        base = nid[: -len("__intro")]
        return float(scores.get(f"{base}__self", scores.get(base, 0.0)) or 0.0)
    if nid.endswith("__outline"):
        base = nid[: -len("__outline")]
        sid = str(getattr(chunk, "section_id", "") or "")
        return float(scores.get(sid, scores.get(base, 0.0)) or 0.0)
    return float(scores.get(nid, 0.0) or 0.0)


def _direct_parent_id(ts: ToolSpace, section_id: str, doc_id: str) -> Optional[str]:
    sid = str(section_id or "").strip()
    if not sid:
        return None
    resolved = _section_doc_id(ts, sid, doc_id)
    if not resolved:
        return None
    idx = getattr(ts, "_idx", None)
    if idx is None:
        return None
    loc = getattr(idx, "_node_to_doc_line", {}).get(sid)
    if not loc or loc[0] != resolved:
        return None
    _, j = loc
    parents = getattr(idx, "_doc_parents", {}).get(resolved, [])
    b = getattr(idx, "_bundles", {}).get(resolved)
    if not b or j >= len(parents):
        return None
    p = parents[j]
    if p is None or p < 0 or p >= len(b.lines):
        return None
    return line_node_id(resolved, b.lines[p].line_id)


def _section_title(ts: ToolSpace, section_id: str, doc_id: str, *, max_chars: int = 40) -> str:
    sid = str(section_id or "").strip()
    if not sid:
        return ""
    resolved = _section_doc_id(ts, sid, doc_id)
    idx = getattr(ts, "_idx", None)
    if idx is None:
        return sid.split(":")[-1]
    loc = getattr(idx, "_node_to_doc_line", {}).get(sid)
    b = getattr(idx, "_bundles", {}).get(resolved) if loc and resolved and loc[0] == resolved else None
    if not b:
        # Document synthetic root → first-line title.
        if sid.endswith(":__doc_root") and resolved:
            bb = getattr(idx, "_bundles", {}).get(resolved)
            if bb and bb.lines:
                title = (bb.lines[0].content or "").strip()
                if len(title) > max_chars:
                    title = title[:max_chars].rstrip()
                return title or sid.split(":")[-1]
        return sid.split(":")[-1]
    _, j = loc
    if j < 0 or j >= len(b.lines):
        return sid.split(":")[-1]
    title = (b.lines[j].content or "").strip()
    if len(title) > max_chars:
        title = title[:max_chars].rstrip()
    return title or sid.split(":")[-1]


def _chunk_body(chunk: Chunk) -> str:
    """Strip legacy full-path [§ ...] headers; body only."""
    text = (chunk.text or "").strip()
    if not text:
        return ""
    lines = text.splitlines()
    if lines and lines[0].strip().startswith("[§"):
        return "\n".join(lines[1:]).strip()
    return text


def _line_key(chunk: Chunk) -> Tuple[int, str]:
    lids = list(chunk.line_ids or ())
    if lids:
        return (min(lids), chunk.node_id)
    return (10**9, chunk.node_id)


def _child_final_score(
    chunk: Chunk,
    state: NavState,
    *,
    w_conf: float,
) -> float:
    owner = evidence_owner_section_id(chunk)
    own_unit = unit_score_for_evidence_chunk(chunk, dict(state.unit_scores or {}))
    conf = _clamp01(float((state.collect_confidence or {}).get(owner, 0.0) or 0.0))
    return float(own_unit) + float(w_conf) * conf


def _is_header_only_owner(owner: str, owners: set[str], ts: ToolSpace, doc_id: str) -> bool:
    """True if owner is a structural ancestor of another collected owner."""
    if not owner or owner not in owners:
        return False
    owner_doc = _section_doc_id(ts, owner, doc_id)
    for other in owners:
        if other == owner:
            continue
        if _section_doc_id(ts, other, doc_id) != owner_doc:
            continue
        cur = other
        for _ in range(64):
            p = _direct_parent_id(ts, cur, owner_doc)
            if p is None:
                break
            if p == owner:
                return True
            cur = p
    return False


@dataclass
class _ChildItem:
    chunk: Chunk
    owner: str
    score: float
    line_key: Tuple[int, str]


@dataclass
class _ParentGroup:
    parent_id: Optional[str]
    parent_title: str
    children: List[_ChildItem]
    priority: float = 0.0

    @property
    def group_key(self) -> float:
        if not self.children:
            return 0.0
        return max(c.score for c in self.children)

    @property
    def doc_order_key(self) -> Tuple[int, str]:
        if not self.children:
            return (10**9, "")
        return min(c.line_key for c in self.children)


@dataclass
class _SelectedChild:
    item: _ChildItem
    mode: str  # "full" | "snippet"


def dedupe_scored(scored: Sequence[Tuple[Chunk, float]]) -> List[Tuple[Chunk, float]]:
    """Keep highest score per chunk.node_id; sort by score descending."""
    best: Dict[str, Tuple[Chunk, float]] = {}
    for c, score in scored:
        nid = str(getattr(c, "node_id", "") or "")
        if not nid:
            continue
        prev = best.get(nid)
        if prev is None or float(score) > float(prev[1]):
            best[nid] = (c, float(score))
    out = list(best.values())
    out.sort(key=lambda x: -x[1])
    return out


def _build_groups(
    scored: Sequence[Tuple[Chunk, float]],
    ts: ToolSpace,
    state: NavState,
    config: NavConfig,
) -> List[_ParentGroup]:
    w_conf = float(getattr(config, "compose_confidence_weight", 0.5) or 0.5)
    seen_ids: set[str] = set()
    items: List[Tuple[Chunk, str, float]] = []
    for chunk, _bag in scored:
        nid = str(getattr(chunk, "node_id", "") or "")
        if not nid or nid in seen_ids:
            continue
        body = _chunk_body(chunk)
        if not body:
            continue
        seen_ids.add(nid)
        owner = evidence_owner_section_id(chunk)
        score = _child_final_score(chunk, state, w_conf=w_conf)
        items.append((chunk, owner, score))

    owners = {owner for _c, owner, _s in items if owner}
    header_owners = {
        o for o in owners if _is_header_only_owner(o, owners, ts, state.doc_id)
    }

    groups: Dict[Optional[str], _ParentGroup] = {}
    for chunk, owner, score in items:
        if owner in header_owners:
            continue
        owner_doc = _section_doc_id(ts, owner, state.doc_id) or str(
            getattr(chunk, "doc_id", "") or ""
        )
        parent_id = _direct_parent_id(ts, owner, owner_doc)
        if parent_id is None:
            parent_id = owner
        if parent_id not in groups:
            title = _section_title(ts, parent_id, owner_doc, max_chars=40)
            groups[parent_id] = _ParentGroup(
                parent_id=parent_id,
                parent_title=title,
                children=[],
                priority=float((state.group_priority or {}).get(parent_id, 0.0) or 0.0),
            )
        groups[parent_id].children.append(
            _ChildItem(
                chunk=chunk,
                owner=owner,
                score=score,
                line_key=_line_key(chunk),
            )
        )
    return list(groups.values())


def build_compose_preview(
    collected: Sequence[Tuple[Chunk, float]],
    ts: ToolSpace,
    state: NavState,
    config: NavConfig,
) -> Tuple[str, Dict[str, str]]:
    """Assemble current pool into [G*] parent-group preview.

    Reuses _build_groups. G* numbering follows (-group_key, doc_order_key) for
    stable ids. Returns (preview_text, {G_id: parent_id}).
    """
    scored = dedupe_scored(list(collected))
    groups = _build_groups(scored, ts, state, config)
    groups.sort(key=lambda g: (-g.group_key, g.doc_order_key))

    snippet_n = max(0, int(getattr(config, "compose_preview_snippet_chars", 60) or 0))
    max_children = max(0, int(getattr(config, "compose_preview_max_children", 0) or 0))

    lines: List[str] = []
    g_map: Dict[str, str] = {}
    for i, g in enumerate(groups, 1):
        gid = f"G{i}"
        if g.parent_id:
            g_map[gid] = str(g.parent_id)
        title = g.parent_title or (g.parent_id or "").split(":")[-1] or gid
        lines.append(f"[{gid}] §{title}")
        children = sorted(g.children, key=lambda c: (-c.score, c.line_key))
        if max_children > 0:
            shown = children[:max_children]
            omitted = len(children) - len(shown)
        else:
            shown = children
            omitted = 0
        for child in shown:
            body = _chunk_body(child.chunk)
            first = body.splitlines()[0].strip() if body else ""
            if snippet_n > 0 and len(first) > snippet_n:
                first = first[:snippet_n].rstrip() + "…"
            unit = unit_score_for_evidence_chunk(child.chunk, dict(state.unit_scores or {}))
            owner_short = (child.owner or "").split(":")[-1] or "?"
            lines.append(
                f"  - {owner_short} u={unit:.3f} | {first} ({len(body)} chars)"
            )
        if omitted > 0:
            lines.append(f"  - … (+{omitted} more)")
    return "\n".join(lines), g_map


def _child_snippet(body: str, snippet_chars: int) -> str:
    """First non-empty line, truncated to snippet_chars."""
    first = ""
    for ln in (body or "").splitlines():
        if ln.strip():
            first = ln.strip()
            break
    if not first:
        return ""
    cap = max(1, int(snippet_chars))
    if len(first) > cap:
        return first[:cap].rstrip() + "…"
    return first


def _display_body(child: _ChildItem, mode: str, snippet_chars: int) -> str:
    body = _chunk_body(child.chunk)
    if not body:
        return ""
    if mode == "snippet":
        return _child_snippet(body, snippet_chars)
    return body


def _render_group(
    group: _ParentGroup,
    selected: Sequence[Union[_SelectedChild, _ChildItem]],
    *,
    evidence_index: int,
    indent: bool,
    snippet_chars: int = 80,
) -> str:
    """Render one evidence block. Accepts _ChildItem (full) or _SelectedChild."""
    parts: List[str] = [f"[E{evidence_index}]"]
    if group.parent_title:
        parts.append(f"[§ {group.parent_title}]")
    for entry in selected:
        if isinstance(entry, _SelectedChild):
            child, mode = entry.item, entry.mode
        else:
            child, mode = entry, "full"
        body = _display_body(child, mode, snippet_chars)
        if not body:
            continue
        if indent:
            indented = "\n".join(
                ("  " + ln if ln.strip() else ln) for ln in body.splitlines()
            )
            parts.append(indented)
        else:
            parts.append(body)
    return "\n".join(parts).strip()


def _scored_flat(groups: Sequence[_ParentGroup]) -> List[Tuple[Chunk, float]]:
    out: List[Tuple[Chunk, float]] = []
    for g in groups:
        for c in sorted(g.children, key=lambda x: (-x.score, x.line_key)):
            out.append((c.chunk, c.score))
    return out


def _n_pool_children(groups: Sequence[_ParentGroup]) -> int:
    return sum(len(g.children) for g in groups)


def _n_owners_from_chunks(chunks: Sequence[Chunk]) -> int:
    return len({evidence_owner_section_id(c) for c in chunks if c})


def _pack_greedy(
    groups: List[_ParentGroup],
    *,
    budget_chars: int,
    min_partial_chars: int = 20,
    snippet_chars: int = 80,
) -> ComposeFillResult:
    """Legacy fill: group-by-group full text, skip oversized, break when budget ends."""
    scored_flat = _scored_flat(groups)
    if budget_chars <= 0:
        return ComposeFillResult([], "", 0, 0, False, scored_flat, dropped_any=False)

    parts: List[str] = []
    kept: List[Chunk] = []
    used = 0
    truncated_last = False
    sep = "\n\n"
    n_pool = _n_pool_children(groups)

    for g in groups:
        if not g.children:
            continue
        by_score = sorted(g.children, key=lambda x: (-x.score, x.line_key))
        selected: List[_ChildItem] = []
        for child in by_score:
            trial = selected + [child]
            trial_doc = sorted(trial, key=lambda x: x.line_key)
            indent = len(trial_doc) >= 2
            block = _render_group(
                g,
                trial_doc,
                evidence_index=len(parts) + 1,
                indent=indent,
                snippet_chars=snippet_chars,
            )
            add = len(block) + (len(sep) if parts else 0)
            if used + add <= budget_chars:
                selected = trial
            # else: skip oversized child; try later (often shorter) candidates

        if not selected:
            if not parts and by_score:
                child = by_score[0]
                one = [child]
                block = _render_group(
                    g, one, evidence_index=1, indent=False, snippet_chars=snippet_chars
                )
                if len(block) > budget_chars and budget_chars >= min_partial_chars:
                    parts.append(block[:budget_chars])
                    kept.append(child.chunk)
                    used = budget_chars
                    truncated_last = True
                    return ComposeFillResult(
                        kept,
                        parts[0],
                        used,
                        len(kept),
                        truncated_last,
                        scored_flat,
                        dropped_any=n_pool > 1,
                    )
            continue

        selected_doc = sorted(selected, key=lambda x: x.line_key)
        indent = len(selected_doc) >= 2
        block = _render_group(
            g,
            selected_doc,
            evidence_index=len(parts) + 1,
            indent=indent,
            snippet_chars=snippet_chars,
        )
        add = len(block) + (len(sep) if parts else 0)
        if used + add <= budget_chars:
            parts.append(block)
            kept.extend(c.chunk for c in selected_doc)
            used += add
            continue
        remain = budget_chars - used - (len(sep) if parts else 0)
        if remain >= min_partial_chars:
            parts.append(block[:remain])
            kept.extend(c.chunk for c in selected_doc)
            used = budget_chars
            truncated_last = True
        break

    text = sep.join(parts)
    return ComposeFillResult(
        kept_chunks=kept,
        evidence_text=text,
        evidence_chars_actual=len(text),
        n_chunks_kept=len(kept),
        truncated_last=truncated_last,
        scored_chunks=scored_flat,
        dropped_any=len(kept) < n_pool,
    )


def _render_selection(
    groups: Sequence[_ParentGroup],
    selected_by_nid: Dict[str, _SelectedChild],
    *,
    budget_chars: int,
    snippet_chars: int,
    min_partial_chars: int = 20,
) -> ComposeFillResult:
    """Render selected children in group order (doc order within group)."""
    scored_flat = _scored_flat(groups)
    parts: List[str] = []
    kept: List[Chunk] = []
    used = 0
    truncated_last = False
    sep = "\n\n"
    n_pool = _n_pool_children(groups)

    for g in groups:
        entries = [
            selected_by_nid[c.chunk.node_id]
            for c in sorted(g.children, key=lambda x: x.line_key)
            if c.chunk.node_id in selected_by_nid
        ]
        if not entries:
            continue
        indent = len(entries) >= 2
        block = _render_group(
            g,
            entries,
            evidence_index=len(parts) + 1,
            indent=indent,
            snippet_chars=snippet_chars,
        )
        add = len(block) + (len(sep) if parts else 0)
        if used + add <= budget_chars:
            parts.append(block)
            kept.extend(e.item.chunk for e in entries)
            used += add
            continue
        remain = budget_chars - used - (len(sep) if parts else 0)
        if remain >= min_partial_chars and not parts:
            parts.append(block[:budget_chars])
            kept.extend(e.item.chunk for e in entries)
            used = budget_chars
            truncated_last = True
            break
        if remain >= min_partial_chars:
            parts.append(block[:remain])
            kept.extend(e.item.chunk for e in entries)
            used = budget_chars
            truncated_last = True
        break

    text = sep.join(parts)
    return ComposeFillResult(
        kept_chunks=kept,
        evidence_text=text,
        evidence_chars_actual=len(text),
        n_chunks_kept=len(kept),
        truncated_last=truncated_last,
        scored_chunks=scored_flat,
        dropped_any=len(kept) < n_pool,
    )


def _trial_fits(
    groups: Sequence[_ParentGroup],
    selected_by_nid: Dict[str, _SelectedChild],
    *,
    budget_chars: int,
    snippet_chars: int,
) -> bool:
    fill = _render_selection(
        groups,
        selected_by_nid,
        budget_chars=budget_chars,
        snippet_chars=snippet_chars,
    )
    return len(fill.kept_chunks) == len(selected_by_nid)


def _pack_waterfill(
    groups: List[_ParentGroup],
    *,
    budget_chars: int,
    cov_frac: float,
    snippet_chars: int,
    min_partial_chars: int = 20,
) -> ComposeFillResult:
    """Tiered pack: full-text head, round-robin snippets, then enrich."""
    scored_flat = _scored_flat(groups)
    if budget_chars <= 0 or not groups:
        return ComposeFillResult([], "", 0, 0, False, scored_flat, dropped_any=False)

    cov_frac = max(0.0, min(0.9, float(cov_frac)))
    full_budget = max(min_partial_chars, int(budget_chars * (1.0 - cov_frac)))
    snippet_chars = max(8, int(snippet_chars))

    greedy = _pack_greedy(
        groups,
        budget_chars=budget_chars,
        min_partial_chars=min_partial_chars,
        snippet_chars=snippet_chars,
    )
    if not greedy.dropped_any:
        return greedy

    selected: Dict[str, _SelectedChild] = {}
    sep = "\n\n"
    used_probe = 0
    tier1_parts: List[str] = []

    # Tier1: full-text head under full_budget.
    for g in groups:
        if not g.children:
            continue
        by_score = sorted(g.children, key=lambda x: (-x.score, x.line_key))
        chosen: List[_ChildItem] = []
        for child in by_score:
            if child.chunk.node_id in selected:
                continue
            trial_items = chosen + [child]
            probe = dict(selected)
            for c in trial_items:
                probe[c.chunk.node_id] = _SelectedChild(c, "full")
            entries = [
                probe[c.chunk.node_id]
                for c in sorted(g.children, key=lambda x: x.line_key)
                if c.chunk.node_id in probe
            ]
            indent = len(entries) >= 2
            block = _render_group(
                g,
                entries,
                evidence_index=len(tier1_parts) + 1,
                indent=indent,
                snippet_chars=snippet_chars,
            )
            add = len(block) + (len(sep) if tier1_parts else 0)
            if used_probe + add <= full_budget:
                chosen = trial_items
                selected[child.chunk.node_id] = _SelectedChild(child, "full")

        if chosen:
            entries = [
                selected[c.chunk.node_id]
                for c in sorted(chosen, key=lambda x: x.line_key)
            ]
            indent = len(entries) >= 2
            block = _render_group(
                g,
                entries,
                evidence_index=len(tier1_parts) + 1,
                indent=indent,
                snippet_chars=snippet_chars,
            )
            add = len(block) + (len(sep) if tier1_parts else 0)
            if used_probe + add <= full_budget:
                tier1_parts.append(block)
                used_probe += add
            else:
                for c in chosen:
                    selected.pop(c.chunk.node_id, None)
                break

    # Tier2: round-robin snippets across groups (doc order within group).
    per_group_queue: List[List[_ChildItem]] = []
    for g in groups:
        remaining = [
            c
            for c in sorted(g.children, key=lambda x: x.line_key)
            if c.chunk.node_id not in selected
        ]
        per_group_queue.append(remaining)

    max_rounds = max((len(q) for q in per_group_queue), default=0)
    for r in range(max_rounds):
        for gi, g in enumerate(groups):
            queue = per_group_queue[gi]
            if r >= len(queue):
                continue
            child = queue[r]
            if child.chunk.node_id in selected:
                continue
            trial = dict(selected)
            trial[child.chunk.node_id] = _SelectedChild(child, "snippet")
            if _trial_fits(
                groups, trial, budget_chars=budget_chars, snippet_chars=snippet_chars
            ):
                selected = trial

    # Tier3: enrich snippets -> full by group/score order.
    enrich_order: List[_ChildItem] = []
    for g in groups:
        for child in sorted(g.children, key=lambda x: (-x.score, x.line_key)):
            sel = selected.get(child.chunk.node_id)
            if sel is not None and sel.mode == "snippet":
                enrich_order.append(child)
    for child in enrich_order:
        trial = dict(selected)
        trial[child.chunk.node_id] = _SelectedChild(child, "full")
        if _trial_fits(
            groups, trial, budget_chars=budget_chars, snippet_chars=snippet_chars
        ):
            selected = trial

    waterfill = _render_selection(
        groups,
        selected,
        budget_chars=budget_chars,
        snippet_chars=snippet_chars,
        min_partial_chars=min_partial_chars,
    )

    if _n_owners_from_chunks(waterfill.kept_chunks) < _n_owners_from_chunks(
        greedy.kept_chunks
    ):
        return greedy
    return waterfill


def pack_nav_evidence(
    collected: Sequence[Tuple[Chunk, float]],
    ts: ToolSpace,
    state: NavState,
    config: NavConfig,
    *,
    budget_chars: int,
    min_partial_chars: int = 20,
) -> ComposeFillResult:
    """Pack collected evidence under parent scopes into a budgeted tree string."""
    if budget_chars <= 0:
        return ComposeFillResult([], "", 0, 0, False, [], dropped_any=False)

    groups = _build_groups(collected, ts, state, config)
    groups.sort(key=lambda g: (-g.priority, -g.group_key, g.doc_order_key))

    mode = str(getattr(config, "compose_packing_mode", "waterfill") or "waterfill").strip().lower()
    snippet_chars = int(getattr(config, "compose_snippet_chars", 80) or 80)

    if mode == "waterfill":
        cov_frac = float(getattr(config, "compose_coverage_budget_frac", 0.4) or 0.4)
        return _pack_waterfill(
            groups,
            budget_chars=budget_chars,
            cov_frac=cov_frac,
            snippet_chars=snippet_chars,
            min_partial_chars=min_partial_chars,
        )

    return _pack_greedy(
        groups,
        budget_chars=budget_chars,
        min_partial_chars=min_partial_chars,
        snippet_chars=snippet_chars,
    )


def parse_collect_confidence(
    obj: Dict[str, Any],
    selected: Sequence[Any],
) -> Dict[str, float]:
    """Map selected LegalActions -> confidence in [0,1]. Missing => 0."""
    raw = (obj or {}).get("confidence")
    out: Dict[str, float] = {}
    if isinstance(raw, (int, float)):
        c = _clamp01(float(raw))
        for a in selected:
            aid = str(getattr(a, "action_id", "") or "").strip().upper()
            if aid:
                out[aid] = c
        return out
    if isinstance(raw, dict):
        norm = {str(k).strip().upper(): v for k, v in raw.items()}
        for a in selected:
            aid = str(getattr(a, "action_id", "") or "").strip().upper()
            if not aid:
                continue
            if aid in norm and norm[aid] is not None:
                try:
                    out[aid] = _clamp01(float(norm[aid]))
                except (TypeError, ValueError):
                    out[aid] = 0.0
            else:
                out[aid] = 0.0
        return out
    for a in selected:
        aid = str(getattr(a, "action_id", "") or "").strip().upper()
        if aid:
            out[aid] = 0.0
    return out
