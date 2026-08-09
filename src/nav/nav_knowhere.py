"""Knowhere-native hierarchy provider for MAP-NAV.

Knowhere stores everything MAP-NAV needs in two tables:

``document_sections``
    ``section_id`` (PK) / ``parent_section_id`` (self FK) / ``section_path`` /
    ``section_title`` / ``section_level`` / ``summary`` / ``sort_order``
``document_chunks``
    ``chunk_id`` / ``section_id`` (FK) / ``chunk_type`` / ``content`` /
    ``chunk_metadata`` / ``sort_order``

``SectionRow`` and ``UnitRow`` below are that pair of shapes, and
``KnowhereProvider`` is a ``HierarchyProvider`` over them. Two loaders produce
the same rows: ``load_debug_parse`` from an on-disk parse track (the pre-insert
form of the very same records), and — in production — a single
``AsyncSession`` query per candidate document. The provider itself is
synchronous over an in-memory snapshot, which is what lets the MAP-NAV kernel
stay synchronous inside knowhere's async request path.

Hierarchy comes from ``parent_section_id`` and depth from ``section_level``,
not from splitting ``section_path`` on a separator.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

from nav_hierarchy import NodeMeta

# Assets are referenced from body text as ``[tables/foo.html]`` /
# ``[images/bar.png]``; that reference is what ties an asset to a section,
# because an asset row's own section linkage is unreliable.
_ASSET_REF_RE = re.compile(r"\[((?:tables|images)/[^\]\s][^\]]*)\]")

_ASSET_TYPES = ("table", "image")


@dataclass(frozen=True)
class SectionRow:
    """One ``document_sections`` row."""

    section_id: str
    parent_section_id: Optional[str]
    section_path: str
    section_title: str
    section_level: int
    summary: str
    sort_order: int


@dataclass(frozen=True)
class UnitRow:
    """One ``document_chunks`` row."""

    chunk_id: str
    section_id: Optional[str]
    chunk_type: str
    content: str
    sort_order: int
    source_chunk_path: str = ""
    file_path: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)


def asset_display_text(unit: UnitRow) -> str:
    """Body text for an asset unit, whose ``content`` is only a file path.

    Mirrors knowhere's own assembly: an asset contributes its summary, not its
    path. Without this an asset unit is unscorable and unreadable.
    """
    meta = unit.metadata or {}
    title = str(meta.get("asset_title") or "").strip()
    summary = str(meta.get("summary") or "").strip()
    ref = unit.file_path or unit.source_chunk_path or unit.content
    label = "Table" if unit.chunk_type == "table" else "Image"
    parts = [f"[{label}: {ref}]"] if ref else [f"[{label}]"]
    if title:
        parts.append(title)
    if summary:
        parts.append(summary)
    return "\n".join(parts)


class KnowhereProvider:
    """``HierarchyProvider`` over knowhere section/chunk rows."""

    def __init__(
        self,
        *,
        doc_id: str,
        sections: Sequence[SectionRow],
        units: Sequence[UnitRow],
    ) -> None:
        self.doc_id = str(doc_id)
        self._sections: Dict[str, SectionRow] = {s.section_id: s for s in sections}
        self._children: Dict[str, List[str]] = {}
        self._roots: List[str] = []
        for row in sorted(sections, key=lambda s: (s.sort_order, s.section_id)):
            parent = row.parent_section_id
            if parent and parent in self._sections:
                self._children.setdefault(parent, []).append(row.section_id)
            else:
                self._roots.append(row.section_id)

        self._units_by_section: Dict[str, List[UnitRow]] = {}
        for unit in sorted(units, key=lambda u: (u.sort_order, u.chunk_id)):
            sid = unit.section_id
            if not sid or sid not in self._sections:
                continue
            self._units_by_section.setdefault(sid, []).append(unit)

    # --- the 5 required capabilities -------------------------------------

    def roots(self, doc_id: str) -> Sequence[str]:
        return list(self._roots) if str(doc_id) == self.doc_id else []

    def children(self, section_id: str) -> Sequence[str]:
        return list(self._children.get(section_id, ()))

    def node_meta(self, section_id: str) -> NodeMeta:
        row = self._sections.get(section_id)
        if row is None:
            return NodeMeta()
        return NodeMeta(
            title=row.section_title,
            summary=row.summary,
            has_children=bool(self._children.get(section_id)),
            n_chunks=len(self.subtree_units(section_id)),
        )

    def relations(self, section_id: str) -> Tuple[Set[str], Set[str]]:
        ancestors: Set[str] = set()
        cur = self._sections.get(section_id)
        while cur is not None and cur.parent_section_id:
            parent = cur.parent_section_id
            if parent in ancestors:
                break
            ancestors.add(parent)
            cur = self._sections.get(parent)
        descendants: Set[str] = set()
        stack = list(self.children(section_id))
        while stack:
            cid = stack.pop()
            if cid in descendants:
                continue
            descendants.add(cid)
            stack.extend(self.children(cid))
        return ancestors, descendants

    def content(self, section_id: str) -> str:
        units = self.subtree_units(section_id)
        return "\n".join(self.unit_text(u) for u in units if self.unit_text(u))

    # --- optional capabilities the adapter forwards when present ---------

    def self_units(self, section_id: str) -> List[UnitRow]:
        """Units attached to this node itself, in document order."""
        return list(self._units_by_section.get(section_id, ()))

    def subtree_units(self, section_id: str) -> List[UnitRow]:
        """This node's units plus every descendant's, in document order."""
        out = list(self._units_by_section.get(section_id, ()))
        for cid in self.relations(section_id)[1]:
            out.extend(self._units_by_section.get(cid, ()))
        out.sort(key=lambda u: (u.sort_order, u.chunk_id))
        return out

    def leaf_ids(self, section_id: str) -> List[str]:
        """Descendant leaf ids in document order (the node itself if leaf)."""
        out: List[str] = []

        def rec(sid: str) -> None:
            kids = self.children(sid)
            if not kids:
                out.append(sid)
                return
            for kid in kids:
                rec(kid)

        rec(section_id)
        return out

    def path_titles(self, section_id: str) -> str:
        """Ancestor titles + own title, root first."""
        chain: List[str] = []
        cur = self._sections.get(section_id)
        while cur is not None:
            if cur.section_title:
                chain.append(cur.section_title)
            parent = cur.parent_section_id
            cur = self._sections.get(parent) if parent else None
        return " / ".join(reversed(chain))

    def parent_id(self, section_id: str) -> Optional[str]:
        row = self._sections.get(section_id)
        return row.parent_section_id if row else None

    def unit_text(self, unit: UnitRow) -> str:
        if unit.chunk_type in _ASSET_TYPES:
            return asset_display_text(unit)
        return str(unit.content or "").strip()

    def summaries(self) -> Dict[str, str]:
        return {
            sid: row.summary
            for sid, row in self._sections.items()
            if str(row.summary or "").strip()
        }

    def all_section_ids(self) -> List[str]:
        return list(self._sections)


# ---------------------------------------------------------------------------
# Loader: on-disk parse track
# ---------------------------------------------------------------------------


def _slug(name: str) -> str:
    """A doc id with no ':' so it stays addressable as ``{doc_id}:{path}``."""
    stem = Path(str(name)).stem or str(name)
    return stem.replace(":", "_").strip() or "doc"


def _iter_nav_nodes(nodes: Sequence[dict]) -> List[dict]:
    out: List[dict] = []
    for node in nodes:
        out.append(node)
        out.extend(_iter_nav_nodes(node.get("children") or ()))
    return out


def _find_anchor(nav_sections: Sequence[dict], anchor_path: str) -> Optional[dict]:
    for node in _iter_nav_nodes(nav_sections):
        if str(node.get("path") or "").strip("/") == anchor_path:
            return node
    return None


def load_debug_parse(
    track_dir: str | Path,
    *,
    doc_id: Optional[str] = None,
) -> KnowhereProvider:
    """Build a provider from a knowhere parse track directory.

    A parse track's ``doc_nav.json`` is rooted at the filesystem path of the
    parsed file, so its top levels are directory names rather than document
    structure. The real document root is the node whose path is the track
    directory itself; its children are the document's top-level sections. That
    wrapper exists only on disk — in the database ``parent_section_id IS NULL``
    already identifies the roots.
    """
    track = Path(track_dir)
    nav = json.loads((track / "doc_nav.json").read_text(encoding="utf-8"))
    raw_units = json.loads((track / "chunks.json").read_text(encoding="utf-8"))["chunks"]

    resolved_doc_id = doc_id or _slug(nav.get("file_name") or track.parent.name)
    anchor_path = str(track).strip("/")
    anchor = _find_anchor(nav.get("sections") or (), anchor_path)
    if anchor is None:
        raise ValueError(
            f"doc_nav.json has no node for track directory {anchor_path!r}; "
            "cannot locate the document root"
        )

    sections: List[SectionRow] = []
    path_to_id: Dict[str, str] = {}
    order = 0

    def add(node: dict, parent_id: Optional[str], level: int) -> None:
        nonlocal order
        rel = str(node.get("path") or "").strip("/")[len(anchor_path) + 1 :]
        if not rel:
            return
        section_id = f"{resolved_doc_id}:{rel}"
        path_to_id[rel] = section_id
        sections.append(
            SectionRow(
                section_id=section_id,
                parent_section_id=parent_id,
                section_path=rel,
                section_title=str(node.get("title") or "").strip(),
                section_level=level,
                summary=str(node.get("summary") or "").strip(),
                sort_order=order,
            )
        )
        order += 1
        for child in node.get("children") or ():
            add(child, section_id, level + 1)

    for top in anchor.get("children") or ():
        add(top, None, 1)

    units, unattached = _build_unit_rows(raw_units, anchor_path, path_to_id)
    if unattached:
        # Assets whose owning section could not be resolved are dropped rather
        # than hung off the root, matching knowhere's refusal to fall back.
        pass
    return KnowhereProvider(doc_id=resolved_doc_id, sections=sections, units=units)


def _build_unit_rows(
    raw_units: Sequence[dict],
    anchor_path: str,
    path_to_id: Dict[str, str],
) -> Tuple[List[UnitRow], List[str]]:
    """Map raw chunks onto section ids, resolving asset ownership by reference."""
    body_units: List[dict] = []
    asset_units: List[dict] = []
    for raw in raw_units:
        path = str(raw.get("path") or "").strip("/")
        if path.startswith(anchor_path):
            body_units.append(raw)
        else:
            asset_units.append(raw)

    owner_by_ref: Dict[str, str] = {}
    owner_by_chunk_id: Dict[str, str] = {}
    rows: List[UnitRow] = []

    for raw in body_units:
        rel = str(raw.get("path") or "").strip("/")[len(anchor_path) + 1 :]
        section_id = path_to_id.get(rel)
        if section_id is None:
            continue
        meta = dict(raw.get("metadata") or {})
        rows.append(
            UnitRow(
                chunk_id=str(raw.get("chunk_id") or ""),
                section_id=section_id,
                chunk_type=str(raw.get("type") or "text"),
                content=str(raw.get("content") or ""),
                sort_order=int(raw.get("order") or 0),
                source_chunk_path=str(raw.get("path") or ""),
                file_path=str(meta.get("file_path") or ""),
                metadata=meta,
            )
        )
        for ref in _ASSET_REF_RE.findall(str(raw.get("content") or "")):
            owner_by_ref.setdefault(ref.strip(), section_id)
        for link in meta.get("connect_to") or ():
            target = str((link or {}).get("target") or "").strip()
            if target:
                owner_by_chunk_id.setdefault(target, section_id)

    unattached: List[str] = []
    for raw in asset_units:
        chunk_id = str(raw.get("chunk_id") or "")
        meta = dict(raw.get("metadata") or {})
        ref = str(raw.get("path") or "").strip()
        section_id = owner_by_ref.get(ref) or owner_by_chunk_id.get(chunk_id)
        if section_id is None:
            unattached.append(ref or chunk_id)
            continue
        rows.append(
            UnitRow(
                chunk_id=chunk_id,
                section_id=section_id,
                chunk_type=str(raw.get("type") or "text"),
                content=str(raw.get("content") or ""),
                sort_order=int(raw.get("order") or 0),
                source_chunk_path=ref,
                file_path=str(meta.get("file_path") or ref),
                metadata=meta,
            )
        )
    return rows, unattached
