#!/usr/bin/env python3
"""Replay map-nav tasks (evidence-only) and dump step traces.

Usage:
  python bin/56_replay_map_nav_traces.py                     # DEFAULT_IDS
  python bin/56_replay_map_nav_traces.py id1 id2
  python bin/56_replay_map_nav_traces.py --ids-file path.txt
  python bin/56_replay_map_nav_traces.py @path.txt

Resume (same output directory, skip finished cases):
  python bin/56_replay_map_nav_traces.py --resume-dir map_nav_trace/replay_20260715_173058 --ids-file ids.txt
  python bin/56_replay_map_nav_traces.py --resume   # auto-pick latest incomplete run

If a case crashes, delete its broken <inspect_id>.json (if any) and re-run with
--resume-dir on the same folder; corrupt JSON is auto-removed on resume.

Always runs with compose_answer=False (EVIDENCE only, no TASK Q&A).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import traceback
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
for source_dir in (ROOT / "src" / "realdata", ROOT / "src" / "nav"):
    if str(source_dir) not in sys.path:
        sys.path.insert(0, str(source_dir))

from agent_delivery.agent.runner_bodyrich import (  # noqa: E402
    _configure_nav_runtime,
    _load_tasks,
)
from agent_delivery.code.embedding_backend import (  # noqa: E402
    DEFAULT_DENSE_EMBEDDING_MODEL,
    resolve_embedding_model,
)
from agent_delivery.code.hierarchical_tools import HierarchicalTools  # noqa: E402
from agent_delivery.code.index_retrieval import CorpusIndex  # noqa: E402
from agent_delivery.code.load_data import bundles_from_paths  # noqa: E402
from agent_delivery.code.llm_config import load_llm_env  # noqa: E402
from nav_agent import run_nav_episode  # noqa: E402
from nav_types import NavConfig  # noqa: E402


DEFAULT_IDS = [
    "latest_clean_multi_0010",
    "real_69c60974d4242eda8c47c615_scope_collection_auto_0030",
]

_MANIFEST_NAME = "run_manifest.json"
_AGGREGATE_FILES = frozenset(
    {"all_cases.json", _MANIFEST_NAME, "action_space_snapshots.json", "canvas_payload.json"}
)


def _env_setup() -> None:
    os.environ.setdefault("NAV_MAP_MODE", "1")
    os.environ.setdefault("NAV_MAP_DENSE", "1")
    os.environ.setdefault("NAV_FILTER_COLLECTED_SECTIONS", "1")
    os.environ.setdefault("NAV_SCOPE_OUTLINE_MODE", "1")
    os.environ.setdefault("NAV_SCOPE_COLLECT_STRATEGY", "multi_band")
    os.environ.setdefault("BODYRICH_EMBEDDING_BACKEND", "remote")
    os.environ.setdefault("BODYRICH_EMBEDDING_MODEL", "text-embedding-v3")
    os.environ.setdefault("EMBEDDING_MODEL", "text-embedding-v3")
    summary_dir = ROOT / "cache" / "section_summaries_headtail"
    if summary_dir.exists():
        os.environ.setdefault("NAV_SECTION_SUMMARY_DIR", str(summary_dir))


def _gold_node_hits(
    gold_nodes: list[str], retrieved_nodes: list[str], evidence_text: str
) -> dict[str, Any]:
    gold = [str(x) for x in (gold_nodes or []) if str(x).strip()]
    retrieved = set(str(x) for x in (retrieved_nodes or []) if str(x).strip())
    text = evidence_text or ""
    hit_by_node = []
    for nid in gold:
        in_ret = nid in retrieved
        in_txt = nid in text or (nid.split(":")[-1] in text)
        hit_by_node.append(
            {"node": nid, "in_retrieved": in_ret, "in_evidence_text": bool(in_txt)}
        )
    n_hit = sum(1 for x in hit_by_node if x["in_retrieved"] or x["in_evidence_text"])
    return {
        "n_gold": len(gold),
        "n_hit": n_hit,
        "recall": (n_hit / len(gold)) if gold else 0.0,
        "hits": hit_by_node,
    }


def _load_old_row(inspect_id: str) -> dict[str, Any] | None:
    path = ROOT / "results" / "latest_clean400_scope_compact_cap180_v1_gold_b500.json"
    if not path.exists():
        return None
    rows = json.loads(path.read_text(encoding="utf-8"))["rows"]
    for row in rows:
        if row.get("inspect_id") == inspect_id:
            return row
    return None


def _is_valid_case(obj: Any) -> bool:
    if not isinstance(obj, dict):
        return False
    if not obj.get("inspect_id"):
        return False
    new = obj.get("new")
    if not isinstance(new, dict):
        return False
    if "evidence_text" not in new:
        return False
    if "gold_node_recall" not in new:
        return False
    if "steps" not in obj:
        return False
    return True


def _load_case_file(path: Path) -> dict[str, Any] | None:
    try:
        obj = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return obj if _is_valid_case(obj) else None


def _scan_completed_cases(out_dir: Path) -> tuple[dict[str, dict[str, Any]], list[str], list[str]]:
    """Return (completed_by_id, corrupt_files, removed_corrupt_ids)."""
    completed: dict[str, dict[str, Any]] = {}
    corrupt: list[str] = []
    removed_ids: list[str] = []
    for fp in sorted(out_dir.glob("*.json")):
        if fp.name in _AGGREGATE_FILES:
            continue
        case = _load_case_file(fp)
        if case is None:
            corrupt.append(fp.name)
            try:
                fp.unlink()
                removed_ids.append(fp.stem)
            except OSError:
                pass
            continue
        iid = str(case["inspect_id"])
        completed[iid] = case
    return completed, corrupt, removed_ids


def _write_json_atomic(path: Path, obj: Any) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)


def _load_manifest(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _save_manifest(path: Path, manifest: dict[str, Any]) -> None:
    manifest["updated_at"] = datetime.now().isoformat(timespec="seconds")
    _write_json_atomic(path, manifest)


def _find_latest_incomplete_run() -> Path | None:
    trace_root = ROOT / "map_nav_trace"
    if not trace_root.is_dir():
        return None
    candidates = sorted(trace_root.glob("replay_*"), key=lambda p: p.stat().st_mtime, reverse=True)
    for run_dir in candidates:
        manifest = _load_manifest(run_dir / _MANIFEST_NAME)
        if manifest is None:
            completed, _, _ = _scan_completed_cases(run_dir)
            if completed:
                return run_dir
            continue
        if manifest.get("status") != "completed":
            return run_dir
        pending = manifest.get("pending") or []
        failed = manifest.get("failed") or {}
        if pending or failed:
            return run_dir
    return None


def _format_eta(seconds: float) -> str:
    if seconds < 0 or seconds == float("inf"):
        return "?"
    if seconds < 60:
        return f"{int(seconds)}s"
    if seconds < 3600:
        return f"{int(seconds // 60)}m{int(seconds % 60)}s"
    return f"{int(seconds // 3600)}h{int((seconds % 3600) // 60)}m"


def _progress_prefix(done: int, total: int, skipped: int, failed: int) -> str:
    pct = (100.0 * done / total) if total else 100.0
    return f"[{done}/{total}] {pct:5.1f}% | ok={skipped} fail={failed}"


def _format_trace_md(payload: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append("# Map-Nav Trace Replay (recursive DISPATCH)")
    lines.append("")
    lines.append(f"- generated_at: `{payload['generated_at']}`")
    lines.append(f"- nav_map_mode: `{payload['env'].get('NAV_MAP_MODE')}`")
    lines.append(
        f"- enable_recursive_dispatch: `{payload['env'].get('enable_recursive_dispatch')}`"
    )
    lines.append(f"- embedding: `{payload['env'].get('EMBEDDING_MODEL')}`")
    if payload.get("resume"):
        lines.append(f"- resumed_from: `{payload['resume']}`")
    lines.append("")
    for case in payload["cases"]:
        lines.append(f"## {case['inspect_id']} ({case['task_type']})")
        lines.append("")
        lines.append(f"**Query:** {case['query']}")
        lines.append("")
        lines.append(f"**Doc:** `{case['doc_id']}`")
        lines.append("")
        old = case.get("old") or {}
        new = case.get("new") or {}
        lines.append("### Evidence comparison")
        lines.append("")
        lines.append(
            f"| | old Gold Nav | new Map-Nav |\n|---|---:|---:|\n"
            f"| score_task | {old.get('score_task')} | {new.get('score_task', 'n/a (compose skipped)')} |\n"
            f"| score_evidence | {old.get('score_evidence')} | {new.get('score_evidence', 'n/a')} |\n"
            f"| evidence_chars | {old.get('evidence_chars')} | {new.get('evidence_chars')} |\n"
            f"| gold_node_recall | {old.get('gold_node_recall')} | {new.get('gold_node_recall')} |\n"
            f"| n_retrieved_nodes | {old.get('n_retrieved_nodes')} | {new.get('n_retrieved_nodes')} |\n"
            f"| trajectory_steps | n/a | {new.get('trajectory_length')} |"
        )
        lines.append("")
        if new.get("gold_node_hits"):
            lines.append("### Gold node hits (new)")
            lines.append("")
            for h in new["gold_node_hits"]:
                mark = "HIT" if (h.get("in_retrieved") or h.get("in_evidence_text")) else "MISS"
                lines.append(
                    f"- `{h['node']}` [{mark}] retrieved={h.get('in_retrieved')} "
                    f"in_text={h.get('in_evidence_text')}"
                )
            lines.append("")
        lines.append("### Step decisions")
        lines.append("")
        for step in case.get("steps") or []:
            lines.append(
                f"**Step {step.get('step_idx')}** `{step.get('action')}`  "
                f"id=`{step.get('action_id')}` kind=`{step.get('kind')}` "
                f"section=`{step.get('section_id')}` scope=`{step.get('scope')}` "
                f"depth=`{step.get('depth')}`"
            )
            if step.get("llm_reason"):
                lines.append(f"- reason: {step['llm_reason']}")
            if step.get("dispatch_regions"):
                lines.append(f"- dispatch_regions: {step['dispatch_regions']}")
                lines.append(
                    f"- child_reports={step.get('n_child_reports')} "
                    f"skipped={step.get('n_child_skipped')}"
                )
            if step.get("collect_section_ids"):
                lines.append(f"- collect_section_ids: {step['collect_section_ids']}")
            if step.get("n_added") is not None:
                lines.append(
                    f"- collect added={step.get('n_added')} hits={step.get('n_hits')} "
                    f"branch_selected={step.get('branch_selected')} "
                    f"collect_full={step.get('collect_full')}"
                )
            if step.get("n_legal_actions") is not None:
                lines.append(f"- legal_actions ({step.get('n_legal_actions')}):")
                for la in step.get("legal_actions_preview") or []:
                    lines.append(f"  - {la}")
            if step.get("projection_chars") is not None:
                lines.append(f"- projection_chars: {step['projection_chars']}")
            lines.append("")
        if new.get("reports_context"):
            lines.append("### Subagent reports_context")
            lines.append("")
            lines.append("```")
            lines.append(str(new.get("reports_context") or "")[:3000])
            lines.append("```")
            lines.append("")
        lines.append("### Evidence text (new)")
        lines.append("")
        lines.append("```")
        lines.append((new.get("evidence_text") or "")[:4000])
        lines.append("```")
        lines.append("")
        lines.append("### Evidence text (old)")
        lines.append("")
        lines.append("```")
        lines.append((old.get("evidence_text") or "")[:2000])
        lines.append("```")
        lines.append("")
    return "\n".join(lines)


def _read_ids_file(path: Path) -> list[str]:
    return [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]


def _build_steps_out(result: Any) -> list[dict[str, Any]]:
    steps_out: list[dict[str, Any]] = []
    for st in result.steps or []:
        detail = dict(st.detail or {})
        steps_out.append(
            {
                "step_idx": st.step_idx,
                "action": st.action,
                "action_id": detail.get("action_id"),
                "kind": detail.get("kind"),
                "section_id": detail.get("section_id"),
                "scope": detail.get("scope"),
                "depth": detail.get("depth"),
                "llm_reason": detail.get("llm_reason"),
                "llm_raw": (detail.get("llm_raw") or "")[:300],
                "dispatch_regions": detail.get("dispatch_regions"),
                "n_child_reports": detail.get("n_child_reports"),
                "n_child_skipped": detail.get("n_child_skipped"),
                "collect_section_ids": detail.get("collect_section_ids"),
                "n_added": detail.get("n_added"),
                "n_hits": detail.get("n_hits"),
                "n_purged_descendant_evidence": detail.get("n_purged_descendant_evidence"),
                "branch_selected": detail.get("branch_selected"),
                "collect_full": detail.get("collect_full"),
                "group_rank": detail.get("group_rank"),
                "n_legal_actions": detail.get("n_legal_actions"),
                "legal_actions_preview": list(detail.get("legal_actions_preview") or [])[:20],
                "projection_chars": detail.get("projection_chars"),
            }
        )
    return steps_out


def _run_one_case(task: Any, tools: HierarchicalTools, cfg: NavConfig) -> dict[str, Any]:
    iid = getattr(task, "inspect_id", None)
    old_row = _load_old_row(str(iid))
    old_arm = (old_row or {}).get("hierarchical_gold") or {}
    old_metrics = old_arm.get("metrics") or {}
    old_evidence = str(old_arm.get("evidence_text") or "")
    old_nodes = list(old_arm.get("retrieved_nodes") or [])
    old_hit = _gold_node_hits(list(task.gold_nodes or []), old_nodes, old_evidence)

    t1 = time.perf_counter()
    result = run_nav_episode(
        tools,
        task.query,
        doc_id=str(task.doc_id),
        budget_chars=500,
        task_type=str(task.task_type or "unknown"),
        compose_format_constraints="",
        compose_answer=False,
        policy="llm",
        config=cfg,
    )
    elapsed = time.perf_counter() - t1
    new_hit = _gold_node_hits(
        list(task.gold_nodes or []),
        list(result.retrieved_nodes or []),
        str(result.evidence_text or ""),
    )

    reports_context = ""
    for st in reversed(list(result.steps or [])):
        detail = dict(st.detail or {})
        if detail.get("reports_snippet"):
            reports_context = str(detail.get("reports_snippet") or "")
            break

    return {
        "inspect_id": iid,
        "task_type": task.task_type,
        "doc_id": task.doc_id,
        "query": task.query,
        "gold_nodes": list(task.gold_nodes or []),
        "elapsed_sec": round(elapsed, 2),
        "old": {
            "score_task": old_metrics.get("score_task"),
            "score_evidence": old_metrics.get("score_evidence")
            or old_metrics.get("inspect_evidence_score"),
            "evidence_chars": old_arm.get("evidence_chars_actual") or len(old_evidence),
            "n_retrieved_nodes": len(old_nodes),
            "gold_node_recall": round(old_hit["recall"], 4),
            "gold_node_hits": old_hit["hits"],
            "evidence_text": old_evidence,
        },
        "new": {
            "score_task": None,
            "score_evidence": None,
            "evidence_chars": int(result.evidence_chars_actual or 0),
            "n_retrieved_nodes": len(result.retrieved_nodes or []),
            "gold_node_recall": round(new_hit["recall"], 4),
            "gold_node_hits": new_hit["hits"],
            "evidence_text": result.evidence_text or "",
            "trajectory_length": result.trajectory_length,
            "reports_context": reports_context,
            "retrieved_nodes": list(result.retrieved_nodes or []),
        },
        "steps": _build_steps_out(result),
        "_elapsed_raw": elapsed,
        "_old_recall": old_hit["recall"],
        "_new_recall": new_hit["recall"],
        "_trajectory_length": result.trajectory_length,
        "_evidence_chars": result.evidence_chars_actual,
    }


def _cases_in_order(requested_ids: list[str], completed: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for iid in requested_ids:
        case = completed.get(iid)
        if case is not None:
            out.append(case)
    return out


def _finalize_outputs(out_dir: Path, payload: dict[str, Any]) -> None:
    (out_dir / "all_cases.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (out_dir / "TRACE.md").write_text(_format_trace_md(payload), encoding="utf-8")
    try:
        sys.path.insert(0, str(ROOT / "bin"))
        import importlib

        report_mod = importlib.import_module("58_report_map_nav_run")
        meta = {k: v for k, v in payload.items() if k != "cases"}
        report_md = report_mod.build_report(meta, list(payload.get("cases") or []))
        (out_dir / "REPORT.md").write_text(report_md + "\n", encoding="utf-8")
        print(f"[replay] wrote report to {out_dir / 'REPORT.md'}", flush=True)
    except Exception as exc:
        print(f"[replay] report generation skipped: {exc}", flush=True)


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Replay map-nav traces (evidence-only).")
    parser.add_argument("ids", nargs="*", help="inspect_id list")
    parser.add_argument("--ids-file", "-f", type=Path, help="file with one inspect_id per line")
    parser.add_argument(
        "--resume-dir",
        type=Path,
        help="resume in an existing replay output directory (skip valid completed cases)",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="auto-resume the latest incomplete replay_* directory under map_nav_trace/",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        help="explicit output directory for a fresh run (default: map_nav_trace/replay_<ts>)",
    )
    parser.add_argument(
        "--stop-on-error",
        action="store_true",
        help="stop the batch on first task failure (default: record failure and continue)",
    )
    return parser.parse_args(argv)


def _collect_requested_ids(args: argparse.Namespace) -> tuple[list[str], bool]:
    ids: list[str] = list(args.ids or [])
    if args.ids_file is not None:
        ids.extend(_read_ids_file(args.ids_file.expanduser()))
    expanded: list[str] = []
    for item in ids:
        if item.startswith("@") and len(item) > 1:
            expanded.extend(_read_ids_file(Path(item[1:]).expanduser()))
        else:
            expanded.append(item)
    explicit = bool(expanded) or args.ids_file is not None
    return expanded, explicit


def main() -> int:
    _env_setup()
    load_llm_env()
    args = _parse_args(sys.argv[1:])
    ids, explicit_ids = _collect_requested_ids(args)

    tasks_path = ROOT / "data/tasks/tasks_realdata_bodyrich_latest_clean_400.jsonl"
    corpus = ROOT / "data/corpus/test_data_full_realdata_clean_latest.jsonl"
    nav_cfg_path = ROOT / "config/nav_default.json"

    _configure_nav_runtime(config_path=nav_cfg_path, policy="llm")
    cfg = NavConfig.from_dict(json.loads(nav_cfg_path.read_text(encoding="utf-8")))
    cfg.map_mode = True
    if cfg.llm_max_tokens < 256:
        cfg.llm_max_tokens = 256

    # output directory + resume state (resolve before loading tasks)
    resume_mode = False
    if args.resume_dir is not None:
        out_dir = args.resume_dir.expanduser()
        if not out_dir.is_absolute():
            out_dir = (ROOT / out_dir).resolve()
        resume_mode = True
    elif args.resume:
        found = _find_latest_incomplete_run()
        if found is None:
            raise SystemExit("[replay] --resume: no incomplete replay_* directory found")
        out_dir = found
        resume_mode = True
    elif args.out_dir is not None:
        out_dir = args.out_dir.expanduser()
        if not out_dir.is_absolute():
            out_dir = (ROOT / out_dir).resolve()
    else:
        out_dir = ROOT / "map_nav_trace" / f"replay_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    out_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = out_dir / _MANIFEST_NAME
    prev_manifest = _load_manifest(manifest_path) or {}
    if resume_mode and prev_manifest.get("requested_ids"):
        manifest_ids = [str(x) for x in prev_manifest["requested_ids"]]
        if not explicit_ids:
            ids = manifest_ids
        elif set(manifest_ids) != set(ids):
            print(
                "[replay] warning: --ids differ from manifest; using manifest order/ids",
                flush=True,
            )
            ids = manifest_ids
    if not ids:
        ids = list(DEFAULT_IDS)

    all_tasks = _load_tasks(tasks_path)
    selected = [t for t in all_tasks if getattr(t, "inspect_id", None) in set(ids)]
    by_id = {getattr(t, "inspect_id", None): t for t in selected}
    selected = [by_id[i] for i in ids if i in by_id]
    if len(selected) != len(ids):
        missing = [i for i in ids if i not in by_id]
        raise SystemExit(f"missing tasks: {missing}")

    completed_map, corrupt_files, removed_corrupt = _scan_completed_cases(out_dir)
    if corrupt_files:
        print(
            f"[replay] removed {len(corrupt_files)} corrupt case file(s): "
            + ", ".join(corrupt_files[:5])
            + (" ..." if len(corrupt_files) > 5 else ""),
            flush=True,
        )
        if removed_corrupt:
            print(f"[replay] will re-run: {', '.join(removed_corrupt[:8])}", flush=True)

    total = len(ids)
    already_done = [i for i in ids if i in completed_map]
    pending = [i for i in ids if i not in completed_map]
    n_skip = len(already_done)

    prev_failed = dict(prev_manifest.get("failed") or {})
    manifest: dict[str, Any] = {
        "started_at": prev_manifest.get("started_at") or datetime.now().isoformat(timespec="seconds"),
        "updated_at": datetime.now().isoformat(timespec="seconds"),
        "status": "running",
        "out_dir": str(out_dir),
        "requested_ids": ids,
        "completed": already_done,
        "pending": pending,
        "failed": prev_failed,
        "task_stats": {
            "total": total,
            "done": n_skip,
            "remaining": len(pending),
            "failed": len(prev_failed),
        },
    }
    _save_manifest(manifest_path, manifest)

    print(f"[replay] out_dir={out_dir}", flush=True)
    if resume_mode:
        print(f"[replay] resume: skip {n_skip}, run {len(pending)}", flush=True)
    print(f"[replay] tasks={total} docs={sorted({t.doc_id for t in selected if t.doc_id})}", flush=True)

    embedding_model = resolve_embedding_model(
        os.environ.get("EMBEDDING_MODEL") or DEFAULT_DENSE_EMBEDDING_MODEL
    )
    t0 = time.perf_counter()
    bundles = bundles_from_paths(corpus, tree_source="gold", pred_path=None, max_docs=0)
    print(f"[replay] loaded bundles in {time.perf_counter()-t0:.1f}s", flush=True)

    t0 = time.perf_counter()
    index = CorpusIndex.from_bundles(
        bundles,
        tree_mode="hierarchical",
        retrieval_backend="dense",
        embedding_model=embedding_model,
    )
    tools = HierarchicalTools(index)
    print(f"[replay] index ready in {time.perf_counter()-t0:.1f}s", flush=True)

    payload: dict[str, Any] = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "resume": str(out_dir) if resume_mode else None,
        "env": {
            "NAV_MAP_MODE": os.environ.get("NAV_MAP_MODE"),
            "NAV_SECTION_SUMMARY_DIR": os.environ.get("NAV_SECTION_SUMMARY_DIR"),
            "EMBEDDING_MODEL": embedding_model,
            "enable_recursive_dispatch": bool(cfg.enable_recursive_dispatch),
            "map_char_limit": int(cfg.map_char_limit),
            "max_steps": int(cfg.max_steps),
            "navigate_max_steps": int(cfg.navigate_max_steps),
        },
        "cases": [],
    }

    run_times: list[float] = []
    n_failed = len(manifest["failed"])
    done_count = n_skip

    try:
        for task in selected:
            iid = str(getattr(task, "inspect_id", None))
            if iid in completed_map:
                continue

            pos = done_count + 1
            avg = sum(run_times) / len(run_times) if run_times else 0.0
            remaining_n = total - done_count
            eta = _format_eta(avg * max(0, remaining_n - 1)) if run_times else "?"
            print(
                f"[replay] {_progress_prefix(pos, total, done_count, n_failed)} "
                f"| ETA ~{eta} | running {iid} ...",
                flush=True,
            )

            case_path = out_dir / f"{iid}.json"
            # Remove stale tmp from a prior crash.
            tmp_path = case_path.with_suffix(case_path.suffix + ".tmp")
            if tmp_path.exists():
                try:
                    tmp_path.unlink()
                except OSError:
                    pass

            try:
                raw_case = _run_one_case(task, tools, cfg)
                elapsed = float(raw_case.pop("_elapsed_raw", 0.0))
                old_recall = float(raw_case.pop("_old_recall", 0.0))
                new_recall = float(raw_case.pop("_new_recall", 0.0))
                traj = int(raw_case.pop("_trajectory_length", 0))
                ev_chars = raw_case.pop("_evidence_chars", 0)

                _write_json_atomic(case_path, raw_case)
                completed_map[iid] = raw_case
                done_count += 1
                run_times.append(elapsed)
                manifest["failed"].pop(iid, None)
                manifest["completed"] = [x for x in ids if x in completed_map]
                manifest["pending"] = [x for x in ids if x not in completed_map]
                manifest["task_stats"] = {
                    "total": total,
                    "done": done_count,
                    "remaining": total - done_count,
                    "failed": len(manifest["failed"]),
                }
                _save_manifest(manifest_path, manifest)

                print(
                    f"[replay] {_progress_prefix(done_count, total, done_count, n_failed)} "
                    f"| done {iid}: recall {old_recall:.2f}->{new_recall:.2f} "
                    f"chars={ev_chars} steps={traj} ({elapsed:.1f}s)",
                    flush=True,
                )
            except Exception as exc:
                n_failed += 1
                err = f"{type(exc).__name__}: {exc}"
                manifest["failed"][iid] = err
                manifest["pending"] = [x for x in ids if x not in completed_map]
                manifest["task_stats"] = {
                    "total": total,
                    "done": done_count,
                    "remaining": total - done_count,
                    "failed": len(manifest["failed"]),
                }
                _save_manifest(manifest_path, manifest)
                for fp in (case_path, tmp_path):
                    if fp.exists():
                        try:
                            fp.unlink()
                        except OSError:
                            pass
                print(f"[replay] FAILED {iid}: {err}", flush=True)
                traceback.print_exc()
                if args.stop_on_error:
                    raise
    finally:
        payload["cases"] = _cases_in_order(ids, completed_map)
        manifest["completed"] = [x for x in ids if x in completed_map]
        manifest["pending"] = [x for x in ids if x not in completed_map]
        manifest["status"] = "completed" if not manifest["pending"] else "incomplete"
        manifest["task_stats"] = {
            "total": total,
            "done": len(manifest["completed"]),
            "remaining": len(manifest["pending"]),
            "failed": len(manifest["failed"]),
        }
        _save_manifest(manifest_path, manifest)
        _finalize_outputs(out_dir, payload)
        print(f"[replay] wrote traces to {out_dir}", flush=True)
        print(
            f"[replay] summary: done={len(manifest['completed'])}/{total} "
            f"pending={len(manifest['pending'])} failed={len(manifest['failed'])}",
            flush=True,
        )
        if manifest["pending"]:
            print(
                f"[replay] resume with: python bin/56_replay_map_nav_traces.py "
                f"--resume-dir {out_dir}",
                flush=True,
            )

    print(str(out_dir))
    return 0 if not manifest["pending"] and not manifest["failed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
