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

from nav_hierarchy import ProviderToolSpace  # noqa: E402
from nav_knowhere import load_debug_parse  # noqa: E402


def _write_track(base: Path) -> Path:
    """A track whose doc_nav is wrapped in two filesystem levels, as on disk."""
    track = base / "probe.pdf" / "text_track"
    track.mkdir(parents=True)
    anchor = str(track).strip("/")
    wrapper_outer = str(base).strip("/")
    wrapper_inner = str(base / "probe.pdf").strip("/")

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
        "file_name": "probe.pdf",
        "sections": [
            node(
                base.name,
                wrapper_outer,
                1,
                "",
                [
                    node(
                        "probe.pdf",
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
                "chunk_id": "u-a",
                "type": "text",
                "content": "A body [tables/t1.html]",
                "path": f"/{anchor}/A",
                "metadata": {},
                "order": 1,
            },
            {
                "chunk_id": "u-t1",
                "type": "table",
                "content": "tables/t1.html",
                "path": "tables/t1.html",
                "metadata": {"summary": "T1 summary", "asset_title": "T1"},
                "order": 2,
            },
            {
                "chunk_id": "u-a1",
                "type": "text",
                "content": "A1 body",
                "path": f"/{anchor}/A/A1",
                "metadata": {},
                "order": 3,
            },
            {
                "chunk_id": "u-b",
                "type": "text",
                "content": "B body",
                "path": f"/{anchor}/B",
                "metadata": {},
                "order": 4,
            },
            {
                "chunk_id": "u-orphan",
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
        self.assertEqual([u.chunk_id for u in units], ["u-a", "u-t1"])
        every = {
            u.chunk_id
            for sid in self.provider.all_section_ids()
            for u in self.provider.self_units(sid)
        }
        self.assertNotIn("u-orphan", every)

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


if __name__ == "__main__":
    unittest.main()
