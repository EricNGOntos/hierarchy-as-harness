#!/usr/bin/env python3
"""Precompute Flat dense vectors for the task-corpus (42-doc) search space.

Builds a Flat CorpusIndex over all doc_ids present in the tasks file and warms
the remote embedding text cache for the flat_chunks pool (text-embedding-v3).
TreeRAG tree/index warming is handled separately via --index-only.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REALDATA = ROOT / "src" / "realdata"
if str(REALDATA) not in sys.path:
    sys.path.insert(0, str(REALDATA))

from agent_delivery.code.embedding_backend import (  # noqa: E402
    resolve_embedding_model,
)
from agent_delivery.code.index_retrieval import CorpusIndex  # noqa: E402
from agent_delivery.code.llm_config import load_llm_env, require_llm_env  # noqa: E402
from agent_delivery.code.load_data import bundles_from_paths  # noqa: E402


def _doc_ids_from_tasks(path: Path) -> list[str]:
    ids: list[str] = []
    with path.open(encoding="utf-8") as handle:
        for raw in handle:
            line = raw.strip()
            if not line:
                continue
            ids.append(str(json.loads(line)["doc_id"]))
    return sorted(set(ids))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tasks", type=Path, required=True)
    parser.add_argument("--corpus", type=Path, required=True)
    parser.add_argument("--embedding-model", default=None)
    args = parser.parse_args()

    load_llm_env()
    require_llm_env(context="task-corpus flat embedding precompute")
    model_name = resolve_embedding_model(args.embedding_model)
    allow = _doc_ids_from_tasks(args.tasks)
    if not allow:
        raise SystemExit(f"no doc_ids found in {args.tasks}")

    t0 = time.perf_counter()
    bundles = bundles_from_paths(
        args.corpus,
        tree_source="flat",
        doc_id_allowlist=set(allow),
    )
    print(
        f"[flat-embed] docs={len(bundles)} allowlist={len(allow)} model={model_name}",
        flush=True,
    )
    idx = CorpusIndex.from_bundles(
        bundles,
        tree_mode="flat",
        retrieval_backend="dense",
        embedding_model=model_name,
    )
    pool = list(idx.flat_chunks)
    print(f"[flat-embed] flat_chunks={len(pool)} encoding…", flush=True)
    t1 = time.perf_counter()
    mat = idx._embeddings_for_pool(pool)
    encode_s = time.perf_counter() - t1
    shape = getattr(mat, "shape", None)
    payload = {
        "ok": True,
        "n_docs": len(bundles),
        "n_flat_chunks": len(pool),
        "embedding_model": model_name,
        "matrix_shape": list(shape) if shape is not None else None,
        "encode_seconds": encode_s,
        "total_seconds": time.perf_counter() - t0,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
