# 论文主实验：fair_clean 51 题 · goldnav_e2_v1

日期：2026-06-24  
任务集：`data/tasks/tasks_realdata_bodyrich_fair_clean.jsonl`（niche / multi_hop / scope 各 17 题）  
协议：共享 b500 evidence 预算、方法无关 `[E1]/[E2]` header、同一 compose + Inspect judge

## 模型配置（Methods）

| 用途 | 模型 |
|------|------|
| Compose / Nav / TreeRAG 建树 | `qwen3.5-flash` |
| Inspect 语义判分 | `deepseek-v4-pro` |
| Dense embedding | `BAAI/bge-m3` |

配置来源：`~/.config/realdata_treerag/llm_api.env`

## 主结果表（score_task_mean）

| 方法 | 总体 | niche | multi | scope | evidence |
|------|-----:|------:|------:|------:|---------:|
| **Gold Nav** | **0.504** | **0.824** | **0.157** | 0.530 | **0.688** |
| TreeRAG | 0.433 | **0.824** | 0.098 | 0.379 | 0.623 |
| Flat | 0.354 | 0.471 | 0.020 | **0.572** | 0.583 |

逐题 paired bootstrap 95% CI：

- Gold − Flat：`[+0.027, +0.276]`（**不跨 0**）
- Gold − TreeRAG：`[-0.046, +0.188]`（**跨 0**，不能写显著优于 TreeRAG）
- TreeRAG − Flat：`[-0.047, +0.208]`

结果文件：

- `results/fair_clean_gold_flat_fair_clean_goldnav_e2_v1_b500.json`
- `results/fair_clean_treerag_fair_clean_goldnav_e2_v1_b500.json`
- `cache/compare_fair_clean_goldnav_e2_v1.md`

## 消融阶梯（Gold Nav 演进，附录用）

数值来自历史复跑；大体积 JSON 未入库，复跑见 `bin/32` + `NAV_RUN_TAG`。

| 版本 | 改动 | Gold 总体 | scope | multi | 备注 |
|------|------|----------:|------:|------:|------|
| scopefix_v2 | scope 金标/判分修复 | 0.425 | 0.392 | 0.118 | 历史基线 |
| goldnav_ac_v4 | A/C v4 导航 | 0.477 | 0.530 | 0.078 | 零增 collect <25% |
| **goldnav_e2_v1** | + 共享 E2 hop budget | **0.504** | 0.530 | **0.157** | **canonical** |

未纳入主叙事：B1 bridge、E1 hop-compose（定向无 Gold 净收益）。

## 可写结论 vs Limitations

**可写：**

- 共享输出预算下，Gold Nav 在 51 题上**均值**高于 Flat 与 TreeRAG。
- Gold 对 Flat 的配对优势在当前样本上 bootstrap CI 不跨 0。
- multi 提升来自**三方共享** E2 hop-aware evidence allocation（`MULTIHOP_EVIDENCE_ALLOCATION=1`），非 Gold 专属 judge。

**Limitations（须写）：**

- scope 分项 Flat（0.572）仍高于 Gold（0.530）。
- Gold − TreeRAG 总体差 CI 跨 0。
- 51 题样本量有限，总体优劣 bootstrap 区间仍宽。
- 无 RealData Pred arm；不能从本批结果推 predicted hierarchy 部署收益。
- goldnav 60 外推集未确认 0.504 的外推性（见 `results/goldnav_e2_v1_validation.md`）。

## 复跑

```bash
bash bin/32_run_quality_balanced_gold_flat.sh
bash bin/35_run_quality_balanced60_treerag.sh
bash bin/21_compare_realdata_baselines.sh
python3 tests/test_protocol.py -q
python3 tests/test_nav_improvements.py -q
```
