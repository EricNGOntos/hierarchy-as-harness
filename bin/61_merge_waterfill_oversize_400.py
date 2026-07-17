#!/usr/bin/env python3
"""Merge 138 oversize-dispatch + 262 waterfill into one 400-case evidence dir."""
from __future__ import annotations

import json
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "map_nav_trace" / "replay_400_waterfill_oversize_merged"
SOURCES = [
    ROOT / "map_nav_trace" / "replay_138_oversize_dispatch",
    ROOT / "map_nav_trace" / "replay_262_waterfill",
]
TASKS = ROOT / "data/tasks/tasks_realdata_bodyrich_latest_clean_400.jsonl"


def main() -> None:
    order = [
        json.loads(line)["inspect_id"]
        for line in TASKS.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    by_id: dict[str, dict] = {}
    for src in SOURCES:
        if not src.is_dir():
            raise SystemExit(f"missing source dir: {src}")
        for p in src.glob("*.json"):
            if p.name in ("all_cases.json", "run_manifest.json"):
                continue
            case = json.loads(p.read_text(encoding="utf-8"))
            iid = str(case["inspect_id"])
            by_id[iid] = case

    missing = [i for i in order if i not in by_id]
    extra = sorted(set(by_id) - set(order))
    if missing:
        raise SystemExit(f"missing {len(missing)} cases, e.g. {missing[:5]}")

    OUT.mkdir(parents=True, exist_ok=True)
    cases = []
    for iid in order:
        case = by_id[iid]
        cases.append(case)
        (OUT / f"{iid}.json").write_text(
            json.dumps(case, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    recalls = [float(c["new"]["gold_node_recall"]) for c in cases]
    manifest = {
        "out_dir": str(OUT),
        "n_cases": len(cases),
        "n_missing": 0,
        "missing_ids": [],
        "extra_ids": extra,
        "recall_mean": round(sum(recalls) / len(recalls), 4) if recalls else 0.0,
        "recall_eq0": sum(1 for r in recalls if r < 1e-9),
        "sources": [str(s) for s in SOURCES],
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "note": "138=waterfill+depth0 oversize COLLECT→DISPATCH; 262=waterfill only",
    }
    (OUT / "run_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (OUT / "all_cases.json").write_text(
        json.dumps(
            {
                "generated_at": manifest["generated_at"],
                "n_cases": len(cases),
                "sources": manifest["sources"],
                "expected_n": 400,
                "missing_ids": [],
                "extra_ids": extra,
                "cases": cases,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
