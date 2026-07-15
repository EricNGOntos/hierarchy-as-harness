"""
Plan §5.3：Tool-space 五工具 + refusal（no_match / too_many）。

在现有 CorpusIndex / HierarchicalTools 之上提供统一接口，供 react_agent 调用。
不修改原 HierarchicalTools 的 RAG 实验接口，避免破坏旧 runner。
"""
from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from typing import List, Literal, Optional, Union

from .hierarchical_tools import HierarchicalTools, ToolHit
from .index_retrieval import Chunk, CorpusIndex
from .load_data import line_node_id


RefusalStatus = Literal["no_match", "too_many"]


@dataclass
class Refusal:
    status: RefusalStatus
    message: str
    available_sections: List[str] = field(default_factory=list)
    hint: str = ""


def _toolspace_no_refusal() -> bool:
    """消融：关闭 no_match/too_many 拒答，总是返回可读的 chunk 列表（plan §5 ablation）。"""
    return os.environ.get("TOOLSPACE_NO_REFUSAL", "").strip() in ("1", "true", "yes")


def _env_enabled(name: str, default: str = "1") -> bool:
    return os.environ.get(name, default).strip().lower() not in {"0", "false", "no", "off"}


class ToolSpace:
    """五工具：get_map / get_structure / read_chunks(+refusal) / discover_files / search。"""

    def __init__(self, tools: HierarchicalTools) -> None:
        self._t = tools
        self._idx: CorpusIndex = tools.index
        self._leaf_path_cache: dict[tuple[str, str], List[Chunk]] = {}

    def _synthetic_root_enabled(self) -> bool:
        return _env_enabled("NAV_SYNTHETIC_ROOT_SECTIONS", "1")

    def _direct_search_mode(self) -> str:
        raw = os.environ.get("NAV_HYBRID_DIRECT_SEARCH", "auto").strip().lower()
        if raw in {"0", "false", "no", "off"}:
            return "off"
        if raw in {"1", "true", "yes", "on", "always"}:
            return "always"
        return "auto"

    def _doc_root_id(self, doc_id: str) -> str:
        return f"{doc_id}:__doc_root"

    def _prefix_id(self, doc_id: str) -> str:
        return f"{doc_id}:__prefix"

    def _synthetic_doc_id(self, section_id: str) -> Optional[str]:
        if section_id.endswith(":__doc_root"):
            return section_id[: -len(":__doc_root")]
        if section_id.endswith(":__prefix"):
            return section_id[: -len(":__prefix")]
        return None

    def _top_level_anchor_indices(self, doc_id: str) -> List[int]:
        b = self._idx._bundles.get(doc_id)
        if not b:
            return []
        return [j for j, level in enumerate(b.levels_for_tree) if level == 1]

    def _doc_needs_direct_search(self, doc_id: Optional[str]) -> bool:
        if not doc_id:
            return True
        b = self._idx._bundles.get(doc_id)
        if not b or not b.lines:
            return False
        levels = list(b.levels_for_tree)
        if levels and levels[0] != 0:
            return True
        anchors = self._top_level_anchor_indices(doc_id)
        if not anchors:
            return True
        prefix_min = max(
            1,
            int(os.environ.get("NAV_SYNTHETIC_PREFIX_MIN_LINES", "2").strip() or "2"),
        )
        if int(anchors[0]) >= prefix_min:
            return True
        return any(levels[i] > levels[i - 1] + 1 for i in range(1, len(levels)))

    def _synthetic_section_bounds(
        self, section_id: str, doc_id: str
    ) -> Optional[tuple[int, int]]:
        if not self._synthetic_root_enabled():
            return None
        b = self._idx._bundles.get(doc_id)
        if not b or not b.lines:
            return None
        if section_id == self._doc_root_id(doc_id):
            return (0, len(b.lines))
        if section_id == self._prefix_id(doc_id):
            anchors = self._top_level_anchor_indices(doc_id)
            if not anchors:
                return None
            prefix_min = max(
                1,
                int(os.environ.get("NAV_SYNTHETIC_PREFIX_MIN_LINES", "2").strip() or "2"),
            )
            first_anchor = int(anchors[0])
            if first_anchor >= prefix_min:
                return (0, first_anchor)
        return None

    def _synthetic_child_rows(
        self, section_id: str, doc_id: str, limit: int = 24
    ) -> List[dict]:
        bounds = self._synthetic_section_bounds(section_id, doc_id)
        b = self._idx._bundles.get(doc_id)
        parents = self._idx._doc_parents.get(doc_id, [])
        if bounds is None or not b:
            return []
        start, end = bounds
        children: List[dict] = []
        for j in range(start, end):
            if j >= len(b.lines):
                continue
            level = b.levels_for_tree[j] if j < len(b.levels_for_tree) else 0
            if level <= 0:
                continue
            parent = parents[j] if j < len(parents) else None
            parent_level = (
                b.levels_for_tree[parent]
                if parent is not None and 0 <= parent < len(b.levels_for_tree)
                else 0
            )
            if parent is not None and start <= parent < end and parent_level > 0:
                continue
            rec = b.lines[j]
            children.append(
                {
                    "section_id": line_node_id(doc_id, rec.line_id),
                    "level": level,
                    "preview": (rec.content or "")[:160],
                }
            )
            if len(children) >= limit:
                break
        return children

    # --- 1) get_map ---
    def get_map(self, doc_id: str) -> str:
        """返回文档内完整 top-level section 骨架，供 agent 自主选路。"""
        lines_out: List[str] = []
        for sid in self._sections_for_doc(doc_id):
            pool = self._pool_for_section_path(sid, doc_id)
            if not pool:
                continue
            prev = (pool[0].text or "")[:120].replace("\n", " ")
            lines_out.append(f"- {sid} :: {prev}")
        if not lines_out:
            return f"(empty map for doc_id={doc_id})"
        return "sections:\n" + "\n".join(lines_out)

    def _sections_for_doc(self, doc_id: str) -> List[str]:
        b = self._idx._bundles.get(doc_id)
        if b and b.lines:
            anchors = self._top_level_anchor_indices(doc_id)
            if self._synthetic_root_enabled():
                if not anchors:
                    return [self._doc_root_id(doc_id)]
                out: List[str] = []
                if self._synthetic_section_bounds(self._prefix_id(doc_id), doc_id):
                    out.append(self._prefix_id(doc_id))
                out.extend(line_node_id(doc_id, b.lines[j].line_id) for j in anchors)
                if out:
                    return out
            if anchors:
                return [line_node_id(doc_id, b.lines[j].line_id) for j in anchors]
            return [line_node_id(doc_id, b.lines[0].line_id)]
        out: List[str] = []
        for sid, pool in self._idx.fact_by_section.items():
            if pool and pool[0].doc_id == doc_id:
                out.append(sid)
        return out

    def _resolve_section_path(self, section_path: Optional[str], doc_id: str) -> Optional[str]:
        if not section_path or not str(section_path).strip():
            return None
        sp = str(section_path).strip()
        if sp.endswith("__path"):
            sp = sp[: -len("__path")]
        if self._synthetic_section_bounds(sp, doc_id):
            return sp
        if sp in self._idx.fact_by_section:
            return sp
        if sp in self._idx._node_to_doc_line:
            ndoc, _ = self._idx._node_to_doc_line[sp]
            if ndoc == doc_id:
                return sp
        m = re.search(r"(?:^|:)L(\d+)$", sp, flags=re.I)
        if m:
            nid = line_node_id(doc_id, int(m.group(1)))
            if nid in self._idx._node_to_doc_line:
                return nid
        # 允许只写 "L12" / 行号片段
        for sid in self._all_node_ids_for_doc(doc_id):
            if sp in sid or sid.endswith(sp):
                return sid
        return None

    def sections_for_doc(self, doc_id: str) -> List[str]:
        """公开给 agent prompt 使用：只列 top-level，不做 query 路由裁剪。"""
        return self._sections_for_doc(doc_id)

    def _all_node_ids_for_doc(self, doc_id: str) -> List[str]:
        b = self._idx._bundles.get(doc_id)
        if not b:
            return self._sections_for_doc(doc_id)
        return [line_node_id(doc_id, r.line_id) for r in b.lines]

    def _pool_for_section_path(self, section_id: str, doc_id: str) -> List[Chunk]:
        """返回任意层级节点覆盖的子树 small chunks；兼容旧的 level-1 fact_by_section。"""
        synthetic_bounds = self._synthetic_section_bounds(section_id, doc_id)
        if synthetic_bounds is not None:
            b = self._idx._bundles.get(doc_id)
            if not b:
                return []
            start, end = synthetic_bounds
            node_to_chunk = {c.node_id: c for c in self._idx.small_chunks if c.doc_id == doc_id}
            out: List[Chunk] = []
            for rec in b.lines[start:end]:
                chunk = node_to_chunk.get(line_node_id(doc_id, rec.line_id))
                if chunk is not None:
                    out.append(chunk)
            return out
        if section_id in self._idx.fact_by_section:
            return [
                c
                for c in self._idx.fact_by_section.get(section_id, [])
                if c.doc_id == doc_id
            ]
        loc = self._idx._node_to_doc_line.get(section_id)
        b = self._idx._bundles.get(doc_id)
        if not loc or loc[0] != doc_id or not b:
            return []
        _, start = loc
        levels = b.levels_for_tree
        base_level = levels[start] if start < len(levels) else 0
        end = len(b.lines)
        if base_level > 0:
            for j in range(start + 1, len(b.lines)):
                lev = levels[j] if j < len(levels) else 0
                if lev > 0 and lev <= base_level:
                    end = j
                    break
        node_to_chunk = {c.node_id: c for c in self._idx.small_chunks if c.doc_id == doc_id}
        out: List[Chunk] = []
        for rec in b.lines[start:end]:
            nid = line_node_id(doc_id, rec.line_id)
            c = node_to_chunk.get(nid)
            if c is not None:
                out.append(c)
        return out

    def _subtree_bounds_for_section_path(
        self, section_id: str, doc_id: str
    ) -> Optional[tuple[int, int]]:
        """返回 section_path 在 bundle.lines 中覆盖的 [start, end) 范围。"""
        synthetic_bounds = self._synthetic_section_bounds(section_id, doc_id)
        if synthetic_bounds is not None:
            return synthetic_bounds
        loc = self._idx._node_to_doc_line.get(section_id)
        b = self._idx._bundles.get(doc_id)
        if not loc or loc[0] != doc_id or not b:
            return None
        _, start = loc
        levels = b.levels_for_tree
        base_level = levels[start] if start < len(levels) else 0
        end = len(b.lines)
        if base_level > 0:
            for j in range(start + 1, len(b.lines)):
                lev = levels[j] if j < len(levels) else 0
                if lev > 0 and lev <= base_level:
                    end = j
                    break
        return start, end

    def section_relation_ids(self, section_id: str, doc_id: str) -> tuple[set[str], set[str]]:
        """Return structural ancestors and subtree section ids for navigation coverage."""
        bounds = self._subtree_bounds_for_section_path(section_id, doc_id)
        b = self._idx._bundles.get(doc_id)
        if bounds is None or not b:
            return set(), {section_id}
        start, end = bounds
        ancestors = set(self._idx.ancestor_line_node_ids(section_id))
        if self._synthetic_section_bounds(section_id, doc_id) is not None:
            ancestors = set()
        # Some document trees contain wrapper headings that span the target but
        # are not linked by the normalized parent pointer chain.
        for j in range(0, start):
            level = b.levels_for_tree[j] if j < len(b.levels_for_tree) else 0
            if level <= 0:
                continue
            candidate = line_node_id(doc_id, b.lines[j].line_id)
            candidate_bounds = self._subtree_bounds_for_section_path(candidate, doc_id)
            if candidate_bounds and candidate_bounds[0] <= start < candidate_bounds[1]:
                ancestors.add(candidate)
        descendants = {section_id}
        for j in range(start, end):
            level = b.levels_for_tree[j] if j < len(b.levels_for_tree) else 0
            if level > 0:
                descendants.add(line_node_id(doc_id, b.lines[j].line_id))
        ancestors.discard(section_id)
        return ancestors, descendants

    def materialize_self_only_chunks(self, section_id: str, doc_id: str) -> List[Chunk]:
        """Return chunks for this node only (exclude descendant sections).

        Used by map scoring / intro units so self text is not diluted by the
        full subtree (Knowhere self_only hydration analogue).
        """
        bounds = self._subtree_bounds_for_section_path(section_id, doc_id)
        b = self._idx._bundles.get(doc_id)
        if bounds is None or not b:
            return []
        start, end = bounds
        levels = b.levels_for_tree
        is_synthetic = self._synthetic_section_bounds(section_id, doc_id) is not None
        base_level = 0 if is_synthetic else (levels[start] if start < len(levels) else 0)
        # Self span: from node start until the first structural child (deeper level).
        self_end = end
        if base_level >= 0:
            for j in range(start + 1, end):
                lev = levels[j] if j < len(levels) else 0
                if lev > base_level:
                    self_end = j
                    break
                if base_level > 0 and lev > 0 and lev <= base_level:
                    self_end = j
                    break
        node_to_chunk = {c.node_id: c for c in self._idx.small_chunks if c.doc_id == doc_id}
        out: List[Chunk] = []
        for rec in b.lines[start:self_end]:
            chunk = node_to_chunk.get(line_node_id(doc_id, rec.line_id))
            if chunk is not None:
                out.append(chunk)
        return out

    def _materialize_leaf_path_chunks(self, section_id: str, doc_id: str) -> List[Chunk]:
        """
        将一个 section_path 子树物化为 evidence units。

        旧实现直接返回子树内的行级 chunks；这里按“叶节/路径块”组织：
        每个 chunk 以叶节 subtree 为正文，并把从所选 section 到叶节的标题路径放入文本。
        这样预算填充和 compose 看到的是可引用的 section/path evidence unit，而不是孤立行。
        """
        cache_key = (doc_id, section_id)
        cached = self._leaf_path_cache.get(cache_key)
        if cached is not None:
            return list(cached)

        bounds = self._subtree_bounds_for_section_path(section_id, doc_id)
        b = self._idx._bundles.get(doc_id)
        if bounds is None or not b:
            return []
        start, end = bounds
        if start >= end:
            return []

        levels = b.levels_for_tree
        parents = self._idx._doc_parents.get(doc_id, [])
        is_synthetic = self._synthetic_section_bounds(section_id, doc_id) is not None
        base_level = 0 if is_synthetic else (levels[start] if start < len(levels) else 0)

        def lev_at(i: int) -> int:
            return levels[i] if i < len(levels) else 0

        def next_boundary(root: int) -> int:
            root_level = lev_at(root)
            if root_level <= 0:
                return min(root + 1, end)
            for k in range(root + 1, end):
                lk = lev_at(k)
                if lk > 0 and lk <= root_level:
                    return k
            return end

        def has_deeper_structural_child(root: int, root_end: int) -> bool:
            root_level = lev_at(root)
            if root_level <= 0:
                return False
            for k in range(root + 1, root_end):
                if lev_at(k) > root_level:
                    return True
            return False

        structural = [
            j
            for j in range(start, end)
            if j == start or (lev_at(j) > max(base_level, 0))
        ]
        leaf_roots: List[int] = []
        for j in structural:
            rb = next_boundary(j)
            if not has_deeper_structural_child(j, rb):
                leaf_roots.append(j)

        if not leaf_roots:
            leaf_roots = [start]

        # Preserve section-level intro text before the first child subsection.
        first_child = next((j for j in leaf_roots if j > start), None)
        spans: List[tuple[str, int, int]] = []
        if first_child is not None and first_child > start + 1:
            spans.append(("intro", start, first_child))
        for root in leaf_roots:
            spans.append(("leaf", root, next_boundary(root)))

        chunks: List[Chunk] = []
        seen_spans: set[tuple[int, int]] = set()
        for kind, root, root_end in spans:
            root_end = max(root + 1, min(root_end, end))
            key = (root, root_end)
            if key in seen_spans:
                continue
            seen_spans.add(key)

            path_indices: List[int] = []
            cur: Optional[int] = root
            visited = 0
            while cur is not None and start <= cur < end and visited <= len(b.lines):
                if cur == start or lev_at(cur) > 0:
                    path_indices.append(cur)
                cur = parents[cur] if cur < len(parents) else None
                visited += 1
            path_indices = list(reversed(path_indices))

            body_indices = list(range(root, root_end))
            text_parts: List[str] = []
            path_only = [i for i in path_indices if i not in set(body_indices)]
            if path_only:
                ctx = " / ".join(
                    (b.lines[i].content or "").strip()[:40] for i in path_only
                )
                text_parts.append(f"[§ {ctx}]")
            text_parts.extend(
                (b.lines[i].content or "").strip() for i in body_indices
            )
            line_ids = tuple(
                b.lines[i].line_id for i in sorted(set(path_indices + body_indices))
            )
            root_nid = line_node_id(doc_id, b.lines[root].line_id)
            suffix = "intro" if kind == "intro" else "path"
            chunks.append(
                Chunk(
                    node_id=f"{root_nid}__{suffix}",
                    doc_id=doc_id,
                    text="\n".join(p for p in text_parts if p),
                    line_ids=line_ids,
                    section_id=section_id,
                )
            )
        self._leaf_path_cache[cache_key] = chunks
        return list(chunks)

    def _materialize_doc_leaf_path_chunks(self, doc_id: str) -> List[Chunk]:
        """返回整个文档的 leaf/path evidence pool，供 toolspace search 使用。"""
        out: List[Chunk] = []
        seen: set[str] = set()
        for sid in self._sections_for_doc(doc_id):
            for c in self._materialize_leaf_path_chunks(sid, doc_id):
                if c.node_id in seen:
                    continue
                seen.add(c.node_id)
                out.append(c)
        if out:
            return out
        # flat / malformed tree fallback：保留可用性，但正常 hierarchical 路径不会走到这里。
        return [c for c in self._idx.small_chunks if c.doc_id == doc_id]

    def materialize_doc_leaf_path_chunks(self, doc_id: str) -> List[Chunk]:
        """Public retrieval-only access to the multi-level leaf/path evidence pool."""
        return self._materialize_doc_leaf_path_chunks(doc_id)

    def _leaf_path_search_pool(self, doc_id: Optional[str]) -> List[Chunk]:
        if doc_id:
            return self._materialize_doc_leaf_path_chunks(doc_id)
        out: List[Chunk] = []
        for did in sorted(self._idx._bundles.keys()):
            out.extend(self._materialize_doc_leaf_path_chunks(did))
        return out

    def leaf_path_search_pool(self, doc_id: Optional[str]) -> List[Chunk]:
        """Public retrieval-only access to leaf/path chunks, optionally scoped to one document."""
        return self._leaf_path_search_pool(doc_id)

    def _children_for_section_path(self, section_id: str, doc_id: str, limit: int | None = None) -> List[dict]:
        if limit is None:
            # Map mode needs full fan-out; legacy projection keeps a modest default.
            if os.environ.get("NAV_MAP_MODE", "0").strip().lower() not in {"0", "false", "no", "off", ""}:
                limit = max(1, int(os.environ.get("NAV_MAP_CHILDREN_LIMIT", "10000") or "10000"))
            else:
                limit = 24

        synthetic_children = self._synthetic_child_rows(section_id, doc_id, limit=limit)
        if synthetic_children:
            return synthetic_children
        loc = self._idx._node_to_doc_line.get(section_id)
        b = self._idx._bundles.get(doc_id)
        parents = self._idx._doc_parents.get(doc_id, [])
        if not loc or loc[0] != doc_id or not b:
            return []
        _, parent_j = loc
        children: List[dict] = []
        for j, p in enumerate(parents):
            if p != parent_j or j >= len(b.lines):
                continue
            rec = b.lines[j]
            children.append(
                {
                    "section_id": line_node_id(doc_id, rec.line_id),
                    "level": b.levels_for_tree[j] if j < len(b.levels_for_tree) else 0,
                    "preview": (rec.content or "")[:160],
                }
            )
            if len(children) >= limit:
                break
        return children

    # --- 2) get_structure ---
    def get_structure(self, section_id: str) -> dict:
        loc = self._idx._node_to_doc_line.get(section_id)
        doc_id = loc[0] if loc else (self._synthetic_doc_id(section_id) or "")
        pool = self._pool_for_section_path(section_id, doc_id) if doc_id else []
        leaf_chunks = self._materialize_leaf_path_chunks(section_id, doc_id) if doc_id else []
        if not pool:
            return {
                "section_id": section_id,
                "n_chunks": 0,
                "n_leaf_path_chunks": 0,
                "n_lines": 0,
                "preview": "",
                "children": [],
                "exists": False,
            }
        return {
            "section_id": section_id,
            "level": 0 if self._synthetic_section_bounds(section_id, doc_id) is not None else None,
            "n_chunks": len(leaf_chunks) if leaf_chunks else len(pool),
            "n_leaf_path_chunks": len(leaf_chunks),
            "n_lines": len(pool),
            "preview": (pool[0].text or "")[:200],
            "children": self._children_for_section_path(section_id, doc_id),
            "exists": True,
        }

    # --- 3) read_chunks (+ refusal) ---
    def read_chunks(
        self,
        section_path: Optional[str],
        keywords: Optional[str],
        *,
        doc_id: str,
        too_many_threshold: int = 20,
        k: int = 48,
    ) -> Union[List[ToolHit], Refusal]:
        """
        - section_path 为空：在全文档 leaf/path 池上按 keywords 检索；若候选过大 → too_many。
        - section_path 非空：解析到任意层级节点后，读取该子树物化出的 leaf/path chunks。
        """
        q = (keywords or "").strip()
        if not section_path or not str(section_path).strip():
            pool = self._materialize_doc_leaf_path_chunks(doc_id)
            if not pool:
                if _toolspace_no_refusal():
                    return []
                return Refusal(
                    status="too_many",
                    message="empty document pool",
                    hint="narrow with sectionPath",
                )
            # 主线策略：无 sectionPath 时，若候选池本身已很大，直接返回 too_many，
            # 迫使 agent 先缩小到章节级，避免“全局检索误读为可直接阅读”。
            if len(pool) > too_many_threshold:
                if _toolspace_no_refusal():
                    scored = self._idx.search(q, pool, min(len(pool), 400), doc_id_filter=doc_id)
                    strong = [(c, s) for c, s in scored if s > 0.0]
                    return [ToolHit(chunk=c, score=s) for c, s in strong[:too_many_threshold]]
                avail = self._sections_for_doc(doc_id)
                return Refusal(
                    status="too_many",
                    message=f"document pool {len(pool)} chunks > {too_many_threshold} without sectionPath",
                    available_sections=avail,
                    hint="请提供 sectionPath 缩小到某一节",
                )
            scored = self._idx.search(q, pool, min(len(pool), 400), doc_id_filter=doc_id)
            strong = [(c, s) for c, s in scored if s > 0.0]
            if len(strong) > too_many_threshold:
                if _toolspace_no_refusal():
                    return [ToolHit(chunk=c, score=s) for c, s in strong[:too_many_threshold]]
                avail = self._sections_for_doc(doc_id)
                return Refusal(
                    status="too_many",
                    message=f"matched {len(strong)} chunks > {too_many_threshold} without sectionPath",
                    available_sections=avail,
                    hint="请提供 sectionPath 缩小到某一节",
                )
            return [ToolHit(chunk=c, score=s) for c, s in strong[:k]]

        sid = self._resolve_section_path(section_path, doc_id)
        if sid is None:
            if _toolspace_no_refusal():
                pool_fb = self._materialize_doc_leaf_path_chunks(doc_id)
                scored = self._idx.search(q, pool_fb, min(len(pool_fb), 400), doc_id_filter=doc_id)
                strong = [(c, s) for c, s in scored if s > 0.0]
                return [ToolHit(chunk=c, score=s) for c, s in strong[:k]]
            return Refusal(
                status="no_match",
                message=f"section_path not found: {section_path!r}",
                available_sections=self._sections_for_doc(doc_id),
                hint="从 get_map / discover_files 返回的 section_id 中选择",
            )
        pool = list(self._idx.fact_by_section.get(sid, []))
        if not pool:
            pool = self._pool_for_section_path(sid, doc_id)
        if not pool:
            if _toolspace_no_refusal():
                return []
            return Refusal(
                status="no_match",
                message=f"empty section: {sid}",
                available_sections=self._sections_for_doc(doc_id),
            )
        evidence_pool = self._materialize_leaf_path_chunks(sid, doc_id)
        if not evidence_pool:
            evidence_pool = pool
        scored = self._idx.search(
            q, evidence_pool, min(len(evidence_pool), k * 2), doc_id_filter=doc_id
        )
        out = [ToolHit(chunk=c, score=s) for c, s in scored[:k]]
        return out

    # --- 4) discover_files ---
    def discover_files(self, keywords: str, *, max_docs: int = 24) -> List[str]:
        """全库关键词检索节摘要，返回 doc_id 列表。"""
        pool = self._idx.section_summaries
        if not pool:
            return []
        scored = self._idx.search(keywords, pool, min(len(pool), 200), doc_id_filter=None)
        seen: set[str] = set()
        out: List[str] = []
        for c, s in scored:
            if s <= 0.0:
                continue
            if c.doc_id not in seen:
                seen.add(c.doc_id)
                out.append(c.doc_id)
            if len(out) >= max_docs:
                break
        return out

    # --- 5) search ---
    def search(self, query: str, k: int, *, doc_id: Optional[str] = None) -> List[ToolHit]:
        pool = self._leaf_path_search_pool(doc_id)
        if not pool:
            return self._t.search_small(query, k, doc_id=doc_id)
        scored = self._idx.search(query, pool, min(len(pool), k), doc_id_filter=doc_id)
        return [ToolHit(chunk=c, score=s) for c, s in scored]

    def _direct_line_window_chunk(
        self,
        chunk: Chunk,
        *,
        before: int,
        after: int,
    ) -> Chunk:
        loc = self._idx._node_to_doc_line.get(chunk.node_id)
        b = self._idx._bundles.get(chunk.doc_id)
        if not loc or not b:
            return chunk
        _, j = loc
        start = max(0, j - max(0, before))
        end = min(len(b.lines), j + max(0, after) + 1)
        records = b.lines[start:end]
        line_ids = tuple(rec.line_id for rec in records)
        text = "\n".join((rec.content or "").strip() for rec in records if (rec.content or "").strip())
        return Chunk(
            node_id=f"{chunk.node_id}__directwin",
            doc_id=chunk.doc_id,
            text=text or chunk.text,
            line_ids=line_ids or chunk.line_ids,
            section_id=chunk.section_id,
        )

    def hybrid_search(
        self,
        query: str,
        k: int,
        *,
        doc_id: Optional[str] = None,
        task_type: str = "unknown",
    ) -> List[ToolHit]:
        """
        Query-only search that combines hierarchical leaf/path chunks with
        direct line chunks. This makes noisy predicted trees robust without
        using gold labels or task-specific evidence ids.
        """
        mode = self._direct_search_mode()
        if mode == "off":
            return self.search(query, k, doc_id=doc_id)
        if mode == "auto" and not self._doc_needs_direct_search(doc_id):
            return self.search(query, k, doc_id=doc_id)

        k = max(0, int(k))
        if k <= 0:
            return []

        leaf_pool = self._leaf_path_search_pool(doc_id)
        direct_pool = [
            chunk for chunk in self._idx.small_chunks if doc_id is None or chunk.doc_id == doc_id
        ]
        leaf_k = min(len(leaf_pool), max(k, int(os.environ.get("NAV_HYBRID_LEAF_K", str(k)).strip() or k)))
        direct_k = min(
            len(direct_pool),
            max(k, int(os.environ.get("NAV_HYBRID_DIRECT_K", str(k)).strip() or k)),
        )
        scored_leaf = self._idx.search(query, leaf_pool, leaf_k, doc_id_filter=doc_id) if leaf_pool else []
        scored_direct = (
            self._idx.search(query, direct_pool, direct_k, doc_id_filter=doc_id) if direct_pool else []
        )

        is_scope = (task_type or "").strip().lower() in {"scope_collection", "regulatory_coverage"}
        before = int(os.environ.get("NAV_SCOPE_DIRECT_WINDOW_BEFORE", "1").strip() or "1")
        after = int(os.environ.get("NAV_SCOPE_DIRECT_WINDOW_AFTER", "1").strip() or "1")
        direct_bonus = float(os.environ.get("NAV_HYBRID_DIRECT_SCORE_BONUS", "0.0").strip() or "0.0")

        merged: dict[str, ToolHit] = {}
        for chunk, score in scored_leaf:
            merged[chunk.node_id] = ToolHit(chunk=chunk, score=float(score))
        for chunk, score in scored_direct:
            out_chunk = self._direct_line_window_chunk(chunk, before=before, after=after) if is_scope else chunk
            out_score = float(score) + direct_bonus
            prev = merged.get(out_chunk.node_id)
            if prev is None or out_score > prev.score:
                merged[out_chunk.node_id] = ToolHit(chunk=out_chunk, score=out_score)

        out = list(merged.values())
        out.sort(key=lambda hit: (-float(hit.score), hit.chunk.node_id))
        return out[:k]
