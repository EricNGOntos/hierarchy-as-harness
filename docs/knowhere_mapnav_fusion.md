# MAP-NAV × Knowhere 融合：决策与实测

实验仓验收文档。生产接入（loader / route / 退役）见
[`.cursor/plans/map-nav_融合迁移_bee0ec95.plan.md`](../.cursor/plans/map-nav_融合迁移_bee0ec95.plan.md)。
机制细节见 [`audit_plan_nav_overlap.md`](audit_plan_nav_overlap.md)。

## 1. 两臂（现行）

| 臂 | 配置 | 含义 |
| --- | --- | --- |
| `baseline` | `mode=navigate` | 纯地图导航 |
| `shared` | `mode=checklist`，`max_replans=1` | 覆盖清单 + harvest + plan_control |

入口：`bin/run_knowhere_probe.py`（默认 probe =
`data/probes/knowhere_archive_corpus.json`，两篇长河坝报告同一 namespace）。

旧 **fusion** 臂（illuminate / ledger / sticky anchor / 一串 enable_*）已退役，
不再维护对照。

## 2. 两套分（勿混）

| 指标 | 量的是什么 | 怎么算 |
| --- | --- | --- |
| **pack** (`pack_hit` / `pack_recall`) | **检索定位**：最终证据包里有没有命中 probe 标注的 `gold_paths` section | `kept_chunks` → owner section ∩ gold；与答案文本无关 |
| **ref** (`reference_score`) | **答案语义**：compose 写出的答案相对 `reference_facts` 对不对 | LLM 对每条 fact 判 对=1 / 半对=0.5 / 错=0，再平均 |

二者独立：可以 **pack=0 但 ref>0**（采到别的节，文字碰巧盖住部分事实）；也可以 **pack 满但 ref 低**（节对了，compose 写错/漏写）。主分用 ref；pack 只诊断「有没有采到该采的节」。

## 3. Thinking 策略

| 角色 | 控制 | 默认 |
| --- | --- | --- |
| navigate / harvest / verify / score（`role=action`） | 恒关 | `disabled` |
| `plan_query` / `plan_control`（`role=planner`） | `NAV_PLANNER_THINKING` | unset → `disabled` |
| 答案 compose | `COMPOSE_THINKING` | unset → `disabled` |

DeepSeek V4 若省略 thinking 字段会默认开 think；短 JSON 路径必须显式关。

## 4. 刻意不做

- LLM 选文档 / 文档清单进 prompt
- 内核合成地址 `__corpus__` / `{doc}:__doc_root`
- sticky `subgoal_anchor` / `enable_anchor_entry` / `reharvest` 锚点决策
- illumination / goal-conditioned folding / BudgetLedger 三池
- per-subgoal `scope_filter` / `route_hints` / `activation` / `budget_share`
- 产品面一串独立 enable 组合（已收成 `mode`）
- 首版 DISPATCH 线程池并发（串行；生产侧再谈 `asyncio.gather`）

## 5. 实测（corpus Q1–Q5，细节对齐 A–D 之后）

跑法（本次：`deepseek-v4-flash`，thinking 关；日志
`map_nav_trace/knowhere_probe/ef_validate_post_cd.log`）：

```bash
NAV_LLM_MODEL=deepseek-v4-flash COMPOSE_MODEL=deepseek-v4-flash \
NAV_PLANNER_MODEL=deepseek-v4-flash NAV_SUBAGENT_MODEL=deepseek-v4-flash \
NAV_PROBE_SCORE_MODEL=deepseek-v4-flash \
NAV_PLANNER_THINKING=disabled COMPOSE_THINKING=disabled \
PYTHONPATH=src/nav:src/realdata python bin/run_knowhere_probe.py \
  --probe data/probes/knowhere_archive_corpus.json \
  --arms baseline,shared \
  --budget-chars 12000
```

结果落盘：`map_nav_trace/knowhere_probe/{arm}__{case}.json` 与 `summary.json`。

| case | baseline ref | shared ref | baseline pack | shared pack | 备注 |
| --- | ---: | ---: | ---: | ---: | --- |
| q1_wang_roles_r1 | 0.0 | 0.5 | 0/2 | 0/2 | 署名短页；shared 曾 widen 再 drop |
| q1_wang_roles_r2 | 1.0 | 1.0 | 0/1 | 1/1 | |
| q2_hydrology_stations | 1.0 | 0.75 | 4/4 | **4/4** | shared 首波 widen→次波 drop，**非首波即弃**；邻域收回 |
| q3_status_and_supply_scope | 1.0 | 1.0 | 2/2 | 2/2 | |
| q4_difficulties_and_key_tech | 0.6667 | 0.6667 | 2/3 | **0/3** | shared 证据在 `1.1.3`/`1.7` 等旁路节，未进 3 个 gold；f1/f2 文字仍判对、f3 错 → ref=2/3 |
| **合计（5 case mean）** | **3.6667** | **3.9167** | | | shared 略高于 baseline |

清理前对照（旧 fusion 臂，同 probe）：shared/fusion 一度全 0；widen≈drop。
更早三臂时代满分约 5 的备忘：baseline≈3、fusion≈1.5、Knowhere 默认≈3.5 /
放开≈4.5——不可与上行直接比绝对分制。

## 6. P1 通过线（现状）

- q2：**已通过** — pack 4/4；control 轨迹含 widen 后再 drop，不再首波即弃。
- q4：**部分** — shared `reference_score=0.67`（有答案分），但 `pack_recall=0`；
  默认预算下证据仍未打中 gold 路径，后续若接生产需单独盯 harvest 落点。
- shared 合计略优于 baseline（3.92 vs 3.67），未出现「清理后退步」信号。
