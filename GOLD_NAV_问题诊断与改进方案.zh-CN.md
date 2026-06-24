# Gold Nav 问题诊断与改进方案

> **说明**：本文为 Nav 改进过程的历史记录与轨迹分析。**当前 canonical 基线与主表**见 [UNIFIED_FIX_PLAN.zh-CN.md](UNIFIED_FIX_PLAN.zh-CN.md) 与 [results/paper_main_experiment.zh-CN.md](results/paper_main_experiment.zh-CN.md)（`goldnav_e2_v1`，Gold 总体 **0.504**）。下文早期段落仍引用 `scopefix_v2` 数值，仅供对照演进路径。

日期：2026-06-22（正文）· canonical 晋升：2026-06-24

状态：`fair_clean_goldnav_e2_v1` 为唯一主结果与代码基线

## 0. 仓库与基线状态

### 0.1 代码拉取情况

- 本地 `main` 曾落后 `origin/main` 7 个提交，已通过 `git pull --ff-only` 快进到最新。
- 最新提交：`309cadb` — `Align canonical results with scope_0008 gold fix and judge-only refresh.`
- 拉取前本地未跟踪文件已通过 `git stash push -u -m "pre-pull local analysis docs"` 保护；`[REVIEW] current status.md` 已从 stash 恢复为未跟踪文件。
- 旧版同名 `UNIFIED_FIX_PLAN.zh-CN.md` 仍在 stash 中；远端已新增 tracked 版同名文件（内容已变为 canonical 协议说明，不再是旧版「待执行三步修复方案」）。

### 0.2 当前 canonical 基线

远端 `UNIFIED_FIX_PLAN.zh-CN.md` 与 `results/summary.md` 均声明：`fair_clean_scopefix_v2` 是唯一主结果与代码基线。

| 方法 | 总体 `score_task` | `niche` | `multi_hop` | `scope_collection` | `score_evidence` |
| --- | ---: | ---: | ---: | ---: | ---: |
| Gold | 0.425 | 0.765 | 0.118 | 0.392 | 0.610 |
| TreeRAG | 0.398 | 0.765 | 0.078 | 0.351 | 0.614 |
| Flat | 0.360 | 0.424 | 0.078 | 0.578 | 0.591 |

结果文件：

- `results/fair_clean_gold_flat_fair_clean_scopefix_v2_b500.json`
- `results/fair_clean_treerag_fair_clean_scopefix_v2_b500.json`
- 摘要：`results/summary.md`

协议要点（修正后）：

- 三方共享：任务集、b500 evidence 预算、方法无关 `[E1]/[E2]` header、compose、Inspect judge
- 无 `PATH:` 行；无导航后 `soft_safety` 注入
- Gold / Flat / TreeRAG 共用 `src/realdata/agent_delivery/` 的 budget fill、compose、judge
- Scope 金标与判分已修复（`bin/23_repair_scope_tasks.py`、`inspect_scoring.py`）

### 0.3 已落地的 Fix（Phase 1）

旧版 `UNIFIED_FIX_PLAN` 中的三大 Fix 在代码层面已落地一版，但效果未完全达到旧计划预期：

| Fix | 内容 | 落地状态 | 效果 |
| --- | --- | --- | --- |
| Fix 1 | 证据组装：去 `PATH:` 重复、精简上下文 `[§ ...]`、方法无关 `[E1]/[E2]` header | 已落地（`tool_space.py`、`budget_eval.py`） | `niche` 已强；`scope` / `multi` 仍弱 |
| Fix 2 | Agent State + 增强 Observation + `FINISH` 规则 | 已落地（`nav_policy.py`、`nav_projection.py`） | 自主 `FINISH` 有提升；`collect` 浪费步仍约 65% |
| Fix 3 | 前置 hybrid discovery → D* `COLLECT`；删后置 `soft_safety`；Emergency Guard | 已落地（`nav_agent.py`、`nav_actions.py`、`nav_discovery.py`） | D* 仅 15 次被选用；Emergency Guard 0 触发 |

协议测试：`python3 tests/test_protocol.py -q` 通过 11 个测试。文档中的 `python3 -m unittest tests.test_protocol -q` 在当前环境导入失败（`tests` 非可导入包）。

## 1. 当前能说什么、不能说什么

### 1.1 Bootstrap CI 的含义

Bootstrap CI 是用「对 51 道题反复重采样」来估计方法差值的不确定区间。

当前逐题 bootstrap 95% CI：

- Gold − TreeRAG：`[-0.090, 0.148]`
- Gold − Flat：`[-0.070, 0.203]`
- TreeRAG − Flat：`[-0.097, 0.175]`

「CI 大幅重叠」指：这些区间都跨过 0。虽然均值是 Gold `0.425` > TreeRAG `0.398` > Flat `0.360`，但重采样后有相当多可能样本会让差值变成负数，即「另一个方法反超」。

为什么不能严谨说「Gold 总体显著优于 TreeRAG/Flat」：

- Gold 比 TreeRAG 只高 `0.027`，但 CI 是 `[-0.090, 0.148]`，不确定性远大于观测差值。
- 51 题样本不足以排除随机题目组成带来的波动。
- 只能说：当前样本均值上 Gold 最高，但总体优势还不稳定。

### 1.2 与旧 `[REVIEW] current status.md` 的关系

旧 Review 的大叙事仍可保留：

- arXiv 作为 retrieval validation
- RealData 作为 agent-like harness validation

但 RealData 部分需更新：

- 当前 canonical 是 51 题、Gold / Flat / TreeRAG，不是旧文档里的 97 题 Gold/Pred/Flat
- 没有 Pred arm，不能用这批 RealData 结果支撑「predicted native hierarchy 可部署收益」
- arXiv 800 六臂结果（Gold/Pred/Flat/RAPTOR/LlamaIndex/TreeRAG）仍可作为论文 retrieval 层证据，与 fair_clean 51 题是不同实验

### 1.3 当前结论定位

方向还没被证伪，反而暴露了下一步该补的 agent 能力；但这版不能声称「方案已经充分落地并显著优于 baseline」。

## 2. 已落地 vs 未充分落地的 feature

### 2.1 代码上已落地、但能力未达标的项

| 项 | 现状 | 目标（旧计划） | 差距 |
| --- | --- | --- | --- |
| `collect` 浪费步 | 约 65.2%（101/155 次 `n_added=0`） | <25% | 未达标 |
| 自主 `FINISH` | 39/51 题 | >50% | 部分达标 |
| D* discovery 利用 | 15 次 D* `collect` | 导航中主动选用 | 利用率低 |
| `multi_hop score_task` | 0.118 | 0.30+（旧预期） | 远未达标 |
| `scope_collection` | Gold 0.392，Flat 0.578 | 接近或超过 Flat | Flat 反而更高 |

### 2.2 尚未充分落地的关键 feature

- `multi-hop` 专用策略
  - 现在只有 compose prompt 约束（`fact_1` / `fact_2` 覆盖两跳）
  - 导航层无 query decomposition、分跳收集、证据分组
  - `multi_hop` Gold 仅 `0.118`
- `scope_collection` 的 broader-scope / sibling expansion
  - Gold nav 对集合型任务仍偏局部
  - Flat 在 scope 上最高（`0.578`）
  - 需要主动展开同级条目、上层范围、列表式证据，而非只收 top-k leaf/path
- D discovery 已有，但 agent 未充分学会使用*
  - discovery 已从「后置注入」变为「agent 可选动作」
  - 实际 D* `collect` 仅 15 次
- Agent State 落地了，但重复/空 `collect` 未解决
  - prompt 告知「不要重复收集」不够
  - C*/E* 无 covered 硬过滤（仅 D* 有 `collected_sids` 过滤）
- RealData 无 Pred arm
  - 论文「predicted native hierarchy 可部署」在 RealData canonical 中无对应
- 无 outline 两段式收集
  - KNOWHERE 有 outline collect → full collect 流程
  - 当前只有「全量子树」一种收集模式

## 3. KNOWHERE 导航机制对照

### 3.1 KNOWHERE 架构概览

KNOWHERE agentic 检索三阶段（`orchestrator.py`）：

- Phase 1：Document selection（`bottom_discovery` + `kg_document_select`）
- Phase 2：Per-document navigation（iterative BFS via `navigate_step`）
- Phase 3：Render evidence text

`knowledge_map`（`knowledge_map.py`）：语料库级文档概览，供 Phase 1 选文件，不参与 in-doc 导航。

文档内 outline：来自 `DocumentSection` 表（`section_tree.py`），经 `load_child_sections` 投影到当前 scope，作为 LLM 的 Actionable Observation。

### 3.2 KNOWHERE 如何处理集合型/范围型查询

结论：没有专门的 `"COLLECTION"` query intent，也没有自动 sibling expansion。

机制是：

- `COLLECT` 语义 = section + 全部后代（`prompts.py` L63–66；hydration 对 `path` 做 `LIKE 'path / %'`）
- outline 模式：`hydrate_mode=outline` 只收 `title+summary`，不算 covered，可继续 drill
- Sibling 不会自动展开：LLM 需一步内多个 `COLLECT`、`COLLECT` 共同父节点、`EXPAND` 进父 scope、或 `BACK` 换分支
- 父节点 full collect 后 sibling 从 action 中消失（`PathLedger.is_covered` 硬过滤）

### 3.3 KNOWHERE Query Intent 分类

六类（`prompts.py` L105–118）：

- `MACRO_SUMMARY`
- `STRUCTURE_OVERVIEW`
- `FACTUAL_DETAIL`
- `NUMERIC_DETAIL`
- `ASSET_LOOKUP`
- `UNKNOWN`

Intent 不进入 `build_legal_actions` 的打分/过滤，只传入 agent state 和 observation。Legal action 由 visible items + discovery + budget + collected/rejected 状态决定。

### 3.4 KNOWHERE 如何避免重复收集、空收集

| 机制 | 行为 |
| --- | --- |
| `PathLedger.is_covered` | 已 full-collect 的路径及后代不再出现 `COLLECT`/`EXPAND` |
| outline 可 upgrade | 已 outline 的路径仍可 `COLLECT` 升级为 full |
| `rejected_paths` | 低价值 scope 禁止 `EXPAND`，除非有 discovery 信号 |
| `rejected_collect_paths` | 工具 reconciliation 拒绝的 collect 永久硬过滤 |
| `doc_exclude` | full collect 后子树从 observation 消失 |
| 空 `SEARCH` 阻断 | 当前 scope 搜 asset 无结果则 block 该 asset 类型 |

### 3.5 KNOWHERE Discovery 传播

- Phase 1：path/content/term 三通道 BM25 → RRF → `discovery_score`
- 导航中 ancestor 衰减 `0.9`、descendant 衰减 `0.65`（`actions.py` L614–627）
- 树外 discovery 生成 D `COLLECT*`（`actions.py` L156–184）
- Rejected path 有 discovery 信号时可复活 `EXPAND`

### 3.6 KNOWHERE FINISH / 终止

- 无自动 coverage 推断，`"FINISH only when collected evidence is sufficient"`
- 系统硬终止：`max_steps`、`latency_budget`、planning `EXHAUSTED`、error
- forced exit + 空 collect：auto-collect visible leaves（兜底）

### 3.7 KNOWHERE Multi-hop

agentic 导航模块内没有 query 分解。Multi-hop 近似能力：`BACK` 换 scope、多文档顺序导航。Query 分解在 workflow 层（`retrieval/workflow/planner.py`），不在 agentic 内。

### 3.8 与 hierarchy-as-harness 的关键差异

| 维度 | KNOWHERE | hierarchy-as-harness（当前） |
| --- | --- | --- |
| `knowledge_map` | 仅选文件 | 无（`pool_mode=none` 给定 `doc_id`） |
| in-doc outline | `section_tree` + outline collect | 无 outline 模式 |
| `COLLECT` 语义 | section + 全部后代 | section 子树 leaf/path chunks |
| 去重 | `PathLedger.is_covered` 硬过滤 | 仅 D* 有 `collected_sids`；C*/E* 无 |
| Discovery | 加分 rerank + D* action | 已有 D*，利用率低 |
| Query intent | 六类，prompt 软引导 | 用 `task_type`（`niche`/`multi`/`scope`） |
| `FINISH` | 纯 LLM 决策 | 纯 LLM 决策 + prompt 步数预警 |
| Multi-hop 分解 | workflow 层 | 无 |

## 4. Scope Collection 深度分析

### 4.1 对早期分析的纠正

纠正 1：scope 的头号问题不是「gold 进不了动作空间」

早期用「gold 叶子行号 == 被 offer 的 `section_id`」精确匹配，得出「3/17 gold 曾进入 C*/E*」。这是测错了——`COLLECT` 父 section 会覆盖 gold 叶子，但父 `section_id` ≠ gold 叶子 `id`。

按行号邻近度重测后，17 题 scope 失败模式：

| 模式 | 数量 | 含义 | 代表 task |
| --- | --- | --- | --- |
| HIT | 7/17 | 导航到位，coverage>0 | 38, 43, 44, 45, 47, 48, 51 |
| NEAR | 5/17 | 导航到正确章节附近（`mindist≤2`），gold 被预算/打分挤出 | 35, 36, 37, 49, 50 |
| FAR | 5/17 | 导航未到达 gold 区域（`mindist 8–29`） | 39, 40, 41, 42, 46 |

结论：scope 不是单一「召回」问题，而是**召回（FAR）+ 预算粒度（NEAR）**各占约一半。

纠正 2：scope collect 按行序打分是 NEAR 失败的直接机制

`nav_agent.py` 中 scope 分支：

```python
if task_type in {"scope_collection", "regulatory_coverage"}:
    ordered = sorted(pool, key=lambda c: (min(c.line_ids or (10**9,)), c.node_id))
    limit = min(len(ordered), int(config.collect_k))
    base = float(config.read_score_bonus) + float(action.score or 0.0)
    return [
        (chunk, base + (limit - rank) * 0.001)
        for rank, chunk in enumerate(ordered[:limit])
    ]
```

当 agent 收「一整章」（如 Task 35 收 `L39` 整章 59 块），共享 budget fill 从章节最前面开始塞满 500 字，gold 子条目在章节中后段（`L83/84`、`L94–99`）被挤出 → `coverage=0`。

这比 header 重复/`PATH` 行更致命，且 Fix1 未覆盖。

纠正 3：祖先衰减 `0.55` 对 NEAR 可能反作用

`nav_discovery.py` 中 scope 用 `NAV_DISCOVERY_SCOPE_ANCESTOR_DECAY=0.55`（默认 `0.90`）。

NEAR 5 题说明 agent 能到达正确章节（甚至收了整章），问题是收得太宽。提高祖先分、把更大范围父 section 顶上来，对 NEAR 是反作用。祖先衰减调整只对 FAR 有意义，对 NEAR 需配合 A1（查询相关优先）而非单纯放宽。

### 4.2 典型失败轨迹

Task 35（NEAR，`cov=0`）：

- `query`：列举事故隐患分类及其具体含义
- `gold_nodes`：`L83, L84`
- 轨迹：`expand L113` → `D1 collect L39（59 chunks）` → `back` → `expand L113` → `back` → `finish`
- `retrieved_nodes` 含 `L39, L81, L92…`，`mindist=2`，但 gold `L83/84` 未进最终 evidence
- evidence 来自 `L39` 子树前段（`2.4.4`、`2.5`、`2.2.1`、`2.1`…），非 gold 条目

Task 36（NEAR，`cov=0`）：

- `gold_nodes`：`L94–L99`
- 轨迹：6 次空 `search` → `C2 collect L1（1 chunk）` → `finish`
- `retrieved` 含 `L1, L39, L62…`，`mindist=1`，gold 被 budget 挤出

### 4.3 KNOWHERE outline 机制能否处理 scope？

能，但依赖两段式，不是自动 sibling expansion。

KNOWHERE 处理 collection 的核心是：

- outline collect：先只收标题/骨架，不算 covered，可继续 drill
- agent 看清范围后 full collect 命中的具体子 section
- 或 `COLLECT` 父节点 一次覆盖所有 sibling（子树语义）

当前仓库只有「全量子树」一种模式 → 要么收太宽（NEAR 被预算挤掉），要么没收到（FAR）。outline 两段式是最值得移植的 KNOWHERE 能力。

### 4.4 按题型的导航失败统计（Gold arm）

| 题型 | 自愿 `FINISH` | 空 `search` / 总 `search` | 零增 `collect` / 总 `collect` | gold 曾进入 C*/E* | gold 被直接 collect |
| --- | ---: | ---: | ---: | ---: | ---: |
| `scope_collection` | 14/17 | 29/37 | 28/51 | 3/17（精确匹配，低估） | 1/17 |
| `multi_hop` | 13/17 | 15/19 | 51/74 | 7/17 | 2/17 |
| `niche_fact` | 12/17 | 47/59 | 22/30 | 5/17 | 5/17 |

## 5. 问题优先级清单（按对分数的影响）

| 级别 | 问题 | 证据 | 影响面 |
| --- | --- | --- | --- |
| P0 | collection `collect` 太宽 + 按行序打分，gold 子条目被预算挤出 | scope NEAR 5/17，`cov=0` 但 `mindist≤2` | scope 最直接 |
| P0 | 导航召回不足，FAR 区域根本没到 | scope FAR 5/17（`mindist 8–29`） | scope、multi |
| P1 | 空/重复 `search` 刷步 | scope 空 `search` 29/37，niche 47/59 | 全类型效率 |
| P1 | 零增 `collect`（重复收已收 section，C*/E* 无 covered 过滤） | 全局 `collect` 空收 101/155 | 效率、轨迹质量 |
| P2 | 无 outline / intent 两段式收集 | 同 KNOWHERE 对照缺失 | scope、macro 型 |
| P3 | `multi_hop` 无分跳检索/分组 compose | multi 0.118 | multi（KNOWHERE 导航层也没有） |

## 6. 完整修改方案（分阶段）

总原则：

- 与 `UNIFIED_FIX_PLAN.zh-CN.md` 约束对齐：
- 守住共享输出预算协议：改动只影响 Gold 喂给共享 `budget_eval` 的候选 chunk 及其打分/导航行为；不改 `[E1]/[E2]` header、不改 compose、不改 judge、不给 Gold 专属最终注入
- 遵循「软导航提示、避免硬性 `FINISH` 门控」
- 每步可回退：环境变量开关包裹，便于消融

### 阶段 A（P0，收益最确定，改动最小）：collection 收集改为「查询相关优先」

#### A1 — scope collect 的「按行序打分」改为「查询相关度优先、同分保序」

- 目标：让 gold 命中的子条目在共享预算里活下来，而不是被章节开头挤掉
- 位置：`src/nav/nav_agent.py` 的 `_collect_subtree` scope 分支（约 L142–150）
- 做法：对 `pool` 先用 `idx.search(query, pool, ...)` 取相关度，`relevance` 作为主序、`line_id` 作为次序，再进预算
- 预期：直接救回 NEAR 5 题中的大部分
- 开关：`NAV_SCOPE_COLLECT_RELEVANCE_FIRST=1`（默认开，可关）

#### A2 — collection collect 增加「子 section 聚焦」上限

- 当一次 `collect` 的 `pool` 远超预算可容纳（如 59 块 vs 500 字），优先保留与 query 相关的「那一段连续子条目」，而非平铺整章
- A1 的补强

### 阶段 B（P0，针对 FAR 的召回）：让正确区域能被导航到

#### B1 — 命中叶子的祖先链注入可见树

- discovery 命中某 leaf 时，把其直接父 section 作为可 `EXPAND/COLLECT` 项注入 projection
- 位置：`src/nav/nav_projection.py` + `src/nav/nav_actions.py`
- 解决 FAR 区域「看不到」

#### B2 — scope 的 FAR/NEAR 分流（谨慎、可灰度）

- 祖先衰减只对「尚未到达任何相关区域」时放宽（帮 FAR）
- 一旦已收到相关章节则收紧（保护 NEAR，避免越收越宽）
- 与 A1 交互，需灰度开关

### 阶段 C（P1，效率，纯软/弱硬规则）：压掉刷步

#### C1 — 空 search 软阻断

- 一次 `nav_search` 的 `n_added=0` 后，在 Agent State 标注「search 已穷尽」，并在该 scope 下从 legal actions 移除 `S1`
- 位置：`src/nav/nav_agent.py` + `src/nav/nav_actions.py`

#### C2 — 已 full-collect 的 section 从 C*/E* 过滤（轻量 PathLedger）

- 当前 C*/E* 不排除已收集 section（`nav_actions.py` L53–70）
- 将 D* 已有的 `collected_sids` 过滤（L45–49、L94）推广到 C*/E*
- 防护：过滤后动作集为空则保留原项（不强制 `FINISH`）

### 阶段 D（P2，结构性、改动较大）：引入 outline 两段式收集

#### D1 — 给 scope/regulatory 增加 outline collect 动作

- 只收 section 标题 + 条目骨架进 evidence（不算 covered，可继续 drill）
- agent 先看清范围，再 full-collect 命中的具体子 section
- 对齐 KNOWHERE collection 能力核心
- 需扩 `_materialize_leaf_path_chunks` 与 action 语义
- fairness：outline 只影响 Gold 导航中间态，最终 evidence 仍走共享预算与 `[E1]/[E2]`

### 阶段 E（P3，单列，架构选择）：multi_hop

- 不建议现在塞进导航层（KNOWHERE 的 query 分解也在 workflow 层）
- 建议独立实验：compose 阶段按 hop 分组 + 两跳证据各留预算配额
- 先不纳入本轮

## 7. 可落地 vs 落地程度不够的 KNOWHERE 能力对照

| KNOWHERE 能力 | 当前落地程度 | 建议 |
| --- | --- | --- |
| Agent State Block | 已落地 | 维持 |
| 增强 Observation（chunk count、Leaf 标记） | 已落地 | 维持 |
| D* discovery `COLLECT` | 已落地，利用率低 | C2 + B1 提升 |
| `PathLedger.is_covered` 硬过滤 | 未落地 | C2 优先落地 |
| outline collect → full collect | 未落地 | D1 阶段 D |
| Query intent 六类 | 用 `task_type` 替代 | 可选：scope 时 prompt 强化 outline 偏好 |
| `rejected_paths` / `doc_exclude` | 未落地 | C2 轻量版 |
| forced exit auto-collect visible leaves | Emergency Guard 仅 `collected=空` | 维持（0 触发说明导航通常有收集） |
| `knowledge_map` 选文件 | N/A（fair_clean 给定 `doc_id`） | 不适用 |
| workflow 层 query 分解 | 未落地 | 阶段 E 单列 |

## 8. 预期效果（若 feature 充分落地）

| 题型 | 当前 | 合理预期 | 前提 |
| --- | --- | --- | --- |
| `niche_fact` | Gold/TreeRAG 0.765 | 稳定或略升 | A/C 减浪费，不拖累 |
| `multi_hop` | 0.118 | 0.20–0.35 | 分跳检索 + 分组 compose（阶段 E） |
| `scope_collection` | Gold 0.392，Flat 0.578 | 接近或超过 TreeRAG，缩小与 Flat 差距 | A1+A2+B1，必要时 D1 |

注意：51 题 bootstrap CI 仍宽，单项改进需同时看 `evidence_coverage` 和 HIT/NEAR/FAR 分类转化，不能只看总分波动。

## 9. 建议执行顺序与风险

### 9.1 执行顺序

第一步：阶段 A1 + C1 + C2

- 改动小、风险低、收益直接（NEAR 5 题 + 全类型刷步）
- 复跑 51 题，看 scope 是否从 `0.392` 回升、`collect` 空收/空 `search` 是否下降

第二步：阶段 B1（+ 可选 B2 灰度）

- 针对 FAR 5 题

第三步：评估是否做 D1（outline）

- 若 A/B 后 scope 仍明显落后 Flat（`0.578`），再投入 outline 两段式

第四步（独立）：阶段 E `multi_hop`

- 不纳入本轮导航改动

### 9.2 复跑命令

```bash
bash bin/32_run_quality_balanced_gold_flat.sh   # Gold + Flat
bash bin/35_run_quality_balanced60_treerag.sh   # TreeRAG
bash bin/21_compare_realdata_baselines.sh       # 对比表
python3 tests/test_protocol.py -q               # 协议单测
```

### 9.3 验证清单

> **历史记录**：下列 ac_v1 条目保留作对照；当前 canonical 为 **goldnav_e2_v1**（§11.4–11.8）。

#### ac_v1（2026-06-23，未晋升）

- [x] A1/C1/C2 已实现且可 env 回退
- [ ] scope NEAR 35/36/37 提升，49/50 仍为 0
- [ ] scope task 降至 `0.284`（相对 scopefix_v2 `0.392` 回退）
- [x] 零增 collect 41.5%；重复空 search 0

#### v4 + E2 canonical（2026-06-24，已晋升 goldnav_e2_v1）

- [x] Nav 单测 23 个、协议单测 14 个全部通过（Desktop 主仓库已合入）
- [x] scope Gold task `0.392 → 0.530`（v4/E2 同值）；原 HIT 38/45/47/48 保持 `1.0`
- [x] 零增 collect `15/89（16.9%）`；重复空 search `0`；process efficiency `0.639`
- [x] niche `0.824`；multi E2 后 `0.157`（>0.118 门槛）
- [x] 三方 E2 同协议：Gold `0.504` / TreeRAG `0.433` / Flat `0.354`
- [x] Gold−Flat bootstrap CI 不跨 0；Gold−TreeRAG CI 仍跨 0
- [x] scope 17 题 HIT/NEAR/FAR 重分类（E2）：HIT 10 / NEAR 7 / FAR 0（见 `results/scope_hit_near_far_e2_v1.md`）
- [ ] scope 仍低于同轮 Flat `0.572`（limitation，非回归）
- [ ] D1 outline 未做；B1/E1 定向无收益

阶段 B 验证

- [x] B1 discovery bridge 定向无收益（默认关）
- [ ] 独立 B2 灰度未做

阶段 D 验证（未做，future work）

- [ ] scope 接近或超过 Flat `0.578`
- [x] 无 Gold 专属最终注入；fairness 协议测试通过

### 9.4 风险点

| 风险 | 说明 | 缓解 |
| --- | --- | --- |
| 公平性回归 | 改动限制在候选生成/排序与导航动作集 | 不改 budget fill header、compose、judge |
| niche 被拖累 | A1 只改 scope 分支 | 开关 + 消融 |
| B2 与 A1 交互 | 祖先衰减放宽可能加剧 NEAR | B2 灰度、NEAR 时收紧 |
| 51 题 CI 仍宽 | 总体优劣仍可能无法稳定区分 | 分项（scope/multi/niche）+ HIT/NEAR/FAR |

## 10. 代码索引

| 模块 | 路径 |
| --- | --- |
| Gold Nav 主循环 | `src/nav/nav_agent.py` |
| Legal actions | `src/nav/nav_actions.py` |
| Agent State / prompt | `src/nav/nav_policy.py` |
| Observation projection | `src/nav/nav_projection.py` |
| Discovery | `src/nav/nav_discovery.py` |
| Evidence 物化 | `src/realdata/agent_delivery/code/tool_space.py` |
| Budget fill | `src/realdata/agent_delivery/code/budget_eval.py` |
| Inspect 判分 | `src/realdata/agent_delivery/code/inspect_scoring.py` |
| Scope 金标修复 | `bin/23_repair_scope_tasks.py` |
| 协议测试 | `tests/test_protocol.py` |
| KNOWHERE 参考 | `/Users/wuchengke/Desktop/knowhere/knowhereapi-main/packages/shared-python/shared/services/retrieval/agentic/` |

## 11. 文档状态

- 本文档整合本对话全部分析，不缩减内容
- 与 `[REVIEW] current status.md`（论文叙事）、`UNIFIED_FIX_PLAN.zh-CN.md`（canonical 协议）并列，本文档专注 Gold Nav 问题诊断与改进路线
- 后续执行以本文档阶段 A→B→D 顺序为准；每阶段完成后更新 `results/summary.md` 与验证清单

### 11.1 阶段 A1 + C1 + C2 执行记录（2026-06-23）

- A1：scope collect 改为相关度主序、行号次序；`NAV_SCOPE_COLLECT_RELEVANCE_FIRST=1` 默认开启
- C1：`n_added=0` 的 search 按 scope 记为穷尽，并隐藏当前 scope 的 `S1`；`NAV_BLOCK_EXHAUSTED_SEARCH=1` 默认开启
- C2：成功 collect 的精确 section ID 从 C*/E*/D* 候选中过滤；全过滤时恢复原 C*/E* 候选，避免动作过滤强制 `FINISH`；`NAV_FILTER_COLLECTED_SECTIONS=1` 默认开启
- checkpoint signature 已包含三个开关与 `goldnav_ac_v1` 行为协议，避免错误复用旧轨迹
- 本地验证：`python3 tests/test_nav_improvements.py -q` 通过 10 个测试；`python3 tests/test_protocol.py -q` 通过 11 个测试；完整 discovery 共 21 个测试通过
- 计划结果标签：`fair_clean_goldnav_ac_v1`
- 51 题复跑已完成，结果：`results/fair_clean_gold_flat_fair_clean_goldnav_ac_v1_b500.json`
- Gold 总体 `score_task`：`0.425 → 0.395`；`score_evidence`：`0.609 → 0.546`；不晋升 canonical
- 分项：niche `0.765 → 0.824`，multi `0.118 → 0.078`，scope `0.392 → 0.284`
- 效率：平均轨迹 `7.745 → 6.745`，process efficiency `0.521 → 0.605`
- 全局零增 collect：`101/155（65.2%）→ 51/123（41.5%）`；空 search：`91/115 → 32/58`；同 scope 重复空 search：`68 → 0`
- 自主 `FINISH`：`39/51 → 42/51`；D* collect：`15 → 21`
- NEAR 五题：Task 35 coverage `0 → 0.5`，36 `0 → 0.167`，37 `0 → 0.667`；49/50 仍为 0
- FAR 中 39/40/41/46 coverage 提升，但原 HIT 题 38/45/47/48 从正 coverage 回退到 0，抵消新增收益
- 回退机制：38/47 在正确 subtree 内被相关度重排挤出 gold；45/48 在首次正确 collect 后继续收宽 section，后续高分候选覆盖先前证据
- 对比表：`cache/compare_fair_clean_goldnav_ac_v1.md`；canonical `scopefix_v2` 未改动

### 11.2 根据 v1 结果修订的下一步（goldnav_ac_v2）

v1 证明 C1 有稳定收益，但纯相关度重排会破坏原 HIT，精确 section 过滤也不足以阻止后续宽 collect 覆盖正确证据。因此执行顺序修订为：

1. 保留 C1：继续按 scope 阻断 `n_added=0` 的重复 search。
2. 升级 C2：任何成功 collect 都阻断其祖先的宽范围 COLLECT；仅当 subtree 的全部物化 chunk 已进入状态时，才把自身及后代标为 covered 并移除 C*/E*/D*。
3. 重做 A1/A2：小 subtree 保持旧行序；大 subtree 先定位最高相关 anchor，再截取其附近固定长度的连续窗口，窗口内部保持行序。
4. 不再恢复已收集候选作为非 FINISH 防护；保留 SEARCH、BACK、EXPAND ancestor 和 FINISH 即可。
5. 使用独立标签 `fair_clean_goldnav_ac_v2` 复跑 51 题；只有同时满足“原 HIT 38/45/47/48 不回退、NEAR 至少保留 v1 收益、scope 不低于 0.392”才考虑进入 B1。

v2 开关与默认值：

- `NAV_SCOPE_COLLECT_STRATEGY=local_band`
- `NAV_SCOPE_LOCAL_BAND_MIN_POOL=20`
- `NAV_SCOPE_LOCAL_BAND_K=8`
- `NAV_SCOPE_LOCAL_BAND_CONTEXT_BEFORE=1`
- `NAV_BLOCK_EXHAUSTED_SEARCH=1`
- `NAV_FILTER_COLLECTED_SECTIONS=1`

### 11.3 v2 结果与 v3 收口修订

v2 结果：总体 task `0.445`、scope `0.412`、evidence `0.634`、process efficiency `0.636`，均高于 `scopefix_v2` 对应的 `0.425 / 0.392 / 0.609 / 0.521`。零增 collect 降至 `15/90（16.7%）`，重复空 search 保持 0。

但关键题检查未完全通过：38/48 恢复，45/47 仍回退。轨迹显示两种边界：

- 45：L144 已完整命中，但结构 parent chain 未把后续宽节点 L1 识别为祖先，导致宽 collect 冲掉证据。
- 47：先 collect 的 L198 是单 leaf；禁止其父节 L193 collect 后，agent 逐 leaf 消耗步骤并在 L199/L200 前结束。

因此 v3 只收紧覆盖规则，不改 local-band 参数：用 subtree 区间补充祖先识别；仅当成功 collect 的 section 含多个物化 chunk 时锁祖先，单 leaf collect 保留父节汇总动作。v3 继续以“38/45/47/48 全部不回退”为晋升条件。

### 11.4 targeted v3 结果与 v4 证据保护

45/47 targeted run 证明 v3 已恢复 47 的父节 L193 collect，但两题最终 evidence 仍被后续 discovery L1 覆盖。原因是 D* 的导航 action score（约 18）被直接加入 evidence score，错误地压倒先前完整命中的局部 section。

v4 将导航分与证据分解耦：scope evidence 最多继承 1.0 action score；完整收集一个多-chunk section 后设置 evidence lock，后续 collect 的 evidence score 软降 2.0。该规则不禁止继续导航或收集，只保护已经完整命中的局部证据不被宽 discovery 候选挤出预算。

v4 全量结果：

- 结果文件：`results/fair_clean_gold_flat_fair_clean_goldnav_ac_v4_b500.json`
- Gold 总体 task `0.477`，高于 canonical `0.425`；evidence `0.673`，高于 `0.609`
- 分项：niche `0.824`、multi `0.078`、scope `0.530`；scope 高于旧 Gold `0.392`，但仍略低于同轮 Flat `0.572`
- process efficiency `0.639`，平均轨迹 `6.333`；canonical 分别为 `0.521 / 7.745`
- 零增 collect `15/89（16.9%）`，达到 <25% 目标；重复空 search 保持 `0`
- 自主 FINISH `47/51`；D* collect `21`
- NEAR：35 `0→0.5`、36 `0→0.667`、37 `0→0.167`、50 `0→0.5`；49 仍为 0
- 原 HIT 38/45/47/48 均保持 coverage/task `1.0`
- v4 Gold − 同轮 Flat：均值 `+0.123`，paired bootstrap 95% CI `[+0.006, +0.246]`
- v4 Gold − canonical TreeRAG：均值 `+0.079`，paired bootstrap 95% CI `[-0.036, +0.200]`，仍不能声称稳定优于 TreeRAG
- 正式对比：`cache/compare_fair_clean_goldnav_ac_v4.md`

阶段结论：A/C 修复已达到预设门槛。下一步可进入 B1，但应继续使用独立候选标签；`scopefix_v2` 在明确执行 canonical 晋升前保持不变。

### 11.5 B1 discovery bridge 定向结果（2026-06-24）

B1 以 `NAV_DISCOVERY_SCOPE_BRIDGE=1` 实现：discovery 命中后，将最近可展开祖先作为 `G* EXPAND` 合法动作，不自动 collect，不写入 evidence。

- 定向题：scope 38–49（FAR/零覆盖 + HIT 回归）
- 结果：12 题 `score_task` 和 `evidence_coverage` 与 v4 逐题完全一致
- `G1` 在前 5 题被 agent 实际选择，证明失败不是“动作未暴露”，而是 bridge 只替代了原有路径，没有改变最终证据
- 结论：不跑 51 题全量，不晋升；代码保留作消融，默认 `NAV_DISCOVERY_SCOPE_BRIDGE=0`
- 结果：`results/fair_clean_gold_flat_fair_clean_goldnav_b1_v1_target_b500.json`

### 11.6 阶段 E1 hop-anchor compose 定向结果（2026-06-24）

E1 以 `MULTIHOP_COMPOSE_HOP_ALIGNMENT=1` 将 query 中的两个层级位置按顺序绑定到 `fact_1` / `fact_2`，并要求保留条件、例外、数字和后续处置。该 compose 逻辑对 Gold / Flat 共享。

- 17 题 Gold multi-hop：`0.0784 → 0.0784`，无净收益
- 逐题：`q400_multi_0029` 从 `0 → 0.3333`，`q400_multi_0009` 从 `0.3333 → 0`，相互抵消
- Flat multi-hop：`0.020 → 0.0588`，Gold 相对优势反而缩小
- 结论：prompt-only hop 对齐不足以解决证据错配；保留消融开关，默认 `MULTIHOP_COMPOSE_HOP_ALIGNMENT=0`
- 结果：`results/fair_clean_gold_flat_fair_clean_goldnav_e_v1_target_b500.json`

### 11.7 修订后的下一步：E2 hop-aware evidence allocation

1. 从 query 提取两个层级锚点，在共享 budget fill 前将候选 chunk 分为 hop-1、hop-2、unassigned 三组。
2. b500 为 hop-1 / hop-2 各保留最小配额，剩余预算再按原分数竞争；不改 evidence header、compose schema 或 judge。
3. 对 Gold / Flat / TreeRAG 使用同一分组与配额函数，保持 fairness。
4. 先定向验证 evidence coverage 已高但内容错配的 26–29/31，再验证低召回的 18–23/30/34。
5. 晋升门槛：Gold multi-hop `>0.118`，且不得使 scope/niche 或原 HIT 回退；否则保持 v4 为推荐候选。

### 11.8 E2 实现状态（2026-06-24）

E2 已在共享 `budget_eval.evaluate_at_budget` 中实现，不改 evidence header、compose schema 或 judge：

- 开关：`MULTIHOP_EVIDENCE_ALLOCATION=1`（默认 `0`）
- 每跳最小保留上限：`MULTIHOP_EVIDENCE_MIN_CHARS_PER_HOP=180`
- 分组：从 query 的两个层级引号片段提取 hop anchor；父子 anchor 同时命中时，归入更具体的子 anchor
- 配额：先为两个可区分 hop 各保留候选证据，超长 chunk 在各自配额内截断，剩余 b500 再按原分数竞争
- 公平性：Gold Nav、Flat、TreeRAG 均传入同一 `query/task_type` 并使用同一共享函数
- checkpoint 签名已纳入 E2 开关与配额，不会误复用 v4/E1 结果
- 测试：`python3 tests/test_protocol.py -q` 14/14；`python3 tests/test_nav_improvements.py -q` 23/23

评测结果：

- 17 题定向：Gold multi-hop `0.0784 → 0.1569`，evidence coverage `0.4755 → 0.5196`，越过 `>0.118` 门槛；Flat task `0.0196` 不变
- 51 题全量：Gold 总体 `0.4774 → 0.5035`，evidence `0.6732 → 0.6879`
- Gold 分项：niche `0.8235` 不变，multi-hop `0.1569`，scope `0.5301` 不变，无 niche/scope 回退
- 同轮 Flat 总体 `0.3542`；Gold − Flat 总体差值由 v4 的 `+0.1232` 扩大为 `+0.1493`
- 结果：`results/fair_clean_gold_flat_fair_clean_goldnav_e2_v1_target_b500.json` 与 `results/fair_clean_gold_flat_fair_clean_goldnav_e2_v1_b500.json`

TreeRAG 同协议复跑：

- TreeRAG 总体 `0.4334`；niche `0.8235`、multi-hop `0.0980`、scope `0.3786`，evidence `0.6229`
- 三方总体：Gold `0.5035` > TreeRAG `0.4334` > Flat `0.3542`
- paired bootstrap 95% CI：Gold−TreeRAG `[-0.0462, 0.1880]`，Gold−Flat `[0.0266, 0.2758]`，TreeRAG−Flat `[-0.0467, 0.2079]`
- 结论：Gold 对 Flat 的优势在当前 51 题上不再跨 0；Gold 对 TreeRAG 仍只能说均值更高，不能声称稳定显著优于
- 结果：`results/fair_clean_treerag_fair_clean_goldnav_e2_v1_b500.json`；对比：`cache/compare_fair_clean_goldnav_e2_v1.md`

API 配置已固定保存到 `~/.config/realdata_treerag/llm_api.env`（权限 `600`），当前 worktree 的标准路径使用被 Git 忽略的符号链接。`llm_config.py` 会优先加载用户级配置，后续新 worktree 无需再复制密钥。
