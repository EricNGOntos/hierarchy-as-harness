from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
for source_dir in (ROOT / "src" / "realdata", ROOT / "src" / "nav"):
    if str(source_dir) not in sys.path:
        sys.path.insert(0, str(source_dir))

from agent_delivery.code.index_retrieval import Chunk  # noqa: E402
from agent_delivery.code.compose_llm import _multi_hop_anchor_guidance  # noqa: E402
from agent_delivery.code.load_data import DocBundle, LineRecord  # noqa: E402
from nav_actions import build_legal_actions  # noqa: E402
from nav_agent import (  # noqa: E402
    _collect_subtree,
    _scope_collect_outline,
    _scope_collect_scored,
    _update_collect_coverage,
)
from nav_policy import _format_agent_state  # noqa: E402
from nav_types import (  # noqa: E402
    ActionKind,
    LegalAction,
    NavConfig,
    NavState,
    Projection,
    SectionView,
)


class _FakeIndex:
    def __init__(self, scores: dict[str, float], bundles: dict[str, DocBundle] | None = None) -> None:
        self.scores = scores
        self._bundles = bundles or {}

    def search(self, query, pool, k, doc_id_filter=None):
        del query, doc_id_filter
        ranked = sorted(pool, key=lambda chunk: -self.scores[chunk.node_id])
        return [(chunk, self.scores[chunk.node_id]) for chunk in ranked[:k]]


class _FakeToolSpace:
    def __init__(
        self,
        chunks: list[Chunk],
        scores: dict[str, float],
        *,
        ancestors: set[str] | None = None,
        descendants: set[str] | None = None,
        bundles: dict[str, DocBundle] | None = None,
    ) -> None:
        self._chunks = chunks
        self._idx = _FakeIndex(scores, bundles)
        self._ancestors = ancestors or set()
        self._descendants = descendants or {"doc:L1"}

    def _materialize_leaf_path_chunks(self, section_id, doc_id):
        del section_id, doc_id
        return list(self._chunks)

    def section_relation_ids(self, section_id, doc_id):
        del section_id, doc_id
        return set(self._ancestors), set(self._descendants)


def _projection(*views: SectionView) -> Projection:
    rows = list(views)
    return Projection(
        doc_id="doc",
        scope=None,
        text="",
        visible_sections=rows,
        tree_sections=rows,
        map_mode=True,
    )


def _view(section_id: str, *, has_children: bool = True) -> SectionView:
    return SectionView(
        section_id=section_id,
        level=1,
        preview=section_id,
        score=1.0,
        n_lines=1,
        n_chunks=1,
        has_children=has_children,
    )


class ScopeCollectTests(unittest.TestCase):
    def setUp(self) -> None:
        self.chunks = [
            Chunk("doc:L30__path", "doc", "third", (30,), "doc:L1"),
            Chunk("doc:L10__path", "doc", "first", (10,), "doc:L1"),
            Chunk("doc:L20__path", "doc", "second", (20,), "doc:L1"),
        ]
        self.action = LegalAction(
            action_id="C1",
            kind=ActionKind.COLLECT,
            section_id="doc:L1",
            score=2.0,
        )
        self.state = NavState(doc_id="doc", query="query", task_type="scope_collection")

    def test_small_scope_collect_preserves_line_order(self) -> None:
        tools = _FakeToolSpace(
            self.chunks,
            {"doc:L30__path": 0.2, "doc:L10__path": 0.8, "doc:L20__path": 0.8},
        )
        with patch.dict(os.environ, {"NAV_SCOPE_COLLECT_STRATEGY": "local_band"}):
            scored = _scope_collect_scored(
                tools._idx, self.chunks, self.action, self.state, NavConfig(collect_k=2)
            )

        self.assertEqual([chunk.node_id for chunk, _ in scored], ["doc:L10__path", "doc:L20__path"])

    def test_large_scope_collect_uses_contiguous_local_band(self) -> None:
        chunks = [
            Chunk(f"doc:L{i}__path", "doc", str(i), (i,), "doc:L1")
            for i in range(1, 26)
        ]
        scores = {chunk.node_id: 0.1 for chunk in chunks}
        scores["doc:L15__path"] = 0.9
        tools = _FakeToolSpace(chunks, scores)
        with patch.dict(
            os.environ,
            {
                "NAV_SCOPE_COLLECT_STRATEGY": "local_band",
                "NAV_SCOPE_LOCAL_BAND_MIN_POOL": "20",
                "NAV_SCOPE_LOCAL_BAND_K": "4",
                "NAV_SCOPE_LOCAL_BAND_CONTEXT_BEFORE": "1",
            },
        ):
            scored = _scope_collect_scored(
                tools._idx, chunks, self.action, self.state, NavConfig(collect_k=8)
            )

        self.assertEqual(
            [chunk.node_id for chunk, _ in scored],
            ["doc:L14__path", "doc:L15__path", "doc:L16__path", "doc:L17__path"],
        )

    def test_large_scope_collect_can_use_multiple_local_bands(self) -> None:
        chunks = [
            Chunk(f"doc:L{i}__path", "doc", str(i), (i,), "doc:L1")
            for i in range(1, 26)
        ]
        scores = {chunk.node_id: 0.1 for chunk in chunks}
        scores.update(
            {
                "doc:L5__path": 0.9,
                "doc:L15__path": 0.8,
                "doc:L23__path": 0.7,
            }
        )
        tools = _FakeToolSpace(chunks, scores)
        with patch.dict(
            os.environ,
            {
                "NAV_SCOPE_COLLECT_STRATEGY": "multi_band",
                "NAV_SCOPE_LOCAL_BAND_MIN_POOL": "20",
                "NAV_SCOPE_LOCAL_BAND_K": "6",
                "NAV_SCOPE_LOCAL_BAND_CONTEXT_BEFORE": "0",
                "NAV_SCOPE_MULTI_BAND_CONTEXT_AFTER": "1",
                "NAV_SCOPE_MULTI_BAND_ANCHORS": "3",
            },
        ):
            scored = _scope_collect_scored(
                tools._idx, chunks, self.action, self.state, NavConfig(collect_k=8)
            )

        self.assertEqual(
            {chunk.node_id for chunk, _ in scored},
            {
                "doc:L5__path",
                "doc:L6__path",
                "doc:L15__path",
                "doc:L16__path",
                "doc:L23__path",
                "doc:L24__path",
            },
        )

    def test_relevance_strategy_remains_available_for_ablation(self) -> None:
        tools = _FakeToolSpace(
            self.chunks,
            {"doc:L30__path": 1.0, "doc:L10__path": 0.1, "doc:L20__path": 0.5},
        )
        with patch.dict(os.environ, {"NAV_SCOPE_COLLECT_STRATEGY": "relevance"}):
            scored = _scope_collect_scored(
                tools._idx, self.chunks, self.action, self.state, NavConfig(collect_k=2)
            )

        self.assertEqual([chunk.node_id for chunk, _ in scored], ["doc:L30__path", "doc:L20__path"])

    def test_scope_collect_can_restore_line_order_ablation(self) -> None:
        tools = _FakeToolSpace(
            self.chunks,
            {"doc:L30__path": 1.0, "doc:L10__path": 0.1, "doc:L20__path": 0.5},
        )
        with patch.dict(os.environ, {"NAV_SCOPE_COLLECT_STRATEGY": "line_order"}):
            scored = _scope_collect_scored(
                tools._idx, self.chunks, self.action, self.state, NavConfig(collect_k=2)
            )

        self.assertEqual([chunk.node_id for chunk, _ in scored], ["doc:L10__path", "doc:L20__path"])

    def test_active_collect_is_task_type_agnostic_doc_order(self) -> None:
        """Map-mode COLLECT ignores task_type / scope strategies; full doc-order hydrate."""
        tools = _FakeToolSpace(
            self.chunks,
            {"doc:L30__path": 1.0, "doc:L10__path": 0.1, "doc:L20__path": 0.5},
        )
        state = NavState(
            doc_id="doc",
            query="列举该部分的主要条目。",
            task_type="scope_collection",
            unit_scores={"doc:L30": 1.0, "doc:L10": 0.1, "doc:L20": 0.5},
        )
        with patch.dict(os.environ, {"NAV_MAP_MODE": "1", "NAV_SCOPE_COLLECT_STRATEGY": "relevance"}):
            scored = _collect_subtree(
                tools, self.action, state, NavConfig(collect_k=2, map_mode=True)
            )
        self.assertEqual(
            [chunk.node_id for chunk, _ in scored],
            ["doc:L10__path", "doc:L20__path", "doc:L30__path"],
        )

    def test_non_scope_collect_keeps_index_order(self) -> None:
        tools = _FakeToolSpace(
            self.chunks,
            {"doc:L30__path": 1.0, "doc:L10__path": 0.1, "doc:L20__path": 0.5},
        )
        state = NavState(doc_id="doc", query="query", task_type="niche_fact")
        scored = _collect_subtree(tools, self.action, state, NavConfig(collect_k=2))
        self.assertEqual([chunk.node_id for chunk, _ in scored], ["doc:L30__path", "doc:L20__path"])

    def test_outline_collect_builds_chunks_from_bundle_lines(self) -> None:
        lines = [
            LineRecord("doc", 1, "Root section", 1),
            LineRecord("doc", 2, "Child A", 2),
            LineRecord("doc", 3, "A detail", 3),
            LineRecord("doc", 4, "Child B", 2),
            LineRecord("doc", 5, "B detail", 3),
            LineRecord("doc", 6, "Child C", 2),
            LineRecord("doc", 7, "C detail", 3),
        ]
        bundle = DocBundle("doc", lines, [1, 2, 3, 2, 3, 2, 3])
        # Deliberately provide leaf/path chunks that do not map by child line_id.
        path_chunks = [
            Chunk("doc:L3__path", "doc", "old path A", (1, 2, 3), "doc:L1"),
            Chunk("doc:L5__path", "doc", "old path B", (1, 4, 5), "doc:L1"),
        ]
        tools = _FakeToolSpace(
            path_chunks,
            {chunk.node_id: 0.1 for chunk in path_chunks},
            bundles={"doc": bundle},
        )
        state = NavState(
            doc_id="doc",
            query="列举该部分的主要条目。",
            task_type="scope_collection",
        )

        # Keyword OUTLINE is retired from the active COLLECT path: even with the
        # legacy env flag, _collect_subtree hydrates the materialized branch.
        with patch.dict(
            os.environ,
            {
                "NAV_SCOPE_OUTLINE_MODE": "1",
                "NAV_SCOPE_OUTLINE_LINES_PER_CHILD": "2",
                "NAV_SCOPE_OUTLINE_MIN_CHUNKS": "4",
                "NAV_MAP_MODE": "1",
            },
        ):
            state.unit_scores = {chunk.node_id: 0.1 for chunk in path_chunks}
            scored = _collect_subtree(tools, self.action, state, NavConfig(collect_k=10, map_mode=True))

        self.assertEqual(
            [chunk.node_id for chunk, _ in scored],
            ["doc:L3__path", "doc:L5__path"],
        )
        self.assertNotIn("__outline", "\n".join(chunk.node_id for chunk, _ in scored))

        # Legacy helper still available for ablation/manual calls.
        outline = _scope_collect_outline(
            tools._idx, path_chunks, self.action, state, NavConfig(collect_k=10)
        )
        self.assertEqual(
            [chunk.node_id for chunk, _ in outline],
            ["doc:L1__outline", "doc:L2__outline", "doc:L4__outline", "doc:L6__outline"],
        )

    def test_successful_collect_blocks_ancestors_and_marks_full_subtree(self) -> None:
        tools = _FakeToolSpace(
            self.chunks,
            {chunk.node_id: 1.0 for chunk in self.chunks},
            ancestors={"doc:L0"},
            descendants={"doc:L1", "doc:L2"},
        )
        self.state.collected_ids.update(chunk.node_id for chunk in self.chunks)
        with patch.dict(os.environ, {"NAV_FILTER_COLLECTED_SECTIONS": "1"}):
            meta = _update_collect_coverage(tools, self.action, self.state, added=3)

        self.assertTrue(meta["collect_full"])
        self.assertTrue(meta["branch_selected"])
        # collected = sid ∪ descendants (merged covered semantics)
        self.assertEqual(self.state.collected_section_ids, {"doc:L1", "doc:L2"})
        self.assertEqual(self.state.blocked_collect_section_ids, {"doc:L0"})
        self.assertFalse(self.state.scope_evidence_locked)

    def test_partial_collect_still_selects_whole_branch(self) -> None:
        """added>0 selects the branch even when hydrate is not full."""
        tools = _FakeToolSpace(
            self.chunks,
            {chunk.node_id: 1.0 for chunk in self.chunks},
            ancestors={"doc:L0"},
            descendants={"doc:L1", "doc:L2"},
        )
        self.state.collected_ids.add(self.chunks[0].node_id)
        with patch.dict(os.environ, {"NAV_FILTER_COLLECTED_SECTIONS": "1"}):
            meta = _update_collect_coverage(tools, self.action, self.state, added=1)

        self.assertFalse(meta["collect_full"])
        self.assertTrue(meta["branch_selected"])
        self.assertEqual(self.state.collected_section_ids, {"doc:L1", "doc:L2"})
        self.assertEqual(self.state.blocked_collect_section_ids, {"doc:L0"})
        self.assertFalse(self.state.scope_evidence_locked)

    def test_single_leaf_collect_keeps_parent_collect_available(self) -> None:
        leaf = [Chunk("doc:L2__path", "doc", "leaf", (2,), "doc:L2")]
        tools = _FakeToolSpace(
            leaf,
            {"doc:L2__path": 1.0},
            ancestors={"doc:L1"},
            descendants={"doc:L2"},
        )
        state = NavState(doc_id="doc", query="query", task_type="scope_collection")
        state.collected_ids.add("doc:L2__path")
        action = LegalAction(
            action_id="C1",
            kind=ActionKind.COLLECT,
            section_id="doc:L2",
        )
        with patch.dict(os.environ, {"NAV_FILTER_COLLECTED_SECTIONS": "1"}):
            meta = _update_collect_coverage(tools, action, state, added=1)

        self.assertTrue(meta["collect_full"])
        self.assertFalse(state.blocked_collect_section_ids)
        self.assertFalse(state.scope_evidence_locked)

    def test_scope_evidence_lock_penalizes_later_collect_scores(self) -> None:
        tools = _FakeToolSpace(
            self.chunks,
            {"doc:L30__path": 0.2, "doc:L10__path": 0.8, "doc:L20__path": 0.8},
        )
        with patch.dict(
            os.environ,
            {
                "NAV_SCOPE_COLLECT_STRATEGY": "line_order",
                "NAV_SCOPE_ACTION_SCORE_CAP": "1.0",
                "NAV_SCOPE_POST_LOCK_SCORE_PENALTY": "2.0",
            },
        ):
            initial = _scope_collect_scored(
                tools._idx, self.chunks, self.action, self.state, NavConfig(collect_k=2)
            )
            self.state.scope_evidence_locked = True
            later = _scope_collect_scored(
                tools._idx, self.chunks, self.action, self.state, NavConfig(collect_k=2)
            )

        self.assertAlmostEqual(initial[0][1] - later[0][1], 2.0)


class MultiHopComposeTests(unittest.TestCase):
    def test_guidance_binds_fact_fields_to_query_order(self) -> None:
        query = '请分别回答“5.2.7 注浆”与“5.2.8 封孔”两处。'
        with patch.dict(os.environ, {"MULTIHOP_COMPOSE_HOP_ALIGNMENT": "1"}):
            guidance = _multi_hop_anchor_guidance(query)

        self.assertIn('fact_1 must answer the first location: "5.2.7 注浆"', guidance)
        self.assertIn('fact_2 must answer the second location: "5.2.8 封孔"', guidance)
        self.assertIn("Do not replace either fact with a nearby section", guidance)

    def test_guidance_can_be_disabled(self) -> None:
        with patch.dict(os.environ, {"MULTIHOP_COMPOSE_HOP_ALIGNMENT": "0"}):
            self.assertEqual(_multi_hop_anchor_guidance("query"), "")

    def test_guidance_is_disabled_by_default(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(_multi_hop_anchor_guidance("query"), "")


class LegalActionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.config = NavConfig(collect_top_k=4, map_mode=True)

    def test_search_action_fully_removed(self) -> None:
        state = NavState(doc_id="doc", query="query")
        projection = _projection(_view("doc:L1"))
        root_actions = build_legal_actions(state, projection, step_idx=6, config=self.config)
        map_cfg = NavConfig(map_mode=True, collect_top_k=4)
        with patch.dict(os.environ, {"NAV_MAP_MODE": "1"}):
            map_actions = build_legal_actions(state, projection, step_idx=6, config=map_cfg)
        for actions in (root_actions, map_actions):
            kinds = {action.kind for action in actions}
            self.assertTrue(kinds <= {ActionKind.COLLECT, ActionKind.DISPATCH, ActionKind.FINISH})
        agent_state = _format_agent_state(state, 1, self.config)
        self.assertNotIn("Search status", agent_state)

    def test_no_discovery_bridge_or_g_actions(self) -> None:
        state = NavState(doc_id="doc", query="query", task_type="scope_collection")
        setattr(
            state,
            "discovery_bridge_sections",
            [{"section_id": "doc:L9", "label": "parent", "discovery_score": 4.0}],
        )
        setattr(state, "discovery_scores", {"doc:L9": 4.0})
        with patch.dict(os.environ, {"NAV_DISCOVERY_SCOPE_BRIDGE": "1"}):
            actions = build_legal_actions(
                state, _projection(_view("doc:L1")), step_idx=6, config=self.config
            )
        self.assertFalse(any(action.action_id.startswith("G") for action in actions))
        # D* is DISPATCH (legal), not discovery.
        self.assertTrue(any(a.kind == ActionKind.DISPATCH for a in actions))

    def test_successful_partial_collect_blocks_repeat(self) -> None:
        state = NavState(doc_id="doc", query="query")
        state.action_history.append({"kind": "collect", "section_id": "doc:L1", "n_added": 2})
        projection = _projection(_view("doc:L1"), _view("doc:L2"))
        with patch.dict(os.environ, {"NAV_FILTER_COLLECTED_SECTIONS": "1"}):
            actions = build_legal_actions(state, projection, step_idx=6, config=self.config)

        collectable = {
            (action.kind, action.section_id)
            for action in actions
            if action.kind == ActionKind.COLLECT
        }
        self.assertNotIn((ActionKind.COLLECT, "doc:L1"), collectable)
        self.assertIn((ActionKind.COLLECT, "doc:L2"), collectable)

    def test_successful_collect_does_not_emit_discovery_g_actions(self) -> None:
        state = NavState(doc_id="doc", query="query")
        setattr(state, "discovery_scores", {"doc:L9": 2.0})
        state.action_history.append({"kind": "collect", "section_id": "doc:L9", "n_added": 2})
        actions = build_legal_actions(
            state, _projection(_view("doc:L1")), step_idx=6, config=self.config
        )
        self.assertFalse(any(action.action_id.startswith("G") for action in actions))

    def test_zero_add_collect_is_not_marked(self) -> None:
        state = NavState(doc_id="doc", query="query")
        state.action_history.append({"kind": "collect", "section_id": "doc:L1", "n_added": 0})
        with patch.dict(os.environ, {"NAV_FILTER_COLLECTED_SECTIONS": "1"}):
            actions = build_legal_actions(
                state, _projection(_view("doc:L1")), step_idx=6, config=self.config
            )
        self.assertIn(
            (ActionKind.COLLECT, "doc:L1"),
            {(action.kind, action.section_id) for action in actions},
        )

    def test_filter_does_not_restore_collected_candidate(self) -> None:
        state = NavState(doc_id="doc", query="query")
        state.collected_section_ids.add("doc:L1")
        with patch.dict(os.environ, {"NAV_FILTER_COLLECTED_SECTIONS": "1"}):
            actions = build_legal_actions(
                state, _projection(_view("doc:L1")), step_idx=6, config=self.config
            )
        self.assertNotIn(
            (ActionKind.COLLECT, "doc:L1"),
            {(action.kind, action.section_id) for action in actions},
        )
        self.assertIn(ActionKind.FINISH, [action.kind for action in actions])

    def test_ancestor_collect_is_blocked_dispatch_remains(self) -> None:
        state = NavState(doc_id="doc", query="query")
        state.blocked_collect_section_ids.add("doc:L1")
        with patch.dict(os.environ, {"NAV_FILTER_COLLECTED_SECTIONS": "1"}):
            actions = build_legal_actions(
                state, _projection(_view("doc:L1")), step_idx=6, config=self.config
            )
        pairs = {(action.kind, action.section_id) for action in actions}
        self.assertNotIn((ActionKind.COLLECT, "doc:L1"), pairs)
        self.assertIn((ActionKind.DISPATCH, "doc:L1"), pairs)

    def test_collected_descendant_blocks_collect_and_dispatch(self) -> None:
        state = NavState(doc_id="doc", query="query")
        state.collected_section_ids.add("doc:L1")
        with patch.dict(os.environ, {"NAV_FILTER_COLLECTED_SECTIONS": "1"}):
            actions = build_legal_actions(
                state, _projection(_view("doc:L1")), step_idx=6, config=self.config
            )
        pairs = {(action.kind, action.section_id) for action in actions}
        self.assertNotIn((ActionKind.COLLECT, "doc:L1"), pairs)
        self.assertNotIn((ActionKind.DISPATCH, "doc:L1"), pairs)

    def test_collect_filter_can_be_disabled(self) -> None:
        state = NavState(doc_id="doc", query="query")
        state.action_history.append({"kind": "collect", "section_id": "doc:L1", "n_added": 1})
        projection = _projection(_view("doc:L1"), _view("doc:L2"))
        with patch.dict(os.environ, {"NAV_FILTER_COLLECTED_SECTIONS": "0"}):
            actions = build_legal_actions(state, projection, step_idx=6, config=self.config)
        self.assertIn(
            (ActionKind.COLLECT, "doc:L1"),
            {(action.kind, action.section_id) for action in actions},
        )


if __name__ == "__main__":
    unittest.main()
