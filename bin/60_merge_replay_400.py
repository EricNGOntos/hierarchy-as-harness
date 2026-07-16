#!/usr/bin/env python3
"""Merge replay_union_66_68 + replay_rest_shard{0,1,2} into one 400-case evidence dir."""
from __future__ import annotations

import json
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "map_nav_trace" / "replay_400_merged_latest"
SOURCES = [
    ROOT / "map_nav_trace" / "replay_union_66_68",
    ROOT / "map_nav_trace" / "replay_rest_shard0",
    ROOT / "map_nav_trace" / "replay_rest_shard1",
    ROOT / "map_nav_trace" / "replay_rest_shard2",
]
ORDER = [
    str(c["inspect_id"])
    for c in json.loads(
        (ROOT / "map_nav_trace" / "replay_20260716_173430" / "all_cases.json").read_text()
    )["cases"]
]


def main() -> None:
    by_id: dict[str, dict] = {}
    missing_sources = [str(p) for p in SOURCES if not (p / "all_cases.json").exists()]
    if missing_sources:
        raise SystemExit(f"missing source all_cases.json: {missing_sources}")

    for src in SOURCES:
        data = json.loads((src / "all_cases.json").read_text())
        for case in data.get("cases") or []:
            iid = str(case["inspect_id"])
            by_id[iid] = case
            src_json = src / f"{iid}.json"
            if src_json.exists():
                OUT.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_json, OUT / f"{iid}.json")

    ordered = []
    missing = []
    for iid in ORDER:
        if iid in by_id:
            ordered.append(by_id[iid])
        else:
            missing.append(iid)
    extra = sorted(set(by_id) - set(ORDER))

    OUT.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "n_cases": len(ordered),
        "sources": [str(p) for p in SOURCES],
        "expected_n": len(ORDER),
        "missing_ids": missing,
        "extra_ids": extra,
        "env": {
            "merged_from": "union_66_68 + rest_shard0/1/2",
            "algorithm": "greedy_pack + recursive_dispatch + zhizengzeng/qwen3.5-flash",
        },
        "cases": ordered,
    }
    (OUT / "all_cases.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")

    zeros = sum(1 for c in ordered if float((c.get("new") or {}).get("gold_node_recall") or 0) == 0)
    mean = (
        sum(float((c.get("new") or {}).get("gold_node_recall") or 0) for c in ordered) / len(ordered)
        if ordered
        else 0.0
    )
    manifest = {
        "out_dir": str(OUT),
        "n_cases": len(ordered),
        "n_missing": len(missing),
        "missing_ids": missing,
        "recall_mean": round(mean, 4),
        "recall_eq0": zeros,
        "generated_at": payload["generated_at"],
    }
    (OUT / "run_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    if missing:
        raise SystemExit(f"incomplete merge: missing {len(missing)}")


if __name__ == "__main__":
    main()
