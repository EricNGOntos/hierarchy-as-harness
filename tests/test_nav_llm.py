"""Boundary LLM adapter: injection + model resolve (no network)."""

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

from nav_llm import (  # noqa: E402
    nav_chat,
    nav_thinking_extra,
    planner_output_max_tokens,
    resolve_nav_model,
    resolve_nav_thinking_mode,
    set_nav_chat_backend,
)


class TestNavLlm(unittest.TestCase):
    def tearDown(self) -> None:
        set_nav_chat_backend(None)

    def test_injected_backend_bypasses_credentials(self) -> None:
        seen: dict = {}

        def backend(**kwargs):
            seen.update(kwargs)
            return {"content": '{"ok":true}', "usage": {"total_tokens": 1}}

        set_nav_chat_backend(backend)
        out = nav_chat(
            purpose="test",
            model="deepseek-v4-flash",
            messages=[{"role": "user", "content": "hi"}],
            usage_tag="nav_test",
        )
        self.assertEqual(out["content"], '{"ok":true}')
        self.assertEqual(seen["model"], "deepseek-v4-flash")
        self.assertEqual(seen["usage_tag"], "nav_test")

    def test_resolve_prefers_explicit_env(self) -> None:
        with mock.patch.dict(
            os.environ,
            {"NAV_LLM_MODEL": "qwen3.5-flash", "DS_KEY": "x", "COMPOSE_MODEL": "other"},
            clear=False,
        ):
            self.assertEqual(
                resolve_nav_model(model_env="NAV_LLM_MODEL"),
                "qwen3.5-flash",
            )

    def test_resolve_falls_back_to_deepseek_when_ds_key(self) -> None:
        env = {
            k: v
            for k, v in os.environ.items()
            if k
            not in {
                "NAV_LLM_MODEL",
                "COMPOSE_MODEL",
                "NAV_PLANNER_MODEL",
                "NAV_PROBE_SCORE_MODEL",
            }
        }
        env["DS_KEY"] = "secret"
        with mock.patch.dict(os.environ, env, clear=True):
            # Clear model envs that load_llm_env may refill from llm_api.env —
            # force empty for this unit by patching load to no-op after set.
            with mock.patch(
                "agent_delivery.code.llm_config.load_llm_env", lambda: None
            ):
                os.environ["DS_KEY"] = "secret"
                for dead in (
                    "NAV_LLM_MODEL",
                    "COMPOSE_MODEL",
                    "NAV_PLANNER_MODEL",
                    "NAV_PROBE_SCORE_MODEL",
                ):
                    os.environ.pop(dead, None)
                self.assertEqual(resolve_nav_model(), "deepseek-v4-flash")

    def test_action_thinking_always_disabled(self) -> None:
        with mock.patch.dict(os.environ, {"NAV_PLANNER_THINKING": "enabled"}, clear=False):
            self.assertEqual(resolve_nav_thinking_mode(role="action"), "disabled")
            extra = nav_thinking_extra(role="action", model="deepseek-v4-flash")
            self.assertEqual(extra["extra_body"]["thinking"]["type"], "disabled")

    def test_planner_thinking_follows_env(self) -> None:
        with mock.patch.dict(os.environ, {"NAV_PLANNER_THINKING": "disabled"}, clear=False):
            self.assertEqual(resolve_nav_thinking_mode(role="planner"), "disabled")
        with mock.patch.dict(os.environ, {"NAV_PLANNER_THINKING": "enabled"}, clear=False):
            self.assertEqual(resolve_nav_thinking_mode(role="planner"), "enabled")
            self.assertGreaterEqual(
                planner_output_max_tokens(1024),
                16384,
            )

    def test_nav_chat_injects_action_thinking_extra(self) -> None:
        seen: dict = {}

        def backend(**kwargs):
            seen.update(kwargs)
            return {"content": "{}", "usage": {}}

        set_nav_chat_backend(backend)
        nav_chat(
            purpose="test",
            model="deepseek-v4-flash",
            messages=[{"role": "user", "content": "hi"}],
        )
        self.assertEqual(
            seen["extra"]["extra_body"]["thinking"]["type"],
            "disabled",
        )
        self.assertEqual(seen["thinking_role"], "action")


if __name__ == "__main__":
    unittest.main()

