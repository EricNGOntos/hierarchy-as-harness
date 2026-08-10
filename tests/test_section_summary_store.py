"""Unit tests for section_summary_store get_summary(doc_id=...)."""

from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
for source_dir in (ROOT / "src" / "nav",):
    if str(source_dir) not in sys.path:
        sys.path.insert(0, str(source_dir))

from section_summary_store import clear_cache, get_summary  # noqa: E402


class TestSectionSummaryStore(unittest.TestCase):
    def tearDown(self) -> None:
        os.environ.pop("NAV_SECTION_SUMMARY_DIR", None)
        clear_cache()

    def test_requires_doc_id_no_colon_split(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "knowhere_doc.json"
            path.write_text(
                json.dumps(
                    {
                        "sections": {
                            "A/A1": {"summary": "hello"},
                            "knowhere_doc:A/A1": {"summary": "wrong-key"},
                        }
                    }
                ),
                encoding="utf-8",
            )
            os.environ["NAV_SECTION_SUMMARY_DIR"] = tmp
            clear_cache()
            # Without doc_id: miss (no colon parsing).
            self.assertIsNone(get_summary("A/A1"))
            self.assertIsNone(get_summary("knowhere_doc:A/A1"))
            # With doc_id: hit by exact section key.
            self.assertEqual(get_summary("A/A1", doc_id="knowhere_doc"), "hello")
            # Colon in section_id is just part of the key, not a doc splitter.
            self.assertEqual(
                get_summary("knowhere_doc:A/A1", doc_id="knowhere_doc"),
                "wrong-key",
            )


if __name__ == "__main__":
    unittest.main()
