from __future__ import annotations

import os
from typing import List, Optional

from nav_types import ActionKind, LegalAction, NavConfig, NavState, Projection


def _env_enabled(name: str, default: str = "1") -> bool:
    return os.environ.get(name, default).strip().lower() not in {"0", "false", "no", "off"}


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
    collected_sids = set(state.collected_section_ids) | {
        str(h.get("section_id") or "").strip()
        for h in state.action_history
        if h.get("kind") == "collect" and int(h.get("n_added", 0) or 0) > 0
    }
    covered_sids = set(state.covered_section_ids)
    blocked_collect_sids = set(state.blocked_collect_section_ids)
    visible_all = list(projection.visible_sections)
    visible_ids = {view.section_id for view in visible_all}
    visible_candidates = visible_all[: max(collect_limit, expand_limit)]
    filter_collected = _env_enabled("NAV_FILTER_COLLECTED_SECTIONS")
    # Keep C*/E* tied to projection order (N1 parity). Hybrid discovery only adds D* paths.
    for view in visible_candidates:
        adjusted_score = float(view.score)
        collect_blocked = filter_collected and view.section_id in (
            collected_sids | covered_sids | blocked_collect_sids
        )
        expand_blocked = filter_collected and view.section_id in covered_sids
        if collect_i <= collect_limit and not collect_blocked:
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
        if (
            view.has_children
            and view.section_id != state.current_scope
            and expand_i <= expand_limit
            and not expand_blocked
        ):
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

    # Discovery bridge exposes a relevant parent as a navigation path. It does
    # not add evidence; the agent must still expand and choose what to collect.
    if (
        _env_enabled("NAV_DISCOVERY_SCOPE_BRIDGE", "0")
        and (state.task_type or "").strip().lower()
        in {"scope_collection", "regulatory_coverage"}
        and mode != "critical"
    ):
        bridge_limit = max(
            1, int(os.environ.get("NAV_DISCOVERY_SCOPE_BRIDGE_K", "3").strip() or "3")
        )
        bridge_i = 1
        existing_expands = {
            action.section_id for action in actions if action.kind == ActionKind.EXPAND
        }
        for bridge in state.discovery_bridge_sections:
            if bridge_i > bridge_limit:
                break
            section_id = str(bridge.get("section_id") or "").strip()
            if (
                not section_id
                or section_id == state.current_scope
                or section_id in existing_expands
                or (filter_collected and section_id in covered_sids)
            ):
                continue
            score = float(bridge.get("discovery_score", 0.0) or 0.0)
            label = str(bridge.get("label") or section_id)[:80]
            add(
                ActionKind.EXPAND,
                "G",
                bridge_i,
                section_id=section_id,
                label=f"Discovery bridge: {label}",
                score=score,
                metadata={
                    "discovery_score": score,
                    "source": "discovery_scope_bridge",
                    "source_section_id": bridge.get("source_section_id"),
                },
            )
            existing_expands.add(section_id)
            bridge_i += 1

    # Hybrid discovery: expose LLM-reranked D* COLLECT actions only (no auto-inject).
    d_i = 1
    d_limit = max(1, int(os.environ.get("NAV_DISCOVERY_PICK_K", "5").strip() or "5"))
    for section_id, score in sorted(discovery_scores.items(), key=lambda item: (-item[1], item[0])):
        if d_i > d_limit:
            break
        if section_id in visible_ids or (
            filter_collected
            and section_id in (collected_sids | covered_sids | blocked_collect_sids)
        ):
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

    search_exhausted = (
        _env_enabled("NAV_BLOCK_EXHAUSTED_SEARCH")
        and state.current_scope in state.exhausted_search_scopes
    )
    if mode != "critical" and not search_exhausted:
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
