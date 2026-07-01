# latest_clean400_scope_compact_cap180_scope133_v1 · Gold/Pred + reused baselines

## Quality

| Method | Status | Overall | Niche | Multi-hop | Scope | Evidence |
|---|---|---:|---:|---:|---:|---:|
| Gold Nav robust-v1 | new | 0.3466 | 0.0000 | 0.0000 | 0.3466 | 0.5823 |
| Pred Nav robust-v1 | new | 0.2474 | 0.0000 | 0.0000 | 0.2474 | 0.3610 |
| TreeRAG | reused | 0.3698 | 0.0000 | 0.0000 | 0.3698 | 0.5564 |
| Flat | reused | 0.2547 | 0.0000 | 0.0000 | 0.2547 | 0.4249 |

## Paired Bootstrap

- `gold_minus_pred`: mean `+0.0992`, 95% CI `[+0.0482, +0.1516]`, win/loss/tie `46/22/65`
- `gold_minus_treerag`: mean `-0.0232`, 95% CI `[-0.0829, +0.0364]`, win/loss/tie `39/44/50`
- `gold_minus_flat`: mean `+0.0920`, 95% CI `[+0.0318, +0.1533]`, win/loss/tie `57/24/52`
- `pred_minus_treerag`: mean `-0.1224`, 95% CI `[-0.1877, -0.0571]`, win/loss/tie `29/53/51`
- `pred_minus_flat`: mean `-0.0073`, 95% CI `[-0.0655, +0.0512]`, win/loss/tie `36/37/60`
- `treerag_minus_flat`: mean `+0.1152`, 95% CI `[+0.0564, +0.1742]`, win/loss/tie `46/20/67`

## Cost And Reuse

| Arm | Status | Billed tokens | API calls | Cache hits | Online response | Judge | End-to-end |
|---|---|---:|---:|---:|---:|---:|---:|
| Gold Nav robust-v1 | new | 688,517 | 453 | 676 | 493.4s | 0.5s | 494.2s |
| Pred Nav robust-v1 | new | 405,213 | 252 | 862 | 336.3s | 0.4s | 337.3s |
| TreeRAG | reused | 714,110 | 1,169 | 177 | 817.0s | 1101.9s | 2804.2s |
| Flat | reused | 388,761 | 731 | 155 | 846.1s | 1286.8s | 2133.0s |

- Gold audit: `453` API calls, `676` cache hits.
- Pred audit: `252` API calls, `862` cache hits.
- No TreeRAG or Flat rows are rerun in this summary.
