# fair_clean 共享输出预算协议（canonical）

> **版本**：`fair_clean_goldnav_e2_v1` · b500 · 51 题
> **状态**：当前唯一主结果与代码基线

---

## 1. 实验在比什么

在 **同一任务集、同一 evidence 字符预算、同一 compose / Inspect judge** 下，比较三种检索方式谁能更好地支撑最终答题：

| 方法 | 检索 |
|------|------|
| **Gold** | LLM Nav Agent + hybrid discovery（D*） |
| **Flat** | flat_react 多轮 dense |
| **TreeRAG** | LLM 建树 + intent + BTR |

这是**共享输出预算协议**，不是等计算量协议：各方法保留自身的检索轮数、候选上限、建树与 LLM 成本。

---

## 2. 协议要点（修正后）

### 2.1 Evidence 呈现

- 三方使用 **方法无关** header：`[E1]`、`[E2]`…（`method_neutral_ordinal_v1`）
- 无 `PATH:` 行；无导航后 soft_safety 注入
- Gold / Flat / TreeRAG 共用 `src/realdata/agent_delivery/` 的 budget fill、compose、judge

### 2.2 Scope 任务与判分

- 17 道 scope 题的 `gold_nodes`、Inspect `gold_line_ids` 与 latest-clean corpus 对齐（`bin/23_repair_scope_tasks.py`）
- 判分使用 `target.table` 逻辑条目 + items 一对一模糊匹配（`inspect_scoring.py`），不用整段 JSON 字符串当 gold

### 2.3 Gold Nav（Phase1，仍生效）

- Agent State + 增强 Observation
- 前置 hybrid discovery → D* COLLECT
- Emergency Guard（collected 为空时，当前 0 触发）

### 2.4 E2 multi-hop evidence allocation

- 从 query 的两个层级锚点对候选证据分组，b500 为每跳保留 180 字上限
- Gold / Flat / TreeRAG 共用同一 `evaluate_at_budget` 实现；不改 header、compose schema 或 judge
- 默认复跑脚本开启 `MULTIHOP_EVIDENCE_ALLOCATION=1`

---

## 3. 当前主结果（score_task_mean）

| 方法 | 总体 | niche | multi | scope |
|------|-----:|------:|------:|------:|
| **Gold** | **0.504** | **0.824** | **0.157** | 0.530 |
| **TreeRAG** | 0.433 | **0.824** | 0.098 | 0.379 |
| **Flat** | 0.354 | 0.471 | 0.020 | **0.572** |

逐题 paired bootstrap 95% CI：Gold−TreeRAG `[-0.046, 0.188]`（仍不能声称稳定优于 TreeRAG）；Gold−Flat `[0.027, 0.276]`。

**结果文件**

- `results/fair_clean_gold_flat_fair_clean_goldnav_e2_v1_b500.json`
- `results/fair_clean_treerag_fair_clean_goldnav_e2_v1_b500.json`
- 摘要：`results/summary.md`

---

## 4. 复跑

```bash
bash bin/32_run_quality_balanced_gold_flat.sh   # Gold + Flat，默认 tag=goldnav_e2_v1
bash bin/35_run_quality_balanced60_treerag.sh   # TreeRAG
bash bin/21_compare_realdata_baselines.sh       # 对比表 → cache/compare_fair_clean_goldnav_e2_v1.md
python3 tests/test_protocol.py -q               # 协议单测
bash bin/36_recompose_judge.sh                  # 重跑 compose+judge（保留 nav/evidence）
python3 bin/36_recompose_judge.py --judge-only  # 仅重判分（改 scope 金标/判分后）
```

Scope 金标修复（改 task 后执行一次）：

```bash
python3 bin/23_repair_scope_tasks.py
```

---

## 5. 已知短板（后续优化方向）

| 项 | 现状 |
|----|------|
| multi_hop task | 0.157，已改善但仍是最弱分项 |
| collect 零增率 | 16.9%，已达 <25% 目标 |
| scope | Gold 0.530，仍低于 Flat 0.572 |

优先方向：针对无法由层级锚点区分的同章相邻 multi-hop，以及 scope 49 的稳定召回；避免硬性 FINISH 门控。

---

## 6. 代码索引

| 模块 | 路径 |
|------|------|
| Evidence budget fill | `src/realdata/agent_delivery/code/budget_eval.py` |
| Inspect 判分 | `src/realdata/agent_delivery/code/inspect_scoring.py` |
| Scope 金标修复 | `bin/23_repair_scope_tasks.py` |
| 重判分 / 重 compose | `bin/36_recompose_judge.py` |
| Gold Nav | `src/nav/` |
| TreeRAG 适配 | `src/treerag/eval_arxiv_treerag.py` |
| 协议测试 | `tests/test_protocol.py` |
