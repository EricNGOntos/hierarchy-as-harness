from __future__ import annotations

from typing import List, Optional

from nav_projection import top_visible_sections
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
    for view in top_visible_sections(projection, limit=max(collect_limit, expand_limit)):
        if view.section_id not in state.collected_ids and collect_i <= collect_limit:
            add(
                ActionKind.COLLECT,
                "C",
                collect_i,
                section_id=view.section_id,
                label=view.preview[:80],
                score=view.score,
                metadata={"n_chunks": view.n_chunks, "n_lines": view.n_lines},
            )
            collect_i += 1
        if view.has_children and expand_i <= expand_limit:
            add(
                ActionKind.EXPAND,
                "E",
                expand_i,
                section_id=view.section_id,
                label=view.preview[:80],
                score=view.score,
                metadata={"n_chunks": view.n_chunks, "n_lines": view.n_lines},
            )
            expand_i += 1

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

