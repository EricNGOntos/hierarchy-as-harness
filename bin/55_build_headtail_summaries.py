#!/usr/bin/env python3
"""Build non-LLM covers rollup section summaries for gold trees.

Non-leaf: ``This section covers:`` + self_only + all child titles, then head…tail.
Leaf: clipped self text. Writes cache/section_summaries_headtail (same path as before).
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "src"), str(ROOT / "src/realdata"), str(ROOT / "src/nav")]

from agent_delivery.code.load_data import bundles_from_paths  # noqa: E402
from summary_rollup import HEAD, TAIL, rollup_doc_summaries  # noqa: E402

OUT_DIR = ROOT / "cache/section_summaries_headtail"
CORPUS = ROOT / "data/corpus/test_data_full_realdata_clean_latest.jsonl"


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    bundles = bundles_from_paths(CORPUS, tree_source="gold")
    n = n_trunc = n_empty = n_nonleaf = 0
    index: dict[str, str] = {}

    for b in bundles:
        order = [r.line_id for r in b.lines]
        levels = b.levels_for_tree
        by_id = {r.line_id: (r.content or "") for r in b.lines}
        rolled = rollup_doc_summaries(order=order, levels=levels, line_text=by_id)

        rows: dict[str, dict] = {}
        for lid, row in rolled.items():
            sid = f"{b.doc_id}:L{lid}"
            summary = str(row.get("summary") or "")
            n_empty += int(not summary)
            n_trunc += int(bool(row.get("summary_truncated")))
            n_nonleaf += int(row.get("rollup_mode") == "title_enum")
            rows[sid] = {
                "section_id": sid,
                **row,
            }
            n += 1

        name = f"{b.doc_id}.json"
        (OUT_DIR / name).write_text(
            json.dumps(
                {"doc_id": b.doc_id, "n_sections": len(rows), "sections": rows},
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        index[b.doc_id] = name

    meta = {
        "version": "2.0",
        "corpus": str(CORPUS),
        "tree_source": "gold",
        "rule": (
            f"nonleaf: 'This section covers:' + self_only + child titles, "
            f"then head{HEAD}...tail{TAIL}; leaf: self head/tail; no LLM"
        ),
        "body_definition": (
            "leaf=self line; nonleaf self_only=own line; titles=direct child titles"
        ),
        "n_docs": len(bundles),
        "n_sections": n,
        "n_nonleaf_title_enum": n_nonleaf,
        "n_truncated_summary": n_trunc,
        "n_empty": n_empty,
        "elapsed_s": round(time.time() - t0, 3),
        "index": index,
    }
    (OUT_DIR / "manifest.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    with (OUT_DIR / "all_sections.jsonl").open("w", encoding="utf-8") as fh:
        for doc_id, name in index.items():
            data = json.loads((OUT_DIR / name).read_text(encoding="utf-8"))
            for row in data["sections"].values():
                fh.write(json.dumps({"doc_id": doc_id, **row}, ensure_ascii=False) + "\n")
    print(json.dumps({k: v for k, v in meta.items() if k != "index"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
