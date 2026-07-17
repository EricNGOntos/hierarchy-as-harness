# Map-Nav 实验总结（2026-07-16）

本文记录当日从 **packing / recursive-dispatch 落地**、到 **400 题 evidence + 问答评估**、再到 **回归诊断与产物清理** 的完整过程。权威结果以文末「保留产物」为准；中间 replay / 临时 id 已清理。

---

## 1. 一句话结论

在 **贪心打包（回退至 `07c41a5` 风格）+ `enable_recursive_dispatch=true` + 智增增单一网关** 配置下，对 `latest_clean400` 全量 400 题：

| 指标 | 数值 |
|------|------|
| Evidence `gold_node_recall` 均值 | **0.744** |
| Evidence recall=0 题数 | **58 / 400** |
| Inspect `score_task_mean` | **0.242** |
| Inspect `score_evidence_mean` | **0.744** |

相对仓库内旧 baseline（Gold / Flat / TreeRAG / scope_compact）：**overall task 与 overall evidence 均领先**；niche 的 evidence 很高（≈0.90）但 task 略低于 Gold hierarchical（≈0.19 vs ≈0.21），瓶颈主要在 **compose/Inspect 严判**，不是 coverage 算错。

---

## 2. 当日目标与时间线

### 2.1 代码侧（上午–下午）

1. 核对并落地方案 `nav_packing_and_recursive_dispatch`（Part 1 打包语义 + Part 2 递归分派 / title-only）。
2. 确认大 scope 超阈值时切 **title-only**，阈值改为 **`evidence_budget × 3 = 1500`**（配置项 `scope_inline_summary_char_limit`）。
3. 明确 subagent / 外部 rerank 职责：**子层只采集与报告，最终证据排序交给外层 COMPOSE + 可选 external rerank**；confidence/子层先验进打包 tiebreak **只留 TODO，未实现**。
4. 屏蔽 / 删除 **scope outline 关键词特判**（只采前几行标题），MAP 模式 COLLECT 改为 **整枝文档序水合**，截断交给 COMPOSE。
5. 实测难例 TRACE 审计：预算截断、outline 欠采、平级章节偏置等失败模式。

### 2.2 评测侧（下午–晚上）

1. 对齐 LLM：一度尝试 Qwen/DeepSeek 官方分流；后确认相对 baseline 真正差异在 **网关**，改回 **智增增 `OPENAI_*` 单一端点**。
2. 全量 400 evidence（中间出现「新打包」严重回归）→ 与 `07c41a5` A/B → 打包回退 + 保留 recursive。
3. 难例并集 91 题重跑 → 其余 309 三分片并发 → 合并为 `replay_400_merged_latest`。
4. 冻结 evidence 上跑 compose + Inspect judge。
5. 清理中间实验产物，只保留最新 400 evidence + QA（及论文对照 baseline）。

---

## 3. 代码与设计变更（当日定稿）

### 3.1 导航算法（recursive dispatch）

- 默认 **`enable_recursive_dispatch=true`**，`max_dispatch_depth=3`。
- 动作空间仍为 **COLLECT / DISPATCH / FINISH**（无 EXPAND/JUMP/PEEK/BACK）。
- scoped map 预估超过 `scope_inline_summary_char_limit`（**1500**）时改为 **title-only**，软促使继续 DISPATCH。
- highlight 透传到各递归层。

### 3.2 证据打包（关键回归点，后回退）

当日一度改为「按 `selection_count` 剪尾 / 文档序优先、不再贪心填满」的新打包，导致大量 **预算未用满却丢掉 gold**，以及「同 COLLECT 进池、出池却丢 gold」的回归。

**定稿回退**到 `07c41a5` 风格：

- 按最近父分组；组间 `group_priority`（外部 FINISH `group_rank`）优先；
- 组内文档序；**贪心填满预算**（大块放不下可跳过、继续塞能进剩余预算的短块）；
- 父节点未显式选中时只作路径表头，不与子块抢预算；
- `compose_confidence_weight` 参与旧版 `own_unit + w_conf·conf` 打分（与 07c41a5 一致）。

### 3.3 水合与死代码清理

- MAP COLLECT：**整枝文档序水合**（不再按 unit score / `collect_k` 在进池前截断）。
- 删除未再使用的 **scope outline / `scope_evidence_locked`** 等死路径。
- 任务类型标签仍可出现在答题/评测侧；**检索阶段不再靠关键词硬切到 outline-only**。

### 3.4 LLM 配置

- 调用统一为 `OPENAI_API_KEY` + `OPENAI_BASE_URL=https://api.zhizengzeng.com/v1`。
- 默认模型：`NAV_LLM_MODEL` / `COMPOSE_MODEL` = `qwen3.5-flash`，`JUDGE_MODEL` = `deepseek-v4-pro`（均走智增增）。
- `QWEN_KEY` / `DS_KEY` 可留在本地 env 供以后消融；**DashScope 的 QWEN_KEY 不能直接打智增增**。

相关提交大致对应：`f5a2f67`（打包回退）、`1a05e70`（网关收束 + 合并脚本 + 结果入库）。

---

## 4. 评测协议与脚本

| 阶段 | 脚本 | 说明 |
|------|------|------|
| Evidence replay | `bin/56_replay_map_nav_traces.py` | 按 `inspect_id` 列表跑导航 + 打包，写出 TRACE / `gold_node_recall` |
| 合并 400 | `bin/60_merge_replay_400.py` | 将难例 91 ∪ 其余 309 合并为完整目录 |
| 冻结 evidence → QA | `bin/59_compose_judge_from_evidence.py` | compose 答题 + Inspect judge，不重跑导航 |

- 任务集：`data/tasks/tasks_realdata_bodyrich_latest_clean_400.jsonl`（+ inspect 侧 jsonl）
- Evidence / compose 预算：**500 字符**（`b500`）
- Arm key：`hierarchical_gold_map`（gold 树 + map-nav）

---

## 5. Evidence 实验过程（数字账本）

> 中间目录（坏打包 400、union、shards、268、A/B）已删除；下表数字来自当日实测记录。

### 5.1 「坏打包」全量 400（当日中间态）

新打包 + recursive 的一次全量：

- recall 均值约 **0.77**
- **zero = 66**

相对旧 268 / baseline，另定义 **68 题「严格变差」回归子集**（含未归零但变差的题）。  
注意：**66 ≠ 68**——前者是「今天 recall=0」，后者是「相对旧结果变差」。

### 5.2 与 `07c41a5` 的 A/B（68 回归题）

在导航 prompt 可缓存命中（决策相近）的前提下，差异主要来自打包：

| | 当天 HEAD（recursive + 新打包） | `07c41a5`（无 recursive + 贪心打包） |
|--|--|--|
| recall 均值 | 0.195 | **0.527** |
| recall=0 | 43 | **17** |

- 旧版救回约 **38** 题；其中约 **26** 题是「今天=0 → 旧版>0」（纯打包）。
- 结论：**回归主因是打包重写，不是 recursive 单独造成。**

### 5.3 定稿配置下的难例并集 91（66∪68）

配置：贪心打包 + recursive=on + 智增增。

| 口径 | 坏打包 HEAD | 定稿配置 |
|------|-------------|----------|
| 并集 91 recall 均值 | 0.146 | **0.426** |
| 并集 zero | 66 | **38** |
| 原 66 zero 中救回 | — | **28** 题变为 >0 |

同贪心打包下，recursive ON vs `07c41a5` OFF（在 68 子集）：更好 20 / 相同 37 / 更差 11，均值 **0.527 → 0.558**（净正，但不稳赚）。

### 5.4 其余 309 + 合并全量 400（权威 evidence）

| 子集 | 坏打包 HEAD | 合并后定稿 |
|------|-------------|------------|
| 难例 91 | mean 0.146，zero 66 | mean **0.426**，zero **38** |
| 其余 309 | mean 0.953，zero 0 | mean **0.837**，zero **20** |
| **全 400** | mean 0.770，zero 66 | mean **0.744**，zero **58** |

账本：救回 28 − 新掉零 20 = **净少 8 个 zero**（66→58）。  
难例确实变好；全量均值略降，是因为 **309 里有 67 题变差**（含 20 个新 zero）拖累。

对 67 题变差的拆分（当日分析）：

| 类型 | 题数 | 新 zero | 含义 |
|------|------|---------|------|
| 同 COLLECT，打包/水合丢 gold | ~37 | ~9 | 选点不变，出池块变了 |
| 导航选点变了 | ~30 | ~11 | collect 目标 / recursive 路径变化 |
| 题型分布 | scope 偏多 | — | scope 回归最明显 |

对 **20 个新 zero** 关 recursive 的小 A/B：仅 **1/20** 变好 → **主因不是 recursive**，而是整枝灌池 + 贪心挤 gold，以及部分选点变化。

### 5.5 权威 Evidence 产物

目录：`map_nav_trace/replay_400_merged_latest/`

`run_manifest.json`：

```json
{
  "n_cases": 400,
  "n_missing": 0,
  "recall_mean": 0.7436,
  "recall_eq0": 58,
  "generated_at": "2026-07-16T22:33:20"
}
```

---

## 6. 问答 + Inspect 评估（权威 QA）

- 输入：上述冻结 evidence
- 输出：`results/latest_clean400_map_nav_merged_latest_b500.json`
- 耗时约 **31 分钟**（compose ≈ 11 min，judge ≈ 21 min），`n_failed=0`
- `generated_at`：`2026-07-16T23:16:10`
- evidence fingerprint：`98b09ef1…577e`

### 6.1 本次 map-nav 主表

| | Overall | Niche (n=134) | Multi-hop (n=133) | Scope (n=133) |
|--|--------:|--------------:|------------------:|--------------:|
| **task** | **0.2419** | 0.1940 | 0.1096 | **0.4224** |
| **evidence** | **0.7436** | **0.9030** | 0.7594 | 0.5671 |
| process | 0.8998 | 0.9422 | 0.9079 | 0.8490 |

### 6.2 与仓库内 baseline 对照（同为 clean400 / b500）

| 方法 | task | evidence | niche task | multi task | scope task |
|------|-----:|---------:|-----------:|-----------:|-----------:|
| **map_nav（本次）** | **0.2419** | **0.7436** | 0.1940 | **0.1096** | **0.4224** |
| GOLD hierarchical (e2) | 0.1974 | 0.5781 | **0.2090** | 0.0777 | 0.3053 |
| FLAT (e2) | 0.1376 | 0.4988 | 0.0903 | 0.0683 | 0.2547 |
| TreeRAG (e2) | 0.2016 | 0.5125 | 0.1522 | 0.0831 | 0.3698 |
| GOLD hierarchical (scope_compact) | 0.1892 | 0.6168 | 0.2090 | 0.0777 | 0.2809 |
| PRED hierarchical (scope_compact) | 0.1324 | 0.4213 | 0.1276 | 0.0601 | 0.2094 |

相对 Flat / TreeRAG / Gold：**overall task 与 overall evidence 均更高**。  
分题型：multi / scope 的 task 明显更好；**niche task 略低于 Gold**。

### 6.3 Niche「高 coverage、低 task」说明

这不是 coverage 算错：

- niche evidence ≈ **0.90**，但 task ≈ **0.19**（近似 0/1）。
- 当日核对：evid=1 约 121 题，其中 task=1 仅约 26 题；**evid=1 且 task=0 ≈ 98 题**。
- 典型失败：证据里已有金段，但 compose 答偏 / 答多 / 未对齐 Inspect 要点，judge 直接 0。

因此：**retrieval/coverage 与答题得分是两段流水线**；niche 下一阶段应重点看 compose prompt / 答案形态，而不是继续只拧导航。

---

## 7. 设计层面的稳定认知（当日对齐）

1. **N\* / C\*|D\*|F\* / L\*** 三套 ID 不可混用；agent 只输出动作 ID。
2. COLLECT = 证据入库（整枝），不是「走进该节点当 viewpoint」；DISPATCH 不改本层 viewpoint。
3. 父未显式 COLLECT 时：父只提供路径表头，子块用自己的 owner 查 confidence。
4. 先 COLLECT 子再 COLLECT 父：会 purge 子孙旧块再整枝水合；子上已有的 confidence **setdefault 不覆盖**。
5. 外部 rerank / FINISH `group_rank` 决定组间优先级；子 agent 不扮演「最终裁判」。

---

## 8. 现行配置快照（与本次权威跑一致的方向）

`config/nav_default.json` 关键项：

| 键 | 值 |
|----|----|
| `map_char_limit` | 5000 |
| `enable_recursive_dispatch` | true |
| `max_dispatch_depth` | 3 |
| `scope_inline_summary_char_limit` | 1500 |
| `scope_inline_summary_budget_mult` | 3.0 |
| `compose_confidence_weight` | 0.5 |
| `enable_external_rerank` | true |

打包实现：`src/nav/nav_compose.py`（贪心填满，07c41a5 风格）。

---

## 9. 遗留问题与建议下一步

1. **整枝灌池 + 贪心挤 gold**：同 COLLECT 仍可能丢掉兄弟金段（如 `multi_0216` 类）。可考虑大枝按 unit/highlight 截断再 pack，或组内优先保 highlight/gold-adjacent。
2. **recursive 净正但不稳**：难例有收益，好题偶发选点漂移；不宜再靠关 recursive「救」新 zero。
3. **仍有 58 题 recall=0**：混合导航 miss、数据侧、打包挤出；需单独分层审计，勿与「相对回归」混谈。
4. **niche task 瓶颈在 compose/judge**：evid 已高，优先做答题侧消融，而不是继续抬 coverage。
5. **模型消融**：若换 DeepSeek 官方做导航，应整链改 `OPENAI_*` 到 DeepSeek，勿把官方 key 塞进智增增；注意 LLM cache 失效。

---

## 10. 保留产物与清理说明

### 保留（权威）

| 用途 | 路径 |
|------|------|
| 400 Evidence + TRACE | `map_nav_trace/replay_400_merged_latest/` |
| 400 Compose + Inspect QA | `results/latest_clean400_map_nav_merged_latest_b500.json` |
| 论文对照 baseline | `results/latest_clean400_goldnav_e2_v1_{gold_flat,treerag}_b500.json` |
| 旧 scope_compact | `results/latest_clean400_scope_compact_cap180_v1_{gold,pred,summary}*` |

### 已清理（中间实验）

- 中间 replay：坏打包 400、`replay_union_66_68`、`replay_rest_shard*`、268、smoke、`ab_zero20_norecurse`
- 临时 id：`ids_rest_shard*.txt`、`ids_union_*`、`today_zero_66.txt` 等
- smoke QA、compose checkpoint cache、相关 log
- A/B worktree `.wt_old`

---

## 11. 复现命令（摘要）

```bash
# Evidence（子集或全量）
python3 bin/56_replay_map_nav_traces.py \
  --ids-file <ids.txt> \
  --out-dir map_nav_trace/replay_<tag>

# 冻结 evidence → 问答+评估
python3 bin/59_compose_judge_from_evidence.py \
  --replay-dir map_nav_trace/replay_400_merged_latest \
  --out results/latest_clean400_map_nav_merged_latest_b500.json \
  --budget-chars 500
```

具体参数以 `.cursor/skills/map-nav-replay-batch/SKILL.md` 为准。

---

*文档生成日期：2026-07-16。数字以当日跑批与仓库内保留 JSON 为准；若后续重跑 evidence，请同步更新 fingerprint 与本文件。*
