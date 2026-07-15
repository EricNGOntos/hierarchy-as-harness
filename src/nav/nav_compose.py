"""Nav COMPOSE packing: parent-scoped rank + one-level indent tree.

Parent sections are path headers only (not competing evidence units).
Child score = own_unit + w_conf * collect_confidence (default w_conf=0.5).
Group order: group_priority (external rank), then max child score, then doc order.
Within a group, skip oversized children and keep packing shorter ones that fit.
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
        return ComposeFillResult([], "", 0, 0, False, [])

    groups = _build_groups(collected, ts, state, config)
    groups.sort(key=lambda g: (-g.priority, -g.group_key, g.doc_order_key))

    scored_flat: List[Tuple[Chunk, float]] = []
    for g in groups:
        for c in sorted(g.children, key=lambda x: (-x.score, x.line_key)):
            scored_flat.append((c.chunk, c.score))

    parts: List[str] = []
    kept: List[Chunk] = []
    used = 0
    truncated_last = False
    sep = "\n\n"

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
                g, trial_doc, evidence_index=len(parts) + 1, indent=indent
            )
            add = len(block) + (len(sep) if parts else 0)
            if used + add <= budget_chars:
                selected = trial
            # else: skip oversized child; try later (often shorter) candidates

        if not selected:
            # Nothing fit whole: last-resort truncate the top-scored child alone.
            if not parts and by_score:
                child = by_score[0]
                one = [child]
                block = _render_group(g, one, evidence_index=1, indent=False)
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
                    )
            continue

        selected_doc = sorted(selected, key=lambda x: x.line_key)
        indent = len(selected_doc) >= 2
        block = _render_group(
            g, selected_doc, evidence_index=len(parts) + 1, indent=indent
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
