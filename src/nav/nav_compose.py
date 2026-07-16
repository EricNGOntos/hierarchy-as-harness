"""Nav COMPOSE packing: document-order groups + selection_count truncation.

Parent sections are path headers only (not competing evidence units).
Unit scores are MAP-projection only — they do not drive pack/truncate order.
Group order: (-group_priority, doc_order). Within a group: document order.
Over budget: drop chunks by (selection_count asc, priority asc, line_key desc).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Sequence, Tuple

from agent_delivery.code.index_retrieval import Chunk
from agent_delivery.code.load_data import line_node_id
from agent_delivery.code.tool_space import ToolSpace

from nav_types import NavConfig, NavState


@dataclass
class ComposeFillResult:
    kept_chunks: List[Chunk]
    evidence_text: str
    evidence_chars_actual: int
    n_chunks_kept: int
    truncated_last: bool
    scored_chunks: List[Tuple[Chunk, float]]


def _clamp01(x: float) -> float:
    return max(0.0, min(1.0, float(x)))


def evidence_owner_section_id(chunk: Chunk) -> str:
    """Section that owns a hydrated evidence chunk (strip __path/__intro suffixes)."""
    nid = str(getattr(chunk, "node_id", "") or "").strip()
    for suf in ("__path", "__intro", "__outline", "__self"):
        if nid.endswith(suf):
            return nid[: -len(suf)]
    sid = str(getattr(chunk, "section_id", "") or "").strip()
    return nid or sid


def unit_score_for_evidence_chunk(chunk: Chunk, unit_scores: Dict[str, float]) -> float:
    """Map leaf/path materialize ids onto hybrid unit scores (display / telemetry)."""
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
    idx = getattr(ts, "_idx", None)
    if idx is None:
        return None
    loc = getattr(idx, "_node_to_doc_line", {}).get(sid)
    if not loc or loc[0] != doc_id:
        return None
    _, j = loc
    parents = getattr(idx, "_doc_parents", {}).get(doc_id, [])
    b = getattr(idx, "_bundles", {}).get(doc_id)
    if not b or j >= len(parents):
        return None
    p = parents[j]
    if p is None or p < 0 or p >= len(b.lines):
        return None
    return line_node_id(doc_id, b.lines[p].line_id)


def selection_count_for_owner(
    owner: str,
    explicit_collect_ids: set[str],
    ts: ToolSpace,
    doc_id: str,
) -> int:
    """How many times this owner is structurally selected (0 / 1 / 2).

    +1 if owner itself is an explicit COLLECT target;
    +1 if any ancestor is an explicit COLLECT target.
    """
    explicit = explicit_collect_ids or set()
    sid = str(owner or "").strip()
    if not sid:
        return 0
    count = 0
    if sid in explicit:
        count += 1
    cur = sid
    for _ in range(64):
        parent = _direct_parent_id(ts, cur, doc_id)
        if parent is None:
            break
        if parent in explicit:
            count += 1
            break
        cur = parent
    return count


def _section_title(ts: ToolSpace, section_id: str, doc_id: str, *, max_chars: int = 40) -> str:
    sid = str(section_id or "").strip()
    if not sid:
        return ""
    idx = getattr(ts, "_idx", None)
    if idx is None:
        return sid.split(":")[-1]
    loc = getattr(idx, "_node_to_doc_line", {}).get(sid)
    b = getattr(idx, "_bundles", {}).get(doc_id) if loc and loc[0] == doc_id else None
    if not b:
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


def _is_header_only_owner(owner: str, owners: set[str], ts: ToolSpace, doc_id: str) -> bool:
    """True if owner is a structural ancestor of another collected owner."""
    if not owner or owner not in owners:
        return False
    for other in owners:
        if other == owner:
            continue
        cur = other
        for _ in range(64):
            p = _direct_parent_id(ts, cur, doc_id)
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
    unit: float  # preview telemetry only; never used for pack/truncate order
    selection_count: int
    line_key: Tuple[int, str]


@dataclass
class _ParentGroup:
    parent_id: Optional[str]
    parent_title: str
    children: List[_ChildItem]
    priority: float = 0.0

    @property
    def doc_order_key(self) -> Tuple[int, str]:
        if not self.children:
            return (10**9, "")
        return min(c.line_key for c in self.children)


def dedupe_scored(scored: Sequence[Tuple[Chunk, float]]) -> List[Tuple[Chunk, float]]:
    """Keep the highest-score copy per node without imposing a packing order."""
    best: Dict[str, Tuple[Chunk, float]] = {}
    for c, score in scored:
        nid = str(getattr(c, "node_id", "") or "")
        if not nid:
            continue
        prev = best.get(nid)
        if prev is None or float(score) > float(prev[1]):
            best[nid] = (c, float(score))
    return list(best.values())


def _build_groups(
    scored: Sequence[Tuple[Chunk, float]],
    ts: ToolSpace,
    state: NavState,
) -> List[_ParentGroup]:
    explicit = set(state.explicit_collect_ids or set())
    seen_ids: set[str] = set()
    items: List[Tuple[Chunk, str, float, int]] = []
    for chunk, _bag in scored:
        nid = str(getattr(chunk, "node_id", "") or "")
        if not nid or nid in seen_ids:
            continue
        body = _chunk_body(chunk)
        if not body:
            continue
        seen_ids.add(nid)
        owner = evidence_owner_section_id(chunk)
        unit = unit_score_for_evidence_chunk(chunk, dict(state.unit_scores or {}))
        sel = selection_count_for_owner(owner, explicit, ts, state.doc_id)
        items.append((chunk, owner, unit, sel))

    owners = {owner for _c, owner, _s, _sel in items if owner}
    header_owners = {
        o for o in owners if _is_header_only_owner(o, owners, ts, state.doc_id)
    }

    groups: Dict[Optional[str], _ParentGroup] = {}
    for chunk, owner, unit, sel in items:
        if owner in header_owners:
            continue
        parent_id = _direct_parent_id(ts, owner, state.doc_id)
        if parent_id is None:
            parent_id = owner
        if parent_id not in groups:
            title = _section_title(ts, parent_id, state.doc_id, max_chars=40)
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
                unit=unit,
                selection_count=sel,
                line_key=_line_key(chunk),
            )
        )
    return list(groups.values())


def _sort_groups(groups: List[_ParentGroup]) -> List[_ParentGroup]:
    return sorted(groups, key=lambda g: (-g.priority, g.doc_order_key))


def build_compose_preview(
    collected: Sequence[Tuple[Chunk, float]],
    ts: ToolSpace,
    state: NavState,
    config: NavConfig,
) -> Tuple[str, Dict[str, str]]:
    """Assemble current pool into [G*] parent-group preview.

    G* numbering follows (-priority, doc_order_key). Children listed in doc order.
    Returns (preview_text, {G_id: parent_id}).
    """
    scored = dedupe_scored(list(collected))
    groups = _sort_groups(_build_groups(scored, ts, state))

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
        children = sorted(g.children, key=lambda c: c.line_key)
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
            owner_short = (child.owner or "").split(":")[-1] or "?"
            lines.append(
                f"  - {owner_short} u={child.unit:.3f} | {first} ({len(body)} chars)"
            )
        if omitted > 0:
            lines.append(f"  - … (+{omitted} more)")
    return "\n".join(lines), g_map


def _render_group(
    group: _ParentGroup,
    selected: List[_ChildItem],
    *,
    evidence_index: int,
    indent: bool,
) -> str:
    parts: List[str] = [f"[E{evidence_index}]"]
    if group.parent_title:
        parts.append(f"[§ {group.parent_title}]")
    for child in selected:
        body = _chunk_body(child.chunk)
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


def _render_all_groups(
    groups: Sequence[_ParentGroup],
    *,
    sep: str = "\n\n",
) -> Tuple[str, List[Chunk]]:
    """Render groups (already ordered) with children in document order."""
    parts: List[str] = []
    kept: List[Chunk] = []
    for g in groups:
        if not g.children:
            continue
        selected = sorted(g.children, key=lambda c: c.line_key)
        indent = len(selected) >= 2
        block = _render_group(g, selected, evidence_index=len(parts) + 1, indent=indent)
        if not block:
            continue
        parts.append(block)
        kept.extend(c.chunk for c in selected)
    return sep.join(parts), kept


def _removal_rank(
    child: _ChildItem, group: _ParentGroup
) -> Tuple[int, float, Tuple[int, str]]:
    """Higher rank = drop sooner: low selection_count, low priority, doc-later.

    TODO(compose-tiebreak): optionally fold collect_confidence (and, if added,
    a subagent RegionReport group prior) into same-tier tiebreak only — never as
    a primary pack key. Prefer: after (selection_count, group_priority) are equal,
    drop lower confidence / missing prior first; keep document order as the last
    key. Do not let subagents emit absolute group_rank that overrides depth-0
    external rerank (root remains the sole ranking authority).
    """
    return (-int(child.selection_count), -float(group.priority), child.line_key)


def pack_nav_evidence(
    collected: Sequence[Tuple[Chunk, float]],
    ts: ToolSpace,
    state: NavState,
    config: NavConfig,
    *,
    budget_chars: int,
    min_partial_chars: int = 20,
) -> ComposeFillResult:
    """Pack collected evidence under parent scopes into a budgeted tree string.

    1) Assemble all chunks in (-priority, doc_order) / within-group doc order.
    2) If under budget, return as-is.
    3) Else drop chunks one-by-one by selection_count / priority / doc-tail.
    4) Never delete a whole group by rerank score; empty groups fall out after drops.
    5) Extreme fallback: truncate remaining text to budget.
    """
    if budget_chars <= 0:
        return ComposeFillResult([], "", 0, 0, False, [])

    groups = _sort_groups(_build_groups(collected, ts, state))
    sep = "\n\n"

    scored_flat: List[Tuple[Chunk, float]] = []
    for g in groups:
        for c in sorted(g.children, key=lambda x: x.line_key):
            scored_flat.append((c.chunk, float(c.selection_count)))

    text, kept = _render_all_groups(groups, sep=sep)
    truncated_last = False

    if len(text) > budget_chars:
        while True:
            text, kept = _render_all_groups(groups, sep=sep)
            if len(text) <= budget_chars:
                break
            # Keep one final chunk for the character-level fallback below.
            if sum(len(g.children) for g in groups) <= 1:
                break
            pick: Optional[Tuple[int, int]] = None
            pick_rank: Optional[Tuple[int, float, Tuple[int, str]]] = None
            for gi, g in enumerate(groups):
                for ci, child in enumerate(g.children):
                    rank = _removal_rank(child, g)
                    if pick_rank is None or rank > pick_rank:
                        pick_rank = rank
                        pick = (gi, ci)
            if pick is None:
                break
            gi, ci = pick
            del groups[gi].children[ci]
            if not groups[gi].children:
                del groups[gi]
            if not any(g.children for g in groups):
                text, kept = "", []
                break
        text, kept = _render_all_groups(groups, sep=sep)

    if text and len(text) > budget_chars:
        if budget_chars >= min_partial_chars:
            text = text[:budget_chars]
            truncated_last = True
        else:
            text, kept = "", []

    return ComposeFillResult(
        kept_chunks=kept,
        evidence_text=text,
        evidence_chars_actual=len(text),
        n_chunks_kept=len(kept),
        truncated_last=truncated_last,
        scored_chunks=scored_flat,
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
