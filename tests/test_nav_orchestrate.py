"""Unit tests for M4/M5 orchestration + verify (no LLM navigate)."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch


ROOT = Path(__file__).resolve().parents[1]
for source_dir in (ROOT / "src" / "realdata", ROOT / "src" / "nav"):
    if str(source_dir) not in sys.path:
        sys.path.insert(0, str(source_dir))

from nav_orchestrate import (  # noqa: E402
    beacons_for_subgoal,
    cluster_by_locality,
    ready_subgoal_ids,
)
from nav_plan import Activation, Contract, RetrievalPlan, Subgoal  # noqa: E402
from nav_types import NavConfig, NavState, SubgoalResult  # noqa: E402
from nav_verify import (  # noqa: E402
    activation_when_holds,
    apply_bindings_from_result,
    extract_slots_heuristic,
    verify_contract,
)


class TestNavVerify(unittest.TestCase):
    def test_heuristic_extract_prefers_must_mention(self) -> None:
        sg = Subgoal(
            id="s1",
            need="seal",
            retrieval_query="印章类型",
            produces=["seal_type"],
            contract=Contract(kind="single_fact", must_mention=["法人章"]),
        )
        evidence = "本章规定对外重大合同应使用法人章办理用印。"
        slots = extract_slots_heuristic(sg, evidence, retrieval_query=sg.retrieval_query)
        self.assertEqual(slots.get("seal_type"), "法人章")

    def test_verify_missing_slot_is_rebind(self) -> None:
        sg = Subgoal(
            id="s1",
            need="a",
            retrieval_query="a",
            produces=["entity"],
            contract=Contract(kind="single_fact"),
        )
        out = verify_contract(
            sg, extracted={}, evidence_text="some evidence without extract", confidence=0.0
        )
        self.assertEqual(out.verdict, "REBIND")
        self.assertFalse(out.result.satisfied)

    def test_verify_enumeration_cardinality(self) -> None:
        sg = Subgoal(
            id="s1",
            need="list",
            retrieval_query="duties",
            produces=["items"],
            contract=Contract(kind="enumeration", cardinality=3),
        )
        out = verify_contract(
            sg,
            extracted={"items": "a、b"},
            evidence_text="a、b",
            confidence=1.0,
        )
        self.assertEqual(out.verdict, "RETRY_SAME_REGION")
        out_ok = verify_contract(
            sg,
            extracted={"items": "a、b、c"},
            evidence_text="a、b、c",
            confidence=1.0,
        )
        self.assertEqual(out_ok.verdict, "SATISFIED")

    def test_activation_when_substring_and_empty(self) -> None:
        self.assertTrue(
            activation_when_holds(
                "",
                parent_extracted={"seal_type": "法人章"},
                parent_satisfied=True,
            )
        )
        self.assertTrue(
            activation_when_holds(
                "seal is 财务专用章",
                parent_extracted={"seal_type": "财务专用章"},
                parent_satisfied=True,
            )
        )
        self.assertFalse(
            activation_when_holds(
                "seal is 财务专用章",
                parent_extracted={"seal_type": "法人章"},
                parent_satisfied=True,
            )
        )
        # No token-bag overlap: shared English chrome alone must not activate.
        self.assertFalse(
            activation_when_holds(
                "seal type is financial",
                parent_extracted={"seal_type": "法人章 corporate seal"},
                parent_satisfied=True,
            )
        )
        self.assertFalse(
            activation_when_holds(
                "anything",
                parent_extracted={"seal_type": "法人章"},
                parent_satisfied=False,
            )
        )

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

    def test_retry_then_satisfied_marks_attempted(self) -> None:
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
                # First pass: evidence without required mention → WIDEN/RETRY path
                state.collected.append((_Chunk("本章规定用印审批程序。"), 1.0))
                state.collected_section_ids.add("doc:L0")
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
    def test_ready_respects_deps_activation_and_slots(self) -> None:
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
                    activation=Activation(mode="on", on="s1", when="财务专用章"),
                ),
            ]
        )
        ready0 = ready_subgoal_ids(
            plan, satisfied=set(), activated=set(), bindings={}
        )
        self.assertEqual(ready0, ["s1"])
        ready1 = ready_subgoal_ids(
            plan,
            satisfied={"s1"},
            activated=set(),
            bindings={"s1.seal_type": "法人章", "seal_type": "法人章"},
        )
        self.assertEqual(ready1, ["s2"])
        ready2 = ready_subgoal_ids(
            plan,
            satisfied={"s1"},
            activated={"s3"},
            bindings={"s1.seal_type": "法人章", "seal_type": "法人章"},
        )
        self.assertEqual(ready2, ["s2", "s3"])

    def test_cluster_by_locality_union(self) -> None:
        ts = MagicMock()

        def rel(sid, doc_id):
            tree = {
                "doc:L2": ({"doc:L1"}, set()),
                "doc:L3": ({"doc:L1"}, set()),
                "doc:L9": ({"doc:L8"}, set()),
            }
            return tree.get(sid, (set(), set()))

        ts.section_relation_ids = rel
        state = NavState(
            doc_id="doc",
            query="q",
            hit_sources={
                "doc:L2": ["s1"],
                "doc:L3": ["s2"],
                "doc:L9": ["s3"],
            },
        )
        clusters = cluster_by_locality(
            ts, state, ["s1", "s2", "s3"], k=2, enabled=True
        )
        # s1+s2 share ancestor L1; s3 separate
        flat = {frozenset(c) for c in clusters}
        self.assertIn(frozenset({"s1", "s2"}), flat)
        self.assertIn(frozenset({"s3"}), flat)
        solo = cluster_by_locality(
            ts, state, ["s1", "s2", "s3"], k=2, enabled=False
        )
        self.assertEqual(solo, [["s1"], ["s2"], ["s3"]])

    def test_beacons_from_hit_sources(self) -> None:
        state = NavState(
            doc_id="doc",
            query="q",
            hit_sources={"doc:L1": ["s1"], "doc:L2": ["s1", "s2"]},
        )
        self.assertEqual(
            set(beacons_for_subgoal(state, "s1", k=10)),
            {"doc:L1", "doc:L2"},
        )

    def test_config_flags_default_off(self) -> None:
        cfg = NavConfig.from_dict({})
        self.assertFalse(cfg.enable_plan_orchestration)
        self.assertFalse(cfg.enable_locality_merge)
        self.assertFalse(cfg.enable_contract_verify)
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


if __name__ == "__main__":
    unittest.main()
