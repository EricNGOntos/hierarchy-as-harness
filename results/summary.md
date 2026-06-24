# 实验结果摘要（fair_clean · b500 · 51 题）

最后更新：2026-06-24

**Canonical**：`goldnav_e2_v1`（A/C v4 Gold Nav + 三方共享 E2 hop-aware evidence allocation）

## 主表（score_task_mean）

| 方法 | 总体 | niche | multi | scope | evidence |
|------|-----:|------:|------:|------:|---------:|
| **Gold** | **0.504** | **0.824** | **0.157** | 0.530 | **0.688** |
| **TreeRAG** | 0.433 | **0.824** | 0.098 | 0.379 | 0.623 |
| Flat | 0.354 | 0.471 | 0.020 | **0.572** | 0.583 |

逐题 paired bootstrap 95% CI：Gold−TreeRAG `[-0.046, 0.188]`；Gold−Flat `[0.027, 0.276]`；TreeRAG−Flat `[-0.047, 0.208]`。

## 入库结果文件

| 方法 | 路径 |
|------|------|
| Gold + Flat | `results/fair_clean_gold_flat_fair_clean_goldnav_e2_v1_b500.json` |
| TreeRAG | `results/fair_clean_treerag_fair_clean_goldnav_e2_v1_b500.json` |

复跑：`bash bin/32_run_quality_balanced_gold_flat.sh` · `bash bin/35_run_quality_balanced60_treerag.sh` · `bash bin/21_compare_realdata_baselines.sh`  
仅重判分：`python3 bin/36_recompose_judge.py --judge-only`

## 文档索引

| 文档 | 用途 |
|------|------|
| [UNIFIED_FIX_PLAN.zh-CN.md](../UNIFIED_FIX_PLAN.zh-CN.md) | 协议说明、复跑命令、已知短板 |
| [paper_main_experiment.zh-CN.md](paper_main_experiment.zh-CN.md) | 论文主实验表、消融阶梯、可写结论 |
| [scope_hit_near_far_e2_v1.md](scope_hit_near_far_e2_v1.md) | 17 道 scope 题 HIT/NEAR/FAR 诊断 |
| [goldnav_e2_v1_validation.md](goldnav_e2_v1_validation.md) | 60 题独立外推验证（**非 canonical**） |
| [GOLD_NAV_问题诊断与改进方案.zh-CN.md](../GOLD_NAV_问题诊断与改进方案.zh-CN.md) | Nav 改进历程与轨迹分析（历史参考） |

## Gold Nav 消融阶梯（数值见论文稿，大 JSON 不入库）

| 版本 | Gold 总体 | scope | multi | 说明 |
|------|----------:|------:|------:|------|
| scopefix_v2 | 0.425 | 0.392 | 0.118 | scope 金标/判分修复基线 |
| goldnav_ac_v4 | 0.477 | 0.530 | 0.078 | A/C v4 导航 |
| **goldnav_e2_v1** | **0.504** | 0.530 | **0.157** | + 共享 E2 hop budget（**canonical**） |

未纳入主叙事：B1 discovery bridge、E1 hop-compose（定向无 Gold 净收益）。

## 60 题外推验证

独立 60 题（niche/multi/scope 各 20）未复现 51 题 canonical 水平；Gold **0.145**、TreeRAG **0.125**、Flat **0.075**。详见 [goldnav_e2_v1_validation.md](goldnav_e2_v1_validation.md)。该批完整 JSON 未入库，仅保留任务文件与摘要表。
