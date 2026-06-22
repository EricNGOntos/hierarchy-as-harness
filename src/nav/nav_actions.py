from __future__ import annotations

import os
from typing import List, Optional

from nav_types import ActionKind, LegalAction, NavConfig, NavState, Projection


def _budget_mode(step_idx: int, config: NavConfig) -> str:
    remaining = max(0, config.max_steps - step_idx)
    if remaining <= config.critical_remaining_steps:
        return "critical"
    if remaining <= config.tight_remaining_steps:
        return "tight"
    return "normal"


def build_legal_actions(
    state: NavState,
    projection: Projection,
    *,
    step_idx: int,
    config: NavConfig,
) -> List[LegalAction]:
    mode = _budget_mode(step_idx, config)
    actions: List[LegalAction] = []

    def add(kind: ActionKind, prefix: str, n: int, **kwargs) -> None:
        actions.append(LegalAction(action_id=f"{prefix}{n}", kind=kind, **kwargs))

    collect_limit = config.collect_top_k
    expand_limit = config.expand_top_k
    if mode == "tight":
        expand_limit = min(expand_limit, 3)
    if mode == "critical":
        expand_limit = 0

    collect_i = 1
    expand_i = 1
    discovery_scores = dict(getattr(state, "discovery_scores", {}) or {})
    label_by_id = {
        str(c.get("section_id") or ""): str(c.get("label") or "")[:100]
        for c in (getattr(state, "hybrid_section_candidates", None) or [])
    }
    collected_sids = {
        str(h.get("section_id") or "").strip()
        for h in state.action_history
        if h.get("kind") == "collect" and int(h.get("n_added", 0) or 0) > 0
    }
    visible_all = list(projection.visible_sections)
    visible_ids = {view.section_id for view in visible_all}
    # Keep C*/E* tied to projection order (N1 parity). Hybrid discovery only adds D* paths.
    for view in visible_all[: max(collect_limit, expand_limit)]:
        adjusted_score = float(view.score)
        if collect_i <= collect_limit:
            add(
                ActionKind.COLLECT,
                "C",
                collect_i,
                section_id=view.section_id,
                label=view.preview[:80],
                score=adjusted_score,
                metadata={
                    "n_chunks": view.n_chunks,
                    "n_lines": view.n_lines,
                    "base_score": view.score,
                    "discovery_score": float(discovery_scores.get(view.section_id, 0.0)),
                },
            )
            collect_i += 1
        if view.has_children and view.section_id != state.current_scope and expand_i <= expand_limit:
            add(
                ActionKind.EXPAND,
                "E",
                expand_i,
                section_id=view.section_id,
                label=view.preview[:80],
                score=adjusted_score,
                metadata={
                    "n_chunks": view.n_chunks,
                    "n_lines": view.n_lines,
                    "base_score": view.score,
                    "discovery_score": float(discovery_scores.get(view.section_id, 0.0)),
                },
            )
            expand_i += 1

    # Hybrid discovery: expose LLM-reranked D* COLLECT actions only (no auto-inject).
    d_i = 1
    d_limit = max(1, int(os.environ.get("NAV_DISCOVERY_PICK_K", "5").strip() or "5"))
    for section_id, score in sorted(discovery_scores.items(), key=lambda item: (-item[1], item[0])):
        if d_i > d_limit:
            break
        if section_id in visible_ids or section_id in collected_sids:
            continue
        if any(a.section_id == section_id for a in actions if a.kind == ActionKind.COLLECT):
            continue
        label = label_by_id.get(section_id) or "discovery section"
        add(
            ActionKind.COLLECT,
            "D",
            d_i,
            section_id=section_id,
            label=f"Discovery collect: {label} (score={float(score):.2f})",
            score=float(score),
            metadata={"discovery_score": float(score), "source": "knowhere_hybrid_rerank"},
        )
        d_i += 1

    if mode != "critical":
        actions.append(
            LegalAction(
                action_id="S1",
                kind=ActionKind.SEARCH,
                query=state.query,
                label="global leaf/path search in current document",
                score=0.0,
            )
        )

    if state.current_scope is not None:
        actions.append(
            LegalAction(
                action_id="B1",
                kind=ActionKind.BACK,
                section_id=state.scope_stack[-2] if len(state.scope_stack) >= 2 else None,
                label="return to parent scope",
            )
        )

    actions.append(
        LegalAction(
            action_id="F1",
            kind=ActionKind.FINISH,
            label="finish navigation and pack final evidence budget",
        )
    )
    return actions


def action_by_id(actions: List[LegalAction], action_id: Optional[str]) -> Optional[LegalAction]:
    aid = (action_id or "").strip().upper()
    if not aid:
        return None
    for a in actions:
        if a.action_id.upper() == aid:
            return a
    return None
