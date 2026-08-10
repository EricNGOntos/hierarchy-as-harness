#!/usr/bin/env python3
"""Run MAP-NAV over a knowhere document, BM25-only, no vectors.

Drives ``run_nav_episode`` through ``KnowhereProvider`` + ``ProviderToolSpace``
instead of this repo's line-indexed ToolSpace, so the only inputs are the
section/chunk rows knowhere already stores. Two arms per case: ``baseline``
(map navigation alone) and ``fusion`` (query planning + anchor entry + one-shot
harvest + plan control).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

ROOT = Path(__file__).resolve().parents[1]
for _p in (ROOT / "src" / "realdata", ROOT / "src" / "nav"):
    sys.path.insert(0, str(_p))

OUT = ROOT / "map_nav_trace" / "knowhere_probe"
OUT.mkdir(parents=True, exist_ok=True)

os.environ.setdefault("NAV_MAP_MODE", "1")
os.environ.setdefault("NAV_MAP_DENSE", "0")  # BM25 only: no vector store anywhere
os.environ.setdefault("NAV_FILTER_COLLECTED_SECTIONS", "1")
os.environ["NAV_SECTION_SUMMARY_DIR"] = str(OUT / "section_summaries")
os.environ.setdefault("BODYRICH_LLM_API_CACHE_PATH", str(OUT / "llm_api_cache.jsonl"))
os.environ.setdefault("BODYRICH_LLM_API_CACHE", "1")

from agent_delivery.code.llm_usage import reset_usage, snapshot_usage  # noqa: E402
from nav_agent import run_nav_episode  # noqa: E402
from nav_compose import evidence_owner_section_id  # noqa: E402
from nav_hierarchy import ProviderToolSpace  # noqa: E402
from nav_knowhere import (  # noqa: E402
    KnowhereProvider,
    NamespaceKnowhereProvider,
    load_debug_parse,
)
from nav_map_scores import (  # noqa: E402
    compute_corpus_map_and_unit_scores,
    compute_map_and_unit_scores,
    select_map_highlights,
)
from nav_projection import build_map  # noqa: E402
from nav_types import NavConfig  # noqa: E402
import section_summary_store  # noqa: E402


def export_summaries(provider: Any, dest_dir: Path) -> int:
    """Write provider summaries where ``section_summary_store`` reads them."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    summaries = provider.summaries()
    if isinstance(provider, NamespaceKnowhereProvider):
        n = 0
        for doc_id in provider.document_ids():
            owned = {
                sid: text
                for sid, text in summaries.items()
                if provider.owner_document(sid) == doc_id
            }
            payload = {
                "sections": {sid: {"summary": text} for sid, text in owned.items()}
            }
            (dest_dir / f"{doc_id}.json").write_text(
                json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8"
            )
            n += len(owned)
        section_summary_store.clear_cache()
        return n
    doc_id = str(getattr(provider, "doc_id", "") or "doc")
    payload = {"sections": {sid: {"summary": text} for sid, text in summaries.items()}}
    (dest_dir / f"{doc_id}.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    section_summary_store.clear_cache()
    return len(summaries)


def load_probe_toolspace(probe: dict) -> Tuple[Any, List[str], Any]:
    """Single-doc ``doc`` or multi-doc ``docs`` → toolspace + corpus ids + provider."""
    docs = list(probe.get("docs") or ())
    if not docs and probe.get("doc"):
        docs = [probe["doc"]]
    if not docs:
        raise ValueError("probe requires doc or docs")

    providers: List[KnowhereProvider] = []
    titles: Dict[str, str] = {}
    for spec in docs:
        provider = load_debug_parse(
            spec["track_dir"], doc_id=spec.get("doc_id") or None
        )
        providers.append(provider)
        title = str(spec.get("title") or "").strip()
        if title:
            titles[provider.doc_id] = title

    if len(providers) == 1:
        provider = providers[0]
        return ProviderToolSpace(provider), [], provider

    ns = NamespaceKnowhereProvider(providers, titles=titles or None)
    return ProviderToolSpace(ns), list(ns.document_ids()), ns


def cfg_baseline() -> NavConfig:
    cfg = NavConfig.from_dict(json.loads((ROOT / "config/nav_default.json").read_text()))
    cfg.map_mode = True
    return cfg


def cfg_fusion() -> NavConfig:
    cfg = cfg_baseline()
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


ARMS = {"baseline": cfg_baseline, "fusion": cfg_fusion}


def usage_delta(before: dict, after: dict) -> dict:
    totals = {
        "prompt_tokens": 0,
        "completion_tokens": 0,
        "api_calls": 0,
        "cache_hits": 0,
    }
    per_tag: Dict[str, dict] = {}
    for key in sorted(set(before) | set(after)):
        b, a = before.get(key) or {}, after.get(key) or {}
        row = {k: int(a.get(k, 0) or 0) - int(b.get(k, 0) or 0) for k in totals}
        if any(row.values()):
            per_tag[key] = row
            for k in totals:
                totals[k] += row[k]
    return {"_total": totals, "per_tag": per_tag}


def gold_hit(gold: Sequence[str], got: Sequence[str]) -> dict:
    gold_set, got_set = list(dict.fromkeys(gold)), set(got)
    hit = [g for g in gold_set if g in got_set]
    return {
        "n_gold": len(gold_set),
        "n_hit": len(hit),
        "recall": round(len(hit) / len(gold_set), 3) if gold_set else 0.0,
        "miss": [g for g in gold_set if g not in got_set],
    }


def key_checks(case: dict, answer: str, evidence: str) -> dict:
    keys = [str(k) for k in case.get("answer_keys") or ()]
    distractors = [str(k) for k in case.get("distractor_keys") or ()]
    in_answer = [k for k in keys if k in answer]
    in_evidence = [k for k in keys if k in evidence]
    return {
        "answer_keys_hit": f"{len(in_answer)}/{len(keys)}",
        "answer_keys_missing": [k for k in keys if k not in answer],
        "evidence_keys_hit": f"{len(in_evidence)}/{len(keys)}",
        "distractors_in_answer": [k for k in distractors if k in answer],
    }


def summarize_steps(episode: Any) -> dict:
    counts: Dict[str, int] = {}
    n_subgoals = None
    n_replan = 0
    control: List[dict] = []
    for step in episode.steps or ():
        action = str(getattr(step, "action", None) or "?")
        counts[action] = counts.get(action, 0) + 1
        detail = getattr(step, "detail", None) or {}
        if action == "query_plan":
            n_subgoals = detail.get("n_subgoals")
        elif action == "replan":
            n_replan += 1
        elif action == "plan_control":
            control.append({"global": detail.get("global"), "subgoals": detail.get("subgoals")})
    return {
        "action_counts": counts,
        "n_steps": len(episode.steps or ()),
        "n_subgoals": n_subgoals,
        "n_replan": n_replan,
        "plan_control": control,
    }


def run_case(
    case: dict,
    *,
    toolspace: Any,
    arm: str,
    budget: int,
    corpus_doc_ids: Optional[Sequence[str]] = None,
    default_doc_id: str = "",
) -> dict:
    gold_doc = str(case.get("doc_id") or default_doc_id or "").strip()
    gold = [f"{gold_doc}:{p}" for p in case.get("gold_paths") or ()] if gold_doc else []
    reset_usage()
    before = snapshot_usage()
    started = time.perf_counter()
    episode = None
    error = None
    try:
        corpus_ids = [str(d).strip() for d in (corpus_doc_ids or []) if str(d).strip()]
        episode = run_nav_episode(
            None,
            case["query"],
            doc_id=None if corpus_ids else (default_doc_id or None),
            corpus_doc_ids=corpus_ids or None,
            budget_chars=budget,
            task_type=str(case.get("task_type") or "unknown"),
            compose_answer=True,
            policy="llm",
            config=ARMS[arm](),
            toolspace=toolspace,
        )
    except Exception as exc:  # noqa: BLE001
        import traceback

        error = f"{type(exc).__name__}: {exc}"
        traceback.print_exc()
    seconds = time.perf_counter() - started
    usage = usage_delta(before, snapshot_usage())

    row: Dict[str, Any] = {
        "arm": arm,
        "id": case["id"],
        "seconds": round(seconds, 2),
        "usage": usage,
    }
    if episode is None:
        row["error"] = error
        return row

    answer = episode.composed_answer or ""
    evidence = episode.evidence_text or ""
    # Gold is labelled at knowhere's section granularity, so score the owning
    # sections of the packed evidence rather than this repo's line-node ids.
    packed_sections = list(
        dict.fromkeys(
            sid
            for sid in (evidence_owner_section_id(c) for c in episode.kept_chunks or ())
            if sid
        )
    )
    pack = gold_hit(gold, packed_sections)
    row.update(
        {
            "pack_recall": pack["recall"],
            "pack_hit": f"{pack['n_hit']}/{pack['n_gold']}",
            "pack_miss": pack["miss"],
            "checks": key_checks(case, answer, evidence),
            "evidence_chars": episode.evidence_chars_actual,
            "packed_sections": packed_sections,
            "composed_answer": answer[:4000],
            **summarize_steps(episode),
        }
    )
    return row


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--probe", default=str(ROOT / "data/probes/knowhere_changheba.json"))
    parser.add_argument("--arms", default="baseline,fusion")
    parser.add_argument("--budget-chars", type=int, default=12000)
    parser.add_argument("--case", default="", help="run only this case id")
    parser.add_argument("--dry-run", action="store_true", help="print the map, run no LLM")
    args = parser.parse_args()

    probe = json.loads(Path(args.probe).read_text(encoding="utf-8"))
    toolspace, corpus_doc_ids, provider = load_probe_toolspace(probe)
    n_summaries = export_summaries(provider, OUT / "section_summaries")
    default_doc_id = (
        ""
        if corpus_doc_ids
        else str(getattr(provider, "doc_id", "") or "")
    )

    if corpus_doc_ids:
        n_sections = len(provider.all_section_ids())
        n_roots = len(toolspace.sections_for_doc(""))
        n_units = sum(
            len(provider.self_units(sid)) for sid in provider.all_section_ids()
        )
        print(
            f"[knowhere] namespace docs={corpus_doc_ids} sections={n_sections} "
            f"doc_nodes={n_roots} units={n_units} summaries={n_summaries}",
            flush=True,
        )
    else:
        roots = provider.roots(provider.doc_id)
        all_units = sum(
            len(provider.self_units(sid)) for sid in provider.all_section_ids()
        )
        print(
            f"[knowhere] doc_id={provider.doc_id} sections={len(provider.all_section_ids())} "
            f"roots={len(roots)} units={all_units} summaries={n_summaries}",
            flush=True,
        )

    if args.dry_run:
        cfg = cfg_baseline()
        for case in probe["cases"]:
            if args.case and case["id"] != args.case:
                continue
            gold_doc = str(case.get("doc_id") or default_doc_id or "").strip()
            gold = (
                [f"{gold_doc}:{p}" for p in case.get("gold_paths") or ()]
                if gold_doc
                else []
            )
            known = set(provider.all_section_ids())
            missing = [g for g in gold if g not in known]
            print(f"\n[case] {case['id']}  gold={len(gold)} missing_gold={missing}")
            for g in gold:
                units = provider.self_units(g)
                text = "\n".join(provider.unit_text(u) for u in units)
                print(f"  - {g}\n    units={len(units)} chars={len(text)}")
            query = str(case["query"])
            if corpus_doc_ids:
                map_scores, unit_scores = compute_corpus_map_and_unit_scores(
                    toolspace, doc_ids=corpus_doc_ids, query=query
                )
                episode_doc = ""
            else:
                roots = list(toolspace.sections_for_doc(default_doc_id))
                map_scores, unit_scores = compute_map_and_unit_scores(
                    toolspace,
                    doc_id=default_doc_id,
                    query=query,
                    root_ids=roots,
                )
                episode_doc = default_doc_id
            highlights = select_map_highlights(unit_scores, k=int(cfg.collect_top_k))
            proj = build_map(
                toolspace,
                doc_id=episode_doc,
                query=query,
                scope=None,
                config=cfg,
                map_scores=map_scores,
                highlight_ids=highlights,
            )
            print(
                f"  map_chars={len(proj.text)} hits={len(proj.highlight_ids)} "
                f"visible={len(proj.tree_sections)}"
            )
            print(proj.text[:2500])
            if len(proj.text) > 2500:
                print("  ... [map truncated for dry-run stdout]")
        return

    rows: List[dict] = []
    for arm in [a.strip() for a in args.arms.split(",") if a.strip()]:
        for case in probe["cases"]:
            if args.case and case["id"] != args.case:
                continue
            print(f"\n=== {arm} :: {case['id']} ===", flush=True)
            row = run_case(
                case,
                toolspace=toolspace,
                arm=arm,
                budget=args.budget_chars,
                corpus_doc_ids=corpus_doc_ids or None,
                default_doc_id=default_doc_id,
            )
            rows.append(row)
            (OUT / f"{arm}__{case['id']}.json").write_text(
                json.dumps(row, ensure_ascii=False, indent=2), encoding="utf-8"
            )
            if "error" in row:
                print(f"  ERROR {row['error']}", flush=True)
                continue
            total = row["usage"]["_total"]
            print(
                f"  sec={row['seconds']} pack={row['pack_recall']} ({row['pack_hit']}) "
                f"answer_keys={row['checks']['answer_keys_hit']} "
                f"distractor={row['checks']['distractors_in_answer']} "
                f"api={total['api_calls']} prompt={total['prompt_tokens']} "
                f"actions={row['action_counts']}",
                flush=True,
            )

    (OUT / "summary.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
