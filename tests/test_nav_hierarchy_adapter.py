"""Port-seam acceptance test (b6): hierarchy + summary alone drives the kernel.

Builds a pure in-memory ``HierarchyProvider`` (no ToolSpace, no BM25/dense
index, no ``_idx``) and drives ``harvest()`` -> ``plan_control()`` ->
``pack_nav_evidence()`` against it through ``ProviderToolSpace``. The
only two LLM call sites (``harvest_policy_call`` / ``plan_control``'s chat
completion) are mocked deterministically; everything else is real code.
This is the acceptance check for the knowhere-main portability claim: no
other file under ``src/nav`` needed to change to run against a provider that
implements only ``HierarchyProvider``'s 5 methods.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
for source_dir in (ROOT / "src" / "realdata", ROOT / "src" / "nav"):
    if str(source_dir) not in sys.path:
        sys.path.insert(0, str(source_dir))

from nav_control import plan_control  # noqa: E402
from nav_compose import pack_nav_evidence  # noqa: E402
from nav_harvest import harvest  # noqa: E402
from nav_hierarchy import InMemoryHierarchyProvider, InMemoryNode, ProviderToolSpace  # noqa: E402
from nav_plan import Contract, RetrievalPlan, Subgoal  # noqa: E402
from nav_types import NavConfig, NavState  # noqa: E402
from nav_verify import build_subgoal_result  # noqa: E402


def _build_ts() -> ProviderToolSpace:
    nodes = {
        "doc1:ROOT": InMemoryNode(
            section_id="doc1:ROOT", title="Manual", children=["doc1:L1", "doc1:L5"]
        ),
        "doc1:L1": InMemoryNode(
            section_id="doc1:L1", title="Intro", content="This manual covers seal types."
        ),
        "doc1:L5": InMemoryNode(
            section_id="doc1:L5",
            title="Seal Specification",
            content="The primary seal type is a mechanical face seal rated to 200C.",
        ),
    }
    provider = InMemoryHierarchyProvider(
        roots_by_doc={"doc1": ["doc1:ROOT"]},
        nodes=nodes,
        summaries={"doc1:L5": "Details the mechanical face seal rating."},
    )
    return ProviderToolSpace(provider)


class HierarchyAdapterPortSeamTests(unittest.TestCase):
    def setUp(self) -> None:
        self.ts = _build_ts()
        self.config = NavConfig(
            mode="checklist",
            map_mode=True,
            map_char_limit=4000,
            max_harvest_depth=2,
        )
        self.subgoal = Subgoal(
            id="s1",
            need="What is the primary seal type and its rating?",
            retrieval_query="primary seal type rating",
            contract=Contract(kind="single_fact"),
        )
        self.plan = RetrievalPlan(subgoals=[self.subgoal])
        self.state = NavState(doc_id="doc1", query=self.subgoal.retrieval_query, retrieval_plan=self.plan)

    def test_adapter_exposes_only_documented_surface(self) -> None:
        for name in (
            "sections_for_doc",
            "get_structure",
            "_children_for_section_path",
            "section_relation_ids",
            "_materialize_leaf_path_chunks",
            "materialize_self_only_chunks",
            "path_titles",
            "read_chunks",
        ):
            self.assertTrue(callable(getattr(self.ts, name)))
        self.assertIsNone(getattr(self.ts, "_idx", None))

    def test_optional_capabilities_degrade_when_provider_lacks_them(self) -> None:
        # InMemoryHierarchyProvider implements only the required 5, so the
        # chunk-granularity and path-channel forwards must stay inert.
        self.assertEqual(self.ts.materialize_self_only_chunks("doc1:L5", "doc1"), [])
        self.assertEqual(self.ts.path_titles("doc1:L5", "doc1"), "")
        self.assertEqual(self.ts.read_chunks("doc1:L5", "q", doc_id="doc1", k=3), [])
        blob = self.ts._materialize_leaf_path_chunks("doc1:L5", "doc1")
        self.assertEqual([c.node_id for c in blob], ["doc1:L5__path"])

    def test_harvest_collects_via_hierarchy_provider_only(self) -> None:
        def fake_policy_call(ts, state, config, *, subgoal, query, projection, actions, depth):
            collect = [a for a in actions if a.kind.value == "collect"]
            self.assertTrue(collect, "expected at least one visible COLLECT action")
            return collect, [], {collect[0].action_id: 0.9}, "matches seal spec", {}

        with patch("nav_harvest.harvest_policy_call", side_effect=fake_policy_call):
            result = harvest(
                self.ts,
                self.state,
                self.config,
                subgoal=self.subgoal,
                entry_scope="doc1:L5",
                query=self.subgoal.retrieval_query,
            )

        self.assertEqual(result.n_policy_calls, 1)
        self.assertIn("doc1:L5", result.new_section_ids)
        self.assertTrue(self.state.collected, "harvest should have hydrated chunks via the adapter")
        self.assertIn("mechanical face seal", self.state.collected[0][0].text)
        self.assertEqual(self.state.harvested_owner_subgoal.get("doc1:L5"), "s1")

    def test_plan_control_and_settle_close_the_loop(self) -> None:
        with patch(
            "nav_harvest.harvest_policy_call",
            side_effect=lambda ts, state, config, *, subgoal, query, projection, actions, depth: (
                [a for a in actions if a.kind.value == "collect"],
                [],
                {a.action_id: 0.9 for a in actions if a.kind.value == "collect"},
                "direct hit",
                {},
            ),
        ):
            harvest(
                self.ts,
                self.state,
                self.config,
                subgoal=self.subgoal,
                entry_scope="doc1:L5",
                query=self.subgoal.retrieval_query,
            )

        new_chunks = list(self.state.collected)
        signal = build_subgoal_result(
            self.plan,
            self.state.collected_section_ids,
            self.config,
            self.subgoal,
            retrieval_query=self.subgoal.retrieval_query,
            new_chunks=new_chunks,
            collected_before=set(),
            use_llm_extract=False,
        )

        def fake_nav_chat(**kwargs):
            return {
                "content": (
                    '{"subgoals": {"s1": {"decision": "accept"}}, '
                    '"global": "done", "reason": "ok"}'
                )
            }

        with patch("nav_llm.nav_chat", side_effect=fake_nav_chat):
            decision = plan_control(
                self.ts,
                self.state,
                self.config,
                plan=self.plan,
                wave_outputs=[{"subgoal_id": "s1", "result": signal, "new_chunks": new_chunks}],
            )

        self.assertEqual(decision.global_action, "done")
        self.assertEqual(decision.per_subgoal["s1"].decision, "accept")

        self.state.satisfied_subgoal_ids.add("s1")
        self.state.subgoal_results["s1"] = {
            "satisfied": True,
            "collected_section_ids": ["doc1:L5"],
        }
        self.state.attempted_subgoal_ids.add("s1")
        settled = pack_nav_evidence(
            self.state.collected, self.ts, self.state, self.config, budget_chars=2000
        )
        self.assertIn("mechanical face seal", settled.evidence_text)


if __name__ == "__main__":
    unittest.main()
