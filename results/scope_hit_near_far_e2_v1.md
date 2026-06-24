# Scope 17 题 HIT/NEAR/FAR 分类（goldnav_e2_v1 · Gold arm）

日期：2026-06-24  
来源：`results/fair_clean_gold_flat_fair_clean_goldnav_e2_v1_b500.json`

分类规则（Gold arm）：

- **HIT**：`evidence_coverage ≥ 0.5` 且 `score_task ≥ 0.3`
- **NEAR**：非 HIT 且 gold 行与 retrieved 行最小距离 `≤ 2`
- **FAR**：其余

## 汇总

| 类别 | 数量 |
|------|-----:|
| HIT | 10 |
| NEAR | 7 |
| FAR | 0 |

相对 scopefix_v2 诊断（HIT 7 / NEAR 5 / FAR 5）：FAR 归零，NEAR 仍有多题 task=0（预算/compose 瓶颈）。

## 逐题

| inspect_id | 类别 | task | coverage | min_dist |
|------------|------|-----:|---------:|---------:|
| q400_scope_0001 | HIT | 0.500 | 0.500 | 0 |
| q400_scope_0002 | HIT | 0.667 | 0.667 | 0 |
| q400_scope_0003 | NEAR | 0.167 | 0.167 | 0 |
| q400_scope_0004 | HIT | 1.000 | 1.000 | 0 |
| q400_scope_0005 | NEAR | 0.000 | 0.333 | 0 |
| q400_scope_0006 | HIT | 0.667 | 0.667 | 0 |
| q400_scope_0007 | NEAR | 0.000 | 0.333 | 0 |
| q400_scope_0008 | NEAR | 0.083 | 0.083 | 0 |
| q400_scope_0009 | HIT | 1.000 | 1.000 | 0 |
| q400_scope_0010 | HIT | 1.000 | 1.000 | 0 |
| q400_scope_0011 | HIT | 1.000 | 1.000 | 0 |
| q400_scope_0012 | NEAR | 0.000 | 0.000 | 2 |
| q400_scope_0013 | HIT | 1.000 | 1.000 | 0 |
| q400_scope_0014 | HIT | 1.000 | 1.000 | 0 |
| q400_scope_0015 | NEAR | 0.000 | 0.000 | 1 |
| q400_scope_0016 | NEAR | 0.262 | 0.500 | 0 |
| q400_scope_0017 | HIT | 0.667 | 0.500 | 0 |

## 解读

- **NEAR 且 task=0**（0005/0007/0012/0015）：导航已到 gold 附近或已有部分 coverage，但 compose/judge 未拿满分 → 不是纯召回问题。
- **Flat scope 0.572 > Gold 0.530**：列表型检索在 scope 上仍有优势；D1 outline 留作 future work。
