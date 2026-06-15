#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


_NODE_RE = re.compile(r"^(.+):L(\d+)$")
_GENERIC_QUERY_RE = re.compile(r"该处明确写出的规定或事实是什么")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def parse_gold_answer(raw: Any) -> dict[str, Any]:
    if isinstance(raw, dict):
        return raw
    try:
        obj = json.loads(str(raw or ""))
        return obj if isinstance(obj, dict) else {"final_answer": str(raw or "")}
    except Exception:
        return {"final_answer": str(raw or "")}


def node_line(node: str) -> tuple[str, int] | None:
    m = _NODE_RE.match(str(node or "").strip())
    if not m:
        return None
    return m.group(1), int(m.group(2))


def load_corpus_meta(corpus: Path) -> dict[str, dict[str, Any]]:
    docs: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in read_jsonl(corpus):
        docs[str(row["doc_id"])].append(row)
    out: dict[str, dict[str, Any]] = {}
    for doc_id, rows in docs.items():
        rows = sorted(rows, key=lambda r: int(r.get("line_id", 0)))
        levels = {int(r.get("line_id", 0)): int(r.get("gold_level", 0) or 0) for r in rows}
        text = {int(r.get("line_id", 0)): str(r.get("content", "") or "") for r in rows}
        out[doc_id] = {"n_lines": len(rows), "levels": levels, "text": text}
    return out


def answer_items_count(obj: dict[str, Any]) -> int:
    if isinstance(obj.get("items"), list):
        return len([x for x in obj["items"] if str(x).strip()])
    if isinstance(obj.get("evidence_points"), list):
        return len([x for x in obj["evidence_points"] if str(x).strip()])
    ans = str(obj.get("final_answer") or obj.get("answer") or "")
    return len([x for x in re.split(r"[；;\n]", ans) if len(x.strip()) >= 4])


def likely_truncated_answer(obj: dict[str, Any]) -> bool:
    ans = str(obj.get("final_answer") or obj.get("answer") or "").strip()
    if not ans:
        return True
    return bool(re.search(r"[，、：:；;（(]$", ans)) or ans.endswith(("需", "应", "为", "按", "与"))


def structural_score(task: dict[str, Any], corpus_meta: dict[str, dict[str, Any]]) -> tuple[int, list[str]]:
    reasons: list[str] = []
    score = 0
    task_type = str(task.get("task_type") or "")
    if task_type in {"multi_hop", "scope_collection", "regulatory_coverage"}:
        score += 3
        reasons.append("complex_task_type")
    elif task_type == "niche_fact":
        score += 1

    nodes = [node_line(n) for n in task.get("gold_nodes") or []]
    nodes = [n for n in nodes if n is not None]
    doc_ids = {n[0] for n in nodes}
    if len(nodes) >= 2:
        score += 2
        reasons.append("multi_evidence")
    if len(doc_ids) >= 2:
        score += 3
        reasons.append("cross_doc")

    levels: list[int] = []
    n_lines = 0
    for doc_id, lid in nodes:
        meta = corpus_meta.get(doc_id, {})
        n_lines = max(n_lines, int(meta.get("n_lines", 0) or 0))
        levels.append(int((meta.get("levels") or {}).get(lid, 0) or 0))
    max_level = max(levels) if levels else 0
    if max_level >= 3:
        score += 3
        reasons.append("deep_gold_level")
    elif max_level >= 2:
        score += 2
        reasons.append("nested_gold_level")
    if n_lines >= 100:
        score += 2
        reasons.append("long_doc")
    elif n_lines >= 50:
        score += 1

    gold_obj = parse_gold_answer(task.get("gold_answer"))
    item_count = answer_items_count(gold_obj)
    if item_count >= 3:
        score += 2
        reasons.append("multi_item_answer")
    elif item_count >= 2:
        score += 1

    query = str(task.get("query") or "")
    if _GENERIC_QUERY_RE.search(query):
        score -= 1
        reasons.append("generic_open_query")
    if likely_truncated_answer(gold_obj):
        score -= 3
        reasons.append("likely_truncated_gold_answer")
    return score, reasons


def main() -> None:
    ap = argparse.ArgumentParser(description="Audit RealData task quality and create structural hierarchy-focused candidates.")
    ap.add_argument("--corpus", type=Path, default=Path("data/corpus/test_data_full_realdata_clean_latest.jsonl"))
    ap.add_argument("--tasks", type=Path, default=Path("data/tasks/tasks_realdata_bodyrich_latest_clean_quality_balanced60.jsonl"))
    ap.add_argument("--inspect", type=Path, default=Path("data/tasks/tasks_realdata_bodyrich_latest_clean_quality_balanced60.inspect.jsonl"))
    ap.add_argument("--out-report", type=Path, default=Path("results/task_quality_audit_latest_clean.json"))
    ap.add_argument("--out-tasks", type=Path, default=Path("data/tasks/tasks_realdata_bodyrich_latest_clean_hierarchy_candidates.jsonl"))
    ap.add_argument("--out-inspect", type=Path, default=Path("data/tasks/tasks_realdata_bodyrich_latest_clean_hierarchy_candidates.inspect.jsonl"))
    ap.add_argument("--min-score", type=int, default=4)
    args = ap.parse_args()

    corpus_meta = load_corpus_meta(args.corpus)
    tasks = read_jsonl(args.tasks)
    inspect_rows = read_jsonl(args.inspect)
    inspect_by_id = {str(r.get("id")): r for r in inspect_rows}

    audited: list[dict[str, Any]] = []
    for idx, task in enumerate(tasks, start=1):
        score, reasons = structural_score(task, corpus_meta)
        audited.append(
            {
                "task_idx": idx,
                "inspect_id": task.get("inspect_id"),
                "task_type": task.get("task_type"),
                "doc_id": task.get("doc_id"),
                "structural_score": score,
                "reasons": reasons,
                "query": task.get("query"),
            }
        )

    selected_ids = {
        str(x.get("inspect_id"))
        for x in audited
        if int(x.get("structural_score", 0) or 0) >= int(args.min_score)
    }
    selected_tasks = [t for t in tasks if str(t.get("inspect_id")) in selected_ids]
    selected_inspect = [inspect_by_id[i] for i in selected_ids if i in inspect_by_id]
    selected_inspect.sort(key=lambda r: str(r.get("id")))

    report = {
        "n_tasks": len(tasks),
        "n_selected": len(selected_tasks),
        "min_score": int(args.min_score),
        "task_type_counts_all": dict(Counter(str(t.get("task_type")) for t in tasks)),
        "task_type_counts_selected": dict(Counter(str(t.get("task_type")) for t in selected_tasks)),
        "reason_counts_selected": dict(Counter(r for x in audited if str(x.get("inspect_id")) in selected_ids for r in x["reasons"])),
        "audited": audited,
    }
    args.out_report.parent.mkdir(parents=True, exist_ok=True)
    args.out_report.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    write_jsonl(args.out_tasks, selected_tasks)
    write_jsonl(args.out_inspect, selected_inspect)
    print(f"selected={len(selected_tasks)}/{len(tasks)} min_score={args.min_score}")
    print(f"wrote {args.out_report}")
    print(f"wrote {args.out_tasks}")
    print(f"wrote {args.out_inspect}")


if __name__ == "__main__":
    main()
