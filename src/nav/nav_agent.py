from __future__ import annotations

import time
import os
import re
from typing import Any, Dict, List, Optional, Tuple

from agent_delivery.agent.types import AgentStep, EpisodeResult
from agent_delivery.code.budget_eval import evaluate_at_budget
from agent_delivery.code.compose_llm import compose_answer_llm
from agent_delivery.code.hierarchical_tools import HierarchicalTools
from agent_delivery.code.index_retrieval import Chunk
from agent_delivery.code.tool_space import Refusal, ToolSpace

from nav_actions import build_legal_actions
from nav_discovery import apply_soft_safety_collect, compute_discovery_scores
from nav_policy import choose_llm_action
from nav_projection import build_projection
from nav_types import ActionKind, LegalAction, NavConfig, NavState


def _chunks_to_retrieved_nodes(chunks: List[Chunk]) -> List[str]:
    seen: set[str] = set()
    out: List[str] = []
    for c in chunks:
        for lid in c.line_ids:
            node = f"{c.doc_id}:L{lid}"
            if node not in seen:
                seen.add(node)
                out.append(node)
    return out


def _dedupe_scored(scored: List[Tuple[Chunk, float]]) -> List[Tuple[Chunk, float]]:
    best: Dict[str, Tuple[Chunk, float]] = {}
    for c, score in scored:
        prev = best.get(c.node_id)
        if prev is None or float(score) > float(prev[1]):
            best[c.node_id] = (c, float(score))
    out = list(best.values())
    out.sort(key=lambda x: -x[1])
    return out


def _query_tokens_for_compose(query: str) -> List[str]:
    raw = (query or "").lower()
    toks = re.findall(r"[a-z0-9_]+|[\u4e00-\u9fff]", raw)
    return [t for t in toks if t.strip()]


def _prepare_compose_evidence_text(
    query: str,
    evidence_text: str,
    *,
    budget_chars: int,
    task_type: str,
) -> str:
    text = (evidence_text or "").strip()
    if not text:
        return ""
    if os.environ.get("NAV_COMPOSE_CLEAN_EVIDENCE", "1").strip().lower() in {"0", "false", "no"}:
        return text[: max(1, int(budget_chars))]

    tt = (task_type or "").strip().lower()
    keep_path = tt == "multi_hop"
    blocks: List[Tuple[str, str]] = []
    for raw_block in re.split(r"\n\s*\n(?=\[)", text):
        chunk = raw_block.strip()
        if not chunk:
            continue
        lines = chunk.splitlines()
        if not lines:
            continue
        header = lines[0].strip()
        body_lines = list(lines[1:]) if keep_path else [ln for ln in lines[1:] if not ln.strip().startswith("PATH:")]
        body = "\n".join(body_lines).strip()
        if not body:
            continue
        blocks.append((header, body))
    if not blocks:
        cleaned = re.sub(r"(?m)^PATH:.*\n?", "", text).strip()
        return (cleaned or text)[: max(1, int(budget_chars))]

    should_rerank = tt in {"scope_collection", "regulatory_coverage"}
    if should_rerank:
        toks = _query_tokens_for_compose(query)

        def _score_block(block: Tuple[str, str]) -> Tuple[int, int]:
            body = block[1].lower()
            overlap = sum(1 for t in toks if t in body)
            return (overlap, len(body))

        blocks.sort(key=_score_block, reverse=True)

    deduped: List[Tuple[str, str]] = []
    seen_body: set[str] = set()
    for h, b in blocks:
        b_norm = re.sub(r"\s+", " ", b).strip()
        if not b_norm or b_norm in seen_body:
            continue
        seen_body.add(b_norm)
        deduped.append((h, b))

    out_parts: List[str] = []
    used = 0
    for h, b in deduped:
        piece = f"{h}\n{b}"
        add_len = len(piece) + (2 if out_parts else 0)
        if used + add_len <= int(budget_chars):
            out_parts.append(piece)
            used += add_len
            continue
        remain = int(budget_chars) - used - (2 if out_parts else 0)
        if remain > 40:
            out_parts.append(piece[:remain])
        break
    if out_parts:
        return "\n\n".join(out_parts)
    return text[: max(1, int(budget_chars))]


def _add_scored(state: NavState, scored: List[Tuple[Chunk, float]]) -> int:
    added = 0
    for c, score in scored:
        if c.node_id in state.collected_ids:
            continue
        state.collected_ids.add(c.node_id)
        state.collected.append((c, float(score)))
        added += 1
    return added


def _collect_subtree(ts: ToolSpace, action: LegalAction, state: NavState, config: NavConfig) -> List[Tuple[Chunk, float]]:
    sid = action.section_id
    if not sid:
        return []
    materialize = getattr(ts, "_materialize_leaf_path_chunks", None)
    idx = getattr(ts, "_idx", None)
    if callable(materialize) and idx is not None:
        pool = list(materialize(sid, state.doc_id))
        if pool:
            task_type = (state.task_type or "").strip().lower()
            if task_type in {"scope_collection", "regulatory_coverage"}:
                ordered = sorted(pool, key=lambda c: (min(c.line_ids or (10**9,)), c.node_id))
                limit = min(len(ordered), int(config.collect_k))
                base = float(config.read_score_bonus) + float(action.score or 0.0)
                return [
                    (chunk, base + (limit - rank) * 0.001)
                    for rank, chunk in enumerate(ordered[:limit])
                ]
            scored = idx.search(state.query, pool, min(len(pool), int(config.collect_k)), doc_id_filter=state.doc_id)
            return [(c, float(s) + float(config.read_score_bonus)) for c, s in scored]
    rc = ts.read_chunks(sid, state.query, doc_id=state.doc_id, k=int(config.collect_k))
    if isinstance(rc, Refusal):
        state.refusal_events.append(
            {
                "tool": "collect",
                "section_id": sid,
                "status": rc.status,
                "message": rc.message,
                "available_sections": list(rc.available_sections),
            }
        )
        return []
    return [(h.chunk, float(h.score) + float(config.read_score_bonus)) for h in rc]


def _search_doc(ts: ToolSpace, state: NavState, config: NavConfig) -> List[Tuple[Chunk, float]]:
    hits = ts.search(state.query, int(config.search_k), doc_id=state.doc_id)
    return [(h.chunk, float(h.score)) for h in hits]


def run_nav_episode(
    tools: HierarchicalTools,
    query: str,
    *,
    doc_id: str,
    budget_chars: int,
    task_type: str = "unknown",
    compose_format_constraints: str = "",
    compose_answer: bool = True,
    policy: str = "rule",
    config: Optional[NavConfig] = None,
) -> EpisodeResult:
    if not doc_id:
        raise ValueError("Nav Agent requires a non-empty doc_id")
    from agent_delivery.code.llm_config import load_llm_env, require_llm_env  # type: ignore

    load_llm_env()
    require_llm_env(context="Nav Agent")
    cfg = config or NavConfig(policy="llm")
    nav_policy = (policy or cfg.policy or "llm").strip().lower()
    if nav_policy != "llm":
        raise ValueError(
            f"Nav Agent 仅支持 llm 策略（须配置 OPENAI_API_KEY）；收到 policy={policy!r}。"
            "请设置 --nav-policy llm 或删除 NAV_POLICY=rule。"
        )
    cfg.policy = "llm"
    retrieval_t0 = time.perf_counter()
    ts = ToolSpace(tools)
    state = NavState(doc_id=doc_id, query=query, task_type=task_type)
    steps: List[AgentStep] = []
    section_ids = ts.sections_for_doc(doc_id)

    for step_idx in range(1, max(1, int(cfg.max_steps)) + 1):
        state.discovery_scores = compute_discovery_scores(ts, state, cfg)
        projection = build_projection(
            ts,
            doc_id=doc_id,
            query=query,
            scope=state.current_scope,
            config=cfg,
        )
        actions = build_legal_actions(state, projection, step_idx=step_idx, config=cfg)
        chosen, llm_meta = choose_llm_action(state, projection, actions, step_idx=step_idx, config=cfg)

        detail: Dict[str, Any] = {
            "action_id": chosen.action_id,
            "kind": chosen.kind.value,
            "section_id": chosen.section_id,
            "scope": state.current_scope,
            "projection_chars": len(projection.text),
            "n_visible_sections": len(projection.visible_sections),
            "n_legal_actions": len(actions),
            "legal_actions": [a.prompt_line() for a in actions],
            "n_discovery_scores": len(state.discovery_scores),
        }
        if state.discovery_rerank_meta:
            detail["discovery_rerank"] = dict(state.discovery_rerank_meta)
        if llm_meta:
            detail["llm"] = llm_meta

        if chosen.kind == ActionKind.FINISH:
            steps.append(AgentStep(step_idx=len(steps) + 1, action="nav_finish", detail=detail))
            state.action_history.append({**detail, "step_idx": step_idx})
            break
        if chosen.kind == ActionKind.EXPAND:
            state.push_scope(chosen.section_id)
            steps.append(AgentStep(step_idx=len(steps) + 1, action="nav_expand", detail=detail))
            state.action_history.append({**detail, "step_idx": step_idx})
            continue
        if chosen.kind == ActionKind.BACK:
            new_scope = state.back()
            detail["new_scope"] = new_scope
            steps.append(AgentStep(step_idx=len(steps) + 1, action="nav_back", detail=detail))
            state.action_history.append({**detail, "step_idx": step_idx})
            continue
        if chosen.kind == ActionKind.SEARCH:
            scored = _search_doc(ts, state, cfg)
            added = _add_scored(state, scored)
            detail["n_hits"] = len(scored)
            detail["n_added"] = added
            steps.append(AgentStep(step_idx=len(steps) + 1, action="nav_search", detail=detail))
            state.action_history.append({**detail, "step_idx": step_idx})
            continue
        if chosen.kind == ActionKind.COLLECT:
            scored = _collect_subtree(ts, chosen, state, cfg)
            added = _add_scored(state, scored)
            detail["n_hits"] = len(scored)
            detail["n_added"] = added
            steps.append(AgentStep(step_idx=len(steps) + 1, action="nav_collect", detail=detail))
            state.action_history.append({**detail, "step_idx": step_idx})
            continue

    added_soft, soft_ids, soft_meta = apply_soft_safety_collect(
        ts,
        state,
        cfg,
        budget_chars=int(budget_chars),
        collect_subtree_fn=_collect_subtree,
        add_scored_fn=_add_scored,
        dedupe_fn=_dedupe_scored,
    )
    if soft_ids:
        steps.append(
            AgentStep(
                step_idx=len(steps) + 1,
                action="nav_soft_safety_collect",
                detail=soft_meta,
            )
        )

    scored_chunks = _dedupe_scored(list(state.collected))
    fill = evaluate_at_budget(scored_chunks, budget_chars=budget_chars)
    retrieval_seconds = time.perf_counter() - retrieval_t0
    composed = ""
    compose_seconds = 0.0
    if compose_answer:
        compose_t0 = time.perf_counter()
        max_ans = min(1024, max(256, int(budget_chars)))
        extra_mh_constraint = ""
        if (task_type or "").strip().lower() == "multi_hop":
            extra_mh_constraint = (
                "multi_hop 约束：fact_1 与 fact_2 必须分别覆盖两跳信息，"
                "final_answer 必须整合二者，任一缺失视为不完整。"
            )
        fc = compose_format_constraints
        if extra_mh_constraint:
            fc = (f"{fc}\n{extra_mh_constraint}" if fc else extra_mh_constraint)
        compose_evidence = _prepare_compose_evidence_text(
            query,
            fill.evidence_text or "",
            budget_chars=int(budget_chars),
            task_type=task_type or "niche_fact",
        )
        composed = compose_answer_llm(
            query,
            task_type=task_type or "niche_fact",
            evidence_text=compose_evidence,
            max_answer_chars=max_ans,
            budget_chars=int(budget_chars),
            format_constraints=fc,
        )
        compose_seconds = time.perf_counter() - compose_t0
        steps.append(
            AgentStep(
                step_idx=len(steps) + 1,
                action="compose_answer",
                detail={
                    "evidence_chars": fill.evidence_chars_actual,
                    "n_chunks_kept": fill.n_chunks_kept,
                    "truncated_last": fill.truncated_last,
                },
            )
        )

    return EpisodeResult(
        representation=f"hierarchical_nav_{cfg.policy}",
        steps=steps,
        scored_chunks=scored_chunks,
        kept_chunks=fill.kept_chunks,
        evidence_text=fill.evidence_text,
        evidence_chars_actual=fill.evidence_chars_actual,
        retrieved_nodes=_chunks_to_retrieved_nodes(list(fill.kept_chunks)),
        composed_answer=composed,
        section_ids=list(section_ids),
        trajectory_length=len(steps),
        truncated_last=fill.truncated_last,
        refusal_events=list(state.refusal_events),
        phase_timings={
            "retrieval_framework_seconds": retrieval_seconds,
            "compose_seconds": compose_seconds,
        },
    )
