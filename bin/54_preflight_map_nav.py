#!/usr/bin/env python3
"""Fail-fast checks before Map-Nav 400-run (remote embeddings, no local GPU)."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _ok(msg: str) -> None:
    print(f"[ok] {msg}")


def _fail(msg: str) -> None:
    print(f"[FAIL] {msg}", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--embedding-model",
        default=os.environ.get("EMBEDDING_MODEL")
        or os.environ.get("BODYRICH_EMBEDDING_MODEL")
        or "text-embedding-v3",
    )
    parser.add_argument(
        "--embedding-backend",
        default=os.environ.get("BODYRICH_EMBEDDING_BACKEND")
        or os.environ.get("EMBEDDING_BACKEND")
        or "remote",
    )
    args = parser.parse_args()

    sys.path.insert(0, str(ROOT / "src" / "realdata"))
    sys.path.insert(0, str(ROOT / "src" / "nav"))

    required = [
        ROOT / "data/corpus/test_data_full_realdata_clean_latest.jsonl",
        ROOT / "data/realdata_clean_m1024_best_pred_levels_prevline_fallback.jsonl",
        ROOT / "data/tasks/tasks_realdata_bodyrich_latest_clean_400.jsonl",
        ROOT / "data/tasks/tasks_realdata_bodyrich_latest_clean_400.inspect.jsonl",
        ROOT / "results/latest_clean400_goldnav_e2_v1_gold_flat_b500.json",
        ROOT / "results/latest_clean400_goldnav_e2_v1_treerag_b500.json",
        ROOT / "config/nav_default.json",
        ROOT / "bin/44_run_pred_only_bodyrich.py",
        ROOT / "bin/53_summarize_map_nav.py",
    ]
    for path in required:
        if not path.exists():
            _fail(f"missing required file: {path}")
        _ok(f"file {path.relative_to(ROOT)}")

    from agent_delivery.code.llm_config import load_llm_env, require_llm_env

    load_llm_env()
    try:
        require_llm_env(context="preflight")
    except Exception as exc:
        _fail(f"LLM env: {exc}")
    _ok(
        "LLM key present "
        f"nav={os.environ.get('NAV_LLM_MODEL')} compose={os.environ.get('COMPOSE_MODEL')}"
    )

    os.environ["BODYRICH_EMBEDDING_BACKEND"] = args.embedding_backend
    os.environ["BODYRICH_EMBEDDING_MODEL"] = args.embedding_model
    os.environ["EMBEDDING_MODEL"] = args.embedding_model

    from agent_delivery.code.embedding_backend import (
        embedding_backend_kind,
        get_dense_encoder,
        encode_query_normalized,
        _embedding_cache_dir,
    )

    kind = embedding_backend_kind()
    if kind != "remote":
        print(
            f"[warn] embedding backend={kind}; this machine has no GPU. Prefer BODYRICH_EMBEDDING_BACKEND=remote.",
            file=sys.stderr,
        )

    try:
        enc = get_dense_encoder(args.embedding_model)
        dim = int(enc.get_sentence_embedding_dimension())
        q = encode_query_normalized(enc, "preflight query 安全职责")
        if int(q.shape[0]) != dim:
            _fail(f"query dim {q.shape[0]} != model dim {dim}")
        _ok(f"embedding backend={kind} model={args.embedding_model} dim={dim}")
        _ok(f"embedding cache dir={_embedding_cache_dir()}")
    except Exception as exc:
        _fail(f"embedding preflight failed: {exc}")

    # Explicitly warn: legacy local bge-m3 .npy caches are NOT compatible with remote v3.
    legacy = ROOT / "cache" / "embeddings"
    if legacy.exists() and kind == "remote":
        print(
            "[warn] legacy cache/embeddings (local bge-m3, 1024-d) will NOT be reused by "
            "remote text-embedding-v3 — different embedding space. New cache goes to "
            f"{_embedding_cache_dir()}. First run will remotely encode pools on demand."
        )

    import nav_projection  # noqa: F401
    import nav_actions  # noqa: F401
    import nav_agent  # noqa: F401
    _ok("nav map modules importable")
    print("[preflight] READY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
