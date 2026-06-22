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

# --- hierarchy-path leak stripping (method-agnostic, fairness) ---
# A leaked path is the literal `层级路径“A / B / C”` marker. The exact, "/"-delimited
# walkable path + the verbatim gold leaf line are what unfairly favor the hierarchical
# navigator (it can pattern-match the path to walk straight to the answer). We remove
# that machine path for ALL methods. niche_fact / scope_collection still carry their
# real intent (关于“X” / 围绕问题“Q”), so the marker is simply deleted. multi_hop has no
# other intent, so we replace the pair with a natural prose topic reference built from
# the section headings (doc name + deepest gold leaf line dropped) so the task stays
# answerable and non-degenerate while no method receives the literal path string.
_PATH_MARKER_RE = re.compile(r"层级路径“([^”]*)”")
_PATH_PAIR_RE = re.compile(r"[：:]\s*层级路径“[^”]*”(?:[与、和]层级路径“[^”]*”)+")
_PATH_SINGLE_XIA_RE = re.compile(r"层级路径“[^”]*”下")
_PATH_SINGLE_RE = re.compile(r"[，,]?\s*层级路径“[^”]*”")
_DOC_SEG_RE = re.compile(r"\.(docx|pdf|doc|xlsx|xls|pptx|txt)$", re.IGNORECASE)
_TOPIC_SEG_CAP = 40


def _topic_label_from_path(path: str) -> str:
    segs = [s.strip() for s in str(path or "").split("/")]
    segs = [s for s in segs if s and not _DOC_SEG_RE.search(s)]
    if len(segs) >= 2:
        segs = segs[:-1]  # drop deepest segment (the gold leaf line / answer text)
    segs = [s[:_TOPIC_SEG_CAP] for s in segs]
    return " - ".join(segs)


def _normalize_punct(q: str) -> str:
    q = re.sub(r"，{2,}", "，", q)
    q = re.sub(r"，。", "。", q)
    q = re.sub(r"：，", "：", q)
    q = re.sub(r"，》", "》", q)
    return q.strip()


def strip_path_leak(query: str) -> str:
    """Remove the literal `层级路径“…”` leak. multi_hop pairs become a prose topic ref."""
    q = str(query or "")

    def _pair_sub(m: re.Match) -> str:
        labels = [_topic_label_from_path(p) for p in _PATH_MARKER_RE.findall(m.group(0))]
        labels = [l for l in labels if l]
        if not labels:
            return ""
        return "，分别涉及“" + "”与“".join(labels) + "”两处"

    q = _PATH_PAIR_RE.sub(_pair_sub, q)
    q = _PATH_SINGLE_XIA_RE.sub("", q)
    q = _PATH_SINGLE_RE.sub("", q)
    return _normalize_punct(q)


def degenerate_scope(task: dict[str, Any]) -> bool:
    if str(task.get("task_type") or "") != "scope_collection":
        return False
    return answer_items_count(parse_gold_answer(task.get("gold_answer"))) < 2


def malformed_gold_json(task: dict[str, Any]) -> bool:
    raw = task.get("gold_answer")
    if isinstance(raw, dict):
        return False
    try:
        return not isinstance(json.loads(str(raw or "")), dict)
    except Exception:
        return True


def gold_nodes_absent(task: dict[str, Any], corpus_meta: dict[str, dict[str, Any]]) -> bool:
    nodes = task.get("gold_nodes") or []
    if not nodes:
        return True
    for n in nodes:
        nl = node_line(n)
        if nl is None:
            return True
        doc_id, lid = nl
        text_map = (corpus_meta.get(doc_id, {}) or {}).get("text") or {}
        if lid not in text_map:
            return True
    return False


def content_drop_reasons(
    task: dict[str, Any], corpus_meta: dict[str, dict[str, Any]]
) -> list[str]:
    """Method-agnostic, content-based drop reasons only (never 'a method got it wrong')."""
    reasons: list[str] = []
    if malformed_gold_json(task):
        reasons.append("malformed_gold_json")
    gold_obj = parse_gold_answer(task.get("gold_answer"))
    ans = str(gold_obj.get("final_answer") or gold_obj.get("answer") or "").strip()
    if not ans:
        reasons.append("empty_gold_answer")
    elif likely_truncated_answer(gold_obj):
        reasons.append("truncated_gold_answer")
    if gold_nodes_absent(task, corpus_meta):
        reasons.append("gold_nodes_absent_from_doc")
    if degenerate_scope(task):
        reasons.append("degenerate_scope_lt2_items")
    return reasons


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


def clean_main(args: argparse.Namespace) -> None:
    corpus_meta = load_corpus_meta(args.corpus)
    tasks = read_jsonl(args.tasks)
    inspect_rows = read_jsonl(args.inspect)
    inspect_by_id = {str(r.get("id")): r for r in inspect_rows}

    drop_log: list[dict[str, Any]] = []
    kept: list[dict[str, Any]] = []

    # Pass 1: content-based drops + path-leak strip + duplicate detection.
    seen_norm: dict[str, str] = {}
    for idx, task in enumerate(tasks, start=1):
        iid = str(task.get("inspect_id"))
        reasons = content_drop_reasons(task, corpus_meta)
        new_query = strip_path_leak(str(task.get("query") or ""))
        norm = re.sub(r"\s+", "", new_query)
        if norm in seen_norm:
            reasons.append(f"duplicate_query(of {seen_norm[norm]})")
        if reasons:
            drop_log.append(
                {"task_idx": idx, "inspect_id": iid, "task_type": task.get("task_type"), "reasons": reasons}
            )
            continue
        seen_norm[norm] = iid
        task = dict(task)
        task["query"] = new_query
        kept.append(task)

    # Pass 2: rebalance symmetrically across task types (keep first N per type by order).
    by_type: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for t in kept:
        by_type[str(t.get("task_type"))].append(t)
    min_count = min((len(v) for v in by_type.values()), default=0)
    balanced_ids: set[str] = set()
    rebalanced: list[dict[str, Any]] = []
    for tt, items in by_type.items():
        for t in items[:min_count]:
            balanced_ids.add(str(t.get("inspect_id")))
            rebalanced.append(t)
        for t in items[min_count:]:
            drop_log.append(
                {
                    "task_idx": None,
                    "inspect_id": str(t.get("inspect_id")),
                    "task_type": tt,
                    "reasons": [f"rebalance_drop(min_per_type={min_count})"],
                }
            )
    # preserve original ordering
    order = {str(t.get("inspect_id")): i for i, t in enumerate(tasks)}
    rebalanced.sort(key=lambda t: order.get(str(t.get("inspect_id")), 1_000_000))

    # Build matching inspect rows with the same query rewrite applied to `input`.
    out_inspect: list[dict[str, Any]] = []
    for t in rebalanced:
        iid = str(t.get("inspect_id"))
        row = inspect_by_id.get(iid)
        if row is None:
            continue
        row = dict(row)
        row["input"] = t["query"]
        out_inspect.append(row)

    write_jsonl(args.out_tasks, rebalanced)
    write_jsonl(args.out_inspect, out_inspect)

    log = {
        "n_input": len(tasks),
        "n_kept": len(rebalanced),
        "min_per_type": min_count,
        "kept_type_counts": dict(Counter(str(t.get("task_type")) for t in rebalanced)),
        "input_type_counts": dict(Counter(str(t.get("task_type")) for t in tasks)),
        "drop_reason_counts": dict(Counter(r for d in drop_log for r in d["reasons"])),
        "drops": drop_log,
        "policy": {
            "path_leak_strip": "remove literal 层级路径“…” marker for all methods; multi_hop replaced with prose section-topic reference (doc name + gold leaf line dropped)",
            "drop_rules": "content-based only: malformed/empty/truncated gold, gold nodes absent from doc, degenerate scope (<2 items), duplicate query; then symmetric rebalance per task_type",
        },
    }
    args.out_log.parent.mkdir(parents=True, exist_ok=True)
    args.out_log.write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"clean: kept={len(rebalanced)}/{len(tasks)} per_type={log['kept_type_counts']}")
    print(f"drop reasons: {log['drop_reason_counts']}")
    print(f"wrote {args.out_tasks}")
    print(f"wrote {args.out_inspect}")
    print(f"wrote {args.out_log}")


def audit_main(args: argparse.Namespace) -> None:
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


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Audit RealData task quality, or clean tasks (strip hierarchy-path leak + content-based drops)."
    )
    ap.add_argument("--mode", choices=["audit", "clean"], default="audit")
    ap.add_argument("--corpus", type=Path, default=Path("data/corpus/test_data_full_realdata_clean_latest.jsonl"))
    ap.add_argument("--tasks", type=Path, default=Path("data/tasks/tasks_realdata_bodyrich_fair_clean.jsonl"))
    ap.add_argument("--inspect", type=Path, default=Path("data/tasks/tasks_realdata_bodyrich_fair_clean.inspect.jsonl"))
    # audit mode outputs
    ap.add_argument("--out-report", type=Path, default=Path("results/task_quality_audit_fair_clean.json"))
    ap.add_argument("--min-score", type=int, default=4)
    # clean mode output
    ap.add_argument("--out-log", type=Path, default=Path("results/task_clean_log.json"))
    # shared outputs (defaults chosen per mode below if left unset)
    ap.add_argument("--out-tasks", type=Path, default=None)
    ap.add_argument("--out-inspect", type=Path, default=None)
    args = ap.parse_args()

    if args.mode == "clean":
        if args.out_tasks is None:
            args.out_tasks = Path("data/tasks/tasks_realdata_bodyrich_fair_clean.jsonl")
        if args.out_inspect is None:
            args.out_inspect = Path("data/tasks/tasks_realdata_bodyrich_fair_clean.inspect.jsonl")
        clean_main(args)
    else:
        if args.out_tasks is None:
            args.out_tasks = Path("data/tasks/tasks_realdata_bodyrich_fair_clean.jsonl")
        if args.out_inspect is None:
            args.out_inspect = Path("data/tasks/tasks_realdata_bodyrich_fair_clean.inspect.jsonl")
        audit_main(args)


if __name__ == "__main__":
    main()
