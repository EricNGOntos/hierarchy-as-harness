"""Unit tests for task_corpus (42-doc) search scope on Flat / TreeRAG paths."""
from __future__ import annotations

import argparse
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
REALDATA_SRC = ROOT / "src" / "realdata"
if str(REALDATA_SRC) not in sys.path:
    sys.path.insert(0, str(REALDATA_SRC))

from agent_delivery.agent.runner_bodyrich import (  # noqa: E402
    SEARCH_SCOPE_TASK_CORPUS,
    SEARCH_SCOPE_TASK_DOC,
    _doc_ids_from_tasks,
    _episode_doc_id_for_arm,
    _normalize_search_scope,
    _parse_arms,
)
from agent_delivery.agent.types import AgentTask  # noqa: E402
from agent_delivery.code.budget_eval import gather_flat_candidates  # noqa: E402
from agent_delivery.code.hierarchical_tools import HierarchicalTools  # noqa: E402
from agent_delivery.code.index_retrieval import CorpusIndex  # noqa: E402
from agent_delivery.code.load_data import bundles_from_paths  # noqa: E402


def _load_treerag_module():
    path = ROOT / "src" / "treerag" / "eval_arxiv_treerag.py"
    spec = importlib.util.spec_from_file_location("test_search_scope_treerag", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class SearchScopeHelpersTests(unittest.TestCase):
    def test_normalize_and_episode_doc_id(self) -> None:
        self.assertEqual(_normalize_search_scope("task_corpus"), SEARCH_SCOPE_TASK_CORPUS)
        task = AgentTask(
            query="q",
            doc_id="docA",
            gold_nodes=["docA:L1"],
            gold_answer="a",
            task_type="niche_fact",
        )
        self.assertEqual(
            _episode_doc_id_for_arm(
                task, search_scope="task_doc", arm="flat", hier_policy="nav"
            ),
            "docA",
        )
        self.assertIsNone(
            _episode_doc_id_for_arm(
                task, search_scope="task_corpus", arm="flat", hier_policy="nav"
            )
        )
        # nav under task_corpus uses corpus root (doc_id=None + corpus_doc_ids).
        self.assertIsNone(
            _episode_doc_id_for_arm(
                task, search_scope="task_corpus", arm="gold", hier_policy="nav"
            )
        )
        self.assertIsNone(
            _episode_doc_id_for_arm(
                task, search_scope="task_corpus", arm="gold", hier_policy="compact"
            )
        )

    def test_parse_arms(self) -> None:
        self.assertEqual(_parse_arms(None, pred_enabled=False), {"gold", "flat"})
        self.assertEqual(_parse_arms("flat", pred_enabled=False), {"flat"})
        with self.assertRaises(ValueError):
            _parse_arms("pred", pred_enabled=False)


class FlatCorpusScopeTests(unittest.TestCase):
    def test_allowlist_and_global_flat_retrieval(self) -> None:
        tasks_path = ROOT / "data/tasks/tasks_realdata_bodyrich_latest_clean_400.jsonl"
        corpus_path = ROOT / "data/corpus/test_data_full_realdata_clean_latest.jsonl"
        if not tasks_path.exists() or not corpus_path.exists():
            self.skipTest("realdata 400 fixtures missing")

        from agent_delivery.agent.tasks_loader import _load_tasks

        all_tasks = _load_tasks(tasks_path)
        allow = _doc_ids_from_tasks(all_tasks)
        self.assertEqual(len(allow), 42)

        bundles = bundles_from_paths(
            corpus_path,
            tree_source="flat",
            doc_id_allowlist=allow,
        )
        self.assertEqual(len(bundles), 42)

        idx = CorpusIndex.from_bundles(
            bundles,
            tree_mode="flat",
            retrieval_backend="overlap",
            embedding_model="unused",
        )
        tools = HierarchicalTools(idx)
        task = all_tasks[0]
        scored = gather_flat_candidates(tools, task.query, doc_id=None)
        self.assertGreater(len(scored), 0)
        hit_docs = {c.doc_id for c, _ in scored[:64]}
        # With 42-doc pool, top hits need not all be task.doc_id; at least pool spans >1 doc.
        pool_docs = {c.doc_id for c in idx.flat_chunks}
        self.assertEqual(len(pool_docs), 42)
        self.assertGreaterEqual(len(hit_docs), 1)
        self.assertTrue(hit_docs.issubset(pool_docs))


class TreeRagCorpusGatherTests(unittest.TestCase):
    def test_corpus_gather_can_select_other_doc(self) -> None:
        treerag = _load_treerag_module()
        TreeRagDocIndex = treerag.TreeRagDocIndex
        TreeRagNode = treerag.TreeRagNode

        def _one_node_doc(doc_id: str, text: str, emb: list[float]) -> object:
            node = TreeRagNode(
                node_id=f"{doc_id}:TREERAG_1",
                line_id=1,
                level=1,
                text=text,
                title=text[:8],
                embedding_text=text,
                parent_idx=None,
                child_indices=tuple(),
                leaf_indices=(0,),
            )
            return TreeRagDocIndex(
                doc_id=doc_id,
                tree_source="unit",
                nodes=(node,),
                node_id_to_idx={f"{doc_id}:TREERAG_1": 0},
                embeddings=np.asarray([emb], dtype=np.float64),
                cache_key="unit",
            )

        # Query embedding is [1,0]; docB matches perfectly, docA does not.
        docs = {
            "docA": _one_node_doc("docA", "alpha", [0.0, 1.0]),
            "docB": _one_node_doc("docB", "beta unique marker", [1.0, 0.0]),
        }

        class _FakeDense:
            pass

        def _fake_scores(doc_index, query, dense_model):
            del query, dense_model
            return np.asarray(doc_index.embeddings @ np.asarray([1.0, 0.0]), dtype=np.float64)

        args = argparse.Namespace(
            initial_top_k=1,
            root_to_leaf_decay=0.97,
            leaf_to_parent_decay=0.94,
            max_traversal_leaves=0,
        )
        with unittest.mock.patch.object(treerag, "_dense_scores", side_effect=_fake_scores):
            with unittest.mock.patch.object(
                treerag, "_build_retrieval_queries", return_value=["q"]
            ):
                with unittest.mock.patch.object(treerag, "_query_weight", return_value=1.0):
                    scored = treerag._gather_treerag_candidates_corpus(
                        docs,
                        "q",
                        dense_model=_FakeDense(),
                        args=args,
                        use_btr=False,
                    )
        self.assertEqual(len(scored), 1)
        self.assertEqual(scored[0][0].doc_id, "docB")


# late import for patch in TreeRagCorpusGatherTests
import unittest.mock  # noqa: E402


if __name__ == "__main__":
    unittest.main()
