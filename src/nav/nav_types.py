from __future__ import annotations

import os
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple


class ActionKind(str, Enum):
    COLLECT = "collect"
    DISPATCH = "dispatch"
    FINISH = "finish"


def map_mode_enabled(config: "NavConfig | None" = None) -> bool:
    """True when map-first observation/actions are active."""
    if config is not None and bool(getattr(config, "map_mode", False)):
        return True
    return os.environ.get("NAV_MAP_MODE", "0").strip().lower() not in {
        "0",
        "false",
        "no",
        "off",
        "",
    }


@dataclass
class NavConfig:
    projection_depth: int = 2
    projection_child_limit: int = 8
    projection_char_limit: int = 8000
    summary_chars: int = 120
    max_steps: int = 8
    collect_k: int = 64
    search_k: int = 40
    collect_top_k: int = 6  # rescue-K for highlights (not action quota)
    read_score_bonus: float = 10.0
    policy: str = "rule"
    llm_model_env: str = "NAV_LLM_MODEL"
    llm_temperature: float = 0.0
    llm_max_tokens: int = 256
    critical_remaining_steps: int = 1
    tight_remaining_steps: int = 2
    # Map-first mode (also gated by NAV_MAP_MODE env).
    map_mode: bool = False
    map_char_limit: int = 5000  # display budget (fold threshold); only hard display limit
    map_children_limit: int = 10000
    # Recursive dispatch.
    enable_recursive_dispatch: bool = True
    max_dispatch_depth: int = 3
    navigate_max_steps: int = 8
    dispatch_group_size: int = 5
    dispatch_max_workers: int = 4
    subagent_model_env: str = "NAV_SUBAGENT_MODEL"
    # Scoped maps whose estimated (with-summary) size exceeds this threshold drop
    # inline summaries (title-only), nudging the agent to DISPATCH deeper rather
    # than broadly COLLECT the whole parent. Default 1500 == evidence budget 500 x3.
    # run_nav_episode re-derives it from the episode's evidence budget x mult below.
    scope_inline_summary_char_limit: int = 1500
    scope_inline_summary_budget_mult: float = 3.0
    # COMPOSE child score = own_unit + compose_confidence_weight * collect_confidence
    # (see nav_compose._child_final_score); drives greedy budget-fill order.
    compose_confidence_weight: float = 0.5
    # Depth-0 external relative rerank of parent groups (compose preview + group_rank).
    enable_external_rerank: bool = True
    compose_preview_snippet_chars: int = 60
    # 0 = show every child in the preview (no per-group child cap).
    compose_preview_max_children: int = 0
    # Evidence packing: "greedy" (legacy fill) | "waterfill" (tiered full+snippet coverage).
    compose_packing_mode: str = "waterfill"
    # Waterfill: fraction of budget reserved for cross-group snippet breadth (Tier2).
    compose_coverage_budget_frac: float = 0.4
    # Waterfill: max chars per snippet line when breadth-filling.
    compose_snippet_chars: int = 80
    # Depth-0 hard rewrite: after agent chooses COLLECT, if branch text length
    # exceeds the limit and the node has children, rewrite that sid to DISPATCH.
    enable_depth0_oversize_to_dispatch: bool = False
    # 0 = use episode evidence budget_chars (set in run_nav_episode).
    depth0_oversize_char_limit: int = 0
    # M2 query planning (structure-conditioned). Off by default → zero regression.
    enable_query_planning: bool = False
    # Display budget for the one-shot planning map; executor still uses map_char_limit.
    # 0 = reuse map_char_limit.
    planning_map_char_limit: int = 10000
    # Soft prompt guidance only when > 0; never silently truncates a valid plan.
    planner_max_subgoals: int = 0
    planner_model_env: str = "NAV_PLANNER_MODEL"
    # Separate from navigate llm_max_tokens: plan JSON is larger.
    planner_llm_max_tokens: int = 1024
    # M3: after planning, re-score the map per bindable subgoal retrieval_query.
    enable_per_subgoal_illumination: bool = False
    # M3: fold merge uses budget_share weights + satisfied decay (else equal max).
    enable_goal_conditioned_folding: bool = False
    # M4: replace single navigate with dependency-wave plan execution.
    enable_plan_orchestration: bool = False
    # M5: contract verify + slot extract + activation + limited replan.
    enable_contract_verify: bool = False
    # M5: navigate+verify cycles per subgoal (RETRY/WIDEN/REBIND). Min 1.
    subgoal_max_attempts: int = 2
    # M5: 0 = never replan; otherwise hard cap on structural replans.
    max_replans: int = 0
    # M4: 0 = no extra wave cap (stop when no ready subgoals).
    max_waves: int = 0
    # M6: settle evidence with per-subgoal floors + leftover recirculation.
    enable_subgoal_budget_ledger: bool = False
    # Fraction of episode budget reserved as floors by budget_share (rest starts in Tier-2 pool).
    subgoal_budget_floor_frac: float = 1.0
    # --- PLAN×NAV fusion (2026-08): anchor entry + one-shot harvest + plan_control ---
    # Enter a subgoal's harvest at its resolved route_hints anchor instead of the
    # document/corpus root. Per-subgoal fallback to root when no anchor resolves.
    enable_anchor_entry: bool = False
    # Replace the multi-step ReAct navigate() with a single collect/dispatch
    # decision per node; recursion only follows explicit DISPATCH selections.
    enable_one_shot_harvest: bool = False
    # Structural recursion depth cap for harvest() (mirrors max_dispatch_depth's
    # existing default; harvest recursion is bounded independently of navigate()).
    max_harvest_depth: int = 3
    # Replace per-subgoal verdict auto-escalation (RETRY/WIDEN/REBIND -> REPLAN)
    # with one LLM call per wave that reviews every subgoal's own new evidence.
    enable_plan_control: bool = False
    # Per-subgoal evidence digest cap shown to plan_control (not the full pool;
    # kept small since plan_control runs once per wave over every subgoal).
    plan_control_digest_chars: int = 600
    # Render collected branches as "[harvested:sN]" instead of removing them from
    # the map/action space, so later subgoals and plan_control still see coverage.
    show_harvested_in_map: bool = False
    # Compute group_priority once at settle time instead of once per per-subgoal
    # navigate() call (which otherwise lets the last subgoal's rank win globally).
    enable_settle_group_rank: bool = False

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "NavConfig":
        flat = dict(data)
        budget_modes = flat.pop("budget_modes", {}) or {}
        if isinstance(budget_modes, dict):
            flat["critical_remaining_steps"] = int(
                budget_modes.get("critical_remaining_steps", cls.critical_remaining_steps)
            )
            flat["tight_remaining_steps"] = int(
                budget_modes.get("tight_remaining_steps", cls.tight_remaining_steps)
            )
        # Drop deprecated keys quietly (legacy map_peek/jump/expand/peek_content).
        for dead in (
            "expand_top_k",
            "map_peek_top_k",
            "map_jump_top_k",
            "peek_content_fanout",
            "peek_content_chars",
            "map_collapse_min_score",
        ):
            flat.pop(dead, None)
        allowed = {f.name for f in cls.__dataclass_fields__.values()}
        cfg = cls(**{k: v for k, v in flat.items() if k in allowed})
        if map_mode_enabled(None) and not cfg.map_mode:
            cfg.map_mode = True
        if cfg.map_mode and cfg.llm_max_tokens < 256:
            cfg.llm_max_tokens = 256
        return cfg


@dataclass
class SectionView:
    section_id: str
    level: int
    preview: str
    score: float = 0.0
    n_lines: int = 0
    n_chunks: int = 0
    has_children: bool = False
    depth_from_scope: int = 0
    map_id: str = ""
    title: str = ""
    n_descendants: int = 0
    is_highlight: bool = False
    parent_id: Optional[str] = None
    summary: str = ""
    # M3: which subgoal illuminations marked this node a Hit (for [Hit:s1,s3]).
    hit_sources: List[str] = field(default_factory=list)
    # PLAN×NAV fusion: subgoal id that collected this node's branch, when the
    # node stays visible (collapsed, no descendant expansion) instead of being
    # deleted from the map — for [harvested:sN].
    harvested_by: str = ""


@dataclass
class Projection:
    doc_id: str
    scope: Optional[str]
    text: str
    visible_sections: List[SectionView]
    truncated: bool = False  # True if any budget-hidden nodes
    id_to_section: Dict[str, str] = field(default_factory=dict)
    map_mode: bool = False
    tree_sections: List[SectionView] = field(default_factory=list)
    highlight_ids: List[str] = field(default_factory=list)


@dataclass
class LegalAction:
    action_id: str
    kind: ActionKind
    section_id: Optional[str] = None
    query: str = ""
    label: str = ""
    score: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)

    def prompt_line(self) -> str:
        target = self.section_id or ""
        bits = [self.action_id, self.kind.value.upper()]
        if target:
            bits.append(target)
        if self.label:
            bits.append(self.label)
        if self.score:
            bits.append(f"score={self.score:.4f}")
        return " | ".join(bits)


@dataclass
class RegionReport:
    """Result of one navigate(scope, ...) call (top-level or dispatched subagent)."""

    scope: Optional[str]
    collected_section_ids: List[str] = field(default_factory=list)
    suggestions: List[str] = field(default_factory=list)
    summary: str = ""
    reason: str = ""
    skipped: bool = False
    depth: int = 0


@dataclass
class SubgoalResult:
    """Typed outcome of one subgoal execution (M5)."""

    subgoal_id: str
    satisfied: bool
    confidence: float = 0.0
    collected_section_ids: List[str] = field(default_factory=list)
    extracted: Dict[str, str] = field(default_factory=dict)
    gap: str = ""
    chars_used: int = 0
    verdict: str = ""  # SATISFIED|RETRY_SAME_REGION|WIDEN|REBIND|REPLAN


@dataclass
class NavState:
    doc_id: str
    query: str
    task_type: str = "unknown"
    # Working scope for the *current* navigate call (set by navigate(), not a stack).
    current_scope: Optional[str] = None
    collected_ids: set[str] = field(default_factory=set)
    collected: List[Tuple[Any, float]] = field(default_factory=list)
    map_scores: Dict[str, float] = field(default_factory=dict)
    unit_scores: Dict[str, float] = field(default_factory=dict)
    highlight_ids: List[str] = field(default_factory=list)
    # "Branch done / removed from map" = COLLECT'd sid ∪ all descendants.
    collected_section_ids: set[str] = field(default_factory=set)
    blocked_collect_section_ids: set[str] = field(default_factory=set)
    action_history: List[Dict[str, Any]] = field(default_factory=list)
    refusal_events: List[Dict[str, Any]] = field(default_factory=list)
    # Subagent / investigate reports shown to the parent agent.
    reports_context: str = ""
    investigated_section_ids: set[str] = field(default_factory=set)
    dismissed_section_ids: set[str] = field(default_factory=set)
    # Explicit COLLECT confidence by section_id; hydration-only descendants stay 0.
    collect_confidence: Dict[str, float] = field(default_factory=dict)
    # Explicit COLLECT targets only (batch action sids); hydration descendants omitted.
    # Drives COMPOSE selection_count (owner hit + any-ancestor hit → 0/1/2).
    explicit_collect_ids: set[str] = field(default_factory=set)
    # External agent relative priority over nearest-parent groups: parent_id -> score
    # (higher packs first). Empty = no external rerank yet.
    group_priority: Dict[str, float] = field(default_factory=dict)
    # M2: structured retrieval plan + slot bindings for delayed query fill.
    retrieval_plan: Optional[Any] = None
    slot_bindings: Dict[str, str] = field(default_factory=dict)
    # M3: per-subgoal illumination caches + fold provenance.
    subgoal_map_scores: Dict[str, Dict[str, float]] = field(default_factory=dict)
    subgoal_unit_scores: Dict[str, Dict[str, float]] = field(default_factory=dict)
    hit_sources: Dict[str, List[str]] = field(default_factory=dict)
    active_subgoal_ids: List[str] = field(default_factory=list)
    satisfied_subgoal_ids: set[str] = field(default_factory=set)
    # Finished trying (success or attempts exhausted). Deps wait on satisfied only.
    attempted_subgoal_ids: set[str] = field(default_factory=set)
    activated_subgoal_ids: set[str] = field(default_factory=set)
    # M4/M5: soft focus for policy (never clips action space).
    focus_subgoal_id: str = ""
    focus_subgoal_need: str = ""
    focus_subgoal_contract: str = ""
    focus_retrieval_query: str = ""
    focus_contract_kind: str = ""
    # Soft scope preference for the active subgoal (doc_ids only; not action clip).
    focus_scope_doc_ids: List[str] = field(default_factory=list)
    subgoal_results: Dict[str, Any] = field(default_factory=dict)
    replan_count: int = 0
    # PLAN×NAV fusion: explicit collect-root section_id -> owning subgoal_id
    # (drives "[harvested:sN]" map tags when show_harvested_in_map is on).
    harvested_owner_subgoal: Dict[str, str] = field(default_factory=dict)
    # Per-subgoal sticky harvest entry point: None == document root (maximum
    # breadth already). Set once by resolve_harvest_anchor's first
    # resolution, moved only by plan_control's "widen" decision (one level up
    # to the parent scope each time) — see nav_orchestrate._apply_plan_control.
    subgoal_anchor: Dict[str, Optional[str]] = field(default_factory=dict)
    # Per-subgoal "seen but not selected" section ids (visible collect/dispatch
    # candidates a harvest call chose neither of, plus dispatched branches that
    # yielded nothing) — hidden from that subgoal's later map views so widen
    # surfaces siblings instead of re-offering the same dead ends. Scoped per
    # subgoal, not merged into the global dismissed_section_ids below.
    subgoal_dismissed_section_ids: Dict[str, set[str]] = field(default_factory=dict)
    # Per-subgoal wave-attempt counter (circuit breaker under plan_control).
    subgoal_attempt_counts: Dict[str, int] = field(default_factory=dict)
    # Terminal "drop" outcomes: disjoint from satisfied_subgoal_ids. Union of
    # the two is "settled" — the only thing ready_subgoal_ids' dependency gate
    # requires from a precursor (F1: a dropped precursor must not starve deps).
    dropped_subgoal_ids: set[str] = field(default_factory=set)
