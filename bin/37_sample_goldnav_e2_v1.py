#!/usr/bin/env python3
"""Build the reproducible 3x20 goldnav_e2_v1 validation split."""

from __future__ import annotations

import argparse
import json
import random
from collections import Counter, defaultdict
from pathlib import Path


TASK_TYPES = ("niche_fact", "multi_hop", "scope_collection")


def read_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def fingerprint(row: dict) -> tuple[str, tuple[str, ...]]:
    return str(row.get("doc_id", "")), tuple(sorted(map(str, row.get("gold_nodes", []))))


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-tasks", type=Path, required=True)
    parser.add_argument("--source-inspect", type=Path, required=True)
    parser.add_argument("--avoid-tasks", type=Path, required=True)
    parser.add_argument("--out-tasks", type=Path, required=True)
    parser.add_argument("--out-inspect", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--per-type", type=int, default=20)
    parser.add_argument("--seed", type=int, default=20260624)
    args = parser.parse_args()

    source = read_jsonl(args.source_tasks)
    inspect_rows = read_jsonl(args.source_inspect)
    avoid = read_jsonl(args.avoid_tasks)
    inspect_by_id = {str(row["id"]): row for row in inspect_rows}

    # The 51-task version changed ids and query wording.  doc_id + gold_nodes is
    # the stable semantic identity, so use it in addition to exact ids/queries.
    avoid_ids = {str(row.get("inspect_id", "")) for row in avoid}
    avoid_queries = {str(row.get("query", "")) for row in avoid}
    avoid_fingerprints = {fingerprint(row) for row in avoid}
    avoid_answers = {(str(row.get("doc_id", "")), str(row.get("gold_answer", ""))) for row in avoid}

    eligible: dict[str, list[dict]] = defaultdict(list)
    excluded = Counter()
    for row in source:
        task_type = str(row.get("task_type", ""))
        if task_type not in TASK_TYPES:
            continue
        reasons = []
        if str(row.get("inspect_id", "")) in avoid_ids:
            reasons.append("inspect_id")
        if str(row.get("query", "")) in avoid_queries:
            reasons.append("query")
        if fingerprint(row) in avoid_fingerprints:
            reasons.append("doc_gold_nodes")
        if (str(row.get("doc_id", "")), str(row.get("gold_answer", ""))) in avoid_answers:
            reasons.append("doc_gold_answer")
        if reasons:
            excluded[task_type] += 1
        else:
            eligible[task_type].append(row)

    rng = random.Random(args.seed)
    selected: list[dict] = []
    for task_type in TASK_TYPES:
        pool = eligible[task_type]
        if len(pool) < args.per_type:
            raise SystemExit(f"not enough eligible {task_type}: {len(pool)} < {args.per_type}")
        picked = rng.sample(pool, args.per_type)
        selected.extend(sorted(picked, key=lambda row: str(row["inspect_id"])))

    selected_inspect = []
    for row in selected:
        inspect_id = str(row["inspect_id"])
        if inspect_id not in inspect_by_id:
            raise SystemExit(f"missing inspect record: {inspect_id}")
        selected_inspect.append(inspect_by_id[inspect_id])

    write_jsonl(args.out_tasks, selected)
    write_jsonl(args.out_inspect, selected_inspect)
    manifest = {
        "name": "goldnav_e2_v1",
        "seed": args.seed,
        "per_type": args.per_type,
        "total": len(selected),
        "source_tasks": str(args.source_tasks),
        "avoid_tasks": str(args.avoid_tasks),
        "avoidance_key": "exact id/query plus doc_id+gold_nodes plus doc_id+gold_answer",
        "source_counts": dict(Counter(str(row.get("task_type", "")) for row in source)),
        "excluded_as_51_semantic_overlap": dict(excluded),
        "eligible_counts": {task_type: len(eligible[task_type]) for task_type in TASK_TYPES},
        "selected_counts": dict(Counter(str(row["task_type"]) for row in selected)),
        "selected_ids": [str(row["inspect_id"]) for row in selected],
    }
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
