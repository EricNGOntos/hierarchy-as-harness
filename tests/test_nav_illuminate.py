"""Unit tests for M3 multi-source illumination / fold merge (no LLM)."""

from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch


ROOT = Path(__file__).resolve().parents[1]
for source_dir in (ROOT / "src" / "realdata", ROOT / "src" / "nav"):
    if str(source_dir) not in sys.path:
        sys.path.insert(0, str(source_dir))

from nav_actions import format_actionable_map_observation  # noqa: E402
from nav_illuminate import (  # noqa: E402
    apply_illumination_to_state,
    bindable_retrieval_queries,
    fold_participant_ids,
    fold_weights_for_plan,
    illuminate_from_plan,
    refresh_fold_from_subgoal_scores,
)
from nav_map_scores import (  # noqa: E402
    merge_score_maps,
    select_map_highlights_multi,
)
from nav_plan import Activation, RetrievalPlan, Subgoal  # noqa: E402
from nav_projection import build_map, format_hit_tag  # noqa: E402
from nav_types import (  # noqa: E402
    ActionKind,
    LegalAction,
    NavConfig,
    NavState,
    Projection,
    SectionView,
)


class _FakeTS:
    def __init__(self, tree: dict[str, dict]) -> None:
        self.tree = tree
        self._idx = MagicMock()
        self._idx._node_to_doc_line = {sid: ("doc", 0) for sid in tree}

    def sections_for_doc(self, doc_id: str):
        del doc_id
        return [sid for sid, node in self.tree.items() if int(node["level"]) == 1]

    def get_structure(self, section_id: str) -> dict:
        node = self.tree[section_id]
        return {
            "section_id": section_id,
            "level": node["level"],
            "preview": node["title"],
            "n_lines": 3,
            "n_chunks": 2,
            "children": [
                {
                    "section_id": cid,
                    "preview": self.tree[cid]["title"],
                    "level": self.tree[cid]["level"],
                }
                for cid in node["children"]
            ],
            "exists": True,
        }

    def _children_for_section_path(self, section_id: str, doc_id: str, limit: int = 24):
        del doc_id
        return self.get_structure(section_id)["children"][:limit]


TREE = {
    "doc:L1": {"title": "Chapter One", "level": 1, "children": ["doc:L2"]},
    "doc:L2": {"title": "Seal Scope", "level": 2, "children": []},
    "doc:L10": {"title": "Chapter Two", "level": 1, "children": ["doc:L11"]},
    "doc:L11": {"title": "Approval Procedure", "level": 2, "children": []},
}


class TestNavIlluminate(unittest.TestCase):
    def test_merge_score_maps_max_weighted(self) -> None:
        per = {
            "s1": {"a": 1.0, "b": 0.5},
            "s2": {"a": 0.4, "c": 2.0},
        }
        merged = merge_score_maps(per, weights={"s1": 1.0, "s2": 0.5})
        self.assertAlmostEqual(merged["a"], 1.0)  # max(1.0, 0.2)
        self.assertAlmostEqual(merged["b"], 0.5)
        self.assertAlmostEqual(merged["c"], 1.0)  # 0.5 * 2.0

    def test_merge_ignores_nonpositive_weight(self) -> None:
        per = {"s1": {"a": 9.0}, "s2": {"a": 1.0}}
        merged = merge_score_maps(per, weights={"s1": 0.0, "s2": 1.0})
        self.assertAlmostEqual(merged["a"], 1.0)

    def test_select_highlights_multi_provenance(self) -> None:
        per = {
            "s1": {"doc:L1": 5.0, "doc:L2": 4.0, "doc:L9": 0.1},
            "s2": {"doc:L3": 6.0, "doc:L1": 3.0},
        }
        hits, sources = select_map_highlights_multi(per, k=1, active_ids=["s1", "s2"])
        self.assertEqual(set(hits), {"doc:L1", "doc:L3"})
        self.assertEqual(sources["doc:L1"], ["s1"])
        self.assertEqual(sources["doc:L3"], ["s2"])

    def test_select_highlights_multi_shared_section(self) -> None:
        per = {
            "s1": {"doc:L1": 5.0},
            "s2": {"doc:L1": 4.0},
        }
        hits, sources = select_map_highlights_multi(per, k=1, active_ids=["s1", "s2"])
        self.assertEqual(hits, ["doc:L1"])
        self.assertEqual(sources["doc:L1"], ["s1", "s2"])

    def test_format_hit_tag(self) -> None:
        self.assertEqual(format_hit_tag(is_highlight=False), "")
        self.assertEqual(format_hit_tag(is_highlight=True), " [Hit]")
        self.assertEqual(
            format_hit_tag(is_highlight=True, hit_sources=["s1", "s3"]),
            " [Hit:s1,s3]",
        )

    def test_observation_renders_multi_hit_tag(self) -> None:
        proj = Projection(
            doc_id="doc",
            scope=None,
            text="",
            visible_sections=[],
            map_mode=True,
            tree_sections=[
                SectionView(
                    section_id="doc:L2",
                    level=1,
                    preview="",
                    map_id="N2",
                    title="Seal Scope",
                    n_chunks=2,
                    is_highlight=True,
                    hit_sources=["s1", "s2"],
                )
            ],
            highlight_ids=["doc:L2"],
        )
        actions = [
            LegalAction(
                action_id="C1",
                kind=ActionKind.COLLECT,
                section_id="doc:L2",
                label="Seal Scope",
            )
        ]
        obs = format_actionable_map_observation(proj, actions)
        self.assertIn("[Hit:s1,s2]", obs)
        self.assertNotIn("[Hit] ", obs)

    def test_build_map_propagates_hit_sources(self) -> None:
        os.environ["NAV_MAP_MODE"] = "1"
        try:
            ts = _FakeTS(TREE)
            cfg = NavConfig(map_mode=True, map_char_limit=5000, map_children_limit=100)
            proj = build_map(
                ts,
                doc_id="doc",
                query="seal",
                scope=None,
                config=cfg,
                map_scores={"doc:L2": 10.0, "doc:L11": 8.0},
                highlight_ids=["doc:L2", "doc:L11"],
                hit_sources={"doc:L2": ["s1"], "doc:L11": ["s2"]},
            )
            by_sid = {v.section_id: v for v in proj.tree_sections}
            self.assertEqual(by_sid["doc:L2"].hit_sources, ["s1"])
            self.assertEqual(by_sid["doc:L11"].hit_sources, ["s2"])
            self.assertIn("[Hit:s1]", proj.text)
            self.assertIn("[Hit:s2]", proj.text)
        finally:
            os.environ.pop("NAV_MAP_MODE", None)

    def test_bindable_and_participants_skip_unbound_and_conditional(self) -> None:
        plan = RetrievalPlan(
            subgoals=[
                Subgoal(
                    id="s1",
                    need="type",
                    retrieval_query="印章类型",
                    budget_share=0.6,
                    activation=Activation(mode="always"),
                ),
                Subgoal(
                    id="s2",
                    need="proc",
                    retrieval_query="{{s1.seal_type}} 审批",
                    budget_share=0.4,
                    activation=Activation(mode="always"),
                ),
                Subgoal(
                    id="s3",
                    need="finance",
                    retrieval_query="财务专用章 使用范围",
                    budget_share=0.3,
                    activation=Activation(mode="on", on="s1", when="finance"),
                ),
            ]
        )
        bindable = bindable_retrieval_queries(plan, {})
        self.assertIn("s1", bindable)
        self.assertNotIn("s2", bindable)
        self.assertIn("s3", bindable)
        parts = fold_participant_ids(
            plan, bindable=bindable, satisfied=set(), activated=set()
        )
        self.assertEqual(parts, ["s1"])
        parts2 = fold_participant_ids(
            plan, bindable=bindable, satisfied=set(), activated={"s3"}
        )
        self.assertEqual(parts2, ["s1", "s3"])
        w = fold_weights_for_plan(plan, parts2, goal_conditioned=True)
        self.assertAlmostEqual(w["s1"], 0.6)
        self.assertAlmostEqual(w["s3"], 0.3)

    def test_slot_binding_unlocks_dependent_subgoal(self) -> None:
        plan = RetrievalPlan(
            subgoals=[
                Subgoal(
                    id="s1",
                    need="type",
                    retrieval_query="印章类型",
                    budget_share=0.5,
                    activation=Activation(),
                ),
                Subgoal(
                    id="s2",
                    need="proc",
                    retrieval_query="{{s1.seal_type}} 用印审批程序",
                    budget_share=0.5,
                    activation=Activation(),
                ),
            ]
        )
        before = bindable_retrieval_queries(plan, {})
        self.assertNotIn("s2", before)
        after = bindable_retrieval_queries(plan, {"s1.seal_type": "法人章"})
        self.assertEqual(after["s2"], "法人章 用印审批程序")
        parts = fold_participant_ids(
            plan, bindable=after, satisfied=set(), activated=set()
        )
        self.assertEqual(parts, ["s1", "s2"])

    def test_route_hints_enter_hit_sources(self) -> None:
        plan = RetrievalPlan(
            subgoals=[
                Subgoal(
                    id="s1",
                    need="a",
                    retrieval_query="a",
                    budget_share=1.0,
                    route_hints=["doc:L99"],
                    activation=Activation(),
                )
            ]
        )
        state = NavState(doc_id="doc", query="q", retrieval_plan=plan)
        apply_illumination_to_state(
            state,
            subgoal_map_scores={"s1": {"doc:L1": 1.0}},
            subgoal_unit_scores={"s1": {"doc:L1": 1.0}},
            participant_ids=["s1"],
            weights={"s1": 1.0},
            collect_top_k=1,
            route_hint_hits={"doc:L99": ["s1"]},
        )
        self.assertIn("doc:L99", state.highlight_ids)
        self.assertEqual(state.hit_sources["doc:L99"], ["s1"])

    def test_equal_weights_when_goal_conditioned_off(self) -> None:
        plan = RetrievalPlan(
            subgoals=[
                Subgoal(id="s1", need="a", retrieval_query="a", budget_share=0.9),
                Subgoal(id="s2", need="b", retrieval_query="b", budget_share=0.1),
            ]
        )
        w = fold_weights_for_plan(plan, ["s1", "s2"], goal_conditioned=False)
        self.assertEqual(w, {"s1": 1.0, "s2": 1.0})

    def test_apply_and_refresh_satisfaction_decay(self) -> None:
        plan = RetrievalPlan(
            subgoals=[
                Subgoal(
                    id="s1",
                    need="a",
                    retrieval_query="a",
                    budget_share=0.5,
                    activation=Activation(),
                ),
                Subgoal(
                    id="s2",
                    need="b",
                    retrieval_query="b",
                    budget_share=0.5,
                    activation=Activation(),
                ),
            ]
        )
        state = NavState(doc_id="doc", query="q", retrieval_plan=plan)
        apply_illumination_to_state(
            state,
            subgoal_map_scores={
                "s1": {"x": 1.0, "y": 0.1},
                "s2": {"x": 0.2, "z": 2.0},
            },
            subgoal_unit_scores={
                "s1": {"x": 1.0},
                "s2": {"z": 2.0},
            },
            participant_ids=["s1", "s2"],
            weights={"s1": 1.0, "s2": 1.0},
            collect_top_k=1,
        )
        self.assertAlmostEqual(state.map_scores["x"], 1.0)
        self.assertAlmostEqual(state.map_scores["z"], 2.0)
        self.assertIn("s1", state.hit_sources.get("x", []))
        self.assertIn("s2", state.hit_sources.get("z", []))

        state.satisfied_subgoal_ids.add("s1")
        cfg = NavConfig(enable_goal_conditioned_folding=True, collect_top_k=1)
        detail = refresh_fold_from_subgoal_scores(state, cfg)
        self.assertIsNotNone(detail)
        self.assertEqual(state.active_subgoal_ids, ["s2"])
        self.assertNotIn("y", state.map_scores)
        self.assertAlmostEqual(state.map_scores["z"], 2.0 * 0.5)

    def test_illuminate_from_plan_off_or_missing_is_noop(self) -> None:
        state = NavState(doc_id="doc", query="q")
        cfg = NavConfig(enable_per_subgoal_illumination=True)
        self.assertIsNone(illuminate_from_plan(None, state, cfg))
        state.retrieval_plan = RetrievalPlan(
            subgoals=[Subgoal(id="s1", need="a", retrieval_query="a")]
        )
        cfg_off = NavConfig(enable_per_subgoal_illumination=False)
        self.assertIsNone(illuminate_from_plan(None, state, cfg_off))

    def test_illuminate_from_plan_wires_multi_source(self) -> None:
        plan = RetrievalPlan(
            subgoals=[
                Subgoal(
                    id="s1",
                    need="seal",
                    retrieval_query="印章使用范围",
                    budget_share=0.5,
                    activation=Activation(),
                ),
                Subgoal(
                    id="s2",
                    need="proc",
                    retrieval_query="用印审批程序",
                    budget_share=0.5,
                    activation=Activation(),
                ),
            ]
        )
        state = NavState(doc_id="doc", query="q", retrieval_plan=plan)
        cfg = NavConfig(
            enable_per_subgoal_illumination=True,
            enable_goal_conditioned_folding=True,
            collect_top_k=1,
        )
        fake_map = {
            "s1": {"doc:L2": 3.0, "doc:L11": 0.1},
            "s2": {"doc:L11": 4.0, "doc:L2": 0.2},
        }
        fake_unit = {
            "s1": {"doc:L2": 3.0},
            "s2": {"doc:L11": 4.0},
        }
        with patch(
            "nav_illuminate.compute_multi_query_map_scores",
            return_value=(fake_map, fake_unit),
        ):
            detail = illuminate_from_plan(MagicMock(), state, cfg)
        self.assertIsNotNone(detail)
        assert detail is not None
        self.assertEqual(set(detail["participant_ids"]), {"s1", "s2"})
        self.assertAlmostEqual(state.map_scores["doc:L2"], 3.0 * 0.5)
        self.assertAlmostEqual(state.map_scores["doc:L11"], 4.0 * 0.5)
        self.assertEqual(state.hit_sources["doc:L2"], ["s1"])
        self.assertEqual(state.hit_sources["doc:L11"], ["s2"])

    def test_config_flags_default_off(self) -> None:
        cfg = NavConfig.from_dict({})
        self.assertFalse(cfg.enable_per_subgoal_illumination)
        self.assertFalse(cfg.enable_goal_conditioned_folding)


if __name__ == "__main__":
    unittest.main()
