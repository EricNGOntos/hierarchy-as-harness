"""Unit tests for the one-shot harvest primitive (src/nav/nav_harvest.py)."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
for source_dir in (ROOT / "src" / "realdata", ROOT / "src" / "nav"):
    if str(source_dir) not in sys.path:
        sys.path.insert(0, str(source_dir))

from nav_harvest import harvest, resolve_harvest_anchor  # noqa: E402
from nav_hierarchy import InMemoryHierarchyProvider, InMemoryNode, ProviderToolSpace  # noqa: E402
from nav_plan import Contract, ScopeFilter, Subgoal  # noqa: E402
from nav_types import ActionKind, NavConfig, NavState  # noqa: E402


def _build_ts() -> ProviderToolSpace:
    nodes = {
        "doc1:__doc_root": InMemoryNode(
            section_id="doc1:__doc_root", title="Manual", children=["doc1:A"]
        ),
        "doc1:A": InMemoryNode(section_id="doc1:A", title="Section A", children=["doc1:A1", "doc1:A2"]),
        "doc1:A1": InMemoryNode(section_id="doc1:A1", title="A1", content="alpha content"),
        "doc1:A2": InMemoryNode(section_id="doc1:A2", title="A2", content="beta content"),
    }
    provider = InMemoryHierarchyProvider(roots_by_doc={"doc1": ["doc1:__doc_root"]}, nodes=nodes)
    return ProviderToolSpace(provider)


def _config(**overrides) -> NavConfig:
    base = dict(map_mode=True, map_char_limit=4000, max_harvest_depth=1)
    base.update(overrides)
    return NavConfig(**base)


def _subgoal(**overrides) -> Subgoal:
    base = dict(id="s1", need="find A", retrieval_query="A", contract=Contract(kind="single_fact"))
    base.update(overrides)
    return Subgoal(**base)


class HarvestRecursionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.ts = _build_ts()

    def test_stops_recursion_when_max_depth_reached(self) -> None:
        """A dispatch chosen at depth==max_harvest_depth must not recurse further."""
        state = NavState(doc_id="doc1", query="A")
        config = _config(max_harvest_depth=0)
        subgoal = _subgoal()

        def fake_policy(ts, state, config, *, subgoal, query, projection, actions, depth):
            dispatch = [a for a in actions if a.kind == ActionKind.DISPATCH and a.section_id == "doc1:A"]
            return [], dispatch, {}, "dispatch deeper", {}

        with patch("nav_harvest.harvest_policy_call", side_effect=fake_policy):
            result = harvest(
                self.ts, state, config, subgoal=subgoal, entry_scope="doc1:__doc_root", query="A"
            )

        self.assertEqual(result.n_policy_calls, 1)
        self.assertTrue(result.max_depth_hit)
        self.assertEqual(result.visited_section_ids, [])
        self.assertEqual(result.new_section_ids, [])

    def test_recurses_across_depths_and_collects_leaf(self) -> None:
        """Dispatch into A (has children), then collect leaf A1 from inside A's scope."""
        state = NavState(doc_id="doc1", query="A")
        config = _config(max_harvest_depth=3)
        subgoal = _subgoal()

        def fake_policy(ts, state, config, *, subgoal, query, projection, actions, depth):
            scope = projection.scope
            if scope == "doc1:__doc_root":
                dispatch = [a for a in actions if a.kind == ActionKind.DISPATCH and a.section_id == "doc1:A"]
                return [], dispatch, {}, "enter A", {}
            # Inside doc1:A: A1/A2 are leaves (no DISPATCH action exists for them),
            # so the leaf is reached via COLLECT, not a further dispatch hop.
            collect = [a for a in actions if a.kind == ActionKind.COLLECT and a.section_id == "doc1:A1"]
            conf = {collect[0].action_id: 0.7} if collect else {}
            return collect, [], conf, "found it", {}

        with patch("nav_harvest.harvest_policy_call", side_effect=fake_policy):
            result = harvest(
                self.ts, state, config, subgoal=subgoal, entry_scope="doc1:__doc_root", query="A"
            )

        self.assertEqual(result.n_policy_calls, 2)
        self.assertFalse(result.max_depth_hit)
        self.assertIn("doc1:A", result.visited_section_ids)
        self.assertIn("doc1:A1", result.new_section_ids)
        self.assertTrue(any("alpha content" in c.text for c, _s in state.collected))

    def test_implicit_finish_on_empty_selection_makes_exactly_one_call(self) -> None:
        state = NavState(doc_id="doc1", query="A")
        config = _config(max_harvest_depth=3)
        subgoal = _subgoal()

        def fake_policy(ts, state, config, *, subgoal, query, projection, actions, depth):
            return [], [], {}, "nothing relevant here", {}

        with patch("nav_harvest.harvest_policy_call", side_effect=fake_policy):
            result = harvest(
                self.ts, state, config, subgoal=subgoal, entry_scope="doc1:A", query="A"
            )

        self.assertEqual(result.n_policy_calls, 1)
        self.assertEqual(result.new_section_ids, [])
        self.assertEqual(result.visited_section_ids, [])
        self.assertFalse(result.max_depth_hit)


class ResolveHarvestAnchorTests(unittest.TestCase):
    def test_disabled_flag_returns_none(self) -> None:
        state = NavState(doc_id="doc1", query="A")
        config = _config(enable_anchor_entry=False)
        subgoal = _subgoal(route_hints=["doc1:A1"])
        self.assertIsNone(resolve_harvest_anchor(subgoal, state, config))

    def test_reharvest_override_wins_over_route_hints(self) -> None:
        state = NavState(doc_id="doc1", query="A")
        state.subgoal_reharvest_anchor["s1"] = "doc1:A2"
        config = _config(enable_anchor_entry=True)
        subgoal = _subgoal(route_hints=["doc1:A1"])
        self.assertEqual(resolve_harvest_anchor(subgoal, state, config), "doc1:A2")

    def test_skips_already_collected_hints(self) -> None:
        state = NavState(doc_id="doc1", query="A")
        state.collected_section_ids.add("doc1:A1")
        config = _config(enable_anchor_entry=True)
        subgoal = _subgoal(route_hints=["doc1:A1", "doc1:A2"])
        self.assertEqual(resolve_harvest_anchor(subgoal, state, config), "doc1:A2")

    def test_skips_hints_outside_declared_doc_scope(self) -> None:
        state = NavState(doc_id="doc1", query="A")
        config = _config(enable_anchor_entry=True)
        subgoal = _subgoal(
            route_hints=["doc2:B1", "doc1:A1"],
            scope_filter=ScopeFilter(doc_ids=["doc1"]),
        )
        self.assertEqual(resolve_harvest_anchor(subgoal, state, config), "doc1:A1")

    def test_no_usable_hint_returns_none(self) -> None:
        state = NavState(doc_id="doc1", query="A")
        config = _config(enable_anchor_entry=True)
        subgoal = _subgoal(route_hints=[])
        self.assertIsNone(resolve_harvest_anchor(subgoal, state, config))


if __name__ == "__main__":
    unittest.main()
