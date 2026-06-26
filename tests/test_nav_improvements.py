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
from nav_actions import build_legal_actions  # noqa: E402
from nav_agent import _collect_subtree, _update_collect_coverage  # noqa: E402
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
    def __init__(self, scores: dict[str, float]) -> None:
        self.scores = scores

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
    ) -> None:
        self._chunks = chunks
        self._idx = _FakeIndex(scores)
        self._ancestors = ancestors or set()
        self._descendants = descendants or {"doc:L1"}

    def _materialize_leaf_path_chunks(self, section_id, doc_id):
        del section_id, doc_id
        return list(self._chunks)

    def section_relation_ids(self, section_id, doc_id):
        del section_id, doc_id
        return set(self._ancestors), set(self._descendants)


def _projection(*views: SectionView) -> Projection:
    return Projection(doc_id="doc", scope=None, text="", visible_sections=list(views))


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
            scored = _collect_subtree(tools, self.action, self.state, NavConfig(collect_k=2))

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
            scored = _collect_subtree(tools, self.action, self.state, NavConfig(collect_k=8))

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
            scored = _collect_subtree(tools, self.action, self.state, NavConfig(collect_k=8))

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
            scored = _collect_subtree(tools, self.action, self.state, NavConfig(collect_k=2))

        self.assertEqual([chunk.node_id for chunk, _ in scored], ["doc:L30__path", "doc:L20__path"])

    def test_scope_collect_can_restore_line_order_ablation(self) -> None:
        tools = _FakeToolSpace(
            self.chunks,
            {"doc:L30__path": 1.0, "doc:L10__path": 0.1, "doc:L20__path": 0.5},
        )
        with patch.dict(os.environ, {"NAV_SCOPE_COLLECT_STRATEGY": "line_order"}):
            scored = _collect_subtree(tools, self.action, self.state, NavConfig(collect_k=2))

        self.assertEqual([chunk.node_id for chunk, _ in scored], ["doc:L10__path", "doc:L20__path"])

    def test_non_scope_collect_keeps_index_order(self) -> None:
        tools = _FakeToolSpace(
            self.chunks,
            {"doc:L30__path": 1.0, "doc:L10__path": 0.1, "doc:L20__path": 0.5},
        )
        state = NavState(doc_id="doc", query="query", task_type="niche_fact")
        scored = _collect_subtree(tools, self.action, state, NavConfig(collect_k=2))
        self.assertEqual([chunk.node_id for chunk, _ in scored], ["doc:L30__path", "doc:L20__path"])

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
        self.assertEqual(self.state.collected_section_ids, {"doc:L1"})
        self.assertEqual(self.state.covered_section_ids, {"doc:L1", "doc:L2"})
        self.assertEqual(self.state.blocked_collect_section_ids, {"doc:L0"})
        self.assertTrue(self.state.scope_evidence_locked)

    def test_partial_collect_blocks_ancestor_without_covering_descendants(self) -> None:
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
        self.assertFalse(self.state.covered_section_ids)
        self.assertEqual(self.state.blocked_collect_section_ids, {"doc:L0"})

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
            initial = _collect_subtree(tools, self.action, self.state, NavConfig(collect_k=2))
            self.state.scope_evidence_locked = True
            later = _collect_subtree(tools, self.action, self.state, NavConfig(collect_k=2))

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
        self.config = NavConfig(collect_top_k=4, expand_top_k=4)

    def test_empty_search_is_blocked_per_scope(self) -> None:
        state = NavState(doc_id="doc", query="query")
        state.exhausted_search_scopes.add(None)
        projection = _projection(_view("doc:L1"))
        with patch.dict(os.environ, {"NAV_BLOCK_EXHAUSTED_SEARCH": "1"}):
            root_actions = build_legal_actions(state, projection, step_idx=1, config=self.config)
            state.push_scope("doc:L1")
            child_actions = build_legal_actions(state, projection, step_idx=2, config=self.config)
            state.exhausted_search_scopes.add("doc:L1")
            exhausted_child_actions = build_legal_actions(state, projection, step_idx=3, config=self.config)

        self.assertNotIn(ActionKind.SEARCH, [action.kind for action in root_actions])
        self.assertIn(ActionKind.SEARCH, [action.kind for action in child_actions])
        self.assertNotIn(ActionKind.SEARCH, [action.kind for action in exhausted_child_actions])

    def test_scope_discovery_bridge_adds_expand_without_collect(self) -> None:
        state = NavState(doc_id="doc", query="query", task_type="scope_collection")
        state.discovery_bridge_sections = [
            {
                "section_id": "doc:L9",
                "label": "relevant parent",
                "discovery_score": 4.0,
                "source_section_id": "doc:L10",
            }
        ]
        with patch.dict(os.environ, {"NAV_DISCOVERY_SCOPE_BRIDGE": "1"}):
            actions = build_legal_actions(
                state, _projection(_view("doc:L1")), step_idx=1, config=self.config
            )

        bridge = [action for action in actions if action.action_id == "G1"]
        self.assertEqual(len(bridge), 1)
        self.assertEqual(bridge[0].kind, ActionKind.EXPAND)
        self.assertEqual(bridge[0].section_id, "doc:L9")
        self.assertFalse(
            any(
                action.kind == ActionKind.COLLECT and action.section_id == "doc:L9"
                for action in actions
            )
        )

    def test_scope_discovery_bridge_respects_covered_and_task_type(self) -> None:
        bridge = [{"section_id": "doc:L9", "label": "parent", "discovery_score": 4.0}]
        covered = NavState(doc_id="doc", query="query", task_type="scope_collection")
        covered.discovery_bridge_sections = bridge
        covered.covered_section_ids.add("doc:L9")
        niche = NavState(doc_id="doc", query="query", task_type="niche_fact")
        niche.discovery_bridge_sections = bridge
        with patch.dict(
            os.environ,
            {"NAV_DISCOVERY_SCOPE_BRIDGE": "1", "NAV_FILTER_COLLECTED_SECTIONS": "1"},
        ):
            covered_actions = build_legal_actions(
                covered, _projection(_view("doc:L1")), step_idx=1, config=self.config
            )
            niche_actions = build_legal_actions(
                niche, _projection(_view("doc:L1")), step_idx=1, config=self.config
            )

        self.assertFalse(any(action.action_id.startswith("G") for action in covered_actions))
        self.assertFalse(any(action.action_id.startswith("G") for action in niche_actions))

    def test_search_block_can_be_disabled(self) -> None:
        state = NavState(doc_id="doc", query="query", exhausted_search_scopes={None})
        with patch.dict(os.environ, {"NAV_BLOCK_EXHAUSTED_SEARCH": "0"}):
            actions = build_legal_actions(
                state, _projection(_view("doc:L1")), step_idx=1, config=self.config
            )
            agent_state = _format_agent_state(state, 1, self.config)
        self.assertIn(ActionKind.SEARCH, [action.kind for action in actions])
        self.assertNotIn("Search status: exhausted", agent_state)

    def test_successful_partial_collect_blocks_repeat_but_allows_expand(self) -> None:
        state = NavState(doc_id="doc", query="query")
        state.action_history.append({"kind": "collect", "section_id": "doc:L1", "n_added": 2})
        projection = _projection(_view("doc:L1"), _view("doc:L2"))
        with patch.dict(os.environ, {"NAV_FILTER_COLLECTED_SECTIONS": "1"}):
            actions = build_legal_actions(state, projection, step_idx=1, config=self.config)

        navigable = {
            (action.kind, action.section_id)
            for action in actions
            if action.kind in {ActionKind.COLLECT, ActionKind.EXPAND}
        }
        self.assertNotIn((ActionKind.COLLECT, "doc:L1"), navigable)
        self.assertIn((ActionKind.EXPAND, "doc:L1"), navigable)
        self.assertIn((ActionKind.COLLECT, "doc:L2"), navigable)

    def test_successful_collect_filters_discovery_section(self) -> None:
        state = NavState(doc_id="doc", query="query")
        state.discovery_scores = {"doc:L9": 2.0}
        state.action_history.append({"kind": "collect", "section_id": "doc:L9", "n_added": 2})
        actions = build_legal_actions(
            state, _projection(_view("doc:L1")), step_idx=1, config=self.config
        )
        self.assertNotIn(
            "doc:L9",
            [action.section_id for action in actions if action.action_id.startswith("D")],
        )

    def test_zero_add_collect_is_not_covered(self) -> None:
        state = NavState(doc_id="doc", query="query")
        state.action_history.append({"kind": "collect", "section_id": "doc:L1", "n_added": 0})
        with patch.dict(os.environ, {"NAV_FILTER_COLLECTED_SECTIONS": "1"}):
            actions = build_legal_actions(
                state, _projection(_view("doc:L1")), step_idx=1, config=self.config
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
                state, _projection(_view("doc:L1")), step_idx=1, config=self.config
            )
        self.assertNotIn(
            (ActionKind.COLLECT, "doc:L1"),
            {(action.kind, action.section_id) for action in actions},
        )
        self.assertIn(ActionKind.FINISH, [action.kind for action in actions])

    def test_ancestor_collect_is_blocked_but_expand_remains_available(self) -> None:
        state = NavState(doc_id="doc", query="query")
        state.blocked_collect_section_ids.add("doc:L1")
        with patch.dict(os.environ, {"NAV_FILTER_COLLECTED_SECTIONS": "1"}):
            actions = build_legal_actions(
                state, _projection(_view("doc:L1")), step_idx=1, config=self.config
            )
        pairs = {(action.kind, action.section_id) for action in actions}
        self.assertNotIn((ActionKind.COLLECT, "doc:L1"), pairs)
        self.assertIn((ActionKind.EXPAND, "doc:L1"), pairs)

    def test_covered_descendant_blocks_collect_and_expand(self) -> None:
        state = NavState(doc_id="doc", query="query")
        state.covered_section_ids.add("doc:L1")
        with patch.dict(os.environ, {"NAV_FILTER_COLLECTED_SECTIONS": "1"}):
            actions = build_legal_actions(
                state, _projection(_view("doc:L1")), step_idx=1, config=self.config
            )
        pairs = {(action.kind, action.section_id) for action in actions}
        self.assertNotIn((ActionKind.COLLECT, "doc:L1"), pairs)
        self.assertNotIn((ActionKind.EXPAND, "doc:L1"), pairs)

    def test_collect_filter_can_be_disabled(self) -> None:
        state = NavState(doc_id="doc", query="query")
        state.action_history.append({"kind": "collect", "section_id": "doc:L1", "n_added": 1})
        projection = _projection(_view("doc:L1"), _view("doc:L2"))
        with patch.dict(os.environ, {"NAV_FILTER_COLLECTED_SECTIONS": "0"}):
            actions = build_legal_actions(state, projection, step_idx=1, config=self.config)
        self.assertIn(
            (ActionKind.COLLECT, "doc:L1"),
            {(action.kind, action.section_id) for action in actions},
        )


if __name__ == "__main__":
    unittest.main()
