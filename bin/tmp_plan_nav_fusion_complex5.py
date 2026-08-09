#!/usr/bin/env python3
"""Run all complex5 probes under PLAN×NAV fusion; compare to prior planned/baseline."""
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

OUT = ROOT / "map_nav_trace" / "plan_nav_fusion_complex5"
OUT.mkdir(parents=True, exist_ok=True)
os.environ["BODYRICH_LLM_API_CACHE_PATH"] = str(OUT / "llm_api_cache.jsonl")
os.environ["BODYRICH_LLM_API_CACHE"] = "1"

PRIOR_DIR = ROOT / "map_nav_trace" / "plan_nav_e2e_complex5_corpus_b20k"

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

# Already measured; skip unless --all
SKIP_DONE = {"cond_accident_grade_then_roles_and_response"}
# Prefer copying the prior fusion smoke result if present
SMOKE = (
    ROOT
    / "map_nav_trace"
    / "plan_nav_fusion_costliest_smoke"
    / "fusion__cond_accident_grade_then_roles_and_response.json"
)


def _cfg_fusion() -> NavConfig:
    cfg = NavConfig.from_dict(json.loads((ROOT / "config/nav_default.json").read_text()))
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
            "prompt_tokens": int(a.get("prompt_tokens", 0) or 0) - int(b.get("prompt_tokens", 0) or 0),
            "completion_tokens": int(a.get("completion_tokens", 0) or 0)
            - int(b.get("completion_tokens", 0) or 0),
            "total_tokens": int(a.get("total_tokens", 0) or 0) - int(b.get("total_tokens", 0) or 0),
            "api_calls": int(a.get("api_calls", 0) or 0) - int(b.get("api_calls", 0) or 0),
            "cache_hits": int(a.get("cache_hits", 0) or 0) - int(b.get("cache_hits", 0) or 0),
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
    anchors: list[str] = []
    cid = case["id"]
    if "seal" in cid:
        anchors = ["法人章", "审批", "登记"]
    elif "accident_grade" in cid:
        anchors = ["Ⅰ级", "总指挥", "1小时"]
    elif "ii_response" in cid:
        anchors = ["Ⅱ级", "信息报告", "应急"]
    elif "worker_right" in cid:
        anchors = ["停止作业", "紧急情况", "监督检查"]
    elif "hazard" in cid:
        anchors = ["重大事故隐患", "一般事故隐患", "报告"]
    blob = (composed or "") + "\n" + (evidence or "")
    hits = [a for a in anchors if a and a in blob]
    return {
        "anchors": anchors,
        "hits": hits,
        "misses": [a for a in anchors if a not in hits],
        "hit_rate": (len(hits) / len(anchors)) if anchors else 0.0,
        "likely_answerable": (len(hits) / max(1, len(anchors))) >= 0.6,
    }


def _extract_final(composed: str) -> str:
    raw = (composed or "").strip()
    if not raw:
        return ""
    try:
        obj = json.loads(raw)
        return str(obj.get("final_answer") or raw)
    except Exception:
        return raw


def main() -> int:
    run_all = "--all" in sys.argv
    load_llm_env()
    tasks = _load_tasks(TASKS)
    corpus_doc_ids = sorted(
        {str(t.doc_id).strip() for t in tasks if str(getattr(t, "doc_id", "") or "").strip()}
    )
    print(f"[fusion5] corpus_docs={len(corpus_doc_ids)}", flush=True)
    t_load = time.perf_counter()
    bundles = bundles_from_paths(
        CORPUS, tree_source="gold", doc_id_allowlist=set(corpus_doc_ids)
    )
    idx = CorpusIndex.from_bundles(bundles, tree_mode="gold", retrieval_backend="overlap")
    tools = HierarchicalTools(idx)
    print(f"[fusion5] loaded {len(bundles)} in {time.perf_counter()-t_load:.1f}s", flush=True)

    cfg = _cfg_fusion()
    rows: list[dict] = []

    # Reuse already-measured costliest case if present
    if not run_all and SMOKE.exists():
        smoke = json.loads(SMOKE.read_text())
        dest = OUT / f"fusion__{smoke['id']}.json"
        if not dest.exists():
            dest.write_text(json.dumps(smoke, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"[fusion5] reused smoke result for {smoke['id']}", flush=True)

    for case in PROBE["cases"]:
        cid = case["id"]
        out_path = OUT / f"fusion__{cid}.json"
        if out_path.exists() and not run_all:
            row = json.loads(out_path.read_text())
            rows.append(row)
            print(f"[fusion5] skip existing {cid}", flush=True)
            continue
        if (not run_all) and cid in SKIP_DONE and not out_path.exists() and SMOKE.exists():
            # already copied above
            row = json.loads(out_path.read_text())
            rows.append(row)
            continue

        print(f"\n=== fusion :: {cid} ===", flush=True)
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
            row = {"arm": "fusion", "id": cid, "error": err, "seconds": seconds, "usage": usage}
            rows.append(row)
            out_path.write_text(json.dumps(row, ensure_ascii=False, indent=2), encoding="utf-8")
            continue

        pack = _gold_hit(case["gold_nodes"], list(ep.retrieved_nodes or []))
        pool = _gold_hit(case["gold_nodes"], sorted(_pool_nodes_from_scored(ep.scored_chunks)))
        ans = _answer_key_checks(case, ep.composed_answer or "", ep.evidence_text or "")
        step_actions = [getattr(s, "action", None) for s in (ep.steps or [])]
        action_counts: dict[str, int] = {}
        for a in step_actions:
            k = str(a or "?")
            action_counts[k] = action_counts.get(k, 0) + 1
        n_subgoals = None
        n_replan = 0
        for s in ep.steps or []:
            act = getattr(s, "action", None)
            if act == "query_plan":
                n_subgoals = (getattr(s, "detail", None) or {}).get("n_subgoals")
            if act == "replan":
                n_replan += 1
        control_globals = []
        for s in ep.steps or []:
            if getattr(s, "action", None) == "plan_control":
                d = getattr(s, "detail", None) or {}
                control_globals.append(
                    {"global": d.get("global"), "subgoals": d.get("subgoals")}
                )

        row = {
            "arm": "fusion",
            "id": cid,
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
            "action_counts": action_counts,
            "n_subgoals": n_subgoals,
            "n_replan": n_replan,
            "plan_control": control_globals,
            "composed_answer": (ep.composed_answer or "")[:3000],
            "final_answer": _extract_final(ep.composed_answer or "")[:2000],
            "evidence_text_head": (ep.evidence_text or "")[:1500],
            "retrieved_nodes": list(ep.retrieved_nodes or []),
            "pack_miss": pack["miss_nodes"],
            "budget_chars": BUDGET,
        }
        rows.append(row)
        out_path.write_text(json.dumps(row, ensure_ascii=False, indent=2), encoding="utf-8")
        u = usage["_total"]
        print(
            f"  sec={seconds:.1f} pack={pack['recall']:.2f} pool={pool['recall']:.2f} "
            f"ans={ans['hit_rate']:.2f} api={u['api_calls']} prompt={u['prompt_tokens']} "
            f"replan={n_replan} actions={action_counts}",
            flush=True,
        )

    # Comparison table
    print("\n========== FUSION vs PRIOR ==========", flush=True)
    print(
        f"{'id':42} {'arm':8} {'api':>4} {'prompt':>8} {'pack':>5} {'pool':>5} {'ans':>4} {'replan':>6}",
        flush=True,
    )
    summary_rows = []
    for case in PROBE["cases"]:
        cid = case["id"]
        fus_path = OUT / f"fusion__{cid}.json"
        if not fus_path.exists():
            continue
        fus = json.loads(fus_path.read_text())
        for arm in ("baseline", "planned", "fusion"):
            if arm == "fusion":
                row = fus
            else:
                p = PRIOR_DIR / f"{arm}__{cid}.json"
                if not p.exists():
                    continue
                row = json.loads(p.read_text())
            u = (row.get("usage") or {}).get("_total") or {}
            ans = row.get("answer_checks") or {}
            hit = ans.get("hit_rate")
            if hit is None and arm == "fusion":
                hit = (row.get("answer_checks") or {}).get("hit_rate")
            print(
                f"{cid:42} {arm:8} {u.get('api_calls') or 0:4} {u.get('prompt_tokens') or 0:8} "
                f"{float(row.get('pack_recall') or 0):5.2f} {float(row.get('pool_recall') or 0):5.2f} "
                f"{float(hit or 0):4.2f} {int(row.get('n_replan') or 0):6}",
                flush=True,
            )
            summary_rows.append(
                {
                    "id": cid,
                    "arm": arm,
                    "api": u.get("api_calls"),
                    "prompt": u.get("prompt_tokens"),
                    "pack": row.get("pack_recall"),
                    "pool": row.get("pool_recall"),
                    "ans_hit_rate": hit,
                    "n_replan": row.get("n_replan"),
                    "final_answer_head": (row.get("final_answer") or row.get("composed_answer") or "")[
                        :300
                    ],
                }
            )

    (OUT / "summary.json").write_text(
        json.dumps({"rows": summary_rows, "fusion_rows": rows}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"\n[fusion5] wrote {OUT/'summary.json'}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
