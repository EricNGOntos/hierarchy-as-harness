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

from nav_actions import build_legal_actions, format_actionable_map_observation  # noqa: E402
from nav_map_scores import select_map_highlights  # noqa: E402
from nav_projection import build_map, build_projection  # noqa: E402
from nav_types import (  # noqa: E402
    ActionKind,
    NavConfig,
    NavState,
    map_mode_enabled,
)


class _FakeTS:
    def __init__(self, tree: dict[str, dict]) -> None:
        self.tree = tree
        self._idx = MagicMock()
        self._idx._node_to_doc_line = {
            sid: ("doc", 0) for sid in tree
        }
        self._idx.section_summaries = []

    def sections_for_doc(self, doc_id: str):
        del doc_id
        return ["doc:L1", "doc:L10"]

    def get_structure(self, section_id: str) -> dict:
        node = self.tree[section_id]
        return {
            "section_id": section_id,
            "level": node["level"],
            "preview": node["title"],
            "n_lines": 3,
            "n_chunks": 2,
            "children": [
                {"section_id": cid, "preview": self.tree[cid]["title"], "level": self.tree[cid]["level"]}
                for cid in node["children"]
            ],
            "exists": True,
        }

    def _children_for_section_path(self, section_id: str, doc_id: str, limit: int = 24):
        del doc_id
        children = self.get_structure(section_id)["children"]
        return children[:limit]

    def _synthetic_doc_id(self, section_id: str):
        return "doc" if section_id.startswith("doc:") else None


TREE = {
    "doc:L1": {"title": "Chapter One", "level": 1, "children": ["doc:L2", "doc:L5"]},
    "doc:L2": {"title": "Section 1.1", "level": 2, "children": ["doc:L3"]},
    "doc:L3": {"title": "Deep Leaf Detail", "level": 3, "children": []},
    "doc:L5": {"title": "Section 1.2", "level": 2, "children": []},
    "doc:L10": {"title": "Chapter Two", "level": 1, "children": ["doc:L11"]},
    "doc:L11": {"title": "Section 2.1", "level": 2, "children": []},
}


class MapModeUnitTests(unittest.TestCase):
    def setUp(self) -> None:
        os.environ["NAV_MAP_MODE"] = "1"
        self.ts = _FakeTS(TREE)
        self.cfg = NavConfig(map_mode=True, map_char_limit=5000, map_children_limit=100)

    def tearDown(self) -> None:
        os.environ.pop("NAV_MAP_MODE", None)

    def test_map_mode_env(self) -> None:
        self.assertTrue(map_mode_enabled(self.cfg))

    def test_build_map_full_depth_no_preview(self) -> None:
        proj = build_map(
            self.ts,
            doc_id="doc",
            query="Deep Leaf Detail",
            scope=None,
            config=self.cfg,
            map_scores={"doc:L3": 10.0, "doc:L2": 5.0, "doc:L1": 4.0},
            highlight_ids=["doc:L3"],
        )
        self.assertTrue(proj.map_mode)
        self.assertIn("[N", proj.text)
        self.assertNotIn("Preview:", proj.text)
        # Deep leaf must be visible without EXPAND chain.
        ids = {v.section_id for v in proj.visible_sections}
        self.assertIn("doc:L3", ids)
        self.assertTrue(proj.id_to_section)
        # Every visible row has a map id.
        self.assertTrue(all(v.map_id.startswith("N") for v in proj.visible_sections))
        leaf = next(v for v in proj.visible_sections if v.section_id == "doc:L3")
        self.assertEqual(leaf.score, 10.0)
        self.assertTrue(leaf.is_highlight)
        self.assertIn("[Hit]", proj.text)

    def test_build_projection_routes_to_map(self) -> None:
        proj = build_projection(
            self.ts,
            doc_id="doc",
            query="Chapter",
            scope=None,
            config=self.cfg,
        )
        self.assertTrue(proj.map_mode)

    def test_map_budget_hide_on_tiny_budget(self) -> None:
        cfg = NavConfig(map_mode=True, map_char_limit=180, collect_top_k=1)
        scores = {
            "doc:L3": 10.0,
            "doc:L2": 9.0,
            "doc:L1": 8.0,
            "doc:L5": 0.01,
            "doc:L11": 0.02,
            "doc:L10": 0.02,
        }
        proj = build_map(
            self.ts,
            doc_id="doc",
            query="Deep Leaf Detail",
            scope=None,
            config=cfg,
            map_scores=scores,
            highlight_ids=["doc:L3"],
        )
        ids = {v.section_id for v in proj.tree_sections}
        # Highlight + ancestor spine kept.
        self.assertIn("doc:L3", ids)
        self.assertIn("doc:L1", ids)
        self.assertIn("doc:L2", ids)
        # Low-score chapter not on the spine should be hidden under tiny budget.
        self.assertNotIn("doc:L10", ids)
        self.assertNotIn("... [projection truncated]", proj.text)
        actions = build_legal_actions(
            NavState(doc_id="doc", query="Deep Leaf Detail", highlight_ids=["doc:L3"]),
            proj,
            step_idx=1,
            config=cfg,
        )
        text = format_actionable_map_observation(proj, actions)
        # Actionable text should fit or be spine-only without hard truncation marker.
        self.assertNotIn("... [projection truncated]", text)
        self.assertLessEqual(len(text), cfg.map_char_limit + 200)

    def test_map_can_hide_depth0_flat_siblings(self) -> None:
        flat = {
            "doc:A": {"title": "Alpha relevant", "level": 1, "children": []},
            "doc:B": {"title": "Beta noise", "level": 1, "children": []},
            "doc:C": {"title": "Gamma noise", "level": 1, "children": []},
            "doc:D": {"title": "Delta noise", "level": 1, "children": []},
        }
        ts = _FakeTS(flat)
        ts.sections_for_doc = lambda doc_id: ["doc:A", "doc:B", "doc:C", "doc:D"]  # type: ignore
        cfg = NavConfig(map_mode=True, map_char_limit=120, collect_top_k=1)
        proj = build_map(
            ts,
            doc_id="doc",
            query="Alpha",
            scope=None,
            config=cfg,
            map_scores={"doc:A": 9.0, "doc:B": 0.1, "doc:C": 0.1, "doc:D": 0.1},
            highlight_ids=["doc:A"],
        )
        ids = {v.section_id for v in proj.tree_sections}
        self.assertIn("doc:A", ids)
        # Depth-0 non-highlight siblings may be hidden under budget.
        self.assertTrue(len(ids) < 4)

    def test_budget_hide_does_not_rescan_tree_per_hidden_node(self) -> None:
        import nav_projection

        flat = {
            f"doc:L{i}": {
                "title": f"Section {i}",
                "level": 1,
                "children": [],
            }
            for i in range(200)
        }
        ts = _FakeTS(flat)
        ts.sections_for_doc = lambda doc_id: list(flat)  # type: ignore
        cfg = NavConfig(
            map_mode=True,
            map_char_limit=180,
            collect_top_k=1,
        )
        scores = {
            section_id: float(index)
            for index, section_id in enumerate(flat, 1)
        }
        highlight = "doc:L199"

        with patch(
            "nav_projection._estimate_actionable_total",
            wraps=nav_projection._estimate_actionable_total,
        ) as estimate:
            projection = build_map(
                ts,
                doc_id="doc",
                query="Section 199",
                scope=None,
                config=cfg,
                map_scores=scores,
                highlight_ids=[highlight],
            )

        self.assertLessEqual(estimate.call_count, 2)
        self.assertIn(
            highlight,
            {view.section_id for view in projection.tree_sections},
        )

    def test_highlight_path_and_leaf_actions(self) -> None:
        proj = build_map(
            self.ts,
            doc_id="doc",
            query="Deep Leaf",
            scope=None,
            config=self.cfg,
            map_scores={
                "doc:L3": 8.0,
                "doc:L2": 4.0,
                "doc:L1": 3.0,
                "doc:L10": 0.1,
                "doc:L11": 0.1,
            },
            highlight_ids=["doc:L3"],
        )
        ids = {v.section_id for v in proj.tree_sections}
        self.assertIn("doc:L3", ids)
        self.assertIn("doc:L2", ids)
        self.assertIn("doc:L1", ids)
        hit = next(v for v in proj.tree_sections if v.section_id == "doc:L3")
        self.assertTrue(hit.is_highlight)

        state = NavState(
            doc_id="doc",
            query="Deep Leaf",
            task_type="niche_fact",
            highlight_ids=["doc:L3"],
            unit_scores={"doc:L3": 8.0},
        )
        actions = build_legal_actions(state, proj, step_idx=1, config=self.cfg)
        by_sid: dict[str, set] = {}
        for a in actions:
            if a.section_id:
                by_sid.setdefault(a.section_id, set()).add(a.kind)
        # Every visible node is collectable; internal nodes also dispatchable.
        self.assertIn(ActionKind.COLLECT, by_sid["doc:L3"])
        self.assertIn(ActionKind.COLLECT, by_sid["doc:L1"])
        self.assertIn(ActionKind.DISPATCH, by_sid["doc:L1"])
        # Leaf has no DISPATCH.
        self.assertNotIn(ActionKind.DISPATCH, by_sid.get("doc:L3", set()))
        text = format_actionable_map_observation(proj, actions)
        self.assertIn("[Hit]", text)
        self.assertIn("collect=", text)

    def test_select_map_highlights_maps_self_units(self) -> None:
        hits = select_map_highlights(
            {"doc:L3": 1.0, "doc:L1__self": 5.0, "doc:L5": 2.0},
            k=2,
        )
        self.assertEqual(hits, ["doc:L1", "doc:L5"])

    def test_map_actions_collect_dispatch_finish_only(self) -> None:
        proj = build_map(
            self.ts,
            doc_id="doc",
            query="Deep Leaf",
            scope=None,
            config=self.cfg,
            map_scores={"doc:L3": 8.0},
            highlight_ids=["doc:L3"],
        )
        state = NavState(
            doc_id="doc",
            query="Deep Leaf",
            task_type="niche_fact",
            highlight_ids=["doc:L3"],
        )
        actions = build_legal_actions(state, proj, step_idx=6, config=self.cfg)
        kinds = {a.kind for a in actions}
        self.assertEqual(
            kinds,
            {ActionKind.COLLECT, ActionKind.DISPATCH, ActionKind.FINISH},
        )
        # Every visible section has COLLECT (no action top-K starvation).
        visible = {v.section_id for v in proj.tree_sections}
        collect_targets = {a.section_id for a in actions if a.kind == ActionKind.COLLECT}
        self.assertTrue(visible.issubset(collect_targets))
        # DISPATCH only on internal nodes.
        dispatch_targets = {a.section_id for a in actions if a.kind == ActionKind.DISPATCH}
        self.assertIn("doc:L1", dispatch_targets)
        self.assertNotIn("doc:L3", dispatch_targets)

    def test_map_parent_max_pool_scores(self) -> None:
        from nav_map_scores import compute_map_scores

        class _ScoreTS(_FakeTS):
            def materialize_self_only_chunks(self, section_id, doc_id):
                del doc_id
                chunk = MagicMock()
                chunk.text = self.tree[section_id]["title"]
                return [chunk]

            def _children_for_section_path(self, section_id, doc_id, limit=100000):
                return super()._children_for_section_path(section_id, doc_id, limit)

        ts = _ScoreTS(TREE)
        scores = compute_map_scores(
            ts, doc_id="doc", query="Deep Leaf Detail", root_ids=["doc:L1", "doc:L10"]
        )
        self.assertIn("doc:L3", scores)
        # Single-child parent: max-pool equals the child leaf score.
        if "doc:L2" in scores and "doc:L3" in scores:
            self.assertAlmostEqual(scores["doc:L2"], scores["doc:L3"], places=6)

    def test_scoped_map_inlines_summary_from_store(self) -> None:
        import tempfile
        from pathlib import Path
        import json
        from section_summary_store import clear_cache

        with tempfile.TemporaryDirectory() as tmp:
            doc_path = Path(tmp) / "doc.json"
            doc_path.write_text(
                json.dumps(
                    {
                        "sections": {
                            "doc:L1": {"summary": "HEAD_TEXT ... TAIL_TEXT"},
                            "doc:L3": {"summary": "LEAF_HEAD ... LEAF_TAIL"},
                        }
                    }
                ),
                encoding="utf-8",
            )
            os.environ["NAV_SECTION_SUMMARY_DIR"] = tmp
            clear_cache()
            try:
                proj = build_map(
                    self.ts,
                    doc_id="doc",
                    query="x",
                    scope="doc:L1",
                    config=self.cfg,
                    map_scores={"doc:L3": 5.0},
                )
                self.assertIn("summary:", proj.text)
                self.assertTrue(
                    any(v.summary for v in proj.tree_sections),
                    msg="scoped map should inline summaries",
                )
            finally:
                os.environ.pop("NAV_SECTION_SUMMARY_DIR", None)
                clear_cache()

    def test_finish_always_available(self) -> None:
        proj = build_map(
            self.ts, doc_id="doc", query="x", scope=None, config=self.cfg
        )
        state = NavState(doc_id="doc", query="x")
        # Early step, empty evidence: FINISH is still legal for LLM exit.
        actions = build_legal_actions(state, proj, step_idx=1, config=self.cfg)
        self.assertIn(ActionKind.FINISH, {a.kind for a in actions})
        actions2 = build_legal_actions(state, proj, step_idx=6, config=self.cfg)
        self.assertIn(ActionKind.FINISH, {a.kind for a in actions2})

    def test_no_self_dispatch_on_current_scope(self) -> None:
        proj = build_map(
            self.ts, doc_id="doc", query="x", scope="doc:L1", config=self.cfg
        )
        state = NavState(doc_id="doc", query="x", current_scope="doc:L1")
        cfg = NavConfig(
            map_mode=True,
            enable_recursive_dispatch=True,
            max_dispatch_depth=3,
        )
        actions = build_legal_actions(
            state, proj, step_idx=1, config=cfg, depth=1
        )
        dispatch_targets = {
            a.section_id for a in actions if a.kind == ActionKind.DISPATCH
        }
        self.assertNotIn("doc:L1", dispatch_targets)
        # Child internal nodes remain dispatchable.
        self.assertIn("doc:L2", dispatch_targets)
        self.assertIn(ActionKind.FINISH, {a.kind for a in actions})
        # Scope root remains collectable (not synthetic).
        self.assertIn(
            "doc:L1",
            {a.section_id for a in actions if a.kind == ActionKind.COLLECT},
        )

    def test_no_covered_field_on_state(self) -> None:
        state = NavState(doc_id="doc", query="x")
        self.assertFalse(hasattr(state, "covered_section_ids"))
        self.assertTrue(hasattr(state, "collected_section_ids"))

    def test_recursion_off_blocks_deep_dispatch(self) -> None:
        proj = build_map(
            self.ts, doc_id="doc", query="x", scope="doc:L1", config=self.cfg
        )
        state = NavState(doc_id="doc", query="x")
        cfg = NavConfig(map_mode=True, enable_recursive_dispatch=False)
        actions = build_legal_actions(
            state, proj, step_idx=1, config=cfg, depth=1
        )
        kinds = {a.kind for a in actions}
        self.assertIn(ActionKind.COLLECT, kinds)
        self.assertNotIn(ActionKind.DISPATCH, kinds)

    def test_recursion_on_allows_deep_dispatch(self) -> None:
        proj = build_map(
            self.ts, doc_id="doc", query="x", scope="doc:L1", config=self.cfg
        )
        state = NavState(doc_id="doc", query="x")
        cfg = NavConfig(
            map_mode=True,
            enable_recursive_dispatch=True,
            max_dispatch_depth=3,
        )
        actions = build_legal_actions(
            state, proj, step_idx=1, config=cfg, depth=1
        )
        self.assertTrue(any(a.kind == ActionKind.DISPATCH for a in actions))
        # Past max depth: no DISPATCH.
        actions2 = build_legal_actions(
            state, proj, step_idx=1, config=cfg, depth=3
        )
        self.assertFalse(any(a.kind == ActionKind.DISPATCH for a in actions2))

    def test_collect_removes_branch_from_map(self) -> None:
        proj = build_map(
            self.ts,
            doc_id="doc",
            query="x",
            scope=None,
            config=self.cfg,
            collected_section_ids={"doc:L1", "doc:L2", "doc:L3", "doc:L5"},
        )
        ids = {v.section_id for v in proj.tree_sections}
        self.assertNotIn("doc:L1", ids)
        self.assertNotIn("doc:L3", ids)
        self.assertIn("doc:L10", ids)

    def test_sort_collected_by_doc_order(self) -> None:
        from nav_navigate import sort_collected_by_doc_order

        class _C:
            def __init__(self, nid: str, lines: list[int]) -> None:
                self.node_id = nid
                self.line_ids = lines
                self.section_id = nid

        scored = [
            (_C("doc:L11", [11]), 9.0),
            (_C("doc:L3", [3]), 5.0),
            (_C("doc:L5", [5]), 8.0),
        ]
        ordered = sort_collected_by_doc_order(scored, self.ts, "doc")
        self.assertEqual(
            [c.node_id for c, _ in ordered],
            ["doc:L3", "doc:L5", "doc:L11"],
        )

    def test_dispatch_merges_reports_and_evidence(self) -> None:
        from nav_navigate import navigate
        from unittest.mock import patch

        cfg = NavConfig(
            map_mode=True,
            policy="rule",
            enable_recursive_dispatch=False,
            max_steps=4,
            navigate_max_steps=3,
            dispatch_concurrency=1,
            collect_k=4,
        )
        state = NavState(doc_id="doc", query="Deep Leaf", task_type="niche_fact")
        state.map_scores = {"doc:L1": 5.0, "doc:L3": 8.0}

        # Fake materialize so COLLECT adds evidence.
        def _materialize(sid: str, doc_id: str):
            del doc_id
            chunk = MagicMock()
            chunk.node_id = f"{sid}__chunk"
            chunk.line_ids = [int(sid.split("L")[-1])]
            chunk.section_id = sid
            chunk.doc_id = "doc"
            chunk.text = sid
            return [chunk]

        self.ts._materialize_leaf_path_chunks = _materialize  # type: ignore

        call_n = {"n": 0}

        def fake_llm(st, proj, actions, **kwargs):
            del st, proj, kwargs
            call_n["n"] += 1
            # Root: DISPATCH doc:L1 first, then FINISH.
            if call_n["n"] == 1:
                for a in actions:
                    if a.kind == ActionKind.DISPATCH and a.section_id == "doc:L1":
                        return a, {"reason": "dispatch chapter"}
            # Subagent / later: COLLECT then FINISH.
            for a in actions:
                if a.kind == ActionKind.COLLECT and a.section_id in {
                    "doc:L3",
                    "doc:L2",
                    "doc:L1",
                    "doc:L5",
                }:
                    return a, {"reason": "collect"}
            for a in actions:
                if a.kind == ActionKind.FINISH:
                    return a, {"reason": "done"}
            return actions[-1], {"reason": "fallback"}

        with patch("nav_navigate.choose_llm_action", side_effect=fake_llm):
            cfg.policy = "llm"
            report = navigate(
                self.ts,
                state=state,
                scope=None,
                query="Deep Leaf",
                config=cfg,
                depth=0,
            )
        self.assertIn("doc:L1", state.investigated_section_ids)
        self.assertTrue(state.reports_context)
        self.assertIn("Investigate results", state.reports_context)
        self.assertTrue(state.collected or state.collected_section_ids)
        self.assertIsInstance(report.reason, str)

    def test_legacy_projection_unchanged_when_map_off(self) -> None:
        os.environ["NAV_MAP_MODE"] = "0"
        cfg = NavConfig(map_mode=False, projection_depth=2)
        proj = build_projection(
            self.ts, doc_id="doc", query="Chapter", scope=None, config=cfg
        )
        self.assertFalse(proj.map_mode)
        self.assertIn("Preview:", proj.text)


if __name__ == "__main__":
    unittest.main()
