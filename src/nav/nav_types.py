from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple


class ActionKind(str, Enum):
    EXPAND = "expand"
    COLLECT = "collect"
    BACK = "back"
    SEARCH = "search"
    FINISH = "finish"


@dataclass
class NavConfig:
    projection_depth: int = 2
    projection_child_limit: int = 8
    projection_char_limit: int = 8000
    summary_chars: int = 120
    max_steps: int = 8
    collect_k: int = 64
    search_k: int = 40
    expand_top_k: int = 6
    collect_top_k: int = 6
    read_score_bonus: float = 10.0
    policy: str = "rule"
    llm_model_env: str = "NAV_LLM_MODEL"
    llm_temperature: float = 0.0
    llm_max_tokens: int = 128
    critical_remaining_steps: int = 1
    tight_remaining_steps: int = 2

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
        allowed = {f.name for f in cls.__dataclass_fields__.values()}
        return cls(**{k: v for k, v in flat.items() if k in allowed})


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


@dataclass
class Projection:
    doc_id: str
    scope: Optional[str]
    text: str
    visible_sections: List[SectionView]
    truncated: bool = False


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
class NavState:
    doc_id: str
    query: str
    task_type: str = "unknown"
    current_scope: Optional[str] = None
    scope_stack: List[Optional[str]] = field(default_factory=lambda: [None])
    collected_ids: set[str] = field(default_factory=set)
    collected: List[Tuple[Any, float]] = field(default_factory=list)
    action_history: List[Dict[str, Any]] = field(default_factory=list)
    refusal_events: List[Dict[str, Any]] = field(default_factory=list)

    def push_scope(self, section_id: Optional[str]) -> None:
        self.current_scope = section_id
        self.scope_stack.append(section_id)

    def back(self) -> Optional[str]:
        if len(self.scope_stack) > 1:
            self.scope_stack.pop()
        self.current_scope = self.scope_stack[-1] if self.scope_stack else None
        return self.current_scope

