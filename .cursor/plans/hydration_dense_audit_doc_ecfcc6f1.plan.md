---
name: Nav Compose 置信度重排 + 层级树展示
overview: 确认 map-nav 导航与水合本身正确、层级错标暂不修、dense/向量部分已完成移除；核心改造聚焦 COMPOSE 收尾——(1) COLLECT 时采集 LLM 置信度；(2) 父节点只作路径信号/分组表头、不作独立 evidence 单元，改为按「最近父」分组、组内以「子节点 own_unit + w_conf·confidence」排序、组间用「组内子节点最终分的 MAX-pool（含 confidence）」排序，取代全局纯 score 降序；(3) 按「最近一层父节点」把同父子节点聚合成缩进层级树展示，仅展示上一层父、不从 ROOT 一路拼，节约上下文预算。
todos:
  - id: collect-confidence
    content: nav_policy 提示词 + 解析采集每个被 COLLECT 子节点的 confidence(0-1)，写入 NavState；水合补充的后代 confidence=0
    status: completed
  - id: combined-rerank
    content: 终局重排改为「按最近父分组、组内 own_unit+w_conf·conf 排序、组间用子最终分的 MAX-pool（含 conf）」；父不占节点位；替换 use_branch_max 整枝压平与全局 score 降序
    status: completed
  - id: tree-compose-render
    content: COMPOSE 展示改为按最近一层父节点聚合的缩进层级树（≥2 同父才聚合，仅显示上一层父路径，组内文档序）
    status: completed
  - id: scope0030-verify
    content: 用 scope_0030 反事实核对：gold L94-L99 应在 500 字内被保留且 gold_recall 上升
    status: pending
isProject: false
---

# Nav COMPOSE 置信度重排 + 层级树展示方案

## 目标与边界

- **只改 COMPOSE 收尾链路**（置信度采集 → 合并重排 → 层级树展示）；不动导航主循环（COLLECT/DISPATCH/FINISH）、不动水合的「收父=整枝纳入」语义。
- **导航与水合本身判定为正确**：scope_0030 已证实导航命中正确子树、gold 全程在收集池内（见 §2）。「先选子、再选父 → 纳入父下全部节点」是期望行为，保留。
- **层级错标暂不修**：`L102/L103`(2.4.5/2.4.6) 落进 `L92`(2.4.4) 子树，根因是 **gold 标注层级错误**（2.4.5/2.4.6 被标成 level=4 而非同级 level=3，见 §2.3），属数据/建树上游问题，本轮不处理。
- **dense/向量部分已完成**：原 §5「dense 除以0 / matmul 审计」及相关 D1-D3 已落地，从本方案移除。

## 1. scope_0030 失败复盘（一句话定位）

案例：`real_69c60974d4242eda8c47c615_scope_collection_auto_0030`，Query「列出重大事故隐患治理方案必须包含的所有内容要素」，gold=`L94–L99`，终局 `gold_recall=0`。

因果序（TRACE）：

1. 根 `D11` DISPATCH → 子 agent 进 `L92`。
2. 子 `C2` COLLECT `L93` multi→`[L93,L94,L95,L96,L97,L98,L99]`，`+7`：**6 个 gold 全部精选到位**（这一步完全正确）。
3. 子 `C1` COLLECT 父 `L92`：purge 后代独立证据 ×7，整枝重灌 `+11`（`L93–L103`）：gold 重新纳入 + 混入 `L100–L103`（其中 `L102/L103` 系层级错标混入）。
4. 子 `F1` → 根 `C10` 再 COLLECT `L82`、`L84` → 根 `F1`。
5. 收尾 `evaluate_at_budget` **按 score 降序**填 500 字：长且高分的 `L92/L102/L103` 吃满预算，**又短又低分**的 gold `L94–L99` 垫底被挤出。终局 `retrieved=[L92,L93,L84,L102,L103]`。

**结论**：gold 一直在收集池里，丢失只发生在**收尾打包**。凶手是「纯 score 降序 + 长块 + gold 又短又低分」，不是导航或水合。

## 2. 事实依据

### 2.1 gold 全程在池

子报告 `collected 12 branch node(s)`：`L92,L93,L94…L99,L100…L103`，gold 齐全（`REPORT.md` reports_context）。

### 2.2 打包丢 gold 的机制

`run_nav_episode`（[`src/nav/nav_agent.py`](src/nav/nav_agent.py) L700-708）：`sort_collected_by_doc_order` 排好文档序后，`evaluate_at_budget`（[`src/realdata/agent_delivery/code/budget_eval.py`](src/realdata/agent_delivery/code/budget_eval.py) L252 `ranked = sorted(..., key=-score)`）**重新按 score 降序**装填，文档序被覆盖。unit 分：`L92=0.0734, L93=0.0734, L102=0.0660, L103=0.0639`，gold `L94–L99=0.033–0.055`——gold 排在长块之后被挤出。

### 2.3 层级错标（不修，仅记录）

实测 `tree_source=gold` 下 `L92–L104` 的 `gold_level`：`L82/L85/L89/L92/L104` 均为 3（2.4.1/.2/.3/.4/.7），但 `L102(2.4.5)/L103(2.4.6)` 被标为 **4**，于是父指针与 span 规则确定性地把它们挂到 `L92` 下。属标注错误，`levels_for_tree` → `build_parent_pointers`/`_subtree_bounds_for_section_path` 只是忠实复现。

## 3. 设计一：COLLECT 采集置信度

**动机**：让「agent 主动精选的 gold」与「水合顺带纳入的噪声」在重排时可区分。

- **提示词**（[`src/nav/nav_policy.py`](src/nav/nav_policy.py) `_system_prompt` / 返回格式）：要求 COLLECT 时对每个 `ids` 项给出 `confidence ∈ [0,1]`。约定返回形如：
  `{"action_id":"C2","ids":["C2","C3",...],"confidence":{"C2":0.7,"C3":0.9,...},"reason":"..."}`
  （单选时可用标量 `confidence`；缺省视为一个中性默认值，作为决策点见 §7）。
- **解析**（`choose_llm_action` / `_normalize_id_list`）：把 `confidence` 按 action_id → `section_id` 映射，随 `selected_section_ids` 一并回传 meta。
- **落库**（`NavState`，[`src/nav/nav_types.py`](src/nav/nav_types.py)）：新增 `collect_confidence: dict[str, float]`（key=section_id）。
  - 显式 COLLECT 的**子节点**：写入 LLM confidence。
  - **水合顺带纳入的后代**（`_collect_by_unit_scores` 里非 action 目标、以及 `_purge_descendant_evidence` 后整枝重灌进来的 `L100–L103`）：`confidence = 0`。
  - **父节点不作为 evidence 单元**（§4），其 confidence 不进入子节点打分；显式 COLLECT 父（如 `L92`）只表示"把该父下子节点纳入 scope"。

## 4. 设计二：以「父节点 scope」为单位的分组内重排

替换终局「全局纯 score 降序」打包。核心心智：**父子并存是所有情况的常态**——因为每个 evidence 节点都要带**最近一层父**作为路径信号。所以重排不是把全体节点拉平混排，而是**先按最近父分组，再在每个父的 scope 内对子节点排序**。

**父节点不作为独立 evidence 单元**：
- 父（如 `L92`）**只承担「路径信号 + 分组表头」**，本身**不占一个竞争预算的节点位**、不参与和其它节点的横向打分比较。
- 真正参与打分/装填的单元是**子节点**（叶）。这直接修掉现状 `_collect_by_unit_scores` 的 `use_branch_max` 把**整枝所有节点压成同一个 `branch_max`**（[`src/nav/nav_agent.py`](src/nav/nav_agent.py) L586）导致 gold 与噪声同分的问题。

**子节点最终得分**：
```
score(child) = own_unit(child) + w_conf * conf(child)
```
- `own_unit`：子节点自身 unit hybrid 得分（沿用 [`_unit_score_for_evidence_chunk`](src/nav/nav_agent.py)）。
- `conf`：§3 采集的置信度；显式精选子=LLM 值；水合顺带纳入的后代（`L100–L103`）=0。
- `w_conf`：把 [0,1] 置信度抬到与 unit 分（约 0.03–0.07）同量级并占主导，初值建议 `~0.1`（决策点，见 §7）。

**两层排序**：
1. **组内**：同一父下的子节点，按 `score(child)` 决定进预算的优先级（confidence 让 gold 稳定高于 `L100–L103`）；**展示时组内按文档序**（列表项 1./2./3.… 的自然顺序）。
2. **组间**：多父 scope 之间的先后，用**派生自子节点的组 key**排列：
   ```
   group_key(parent) = max_{child ∈ parent} score(child)   # 即含 confidence 的最终分
   ```
   即"一个父 scope 的强度 = 它最强子节点的强度"。父仍不占节点位、不产出独立 evidence 块，只把子的最大分作为组排序 key。
   - **组 key 含 confidence**（用子最终分，非仅 `own_unit`）：否则会在组这一层重犯"离题高 unit 组盖过 gold 组"的错——例：`w_conf=0.1` 时 gold 组最强子 `0.055+0.1·0.9=0.145` 应压过离题组 `0.08+0=0.08`；若只比 `own_unit` 则 0.055<0.08、gold 组反而靠后。
   - 组间是否改回文档序、或组是否给最小配额，见 §7。

如此 scope_0030 的效果：`L92` 只作为 `[§ 2.4.4]` 表头出现一次；其下子节点 `L93–L103` 在该 scope 内按 `score` 竞争预算，gold `L94–L99`（conf>0）胜出、`L100–L103`（conf=0）被挤出，组内再按文档序输出。

## 5. 设计三：COMPOSE 层级树展示

替换 `_block_text_for` 的「每块一个完整 `[§ 祖先路径]` 扁平罗列」，改为按**最近一层父节点**聚合的缩进层级树。

规则（与 §4 的分组一致——父只是表头，不是节点）：
- **聚合条件**：被保留的子节点中，只要有 **≥2 个共享同一直接父节点**，就归到该父下渲染成缩进树；父标题（路径信号）只展示**一次**。
- **纯叶场景**：若保留节点彼此无共同父（全是孤立叶），退化为扁平展示（等价现状）。
- **只展示上一层父**：父标题只取**直接父节点**一层（如 `2.4.4`），**不从 ROOT（第二章/2.4/…）一路拼**，节约上下文预算。
- 组内子节点按**文档序**（line 顺序）排列；组间按 §4 的组排序 key。

scope_0030 期望产出（500 字内）：
```
[§ 2.4.4 重大事故隐患整改、复查、销项]
对重大事故隐患…方案包括以下内容：        (L93)
  1、治理的目标和任务；                   (L94*)
  2、采取的方法和措施；                   (L95*)
  3、经费和物资的落实；                   (L96*)
  4、负责治理的机构和人员；               (L97*)
  5、治理的时限和要求；                   (L98*)
  6、安全措施和应急预案。                 (L99*)
```
gold `L94–L99` 因 confidence>0 且体量小，全部保留 → `gold_recall` 显著上升；`L102/L103`(conf=0、长) 被合并分挤到预算外。

## 6. 代码落点与改动清单

| 环节 | 文件 / 符号 | 改动 |
|---|---|---|
| 采集置信度 | [`nav_policy.py`](src/nav/nav_policy.py) `_system_prompt` / `choose_llm_action` / `_normalize_id_list` | 提示词加 confidence；解析映射 action_id→section_id→conf |
| 状态 | [`nav_types.py`](src/nav/nav_types.py) `NavState` | 新增 `collect_confidence: dict[str,float]` |
| 写入 conf | [`nav_agent.py`](src/nav/nav_agent.py) `_add_scored` / `_collect_by_unit_scores` / `_purge_descendant_evidence` | 显式精选子写 conf；水合后代 conf=0；父不作节点、conf 不入子打分 |
| 分组内重排 | [`nav_agent.py`](src/nav/nav_agent.py) `run_nav_episode`（L700-708 收尾） | 按最近父分组；组内 `score=own_unit+w_conf·conf`；组间 `group_key=max(子最终分)`（含 conf）；取代 `use_branch_max` 整枝压平与全局 score 降序 |
| 层级树展示 | 新增 nav 侧格式化（替代 [`_block_text_for`](src/realdata/agent_delivery/code/budget_eval.py) 在 nav 路径的调用）/ 或扩展 [`_prepare_compose_evidence_text`](src/nav/nav_agent.py) | 同父聚合、仅上一层父、组内文档序 |

**隔离原则**：`evaluate_at_budget` 为多实验共用，尽量**不改其通用语义**；合并重排 + 层级树渲染优先落在 **nav 收尾链路**（`run_nav_episode` / nav 侧新 formatter），避免污染其它 runner。

## 7. 决策点（实现前确认）

- `w_conf` 取值（confidence 与 unit 分的相对权重）；建议 `0.1` 起，按 scope_0030 + multi_0010 调。
- 缺省 confidence（LLM 未给时）取 0 还是中性值（如 0.3）；影响水合/无置信度子节点的相对次序。
- **组间排序**：默认 `group_key=max(子最终分)`（含 conf，见 §4）；是否需要可切换回文档序（父在文中的先后）。
- **预算按组分配**：是否给每个父组一个最小配额（保证多组都露出），还是按 `group_key` 顺序逐组填、组内按 `score` 抢预算。
- 层级树里父标题的字数上限（现状祖先每级截 40 字，`tool_space.py:449`）。

## 8. 验证与后续

- 复现：`PYTHONPATH=src/nav:src/realdata python bin/56_replay_map_nav_traces.py real_69c60974d4242eda8c47c615_scope_collection_auto_0030`，对比 `REPORT.md` 的 `retrieved_nodes` 与 gold 命中。
- 通过判据：scope_0030 `L94–L99` 进入 500 字 evidence、`gold_recall` 上升；multi_0010 不回退。
- 本方案聚焦 COMPOSE；层级错标（§2.3）与水合语义保持不变。
