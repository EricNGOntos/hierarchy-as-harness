# 实验结果摘要

更新日期：2026-06-26

Canonical 实验：**`latest_clean400_goldpred_robust_v1 · b500 · 400 题`**

Gold/Pred 使用同一 robust-v1 导航、b500 evidence 预算、compose、Inspect judge；差异仅在 `tree_source`。Flat / TreeRAG 按 `inspect_id` 复用 400 题 baseline，未在本轮重跑。

## 主表（score_task_mean）

| 方法 | 状态 | Overall | Niche | Multi-hop | Scope | Evidence |
|---|---|---:|---:|---:|---:|---:|
| Gold Nav robust-v1 | new | 0.1891 | 0.2090 | 0.0777 | 0.2806 | 0.5697 |
| Pred Nav robust-v1 | new | 0.1338 | 0.1276 | 0.0601 | 0.2136 | 0.3946 |
| TreeRAG | reused | 0.2016 | 0.1522 | 0.0831 | 0.3698 | 0.5125 |
| Flat | reused | 0.1376 | 0.0903 | 0.0683 | 0.2547 | 0.4988 |

## Bootstrap 摘要

- Gold−Pred：`+0.0553`，CI `[+0.0268, +0.0846]`
- Gold−TreeRAG：`-0.0125`，CI `[-0.0465, +0.0217]`（跨 0）
- Pred−TreeRAG：`-0.0678`，CI `[-0.1006, -0.0355]`
- Pred−Flat：`-0.0039`，CI `[-0.0345, +0.0274]`（跨 0）

## 结论

Pred 显著低于 TreeRAG，与 Flat 基本持平。Gold 不能声称稳定优于 TreeRAG。robust-v1 应作为公平修复后的**负结果记录**，不宜作论文正向主 claim。

## 入库文件

| 用途 | 路径 |
|---|---|
| Gold / Pred 400 题 | `results/latest_clean400_goldpred_robust_v1_{gold,pred}_b500.json` |
| 汇总 | `results/latest_clean400_goldpred_robust_v1_summary.{json,md}` |
| Flat / TreeRAG 复用 | `results/latest_clean400_goldnav_e2_v1_{gold_flat,treerag}_b500.json` |
| 结构诊断 | `results/gold_pred_robust_v1_diagnostics.{json,md}` |

## 复跑

```bash
bash bin/51_run_latest_clean400_goldpred_robust_v1.sh
python3 bin/48_diagnose_gold_pred_robust.py
```

详见 [latest_clean400_goldpred_robust_v1_summary.md](latest_clean400_goldpred_robust_v1_summary.md)。
