"""Unit tests for offline reference-fact probe scoring (no LLM)."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
for source_dir in (ROOT / "src" / "realdata", ROOT / "src" / "nav"):
    if str(source_dir) not in sys.path:
        sys.path.insert(0, str(source_dir))

from nav_probe_score import (  # noqa: E402
    GRADE_CORRECT,
    GRADE_HALF,
    GRADE_WRONG,
    aggregate_fact_grades,
    coerce_grade,
    parse_grade_payload,
    resolve_reference_facts,
)


class TestNavProbeScore(unittest.TestCase):
    def test_resolve_prefers_reference_facts(self) -> None:
        case = {
            "reference_answer": "prose fallback",
            "reference_facts": [
                {"id": "f1", "fact": "fact A"},
                "fact B",
            ],
        }
        facts = resolve_reference_facts(case)
        self.assertEqual([f["id"] for f in facts], ["f1", "f2"])
        self.assertEqual(facts[1]["fact"], "fact B")

    def test_resolve_falls_back_to_reference_answer(self) -> None:
        facts = resolve_reference_facts({"reference_answer": "one prose fact"})
        self.assertEqual(facts, [{"id": "f1", "fact": "one prose fact"}])

    def test_coerce_and_aggregate(self) -> None:
        self.assertEqual(coerce_grade("半对"), GRADE_HALF)
        self.assertEqual(coerce_grade(1), GRADE_CORRECT)
        self.assertEqual(coerce_grade("wrong"), GRADE_WRONG)
        self.assertEqual(aggregate_fact_grades([1.0, 0.5, 0.0]), 0.5)
        self.assertEqual(aggregate_fact_grades([]), 0.0)

    def test_parse_grade_payload_defaults_missing_to_wrong(self) -> None:
        facts = [{"id": "f1", "fact": "a"}, {"id": "f2", "fact": "b"}]
        grades = parse_grade_payload(
            {"grades": [{"id": "f1", "grade": "对"}]},
            facts,
        )
        self.assertEqual(grades["f1"], GRADE_CORRECT)
        self.assertEqual(grades["f2"], GRADE_WRONG)


if __name__ == "__main__":
    unittest.main()
