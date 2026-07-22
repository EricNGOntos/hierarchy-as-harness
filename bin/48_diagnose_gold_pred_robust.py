#!/usr/bin/env python3
"""Zero-token diagnostics for Gold/Pred robust-navigation work."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean
from typing import Any


TASK_TYPES = ("niche_fact", "multi_hop", "scope_collection")


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _read_jsonl_groups(path: Path) -> dict[str, list[dict[str, Any]]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        groups[str(row["doc_id"])].append(row)
    for doc_id in groups:
        groups[doc_id].sort(key=lambda row: int(row.get("line_id", 0)))
    return dict(groups)


def _parents(levels: list[int]) -> list[int | None]:
    stack: list[tuple[int, int]] = [(-1, -1)]
    out: list[int | None] = []
    for idx, level in enumerate(levels):
        while len(stack) > 1 and stack[-1][1] >= level:
            stack.pop()
        parent = stack[-1][0]
        out.append(parent if parent >= 0 else None)
        stack.append((idx, level))
    return out


def _line_id_from_node(node_id: str) -> int | None:
    match = re.search(r":L(\d+)$", str(node_id))
    return int(match.group(1)) if match else None


def _metric(row: dict[str, Any], arm: str, metric: str, tree_by_id: dict[str, dict[str, Any]]) -> float:
    if arm == "treerag":
        return float(tree_by_id[str(row["inspect_id"])]["treerag"].get(metric, 0.0) or 0.0)
    key = {"gold": "hierarchical_gold", "pred": "hierarchical_pred", "flat": "flat"}[arm]
    return float(row[key]["metrics"].get(metric, 0.0) or 0.0)


def _quality(
    gold_rows: list[dict[str, Any]],
    pred_by_id: dict[str, dict[str, Any]],
    tree_by_id: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    rows = [{**row, "hierarchical_pred": pred_by_id[str(row["inspect_id"])]["hierarchical_pred"]} for row in gold_rows]
    out: dict[str, Any] = {"overall": {}, "per_type": {}}
    for arm in ("gold", "pred", "treerag", "flat"):
        out["overall"][arm] = {
            "score_task": mean(_metric(row, arm, "score_task", tree_by_id) for row in rows),
            "score_evidence": mean(_metric(row, arm, "score_evidence", tree_by_id) for row in rows),
        }
    for task_type in TASK_TYPES:
        subset = [row for row in rows if row.get("task_type") == task_type]
        out["per_type"][task_type] = {
            "n": len(subset),
            **{
                arm: {
                    "score_task": mean(_metric(row, arm, "score_task", tree_by_id) for row in subset),
                    "score_evidence": mean(_metric(row, arm, "score_evidence", tree_by_id) for row in subset),
                }
                for arm in ("gold", "pred", "treerag", "flat")
            },
        }
    return out


def _pairwise(
    gold_rows: list[dict[str, Any]],
    pred_by_id: dict[str, dict[str, Any]],
    tree_by_id: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    rows = [{**row, "hierarchical_pred": pred_by_id[str(row["inspect_id"])]["hierarchical_pred"]} for row in gold_rows]
    out: dict[str, Any] = {}
    for metric in ("score_task", "score_evidence"):
        out[metric] = {}
        for left, right in (
            ("gold", "pred"),
            ("gold", "treerag"),
            ("gold", "flat"),
            ("pred", "treerag"),
            ("pred", "flat"),
            ("treerag", "flat"),
        ):
            key = f"{left}_minus_{right}"
            diffs = [_metric(row, left, metric, tree_by_id) - _metric(row, right, metric, tree_by_id) for row in rows]
            out[metric][key] = {
                "mean": mean(diffs),
                "positive": sum(value > 0 for value in diffs),
                "negative": sum(value < 0 for value in diffs),
                "ties": sum(value == 0 for value in diffs),
            }
    return out


def _action_stats(rows: list[dict[str, Any]], arm_key: str) -> dict[str, Any]:
    overall: Counter[str] = Counter()
    by_type: dict[str, Counter[str]] = defaultdict(Counter)
    for row in rows:
        task_type = str(row.get("task_type") or "unknown")
        steps = list((row.get(arm_key) or {}).get("steps") or [])
        overall["episodes"] += 1
        overall["steps"] += len(steps)
        by_type[task_type]["episodes"] += 1
        by_type[task_type]["steps"] += len(steps)
        for step in steps:
            action = str(step.get("action") or "")
            detail = step.get("detail") or {}
            overall[action] += 1
            by_type[task_type][action] += 1
            if action == "nav_collect":
                if int(detail.get("n_added", 0) or 0) == 0:
                    overall["zero_collect"] += 1
                    by_type[task_type]["zero_collect"] += 1
                overall[f"collect_{str(detail.get('action_id') or '')[:1]}"] += 1
                by_type[task_type][f"collect_{str(detail.get('action_id') or '')[:1]}"] += 1
            if action == "nav_search" and int(detail.get("n_added", 0) or 0) == 0:
                overall["zero_search"] += 1
                by_type[task_type]["zero_search"] += 1
    return {
        "overall": dict(overall),
        "per_type": {task_type: dict(counter) for task_type, counter in sorted(by_type.items())},
    }


def _structure_diagnostics(
    corpus_path: Path,
    pred_path: Path,
    gold_rows: list[dict[str, Any]],
    pred_by_id: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    corpus = _read_jsonl_groups(corpus_path)
    pred = _read_jsonl_groups(pred_path)
    line_parent: dict[tuple[str, int], tuple[int | None, int | None, int, int]] = {}
    stats: Counter[str] = Counter()
    root_bad_docs: set[str] = set()
    jump_docs: set[str] = set()
    top_coverage: dict[str, set[int]] = {}

    for doc_id, rows in corpus.items():
        pred_by_line = {int(row["line_id"]): row for row in pred.get(doc_id, [])}
        gold_levels = [int(row.get("gold_level", 0) or 0) for row in rows]
        pred_levels = [
            int(pred_by_line.get(int(row["line_id"]), {}).get("predicted_level", 0) or 0)
            for row in rows
        ]
        gold_parents = _parents(gold_levels)
        pred_parents = _parents(pred_levels)
        if pred_levels and pred_levels[0] != 0:
            root_bad_docs.add(doc_id)
        for idx in range(1, len(pred_levels)):
            if pred_levels[idx] > pred_levels[idx - 1] + 1:
                jump_docs.add(doc_id)
                stats["upward_jump_violations"] += 1
        for idx, row in enumerate(rows):
            line_id = int(row["line_id"])
            gold_parent = None if gold_parents[idx] is None else int(rows[gold_parents[idx]]["line_id"])
            pred_parent = None if pred_parents[idx] is None else int(rows[pred_parents[idx]]["line_id"])
            line_parent[(doc_id, line_id)] = (gold_parent, pred_parent, gold_levels[idx], pred_levels[idx])
            stats["lines"] += 1
            stats["level_exact"] += int(gold_levels[idx] == pred_levels[idx])
            stats["parent_exact"] += int(gold_parent == pred_parent)
            stats["level_abs_error"] += abs(gold_levels[idx] - pred_levels[idx])

        anchors = [idx for idx, level in enumerate(pred_levels) if level == 1]
        if not anchors and rows:
            anchors = [0]
        covered: set[int] = set()
        for pos, start in enumerate(anchors):
            end = anchors[pos + 1] if pos + 1 < len(anchors) else len(rows)
            covered.update(int(row["line_id"]) for row in rows[start:end])
        top_coverage[doc_id] = covered
        stats["top_coverage_missing_lines"] += len(rows) - len(covered)
        stats["top_coverage_missing_docs"] += int(len(rows) != len(covered))

    task_line_stats: dict[str, Counter[str]] = defaultdict(Counter)
    for row in gold_rows:
        task_type = str(row.get("task_type") or "unknown")
        task_miss = 0
        for node_id in row.get("gold_nodes") or []:
            line_id = _line_id_from_node(str(node_id))
            if line_id is None:
                continue
            key = (str(row["doc_id"]), line_id)
            if key not in line_parent:
                continue
            gold_parent, pred_parent, gold_level, pred_level = line_parent[key]
            for bucket in ("ALL", task_type):
                task_line_stats[bucket]["lines"] += 1
                task_line_stats[bucket]["level_exact"] += int(gold_level == pred_level)
                task_line_stats[bucket]["parent_exact"] += int(gold_parent == pred_parent)
            if line_id not in top_coverage.get(str(row["doc_id"]), set()):
                task_miss += 1
        pred_metrics = pred_by_id[str(row["inspect_id"])]["hierarchical_pred"]["metrics"]
        for bucket in ("ALL", task_type):
            task_line_stats[bucket]["tasks"] += 1
            task_line_stats[bucket]["top_miss_tasks"] += int(task_miss > 0)
            task_line_stats[bucket]["pred_score_task_sum"] += float(pred_metrics.get("score_task", 0.0) or 0.0)
            task_line_stats[bucket]["pred_score_evidence_sum"] += float(pred_metrics.get("score_evidence", 0.0) or 0.0)

    return {
        "corpus": {
            "lines": stats["lines"],
            "level_exact_rate": stats["level_exact"] / max(1, stats["lines"]),
            "parent_exact_rate": stats["parent_exact"] / max(1, stats["lines"]),
            "level_mae": stats["level_abs_error"] / max(1, stats["lines"]),
            "root_bad_docs": len(root_bad_docs),
            "upward_jump_docs": len(jump_docs),
            "upward_jump_violations": stats["upward_jump_violations"],
            "top_coverage_missing_lines": stats["top_coverage_missing_lines"],
            "top_coverage_missing_docs": stats["top_coverage_missing_docs"],
        },
        "task_gold_lines": {
            bucket: {
                "lines": counter["lines"],
                "level_exact_rate": counter["level_exact"] / max(1, counter["lines"]),
                "parent_exact_rate": counter["parent_exact"] / max(1, counter["lines"]),
                "tasks": counter["tasks"],
                "top_miss_tasks": counter["top_miss_tasks"],
                "pred_score_task": counter["pred_score_task_sum"] / max(1, counter["tasks"]),
                "pred_score_evidence": counter["pred_score_evidence_sum"] / max(1, counter["tasks"]),
            }
            for bucket, counter in sorted(task_line_stats.items())
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gold-flat", type=Path, default=Path("results/latest_clean400_task_doc_v3_flat_b500.json"))
    parser.add_argument("--pred", type=Path, default=Path("results/latest_clean400_goldpred_robust_v1_pred_b500.json"))
    parser.add_argument("--treerag", type=Path, default=Path("results/latest_clean400_task_doc_v3_treerag_b500.json"))
    parser.add_argument("--corpus", type=Path, default=Path("data/corpus/test_data_full_realdata_clean_latest.jsonl"))
    parser.add_argument("--pred-jsonl", type=Path, default=Path("data/realdata_clean_m1024_best_pred_levels_prevline_fallback.jsonl"))
    parser.add_argument("--out-json", type=Path, default=Path("results/gold_pred_robust_v1_diagnostics.json"))
    parser.add_argument("--out-md", type=Path, default=Path("results/gold_pred_robust_v1_diagnostics.md"))
    args = parser.parse_args()

    gold_flat = _read_json(args.gold_flat)
    pred = _read_json(args.pred)
    treerag = _read_json(args.treerag)
    gold_rows = gold_flat.get("rows") or []
    pred_rows = pred.get("rows") or []
    tree_rows = treerag.get("rows") or []
    pred_by_id = {str(row.get("inspect_id")): row for row in pred_rows}
    tree_by_id = {str((row.get("treerag") or {}).get("inspect_id")): row for row in tree_rows}
    if len(gold_rows) != len(pred_rows) or len(gold_rows) != len(tree_rows):
        raise RuntimeError("result files are not row-count aligned")

    report = {
        "inputs": {
            "gold_flat": str(args.gold_flat),
            "pred": str(args.pred),
            "treerag": str(args.treerag),
            "corpus": str(args.corpus),
            "pred_jsonl": str(args.pred_jsonl),
        },
        "quality": _quality(gold_rows, pred_by_id, tree_by_id),
        "pairwise": _pairwise(gold_rows, pred_by_id, tree_by_id),
        "actions": {
            "gold": _action_stats(gold_rows, "hierarchical_gold"),
            "pred": _action_stats(pred_rows, "hierarchical_pred"),
        },
        "pred_structure": _structure_diagnostics(args.corpus, args.pred_jsonl, gold_rows, pred_by_id),
    }
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    q = report["quality"]
    lines = [
        "# Gold/Pred Robust-v1 Diagnostics",
        "",
        "## Current Quality",
        "",
        "| Method | Overall | Niche | Multi-hop | Scope | Evidence |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for arm, label in (("gold", "Gold Nav"), ("pred", "Pred Nav"), ("treerag", "TreeRAG"), ("flat", "Flat")):
        lines.append(
            f"| {label} | {q['overall'][arm]['score_task']:.4f} | "
            f"{q['per_type']['niche_fact'][arm]['score_task']:.4f} | "
            f"{q['per_type']['multi_hop'][arm]['score_task']:.4f} | "
            f"{q['per_type']['scope_collection'][arm]['score_task']:.4f} | "
            f"{q['overall'][arm]['score_evidence']:.4f} |"
        )
    struct = report["pred_structure"]["corpus"]
    lines.extend([
        "",
        "## Pred Structure",
        "",
        f"- Level exact: `{struct['level_exact_rate']:.4f}`; parent exact: `{struct['parent_exact_rate']:.4f}`; level MAE: `{struct['level_mae']:.4f}`.",
        f"- Root-bad docs: `{struct['root_bad_docs']}`; upward-jump docs: `{struct['upward_jump_docs']}`; upward-jump violations: `{struct['upward_jump_violations']}`.",
        f"- Top-level coverage missing lines: `{struct['top_coverage_missing_lines']}` across `{struct['top_coverage_missing_docs']}` docs.",
        "",
        "## Action Waste",
        "",
    ])
    for arm in ("gold", "pred"):
        a = report["actions"][arm]["overall"]
        lines.append(
            f"- `{arm}`: search `{a.get('nav_search', 0)}`, zero-search `{a.get('zero_search', 0)}`; "
            f"collect `{a.get('nav_collect', 0)}`, zero-collect `{a.get('zero_collect', 0)}`."
        )
    lines.extend([
        "",
        "## Artifacts",
        "",
        f"- `{args.out_json}`",
    ])
    args.out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"json": str(args.out_json), "markdown": str(args.out_md)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
