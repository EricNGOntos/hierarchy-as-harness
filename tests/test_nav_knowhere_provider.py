"""KnowhereProvider over production-shaped sec_* rows (no parse-track minting)."""
from __future__ import annotations

import os
import sys
import unittest

ROOT = __import__("pathlib").Path(__file__).resolve().parents[1]
for _p in (ROOT / "src" / "realdata", ROOT / "src" / "nav"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from nav_actions import build_legal_actions  # noqa: E402
from nav_address import NavLevel, uses_document_nodes  # noqa: E402
from nav_hierarchy import ProviderToolSpace  # noqa: E402
from nav_knowhere import (  # noqa: E402
    KnowhereProvider,
    NamespaceKnowhereProvider,
    SectionRow,
    UnitRow,
    load_document_from_db,
    normalize_section_path,
)
from nav_map_scores import (  # noqa: E402
    compute_corpus_map_and_unit_scores,
    select_map_highlights,
)
from nav_projection import build_map  # noqa: E402
from nav_types import ActionKind, NavConfig, NavState  # noqa: E402


def make_micro_provider(
    doc_id: str = "doc_probe",
    *,
    body_a: str = "A body [tables/t1.html]",
    body_a1: str = "A1 body",
    body_b: str = "B body",
) -> KnowhereProvider:
    """Tiny tree with production-like ``sec_*`` ids (no colon-in-id minting)."""
    sections = [
        SectionRow("sec_a", None, "A", "A", 1, "sum A", 0),
        SectionRow("sec_a1", "sec_a", "A / A1", "A1", 2, "sum A1", 1),
        SectionRow("sec_b", None, "B", "B", 1, "sum B", 2),
    ]
    units = [
        UnitRow("u-a", "sec_a", "text", body_a, 1),
        UnitRow(
            "u-t1",
            "sec_a",
            "table",
            "tables/t1.html",
            2,
            source_chunk_path="tables/t1.html",
            file_path="tables/t1.html",
            metadata={"summary": "T1 summary", "asset_title": "T1"},
        ),
        UnitRow("u-a1", "sec_a1", "text", body_a1, 3),
        UnitRow("u-b", "sec_b", "text", body_b, 4),
        # Orphan asset: section_id missing / unknown → dropped by provider
        UnitRow(
            "u-orphan",
            "sec_missing",
            "table",
            "tables/zz.html",
            5,
            source_chunk_path="tables/zz.html",
            metadata={"summary": "unreferenced"},
        ),
    ]
    return KnowhereProvider(doc_id=doc_id, sections=sections, units=units)


class KnowhereProviderTests(unittest.TestCase):
    def setUp(self) -> None:
        self.provider = make_micro_provider()
        self.doc_id = self.provider.doc_id

    def test_section_ids_are_opaque_keys(self) -> None:
        self.assertEqual(self.doc_id, "doc_probe")
        self.assertEqual(
            sorted(self.provider.all_section_ids()),
            sorted(["sec_a", "sec_a1", "sec_b"]),
        )

    def test_roots_and_children_follow_parent_pointers_in_order(self) -> None:
        self.assertEqual(list(self.provider.roots(self.doc_id)), ["sec_a", "sec_b"])
        self.assertEqual(list(self.provider.children("sec_a")), ["sec_a1"])
        self.assertEqual(list(self.provider.children("sec_b")), [])
        self.assertEqual(self.provider.parent_id("sec_a1"), "sec_a")

    def test_asset_on_known_section_orphan_dropped(self) -> None:
        units = self.provider.self_units("sec_a")
        self.assertEqual([u.chunk_id for u in units], ["u-a", "u-t1"])
        every = {
            u.chunk_id
            for sid in self.provider.all_section_ids()
            for u in self.provider.self_units(sid)
        }
        self.assertNotIn("u-orphan", every)

    def test_content_is_subtree_in_document_order_with_asset_summary(self) -> None:
        text = self.provider.content("sec_a")
        self.assertLess(text.index("A body"), text.index("T1 summary"))
        self.assertLess(text.index("T1 summary"), text.index("A1 body"))
        self.assertNotIn("B body", text)

    def test_node_meta_path_titles_resolve_path(self) -> None:
        meta = self.provider.node_meta("sec_a")
        self.assertEqual(meta.title, "A")
        self.assertEqual(meta.summary, "sum A")
        self.assertTrue(meta.has_children)
        self.assertEqual(meta.n_chunks, 3)
        self.assertEqual(self.provider.path_titles("sec_a1"), "A / A1")
        self.assertEqual(self.provider.resolve_path("A/A1"), "sec_a1")
        self.assertEqual(self.provider.resolve_path("A / A1"), "sec_a1")
        self.assertEqual(
            self.provider.summaries(),
            {"sec_a": "sum A", "sec_a1": "sum A1", "sec_b": "sum B"},
        )

    def test_adapter_emits_units_keyed_for_map_scoring(self) -> None:
        ts = ProviderToolSpace(self.provider)
        chunks = ts._materialize_leaf_path_chunks("sec_a", self.doc_id)
        self.assertEqual(
            [c.node_id for c in chunks],
            ["sec_a__self", "sec_a1"],
        )


class NamespaceKnowhereProviderTests(unittest.TestCase):
    def setUp(self) -> None:
        self.p_a = KnowhereProvider(
            doc_id="doc_a",
            sections=[
                SectionRow("sec_a_a", None, "A", "A", 1, "sum A", 0),
                SectionRow("sec_a_a1", "sec_a_a", "A / A1", "A1", 2, "sum A1", 1),
                SectionRow("sec_a_b", None, "B", "B", 1, "sum B", 2),
            ],
            units=[
                UnitRow("a-u-a", "sec_a_a", "text", "hydrology rainfall station upstream", 1),
                UnitRow("a-u-a1", "sec_a_a1", "text", "hydrology detail", 2),
                UnitRow("a-u-b", "sec_a_b", "text", "misc note", 3),
            ],
        )
        self.p_b = KnowhereProvider(
            doc_id="doc_b",
            sections=[
                SectionRow("sec_b_a", None, "A", "A", 1, "sum A", 0),
                SectionRow("sec_b_a1", "sec_b_a", "A / A1", "A1", 2, "sum A1", 1),
                SectionRow("sec_b_b", None, "B", "B", 1, "sum B", 2),
            ],
            units=[
                UnitRow("b-u-a", "sec_b_a", "text", "geology rock foundation", 1),
                UnitRow("b-u-a1", "sec_b_a1", "text", "geology detail", 2),
                UnitRow("b-u-b", "sec_b_b", "text", "misc note", 3),
            ],
        )
        self.ns = NamespaceKnowhereProvider(
            [self.p_a, self.p_b],
            titles={"doc_a": "Report A", "doc_b": "Report B"},
        )
        self.ts = ProviderToolSpace(self.ns)

    def test_namespace_root_lists_document_nodes(self) -> None:
        self.assertTrue(uses_document_nodes(self.ts))
        self.assertEqual(self.ts.sections_for_doc(""), ["doc_a", "doc_b"])
        self.assertEqual(self.ns.address_level("doc_a"), NavLevel.DOCUMENT)
        self.assertEqual(self.ns.address_level("sec_a_a"), NavLevel.SECTION)
        self.assertEqual(self.ns.owner_document("sec_a_a1"), "doc_a")
        self.assertEqual(list(self.ns.children("doc_a")), ["sec_a_a", "sec_a_b"])

    def test_document_nodes_are_dispatch_only(self) -> None:
        map_scores, unit_scores = compute_corpus_map_and_unit_scores(
            self.ts, doc_ids=["doc_a", "doc_b"], query="hydrology"
        )
        highlights = select_map_highlights(unit_scores, k=3)
        proj = build_map(
            self.ts,
            doc_id="",
            query="hydrology",
            scope=None,
            config=NavConfig(map_mode=True, map_char_limit=4000, collect_top_k=3),
            map_scores=map_scores,
            highlight_ids=highlights,
        )
        self.assertIn("[Hit]", proj.text)
        self.assertIn("doc_a", map_scores)
        self.assertIn("doc_b", map_scores)
        self.assertGreater(map_scores["doc_a"], map_scores["doc_b"])

        state = NavState(doc_id="", query="hydrology")
        state.map_scores = map_scores
        state.unit_scores = unit_scores
        state.highlight_ids = highlights
        actions = build_legal_actions(
            state, proj, step_idx=0, config=NavConfig(map_mode=True), ts=self.ts
        )
        by_sid = {}
        for act in actions:
            by_sid.setdefault(act.section_id, set()).add(act.kind)
        self.assertIn(ActionKind.DISPATCH, by_sid.get("doc_a", set()))
        self.assertNotIn(ActionKind.COLLECT, by_sid.get("doc_a", set()))
        self.assertIn(ActionKind.DISPATCH, by_sid.get("doc_b", set()))
        self.assertNotIn(ActionKind.COLLECT, by_sid.get("doc_b", set()))


class NormalizePathTests(unittest.TestCase):
    def test_slash_variants(self) -> None:
        self.assertEqual(normalize_section_path("a/b"), "a / b")
        self.assertEqual(normalize_section_path("a / b"), "a / b")

    def test_root_path_normalizes_empty(self) -> None:
        from nav_knowhere import ROOT_SECTION_PATH

        self.assertEqual(normalize_section_path(ROOT_SECTION_PATH), "")
        self.assertEqual(normalize_section_path(""), "")


@unittest.skipUnless(
    os.environ.get("KNOWHERE_DB_SMOKE") == "1"
    or os.environ.get("KNOWHERE_DATABASE_URL", "").strip(),
    "set KNOWHERE_DB_SMOKE=1 (or KNOWHERE_DATABASE_URL) to hit local Docker",
)
class KnowhereDbSmokeTests(unittest.TestCase):
    def test_load_changheba_doc1(self) -> None:
        p = load_document_from_db("doc_4b0c671767af")
        self.assertTrue(p.doc_id.startswith("doc_"))
        sid = p.resolve_path("总目录/目录/2.3 水文基本资料")
        # path may live on report2; report1 should still load sec_* keys
        self.assertTrue(all(s.startswith("sec_") for s in p.all_section_ids()[:5]))
        self.assertGreater(len(p.all_section_ids()), 100)
        hit = p.resolve_path("1 综合说明")
        self.assertIsNotNone(hit)
        self.assertTrue(str(hit).startswith("sec_"))


if __name__ == "__main__":
    unittest.main()
