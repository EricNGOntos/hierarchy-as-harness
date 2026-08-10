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

from nav_harvest import harvest  # noqa: E402
from nav_hierarchy import InMemoryHierarchyProvider, InMemoryNode, ProviderToolSpace  # noqa: E402
from nav_plan import Contract, Subgoal  # noqa: E402
from nav_types import ActionKind, NavConfig, NavState  # noqa: E402


def _build_ts() -> ProviderToolSpace:
    nodes = {
        "doc1:ROOT": InMemoryNode(
            section_id="doc1:ROOT", title="Manual", children=["doc1:A"]
        ),
        "doc1:A": InMemoryNode(section_id="doc1:A", title="Section A", children=["doc1:A1", "doc1:A2"]),
        "doc1:A1": InMemoryNode(section_id="doc1:A1", title="A1", content="alpha content"),
        "doc1:A2": InMemoryNode(section_id="doc1:A2", title="A2", content="beta content"),
    }
    provider = InMemoryHierarchyProvider(roots_by_doc={"doc1": ["doc1:ROOT"]}, nodes=nodes)
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
                self.ts, state, config, subgoal=subgoal, entry_scope="doc1:ROOT", query="A"
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
            if scope == "doc1:ROOT":
                dispatch = [a for a in actions if a.kind == ActionKind.DISPATCH and a.section_id == "doc1:A"]
                return [], dispatch, {}, "enter A", {}
            # Inside doc1:A: A1/A2 are leaves (no DISPATCH action exists for them),
            # so the leaf is reached via COLLECT, not a further dispatch hop.
            collect = [a for a in actions if a.kind == ActionKind.COLLECT and a.section_id == "doc1:A1"]
            conf = {collect[0].action_id: 0.7} if collect else {}
            return collect, [], conf, "found it", {}

        with patch("nav_harvest.harvest_policy_call", side_effect=fake_policy):
            result = harvest(
                self.ts, state, config, subgoal=subgoal, entry_scope="doc1:ROOT", query="A"
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

    def test_unselected_visible_nodes_are_dismissed_for_this_subgoal(self) -> None:
        """A1/A2/A (self) are all directly decided here; collecting only A1
        must dismiss the other two (F2/F3 fix)."""
        state = NavState(doc_id="doc1", query="A")
        config = _config(max_harvest_depth=3)
        subgoal = _subgoal()

        def fake_policy(ts, state, config, *, subgoal, query, projection, actions, depth):
            collect = [a for a in actions if a.kind == ActionKind.COLLECT and a.section_id == "doc1:A1"]
            return collect, [], {collect[0].action_id: 0.9}, "A1 matches", {}

        with patch("nav_harvest.harvest_policy_call", side_effect=fake_policy):
            harvest(self.ts, state, config, subgoal=subgoal, entry_scope="doc1:A", query="A")

        self.assertEqual(state.subgoal_dismissed_section_ids.get("s1"), {"doc1:A", "doc1:A2"})

    def test_dispatch_branch_with_zero_yield_is_dismissed(self) -> None:
        """Dispatching into A and collecting nothing inside dismisses A itself."""
        state = NavState(doc_id="doc1", query="A")
        config = _config(max_harvest_depth=3)
        subgoal = _subgoal()

        def fake_policy(ts, state, config, *, subgoal, query, projection, actions, depth):
            if projection.scope == "doc1:ROOT":
                dispatch = [a for a in actions if a.kind == ActionKind.DISPATCH and a.section_id == "doc1:A"]
                return [], dispatch, {}, "look inside A", {}
            return [], [], {}, "nothing here either", {}

        with patch("nav_harvest.harvest_policy_call", side_effect=fake_policy):
            harvest(
                self.ts, state, config, subgoal=subgoal, entry_scope="doc1:ROOT", query="A"
            )

        self.assertIn("doc1:A", state.subgoal_dismissed_section_ids.get("s1", set()))

    def test_harvest_reason_accumulates_across_recursion(self) -> None:
        state = NavState(doc_id="doc1", query="A")
        config = _config(max_harvest_depth=3)
        subgoal = _subgoal()

        def fake_policy(ts, state, config, *, subgoal, query, projection, actions, depth):
            if projection.scope == "doc1:ROOT":
                dispatch = [a for a in actions if a.kind == ActionKind.DISPATCH and a.section_id == "doc1:A"]
                return [], dispatch, {}, "enter A", {}
            collect = [a for a in actions if a.kind == ActionKind.COLLECT and a.section_id == "doc1:A1"]
            return collect, [], {collect[0].action_id: 0.7}, "found A1", {}

        with patch("nav_harvest.harvest_policy_call", side_effect=fake_policy):
            result = harvest(
                self.ts, state, config, subgoal=subgoal, entry_scope="doc1:ROOT", query="A"
            )

        self.assertIn("enter A", result.reason)
        self.assertIn("found A1", result.reason)



if __name__ == "__main__":
    unittest.main()
