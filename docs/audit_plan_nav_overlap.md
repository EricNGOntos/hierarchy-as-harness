# PLAN × NAV 重叠审计与融合瘦身方案

本文档是 2026-08 一轮 "PLAN NAV 融合瘦身" 改动的审计记录 + 设计依据。`src/nav`
下多处代码注释直接引用本文档的章节号（例如 `nav_control.py` 引用 `§1.6`，
`nav_orchestrate.py` 引用 `§1.4-1` / `§2.4`，`nav_hierarchy.py` 引用
`§ToolSpace surface`），修改这些章节号时请同步修改引用处。

## 1. 现状审计：NAV 为什么重、PLAN 和 NAV 到底重叠在哪

### 1.1 NAV 的"重"从哪来

`navigate()` 是一个 ReAct 循环：每一步都要问一次 LLM "COLLECT / DISPATCH /
FINISH 选哪个"，DISPATCH 命中子树后还会递归再开一整套
COLLECT/DISPATCH/FINISH 循环（`enable_recursive_dispatch` +
`max_dispatch_depth`）。在 `enable_plan_orchestration=True` 之后，这套循环
是**每个 subgoal 各跑一遍**，于是单次检索请求的 LLM 调用量 =
`n_subgoals × navigate_max_steps × (1 + recursive dispatch 展开的子树数)`，
外加每个 subgoal 的 contract verify（可选 LLM 抽取）、以及原 REPLAN 触发
时的完整重跑。这是成本的主要来源，也是"太笨重"的直接原因。

### 1.2 depth 塌缩与 FINISH 膨胀

`enable_plan_orchestration` 下，每个 subgoal 的 `navigate()` 都从
`depth=0` 重新开始（`_run_navigate_for_query` 固定传 `depth=0`）。这意味着
"只有 depth 0 享受 group_rank 外部重排" 这条原本为单文档单 episode 设计的
特权，在多 subgoal 场景下被重复触发 N 次而不是 1 次（见 §2.5）；同时
"地图看起来够不够、要不要 FINISH" 这个判断也在每个 subgoal 的每次
attempt 里各自问一遍 LLM，而不是把"够不够"交给一个更懂全局的裁判。

### 1.3 未使用的 plan 产物：`route_hints`

`plan_query` 已经在生成 `Subgoal.route_hints`（规划阶段在地图上标出的锚点
N* id / section_id），但融合之前的 `navigate()` 从不读它——每个 subgoal
不论 planner 给出多精确的锚点，执行时都从文档/语料根重新走一遍完整的
COLLECT/DISPATCH 决策链。这是最直接的"PLAN 算过的东西 NAV 不认"的重叠浪费。
融合后由 `nav_harvest.resolve_harvest_anchor` 消费它（见 §2.1），解析结果
粘在 `state.subgoal_anchor[sid]` 上，只有 `plan_control` 的 `widen` 决策
（`nav_orchestrate._apply_plan_control`）才会移动它——一次性解析，而不是
每次都重新扫一遍 `route_hints`（2026-08-09 修订：早期版本每次都无状态重扫
`route_hints`，"没被收集过"≠"没被看过没选中"，同一个错误锚点会被反复选中，
是 F2 空转的根因之一，见下）。

### 1.4 证据归属泄漏

#### 1.4-1 `_verify_subgoal` 用全局证据池验证单个 subgoal

融合之前，contract verify 调用 `build_evidence_text_from_state`——拼接
`state.collected` 里**从 episode 开始以来收集的所有证据**，而不是"这个
subgoal 这一次 attempt 新收集的证据"。后果：
- 一个 subgoal 可能因为**另一个 subgoal**碰巧收集到的、字面上命中
  `must_mention` 的文本而被误判 `SATISFIED`。
- REPLAN 之后重新验证时，旧 subgoal 已经满足的证据会持续污染新 subgoal
  的验证结论。

修复：`nav_verify.build_evidence_text_from_chunks(chunks)` 只接受调用方
显式传入的 chunk 列表；`_verify_subgoal` 现在总是用
`state.collected[before_len:]`（本次 attempt 新增的 chunk）而不是整个
`state.collected`。旧的 `build_evidence_text_from_state`（拼接整个
episode 累积证据池）已确认无任何调用点后整体删除，不保留死代码。

#### 1.4-2 地图失明：collected 分支从地图上被整段删除

`_build_map_tree` 原来把 `collected_section_ids` 直接并入 `gone`
集合——COLLECT 过的分支从地图上彻底消失。这对同一个 subgoal 内部的连续
决策是对的（不会重复收集），但对**跨 subgoal / REPLAN 后的新一轮规划**
是有害的：planner 和后续 subgoal 的 harvester 看到的地图会漏掉"这块已经
被覆盖过"这个信息，只能靠 `collected_section_ids` 这个不可见的 side
channel 去猜，容易导致 REPLAN 生成的新 subgoal 重新扫一遍已经覆盖过的
区域，或者反过来误以为覆盖区域"不存在"而放弃探索它的邻居。

修复见 §2.3（`[harvested:sN]` 渐进可见性）。

### 1.6 四个互不通气的"够不够"判据 + 跨 subgoal report 泄漏

融合之前，一次 plan 执行里同时存在四个独立的"这个区域够不够/该不该继续"
判据，彼此不通气、不共享证据、不共享结论：

1. **NAV 内层 FINISH**：`navigate()` 循环内，模型每步都可以选 FINISH 退出
   当前 scope——这是"够不够"的第一层判断，纯靠单次 LLM 上下文里能看到的
   地图片段。
2. **depth-0 的 `group_rank` 重排**：`enable_external_rerank` 在 depth 0
   额外问一次"这些已收集的组，谁更该往前排"，某种程度上也是一种"当前
   证据够不够、该给谁让路"的判断，但只在 depth 0 触发、且每个 subgoal
   各触发一次（见 §1.2、§2.5）。
3. **子 agent 自由文本 report**：递归 DISPATCH 展开的子树在返回时会把自己
   的发现写成一段自由文本塞进 `state.reports_context`，供父层参考——这段
   文本不但没有结构化的"够/不够"结论，还会在 subgoal 间不清空的情况下
   持续累积，造成 prompt 膨胀（跨 subgoal report 泄漏）。
4. **PLAN 的 contract verify**：`verify_contract` 是唯一带结构化 verdict
   （SATISFIED/RETRY/WIDEN/REBIND/REPLAN）的判据，但它只在每个 subgoal
   attempt 结束后才跑一次，看不到 1-3 的过程信息，也无法在 subgoal 之间
   做全局取舍（例如"s1 该 widen 还是该整体 replan"这类判断需要看到全部
   subgoal 的情况，而 verify_contract 只看单个 subgoal）。

修复：合并 1/2/3 为单次 `harvest()` 决策（隐式 FINISH，不再有独立的"是否
结束"往返；不再有 depth-0 特权重排；不再有自由文本 report——见 §2.1），
用零成本的规则判据（`verify_contract`，不消耗 LLM）取代 4 里对 LLM 的
依赖作为唯一输入，再引入 `plan_control()` 作为**唯一**读全局证据、下
结构化决策（accept/widen/drop + 全局 continue/replan/done）的
裁判（见 §2.2）。旧的"attempts 耗尽→自动升级为 REPLAN"路径
（`_execute_subgoal_with_verdicts` 内的逻辑）在 `enable_plan_control=True`
时不再被调用——REPLAN 只能由 `plan_control` 发出。

## 2. 融合设计（已实现，均由 config 开关灰度控制，默认关闭=不变旧行为）

### 2.1 `harvest()`：单次决策 + 隐式终止 + 仅溢出递归（`nav_harvest.py`）

替换掉"多步 ReAct 循环 + 独立 FINISH 往返"，改为**每个可见地图区域一次
LLM 调用**：模型在一次响应里返回要 COLLECT 的节点集合和要 DISPATCH 给更
深层 harvester 的节点集合；两者都不选 = 隐式结束这个区域，不再有额外的
"你确定要结束吗"往返。递归只在模型显式选择 DISPATCH 时才发生，并由
`max_harvest_depth` 硬性限界（独立于 `navigate()` 自己的
`max_dispatch_depth`，两者共享 `nav_actions.build_legal_actions` 的
DISPATCH 合法性判断——即 DISPATCH 选项本身仍受 `enable_recursive_dispatch`
/`max_dispatch_depth` 门控，`max_harvest_depth` 是 harvest 自己的递归深度
上限，二者都满足才会真正递归）。

`resolve_harvest_anchor`（`enable_anchor_entry`）把 §1.3 提到的
`route_hints` 接上：每个 subgoal 第一次调用时从 `route_hints` 里挑一个
可用的入口（跳过已收集 / 已被这个 subgoal dismiss 过 / 越出
`scope_filter.doc_ids` 的候选），否则退回文档根，而不是每次都从文档/
语料根重新展开完整的地图决策链；结果粘在 `state.subgoal_anchor[sid]`
上，后续调用直接读缓存。`scope_filter.doc_ids` 声明过的 subgoal 永远不会
被锚点带出自己声明的文档边界。

每次 `harvest()` 调用里，"看到过（有 collect/dispatch 选项）但既没
collect 也没 dispatch"的直接子节点 + 自身，会被记进
`state.subgoal_dismissed_section_ids[sid]`（整棵 dispatch 子树颗粒无收时
也会把 dispatch 目标本身记进去）；同一 subgoal 后续任何一次 harvest 调用
都会把这些 id 从地图里剔除（`nav_projection.build_map` 的
`dismissed_section_ids` 入参，按 subgoal 各自维护，不进全局
`state.dismissed_section_ids`，不影响其它 subgoal）。这是 widen 上移到父
节点后能看到"真正还没看过"的兄弟节点、而不是原样再看一遍已经拒绝过的
节点的关键。

### 2.2 `plan_control()`：唯一检查权威（`nav_control.py`）

每个 wave 结束后调用一次（而不是每个 subgoal 各自调用）：输入是这个 wave
里每个 subgoal**自己新收集的证据**（`new_chunks`，绝不是全局池——直接
复用 §1.4-1 的 `collected_before` 差分修复）+ 零成本的规则判据
（`verify_contract` 的输出，不额外花 LLM 调用）+ `harvest_reason`（harvester
自己对这一轮看到什么、为什么选/不选的解释——2026-08-09 之前只写进
`AgentStep.detail` 供 TRACE 用，从未传回 `plan_control` 的输入，控制器只能
靠零成本规则信号猜；现在并入每个 subgoal 的证据块）。输出是每个 subgoal
的 `accept/widen/drop` 决策 + 一个全局的 `continue/replan/done` 决策。

`reharvest` 已经删除（2026-08-09）：原方案 `reharvest`（模型给 anchor）和
`widen`（清空 `scope_filter`，对 `resolve_harvest_anchor` 的入口解析完全
没有作用）两条决策一起管"换个入口再采一次"，却没有一条把 anchor 到底该
定成什么、定完怎么持续生效的全部逻辑管全——这正是 F2 空转
（`widen, anchor=""`）的根因。现在只有一种"再采一次"决策：`widen` 由
`_apply_plan_control` 确定性执行，把 `state.subgoal_anchor[sid]` 移到当前
anchor 的父节点（`nav_harvest.resolve_parent_section_id`，同时兼容
knowhere/legacy 两种 ToolSpace 后端）；不接受模型给 anchor。当前 anchor
已经是 `None`（文档根，已是最粗粒度）时无处可 widen，直接确定性降级为
`drop`。`_apply_plan_control` 里还有一个不依赖 LLM 的电路breaker：`widen`
累计次数达到 `subgoal_max_attempts` 时同样强制降级为 `drop`，避免
`plan_control` 判断出错导致的死循环——现在只有一种循环（widen）需要
断路，不再是两种互相踩脚的路径。

### 2.3 `[harvested:sN]` 渐进可见性（`nav_projection.py` / `nav_actions.py`）

修复 §1.4-2：`show_harvested_in_map=True` 时，已被某个 subgoal 收集的
分支不再从地图上整段消失，而是保留为一行折叠状态、标注
`[harvested:s1]`（`state.harvested_owner_subgoal: section_id -> subgoal_id`
记录归属）。其后代节点仍然像普通 collected 分支一样从地图隐藏（不重新
展开子树），保留的只是"这里已经被谁覆盖过"这条覆盖信息本身，不是重新
探索的入口。

### 2.4 REPLAN 状态处理：已经拿到手的不能丢

旧逻辑在 REPLAN 时无差别清空 `satisfied_subgoal_ids` /
`attempted_subgoal_ids` / `activated_subgoal_ids` / `slot_bindings` /
`subgoal_results`。问题：新 plan 的 subgoal id 从 `s1` 重新编号，旧 id
下累计的 per-id bookkeeping 确实不能带过去（语义已经变了），**但**
`slot_bindings` 里不带 `.` 的无限定 key（例如直接的事实值 `seal_type`）
和 `state.collected` 里已经收集到的 chunk 都是与 subgoal id 无关的、已经
证实有效的产出，没有理由跟着 REPLAN 一起丢弃。现在 REPLAN 时只清空
per-id 的四个集合/字典，`slot_bindings` 按 `"." not in k` 过滤后保留，
`state.collected` 完全不受影响。

### 2.5 `group_rank` 结算时机后移到 settle（`nav_navigate.py`）

§1.2 提到的"depth-0 特权"在 plan 执行下会被每个 subgoal 的
`navigate()` 各触发一次，最后一个跑完的 subgoal 的排序结果会覆盖前面
所有 subgoal 的排序（`state.group_priority` 是单一全局字典）。
`enable_settle_group_rank=True` 时，在 `state.retrieval_plan is not None`
的情况下直接跳过这次逐 subgoal 的重排 LLM 调用，把排序完全交给
`settle_subgoal_evidence` / `pack_nav_evidence` 打包时本来就有的
按分数排序兜底逻辑，作为唯一一致的排序策略，省掉这次多余的 LLM 调用。

## ToolSpace surface（`src/nav` 实际依赖的最小面，供 knowhere-main 移植）

审计 `src/nav` 全部对 `ts` 的调用（`map_mode=True` 路径，即 harvest/
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

`src/nav/nav_hierarchy.py` 把这 5 个方法定义为 `HierarchyProvider`
Protocol，`ProviderToolSpace` 把任意实现适配成上面的 ToolSpace 鸭子类型
——knowhere-main 只需要实现 `HierarchyProvider`（层级节点 + summary，不需要
BM25/dense 索引、不需要 `_idx`），`src/nav` 下其余文件不需要改一行。验收
测试见 `tests/test_nav_hierarchy_adapter.py`：一个纯内存 provider 驱动完整
的 plan → harvest → plan_control → settle 链路。

## 3. 配置开关（默认全部关闭 = 与融合前行为完全一致）

| 开关 | 默认 | 作用 |
| --- | --- | --- |
| `enable_anchor_entry` | `false` | harvest 从 `route_hints` 解析出的粘滞 anchor 进入，而非总从根开始 |
| `enable_one_shot_harvest` | `false` | 用 `harvest()` 替换 `navigate()` 作为每个 subgoal 的执行原语 |
| `max_harvest_depth` | `3` | harvest 递归深度上限（独立于 `max_dispatch_depth`） |
| `enable_plan_control` | `false` | 用 `plan_control()` 替换逐 subgoal 的 verdict 自动升级/REPLAN 路径 |
| `plan_control_digest_chars` | `600` | 每个 subgoal 展示给 `plan_control` 的证据摘要字符上限 |
| `show_harvested_in_map` | `false` | 已收集分支保留为 `[harvested:sN]` 而非从地图整段删除 |
| `enable_settle_group_rank` | `false` | plan 执行下跳过逐 subgoal 的 depth-0 重排，交给 settle 阶段的分数排序兜底 |

四个开关独立生效，但只有同时打开 `enable_anchor_entry` +
`enable_one_shot_harvest` + `enable_plan_control` 才构成完整的融合路径；
`enable_contract_verify`（LLM 槎位抽取）、`enable_subgoal_budget_ledger`
等既有 M5/M6 开关与本轮改动正交，行为不变。

## 4. 已知局限（未在本轮解决，留给后续）

- `nav_projection.py` 的行内摘要仍然从独立的 `section_summary_store`
  取，不是 `HierarchyProvider.node_meta().summary`——移植到
  knowhere-main 时这一路径会静默降级为空摘要（已有 try/except 兜底，
  不会崩溃，但摘要质量会下降）。如果 knowhere-main 的摘要不走同名模块，
  需要单独接一层适配。
- `max_dispatch_depth`/`enable_recursive_dispatch` 仍然同时门控
  `navigate()` 和 `harvest()` 的 DISPATCH 合法性（见 §2.1）；如果未来
  需要让两条路径的递归深度完全独立配置，需要在 `build_legal_actions`
  里把这两个门控参数化，而不是复用同一对配置字段。
