"""Unit tests for M6 per-subgoal budget ledger settle."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock

ROOT = Path(__file__).resolve().parents[1]
for source_dir in (ROOT / "src" / "realdata", ROOT / "src" / "nav"):
    if str(source_dir) not in sys.path:
        sys.path.insert(0, str(source_dir))

from agent_delivery.code.index_retrieval import Chunk  # noqa: E402
from nav_compose import (  # noqa: E402
    build_budget_ledger,
    pack_nav_evidence,
    settle_subgoal_evidence,
)
from nav_plan import Contract, RetrievalPlan, Subgoal  # noqa: E402
from nav_types import NavConfig, NavState  # noqa: E402


def _line(doc: str, lid: int, content: str, level: int):
    return SimpleNamespace(line_id=lid, content=content, gold_level=level)


class BudgetLedgerSettleTests(unittest.TestCase):
    def setUp(self) -> None:
        lines = [
            _line("doc", 1, "章", 1),
            _line("doc", 10, "s1-a", 2),
            _line("doc", 11, "s1-b", 2),
            _line("doc", 20, "s2-a", 2),
            _line("doc", 21, "s2-b", 2),
        ]
        parents = [None, 0, 0, 0, 0]
        levels = [1, 2, 2, 2, 2]
        bundle = SimpleNamespace(lines=lines, levels_for_tree=levels)
        idx = MagicMock()
        idx._bundles = {"doc": bundle}
        idx._doc_parents = {"doc": parents}
        idx._node_to_doc_line = {
            f"doc:L{ln.line_id}": ("doc", i) for i, ln in enumerate(lines)
        }
        self.ts = MagicMock()
        self.ts._idx = idx

    def _chunk(self, lid: int, text: str) -> Chunk:
        return Chunk(
            node_id=f"doc:L{lid}__path",
            doc_id="doc",
            text=text,
            line_ids=(lid,),
            section_id=f"doc:L{lid}",
        )

    def _plan_two(self) -> RetrievalPlan:
        return RetrievalPlan(
            subgoals=[
                Subgoal(
                    id="s1",
                    need="hop1",
                    retrieval_query="hop1",
                    budget_share=0.5,
                    produces=["a"],
                    contract=Contract(kind="single_fact"),
                ),
                Subgoal(
                    id="s2",
                    need="hop2",
                    retrieval_query="hop2",
                    budget_share=0.5,
                    produces=["b"],
                    contract=Contract(kind="enumeration", cardinality=3),
                ),
            ]
        )

    def test_config_defaults_off(self) -> None:
        cfg = NavConfig.from_dict({})
        self.assertFalse(cfg.enable_subgoal_budget_ledger)
        self.assertAlmostEqual(cfg.subgoal_budget_floor_frac, 1.0)

    def test_disabled_matches_global_pack(self) -> None:
        plan = self._plan_two()
        state = NavState(doc_id="doc", query="q", retrieval_plan=plan)
        state.attempted_subgoal_ids = {"s1", "s2"}
        state.satisfied_subgoal_ids = {"s1"}
        state.subgoal_results = {
            "s1": {
                "satisfied": True,
                "verdict": "SATISFIED",
                "collected_section_ids": ["doc:L10", "doc:L11"],
            },
            "s2": {
                "satisfied": False,
                "verdict": "RETRY_SAME_REGION",
                "gap": "enumeration_short:1<3",
                "collected_section_ids": ["doc:L20", "doc:L21"],
            },
        }
        long_s1 = "甲" * 180
        collected = [
            (self._chunk(10, long_s1), 2.0),
            (self._chunk(11, "乙" * 40), 1.5),
            (self._chunk(20, "丙重要证据二跳"), 1.0),
            (self._chunk(21, "丁补充条目"), 0.5),
        ]
        cfg = NavConfig(
            compose_packing_mode="greedy",
            enable_subgoal_budget_ledger=False,
        )
        global_fill = pack_nav_evidence(
            collected, self.ts, state, cfg, budget_chars=120
        )
        settled, ledger = settle_subgoal_evidence(
            collected, self.ts, state, cfg, budget_chars=120
        )
        self.assertIsNone(ledger)
        self.assertEqual(settled.evidence_text, global_fill.evidence_text)

    def test_floor_protects_second_hop(self) -> None:
        plan = self._plan_two()
        state = NavState(doc_id="doc", query="q", retrieval_plan=plan)
        state.attempted_subgoal_ids = {"s1", "s2"}
        state.satisfied_subgoal_ids = {"s1"}
        state.subgoal_results = {
            "s1": {
                "satisfied": True,
                "verdict": "SATISFIED",
                "collected_section_ids": ["doc:L10", "doc:L11"],
            },
            "s2": {
                "satisfied": False,
                "verdict": "RETRY_SAME_REGION",
                "gap": "enumeration_short:1<3",
                "collected_section_ids": ["doc:L20", "doc:L21"],
            },
        }
        marker = "SECOND_HOP_GOLD_MARKER"
        # Two ~70-char high-score s1 chunks fill B=100; low-score marker is dropped globally.
        collected = [
            (self._chunk(10, "甲" * 70), 5.0),
            (self._chunk(11, "乙" * 70), 4.0),
            (self._chunk(20, marker), 0.05),
            (self._chunk(21, "丁"), 0.01),
        ]
        cfg_off = NavConfig(
            compose_packing_mode="greedy",
            enable_subgoal_budget_ledger=False,
        )
        cfg_on = NavConfig(
            compose_packing_mode="greedy",
            enable_subgoal_budget_ledger=True,
            subgoal_budget_floor_frac=1.0,
        )
        B = 100
        global_fill = pack_nav_evidence(
            collected, self.ts, state, cfg_off, budget_chars=B
        )
        settled, ledger = settle_subgoal_evidence(
            collected, self.ts, state, cfg_on, budget_chars=B
        )
        self.assertIsNotNone(ledger)
        assert ledger is not None
        self.assertEqual(ledger.floors.get("s1"), 50)
        self.assertEqual(ledger.floors.get("s2"), 50)
        self.assertNotIn(marker, global_fill.evidence_text)
        self.assertIn(marker, settled.evidence_text)
        # Floor reserves 50; actual alloc is min(floor, need) so may be < floor for short evidence.
        self.assertGreater(ledger.final_alloc.get("s2", 0), 0)
        self.assertEqual(ledger.floors.get("s2"), 50)

    def test_tier2_recirculates_to_unsatisfied_enumeration(self) -> None:
        plan = self._plan_two()
        state = NavState(doc_id="doc", query="q", retrieval_plan=plan)
        state.attempted_subgoal_ids = {"s1", "s2"}
        state.satisfied_subgoal_ids = {"s1"}
        state.subgoal_results = {
            "s1": {
                "satisfied": True,
                "verdict": "SATISFIED",
                "collected_section_ids": ["doc:L10"],
            },
            "s2": {
                "satisfied": False,
                "verdict": "RETRY_SAME_REGION",
                "gap": "enumeration_short:1<3",
                "collected_section_ids": ["doc:L20", "doc:L21"],
            },
        }
        needs = {"s1": 10, "s2": 200}
        ledger = build_budget_ledger(
            state, budget_chars=100, floor_frac=1.0, needs=needs
        )
        self.assertEqual(ledger.floors["s1"], 50)
        self.assertEqual(ledger.floors["s2"], 50)
        self.assertEqual(ledger.tier1["s1"], 10)
        self.assertEqual(ledger.tier1["s2"], 50)
        self.assertEqual(ledger.tier2_bonus.get("s2"), 40)
        self.assertEqual(ledger.final_alloc["s2"], 90)
        self.assertIn("s2", ledger.tier2_recipients)

        collected = [
            (self._chunk(10, "短"), 1.0),
            (self._chunk(20, "枚举一AAA"), 1.0),
            (self._chunk(21, "枚举二BBB"), 1.0),
        ]
        cfg = NavConfig(
            compose_packing_mode="greedy",
            enable_subgoal_budget_ledger=True,
            subgoal_budget_floor_frac=1.0,
        )
        fill, led2 = settle_subgoal_evidence(
            collected, self.ts, state, cfg, budget_chars=100
        )
        self.assertIsNotNone(led2)
        assert led2 is not None
        # Short s2 items: need may be <= floor, so bonus can be 0; still both must appear
        # because floors alone cover them. Recirculation math is covered above.
        self.assertIn("枚举一AAA", fill.evidence_text)
        self.assertIn("枚举二BBB", fill.evidence_text)
        self.assertGreaterEqual(led2.final_alloc.get("s2", 0), led2.used.get("s2", 0))


if __name__ == "__main__":
    unittest.main()
