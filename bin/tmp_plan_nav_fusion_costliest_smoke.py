#!/usr/bin/env python3
"""Smoke measure: costliest complex5 case under PLAN×NAV fusion flags.

Case: cond_accident_grade_then_roles_and_response
Prior planned arm (map_nav_trace/plan_nav_e2e_complex5_corpus_b20k):
  api=51  prompt≈667k  pack_recall≈0.619

This script runs ONLY that case with fusion ON, writes a comparable row, and
prints a side-by-side against the prior planned JSON.
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for p in (ROOT / "src" / "realdata", ROOT / "src" / "nav"):
    sys.path.insert(0, str(p))

os.environ.setdefault("NAV_MAP_MODE", "1")
os.environ.setdefault("NAV_MAP_DENSE", "0")
os.environ.setdefault("NAV_FILTER_COLLECTED_SECTIONS", "1")
summary = ROOT / "cache" / "section_summaries_headtail"
if summary.exists():
    os.environ.setdefault("NAV_SECTION_SUMMARY_DIR", str(summary))

CASE_ID = "cond_accident_grade_then_roles_and_response"
OUT = ROOT / "map_nav_trace" / "plan_nav_fusion_costliest_smoke"
OUT.mkdir(parents=True, exist_ok=True)
os.environ["BODYRICH_LLM_API_CACHE_PATH"] = str(OUT / "llm_api_cache.jsonl")
os.environ["BODYRICH_LLM_API_CACHE"] = "1"

from agent_delivery.code.hierarchical_tools import HierarchicalTools  # noqa: E402
from agent_delivery.code.index_retrieval import CorpusIndex  # noqa: E402
from agent_delivery.code.llm_config import load_llm_env  # noqa: E402
from agent_delivery.code.llm_usage import reset_usage, snapshot_usage  # noqa: E402
from agent_delivery.code.load_data import bundles_from_paths  # noqa: E402
from agent_delivery.agent.tasks_loader import _load_tasks  # noqa: E402
from nav_agent import run_nav_episode  # noqa: E402
from nav_types import NavConfig  # noqa: E402

BUDGET = 20000
PROBE = json.loads((ROOT / "data/probes/plan_nav_complex5_gold.json").read_text())
TASKS = ROOT / "data/tasks/tasks_realdata_bodyrich_latest_clean_400.jsonl"
CORPUS = ROOT / "data/corpus/test_data_full_realdata_clean_latest.jsonl"
PRIOR = (
    ROOT
    / "map_nav_trace"
    / "plan_nav_e2e_complex5_corpus_b20k"
    / f"planned__{CASE_ID}.json"
)


def _cfg_fusion() -> NavConfig:
    cfg = NavConfig.from_dict(
        json.loads((ROOT / "config/nav_default.json").read_text())
    )
    cfg.map_mode = True
    # Same PLAN surface as prior planned arm …
    cfg.enable_query_planning = True
    cfg.enable_per_subgoal_illumination = True
    cfg.enable_goal_conditioned_folding = True
    cfg.enable_plan_orchestration = True
    cfg.enable_slot_extract = True
    cfg.enable_subgoal_budget_ledger = True
    cfg.subgoal_budget_floor_frac = 1.0
    cfg.max_replans = 1
    cfg.subgoal_max_attempts = 2
    cfg.max_waves = 0
    # … plus fusion lean path.
    cfg.enable_anchor_entry = True
    cfg.enable_one_shot_harvest = True
    cfg.max_harvest_depth = 3
    cfg.enable_plan_control = True
    cfg.plan_control_digest_chars = 600
    cfg.show_harvested_in_map = True
    cfg.enable_settle_group_rank = True
    return cfg


def _usage_delta(before: dict, after: dict) -> dict:
    out: dict = {}
    keys = set(before) | set(after)
    totals = {
        "prompt_tokens": 0,
        "completion_tokens": 0,
        "total_tokens": 0,
        "api_calls": 0,
        "cache_hits": 0,
    }
    for k in sorted(keys):
        b = before.get(k) or {}
        a = after.get(k) or {}
        row = {
            "prompt_tokens": int(a.get("prompt_tokens", 0) or 0)
            - int(b.get("prompt_tokens", 0) or 0),
            "completion_tokens": int(a.get("completion_tokens", 0) or 0)
            - int(b.get("completion_tokens", 0) or 0),
            "total_tokens": int(a.get("total_tokens", 0) or 0)
            - int(b.get("total_tokens", 0) or 0),
            "api_calls": int(a.get("api_calls", 0) or 0)
            - int(b.get("api_calls", 0) or 0),
            "cache_hits": int(a.get("cache_hits", 0) or 0)
            - int(b.get("cache_hits", 0) or 0),
        }
        out[k] = row
        for t in totals:
            totals[t] += row[t]
    out["_total"] = totals
    return out


def _gold_hit(nodes: list[str], retrieved: list[str]) -> dict:
    g = set(nodes)
    r = set(retrieved or [])
    inter = g & r
    return {
        "n_gold": len(g),
        "n_hit": len(inter),
        "recall": (len(inter) / len(g)) if g else 0.0,
        "hit_nodes": sorted(inter),
        "miss_nodes": sorted(g - r),
    }


def _pool_nodes_from_scored(scored) -> set[str]:
    out: set[str] = set()
    for chunk, _ in scored or []:
        did = str(getattr(chunk, "doc_id", "") or "")
        for lid in getattr(chunk, "line_ids", ()) or ():
            out.add(f"{did}:L{lid}")
        sid = str(getattr(chunk, "section_id", "") or "")
        if sid:
            out.add(sid)
        nid = str(getattr(chunk, "node_id", "") or "")
        for suf in ("__path", "__intro", "__outline", "__self"):
            if nid.endswith(suf):
                out.add(nid[: -len(suf)])
                break
    return out


def main() -> int:
    load_llm_env()
    case = next(c for c in PROBE["cases"] if c["id"] == CASE_ID)
    tasks = _load_tasks(TASKS)
    corpus_doc_ids = sorted(
        {str(t.doc_id).strip() for t in tasks if str(getattr(t, "doc_id", "") or "").strip()}
    )
    print(f"[fusion-smoke] case={CASE_ID} corpus_docs={len(corpus_doc_ids)}", flush=True)

    t_load = time.perf_counter()
    bundles = bundles_from_paths(
        CORPUS, tree_source="gold", doc_id_allowlist=set(corpus_doc_ids)
    )
    idx = CorpusIndex.from_bundles(
        bundles, tree_mode="gold", retrieval_backend="overlap"
    )
    tools = HierarchicalTools(idx)
    print(f"[fusion-smoke] loaded {len(bundles)} bundles in {time.perf_counter()-t_load:.1f}s", flush=True)

    cfg = _cfg_fusion()
    reset_usage()
    before = snapshot_usage()
    t0 = time.perf_counter()
    err = None
    ep = None
    try:
        ep = run_nav_episode(
            tools,
            case["query"],
            doc_id=None,
            corpus_doc_ids=corpus_doc_ids,
            budget_chars=BUDGET,
            task_type="multi_hop",
            compose_answer=True,
            policy="llm",
            config=cfg,
        )
    except Exception as exc:  # noqa: BLE001
        err = f"{type(exc).__name__}: {exc}"
        print(f"[error] {err}", flush=True)
        import traceback

        traceback.print_exc()
    seconds = time.perf_counter() - t0
    usage = _usage_delta(before, snapshot_usage())

    if ep is None:
        row = {"arm": "fusion", "id": CASE_ID, "error": err, "seconds": seconds, "usage": usage}
        (OUT / f"fusion__{CASE_ID}.json").write_text(
            json.dumps(row, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        return 1

    pack = _gold_hit(case["gold_nodes"], list(ep.retrieved_nodes or []))
    pool = _gold_hit(case["gold_nodes"], sorted(_pool_nodes_from_scored(ep.scored_chunks)))
    step_actions = [getattr(s, "action", None) for s in (ep.steps or [])]
    action_counts: dict[str, int] = {}
    for a in step_actions:
        k = str(a or "?")
        action_counts[k] = action_counts.get(k, 0) + 1
    n_subgoals = None
    for s in ep.steps or []:
        if getattr(s, "action", None) == "query_plan":
            d = getattr(s, "detail", None) or {}
            n_subgoals = d.get("n_subgoals")

    row = {
        "arm": "fusion",
        "id": CASE_ID,
        "seconds": round(seconds, 2),
        "usage": usage,
        "pack_recall": pack["recall"],
        "pack_hit": f"{pack['n_hit']}/{pack['n_gold']}",
        "pool_recall": pool["recall"],
        "pool_hit": f"{pool['n_hit']}/{pool['n_gold']}",
        "evidence_chars": ep.evidence_chars_actual,
        "n_steps": len(ep.steps or []),
        "step_actions": step_actions,
        "action_counts": action_counts,
        "n_subgoals": n_subgoals,
        "composed_answer": (ep.composed_answer or "")[:2000],
        "evidence_text_head": (ep.evidence_text or "")[:1500],
        "retrieved_nodes": list(ep.retrieved_nodes or []),
        "pack_miss": pack["miss_nodes"],
        "budget_chars": BUDGET,
        "fusion_flags": {
            "enable_anchor_entry": True,
            "enable_one_shot_harvest": True,
            "enable_plan_control": True,
            "show_harvested_in_map": True,
            "enable_settle_group_rank": True,
        },
    }
    (OUT / f"fusion__{CASE_ID}.json").write_text(
        json.dumps(row, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    prior = json.loads(PRIOR.read_text()) if PRIOR.exists() else None
    print("\n========== COST COMPARISON ==========", flush=True)
    print(f"case: {CASE_ID}", flush=True)
    print(
        f"fusion:  api={usage['_total']['api_calls']} "
        f"prompt={usage['_total']['prompt_tokens']} "
        f"compl={usage['_total']['completion_tokens']} "
        f"pack={pack['recall']:.3f} pool={pool['recall']:.3f} "
        f"sec={seconds:.1f} steps={row['n_steps']} "
        f"actions={action_counts}",
        flush=True,
    )
    if prior:
        pu = (prior.get("usage") or {}).get("_total") or {}
        print(
            f"prior planned: api={pu.get('api_calls')} "
            f"prompt={pu.get('prompt_tokens')} "
            f"compl={pu.get('completion_tokens')} "
            f"pack={prior.get('pack_recall')} pool={prior.get('pool_recall')} "
            f"sec={prior.get('seconds')} steps={prior.get('n_steps')}",
            flush=True,
        )
        if pu.get("api_calls"):
            print(
                f"api ratio fusion/planned = "
                f"{usage['_total']['api_calls'] / max(1, int(pu['api_calls'])):.2f}",
                flush=True,
            )
        if pu.get("prompt_tokens"):
            print(
                f"prompt ratio fusion/planned = "
                f"{usage['_total']['prompt_tokens'] / max(1, int(pu['prompt_tokens'])):.2f}",
                flush=True,
            )
    print("by_purpose (fusion):", flush=True)
    for k, v in sorted(usage.items()):
        if k == "_total":
            continue
        if v.get("api_calls") or v.get("prompt_tokens"):
            print(f"  {k}: {v}", flush=True)
    print(f"wrote {OUT / f'fusion__{CASE_ID}.json'}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
