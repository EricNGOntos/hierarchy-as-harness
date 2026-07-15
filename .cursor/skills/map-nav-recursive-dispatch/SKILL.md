---
name: map-nav-recursive-dispatch
description: >-
  Hierarchy-as-harness recursive-dispatch MAP navigation: terminology (N* vs
  C*/D*/F* vs L*), algorithm (COLLECT/DISPATCH/FINISH), TRACE reading, and
  known packing failure modes. Use when editing src/nav, map nav configs,
  TRACE/replay, scope_0030-style case analysis, or when the user mentions
  map-nav, DISPATCH, action tree, N19, D6, section_id, or gold Lxx nodes.
---

# MAP 递归分派导航（语言对齐 + 算法）

与用户讨论本仓库 map-nav 时**必须**遵守本 skill 的术语；禁止混用或把内部 `Lxx` 说成 agent「点选」的目标。

## 1. 三套 ID（必对齐）

同一树行上有三套符号，职责不同：

| 符号 | 名称 | 谁看见 | Agent 是否输出 |
|------|------|--------|----------------|
| `N19` | map 显示编号 | 观测树行首 `[N19]` | **否** |
| `D6` / `C19` / `F1` | **可执行动作 ID** | 行尾 `actions: collect=C…, dispatch=D…` | **是**（唯一合法选择） |
| `doc:L92` | **section_id**（内部） | 代码 / gold / TRACE 字段 `section_id` | **否**（由动作 ID 解析得到） |

**正确说法：**

> Agent 选了 `D6`；`D6` 挂在 `N19` 那一行；该行内部 `section_id` 是 `…:L92`。

**错误说法：**

- 「Agent 选了 N19」（模型 JSON 不写 N*）
- 「Agent 选了 L92」（观测树不要求写 L*；L* 是解析结果）
- 把 `Lxx` 和树上的 `N*` / `C*`/`D*` 当成同一层符号混讲

### 观测行形态（KNOWHERE 风格）

```text
[N19] 2.4.4 重大事故隐患整改… (11 chunks) actions: collect=C19, dispatch=D9
```

- 根 scope：标题为主，一般不内联 summary  
- 子域（DISPATCH 后）：可内联 `summary:`  
- `[Hit]` = highlight rescue；`[Leaf]` = 无子节点 → 通常只有 collect，无 dispatch  
- **唯一硬显示预算**：`map_char_limit`（默认 5000）折叠；**不对动作空间做 top-K**

### LLM 输出

```json
{"action_id":"D6","reason":"…"}
```

多选同 kind：`{"action_id":"C1","ids":["C1","C3"],"reason":"…"}`  
最终选中集 = `action_id ∪ ids`；水合由层级决定（父=整枝，叶=仅自身）。  
`reason` 必须英文。解析：`action_id` → `LegalAction` → `section_id`。

## 2. 算法模型（现行）

核心：一个递归过程，外层与 subagent 都是它：

```text
navigate(scope, budget, depth) -> RegionReport
  观测 = 折叠标题图(scope)   # 超 map_char_limit 才折；Hit rescue；人人可选
  loop:
    COLLECT(ids)  -> 收 sid∪后代证据；枝从地图移除（collected_section_ids）
    DISPATCH(ids) -> 并发 navigate(child, budget', depth+1)；汇总 reports_context
    FINISH        -> 结束本层
```

| 动作 | 含义 |
|------|------|
| COLLECT | 证据入库；**不是**「走进该节点当 viewpoint」 |
| DISPATCH | 派子 agent 探索子树；**本层 viewpoint 不变**；取代旧 EXPAND/JUMP/PEEK/BACK |
| FINISH | 结束本 scope / 文档 |

**已删除（勿再实现/勿在 TRACE 里当现行）：** EXPAND / JUMP_TO / PEEK / BACK / covered_section_ids / action top-K。

### 递归开关

- `enable_recursive_dispatch=false`（实验默认）：**仅 depth=0** 可 DISPATCH；深层只有 COLLECT/FINISH；区域溢出可 skip+reason  
- `true`：允许更深 DISPATCH，受 `max_dispatch_depth` 约束  

### 其它现行约定

- **OUTLINE**：不暴露给 agent；`scope_collection` 等任务下关键词自动触发（`_is_scope_outline_query`）。TODO(knowhere-align): 迁回用 `query_intent`  
- **空 FINISH**：`collected` 空且剩余步数 >2 时不发 FINISH  
- **证据收尾**：去重 → `pack_nav_evidence`（按最近父分组；组内 `own_unit+w_conf·conf`，默认 `w_conf=0.5`；组间优先 `group_priority`（外部 FINISH `group_rank`），回退 `max(子最终分)`；父只做上一层路径表头；组内文档序缩进树；**组内跳过放不下的大块，继续塞能进剩余预算的短块**）
- **外部相对重排（depth0）**：有收集池时观测附 `Assembled Evidence` `[G*]` 预览；FINISH 须带 `group_rank`（序数相对排序）；写入 `NavState.group_priority`
- **COLLECT confidence**：LLM 对每个 collect id 给 `[0,1]`；水合后代缺省 0；缺失 confidence=0（组间主判别已转交外部 `group_priority`）
- **选中集**：`action_id ∪ ids` 合并为同一选中集；选完后按层级决定水合（父=整枝，叶=仅自身）
- 提示词：对齐 KNOWHERE collector 规则结构；**禁止**过拟合到具体题面；不做 SEARCH 图表（TODO knowhere-align）

## 3. 关键代码

| 路径 | 职责 |
|------|------|
| `src/nav/nav_navigate.py` | `navigate` / `dispatch` / 文档序排序 |
| `src/nav/nav_actions.py` | 人人可选 legal actions + 树观测渲染 |
| `src/nav/nav_policy.py` | LLM 提示词与 `action_id`/`ids` 解析 |
| `src/nav/nav_projection.py` | `build_map` 折叠 + Hit |
| `src/nav/nav_agent.py` | `run_nav_episode` → depth0 navigate；COLLECT hydrate |
| `src/nav/nav_compose.py` | COMPOSE：confidence 解析、父 scope 分组重排、缩进树打包 |
| `src/nav/nav_types.py` | `ActionKind` / `NavConfig` / `NavState` / `RegionReport` |
| `config/nav_default.json` | `map_char_limit`、`enable_recursive_dispatch` 等 |
| `bin/56_replay_map_nav_traces.py` | 单题/批量 TRACE 回放（evidence-only）；批量续跑见 skill [`map-nav-replay-batch`](../map-nav-replay-batch/SKILL.md) |

## 4. 读 TRACE 时怎么说话

1. 先报 **因果序**（JSON 里子步骤可能排在父 DISPATCH 前，勿被 step_idx 误导）  
2. 决策句式：`action_id=D6`（挂在观测行 `N…`；内部 `section_id=…:L92`）  
3. 展示观测树时突出行尾 `actions:`，不要只报 L*  
4. gold 评估可以说 `gold nodes L94–L99`，并同时指出树上对应的 C*（若可见）

典型因果序（scope_0030）：

1. 根 `D6` DISPATCH → 内部 L92  
2. 子 `C2` COLLECT → 内部 L93  
3. 子 `C1` COLLECT → 内部 L92（整枝）  
4. 子 `F1` FINISH  
5. 根 `C5` COLLECT → 内部 L84  
6. 根 `F1` FINISH  

## 5. 已知失败模式（勿误判为「跳不进树」）

导航常已命中正确子树且 gold 行带 COLLECT；终局 `gold_recall=0` 常见原因：

- **旧 packing（已替换）**：曾用 `evaluate_at_budget` 全局 score 降序，长块挤掉短 gold；现行改为 `pack_nav_evidence`（confidence + 父 scope）
- 根在子报告已充分后仍 COLLECT 干扰叶，进一步占预算  
- 子 agent 先收引言行再收父节（可选 multi-collect 叶列表，属策略不是动作空间缺失）
- **层级错标**：gold `levels_for_tree` 把兄弟节标成后代（如 2.4.5 挂进 2.4.4），整枝水合会带入噪声；属数据问题，非导航动作缺失

## 6. 改代码时的硬约束

- 除 `map_char_limit` 显示折叠外，**不对动作空间硬截断 / top-K**  
- 不恢复 JUMP/PEEK/EXPAND 当主循环  
- 不把 `covered` 与 `collected` 再拆开  
- 用户问「树上怎么选」→ 答 **C*/D*/F***，再补 N* 行与 L* 内部映射  

## 补充

- 更细的配置字段与 scope_0030 对照：[reference.md](reference.md)
