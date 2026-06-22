# 公平协议实验结果摘要（fair_clean / b500）

最后更新：2026-06-22

> 在 fair_clean 51 题协议下，三方共享 b500 + 同一 compose/judge 流水线（TreeRAG 已与 Gold/Flat 同构 evidence header 与 compose 提示）。**Gold 与 TreeRAG 总体持平**（0.336 vs 0.338）；Gold 在 multi 上更好，TreeRAG 在 scope 上更好。

## 主表：score_task_mean（51 题，b500）

| 方法 | 总体 | niche_fact | multi_hop | scope_collection | evidence |
|------|-----:|-----------:|----------:|-----------------:|---------:|
| **TreeRAG** | **0.338** | 0.853 | 0.098 | **0.063** | 0.484 |
| **Gold（nav）** | 0.336 | **0.853** | **0.118** | 0.038 | **0.602** |
| Flat | 0.194 | 0.424 | 0.059 | 0.100 | 0.456 |

- Gold **> Flat（总体）**：0.336 vs 0.194。
- Gold **≈ TreeRAG（总体）**；multi 上 Gold 领先，scope 上 TreeRAG 领先。
- 无 `nav_soft_safety_collect`；无 PATH 泄漏；无按方法的候选上限（`TREERAG_FAIR_CAP=0`）。

## 公平协议

1. 三方共享 b500 字符预算，无按方法候选数截断。
2. 统一 `_prepare_compose_evidence_text` + `compose_llm` + `inspect_scoring` judge。
3. 任务 query 已删除字面层级路径；51 题（17/17/17）。日志：`results/task_clean_log.json`。

## Gold Nav（Unified Fix）

- **Fix 1**：证据组装去 PATH 重复、短 header `[L10]`。
- **Fix 2**：Agent State prompt + Observation 增强。
- **Fix 3**：循环前 discovery rerank；D* 动作；删 soft_safety；Emergency Guard（仅 collected 为空）。

## 结果文件

| 配置 | 路径 |
|------|------|
| Gold + Flat | `results/fair_clean_gold_flat_fair_clean_unified_v1_b500.json` |
| TreeRAG（同构 compose/evidence） | `results/fair_clean_treerag_fair_clean_unified_v2_b500.json` |
| 对比表 | `cache/compare_fair_clean_unified_v2.md` |
| 任务清洗日志 | `results/task_clean_log.json` |

复跑：`bash bin/32_run_quality_balanced_gold_flat.sh` + `bash bin/35_run_quality_balanced60_treerag.sh` + `bash bin/21_compare_realdata_baselines.sh`。
