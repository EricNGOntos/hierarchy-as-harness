# Hierarchy-as-Harness · RealData 共享输出预算基线（fair_clean）

本仓库包含 **RealData latest-clean** 上的端到端对比：Gold（金标层级 Nav Agent）、Flat、 [TreeRAG](https://aclanthology.org/2025.findings-acl.20/) 基线。三方采用同一任务集、最终 evidence 字符预算、compose 与 judge；检索过程保留各方法自身的候选策略、工具调用和预处理成本，因此这是**共享输出预算协议**，不是等计算量协议。

- **任务**：51 题（niche / multi_hop / scope 各 17，方法无关清洗 + 对称再平衡）
- **预算**：b500，三方共享最终 evidence 字符预算 + 方法无关 `[E1]`/`[E2]` header + 同一 compose + 同一 judge；不做跨方法候选数匹配截断，各方法仍使用自身的检索上限
- **路径泄漏**：已从所有方法的 query 中删除字面层级路径
- **结果摘要**：[results/summary.md](results/summary.md)

## Nav 架构

Gold Nav 采用 **[KnowWhere](https://github.com/Ontos-AI/knowhere)** 风格的三通道 hybrid discovery + LLM rerank：

1. **宽召回**：path BM25 + content BM25 + term 子串匹配 → 加权 RRF
2. **LLM rerank**：导航模型挑选 1–3 个 section，暴露为 **D*** COLLECT 动作
3. **显式收集**：只有 agent 选择 COLLECT/SEARCH 后 evidence 才进入 pool；**无**导航后 soft_safety 注入

`bin/32` 默认 env：`NAV_DISCOVERY_SOFT_SIGNAL=1`，`NAV_DISCOVERY_RECALL_K=10`，`NAV_DISCOVERY_PICK_K=3`。

---

## 当前结果（51 题 · b500 · scopefix_v2）

| 方法 | 总体 | niche | multi | scope |
|------|-----:|------:|------:|------:|
| **Gold（nav）** | **0.422** | **0.794** | 0.078 | 0.392 |
| **TreeRAG** | 0.398 | **0.765** | 0.078 | 0.351 |
| Flat | 0.373 | 0.482 | 0.059 | **0.578** |

Gold、TreeRAG、Flat 总体互有胜负，当前样本不足以稳定区分总体优劣。逐题 bootstrap 95% CI：Gold−TreeRAG `[-0.090, 0.148]`，Gold−Flat `[-0.070, 0.203]`，TreeRAG−Flat `[-0.097, 0.175]`。详见 [results/summary.md](results/summary.md)。

---

## 目录结构

```
├── bin/
├── config/
├── data/tasks/          # tasks_realdata_bodyrich_fair_clean*（51 题）
├── results/
│   ├── fair_clean_gold_flat_fair_clean_scopefix_v2_b500.json
│   ├── fair_clean_treerag_fair_clean_scopefix_v2_b500.json
│   ├── task_clean_log.json
│   └── summary.md
├── cache/               # 断点续跑（不入库）
└── src/{realdata,nav,treerag}/
```

## 快速开始

```bash
cp src/realdata/agent_delivery/llm_api.env.example src/realdata/agent_delivery/llm_api.env
# 填入 OPENAI_API_KEY 等

bash bin/32_run_quality_balanced_gold_flat.sh   # Gold + Flat
bash bin/35_run_quality_balanced60_treerag.sh   # TreeRAG
bash bin/21_compare_realdata_baselines.sh       # 对比表
```

## 实验口径

| 方法 | 检索 | 答题 |
|------|------|------|
| **Gold** | LLM Nav Agent（expand/collect/search + hybrid discovery D*） | 共享 compose + Inspect judge |
| **Flat** | flat_react 多轮 dense | 同上 |
| **TreeRAG** | LLM 建树 + intent + BTR（自身 top-k / traversal 配置） | 同上 |

三方共享 b500、同一 budget fill / compose / judge 流水线。Gold Nav、Flat-ReAct 与 TreeRAG 的检索轮数、候选上限、LLM 调用和离线建树成本属于方法本身，不强行对齐；成本指标应与质量指标分开解读。
