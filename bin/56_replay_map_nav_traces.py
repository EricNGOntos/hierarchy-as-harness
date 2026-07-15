#!/usr/bin/env python3
"""Replay a few failing tasks under map-nav and dump step traces to Desktop."""

from __future__ import annotations

import json
import os
import re
import sys
import time
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


def _gold_node_hits(gold_nodes: list[str], retrieved_nodes: list[str], evidence_text: str) -> dict[str, Any]:
    gold = [str(x) for x in (gold_nodes or []) if str(x).strip()]
    retrieved = set(str(x) for x in (retrieved_nodes or []) if str(x).strip())
    text = evidence_text or ""
    hit_by_node = []
    for nid in gold:
        in_ret = nid in retrieved
        # also allow line-id substring match in evidence headers
        in_txt = nid in text or (nid.split(":")[-1] in text)
        hit_by_node.append({"node": nid, "in_retrieved": in_ret, "in_evidence_text": bool(in_txt)})
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


def main() -> int:
    _env_setup()
    load_llm_env()
    ids = list(DEFAULT_IDS)
    if len(sys.argv) > 1:
        ids = [x.strip() for x in sys.argv[1:] if x.strip()]

    tasks_path = ROOT / "data/tasks/tasks_realdata_bodyrich_latest_clean_400.jsonl"
    corpus = ROOT / "data/corpus/test_data_full_realdata_clean_latest.jsonl"
    nav_cfg_path = ROOT / "config/nav_default.json"

    _configure_nav_runtime(config_path=nav_cfg_path, policy="llm")
    cfg = NavConfig.from_dict(json.loads(nav_cfg_path.read_text(encoding="utf-8")))
    cfg.map_mode = True
    if cfg.llm_max_tokens < 256:
        cfg.llm_max_tokens = 256

    all_tasks = _load_tasks(tasks_path)
    selected = [t for t in all_tasks if getattr(t, "inspect_id", None) in set(ids)]
    # preserve requested order
    by_id = {getattr(t, "inspect_id", None): t for t in selected}
    selected = [by_id[i] for i in ids if i in by_id]
    if len(selected) != len(ids):
        missing = [i for i in ids if i not in by_id]
        raise SystemExit(f"missing tasks: {missing}")

    needed_docs = sorted({t.doc_id for t in selected if t.doc_id})
    print(f"[replay] tasks={ids} docs={needed_docs}", flush=True)

    embedding_model = resolve_embedding_model(
        os.environ.get("EMBEDDING_MODEL") or DEFAULT_DENSE_EMBEDDING_MODEL
    )
    t0 = time.perf_counter()
    # Load full corpus once (index needs neighbors); filter is expensive otherwise.
    bundles = bundles_from_paths(corpus, tree_source="gold", pred_path=None, max_docs=0)
    # Keep only needed docs in a shallow way by rebuilding from subset if possible.
    if hasattr(bundles, "items"):
        pass
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

    out_dir = ROOT / "map_nav_trace" / f"replay_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    out_dir.mkdir(parents=True, exist_ok=True)

    payload: dict[str, Any] = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
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

    for task in selected:
        iid = getattr(task, "inspect_id", None)
        print(f"[replay] running {iid} ...", flush=True)
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
            compose_answer=False,  # focus on evidence
            policy="llm",
            config=cfg,
        )
        elapsed = time.perf_counter() - t1
        new_hit = _gold_node_hits(
            list(task.gold_nodes or []),
            list(result.retrieved_nodes or []),
            str(result.evidence_text or ""),
        )

        # Recover reports_context from last dispatch step if present on result steps.
        reports_context = ""
        for st in reversed(list(result.steps or [])):
            detail = dict(st.detail or {})
            if detail.get("reports_snippet"):
                reports_context = str(detail.get("reports_snippet") or "")
                break

        steps_out = []
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
                    "n_purged_descendant_evidence": detail.get(
                        "n_purged_descendant_evidence"
                    ),
                    "branch_selected": detail.get("branch_selected"),
                    "collect_full": detail.get("collect_full"),
                    "n_legal_actions": detail.get("n_legal_actions"),
                    "legal_actions_preview": list(
                        detail.get("legal_actions_preview") or []
                    )[:20],
                    "projection_chars": detail.get("projection_chars"),
                }
            )

        case = {
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
            "steps": steps_out,
        }
        payload["cases"].append(case)

        case_path = out_dir / f"{iid}.json"
        case_path.write_text(json.dumps(case, ensure_ascii=False, indent=2), encoding="utf-8")
        print(
            f"[replay] done {iid}: old_recall={old_hit['recall']:.2f} "
            f"new_recall={new_hit['recall']:.2f} chars={result.evidence_chars_actual} "
            f"steps={result.trajectory_length} ({elapsed:.1f}s)",
            flush=True,
        )

    (out_dir / "all_cases.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (out_dir / "TRACE.md").write_text(_format_trace_md(payload), encoding="utf-8")
    print(f"[replay] wrote traces to {out_dir}", flush=True)

    # Auto-generate the human-readable per-run report (trace + hydration + evidence + scores).
    try:
        sys.path.insert(0, str(ROOT / "bin"))
        import importlib

        report_mod = importlib.import_module("58_report_map_nav_run")
        meta = {k: v for k, v in payload.items() if k != "cases"}
        report_md = report_mod.build_report(meta, list(payload.get("cases") or []))
        (out_dir / "REPORT.md").write_text(report_md + "\n", encoding="utf-8")
        print(f"[replay] wrote report to {out_dir / 'REPORT.md'}", flush=True)
    except Exception as exc:  # report is best-effort; never fail the replay
        print(f"[replay] report generation skipped: {exc}", flush=True)

    print(str(out_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
