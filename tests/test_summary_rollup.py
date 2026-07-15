"""Tests for non-LLM covers summary rollup."""

from __future__ import annotations

import unittest

from summary_rollup import (
    SECTION_COVERS_PREFIX,
    deterministic_covers_summary,
    rollup_doc_summaries,
)


class TestDeterministicCovers(unittest.TestCase):
    def test_order_covers_self_then_titles(self) -> None:
        text, _ = deterministic_covers_summary(
            self_only="intro here",
            child_titles=["Alpha", "Beta"],
        )
        self.assertTrue(text.startswith(SECTION_COVERS_PREFIX))
        self.assertIn("intro here", text)
        self.assertIn("Alpha, Beta", text)
        self.assertLess(text.index("intro here"), text.index("Alpha, Beta"))

    def test_all_child_titles_included(self) -> None:
        order = [1, 2, 3]
        levels = {1: 1, 2: 2, 3: 2}
        line_text = {
            1: "Parent heading",
            2: "Child A title",
            3: "Child B title",
        }
        out = rollup_doc_summaries(order=order, levels=levels, line_text=line_text)
        parent = out[1]
        self.assertEqual(parent["rollup_mode"], "title_enum")
        summary = str(parent["summary"])
        self.assertTrue(summary.startswith(SECTION_COVERS_PREFIX))
        self.assertIn("Parent heading", summary)
        self.assertIn("Child A title", summary)
        self.assertIn("Child B title", summary)
        self.assertEqual(out[2]["rollup_mode"], "leaf")
        self.assertEqual(out[2]["summary"], "Child A title")


if __name__ == "__main__":
    unittest.main()
