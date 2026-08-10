"""Unit tests for the merged plan_control check authority (src/nav/nav_control.py)."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
for source_dir in (ROOT / "src" / "realdata", ROOT / "src" / "nav"):
    if str(source_dir) not in sys.path:
        sys.path.insert(0, str(source_dir))

from agent_delivery.code.index_retrieval import Chunk  # noqa: E402
from nav_control import _digest_collected_summaries, plan_control  # noqa: E402
from nav_plan import Contract, RetrievalPlan, Subgoal  # noqa: E402
from nav_types import NavConfig, NavState  # noqa: E402


def _chunk(text: str, *, section_id: str = "doc:L1") -> Chunk:
    return Chunk(
        node_id=f"{section_id}__path",
        doc_id="doc",
        text=text,
        line_ids=(1,),
        section_id=section_id,
    )


def _signal(
    *,
    chars_used: int = 0,
    gap: str = "",
    collected_section_ids: list[str] | None = None,
) -> SimpleNamespace:
    return SimpleNamespace(
        chars_used=chars_used,
        gap=gap,
        satisfied=chars_used > 0,
        collected_section_ids=list(collected_section_ids or []),
    )


def _plan_two() -> RetrievalPlan:
    return RetrievalPlan(
        subgoals=[
            Subgoal(id="s1", need="hop1", retrieval_query="hop1", contract=Contract(kind="single_fact")),
            Subgoal(id="s2", need="hop2", retrieval_query="hop2", contract=Contract(kind="enumeration", cardinality=3)),
        ]
    )


class DigestCollectedSummariesTests(unittest.TestCase):
    def test_uses_section_summaries_without_char_cut(self) -> None:
        long_summary = "S" * 400

        class _TS:
            def get_structure(self, section_id: str) -> dict:
                return {"preview": "1.1.3 勘测设计过程", "summary": long_summary}

        digest = _digest_collected_summaries(
            _TS(),
            collected_section_ids=["sec_survey"],
        )
        self.assertIn("1.1.3 勘测设计过程", digest)
        self.assertIn(long_summary, digest)
        self.assertEqual(digest.count(long_summary), 1)

    def test_empty_without_explicit_collect_ids(self) -> None:
        class _TS:
            def get_structure(self, section_id: str) -> dict:
                return {"preview": "parent", "summary": f"sum:{section_id}"}

        digest = _digest_collected_summaries(
            _TS(),
            collected_section_ids=[],
        )
        self.assertEqual(digest, "")

    def test_only_listed_explicit_collects(self) -> None:
        class _TS:
            def get_structure(self, section_id: str) -> dict:
                return {"preview": section_id, "summary": f"sum:{section_id}"}

        digest = _digest_collected_summaries(
            _TS(),
            collected_section_ids=["sec_parent"],
        )
        self.assertIn("sum:sec_parent", digest)
        self.assertNotIn("sum:sec_child", digest)

    def test_empty_when_nothing_collected(self) -> None:
        self.assertEqual(
            _digest_collected_summaries(None, collected_section_ids=[]),
            "",
        )


class PlanControlTests(unittest.TestCase):
    def setUp(self) -> None:
        self.plan = _plan_two()
        self.state = NavState(doc_id="doc", query="q", retrieval_plan=self.plan)
        self.config = NavConfig(mode="checklist")

    def test_no_wave_outputs_returns_continue(self) -> None:
        decision = plan_control(None, self.state, self.config, plan=self.plan, wave_outputs=[])
        self.assertEqual(decision.global_action, "continue")
        self.assertEqual(decision.per_subgoal, {})

    def test_fallback_on_llm_failure_maps_evidence_to_accept_else_widen(self) -> None:
        wave_outputs = [
            {"subgoal_id": "s1", "result": _signal(chars_used=12), "new_chunks": [(_chunk("ok"), 1.0)]},
            {"subgoal_id": "s2", "result": _signal(chars_used=0), "new_chunks": []},
        ]
        with patch(
            "agent_delivery.code.llm_config.require_llm_env",
            side_effect=RuntimeError("no llm env in test"),
        ):
            decision = plan_control(
                None, self.state, self.config, plan=self.plan, wave_outputs=wave_outputs
            )
        self.assertEqual(decision.global_action, "continue")
        self.assertEqual(decision.per_subgoal["s1"].decision, "accept")
        self.assertEqual(decision.per_subgoal["s2"].decision, "widen")
        self.assertEqual(decision.reason, "fallback")

    def test_parses_llm_decision_and_fills_missing_subgoal(self) -> None:
        """LLM only mentions s1; s2 must still get an explicit accept/widen fallback."""
        wave_outputs = [
            {"subgoal_id": "s1", "result": _signal(chars_used=12), "new_chunks": [(_chunk("ok"), 1.0)]},
            {"subgoal_id": "s2", "result": _signal(chars_used=0), "new_chunks": []},
        ]

        def fake_nav_chat(**kwargs):
            return {
                "content": (
                    '{"subgoals": {"s1": {"decision": "accept", "note": "done"}}, '
                    '"global": "continue", "reason": "s1 has evidence, s2 empty"}'
                )
            }

        with patch("nav_llm.nav_chat", side_effect=fake_nav_chat):
            decision = plan_control(
                None, self.state, self.config, plan=self.plan, wave_outputs=wave_outputs
            )

        self.assertEqual(decision.global_action, "continue")
        self.assertEqual(decision.per_subgoal["s1"].decision, "accept")
        self.assertEqual(decision.per_subgoal["s1"].note, "done")
        # s2 was omitted by the LLM; must still receive an explicit decision.
        self.assertIn("s2", decision.per_subgoal)
        self.assertEqual(decision.per_subgoal["s2"].decision, "widen")

    def test_invalid_decision_and_global_values_fall_back_to_defaults(self) -> None:
        wave_outputs = [
            {"subgoal_id": "s1", "result": _signal(chars_used=0), "new_chunks": []},
        ]

        def fake_nav_chat(**kwargs):
            return {
                "content": (
                    '{"subgoals": {"s1": {"decision": "not_a_real_decision"}}, '
                    '"global": "not_a_real_global", "reason": "garbage"}'
                )
            }

        with patch("nav_llm.nav_chat", side_effect=fake_nav_chat):
            decision = plan_control(
                None, self.state, self.config, plan=self.plan, wave_outputs=wave_outputs
            )

        self.assertEqual(decision.global_action, "continue")
        # Unknown per-subgoal decision token still defaults to accept in the parser.
        self.assertEqual(decision.per_subgoal["s1"].decision, "accept")


if __name__ == "__main__":
    unittest.main()
