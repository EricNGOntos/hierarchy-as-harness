from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
for source_dir in (ROOT / "src" / "realdata", ROOT / "src" / "nav"):
    if str(source_dir) not in sys.path:
        sys.path.insert(0, str(source_dir))

from agent_delivery.code.index_retrieval import Chunk  # noqa: E402
from knowhere_hybrid import (  # noqa: E402
    fuse_channel_bm25_dense,
    rank_rows_by_bm25,
    score_dense_channel,
    score_rows_hybrid_all,
)
from nav_agent import (  # noqa: E402
    _collect_in_doc_order,
    _unit_score_for_evidence_chunk,
)
from nav_types import NavConfig  # noqa: E402


class DenseChannelTests(unittest.TestCase):
    def tearDown(self) -> None:
        os.environ.pop("NAV_MAP_DENSE", None)
        os.environ.pop("NAV_MAP_DENSE_MOCK", None)
        os.environ.pop("NAV_MAP_CHANNEL_DENSE_WEIGHT", None)

    def test_dense_disabled_returns_none(self) -> None:
        os.environ["NAV_MAP_DENSE"] = "0"
        self.assertIsNone(score_dense_channel(["path a", "path b"], "query"))

    def test_dense_mock_overlap(self) -> None:
        with mock.patch.dict(
            os.environ,
            {"NAV_MAP_DENSE": "1", "NAV_MAP_DENSE_MOCK": "1"},
        ):
            scores = score_dense_channel(
                ["alpha beta gamma", "zzz unrelated"],
                "alpha beta",
            )
        self.assertIsNotNone(scores)
        assert scores is not None
        self.assertGreater(scores[0], scores[1])

    def test_fuse_changes_ordering_with_dense(self) -> None:
        unit_ids = ["a", "b"]
        bm25 = {"a": 1.0, "b": 0.9}
        dense = {"a": 0.1, "b": 1.0}
        with mock.patch.dict(os.environ, {"NAV_MAP_CHANNEL_DENSE_WEIGHT": "1.0"}):
            fused = fuse_channel_bm25_dense(bm25, dense, unit_ids)
        self.assertGreater(fused["b"], fused["a"])

    def test_hybrid_all_uses_mock_dense(self) -> None:
        rows = [
            {
                "chunk_id": "u1",
                "path_search_text": "alpha path",
                "content_search_text": "alpha body",
                "term_search_text": "alpha body",
                "path_text": "alpha path",
                "content": "alpha body",
            },
            {
                "chunk_id": "u2",
                "path_search_text": "zzz path",
                "content_search_text": "zzz body",
                "term_search_text": "zzz body",
                "path_text": "zzz path",
                "content": "zzz body",
            },
        ]
        with mock.patch.dict(
            os.environ,
            {"NAV_MAP_DENSE": "1", "NAV_MAP_DENSE_MOCK": "1"},
        ):
            scored = score_rows_hybrid_all(
                rows,
                "alpha",
                path_texts={"u1": "alpha path", "u2": "zzz path"},
                content_texts={"u1": "alpha body", "u2": "zzz body"},
            )
        by_id = {r["chunk_id"]: float(r["score"]) for r in scored}
        self.assertGreater(by_id["u1"], by_id["u2"])

    def test_bm25_idf_uses_complete_input_pool(self) -> None:
        rows = [
            {"chunk_id": "hit", "path_search_text": "alpha target"},
            {"chunk_id": "miss", "path_search_text": "background only"},
        ]

        class FakeBM25:
            seen_corpus = None

            def __init__(self, corpus):
                FakeBM25.seen_corpus = corpus

            def get_scores(self, query_tokens):
                del query_tokens
                return [2.0, 0.0]

        with mock.patch("rank_bm25.BM25Okapi", FakeBM25):
            ranked = rank_rows_by_bm25(
                rows,
                ["alpha"],
                search_field="path_search_text",
            )

        self.assertEqual(
            FakeBM25.seen_corpus,
            [["alpha", "target"], ["background", "only"]],
        )
        self.assertEqual([row["chunk_id"] for row in ranked], ["hit", "miss"])


class CollectHydrationTests(unittest.TestCase):
    def test_unit_score_for_path_and_intro(self) -> None:
        scores = {"doc:L3": 0.8, "doc:L1__self": 0.5}
        path = Chunk(
            node_id="doc:L3__path",
            doc_id="doc",
            text="x",
            line_ids=(3,),
            section_id="doc:L1",
        )
        intro = Chunk(
            node_id="doc:L1__intro",
            doc_id="doc",
            text="y",
            line_ids=(1,),
            section_id="doc:L1",
        )
        self.assertAlmostEqual(_unit_score_for_evidence_chunk(path, scores), 0.8)
        self.assertAlmostEqual(_unit_score_for_evidence_chunk(intro, scores), 0.5)
        self_hit = Chunk(
            node_id="doc:L1__self",
            doc_id="doc",
            text="z",
            line_ids=(1,),
            section_id="doc:L1",
        )
        self.assertAlmostEqual(_unit_score_for_evidence_chunk(self_hit, scores), 0.5)
        # Prefer __self key; fall back to bare section id when missing.
        self_fallback = Chunk(
            node_id="doc:L3__self",
            doc_id="doc",
            text="w",
            line_ids=(3,),
            section_id="doc:L3",
        )
        self.assertAlmostEqual(
            _unit_score_for_evidence_chunk(self_fallback, scores), 0.8
        )

    def test_collect_hydrates_all_chunks_in_doc_order(self) -> None:
        pool = [
            Chunk(
                node_id="doc:L9__path",
                doc_id="doc",
                text="later",
                line_ids=(9,),
                section_id="doc:L1",
            ),
            Chunk(
                node_id="doc:L2__path",
                doc_id="doc",
                text="earlier",
                line_ids=(2,),
                section_id="doc:L1",
            ),
        ]
        cfg = NavConfig(collect_k=1, read_score_bonus=0.0)
        hydrated = _collect_in_doc_order(pool, cfg)
        self.assertEqual(
            [chunk.node_id for chunk, _score in hydrated],
            ["doc:L2__path", "doc:L9__path"],
        )

    def test_emergency_guard_removed(self) -> None:
        import nav_agent

        self.assertFalse(hasattr(nav_agent, "_emergency_guard_collect"))
        self.assertFalse(hasattr(nav_agent, "_search_doc"))


class MapUnitDiskCacheTests(unittest.TestCase):
    def test_l2_normalize_zeros_nan_without_blowup(self) -> None:
        import numpy as np
        from agent_delivery.code.embedding_backend import l2_normalize_rows

        mat = np.asarray(
            [
                [3.0, 4.0, 0.0],  # → unit
                [0.0, 0.0, 0.0],  # stay zero
                [np.nan, 1.0, 0.0],  # nan cleared → then normalize or zero
            ],
            dtype=np.float32,
        )
        out = l2_normalize_rows(mat, label="test")
        self.assertTrue(np.isfinite(out).all())
        self.assertAlmostEqual(float(np.linalg.norm(out[0])), 1.0, places=5)
        self.assertTrue(np.allclose(out[1], 0.0))
        # After zeroing nan cell, row becomes [0,1,0] → unit
        self.assertAlmostEqual(float(np.linalg.norm(out[2])), 1.0, places=5)

    def test_labeled_cache_reencodes_nonfinite_rows(self) -> None:
        import tempfile
        from pathlib import Path

        import numpy as np
        from agent_delivery.code.embedding_backend import encode_labeled_texts_normalized

        class _FakeEnc:
            model_name = "fake-emb"
            calls = 0

            def encode(self, texts, convert_to_numpy=True, batch_size=10, show_progress_bar=False):
                del convert_to_numpy, batch_size, show_progress_bar
                self.calls += 1
                return np.asarray(
                    [[float(len(t)), 1.0, 0.0, 0.0] for t in texts],
                    dtype=np.float32,
                )

        enc = _FakeEnc()
        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch.dict(
                os.environ,
                {
                    "BODYRICH_EMBEDDING_CACHE": "1",
                    "BODYRICH_EMBEDDING_CACHE_DIR": tmp,
                    "BODYRICH_EMBEDDING_BACKEND": "remote",
                },
            ):
                encode_labeled_texts_normalized(
                    enc,
                    doc_id="docB",
                    channel="content",
                    unit_ids=["u1", "u2"],
                    texts=["aa", "bb"],
                    namespace="default",
                )
                self.assertEqual(enc.calls, 1)
                cache = list(Path(tmp).rglob("content.npz"))[0]
                data = np.load(cache, allow_pickle=True)
                emb = np.array(data["embeddings"], dtype=np.float32, copy=True)
                emb[0] = np.nan
                np.savez_compressed(
                    cache,
                    unit_ids=data["unit_ids"],
                    text_sha1=data["text_sha1"],
                    embeddings=emb,
                )
                encode_labeled_texts_normalized(
                    enc,
                    doc_id="docB",
                    channel="content",
                    unit_ids=["u1", "u2"],
                    texts=["aa", "bb"],
                    namespace="default",
                )
                # u1 bad → re-encode; u2 hit → one encode call for the miss slice
                self.assertEqual(enc.calls, 2)

    def test_labeled_cache_persists_and_skips_reencode(self) -> None:
        import tempfile
        from pathlib import Path

        import numpy as np
        from agent_delivery.code.embedding_backend import encode_labeled_texts_normalized

        class _FakeEnc:
            model_name = "fake-emb"
            calls = 0

            def encode(self, texts, convert_to_numpy=True, batch_size=10, show_progress_bar=False):
                del convert_to_numpy, batch_size, show_progress_bar
                self.calls += 1
                # 4-d vectors from text length
                return np.asarray(
                    [[float(len(t)), 1.0, 0.0, 0.0] for t in texts],
                    dtype=np.float32,
                )

        enc = _FakeEnc()
        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch.dict(
                os.environ,
                {
                    "BODYRICH_EMBEDDING_CACHE": "1",
                    "BODYRICH_EMBEDDING_CACHE_DIR": tmp,
                    "BODYRICH_EMBEDDING_BACKEND": "remote",
                },
            ):
                mat1 = encode_labeled_texts_normalized(
                    enc,
                    doc_id="docA",
                    channel="path",
                    unit_ids=["u1", "u2"],
                    texts=["hello", "world"],
                    namespace="gold",
                )
                self.assertEqual(enc.calls, 1)
                self.assertEqual(mat1.shape[0], 2)
                cache = list(Path(tmp).rglob("path.npz"))
                self.assertTrue(cache)
                self.assertIn("gold", str(cache[0]))
                mat2 = encode_labeled_texts_normalized(
                    enc,
                    doc_id="docA",
                    channel="path",
                    unit_ids=["u1", "u2"],
                    texts=["hello", "world"],
                    namespace="gold",
                )
                self.assertEqual(enc.calls, 1)  # full hit
                self.assertTrue(np.allclose(mat1, mat2))
                # change one text → only that miss re-encodes
                mat3 = encode_labeled_texts_normalized(
                    enc,
                    doc_id="docA",
                    channel="path",
                    unit_ids=["u1", "u2"],
                    texts=["hello", "WORLD2"],
                    namespace="gold",
                )
                self.assertEqual(enc.calls, 2)
                self.assertFalse(np.allclose(mat1[1], mat3[1]))


if __name__ == "__main__":
    unittest.main()
