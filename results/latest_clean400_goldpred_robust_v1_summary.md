# latest_clean400_goldpred_robust_v1 · Gold/Pred + reused baselines

## Quality

| Method | Status | Overall | Niche | Multi-hop | Scope | Evidence |
|---|---|---:|---:|---:|---:|---:|
| Gold Nav robust-v1 | new | 0.1891 | 0.2090 | 0.0777 | 0.2806 | 0.5697 |
| Pred Nav robust-v1 | new | 0.1338 | 0.1276 | 0.0601 | 0.2136 | 0.3946 |
| TreeRAG | reused | 0.2016 | 0.1522 | 0.0831 | 0.3698 | 0.5125 |
| Flat | reused | 0.1376 | 0.0903 | 0.0683 | 0.2547 | 0.4988 |

## Paired Bootstrap

- `gold_minus_pred`: mean `+0.0553`, 95% CI `[+0.0268, +0.0846]`, win/loss/tie `67/34/299`
- `gold_minus_treerag`: mean `-0.0125`, 95% CI `[-0.0465, +0.0217]`, win/loss/tie `58/74/268`
- `gold_minus_flat`: mean `+0.0515`, 95% CI `[+0.0159, +0.0875]`, win/loss/tie `78/55/267`
- `pred_minus_treerag`: mean `-0.0678`, 95% CI `[-0.1006, -0.0355]`, win/loss/tie `38/85/277`
- `pred_minus_flat`: mean `-0.0039`, 95% CI `[-0.0345, +0.0274]`, win/loss/tie `56/64/280`
- `treerag_minus_flat`: mean `+0.0640`, 95% CI `[+0.0327, +0.0960]`, win/loss/tie `76/39/285`

## Cost And Reuse

| Arm | Status | Billed tokens | API calls | Cache hits | Online response | Judge | End-to-end |
|---|---|---:|---:|---:|---:|---:|---:|
| Gold Nav robust-v1 | new | 525,406 | 356 | 3,265 | 261.1s | 0.2s | 261.7s |
| Pred Nav robust-v1 | new | 907,302 | 544 | 3,014 | 805.6s | 270.2s | 1076.4s |
| TreeRAG | reused | 714,110 | 1,169 | 177 | 817.0s | 1101.9s | 2804.2s |
| Flat | reused | 388,761 | 731 | 155 | 846.1s | 1286.8s | 2133.0s |

- Gold audit: `356` API calls, `3265` cache hits.
- Pred audit: `544` API calls, `3014` cache hits.
- No TreeRAG or Flat rows are rerun in this summary.
