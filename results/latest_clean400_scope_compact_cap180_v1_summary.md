# latest_clean400_scope_compact_cap180_v1 · Gold/Pred + reused baselines

This is the current canonical 400-row result. It is a cost-saving merge: only the 133 `scope_collection` rows were rerun with scope compact evidence and compose guidance; the 267 non-scope rows are reused unchanged from `latest_clean400_scope_outline_fixed_v1`.

## Quality

| Method | Status | Overall | Niche | Multi-hop | Scope | Evidence |
|---|---|---:|---:|---:|---:|---:|
| Gold Nav robust-v1 | new | 0.2111 | 0.2090 | 0.0777 | 0.3466 | 0.6188 |
| Pred Nav robust-v1 | new | 0.1450 | 0.1276 | 0.0601 | 0.2474 | 0.4213 |
| TreeRAG | reused | 0.2016 | 0.1522 | 0.0831 | 0.3698 | 0.5125 |
| Flat | reused | 0.1376 | 0.0903 | 0.0683 | 0.2547 | 0.4988 |

## Paired Bootstrap

- `gold_minus_pred`: mean `+0.0661`, 95% CI `[+0.0372, +0.0957]`, win/loss/tie `71/31/298`
- `gold_minus_treerag`: mean `+0.0095`, 95% CI `[-0.0236, +0.0428]`, win/loss/tie `67/68/265`
- `gold_minus_flat`: mean `+0.0735`, 95% CI `[+0.0385, +0.1092]`, win/loss/tie `94/44/262`
- `pred_minus_treerag`: mean `-0.0566`, 95% CI `[-0.0891, -0.0242]`, win/loss/tie `44/81/275`
- `pred_minus_flat`: mean `+0.0074`, 95% CI `[-0.0227, +0.0383]`, win/loss/tie `59/59/282`
- `treerag_minus_flat`: mean `+0.0640`, 95% CI `[+0.0327, +0.0960]`, win/loss/tie `76/39/285`

## Cost And Reuse

Gold/Pred costs below are the incremental scope-only rerun costs, not the cost of rerunning all 400 rows from scratch.

| Arm | Status | Billed tokens | API calls | Cache hits | Online response | Judge | End-to-end |
|---|---|---:|---:|---:|---:|---:|---:|
| Gold Nav robust-v1 | new | 688,517 | 453 | 676 | 572.7s | 1.1s | 574.1s |
| Pred Nav robust-v1 | new | 405,213 | 252 | 862 | 431.0s | 0.8s | 432.4s |
| TreeRAG | reused | 714,110 | 1,169 | 177 | 817.0s | 1101.9s | 2804.2s |
| Flat | reused | 388,761 | 731 | 155 | 846.1s | 1286.8s | 2133.0s |

- Gold audit: `453` API calls, `676` cache hits.
- Pred audit: `252` API calls, `862` cache hits.
- No TreeRAG or Flat rows are rerun in this summary.
