from __future__ import annotations

import math
import re
from typing import Any, Iterable, List, Optional

from nav_types import NavConfig, Projection, SectionView


def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[\w\u4e00-\u9fff]+", (text or "").lower()))


def _lexical_score(query: str, text: str) -> float:
    q = _tokens(query)
    if not q:
        return 0.0
    t = _tokens(text)
    if not t:
        return 0.0
    inter = len(q & t)
    if inter == 0:
        return 0.0
    return float(inter) / math.sqrt(float(len(q) * len(t)))


def _section_view_from_structure(
    ts: Any,
    section_id: str,
    *,
    query: str,
    depth_from_scope: int,
    summary_chars: int,
) -> SectionView:
    st = ts.get_structure(section_id)
    preview = str(st.get("preview") or "").replace("\n", " ")[:summary_chars]
    children = st.get("children") or []
    return SectionView(
        section_id=str(st.get("section_id") or section_id),
        level=int(st.get("level") or 0) if str(st.get("level") or "").isdigit() else 0,
        preview=preview,
        score=_lexical_score(query, f"{section_id} {preview}"),
        n_lines=int(st.get("n_lines") or 0),
        n_chunks=int(st.get("n_chunks") or 0),
        has_children=bool(children),
        depth_from_scope=depth_from_scope,
    )


def _children(ts: Any, section_id: str) -> List[dict]:
    st = ts.get_structure(section_id)
    children = st.get("children") or []
    if isinstance(children, list):
        return [c for c in children if isinstance(c, dict)]
    return []


def _top_sections(ts: Any, doc_id: str) -> List[str]:
    try:
        return list(ts.sections_for_doc(doc_id))
    except Exception:
        return []


def build_projection(
    ts: Any,
    *,
    doc_id: str,
    query: str,
    scope: Optional[str],
    config: NavConfig,
) -> Projection:
    visible: List[SectionView] = []
    lines: List[str] = []
    truncated = False

    def add_line(text: str) -> None:
        nonlocal truncated
        if truncated:
            return
        candidate_len = sum(len(x) + 1 for x in lines) + len(text)
        if candidate_len > config.projection_char_limit:
            lines.append("... [projection truncated]")
            truncated = True
            return
        lines.append(text)

    add_line(f"doc_id={doc_id}")
    add_line(f"scope={scope or '<document-root>'}")

    if scope:
        root_ids = [scope]
    else:
        root_ids = _top_sections(ts, doc_id)

    root_ids = root_ids[: max(1, config.projection_child_limit)]
    frontier: List[tuple[str, int]] = [(sid, 0) for sid in root_ids]
    seen: set[str] = set()
    while frontier:
        sid, depth = frontier.pop(0)
        if sid in seen:
            continue
        seen.add(sid)
        try:
            view = _section_view_from_structure(
                ts,
                sid,
                query=query,
                depth_from_scope=depth,
                summary_chars=config.summary_chars,
            )
        except Exception:
            continue
        visible.append(view)
        indent = "  " * depth
        marker = "+" if view.has_children else "-"
        add_line(
            f"{indent}{marker} {view.section_id} "
            f"chunks={view.n_chunks} lines={view.n_lines} score={view.score:.4f} :: {view.preview}"
        )
        if depth + 1 >= max(1, config.projection_depth):
            continue
        child_rows = _children(ts, sid)[: max(0, config.projection_child_limit)]
        for child in child_rows:
            child_id = str(child.get("section_id") or "").strip()
            if child_id and child_id not in seen:
                frontier.append((child_id, depth + 1))

    visible.sort(key=lambda v: (-v.score, v.depth_from_scope, v.section_id))
    return Projection(
        doc_id=doc_id,
        scope=scope,
        text="\n".join(lines),
        visible_sections=visible,
        truncated=truncated,
    )


def top_visible_sections(projection: Projection, *, limit: int) -> List[SectionView]:
    return list(projection.visible_sections[: max(0, limit)])

