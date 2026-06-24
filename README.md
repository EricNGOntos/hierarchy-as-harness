# Hierarchy-as-Harness · RealData 共享输出预算基线（fair_clean）

本仓库包含 **RealData latest-clean** 上的端到端对比：Gold（金标层级 Nav Agent）、Flat、[TreeRAG](https://aclanthology.org/2025.findings-acl.20/) 基线。三方采用同一任务集、最终 evidence 字符预算、compose 与 judge；检索过程保留各方法自身的候选策略与成本，因此这是**共享输出预算协议**，不是等计算量协议。

- **任务**：51 题（niche / multi_hop / scope 各 17）
- **预算**：b500，三方共享最终 evidence 字符预算 + 方法无关 `[E1]`/`[E2]` header + 同一 compose + 同一 judge
- **Canonical 配置**：`goldnav_e2_v1`（见 [UNIFIED_FIX_PLAN.zh-CN.md](UNIFIED_FIX_PLAN.zh-CN.md)）

## 当前主结果（51 题 · b500 · goldnav_e2_v1）

| 方法 | 总体 | niche | multi | scope |
|------|-----:|------:|------:|------:|
| **Gold（nav）** | **0.504** | **0.824** | **0.157** | 0.530 |
| **TreeRAG** | 0.433 | **0.824** | 0.098 | 0.379 |
| Flat | 0.354 | 0.471 | 0.020 | **0.572** |

Gold−Flat bootstrap 95% CI `[0.027, 0.276]`；Gold−TreeRAG `[-0.046, 0.188]`（不能声称稳定优于 TreeRAG）。

**文档**：[results/summary.md](results/summary.md)（索引）· [results/paper_main_experiment.zh-CN.md](results/paper_main_experiment.zh-CN.md)（论文稿）

## Nav 架构

Gold Nav 采用 **[KnowWhere](https://github.com/Ontos-AI/knowhere)** 风格的三通道 hybrid discovery + LLM rerank：

1. **宽召回**：path BM25 + content BM25 + term 子串 → 加权 RRF
2. **LLM rerank**：导航模型挑选 1–3 个 section，暴露为 **D*** COLLECT 动作
3. **显式收集**：只有 agent 选择 COLLECT/SEARCH 后 evidence 才进入 pool

`bin/32` 默认 env：`NAV_DISCOVERY_SOFT_SIGNAL=1`，`NAV_DISCOVERY_RECALL_K=10`，`NAV_DISCOVERY_PICK_K=3`。

## 目录结构

```
├── bin/                 # 复跑与对比脚本
├── config/
├── data/tasks/          # 51 题 fair_clean + 可选 60 题外推集
├── results/             # canonical JSON + 摘要/论文 md
├── cache/               # 断点续跑（gitignore，不入库）
└── src/{realdata,nav,treerag}/
```

## 快速开始

### LLM 配置（勿提交密钥）

```bash
mkdir -p ~/.config/realdata_treerag
cp src/realdata/agent_delivery/llm_api.env.example ~/.config/realdata_treerag/llm_api.env
# 填入 OPENAI_API_KEY、OPENAI_BASE_URL、COMPOSE_MODEL 等；chmod 600
```

也可在仓库内复制为 `src/realdata/agent_delivery/llm_api.env`（已在 `.gitignore` 中，**不会**被 git 跟踪）。`llm_config.py` 优先读取用户级 `~/.config/realdata_treerag/llm_api.env`。

**安全**：切勿 commit `llm_api.env`、`.env*` 或 `cache/` 下的 LLM 响应缓存。

### 复跑

```bash
bash bin/32_run_quality_balanced_gold_flat.sh   # Gold + Flat
bash bin/35_run_quality_balanced60_treerag.sh   # TreeRAG
bash bin/21_compare_realdata_baselines.sh       # 对比表 → cache/
python3 tests/test_protocol.py -q
python3 tests/test_nav_improvements.py -q
```

## 实验口径

| 方法 | 检索 | 答题 |
|------|------|------|
| **Gold** | LLM Nav Agent（expand/collect/search + hybrid discovery D*） | 共享 compose + Inspect judge |
| **Flat** | flat_react 多轮 dense | 同上 |
| **TreeRAG** | LLM 建树 + intent + BTR | 同上 |
