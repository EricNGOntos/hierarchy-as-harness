# Gold/Pred Robust-v1 Diagnostics

## Current Quality

| Method | Overall | Niche | Multi-hop | Scope | Evidence |
|---|---:|---:|---:|---:|---:|
| Gold Nav | 0.1974 | 0.2090 | 0.0777 | 0.3053 | 0.5781 |
| Pred Nav | 0.1373 | 0.1567 | 0.0579 | 0.1973 | 0.4107 |
| TreeRAG | 0.2016 | 0.1522 | 0.0831 | 0.3698 | 0.5125 |
| Flat | 0.1376 | 0.0903 | 0.0683 | 0.2547 | 0.4988 |

## Pred Structure

- Level exact: `0.8563`; parent exact: `0.4084`; level MAE: `0.1595`.
- Root-bad docs: `43`; upward-jump docs: `113`; upward-jump violations: `1292`.
- Top-level coverage missing lines: `2283` across `178` docs.

## Action Waste

- `gold`: search `221`, zero-search `115`; collect `975`, zero-collect `57`.
- `pred`: search `427`, zero-search `238`; collect `814`, zero-collect `85`.

## Artifacts

- `results/gold_pred_robust_v1_diagnostics.json`
