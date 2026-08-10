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

from nav_address import NavLevel
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
        self._chunk_ids: Set[str] = set()
        for unit in sorted(units, key=lambda u: (u.sort_order, u.chunk_id)):
            sid = unit.section_id
            if not sid or sid not in self._sections:
                continue
            self._units_by_section.setdefault(sid, []).append(unit)
            if unit.chunk_id:
                self._chunk_ids.add(unit.chunk_id)

    # --- address registry (NavAddress levels) ----------------------------

    def address_level(self, node_id: str) -> Optional[NavLevel]:
        sid = str(node_id or "").strip()
        if not sid:
            return NavLevel.NAMESPACE
        if sid == self.doc_id:
            return NavLevel.DOCUMENT
        if sid in self._sections:
            return NavLevel.SECTION
        if sid in self._chunk_ids:
            return NavLevel.CHUNK
        return None

    def owner_document(self, node_id: str) -> Optional[str]:
        sid = str(node_id or "").strip()
        if not sid:
            return None
        if sid == self.doc_id or sid in self._sections or sid in self._chunk_ids:
            return self.doc_id
        return None

    # --- the 5 required capabilities -------------------------------------
    # Namespace mode (document ids as map nodes) is only
    # ``NamespaceKnowhereProvider.document_ids`` — single-doc providers omit it.

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
    """Stable local doc id for an on-disk parse track (not a DB key)."""
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
    file_name = str(nav.get("file_name") or track.parent.name or "").strip()
    nav_sections = list(nav.get("sections") or ())
    # Fixture tracks nest document roots under an absolute track-dir node.
    # Real knowhere parse tracks often use a flat top-level list: an empty
    # ``file_name`` placeholder plus sibling roots whose paths are
    # ``{file_name}/...``.
    anchor_path = ""
    root_nodes: List[dict] = []
    for candidate in (
        str(track).strip("/"),
        str(track.resolve()).strip("/"),
    ):
        if not candidate:
            continue
        hit = _find_anchor(nav_sections, candidate)
        if hit is not None and list(hit.get("children") or ()):
            anchor_path = candidate
            root_nodes = list(hit.get("children") or ())
            break
    if not root_nodes:
        prefix = file_name.strip("/") or str(track.parent.name).strip("/")
        anchor_path = prefix
        for node in nav_sections:
            path = str(node.get("path") or "").strip("/")
            if not path:
                continue
            if path == prefix:
                root_nodes.extend(list(node.get("children") or ()))
                continue
            if prefix and path.startswith(prefix + "/"):
                root_nodes.append(node)
            elif not prefix:
                root_nodes.append(node)
    if not root_nodes:
        raise ValueError(
            f"doc_nav.json has no document roots for track {str(track).strip('/')!r} "
            f"or file_name {file_name!r}"
        )

    sections: List[SectionRow] = []
    path_to_id: Dict[str, str] = {}
    order = 0

    def add(node: dict, parent_id: Optional[str], level: int) -> None:
        nonlocal order
        path = str(node.get("path") or "").strip("/")
        if anchor_path and path.startswith(anchor_path + "/"):
            rel = path[len(anchor_path) + 1 :]
        elif path == anchor_path:
            return
        else:
            rel = path
        if not rel:
            return
        # Local track has no DB surrogate keys; section_path is the stable id.
        # Ownership is via ``owner_document``, not by parsing this string.
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

    for top in root_nodes:
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


class NamespaceKnowhereProvider:
    """Multi-document provider: document ids are DISPATCH-only map nodes.

    Namespace root is empty scope (not a node). ``roots("")`` returns the
    document ids; ``children(document_id)`` returns that document's section
    roots. Section/chunk identity and ownership stay on the real keys.
    """

    def __init__(
        self,
        providers: Sequence[KnowhereProvider],
        *,
        titles: Optional[Dict[str, str]] = None,
    ) -> None:
        self._docs: Dict[str, KnowhereProvider] = {}
        for provider in providers:
            doc_id = str(provider.doc_id or "").strip()
            if not doc_id:
                raise ValueError("KnowhereProvider.doc_id is required")
            if doc_id in self._docs:
                raise ValueError(f"duplicate document_id in namespace: {doc_id}")
            self._docs[doc_id] = provider
        self._titles = {
            str(k): str(v)
            for k, v in (titles or {}).items()
            if str(k).strip() and str(v).strip()
        }
        self._section_owner: Dict[str, str] = {}
        self._chunk_owner: Dict[str, str] = {}
        for doc_id, provider in self._docs.items():
            for sid in provider.all_section_ids():
                self._section_owner[sid] = doc_id
            for sid in provider.all_section_ids():
                for unit in provider.self_units(sid):
                    if unit.chunk_id:
                        self._chunk_owner[unit.chunk_id] = doc_id

    def document_ids(self) -> List[str]:
        return list(self._docs)

    def address_level(self, node_id: str) -> Optional[NavLevel]:
        sid = str(node_id or "").strip()
        if not sid:
            return NavLevel.NAMESPACE
        if sid in self._docs:
            return NavLevel.DOCUMENT
        if sid in self._section_owner:
            return NavLevel.SECTION
        if sid in self._chunk_owner:
            return NavLevel.CHUNK
        return None

    def owner_document(self, node_id: str) -> Optional[str]:
        sid = str(node_id or "").strip()
        if not sid:
            return None
        if sid in self._docs:
            return sid
        return self._section_owner.get(sid) or self._chunk_owner.get(sid)

    def roots(self, doc_id: str) -> Sequence[str]:
        key = str(doc_id or "").strip()
        if not key:
            return list(self._docs)
        provider = self._docs.get(key)
        return list(provider.roots(key)) if provider else []

    def children(self, section_id: str) -> Sequence[str]:
        sid = str(section_id or "").strip()
        if sid in self._docs:
            return list(self._docs[sid].roots(sid))
        owner = self._section_owner.get(sid)
        if not owner:
            return []
        return list(self._docs[owner].children(sid))

    def node_meta(self, section_id: str) -> NodeMeta:
        sid = str(section_id or "").strip()
        if sid in self._docs:
            provider = self._docs[sid]
            n_chunks = sum(
                len(provider.self_units(sec)) for sec in provider.all_section_ids()
            )
            return NodeMeta(
                title=self._titles.get(sid, sid),
                summary="",
                has_children=bool(provider.roots(sid)),
                n_chunks=n_chunks,
            )
        owner = self._section_owner.get(sid)
        if not owner:
            return NodeMeta()
        return self._docs[owner].node_meta(sid)

    def relations(self, section_id: str) -> Tuple[Set[str], Set[str]]:
        sid = str(section_id or "").strip()
        if sid in self._docs:
            descendants = set(self._docs[sid].all_section_ids())
            return set(), descendants
        owner = self._section_owner.get(sid)
        if not owner:
            return set(), set()
        ancestors, descendants = self._docs[owner].relations(sid)
        # Document id is the parent of top-level sections.
        row_parent = self._docs[owner].parent_id(sid)
        if row_parent is None:
            ancestors = set(ancestors) | {owner}
        return ancestors, descendants

    def content(self, section_id: str) -> str:
        sid = str(section_id or "").strip()
        if sid in self._docs:
            provider = self._docs[sid]
            return "\n".join(
                provider.content(root) for root in provider.roots(sid) if provider.content(root)
            )
        owner = self._section_owner.get(sid)
        if not owner:
            return ""
        return self._docs[owner].content(sid)

    def self_units(self, section_id: str) -> List[UnitRow]:
        sid = str(section_id or "").strip()
        if sid in self._docs:
            return []
        owner = self._section_owner.get(sid)
        if not owner:
            return []
        return self._docs[owner].self_units(sid)

    def leaf_ids(self, section_id: str) -> List[str]:
        sid = str(section_id or "").strip()
        if sid in self._docs:
            out: List[str] = []
            for root in self._docs[sid].roots(sid):
                out.extend(self._docs[sid].leaf_ids(root))
            return out
        owner = self._section_owner.get(sid)
        if not owner:
            return []
        return self._docs[owner].leaf_ids(sid)

    def path_titles(self, section_id: str) -> str:
        sid = str(section_id or "").strip()
        if sid in self._docs:
            return self._titles.get(sid, sid)
        owner = self._section_owner.get(sid)
        if not owner:
            return ""
        title = self._docs[owner].path_titles(sid)
        doc_title = self._titles.get(owner, owner)
        return f"{doc_title} / {title}" if title else doc_title

    def parent_id(self, section_id: str) -> Optional[str]:
        sid = str(section_id or "").strip()
        if sid in self._docs:
            return None
        owner = self._section_owner.get(sid)
        if not owner:
            return None
        parent = self._docs[owner].parent_id(sid)
        return parent if parent is not None else owner

    def unit_text(self, unit: UnitRow) -> str:
        owner = self._chunk_owner.get(unit.chunk_id) or self._section_owner.get(
            str(unit.section_id or "")
        )
        if not owner:
            return ""
        return self._docs[owner].unit_text(unit)

    def summaries(self) -> Dict[str, str]:
        out: Dict[str, str] = {}
        for provider in self._docs.values():
            out.update(provider.summaries())
        return out

    def all_section_ids(self) -> List[str]:
        out: List[str] = []
        for provider in self._docs.values():
            out.extend(provider.all_section_ids())
        return out
