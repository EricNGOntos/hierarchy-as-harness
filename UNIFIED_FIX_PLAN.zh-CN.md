# fair_clean 共享输出预算协议（canonical）

> **版本**：`fair_clean_scopefix_v2` · b500 · 51 题  
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

### 2.2 Scope / Multi 任务与判分

- 17 道 scope：`gold_nodes`、Inspect `gold_line_ids` 与 corpus 对齐（`bin/23_repair_scope_tasks.py`）
- 17 道 multi_hop：两跳 gold 按 query 第一处/第二处 + corpus 行组重建（`bin/24_repair_multi_hop_tasks.py`）
- Scope 判分：`target.table` + items 一对一模糊匹配
- Multi M1 判分：fact_1/fact_2 允许顺序互换后取最优匹配（`inspect_scoring.py`）

### 2.3 Gold Nav（Phase1，仍生效）

- Agent State + 增强 Observation
- 前置 hybrid discovery → D* COLLECT
- Emergency Guard（collected 为空时，当前 0 触发）

---

## 3. 当前主结果（score_task_mean）

| 方法 | 总体 | niche | multi | scope |
|------|-----:|------:|------:|------:|
| **Gold** | **0.422** | 0.794 | 0.078 | 0.392 |
| **TreeRAG** | 0.398 | 0.765 | 0.078 | 0.351 |
| **Flat** | 0.373 | 0.482 | 0.059 | **0.578** |

逐题 bootstrap 95% CI：Gold−TreeRAG `[-0.090, 0.148]`（暂不能稳定区分总体优劣）。

**结果文件**

- `results/fair_clean_gold_flat_fair_clean_scopefix_v2_b500.json`
- `results/fair_clean_treerag_fair_clean_scopefix_v2_b500.json`
- 摘要：`results/summary.md`

---

## 4. 复跑

```bash
bash bin/32_run_quality_balanced_gold_flat.sh   # Gold + Flat，默认 tag=scopefix_v2
bash bin/35_run_quality_balanced60_treerag.sh   # TreeRAG
bash bin/21_compare_realdata_baselines.sh       # 对比表 → cache/compare_fair_clean_final.md
python3 -m unittest tests.test_protocol -q      # 协议单测
bash bin/36_recompose_judge.sh                  # 重跑 compose+judge（保留 nav/evidence）
python3 bin/36_recompose_judge.py --judge-only  # 仅重判分（改 gold/判分后）
```

Scope / Multi 金标修复（改 task 后执行一次）：

```bash
python3 bin/23_repair_scope_tasks.py
python3 bin/24_repair_multi_hop_tasks.py
```

---

## 5. 已知短板（后续优化方向）

| 项 | 现状 |
|----|------|
| multi_hop task | Gold **0.078**（17 题中 15 题 task&lt;0.5）；金标已修，主因见下节 |
| collect 浪费步 | ~66%，未达 &lt;25% 目标 |
| scope | Flat &gt; Gold；检索/compose 仍可优化 |

### multi_hop 诊断（scopefix_v2 · 金标修复 + 真实 evidence 判分后）

| 失败模式 | 题数 | 说明 |
|----------|-----:|------|
| 检索不足（ev &lt; 0.5） | 8 | 两跳 line 未收齐（如 0073 ev=0.22、0056 ev=0.25） |
| 检索够、compose 错配 | 7 | 两跳内容对错调或答非所问（如 0005 把 7.3/7.8 与 5.2.8 搞混） |
| 部分命中 | 1 | 0041 task=0.67（顺序无关匹配生效） |
| 正常 | 1 | 0009 task=0.33 |

**任务集（已修）**：原 17 题中有 **错位金标**（query 问 A/B 两节，gold 却来自其它条款，如 0073 问 6.10+第四章却标 4.4.x；0123 问 1.2+1.4 却标 1.3 适用范围；0005 hop2 误标 7.6 而非 7.3）。`bin/24` 已按 corpus 行组重建 fact_1/fact_2。

**仍低分原因**：修复金标后 multi 均值仍 ~0.078，说明瓶颈在 **nav 双 section 召回** 与 **compose 按 query 两位置对齐**，而非 scope 式「测错了」。evidence 分已从虚高 1.0 回落到 Gold multi **0.573**（真实检索覆盖率）。

优先方向：**multi 软导航（双 section collect）**、compose 强约束「第一处→fact_1」；避免硬性 FINISH 门控。

---

## 6. 代码索引

| 模块 | 路径 |
|------|------|
| Evidence budget fill | `src/realdata/agent_delivery/code/budget_eval.py` |
| Inspect 判分 | `src/realdata/agent_delivery/code/inspect_scoring.py` |
| Scope 金标修复 | `bin/23_repair_scope_tasks.py` |
| Multi 金标修复 | `bin/24_repair_multi_hop_tasks.py` |
| 重判分 / 重 compose | `bin/36_recompose_judge.py` |
| Gold Nav | `src/nav/` |
| TreeRAG 适配 | `src/treerag/eval_arxiv_treerag.py` |
| 协议测试 | `tests/test_protocol.py` |
