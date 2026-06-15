from __future__ import annotations

import re
from typing import Iterable, List, Optional


_LINE_RE = re.compile(r"^(?P<doc>.+):L(?P<line>\d+)(?P<suffix>.*)$")


def normalize_section_id(section_id: Optional[str]) -> Optional[str]:
    if not section_id:
        return None
    s = str(section_id).strip()
    if not s:
        return None
    for suffix in ("__path", "__intro", "__partial"):
        if s.endswith(suffix):
            s = s[: -len(suffix)]
    return s


def line_number(section_id: Optional[str]) -> Optional[int]:
    s = normalize_section_id(section_id)
    if not s:
        return None
    m = _LINE_RE.match(s)
    if not m:
        return None
    try:
        return int(m.group("line"))
    except Exception:
        return None


def doc_id_for(section_id: Optional[str]) -> Optional[str]:
    s = normalize_section_id(section_id)
    if not s:
        return None
    m = _LINE_RE.match(s)
    return m.group("doc") if m else None


def is_same_or_descendant(child: Optional[str], ancestor: Optional[str], all_descendants: Iterable[str]) -> bool:
    c = normalize_section_id(child)
    a = normalize_section_id(ancestor)
    if not c or not a:
        return False
    if c == a:
        return True
    return c in {normalize_section_id(x) for x in all_descendants}


def dedupe_preserve_order(values: Iterable[str]) -> List[str]:
    seen: set[str] = set()
    out: List[str] = []
    for v in values:
        n = normalize_section_id(v)
        if not n or n in seen:
            continue
        seen.add(n)
        out.append(n)
    return out

