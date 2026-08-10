"""Lock KnowhereProvider's row mapping against a micro parse track."""
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

from nav_actions import build_legal_actions  # noqa: E402
from nav_address import NavLevel, uses_document_nodes  # noqa: E402
from nav_hierarchy import ProviderToolSpace  # noqa: E402
from nav_knowhere import NamespaceKnowhereProvider, load_debug_parse  # noqa: E402
from nav_map_scores import (  # noqa: E402
    compute_corpus_map_and_unit_scores,
    select_map_highlights,
)
from nav_projection import build_map  # noqa: E402
from nav_types import ActionKind, NavConfig, NavState  # noqa: E402


def _write_track(
    base: Path,
    *,
    name: str = "probe",
    body_a: str = "A body [tables/t1.html]",
    body_a1: str = "A1 body",
    body_b: str = "B body",
) -> Path:
    """A track whose doc_nav is wrapped in two filesystem levels, as on disk."""
    track = base / f"{name}.pdf" / "text_track"
    track.mkdir(parents=True)
    anchor = str(track).strip("/")
    wrapper_outer = str(base).strip("/")
    wrapper_inner = str(base / f"{name}.pdf").strip("/")

    def node(title, path, level, summary, children, chunk_count=1):
        return {
            "title": title,
            "path": path,
            "level": level,
            "summary": summary,
            "chunk_count": chunk_count,
            "children": children,
        }

    nav = {
        "file_name": f"{name}.pdf",
        "sections": [
            node(
                base.name,
                wrapper_outer,
                1,
                "",
                [
                    node(
                        f"{name}.pdf",
                        wrapper_inner,
                        2,
                        "",
                        [
                            node(
                                "text_track",
                                anchor,
                                3,
                                "",
                                [
                                    node(
                                        "A",
                                        f"{anchor}/A",
                                        4,
                                        "sum A",
                                        [node("A1", f"{anchor}/A/A1", 5, "sum A1", [])],
                                    ),
                                    node("B", f"{anchor}/B", 4, "sum B", []),
                                ],
                            )
                        ],
                    )
                ],
            )
        ],
    }
    chunks = {
        "chunks": [
            {
                "chunk_id": f"{name}-u-a",
                "type": "text",
                "content": body_a,
                "path": f"/{anchor}/A",
                "metadata": {},
                "order": 1,
            },
            {
                "chunk_id": f"{name}-u-t1",
                "type": "table",
                "content": "tables/t1.html",
                "path": "tables/t1.html",
                "metadata": {"summary": "T1 summary", "asset_title": "T1"},
                "order": 2,
            },
            {
                "chunk_id": f"{name}-u-a1",
                "type": "text",
                "content": body_a1,
                "path": f"/{anchor}/A/A1",
                "metadata": {},
                "order": 3,
            },
            {
                "chunk_id": f"{name}-u-b",
                "type": "text",
                "content": body_b,
                "path": f"/{anchor}/B",
                "metadata": {},
                "order": 4,
            },
            {
                "chunk_id": f"{name}-u-orphan",
                "type": "table",
                "content": "tables/zz.html",
                "path": "tables/zz.html",
                "metadata": {"summary": "unreferenced"},
                "order": 5,
            },
        ]
    }
    (track / "doc_nav.json").write_text(json.dumps(nav), encoding="utf-8")
    (track / "chunks.json").write_text(json.dumps(chunks), encoding="utf-8")
    return track


class KnowhereProviderTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        track = _write_track(Path(self._tmp.name))
        self.provider = load_debug_parse(track)
        self.doc_id = self.provider.doc_id

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_strips_filesystem_wrapper_levels(self) -> None:
        self.assertEqual(self.doc_id, "probe")
        self.assertEqual(
            sorted(self.provider.all_section_ids()),
            sorted([f"{self.doc_id}:A", f"{self.doc_id}:A/A1", f"{self.doc_id}:B"]),
        )

    def test_roots_and_children_follow_parent_pointers_in_order(self) -> None:
        self.assertEqual(
            list(self.provider.roots(self.doc_id)),
            [f"{self.doc_id}:A", f"{self.doc_id}:B"],
        )
        self.assertEqual(
            list(self.provider.children(f"{self.doc_id}:A")), [f"{self.doc_id}:A/A1"]
        )
        self.assertEqual(list(self.provider.children(f"{self.doc_id}:B")), [])
        self.assertEqual(self.provider.parent_id(f"{self.doc_id}:A/A1"), f"{self.doc_id}:A")

    def test_asset_attaches_to_referencing_section_and_orphan_is_dropped(self) -> None:
        units = self.provider.self_units(f"{self.doc_id}:A")
        self.assertEqual(
            [u.chunk_id for u in units],
            [f"{self.doc_id}-u-a", f"{self.doc_id}-u-t1"],
        )
        every = {
            u.chunk_id
            for sid in self.provider.all_section_ids()
            for u in self.provider.self_units(sid)
        }
        self.assertNotIn(f"{self.doc_id}-u-orphan", every)

    def test_content_is_subtree_in_document_order_with_asset_summary(self) -> None:
        # Ordering is strictly sort_order, so an asset owned by A interleaves
        # ahead of A1's body even though A1 sits deeper in the tree.
        text = self.provider.content(f"{self.doc_id}:A")
        self.assertLess(text.index("A body"), text.index("T1 summary"))
        self.assertLess(text.index("T1 summary"), text.index("A1 body"))
        self.assertNotIn("B body", text)

    def test_node_meta_and_path_titles(self) -> None:
        meta = self.provider.node_meta(f"{self.doc_id}:A")
        self.assertEqual(meta.title, "A")
        self.assertEqual(meta.summary, "sum A")
        self.assertTrue(meta.has_children)
        self.assertEqual(meta.n_chunks, 3)  # own text + asset + A1
        self.assertEqual(self.provider.path_titles(f"{self.doc_id}:A/A1"), "A / A1")
        self.assertEqual(
            self.provider.summaries(),
            {
                f"{self.doc_id}:A": "sum A",
                f"{self.doc_id}:A/A1": "sum A1",
                f"{self.doc_id}:B": "sum B",
            },
        )

    def test_adapter_emits_units_keyed_for_map_scoring(self) -> None:
        ts = ProviderToolSpace(self.provider)
        chunks = ts._materialize_leaf_path_chunks(f"{self.doc_id}:A", self.doc_id)
        # One unit per descendant leaf, plus a __self unit because A owns more
        # than one unit of its own — the exact keys build_score_units produces.
        self.assertEqual(
            [c.node_id for c in chunks],
            [f"{self.doc_id}:A__self", f"{self.doc_id}:A/A1"],
        )
        self.assertEqual([min(c.line_ids) for c in chunks], [1, 3])


class NamespaceKnowhereProviderTests(unittest.TestCase):
    """P0.2: namespace root + document DISPATCH-only nodes + fold/[Hit]."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        base = Path(self._tmp.name)
        track_a = _write_track(
            base / "a",
            name="doc_a",
            body_a="hydrology rainfall station upstream",
            body_a1="hydrology detail",
            body_b="misc note",
        )
        track_b = _write_track(
            base / "b",
            name="doc_b",
            body_a="geology rock foundation",
            body_a1="geology detail",
            body_b="misc note",
        )
        self.p_a = load_debug_parse(track_a, doc_id="doc_a")
        self.p_b = load_debug_parse(track_b, doc_id="doc_b")
        self.ns = NamespaceKnowhereProvider(
            [self.p_a, self.p_b],
            titles={"doc_a": "Report A", "doc_b": "Report B"},
        )
        self.ts = ProviderToolSpace(self.ns)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_namespace_root_lists_document_nodes(self) -> None:
        self.assertTrue(uses_document_nodes(self.ts))
        self.assertEqual(self.ts.sections_for_doc(""), ["doc_a", "doc_b"])
        self.assertEqual(self.ns.address_level("doc_a"), NavLevel.DOCUMENT)
        self.assertEqual(self.ns.address_level("doc_a:A"), NavLevel.SECTION)
        self.assertEqual(self.ns.owner_document("doc_a:A/A1"), "doc_a")
        self.assertEqual(list(self.ns.children("doc_a")), ["doc_a:A", "doc_a:B"])

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


if __name__ == "__main__":
    unittest.main()
