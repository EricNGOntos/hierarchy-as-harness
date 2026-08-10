"""P0.3: search_assets kind→chunk_type filter under scope."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for _p in (ROOT / "src" / "realdata", ROOT / "src" / "nav"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from nav_assets import (  # noqa: E402
    apply_search_assets,
    asset_chunk_type,
    gather_scoped_asset_chunks,
    parse_search_assets,
)
from nav_hierarchy import ProviderToolSpace  # noqa: E402
from nav_knowhere import load_debug_parse  # noqa: E402
from nav_types import NavConfig, NavState  # noqa: E402
from test_nav_knowhere_provider import _write_track  # noqa: E402


class ParseSearchAssetsTests(unittest.TestCase):
    def test_kind_aliases(self) -> None:
        self.assertEqual(asset_chunk_type("images"), "image")
        self.assertEqual(asset_chunk_type("TABLES"), "table")
        self.assertIsNone(asset_chunk_type("text"))

    def test_parse_skips_unknown(self) -> None:
        got = parse_search_assets(
            [
                {"kind": "tables", "query": "flood", "scope": "sec-a"},
                {"kind": "pages", "query": "x"},
                "bad",
            ]
        )
        self.assertEqual(len(got), 1)
        self.assertEqual(got[0]["asset_type"], "table")
        self.assertEqual(got[0]["scope"], "sec-a")


class GatherScopedAssetChunksTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        track = _write_track(Path(self._tmp.name), name="probe")
        self.provider = load_debug_parse(track, doc_id="probe")
        self.ts = ProviderToolSpace(self.provider)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_filters_tables_under_section_scope(self) -> None:
        chunks = gather_scoped_asset_chunks(
            self.ts,
            asset_type="table",
            scope="probe:A",
            doc_id="probe",
        )
        self.assertEqual([c.node_id for c in chunks], ["probe-u-t1"])
        self.assertIn("T1 summary", chunks[0].text)

    def test_images_empty_when_track_has_none(self) -> None:
        chunks = gather_scoped_asset_chunks(
            self.ts,
            asset_type="image",
            scope="probe:A",
            doc_id="probe",
        )
        self.assertEqual(chunks, [])

    def test_apply_search_assets_adds_to_state(self) -> None:
        state = NavState(doc_id="probe", query="table")
        n, trace = apply_search_assets(
            self.ts,
            state,
            NavConfig(read_score_bonus=1.0),
            requests=[{"kind": "tables", "query": "t", "scope": "probe:A", "asset_type": "table"}],
            default_scope=None,
        )
        self.assertEqual(n, 1)
        self.assertEqual(trace[0]["n_added"], 1)
        self.assertIn("probe-u-t1", state.collected_ids)


if __name__ == "__main__":
    unittest.main()
