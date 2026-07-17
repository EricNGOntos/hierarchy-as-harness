#!/usr/bin/env python3
"""Compose + Inspect-judge from frozen map-nav evidence (no re-navigation).

Reads evidence from a ``bin/56`` replay directory (or ``evidence_for_compose.jsonl``),
reuses the same ``_make_composed_answer`` / ``_fill_agg`` path as ``bin/44``, and
writes a ``results/*_b500.json``-compatible payload.

Resume: skip completed ``inspect_id`` rows in ``--checkpoint-jsonl``.

Examples:
  python bin/59_compose_judge_from_evidence.py \\
    --replay-dir map_nav_trace/replay_20260716_173430

  # interrupt then continue
  python bin/59_compose_judge_from_evidence.py \\
    --replay-dir map_nav_trace/replay_20260716_173430 \\
    --checkpoint-jsonl cache/compose_from_replay_400/checkpoint.jsonl \\
    --out results/latest_clean400_map_nav_from_replay_b500.json

  # smoke
  python bin/59_compose_judge_from_evidence.py \\
    --replay-dir map_nav_trace/replay_20260716_173430 --max-tasks 2
"""

from __future__ import annotations

import argparse
import hashlib
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
    _agg_summary,
    _append_row_metrics_to_agg,
    _configure_bodyrich_task_judge,
    _empty_agg,
    _empty_cost_block,
    _fill_agg,
    _finalize_cost,
    _load_tasks,
    _make_composed_answer,
    _per_type_summary,
    _require_inspect_registry_for_judge,
    _write_task_outputs_jsonl,
)
from agent_delivery.agent.types import AgentStep, AgentTask, EpisodeResult  # noqa: E402
from agent_delivery.code.budget_eval import BudgetFillResult  # noqa: E402
from agent_delivery.code.inspect_scoring import (  # noqa: E402
    default_inspect_task_paths,
    load_inspect_registry,
)
from agent_delivery.code.llm_config import load_llm_env  # noqa: E402
from agent_delivery.code.llm_usage import reset_usage, snapshot_usage  # noqa: E402


_SKIP_REPLAY = frozenset(
    {
        "all_cases.json",
        "run_manifest.json",
        "action_space_snapshots.json",
        "canvas_payload.json",
        "part12_rerun_summary.json",
    }
)
_ARM_KEY = "hierarchical_gold_map"
_DEFAULT_REPLAY = ROOT / "map_nav_trace" / "replay_20260716_173430"
_DEFAULT_TASKS = ROOT / "data" / "tasks" / "tasks_realdata_bodyrich_latest_clean_400.jsonl"
_DEFAULT_INSPECT = (
    ROOT / "data" / "tasks" / "tasks_realdata_bodyrich_latest_clean_400.inspect.jsonl"
)


def _resolve(path: Path) -> Path:
    return path if path.is_absolute() else (ROOT / path)


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _normalize_case(raw: dict[str, Any], *, from_replay: bool) -> dict[str, Any] | None:
    """Normalize one evidence row; return None if unusable."""
    iid = str(raw.get("inspect_id") or "").strip()
    if not iid:
        return None
    if from_replay:
        new = raw.get("new") or {}
        if not isinstance(new, dict) or new.get("evidence_text") is None:
            return None
        evidence_text = str(new.get("evidence_text") or "")
        retrieved = list(new.get("retrieved_nodes") or [])
        evidence_chars = new.get("evidence_chars")
        traj = int(new.get("trajectory_length") or 0)
        gold_node_recall = new.get("gold_node_recall")
        steps = list(raw.get("steps") or [])
        gold_nodes = list(raw.get("gold_nodes") or [])
        query = raw.get("query")
        task_type = raw.get("task_type")
        doc_id = raw.get("doc_id")
    else:
        if raw.get("evidence_text") is None:
            return None
        evidence_text = str(raw.get("evidence_text") or "")
        retrieved = list(raw.get("retrieved_nodes") or [])
        evidence_chars = raw.get("evidence_chars")
        traj = int(raw.get("trajectory_length") or 0)
        gold_node_recall = raw.get("gold_node_recall")
        steps = []
        gold_nodes = list(raw.get("gold_nodes") or [])
        query = raw.get("query")
        task_type = raw.get("task_type")
        doc_id = raw.get("doc_id")
    return {
        "inspect_id": iid,
        "query": query,
        "task_type": task_type,
        "doc_id": doc_id,
        "gold_nodes": gold_nodes,
        "evidence_text": evidence_text,
        "evidence_chars": evidence_chars if evidence_chars is not None else len(evidence_text),
        "retrieved_nodes": retrieved,
        "trajectory_length": traj,
        "gold_node_recall": gold_node_recall,
        "steps": steps,
    }


def _dedupe_cases(cases: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Keep first occurrence; warn on duplicates."""
    seen: set[str] = set()
    out: list[dict[str, Any]] = []
    dup = 0
    for c in cases:
        iid = str(c["inspect_id"])
        if iid in seen:
            dup += 1
            continue
        seen.add(iid)
        out.append(c)
    if dup:
        print(f"[compose] warn: dropped {dup} duplicate inspect_id rows", flush=True)
    return out


def _load_evidence_cases(
    *,
    replay_dir: Path | None,
    evidence_jsonl: Path | None,
) -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    if evidence_jsonl is not None:
        with evidence_jsonl.open(encoding="utf-8") as f:
            for lineno, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError as exc:
                    print(
                        f"[compose] warn: skip bad jsonl line {lineno}: {exc}",
                        file=sys.stderr,
                        flush=True,
                    )
                    continue
                if not isinstance(row, dict):
                    continue
                norm = _normalize_case(row, from_replay=False)
                if norm is not None:
                    cases.append(norm)
        return _dedupe_cases(cases)

    if replay_dir is None:
        raise SystemExit("require --replay-dir or --evidence-jsonl")

    all_cases = replay_dir / "all_cases.json"
    raw_cases: list[dict[str, Any]] = []
    if all_cases.exists():
        try:
            payload = json.loads(all_cases.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise SystemExit(f"failed to read {all_cases}: {exc}") from exc
        raw_cases = [c for c in (payload.get("cases") or []) if isinstance(c, dict)]
    else:
        for fp in sorted(replay_dir.glob("*.json")):
            if fp.name in _SKIP_REPLAY:
                continue
            try:
                c = json.loads(fp.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                print(f"[compose] warn: skip corrupt {fp.name}: {exc}", flush=True)
                continue
            if isinstance(c, dict):
                raw_cases.append(c)

    for c in raw_cases:
        norm = _normalize_case(c, from_replay=True)
        if norm is not None:
            cases.append(norm)
    return _dedupe_cases(cases)


def _validate_cases(cases: list[dict[str, Any]]) -> list[str]:
    """Return human-readable warnings; does not mutate."""
    warnings: list[str] = []
    empty_ev = sum(1 for c in cases if not str(c.get("evidence_text") or "").strip())
    empty_nodes = sum(1 for c in cases if not (c.get("retrieved_nodes") or []))
    empty_query = sum(1 for c in cases if not str(c.get("query") or "").strip())
    if empty_ev:
        warnings.append(f"{empty_ev} cases have empty evidence_text")
    if empty_nodes:
        warnings.append(f"{empty_nodes} cases have empty retrieved_nodes")
    if empty_query:
        warnings.append(f"{empty_query} cases have empty query")
    return warnings


def _evidence_fingerprint(cases: list[dict[str, Any]]) -> str:
    """Stable fingerprint so checkpoint invalidates if evidence set changes."""
    parts = []
    for c in sorted(cases, key=lambda x: str(x.get("inspect_id") or "")):
        iid = str(c.get("inspect_id") or "")
        ev = str(c.get("evidence_text") or "")
        nodes = ",".join(str(x) for x in (c.get("retrieved_nodes") or []))
        parts.append(f"{iid}|{len(ev)}|{hashlib.sha256(ev.encode()).hexdigest()[:16]}|{nodes}")
    blob = "\n".join(parts)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def _signature(
    *,
    evidence_fp: str,
    tasks: Path,
    inspect_tasks: list[Path],
    budget_chars: int,
    inspect_judge: bool,
    arm_key: str,
    compose_only: bool = False,
) -> str:
    payload = {
        "adapter": "compose_judge_from_frozen_evidence_v1",
        "evidence_fingerprint": evidence_fp,
        "tasks": str(tasks.resolve()),
        "tasks_sha256": _file_sha256(tasks) if tasks.exists() else None,
        "inspect_tasks": [str(p.resolve()) for p in inspect_tasks],
        "budget_chars": int(budget_chars),
        "inspect_judge": bool(inspect_judge),
        "compose_only": bool(compose_only),
        "arm_key": arm_key,
        "compose_model": os.environ.get("COMPOSE_MODEL", "").strip(),
        "judge_model": os.environ.get("JUDGE_MODEL", "").strip(),
    }
    return hashlib.sha256(
        json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()


def _checkpoint_row_ok(row: dict[str, Any]) -> bool:
    """Require arm payload with composed_answer + metrics (skip half-written rows)."""
    arm = row.get(_ARM_KEY)
    if not isinstance(arm, dict):
        arm = row.get("hierarchical_gold")
    if not isinstance(arm, dict):
        return False
    if arm.get("composed_answer") is None:
        return False
    if not isinstance(arm.get("metrics"), dict):
        return False
    return True


def _load_checkpoint(path: Path | None, signature: str) -> dict[str, dict[str, Any]]:
    """Return {inspect_id: {row, cost_delta}} for matching signature."""
    if path is None or not path.exists():
        return {}
    try:
        with path.open("r", encoding="utf-8") as f:
            first = f.readline().strip()
            if not first:
                return {}
            meta = json.loads(first)
            if meta.get("kind") != "meta" or meta.get("signature") != signature:
                print(
                    f"[checkpoint] ignoring stale checkpoint {path}",
                    file=sys.stderr,
                    flush=True,
                )
                return {}
            out: dict[str, dict[str, Any]] = {}
            skipped = 0
            for line_no, line in enumerate(f, start=2):
                line = line.strip()
                if not line:
                    continue
                try:
                    payload = json.loads(line)
                except json.JSONDecodeError:
                    skipped += 1
                    print(
                        f"[checkpoint] warn: skip corrupt line {line_no} in {path}",
                        flush=True,
                    )
                    continue
                if payload.get("kind") != "task":
                    continue
                iid = str(payload.get("inspect_id") or "").strip()
                row = payload.get("row")
                if not iid or not isinstance(row, dict) or not _checkpoint_row_ok(row):
                    skipped += 1
                    continue
                # Ensure arm key present for downstream agg.
                if _ARM_KEY not in row and isinstance(row.get("hierarchical_gold"), dict):
                    row = dict(row)
                    row[_ARM_KEY] = row["hierarchical_gold"]
                out[iid] = {
                    "row": row,
                    "cost_delta": payload.get("cost_delta") or {},
                }
            if skipped:
                print(
                    f"[checkpoint] skipped {skipped} incomplete/corrupt task lines",
                    flush=True,
                )
            return out
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        print(f"[checkpoint] failed to read {path}: {exc}", file=sys.stderr, flush=True)
        return {}


def _append_checkpoint(
    path: Path | None,
    signature: str,
    *,
    inspect_id: str,
    task_idx: int,
    row: dict[str, Any],
    cost_delta: dict[str, Any],
) -> None:
    if path is None:
        return
    if not _checkpoint_row_ok(row):
        raise ValueError(f"refusing to checkpoint incomplete row for {inspect_id}")
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        meta = {
            "kind": "meta",
            "signature": signature,
            "created_at": time.time(),
            "adapter": "compose_judge_from_frozen_evidence_v1",
        }
        with path.open("w", encoding="utf-8") as f:
            f.write(json.dumps(meta, ensure_ascii=False) + "\n")
            f.flush()
            os.fsync(f.fileno())
    payload = {
        "kind": "task",
        "inspect_id": inspect_id,
        "task_idx": int(task_idx),
        "row": row,
        "cost_delta": cost_delta,
    }
    line = json.dumps(payload, ensure_ascii=False) + "\n"
    with path.open("a", encoding="utf-8") as f:
        f.write(line)
        f.flush()
        os.fsync(f.fileno())


def _write_run_manifest(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def _merge_cost(target: dict[str, Any], delta: dict[str, Any]) -> None:
    for key, value in delta.items():
        if isinstance(value, dict):
            child = target.setdefault(key, {})
            if isinstance(child, dict):
                _merge_cost(child, value)
            else:
                target[key] = value
        elif isinstance(value, (int, float)):
            target[key] = float(target.get(key, 0.0) or 0.0) + float(value)
        else:
            target[key] = value


def _usage_delta(before: dict[str, Any], after: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    keys = set(before) | set(after)
    for purpose in keys:
        b = before.get(purpose) or {}
        a = after.get(purpose) or {}
        out[purpose] = {
            "prompt_tokens": float(a.get("prompt_tokens", 0) or 0)
            - float(b.get("prompt_tokens", 0) or 0),
            "completion_tokens": float(a.get("completion_tokens", 0) or 0)
            - float(b.get("completion_tokens", 0) or 0),
            "total_tokens": float(a.get("total_tokens", 0) or 0)
            - float(b.get("total_tokens", 0) or 0),
            "api_calls": float(a.get("api_calls", 0) or 0) - float(b.get("api_calls", 0) or 0),
            "cache_hits": float(a.get("cache_hits", 0) or 0) - float(b.get("cache_hits", 0) or 0),
        }
    return out


def _task_for_case(
    case: dict[str, Any],
    tasks_by_id: dict[str, AgentTask],
) -> AgentTask:
    iid = str(case["inspect_id"])
    base = tasks_by_id.get(iid)
    if base is not None:
        return base
    # Fallback: build from evidence row (should be rare if tasks file is complete).
    return AgentTask(
        query=str(case.get("query") or ""),
        doc_id=str(case["doc_id"]) if case.get("doc_id") is not None else None,
        gold_nodes=[str(x) for x in (case.get("gold_nodes") or [])],
        gold_answer="",
        task_type=str(case.get("task_type") or "unknown"),
        inspect_id=iid,
    )


def _metrics_compose_only(case: dict[str, Any], episode: EpisodeResult) -> dict[str, Any]:
    """Skip Inspect/semantic judge; keep retrieval coverage from frozen replay."""
    recall = case.get("gold_node_recall")
    try:
        score_evidence = float(recall) if recall is not None else float("nan")
    except (TypeError, ValueError):
        score_evidence = float("nan")
    return {
        "score_task": float("nan"),
        "score_evidence": score_evidence,
        "score_process": float("nan"),
        "task_success": float("nan"),
        "inspect_judge_used": False,
        "compose_only": True,
        "inspect_id": case.get("inspect_id"),
        "source_gold_node_recall": recall,
        "evidence_chars_actual": episode.evidence_chars_actual,
    }


def _episode_from_frozen(
    *,
    case: dict[str, Any],
    composed: str,
    compose_seconds: float,
) -> EpisodeResult:
    evidence_text = str(case.get("evidence_text") or "")
    evidence_chars = int(case.get("evidence_chars") or len(evidence_text) or 0)
    traj = int(case.get("trajectory_length") or 0)
    steps = [
        AgentStep(
            step_idx=1,
            action="compose_answer",
            detail={
                "evidence_chars": evidence_chars,
                "frozen_evidence": True,
                "gold_node_recall": case.get("gold_node_recall"),
            },
        )
    ]
    return EpisodeResult(
        representation="hierarchical_nav_frozen_evidence",
        steps=steps,
        scored_chunks=[],
        kept_chunks=[],
        evidence_text=evidence_text,
        evidence_chars_actual=evidence_chars,
        retrieved_nodes=list(case.get("retrieved_nodes") or []),
        composed_answer=composed,
        section_ids=[],
        trajectory_length=max(traj, 1),
        truncated_last=False,
        refusal_events=[],
        phase_timings={
            "retrieval_framework_seconds": 0.0,
            "compose_seconds": float(compose_seconds),
            "online_response_seconds": float(compose_seconds),
        },
    )


def _write_payload(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def _build_argparser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Compose + Inspect judge from frozen map-nav evidence (resume-capable)."
    )
    p.add_argument(
        "--replay-dir",
        type=Path,
        default=None,
        help="bin/56 replay directory containing all_cases.json / per-task JSON",
    )
    p.add_argument(
        "--evidence-jsonl",
        type=Path,
        default=None,
        help="optional evidence_for_compose.jsonl (from bin/57); overrides --replay-dir",
    )
    p.add_argument("--tasks", type=Path, default=_DEFAULT_TASKS)
    p.add_argument(
        "--inspect-tasks",
        action="append",
        type=Path,
        default=None,
        help="Inspect JSONL (repeatable). Default: 400-task inspect file if present.",
    )
    p.add_argument("--budget-chars", type=int, default=500)
    p.add_argument("--max-tasks", type=int, default=0, help="0 = all")
    p.add_argument(
        "--ids-file",
        type=Path,
        default=None,
        help="optional inspect_id allowlist (one per line)",
    )
    p.add_argument(
        "--out",
        type=Path,
        default=ROOT / "results" / "latest_clean400_map_nav_from_replay_b500.json",
    )
    p.add_argument(
        "--checkpoint-jsonl",
        type=Path,
        default=None,
        help="default: cache/compose_from_replay_<out_stem>/checkpoint.jsonl",
    )
    p.add_argument("--task-outputs-jsonl", type=Path, default=None)
    p.add_argument(
        "--no-inspect-judge",
        action="store_true",
        help="disable Inspect scoring (fallback semantic task_success)",
    )
    p.add_argument(
        "--compose-only",
        action="store_true",
        help="only run compose LLM; skip Inspect and semantic judge (score_task=NaN)",
    )
    p.add_argument(
        "--stop-on-error",
        action="store_true",
        help="stop on first compose/judge failure (default: record and continue)",
    )
    p.add_argument(
        "--flush-every",
        type=int,
        default=10,
        help="rewrite --out every N newly completed tasks (0 = only at end)",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="validate evidence/tasks/inspect/checkpoint wiring only; no LLM calls",
    )
    return p


def _build_row(
    *,
    task_idx: int,
    task: AgentTask,
    iid: str,
    arm_block: dict[str, Any],
) -> dict[str, Any]:
    """Result row with map arm + hierarchical_gold alias for summarize helpers."""
    return {
        "task_idx": task_idx,
        "query": task.query,
        "doc_id": task.doc_id,
        "task_type": task.task_type,
        "gold_nodes": list(task.gold_nodes),
        "gold_answer": task.gold_answer,
        "inspect_id": iid,
        _ARM_KEY: arm_block,
        "hierarchical_gold": arm_block,
    }


def main() -> int:
    args = _build_argparser().parse_args()
    dry_run = bool(args.dry_run)
    if not dry_run:
        load_llm_env()
        _configure_bodyrich_task_judge()

    replay_dir = _resolve(args.replay_dir) if args.replay_dir else None
    evidence_jsonl = _resolve(args.evidence_jsonl) if args.evidence_jsonl else None
    if evidence_jsonl is None and replay_dir is None:
        if _DEFAULT_REPLAY.is_dir():
            replay_dir = _DEFAULT_REPLAY
            print(f"[compose] default --replay-dir {replay_dir}", flush=True)
        else:
            raise SystemExit("pass --replay-dir or --evidence-jsonl")

    if evidence_jsonl is not None and not evidence_jsonl.is_file():
        raise SystemExit(f"missing evidence jsonl: {evidence_jsonl}")
    if evidence_jsonl is None and (replay_dir is None or not replay_dir.is_dir()):
        raise SystemExit(f"missing replay dir: {replay_dir}")

    tasks_path = _resolve(args.tasks)
    if not tasks_path.is_file():
        raise SystemExit(f"missing tasks file: {tasks_path}")
    out_path = _resolve(args.out)
    ckpt_path = (
        _resolve(args.checkpoint_jsonl)
        if args.checkpoint_jsonl
        else ROOT / "cache" / f"compose_from_replay_{out_path.stem}" / "checkpoint.jsonl"
    )
    manifest_path = ckpt_path.parent / "run_manifest.json"
    task_outputs = _resolve(args.task_outputs_jsonl) if args.task_outputs_jsonl else None

    cases = _load_evidence_cases(replay_dir=replay_dir, evidence_jsonl=evidence_jsonl)
    if not cases:
        raise SystemExit("no evidence cases loaded")

    allow: set[str] | None = None
    if args.ids_file:
        idp = _resolve(args.ids_file)
        if not idp.is_file():
            raise SystemExit(f"missing ids file: {idp}")
        allow = {
            ln.strip()
            for ln in idp.read_text(encoding="utf-8").splitlines()
            if ln.strip() and not ln.strip().startswith("#")
        }
        before = len(cases)
        cases = [c for c in cases if c["inspect_id"] in allow]
        missing_allow = sorted(allow - {c["inspect_id"] for c in cases})
        print(
            f"[compose] ids-file filter: {before} -> {len(cases)} "
            f"(missing_in_evidence={len(missing_allow)})",
            flush=True,
        )

    # Stable order: tasks file order when possible, else inspect_id sort.
    tasks_all = _load_tasks(tasks_path)
    tasks_by_id = {
        str(t.inspect_id): t for t in tasks_all if getattr(t, "inspect_id", None)
    }
    order_index = {
        str(t.inspect_id): i
        for i, t in enumerate(tasks_all)
        if getattr(t, "inspect_id", None)
    }
    cases.sort(
        key=lambda c: (
            order_index.get(str(c["inspect_id"]), 10**9),
            str(c["inspect_id"]),
        )
    )
    if args.max_tasks > 0:
        cases = cases[: int(args.max_tasks)]

    for w in _validate_cases(cases):
        print(f"[compose] warn: {w}", flush=True)

    compose_only = bool(args.compose_only)
    use_inspect = (not bool(args.no_inspect_judge)) and (not compose_only)
    if args.inspect_tasks:
        inspect_paths = [_resolve(p) for p in args.inspect_tasks]
    elif _DEFAULT_INSPECT.exists():
        inspect_paths = [_DEFAULT_INSPECT]
    else:
        inspect_paths = default_inspect_task_paths(ROOT)
    inspect_paths = [p for p in inspect_paths if p.exists()]
    # Compose still needs inspect metadata for output format hints.
    inspect_by_id = load_inspect_registry(inspect_paths) if inspect_paths else None

    work_tasks = [_task_for_case(c, tasks_by_id) for c in cases]
    missing_task = [t.inspect_id for t in work_tasks if t.inspect_id not in tasks_by_id]
    if missing_task:
        print(
            f"[compose] warn: {len(missing_task)} cases missing from tasks file "
            f"(using evidence metadata), e.g. {missing_task[:3]}",
            file=sys.stderr,
            flush=True,
        )
    if not compose_only:
        _require_inspect_registry_for_judge(
            use_inspect_judge=use_inspect,
            inspect_by_id=inspect_by_id,
            inspect_paths_resolved=inspect_paths,
            kit_root=ROOT,
            tasks=work_tasks,
        )

    evidence_fp = _evidence_fingerprint(cases)
    signature = _signature(
        evidence_fp=evidence_fp,
        tasks=tasks_path,
        inspect_tasks=inspect_paths,
        budget_chars=int(args.budget_chars),
        inspect_judge=use_inspect,
        arm_key=_ARM_KEY,
        compose_only=compose_only,
    )
    resumed = _load_checkpoint(ckpt_path, signature)
    pending_ids = [c["inspect_id"] for c in cases if c["inspect_id"] not in resumed]
    if resumed:
        print(
            f"[checkpoint] resumed {len(resumed)}/{len(cases)} from {ckpt_path}",
            flush=True,
        )

    _write_run_manifest(
        manifest_path,
        {
            "status": "dry_run" if dry_run else "running",
            "started_at": datetime.now().isoformat(timespec="seconds"),
            "signature": signature,
            "replay_dir": str(replay_dir) if replay_dir else None,
            "evidence_jsonl": str(evidence_jsonl) if evidence_jsonl else None,
            "out": str(out_path),
            "checkpoint": str(ckpt_path),
            "n_cases": len(cases),
            "n_resumed": len(resumed),
            "n_pending": len(pending_ids),
            "pending_sample": pending_ids[:10],
            "inspect_judge": use_inspect,
            "compose_only": compose_only,
            "dry_run": dry_run,
        },
    )

    if dry_run:
        print(
            json.dumps(
                {
                    "ok": True,
                    "dry_run": True,
                    "n_cases": len(cases),
                    "n_resumed": len(resumed),
                    "n_pending": len(pending_ids),
                    "n_missing_tasks": len(missing_task),
                    "inspect_registry": len(inspect_by_id or {}),
                    "inspect_paths": [str(p) for p in inspect_paths],
                    "signature": signature,
                    "checkpoint": str(ckpt_path),
                    "out": str(out_path),
                    "sample_ids": [c["inspect_id"] for c in cases[:5]],
                },
                ensure_ascii=False,
                indent=2,
            ),
            flush=True,
        )
        return 0

    agg = _empty_agg()
    rows: list[dict[str, Any]] = []
    cost: dict[str, Any] = {_ARM_KEY: _empty_cost_block()}
    failed: dict[str, str] = {}
    newly_done = 0
    t_run0 = time.perf_counter()
    reset_usage()

    for task_idx, case in enumerate(cases, start=1):
        iid = str(case["inspect_id"])
        if iid in resumed:
            row = resumed[iid]["row"]
            rows.append(row)
            arm = row.get(_ARM_KEY) or row.get("hierarchical_gold")
            if isinstance(arm, dict):
                _append_row_metrics_to_agg(agg, arm)
            delta = resumed[iid].get("cost_delta") or {}
            if isinstance(delta, dict):
                _merge_cost(cost, delta)
            continue

        task = _task_for_case(case, tasks_by_id)
        usage_before = snapshot_usage()
        t0 = time.perf_counter()
        try:
            fill = BudgetFillResult(
                kept_chunks=[],
                evidence_text=str(case.get("evidence_text") or ""),
                evidence_chars_actual=int(
                    case.get("evidence_chars") or len(str(case.get("evidence_text") or ""))
                ),
                n_chunks_kept=0,
                truncated_last=False,
            )
            compose_t0 = time.perf_counter()
            composed = _make_composed_answer(
                task,
                fill,
                budget_chars=int(args.budget_chars),
                inspect_by_id=inspect_by_id,
            )
            if not str(composed or "").strip():
                raise RuntimeError("compose returned empty answer")
            compose_seconds = time.perf_counter() - compose_t0
            episode = _episode_from_frozen(
                case=case, composed=composed, compose_seconds=compose_seconds
            )
            judge_t0 = time.perf_counter()
            if compose_only:
                metrics = _metrics_compose_only(case, episode)
                _append_row_metrics_to_agg(agg, {"metrics": metrics})
            else:
                metrics = _fill_agg(
                    agg,
                    episode,
                    task,
                    hier_policy="nav",
                    inspect_by_id=inspect_by_id,
                    use_inspect_judge=use_inspect,
                )
            judge_seconds = time.perf_counter() - judge_t0
            elapsed = time.perf_counter() - t0
            usage_after = snapshot_usage()
            usage_d = _usage_delta(usage_before, usage_after)

            arm_block = {
                "n_scored_candidates": 0,
                "evidence_chars_actual": episode.evidence_chars_actual,
                "evidence_text": episode.evidence_text,
                "composed_answer": episode.composed_answer,
                "trajectory_length": episode.trajectory_length,
                "truncated_last": False,
                "section_ids": [],
                "retrieved_nodes": episode.retrieved_nodes,
                "refusal_events": [],
                "metrics": metrics,
                "steps": [s.__dict__ for s in episode.steps],
                "frozen_evidence": True,
                "source_gold_node_recall": case.get("gold_node_recall"),
                "phase_timings": episode.phase_timings,
                "compose_only": compose_only,
            }
            row = _build_row(task_idx=task_idx, task=task, iid=iid, arm_block=arm_block)
            cost_delta = {
                _ARM_KEY: {
                    "total_seconds": elapsed,
                    "compose_seconds": compose_seconds,
                    "judge_eval_seconds": judge_seconds,
                    "online_response_seconds": compose_seconds,
                    "token_usage_by_purpose": usage_d,
                }
            }
            _merge_cost(cost, cost_delta)
            rows.append(row)
            _append_checkpoint(
                ckpt_path,
                signature,
                inspect_id=iid,
                task_idx=task_idx,
                row=row,
                cost_delta=cost_delta,
            )
            newly_done += 1
            st = (metrics or {}).get("score_task")
            mode = "compose_only" if compose_only else "compose+judge"
            print(
                f"[compose] [{task_idx}/{len(cases)}] {iid} ({mode}) "
                f"score_task={st} compose={compose_seconds:.1f}s judge={judge_seconds:.1f}s",
                flush=True,
            )
        except Exception as exc:
            failed[iid] = f"{type(exc).__name__}: {exc}"
            traceback.print_exc()
            print(f"[compose] FAIL {iid}: {failed[iid]}", file=sys.stderr, flush=True)
            _write_run_manifest(
                manifest_path,
                {
                    "status": "running",
                    "updated_at": datetime.now().isoformat(timespec="seconds"),
                    "n_rows": len(rows),
                    "n_failed": len(failed),
                    "last_failed": iid,
                    "failed": failed,
                    "signature": signature,
                },
            )
            if args.stop_on_error:
                break
            continue

        if args.flush_every > 0 and newly_done % int(args.flush_every) == 0:
            _finalize_cost(cost)
            partial = {
                "summary": {
                    "config": {
                        "adapter": "compose_judge_from_frozen_evidence_v1",
                        "replay_dir": str(replay_dir) if replay_dir else None,
                        "evidence_jsonl": str(evidence_jsonl) if evidence_jsonl else None,
                        "tasks": str(tasks_path),
                        "budget_chars": int(args.budget_chars),
                        "inspect_judge": use_inspect,
                        "compose_only": compose_only,
                        "partial": True,
                        "n_rows": len(rows),
                        "n_failed": len(failed),
                        "updated_at": datetime.now().isoformat(timespec="seconds"),
                    },
                    _ARM_KEY: _agg_summary(agg),
                    f"per_type_{_ARM_KEY}": _per_type_summary(rows, _ARM_KEY),
                    "cost": cost,
                },
                "rows": rows,
            }
            _write_payload(out_path, partial)
            print(f"[compose] flushed partial out -> {out_path}", flush=True)

    _finalize_cost(cost)
    summary = {
        "config": {
            "adapter": "compose_judge_from_frozen_evidence_v1",
            "replay_dir": str(replay_dir) if replay_dir else None,
            "evidence_jsonl": str(evidence_jsonl) if evidence_jsonl else None,
            "tasks": str(tasks_path),
            "inspect_tasks": [str(p) for p in inspect_paths],
            "budget_chars": int(args.budget_chars),
            "inspect_judge": use_inspect,
            "compose_only": compose_only,
            "arm_key": _ARM_KEY,
            "evidence_fingerprint": evidence_fp,
            "checkpoint": str(ckpt_path),
            "n_evidence": len(cases),
            "n_rows": len(rows),
            "n_failed": len(failed),
            "failed": failed,
            "elapsed_sec": round(time.perf_counter() - t_run0, 2),
            "generated_at": datetime.now().isoformat(timespec="seconds"),
        },
        _ARM_KEY: _agg_summary(agg),
        f"per_type_{_ARM_KEY}": _per_type_summary(rows, _ARM_KEY),
        "cost": cost,
    }
    payload = {"summary": summary, "rows": rows}
    _write_payload(out_path, payload)
    if task_outputs is not None:
        _write_task_outputs_jsonl(task_outputs, rows)

    status = "completed" if not failed and len(rows) == len(cases) else "incomplete"
    _write_run_manifest(
        manifest_path,
        {
            "status": status,
            "finished_at": datetime.now().isoformat(timespec="seconds"),
            "signature": signature,
            "n_cases": len(cases),
            "n_rows": len(rows),
            "n_failed": len(failed),
            "failed": failed,
            "out": str(out_path),
            "checkpoint": str(ckpt_path),
        },
    )

    mean_st = (summary.get(_ARM_KEY) or {}).get("score_task_mean")
    print(
        f"[compose] done rows={len(rows)}/{len(cases)} failed={len(failed)} "
        f"score_task_mean={mean_st} out={out_path} checkpoint={ckpt_path}",
        flush=True,
    )
    return 0 if status == "completed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
