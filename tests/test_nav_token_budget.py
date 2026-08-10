"""Unit tests for episode LLM token hard stop."""

from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
for source_dir in (ROOT / "src" / "realdata", ROOT / "src" / "nav"):
    if str(source_dir) not in sys.path:
        sys.path.insert(0, str(source_dir))

from agent_delivery.code.llm_usage import record_usage, reset_usage  # noqa: E402
from nav_token_budget import (  # noqa: E402
    NavTokenLimit,
    nav_token_budget_exhausted,
    nav_token_episode,
    nav_token_limit,
    nav_tokens_used,
    record_episode_tokens,
)


class TestNavTokenBudget(unittest.TestCase):
    def tearDown(self) -> None:
        reset_usage()
        os.environ.pop("RETRIEVAL_NAV_TOKEN_LIMIT", None)

    def test_default_limit_from_plan(self) -> None:
        os.environ.pop("RETRIEVAL_NAV_TOKEN_LIMIT", None)
        self.assertEqual(nav_token_limit(), 100_000)

    def test_env_override(self) -> None:
        os.environ["RETRIEVAL_NAV_TOKEN_LIMIT"] = "50"
        self.assertEqual(nav_token_limit(), 50)

    def test_exhausted_uses_snapshot_total_outside_episode(self) -> None:
        os.environ["RETRIEVAL_NAV_TOKEN_LIMIT"] = "100"
        reset_usage()
        self.assertFalse(nav_token_budget_exhausted())
        record_usage("nav", {"prompt_tokens": 40, "completion_tokens": 60, "total_tokens": 100})
        self.assertEqual(nav_tokens_used(), 100)
        self.assertTrue(nav_token_budget_exhausted())

    def test_episode_scope_isolates_from_process_usage(self) -> None:
        os.environ["RETRIEVAL_NAV_TOKEN_LIMIT"] = "50"
        reset_usage()
        record_usage("other", {"total_tokens": 10_000})
        with nav_token_episode():
            self.assertEqual(nav_tokens_used(), 0)
            self.assertFalse(nav_token_budget_exhausted())
            record_episode_tokens({"total_tokens": 50})
            self.assertEqual(nav_tokens_used(), 50)
            self.assertTrue(nav_token_budget_exhausted())
        # Outside episode, process snapshot still applies.
        self.assertEqual(nav_tokens_used(), 10_000)

    def test_nav_chat_refuses_when_exhausted(self) -> None:
        from nav_llm import nav_chat, set_nav_chat_backend

        os.environ["RETRIEVAL_NAV_TOKEN_LIMIT"] = "10"
        called = {"n": 0}

        def backend(**_kwargs):
            called["n"] += 1
            return {"content": "{}", "usage": {"total_tokens": 1}}

        set_nav_chat_backend(backend)
        try:
            with nav_token_episode():
                record_episode_tokens({"total_tokens": 10})
                with self.assertRaises(NavTokenLimit):
                    nav_chat(
                        purpose="t",
                        messages=[{"role": "user", "content": "x"}],
                        model="m",
                    )
                self.assertEqual(called["n"], 0)
        finally:
            set_nav_chat_backend(None)

    def test_nav_chat_credits_episode_counter(self) -> None:
        from nav_llm import nav_chat, set_nav_chat_backend

        os.environ["RETRIEVAL_NAV_TOKEN_LIMIT"] = "100"

        def backend(**_kwargs):
            return {"content": "{}", "usage": {"total_tokens": 7}}

        set_nav_chat_backend(backend)
        try:
            with nav_token_episode():
                nav_chat(
                    purpose="t",
                    messages=[{"role": "user", "content": "x"}],
                    model="m",
                )
                self.assertEqual(nav_tokens_used(), 7)
        finally:
            set_nav_chat_backend(None)

    def test_non_positive_or_invalid_falls_back_to_default(self) -> None:
        reset_usage()
        for raw in ("0", "-1", "abc"):
            os.environ["RETRIEVAL_NAV_TOKEN_LIMIT"] = raw
            self.assertEqual(nav_token_limit(), 100_000)
        record_usage("nav", {"total_tokens": 100_000})
        self.assertTrue(nav_token_budget_exhausted())

    def test_harvest_skips_llm_when_exhausted(self) -> None:
        from nav_harvest import harvest_policy_call
        from nav_plan import Subgoal
        from nav_types import NavConfig, NavState, Projection

        os.environ["RETRIEVAL_NAV_TOKEN_LIMIT"] = "1"
        reset_usage()
        record_usage("nav", {"total_tokens": 1})
        state = NavState(doc_id="d", query="q")
        projection = Projection(
            doc_id="d",
            scope=None,
            text="",
            visible_sections=[],
            id_to_section={},
            tree_sections=[],
        )
        with mock.patch("agent_delivery.code.llm_api_cache.cached_chat_completion") as mocked:
            collects, dispatches, _conf, reason, meta = harvest_policy_call(
                None,
                state,
                NavConfig(),
                subgoal=Subgoal(id="s1", need="n", retrieval_query="q"),
                query="q",
                projection=projection,
                actions=[],
                depth=0,
            )
        self.assertEqual(collects, [])
        self.assertEqual(dispatches, [])
        self.assertEqual(reason, "token_limit")
        self.assertEqual(meta.get("stop_reason"), "token_limit")
        mocked.assert_not_called()

    def test_policy_retry_does_not_call_again_after_limit(self) -> None:
        from nav_actions import LegalAction
        from nav_policy import choose_llm_action
        from nav_types import ActionKind, NavConfig, NavState, Projection

        os.environ["RETRIEVAL_NAV_TOKEN_LIMIT"] = "5"
        calls = {"n": 0}

        def backend(**_kwargs):
            calls["n"] += 1
            return {
                "content": '{"action_id":"BAD"}',
                "usage": {"total_tokens": 5},
            }

        from nav_llm import set_nav_chat_backend

        set_nav_chat_backend(backend)
        try:
            finish = LegalAction(
                action_id="F1",
                kind=ActionKind.FINISH,
                section_id="",
                label="finish",
            )
            state = NavState(doc_id="d", query="q")
            projection = Projection(
                doc_id="d",
                scope=None,
                text="obs",
                visible_sections=[],
                id_to_section={},
                tree_sections=[],
            )
            with nav_token_episode():
                chosen, meta = choose_llm_action(
                    state,
                    projection,
                    [finish],
                    step_idx=1,
                    config=NavConfig(),
                )
                # First call credits 5 → exhausted; retry must FINISH without 2nd call.
                self.assertEqual(calls["n"], 1)
                self.assertEqual(chosen.kind, ActionKind.FINISH)
                self.assertEqual(meta.get("stop_reason"), "token_limit")
        finally:
            set_nav_chat_backend(None)


if __name__ == "__main__":
    unittest.main()
