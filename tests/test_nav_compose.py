"""Tests for nav COMPOSE packing (confidence + parent-scoped tree)."""
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
    build_compose_preview,
    pack_nav_evidence,
    parse_collect_confidence,
)
from nav_types import ActionKind, LegalAction, NavConfig, NavState  # noqa: E402


def _line(doc: str, lid: int, content: str, level: int):
    return SimpleNamespace(line_id=lid, content=content, gold_level=level)


class NavComposePackTests(unittest.TestCase):
    def setUp(self) -> None:
        # L81 parent of L92; L92 parent of L93-L103; L81 parent of L84
        lines = [
            _line("doc", 81, "2.4 隐患整改", 2),
            _line("doc", 84, "2、重大事故隐患定义", 3),
            _line("doc", 92, "2.4.4 重大事故隐患整改、复查、销项", 3),
            _line("doc", 93, "方案包括以下内容：", 4),
            _line("doc", 94, "1、治理的目标和任务；", 4),
            _line("doc", 95, "2、采取的方法和措施；", 4),
            _line("doc", 102, "2.4.5 很长很长很长的无关段落" + ("哈" * 200), 4),
            _line("doc", 103, "2.4.6 另一段很长很长无关内容" + ("哈" * 200), 4),
        ]
        # parents by index: 81=None, 84->81, 92->81, 93-103->92
        parents = [None, 0, 0, 2, 2, 2, 2, 2]
        levels = [2, 3, 3, 4, 4, 4, 4, 4]
        bundle = SimpleNamespace(lines=lines, levels_for_tree=levels)
        idx = MagicMock()
        idx._bundles = {"doc": bundle}
        idx._doc_parents = {"doc": parents}
        idx._node_to_doc_line = {
            f"doc:L{ln.line_id}": ("doc", i) for i, ln in enumerate(lines)
        }
        self.ts = MagicMock()
        self.ts._idx = idx
        self.cfg = NavConfig(compose_confidence_weight=0.5)

    def _chunk(self, lid: int, text: str) -> Chunk:
        return Chunk(
            node_id=f"doc:L{lid}__path",
            doc_id="doc",
            text=text,
            line_ids=(lid,),
            section_id=f"doc:L{lid}",
        )

    def test_parse_confidence_map_and_scalar(self) -> None:
        acts = [
            LegalAction("C1", ActionKind.COLLECT, section_id="doc:L94"),
            LegalAction("C2", ActionKind.COLLECT, section_id="doc:L95"),
        ]
        m = parse_collect_confidence(
            {"confidence": {"C1": 0.9, "C2": 0.8}}, acts
        )
        self.assertAlmostEqual(m["C1"], 0.9)
        self.assertAlmostEqual(m["C2"], 0.8)
        s = parse_collect_confidence({"confidence": 0.7}, acts)
        self.assertAlmostEqual(s["C1"], 0.7)
        self.assertAlmostEqual(s["C2"], 0.7)
        z = parse_collect_confidence({}, acts)
        self.assertEqual(z["C1"], 0.0)

    def test_pack_prefers_confident_short_gold_over_long_noise(self) -> None:
        state = NavState(doc_id="doc", query="q", task_type="scope_collection")
        state.unit_scores = {
            "doc:L93": 0.073,
            "doc:L94": 0.045,
            "doc:L95": 0.038,
            "doc:L102": 0.066,
            "doc:L103": 0.064,
            "doc:L92": 0.073,
        }
        # Explicit gold conf; hydration noise conf=0
        state.collect_confidence = {
            "doc:L93": 0.8,
            "doc:L94": 0.9,
            "doc:L95": 0.9,
            "doc:L102": 0.0,
            "doc:L103": 0.0,
            "doc:L92": 0.5,
        }
        collected = [
            (self._chunk(92, "[§ 2.4.4]\n2.4.4 重大事故隐患整改、复查、销项"), 1.0),
            (self._chunk(93, "[§ 2.4.4]\n方案包括以下内容："), 1.0),
            (self._chunk(94, "[§ 2.4.4]\n1、治理的目标和任务；"), 1.0),
            (self._chunk(95, "[§ 2.4.4]\n2、采取的方法和措施；"), 1.0),
            (
                self._chunk(
                    102,
                    "[§ 2.4.4]\n2.4.5 很长很长很长的无关段落" + ("哈" * 200),
                ),
                1.0,
            ),
            (
                self._chunk(
                    103,
                    "[§ 2.4.4]\n2.4.6 另一段很长很长无关内容" + ("哈" * 200),
                ),
                1.0,
            ),
        ]
        fill = pack_nav_evidence(
            collected, self.ts, state, self.cfg, budget_chars=220
        )
        text = fill.evidence_text
        self.assertIn("治理的目标和任务", text)
        self.assertIn("采取的方法和措施", text)
        self.assertIn("[§ 2.4.4", text)
        # Parent is header only — should not keep L92 body as a competing peer.
        kept_owners = {c.section_id for c in fill.kept_chunks}
        self.assertNotIn("doc:L92", kept_owners)
        # Long noise loses to confident short gold under a tight budget.
        self.assertNotIn("2.4.5", text)
        self.assertNotIn("2.4.6", text)

    def test_group_key_uses_child_final_score_with_confidence(self) -> None:
        state = NavState(doc_id="doc", query="q")
        state.unit_scores = {
            "doc:L94": 0.05,
            "doc:L84": 0.08,
        }
        state.collect_confidence = {"doc:L94": 0.9, "doc:L84": 0.0}
        collected = [
            (self._chunk(94, "1、治理的目标和任务；"), 1.0),
            (self._chunk(84, "2、重大事故隐患定义"), 1.0),
        ]
        fill = pack_nav_evidence(
            collected, self.ts, state, self.cfg, budget_chars=500
        )
        # L94 group score = 0.05+0.5*0.9=0.50 > L84 0.08 → L92 group first
        self.assertTrue(fill.evidence_text.index("治理") < fill.evidence_text.index("重大事故隐患定义"))

    def test_pack_skips_oversized_keeps_later_short(self) -> None:
        """Within a group: skip a too-large high-score child; pack later short ones."""
        state = NavState(doc_id="doc", query="q", task_type="scope_collection")
        state.unit_scores = {
            "doc:L102": 0.09,
            "doc:L94": 0.05,
            "doc:L95": 0.04,
        }
        state.collect_confidence = {
            "doc:L102": 0.9,
            "doc:L94": 0.9,
            "doc:L95": 0.9,
        }
        collected = [
            (
                self._chunk(
                    102,
                    "[§ 2.4.4]\n2.4.5 很长很长很长的无关段落" + ("哈" * 200),
                ),
                1.0,
            ),
            (self._chunk(94, "[§ 2.4.4]\n1、治理的目标和任务；"), 1.0),
            (self._chunk(95, "[§ 2.4.4]\n2、采取的方法和措施；"), 1.0),
        ]
        fill = pack_nav_evidence(
            collected, self.ts, state, self.cfg, budget_chars=120
        )
        text = fill.evidence_text
        self.assertIn("治理的目标和任务", text)
        self.assertIn("采取的方法和措施", text)
        self.assertNotIn("2.4.5", text)

    def test_group_priority_overrides_unit_score_order(self) -> None:
        """External group_rank priority packs low-unit gold group before high-unit intro."""
        state = NavState(doc_id="doc", query="q", task_type="scope_collection")
        state.unit_scores = {
            "doc:L94": 0.04,
            "doc:L84": 0.09,
        }
        state.collect_confidence = {"doc:L94": 0.0, "doc:L84": 0.0}
        # Prefer the L92-parented gold group over the L81-parented intro group.
        state.group_priority = {
            "doc:L92": 2.0,
            "doc:L81": 1.0,
        }
        collected = [
            (self._chunk(94, "1、治理的目标和任务；"), 1.0),
            (self._chunk(84, "2、重大事故隐患定义" + ("X" * 80)), 1.0),
        ]
        fill = pack_nav_evidence(
            collected, self.ts, state, self.cfg, budget_chars=120
        )
        self.assertIn("治理的目标和任务", fill.evidence_text)
        # Intro may be dropped under tight budget; if present it must follow gold.
        if "重大事故隐患定义" in fill.evidence_text:
            self.assertTrue(
                fill.evidence_text.index("治理")
                < fill.evidence_text.index("重大事故隐患定义")
            )

    def test_build_compose_preview_emits_g_ids(self) -> None:
        state = NavState(doc_id="doc", query="q")
        state.unit_scores = {"doc:L94": 0.05, "doc:L84": 0.08}
        collected = [
            (self._chunk(94, "1、治理的目标和任务；"), 1.0),
            (self._chunk(84, "2、重大事故隐患定义"), 1.0),
        ]
        text, g_map = build_compose_preview(collected, self.ts, state, self.cfg)
        self.assertIn("[G1]", text)
        self.assertTrue(g_map)
        self.assertTrue(all(k.startswith("G") for k in g_map))
        self.assertTrue(all(":" in v for v in g_map.values()))

    def test_waterfill_single_group_keeps_low_score_gold_as_snippet(self) -> None:
        """Large single group: low-score gold still enters kept via snippet breadth."""
        cfg = NavConfig(
            compose_confidence_weight=0.5,
            compose_packing_mode="waterfill",
            compose_coverage_budget_frac=0.4,
            compose_snippet_chars=40,
        )
        state = NavState(doc_id="doc", query="q", task_type="multi_hop")
        # High scores on long noise; low on short gold.
        state.unit_scores = {
            "doc:L102": 0.09,
            "doc:L103": 0.08,
            "doc:L93": 0.07,
            "doc:L94": 0.02,
            "doc:L95": 0.01,
        }
        state.collect_confidence = {k: 0.0 for k in state.unit_scores}
        long = "很长很长无关段落" + ("哈" * 120)
        collected = [
            (self._chunk(102, f"[§ 2.4.4]\n2.4.5 {long}"), 1.0),
            (self._chunk(103, f"[§ 2.4.4]\n2.4.6 {long}"), 1.0),
            (self._chunk(93, "[§ 2.4.4]\n方案包括以下内容："), 1.0),
            (self._chunk(94, "[§ 2.4.4]\n1、治理的目标和任务；"), 1.0),
            (self._chunk(95, "[§ 2.4.4]\n2、采取的方法和措施；"), 1.0),
        ]
        greedy = pack_nav_evidence(
            collected, self.ts, state, NavConfig(compose_packing_mode="greedy"), budget_chars=160
        )
        fill = pack_nav_evidence(collected, self.ts, state, cfg, budget_chars=160)
        kept_owners = {c.section_id for c in fill.kept_chunks}
        self.assertIn("doc:L94", kept_owners)
        self.assertIn("doc:L95", kept_owners)
        self.assertGreaterEqual(len(kept_owners), len({c.section_id for c in greedy.kept_chunks}))

    def test_waterfill_cross_group_does_not_zero_low_priority(self) -> None:
        """Low-priority group with gold still keeps at least one owner under waterfill."""
        cfg = NavConfig(
            compose_confidence_weight=0.5,
            compose_packing_mode="waterfill",
            compose_coverage_budget_frac=0.5,
            compose_snippet_chars=40,
        )
        state = NavState(doc_id="doc", query="q", task_type="scope_collection")
        state.unit_scores = {
            "doc:L102": 0.09,
            "doc:L103": 0.08,
            "doc:L94": 0.01,
        }
        state.collect_confidence = {k: 0.0 for k in state.unit_scores}
        # Prefer L81-parented noise group over L92-parented gold.
        state.group_priority = {"doc:L81": 2.0, "doc:L92": 1.0}
        collected = [
            (self._chunk(84, "2、重大事故隐患定义" + ("X" * 200)), 1.0),
            (self._chunk(94, "1、治理的目标和任务；"), 1.0),
        ]
        state.unit_scores = {"doc:L84": 0.09, "doc:L94": 0.01}
        state.collect_confidence = {"doc:L84": 0.0, "doc:L94": 0.0}
        fill = pack_nav_evidence(collected, self.ts, state, cfg, budget_chars=120)
        kept_owners = {c.section_id for c in fill.kept_chunks}
        self.assertIn("doc:L94", kept_owners)

    def test_waterfill_fit_shortcircuit_matches_greedy(self) -> None:
        """When pool fits, waterfill returns the same evidence_text as greedy."""
        cfg_w = NavConfig(compose_packing_mode="waterfill", compose_coverage_budget_frac=0.4)
        cfg_g = NavConfig(compose_packing_mode="greedy")
        state = NavState(doc_id="doc", query="q")
        state.unit_scores = {"doc:L94": 0.05, "doc:L95": 0.04}
        state.collect_confidence = {"doc:L94": 0.9, "doc:L95": 0.9}
        collected = [
            (self._chunk(94, "1、治理的目标和任务；"), 1.0),
            (self._chunk(95, "2、采取的方法和措施；"), 1.0),
        ]
        g = pack_nav_evidence(collected, self.ts, state, cfg_g, budget_chars=500)
        w = pack_nav_evidence(collected, self.ts, state, cfg_w, budget_chars=500)
        self.assertEqual(w.evidence_text, g.evidence_text)
        self.assertFalse(w.dropped_any)

    def test_waterfill_owner_floor_vs_greedy(self) -> None:
        """Waterfill never keeps fewer distinct owners than greedy on same pool."""
        cfg_w = NavConfig(
            compose_packing_mode="waterfill",
            compose_coverage_budget_frac=0.4,
            compose_snippet_chars=40,
        )
        cfg_g = NavConfig(compose_packing_mode="greedy")
        state = NavState(doc_id="doc", query="q")
        state.unit_scores = {
            "doc:L102": 0.09,
            "doc:L103": 0.08,
            "doc:L94": 0.02,
            "doc:L95": 0.01,
        }
        state.collect_confidence = {k: 0.0 for k in state.unit_scores}
        long = "很长很长无关段落" + ("哈" * 120)
        collected = [
            (self._chunk(102, f"2.4.5 {long}"), 1.0),
            (self._chunk(103, f"2.4.6 {long}"), 1.0),
            (self._chunk(94, "1、治理的目标和任务；"), 1.0),
            (self._chunk(95, "2、采取的方法和措施；"), 1.0),
        ]
        g = pack_nav_evidence(collected, self.ts, state, cfg_g, budget_chars=140)
        w = pack_nav_evidence(collected, self.ts, state, cfg_w, budget_chars=140)
        self.assertGreaterEqual(
            len({c.section_id for c in w.kept_chunks}),
            len({c.section_id for c in g.kept_chunks}),
        )


if __name__ == "__main__":
    unittest.main()
