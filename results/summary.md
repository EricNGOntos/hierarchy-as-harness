# 共享输出预算实验结果摘要（fair_clean / b500）

最后更新：2026-06-22

> **Canonical（唯一主结果）**：`scopefix_v2` — 方法无关 `[E1]/[E2]` header + scope/multi 金标修复 + 真实 evidence 判分。Gold **0.422**、TreeRAG **0.398**、Flat **0.373**。

## 主表：score_task_mean（51 题，b500）

| 方法 | 总体 | niche | multi | scope | evidence |
|------|-----:|------:|------:|------:|---------:|
| **Gold** | **0.422** | **0.794** | 0.078 | 0.392 | 0.642 |
| **TreeRAG** | 0.398 | **0.765** | 0.078 | 0.351 | **0.614** |
| Flat | 0.373 | 0.482 | 0.059 | **0.578** | 0.615 |

逐题 bootstrap 95% CI（与 scopefix_v2 初版同量级）：Gold−TreeRAG `[-0.090, 0.148]`；Gold−Flat `[-0.070, 0.203]`；TreeRAG−Flat `[-0.097, 0.175]`。

## 协议要点

- 三方共享：任务集、b500 evidence 预算、`[E1]/[E2]` header、compose、Inspect judge
- 检索/建树/导航成本各方法保留自身配置（共享输出预算，非等计算量）
- Scope 修复：`bin/23_repair_scope_tasks.py` + 结构化 items 判分
- Multi 修复：`bin/24_repair_multi_hop_tasks.py`（17 题 gold 与 query 两跳位置 + corpus 行对齐）；M1 判分对 fact_1/fact_2 **顺序无关**最优匹配
- `bin/36_recompose_judge.py --judge-only`：仅重判分；evidence 从 `retrieved_nodes` 映射（不再误用 gold_line_ids）

## 结果文件

| 配置 | 路径 |
|------|------|
| Gold + Flat | `results/fair_clean_gold_flat_fair_clean_scopefix_v2_b500.json` |
| TreeRAG | `results/fair_clean_treerag_fair_clean_scopefix_v2_b500.json` |
| 对比表 | `cache/compare_fair_clean_final.md` |

复跑：`bash bin/32_run_quality_balanced_gold_flat.sh` · `bash bin/35_run_quality_balanced60_treerag.sh` · `bash bin/21_compare_realdata_baselines.sh`  
仅 refresh compose+judge：`bash bin/36_recompose_judge.sh` · 仅重判分：`python3 bin/36_recompose_judge.py --judge-only`
