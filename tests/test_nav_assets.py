"""Asset SEARCH: document-bound scope + Knowhere-style inspector."""
from __future__ import annotations

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
    resolve_asset_search_scope,
    set_nav_vlm_backend,
)
from nav_hierarchy import ProviderToolSpace  # noqa: E402
from nav_knowhere import NamespaceKnowhereProvider, load_debug_parse  # noqa: E402
from nav_llm import set_nav_chat_backend  # noqa: E402
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
            self.ts, asset_type="table", scope="probe:A", doc_id="probe"
        )
        self.assertEqual([c.node_id for c in chunks], ["probe-u-t1"])

    def test_document_root_scope_finds_section_assets(self) -> None:
        chunks = gather_scoped_asset_chunks(
            self.ts, asset_type="table", scope="probe", doc_id="probe"
        )
        self.assertEqual([c.node_id for c in chunks], ["probe-u-t1"])

    def test_namespace_default_scope_is_skipped(self) -> None:
        state = NavState(doc_id="", query="table")
        n, trace = apply_search_assets(
            self.ts,
            state,
            NavConfig(read_score_bonus=1.0),
            requests=[
                {"kind": "tables", "query": "t", "scope": "", "asset_type": "table"}
            ],
            default_scope=None,
        )
        self.assertEqual(n, 0)
        self.assertEqual(trace[0]["skip_reason"], "skipped_no_document_scope")


class InspectorTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        track = _write_track(Path(self._tmp.name), name="probe")
        self.provider = load_debug_parse(track, doc_id="probe")
        self.ts = ProviderToolSpace(self.provider)
        set_nav_vlm_backend(None)

    def tearDown(self) -> None:
        set_nav_chat_backend(None)
        set_nav_vlm_backend(None)
        self._tmp.cleanup()

    def test_inspector_keeps_only_matched_and_injects_context(self) -> None:
        def _backend(**kwargs):
            return {"content": '["T1"]'}

        set_nav_chat_backend(_backend)
        state = NavState(doc_id="probe", query="T1 summary flood table")
        n, trace = apply_search_assets(
            self.ts,
            state,
            NavConfig(read_score_bonus=1.0),
            requests=[
                {
                    "kind": "tables",
                    "query": "T1 summary",
                    "scope": "probe:A",
                    "asset_type": "table",
                }
            ],
            default_scope=None,
        )
        self.assertEqual(n, 1)
        self.assertEqual(trace[0]["n_candidates"], 1)
        self.assertEqual(trace[0]["n_matched"], 1)
        self.assertEqual(trace[0]["status"], "matched")
        self.assertIn("probe-u-t1", state.collected_ids)
        self.assertIn("SEARCH_TABLES", state.asset_observation_context)
        self.assertIn("T1", state.asset_observation_context)

    def test_inspector_empty_match_adds_nothing_but_writes_context(self) -> None:
        set_nav_chat_backend(lambda **kwargs: {"content": "[]"})
        state = NavState(doc_id="probe", query="unrelated")
        n, trace = apply_search_assets(
            self.ts,
            state,
            NavConfig(read_score_bonus=1.0),
            requests=[
                {
                    "kind": "tables",
                    "query": "zzz",
                    "scope": "probe:A",
                    "asset_type": "table",
                }
            ],
            default_scope=None,
        )
        self.assertEqual(n, 0)
        self.assertEqual(trace[0]["n_matched"], 0)
        self.assertEqual(state.collected_ids, set())
        self.assertIn("No matching tables", state.asset_observation_context)

    def test_image_vlm_unavailable_falls_back_to_text(self) -> None:
        # No image candidates in fixture; still exercises fallback status path
        # when gather is empty → empty status without calling LLM.
        state = NavState(doc_id="probe", query="img")
        n, trace = apply_search_assets(
            self.ts,
            state,
            NavConfig(read_score_bonus=1.0),
            requests=[
                {
                    "kind": "images",
                    "query": "img",
                    "scope": "probe:A",
                    "asset_type": "image",
                }
            ],
            default_scope=None,
        )
        self.assertEqual(n, 0)
        self.assertEqual(trace[0]["status"], "empty")

    def test_image_vlm_failure_falls_back_to_text_llm(self) -> None:
        # Build a synthetic image candidate via unit metadata by patching gather.
        from nav_assets import search_assets_step

        def boom(**kwargs):
            raise RuntimeError("vlm down")

        set_nav_vlm_backend(boom)
        set_nav_chat_backend(lambda **kwargs: {"content": '["I1"]'})
        candidates = [
            {
                "chunk_id": "img-1",
                "chunk_type": "image",
                "content": "",
                "file_path": "images/a.png",
                "section_id": "probe:A",
                "section_path": "probe:A",
                "owner_section_path": "probe:A",
                "summary": "flood map",
                "chunk_metadata": {"url": "https://example.com/a.png"},
                "display_text": "[Image] flood map",
                "chunk": type("C", (), {"node_id": "img-1", "line_ids": (1,)})(),
                "url": "https://example.com/a.png",
            }
        ]
        result = search_assets_step(
            query="flood map",
            asset_type="image",
            candidates=candidates,
            config=NavConfig(),
        )
        self.assertEqual(result["status"], "fallback_matched")
        self.assertIn("vlm_failed_text_fallback", result["status_detail"])
        self.assertEqual(len(result["matched_assets"]), 1)


class NamespaceAssetScopeTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        base = Path(self._tmp.name)
        pa = load_debug_parse(_write_track(base / "a", name="doc_a"), doc_id="doc_a")
        pb = load_debug_parse(_write_track(base / "b", name="doc_b"), doc_id="doc_b")
        self.ts = ProviderToolSpace(
            NamespaceKnowhereProvider([pa, pb], titles={"doc_a": "A", "doc_b": "B"})
        )
        set_nav_chat_backend(lambda **kwargs: {"content": '["T1"]'})

    def tearDown(self) -> None:
        set_nav_chat_backend(None)
        self._tmp.cleanup()

    def test_resolve_rejects_namespace_root(self) -> None:
        scope, doc, reason = resolve_asset_search_scope(
            self.ts, requested_scope="", default_scope="", fallback_doc_id=""
        )
        self.assertEqual(reason, "skipped_no_document_scope")

    def test_document_scope_does_not_leak_other_docs(self) -> None:
        chunks = gather_scoped_asset_chunks(
            self.ts, asset_type="table", scope="doc_a", doc_id="doc_a"
        )
        self.assertEqual([c.node_id for c in chunks], ["doc_a-u-t1"])

    def test_apply_defaults_to_current_document_not_namespace(self) -> None:
        state = NavState(doc_id="", query="table")
        n, trace = apply_search_assets(
            self.ts,
            state,
            NavConfig(read_score_bonus=1.0),
            requests=[
                {"kind": "tables", "query": "t", "scope": "", "asset_type": "table"}
            ],
            default_scope="doc_b",
        )
        self.assertEqual(n, 1)
        self.assertEqual(trace[0]["doc_id"], "doc_b")
        self.assertIn("doc_b-u-t1", state.collected_ids)
        self.assertNotIn("doc_a-u-t1", state.collected_ids)


if __name__ == "__main__":
    unittest.main()
