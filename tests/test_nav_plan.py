"""Unit tests for M2 retrieval planning (no LLM)."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
for source_dir in (ROOT / "src" / "realdata", ROOT / "src" / "nav"):
    if str(source_dir) not in sys.path:
        sys.path.insert(0, str(source_dir))

from nav_plan import (  # noqa: E402
    Activation,
    bind_slots,
    extract_plan_json,
    fallback_plan,
    is_always_active,
    parse_retrieval_plan,
    planning_char_limit,
    retrieval_query_language_mismatch,
    unbound_slots,
    validate_retrieval_plan,
)
from nav_types import NavConfig, Projection, SectionView  # noqa: E402


class TestNavPlan(unittest.TestCase):
    def test_bind_slots(self) -> None:
        text = "Find duties of {{entity}} under {{s1.law}}"
        out = bind_slots(text, {"entity": "operators", "law": "Act A"})
        self.assertEqual(out, "Find duties of operators under Act A")
        self.assertEqual(unbound_slots("keep {{missing}}"), ["missing"])

    def test_extract_plan_json_nested(self) -> None:
        prose = (
            'Here is the plan:\n'
            '{"reason":"ok","subgoals":[{"id":"s1","need":"a","retrieval_query":"a",'
            '"contract":{"kind":"single_fact"}}]}\n'
            "thanks"
        )
        obj = extract_plan_json(prose)
        self.assertIsInstance(obj, dict)
        self.assertEqual(obj["subgoals"][0]["id"], "s1")
        self.assertEqual(obj["subgoals"][0]["contract"]["kind"], "single_fact")

    def test_language_mismatch_is_script_relative(self) -> None:
        ref_zh = "第三章 印章的使用范围 第四章 用印审批程序"
        self.assertTrue(
            retrieval_query_language_mismatch(
                "What seal type is required for major contracts?",
                ref_zh,
            )
        )
        self.assertFalse(
            retrieval_query_language_mismatch("印章类型 重大合同 用印审批", ref_zh)
        )
        ref_en = "Chapter 3 Seal usage Chapter 4 Approval procedure"
        self.assertTrue(
            retrieval_query_language_mismatch("印章类型 重大合同", ref_en)
        )
        self.assertFalse(
            retrieval_query_language_mismatch("seal type approval procedure", ref_en)
        )

    def test_language_reference_ignores_action_chrome(self) -> None:
        from nav_plan import language_reference_text

        projection = Projection(
            doc_id="doc",
            scope=None,
            text="",
            visible_sections=[],
            id_to_section={"N1": "doc:L1"},
            tree_sections=[
                SectionView(
                    section_id="doc:L1",
                    level=0,
                    preview="collect=C1 dispatch=D1 [Hit]",
                    map_id="N1",
                    title="第三章 印章的使用范围",
                )
            ],
        )
        ref = language_reference_text(
            query="重大合同应使用哪类印章？",
            projection=projection,
        )
        # English chrome must not flip the reference to latin.
        self.assertFalse(
            retrieval_query_language_mismatch(
                "第三章 印章的使用范围 重大合同",
                ref,
            )
        )
        self.assertTrue(
            retrieval_query_language_mismatch(
                "What seal type is required for major contracts?",
                ref,
            )
        )

    def test_parse_shared_space_strips_scope_and_activation(self) -> None:
        obj = {
            "reason": "shared space",
            "map_coverage": "partial",
            "coverage_checklist": [
                {"id": "c1", "fact": "seal type"},
                {"id": "c2", "fact": "seal scope"},
            ],
            "subgoals": [
                {
                    "id": "s1",
                    "need": "find seal type",
                    "retrieval_query": "印章类型",
                    "produces": ["seal_type"],
                    "budget_share": 1,
                    "activation": {"mode": "always"},
                    "contract": {"kind": "single_fact"},
                    "route_hints": ["N1"],
                    "scope_filter": {"doc_ids": ["doc"]},
                },
                {
                    "id": "s2",
                    "need": "scope for seal",
                    "retrieval_query": "{{s1.seal_type}} 使用范围",
                    "budget_share": 1,
                    "activation": {"mode": "always"},
                    "contract": {"kind": "enumeration"},
                },
                {
                    "id": "s3",
                    "need": "finance seal fallback",
                    "retrieval_query": "财务专用章 使用范围",
                    "budget_share": 1,
                    "activation": {
                        "mode": "on",
                        "on": "s1",
                        "when": "seal is finance seal",
                    },
                    "contract": {"kind": "enumeration"},
                },
            ],
            "relations": [
                {"source": "s1", "target": "s2", "kind": "parent-child"},
                {"source": "s1", "target": "s3", "kind": "unrelated"},
            ],
        }
        projection = Projection(
            doc_id="doc",
            scope=None,
            text="",
            visible_sections=[],
            id_to_section={"N1": "doc:L1"},
            tree_sections=[
                SectionView(
                    section_id="doc:L1",
                    level=0,
                    preview="title",
                    map_id="N1",
                    title="title",
                )
            ],
        )
        plan = parse_retrieval_plan(obj, query="q", projection=projection)
        ok, why = validate_retrieval_plan(plan)
        self.assertTrue(ok, why)
        self.assertEqual(plan.map_coverage, "partial")
        self.assertEqual([c.id for c in plan.coverage_checklist], ["c1", "c2"])
        self.assertEqual(plan.subgoals[0].route_hints, [])
        self.assertEqual(plan.subgoals[0].scope_filter.doc_ids, [])
        self.assertIn("s1", plan.subgoals[1].depends_on)
        self.assertEqual(plan.subgoals[0].produces, ["seal_type"])
        # Activation forks are ignored; every subgoal stays always-active.
        self.assertEqual(plan.subgoals[2].activation.mode, "always")
        self.assertTrue(all(is_always_active(s) for s in plan.subgoals))
        self.assertAlmostEqual(
            sum(s.budget_share for s in plan.subgoals),
            1.0,
        )
        # unrelated edges dropped
        self.assertTrue(all(e.kind != "unrelated" for e in plan.relations))

    def test_slot_infers_depends_without_explicit_depends_on(self) -> None:
        obj = {
            "subgoals": [
                {
                    "id": "s1",
                    "need": "level",
                    "retrieval_query": "响应分级",
                    "contract": {"kind": "single_fact"},
                },
                {
                    "id": "s2",
                    "need": "duties",
                    "retrieval_query": "总指挥职责 {{s1.response_level}}",
                    "contract": {"kind": "enumeration"},
                },
            ]
        }
        plan = parse_retrieval_plan(obj, query="q")
        ok, why = validate_retrieval_plan(plan)
        self.assertTrue(ok, why)
        self.assertIn("s1", plan.subgoals[1].depends_on)
        self.assertEqual(plan.subgoals[0].produces, ["response_level"])

    def test_legacy_alternatives_ignored(self) -> None:
        obj = {
            "subgoals": [
                {
                    "id": "s1",
                    "need": "a",
                    "retrieval_query": "a",
                    "alternatives": [{"when": "missing", "use": "s1_alt"}],
                    "contract": {"kind": "single_fact"},
                },
                {
                    "id": "s1_alt",
                    "need": "alt",
                    "retrieval_query": "alt",
                    "contract": {"kind": "single_fact"},
                },
            ]
        }
        plan = parse_retrieval_plan(obj, query="q")
        ok, why = validate_retrieval_plan(plan)
        self.assertTrue(ok, why)
        alt = plan.subgoal_by_id()["s1_alt"]
        self.assertEqual(alt.activation.mode, "always")
        self.assertEqual(alt.activation.on, "")

    def test_multi_produces_trimmed(self) -> None:
        obj = {
            "subgoals": [
                {
                    "id": "s1",
                    "need": "a",
                    "retrieval_query": "a",
                    "produces": ["x", "y"],
                    "contract": {"kind": "single_fact"},
                }
            ]
        }
        plan = parse_retrieval_plan(obj, query="q")
        self.assertEqual(plan.subgoals[0].produces, ["x"])
        ok, why = validate_retrieval_plan(plan)
        self.assertTrue(ok, why)

    def test_cycle_back_edge_to_prefer_after(self) -> None:
        obj = {
            "subgoals": [
                {"id": "s1", "need": "a", "retrieval_query": "a", "depends_on": ["s2"]},
                {"id": "s2", "need": "b", "retrieval_query": "b", "depends_on": ["s1"]},
            ]
        }
        plan = parse_retrieval_plan(obj, query="q")
        ok, why = validate_retrieval_plan(plan)
        self.assertTrue(ok, why)
        d0 = plan.subgoals[0].depends_on
        d1 = plan.subgoals[1].depends_on
        self.assertFalse(bool(d0) and bool(d1))
        prefs = plan.subgoals[0].prefer_after + plan.subgoals[1].prefer_after
        self.assertTrue(prefs)

    def test_fallback_plan(self) -> None:
        plan = fallback_plan("what is X")
        ok, why = validate_retrieval_plan(plan)
        self.assertTrue(ok, why)
        self.assertTrue(plan.fallback)
        self.assertEqual(plan.subgoals[0].retrieval_query, "what is X")
        self.assertEqual(plan.subgoals[0].activation.mode, "always")
        self.assertEqual(len(plan.coverage_checklist), 1)
        self.assertEqual(plan.coverage_checklist[0].fact, "what is X")

    def test_planning_char_limit(self) -> None:
        cfg = NavConfig(map_char_limit=5000, planning_map_char_limit=10000)
        self.assertEqual(planning_char_limit(cfg), 10000)
        cfg2 = NavConfig(map_char_limit=5000, planning_map_char_limit=0)
        self.assertEqual(planning_char_limit(cfg2), 5000)

    def test_config_from_dict_keeps_planning_off(self) -> None:
        cfg = NavConfig.from_dict(
            {
                "map_char_limit": 5000,
                "enable_query_planning": False,
                "planning_map_char_limit": 10000,
            }
        )
        self.assertFalse(cfg.enable_query_planning)
        self.assertEqual(cfg.planning_map_char_limit, 10000)

    def test_thinking_mode_helpers(self) -> None:
        from agent_delivery.code.llm_config import (  # type: ignore
            chat_thinking_extra,
            resolve_thinking_mode,
        )

        self.assertEqual(resolve_thinking_mode("enabled"), "enabled")
        self.assertEqual(resolve_thinking_mode("nothink"), "disabled")
        self.assertEqual(resolve_thinking_mode("auto"), None)
        on = chat_thinking_extra(mode="enabled", model="deepseek-v4-flash")
        self.assertEqual(on["extra_body"]["thinking"]["type"], "enabled")
        off = chat_thinking_extra(mode="disabled", model="deepseek-v4-flash")
        self.assertEqual(off["extra_body"]["thinking"]["type"], "disabled")


if __name__ == "__main__":
    unittest.main()
