#!/usr/bin/env python3
"""E2E: 5 plan probes under task_corpus (__corpus__), planned vs baseline.

Measures: wall time, LLM tokens, gold_node pack/pool recall, compose answer
keyword hit against gold_answer.answer_text key facts.
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

OUT = ROOT / "map_nav_trace" / "plan_nav_e2e_complex5_corpus_b20k"
OUT.mkdir(parents=True, exist_ok=True)
os.environ["BODYRICH_LLM_API_CACHE_PATH"] = str(
    OUT / "llm_api_cache.jsonl"
)
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


def _cfg_planned() -> NavConfig:
    cfg = NavConfig.from_dict(
        json.loads((ROOT / "config/nav_default.json").read_text())
    )
    cfg.map_mode = True
    cfg.enable_query_planning = True
    cfg.enable_per_subgoal_illumination = True
    cfg.enable_goal_conditioned_folding = True
    cfg.enable_plan_orchestration = True
    cfg.enable_contract_verify = True
    cfg.enable_subgoal_budget_ledger = True
    cfg.subgoal_budget_floor_frac = 1.0
    cfg.max_replans = 1
    cfg.subgoal_max_attempts = 2
    cfg.max_waves = 0
    return cfg


def _cfg_baseline() -> NavConfig:
    cfg = NavConfig.from_dict(
        json.loads((ROOT / "config/nav_default.json").read_text())
    )
    cfg.map_mode = True
    cfg.enable_query_planning = False
    cfg.enable_per_subgoal_illumination = False
    cfg.enable_goal_conditioned_folding = False
    cfg.enable_plan_orchestration = False
    cfg.enable_contract_verify = False
    cfg.enable_subgoal_budget_ledger = False
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


def _answer_key_checks(case: dict, composed: str, evidence: str) -> dict:
    """Lightweight: require a few distinctive gold phrases in compose or evidence."""
    ga = case.get("gold_answer") or {}
    answer_text = str(ga.get("answer_text") or "")
    # Pick short distinctive anchors from structured fields + answer_text.
    anchors: list[str] = []
    for key in ("seal_type", "response_level", "right_clause"):
        v = ga.get(key)
        if isinstance(v, str) and len(v.strip()) >= 2:
            anchors.append(v.strip()[:40])
    # Fall back: extract 3–6 Chinese chunks of length>=4 from answer_text
    if len(anchors) < 2:
        parts = re.findall(r"[\u4e00-\u9fff]{4,12}", answer_text)
        # Prefer distinctive-looking ones
        for p in parts:
            if p not in anchors:
                anchors.append(p)
            if len(anchors) >= 5:
                break
    # Case-specific hard anchors
    cid = case["id"]
    if "seal" in cid:
        anchors = ["法人章", "审批", "登记"]
    elif "accident_grade" in cid or "ii_response" in cid:
        if "ii_response" in cid:
            anchors = ["Ⅱ级", "信息报告", "应急"]
        else:
            anchors = ["Ⅰ级", "总指挥", "1小时"]
    elif "worker_right" in cid:
        anchors = ["停止作业", "紧急情况", "监督检查"]
    elif "hazard" in cid:
        anchors = ["重大事故隐患", "一般事故隐患", "报告"]

    blob = (composed or "") + "\n" + (evidence or "")
    hits = [a for a in anchors if a and a in blob]
    return {
        "anchors": anchors,
        "n_hit": len(hits),
        "n_anchors": len(anchors),
        "hit_rate": (len(hits) / len(anchors)) if anchors else 0.0,
        "hits": hits,
        "misses": [a for a in anchors if a not in hits],
        "likely_answerable": (len(hits) / max(1, len(anchors))) >= 0.6,
    }


def main() -> int:
    load_llm_env()
    tasks = _load_tasks(TASKS)
    corpus_doc_ids = sorted(
        {str(t.doc_id).strip() for t in tasks if str(getattr(t, "doc_id", "") or "").strip()}
    )
    print(f"[e2e] corpus_docs={len(corpus_doc_ids)} budget={BUDGET}", flush=True)

    t_load = time.perf_counter()
    bundles = bundles_from_paths(
        CORPUS,
        tree_source="gold",
        doc_id_allowlist=set(corpus_doc_ids),
    )
    idx = CorpusIndex.from_bundles(
        bundles, tree_mode="gold", retrieval_backend="overlap"
    )
    tools = HierarchicalTools(idx)
    print(
        f"[e2e] loaded {len(bundles)} bundles in {time.perf_counter()-t_load:.1f}s",
        flush=True,
    )

    arms = [
        ("planned", _cfg_planned()),
        ("baseline", _cfg_baseline()),
    ]
    rows: list[dict] = []

    for arm_name, cfg in arms:
        for case in PROBE["cases"]:
            cid = case["id"]
            print(f"\n=== {arm_name} :: {cid} ===", flush=True)
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
            seconds = time.perf_counter() - t0
            after = snapshot_usage()
            usage = _usage_delta(before, after)

            if ep is None:
                row = {
                    "arm": arm_name,
                    "id": cid,
                    "error": err,
                    "seconds": seconds,
                    "usage": usage,
                }
                rows.append(row)
                (OUT / f"{arm_name}__{cid}.json").write_text(
                    json.dumps(row, ensure_ascii=False, indent=2), encoding="utf-8"
                )
                continue

            pack = _gold_hit(case["gold_nodes"], list(ep.retrieved_nodes or []))
            pool = _gold_hit(
                case["gold_nodes"], sorted(_pool_nodes_from_scored(ep.scored_chunks))
            )
            ans = _answer_key_checks(
                case, ep.composed_answer or "", ep.evidence_text or ""
            )
            step_actions = [
                getattr(s, "action", None) for s in (ep.steps or [])
            ]
            plan_fallback = None
            n_subgoals = None
            for s in ep.steps or []:
                if getattr(s, "action", None) == "query_plan":
                    d = getattr(s, "detail", None) or {}
                    plan_fallback = d.get("fallback")
                    n_subgoals = d.get("n_subgoals")
            row = {
                "arm": arm_name,
                "id": cid,
                "doc_id": case["doc_id"],
                "seconds": round(seconds, 2),
                "usage": usage,
                "pack_recall": pack["recall"],
                "pack_hit": f"{pack['n_hit']}/{pack['n_gold']}",
                "pool_recall": pool["recall"],
                "pool_hit": f"{pool['n_hit']}/{pool['n_gold']}",
                "answer_checks": ans,
                "likely_answerable": ans["likely_answerable"],
                "evidence_chars": ep.evidence_chars_actual,
                "n_steps": len(ep.steps or []),
                "step_actions": step_actions,
                "plan_fallback": plan_fallback,
                "n_subgoals": n_subgoals,
                "composed_answer": (ep.composed_answer or "")[:2000],
                "evidence_text_head": (ep.evidence_text or "")[:1500],
                "retrieved_nodes": list(ep.retrieved_nodes or []),
                "pack_miss": pack["miss_nodes"],
                "mode": "task_corpus",
                "n_corpus_docs": len(corpus_doc_ids),
                "budget_chars": BUDGET,
            }
            rows.append(row)
            (OUT / f"{arm_name}__{cid}.json").write_text(
                json.dumps(row, ensure_ascii=False, indent=2), encoding="utf-8"
            )
            print(
                f"  sec={seconds:.1f} pack={pack['recall']:.2f} pool={pool['recall']:.2f} "
                f"ans={ans['hit_rate']:.2f} tok={usage['_total']['total_tokens']} "
                f"api={usage['_total']['api_calls']} cache={usage['_total']['cache_hits']}",
                flush=True,
            )

    summary = {
        "mode": "task_corpus",
        "budget_chars": BUDGET,
        "n_corpus_docs": len(corpus_doc_ids),
        "out_dir": str(OUT),
        "yesterday_single_doc_b20k_ref": {
            "note": "单文档 episode；产物已删，数字来自当时汇总",
            "planned_pack_recall": {
                "cond_seal_type_then_scope_and_approval": 1.00,
                "cond_accident_grade_then_roles_and_response": 0.71,
                "cond_worker_right_then_duty_plus_supervise": 0.57,
                "compose_hazard_then_fix_then_report": 0.74,
                "cond_ii_response_then_report_and_support": 1.00,
            },
            "baseline_pack_recall": {
                "cond_seal_type_then_scope_and_approval": 1.00,
                "cond_accident_grade_then_roles_and_response": 0.71,
                "cond_worker_right_then_duty_plus_supervise": 0.71,
                "compose_hazard_then_fix_then_report": 0.74,
                "cond_ii_response_then_report_and_support": 1.00,
            },
        },
        "rows": rows,
    }
    (OUT / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"\n[e2e] wrote {OUT/'summary.json'}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
