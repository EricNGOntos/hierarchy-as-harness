# latest_clean400_scope_outline_fixed_v1 · Gold/Pred + reused baselines

## Quality

| Method | Status | Overall | Niche | Multi-hop | Scope | Evidence |
|---|---|---:|---:|---:|---:|---:|
| Gold Nav robust-v1 | new | 0.1892 | 0.2090 | 0.0777 | 0.2809 | 0.6168 |
| Pred Nav robust-v1 | new | 0.1324 | 0.1276 | 0.0601 | 0.2094 | 0.4213 |
| TreeRAG | reused | 0.2016 | 0.1522 | 0.0831 | 0.3698 | 0.5125 |
| Flat | reused | 0.1376 | 0.0903 | 0.0683 | 0.2547 | 0.4988 |

## Paired Bootstrap

- `gold_minus_pred`: mean `+0.0569`, 95% CI `[+0.0278, +0.0868]`, win/loss/tie `61/32/307`
- `gold_minus_treerag`: mean `-0.0124`, 95% CI `[-0.0471, +0.0227]`, win/loss/tie `56/76/268`
- `gold_minus_flat`: mean `+0.0516`, 95% CI `[+0.0158, +0.0880]`, win/loss/tie `79/52/269`
- `pred_minus_treerag`: mean `-0.0692`, 95% CI `[-0.1018, -0.0368]`, win/loss/tie `33/83/284`
- `pred_minus_flat`: mean `-0.0053`, 95% CI `[-0.0354, +0.0255]`, win/loss/tie `52/61/287`
- `treerag_minus_flat`: mean `+0.0640`, 95% CI `[+0.0327, +0.0960]`, win/loss/tie `76/39/285`

## Cost And Reuse

| Arm | Status | Billed tokens | API calls | Cache hits | Online response | Judge | End-to-end |
|---|---|---:|---:|---:|---:|---:|---:|
| Gold Nav robust-v1 | new | 665,822 | 446 | 3,152 | 572.7s | 1.1s | 574.1s |
| Pred Nav robust-v1 | new | 347,750 | 205 | 3,356 | 431.0s | 0.8s | 432.4s |
| TreeRAG | reused | 714,110 | 1,169 | 177 | 817.0s | 1101.9s | 2804.2s |
| Flat | reused | 388,761 | 731 | 155 | 846.1s | 1286.8s | 2133.0s |

- Gold audit: `446` API calls, `3152` cache hits.
- Pred audit: `205` API calls, `3356` cache hits.
- No TreeRAG or Flat rows are rerun in this summary.
