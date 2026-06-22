#!/usr/bin/env python3
"""Re-run shared compose + Inspect judge on existing result rows (nav/evidence unchanged)."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict


ROOT = Path(__file__).resolve().parents[1]
REALDATA_SRC = ROOT / "src" / "realdata"
for path in (REALDATA_SRC, ROOT / "src" / "nav"):
    text = str(path)
    if text not in sys.path:
        sys.path.insert(0, text)

from agent_delivery.agent.runner_bodyrich import (  # noqa: E402
    _append_row_metrics_to_agg,
    _build_summary,
    _configure_bodyrich_task_judge,
    _empty_agg,
    _make_composed_answer,
)
from agent_delivery.agent.types import AgentTask  # noqa: E402
from agent_delivery.code.budget_eval import BudgetFillResult  # noqa: E402
from agent_delivery.code.inspect_scoring import (  # noqa: E402
    build_inspect_pred_output,
    evidence_line_ids_from_runner,
    score_sample,
)


def _load_inspect(path: Path) -> Dict[str, Dict[str, Any]]:
    out: Dict[str, Dict[str, Any]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        out[str(row["id"])] = row
    return out


def _task_from_row(row: Dict[str, Any]) -> AgentTask:
    return AgentTask(
        query=str(row.get("query") or ""),
        doc_id=row.get("doc_id"),
        gold_nodes=list(row.get("gold_nodes") or []),
        gold_answer=str(row.get("gold_answer") or ""),
        task_type=str(row.get("task_type") or "unknown"),
        inspect_id=str(row.get("inspect_id") or "") or None,
    )


def _judge_arm(
    task: AgentTask,
    arm: Dict[str, Any],
    *,
    composed: str,
    inspect_by_id: Dict[str, Dict[str, Any]],
    treerag_layout: bool,
) -> Dict[str, Any]:
    arm = dict(arm)
    iid = str(task.inspect_id or "")
    insp = inspect_by_id.get(iid)
    if not insp:
        return arm
    eids = evidence_line_ids_from_runner(
        retrieved_nodes=list(arm.get("retrieved_nodes") or []),
        kept_chunks=[],
        doc_id=task.doc_id,
    )
    pred = build_inspect_pred_output(
        composed,
        evidence_line_ids=eids,
        inspect_task=insp,
    )
    c_sc, e_sc, extra = score_sample(insp, pred)
    if treerag_layout:
        arm["score_task"] = float(c_sc)
        arm["score_evidence"] = float(e_sc)
        return arm
    metrics = dict(arm.get("metrics") or {})
    metrics["score_task"] = float(c_sc)
    metrics["score_evidence"] = float(e_sc)
    metrics["inspect_content_score"] = float(c_sc)
    metrics["inspect_evidence_score"] = float(e_sc)
    metrics["inspect_judge_used"] = True
    metrics["task_success"] = float(c_sc)
    for key, val in extra.items():
        if isinstance(val, (int, float)):
            metrics[f"inspect_{key}"] = float(val)
    arm["metrics"] = metrics
    return arm


def _recompose_arm(
    task: AgentTask,
    arm: Dict[str, Any],
    *,
    budget: int,
    inspect_by_id: Dict[str, Dict[str, Any]],
    treerag_layout: bool,
) -> Dict[str, Any]:
    arm = dict(arm)
    ev = str(arm.get("evidence_text") or "").strip()
    if not ev:
        return arm
    fill = BudgetFillResult(
        kept_chunks=[],
        evidence_text=ev,
        evidence_chars_actual=int(arm.get("evidence_chars_actual") or len(ev)),
        n_chunks_kept=int(arm.get("n_scored_candidates") or arm.get("n_chunks_kept") or 0),
        truncated_last=bool(arm.get("truncated_last")),
    )
    composed = _make_composed_answer(
        task,
        fill,
        budget_chars=int(budget),
        inspect_by_id=inspect_by_id,
    )
    arm["composed_answer"] = composed
    return _judge_arm(
        task,
        arm,
        composed=composed,
        inspect_by_id=inspect_by_id,
        treerag_layout=treerag_layout,
    )


def _rejudge_arm(
    task: AgentTask,
    arm: Dict[str, Any],
    *,
    inspect_by_id: Dict[str, Dict[str, Any]],
    treerag_layout: bool,
) -> Dict[str, Any]:
    composed = str(arm.get("composed_answer") or "").strip()
    if not composed:
        return arm
    return _judge_arm(
        task,
        arm,
        composed=composed,
        inspect_by_id=inspect_by_id,
        treerag_layout=treerag_layout,
    )


def _rebuild_gold_flat_summary(payload: Dict[str, Any]) -> Dict[str, Any]:
    rows = payload.get("rows") or []
    agg_g = _empty_agg()
    agg_f = _empty_agg()
    for row in rows:
        if isinstance(row.get("hierarchical_gold"), dict):
            _append_row_metrics_to_agg(agg_g, row["hierarchical_gold"])
        if isinstance(row.get("flat"), dict):
            _append_row_metrics_to_agg(agg_f, row["flat"])
    summary = _build_summary(agg_g, _empty_agg(), agg_f, rows, pred_enabled=False)
    old = payload.get("summary") if isinstance(payload.get("summary"), dict) else {}
    summary["config"] = old.get("config", summary.get("config", {}))
    if "cost" in old:
        summary["cost"] = old["cost"]
    return summary


def _rebuild_treerag_summary(payload: Dict[str, Any]) -> Dict[str, Any]:
    import importlib.util

    path = ROOT / "src" / "treerag" / "eval_arxiv_treerag.py"
    spec = importlib.util.spec_from_file_location("treerag_eval_recompose", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    rows = payload.get("rows") or []
    old = payload.get("summary") if isinstance(payload.get("summary"), dict) else {}
    summary = dict(old)
    summary["treerag"] = mod._summarize_arm(rows, "treerag")
    summary["per_type_treerag"] = mod._per_type(rows, "treerag")
    return summary


def recompose_file(
    results_path: Path,
    *,
    inspect_path: Path,
    budget: int,
    mode: str,
    judge_only: bool,
) -> None:
    _configure_bodyrich_task_judge()
    inspect_by_id = _load_inspect(inspect_path)
    payload = json.loads(results_path.read_text(encoding="utf-8"))
    rows = payload.get("rows") or []
    treerag_layout = mode == "treerag"
    action = "rejudge" if judge_only else "recompose"
    for idx, row in enumerate(rows, start=1):
        task = _task_from_row(row)
        if mode == "gold_flat":
            for arm_name in ("hierarchical_gold", "flat"):
                if isinstance(row.get(arm_name), dict):
                    if judge_only:
                        row[arm_name] = _rejudge_arm(
                            task,
                            row[arm_name],
                            inspect_by_id=inspect_by_id,
                            treerag_layout=False,
                        )
                    else:
                        row[arm_name] = _recompose_arm(
                            task,
                            row[arm_name],
                            budget=budget,
                            inspect_by_id=inspect_by_id,
                            treerag_layout=False,
                        )
        elif mode == "treerag":
            if isinstance(row.get("treerag"), dict):
                if judge_only:
                    row["treerag"] = _rejudge_arm(
                        task,
                        row["treerag"],
                        inspect_by_id=inspect_by_id,
                        treerag_layout=True,
                    )
                else:
                    row["treerag"] = _recompose_arm(
                        task,
                        row["treerag"],
                        budget=budget,
                        inspect_by_id=inspect_by_id,
                        treerag_layout=True,
                    )
        else:
            raise ValueError(f"unknown mode: {mode}")
        if idx % 10 == 0 or idx == len(rows):
            print(f"[{action}] {results_path.name}: {idx}/{len(rows)}", file=sys.stderr, flush=True)
    payload["summary"] = (
        _rebuild_gold_flat_summary(payload) if mode == "gold_flat" else _rebuild_treerag_summary(payload)
    )
    results_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[recompose] saved {results_path}", file=sys.stderr, flush=True)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--gold-flat-results",
        type=Path,
        default=Path("results/fair_clean_gold_flat_fair_clean_scopefix_v2_b500.json"),
    )
    ap.add_argument(
        "--treerag-results",
        type=Path,
        default=Path("results/fair_clean_treerag_fair_clean_scopefix_v2_b500.json"),
    )
    ap.add_argument(
        "--inspect-tasks",
        type=Path,
        default=Path("data/tasks/tasks_realdata_bodyrich_fair_clean.inspect.jsonl"),
    )
    ap.add_argument("--budget", type=int, default=500)
    ap.add_argument(
        "--only",
        choices=("all", "gold_flat", "treerag"),
        default="all",
    )
    ap.add_argument(
        "--judge-only",
        action="store_true",
        help="Keep existing composed_answer; only rerun Inspect judge with current tasks/scoring.",
    )
    args = ap.parse_args()
    if args.only in {"all", "gold_flat"}:
        recompose_file(
            args.gold_flat_results,
            inspect_path=args.inspect_tasks,
            budget=args.budget,
            mode="gold_flat",
            judge_only=bool(args.judge_only),
        )
    if args.only in {"all", "treerag"}:
        recompose_file(
            args.treerag_results,
            inspect_path=args.inspect_tasks,
            budget=args.budget,
            mode="treerag",
            judge_only=bool(args.judge_only),
        )


if __name__ == "__main__":
    main()
