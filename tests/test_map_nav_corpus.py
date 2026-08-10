"""Golden Map namespace mode: document-as-node tree, actions, depth-neutral DISPATCH."""
from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path
from typing import List, Tuple
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
for p in (ROOT / "src" / "realdata", ROOT / "src" / "nav"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from agent_delivery.code.index_retrieval import Chunk, CorpusIndex  # noqa: E402
from agent_delivery.code.load_data import DocBundle, LineRecord  # noqa: E402
from agent_delivery.code.hierarchical_tools import HierarchicalTools  # noqa: E402
from agent_delivery.code.tool_space import ToolSpace  # noqa: E402
from nav_actions import build_legal_actions  # noqa: E402
from nav_address import is_dispatch_only_node  # noqa: E402
from nav_map_scores import compute_corpus_map_and_unit_scores  # noqa: E402
from nav_navigate import (  # noqa: E402
    _fork_nav_state,
    _merge_nav_state,
    dispatch,
    sort_collected_by_doc_order,
)
from nav_projection import build_map  # noqa: E402
from nav_types import (  # noqa: E402
    ActionKind,
    NavConfig,
    NavState,
    Projection,
    RegionReport,
    SectionView,
)


def _bundle(doc_id: str, lines: List[Tuple[int, int, str]]) -> DocBundle:
    """lines: (line_id, level, content)."""
    recs = [
        LineRecord(
            doc_id=doc_id,
            line_id=lid,
            content=text,
            gold_level=lev,
            pred_level=lev,
        )
        for lid, lev, text in lines
    ]
    levels = [lev for _lid, lev, _t in lines]
    return DocBundle(doc_id=doc_id, lines=recs, levels_for_tree=levels)


def _tiny_index() -> CorpusIndex:
    bundles = [
        _bundle(
            "docA",
            [
                (0, 0, "Document A Title"),
                (1, 1, "A Chapter One"),
                (2, 2, "A leaf about safety"),
            ],
        ),
        _bundle(
            "docB",
            [
                (0, 0, "Document B Title"),
                (1, 1, "B Chapter One"),
                (2, 2, "B leaf about payroll"),
            ],
        ),
    ]
    return CorpusIndex.from_bundles(
        bundles, tree_mode="hierarchical", retrieval_backend="dense", embedding_model=None
    )


class ToolSpaceNamespaceRootTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tools = HierarchicalTools(_tiny_index())
        self.ts = ToolSpace(self.tools, corpus_doc_ids=["docA", "docB"])

    def test_sections_and_children(self) -> None:
        tops = self.ts.sections_for_doc("")
        self.assertEqual(tops, ["docA", "docB"])
        self.assertEqual(self.ts.document_ids(), ["docA", "docB"])
        self.assertEqual(self.ts.address_level("docA"), "document")
        self.assertEqual(self.ts.owner_document("docA:L1"), "docA")
        kids = self.ts._children_for_section_path("docA", "docA")
        self.assertTrue(any(k["section_id"] == "docA:L1" for k in kids))

    def test_get_structure_document_node(self) -> None:
        st = self.ts.get_structure("")
        self.assertTrue(st["exists"])
        self.assertEqual([c["section_id"] for c in st["children"]], ["docA", "docB"])
        st_a = self.ts.get_structure("docA")
        self.assertTrue(st_a["exists"])
        self.assertIn("Document A", st_a["preview"])


class MapBuildAndActionsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tools = HierarchicalTools(_tiny_index())
        self.ts = ToolSpace(self.tools, corpus_doc_ids=["docA", "docB"])
        self.cfg = NavConfig(map_mode=True, map_char_limit=5000, collect_top_k=6)

    def test_build_map_shows_document_nodes(self) -> None:
        map_scores, _unit_scores = compute_corpus_map_and_unit_scores(
            self.ts, doc_ids=["docA", "docB"], query="safety"
        )
        self.assertIn("docA", map_scores)
        self.assertIn("docB", map_scores)
        proj = build_map(
            self.ts,
            doc_id="",
            query="safety",
            scope=None,
            config=self.cfg,
            map_scores=map_scores,
            highlight_ids=["docA:L2"],
        )
        sids = {v.section_id for v in proj.tree_sections}
        self.assertIn("docA", sids)
        self.assertIn("docB", sids)

    def test_corpus_scores_all_units_in_one_global_pool(self) -> None:
        seen: dict = {}

        def fake_dense(
            texts,
            query,
            *,
            unit_ids=None,
            doc_id=None,
            channel="content",
            namespace=None,
        ):
            del texts, query, channel, namespace
            self.assertIn(doc_id, {"docA", "docB"})
            return [0.5 for _ in (unit_ids or [])]

        def fake_hybrid(rows, query, **kwargs):
            del query
            seen["calls"] = seen.get("calls", 0) + 1
            seen["unit_ids"] = [row["chunk_id"] for row in rows]
            seen["kwargs"] = kwargs
            return [
                dict(row, score=0.9 if row["chunk_id"].startswith("docA:") else 0.2)
                for row in rows
            ]

        with (
            mock.patch("nav_map_scores.score_dense_channel", side_effect=fake_dense),
            mock.patch("nav_map_scores.score_rows_hybrid_all", side_effect=fake_hybrid),
            mock.patch(
                "nav_map_scores.compute_map_and_unit_scores",
                side_effect=AssertionError("corpus mode must not use per-doc RRF"),
            ),
        ):
            map_scores, unit_scores = compute_corpus_map_and_unit_scores(
                self.ts, doc_ids=["docA", "docB"], query="safety"
            )

        self.assertEqual(seen["calls"], 1)
        self.assertTrue(any(uid.startswith("docA:") for uid in seen["unit_ids"]))
        self.assertTrue(any(uid.startswith("docB:") for uid in seen["unit_ids"]))
        self.assertNotIn("doc_id", seen["kwargs"])
        dense = seen["kwargs"]["dense_scores_by_channel"]
        self.assertEqual(set(dense), {"path", "content"})
        self.assertEqual(set(dense["path"]), set(seen["unit_ids"]))
        self.assertEqual(set(dense["content"]), set(seen["unit_ids"]))
        self.assertEqual(set(unit_scores), set(seen["unit_ids"]))
        self.assertGreater(map_scores["docA"], map_scores["docB"])

    def test_global_rrf_preserves_cross_doc_relevance(self) -> None:
        index = CorpusIndex.from_bundles(
            [
                _bundle(
                    "gold",
                    [
                        (0, 0, "target exact title"),
                        (1, 1, "target exact fact"),
                    ],
                ),
                _bundle(
                    "wrong",
                    [
                        (0, 0, "target attachment"),
                        (1, 1, "target unrelated"),
                    ],
                ),
            ],
            tree_mode="hierarchical",
            retrieval_backend="dense",
            embedding_model=None,
        )
        ts = ToolSpace(
            HierarchicalTools(index),
            corpus_doc_ids=["gold", "wrong"],
        )
        with mock.patch.dict(os.environ, {"NAV_MAP_DENSE": "0"}):
            map_scores, _unit_scores = compute_corpus_map_and_unit_scores(
                ts,
                doc_ids=["gold", "wrong"],
                query="target exact",
            )
        self.assertGreater(map_scores["gold"], map_scores["wrong"])

    def test_document_nodes_dispatch_only(self) -> None:
        state = NavState(doc_id="", query="q", task_type="niche_fact")
        views = [
            SectionView(
                section_id="docA",
                level=0,
                preview="A",
                score=0.9,
                n_lines=3,
                n_chunks=3,
                has_children=True,
                depth_from_scope=0,
                title="A",
                map_id="N1",
            ),
            SectionView(
                section_id="docA:L2",
                level=2,
                preview="leaf",
                score=0.8,
                n_lines=1,
                n_chunks=1,
                has_children=False,
                depth_from_scope=1,
                title="leaf",
                map_id="N2",
            ),
        ]
        proj = Projection(
            doc_id="",
            scope=None,
            text="",
            visible_sections=views,
            truncated=False,
            tree_sections=views,
            highlight_ids=["docA:L2"],
        )
        actions = build_legal_actions(state, proj, step_idx=0, config=self.cfg, depth=0, ts=self.ts)
        by_sid: dict[str, set] = {}
        for a in actions:
            if a.section_id:
                by_sid.setdefault(a.section_id, set()).add(a.kind)
        self.assertNotIn(ActionKind.COLLECT, by_sid.get("docA", set()))
        self.assertIn(ActionKind.DISPATCH, by_sid.get("docA", set()))
        self.assertIn(ActionKind.COLLECT, by_sid.get("docA:L2", set()))
        self.assertTrue(is_dispatch_only_node(self.ts, "docA"))
        self.assertIn(ActionKind.FINISH, {a.kind for a in actions})

        # Inside a document episode: no self-DISPATCH on the document scope.
        state.current_scope = "docA"
        state.doc_id = "docA"
        proj_scoped = Projection(
            doc_id="docA",
            scope="docA",
            text="",
            visible_sections=views,
            truncated=False,
            tree_sections=views,
            highlight_ids=["docA:L2"],
        )
        actions2 = build_legal_actions(
            state, proj_scoped, step_idx=0, config=self.cfg, depth=0, ts=self.ts
        )
        by_sid2: dict[str, set] = {}
        for a in actions2:
            if a.section_id:
                by_sid2.setdefault(a.section_id, set()).add(a.kind)
        self.assertNotIn(ActionKind.DISPATCH, by_sid2.get("docA", set()))
        self.assertIn(ActionKind.FINISH, {a.kind for a in actions2})


class DepthNeutralDispatchTests(unittest.TestCase):
    def test_namespace_to_doc_resets_depth_and_doc_id(self) -> None:
        ts = ToolSpace(HierarchicalTools(_tiny_index()), corpus_doc_ids=["docA", "docB"])
        state = NavState(doc_id="", query="q", task_type="niche_fact")
        cfg = NavConfig(
            map_mode=True,
            enable_recursive_dispatch=True,
            max_dispatch_depth=3,
            max_steps=8,
            navigate_max_steps=4,
        )
        seen: dict = {}

        def fake_navigate(ts_arg, *, state, scope, query, config, depth, budget, steps_out=None):
            seen["depth"] = depth
            seen["doc_id"] = state.doc_id
            seen["scope"] = scope
            max_steps = cfg.navigate_max_steps if depth > 0 else cfg.max_steps
            seen["max_steps"] = max_steps
            return RegionReport(scope=scope, depth=depth)

        with mock.patch("nav_navigate.navigate", side_effect=fake_navigate):
            reports = dispatch(
                ts,
                state,
                ["docA"],
                query="q",
                config=cfg,
                depth=0,
                budget=5000,
            )
        self.assertEqual(len(reports), 1)
        self.assertEqual(seen["depth"], 0)
        self.assertEqual(seen["doc_id"], "docA")
        self.assertEqual(seen["scope"], "docA")
        self.assertEqual(seen["max_steps"], cfg.max_steps)

    def test_namespace_to_real_section_starts_at_in_doc_depth_one(self) -> None:
        ts = ToolSpace(HierarchicalTools(_tiny_index()), corpus_doc_ids=["docA", "docB"])
        state = NavState(doc_id="", query="q", task_type="niche_fact")
        cfg = NavConfig(
            map_mode=True,
            enable_recursive_dispatch=True,
            max_dispatch_depth=3,
            max_steps=8,
            navigate_max_steps=4,
        )
        seen: dict = {}

        def fake_navigate(ts_arg, *, state, scope, query, config, depth, budget, steps_out=None):
            seen["depth"] = depth
            seen["doc_id"] = state.doc_id
            seen["scope"] = scope
            seen["max_steps"] = cfg.navigate_max_steps if depth > 0 else cfg.max_steps
            return RegionReport(scope=scope, depth=depth)

        with mock.patch("nav_navigate.navigate", side_effect=fake_navigate):
            reports = dispatch(
                ts,
                state,
                ["docA:L1"],
                query="q",
                config=cfg,
                depth=0,
                budget=5000,
            )
        self.assertEqual(len(reports), 1)
        self.assertEqual(seen["depth"], 1)
        self.assertEqual(seen["doc_id"], "docA")
        self.assertEqual(seen["scope"], "docA:L1")
        self.assertEqual(seen["max_steps"], cfg.navigate_max_steps)

    def test_in_doc_dispatch_increments_depth(self) -> None:
        ts = ToolSpace(HierarchicalTools(_tiny_index()), corpus_doc_ids=["docA", "docB"])
        state = NavState(doc_id="docA", query="q", task_type="niche_fact")
        cfg = NavConfig(map_mode=True, enable_recursive_dispatch=True, max_dispatch_depth=3)
        seen: dict = {}

        def fake_navigate(ts_arg, *, state, scope, query, config, depth, budget, steps_out=None):
            seen["depth"] = depth
            seen["doc_id"] = state.doc_id
            return RegionReport(scope=scope, depth=depth)

        with mock.patch("nav_navigate.navigate", side_effect=fake_navigate):
            dispatch(
                ts,
                state,
                ["docA:L1"],
                query="q",
                config=cfg,
                depth=0,
                budget=5000,
            )
        self.assertEqual(seen["depth"], 1)
        self.assertEqual(seen["doc_id"], "docA")


class GroupRankMergeTests(unittest.TestCase):
    """Side effect B: doc-level group_priority merges into namespace parent."""

    def test_merge_group_priority(self) -> None:
        parent = NavState(doc_id="", query="q", task_type="niche_fact")
        child = _fork_nav_state(parent, doc_id="docA")
        child.group_priority["docA:L1"] = 2.0
        _merge_nav_state(parent, child)
        self.assertEqual(parent.group_priority.get("docA:L1"), 2.0)
        parent.group_priority["docA:L1"] = 5.0
        self.assertEqual(parent.group_priority["docA:L1"], 5.0)


class SortCrossDocTests(unittest.TestCase):
    def test_sort_collected_cross_doc(self) -> None:
        ts = ToolSpace(HierarchicalTools(_tiny_index()), corpus_doc_ids=["docA", "docB"])
        a = Chunk(
            node_id="docB:L2",
            doc_id="docB",
            text="b",
            line_ids=(2,),
            section_id="docB:L2",
        )
        b = Chunk(
            node_id="docA:L2",
            doc_id="docA",
            text="a",
            line_ids=(2,),
            section_id="docA:L2",
        )
        ordered = sort_collected_by_doc_order([(a, 1.0), (b, 1.0)], ts, "")
        self.assertEqual([c.node_id for c, _ in ordered], ["docA:L2", "docB:L2"])


if __name__ == "__main__":
    unittest.main()
