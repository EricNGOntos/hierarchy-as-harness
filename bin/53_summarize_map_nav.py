#!/usr/bin/env python3
"""Summarize Map-Nav arms against baseline Gold Nav + Flat/TreeRAG."""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path
from statistics import mean
from typing import Any


TASK_TYPES = ("niche_fact", "multi_hop", "scope_collection")


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _ci(values: list[float], *, seed: int, samples: int) -> list[float]:
    rng = random.Random(seed)
    n = len(values)
    draws = sorted(sum(values[rng.randrange(n)] for _ in range(n)) / n for _ in range(samples))
    return [draws[int(samples * 0.025)], draws[int(samples * 0.975)]]


def _audit(path: Path) -> dict[str, Any]:
    calls = api_calls = cache_hits = billed_tokens = logical_tokens = 0
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            calls += 1
            cache_hit = bool(row.get("cache_hit"))
            cache_hits += int(cache_hit)
            api_calls += int(not cache_hit)
            billed_tokens += int(((row.get("billed_usage") or {}).get("total_tokens", 0)) or 0)
            logical_tokens += int(((row.get("original_usage") or {}).get("total_tokens", 0)) or 0)
    return {
        "path": str(path),
        "calls": calls,
        "api_calls": api_calls,
        "cache_hits": cache_hits,
        "billed_tokens": billed_tokens,
        "cache_reused_logical_tokens": max(0, logical_tokens - billed_tokens),
    }


def _wall(path: Path) -> dict[str, float]:
    out: dict[str, float] = {}
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            parts = line.split()
            if len(parts) == 2 and parts[0] in {"real", "user", "sys"}:
                out[parts[0]] = float(parts[1])
    return out


def _mean_or_zero(values: list[float]) -> float:
    return mean(values) if values else 0.0


def _pick_arm(row: dict[str, Any], candidates: tuple[str, ...]) -> dict[str, Any]:
    for key in candidates:
        payload = row.get(key)
        if isinstance(payload, dict) and "metrics" in payload:
            return payload
    raise KeyError(f"none of {candidates} found in row keys={list(row.keys())}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--map-gold", type=Path, required=True)
    parser.add_argument("--map-pred", type=Path, required=True)
    parser.add_argument("--baseline-gold", type=Path, required=True)
    parser.add_argument("--flat-source", type=Path, required=True)
    parser.add_argument("--treerag", type=Path, required=True)
    parser.add_argument("--gold-run-root", type=Path, required=True)
    parser.add_argument("--pred-run-root", type=Path, required=True)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    parser.add_argument("--protocol", default="map_nav_v1")
    parser.add_argument("--bootstrap-samples", type=int, default=100000)
    parser.add_argument("--bootstrap-seed", type=int, default=20260625)
    args = parser.parse_args()

    map_gold = _read_json(args.map_gold)
    map_pred = _read_json(args.map_pred)
    baseline_gold = _read_json(args.baseline_gold)
    flat_source = _read_json(args.flat_source)
    treerag = _read_json(args.treerag)

    map_gold_by_id = {str(row.get("inspect_id")): row for row in map_gold.get("rows") or []}
    map_pred_by_id = {str(row.get("inspect_id")): row for row in map_pred.get("rows") or []}
    base_gold_by_id = {str(row.get("inspect_id")): row for row in baseline_gold.get("rows") or []}
    flat_by_id = {str(row.get("inspect_id")): row for row in flat_source.get("rows") or []}
    tree_by_id = {
        str((row.get("treerag") or {}).get("inspect_id")): row for row in treerag.get("rows") or []
    }
    ids = sorted(
        set(map_gold_by_id)
        & set(map_pred_by_id)
        & set(base_gold_by_id)
        & set(flat_by_id)
        & set(tree_by_id)
    )
    if not ids:
        raise RuntimeError("no aligned inspect_id rows across Map/Baseline/Flat/TreeRAG")

    def score(task_id: str, arm: str, metric: str) -> float:
        if arm == "map_gold":
            payload = _pick_arm(
                map_gold_by_id[task_id],
                ("hierarchical_gold_map", "hierarchical_gold"),
            )
            return float(payload["metrics"].get(metric, 0.0) or 0.0)
        if arm == "map_pred":
            payload = _pick_arm(
                map_pred_by_id[task_id],
                ("hierarchical_pred_map", "hierarchical_pred"),
            )
            return float(payload["metrics"].get(metric, 0.0) or 0.0)
        if arm == "baseline_gold":
            payload = _pick_arm(base_gold_by_id[task_id], ("hierarchical_gold",))
            return float(payload["metrics"].get(metric, 0.0) or 0.0)
        if arm == "flat":
            return float(flat_by_id[task_id]["flat"]["metrics"].get(metric, 0.0) or 0.0)
        return float(tree_by_id[task_id]["treerag"].get(metric, 0.0) or 0.0)

    def task_type(task_id: str) -> str:
        return str(
            map_gold_by_id[task_id].get("task_type")
            or base_gold_by_id[task_id].get("task_type")
            or "unknown"
        )

    arms = ("map_gold", "map_pred", "baseline_gold", "treerag", "flat")
    quality: dict[str, Any] = {"overall": {}, "per_type": {}}
    for arm in arms:
        quality["overall"][arm] = {
            "score_task": mean(score(task_id, arm, "score_task") for task_id in ids),
            "score_evidence": mean(score(task_id, arm, "score_evidence") for task_id in ids),
        }
    for tt in TASK_TYPES:
        subset = [task_id for task_id in ids if task_type(task_id) == tt]
        quality["per_type"][tt] = {
            "n": len(subset),
            **{
                arm: {
                    "score_task": _mean_or_zero(
                        [score(task_id, arm, "score_task") for task_id in subset]
                    ),
                    "score_evidence": _mean_or_zero(
                        [score(task_id, arm, "score_evidence") for task_id in subset]
                    ),
                }
                for arm in arms
            },
        }

    comparisons: dict[str, Any] = {}
    for name, left, right in (
        ("map_gold_minus_baseline_gold", "map_gold", "baseline_gold"),
        ("map_gold_minus_treerag", "map_gold", "treerag"),
        ("map_gold_minus_flat", "map_gold", "flat"),
        ("map_pred_minus_flat", "map_pred", "flat"),
        ("map_pred_minus_treerag", "map_pred", "treerag"),
        ("map_gold_minus_map_pred", "map_gold", "map_pred"),
    ):
        diffs = [
            score(task_id, left, "score_task") - score(task_id, right, "score_task")
            for task_id in ids
        ]
        comparisons[name] = {
            "mean": mean(diffs),
            "paired_bootstrap_95_ci": _ci(
                diffs, seed=args.bootstrap_seed, samples=args.bootstrap_samples
            ),
            "positive": sum(value > 0 for value in diffs),
            "negative": sum(value < 0 for value in diffs),
            "ties": sum(value == 0 for value in diffs),
        }

    report = {
        "protocol": args.protocol,
        "integrity": {
            "aligned_inspect_ids": len(ids),
            "map_gold_rows": len(map_gold_by_id),
            "map_pred_rows": len(map_pred_by_id),
            "baseline_gold_rows": len(base_gold_by_id),
            "flat_source_rows": len(flat_by_id),
            "treerag_rows": len(tree_by_id),
            "task_type_counts": {tt: quality["per_type"][tt]["n"] for tt in TASK_TYPES},
        },
        "quality": quality,
        "comparisons": comparisons,
        "cost": {
            "map_gold_wall_time": _wall(args.gold_run_root / "logs" / "gold.time"),
            "map_pred_wall_time": _wall(args.pred_run_root / "logs" / "pred.time"),
            "map_gold_audit": _audit(args.gold_run_root / "llm_call_audit.jsonl"),
            "map_pred_audit": _audit(args.pred_run_root / "llm_call_audit.jsonl"),
            "semantics": "Map-Nav is newly evaluated. Baseline Gold/Flat/TreeRAG are reused by inspect_id.",
        },
        "artifacts": {
            "map_gold": str(args.map_gold),
            "map_pred": str(args.map_pred),
            "baseline_gold": str(args.baseline_gold),
            "flat_source": str(args.flat_source),
            "treerag": str(args.treerag),
        },
    }
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        f"# {args.protocol} · Map-Nav vs baselines",
        "",
        "## Quality",
        "",
        "| Method | Status | Overall | Niche | Multi-hop | Scope | Evidence |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for arm, label, status in (
        ("map_gold", "Gold Map-Nav", "new"),
        ("map_pred", "Pred Map-Nav", "new"),
        ("baseline_gold", "Gold Nav (baseline)", "reused"),
        ("treerag", "TreeRAG", "reused"),
        ("flat", "Flat", "reused"),
    ):
        q = quality["overall"][arm]
        lines.append(
            f"| {label} | {status} | {q['score_task']:.4f} | "
            f"{quality['per_type']['niche_fact'][arm]['score_task']:.4f} | "
            f"{quality['per_type']['multi_hop'][arm]['score_task']:.4f} | "
            f"{quality['per_type']['scope_collection'][arm]['score_task']:.4f} | "
            f"{q['score_evidence']:.4f} |"
        )
    lines.extend(["", "## Paired Bootstrap (score_task)", ""])
    for name, value in comparisons.items():
        lo, hi = value["paired_bootstrap_95_ci"]
        lines.append(
            f"- `{name}`: mean `{value['mean']:+.4f}`, 95% CI `[{lo:+.4f}, {hi:+.4f}]`, "
            f"win/loss/tie `{value['positive']}/{value['negative']}/{value['ties']}`"
        )
    args.out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"json": str(args.out_json), "markdown": str(args.out_md)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
