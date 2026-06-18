# Hierarchy-as-Harness · RealData 公平协议基线（fair_clean）

本仓库包含 **RealData latest-clean** 上的端到端对比：Gold（金标层级 Nav Agent）、Flat、 [TreeRAG](https://aclanthology.org/2025.findings-acl.20/) 基线，**在一套完全公平的协议下**评测。

- **任务**：51 题（niche / multi_hop / scope 各 17，方法无关清洗 + 对称再平衡）
- **预算**：b500，三方共享同一预算 + 同一 compose + 同一 judge，**无任何按方法的候选上限**
- **路径泄漏**：已从所有方法的 query 中删除字面层级路径（详见 summary）
- **结果摘要**：[results/summary.md](results/summary.md)

> 诚实结论：公平协议下 **Gold（总体）> Flat**，但 **Gold < TreeRAG**。未做分数注水；差距与原因如实记录于 summary。

## Nav 架构（2026-06 起）

Gold Nav 采用 **[KnowWhere](https://github.com/Ontos-AI/knowhere)** 风格的三通道 hybrid discovery + LLM rerank：

1. **宽召回**：path BM25 + content BM25 + term 子串匹配 → 加权 RRF（默认 recall ~10 sections）
2. **LLM rerank**：导航模型从候选中挑选 1–3 个 section，暴露为 **D*** COLLECT 动作
3. **显式收集**：只有 agent 选择 COLLECT/SEARCH 后 evidence 才进入 pool；**不**做导航后硬注入

`bin/32` 默认 env：

| 变量 | 默认 | 说明 |
|------|------|------|
| `NAV_DISCOVERY_SOFT_SIGNAL` | `1` | 开启 hybrid discovery |
| `NAV_DISCOVERY_RECALL_K` | `10` | 三通道召回候选 section 数 |
| `NAV_DISCOVERY_PICK_K` | `3` | LLM rerank 最多挑选数（非硬 TOP-K 截断） |
| `NAV_DISCOVERY_LLM_RERANK` | `1` | LLM 置信度挑选；关则按 hybrid 分排序 |

可选：`pip install rank-bm25`（未安装时退化为 token overlap）

---

## 当前结果（公平协议 · 51 题 · b500）

| 方法 | 总体 | niche | multi | scope |
|------|-----:|------:|------:|------:|
| **TreeRAG** | **0.333** | 0.853 | 0.078 | 0.068 |
| **Gold（nav）** | 0.236 | 0.677 | 0.020 | 0.012 |
| Flat | 0.194 | 0.424 | 0.059 | 0.100 |

- Gold **> Flat（总体）**，主要来自 niche_fact；但 Gold 在 multi/scope 低于 Flat。
- Gold **< TreeRAG**（总体与各题型）。差距主因是 compose 环节（证据正确但复述不全），**非检索**；详见 [results/summary.md](results/summary.md)。
- **成本**：Gold/Flat 在线/离线均远低于 TreeRAG（后者需 ~881s 离线 LLM 切树）。导航后软兜底已改为“原生分数尺度 + 限量”（`NAV_SOFT_SAFETY_MAX_ADD`），修复了海量注入回归（+0.015）。

---

## 目录结构

```
├── bin/                 # 运行入口
├── config/              # Nav 配置
├── data/tasks/          # tasks_realdata_bodyrich_fair_clean*（公平清洗后 51 题）
├── results/
│   ├── fair_clean_gold_flat_fair_clean_v1_b500.json   # Gold + Flat（公平）
│   ├── fair_clean_treerag_fair_clean_v1_b500.json     # TreeRAG（公平，无 cap）
│   └── task_clean_log.json                            # 清洗/再平衡日志
├── cache/               # 断点续跑（不入库）
└── src/{realdata,nav,treerag}/
    └── nav/
        ├── knowhere_hybrid.py   # 三通道 RRF（移植自 KnowWhere）
        └── nav_discovery.py     # hybrid 召回 + LLM rerank
```

## 快速开始

```bash
git clone https://github.com/EricNGOntos/hierarchy-as-harness.git
cd hierarchy-as-harness

cp src/realdata/agent_delivery/llm_api.env.example src/realdata/agent_delivery/llm_api.env
# 填入 OPENAI_API_KEY 等

# Gold + Flat（KnowWhere hybrid discovery 默认开）
bash bin/32_run_quality_balanced_gold_flat.sh

# TreeRAG
bash bin/35_run_quality_balanced60_treerag.sh

# 三方法对比
bash bin/21_compare_realdata_baselines.sh
```

## 实验口径

| 方法 | 检索 | 答题 |
|------|------|------|
| **Gold** | LLM Nav Agent（expand/collect/search + hybrid discovery D* + 限量软兜底） | 共享 compose + Inspect judge |
| **Flat** | flat_react 多轮 dense | 同上 |
| **TreeRAG** | LLM 建树 + intent + BTR | 同上，**无候选上限**（仅 `TREERAG_FAIR_CAP=1` 可复现旧的截断行为） |

三方共享同一 `b500` 预算、同一 `_prepare_compose_evidence_text` compose 流水线、同一 `inspect_scoring`/`compose_llm` judge。

## 脚本

| 脚本 | 用途 |
|------|------|
| `bin/32_run_quality_balanced_gold_flat.sh` | Gold + Flat（默认指向 fair_clean） |
| `bin/35_run_quality_balanced60_treerag.sh` | TreeRAG（默认指向 fair_clean，无 cap） |
| `bin/21_compare_realdata_baselines.sh` | 对比表 |
| `bin/22_audit_task_quality.py` | 任务审计（`--mode audit`）/ 公平清洗（`--mode clean`） |
