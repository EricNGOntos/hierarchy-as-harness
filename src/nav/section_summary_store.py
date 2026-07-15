from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

_ROOT = Path(__file__).resolve().parents[2]
_DEFAULT_DIR = _ROOT / "cache" / "section_summaries_headtail"

_doc_cache: Dict[str, Dict[str, Any]] = {}


def summary_cache_dir() -> Path:
    raw = os.environ.get("NAV_SECTION_SUMMARY_DIR", "").strip()
    return Path(raw) if raw else _DEFAULT_DIR


def _load_doc(doc_id: str) -> Dict[str, Any]:
    if doc_id in _doc_cache:
        return _doc_cache[doc_id]
    path = summary_cache_dir() / f"{doc_id}.json"
    if not path.is_file():
        _doc_cache[doc_id] = {}
        return _doc_cache[doc_id]
    data = json.loads(path.read_text(encoding="utf-8"))
    sections = data.get("sections") if isinstance(data, dict) else None
    _doc_cache[doc_id] = sections if isinstance(sections, dict) else {}
    return _doc_cache[doc_id]


def get_summary(section_id: str) -> Optional[str]:
    """Return non-LLM covers/leaf summary for section_id, or None if missing."""
    sid = str(section_id or "").strip()
    if not sid or ":" not in sid:
        return None
    doc_id = sid.split(":", 1)[0]
    row = _load_doc(doc_id).get(sid)
    if not isinstance(row, dict):
        return None
    text = str(row.get("summary") or "").strip()
    return text or None


def clear_cache() -> None:
    _doc_cache.clear()
