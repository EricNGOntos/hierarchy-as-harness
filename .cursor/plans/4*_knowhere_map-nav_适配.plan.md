---
name: Knowhere MAP-NAV 迁移
overview: 以 knowhere 生产为准，把 MAP-NAV（PLAN×NAV 融合）迁进 knowhereapi-main 替换现有 agentic 检索。今天已确认：表结构/BM25 参数与我们完全对齐，单文档路径已跑通（长河坝 fusion gold 2/2、答案正确）。接入前必修 F1/F2/F3 三个机制缺陷，再做 AsyncSession loader + run_retrieval_route——估计 1–2 天到可切换单 namespace。
todos:
  - id: f1starve
    content: "【已完成·迁移前必修】F1 依赖饥饿：ready_subgoal_ids 解锁改为 settled(satisfied∪dropped)，后继不因前驱 drop/槽位未齐被永久卡住"
    status: completed
  - id: f2widen
    content: "【已完成·迁移前必修】F2/reharvest 合并：删 reharvest，widen 确定性上移到父级 anchor；到根再 widen → 自动 drop（长河坝已复现空转）"
    status: completed
  - id: f3harvest
    content: "【已完成·迁移前必修】F3 单发 harvest 欠采：靠 widen 上移 + 已看未选节点剔除自然补采，去掉 harvest 提示词里的 collect 偏置措辞"
    status: completed
  - id: f4reason
    content: "【已完成·迁移前必修】harvest 的 reason 现在只进 step detail 不进 plan_control 输入；补传，让 control 基于 harvest 自己的解释判断"
    status: completed
  - id: f5dismiss
    content: "【已完成·迁移前必修】看过未选的节点（含探空的 dispatch 分支）写入 per-subgoal dismissed，同 subgoal 后续地图隐藏，不入全局 state.dismissed_section_ids"
    status: completed
  - id: rowsource
    content: 【已完成·迁移本体】src/nav/nav_knowhere.py：SectionRow/UnitRow 行契约 + load_debug_parse；生产 AsyncSession loader 待 P2
    status: completed
  - id: provider
    content: 【已完成·迁移本体】KnowhereProvider：parent_section_id 建树、sort_order 保序、正文 [tables/]/[images/] 引用挂资产（132/133 归位）
    status: completed
  - id: seam
    content: 【已完成·迁移本体】ProviderToolSpace 转发 self_units/leaf_ids/unit_text/path_titles；修 InMemory content() set 乱序；_ancestor_path_titles 补 provider 回落
    status: completed
  - id: inject
    content: 【已完成·迁移本体】run_nav_episode 支持 toolspace 注入，跳过内部 ToolSpace 构造
    status: completed
  - id: scores_smoke
    content: 【已完成·验证】BM25-only（NAV_MAP_DENSE=0）点亮：gold 排 1/4，干扰项金川排 3 压过泸定——位置依赖成立
    status: completed
  - id: probe
    content: 【已完成·评测脚手架】data/probes/knowhere_changheba.json + bin/run_knowhere_probe.py；fusion pack 1.0 / baseline 0.5，两臂答案 3/3
    status: completed
  - id: tests
    content: 【已完成·测试】tests/test_nav_knowhere_provider.py + adapter 表面更新；167 通过（2 项缺数据文件既有失败）
    status: completed
  - id: unitkey
    content: 【待做·迁移本体】内核 retrieved_nodes 从 L{行号} 改为 section_id/chunk_id；harness 已按 owner section 打分，接入前内核要一致
    status: pending
  - id: dbloader
    content: 【待做·迁移本体】KnowhereProvider 的 AsyncSession loader：一次查询预加载候选文档 sections+chunks 成同步快照（内核不改 async）
    status: pending
  - id: route
    content: 【待做·P2】knowhere execution/routes.py 新增 _run_mapnav_route，产出 RetrievalRouteOutcome；results 行补齐 hydration/投影字段
    status: pending
  - id: trace
    content: 【待做·P2】复用 retrieval_runs/retrieval_steps，落 plan/harvest/plan_control；诊断写进 action_input（observation 只存键名）
    status: pending
  - id: address
    content: 【待做·多文档才需要】nav_address 四级地址，删 __corpus__:__root / :__doc_root；单文档/单 namespace 首版可继续用 doc:path 临时 id
    status: pending
  - id: docgate
    content: 【待做·多文档才需要】根 scope 文档级 BM25 收敛 + 候选上限；单文档首版跳过
    status: pending
  - id: retire
    content: 【待做·验证后】开关切到 mapnav 后下线 agentic/（~9.5k）与重叠的 workflow QueryPlanner
    status: pending
isProject: false
---

# Knowhere MAP-NAV 迁移（按今日实测更新）

## 一、结论（今日重估）

| 原先判断 | 今日实测后 |
| --- | --- |
| 工程量 1–2 周到能替换 agentic | **单文档路径已通；接进 knowhere 单 namespace 约 1–2 天** |
| 难点是适配数据库结构 | **表已经存好了，现有检索代码没用** |
| 要先做完整地址重构才能跑 | **单文档用 `doc_id:section_path` 临时 id 即可；四级地址仅多文档需要** |
| 机制缺陷是理论风险 | **F1/F2/F3 来自 complex5；F2 在长河坝再次复现——三者接入前必修** |

真正的阻塞：

1. **修 F1 / F2 / F3**（约半天，见第六节）——不修就迁，质量会不如现状
2. **AsyncSession loader + `_run_mapnav_route`**——约一天
3. **trace 落库 + 开关切换**——约半天

多文档地址重构 / 文档级收敛 / 下线 agentic/ 可以跟在后面，不挡首版。

## 二、今天已经证明的事实

### 2.1 数据对齐（测绘）

| MAP-NAV 需要 | knowhere 现成 | 备注 |
| --- | --- | --- |
| 子节点 | `parent_section_id` | 现有 agentic **没用**，靠切 `section_path` |
| 深度 | `section_level` | 同上，死字段 |
| 摘要 | `summary` | 有 |
| 文档序 | `sort_order` | sections / chunks 都有 |
| BM25 三路 | `*_search_text` 已物化 | 权重 / RRF_K / 召回倍数与我们逐值一致 |
| 向量 | **不存在** | `pgvector` 只在依赖清单；"只用 BM25"是现状 |

唯一替换点：`execution/routes.py:33` 的 `run_retrieval_route` → 加 `_run_mapnav_route`，不碰 API 契约。

### 2.2 单文档跑通（长河坝）

- Provider：67 section、132/133 chunk 归位、55 份 summary、资产靠正文引用挂宿主
- BM25 点亮：第一跳 gold 排 1；第二跳干扰项**金川排 3、正确泸定排 4**——纯检索会选错，必须靠第一跳内容定位
- 实测：

| 臂 | gold | 答案关键项 | 干扰项 | API | prompt | 证据字数 |
| --- | --- | --- | --- | --- | --- | --- |
| baseline | 1/2 | 3/3 | 无 | 10 | 21120 | 6218 |
| fusion | **2/2** | 3/3 | 无 | 11 | 19832 | 8245 |

baseline 答对但漏了第一跳节点（靠推断）；fusion 两跳都取到。fusion 慢（50s vs 12s）主因是 **F2：s2 连 widen 两次且 anchor 为空**。

## 三、哪些是迁移本体，哪些只是测试

| 性质 | 产物 |
| --- | --- |
| **迁移本体（进生产）** | `src/nav/nav_knowhere.py`、`nav_hierarchy.py` 改动、`nav_map_scores.py` provider 回落、`nav_agent.py` toolspace 注入 |
| **评测脚手架（不进生产）** | `data/probes/knowhere_changheba.json`、`bin/run_knowhere_probe.py`、`map_nav_trace/knowhere_probe/` |
| **测试** | `tests/test_nav_knowhere_provider.py` 及 adapter 表面更新 |
| **还没做的生产接入** | AsyncSession loader、`_run_mapnav_route`、trace、开关切流量 |

本地 `_debug_parse` JSON 与库表是同一行契约的两种装载方式；JSON loader 不是临时适配层，是入库前原料的镜像。差异只在：本地没有 `sec_xxx` surrogate key、三路 lexical text 需本地补算。

## 四、六个不对齐点：今日状态

| # | 不对齐 | 今日处置 | 状态 |
| --- | --- | --- | --- |
| 1 | 合成 id（`__corpus__` / `:__doc_root` / `doc:path`） | 单文档继续用 `doc:path`；四级地址推到多文档 | 降级，不挡首版 |
| 2 | 同步内核 vs async DB | 预加载同步快照；内核不改 async | 路径已定，loader 待写 |
| 3 | 根 scope 平铺全部文档 | 单文档跳过；多文档再做 docgate | 降级，不挡首版 |
| 4 | `line_ids` vs `chunk_id` | harness 已按 owner section 打分；内核 `retrieved_nodes` 仍报 `L{n}` | **接入前必改** |
| 5 | 资产 SEARCH/VLM | 不引入；正文引用挂宿主 + summary 作正文 | 已做 |
| 6 | 预算模型 | 保留我们的 `budget_chars`；边界接 `BudgetLedger` 记账 | 接入时顺手做 |

原先把 #1 当成"最大一块"——对**完整多文档迁移**仍成立，但对**首版单 namespace 替换**不是阻塞。今日实测证明：不改地址也能用 knowhere 数据跑完 fusion。

## 五、分期（重排）

### P0 已完成：knowhere 原生内核 + 单文档验证

- 行契约 + `KnowhereProvider` + `_debug_parse` loader
- ToolSpace 接缝（chunk 粒度、path 回落、toolspace 注入）
- 长河坝位置依赖两跳题：fusion gold 2/2、答案正确
- 测试锁住 id 转换 / 包裹层剥离 / 资产归属 / 保序

### P0.5 机制补丁（接入前必修，约半天）

修完第六节的 **F1 / F2 / F3**，并用 complex5 + 长河坝回归确认。另做 **unitkey**：`retrieved_nodes` / `_line_key` 改为 section_id 或 chunk_id+sort_order。

### P1 knowhere 接入首版（约 1 天）

目标：单 namespace、`use_agentic=True` 可切到 mapnav，API 契约不变。

1. `load_from_session(db, user_id, namespace, document_ids)` → 同步 `KnowhereProvider` 快照
2. `_run_mapnav_route` → `RetrievalRouteOutcome`；`results` 补齐 hydration 所需字段后走现有 `assemble` / `attach_citation` / `enrich_asset_url` / `project_public`
3. `TraceRecorder` 落 plan / harvest / plan_control（诊断进 `action_input`）
4. 配置开关（如 `use_mapnav` 或复用/重定义 `use_agentic`）灰度

**不做**：地址四级重构、文档级收敛、VLM、下线 agentic/。

### P2 多文档 + 退役（约 1–2 天，可并行）

- `nav_address`：document 一等节点（仅 DISPATCH）替代 `:__doc_root`；namespace+候选集替代 `__corpus__:__root`
- 根 scope 文档级 BM25 收敛（上限对齐现有 discovery 的 ~5 篇量级）
- 验证通过后删 `agentic/` 与重叠的 `workflow` QueryPlanner

## 六、迁移前必修：F1 / F2 / F3（2026-08-09 对齐：合并 widen/reharvest 的修订版）

来源：complex5 fusion 实测（成本降到 API≈0.31x、prompt≈0.05x，但 pack recall 0.619→0.571）。长河坝档案库真实问题回归（Q1/Q2）再次打中 F2，并暴露出比最初诊断更深的三个机制漏洞——原方案的 `reharvest`/`widen` 双决策本身就是 F2 的根因之一，本节整体推翻重写，**不是在原方案上打补丁**。

**这一轮要动代码的三点（用户对齐，客观核实均成立）：**

1. `harvest()` 每次决策的 `reason` 目前只写进 `AgentStep.detail`（TRACE 用），从不传回 `plan_control` 的输入——控制器看不到"harvester 自己为什么这么选"，只能靠 `verify_contract` 的零成本规则信号猜。→ 把 `reason` 并入 `plan_control` 看到的每个 subgoal 的证据块。
2. "看过但没选中"的节点（`harvest` 一次调用里展示过、但既不在 `collect_ids` 也不在 `dispatch_ids` 里的节点；以及被 dispatch 进去但整棵子树颗粒无收的节点）从未被记住——`state.dismissed_section_ids` 这个字段存在但从未被写入过（纯读不写的死字段）。同一个 subgoal 下一次再看到同一父级地图时，这些已经判过"不相关"的节点还会原样出现，浪费上下文、也让 widen 之后的地图看起来和之前几乎一样。→ 按 subgoal 记录这些节点，同 subgoal 后续视图隐藏（不进全局 `dismissed_section_ids`，不影响其它 subgoal / planning map）。
3. `widen` 和 `reharvest` 是两个语义重叠到没法讲清楚区别的决策：`reharvest` 带 anchor 直接进入；`widen` 原意是"不知道去哪就放宽范围"，但实现上只是清空 `scope_filter`（对 harvest 的入口点毫无影响）——这正是"widen anchor=''"空转的根因。两者都是"换个入口再采一次"，唯一差别是 anchor 从哪来。→ 合并成一个 `widen`：不接受模型给 anchor，确定性地把当前 anchor 上移一层父节点（粒度变粗，天然把之前被 dismiss 的子节点从新地图里剔除，同级兄弟自然露出来）；到文档根后再 widen → 没有更粗的粒度了，确定性降级为 `drop`。

### F1 依赖饥饿 → 解锁条件改为 `settled`

- **现象**：后继 subgoal 一直不跑，或整波卡死。
- **根因**：`ready_subgoal_ids`（`nav_orchestrate`）解锁过严——依赖链上任何一个前驱只要没进 `satisfied_subgoal_ids`（哪怕已经明确 `drop` 掉、不会再有更新了）就永久卡住后继；槽位没填满时同样直接拒绝执行，而不是带着已有绑定降级重试。
- **修法**：引入 `state.dropped_subgoal_ids`（`drop` 决策的终态归宿，与 `satisfied` 并列，二者不相交）。`ready_subgoal_ids` 的依赖判定从 `d in satisfied` 改成 `d in settled`（`settled = satisfied ∪ dropped`）——前驱不管成没成，只要"不会再变"就放行后继。同时去掉"槽位必须能完全填充才可执行"这道门（这本来就是 `bindable_retrieval_queries` 的门槅，只在 deps 还没 settled 时该拦；deps 已经 settled 后，槎位缺失交给 `_unbound_retrieval_query` 降级成裸查询，由 `plan_control` 事后 widen/drop，而不是永久假死）。

### F2 `widen`/`reharvest` 空转 → 合并成一个确定性 `widen`

- **现象**：`plan_control` 判 `widen` 后重试，检索位置没变，白烧一轮控制调用。
- **根因**：旧方案里 `widen`（清空 `scope_filter`，对 `resolve_harvest_anchor` 的入口解析完全没有作用）和 `reharvest`（模型给 anchor，但 `resolve_harvest_anchor` 每次都无状态地重新从 `route_hints` 里挑"第一个没被收集过的" —— 同一个错误锚点会被反复选中，因为它没被收集≠它没被看过没选中）互相踩脚，anchor 到底该谁定、定完怎么持续生效，两条路径各管一半、都没管全。
- **实测**（长河坝 fusion，档案库 Q2 复现同样模式）：

```
wave1: s1 accept
wave2: s2 widen, anchor=""
wave3: s2 widen, anchor=""
```

- **修法**（新增 `NavState.subgoal_anchor: Dict[str, Optional[str]]`，记录每个 subgoal 当前该从哪个 anchor 进入 harvest，一旦解析就保持粘滞，只有 `widen` 才移动它）：
  1. `resolve_harvest_anchor` 第一次解析：`route_hints` 里第一个"没被收集过、没被这个 subgoal dismiss 过、没跨出 `scope_filter.doc_ids`"的 hint，否则文档根（`None`）；解析结果写进 `subgoal_anchor[sid]`，此后同一 subgoal 直接读缓存，不再重新扫 `route_hints`。
  2. `plan_control` 只再做三种 per-subgoal 决策：`accept` / `widen` / `drop`（删 `reharvest`，`SubgoalDecision` 不再带 `anchor` 字段——不需要模型猜锚点）。
  3. `widen` 由 `nav_orchestrate._apply_plan_control` 确定性执行：查 `subgoal_anchor[sid]` 当前值的父节点（`nav_harvest.resolve_parent_section_id`，跨 knowhere/legacy 两种 ToolSpace 后端），写回 `subgoal_anchor[sid]`；当前已经是 `None`（文档根，已是最粗粒度）时无处可widen，直接强制降级为 `drop`。电路breaker（`subgoal_max_attempts` 累计次数触发降级 `drop`）保留，仍然只有一种循环（widen）需要断路。

### F3 单发 harvest 欠采 → 靠 F2 的新 widen + dismiss 自然吸收，不再单独开补采通道

- **现象**：答案可能对，但 gold / 依据节点未进证据包（complex5 漏 `L22`；baseline 长河坝漏第一跳 `2.5.4.2`，靠推断答「泸定」）。
- **根因**：`harvest` 一次成型、模型倾向"标题够清楚就直接 collect 不深挖"（旧提示词里明确写了"Prefer being decisive... collect directly instead of dispatching"），偏置鼓励欠采；漏节点后只能靠模型从已有证据推断，原方案想加一条独立的"accept 前补采一轮"通道来弥补。
- **为什么不需要独立通道**：F2 的新 `widen` 每次上移一层父节点，父节点的地图天然包含了之前没被选中的兄弟节点；配合 F1 新增的"看过未选即 dismiss"，被驳回过的分支不会重新占位——`plan_control` 只要判"不满足"就 `widen`，下一轮 harvest 看到的就是"更粗粒度 + 已排除死胡同"的新地图，等价于一次有方向的补采，不需要再发明一条平行的"补采"决策类型。
- **仍要做的收口**：把 `harvest` 系统提示词里"标题/摘要够清楚就直接 collect、别 dispatch"这条决策偏置去掉，改成中性描述（不确定就 dispatch 而不是直接 collect 或者跳过）；顺带告知模型"没被选中的可见节点这个 subgoal 以后不会再看到"，让模型的 collect/dispatch/跳过 三选一决策更审慎，而不是靠提示词诱导它少选。

### 新增状态字段（`NavState`，均无默认硬编码阈值，复用既有 `subgoal_max_attempts` 断路器）

| 字段 | 用途 | 替代/删除 |
| --- | --- | --- |
| `subgoal_anchor: Dict[str, Optional[str]]` | 每个 subgoal 当前粘滞 anchor（`None`=文档根） | 替代 `subgoal_reharvest_anchor` |
| `subgoal_dismissed_section_ids: Dict[str, Set[str]]` | 每个 subgoal 看过未选（含颗粒无收的 dispatch 分支）的节点 | 新增；不复用全局 `dismissed_section_ids`（那个字段继续保持"从未写入"的现状，用于其它尚未接的路径） |
| `dropped_subgoal_ids: Set[str]` | `drop` 的终态归宿，供 `ready_subgoal_ids` 的 `settled` 判定使用 | 新增；与 `satisfied_subgoal_ids` 并列不相交 |

## 七、接入契约速查

```python
# 唯一替换点
async def run_retrieval_route(context: RetrievalRouteContext) -> RetrievalRouteOutcome
# execution/routes.py:33；plan.py:145 是唯一调用方
```

`response` 必含：`namespace / query / router_used / evidence_text / results`  
`results` 行需满足：`hydration/row_utils.py` 白名单 + `job_id/file_path/chunk_metadata`（资产）+ `document_id/chunk_id`（hit stats）

## 八、刻意不做

- 不引入 `SEARCH_IMAGES` / `SEARCH_TABLES` / VLM
- 不把内核改成 async
- 不把 `__corpus__` 合成 id 当成 knowhere 标准
- 不用 CORPUS 节点临时处置冒充生产模型
- 不碰 API 请求/响应契约；只换路由实现
