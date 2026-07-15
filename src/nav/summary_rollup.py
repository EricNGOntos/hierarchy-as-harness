"""Non-LLM section summary rollup (KNOWHERE-aligned covers path).

Assembly for non-leaves:
  ``This section covers:`` + self_only (if any) + all direct child titles
then head…tail the whole string.

Leaves keep a clipped self-text summary. No LLM.
"""

from __future__ import annotations

from typing import Dict, List, Mapping, Sequence, Tuple

SECTION_COVERS_PREFIX = "This section covers: "
HEAD = 100
TAIL = 100


def normalize_ws(text: str) -> str:
    return " ".join((text or "").split())


def clip_head_tail(text: str, head: int = HEAD, tail: int = TAIL) -> Tuple[str, bool]:
    flat = normalize_ws(text)
    if len(flat) <= head + tail:
        return flat, False
    return flat[:head] + "..." + flat[-tail:], True


def node_title(self_text: str, *, max_chars: int = 80) -> str:
    flat = normalize_ws(self_text)
    if len(flat) <= max_chars:
        return flat
    return flat[:max_chars]


def deterministic_covers_summary(
    *,
    self_only: str,
    child_titles: Sequence[str],
    head: int = HEAD,
    tail: int = TAIL,
) -> Tuple[str, bool]:
    """covers prefix → self_only → child titles; head…tail on the whole string."""
    segments: List[str] = []
    self_text = normalize_ws(self_only)
    if self_text:
        segments.append(self_text)
    titles = [normalize_ws(t) for t in child_titles if normalize_ws(t)]
    if titles:
        segments.append(", ".join(titles))
    assembled = (
        SECTION_COVERS_PREFIX + " ".join(segments)
        if segments
        else SECTION_COVERS_PREFIX.rstrip()
    )
    return clip_head_tail(assembled, head=head, tail=tail)


def build_children_map(
    levels: Mapping[int, int],
    order: Sequence[int],
) -> Dict[int, List[int]]:
    children: Dict[int, List[int]] = {lid: [] for lid in order}
    stack: List[int] = []
    for lid in order:
        lv = int(levels[lid])
        while stack and int(levels[stack[-1]]) >= lv:
            stack.pop()
        if stack:
            children[stack[-1]].append(lid)
        stack.append(lid)
    return children


def count_descendants(children: Mapping[int, Sequence[int]], lid: int) -> int:
    total = 0
    for ch in children[lid]:
        total += 1 + count_descendants(children, ch)
    return total


def rollup_doc_summaries(
    *,
    order: Sequence[int],
    levels: Mapping[int, int],
    line_text: Mapping[int, str],
    head: int = HEAD,
    tail: int = TAIL,
) -> Dict[int, Dict[str, object]]:
    """Bottom-up non-LLM summaries keyed by line_id."""
    children = build_children_map(levels, order)
    out: Dict[int, Dict[str, object]] = {}

    def _rollup(lid: int) -> str:
        kids = list(children.get(lid) or [])
        self_text = line_text.get(lid, "") or ""
        self_flat = normalize_ws(self_text)
        title = node_title(self_text)
        self_sum, self_trunc = clip_head_tail(self_flat, head=head, tail=tail)

        if not kids:
            summary, truncated = self_sum, self_trunc
            rollup_mode = "leaf"
            has_self_only = bool(self_flat)
        else:
            for ch in kids:
                _rollup(ch)
            child_titles = [
                str(out[ch]["title"] or "").strip()
                for ch in kids
                if str(out[ch].get("title") or "").strip()
            ]
            # Non-leaf self_only = this node's own line (heading / interstitial).
            summary, truncated = deterministic_covers_summary(
                self_only=self_flat,
                child_titles=child_titles,
                head=head,
                tail=tail,
            )
            rollup_mode = "title_enum"
            has_self_only = bool(self_flat)

        out[lid] = {
            "line_id": lid,
            "level": int(levels[lid]),
            "title": title,
            "self_chars": len(self_flat),
            "n_descendants": count_descendants(children, lid),
            "summary": summary,
            "summary_truncated": truncated,
            "self_summary": self_sum,
            "self_summary_truncated": self_trunc,
            "rollup_mode": rollup_mode,
            "has_self_only": has_self_only,
            "n_direct_children": len(kids),
        }
        return str(summary)

    child_set = {ch for kids in children.values() for ch in kids}
    for lid in order:
        if lid not in child_set:
            _rollup(lid)
    for lid in order:
        if lid not in out:
            _rollup(lid)
    return out
