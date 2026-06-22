# Hierarchy-as-Harness · RealData 公平协议基线（fair_clean）

本仓库包含 **RealData latest-clean** 上的端到端对比：Gold（金标层级 Nav Agent）、Flat、 [TreeRAG](https://aclanthology.org/2025.findings-acl.20/) 基线，**在一套完全公平的协议下**评测。

- **任务**：51 题（niche / multi_hop / scope 各 17，方法无关清洗 + 对称再平衡）
- **预算**：b500，三方共享同一预算 + 同一 compose + 同一 judge，**无任何按方法的候选上限**
- **路径泄漏**：已从所有方法的 query 中删除字面层级路径
- **结果摘要**：[results/summary.md](results/summary.md)

## Nav 架构

Gold Nav 采用 **[KnowWhere](https://github.com/Ontos-AI/knowhere)** 风格的三通道 hybrid discovery + LLM rerank：

1. **宽召回**：path BM25 + content BM25 + term 子串匹配 → 加权 RRF
2. **LLM rerank**：导航模型挑选 1–3 个 section，暴露为 **D*** COLLECT 动作
3. **显式收集**：只有 agent 选择 COLLECT/SEARCH 后 evidence 才进入 pool；**无**导航后 soft_safety 注入

`bin/32` 默认 env：`NAV_DISCOVERY_SOFT_SIGNAL=1`，`NAV_DISCOVERY_RECALL_K=10`，`NAV_DISCOVERY_PICK_K=3`。

---

## 当前结果（51 题 · b500 · Unified Fix）

| 方法 | 总体 | niche | multi | scope |
|------|-----:|------:|------:|------:|
| **TreeRAG** | **0.338** | 0.853 | 0.098 | **0.063** |
| **Gold（nav）** | 0.336 | **0.853** | **0.118** | 0.038 |
| Flat | 0.194 | 0.424 | 0.059 | 0.100 |

Gold **> Flat**；Gold **≈ TreeRAG**（总体持平，分题型互有胜负）。详见 [results/summary.md](results/summary.md)。

---

## 目录结构

```
├── bin/
├── config/
├── data/tasks/          # tasks_realdata_bodyrich_fair_clean*（51 题）
├── results/
│   ├── fair_clean_gold_flat_fair_clean_unified_v1_b500.json
│   ├── fair_clean_treerag_fair_clean_unified_v2_b500.json
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
| **TreeRAG** | LLM 建树 + intent + BTR | 同上，无候选上限 |

三方共享 b500、同一 evidence 拼装与 judge 流水线。
