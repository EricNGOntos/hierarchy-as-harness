"""Asset SEARCH: document-bound scope + Knowhere-style inspector."""
from __future__ import annotations

import sys
import unittest

ROOT = __import__("pathlib").Path(__file__).resolve().parents[1]
for _p in (ROOT / "src" / "realdata", ROOT / "src" / "nav"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from nav_assets import (  # noqa: E402
    apply_search_assets,
    asset_chunk_type,
    gather_scoped_asset_chunks,
    parse_search_assets,
    set_nav_vlm_backend,
)
from nav_hierarchy import ProviderToolSpace  # noqa: E402
from nav_knowhere import (  # noqa: E402
    KnowhereProvider,
    NamespaceKnowhereProvider,
    SectionRow,
    UnitRow,
)
from nav_llm import set_nav_chat_backend  # noqa: E402
from nav_types import NavConfig, NavState  # noqa: E402
from test_nav_knowhere_provider import make_micro_provider  # noqa: E402


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
        self.provider = make_micro_provider()
        self.ts = ProviderToolSpace(self.provider)

    def test_filters_tables_under_section_scope(self) -> None:
        chunks = gather_scoped_asset_chunks(
            self.ts, asset_type="table", scope="sec_a", doc_id="doc_probe"
        )
        self.assertEqual([c.node_id for c in chunks], ["u-t1"])

    def test_document_root_scope_finds_section_assets(self) -> None:
        chunks = gather_scoped_asset_chunks(
            self.ts, asset_type="table", scope="doc_probe", doc_id="doc_probe"
        )
        self.assertEqual([c.node_id for c in chunks], ["u-t1"])

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
        self.provider = make_micro_provider()
        self.ts = ProviderToolSpace(self.provider)
        set_nav_vlm_backend(None)

    def tearDown(self) -> None:
        set_nav_chat_backend(None)
        set_nav_vlm_backend(None)

    def test_inspector_keeps_only_matched_and_injects_context(self) -> None:
        set_nav_chat_backend(lambda **kwargs: {"content": '["T1"]'})
        state = NavState(doc_id="doc_probe", query="T1 summary flood table")
        n, trace = apply_search_assets(
            self.ts,
            state,
            NavConfig(read_score_bonus=1.0),
            requests=[
                {
                    "kind": "tables",
                    "query": "T1 summary",
                    "scope": "sec_a",
                    "asset_type": "table",
                }
            ],
            default_scope=None,
        )
        self.assertEqual(n, 1)
        self.assertEqual(trace[0]["n_candidates"], 1)
        self.assertEqual(trace[0]["n_matched"], 1)
        self.assertEqual(trace[0]["status"], "matched")
        self.assertIn("u-t1", state.collected_ids)
        self.assertIn("SEARCH_TABLES", state.asset_observation_context)
        self.assertIn("T1", state.asset_observation_context)

    def test_inspector_empty_match_adds_nothing_but_writes_context(self) -> None:
        set_nav_chat_backend(lambda **kwargs: {"content": "[]"})
        state = NavState(doc_id="doc_probe", query="unrelated")
        n, trace = apply_search_assets(
            self.ts,
            state,
            NavConfig(read_score_bonus=1.0),
            requests=[
                {
                    "kind": "tables",
                    "query": "zzz",
                    "scope": "sec_a",
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
        state = NavState(doc_id="doc_probe", query="img")
        n, trace = apply_search_assets(
            self.ts,
            state,
            NavConfig(read_score_bonus=1.0),
            requests=[
                {
                    "kind": "images",
                    "query": "img",
                    "scope": "sec_a",
                    "asset_type": "image",
                }
            ],
            default_scope=None,
        )
        self.assertEqual(n, 0)
        self.assertEqual(trace[0]["status"], "empty")

    def test_image_vlm_failure_falls_back_to_text_llm(self) -> None:
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
                "section_id": "sec_a",
                "section_path": "A",
                "owner_section_path": "A",
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
        pa = KnowhereProvider(
            doc_id="doc_a",
            sections=[
                SectionRow("sec_a_a", None, "A", "A", 1, "", 0),
                SectionRow("sec_a_b", None, "B", "B", 1, "", 1),
            ],
            units=[
                UnitRow(
                    "a-t1",
                    "sec_a_a",
                    "table",
                    "tables/t1.html",
                    1,
                    file_path="tables/t1.html",
                    metadata={"summary": "T1", "asset_title": "T1"},
                ),
            ],
        )
        pb = KnowhereProvider(
            doc_id="doc_b",
            sections=[SectionRow("sec_b_a", None, "A", "A", 1, "", 0)],
            units=[],
        )
        self.ts = ProviderToolSpace(
            NamespaceKnowhereProvider([pa, pb], titles={"doc_a": "A", "doc_b": "B"})
        )
        set_nav_chat_backend(lambda **kwargs: {"content": '["T1"]'})

    def tearDown(self) -> None:
        set_nav_chat_backend(None)

    def test_resolve_rejects_namespace_root(self) -> None:
        from nav_assets import resolve_asset_search_scope

        self.assertEqual(
            resolve_asset_search_scope(
                self.ts,
                requested_scope="",
                default_scope=None,
                fallback_doc_id="",
            ),
            ("", "", "skipped_no_document_scope"),
        )

    def test_search_under_document_node(self) -> None:
        state = NavState(doc_id="", query="T1")
        n, trace = apply_search_assets(
            self.ts,
            state,
            NavConfig(read_score_bonus=1.0),
            requests=[
                {
                    "kind": "tables",
                    "query": "T1",
                    "scope": "doc_a",
                    "asset_type": "table",
                }
            ],
            default_scope=None,
        )
        self.assertEqual(n, 1)
        self.assertEqual(trace[0]["status"], "matched")


if __name__ == "__main__":
    unittest.main()
