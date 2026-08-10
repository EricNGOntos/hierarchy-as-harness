# PLAN × NAV：现行设计纪要（原「重叠审计」更新版）

> 本文档取代 2026-08 的三臂 fusion 审计稿。旧开关族（`enable_anchor_entry` /
> `enable_one_shot_harvest` / illumination / budget ledger / `route_hints` 粘滞
> anchor 等）已删除。产品面只剩两个模式：`mode=navigate|checklist`。
>
> 迁移决策与实测分数见 [`docs/knowhere_mapnav_fusion.md`](knowhere_mapnav_fusion.md)。
> `src/nav` 注释若仍写「§ToolSpace surface」，即指本文末节。

## 1. 两臂分别是什么

| 臂 | `NavConfig.mode` | 执行路径 |
| --- | --- | --- |
| **baseline** | `navigate` | 根上 `navigate()`：COLLECT / DISPATCH / FINISH 多轮循环 |
| **shared** | `checklist` | `plan_query` → 依赖波次 `harvest()` → `plan_control`（accept / widen / drop） |

checklist 内固定打开：规划、编排、one-shot harvest、plan_control、地图上的
`[harvested:sN]`、槽位 LLM 抽取。不再提供独立的产品 bool 组合。

## 2. 曾经重叠、现已收敛的点

### 2.1 harvest 取代 per-subgoal navigate

checklist 不再对每个 subgoal 跑一整套 `navigate()` ReAct。每个 ready subgoal
一次 `harvest()`：同轮报 `collect_ids` + `dispatch_ids` + `search_assets`，
空选择即隐式结束该区域。递归 DISPATCH 受 `max_harvest_depth` 约束。

### 2.2 单一共享检索空间

`plan_query` 产出 **coverage_checklist** + subgoal DAG（need / query /
depends_on / contract / produces）。**不再**有 per-subgoal `scope_filter` /
`route_hints` / `budget_share` / `activation`。所有 harvest 从 namespace /
document 根进入。

### 2.3 plan_control 是唯一裁决

每波结束后调用一次 `plan_control()`。输入：本波各 subgoal 的差分证据 +
`harvest_reason` + 覆盖清单。输出：per-subgoal `accept|widen|drop` + 全局
`continue|replan|done`。

| 决策 | 语义 |
| --- | --- |
| accept | 写入 `satisfied_subgoal_ids`，结案 |
| drop | 写入 `dropped_subgoal_ids`，结案（下游依赖视作 settled） |
| widen | **不结案**；`gap` → `subgoal_widen_gaps[sid]`；死胡同已在 harvest 写入 `subgoal_dismissed_section_ids`；下一波从根重跑并拼 gap。`subgoal_attempt_counts >= subgoal_max_attempts` 强制 drop |

已删除：`reharvest` 决策、`subgoal_anchor`、`resolve_harvest_anchor`、
「widen = 上移父节点」。

### 2.4 证据归属与 REPLAN

- 本波证据用 `collected_before` 差分，不把全局池塞进单个 subgoal 的 control 卡片。
- REPLAN：清空 per-id 记账（satisfied / attempted / dropped / results / widen gaps /
  attempt counts / dismissed）；保留无限定 `slot_bindings` 与已 collect 的 chunk。

### 2.5 `[harvested:sN]`

checklist 下已收集枝在地图上保留为折叠行并标注归属，避免后续 subgoal 误以为
「空白未覆盖」。

## 3. 刻意不做（与 fusion 清理一致）

- 不恢复 sticky anchor / `enable_anchor_entry`
- 不恢复 illumination / goal-conditioned folding / BudgetLedger
- 不恢复 activation forks / per-subgoal scope
- 不把 `__corpus__` / `{doc}:__doc_root` 合成 id 写回内核（地址一律 `NavAddress`）

## ToolSpace surface（`src/nav` 实际依赖的最小面，供 knowhere-main 移植）

审计 `src/nav` 全部对 `ts` 的调用（`map_mode=True` 路径，即 harvest /
plan_control 实际运行的路径）发现，除了可选的评分面（`_idx` /
`read_chunks` / `materialize_self_only_chunks` / `corpus_doc_ids`——所有
调用点都用 `getattr(ts, "...", None)` 或 `callable(...)` 保护，缺失时只
降级排序质量，不会中断流程），核心链路只用到 5 个方法：

1. `sections_for_doc(doc_id) -> List[section_id]`：一个文档/语料的顶层
   节点。
2. `get_structure(section_id) -> {preview, n_lines, n_chunks, children}`：
   单个节点的标题/摘要/子块数/子节点列表。
3. `_children_for_section_path(section_id, doc_id, limit=None) -> List[dict]`
   （可选加速；缺失时回退到 `get_structure(...)["children"]`）。
4. `section_relation_ids(section_id, doc_id) -> (ancestor_ids, descendant_ids)`：
   祖先/后代集合（可选；缺失时有基于地图树的回退实现）。
5. `_materialize_leaf_path_chunks(section_id, doc_id) -> List[Chunk]`：把
   一个节点的整个子树物化成证据 chunk（COLLECT 的唯一取数入口）。

另需 provider 能力（地址层，非历史「字符串后缀」）：

- `document_ids()` / `address_level(sid)` / `owner_document(sid)` / `parent_id(sid)`

`src/nav/nav_hierarchy.py` 把层级方法定义为 `HierarchyProvider`
Protocol，`ProviderToolSpace` 适配成 ToolSpace 鸭子类型——knowhere-main 只
需实现 `HierarchyProvider`。验收见 `tests/test_nav_hierarchy_adapter.py`。

## 4. 已知局限

- `nav_projection` 行内摘要仍可读独立 `section_summary_store`；Knowhere 侧需
  接 provider summary。
- DISPATCH 实验仓串行；生产侧可选 `asyncio.gather` 尚未接。
- `max_dispatch_depth` / `enable_recursive_dispatch` 同时门控 navigate 与
  harvest 的 DISPATCH 合法性。
