#!/usr/bin/env python3
"""Precompute path/content dense vectors for map-nav score units."""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for p in (ROOT / "src" / "realdata", ROOT / "src" / "nav"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from agent_delivery.code.embedding_backend import (  # noqa: E402
    encode_labeled_texts_normalized,
    get_dense_encoder,
    resolve_embedding_model,
)
from agent_delivery.code.hierarchical_tools import HierarchicalTools  # noqa: E402
from agent_delivery.code.index_retrieval import CorpusIndex  # noqa: E402
from agent_delivery.code.load_data import groups_to_bundles, load_test_groups  # noqa: E402
from agent_delivery.code.tool_space import ToolSpace  # noqa: E402
from nav_map_scores import build_score_units  # noqa: E402


def _doc_ids_from_tasks(path: Path) -> list[str]:
    ids = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            ids.append(str(json.loads(line)["doc_id"]))
    return sorted(set(ids))


def _precompute_tree(
    *,
    tree_source: str,
    groups: dict,
    pred_groups: dict | None,
    doc_ids: list[str],
    model,
    batch_size: int,
) -> dict:
    bundles = groups_to_bundles(
        {d: groups[d] for d in doc_ids},
        tree_source=tree_source,
        pred_groups=pred_groups if tree_source == "pred" else None,
    )
    idx = CorpusIndex.from_bundles(
        bundles,
        tree_mode="hierarchical",
        retrieval_backend="overlap",  # build tree only; dense via encode_labeled
    )
    ts = ToolSpace(HierarchicalTools(idx))
    total_units = 0
    total_vectors = 0
    encoded_vectors = 0
    t0 = time.perf_counter()
    for i, b in enumerate(bundles, 1):
        roots = ts.sections_for_doc(b.doc_id)
        units = build_score_units(ts, b.doc_id, root_ids=roots)
        unit_ids = [str(u["chunk_id"]) for u in units]
        path_texts = [str(u.get("path_text") or "") for u in units]
        content_texts = [str(u.get("content") or "") for u in units]
        n = len(unit_ids)
        total_units += n
        total_vectors += 2 * n
        print(
            f"[{tree_source}] {i}/{len(bundles)} doc={b.doc_id} lines={len(b.lines)} units={n}",
            flush=True,
        )
        # encode_labeled reports miss counts itself; call both channels
        before = time.perf_counter()
        encode_labeled_texts_normalized(
            model,
            doc_id=b.doc_id,
            channel="path",
            unit_ids=unit_ids,
            texts=path_texts,
            batch_size=batch_size,
            namespace=tree_source,
        )
        encode_labeled_texts_normalized(
            model,
            doc_id=b.doc_id,
            channel="content",
            unit_ids=unit_ids,
            texts=content_texts,
            batch_size=batch_size,
            namespace=tree_source,
        )
        encoded_vectors += 2 * n
        print(
            f"[{tree_source}] done doc={b.doc_id} in {time.perf_counter()-before:.1f}s",
            flush=True,
        )
    return {
        "tree_source": tree_source,
        "docs": len(bundles),
        "units": total_units,
        "vectors": total_vectors,
        "encoded_vectors": encoded_vectors,
        "seconds": round(time.perf_counter() - t0, 2),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tasks", type=Path, required=True)
    ap.add_argument("--corpus", type=Path, required=True)
    ap.add_argument("--pred-jsonl", type=Path, required=True)
    ap.add_argument("--tree-sources", type=str, default="gold,pred")
    ap.add_argument("--embedding-model", type=str, default="")
    ap.add_argument("--batch-size", type=int, default=0)
    args = ap.parse_args()

    doc_ids = _doc_ids_from_tasks(args.tasks)
    print(f"[precompute] tasks_docs={len(doc_ids)}", flush=True)
    print("[precompute] loading corpus…", flush=True)
    groups_all = load_test_groups(args.corpus)
    groups = {d: groups_all[d] for d in doc_ids if d in groups_all}
    missing = [d for d in doc_ids if d not in groups]
    if missing:
        raise SystemExit(f"missing docs in corpus: {missing[:5]}… ({len(missing)})")
    pred_all = load_test_groups(args.pred_jsonl)
    pred_groups = {d: pred_all[d] for d in doc_ids if d in pred_all}

    model_name = resolve_embedding_model(args.embedding_model or None)
    model = get_dense_encoder(model_name)
    batch = int(args.batch_size or os.environ.get("BODYRICH_EMBEDDING_BATCH_SIZE", "10") or "10")
    batch = max(1, min(batch, 10))

    trees = [t.strip() for t in str(args.tree_sources).split(",") if t.strip()]
    summaries = []
    for tree in trees:
        if tree not in {"gold", "pred"}:
            raise SystemExit(f"unsupported tree-source {tree!r}")
        summaries.append(
            _precompute_tree(
                tree_source=tree,
                groups=groups,
                pred_groups=pred_groups,
                doc_ids=doc_ids,
                model=model,
                batch_size=batch,
            )
        )

    print("[precompute] SUMMARY", flush=True)
    for s in summaries:
        print(json.dumps(s, ensure_ascii=False), flush=True)
    total_vectors = sum(int(s["vectors"]) for s in summaries)
    print(
        json.dumps(
            {
                "docs": len(doc_ids),
                "trees": trees,
                "total_vectors": total_vectors,
                "note": "each unit contributes path+content (=2 vectors)",
            },
            ensure_ascii=False,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
