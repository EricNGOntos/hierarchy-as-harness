# RealData Gold/Pred Hierarchy Evaluation

当前 canonical 实验：**`latest_clean400_scope_compact_cap180_v1 · b500 · 400 题`**

在 latest-clean 400 题上比较 Gold Nav / Pred Nav / Flat / TreeRAG。Gold 与 Pred 使用同一 robust-v1 导航算法与共享输出预算协议，并加入 scope collection 的 outline collection、compact evidence packing 与 compose guidance 修复；Flat 与 TreeRAG 按 `inspect_id` 复用已有 400 题 baseline。

本版为省成本复跑：仅重跑受改动影响的 `scope_collection` 133 题，`niche_fact` / `multi_hop` 267 题复用同一批 400 题上一版结果；最终质量表仍是完整 400 题口径。

## 主结果（400 题）

| 方法 | 状态 | Overall | Niche | Multi-hop | Scope | Evidence |
|---|---|---:|---:|---:|---:|---:|
| Gold Nav robust-v1 | scope rerun + reused non-scope | 0.2111 | 0.2090 | 0.0777 | 0.3466 | 0.6188 |
| Pred Nav robust-v1 | scope rerun + reused non-scope | 0.1450 | 0.1276 | 0.0601 | 0.2474 | 0.4213 |
| TreeRAG | reused | 0.2016 | 0.1522 | 0.0831 | 0.3698 | 0.5125 |
| Flat | reused | 0.1376 | 0.0903 | 0.0683 | 0.2547 | 0.4988 |

要点：Gold Nav 的 overall 已高于 TreeRAG，但 Gold−TreeRAG 的 bootstrap CI 仍跨 0，不能写稳定优于 TreeRAG；Pred Nav 略高于 Flat，但 CI 也跨 0。相比 `scope_outline_fixed_v1`，提升全部来自 scope 子集：Gold overall +0.0219、scope +0.0658；Pred overall +0.0126、scope +0.0380；267 条非 scope 行逐行完全未变。

## 公平协议

Gold/Pred 共享：同一 `src/nav` 导航、b500 evidence budget、compose、Inspect judge、cache 策略。唯一差异是 `tree_source=gold` vs `tree_source=pred`。

robust-v1 与 scope compact 修复均为通用结构/预算修复（synthetic root、hybrid direct search、scope outline、compact evidence packing、scope compose guidance），不使用 gold answer 或 Pred tree 作弊。

## 入库文件

**400 题 canonical**

- `results/latest_clean400_scope_compact_cap180_v1_gold_b500.json`
- `results/latest_clean400_scope_compact_cap180_v1_pred_b500.json`
- `results/latest_clean400_scope_compact_cap180_v1_summary.{json,md}`

**scope-only 增量复跑**

- `results/latest_clean400_scope_compact_cap180_scope133_v1_gold_b500.json`
- `results/latest_clean400_scope_compact_cap180_scope133_v1_pred_b500.json`
- `results/latest_clean400_scope_compact_cap180_scope133_v1_summary.{json,md}`

**对照基线**

- `results/latest_clean400_scope_outline_fixed_v1_gold_b500.json`
- `results/latest_clean400_scope_outline_fixed_v1_pred_b500.json`
- `results/latest_clean400_scope_outline_fixed_v1_summary.{json,md}`

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
| `bin/51_run_latest_clean400_goldpred_robust_v1.sh` | 400 题完整复跑入口；可通过 `RUN_TAG` / `TASKS` / `INSPECT_TASKS` 跑 scope-only 增量 |
| `bin/25_check_llm_endpoint.py` | LLM 连通性检查 |

## 复跑

```bash
python3 tests/test_protocol.py -q
python3 tests/test_nav_improvements.py -q
```

推荐省成本复跑方式是只重跑受改动影响的 scope rows，然后按 `inspect_id` 合并回 400 题结果：

```bash
RUN_TAG=latest_clean400_scope_compact_cap180_scope133_v1 \
TASKS=data/tasks/tmp_scope_compact_all_scope133.jsonl \
INSPECT_TASKS=data/tasks/tmp_scope_compact_all_scope133.inspect.jsonl \
NAV_SCOPE_OUTLINE_MODE=1 \
NAV_SCOPE_OUTLINE_LINES_PER_CHILD=3 \
NAV_SCOPE_OUTLINE_MIN_CHUNKS=3 \
BODYRICH_SCOPE_COMPACT_EVIDENCE=1 \
BODYRICH_SCOPE_COMPACT_CHARS_PER_CHUNK=180 \
bash bin/51_run_latest_clean400_goldpred_robust_v1.sh
```

本地 cache（`cache/`，不入库）可加速复跑：`cache/llm_api_cache.jsonl`、`cache/latest_clean400_scope_compact_cap180_scope133_v1/`、`cache/embeddings/`。

API 密钥放在 `src/realdata/agent_delivery/llm_api.env`（或 `~/.config/realdata_treerag/llm_api.env`），已在 `.gitignore` 中。

## 文档

- [results/summary.md](results/summary.md) — 结果索引与协议摘要
- [results/latest_clean400_scope_compact_cap180_v1_summary.md](results/latest_clean400_scope_compact_cap180_v1_summary.md) — 400 题详细汇总

## Next Step

不要在已观察 400 题上继续调导航规则。下一步应修 Pred tree 离线结构，并用新 holdout 支撑论文 claim；当前 400 题结果可作为 scope 修复后的观察集记录。
