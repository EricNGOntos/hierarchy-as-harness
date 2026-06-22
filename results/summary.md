# 共享输出预算实验结果摘要（fair_clean / b500）

最后更新：2026-06-22

> **Canonical（唯一主结果）**：`scopefix_v2` — 方法无关 `[E1]/[E2]` header + scope 金标/判分修复。Gold **0.425**、TreeRAG **0.398**、Flat **0.360**。

## 主表：score_task_mean（51 题，b500）

| 方法 | 总体 | niche | multi | scope | evidence |
|------|-----:|------:|------:|------:|---------:|
| **Gold** | **0.425** | **0.765** | **0.118** | 0.392 | 0.609 |
| **TreeRAG** | 0.398 | **0.765** | 0.078 | 0.351 | **0.614** |
| Flat | 0.360 | 0.424 | 0.078 | **0.578** | 0.592 |

逐题 bootstrap 95% CI：Gold−TreeRAG `[-0.090, 0.148]`；Gold−Flat `[-0.070, 0.203]`；TreeRAG−Flat `[-0.097, 0.175]`。

## 协议要点

- 三方共享：任务集、b500 evidence 预算、`[E1]/[E2]` header、compose、Inspect judge
- 检索/建树/导航成本各方法保留自身配置（共享输出预算，非等计算量）
- Scope 修复：`score_sample` 结构化对齐、`gold_nodes`/行号与 corpus 一致（`bin/23_repair_scope_tasks.py`）

## 结果文件

| 配置 | 路径 |
|------|------|
| Gold + Flat | `results/fair_clean_gold_flat_fair_clean_scopefix_v2_b500.json` |
| TreeRAG | `results/fair_clean_treerag_fair_clean_scopefix_v2_b500.json` |
| 对比表 | `cache/compare_fair_clean_final.md` |

复跑：`bash bin/32_run_quality_balanced_gold_flat.sh` · `bash bin/35_run_quality_balanced60_treerag.sh` · `bash bin/21_compare_realdata_baselines.sh`
