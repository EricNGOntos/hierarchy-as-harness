---
name: map-nav-replay-batch
description: >-
  Batch replay map-nav evidence retrieval for subset or full 400 tasks: run
  bin/56_replay_map_nav_traces.py, resume interrupted runs, read gold_node_recall
  coverage and evidence_text outputs. Also covers frozen-evidence compose+judge via
  bin/59_compose_judge_from_evidence.py. Use when the user asks to replay map-nav
  traces, batch test 92/99/400 inspect_ids, resume replay, export evidence context
  for downstream QA, compose/judge from replay evidence, or read map_nav_trace/replay_* results.
---

# Map-Nav 批量 Replay（evidence-only）+ 冻结 evidence QA

本 skill 管 **批量跑导航、拿 evidence 上下文 + gold coverage**，以及 **用冻结 evidence 做 compose/Inspect 评分**。

与 [`map-nav-recursive-dispatch`](../map-nav-recursive-dispatch/SKILL.md) 的分工：
- **recursive-dispatch**：算法/TRACE 语义、单题因果分析
- **本 skill**：批量基础设施、怎么跑、结果在哪、怎么续跑、怎么抽 evidence、怎么接问答评估

## 核心脚本

| 脚本 | 用途 |
|------|------|
| [`bin/56_replay_map_nav_traces.py`](../../bin/56_replay_map_nav_traces.py) | **主入口**：evidence-only replay + 断点续跑 |
| [`bin/58_report_map_nav_run.py`](../../bin/58_report_map_nav_run.py) | 离线读结果生成 `REPORT.md`（56 已自动调用） |
| [`bin/59_compose_judge_from_evidence.py`](../../bin/59_compose_judge_from_evidence.py) | **冻结 evidence → compose + Inspect judge**（可断点续跑） |

**不要**用 `bin/52_run_map_nav.sh` 做「只要 evidence」的批量——那是全链路 400 题（含 compose/评分），更重，且会重跑导航。

## 快速决策

```
要 evidence + coverage，可续跑？           → 56_replay_map_nav_traces.py
要基于已有 replay evidence 做问答+评估？   → 59_compose_judge_from_evidence.py
要全量 400 含问答（会重跑 nav）？          → 52_run_map_nav.sh
只读已有 replay 目录？                     → 58_report_map_nav_run.py
```

## 冻结 evidence → QA（59）

```bash
# 先 dry-run 校验接线（不调 LLM）
python bin/59_compose_judge_from_evidence.py \
  --replay-dir map_nav_trace/replay_20260716_173430 \
  --max-tasks 2 --dry-run

# 小批量冒烟后再全量
python bin/59_compose_judge_from_evidence.py \
  --replay-dir map_nav_trace/replay_20260716_173430 \
  --max-tasks 2 \
  --out results/smoke_compose_from_replay_b500.json

# 全量（同 checkpoint 可中断续跑）
python bin/59_compose_judge_from_evidence.py \
  --replay-dir map_nav_trace/replay_20260716_173430 \
  --out results/latest_clean400_map_nav_from_replay_b500.json
```

- 断点：`cache/compose_from_replay_<out_stem>/checkpoint.jsonl`（按 `inspect_id`）
- 进度：同目录 `run_manifest.json`
- 复用：`_make_composed_answer` / `_fill_agg`（与 `bin/44` 同一套）

## 三种批量规模

### A. 指定题目（如 92/99 道 baseline-zero）

```bash
cd <repo-root>

# 从项目内清单抽 id（92 道剩余）
python3 - <<'PY' > /tmp/replay_ids.txt
import json
d = json.load(open("map_nav_trace/map_nav_still_gold_recall_zero.json"))
for i in d["inspect_ids"]:
    print(i)
PY

python bin/56_replay_map_nav_traces.py --ids-file /tmp/replay_ids.txt
```

原始 **99** 道 = `inspect_ids`（92）+ `recovered_excluded`（7），合并后写入 ids 文件。

### B. 全量 400 题

```bash
python3 - <<'PY' > /tmp/all400_ids.txt
import json
from pathlib import Path
for line in Path("data/tasks/tasks_realdata_bodyrich_latest_clean_400.jsonl").read_text().splitlines():
    if line.strip():
        print(json.loads(line)["inspect_id"])
PY

python bin/56_replay_map_nav_traces.py --ids-file /tmp/all400_ids.txt
```

### C. 少量冒烟（默认 2 题）

```bash
python bin/56_replay_map_nav_traces.py
# 或显式传 id
python bin/56_replay_map_nav_traces.py scope_0076 multi_0010
```

## 断点续跑（必会）

每次新跑生成 `map_nav_trace/replay_<timestamp>/`。中断后**同一目录**续跑：

```bash
# 推荐：指定目录
python bin/56_replay_map_nav_traces.py --resume-dir map_nav_trace/replay_20260715_173058

# 自动找最近未完成的 replay_*
python bin/56_replay_map_nav_traces.py --resume
```

续跑行为：
- 跳过 **合法已完成** 的 `<inspect_id>.json`
- **损坏/半截** JSON 自动删除并重跑
- 失败题记录在 `run_manifest.json` 的 `failed`，默认继续跑下一题
- `--stop-on-error`：遇错即停

进度示例：
```
[replay] [15/92]  16.3% | ok=14 fail=1 | ETA ~8m | running scope_0076 ...
```

## 输出目录结构

```
map_nav_trace/replay_YYYYMMDD_HHMMSS/
├── run_manifest.json      # 进度/续跑状态（pending/completed/failed）
├── all_cases.json         # 汇总（跑完或 finally 时刷新）
├── REPORT.md              # 人类可读：coverage + TRACE + evidence
├── TRACE.md               # 逐步 TRACE
└── <inspect_id>.json      # 单题（跑完一题写一题，原子写入）
```

### 下游 QA 最常用字段

单题 JSON 路径：`<replay_dir>/<inspect_id>.json`

```json
{
  "inspect_id": "...",
  "query": "...",
  "gold_nodes": ["doc:L141", "..."],
  "new": {
    "gold_node_recall": 0.12,
    "evidence_text": "[E1]\n[§ ...]\n  ...",
    "retrieved_nodes": ["doc:L128", "..."],
    "evidence_chars": 499
  },
  "steps": [ ... ]
}
```

- **coverage**：`new.gold_node_recall`（0–1，按 gold 节点命中）
- **上下文**：`new.evidence_text`（直接喂 compose/人工检查）
- **旧 baseline 对比**：`old.gold_node_recall` / `old.evidence_text`

从 `all_cases.json` 批量抽 evidence 见 [reference.md](reference.md#extract-evidence-jsonl)。

## 前置依赖（跑之前确认）

| 项 | 路径/说明 |
|----|-----------|
| 任务集 | `data/tasks/tasks_realdata_bodyrich_latest_clean_400.jsonl`（400 题） |
| 语料 | `data/corpus/test_data_full_realdata_clean_latest.jsonl` |
| Nav 配置 | `config/nav_default.json`（默认 waterfill+oversize；消融 greedy 用 `config/nav_greedy.json`） |
| LLM 环境 | `load_llm_env()`；模型 `NAV_LLM_MODEL` / `NAV_SUBAGENT_MODEL` |
| Embedding | 默认 `text-embedding-v3` remote；缓存 `cache/embeddings/` |
| LLM 缓存 | `cache/llm_api_cache.jsonl`（复跑同轨迹会 hit，快很多） |
| Section summary | `cache/section_summaries_headtail/`（存在则自动用） |

## 关键注意事项

1. **只跑 evidence**：`compose_answer=False`，无 `score_task`；要答题需另 pipeline。
2. **预算固定 500 字**：脚本内 `budget_chars=500`；coverage 低可能是打包预算而非导航未命中。
3. **耗时**：单题约 2–6s（有 cache）；92 题约 10–20min；400 题约 30–90min。
4. **索引**：每次启动加载全 corpus 建索引（~0.3–1s），然后逐题 replay。
5. **LLM 非确定性**：提示词/缓存变化可能导致同题轨迹与旧 replay 不同——对比实验请固定 cache 或记录 `run_manifest` 时间。
6. **manifest 优先**：`--resume-dir` 且不传 id 时，用 manifest 里的 `requested_ids`，不是 DEFAULT_IDS。
7. **退出码**：`0` = 全部完成且无 failed；有 pending/failed 返回 `1`（仍写出已完成结果）。

## Agent 标准工作流

```
1. 确认规模（冒烟 / 92 / 99 / 400）
2. 生成 ids 文件或用 --ids-file
3. 运行 56_replay（大批量建议 nohup/后台）
4. 中断 → --resume-dir 同一目录
5. 读 REPORT.md 或 all_cases.json 看 coverage 分布
6. 抽 evidence_text → `59_compose_judge_from_evidence.py`（先 `--dry-run` / `--max-tasks 2`）
```

## 权威结果目录（保留）

| 目录/文件 | 内容 |
|-----------|------|
| `map_nav_trace/replay_400_waterfill_oversize_merged/` | task_doc Map-Nav waterfill+oversize 全量 evidence |
| `map_nav_trace/replay_400_task_corpus_waterfill_oversize_*` | task_corpus Map-Nav waterfill+oversize 全量 evidence |
| `results/latest_clean400_map_nav_waterfill_oversize_*_b500.json` | task_doc Map-Nav 冻结 evidence 的 compose/judge |

## 进一步细节

- 命令行全集、manifest schema、抽 JSONL、与 52 全量对比：[reference.md](reference.md)
