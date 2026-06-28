# RealData Gold/Pred Hierarchy Evaluation

当前 canonical 实验：**`latest_clean400_goldpred_robust_v1 · b500 · 400 题`**

在 latest-clean 400 题上比较 Gold Nav / Pred Nav / Flat / TreeRAG。Gold 与 Pred 使用同一 robust-v1 导航算法与共享输出预算协议；Flat 与 TreeRAG 按 `inspect_id` 复用已有 400 题 baseline。

## 主结果（400 题）

| 方法 | 状态 | Overall | Niche | Multi-hop | Scope | Evidence |
|---|---|---:|---:|---:|---:|---:|
| Gold Nav robust-v1 | new | 0.1891 | 0.2090 | 0.0777 | 0.2806 | 0.5697 |
| Pred Nav robust-v1 | new | 0.1338 | 0.1276 | 0.0601 | 0.2136 | 0.3946 |
| TreeRAG | reused | 0.2016 | 0.1522 | 0.0831 | 0.3698 | 0.5125 |
| Flat | reused | 0.1376 | 0.0903 | 0.0683 | 0.2547 | 0.4988 |

要点：Pred 显著低于 TreeRAG；Gold 与 TreeRAG 差值 bootstrap CI 跨 0，不能写稳定优于 TreeRAG。

## 公平协议

Gold/Pred 共享：同一 `src/nav` 导航、b500 evidence budget、compose、Inspect judge、cache 策略。唯一差异是 `tree_source=gold` vs `tree_source=pred`。

robust-v1 为通用结构修复（synthetic root、hybrid direct search、scope direct window 等），不使用 gold answer 或 Pred tree 作弊。

## 入库文件

**400 题新跑**

- `results/latest_clean400_goldpred_robust_v1_gold_b500.json`
- `results/latest_clean400_goldpred_robust_v1_pred_b500.json`
- `results/latest_clean400_goldpred_robust_v1_summary.{json,md}`

**400 题复用 baseline**

- `results/latest_clean400_goldnav_e2_v1_gold_flat_b500.json`
- `results/latest_clean400_goldnav_e2_v1_treerag_b500.json`

**诊断**

- `results/gold_pred_robust_v1_diagnostics.{json,md}`

**任务与语料**

- `data/tasks/tasks_realdata_bodyrich_latest_clean_400.{jsonl,inspect.jsonl}`
- `data/corpus/test_data_full_realdata_clean_latest.jsonl`
- `data/realdata_clean_m1024_best_pred_levels_prevline_fallback.jsonl`

## 脚本

| 脚本 | 用途 |
|---|---|
| `bin/44_run_pred_only_bodyrich.py` | 单臂 Gold/Pred runner |
| `bin/47_prepare_pred400_cache.py` | 合并可复用 LLM cache |
| `bin/48_diagnose_gold_pred_robust.py` | 零 token 结构诊断 |
| `bin/50_summarize_goldpred_reuse.py` | Gold/Pred + Flat/TreeRAG 汇总 |
| `bin/51_run_latest_clean400_goldpred_robust_v1.sh` | 400 题完整复跑 |
| `bin/25_check_llm_endpoint.py` | LLM 连通性检查 |

## 复跑

```bash
python3 tests/test_protocol.py -q
python3 tests/test_nav_improvements.py -q
bash bin/51_run_latest_clean400_goldpred_robust_v1.sh
```

本地 cache（`cache/`，不入库）可加速复跑：`cache/llm_api_cache.jsonl`、`cache/latest_clean400_goldpred_robust_v1/`、`cache/embeddings/`。

API 密钥放在 `src/realdata/agent_delivery/llm_api.env`（或 `~/.config/realdata_treerag/llm_api.env`），已在 `.gitignore` 中。

## 文档

- [UNIFIED_FIX_PLAN.zh-CN.md](UNIFIED_FIX_PLAN.zh-CN.md) — 协议与结论
- [results/summary.md](results/summary.md) — 结果索引

## Next Step

不要在已观察 400 题上继续调导航规则。下一步应修 Pred tree 离线结构，并用新 holdout 支撑论文 claim。
