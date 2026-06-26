# Current Results Summary

更新日期：2026-06-26

当前最新完整实验是 `latest_clean400_goldpred_robust_v1 · b500 · 400 题`。这轮按预注册的公平修复执行：Gold/Pred 使用同一导航算法、同一 b500 evidence 预算、同一 compose、同一 Inspect judge；差异只在 `tree_source=gold` 或 `tree_source=pred`。TreeRAG 和 Flat 没有重跑，只按 `inspect_id` 复用已有完整 400 题结果。

## Latest-clean 400 · robust-v1

| 方法 | 状态 | Overall | Niche | Multi-hop | Scope | Evidence |
|---|---|---:|---:|---:|---:|---:|
| Gold Nav robust-v1 | new | 0.1891 | 0.2090 | 0.0777 | 0.2806 | 0.5697 |
| Pred Nav robust-v1 | new | 0.1338 | 0.1276 | 0.0601 | 0.2136 | 0.3946 |
| TreeRAG | reused | 0.2016 | 0.1522 | 0.0831 | 0.3698 | 0.5125 |
| Flat | reused | 0.1376 | 0.0903 | 0.0683 | 0.2547 | 0.4988 |

Paired bootstrap:

- `gold_minus_pred`: mean `+0.0553`, 95% CI `[+0.0268, +0.0846]`
- `gold_minus_treerag`: mean `-0.0125`, 95% CI `[-0.0465, +0.0217]`
- `gold_minus_flat`: mean `+0.0515`, 95% CI `[+0.0159, +0.0875]`
- `pred_minus_treerag`: mean `-0.0678`, 95% CI `[-0.1006, -0.0355]`
- `pred_minus_flat`: mean `-0.0039`, 95% CI `[-0.0345, +0.0274]`
- `treerag_minus_flat`: mean `+0.0640`, 95% CI `[+0.0327, +0.0960]`

结论：robust-v1 在 51 题 dev gate 上通过，但在完整 400 题上没有泛化。Gold 低于 TreeRAG 但 CI 跨 0；Pred 仍显著低于 TreeRAG，且与 Flat 基本持平。

## 与上一版 400 结果对比

上一版 `latest_clean400_pred_multiband_v1`：

| 方法 | Overall | Niche | Multi-hop | Scope | Evidence |
|---|---:|---:|---:|---:|---:|
| Gold Nav | 0.1974 | 0.2090 | 0.0777 | 0.3053 | 0.5781 |
| Pred Nav multi-band | 0.1373 | 0.1567 | 0.0579 | 0.1973 | 0.4107 |
| TreeRAG | 0.2016 | 0.1522 | 0.0831 | 0.3698 | 0.5125 |
| Flat | 0.1376 | 0.0903 | 0.0683 | 0.2547 | 0.4988 |

robust-v1 的变化：

- Gold overall `-0.0083`，主要来自 scope `0.3053 -> 0.2806`。
- Pred overall `-0.0035`，scope `0.1973 -> 0.2136` 小幅改善，但 niche `0.1567 -> 0.1276` 和 evidence 下降。
- 因此 robust-v1 只能作为公平通用修复的负结果/消融记录，不能作为论文主结果。

## Cost And Reuse

`latest_clean400_goldpred_robust_v1` 实际新增成本按 audit 记录：

| Arm | Billed tokens | API calls | Cache hits |
|---|---:|---:|---:|
| Gold Nav robust-v1 | 525,406 | 356 | 3,265 |
| Pred Nav robust-v1 | 907,302 | 544 | 3,014 |

TreeRAG 和 Flat 没有在本轮重跑；summary 中展示的 TreeRAG/Flat 成本是复用文件里的历史成本，不是新增成本。

## Active Artifacts

robust-v1 结果：

- `results/latest_clean400_goldpred_robust_v1_gold_b500.json`
- `results/latest_clean400_goldpred_robust_v1_pred_b500.json`
- `results/latest_clean400_goldpred_robust_v1_summary.json`
- `results/latest_clean400_goldpred_robust_v1_summary.md`
- `cache/latest_clean400_goldpred_robust_v1/`

复用 baseline：

- `results/latest_clean400_goldnav_e2_v1_gold_flat_b500.json`
- `results/latest_clean400_goldnav_e2_v1_treerag_b500.json`

诊断：

- `results/gold_pred_robust_v1_diagnostics.json`
- `results/gold_pred_robust_v1_diagnostics.md`

## Recommended Next Step

不要继续在已观察的 400 题上微调导航规则。下一步应转向 Pred tree 离线结构修复，并为论文 claim 准备新的 holdout：

- 修 Pred tree 父节点准确率、top-level/prefix coverage、upward jump、过宽父节点。
- 在不调用 LLM 的结构指标上确认 Pred tree 质量提升。
- 只在小 dev set 上调规则，最终 claim 必须用未参与调参的新 holdout。
