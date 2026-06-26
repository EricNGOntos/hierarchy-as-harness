# RealData Gold/Pred Hierarchy Evaluation

当前工作区主线是 latest-clean 400 题 Gold/Pred/Flat/TreeRAG 对齐评测。最新完整实验是 `latest_clean400_goldpred_robust_v1 · b500 · 400 题`。

## 当前结论

robust-v1 已按公平协议完成，但结果为负：51 题 dev gate 通过，完整 400 题没有泛化。

| 方法 | 状态 | Overall | Niche | Multi-hop | Scope | Evidence |
|---|---|---:|---:|---:|---:|---:|
| Gold Nav robust-v1 | new | 0.1891 | 0.2090 | 0.0777 | 0.2806 | 0.5697 |
| Pred Nav robust-v1 | new | 0.1338 | 0.1276 | 0.0601 | 0.2136 | 0.3946 |
| TreeRAG | reused | 0.2016 | 0.1522 | 0.0831 | 0.3698 | 0.5125 |
| Flat | reused | 0.1376 | 0.0903 | 0.0683 | 0.2547 | 0.4988 |

Pred robust-v1 显著低于 TreeRAG，且与 Flat 基本持平。Gold robust-v1 与 TreeRAG 差值 CI 跨 0，不能声称稳定优于 TreeRAG。

## Fairness Protocol

Gold/Pred robust-v1 共享同一导航算法、b500 evidence budget、compose、Inspect judge 和 cache 策略。区别只在 `tree_source=gold` vs `tree_source=pred`。

TreeRAG 和 Flat 在 robust-v1 中没有重跑，只按 `inspect_id` 复用已有完整结果。

## Key Artifacts

robust-v1：

- `results/latest_clean400_goldpred_robust_v1_gold_b500.json`
- `results/latest_clean400_goldpred_robust_v1_pred_b500.json`
- `results/latest_clean400_goldpred_robust_v1_summary.md`
- `cache/latest_clean400_goldpred_robust_v1/`

复用 baseline：

- `results/latest_clean400_goldnav_e2_v1_gold_flat_b500.json`
- `results/latest_clean400_goldnav_e2_v1_treerag_b500.json`

诊断：

- `results/gold_pred_robust_v1_diagnostics.md`

## Main Scripts

- `bin/44_run_pred_only_bodyrich.py`：single hierarchical arm runner，支持 `--tree-source gold|pred`
- `bin/48_diagnose_gold_pred_robust.py`：零 token Gold/Pred 结构诊断
- `bin/49_run_fair_clean_goldpred_robust_v1_dev51.sh`：51 题 dev gate
- `bin/50_summarize_goldpred_reuse.py`：Gold/Pred 新结果 + Flat/TreeRAG 复用汇总
- `bin/51_run_latest_clean400_goldpred_robust_v1.sh`：400 题 robust-v1 最终脚本

## Reproduce

```bash
python3 tests/test_protocol.py -q
bash bin/49_run_fair_clean_goldpred_robust_v1_dev51.sh
bash bin/51_run_latest_clean400_goldpred_robust_v1.sh
```

脚本会复用 `cache/llm_api_cache.jsonl`、`cache/fair_clean_goldpred_robust_v1b_dev51/` 和 `cache/latest_clean400_goldpred_robust_v1/` 中可用缓存。已有结果文件存在时会跳过对应 arm。

## Next Step

不要继续在已观察 400 题上刷导航规则。下一步应修 Pred tree 生成质量，并用新的 holdout 支撑论文 claim。
