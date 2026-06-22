#!/usr/bin/env python3
"""Align fair-clean multi_hop gold to query locations and corpus line groups."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TASKS = ROOT / "data/tasks/tasks_realdata_bodyrich_fair_clean.jsonl"
INSPECT = ROOT / "data/tasks/tasks_realdata_bodyrich_fair_clean.inspect.jsonl"
CORPUS = ROOT / "data/corpus/test_data_full_realdata_clean_latest.jsonl"

# hop1 / hop2 line groups per inspect_id (aligned to query 第一处/第二处).
HOP_GROUPS: dict[str, list[list[int]]] = {
    "q400_multi_0002": [[108, 109], [112]],
    "q400_multi_0005": [[112], [130]],
    "q400_multi_0008": [list(range(129, 140)), list(range(140, 147))],
    "q400_multi_0009": [[163], [170]],
    "q400_multi_0023": [[7], [8]],
    "q400_multi_0029": [[46], [48]],
    "q400_multi_0041": [[103], [104]],
    "q400_multi_0042": [[111], [112]],
    "q400_multi_0048": [[30], [32]],
    "q400_multi_0054": [[41, 42, 43], [63, 64]],
    "q400_multi_0056": [[72, 73], [63, 64]],
    "q400_multi_0073": [[274, 275, 276, 277, 278, 279], [157, 170, 171]],
    "q400_multi_0094": [[262, 263, 264], [384, 385]],
    "q400_multi_0095": [[391], [392]],
    "q400_multi_0097": [[414, 415], [417]],
    "q400_multi_0107": [[414, 415], [478, 479]],
    "q400_multi_0123": [list(range(5, 16)), [19, 20]],
}


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


def _load_corpus() -> dict[str, dict[int, str]]:
    out: dict[str, dict[int, str]] = {}
    for line in CORPUS.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        doc_id = str(row["doc_id"])
        out.setdefault(doc_id, {})[int(row["line_id"])] = str(row["content"])
    return out


def _fact_text(corpus: dict[str, dict[int, str]], doc_id: str, line_ids: list[int]) -> str:
    lines = corpus.get(doc_id, {})
    parts = [lines[lid].strip() for lid in sorted(set(line_ids)) if lines.get(lid, "").strip()]
    return " ".join(parts).strip()


def _final_answer(f1: str, f2: str) -> str:
    return f"第一处要点：{f1} 第二处要点：{f2}"


def main() -> None:
    corpus = _load_corpus()
    tasks = _read_jsonl(TASKS)
    inspect_rows = _read_jsonl(INSPECT)
    inspect_by_id = {str(row["id"]): row for row in inspect_rows}

    for task in tasks:
        iid = str(task.get("inspect_id") or "")
        if iid not in HOP_GROUPS:
            continue
        inspect = inspect_by_id[iid]
        doc_id = str(task.get("doc_id") or inspect.get("metadata", {}).get("doc_id") or "")
        hop1, hop2 = HOP_GROUPS[iid]
        fact_1 = _fact_text(corpus, doc_id, hop1)
        fact_2 = _fact_text(corpus, doc_id, hop2)
        if not fact_1 or not fact_2:
            raise RuntimeError(f"{iid}: empty fact from hop groups hop1={hop1} hop2={hop2}")

        gold_line_ids = list(dict.fromkeys(hop1 + hop2))
        target = dict(inspect["target"])
        target["fact_1"] = fact_1
        target["fact_2"] = fact_2
        target["final_answer"] = _final_answer(fact_1, fact_2)
        target["evidence_line_ids"] = gold_line_ids
        inspect["target"] = target

        md = dict(inspect.get("metadata") or {})
        md["gold_line_ids"] = gold_line_ids
        inspect["metadata"] = md

        task["gold_nodes"] = [f"{doc_id}:L{lid}" for lid in gold_line_ids]
        task["gold_answer"] = json.dumps(
            {
                "fact_1": fact_1,
                "fact_2": fact_2,
                "final_answer": target["final_answer"],
                "evidence_line_ids": gold_line_ids,
            },
            ensure_ascii=False,
        )

    _write_jsonl(TASKS, tasks)
    _write_jsonl(INSPECT, inspect_rows)
    print(f"repaired {len(HOP_GROUPS)} multi_hop tasks -> {TASKS.name}, {INSPECT.name}")


if __name__ == "__main__":
    main()
