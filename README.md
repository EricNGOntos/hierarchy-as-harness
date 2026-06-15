# Hierarchy-as-Harness · RealData balanced60 基线

本仓库包含 **RealData latest-clean** 上的 60 题端到端对比实验：在金标层级（Gold）、扁平检索（Flat）与 [TreeRAG](https://aclanthology.org/2025.findings-acl.20/) 基线之间，评估层级结构对长文档问答的帮助。

- **任务规模**：60 题（`niche_fact` / `multi_hop` / `scope_collection` 各 20 题）
- **字符预算**：500（`b500`）
- **评测口径**：costclean（`BODYRICH_LLM_API_CACHE=0`，不读取 LLM 响应缓存）
- **详细结果**：[results/summary.md](results/summary.md)

## 主要结果（score_task_mean）

| 方法 | 总分 | niche_fact | multi_hop | scope_collection |
|------|-----:|-----------:|----------:|-----------------:|
| **Gold** | **0.479** | **0.850** | **0.467** | **0.119** |
| TreeRAG | 0.409 | 0.800 | 0.367 | 0.061 |
| Flat | 0.305 | 0.450 | 0.367 | 0.098 |

Gold 在总分及三类题型上均优于 TreeRAG 和 Flat。层级导航相对 Flat 总分提升约 17 个百分点；niche 题型差距最大，scope 三类方法得分均偏低。

证据得分（`score_evidence_mean`）：Gold **0.849** > TreeRAG 0.569 > Flat 0.528。

## 目录结构

```
├── bin/                 # 运行入口
├── config/              # Nav Agent 配置
├── data/
│   ├── corpus/          # latest-clean 语料（195 篇文档）
│   └── tasks/           # balanced60 任务 + inspect 注册表
├── results/             # 最终结果 JSON 与中文摘要
├── cache/               # 断点续跑缓存（本地生成，不入库）
└── src/
    ├── realdata/        # Gold/Flat runner、检索、compose/judge
    ├── nav/             # Nav Agent 与 TreeRAG wrapper
    └── treerag/         # TreeRAG paper-style adapter
```

## 快速开始

### 1. 克隆与依赖

```bash
git clone https://github.com/EricNGOntos/hierarchy-as-harness.git
cd hierarchy-as-harness
# 按本地环境安装依赖（torch、sentence-transformers、openai 等）
```

### 2. 配置 API

```bash
cp src/realdata/agent_delivery/llm_api.env.example src/realdata/agent_delivery/llm_api.env
cp src/treerag/agent_delivery/llm_api.env.example src/treerag/agent_delivery/llm_api.env
# 编辑两处 llm_api.env，填入 OPENAI_API_KEY、OPENAI_BASE_URL 等
```

`llm_api.env` 已在 `.gitignore` 中排除，不会提交到 GitHub。

### 3. 运行

```bash
# 离线对齐检查（无需 API）
bash bin/11_run_latest_treerag_check.sh

# Gold + Flat 端到端
BODYRICH_LLM_API_CACHE=0 bash bin/32_run_quality_balanced_gold_flat.sh

# TreeRAG 端到端（compose + judge）
BODYRICH_LLM_API_CACHE=0 bash bin/35_run_quality_balanced60_treerag.sh

# 三方法对比表（输出到 cache/compare_run_summary.md）
bash bin/21_compare_realdata_baselines.sh
```

中断后重跑同一命令即可从 `cache/` 断点续跑。

## 实验口径

| 方法 | 检索 | 答题与评分 |
|------|------|-----------|
| **Gold** | Nav Agent + 金标层级图 | 共享 compose/judge + Inspect |
| **Flat** | 扁平 dense 检索 | 同上 |
| **TreeRAG** | LLM 树分块 + intent + 双向遍历 | 同上（fair cap 与 Gold/Flat 候选数对齐） |

- **语料**：`data/corpus/test_data_full_realdata_clean_latest.jsonl`
- **任务**：`data/tasks/tasks_realdata_bodyrich_latest_clean_quality_balanced60.jsonl`
- **结果**：
  - Gold/Flat：`results/latest_clean_quality_balanced60_gold_flat_quality_balanced60_costclean_v1_b500.json`
  - TreeRAG：`results/latest_clean_treerag_quality_balanced60_costclean_v1_b500.json`

## 脚本说明

| 脚本 | 用途 |
|------|------|
| `bin/11_run_latest_treerag_check.sh` | 任务/语料对齐检查 |
| `bin/32_run_quality_balanced_gold_flat.sh` | 重跑 Gold + Flat |
| `bin/35_run_quality_balanced60_treerag.sh` | 重跑 TreeRAG |
| `bin/21_compare_realdata_baselines.sh` | 生成三方法对比表 |
| `bin/22_audit_task_quality.py` | 任务质量审计 |
| `bin/25_check_llm_endpoint.py` | API 连通性检查 |
