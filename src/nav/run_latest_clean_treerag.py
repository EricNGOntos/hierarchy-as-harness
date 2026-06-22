#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List


def _ensure_paths() -> Path:
    here = Path(__file__).resolve()
    root = here.parents[2]
    realdata_code = root / "src" / "realdata"
    for path in (root, realdata_code):
        path_text = str(path)
        if path_text not in sys.path:
            sys.path.insert(0, path_text)
    return root


ROOT = _ensure_paths()


def _load_arxiv_treerag_module() -> Any:
    module_path = ROOT / "src" / "treerag" / "eval_arxiv_treerag.py"
    spec = importlib.util.spec_from_file_location("realdata_wrapped_arxiv_treerag", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import TreeRAG module at {module_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _parse_nodes(raw_nodes: List[str]) -> List[tuple[str, int]]:
    out: List[tuple[str, int]] = []
    for raw_node in raw_nodes:
        match = re.match(r"^(.+):L(\d+)$", str(raw_node))
        if match:
            out.append((match.group(1), int(match.group(2))))
    return out


def _validate_alignment(test_jsonl: Path, tasks: Path) -> Dict[str, Any]:
    corpus_nodes: set[tuple[str, int]] = set()
    corpus_docs: set[str] = set()
    with test_jsonl.open(encoding="utf-8") as input_file:
        for raw_line in input_file:
            if not raw_line.strip():
                continue
            row = json.loads(raw_line)
            doc_id = str(row["doc_id"])
            corpus_docs.add(doc_id)
            corpus_nodes.add((doc_id, int(row["line_id"])))

    missing_docs: list[str] = []
    missing_nodes: list[dict[str, Any]] = []
    task_count = 0
    with tasks.open(encoding="utf-8") as input_file:
        for raw_line in input_file:
            if not raw_line.strip():
                continue
            task_count += 1
            row = json.loads(raw_line)
            doc_id = str(row.get("doc_id") or "")
            if doc_id not in corpus_docs:
                missing_docs.append(doc_id)
            for ref in _parse_nodes(list(row.get("gold_nodes") or [])):
                if ref not in corpus_nodes:
                    missing_nodes.append({"inspect_id": row.get("inspect_id"), "node": f"{ref[0]}:L{ref[1]}"})
    return {
        "tasks": task_count,
        "corpus_docs": len(corpus_docs),
        "missing_docs": len(missing_docs),
        "missing_nodes": len(missing_nodes),
        "missing_node_examples": missing_nodes[:10],
    }


def _usage_by_purpose(cache_path: Path) -> Dict[str, Dict[str, int]]:
    totals: dict[str, dict[str, int]] = defaultdict(
        lambda: {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0, "api_calls": 0}
    )
    if not cache_path.exists():
        return {}
    with cache_path.open(encoding="utf-8") as input_file:
        for raw_line in input_file:
            if not raw_line.strip():
                continue
            try:
                row = json.loads(raw_line)
            except Exception:
                continue
            purpose = str(row.get("purpose") or "unknown")
            usage = row.get("usage") if isinstance(row.get("usage"), dict) else {}
            totals[purpose]["prompt_tokens"] += int(usage.get("prompt_tokens", 0) or 0)
            totals[purpose]["completion_tokens"] += int(usage.get("completion_tokens", 0) or 0)
            totals[purpose]["total_tokens"] += int(usage.get("total_tokens", 0) or 0)
            totals[purpose]["api_calls"] += 1
    return {purpose: dict(values) for purpose, values in sorted(totals.items())}


def _postprocess_outputs(args: argparse.Namespace, alignment: Dict[str, Any]) -> None:
    cache_file_usage_by_purpose = _usage_by_purpose(args.cache_dir / "llm_cache.jsonl")
    budgets = [int(part.strip()) for part in str(args.budgets).split(",") if part.strip()]
    for budget in budgets:
        out_path = Path(str(args.out_template).format(budget=budget))
        if not out_path.exists():
            continue
        payload = json.loads(out_path.read_text(encoding="utf-8"))
        summary = payload.setdefault("summary", {})
        summary["experiment"] = "realdata_latest_clean_treerag_baseline"
        config = summary.setdefault("config", {})
        config["test_jsonl"] = str(args.test_jsonl)
        config["tasks"] = str(args.tasks)
        config["alignment"] = alignment
        current_usage_by_purpose = config.get("token_usage_by_purpose") if isinstance(config.get("token_usage_by_purpose"), dict) else {}
        config["token_usage_by_purpose"] = current_usage_by_purpose or cache_file_usage_by_purpose
        config["token_usage_by_purpose_cache_file"] = cache_file_usage_by_purpose
        config["baseline_role"] = "TreeRAG baseline; does not consume latest clean gold hierarchy labels for tree construction"
        payload["summary"] = summary
        out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    treerag = _load_arxiv_treerag_module()
    parser = argparse.ArgumentParser(description="Run TreeRAG baseline on RealData fair_clean tasks.")
    parser.add_argument("--test-jsonl", type=Path, default=Path("data/corpus/test_data_full_realdata_clean_latest.jsonl"))
    parser.add_argument("--tasks", type=Path, default=Path("data/tasks/tasks_realdata_bodyrich_fair_clean.jsonl"))
    parser.add_argument("--budgets", default="500")
    parser.add_argument("--out-template", default="results/fair_clean_treerag_fair_clean_scopefix_v2_b{budget}.json")
    parser.add_argument("--summary-md", type=Path, default=Path("cache/treerag_fair_clean_scopefix_v2/run_summary.md"))
    parser.add_argument("--cache-dir", type=Path, default=Path("cache/treerag_fair_clean_scopefix_v2"))
    parser.add_argument("--embedding-model", default=getattr(treerag, "PAPER_DENSE_EMBEDDING_MODEL", treerag.DEFAULT_DENSE_EMBEDDING_MODEL))
    parser.add_argument("--max-docs", type=int, default=0)
    parser.add_argument("--max-tasks", type=int, default=0)
    parser.add_argument("--treerag-model", default=None)
    parser.add_argument("--intent-mode", choices=("llm", "always", "never"), default="llm")
    parser.add_argument("--tree-lines-per-call", type=int, default=60)
    parser.add_argument("--tree-line-char-limit", type=int, default=700)
    parser.add_argument("--tree-max-level", type=int, default=4)
    parser.add_argument("--tree-max-tokens", type=int, default=12000)
    parser.add_argument("--intent-max-tokens", type=int, default=64)
    parser.add_argument("--initial-top-k", type=int, default=80)
    parser.add_argument("--root-to-leaf-decay", type=float, default=0.97)
    parser.add_argument("--leaf-to-parent-decay", type=float, default=0.94)
    parser.add_argument("--max-traversal-leaves", type=int, default=0)
    parser.add_argument("--path-char-limit", type=int, default=700)
    parser.add_argument("--embedding-batch-size", type=int, default=64)
    parser.add_argument("--compose-judge", action="store_true", help="Run shared compose/judge for end-to-end TreeRAG cost.")
    parser.add_argument("--inspect-judge", action="store_true", help="Run shared Inspect scoring for end-to-end TreeRAG quality.")
    parser.add_argument(
        "--inspect-tasks",
        dest="inspect_tasks",
        action="append",
        type=Path,
        default=None,
        metavar="PATH",
    )
    parser.add_argument("--rebuild-cache", action="store_true")
    parser.add_argument("--skip-llm-preflight", action="store_true")
    parser.add_argument("--skip-llm-smoke-check", action="store_true")
    parser.add_argument("--check-only", action="store_true", help="Only validate task/corpus alignment and CLI wiring.")
    args = parser.parse_args()

    alignment = _validate_alignment(args.test_jsonl, args.tasks)
    if alignment["missing_docs"] or alignment["missing_nodes"]:
        raise RuntimeError(f"TreeRAG RealData alignment failed: {alignment}")
    if args.check_only:
        print(json.dumps({"ok": True, "alignment": alignment}, ensure_ascii=False, indent=2))
        return
    if not os.environ.get("OPENAI_API_KEY", "").strip():
        raise RuntimeError("TreeRAG paper-style baseline requires OPENAI_API_KEY; rerun with --check-only for offline validation.")
    treerag.run_eval(args)
    _postprocess_outputs(args, alignment)


if __name__ == "__main__":
    main()
