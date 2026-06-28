# Gold/Pred/Flat/TreeRAG 协议说明（400 题 canonical）

> **实验**：`latest_clean400_goldpred_robust_v1 · b500 · 400 题`
> **状态**：robust-v1 已完成；400 题结果为负，Pred 不能作为正向 hierarchy 部署证据

---

## 1. 比较口径

| 方法 | 来源 |
|---|---|
| Gold Nav robust-v1 | 新跑 `results/latest_clean400_goldpred_robust_v1_gold_b500.json` |
| Pred Nav robust-v1 | 新跑 `results/latest_clean400_goldpred_robust_v1_pred_b500.json` |
| Flat | 复用 `results/latest_clean400_goldnav_e2_v1_gold_flat_b500.json` |
| TreeRAG | 复用 `results/latest_clean400_goldnav_e2_v1_treerag_b500.json` |

四方按同一 400 个 `inspect_id` 对齐，最终 evidence 字符预算均为 b500。

Gold/Pred 共享同一导航算法、`budget_eval` / compose / Inspect judge、LLM cache 策略与输出 schema。唯一允许差异：`tree_source=gold` vs `tree_source=pred`。

---

## 2. robust-v1 改动边界

通用结构鲁棒性修复，**不使用 gold answer 刷分**：

- synthetic prefix / doc-root section
- hybrid direct search（`auto` 模式）
- scope direct hit local window
- Gold/Pred single-arm runner（`bin/44`）
- scope compose parser fallback（畸形 `items` 容错）

**不进入正式方法**：`previous_level`、用 `gold_nodes` 修 Pred tree、Gold 专属最终 evidence 注入、在本轮重跑 TreeRAG/Flat。

---

## 3. 400 题主结果

| 方法 | Overall | Niche | Multi-hop | Scope | Evidence |
|---|---:|---:|---:|---:|---:|
| Gold Nav robust-v1 | 0.1891 | 0.2090 | 0.0777 | 0.2806 | 0.5697 |
| Pred Nav robust-v1 | 0.1338 | 0.1276 | 0.0601 | 0.2136 | 0.3946 |
| TreeRAG | 0.2016 | 0.1522 | 0.0831 | 0.3698 | 0.5125 |
| Flat | 0.1376 | 0.0903 | 0.0683 | 0.2547 | 0.4988 |

Paired bootstrap（详见 `results/latest_clean400_goldpred_robust_v1_summary.md`）：

- Gold−TreeRAG：均值 `-0.0125`，95% CI `[-0.0465, +0.0217]`（跨 0）
- Pred−TreeRAG：均值 `-0.0678`，95% CI `[-0.1006, -0.0355]`
- Pred−Flat：均值 `-0.0039`，95% CI `[-0.0345, +0.0274]`（跨 0）

---

## 4. 成本

| Arm | Billed tokens | API calls | Cache hits |
|---|---:|---:|---:|
| Gold Nav robust-v1 | 525,406 | 356 | 3,265 |
| Pred Nav robust-v1 | 907,302 | 544 | 3,014 |

TreeRAG / Flat 为本轮复用，上表不含其新增成本。

---

## 5. 复跑

```bash
bash bin/51_run_latest_clean400_goldpred_robust_v1.sh
python3 bin/48_diagnose_gold_pred_robust.py
python3 tests/test_protocol.py -q
```

---

## 6. 建议

停止在已观察 400 题上继续调导航。下一步：修 Pred tree 离线结构（parent exact、prefix coverage、upward jump、过宽父节点），在新 holdout 上验证后再写论文主 claim。
