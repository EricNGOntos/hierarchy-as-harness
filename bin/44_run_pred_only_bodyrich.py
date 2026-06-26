#!/usr/bin/env python3
"""Run one hierarchical arm for Body-rich RealData tasks.

This keeps Gold/Flat/TreeRAG reusable from existing result files while still
using the same episode, compose, budget-fill, and Inspect judge implementation
as the main runner.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
for source_dir in (ROOT / "src" / "realdata", ROOT / "src" / "nav"):
    if str(source_dir) not in sys.path:
        sys.path.insert(0, str(source_dir))

from agent_delivery.agent.runner_bodyrich import (  # noqa: E402
    _agg_summary,
    _append_row_metrics_to_agg,
    _append_task_checkpoint,
    _apply_setup_cost,
    _checkpoint_signature,
    _configure_bodyrich_task_judge,
    _configure_nav_runtime,
    _cost_snapshot,
    _empty_agg,
    _empty_cost_block,
    _fill_agg,
    _finalize_cost,
    _load_task_checkpoint,
    _load_tasks,
    _numeric_delta,
    _per_type_summary,
    _require_inspect_registry_for_judge,
    _run_timed_arm,
    _validate_task_gold_nodes_in_corpus,
    _write_task_outputs_jsonl,
    default_inspect_task_paths,
    load_inspect_registry,
    run_bodyrich_episode,
)
from agent_delivery.code.embedding_backend import (  # noqa: E402
    DEFAULT_DENSE_EMBEDDING_MODEL,
    resolve_embedding_model,
)
from agent_delivery.code.hierarchical_tools import HierarchicalTools  # noqa: E402
from agent_delivery.code.index_retrieval import CorpusIndex  # noqa: E402
from agent_delivery.code.load_data import bundles_from_paths  # noqa: E402


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _signature(args: argparse.Namespace, embedding_model: str) -> str:
    pred_jsonl = args.pred_jsonl.resolve() if args.pred_jsonl else None
    payload = {
        "adapter": "single_hier_bodyrich_v2",
        "tree_source": args.tree_source,
        "test_jsonl": str(args.test_jsonl.resolve()),
        "tasks": str(args.tasks.resolve()),
        "pred_jsonl": str(pred_jsonl) if pred_jsonl else None,
        "test_sha256": _file_sha256(args.test_jsonl),
        "tasks_sha256": _file_sha256(args.tasks),
        "pred_sha256": _file_sha256(args.pred_jsonl) if args.pred_jsonl else None,
        "budget_chars": int(args.budget_chars),
        "retrieval": args.retrieval,
        "embedding_model": embedding_model,
        "max_docs": int(args.max_docs),
        "max_tasks": int(args.max_tasks),
        "route_m": int(args.route_m),
        "hier_policy": args.hier_policy,
        "inspect_judge": bool(args.inspect_judge),
        "inspect_tasks": [str(p.resolve()) for p in args.inspect_tasks or []],
        "nav_scope_collect_strategy": os.environ.get("NAV_SCOPE_COLLECT_STRATEGY", ""),
        "multihop_evidence_allocation": os.environ.get("MULTIHOP_EVIDENCE_ALLOCATION", ""),
        "multihop_evidence_min_chars_per_hop": os.environ.get(
            "MULTIHOP_EVIDENCE_MIN_CHARS_PER_HOP", ""
        ),
        "nav_synthetic_root_sections": os.environ.get("NAV_SYNTHETIC_ROOT_SECTIONS", ""),
        "nav_synthetic_prefix_min_lines": os.environ.get("NAV_SYNTHETIC_PREFIX_MIN_LINES", ""),
        "nav_hybrid_direct_search": os.environ.get("NAV_HYBRID_DIRECT_SEARCH", ""),
        "nav_hybrid_direct_k": os.environ.get("NAV_HYBRID_DIRECT_K", ""),
        "nav_scope_direct_window_before": os.environ.get("NAV_SCOPE_DIRECT_WINDOW_BEFORE", ""),
        "nav_scope_direct_window_after": os.environ.get("NAV_SCOPE_DIRECT_WINDOW_AFTER", ""),
    }
    text = json.dumps(payload, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _build_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run one hierarchical arm for Body-rich tasks.")
    parser.add_argument("--test-jsonl", type=Path, required=True)
    parser.add_argument("--tasks", type=Path, required=True)
    parser.add_argument("--tree-source", choices=("gold", "pred"), default="pred")
    parser.add_argument("--pred-jsonl", type=Path, default=None)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--retrieval", choices=("dense",), default="dense")
    parser.add_argument("--embedding-model", default=None)
    parser.add_argument("--max-docs", type=int, default=0)
    parser.add_argument("--max-tasks", type=int, default=0)
    parser.add_argument("--budget-chars", type=int, default=500)
    parser.add_argument("--route-m", type=int, default=2)
    parser.add_argument("--hier-policy", choices=("nav", "fixed", "toolspace", "compact"), default="nav")
    parser.add_argument("--nav-config", type=Path, default=None)
    parser.add_argument("--nav-policy", choices=("llm",), default="llm")
    parser.add_argument("--inspect-judge", action="store_true")
    parser.add_argument("--inspect-tasks", action="append", type=Path, default=None)
    parser.add_argument("--task-outputs-jsonl", type=Path, default=None)
    parser.add_argument("--checkpoint-jsonl", type=Path, default=None)
    return parser


def main() -> int:
    args = _build_argparser().parse_args()
    if args.tree_source == "pred" and not args.pred_jsonl:
        raise SystemExit("--tree-source pred requires --pred-jsonl")
    _configure_bodyrich_task_judge()
    if str(args.hier_policy).strip().lower() == "nav":
        _configure_nav_runtime(config_path=args.nav_config, policy=args.nav_policy)
    embedding_model = resolve_embedding_model(args.embedding_model or DEFAULT_DENSE_EMBEDDING_MODEL)

    tasks = _load_tasks(args.tasks)
    if args.max_tasks > 0:
        tasks = tasks[: args.max_tasks]

    kit_root = Path(__file__).resolve().parents[1]
    if args.inspect_judge:
        inspect_paths = list(args.inspect_tasks) if args.inspect_tasks else default_inspect_task_paths(kit_root)
    else:
        inspect_paths = default_inspect_task_paths(kit_root)
    inspect_paths = [p for p in inspect_paths if p.exists()]
    inspect_by_id = load_inspect_registry(inspect_paths) if inspect_paths else None
    _require_inspect_registry_for_judge(
        use_inspect_judge=bool(args.inspect_judge),
        inspect_by_id=inspect_by_id,
        inspect_paths_resolved=inspect_paths,
        kit_root=kit_root,
        tasks=tasks,
    )

    arm_key = "hierarchical_pred" if args.tree_source == "pred" else "hierarchical_gold"
    setup_cost: dict[str, dict[str, float]] = {}
    t0 = time.perf_counter()
    bundles = bundles_from_paths(
        args.test_jsonl,
        tree_source=args.tree_source,
        pred_path=args.pred_jsonl if args.tree_source == "pred" else None,
        max_docs=args.max_docs,
    )
    setup_cost[arm_key] = {"data_load_seconds": time.perf_counter() - t0}
    _validate_task_gold_nodes_in_corpus(
        tasks,
        bundles,
        context=f"{args.tree_source}-only(test_jsonl={args.test_jsonl}, tasks={args.tasks})",
    )
    t0 = time.perf_counter()
    index = CorpusIndex.from_bundles(
        bundles,
        tree_mode="hierarchical",
        retrieval_backend=args.retrieval,
        embedding_model=embedding_model,
    )
    setup_cost[arm_key]["index_build_seconds"] = time.perf_counter() - t0
    tools = HierarchicalTools(index)

    agg = _empty_agg()
    rows: list[dict[str, Any]] = []
    cost: dict[str, Any] = {arm_key: _empty_cost_block()}
    signature = _signature(args, embedding_model)
    checkpoint_rows = _load_task_checkpoint(args.checkpoint_jsonl, signature)
    if checkpoint_rows:
        print(
            f"[checkpoint] resumed {len(checkpoint_rows)}/{len(tasks)} tasks from {args.checkpoint_jsonl}",
            file=sys.stderr,
            flush=True,
        )

    for task_idx, task in enumerate(tasks, start=1):
        resumed = checkpoint_rows.get(task_idx)
        if resumed is not None:
            row = resumed.get("row") if isinstance(resumed, dict) else {}
            if isinstance(row, dict):
                rows.append(row)
                if isinstance(row.get(arm_key), dict):
                    _append_row_metrics_to_agg(agg, row[arm_key])
            if task_idx % 10 == 0 or task_idx == len(tasks):
                print(f"[checkpoint] restored task {task_idx}/{len(tasks)}", file=sys.stderr, flush=True)
            continue

        before = _cost_snapshot(cost)
        episode = _run_timed_arm(
            cost,
            arm_key,
            lambda: run_bodyrich_episode(
                tools,
                task.query,
                doc_id=task.doc_id,
                representation="hierarchical",
                budget_chars=int(args.budget_chars),
                route_m=int(args.route_m),
                hier_policy=args.hier_policy,
                task=task,
                inspect_by_id=inspect_by_id,
                compose_answer=True,
            ),
        )
        metrics = _run_timed_arm(
            cost,
            arm_key,
            lambda: _fill_agg(
                agg,
                episode,
                task,
                hier_policy=args.hier_policy,
                inspect_by_id=inspect_by_id,
                use_inspect_judge=bool(args.inspect_judge),
            ),
        )
        row = {
            "task_idx": task_idx,
            "query": task.query,
            "doc_id": task.doc_id,
            "task_type": task.task_type,
            "gold_nodes": task.gold_nodes,
            "gold_answer": task.gold_answer,
            "inspect_id": getattr(task, "inspect_id", None),
            arm_key: {
                "n_scored_candidates": len(episode.scored_chunks),
                "evidence_chars_actual": episode.evidence_chars_actual,
                "evidence_text": episode.evidence_text,
                "composed_answer": episode.composed_answer,
                "trajectory_length": episode.trajectory_length,
                "truncated_last": episode.truncated_last,
                "section_ids": episode.section_ids,
                "retrieved_nodes": episode.retrieved_nodes,
                "refusal_events": list(episode.refusal_events),
                "metrics": metrics,
                "steps": [step.__dict__ for step in episode.steps],
            },
        }
        rows.append(row)
        _append_task_checkpoint(
            args.checkpoint_jsonl,
            signature,
            row,
            _numeric_delta(_cost_snapshot(cost), before),
        )
        if task_idx % 10 == 0 or task_idx == len(tasks):
            print(f"[checkpoint] saved task {task_idx}/{len(tasks)}", file=sys.stderr, flush=True)

    _apply_setup_cost(cost, setup_cost)
    _finalize_cost(cost)
    summary = {
        "config": {
            "adapter": "single_hier_bodyrich_v2",
            "tree_source": args.tree_source,
            "test_jsonl": str(args.test_jsonl),
            "tasks": str(args.tasks),
            "pred_jsonl": str(args.pred_jsonl) if args.pred_jsonl else None,
            "budget_chars": int(args.budget_chars),
            "hier_policy": args.hier_policy,
            "nav_scope_collect_strategy": os.environ.get("NAV_SCOPE_COLLECT_STRATEGY", ""),
            "nav_synthetic_root_sections": os.environ.get("NAV_SYNTHETIC_ROOT_SECTIONS", "1"),
            "nav_hybrid_direct_search": os.environ.get("NAV_HYBRID_DIRECT_SEARCH", "auto"),
        },
        arm_key: _agg_summary(agg),
        f"per_type_{arm_key}": _per_type_summary(rows, arm_key),
        "cost": cost,
    }
    payload = {"summary": summary, "rows": rows}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.task_outputs_jsonl:
        _write_task_outputs_jsonl(args.task_outputs_jsonl, rows)
    print(f"saved: {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
