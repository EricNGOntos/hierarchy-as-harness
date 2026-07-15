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
    # Recursive dispatch (default off for experiments: only depth-0 may DISPATCH).
    enable_recursive_dispatch: bool = False
    max_dispatch_depth: int = 3
    navigate_max_steps: int = 8
    dispatch_group_size: int = 5
    dispatch_max_workers: int = 4
    subagent_model_env: str = "NAV_SUBAGENT_MODEL"
    # COMPOSE: child_score = own_unit + compose_confidence_weight * collect_confidence
    compose_confidence_weight: float = 0.5
    # Depth-0 external relative rerank of parent groups (compose preview + group_rank).
    enable_external_rerank: bool = True
    compose_preview_snippet_chars: int = 60
    # 0 = show every child in the preview (no per-group child cap).
    compose_preview_max_children: int = 0

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
    scope_evidence_locked: bool = False
    action_history: List[Dict[str, Any]] = field(default_factory=list)
    refusal_events: List[Dict[str, Any]] = field(default_factory=list)
    # Subagent / investigate reports shown to the parent agent.
    reports_context: str = ""
    investigated_section_ids: set[str] = field(default_factory=set)
    dismissed_section_ids: set[str] = field(default_factory=set)
    # Explicit COLLECT confidence by section_id; hydration-only descendants stay 0.
    collect_confidence: Dict[str, float] = field(default_factory=dict)
    # External agent relative priority over nearest-parent groups: parent_id -> score
    # (higher packs first). Empty = no external rerank yet.
    group_priority: Dict[str, float] = field(default_factory=dict)
