#!/usr/bin/env python3
"""Merge reusable caches into an append-only full-400 run directory."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import time
from pathlib import Path


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _merge_jsonl_by_key(sources: list[Path], destination: Path) -> dict:
    rows: dict[str, dict] = {}
    source_stats = []
    for source in sources:
        seen = 0
        accepted = 0
        if source.exists():
            with source.open(encoding="utf-8") as handle:
                for line in handle:
                    try:
                        row = json.loads(line)
                    except (ValueError, TypeError):
                        continue
                    key = str(row.get("key") or "")
                    if not key:
                        continue
                    seen += 1
                    if key not in rows:
                        rows[key] = row
                        accepted += 1
        source_stats.append({"path": str(source), "rows": seen, "accepted": accepted})
    destination.parent.mkdir(parents=True, exist_ok=True)
    tmp = destination.with_suffix(destination.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as handle:
        for key in sorted(rows):
            handle.write(json.dumps(rows[key], ensure_ascii=False, separators=(",", ":")) + "\n")
        handle.flush()
    tmp.replace(destination)
    return {"destination": str(destination), "unique_rows": len(rows), "sources": source_stats}


def _merge_trees(sources: list[Path], destination: Path) -> dict:
    destination.mkdir(parents=True, exist_ok=True)
    copied = []
    reused = []
    conflicts = []
    for source_dir in sources:
        for source in sorted((source_dir / "trees").glob("*.pkl")):
            target = destination / source.name
            source_hash = _sha256(source)
            if target.exists():
                target_hash = _sha256(target)
                reused.append(source.name)
                if source_hash != target_hash:
                    conflicts.append({
                        "tree": source.name,
                        "kept": str(target),
                        "ignored": str(source),
                        "kept_sha256": target_hash,
                        "ignored_sha256": source_hash,
                    })
                continue
            shutil.copy2(source, target)
            copied.append({"tree": source.name, "source": str(source), "sha256": source_hash})
    inventory = [
        {"tree": path.name, "sha256": _sha256(path), "bytes": path.stat().st_size}
        for path in sorted(destination.glob("*.pkl"))
    ]
    return {
        "destination": str(destination),
        "tree_count": len(inventory),
        "copied": copied,
        "reused_names": sorted(set(reused)),
        "conflicts_kept_first_source": conflicts,
        "inventory": inventory,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-root", type=Path, required=True)
    parser.add_argument("--shared-cache", type=Path, action="append", default=[])
    parser.add_argument("--treerag-cache", type=Path, action="append", default=[])
    args = parser.parse_args()
    args.run_root.mkdir(parents=True, exist_ok=True)
    tree_sources = [path.resolve() for path in args.treerag_cache]
    report = {
        "created_at": time.time(),
        "policy": "append-only; first tree with a cache-key filename wins; conflicts are recorded",
        "shared_llm_cache": _merge_jsonl_by_key(
            [path.resolve() for path in args.shared_cache],
            args.run_root / "shared_llm_api_cache.jsonl",
        ),
        "treerag_llm_cache": _merge_jsonl_by_key(
            [path / "llm_cache.jsonl" for path in tree_sources],
            args.run_root / "treerag" / "llm_cache.jsonl",
        ),
        "trees": _merge_trees(tree_sources, args.run_root / "treerag" / "trees"),
    }
    output = args.run_root / "cache_preparation_manifest.json"
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "manifest": str(output),
        "shared_cache_rows": report["shared_llm_cache"]["unique_rows"],
        "treerag_cache_rows": report["treerag_llm_cache"]["unique_rows"],
        "trees": report["trees"]["tree_count"],
        "tree_conflicts": len(report["trees"]["conflicts_kept_first_source"]),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
