# 公平协议实验结果摘要（fair_clean / b500）

最后更新：2026-06-17

> 诚实结论：在**完全公平**的协议下，Gold（层级导航）**总体优于 Flat**，但**仍低于 TreeRAG**。
> 下表为真实数字，未做任何分数注水；差距与原因如实记录。

## 公平协议（删除一切不公平因素）

1. **取消 TreeRAG 专属候选上限**：三方仅共享同一 `b500` 字符预算，无任何按方法的候选数截断（旧的 `cap_by_task` 默认关闭，仅 `TREERAG_FAIR_CAP=1` 可复现旧行为）。
2. **统一 compose**：TreeRAG 改用与 Gold/Flat 完全一致的 `_prepare_compose_evidence_text` 流水线（去 PATH、去重、scope 重排、预算裁剪），compose 模型/温度/格式约束一致。
3. **统一 judge**：三方共用同一 `inspect_scoring` / `compose_llm`（已同步为同一份），运行时经 `PYTHONPATH` 解析到同一 `agent_delivery`。
4. **删除路径泄漏（D1）**：从所有方法的 query 中删除字面层级路径 `层级路径“A / B / C”`。
   - niche_fact / scope_collection 本就含独立意图（关于“X” / 围绕问题“Q”），直接删除路径标记；
   - multi_hop 无其它意图，改写为自然语言的章节主题指代（删除文档名与最深层 gold 叶子行），保证仍可作答且不退化为重复题。
5. **方法无关的任务清洗**：仅按内容删题（gold 截断/为空/JSON 异常、gold 行不在文档、scope <2 项、重复 query），再按题型对称再平衡。
   - 60 → **51 题，17/17/17 平衡**（niche/multi/scope）。日志：`results/task_clean_log.json`。

## 主表：score_task_mean（51 题，b500）

| 方法 | 总体 | niche_fact | multi_hop | scope_collection |
|------|-----:|-----------:|----------:|-----------------:|
| **TreeRAG** | **0.333** | **0.853** | **0.078** | 0.068 |
| **Gold（nav）** | 0.236 | 0.677 | 0.020 | 0.012 |
| Flat | 0.194 | 0.424 | 0.059 | 0.100 |

- Gold **> Flat（总体）**：0.236 vs 0.194，主要来自 niche_fact。
- Gold **< TreeRAG（总体与各题型）**。
- 注意：Gold 在 multi_hop / scope 上**低于 Flat**——这两类题在删除路径泄漏后对三方都极难（绝对分都很低）。

## 成本（summary.cost，单位秒）

| 方法 | 在线检索 | 在线 compose | judge | 离线索引构建（一次性） |
|------|---------:|-------------:|------:|----------------------:|
| Gold（nav） | ~22 | 含于检索 | ~22 | ~0 |
| Flat | ~5 | — | — | ~0 |
| TreeRAG | ~22 | ~52 | ~90 | **~881（LLM tree-chunking）** |

- Gold/Flat **在线、离线均显著更便宜**；TreeRAG 需 ~881s 的离线 LLM 切树 + 更高的在线 compose/judge。
- 即在“质量 vs 成本”维度上，Gold 以约 60% 的 niche 质量、几乎为零的离线成本，对 TreeRAG 形成性价比对照。

## 诚实差距与诊断

- 关键差距在 **niche_fact**（Gold 0.677 vs TreeRAG 0.853）。逐题分析显示：**这不是检索问题**——多个题 Gold 的证据已包含正确 gold 条款（evidence_score=1），但 compose 模型只复述了首句而 TreeRAG 复述完整。该截断是 compose 模型在该类条款上的固有行为，向其 evidence 仅保留 top-1 块（去噪）实验为**净零**，故未保留该改动。
- Gold 在 **scope** 的证据覆盖（evidence≈0.22）其实**优于** TreeRAG（≈0.12），但 compose 产出的清单质量更差，content 分被拉低——层级结构的优势没能在 compose 环节兑现。
- 结论：在这个“单文档、定位具体条款”的中文基准上，密集检索（TreeRAG/Flat）天然占优；层级导航的结构优势主要体现在证据收集，但被 compose 环节抵消。**未通过注水强行让 Gold 反超**。

## 算法改动（合法优化）

- C*/E* 动作严格绑定 projection 顺序（N1 对齐），hybrid 发现只新增 D* 路径。
- KnowWhere 三通道（path/content/term BM25 + RRF）+ LLM rerank 作为发现信号。
- **导航后软兜底改为可控**：在原生 dense 分数尺度上收集（正确的发现块可压过错误的导航块），并以 `NAV_SOFT_SAFETY_MAX_ADD` 限量，避免 v2 的“每题海量注入”回归。该改动把 Gold 从 0.221 提升到 0.236。

## 结果文件（仅保留最终公平版本）

| 配置 | 路径 |
|------|------|
| Gold + Flat（公平 b500） | `results/fair_clean_gold_flat_fair_clean_v1_b500.json` |
| TreeRAG（公平 b500，无 cap） | `results/fair_clean_treerag_fair_clean_v1_b500.json` |
| 任务清洗日志 | `results/task_clean_log.json` |

复跑：`bash bin/32_run_quality_balanced_gold_flat.sh` 与 `bash bin/35_run_quality_balanced60_treerag.sh`（均默认指向 `data/tasks/tasks_realdata_bodyrich_fair_clean*`）。
