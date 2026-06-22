#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Optional


def _load(path: Path) -> Optional[dict[str, Any]]:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def _load_first(paths: list[Path]) -> Optional[dict[str, Any]]:
    for path in paths:
        loaded = _load(path)
        if loaded is not None:
            return loaded
    return None


def _fmt(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def _arm(payload: Optional[dict[str, Any]], name: str) -> dict[str, Any]:
    if not payload:
        return {}
    return ((payload.get("summary") or {}).get(name) or {})


def _cost(payload: Optional[dict[str, Any]], name: str) -> dict[str, Any]:
    if not payload:
        return {}
    return (((payload.get("summary") or {}).get("cost") or {}).get(name) or {})


def _treerag_cost(payload: Optional[dict[str, Any]]) -> dict[str, Any]:
    if not payload:
        return {}
    summary = payload.get("summary") or {}
    cost = ((summary.get("cost") or {}).get("treerag") or {})
    if cost:
        return cost
    cfg = summary.get("config") or {}
    runtime = cfg.get("runtime_seconds")
    retrieval = cfg.get("retrieval_eval_seconds")
    preflight = float(cfg.get("preflight_seconds", 0.0) or 0.0)
    embedding = float(cfg.get("embedding_load_seconds", 0.0) or 0.0)
    data_load = float(cfg.get("data_load_seconds", 0.0) or 0.0)
    index = float(cfg.get("index_seconds", 0.0) or 0.0)
    cold = preflight + embedding + data_load + index
    if cold <= 0.0 and cfg.get("index_seconds") is not None:
        cold = index
    return {
        "cold_start_seconds": cold,
        "data_load_seconds": data_load,
        "embedding_load_seconds": embedding,
        "preflight_seconds": preflight,
        "index_build_seconds": index,
        "retrieval_framework_seconds": retrieval,
        "online_response_seconds": retrieval,
        "warm_end_to_end_eval_seconds": retrieval,
        "end_to_end_eval_seconds": runtime,
        "total_seconds": retrieval,
    }


def _usage(cost: dict[str, Any]) -> dict[str, int]:
    usage = cost.get("token_usage_total") or {}
    return {
        "prompt_tokens": int(usage.get("prompt_tokens", 0) or 0),
        "completion_tokens": int(usage.get("completion_tokens", 0) or 0),
        "total_tokens": int(usage.get("total_tokens", 0) or 0),
        "api_calls": int(usage.get("api_calls", 0) or 0),
        "cache_hits": int(usage.get("cache_hits", 0) or 0),
    }


def _usage_excluding(cost: dict[str, Any], excluded: set[str]) -> dict[str, int]:
    total = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0, "api_calls": 0}
    by_purpose = cost.get("token_usage_by_purpose") or {}
    if not isinstance(by_purpose, dict):
        return _usage(cost)
    saw_any = False
    for purpose, block in by_purpose.items():
        if str(purpose) in excluded or not isinstance(block, dict):
            continue
        saw_any = True
        for key in total:
            total[key] += int(block.get(key, 0) or 0)
    # A real by-purpose map containing only excluded phases means zero tokens
    # for this view; fallback is only for legacy payloads without such a map.
    return total if by_purpose else _usage(cost)


def _treerag_retrieval_view(payload: Optional[dict[str, Any]]) -> dict[str, Any]:
    cost = _treerag_cost(payload)
    retrieval = float(cost.get("retrieval_framework_seconds", 0.0) or 0.0)
    cold = float(cost.get("cold_start_seconds", 0.0) or 0.0)
    return {
        **cost,
        "compose_seconds": 0.0,
        "judge_eval_seconds": 0.0,
        "online_response_seconds": retrieval,
        "warm_end_to_end_eval_seconds": retrieval,
        "end_to_end_eval_seconds": cold + retrieval,
        "total_seconds": retrieval,
    }


def _treerag(payload: Optional[dict[str, Any]]) -> dict[str, Any]:
    if not payload:
        return {}
    return ((payload.get("summary") or {}).get("treerag") or {})


def _treerag_cfg(payload: Optional[dict[str, Any]]) -> dict[str, Any]:
    if not payload:
        return {}
    return ((payload.get("summary") or {}).get("config") or {})


def _cache_hits(payload: Optional[dict[str, Any]]) -> str:
    cfg = _treerag_cfg(payload)
    score_hits = cfg.get("budget_score_cache_hits")
    llm_hits = cfg.get("llm_cache_hits")
    doc_hits = cfg.get("doc_index_cache_hits")
    parts = []
    if score_hits is not None:
        parts.append(f"score={score_hits}")
    if llm_hits is not None:
        parts.append(f"llm={llm_hits}")
    if doc_hits is not None:
        parts.append(f"doc={doc_hits}")
    return ", ".join(parts)


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize RealData Gold/Pred/Flat plus TreeRAG baseline.")
    parser.add_argument("--budgets", default="500")
    parser.add_argument("--gpf-template", default="results/latest_clean_quality_balanced60_gold_flat_quality_balanced60_costclean_v1_b{budget}.json")
    parser.add_argument("--treerag-template", default="results/latest_clean_treerag_quality_balanced60_costclean_v1_b{budget}.json")
    parser.add_argument("--treerag-wrapper-template", default="results/latest_clean_treerag_quality_balanced60_costclean_v1_b{budget}.json")
    parser.add_argument("--out-md", type=Path, default=Path("cache/compare_run_summary.md"))
    args = parser.parse_args()

    lines = ["# RealData Latest Baselines", ""]
    lines.append("## Quality")
    lines.append("")
    lines.append("| budget | Gold task | Pred task | Flat task | TreeRAG coverage-only | TreeRAG+wrapper task | Gold evidence | Pred evidence | Flat evidence | TreeRAG coverage | TreeRAG+wrapper evidence |")
    lines.append("| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |")
    loaded: list[tuple[int, Optional[dict[str, Any]], Optional[dict[str, Any]], Optional[dict[str, Any]]]] = []
    for raw in str(args.budgets).split(","):
        if not raw.strip():
            continue
        budget = int(raw.strip())
        gpf = _load(Path(str(args.gpf_template).format(budget=budget)))
        tr = _load(Path(str(args.treerag_template).format(budget=budget)))
        trw = _load(Path(str(args.treerag_wrapper_template).format(budget=budget)))
        loaded.append((budget, gpf, tr, trw))
        gold = _arm(gpf, "hierarchical_gold")
        pred = _arm(gpf, "hierarchical_pred")
        flat = _arm(gpf, "flat")
        treerag = _treerag(tr)
        treerag_wrapper = _treerag(trw)
        treerag_for_coverage = treerag or treerag_wrapper
        lines.append(
            f"| {budget} | {_fmt(gold.get('score_task_mean'))} | {_fmt(pred.get('score_task_mean'))} | {_fmt(flat.get('score_task_mean'))} | "
            f"{_fmt(treerag_for_coverage.get('coverage_budget_lenient_mean'))} | {_fmt(treerag_wrapper.get('score_task_mean'))} | "
            f"{_fmt(gold.get('score_evidence_mean'))} | {_fmt(pred.get('score_evidence_mean'))} | {_fmt(flat.get('score_evidence_mean'))} | "
            f"{_fmt(treerag_for_coverage.get('coverage_budget_lenient_mean'))} | {_fmt(treerag_wrapper.get('score_evidence_mean'))} |"
        )

    lines.append("")
    lines.append("## Time And Token")
    lines.append("")
    lines.append("> 本表记录本次缓存辅助重跑的实测耗时与增量计费 token；cache hit 的 token 记为 0，不代表无缓存完整运行成本。")
    lines.append("")
    lines.append("| budget | arm | cold start | retrieval framework | compose | judge | online response | end-to-end eval | prompt | completion | total tokens | API calls | cache hits |")
    lines.append("| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |")
    for budget, gpf, tr, trw in loaded:
        for arm, label in [
            ("hierarchical_gold", "Gold"),
            ("hierarchical_pred", "Pred"),
            ("flat", "Flat"),
        ]:
            cost = _cost(gpf, arm)
            usage = _usage(cost)
            lines.append(
                f"| {budget} | {label} | {_fmt(cost.get('cold_start_seconds'))} | "
                f"{_fmt(cost.get('retrieval_framework_seconds'))} | {_fmt(cost.get('compose_seconds'))} | "
                f"{_fmt(cost.get('judge_eval_seconds'))} | {_fmt(cost.get('online_response_seconds'))} | "
                f"{_fmt(cost.get('end_to_end_eval_seconds'))} | {_fmt(usage['prompt_tokens'])} | "
                f"{_fmt(usage['completion_tokens'])} | {_fmt(usage['total_tokens'])} | {_fmt(usage['api_calls'])} | "
                f"{_fmt(usage.get('cache_hits'))} |"
            )
        retrieval_payload = tr or trw
        for payload, label in [(retrieval_payload, "TreeRAG retrieval-only"), (trw, "TreeRAG+wrapper")]:
            cost = _treerag_retrieval_view(payload) if label == "TreeRAG retrieval-only" else _treerag_cost(payload)
            usage = _usage_excluding(_treerag_cost(payload), {"compose", "judge"}) if label == "TreeRAG retrieval-only" else _usage(cost)
            if not any(usage.values()) and not (_treerag_cost(payload).get("token_usage_by_purpose") or {}):
                cfg = _treerag_cfg(payload)
                usage = cfg.get("token_usage") or {}
            lines.append(
                f"| {budget} | {label} | {_fmt(cost.get('cold_start_seconds'))} | "
                f"{_fmt(cost.get('retrieval_framework_seconds'))} | {_fmt(cost.get('compose_seconds'))} | "
                f"{_fmt(cost.get('judge_eval_seconds'))} | {_fmt(cost.get('online_response_seconds'))} | "
                f"{_fmt(cost.get('end_to_end_eval_seconds'))} | {_fmt(usage.get('prompt_tokens'))} | "
                f"{_fmt(usage.get('completion_tokens'))} | {_fmt(usage.get('total_tokens'))} | {_fmt(usage.get('api_calls'))} | "
                f"{_cache_hits(payload)} |"
            )

    args.out_md.parent.mkdir(parents=True, exist_ok=True)
    args.out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {args.out_md}")


if __name__ == "__main__":
    main()
