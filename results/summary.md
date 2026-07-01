# 实验结果摘要

更新日期：2026-07-02

Canonical 实验：**`latest_clean400_scope_compact_cap180_v1 · b500 · 400 题`**

Gold/Pred 使用同一 robust-v1 导航、b500 evidence 预算、compose、Inspect judge；差异仅在 `tree_source`。本版加入 scope outline collection、compact evidence packing 与 scope compose guidance。Flat / TreeRAG 按 `inspect_id` 复用 400 题 baseline，未在本轮重跑。

省成本口径：只重跑受改动影响的 `scope_collection` 133 题，`niche_fact` / `multi_hop` 267 题复用上一版同题结果；最终表是完整 400 题质量。仓库只保留最终最佳结果文件，不保留 smoke、中间子集和旧对照结果。

## 主表（score_task_mean）

| 方法 | 状态 | Overall | Niche | Multi-hop | Scope | Evidence |
|---|---|---:|---:|---:|---:|---:|
| Gold Nav robust-v1 | scope rerun + reused non-scope | 0.2111 | 0.2090 | 0.0777 | 0.3466 | 0.6188 |
| Pred Nav robust-v1 | scope rerun + reused non-scope | 0.1450 | 0.1276 | 0.0601 | 0.2474 | 0.4213 |
| TreeRAG | reused | 0.2016 | 0.1522 | 0.0831 | 0.3698 | 0.5125 |
| Flat | reused | 0.1376 | 0.0903 | 0.0683 | 0.2547 | 0.4988 |

## Bootstrap 摘要

- Gold−Pred：`+0.0661`，CI `[+0.0372, +0.0957]`
- Gold−TreeRAG：`+0.0095`，CI `[-0.0236, +0.0428]`（跨 0）
- Pred−TreeRAG：`-0.0566`，CI `[-0.0891, -0.0242]`
- Pred−Flat：`+0.0074`，CI `[-0.0227, +0.0383]`（跨 0）

## 相比上一版同题结果

| Arm | Overall Δ | Scope Δ | Evidence Δ | Scope W/L/T |
|---|---:|---:|---:|---:|
| Gold | +0.0219 | +0.0658 | +0.0021 | 36/11/86 |
| Pred | +0.0126 | +0.0380 | +0.0000 | 27/10/96 |

267 条非 scope 行逐行完全未变，提升全部来自 133 条 scope。

## 结论

scope 修复显著改善 Gold/Pred 的 scope_collection 表现。Gold overall 略高于 TreeRAG，但置信区间跨 0；Pred 略高于 Flat，但置信区间也跨 0。当前结果适合作为 scope 修复后的观察集记录，不应在同一 400 题上继续调参并写作稳定正向 claim。

## 入库文件

| 用途 | 路径 |
|---|---|
| Gold / Pred 400 题 | `results/latest_clean400_scope_compact_cap180_v1_{gold,pred}_b500.json` |
| 汇总 | `results/latest_clean400_scope_compact_cap180_v1_summary.{json,md}` |

## 复跑

```bash
python3 tests/test_protocol.py -q
python3 tests/test_nav_improvements.py -q
```

详见 [latest_clean400_scope_compact_cap180_v1_summary.md](latest_clean400_scope_compact_cap180_v1_summary.md)。
