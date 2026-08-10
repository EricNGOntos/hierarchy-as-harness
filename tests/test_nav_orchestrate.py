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
from nav_orchestrate import ready_subgoal_ids  # noqa: E402
from nav_plan import Contract, RetrievalPlan, Subgoal  # noqa: E402
from nav_types import NavConfig, NavState  # noqa: E402
from nav_verify import (  # noqa: E402
    apply_bindings_from_result,
    demanded_slot_names,
    extract_slots_heuristic,
)


class _Chunk:
    def __init__(self, text: str, node_id: str = "n1") -> None:
        self.text = text
        self.node_id = node_id


def _checklist_cfg(**overrides) -> NavConfig:
    base = dict(mode="checklist", map_char_limit=5000, subgoal_max_attempts=2)
    base.update(overrides)
    return NavConfig(**base)


def _control_accept_if_evidence(*, plan, wave_outputs):
    per = {}
    for item in wave_outputs:
        sid = item["subgoal_id"]
        chars = int(getattr(item["result"], "chars_used", 0) or 0)
        per[sid] = SubgoalDecision(
            subgoal_id=sid, decision="accept" if chars > 0 else "drop"
        )
    return PlanControlDecision(per_subgoal=per, global_action="continue")


def _fake_harvest_by_query(query_to_text: dict[str, str]):
    def fake_harvest(ts, state, config, *, subgoal, entry_scope, query, steps_out=None):
        del ts, config, subgoal, entry_scope, steps_out
        for key, text in query_to_text.items():
            if key in (query or ""):
                state.collected.append((_Chunk(text, node_id=f"n-{key}"), 1.0))
                state.collected_section_ids.add(f"doc:{key}")
                break
        return SimpleNamespace(
            n_policy_calls=1,
            visited_section_ids=[],
            max_depth_hit=False,
            reason="ok",
        )

    return fake_harvest


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

    def test_empty_evidence_dropped_by_plan_control(self) -> None:
        """Checklist harvest is one-shot per wave; empty → control drops (no silent accept)."""
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
        cfg = _checklist_cfg()

        with patch("nav_harvest.harvest", side_effect=_fake_harvest_by_query({})), patch(
            "nav_control.plan_control",
            side_effect=lambda *a, **k: _control_accept_if_evidence(
                plan=k["plan"], wave_outputs=k["wave_outputs"]
            ),
        ):
            execute_plan(MagicMock(), state, cfg, steps_out=[], episode_query="q")
        self.assertIn("s1", state.dropped_subgoal_ids)
        self.assertIn("s1", state.attempted_subgoal_ids)
        self.assertNotIn("s1", state.satisfied_subgoal_ids)

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
        ready0 = ready_subgoal_ids(plan, satisfied=set())
        self.assertEqual(ready0, ["s1", "s3"])
        ready1 = ready_subgoal_ids(plan, satisfied={"s1"})
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
            plan, satisfied=set(), dropped=set(), attempted={"s1"}
        )
        self.assertEqual(still_blocked, [])
        unblocked = ready_subgoal_ids(
            plan, satisfied=set(), dropped={"s1"}, attempted={"s1"}
        )
        self.assertEqual(unblocked, ["s2"])

    def test_same_wave_subgoals_run_own_queries(self) -> None:
        """Independent subgoals never share one harvest call or one result."""
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
        cfg = _checklist_cfg()
        calls: list[str] = []

        def fake_harvest(ts, state, config, *, subgoal, entry_scope, query, steps_out=None):
            calls.append(query)
            if "法人章" in query:
                state.collected.append((_Chunk("对外重大合同应使用法人章。"), 1.0))
                state.collected_section_ids.add("doc:L1")
            return SimpleNamespace(
                n_policy_calls=1, visited_section_ids=[], max_depth_hit=False, reason="ok"
            )

        with patch("nav_harvest.harvest", side_effect=fake_harvest), patch(
            "nav_control.plan_control",
            side_effect=lambda *a, **k: _control_accept_if_evidence(
                plan=k["plan"], wave_outputs=k["wave_outputs"]
            ),
        ):
            execute_plan(MagicMock(), state, cfg, steps_out=[], episode_query="q")

        self.assertTrue(any("法人章" in c and "档案保管" not in c for c in calls))
        self.assertTrue(any("档案保管" in c and "法人章" not in c for c in calls))
        self.assertIn("s1", state.satisfied_subgoal_ids)
        self.assertNotIn("s2", state.satisfied_subgoal_ids)

    def test_config_mode_defaults_navigate(self) -> None:
        cfg = NavConfig.from_dict({})
        self.assertEqual(cfg.mode, "navigate")
        self.assertFalse(cfg.is_checklist)
        self.assertEqual(cfg.max_replans, 1)
        self.assertEqual(cfg.max_waves, 0)

    def test_execute_plan_wave_order_with_mocked_harvest(self) -> None:
        from nav_orchestrate import execute_plan

        plan = RetrievalPlan(
            subgoals=[
                Subgoal(
                    id="s1",
                    need="type",
                    retrieval_query="印章类型 法人章",
                    produces=["seal_type"],
                    contract=Contract(kind="single_fact", must_mention=["法人章"]),
                ),
                Subgoal(
                    id="s2",
                    need="proc",
                    retrieval_query="{{s1.seal_type}} 用印审批",
                    depends_on=["s1"],
                    produces=["proc"],
                    contract=Contract(kind="single_fact"),
                ),
            ]
        )
        state = NavState(doc_id="doc", query="q", retrieval_plan=plan)
        cfg = _checklist_cfg()
        calls: list[str] = []

        def fake_harvest(ts, state, config, *, subgoal, entry_scope, query, steps_out=None):
            calls.append(query)
            if "印章类型" in query:
                state.collected.append((_Chunk("对外重大合同应使用法人章。"), 1.0))
                state.collected_section_ids.add("doc:L1")
            else:
                state.collected.append((_Chunk("用印审批程序见第四章。"), 1.0))
                state.collected_section_ids.add("doc:L2")
            return SimpleNamespace(
                n_policy_calls=1, visited_section_ids=[], max_depth_hit=False, reason="ok"
            )

        with patch("nav_harvest.harvest", side_effect=fake_harvest), patch(
            "nav_control.plan_control",
            side_effect=lambda *a, **k: _control_accept_if_evidence(
                plan=k["plan"], wave_outputs=k["wave_outputs"]
            ),
        ):
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
        cfg = _checklist_cfg()

        with patch(
            "nav_harvest.harvest",
            side_effect=_fake_harvest_by_query({"印章类型": "对外重大合同应使用法人章。"}),
        ), patch(
            "nav_control.plan_control",
            side_effect=lambda *a, **k: _control_accept_if_evidence(
                plan=k["plan"], wave_outputs=k["wave_outputs"]
            ),
        ), patch("nav_verify.extract_slots_llm") as llm:
            execute_plan(MagicMock(), state, cfg, steps_out=[], episode_query="q")
        llm.assert_not_called()
        self.assertEqual(state.slot_bindings, {})

    def test_widen_asks_plan_to_rewrite_query_then_drops_at_max_attempts(self) -> None:
        """Widen keeps the subgoal unsettled and hands control's gap to PLAN,
        whose rewritten query overrides the planned one for the next harvest.
        Only drops once subgoal_attempt_counts >= subgoal_max_attempts.

        (execute_plan increments attempt_counts before calling this helper.)
        """
        from nav_orchestrate import _apply_plan_control

        subgoal = Subgoal(id="s1", need="x", retrieval_query="原查询")
        plan = RetrievalPlan(subgoals=[subgoal])
        state = NavState(doc_id="doc1", query="x", retrieval_plan=plan)
        cfg = NavConfig(subgoal_max_attempts=3)
        ts = MagicMock()
        outputs = [
            {
                "subgoal_id": "s1",
                "result": SimpleNamespace(
                    satisfied=False,
                    chars_used=0,
                    gap="empty_evidence",
                    collected_section_ids=["sec-a", "sec-a-child"],
                    explicit_collect_ids=["sec-a"],
                ),
                "new_chunks": [],
            }
        ]
        widen_decision = PlanControlDecision(
            per_subgoal={
                "s1": SubgoalDecision(
                    subgoal_id="s1", decision="widen", note="difficulties missing"
                )
            },
            global_action="continue",
        )

        def _widen_wave(refined: str) -> MagicMock:
            with patch(
                "nav_control.plan_control", return_value=widen_decision
            ), patch(
                "nav_orchestrate.refine_subgoal_query", return_value=refined
            ) as refine:
                _apply_plan_control(
                    ts,
                    state,
                    cfg,
                    plan=plan,
                    outputs=outputs,
                    by_id={"s1": subgoal},
                    steps_out=None,
                )
            return refine

        state.subgoal_attempt_counts["s1"] = 1
        refine = _widen_wave("勘察设计难点")
        self.assertNotIn("s1", state.dropped_subgoal_ids)
        self.assertNotIn("s1", state.attempted_subgoal_ids)
        # Control's note reaches PLAN as the gap, alongside the failed query
        # and this wave's selected section ids.
        self.assertEqual(refine.call_args.kwargs["gap"], "difficulties missing")
        self.assertEqual(refine.call_args.kwargs["previous_query"], "原查询")
        self.assertEqual(refine.call_args.kwargs["selected_section_ids"], ["sec-a"])
        self.assertEqual(state.subgoal_widen_gaps.get("s1"), "difficulties missing")
        self.assertEqual(state.subgoal_refined_queries.get("s1"), "勘察设计难点")

        # A second widen rewrites from the last rewrite, not the planned query.
        state.subgoal_attempt_counts["s1"] = 2
        refine = _widen_wave("枢纽布置 地质条件")
        self.assertNotIn("s1", state.dropped_subgoal_ids)
        self.assertEqual(refine.call_args.kwargs["previous_query"], "勘察设计难点")
        self.assertEqual(state.subgoal_refined_queries.get("s1"), "枢纽布置 地质条件")

        state.subgoal_attempt_counts["s1"] = 3
        _widen_wave("never used")
        self.assertIn("s1", state.dropped_subgoal_ids)
        self.assertIn("s1", state.attempted_subgoal_ids)
        self.assertNotIn("s1", state.subgoal_widen_gaps)
        self.assertNotIn("s1", state.subgoal_refined_queries)

    def test_harvest_always_relights_map_with_retrieval_query(self) -> None:
        """Every harvest (wave-1 planned query or later refine) re-scores the
        map against the retrieval_query in force, then restores episode lighting."""
        from nav_orchestrate import _execute_subgoal_harvest_once

        subgoal = Subgoal(id="s1", need="x", retrieval_query="原查询")
        plan = RetrievalPlan(subgoals=[subgoal])
        state = NavState(doc_id="doc1", query="x", retrieval_plan=plan)
        state.map_scores = {"a": 1.0}
        state.unit_scores = {"a": 1.0}
        state.highlight_ids = ["a"]
        cfg = _checklist_cfg()
        seen: dict = {}

        def _fake_harvest(ts_arg, st, config, *, subgoal, entry_scope, query, steps_out):
            seen["query"] = query
            seen["map_scores"] = dict(st.map_scores)
            seen["highlight_ids"] = list(st.highlight_ids)
            return SimpleNamespace(
                n_policy_calls=1,
                visited_section_ids=[],
                max_depth_hit=False,
                reason="",
                search_assets=[],
            )

        with patch("nav_harvest.harvest", side_effect=_fake_harvest), patch(
            "nav_map_scores.relight_map_for_query",
            return_value=({"b": 2.0}, {"b": 2.0}, ["b"]),
        ) as relight:
            _execute_subgoal_harvest_once(
                MagicMock(), state, cfg, plan, subgoal, steps_out=None
            )

        self.assertEqual(seen["query"], "原查询")
        self.assertEqual(relight.call_args.kwargs["query"], "原查询")
        self.assertEqual(seen["map_scores"], {"b": 2.0})
        self.assertEqual(seen["highlight_ids"], ["b"])
        self.assertEqual(state.map_scores, {"a": 1.0})
        self.assertEqual(state.highlight_ids, ["a"])

        # Refined override also relights against the rewritten query.
        state.subgoal_refined_queries["s1"] = "勘察设计难点"
        with patch("nav_harvest.harvest", side_effect=_fake_harvest), patch(
            "nav_map_scores.relight_map_for_query",
            return_value=({"c": 3.0}, {"c": 3.0}, ["c"]),
        ) as relight:
            out = _execute_subgoal_harvest_once(
                MagicMock(), state, cfg, plan, subgoal, steps_out=None
            )
        self.assertEqual(seen["query"], "勘察设计难点")
        self.assertEqual(relight.call_args.kwargs["query"], "勘察设计难点")
        self.assertEqual(out["harvest"]["refined_query"], "勘察设计难点")
        self.assertEqual(state.map_scores, {"a": 1.0})

if __name__ == "__main__":
    unittest.main()
