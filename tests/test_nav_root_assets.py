"""Root section assets: remount via connect_to; no COLLECT / SEARCH owner dump."""
from __future__ import annotations

import sys
import unittest

ROOT = __import__("pathlib").Path(__file__).resolve().parents[1]
for _p in (ROOT / "src" / "realdata", ROOT / "src" / "nav"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from nav_actions import build_legal_actions  # noqa: E402
from nav_assets import gather_scoped_asset_candidates  # noqa: E402
from nav_hierarchy import ProviderToolSpace  # noqa: E402
from nav_knowhere import (  # noqa: E402
    KnowhereProvider,
    ROOT_SECTION_PATH,
    SectionRow,
    UnitRow,
    is_root_section,
)
from nav_projection import build_map  # noqa: E402
from nav_types import ActionKind, NavConfig, NavState  # noqa: E402


def make_root_asset_provider() -> KnowhereProvider:
    """Root holds image+table FK; host text points at them via connect_to."""
    sections = [
        SectionRow("sec_root", None, ROOT_SECTION_PATH, "Root", 0, "", 0),
        SectionRow("sec_host", None, "工程设计证书", "工程设计证书", 1, "sum host", 1),
        SectionRow("sec_other", None, "其它", "其它", 1, "sum other", 2),
    ]
    long_summary = "x" * 5000
    units = [
        UnitRow(
            "u-host-text",
            "sec_host",
            "text",
            "host body with figures",
            1,
            metadata={
                "connect_to": [
                    {"target": "u-root-img"},
                    {"target": "u-root-tbl"},
                ]
            },
        ),
        UnitRow("u-other-text", "sec_other", "text", "other body", 2),
        UnitRow(
            "u-root-img",
            "sec_root",
            "image",
            "images/geo.png",
            3,
            file_path="images/geo.png",
            metadata={
                "summary": long_summary,
                "asset_title": "地理位置示意图",
            },
        ),
        UnitRow(
            "u-root-tbl",
            "sec_root",
            "table",
            "tables/cert.html",
            4,
            file_path="tables/cert.html",
            metadata={"summary": "cert table " + ("y" * 2000), "asset_title": "证书表"},
        ),
        # Unresolved Root asset: no connect_to → discarded from evidence surface.
        UnitRow(
            "u-root-orphan",
            "sec_root",
            "image",
            "images/orphan.png",
            5,
            file_path="images/orphan.png",
            metadata={"summary": "orphan dump " + ("z" * 3000)},
        ),
        UnitRow("u-root-text", "sec_root", "text", "brief front matter", 0),
    ]
    return KnowhereProvider(doc_id="doc_root_probe", sections=sections, units=units)


class RootRemountTests(unittest.TestCase):
    def setUp(self) -> None:
        self.provider = make_root_asset_provider()
        self.ts = ProviderToolSpace(self.provider)

    def test_is_root_section(self) -> None:
        self.assertTrue(is_root_section(self.provider, "sec_root"))
        self.assertTrue(is_root_section(self.ts, "sec_root"))
        self.assertFalse(is_root_section(self.provider, "sec_host"))

    def test_root_self_units_drop_assets_keep_text(self) -> None:
        root_units = self.provider.self_units("sec_root")
        self.assertEqual([u.chunk_id for u in root_units], ["u-root-text"])
        host_ids = {u.chunk_id for u in self.provider.self_units("sec_host")}
        self.assertEqual(host_ids, {"u-host-text", "u-root-img", "u-root-tbl"})
        every = {
            u.chunk_id
            for sid in self.provider.all_section_ids()
            for u in self.provider.self_units(sid)
        }
        self.assertNotIn("u-root-orphan", every)

    def test_content_root_has_no_asset_dump(self) -> None:
        text = self.provider.content("sec_root")
        self.assertEqual(text, "brief front matter")
        self.assertLess(len(text), 200)
        self.assertNotIn("地理位置示意图", text)
        self.assertNotIn("orphan dump", text)

    def test_collect_host_includes_remounted_assets(self) -> None:
        host_text = self.provider.content("sec_host")
        self.assertIn("host body", host_text)
        self.assertIn("地理位置示意图", host_text)
        self.assertIn("证书表", host_text)


class RootActionsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.provider = make_root_asset_provider()
        self.ts = ProviderToolSpace(self.provider)

    def test_root_has_no_collect_action(self) -> None:
        proj = build_map(
            self.ts,
            doc_id="doc_root_probe",
            query="证书",
            scope=None,
            config=NavConfig(map_mode=True, map_char_limit=4000),
        )
        state = NavState(doc_id="doc_root_probe", query="证书")
        actions = build_legal_actions(
            state, proj, step_idx=0, config=NavConfig(map_mode=True), ts=self.ts
        )
        by_sid: dict = {}
        for act in actions:
            by_sid.setdefault(act.section_id, set()).add(act.kind)
        self.assertNotIn(ActionKind.COLLECT, by_sid.get("sec_root", set()))
        self.assertIn(ActionKind.COLLECT, by_sid.get("sec_host", set()))


class RootSearchTests(unittest.TestCase):
    def setUp(self) -> None:
        self.provider = make_root_asset_provider()
        self.ts = ProviderToolSpace(self.provider)

    def test_search_host_scope_hits_remounted_root_fk(self) -> None:
        imgs = gather_scoped_asset_candidates(
            self.ts, asset_type="image", scope="sec_host", doc_id="doc_root_probe"
        )
        self.assertEqual([a["chunk_id"] for a in imgs], ["u-root-img"])
        self.assertEqual(imgs[0]["owner_section_path"], "工程设计证书")
        tbls = gather_scoped_asset_candidates(
            self.ts, asset_type="table", scope="sec_host", doc_id="doc_root_probe"
        )
        self.assertEqual([a["chunk_id"] for a in tbls], ["u-root-tbl"])

    def test_search_root_scope_yields_no_assets(self) -> None:
        imgs = gather_scoped_asset_candidates(
            self.ts, asset_type="image", scope="sec_root", doc_id="doc_root_probe"
        )
        tbls = gather_scoped_asset_candidates(
            self.ts, asset_type="table", scope="sec_root", doc_id="doc_root_probe"
        )
        self.assertEqual(imgs, [])
        self.assertEqual(tbls, [])

    def test_document_scope_excludes_unresolved_orphan(self) -> None:
        imgs = gather_scoped_asset_candidates(
            self.ts,
            asset_type="image",
            scope="doc_root_probe",
            doc_id="doc_root_probe",
        )
        self.assertEqual([a["chunk_id"] for a in imgs], ["u-root-img"])


if __name__ == "__main__":
    unittest.main()
