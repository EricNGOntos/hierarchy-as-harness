# fair_clean_goldpred_robust_v1b_dev51 · Gold/Pred + reused baselines

## Quality

| Method | Status | Overall | Niche | Multi-hop | Scope | Evidence |
|---|---|---:|---:|---:|---:|---:|
| Gold Nav robust-v1 | new | 0.4968 | 0.8235 | 0.1569 | 0.5100 | 0.6454 |
| Pred Nav robust-v1 | new | 0.4627 | 0.8235 | 0.1569 | 0.4078 | 0.5596 |
| TreeRAG | reused | 0.4334 | 0.8235 | 0.0980 | 0.3786 | 0.6229 |
| Flat | reused | 0.3542 | 0.4706 | 0.0196 | 0.5723 | 0.5825 |

## Paired Bootstrap

- `gold_minus_pred`: mean `+0.0341`, 95% CI `[-0.0642, +0.1318]`, win/loss/tie `10/7/34`
- `gold_minus_treerag`: mean `+0.0634`, 95% CI `[-0.0432, +0.1684]`, win/loss/tie `14/7/30`
- `gold_minus_flat`: mean `+0.1426`, 95% CI `[+0.0241, +0.2656]`, win/loss/tie `16/8/27`
- `pred_minus_treerag`: mean `+0.0294`, 95% CI `[-0.0831, +0.1421]`, win/loss/tie `10/8/33`
- `pred_minus_flat`: mean `+0.1086`, 95% CI `[-0.0365, +0.2565]`, win/loss/tie `16/11/24`
- `treerag_minus_flat`: mean `+0.0792`, 95% CI `[-0.0464, +0.2077]`, win/loss/tie `13/9/29`

## Cost And Reuse

| Arm | Status | Billed tokens | API calls | Cache hits | Online response | Judge | End-to-end |
|---|---|---:|---:|---:|---:|---:|---:|
| Gold Nav robust-v1 | new | 0 | 0 | 476 | 36.7s | 0.1s | 37.1s |
| Pred Nav robust-v1 | new | 66,992 | 52 | 414 | 78.1s | 17.8s | 96.5s |
| TreeRAG | reused | 298,602 | 194 | 19 | 111.3s | 98.1s | 1030.8s |
| Flat | reused | 0 | 0 | 108 | 6.0s | 0.0s | 6.2s |

- Gold audit: `0` API calls, `476` cache hits.
- Pred audit: `52` API calls, `414` cache hits.
- No TreeRAG or Flat rows are rerun in this summary.
