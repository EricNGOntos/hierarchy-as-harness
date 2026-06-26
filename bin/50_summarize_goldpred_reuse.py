#!/usr/bin/env python3
"""Summarize new Gold/Pred arms with reused Flat/TreeRAG baselines."""

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


def _cost(payload: dict[str, Any], arm_key: str) -> dict[str, Any]:
    return ((payload.get("summary") or {}).get("cost") or {}).get(arm_key) or {}


def _usage(cost: dict[str, Any]) -> dict[str, float]:
    usage = cost.get("token_usage_total") or {}
    return {
        "total_tokens": float(usage.get("total_tokens", 0.0) or 0.0),
        "api_calls": float(usage.get("api_calls", 0.0) or 0.0),
        "cache_hits": float(usage.get("cache_hits", 0.0) or 0.0),
        "online_response_seconds": float(cost.get("online_response_seconds", 0.0) or 0.0),
        "judge_eval_seconds": float(cost.get("judge_eval_seconds", 0.0) or 0.0),
        "end_to_end_eval_seconds": float(cost.get("end_to_end_eval_seconds", 0.0) or 0.0),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gold", type=Path, required=True)
    parser.add_argument("--pred", type=Path, required=True)
    parser.add_argument("--flat-source", type=Path, required=True)
    parser.add_argument("--treerag", type=Path, required=True)
    parser.add_argument("--gold-run-root", type=Path, required=True)
    parser.add_argument("--pred-run-root", type=Path, required=True)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    parser.add_argument("--protocol", default="goldpred_robust_v1")
    parser.add_argument("--bootstrap-samples", type=int, default=100000)
    parser.add_argument("--bootstrap-seed", type=int, default=20260625)
    args = parser.parse_args()

    gold = _read_json(args.gold)
    pred = _read_json(args.pred)
    flat_source = _read_json(args.flat_source)
    treerag = _read_json(args.treerag)
    gold_by_id = {str(row.get("inspect_id")): row for row in gold.get("rows") or []}
    pred_by_id = {str(row.get("inspect_id")): row for row in pred.get("rows") or []}
    flat_by_id = {str(row.get("inspect_id")): row for row in flat_source.get("rows") or []}
    tree_by_id = {str((row.get("treerag") or {}).get("inspect_id")): row for row in treerag.get("rows") or []}
    ids = sorted(set(gold_by_id) & set(pred_by_id) & set(flat_by_id) & set(tree_by_id))
    if not ids:
        raise RuntimeError("no aligned inspect_id rows across Gold/Pred/Flat/TreeRAG")

    def score(task_id: str, arm: str, metric: str) -> float:
        if arm == "gold":
            return float(gold_by_id[task_id]["hierarchical_gold"]["metrics"].get(metric, 0.0) or 0.0)
        if arm == "pred":
            return float(pred_by_id[task_id]["hierarchical_pred"]["metrics"].get(metric, 0.0) or 0.0)
        if arm == "flat":
            return float(flat_by_id[task_id]["flat"]["metrics"].get(metric, 0.0) or 0.0)
        return float(tree_by_id[task_id]["treerag"].get(metric, 0.0) or 0.0)

    def task_type(task_id: str) -> str:
        return str(gold_by_id[task_id].get("task_type") or pred_by_id[task_id].get("task_type") or "unknown")

    quality: dict[str, Any] = {"overall": {}, "per_type": {}}
    for arm in ("gold", "pred", "treerag", "flat"):
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
                    "score_task": mean(score(task_id, arm, "score_task") for task_id in subset),
                    "score_evidence": mean(score(task_id, arm, "score_evidence") for task_id in subset),
                }
                for arm in ("gold", "pred", "treerag", "flat")
            },
        }

    comparisons: dict[str, Any] = {}
    for name, left, right in (
        ("gold_minus_pred", "gold", "pred"),
        ("gold_minus_treerag", "gold", "treerag"),
        ("gold_minus_flat", "gold", "flat"),
        ("pred_minus_treerag", "pred", "treerag"),
        ("pred_minus_flat", "pred", "flat"),
        ("treerag_minus_flat", "treerag", "flat"),
    ):
        diffs = [score(task_id, left, "score_task") - score(task_id, right, "score_task") for task_id in ids]
        comparisons[name] = {
            "mean": mean(diffs),
            "paired_bootstrap_95_ci": _ci(diffs, seed=args.bootstrap_seed, samples=args.bootstrap_samples),
            "positive": sum(value > 0 for value in diffs),
            "negative": sum(value < 0 for value in diffs),
            "ties": sum(value == 0 for value in diffs),
        }

    gold_cost = _cost(gold, "hierarchical_gold")
    pred_cost = _cost(pred, "hierarchical_pred")
    flat_cost = _cost(flat_source, "flat")
    treerag_cost = _cost(treerag, "treerag")
    report = {
        "protocol": args.protocol,
        "integrity": {
            "aligned_inspect_ids": len(ids),
            "gold_rows": len(gold_by_id),
            "pred_rows": len(pred_by_id),
            "flat_source_rows": len(flat_by_id),
            "treerag_rows": len(tree_by_id),
            "task_type_counts": {tt: quality["per_type"][tt]["n"] for tt in TASK_TYPES},
        },
        "quality": quality,
        "comparisons": comparisons,
        "cost": {
            "new_gold_cost": gold_cost,
            "new_pred_cost": pred_cost,
            "reused_flat_cost": flat_cost,
            "reused_treerag_cost": treerag_cost,
            "gold_wall_time": _wall(args.gold_run_root / "logs" / "gold.time"),
            "pred_wall_time": _wall(args.pred_run_root / "logs" / "pred.time"),
            "gold_audit": _audit(args.gold_run_root / "llm_call_audit.jsonl"),
            "pred_audit": _audit(args.pred_run_root / "llm_call_audit.jsonl"),
            "semantics": "Only Gold and Pred are newly evaluated. Flat and TreeRAG rows are reused by inspect_id.",
        },
        "artifacts": {
            "gold": str(args.gold),
            "pred": str(args.pred),
            "flat_source": str(args.flat_source),
            "treerag": str(args.treerag),
        },
    }
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        f"# {args.protocol} · Gold/Pred + reused baselines",
        "",
        "## Quality",
        "",
        "| Method | Status | Overall | Niche | Multi-hop | Scope | Evidence |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for arm, label, status in (
        ("gold", "Gold Nav robust-v1", "new"),
        ("pred", "Pred Nav robust-v1", "new"),
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
    lines.extend(["", "## Paired Bootstrap", ""])
    for name, value in comparisons.items():
        lo, hi = value["paired_bootstrap_95_ci"]
        lines.append(
            f"- `{name}`: mean `{value['mean']:+.4f}`, 95% CI `[{lo:+.4f}, {hi:+.4f}]`, "
            f"win/loss/tie `{value['positive']}/{value['negative']}/{value['ties']}`"
        )
    lines.extend(["", "## Cost And Reuse", ""])
    lines.extend([
        "| Arm | Status | Billed tokens | API calls | Cache hits | Online response | Judge | End-to-end |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ])
    gold_audit = report["cost"]["gold_audit"]
    pred_audit = report["cost"]["pred_audit"]
    for label, status, cost, audit in (
        ("Gold Nav robust-v1", "new", gold_cost, gold_audit),
        ("Pred Nav robust-v1", "new", pred_cost, pred_audit),
        ("TreeRAG", "reused", treerag_cost, None),
        ("Flat", "reused", flat_cost, None),
    ):
        u = _usage(cost)
        billed_tokens = int(audit["billed_tokens"]) if audit is not None else int(u["total_tokens"])
        api_calls = int(audit["api_calls"]) if audit is not None else int(u["api_calls"])
        cache_hits = int(audit["cache_hits"]) if audit is not None else int(u["cache_hits"])
        lines.append(
            f"| {label} | {status} | {billed_tokens:,} | {api_calls:,} | "
            f"{cache_hits:,} | {u['online_response_seconds']:.1f}s | "
            f"{u['judge_eval_seconds']:.1f}s | {u['end_to_end_eval_seconds']:.1f}s |"
        )
    lines.extend([
        "",
        f"- Gold audit: `{report['cost']['gold_audit']['api_calls']}` API calls, `{report['cost']['gold_audit']['cache_hits']}` cache hits.",
        f"- Pred audit: `{report['cost']['pred_audit']['api_calls']}` API calls, `{report['cost']['pred_audit']['cache_hits']}` cache hits.",
        "- No TreeRAG or Flat rows are rerun in this summary.",
    ])
    args.out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"json": str(args.out_json), "markdown": str(args.out_md)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
