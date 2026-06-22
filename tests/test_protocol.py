from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REALDATA_SRC = ROOT / "src" / "realdata"
if str(REALDATA_SRC) not in sys.path:
    sys.path.insert(0, str(REALDATA_SRC))

from agent_delivery.code.budget_eval import evaluate_at_budget  # noqa: E402
from agent_delivery.code.index_retrieval import Chunk  # noqa: E402
from agent_delivery.code.inspect_scoring import (  # noqa: E402
    build_inspect_pred_output,
    scope_collection_items_score,
    score_sample,
)
from agent_delivery.agent.runner_bodyrich import _finalize_cost  # noqa: E402


def _load_treerag_module():
    path = ROOT / "src" / "treerag" / "eval_arxiv_treerag.py"
    spec = importlib.util.spec_from_file_location("test_treerag_adapter", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class BudgetProtocolTests(unittest.TestCase):
    def test_budget_fill_never_exceeds_character_budget(self) -> None:
        chunks = [
            (Chunk("doc:L1", "doc", "甲" * 80, (1,)), 1.0),
            (Chunk("doc:L2", "doc", "乙" * 80, (2,)), 0.9),
        ]
        result = evaluate_at_budget(chunks, budget_chars=100)
        self.assertEqual(result.evidence_chars_actual, len(result.evidence_text))
        self.assertLessEqual(result.evidence_chars_actual, 100)
        self.assertTrue(result.evidence_text.startswith("[E1]\n"))
        self.assertNotIn("doc:L1", result.evidence_text)

    def test_headers_are_method_neutral_ordinals(self) -> None:
        chunks = [
            (Chunk("doc:L1", "doc", "甲", (1,)), 1.0),
            (Chunk("very-long-doc-id:TREERAG_999", "doc", "乙", (2,)), 0.9),
            (Chunk("another-long-doc-id:FLAT_123", "doc", "丙", (3,)), 0.8),
        ]
        result = evaluate_at_budget(chunks, budget_chars=100)
        self.assertEqual(result.evidence_text, "[E1]\n甲\n\n[E2]\n乙\n\n[E3]\n丙")

    def test_cost_online_response_is_derived_from_phases(self) -> None:
        cost = {"arm": {
            "total_seconds": 10.0,
            "cold_start_seconds": 2.0,
            "retrieval_framework_seconds": 3.0,
            "compose_seconds": 4.0,
            "online_response_seconds": 0.0,
        }}
        _finalize_cost(cost)
        self.assertEqual(cost["arm"]["online_response_seconds"], 7.0)
        self.assertEqual(cost["arm"]["judge_eval_seconds"], 3.0)

    def test_scope_scoring_uses_structured_target_items(self) -> None:
        task = {
            "target": {
                "final_answer": "甲，含内部逗号；乙",
                "table": [{"项": "甲，含内部逗号"}, {"项": "乙"}],
            },
            "metadata": {"task_type": "scope_collection", "gold_line_ids": [1, 2]},
        }
        content, evidence, extra = score_sample(
            task,
            {"items": ["甲，含内部逗号", "乙"], "final_answer": "甲；乙", "evidence_line_ids": [1, 2]},
        )
        self.assertEqual(content, 1.0)
        self.assertEqual(evidence, 1.0)
        self.assertEqual(extra["matched_item_recall"], 1.0)

    def test_scope_item_alignment_does_not_split_internal_commas(self) -> None:
        self.assertEqual(
            scope_collection_items_score(
                ["事故的时间、地点和工程项目有关单位名称", "事故的简要经过"],
                ["事故的时间、地点和工程项目有关单位名称", "事故的简要经过"],
            ),
            1.0,
        )

    def test_scope_compose_mapping_preserves_item_boundaries(self) -> None:
        pred = build_inspect_pred_output(
            '{"task_type":"scope_collection","items":["甲，含逗号","乙"]}',
            evidence_line_ids=[1],
            inspect_task={"metadata": {"task_type": "scope_collection"}},
        )
        self.assertEqual(pred["items"], ["甲，含逗号", "乙"])
        self.assertEqual(pred["final_answer"], "甲，含逗号；乙")

    def test_treerag_metadata_reports_output_not_compute_parity(self) -> None:
        module = _load_treerag_module()
        args = argparse.Namespace(initial_top_k=80, max_traversal_leaves=0)
        metadata = module._fairness_control_metadata(args, candidate_cap_enabled=False)
        self.assertEqual(metadata["candidate_count_matching"], "disabled")
        self.assertFalse(metadata["compute_budget_matched"])
        self.assertIn("evidence_character_budget", metadata["shared_controls"])

    def test_treerag_imports_shared_agent_delivery(self) -> None:
        module = _load_treerag_module()
        imported = Path(sys.modules[module.AgentTask.__module__].__file__).resolve()
        self.assertTrue(imported.is_relative_to(REALDATA_SRC.resolve()), imported)

    def test_shared_chunk_reads_existing_treerag_checkpoint_schema(self) -> None:
        module = _load_treerag_module()
        chunk = module._deserialize_chunk({
            "node_id": "doc:TREERAG_1",
            "doc_id": "doc",
            "text": "证据",
            "line_ids": [1, 2],
            "section_id": "treerag_level_1",
            "text_line_id_groups": [[1], [2]],
        })
        self.assertEqual(chunk.text_line_id_groups, ((1,), (2,)))


class FairCleanTaskTests(unittest.TestCase):
    def test_tasks_are_balanced_and_aligned_with_inspect(self) -> None:
        task_path = ROOT / "data" / "tasks" / "tasks_realdata_bodyrich_fair_clean.jsonl"
        inspect_path = ROOT / "data" / "tasks" / "tasks_realdata_bodyrich_fair_clean.inspect.jsonl"
        tasks = [json.loads(line) for line in task_path.read_text(encoding="utf-8").splitlines() if line]
        inspect = [json.loads(line) for line in inspect_path.read_text(encoding="utf-8").splitlines() if line]
        inspect_by_id = {row["id"]: row for row in inspect}

        self.assertEqual(len(tasks), 51)
        self.assertEqual(Counter(row["task_type"] for row in tasks), {
            "niche_fact": 17,
            "multi_hop": 17,
            "scope_collection": 17,
        })
        self.assertEqual(len({row["query"] for row in tasks}), len(tasks))
        for row in tasks:
            self.assertNotIn("层级路径“", row["query"])
            self.assertEqual(row["query"], inspect_by_id[row["inspect_id"]]["input"])

    def test_scope_gold_nodes_match_inspect_and_logical_table(self) -> None:
        task_path = ROOT / "data" / "tasks" / "tasks_realdata_bodyrich_fair_clean.jsonl"
        inspect_path = ROOT / "data" / "tasks" / "tasks_realdata_bodyrich_fair_clean.inspect.jsonl"
        tasks = [json.loads(line) for line in task_path.read_text(encoding="utf-8").splitlines() if line]
        inspect_by_id = {
            row["id"]: row
            for row in [json.loads(line) for line in inspect_path.read_text(encoding="utf-8").splitlines() if line]
        }
        for task in tasks:
            if task["task_type"] != "scope_collection":
                continue
            inspect = inspect_by_id[task["inspect_id"]]
            target = inspect["target"]
            line_ids = [int(node.rsplit(":L", 1)[1]) for node in task["gold_nodes"]]
            self.assertEqual(line_ids, inspect["metadata"]["gold_line_ids"])
            self.assertEqual(line_ids, target["evidence_line_ids"])
            self.assertEqual(len(target["table"]), target["summary"]["total_items"])
            self.assertLess(len(target["final_answer"]), 500)


if __name__ == "__main__":
    unittest.main()
