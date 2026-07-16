# MAP Nav Reference

## Config knobs (`NavConfig` / `config/nav_default.json`)

| Field | Default | Meaning |
|-------|---------|---------|
| `map_mode` / `NAV_MAP_MODE` | env/config | 开启折叠标题图观测 |
| `map_char_limit` | 5000 | **唯一**显示硬预算（折叠阈值） |
| `collect_top_k` | 6 | highlight rescue-K，**不是**动作 top-K |
| `enable_recursive_dispatch` | true | true → 深层可继续 DISPATCH；false 仅 depth0 |
| `max_dispatch_depth` | 3 | 递归分派深度上限 |
| `scope_inline_summary_char_limit` | 1500 | scoped map 预估超过该字符数改 title-only；run_nav_episode 用 `budget_chars×mult` 重算 |
| `scope_inline_summary_budget_mult` | 3.0 | 阈值 = evidence 预算 × 该倍数（预算 500 → 1500） |
| `navigate_max_steps` | 8 | 子 agent 步数 |
| `max_steps` | 8 | 根 agent 步数 |
| `dispatch_group_size` | 5 | 并发分组 |
| `dispatch_max_workers` | 4 | 线程池；子状态 fork/merge |
| `subagent_model_env` | NAV_SUBAGENT_MODEL | 深层模型 env |

Deprecated keys quietly dropped: `expand_top_k`, `map_peek_top_k`, `map_jump_top_k`, `peek_content_*`, …

## State fields (current)

- `collected_section_ids`：COLLECT 成功后写入 `sid ∪ descendants`，枝从地图移除  
- **无** `covered_section_ids`  
- `reports_context`：子 RegionReport 文本块给父看  
- `investigated_section_ids`：已 DISPATCH 过的 region  
- `explicit_collect_ids`：只记录 Agent 明确选择的 COLLECT 目标，供 COMPOSE 计算 `selection_count`
- Agent State「Evidence collected」只列**主动 COLLECT 根**（action_history），不列后代

## ID resolution path

```text
观测行: [N19] title … actions: collect=C19, dispatch=D6
                │                              │
                │ display only                 │ LLM returns action_id
                ▼                              ▼
           map_id="N19"              LegalAction(kind=DISPATCH, section_id="…:L92")
                                               │
                                               ▼
                                    hydrate / gold / packing 用 L92
```

直播与复现的 `D*` 编号可能差几个（折叠/Hit 不同）；**对齐时以 section_id / 标题为准**，不要死盯编号。

## Replay

```bash
PYTHONPATH=src/nav:src/realdata python bin/56_replay_map_nav_traces.py \
  real_69c60974d4242eda8c47c615_scope_collection_auto_0030
```

输出目录：`map_nav_trace/replay_*`；逐步树+决策可读副本：`map_nav_trace/scope0030_step_action_spaces.md`。

## KNOWHERE migration TODOs (do not implement unless asked)

- SEARCH_IMAGES / SEARCH_TABLES  
- OUTLINE via `query_intent` instead of keyword heuristics (keyword OUTLINE already retired from COLLECT)
- Optionally expose outline as explicit COLLECT variant  

## Speaking checklist (before answering user)

- [ ] 决策用 `action_id=C*|D*|F*`  
- [ ] 需要指行时说「N* 那一行上的 D*」  
- [ ] `L*` 只当内部/gold/日志  
- [ ] 不提 JUMP/PEEK/EXPAND 为现行动作  
- [ ] 区分「导航命中」vs「budget packing 丢掉 gold」
