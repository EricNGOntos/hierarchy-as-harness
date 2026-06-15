# balanced60 实验结果摘要（costclean_v1 / b500）

## 实验设置

- **任务数**：60（`niche_fact` 20 + `multi_hop` 20 + `scope_collection` 20）
- **字符预算**：500
- **口径**：costclean（`BODYRICH_LLM_API_CACHE=0`，不读 LLM 响应缓存）
- **对比方法**：Gold（金标层级 Nav Agent）、Flat（扁平检索）、TreeRAG（论文式树检索 + 共享 compose/judge）
- **任务文件**：`data/tasks/tasks_realdata_bodyrich_latest_clean_quality_balanced60.jsonl`
- **结果文件**：
  - Gold/Flat：`results/latest_clean_quality_balanced60_gold_flat_quality_balanced60_costclean_v1_b500.json`
  - TreeRAG：`results/latest_clean_treerag_quality_balanced60_costclean_v1_b500.json`

## 总体对比（score_task_mean）

| 方法 | 任务得分 | 证据得分 |
|------|---------:|---------:|
| **Gold** | **0.479** | **0.849** |
| TreeRAG | 0.409 | 0.569 |
| Flat | 0.305 | 0.528 |

**排序**：Gold > TreeRAG > Flat。

## 分题型对比（score_task_mean）

| 题型 | n | Gold | TreeRAG | Flat | 最优 |
|------|--:|-----:|--------:|-----:|------|
| niche_fact（细节事实） | 20 | **0.850** | 0.800 | 0.450 | Gold |
| multi_hop（多跳推理） | 20 | **0.467** | 0.367 | 0.367 | Gold |
| scope_collection（范围收集） | 20 | **0.119** | 0.061 | 0.098 | Gold |

三类题型上 **Gold 均优于 TreeRAG 和 Flat**。其中 niche 差距最大（Gold 0.85 vs Flat 0.45），multi_hop 上 TreeRAG 与 Flat 基本持平，scope 三类得分都偏低但 Gold 仍领先。

## 简要结论

1. **层级结构有收益**：Gold 在 60 题总分上比 Flat 高约 17 个百分点，说明金标层级导航对端到端答题有帮助。
2. **Gold 全面领先 TreeRAG**：总分 0.479 vs 0.409，三类题型均为 Gold 最高。
3. **niche 是主要拉分项**：Gold niche 达 0.85，TreeRAG 0.80，Flat 仅 0.45。
4. **scope 仍是短板**：三类方法在 scope_collection 上得分都低（< 0.12），需单独分析任务难度或检索策略。
5. **成本**：Gold 检索耗时较长（~670s），Flat 检索最快（~11s），TreeRAG 冷启动建索引约 691s、在线检索约 33s。
