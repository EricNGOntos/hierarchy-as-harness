# Gold/Pred/Flat/TreeRAG 当前协议说明

> 当前完整实验：`latest_clean400_goldpred_robust_v1 · b500 · 400 题`
> 状态：robust-v1 已完成；结果为负，不作为正向主 claim。

## 1. 比较口径

本轮执行的是 Gold/Pred 公平优化实验：

| 方法 | 来源 |
|---|---|
| Gold Nav robust-v1 | 新跑 `results/latest_clean400_goldpred_robust_v1_gold_b500.json` |
| Pred Nav robust-v1 | 新跑 `results/latest_clean400_goldpred_robust_v1_pred_b500.json` |
| Flat | 复用 `results/latest_clean400_goldnav_e2_v1_gold_flat_b500.json` |
| TreeRAG | 复用 `results/latest_clean400_goldnav_e2_v1_treerag_b500.json` |

四方按同一 400 个 `inspect_id` 对齐，最终 evidence budget 均为 b500。

Gold/Pred 共享：

- 同一 `src/nav` 导航算法
- 同一 `src/realdata/agent_delivery` budget fill / compose / Inspect judge
- 同一 LLM cache 策略
- 同一输出 JSON schema

唯一允许差异：

- Gold 使用 `tree_source=gold`
- Pred 使用 `tree_source=pred`

## 2. robust-v1 改动边界

robust-v1 是通用结构鲁棒性修复，不使用 gold answer 刷分：

- synthetic prefix/doc-root section
- hybrid direct search in `auto` mode
- scope direct hit local window
- Gold/Pred single-arm runner
- shared compose parser fallback for malformed scope `items`

不进入正式方法：

- `previous_level`
- 用 `gold_nodes` 修 Pred tree
- Gold 专属最终 evidence 注入
- TreeRAG/Flat 重跑或重建树

## 3. 400 题结果

| 方法 | 状态 | Overall | Niche | Multi-hop | Scope | Evidence |
|---|---|---:|---:|---:|---:|---:|
| Gold Nav robust-v1 | new | 0.1891 | 0.2090 | 0.0777 | 0.2806 | 0.5697 |
| Pred Nav robust-v1 | new | 0.1338 | 0.1276 | 0.0601 | 0.2136 | 0.3946 |
| TreeRAG | reused | 0.2016 | 0.1522 | 0.0831 | 0.3698 | 0.5125 |
| Flat | reused | 0.1376 | 0.0903 | 0.0683 | 0.2547 | 0.4988 |

Paired bootstrap：

- Gold−TreeRAG：`-0.0125`，95% CI `[-0.0465, +0.0217]`
- Pred−TreeRAG：`-0.0678`，95% CI `[-0.1006, -0.0355]`
- Pred−Flat：`-0.0039`，95% CI `[-0.0345, +0.0274]`

结论：robust-v1 没有在 400 题上泛化。Pred 不能作为正式论文中的 predicted hierarchy 正向优势证据；Gold 也不能声称稳定优于 TreeRAG。

## 4. 成本与过程量

新增 Gold/Pred 成本按 audit：

| Arm | Billed tokens | API calls | Cache hits |
|---|---:|---:|---:|
| Gold Nav robust-v1 | 525,406 | 356 | 3,265 |
| Pred Nav robust-v1 | 907,302 | 544 | 3,014 |

过程量：

- `cache/latest_clean400_goldpred_robust_v1/`
- `results/latest_clean400_goldpred_robust_v1_summary.json`
- `results/latest_clean400_goldpred_robust_v1_summary.md`

## 5. 当前建议

停止在已观察的 400 题上继续调导航规则。下一步应先修 Pred tree 生成质量，并使用新 holdout 支撑论文主 claim：

- 修 parent exact、top-level/prefix coverage、upward jump、过宽父节点。
- 离线结构指标过关后再跑小 dev。
- 最强论文结论必须来自未参与调参的新 holdout。
