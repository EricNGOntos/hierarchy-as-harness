# Map-Nav Replay Batch — Reference

## CLI 完整参数（`bin/56_replay_map_nav_traces.py`）

```bash
python bin/56_replay_map_nav_traces.py [inspect_id ...] [OPTIONS]
```

| 参数 | 说明 |
|------|------|
| `inspect_id ...` | positional，一个或多个 id |
| `--ids-file`, `-f` | 每行一个 inspect_id，`#` 开头为注释 |
| `@path.txt` | positional 里 legacy 写法，等同 ids 文件 |
| `--resume-dir PATH` | 在已有 `replay_*` 目录续跑，跳过已完成 |
| `--resume` | 自动选择 `map_nav_trace/` 下最近 incomplete 的 `replay_*` |
| `--out-dir PATH` | 新跑时指定输出目录（默认 `replay_<timestamp>`） |
| `--stop-on-error` | 单题失败即停（默认记录失败并继续） |

无参数 → `DEFAULT_IDS`（2 题冒烟）。

## 生成 ids 文件的常用片段

### 92 剩余 baseline-zero

```bash
python3 - <<'PY' > /tmp/replay_ids.txt
import json
d = json.load(open("map_nav_trace/map_nav_still_gold_recall_zero.json"))
for i in d["inspect_ids"]:
    print(i)
PY
```

### 99 原始 baseline-zero（含已恢复 7 题）

```bash
python3 - <<'PY' > /tmp/replay_ids_99.txt
import json
d = json.load(open("map_nav_trace/map_nav_still_gold_recall_zero.json"))
ids = list(d["inspect_ids"])
for i in d.get("recovered_excluded") or []:
    if i not in ids:
        ids.append(i)
for i in ids:
    print(i)
print("# total", len(ids), file=__import__("sys").stderr)
PY
```

### 全量 400

```bash
python3 - <<'PY' > /tmp/all400_ids.txt
import json
from pathlib import Path
for line in Path("data/tasks/tasks_realdata_bodyrich_latest_clean_400.jsonl").read_text().splitlines():
    if line.strip():
        print(json.loads(line)["inspect_id"])
PY
```

### 按 task_type 过滤

```bash
python3 - <<'PY' > /tmp/scope_only.txt
import json
from pathlib import Path
for line in Path("data/tasks/tasks_realdata_bodyrich_latest_clean_400.jsonl").read_text().splitlines():
    if not line.strip():
        continue
    row = json.loads(line)
    if row.get("task_type") == "scope_collection":
        print(row["inspect_id"])
PY
```

## `run_manifest.json` Schema

```json
{
  "started_at": "2026-07-15T17:30:58",
  "updated_at": "2026-07-15T17:45:00",
  "status": "incomplete",
  "out_dir": "/abs/path/map_nav_trace/replay_...",
  "requested_ids": ["id1", "id2"],
  "completed": ["id1"],
  "pending": ["id2"],
  "failed": {
    "id3": "RuntimeError: ..."
  },
  "task_stats": {
    "total": 92,
    "done": 1,
    "remaining": 91,
    "failed": 1
  }
}
```

- `status`: `running` → 结束时 `completed` 或 `incomplete`
- 合法 case 文件判定：含 `inspect_id`、`new.evidence_text`、`new.gold_node_recall`、`steps`

## 单题 JSON 字段说明

| 字段 | 用途 |
|------|------|
| `inspect_id` | 任务 id |
| `query` | 用户问题 |
| `gold_nodes` | 标注 gold section_id 列表 |
| `task_type` | `scope_collection` / `multi_hop` / `niche_fact` 等 |
| `new.gold_node_recall` | **coverage**（节点级 recall） |
| `new.gold_node_hits` | 每个 gold 的 `in_retrieved` / `in_evidence_text` |
| `new.evidence_text` | **最终打包 evidence**（下游 QA 输入） |
| `new.retrieved_nodes` | 检索到的 section_id |
| `new.evidence_chars` | evidence 字符数 |
| `steps` | 逐步决策 TRACE（含 `action_id`、`collect_section_ids`、`group_rank`） |
| `old.*` | 对比 baseline（`results/latest_clean400_scope_compact_cap180_v1_gold_b500.json`） |

## Extract evidence JSONL {#extract-evidence-jsonl}

从 `all_cases.json` 抽出下游 compose 用的一行一题 JSONL：

```bash
python3 - <<'PY'
import json
from pathlib import Path
import sys
replay = Path(sys.argv[1])  # e.g. map_nav_trace/replay_20260715_173058
data = json.loads((replay / "all_cases.json").read_text())
out = replay / "evidence_for_compose.jsonl"
with out.open("w", encoding="utf-8") as f:
    for c in data.get("cases") or []:
        row = {
            "inspect_id": c["inspect_id"],
            "query": c["query"],
            "task_type": c.get("task_type"),
            "gold_nodes": c.get("gold_nodes"),
            "gold_node_recall": (c.get("new") or {}).get("gold_node_recall"),
            "evidence_text": (c.get("new") or {}).get("evidence_text"),
            "retrieved_nodes": (c.get("new") or {}).get("retrieved_nodes"),
        }
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
print("wrote", out)
PY
map_nav_trace/replay_YYYYMMDD_HHMMSS
```

## 中断与恢复场景

| 场景 | 处理 |
|------|------|
| 进程被杀 / Ctrl+C | `finally` 仍写 manifest + all_cases（已完成部分） |
| 单题异常 | 删该题 `.json`/`.tmp`，记入 `failed`，默认继续 |
| 损坏 JSON | `--resume-dir` 时自动删并重跑 |
| 想重跑某一题 | 手动删 `<inspect_id>.json`，再 `--resume-dir` |
| 想换题目集 | 新 `--ids-file` + 新 `--out-dir`（不要混用旧 manifest） |

续跑命令（脚本结束时会打印）：

```bash
python bin/56_replay_map_nav_traces.py --resume-dir map_nav_trace/replay_<timestamp>
```

## 读结果（不重新跑）

```bash
# 人类报告
python bin/58_report_map_nav_run.py map_nav_trace/replay_20260715_173058

# 单题
cat map_nav_trace/replay_.../real_*_scope_collection_auto_0076.json | jq '.new.gold_node_recall, .new.evidence_text[:200]'
```

## 与 `bin/52_run_map_nav.sh` 对比

| | `56_replay` | `52_run_map_nav` |
|---|-------------|------------------|
| 规模 | 任意 ids 列表 | 固定 400 全量 |
| 输出 | `map_nav_trace/replay_*` | `results/*_gold_map_b500.json` |
| compose 答题 | 否 | 是 |
| checkpoint | `run_manifest.json` + 单题 JSON | `checkpoint-jsonl`（44 脚本） |
| 典型用途 | coverage 审计、抽 evidence | 正式 benchmark 对比 |

## 环境变量（56 内 `_env_setup` 默认）

```
NAV_MAP_MODE=1
NAV_MAP_DENSE=1
NAV_FILTER_COLLECTED_SECTIONS=1
NAV_SCOPE_OUTLINE_MODE=1
NAV_SCOPE_COLLECT_STRATEGY=multi_band
BODYRICH_EMBEDDING_BACKEND=remote
EMBEDDING_MODEL=text-embedding-v3
NAV_SECTION_SUMMARY_DIR=cache/section_summaries_headtail  # 若存在
```

Nav 行为细节（COLLECT/DISPATCH、打包）见 [`map-nav-recursive-dispatch`](../map-nav-recursive-dispatch/SKILL.md)。

## 耗时参考（有 LLM cache）

| 规模 | 粗估 |
|------|------|
| 5 题 | ~25s |
| 92 题 | ~10–20 min |
| 400 题 | ~30–90 min |

首跑无 cache 明显更慢；embedding 索引加载一次约 0.3–1s。

## 后台长跑示例

```bash
nohup python bin/56_replay_map_nav_traces.py --ids-file /tmp/all400_ids.txt \
  > map_nav_trace/replay_all400.log 2>&1 &
# 中断后续跑
python bin/56_replay_map_nav_traces.py --resume
```
