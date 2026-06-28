# goldnav_e2_v1 独立抽样验证

- 日期：2026-06-24
- 母集：`tasks_realdata_bodyrich_latest_clean_400.jsonl`
- 抽样：固定随机种子 `20260624`，niche / multi_hop / scope 各20题，共60题
- 去重：对旧51题版本排除 exact id/query、`doc_id + gold_nodes` 及 `doc_id + gold_answer` 重合
- 评测：当前 `main` 的 Gold Nav / TreeRAG / Flat，b500，Inspect judge（同任务集、同 compose/judge 协议）
- TreeRAG 建树 LLM 超时：`TREERAG_LLM_TIMEOUT_SECONDS=120`（默认由 20s 上调，避免 `tree_chunking` 频繁 APITimeout）

## 结果

| 方法 | 总体内容分 | niche | multi_hop | scope | 证据分 |
|---|---:|---:|---:|---:|---:|
| Gold Nav | 0.145 | 0.200 | 0.033 | 0.201 | 0.536 |
| TreeRAG | 0.125 | 0.150 | 0.000 | 0.226 | 0.450 |
| Flat | 0.075 | 0.005 | 0.058 | 0.161 | 0.497 |

Gold Nav 内容分 bootstrap 95% CI 为 `[0.075, 0.225]`。Gold Nav 相对 Flat 的配对均值差为 `+0.070`，95% CI 为 `[-0.010, 0.155]`。

完整评测 JSON 体积较大、未入库；指标见上表。任务文件：`data/tasks/tasks_realdata_bodyrich_goldnav_e2_v1_60.jsonl`

## 完整性检查

- 60/60 题完成，三类各20题，Inspect 记录全部对齐
- 与旧51题的 query 重合数和稳定语义指纹重合数均为0
- 抽样题涉及的文档在评测 corpus 中全部存在
- Gold Nav、TreeRAG 和 Flat 的 Inspect judge 使用率均为100%
- 项目协议测试 11/11 通过

## 结论

该独立 60 题样本未复现 51 题 canonical Gold Nav 的 **0.504**。新样本上 Gold Nav（0.145）仍高于 Flat（0.075），TreeRAG（0.125）介于两者之间；Gold−Flat 差异的 95% CI 跨 0。两次评测题集不同，只能作外推对照，不是同题回归比较。
