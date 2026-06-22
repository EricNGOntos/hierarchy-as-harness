# Gold Nav 统一修复方案

> **日期**：2025-06-20（Phase1 2026-06-22；canonical **scopefix_v2** 2026-06-22）
> **状态**：Phase1 已实施；Phase2 nav 门控已回退；**canonical = scopefix_v2**（`[E1]` header + scope 判分/金标修复）
> **适用范围**：`src/nav/`（导航 agent）、`src/realdata/agent_delivery/code/`（evidence 组装）
> **参考代码库**：KNOWHERE 生产工程 `/Users/wuchengke/Desktop/knowhere/knowhereapi-main/packages/shared-python/shared/services/retrieval/agentic/`

---

## 0. 问题全景与修复目标

### 当前架构（有问题的）

```
┌─────────────────────────────────────────────────────────────────────────┐
│                       当前 Gold Nav 全链路                              │
│                                                                         │
│  ① 导航决策            ② chunk 物化          ③ 预算截断      ④ compose  │
│  nav_policy.py     →  tool_space.py      →  budget_eval.py  →  LLM    │
│                                                                         │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────┐    ┌────────┐  │
│  │ LLM 选路     │ →   │ __path chunk │ →   │ b500截断 │ →  │compose │  │
│  │ 无 state     │     │ PATH行+正文  │     │          │    │        │  │
│  │ 69%步浪费    │     │ 75% overhead │     │ 123字有效│    │  回答  │  │
│  │ 不知道已收集 │     │ 文本重复     │     │          │    │        │  │
│  └──────┬───────┘     └──────────────┘     └──────────┘    └────────┘  │
│         ↓                                                               │
│  ┌──────────────┐                                                       │
│  │ 后置safety   │  ← 100%触发，绕过agent决策，直接注入3个section的chunks │
│  │ (soft_safety) │                                                      │
│  └──────────────┘                                                       │
└─────────────────────────────────────────────────────────────────────────┘

问题清单：
  P0: __path chunk 文本重复 → 75% evidence 预算被浪费
  N1: Agent State 缺失 → 69% 导航步数浪费（LLM 不知道已收集了什么）
  N4: FINISH 不主动 → 88% 跑满 max_steps
  N5: Observation 信息不足 → LLM 盲选 section
  S1: 后置 soft_safety 绕过 agent 决策 → 公平性问题 + 不利于 multi_hop
```

### 目标架构（修复后）

```
┌─────────────────────────────────────────────────────────────────────────┐
│                       目标 Gold Nav 全链路                              │
│                                                                         │
│  ⓪ 前置 Discovery    ① 导航决策          ② chunk 物化       ③ compose  │
│  nav_discovery.py →  nav_policy.py    →  tool_space.py   →  LLM       │
│                                                                         │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐  ┌────────┐   │
│  │ hybrid BM25  │   │ LLM 选路     │   │ 纯正文chunk  │  │compose │   │
│  │ + dense 检索 │ → │ 有 Agent State│ → │ 无PATH重复   │→ │        │   │
│  │ 产出 D* hint │   │ 看到 D* action│   │ 短 header    │  │  回答  │   │
│  │              │   │ 知道已收集    │   │ 350+字有效   │  │        │   │
│  └──────────────┘   │ 主动 FINISH   │   └──────────────┘  └────────┘   │
│                     └──────┬───────┘                                    │
│                            ↓                                            │
│                     ┌──────────────┐                                    │
│                     │ Emergency    │  ← 仅在 collected=空 时触发        │
│                     │ Guard(可选)  │    简单 dense top-k，对所有臂一致   │
│                     └──────────────┘                                    │
└─────────────────────────────────────────────────────────────────────────┘
```

### 预期效果

| 任务类型 | 当前 recall | 当前 compose 正确 | 修复后预期 recall | 修复后预期 compose |
|---------|-----------|-----------------|-----------------|------------------|
| niche_fact | 94% | 82% | 94%+ | **90%+** |
| multi_hop | 12% | 11% | **40-50%** | **30%+** |
| scope_collection | 0% | 0% | **25-30%** | **15%+** |

---

## 1. 实验条件说明（不变）

- `pool_mode=none`：每题给定 gold doc_id，不测文档选择
- 12 个文档，51 道题（niche_fact/multi_hop/scope_collection 各 17 题）
- b500（500 字符 evidence 上限），三种方法（Gold nav / TreeRAG / Flat）公平对比
- LLM：qwen3.5-flash

---

## 2. 修复内容（共三个 Fix，按顺序执行）

---

### Fix 1: 证据组装 — 去掉 `__path` chunk 文本重复

**优先级**：🔴 最高（改动最小，收益最确定）
**影响**：niche_fact compose 正确率 82% → 90%+

#### 2.1.1 问题（当前代码）

**文件**：`src/realdata/agent_delivery/code/tool_space.py`
**函数**：`_materialize_leaf_path_chunks()`（约 L157-266）

当前代码（L246-260）：

```python
body_indices = list(range(root, root_end))
text_parts: List[str] = []
if path_indices:
    path = " / ".join((b.lines[i].content or "").strip() for i in path_indices)
    text_parts.append(f"PATH: {path}")                                    # ← 问题1: PATH行
text_parts.extend((b.lines[i].content or "").strip() for i in body_indices) # ← 问题2: body包含root
```

**Bug**：`path_indices` 最后一个 = `root`，`body_indices` 第一个也是 `root`。root 节点内容出现了**两次**。再加 `_block_for()` 的 42 字符 header，一个 188 字符的 block 只有 57 字符有效（30%）。

实际 evidence block 长这样：
```
[real_69c6095ed4242eda8c47c5b2:L10__path]                       ← 42字符 header（冗长）
PATH: 一、管理机构/（四）平台管理员/1.各专家组平台管理员：负责... ← 88字符 PATH（含叶子正文重复）
1.各专家组平台管理员：负责本专家组课件和考试习题的上传...        ← 57字符 实际内容
────────────────────────────────────────────────────────
总计 188 字符，有效内容仅 57 字符 (30%)
```

量化影响（51题总量）：

| 方法 | overhead | 有效证据 | 500字中可用 |
|------|----------|---------|------------|
| Gold nav | **75.3%** | 24.7% | **~123 字符** |
| TreeRAG | 42.5% | 57.5% | ~287 字符 |
| Flat | 13.4% | 86.6% | ~432 字符 |

#### 2.1.2 修改方案

**改动 A：`tool_space.py` 的 `_materialize_leaf_path_chunks()`**

找到以下代码块（约 L246-260）：

```python
            body_indices = list(range(root, root_end))
            text_parts: List[str] = []
            if path_indices:
                path = " / ".join((b.lines[i].content or "").strip() for i in path_indices)
                text_parts.append(f"PATH: {path}")
            text_parts.extend((b.lines[i].content or "").strip() for i in body_indices)
```

替换为：

```python
            body_indices = list(range(root, root_end))
            text_parts: List[str] = []
            # 只保留正文，不写 PATH 行（去除冗余）
            # 如果有祖先路径且不在 body 中，添加精简的上下文标记
            path_only = [i for i in path_indices if i not in set(body_indices)]
            if path_only:
                ctx = " / ".join(
                    (b.lines[i].content or "").strip()[:40] for i in path_only
                )
                text_parts.append(f"[§ {ctx}]")
            text_parts.extend(
                (b.lines[i].content or "").strip() for i in body_indices
            )
```

**改动 B：`budget_eval.py` 的 `_block_for()`**

找到（约 L61-62）：

```python
def _block_for(chunk: Chunk) -> str:
    return f"[{chunk.node_id}]\n{chunk.text or ''}"
```

替换为：

```python
def _block_for(chunk: Chunk) -> str:
    # 缩短 header: real_69c6095ed4242eda8c47c5b2:L10__path → L10
    import re
    short_id = re.sub(r'^[^:]*:(L\d+)(?:__\w+)?$', r'\1', chunk.node_id)
    return f"[{short_id}]\n{chunk.text or ''}"
```

#### 2.1.3 修复后 evidence block 示例

```
[L10]                                                            ← 4字符 header
[§ 一、管理机构 / （四）平台管理员]                                ← 20字符 精简上下文
1.各专家组平台管理员：负责本专家组课件和考试习题的上传...           ← 57字符 实际内容
────────────────────────────────────────────────────────
总计 82 字符，有效内容 57 字符 (69%)  ← 之前只有 30%
```

#### 2.1.4 验证

```bash
# 修改后重跑实验
python run_experiment.py --config fair_clean_v1 --budget 500

# 检查点：
# 1. evidence_text 中不应再有 "PATH:" 行
# 2. 有效内容占比应从 25% 提升到 65%+
# 3. niche_fact 的 compose 正确率应从 82% 提升到 88%+
```

---

### Fix 2: 导航效率 — Agent State + FINISH + Observation 增强

**优先级**：🔴 高（与 Fix 3 一起做）
**影响**：浪费步数 69% → <20%，multi_hop recall 提升

#### 2.2.1 问题（当前代码）

**文件**：`src/nav/nav_policy.py` 的 `choose_llm_action()`（约 L96-189）

当前给 LLM 的信息（L114-132）：

```python
# 当前 system prompt (L118-124):
system = (
    "You are a constrained document navigation policy. "
    "Return one JSON object only. You must choose exactly one action_id from the legal action list. "
    "Do not invent paths, tools, or action ids. "
    "Discovery collect actions are named D1, D2, etc.; if only D actions are legal, return a D id, not C. "
    "Keep reason under 12 words."
)

# 当前 user prompt (L125-133):
history = "\n".join(
    f"- step={h.get('step_idx')} action={h.get('action_id')} kind={h.get('kind')} section={h.get('section_id')}"
    for h in state.action_history[-6:]
)
user = (
    f"query: {state.query}\n"
    f"task_type: {state.task_type}\n"
    f"current_scope: {state.current_scope or '<document-root>'}\n"
    f"recent_history:\n{history or '(none)'}\n\n"
    f"section_projection:\n{projection.text}\n\n"
    f"legal_actions:\n{action_block}\n\n"
    'Return: {"action_id":"C1","reason":"short reason"}'
)
```

**缺失**：
- ❌ LLM 不知道已经收集了什么（只有 action 列表，没有"已收集路径"）
- ❌ LLM 不知道还剩多少步（没有步数信息）
- ❌ 没有 FINISH 规则（88% 跑满 max_steps）
- ❌ Observation 没有 chunk count / Leaf 标记

KNOWHERE 对应代码：`agentic/navigation/actions.py` 的 `format_agent_state_block()`（L234-305）

#### 2.2.2 修改方案

**改动 A：`nav_policy.py` 新增 `_format_agent_state()` 函数**

在文件顶部（import 之后）新增：

```python
def _format_agent_state(state: NavState, step_idx: int, config: NavConfig) -> str:
    """生成 Agent State Block，让 LLM 知道当前状态。
    
    参考 KNOWHERE: agentic/navigation/actions.py → format_agent_state_block()
    """
    lines = ["=== Agent State ==="]
    lines.append(f"Current scope: {state.current_scope or 'document-root'}")
    lines.append(f"Step: {step_idx + 1} / {config.max_steps}")
    
    # 已收集的 section（去重，只显示成功收集的）
    collected_sections = []
    explored_empty = []
    seen = set()
    for h in state.action_history:
        sid = h.get('section_id', '')
        if not sid or sid in seen:
            continue
        seen.add(sid)
        if h.get('kind') == 'collect' and h.get('n_added', 0) > 0:
            collected_sections.append(sid)
        elif h.get('kind') == 'collect' and h.get('n_added', 0) == 0:
            explored_empty.append(sid)
    
    if collected_sections:
        lines.append(f"Evidence collected: {len(collected_sections)} section(s)")
        for sid in collected_sections:
            lines.append(f'  - "{sid}"')
    else:
        lines.append("Evidence collected: none")
    
    if explored_empty:
        lines.append(f"Already explored (no new evidence): {len(explored_empty)} section(s)")
        for sid in explored_empty[:5]:
            lines.append(f'  - "{sid}"')
    
    # 步数预警
    remaining = config.max_steps - step_idx - 1
    if remaining <= 2:
        lines.append(f"⚠️ Only {remaining} step(s) remaining. Consider FINISH if evidence is sufficient.")
    
    lines.append("=== End Agent State ===")
    return "\n".join(lines)
```

**改动 B：修改 `choose_llm_action()` 的 system 和 user prompt**

将 L118-132 的 system 和 user prompt 替换为：

```python
    agent_state = _format_agent_state(state, step_idx, config)
    action_block = "\n".join(f"- {a.prompt_line()}" for a in actions)
    
    system = (
        "You are a document navigation agent running an observe-act loop.\n\n"
        "Each step chooses exactly ONE action_id from the legal action list.\n\n"
        "Action semantics:\n"
        "  - C* (COLLECT): adds a section and all descendant content to evidence.\n"
        "  - E* (EXPAND): opens a section to see its children in the next step.\n"
        "  - D* (DISCOVERY COLLECT): collects a section found by bottom-up search.\n"
        "  - S* (SEARCH): keyword search within the document.\n"
        "  - B* (BACK): return to parent scope.\n"
        "  - F* (FINISH): end navigation for this document.\n\n"
        "Rules:\n"
        "  - Do NOT re-collect a section already listed in 'Evidence collected'.\n"
        "  - Do NOT re-explore a section listed in 'Already explored'.\n"
        "  - For [Leaf] sections, prefer COLLECT over EXPAND.\n"
        "  - If evidence is sufficient for the query, choose FINISH.\n"
        "  - When steps remaining <= 2, prioritize COLLECT or FINISH.\n"
        "  - Do not invent action IDs. Use only IDs from the legal action list.\n\n"
        "Return ONLY one JSON object: {\"action_id\":\"C1\",\"reason\":\"short reason\"}\n"
        "Keep reason under 15 words. Reason must be in English."
    )
    
    user = (
        f"User query: {state.query}\n"
        f"Task type: {state.task_type}\n\n"
        f"{agent_state}\n\n"
        f"=== Actionable Observation ===\n"
        f"{projection.text}\n"
        f"=== End Actionable Observation ===\n\n"
        f"Legal actions:\n{action_block}\n\n"
        'Return: {"action_id":"...","reason":"..."}'
    )
```

**改动 C：`nav_projection.py` 增强 Observation 格式**

找到 projection 文本的生成逻辑，为每个 section 添加 chunk count 和 Leaf 标记。具体位置需要看 `nav_projection.py` 的实现，修改 section 行的格式：

```python
# 修改前:
f"- {section_id} :: {preview}"

# 修改后:
f"  [{action_id}] {section_title} ({n_chunks} chunks){' [Leaf]' if is_leaf else ''}"
f"       Preview: \"{preview[:80]}...\""
```

KNOWHERE 参考：`agentic/navigation/actions.py` → `_render_actionable_item()`（L377-409）

#### 2.2.3 改动前后对比

**改动前 LLM 看到的**：
```
query: 在《线上学习平台学习管理方案（修订）.docx》，关于...
task_type: niche_fact
current_scope: <document-root>
recent_history:
- step=1 action=C1 kind=collect section=real_69c6095ed4242eda8c47c5b2:L3
- step=2 action=C1 kind=collect section=real_69c6095ed4242eda8c47c5b2:L3
- step=3 action=C1 kind=collect section=real_69c6095ed4242eda8c47c5b2:L3

section_projection:
- real_69c6095ed4242eda8c47c5b2:L3 :: 一、管理机构及其职责...
- real_69c6095ed4242eda8c47c5b2:L17 :: 二、课程及指派管理...

legal_actions:
- C1: collect real_69c6095ed4242eda8c47c5b2:L3
- C2: collect real_69c6095ed4242eda8c47c5b2:L17
- F1: finish

Return: {"action_id":"C1","reason":"short reason"}
```

**改动后 LLM 看到的**：
```
User query: 在《线上学习平台学习管理方案（修订）.docx》，关于...
Task type: niche_fact

=== Agent State ===
Current scope: document-root
Step: 4 / 8
Evidence collected: 1 section(s)
  - "real_69c6095ed4242eda8c47c5b2:L3"
Already explored (no new evidence): 1 section(s)
  - "real_69c6095ed4242eda8c47c5b2:L3"
⚠️ Only 4 step(s) remaining. Consider FINISH if evidence is sufficient.
=== End Agent State ===

=== Actionable Observation ===
  [C1] 一、管理机构及其职责 (10 chunks) 
       Preview: "（一）成立线上学习平台管理领导小组..."
  [C2] 二、课程及指派管理 (12 chunks)
       Preview: "（一）课程管理。由培训中心统一管理..."
  [D1] 三、考核及奖惩 (8 chunks) [Discovery hit, score=0.78]
       Preview: "（一）考核方式。采用线上考试..."
=== End Actionable Observation ===

Legal actions:
- C1: collect 一、管理机构及其职责
- C2: collect 二、课程及指派管理
- D1: discovery collect 三、考核及奖惩
- F1: finish

Return: {"action_id":"...","reason":"..."}
```

**关键变化**：
1. LLM 看到"Evidence collected: L3"→ 不会再选 C1
2. LLM 看到"Already explored: L3"→ 知道 L3 已经没有新内容
3. LLM 看到 D1 discovery hint → 可以主动去收集 discovery 发现的 section
4. LLM 看到"4 steps remaining"→ 会考虑 FINISH

---

### Fix 3: 兜底机制 — 后置注入改为前置 Discovery + Emergency Guard

**优先级**：🔴 高（与 Fix 2 一起做）
**影响**：multi_hop recall 12% → 40-50%，消除公平性问题

#### 2.3.1 问题（当前代码）

**文件**：`src/nav/nav_agent.py` 的 `run_nav_episode()`

当前兜底逻辑（约 L265-281）：

```python
    # 导航循环结束后，100% 触发 soft_safety
    added_soft, soft_ids, soft_meta = apply_soft_safety_collect(
        ts, state, cfg,
        budget_chars=int(budget_chars),
        collect_subtree_fn=_collect_subtree,
        add_scored_fn=_add_scored,
        dedupe_fn=_dedupe_scored,
    )
    if soft_ids:
        steps.append(AgentStep(
            step_idx=len(steps) + 1,
            action="nav_soft_safety_collect",
            detail=soft_meta,
        ))
    
    scored_chunks = _dedupe_scored(list(state.collected))  # ← 包含了 soft_safety 注入的 chunks
```

**问题**：
- 100% 触发，不管导航是否已经收集够了
- 绕过 agent 决策：LLM rerank 后直接 collect 3 个新 section
- 只给 Gold nav 用，TreeRAG/Flat 没有对等物 → 公平性问题
- 是"后置补救"而非"前置引导"

**当前数据**：
```
soft_safety 触发: 51/51 (100%)
soft_safety 注入新 section: 103 个 (100% 导航没去过的)
soft_safety 总 added: 299 chunks (占总收集的 15%)
```

KNOWHERE 的做法完全不同：
1. Discovery 信号在导航**之前**计算，作为 D* action 传入导航循环
2. Agent **自主决定**是否 COLLECT D* action
3. Emergency guard 只在 collected=空 时触发

KNOWHERE 参考代码：
- `agentic/navigation/actions.py` L156-184 → D* action 生成
- `agentic/navigation/actions.py` L614-627 → `_score_item()` discovery 分数传播
- `agentic/navigation/document.py` L421-483 → Emergency guard

#### 2.3.2 修改方案

**改动 A：`nav_agent.py` — 把 discovery 从循环后移到循环前**

在 `run_nav_episode()` 中，找到导航循环的开始位置。在循环**之前**添加 discovery 计算：

```python
    # ═══ 修改：在导航循环前计算 discovery hints ═══
    # 复用现有的 _hybrid_section_candidates + compute_discovery_scores
    from nav_discovery import compute_discovery_scores
    
    discovery_hints = compute_discovery_scores(ts, state, cfg)
    # discovery_hints = [{"section_id": "...", "discovery_score": 0.82, "label": "..."}, ...]
    
    # 把 discovery_hints 存入 state，供 build_legal_actions 使用
    state.discovery_hints = discovery_hints
```

**改动 B：`nav_actions.py` — build_legal_actions 添加 D* action**

在 `build_legal_actions()` 中，现有的 COLLECT/EXPAND action 生成之后，添加 D* discovery action：

```python
def build_legal_actions(
    state: NavState,
    projection: Projection,
    *,
    config: NavConfig,
) -> List[LegalAction]:
    actions = []
    # ... 现有的 C*/E*/S*/B*/F* action 生成 ...
    
    # ═══ 新增：D* discovery COLLECT actions ═══
    discovery_hints = getattr(state, 'discovery_hints', []) or []
    collected_sids = {
        h.get('section_id', '') for h in state.action_history
        if h.get('kind') == 'collect' and h.get('n_added', 0) > 0
    }
    d_index = 1
    for hint in sorted(discovery_hints, key=lambda x: -float(x.get('discovery_score', 0))):
        sid = hint.get('section_id', '')
        if not sid or sid in collected_sids:
            continue
        # 不重复现有 C* actions
        if any(a.section_id == sid for a in actions if a.kind == ActionKind.COLLECT):
            continue
        actions.append(LegalAction(
            action_id=f"D{d_index}",
            kind=ActionKind.COLLECT,
            section_id=sid,
            label=f"Discovery collect: {hint.get('label', sid)[:60]} (score={float(hint.get('discovery_score', 0)):.2f})",
            score=float(hint.get('discovery_score', 0)),
        ))
        d_index += 1
        if d_index > 5:  # 最多 5 个 D* action
            break
    
    return actions
```

**改动 C：`nav_agent.py` — 删除后置 soft_safety，改为 Emergency Guard**

删除当前的 `apply_soft_safety_collect` 调用（L265-281），替换为：

```python
    # ═══ 修改：删除后置 soft_safety，改为 Emergency Guard ═══
    # Emergency Guard: 仅在导航完全没收集到任何东西时触发
    if not state.collected:
        # 极端情况：agent 走了 max_steps 但一个 chunk 都没收集到
        # 用简单的 dense top-k 作为最后防线（对所有方法臂都可用）
        pool = ts.leaf_path_search_pool(state.doc_id)
        if pool:
            from agent_delivery.code.index_retrieval import CorpusIndex
            scored = ts._idx.search(state.query, pool, min(len(pool), 8), doc_id_filter=state.doc_id)
            for chunk, score in scored:
                state.collected.append((chunk, score * 0.4))  # 低权重
        steps.append(AgentStep(
            step_idx=len(steps) + 1,
            action="nav_emergency_guard",
            detail={"reason": "zero_collection_fallback", "n_added": len(state.collected)},
        ))
    
    scored_chunks = _dedupe_scored(list(state.collected))
```

**改动 D（可选但推荐）：`nav_discovery.py` — 调整 `compute_discovery_scores`**

确保 `compute_discovery_scores` 返回的格式适合传入 `build_legal_actions`。如果当前返回格式不同，需要适配。参考 KNOWHERE 的 `_score_item()` 的 ancestor/descendant 衰减逻辑（0.9/0.65）：

```python
def compute_discovery_scores(ts, state, config):
    """计算 discovery hints，供导航循环使用。
    
    参考 KNOWHERE: agentic/navigation/actions.py → _score_item()
    """
    section_candidates = _hybrid_section_candidates(ts, state, config)
    if not section_candidates:
        return []
    
    # 可选：LLM rerank 精选 top candidates
    # picked_ids = _picked_discovery_ids(state, section_candidates, config)
    
    return [
        {
            "section_id": str(c.get("section_id", "")),
            "discovery_score": float(c.get("discovery_score", 0.0)),
            "label": str(c.get("label", ""))[:100],
        }
        for c in section_candidates
        if float(c.get("discovery_score", 0.0)) > 0.1  # 过滤低分噪音
    ]
```

#### 2.3.3 改动前后对比

**改动前（后置注入）**：
```
导航循环 8 步 → agent 收集了 section A
                                     ↓
                           apply_soft_safety_collect（100% 触发）
                           LLM rerank 选 section B, C, D
                           直接 collect B, C, D → 注入 state.collected
                                     ↓
                           evidence = A + B + C + D 的 chunks
```

**改动后（前置 Discovery + Emergency Guard）**：
```
compute_discovery_scores → 得到 D1=section_B(0.82), D2=section_C(0.71)
                                     ↓
导航循环:
  step 1: LLM 看到 C1=A, D1=B, D2=C → 选 C1(收集A)
  step 2: LLM 看到 Agent State "已收集A", D1=B, D2=C → 选 D1(收集B) 
  step 3: LLM 看到 "已收集A,B", D2=C → 选 D2(收集C)
  step 4: LLM 看到 "已收集A,B,C", 3 steps left → 选 F1(FINISH)
                                     ↓
evidence = A + B + C 的 chunks（全部由 agent 自主决策）
```

**核心区别**：
1. Agent 自己决定要不要 COLLECT discovery 提示的 section（不是被动注入）
2. Discovery 作为选项出现在导航循环中，agent 可以结合 query 和 state 做判断
3. Emergency guard 只在极端情况（零收集）触发
4. 公平性：D* actions 是 Gold nav 架构的一部分，不是额外的"补丁"

---

## 3. 文件修改清单

| 文件 | Fix | 改动内容 | 改动量 |
|------|-----|---------|--------|
| `src/realdata/agent_delivery/code/tool_space.py` | Fix1 | `_materialize_leaf_path_chunks()` 去掉 PATH 行重复 | ~10 行 |
| `src/realdata/agent_delivery/code/budget_eval.py` | Fix1 | `_block_for()` 缩短 header | ~5 行 |
| `src/nav/nav_policy.py` | Fix2 | 新增 `_format_agent_state()` + 重写 system/user prompt | ~60 行 |
| `src/nav/nav_projection.py` | Fix2 | Observation 格式增加 chunk count / Leaf 标记 | ~15 行 |
| `src/nav/nav_agent.py` | Fix2+3 | 前置 discovery + 删后置 soft_safety + Emergency Guard | ~30 行 |
| `src/nav/nav_actions.py` | Fix3 | `build_legal_actions()` 添加 D* action 生成 | ~25 行 |
| `src/nav/nav_discovery.py` | Fix3 | 调整 `compute_discovery_scores` 返回格式 | ~10 行 |

**总改动量**：约 155 行（新增+修改），删除 `apply_soft_safety_collect` 调用约 20 行。

---

## 4. 执行顺序

```
第一步（1天）：Fix1 — 证据组装
  改 tool_space.py + budget_eval.py
  重跑实验，确认 niche_fact 分数提升
  ↓
第二步（2天）：Fix2 + Fix3 — 导航效率 + Discovery（一起做）
  改 nav_policy.py（Agent State + prompt）
  改 nav_projection.py（Observation 格式）
  改 nav_agent.py（前置 discovery + 删 soft_safety + Emergency Guard）
  改 nav_actions.py（D* action）
  改 nav_discovery.py（调整返回格式）
  重跑实验，确认 multi_hop / scope_collection 分数提升
  ↓
第三步（半天）：验证 + 消融
  跑消融：分别关闭 discovery / Agent State，量化各组件贡献
  出最终对比表
```

---

## 5. 验证清单

修复完成后，逐项检查（canonical tag=`fair_clean_scopefix_v2`；历史 Phase2 tag=`fair_clean_unified_v3`）：

### Fix1 验证
- [x] `evidence_text` 中不再有 `PATH:` 行（51/51）
- [x] evidence block header 为方法无关 `[E1]`/`[E2]`（`method_neutral_ordinal_v1`）
- [x] 有效 evidence 字符显著提升（相对 Fix 前 ~123 字）
- [x] niche_fact task 0.765（scopefix_v2）

### Fix2 验证
- [ ] collect 浪费步（added=0）从 69% 降到 <25%（v1 仍 ~66%；Phase2 过滤已 collect/empty section）
- [x] FINISH 步数明显增加（v1: 39 finish / 51 题）
- [x] Phase2：已 collect / 已 explore 的 section 不再出现在 C* 列表

### Fix3 验证
- [x] `nav_soft_safety_collect` step 不再出现
- [x] D* 出现在 legal_actions；部分题 agent 实际选择 D*
- [ ] multi_hop task 目标 30%+（scopefix_v2 0.118）
- [ ] scope_collection task 目标 15%+（scopefix_v2 0.392，判分修复后）
- [x] Emergency guard 触发率 0%

### 公平性验证
- [x] 三方同 b500；无 soft_safety 后置注入
- [x] TreeRAG compose/evidence 与 Gold 共用 `src/realdata/agent_delivery`
- [ ] Emergency Guard 三方对称（仍仅 Gold 实现，0 触发）

### 历史 Phase2 消融（nav 已回退，结果未纳入 canonical）
- [x] `fair_clean_unified_v3`：Gold 0.325（低于 Phase1 unified header）
- [x] `fair_clean_ablation_no_discovery`：Gold 0.333
- [x] `fair_clean_ablation_no_agent_state`：Gold 0.297（Agent State **关键**）

### Canonical 结论（2026-06-22）
- **唯一主结果**：`fair_clean_scopefix_v2`（Gold 0.425 / TreeRAG 0.398 / Flat 0.360）
- 旧 tag（`unified_v1/v2`、`header_v1`、`scopefix_v1`）已从仓库移除
- 下一步若提 multi：优先 compose 分组 / 软导航，勿用 Phase2 FINISH 硬门控

---

## 6. KNOWHERE 参考代码索引

| 功能 | KNOWHERE 文件 | 函数/类 |
|------|-------------|---------|
| Agent State Block | `agentic/navigation/actions.py` | `format_agent_state_block()` (L234-305) |
| Observation 格式 | `agentic/navigation/actions.py` | `format_actionable_observation()` (L308-374) |
| D* action 生成 | `agentic/navigation/actions.py` | `build_legal_actions()` (L64-231) |
| Discovery 分数传播 | `agentic/navigation/actions.py` | `_score_item()` (L614-627) |
| Rejected 复活 | `agentic/navigation/actions.py` | `_path_has_discovery_signal()` (L651-660) |
| Collector prompt | `agentic/prompts.py` | `COLLECTOR_PROMPT` (L33-102) |
| Query Intent 分类 | `agentic/prompts.py` | `QUERY_INTENT_PROMPT` (L105-119) |
| 导航主循环 | `agentic/navigation/document.py` | `_navigate_collector()` (L156-521) |
| Emergency Guard | `agentic/navigation/document.py` | L421-483 |
| 预算管理 | `agentic/navigation/actions.py` | `_format_budget_state()` (L534-553) |

---

## 7. 关键数据支撑

### 当前检索 recall（修复前基线）

| 任务类型 | Gold nav recall | TreeRAG recall | 差距来源 |
|---------|----------------|---------------|---------|
| niche_fact (17题) | **94%** | 100% | 几乎持平 → 问题在证据组装 |
| multi_hop (17题) | **12%** | 36% | 导航能力不足 + 证据组装差 |
| scope_collection (17题) | **0%** | 30% | 导航策略不适配 + 证据组装差 |

### 当前导航效率

```
总导航步数 (不含 compose/safety): 390
浪费步数 (collect added=0): 269 (69%)
连续重复收集同一 section: 209
自主 FINISH: 6/51 题 (12%)
跑满 max_steps: 45/51 题 (88%)
平均每题: 7.6 步导航，其中 5.3 步是无效的
```

### 当前 soft_safety 贡献

```
soft_safety 触发: 51/51 (100%)
soft_safety 注入新 section: 103 个 (0% 与导航重叠，100% 导航没去过)
soft_safety 总 added: 299 chunks (占总收集的 15%)
按题型: niche_fact 13%, multi_hop 18%, scope_collection 13%
```

### 当前 evidence 有效内容

```
Gold nav: 平均 123 字符有效 / 500 字符预算 (25%)
TreeRAG: 平均 299 字符有效 / 500 字符预算 (60%)
Flat:    平均 432 字符有效 / 500 字符预算 (87%)
```
