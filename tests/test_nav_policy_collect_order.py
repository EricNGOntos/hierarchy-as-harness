"""#11 illegal-action FINISH + #12 deepest-first batch COLLECT."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
for source_dir in (ROOT / "src" / "realdata", ROOT / "src" / "nav"):
    if str(source_dir) not in sys.path:
        sys.path.insert(0, str(source_dir))

from nav_navigate import (  # noqa: E402
    _batch_collect_deepest_first,
    _section_ancestor_depth,
)
from nav_policy import choose_llm_action, choose_rule_action  # noqa: E402
from nav_types import ActionKind, LegalAction, NavConfig, NavState, Projection  # noqa: E402


def _actions() -> list[LegalAction]:
    return [
        LegalAction(action_id="C1", kind=ActionKind.COLLECT, section_id="doc:L1", label="a"),
        LegalAction(action_id="D1", kind=ActionKind.DISPATCH, section_id="doc:L2", label="b"),
        LegalAction(action_id="F1", kind=ActionKind.FINISH, section_id="", label="finish"),
    ]


class FakeTS:
    def __init__(self, depth_by_sid: dict[str, int]) -> None:
        self._depth = depth_by_sid

    def section_relation_ids(self, section_id: str, doc_id: str):
        del doc_id
        n = int(self._depth.get(section_id, 0))
        return {f"anc{i}" for i in range(n)}, set()


class TestIllegalActionFinish(unittest.TestCase):
    def test_rule_policy_still_prefers_collect(self) -> None:
        acts = _actions()
        chosen = choose_rule_action(
            NavState(doc_id="doc", query="q"),
            Projection(doc_id="doc", scope=None, text="", visible_sections=[]),
            acts,
            step_idx=0,
            config=NavConfig(),
        )
        self.assertEqual(chosen.action_id, "C1")

    def test_illegal_llm_finishes_and_records_refusal(self) -> None:
        state = NavState(doc_id="doc", query="q")
        acts = _actions()
        projection = Projection(
            doc_id="doc", scope=None, text="map", visible_sections=[]
        )

        def fake_chat(**_kwargs):
            return {"content": '{"action_id":"C99","reason":"bogus"}'}

        with patch("nav_llm.nav_chat", side_effect=fake_chat), patch(
            "nav_llm.resolve_nav_model", return_value="m"
        ), patch("nav_policy.time.sleep", return_value=None):
            chosen, meta = choose_llm_action(
                state,
                projection,
                acts,
                step_idx=1,
                config=NavConfig(policy="llm"),
                depth=0,
            )
        self.assertEqual(chosen.kind, ActionKind.FINISH)
        self.assertEqual(chosen.action_id, "F1")
        self.assertEqual(meta.get("reason"), "illegal_action_finish")
        self.assertEqual(len(state.refusal_events), 1)
        self.assertEqual(state.refusal_events[0].get("status"), "illegal_action")
        self.assertEqual(state.refusal_events[0].get("illegal_action_id"), "C99")


class TestBatchCollectDeepestFirst(unittest.TestCase):
    def test_parent_before_child_in_llm_order_becomes_child_first(self) -> None:
        ts = FakeTS({"doc:L1": 0, "doc:L2": 1, "doc:L3": 2})
        state = NavState(doc_id="doc", query="q")
        parent = LegalAction(action_id="C1", kind=ActionKind.COLLECT, section_id="doc:L1")
        mid = LegalAction(action_id="C2", kind=ActionKind.COLLECT, section_id="doc:L2")
        leaf = LegalAction(action_id="C3", kind=ActionKind.COLLECT, section_id="doc:L3")
        parent.metadata = {"batch_actions": [parent, mid, leaf]}  # shallow → deep

        ordered = _batch_collect_deepest_first(ts, state, parent)
        self.assertEqual(
            [a.section_id for a in ordered],
            ["doc:L3", "doc:L2", "doc:L1"],
        )
        self.assertEqual(_section_ancestor_depth(ts, state, "doc:L3"), 2)


if __name__ == "__main__":
    unittest.main()
