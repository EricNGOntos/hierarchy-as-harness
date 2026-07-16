#!/usr/bin/env python3
"""Merge evidence from afternoon 99 + remaining replay into one QA-ready set.

Usage:
  python bin/57_merge_replay_evidence.py \\
    --primary map_nav_trace/replay_20260715_174808 \\
    --add map_nav_trace/replay_prev_zero_remaining_169 \\
    --out map_nav_trace/prev_goldnav_either0_evidence_merged
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
_SKIP = frozenset({"all_cases.json", "run_manifest.json", "action_space_snapshots.json", "canvas_payload.json"})


def _load_cases(run_dir: Path) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    all_cases = run_dir / "all_cases.json"
    if all_cases.exists():
        payload = json.loads(all_cases.read_text(encoding="utf-8"))
        for c in payload.get("cases") or []:
            iid = c.get("inspect_id")
            if iid and (c.get("new") or {}).get("evidence_text") is not None:
                out[str(iid)] = c
        return out
    for fp in sorted(run_dir.glob("*.json")):
        if fp.name in _SKIP:
            continue
        try:
            c = json.loads(fp.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        iid = c.get("inspect_id")
        if iid and (c.get("new") or {}).get("evidence_text") is not None:
            out[str(iid)] = c
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--primary", type=Path, required=True, help="first replay dir (e.g. afternoon 99)")
    ap.add_argument("--add", type=Path, action="append", default=[], help="additional replay dirs")
    ap.add_argument("--ids-file", type=Path, default=None, help="optional expected id list for coverage check")
    ap.add_argument("--out", type=Path, required=True, help="output directory")
    args = ap.parse_args()

    primary = args.primary if args.primary.is_absolute() else ROOT / args.primary
    add_dirs = [(p if p.is_absolute() else ROOT / p) for p in (args.add or [])]
    out_dir = args.out if args.out.is_absolute() else ROOT / args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    merged: dict[str, dict[str, Any]] = {}
    sources: dict[str, str] = {}

    for label, d in [("primary", primary), *[("add", d) for d in add_dirs]]:
        if not d.is_dir():
            raise SystemExit(f"missing dir: {d}")
        cases = _load_cases(d)
        for iid, c in cases.items():
            if iid not in merged:
                merged[iid] = c
                sources[iid] = str(d)
            # primary wins if conflict; later adds only fill gaps

    expected: list[str] | None = None
    if args.ids_file:
        idp = args.ids_file if args.ids_file.is_absolute() else ROOT / args.ids_file
        expected = [
            ln.strip()
            for ln in idp.read_text(encoding="utf-8").splitlines()
            if ln.strip() and not ln.strip().startswith("#")
        ]

    # order: expected list if given, else primary order then adds
    if expected:
        order = list(expected)
        for iid in merged:
            if iid not in order:
                order.append(iid)
    else:
        order = list(merged.keys())

    rows = []
    for iid in order:
        c = merged.get(iid)
        if not c:
            continue
        new = c.get("new") or {}
        rows.append(
            {
                "inspect_id": iid,
                "task_type": c.get("task_type"),
                "doc_id": c.get("doc_id"),
                "query": c.get("query"),
                "gold_nodes": c.get("gold_nodes"),
                "gold_node_recall": new.get("gold_node_recall"),
                "evidence_text": new.get("evidence_text"),
                "evidence_chars": new.get("evidence_chars"),
                "retrieved_nodes": new.get("retrieved_nodes"),
                "source_replay": sources.get(iid),
            }
        )

    jsonl_path = out_dir / "evidence_for_compose.jsonl"
    with jsonl_path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    all_path = out_dir / "all_cases.json"
    payload = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "n_cases": len(rows),
        "sources": [str(primary), *[str(d) for d in add_dirs]],
        "expected_n": len(expected) if expected else None,
        "missing_ids": [i for i in (expected or []) if i not in merged],
        "cases": [merged[i] for i in order if i in merged],
    }
    all_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    ids_path = out_dir / "inspect_ids.txt"
    ids_path.write_text("\n".join(r["inspect_id"] for r in rows) + "\n", encoding="utf-8")

    summary = {
        "n_merged": len(rows),
        "n_expected": len(expected) if expected else None,
        "n_missing": len(payload["missing_ids"]),
        "missing_ids": payload["missing_ids"],
        "recall_gt0": sum(1 for r in rows if (r.get("gold_node_recall") or 0) > 0),
        "recall_eq0": sum(1 for r in rows if (r.get("gold_node_recall") or 0) == 0),
        "jsonl": str(jsonl_path),
        "all_cases": str(all_path),
    }
    (out_dir / "MERGE_SUMMARY.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print(f"[merge] wrote {jsonl_path}")
    return 0 if not payload["missing_ids"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
