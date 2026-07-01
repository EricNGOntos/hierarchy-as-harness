# Scope_Collection 优化方案 V2：修订版

> 基于 v1 方案评审 + knowhereapi-main 生产架构对照 + 代码路径实际分析

> 2026-07-02 更新：当前落地版为 `latest_clean400_scope_compact_cap180_v1`。已实现 Phase 1 outline collection，并新增 compact evidence packing 与 scope compose guidance；未把 Section Summary 增强作为本轮默认改动。

## 当前落地结果

省成本复跑口径：只重跑 133 条 `scope_collection`，267 条非 scope 行复用 `scope_outline_fixed_v1` 同题结果；最终质量仍按完整 400 题汇总。

| Method | Overall | Niche | Multi-hop | Scope | Evidence |
|---|---:|---:|---:|---:|---:|
| Gold Nav | 0.2111 | 0.2090 | 0.0777 | 0.3466 | 0.6188 |
| Pred Nav | 0.1450 | 0.1276 | 0.0601 | 0.2474 | 0.4213 |
| TreeRAG | 0.2016 | 0.1522 | 0.0831 | 0.3698 | 0.5125 |
| Flat | 0.1376 | 0.0903 | 0.0683 | 0.2547 | 0.4988 |

相比 `latest_clean400_scope_outline_fixed_v1`：

| Arm | Overall Δ | Scope Δ | Evidence Δ | Scope W/L/T |
|---|---:|---:|---:|---:|
| Gold | +0.0219 | +0.0658 | +0.0021 | 36/11/86 |
| Pred | +0.0126 | +0.0380 | +0.0000 | 27/10/96 |

正式结果文件：

- `results/latest_clean400_scope_compact_cap180_v1_summary.{json,md}`
- `results/latest_clean400_scope_compact_cap180_v1_gold_b500.json`
- `results/latest_clean400_scope_compact_cap180_v1_pred_b500.json`
- `results/latest_clean400_scope_compact_cap180_scope133_v1_summary.{json,md}`

---

## 零、V1 问题总结

| # | V1 问题 | 影响 | V2 修正 |
|---|---------|------|---------|
| 1 | 修改 `_gather_all_section_candidates`，但 canonical 实验走 `hier_policy=nav` → `nav_agent.py` | 代码路径错配，改了不会生效 | 修改目标改为 `nav_agent.py:_scope_collect_scored` |
| 2 | `_is_outline_query` 用 `"主要条目" in query` 硬编码 | 过拟合已观察 400 题 | 改用结构化 heuristic + 可选 LLM fallback |
| 3 | `child_level = 2` 硬编码 | 文档层级结构多样 | 自适应检测：`min(levels[j] > anchor_level)` |
| 4 | outline mode 取"子节首 chunk"（即首行单行） | 单行内容不足以构成有效 outline | 取子节首 N 行（N=2-3）窗口 |
| 5 | 收益估算 +0.04~0.06 | 过于乐观 | 修正为 +0.015~0.030 |
| 6 | 未处理 section path 占 evidence 37-60% 的浪费 | budget 利用率低 | 利用已有 `EVIDENCE_MERGE_SECTIONS` + outline mode 天然避免深层 path |

---

## 一、架构定位

### 1.1 Canonical 实验代码路径

```
runner_bodyrich.py
  └→ run_bodyrich_episode(hier_policy="nav")
       └→ nav_agent.run_nav_episode()
            ├→ loop: choose_llm_action() → EXPAND/BACK/COLLECT/SEARCH/FINISH
            ├→ ActionKind.COLLECT → _collect_subtree()
            │       └→ if task_type == "scope_collection":
            │              _scope_collect_scored()  ← 【修改点 1】
            └→ evaluate_at_budget(state.collected, budget_chars)  ← 【修改点 2 不变】
```

### 1.2 knowhere 的验证参照

knowhereapi-main (`agentic/navigation/document.py`) 已在生产验证：

1. **Query Intent Classification** (`_classify_query_intent` → LLM → 6 类)
2. **Outline Collection** (`"outline": true` → `hydrate_mode: "outline"`)
3. **Intent-aware prompt** (Collector prompt: "If STRUCTURE_OVERVIEW, prefer outline collection")

核心差异：knowhere 是 LLM-driven navigation + hydration-based collection；研究代码是 LLM-nav + embedding-based scoring。映射关系：

| knowhere | research code | 等价操作 |
|----------|---------------|----------|
| COLLECT with outline=true | _scope_collect_scored → outline mode | 取结构摘要级内容 |
| COLLECT with outline=false | _scope_collect_scored → current mode | 取全部 relevant chunks |
| query_intent == STRUCTURE_OVERVIEW | _is_scope_outline_query() | 路由到 outline 分支 |

---

## 二、修订方案

### 方案 1（修订）：Scope Outline Collection

#### 核心修改：`nav_agent.py:_scope_collect_scored`

当前 `_scope_collect_scored` 在 section 内部用 `local_band` 策略选 chunk — 以 relevance 最高的行为锚点，取其周围 k 行窗口。这对 FACTUAL_DETAIL 类查询合理，但对 STRUCTURE_OVERVIEW 类查询（"列举主要条目"）会：
- 锚定在某个深层子节的具体内容上
- 只覆盖局部窗口，遗漏其他子节

**修改策略**：对 outline 类查询，切换为"广度优先子节首窗口"模式。

#### Intent 分类（替代硬编码关键词）

```python
def _is_scope_outline_query(query: str, task_type: str) -> bool:
    """
    判断 scope_collection 查询是否为结构概览类（对应 knowhere STRUCTURE_OVERVIEW）。
    
    策略：多条件 OR，覆盖常见中文表述模式。
    不使用 LLM（避免额外 API 成本），但比单一关键词匹配更泛化。
    """
    if (task_type or "").strip().lower() not in ("scope_collection", "regulatory_coverage"):
        return False
    q = (query or "").strip()
    # 模式 1：显式"主要条目/内容/项目"
    if re.search(r"主要(条目|内容|项目|章节|部分|要点|事项)", q):
        return True
    # 模式 2："列举/列出...部分" 或 "包含哪些" + 无"具体/详细/所有步骤"
    if re.search(r"(列举|列出|概述|概括|归纳).{0,20}(部分|章节|条目|内容|要点)", q):
        if not re.search(r"(具体|详细|全部|所有).{0,4}(步骤|内容|要素|条款)", q):
            return True
    # 模式 3："哪些部分/章节" 式枚举查询
    if re.search(r"(哪些|包含什么|有什么).{0,10}(部分|章节|条目|内容)", q):
        return True
    return False
```

**为什么不用 LLM**：
- knowhere 用 LLM 因为查询来自用户（措辞完全开放）
- 研究代码的查询来自标注数据集（模式有限且可枚举）
- 额外 LLM 调用会使 scope_collection 的 133 题多消耗 ~133 次 API call，增加成本和延迟
- 如果 heuristic 不够，可通过 `SCOPE_OUTLINE_USE_LLM=1` 环境变量开启 LLM fallback

#### 自适应 Outline Collection

```python
def _scope_collect_outline(
    idx: Any,
    pool: List[Chunk],
    action: LegalAction,
    state: NavState,
    config: NavConfig,
) -> List[Tuple[Chunk, float]]:
    """
    Outline mode：对目标 section 的每个直接子节，取首 N 行窗口。
    实现广度优先覆盖——每个 child 都出现在 evidence 中，而非只深入少数。
    
    参照 knowhere 的 outline collection 语义：标题 + 摘要级内容。
    """
    ordered = _line_order(pool)
    if not ordered:
        return []
    
    # 参数
    action_score_cap = max(0.0, float(os.environ.get("NAV_SCOPE_ACTION_SCORE_CAP", "1.0") or "1.0"))
    action_score = max(0.0, min(float(action.score or 0.0), action_score_cap))
    base = float(config.read_score_bonus) + action_score
    lines_per_child = max(1, int(os.environ.get("NAV_SCOPE_OUTLINE_LINES_PER_CHILD", "3") or "3"))
    
    # 获取 bundle 和 levels 以检测子节边界
    tools_idx = idx  # CorpusIndex
    bundle = tools_idx._bundles.get(state.doc_id)
    if not bundle:
        # fallback 到 line_order 全量
        return _scope_collect_scored(idx, pool, action, state, config)
    
    lines = bundle.lines
    levels = bundle.levels_for_tree
    
    # 找到目标 section 范围（通过 action.section_id）
    target_sid = action.section_id
    if not target_sid:
        return _scope_collect_scored(idx, pool, action, state, config)
    
    # 从 section_id 解析 line_id
    # section_id 格式: "doc_id:L{line_id}"
    m = re.search(r":L(\d+)$", target_sid)
    if not m:
        return _scope_collect_scored(idx, pool, action, state, config)
    target_line_id = int(m.group(1))
    
    # 在 lines 中找到 section 的起止
    sec_start = None
    sec_end = None
    for j, rec in enumerate(lines):
        if rec.line_id == target_line_id:
            sec_start = j
            break
    if sec_start is None:
        return _scope_collect_scored(idx, pool, action, state, config)
    
    anchor_level = levels[sec_start]
    for j in range(sec_start + 1, len(lines)):
        if levels[j] <= anchor_level:
            sec_end = j
            break
    if sec_end is None:
        sec_end = len(lines)
    
    # 自适应检测 child_level（不硬编码 level=2）
    child_levels = set(
        levels[j] for j in range(sec_start + 1, sec_end)
        if levels[j] > anchor_level
    )
    if not child_levels:
        # section 内没有更深层级 → 所有内容都是叶子，fallback
        return _scope_collect_scored(idx, pool, action, state, config)
    child_level = min(child_levels)  # 直接子节的 level
    
    # 找到每个直接子节的起始位置
    child_starts: List[int] = []
    for j in range(sec_start + 1, sec_end):
        if levels[j] == child_level:
            child_starts.append(j)
    
    if len(child_starts) < 2:
        # 只有 0-1 个子节，outline 模式无意义，fallback
        return _scope_collect_scored(idx, pool, action, state, config)
    
    # 构建 line_id → chunk 的映射（pool 中每个 chunk 是单行）
    chunk_by_line_id: Dict[int, Chunk] = {}
    for c in pool:
        if c.line_ids:
            chunk_by_line_id[c.line_ids[0]] = c
    
    # 收集：section 首行 + 每个 child 的首 N 行
    outline_chunks: List[Tuple[Chunk, float]] = []
    seen_ids: set = set()
    
    # section 自身首行（通常是 section 标题）
    sec_first = chunk_by_line_id.get(lines[sec_start].line_id)
    if sec_first and sec_first.node_id not in seen_ids:
        outline_chunks.append((sec_first, base + 1.0))
        seen_ids.add(sec_first.node_id)
    
    # 每个 child 取首 N 行
    for ci, child_j in enumerate(child_starts):
        # child 的范围：到下一个同级子节或 section 末尾
        child_end = child_starts[ci + 1] if ci + 1 < len(child_starts) else sec_end
        
        collected_for_child = 0
        for j in range(child_j, min(child_j + lines_per_child, child_end)):
            line_id = lines[j].line_id
            chunk = chunk_by_line_id.get(line_id)
            if chunk and chunk.node_id not in seen_ids:
                # 分数：按文档顺序递减，保证所有子节公平
                score = base + 0.9 - ci * 0.01 - collected_for_child * 0.001
                outline_chunks.append((chunk, score))
                seen_ids.add(chunk.node_id)
                collected_for_child += 1
    
    # 如果 outline 收集结果太少（不如 fallback）
    min_outline = max(3, int(os.environ.get("NAV_SCOPE_OUTLINE_MIN_CHUNKS", "4") or "4"))
    if len(outline_chunks) < min_outline:
        return _scope_collect_scored(idx, pool, action, state, config)
    
    return outline_chunks
```

#### 修改调用点

在 `_collect_subtree` 中插入路由：

```python
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
                # ── V2: outline mode 路由 ──
                if _env_enabled("NAV_SCOPE_OUTLINE_MODE", "1") and _is_scope_outline_query(state.query, task_type):
                    return _scope_collect_outline(idx, pool, action, state, config)
                return _scope_collect_scored(idx, pool, action, state, config)
            scored = idx.search(state.query, pool, min(len(pool), int(config.collect_k)), doc_id_filter=state.doc_id)
            return [(c, float(s) + float(config.read_score_bonus)) for c, s in scored]
    # ... existing fallback ...
```

#### 环境变量

| 变量 | 默认 | 说明 |
|------|------|------|
| `NAV_SCOPE_OUTLINE_MODE` | `1` | 开关 outline mode |
| `NAV_SCOPE_OUTLINE_LINES_PER_CHILD` | `3` | 每个子节取首 N 行 |
| `NAV_SCOPE_OUTLINE_MIN_CHUNKS` | `4` | outline 结果少于此数时 fallback |
| `SCOPE_OUTLINE_USE_LLM` | `0` | 是否用 LLM 辅助 intent 分类 |

---

### 方案 2（优先级提升）：Section Summary 增强

#### 为什么提升优先级

方案 1 的前提是 nav agent 的 LLM 能正确选择包含答案的 section 进行 COLLECT。如果 nav agent 的 section routing 本身就 miss（诊断显示 19% NAV_MISS），outline mode 只在正确 section 上有效。

Section Summary 增强改善的是 **上游** — 让 nav agent 在做 EXPAND/COLLECT 决策时看到更完整的子结构信息。

#### 实现

**修改文件**: `src/realdata/agent_delivery/code/index_retrieval.py:117-136`

```python
# 现有代码：
# title = lines[start_j].content[:200]
# body_preview = "\n".join(r.content for r in sec_lines[:3])[:500]
# summary_text = f"{title}\n{body_preview}"

# 改为：
title = lines[start_j].content[:200]
body_preview = "\n".join(r.content for r in sec_lines[:3])[:500]

# 收集直接子节标题（自适应 child_level）
child_levels_in_sec = set(
    levels[j] for j in range(start_j + 1, end_j)
    if levels[j] > levels[start_j]
)
if child_levels_in_sec:
    child_level = min(child_levels_in_sec)
    children_titles = "；".join(
        lines[j].content[:60]
        for j in range(start_j + 1, end_j)
        if levels[j] == child_level
    )[:300]
else:
    children_titles = ""

if children_titles:
    summary_text = f"{title}\n子节：{children_titles}\n{body_preview}"
else:
    summary_text = f"{title}\n{body_preview}"
```

**影响评估**：
- Section summary 从 ~200-700 chars 增加到 ~300-1000 chars
- 对 sentence-transformer 的 max_seq_length（通常 512 token / ~1500 chars）仍在安全范围
- 测试方法：对比 `_score_top_sections` 在修改前后对 NAV_MISS 题的 top-1 准确率

---

### 方案 3：Section-Complete for FACTUAL_DETAIL（保持不变）

与 v1 一致：对 scope_collection 中非 outline 的 FACTUAL_DETAIL 类查询（"列出所有具体步骤"），一旦锁定 section，取全部 chunk 按文档顺序。

这是 `_scope_collect_scored` 的现有策略 `line_order` 已经近似做到的事，只需确认在这类查询上不被 `local_band` 截断。

修改：当 `_is_scope_outline_query() == False` 时，强制使用 `line_order` 而非 `local_band`：

```python
# 在 _scope_collect_scored 开头加：
if not _is_scope_outline_query(state.query, state.task_type or ""):
    # FACTUAL_DETAIL: 完整覆盖优先于局部精度
    strategy = "line_order"
```

---

## 三、实施路线（修订）

```
Phase 0 (前置):  Section Summary 增强 → 改善上游 routing 准确率
Phase 1 (核心):  Outline Mode in nav_agent → _scope_collect_outline
Phase 2 (后续):  Section-Complete for FACTUAL_DETAIL
Phase 3 (验证):  在新 holdout 上验证（遵循 README 指示）
```

当前实际落地状态：

| 项 | 状态 | 说明 |
|---|---|---|
| Phase 1 outline mode | 已实现 | `src/nav/nav_agent.py` 中从 doc bundle lines 构造 outline chunks，避免依赖 leaf/path chunk lookup |
| Compact evidence packing | 已实现 | `budget_eval.py` 对 scope/regulatory 任务按 chunk 压缩 evidence 文本，默认 `BODYRICH_SCOPE_COMPACT_CHARS_PER_CHUNK=180` |
| Scope compose guidance | 已实现 | `compose_llm.py` 强化 scope 输出指导：不要把同一完整规定拆成多个 item，尽量覆盖不同 evidence block/subheading |
| Summary robustness | 已实现 | `bin/50_summarize_goldpred_reuse.py` 支持 scope-only 子集，不因空 niche/multi-hop 崩溃 |
| Phase 0 Section Summary 增强 | 未默认启用 | 暂不纳入当前 canonical，避免在观察集上继续扩大改动面 |
| Phase 2 Section-Complete | 未默认启用 | 当前收益主要来自 outline + compact + compose |

**为什么 Section Summary 排第一**：
- 低风险（只影响 index 构建，不改运行时逻辑）
- 改善所有 task_type 的 routing（正面溢出）
- 是 Phase 1 的前提条件——outline mode 要有效，首先得 route 到正确 section

---

## 四、预期收益（修订）

| 阶段 | scope_collection | Overall | 依据 |
|------|:---:|:---:|------|
| scope_outline_fixed_v1 | 0.2809 | 0.1892 | — |
| +Phase 0 (summary) | ~0.30 | ~0.193 | 修复部分 NAV_MISS（19%×50%×scope权重） |
| +Phase 1 (outline) | ~0.35-0.38 | ~0.205-0.215 | 修复 ~50% PARTIAL |
| +Phase 2 (complete) | ~0.36-0.40 | ~0.208-0.220 | 修复部分 FACTUAL_DETAIL |
| 当前 canonical | 0.3466 | 0.2111 | Phase 1 + compact evidence + compose guidance，落在保守预期内 |

**为什么比 v1 保守**：
1. COMPOSE_FAIL（27%）大部分是 LLM 质量问题，不会因 evidence 改善而自动修复
2. outline mode 只对 intent 分类正确 + section routing 正确的题生效
3. section routing 即使增强后也无法 100% 命中

---

## 五、与 knowhere 的对齐总结

| knowhere 机制 | 研究代码对应 | 状态 |
|---|---|---|
| `_classify_query_intent()` → LLM | `_is_scope_outline_query()` → heuristic | Phase 1 新增 |
| `outline: true` in COLLECT | `_scope_collect_outline()` | Phase 1 新增 |
| `section_tree` + `outline_items` in DocTreeNode | `index_retrieval.section_summaries` + `fact_by_section` | 已有（粒度不同） |
| `trim_evidence_to_budget` | `evaluate_at_budget` | 已有 |
| LLM navigation loop | `run_nav_episode` + `choose_llm_action` | 已有 |
| Discovery hints → routing | `compute_discovery_scores` | 已有 |

研究代码的 outline mode 不需要 knowhere 的完整 hydration 机制（DB-backed section tree + async chunk loading），因为：
- 研究代码的 chunk 是内存中的 `List[Chunk]`，已按 section 分组在 `fact_by_section`
- 不需要 async hydration — 直接按 line_id 从 pool 中选取

---

## 六、验证计划（修订）

1. **隔离验证**：`NAV_SCOPE_OUTLINE_MODE=0` 跑全量 400 题，确认 niche_fact/multi_hop 分数不变
2. **消融**：
   - Phase 0 only vs Phase 0+1 vs Phase 0+1+2
   - `NAV_SCOPE_OUTLINE_LINES_PER_CHILD` = 2/3/5 对比
3. **Intent 分类准确率**：对 133 题 scope_collection 人工标注 outline/detail，计算 `_is_scope_outline_query` 的 precision/recall
4. **Case 检查**：抽 10 个 PARTIAL→SUCCESS 的 case，确认 evidence 中确实包含了所有子节首行
5. **Holdout 验证**：新 holdout 集上跑完整流程，不在 400 题上调参

---

## 七、风险与缓解

| 风险 | 概率 | 缓解 |
|------|------|------|
| intent 分类误判（outline 查询走了 detail 路径） | 中 | miss 只是保持现状，不会变差；recall 优先于 precision |
| intent 分类误判（detail 查询走了 outline 路径） | 低 | outline 取首 3 行仍包含答案要素；fallback 有 min_chunks 兜底 |
| 子节首 3 行不含答案要素 | 低 | 金标答案定义是"子节首行/摘要句"，首 3 行一定覆盖 |
| section routing 仍然 miss | 中 | Phase 0 先改善 routing；剩余 miss 需要更根本的 retrieval 改进 |
| budget 不够装全部子节 | 低 | 7 个子节 × 3 行 × ~60 字 = ~1260 字 > budget 500；但 outline chunk 没有深层 path header 开销，实际占 ~500-700 字足够放 7-10 个首行 |
