"""NavAddress level registry — no string-suffix parsing."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src" / "nav"))

from nav_address import (  # noqa: E402
    NavAddress,
    NavLevel,
    address_level,
    is_dispatch_only_level,
    is_dispatch_only_node,
    namespace_root,
    owner_document,
    uses_document_nodes,
)


class _Provider:
    def __init__(self) -> None:
        self._levels = {
            "doc-a": NavLevel.DOCUMENT,
            "sec-1": NavLevel.SECTION,
            "chk-1": NavLevel.CHUNK,
        }
        self._owners = {
            "doc-a": "doc-a",
            "sec-1": "doc-a",
            "chk-1": "doc-a",
        }

    def address_level(self, node_id: str):
        return self._levels.get(node_id)

    def owner_document(self, node_id: str):
        return self._owners.get(node_id)

    def document_ids(self):
        return ["doc-a"]


class NavAddressTests(unittest.TestCase):
    def test_namespace_root_is_empty_id(self) -> None:
        root = namespace_root()
        self.assertEqual(root.level, NavLevel.NAMESPACE)
        self.assertEqual(root.id, "")

    def test_dispatch_only_levels(self) -> None:
        self.assertTrue(is_dispatch_only_level(NavLevel.NAMESPACE))
        self.assertTrue(is_dispatch_only_level(NavLevel.DOCUMENT))
        self.assertFalse(is_dispatch_only_level(NavLevel.SECTION))
        self.assertFalse(is_dispatch_only_level(NavLevel.CHUNK))

    def test_level_and_owner_from_provider_toolspace(self) -> None:
        ts = SimpleNamespace(_provider=_Provider())
        self.assertEqual(address_level(ts, "doc-a"), NavLevel.DOCUMENT)
        self.assertEqual(address_level(ts, "sec-1"), NavLevel.SECTION)
        self.assertEqual(address_level(ts, ""), NavLevel.NAMESPACE)
        self.assertTrue(is_dispatch_only_node(ts, "doc-a"))
        self.assertFalse(is_dispatch_only_node(ts, "sec-1"))
        self.assertEqual(owner_document(ts, "sec-1"), "doc-a")
        self.assertTrue(uses_document_nodes(ts))

    def test_address_frozen(self) -> None:
        addr = NavAddress(NavLevel.SECTION, "  sec-1  ")
        self.assertEqual(addr.id, "sec-1")


if __name__ == "__main__":
    unittest.main()
