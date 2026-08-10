"""Unit tests for M4/M5 orchestration + slot binding (no LLM navigate)."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch


ROOT = Path(__file__).resolve().parents[1]
for source_dir in (ROOT / "src" / "realdata", ROOT / "src" / "nav"):
    if str(source_dir) not in sys.path:
        sys.path.insert(0, str(source_dir))

from nav_control import PlanControlDecision, SubgoalDecision  # noqa: E402
from nav_hierarchy import InMemoryHierarchyProvider, InMemoryNode, ProviderToolSpace  # noqa: E402
from nav_orchestrate import ready_subgoal_ids  # noqa: E402
from nav_plan import Contract, RetrievalPlan, Subgoal  # noqa: E402
from nav_types import NavConfig, NavState  # noqa: E402
from nav_verify import (  # noqa: E402
    apply_bindings_from_result,
    demanded_slot_names,
    extract_slots_heuristic,
)


class TestNavSlots(unittest.TestCase):
    def test_heuristic_extract_prefers_must_mention(self) -> None:
        evidence = "本章规定对外重大合同应使用法人章办理用印。"
        slots = extract_slots_heuristic(
            ["seal_type"],
            evidence,
            retrieval_query="印章类型",
            need="seal",
            must_mention=["法人章"],
        )
        self.assertEqual(slots.get("seal_type"), "法人章")

    def test_demanded_slots_only_when_downstream_refs(self) -> None:
        plan = RetrievalPlan(
            subgoals=[
                Subgoal(
                    id="s1",
                    need="type",
                    retrieval_query="印章类型",
                    produces=["seal_type", "unused"],
                ),
                Subgoal(
                    id="s2",
                    need="proc",
                    retrieval_query="{{s1.seal_type}} 审批",
                    depends_on=["s1"],
                ),
            ]
        )
        self.assertEqual(demanded_slot_names(plan, plan.subgoals[0]), ["seal_type"])
        self.assertEqual(demanded_slot_names(plan, plan.subgoals[1]), [])

    def test_prefer_after_orders_ready(self) -> None:
        from nav_orchestrate import order_ready_by_prefer_after

        plan = RetrievalPlan(
            subgoals=[
                Subgoal(id="s1", need="a", retrieval_query="a"),
                Subgoal(
                    id="s2",
                    need="b",
                    retrieval_query="b",
                    prefer_after=["s1"],
                ),
            ]
        )
        self.assertEqual(
            order_ready_by_prefer_after(plan, ["s2", "s1"]),
            ["s1", "s2"],
        )

    def test_empty_evidence_retries_then_marks_satisfied(self) -> None:
        from nav_orchestrate import execute_plan

        plan = RetrievalPlan(
            subgoals=[
                Subgoal(
                    id="s1",
                    need="type",
                    retrieval_query="印章类型",
                    produces=["seal_type"],
                    contract=Contract(kind="single_fact", must_mention=["法人章"]),
                ),
            ]
        )
        state = NavState(doc_id="doc", query="q", retrieval_plan=plan)
        cfg = NavConfig(
            enable_plan_orchestration=True,
            map_char_limit=5000,
            subgoal_max_attempts=2,
        )

        class _Chunk:
            def __init__(self, text: str) -> None:
                self.text = text
                self.node_id = "n1"

        calls = {"n": 0}

        def fake_nav(ts, *, state, scope, query, config, depth=0, budget=None, steps_out=None):
            calls["n"] += 1
            if calls["n"] == 1:
                pass
            else:
                state.collected.append((_Chunk("对外重大合同应使用法人章。"), 1.0))
                state.collected_section_ids.add("doc:L1")

        with patch("nav_orchestrate.navigate", side_effect=fake_nav):
            execute_plan(MagicMock(), state, cfg, steps_out=[], episode_query="q")
        self.assertGreaterEqual(calls["n"], 2)
        self.assertIn("s1", state.satisfied_subgoal_ids)
        self.assertIn("s1", state.attempted_subgoal_ids)

    def test_apply_bindings_writes_qualified_keys(self) -> None:
        sg = Subgoal(id="s1", need="a", retrieval_query="a", produces=["seal_type"])
        out = apply_bindings_from_result({}, sg, {"seal_type": "法人章"})
        self.assertEqual(out["seal_type"], "法人章")
        self.assertEqual(out["s1.seal_type"], "法人章")


class TestNavOrchestrate(unittest.TestCase):
    def test_ready_respects_deps_only(self) -> None:
        plan = RetrievalPlan(
            subgoals=[
                Subgoal(id="s1", need="a", retrieval_query="印章类型", produces=["seal_type"]),
                Subgoal(
                    id="s2",
                    need="b",
                    retrieval_query="{{s1.seal_type}} 审批",
                    depends_on=["s1"],
                    produces=["proc"],
                ),
                Subgoal(
                    id="s3",
                    need="c",
                    retrieval_query="财务专用章",
                ),
            ]
        )
        ready0 = ready_subgoal_ids(plan, satisfied=set(), activated=set())
        self.assertEqual(ready0, ["s1", "s3"])
        ready1 = ready_subgoal_ids(plan, satisfied={"s1"}, activated=set())
        self.assertEqual(ready1, ["s2", "s3"])

    def test_dropped_precursor_settles_deps_like_satisfied(self) -> None:
        """F1: a dropped precursor must not starve a downstream subgoal forever."""
        plan = RetrievalPlan(
            subgoals=[
                Subgoal(id="s1", need="a", retrieval_query="a"),
                Subgoal(id="s2", need="b", retrieval_query="b", depends_on=["s1"]),
            ]
        )
        still_blocked = ready_subgoal_ids(
            plan, satisfied=set(), activated=set(), dropped=set(), attempted={"s1"}
        )
        self.assertEqual(still_blocked, [])
        unblocked = ready_subgoal_ids(
            plan, satisfied=set(), activated=set(), dropped={"s1"}, attempted={"s1"}
        )
        self.assertEqual(unblocked, ["s2"])

    def test_same_wave_subgoals_run_own_queries(self) -> None:
        """Independent subgoals never share one navigate call or one result."""
        from nav_orchestrate import execute_plan

        plan = RetrievalPlan(
            subgoals=[
                Subgoal(
                    id="s1",
                    need="a",
                    retrieval_query="法人章 适用范围",
                    produces=["seal_type"],
                    contract=Contract(kind="single_fact", must_mention=["法人章"]),
                ),
                Subgoal(
                    id="s2",
                    need="b",
                    retrieval_query="档案保管 年限",
                    produces=["years"],
                    contract=Contract(kind="single_fact", must_mention=["保管"]),
                ),
            ]
        )
        state = NavState(doc_id="doc", query="q", retrieval_plan=plan)
        cfg = NavConfig(enable_plan_orchestration=True, map_char_limit=5000)

        class _Chunk:
            def __init__(self, text: str) -> None:
                self.text = text
                self.node_id = "n1"

        calls: list[str] = []

        def fake_nav(ts, *, state, scope, query, config, depth=0, budget=None, steps_out=None):
            calls.append(query)
            if "法人章" in query:
                state.collected.append((_Chunk("对外重大合同应使用法人章。"), 1.0))
                state.collected_section_ids.add("doc:L1")

        with patch("nav_orchestrate.navigate", side_effect=fake_nav):
            execute_plan(MagicMock(), state, cfg, steps_out=[], episode_query="q")

        self.assertTrue(any("法人章" in c and "档案保管" not in c for c in calls))
        self.assertTrue(any("档案保管" in c and "法人章" not in c for c in calls))
        self.assertIn("s1", state.satisfied_subgoal_ids)
        self.assertNotIn("s2", state.satisfied_subgoal_ids)

    def test_config_flags_default_off(self) -> None:
        cfg = NavConfig.from_dict({})
        self.assertFalse(cfg.enable_plan_orchestration)
        self.assertFalse(cfg.enable_slot_extract)
        self.assertEqual(cfg.max_replans, 0)
        self.assertEqual(cfg.max_waves, 0)

    def test_execute_plan_wave_order_with_mocked_navigate(self) -> None:
        from nav_orchestrate import execute_plan

        plan = RetrievalPlan(
            subgoals=[
                Subgoal(
                    id="s1",
                    need="type",
                    retrieval_query="印章类型 法人章",
                    produces=["seal_type"],
                    contract=Contract(kind="single_fact", must_mention=["法人章"]),
                    budget_share=0.5,
                ),
                Subgoal(
                    id="s2",
                    need="proc",
                    retrieval_query="{{s1.seal_type}} 用印审批",
                    depends_on=["s1"],
                    produces=["proc"],
                    contract=Contract(kind="single_fact"),
                    budget_share=0.5,
                ),
            ]
        )
        state = NavState(doc_id="doc", query="q", retrieval_plan=plan)
        cfg = NavConfig(enable_plan_orchestration=True, map_char_limit=5000)

        class _Chunk:
            def __init__(self, text: str) -> None:
                self.text = text
                self.node_id = "n1"

        calls = []

        def fake_nav(ts, *, state, scope, query, config, depth=0, budget=None, steps_out=None):
            calls.append(query)
            if "印章类型" in query:
                state.collected.append((_Chunk("对外重大合同应使用法人章。"), 1.0))
                state.collected_section_ids.add("doc:L1")
            else:
                state.collected.append((_Chunk("用印审批程序见第四章。"), 1.0))
                state.collected_section_ids.add("doc:L2")

        with patch("nav_orchestrate.navigate", side_effect=fake_nav):
            detail = execute_plan(MagicMock(), state, cfg, steps_out=[], episode_query="q")
        self.assertGreaterEqual(len(calls), 2)
        self.assertIn("印章类型", calls[0])
        self.assertIn("法人章", calls[1])  # rebound
        self.assertIn("s1", state.satisfied_subgoal_ids)
        self.assertIn("s2", state.satisfied_subgoal_ids)
        self.assertEqual(state.slot_bindings.get("seal_type"), "法人章")
        self.assertGreaterEqual(detail.get("n_waves", 0), 2)

    def test_no_slot_extract_when_nobody_consumes(self) -> None:
        from nav_orchestrate import execute_plan
        from nav_verify import extract_slots

        plan = RetrievalPlan(
            subgoals=[
                Subgoal(
                    id="s1",
                    need="type",
                    retrieval_query="印章类型",
                    produces=["seal_type"],
                    contract=Contract(kind="single_fact", must_mention=["法人章"]),
                ),
            ]
        )
        # Leaf subgoal: produces declared but no downstream consumer.
        extracted, _ = extract_slots(
            plan,
            plan.subgoals[0],
            "对外重大合同应使用法人章。",
            NavConfig(),
            use_llm=True,
        )
        self.assertEqual(extracted, {})

        state = NavState(doc_id="doc", query="q", retrieval_plan=plan)
        cfg = NavConfig(
            enable_plan_orchestration=True,
            enable_slot_extract=True,
            map_char_limit=5000,
        )

        class _Chunk:
            def __init__(self, text: str) -> None:
                self.text = text

        def fake_nav(ts, *, state, scope, query, config, depth=0, budget=None, steps_out=None):
            state.collected.append((_Chunk("对外重大合同应使用法人章。"), 1.0))
            state.collected_section_ids.add("doc:L1")

        with patch("nav_orchestrate.navigate", side_effect=fake_nav), patch(
            "nav_verify.extract_slots_llm"
        ) as llm:
            execute_plan(MagicMock(), state, cfg, steps_out=[], episode_query="q")
        llm.assert_not_called()
        self.assertEqual(state.slot_bindings, {})

    def test_widen_moves_anchor_to_parent_then_drops_at_root(self) -> None:
        """F2 fix: widen is deterministic move-to-parent; exhausting the
        document with nowhere coarser to go degrades to drop, never an
        anchor="" empty-loop repeat of the exact same harvest."""
        from nav_orchestrate import _apply_plan_control

        nodes = {
            "doc1:ROOT": InMemoryNode(
                section_id="doc1:ROOT", title="Root", children=["doc1:A"]
            ),
            "doc1:A": InMemoryNode(section_id="doc1:A", title="A", children=["doc1:A1"]),
            "doc1:A1": InMemoryNode(section_id="doc1:A1", title="A1", content="x"),
        }
        provider = InMemoryHierarchyProvider(roots_by_doc={"doc1": ["doc1:ROOT"]}, nodes=nodes)
        ts = ProviderToolSpace(provider)

        subgoal = Subgoal(id="s1", need="x", retrieval_query="x")
        plan = RetrievalPlan(subgoals=[subgoal])
        state = NavState(doc_id="doc1", query="x", retrieval_plan=plan)
        state.subgoal_anchor["s1"] = "doc1:A1"
        cfg = NavConfig(subgoal_max_attempts=5)
        outputs = [
            {
                "subgoal_id": "s1",
                "result": SimpleNamespace(satisfied=False, chars_used=0, gap="empty_evidence"),
                "new_chunks": [],
            }
        ]
        widen_decision = PlanControlDecision(
            per_subgoal={"s1": SubgoalDecision(subgoal_id="s1", decision="widen")},
            global_action="continue",
        )

        with patch("nav_control.plan_control", return_value=widen_decision):
            _apply_plan_control(
                ts, state, cfg, plan=plan, outputs=outputs, by_id={"s1": subgoal}, steps_out=None
            )
        self.assertEqual(state.subgoal_anchor["s1"], "doc1:A")

        with patch("nav_control.plan_control", return_value=widen_decision):
            _apply_plan_control(
                ts, state, cfg, plan=plan, outputs=outputs, by_id={"s1": subgoal}, steps_out=None
            )
        self.assertEqual(state.subgoal_anchor["s1"], "doc1:ROOT")

        with patch("nav_control.plan_control", return_value=widen_decision):
            _apply_plan_control(
                ts, state, cfg, plan=plan, outputs=outputs, by_id={"s1": subgoal}, steps_out=None
            )
        self.assertIsNone(state.subgoal_anchor["s1"])

        with patch("nav_control.plan_control", return_value=widen_decision):
            _apply_plan_control(
                ts, state, cfg, plan=plan, outputs=outputs, by_id={"s1": subgoal}, steps_out=None
            )
        self.assertIn("s1", state.dropped_subgoal_ids)
        self.assertIn("s1", state.attempted_subgoal_ids)


if __name__ == "__main__":
    unittest.main()
