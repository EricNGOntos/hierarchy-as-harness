# 公平协议实验结果摘要（fair_clean / b500）

最后更新：2026-06-22

> **主结果（canonical）**：Gold `unified_v1` **0.336** ≈ TreeRAG `unified_v2` **0.338**；Gold **> Flat**（0.194）。Phase2 导航改动已实验并**回退**（见消融）；compose scope 提示保留。

## 主表：score_task_mean（51 题，b500）

| 方法 | 总体 | niche | multi | scope | evidence |
|------|-----:|------:|------:|------:|---------:|
| **TreeRAG（unified_v2）** | **0.338** | 0.853 | 0.098 | **0.063** | 0.484 |
| **Gold（unified_v1）** | 0.336 | **0.853** | **0.118** | 0.038 | **0.602** |
| Flat（unified_v1） | 0.194 | 0.424 | 0.059 | 0.100 | 0.456 |

## Phase2 实验（已跑、nav 已回退）

| 配置 | Gold 总体 | multi | scope | 说明 |
|------|----------:|------:|------:|------|
| unified_v3（FINISH 门控 + 去重 C*） | 0.325 | 0.098 | 0.025 | 相对 v1 **下降**，nav 已 revert |
| ablation 无 discovery | 0.333 | 0.098 | 0.047 | discovery 贡献约 **+0.003** |
| ablation 无 agent state | 0.297 | 0.059 | 0.009 | Agent State 贡献约 **+0.039** |

Phase2 唯一保留：**collect 浪费步** 66%→43%（效率提升但未转化为 task 分）。

## Unified Fix Phase1（已上线）

- Fix1：证据组装（无 PATH、短 header）
- Fix2：Agent State + Observation
- Fix3：前置 discovery、D*、删 soft_safety

## 结果文件

| 配置 | 路径 |
|------|------|
| Gold + Flat（canonical） | `results/fair_clean_gold_flat_fair_clean_unified_v1_b500.json` |
| TreeRAG（canonical） | `results/fair_clean_treerag_fair_clean_unified_v2_b500.json` |
| 对比表 | `cache/compare_fair_clean_final.md` |
| 计划与验收（含 Phase2 消融数字） | `UNIFIED_FIX_PLAN.zh-CN.md` |

复跑：`bash bin/32_run_quality_balanced_gold_flat.sh` · `bash bin/35_run_quality_balanced60_treerag.sh` · 消融 `bash bin/33_run_unified_ablations.sh`（结果不纳入 canonical）
