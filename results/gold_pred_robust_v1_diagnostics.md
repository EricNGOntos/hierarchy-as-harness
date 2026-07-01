# Gold/Pred Robust-v1 Diagnostics

> Updated 2026-07-02. Current canonical quality is `latest_clean400_scope_compact_cap180_v1`; structural diagnostics below still describe the robust-v1 Gold/Pred navigation run.

## Current Quality

| Method | Overall | Niche | Multi-hop | Scope | Evidence |
|---|---:|---:|---:|---:|---:|
| Gold Nav | 0.2111 | 0.2090 | 0.0777 | 0.3466 | 0.6188 |
| Pred Nav | 0.1450 | 0.1276 | 0.0601 | 0.2474 | 0.4213 |
| TreeRAG | 0.2016 | 0.1522 | 0.0831 | 0.3698 | 0.5125 |
| Flat | 0.1376 | 0.0903 | 0.0683 | 0.2547 | 0.4988 |

## Scope Compact Delta

Compared with `latest_clean400_scope_outline_fixed_v1`, the current canonical run only reruns `scope_collection` rows.

| Arm | Overall Δ | Scope Δ | Evidence Δ | Scope W/L/T |
|---|---:|---:|---:|---:|
| Gold | +0.0219 | +0.0658 | +0.0021 | 36/11/86 |
| Pred | +0.0126 | +0.0380 | +0.0000 | 27/10/96 |

The 267 non-scope rows are reused unchanged.

## Pred Structure

- Level exact: `0.8563`; parent exact: `0.4084`; level MAE: `0.1595`.
- Root-bad docs: `43`; upward-jump docs: `113`; upward-jump violations: `1292`.
- Top-level coverage missing lines: `2283` across `178` docs.

## Action Waste

- `gold`: search `221`, zero-search `115`; collect `975`, zero-collect `57`.
- `pred`: search `432`, zero-search `244`; collect `784`, zero-collect `72`.

## Artifacts

- `results/gold_pred_robust_v1_diagnostics.json`
- `results/latest_clean400_scope_compact_cap180_v1_summary.md`
