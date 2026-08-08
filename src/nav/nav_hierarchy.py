"""Portable kernel seam: HierarchyProvider Protocol + ToolSpace-shaped adapter.

``docs/audit_plan_nav_overlap.md`` (§ToolSpace surface) shows every call site
under ``src/nav`` touches at most 5 hierarchy operations: a document's
top-level sections, a node's children, a node's structural metadata
(title/summary/chunk count), a node's ancestor/descendant ids, and a node's
full-subtree text as one evidence unit. Everything else this codebase's
``ToolSpace`` exposes (BM25/dense scoring, ``read_chunks``, ``_idx``,
``corpus_doc_ids``) is optional — every caller already reaches it through
``getattr(ts, "...", None)`` / ``callable(...)`` guards, so omitting it only
degrades ranking quality, never breaks the pipeline.

``HierarchyProvider`` names that 5-method minimum explicitly.
``ProviderToolSpace`` adapts any implementation of it to the ToolSpace-shaped
duck type every existing ``src/nav`` module already calls, so a knowhere-main
port only has to implement ``HierarchyProvider`` once — no other file in
``src/nav`` needs to change. See ``tests/test_nav_hierarchy_adapter.py`` for
the acceptance test: a pure in-memory provider (no scoring, no ToolSpace)
driving the full plan -> harvest -> plan_control -> settle pipeline.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Protocol, Sequence, Set, Tuple, runtime_checkable


@dataclass
class NodeMeta:
    title: str = ""
    summary: str = ""
    has_children: bool = False
    n_chunks: int = 0


@runtime_checkable
class HierarchyProvider(Protocol):
    """The 5 capabilities every src/nav module needs, and nothing else."""

    def roots(self, doc_id: str) -> Sequence[str]:
        """Top-level section ids for a document (or corpus root)."""
        ...

    def children(self, section_id: str) -> Sequence[str]:
        """Direct child section ids, in document order."""
        ...

    def node_meta(self, section_id: str) -> NodeMeta:
        """Title/summary/chunk-count/has_children for one node."""
        ...

    def relations(self, section_id: str) -> Tuple[Set[str], Set[str]]:
        """(ancestor_ids, descendant_ids); section_id itself excluded from both."""
        ...

    def content(self, section_id: str) -> str:
        """Full text for this node's subtree, as one evidence unit."""
        ...


class ProviderToolSpace:
    """Adapts a ``HierarchyProvider`` to the ToolSpace duck type nav modules use.

    Deliberately does not implement ``_idx`` / ``read_chunks`` /
    ``materialize_self_only_chunks`` / ``corpus_doc_ids`` — the optional
    scoring surface. Grouping/title lookups in ``nav_compose`` and the
    non-map-mode collect fallback in ``nav_agent`` already fall back to
    id-derived defaults when ``_idx`` is absent.
    """

    def __init__(self, provider: HierarchyProvider) -> None:
        self._provider = provider

    def sections_for_doc(self, doc_id: str) -> List[str]:
        return [str(s) for s in self._provider.roots(doc_id)]

    def get_structure(self, section_id: str) -> dict:
        meta = self._provider.node_meta(section_id)
        child_ids = [str(c) for c in self._provider.children(section_id)]
        return {
            "section_id": section_id,
            "level": 0,
            "preview": meta.title,
            "n_lines": 1,
            "n_chunks": int(meta.n_chunks),
            "children": [
                {"section_id": cid, "preview": self._provider.node_meta(cid).title}
                for cid in child_ids
            ],
            "exists": True,
        }

    def _children_for_section_path(
        self, section_id: str, doc_id: str, limit: Optional[int] = None
    ) -> List[dict]:
        del doc_id  # section_id is globally addressable in this provider model.
        child_ids = [str(c) for c in self._provider.children(section_id)]
        if limit is not None:
            child_ids = child_ids[: max(0, int(limit))]
        return [
            {"section_id": cid, "preview": self._provider.node_meta(cid).title}
            for cid in child_ids
        ]

    def section_relation_ids(
        self, section_id: str, doc_id: str
    ) -> Tuple[Set[str], Set[str]]:
        del doc_id
        return self._provider.relations(section_id)

    def _materialize_leaf_path_chunks(self, section_id: str, doc_id: str) -> List[Any]:
        from agent_delivery.code.index_retrieval import Chunk  # type: ignore

        text = str(self._provider.content(section_id) or "")
        if not text.strip():
            return []
        return [
            Chunk(
                node_id=f"{section_id}__path",
                doc_id=doc_id,
                text=text,
                line_ids=(0,),
                section_id=section_id,
            )
        ]


@dataclass
class InMemoryNode:
    section_id: str
    title: str
    content: str = ""
    children: List[str] = field(default_factory=list)


class InMemoryHierarchyProvider:
    """Minimal reference ``HierarchyProvider``: no scoring, no ToolSpace.

    Built directly from a ``{doc_id: [InMemoryNode, ...]}`` map plus a
    ``{doc_id: [root_section_id, ...]}`` map — the "hierarchy + summary is
    enough" claim's simplest possible witness.
    """

    def __init__(
        self,
        *,
        roots_by_doc: Dict[str, Sequence[str]],
        nodes: Dict[str, InMemoryNode],
        summaries: Optional[Dict[str, str]] = None,
    ) -> None:
        self._roots_by_doc = {k: list(v) for k, v in roots_by_doc.items()}
        self._nodes = dict(nodes)
        self._summaries = dict(summaries or {})
        self._parent: Dict[str, str] = {}
        for node in self._nodes.values():
            for child_id in node.children:
                self._parent[child_id] = node.section_id

    def roots(self, doc_id: str) -> Sequence[str]:
        return list(self._roots_by_doc.get(doc_id, ()))

    def children(self, section_id: str) -> Sequence[str]:
        node = self._nodes.get(section_id)
        return list(node.children) if node else []

    def node_meta(self, section_id: str) -> NodeMeta:
        node = self._nodes.get(section_id)
        if node is None:
            return NodeMeta()
        return NodeMeta(
            title=node.title,
            summary=self._summaries.get(section_id, ""),
            has_children=bool(node.children),
            n_chunks=1,
        )

    def relations(self, section_id: str) -> Tuple[Set[str], Set[str]]:
        ancestors: Set[str] = set()
        cur = self._parent.get(section_id)
        while cur:
            ancestors.add(cur)
            cur = self._parent.get(cur)
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
        node = self._nodes.get(section_id)
        if node is None:
            return ""
        parts = [node.content] if node.content else []
        for cid in self.relations(section_id)[1]:
            child = self._nodes.get(cid)
            if child and child.content:
                parts.append(child.content)
        return "\n".join(parts)
