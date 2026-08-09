---
name: nav packing and recursive dispatch
overview: 重构 COMPOSE 打包/截断为"文档顺序 + selection_count 分层截断"（unit 只留给 MAP 投影、confidence 仅同层 tiebreak），并为大 section 开启"软触发递归分派"（大 scope 投影转 title-only + 全局 highlight 透传到子层 + 开启递归），以修复检索侧的 ② 打包挤出与 ③ 大 section 问题。
todos:
  - id: explicit-set
    content: NavState 增加 explicit_collect_ids 并在 _apply_collect/fork/merge 同步
    status: pending
  - id: selcount-helper
    content: nav_compose 增加 selection_count 计算（owner+祖先是否在显式选中集）
    status: pending
  - id: group-order
    content: 组间排序改 (-priority, doc_order)，preview 子节点改文档序，去掉 unit 驱动排序
    status: pending
  - id: pack-rewrite
    content: 重写 pack_nav_evidence：全量组装→分层截断(selection_count升/priority升/line_key降)→剪尾，永不按rerank删整组
    status: pending
  - id: highlight-alldepth
    content: navigate 各层透传 state.highlight_ids（去掉 depth==0 限制）
    status: pending
  - id: scope-titleonly
    content: build_map 大 scope 超 scope_inline_summary_char_limit 转 title-only
    status: pending
  - id: enable-recursion
    content: nav_default.json 开启 enable_recursive_dispatch 并加 scope_inline_summary_char_limit；NavConfig 增字段
    status: pending
  - id: tests-regression
    content: 更新 test_nav_compose 用例；按 Part 3.5 清单回归 48 题（Part1 11+1 / Part2 17 / 数据侧 20 负例）
    status: pending
isProject: false
---

# Nav 打包保序 + 大 section 递归分派修复方案

## 背景与目标
针对 48 个 `gold_recall=0` 中的检索侧问题：
- **②（11 个 pack-drop）**：AGENT 采了父 section，gold 子叶因 `unit` 低被组内分数排序挤出。
- **③（16 个，大 section / 评分选别处）**：大 section 被整体 COLLECT 只拿到 outline，或递归分派几乎没启用。
- 数据侧 ①（20 个）本轮不处理（Point 3 后续）。

自洽模型（已与用户确认）：
- **unit score** 单一职责：只用于最初 MAP 投影隐藏（`_apply_budget_hide`），退出打包与截断排序。
- **confidence** 单一职责：SUBAGENT 自评，仅作同层 tiebreak（本期可不参与，保留字段）。
- **selection_count（结构事实，1/2）** 驱动截断分层。
- 组内打包按**文档顺序**；SUBAGENT 不截断；只有最终 COMPOSE 对 `budget_chars` 截断。

## Part 1：打包与截断重构（Point 1）

### 1.1 记录显式选中集
- `src/nav/nav_types.py`：`NavState` 增加 `explicit_collect_ids: set[str]`。
- `src/nav/nav_navigate.py` `_apply_collect`（110-135）：每个 `_batch_actions` 的目标 `sid` 加入 `state.explicit_collect_ids`；`_fork_nav_state`/`_merge_nav_state` 同步该集合（与 `collect_confidence` 并列）。confidence 记录保留（供 tiebreak/preview）。

### 1.2 selection_count 计算
在 `src/nav/nav_compose.py` 增加 helper：
- `owner ∈ explicit_collect_ids` → +1；`owner` 有任一祖先 ∈ explicit_collect_ids → +1。
- 结果：只在被采父节点下的叶子=1（选中1次）；子叶被单独点名且父又被采=2（选中2次）；两者皆非=0（Tier3，当前为空，预留邻域补丁/MAP 自动入选）。

### 1.3 组内=文档顺序，组间=外部优先级
- `_build_groups`：`_ChildItem` 附加 `selection_count`、`unit`（仅 tiebreak/preview）、`line_key`。
- 组间排序由 `nav_compose.py:331` 的 `(-priority, -group_key, doc_order)` 改为 `(-priority, doc_order_key)`（去掉 unit 驱动的 `group_key`）。
- `build_compose_preview`（271 行）子节点排序由 `-score` 改为 `line_key`（文档序），`u=` 仅展示。

### 1.4 重写 `pack_nav_evidence`（317-409）
```
1) 按组(优先级序)、组内文档序，先"全量组装"所有 chunk（不截断）。
2) 若总渲染字符 ≤ budget_chars → 直接返回。
3) 否则分层截断（逐 chunk 移除，重算尺寸，永不整组按 rerank 删）：
   移除顺序 = key(selection_count 升, group_priority 升, line_key 降)
   即：先删 Tier3 → 再删 Tier2(选中1次) → 最后 Tier1(选中2次)；
   同层内优先删"外部排序靠后的组"里"文档靠后"的 chunk（剪尾）。
4) 组可因剪尾而清空并被丢弃（这是 chunk 级结果，非按组 rerank 删整组）。
5) 保留极端兜底：单块超预算时截断首块。
```
- `_child_final_score`/`compose_confidence_weight` 不再参与打包/截断排序；`w_conf` 降级为 Tier1 内可选 tiebreak（本期文档序优先，confidence 仅并列时用）。

## Part 2：大 section 软触发递归分派（Point 2）

### 2.1 全局 highlight 透传到子层
- `src/nav/nav_navigate.py:285`：`highlight_ids=state.highlight_ids if depth == 0 else None` → 各层都传 `state.highlight_ids`，使子区域 `must_keep` 也保护 3 通道命中（`nav_projection.py:443-445`）。

### 2.2 大 scope 投影转 title-only
- `src/nav/nav_projection.py` `build_map`（447-456）：`inline_summary` 由固定 `scope is not None` 改为：带 summary 估算 `_estimate_actionable_total(roots, with_summary=True)` 超过新阈值 `scope_inline_summary_char_limit` 时转 title-only（隐藏 summary、更紧凑，促使 AGENT 深入分派）；命中节点仍靠 `must_keep` 保留。是否深入仍由 AGENT 自主。

### 2.3 开启递归
- `config/nav_default.json`：`enable_recursive_dispatch: true`；新增 `scope_inline_summary_char_limit`（默认 2000，即用户"预算×乘数"启发式的参数化）。
- `src/nav/nav_types.py` `NavConfig`：新增 `scope_inline_summary_char_limit: int = 2000`。
- DISPATCH 门控已尊重 `max_dispatch_depth`（`nav_actions.py:57-60`），无需改。

## Part 3：48 题逐案归类与修复影响评估

基于真实 TRACE 的逐案判定（`gold_node_recall=0` 全集）。影响等级：**高**=机制直接对症、预期可救回；**中**=部分对症或需 AGENT 行为配合；**低**=间接受益；**无**=数据/标注问题，算法不修。

### 3.1 总览

| 根因类别 | 数量 | Part 1 影响 | Part 2 影响 | 备注 |
|---|---|---|---|---|
| ② 打包挤出（兄弟进了、gold 没进） | 11 | **高（11）** | 低（0-1） | Part 1 主战场 |
| ③ 大 section / 选错分支 / outline | 16 | 低-中（3-5） | **高-中（10-14）** | Part 2 主战场 |
| 导航欠采 | 1 | 无 | 中 | scope_0092 |
| 数据侧 gold 错标/错挂/重复标题 | 20 | **无** | **无** | Point 3 后续 |

**修复后预期（保守）**：
- Part 1 单独：48 中约 **8-11** 个可救回（② 全集，扣除 outline 未物化个案）
- Part 2 单独：48 中约 **6-12** 个可救回（③ 子集 + 欠采，依赖 AGENT 改选 DISPATCH）
- Part 1+2 叠加：约 **18-25** 个可救回；剩余 **20 数据侧 + 3-10 导航/残留**

---

### 3.2 Part 1 主修复：打包挤出（11 题）— 预期 **高**

机制：组内文档序 + selection_count 分层截断，gold 在父 section 内且文档靠前时优先保留。

| inspect_id | 题型 | Part1 | Part2 | 简要现象 |
|---|---|---|---|---|
| latest_clean_multi_0216 | multi_hop | **高** | 低 | 采了 2.3 父节，retrieved 有 2.3.6 等，丢 gold L63/L64（最前两条） |
| latest_clean_multi_0230 | multi_hop | **高** | 低 | 同上模式，区域兄弟进了、前位 gold 被 unit 挤出 |
| latest_clean_multi_0495 | multi_hop | **高** | 低 | 父节已采，gold 兄弟部分进 retrieved |
| latest_clean_multi_0641 | multi_hop | **高** | 低 | 父节已采，gold 有 heading 兄弟，前位 gold 被挤出 |
| latest_clean_niche_0114 | niche_fact | **高** | 低 | 采第四章，L60/L61 进了，gold L59（第十五条）夹在中间被丢 |
| latest_clean_niche_0460 | niche_fact | **高** | 低 | 7 兄弟中 6 个进了，gold 唯一未进 |
| latest_clean_niche_0473 | niche_fact | **高** | 低 | 同上，6/9 兄弟进了 |
| latest_clean_niche_0531 | niche_fact | **高** | 低 | 10/14 兄弟进了，gold 未进 |
| latest_clean_niche_0711 | niche_fact | **高** | 低 | 12/40 兄弟进了，gold 职责条目未进 |
| latest_clean_scope_0135 | scope_collection | **高** | 低 | 采「八、应急处置」，区域兄弟进了、gold 叶未进 |
| real_69cb12d0919452cda2225a0b_scope_collection_auto_0073 | scope_collection | **中** | 低 | 采父 L63，L64/L65 进了，gold L66 是最后一个 child，文档序保序可救但预算极紧时仍可能丢 |

**特殊：scope_0132**（原归 ②，实际更像 outline 未物化）
| latest_clean_scope_0132 | scope_collection | **低** | **中** | 采大 section「五、施工保证措施」，evidence 只有 outline 标题，深层 gold 叶 L278/L282-286 从未物化；Part 1 救不了（池里根本没有 gold chunk），需 Part 2 引导分派或后续修 outline 水合 |

---

### 3.3 Part 2 主修复：大 section / 选错分支 / 导航（17 题）

机制：大 scope title-only 投影 + 全局 highlight 透传 + 开启递归分派，引导 AGENT 深入而非整体 COLLECT 大节。

| inspect_id | 题型 | Part1 | Part2 | 简要现象 |
|---|---|---|---|---|
| latest_clean_multi_0180 | multi_hop | 低 | **中** | 到达 gold 区域但打包选了别的分支 |
| latest_clean_multi_0296 | multi_hop | 低 | **中** | 采了多节，gold 区域兄弟一个都没进 |
| latest_clean_multi_0372 | multi_hop | 低 | **中** | 有 1 次 DISPATCH，仍选错分支 |
| latest_clean_niche_0038 | niche_fact | 低 | **中** | 采了 19 个根，gold 区域未覆盖 |
| latest_clean_niche_0249 | niche_fact | 低 | **中** | 采第三章，evidence 从 3.2 开始，gold 3.1 总则被丢 |
| latest_clean_scope_0019 | scope_collection | 低 | **高** | 采多章节头，打包选第三/四章，第一章总则 gold 未进 |
| latest_clean_scope_0036 | scope_collection | 低 | **高** | 有 DISPATCH，仍选错分支 |
| latest_clean_scope_0040 | scope_collection | 低 | **高** | 列举整篇，采 5 章头但打包选第三/四章，第一章总则丢 |
| latest_clean_scope_0046 | scope_collection | 低 | **高** | 采 9 个节，gold 区域兄弟未进 |
| latest_clean_scope_0089 | scope_collection | 低 | **高** | 采了祖先 L2，打包选「复盘分析」高分节，背景 gold L4-L8 丢 |
| latest_clean_scope_0102 | scope_collection | 低 | **高** | 文档两处 Site Agent，打包选了 L834 另一处而非 gold L123 区 |
| latest_clean_scope_0116 | scope_collection | 低 | **高** | 采 10 个节，gold 在 L41 子树，打包选别处 |
| latest_clean_scope_0124 | scope_collection | 低 | **高** | 采文档根 L1，打包选「施工工艺」高分节，工程概况 gold 丢 |
| real_69c6ef484cca74801cb63bb9_multi_hop_auto_0006 | multi_hop | 低 | **中** | 采 12 个节，gold 区域未覆盖 |
| real_69c6ef4e4cca74801cb63bc6_scope_collection_auto_0061 | scope_collection | 低 | **高** | 采了祖先，gold 子树兄弟未进 |
| latest_clean_scope_0132 | scope_collection | 低 | **中** | outline 只给标题，深层叶未物化（见 3.2 特殊项） |
| latest_clean_scope_0092 | scope_collection | 无 | **中** | **导航欠采**：采了 H3 第一个子分支，漏第二个「②深化设计」gold |

Part 1 对部分 ③ 的间接收益：若 AGENT 仍整体 COLLECT 大节且 gold chunk 已在池内，文档序截断可能比分数排序多保留早位 gold（约 3-5 题，不确定，回归验证）。

---

### 3.4 数据侧（20 题）— Part 1/2 均 **无**，Point 3 后续

AGENT 实际导航到了 query 点名的 section，但 gold 标注指向别处。分三子类：

**A. 重复/近似标题（gold 指向另一份同名节）— 6 题**

| inspect_id | 题型 | 数据子类 | 说明 |
|---|---|---|---|
| latest_clean_multi_0572 | multi_hop | 重复标题 | query 附表6.6.1-1，agent 命中正确节点，gold 标另一份 |
| latest_clean_multi_0573 | multi_hop | 重复标题 | query 附表6.6.1-2，agent 采 L412（正确），gold 标 L556（另一份） |
| latest_clean_niche_0572 | niche_fact | 重复标题 | 同上 6.6.1-2 双份 |
| latest_clean_multi_0568 | multi_hop | 重复标题 | 附件5.2.2 vs 附表5.2.2 |
| latest_clean_niche_0306 | niche_fact | 重复标题 | 同上 5.2.2 双份 |
| latest_clean_scope_0124 | scope_collection | 重复标题(dup=2) | 文档名重复，agent 采根节但 gold 在另一语义分支（亦含 ③ 因素，数据复核优先） |

**B. gold 层级错挂（标到了错误父 section）— 8 题**

| inspect_id | 题型 | 数据子类 | 说明 |
|---|---|---|---|
| latest_clean_niche_0554 | niche_fact | 错挂 | query 6.7.3，agent 正确；gold L505 父是「附表1.1.1」非 6.7.3 |
| real_69c6ef4e4cca74801cb63bc6_scope_collection_auto_0062 | scope_collection | 错挂 | query 横向龙骨 5.2.5，agent 正确；gold 挂在 5.2.6 |
| real_69c6ef4e4cca74801cb63bc6_scope_collection_auto_0063 | scope_collection | 错挂 | query 摞底排砖 5.2.6，agent 正确；gold 挂在 5.2.7 铝板安装 |
| latest_clean_scope_0096 | scope_collection | 错挂 | L100-L103 父应是「如果出现变化或意外」，实际挂「教训记录单」 |
| latest_clean_scope_0097 | scope_collection | 错挂 | query 问不足L3，gold 挂在附件3-2 下非目标节 |
| latest_clean_scope_0101 | scope_collection | 错挂 | query Levels And Setting Out，gold 在 Materials/Workmanship |
| latest_clean_scope_0109 | scope_collection | 错挂 | 同上（另一文档副本） |
| latest_clean_scope_0129 | scope_collection | 错挂 | query 施工管理配备，gold 在「组织机构」子树深处，agent 采了同级节 |

**C. gold 标注与 query 语义无关（答非所问）— 6 题**

| inspect_id | 题型 | 数据子类 | 说明 |
|---|---|---|---|
| real_69c6ef4e4cca74801cb63bc6_scope_collection_auto_0064 | scope_collection | 错标 | query 验收标准编号，agent 完美采 7.1 标准清单；gold 全在 10.1 经济效益 |
| latest_clean_multi_0046 | multi_hop | 错标 | query 总则相邻证据，agent 采了第五/二章；gold 在第一章 L4/L5 |
| latest_clean_multi_0075 | multi_hop | 错标 | query 指向 docx 文件名节，gold 在第一章总则 |
| latest_clean_multi_0496 | multi_hop | 错标 | query 问 7.1 总则，agent 采了 7.5.2 等；gold 在 7.1 |
| real_69c6ef484cca74801cb63bb9_multi_hop_auto_0001 | multi_hop | 错标 | query 注浆结束条件，gold 是规范引用列表非操作条款 |
| real_69c6ef484cca74801cb63bb9_multi_hop_auto_0003 | multi_hop | 错标 | query 波美度/质量控制，gold 是工法应用节 L167 |
| latest_clean_scope_0053 | scope_collection | 错标 | query 建设工程买卖合同，gold 在合同条款深处，agent 采了别的合同节（31 步/14 DISPATCH 仍错） |

---

### 3.5 回归验证清单

修复后必须用 `bin/56_replay_map_nav_traces.py` 重跑以下 ID 文件（可从 `/tmp/zero48_ids.txt` 或上表汇总）：

```
# Part 1 重点验证（11+1）
latest_clean_multi_0216, latest_clean_multi_0230, latest_clean_multi_0495, latest_clean_multi_0641,
latest_clean_niche_0114, latest_clean_niche_0460, latest_clean_niche_0473, latest_clean_niche_0531, latest_clean_niche_0711,
latest_clean_scope_0135, real_69cb12d0919452cda2225a0b_scope_collection_auto_0073,
latest_clean_scope_0132  # 预期 Part1 无效，作负例

# Part 2 重点验证（16+1）
latest_clean_multi_0180, latest_clean_multi_0296, latest_clean_multi_0372,
latest_clean_niche_0038, latest_clean_niche_0249,
latest_clean_scope_0019, latest_clean_scope_0036, latest_clean_scope_0040, latest_clean_scope_0046,
latest_clean_scope_0089, latest_clean_scope_0102, latest_clean_scope_0116, latest_clean_scope_0124,
real_69c6ef484cca74801cb63bb9_multi_hop_auto_0006, real_69c6ef4e4cca74801cb63bc6_scope_collection_auto_0061,
latest_clean_scope_0132, latest_clean_scope_0092

# 数据侧负例（20，预期仍 0，确认不误伤）
# 见 3.4 全表
```

成功标准：
- Part 1 验证集：11 题中 ≥8 题 `gold_node_recall > 0`
- Part 2 验证集：17 题中 ≥6 题 `gold_node_recall > 0`（允许 AGENT 非确定性波动）
- 数据侧 20 题：仍 0（或仅因标注修正而变，非算法假阳性）

---

## Part 4：验证（实现后）
- `tests/test_nav_compose.py`：更新为文档序打包；新增 selection_count 分层截断用例（Tier2 先于 Tier1 被剪、gold 早位保序）。
- 回归：用 `bin/56_replay_map_nav_traces.py` 重跑 Part 3.5 清单 + 全量 48 + 对照集（268 或 400），比较 `gold_node_recall`。
- 已知残留：`_scope_collect_outline` 造成的"大 section 只拿 outline、深层叶未物化"——Part 2 间接缓解；若 scope_0132 仍失败，后续单独修 outline 水合。

## 不做
- 数据侧 20 个（3.4 全表）——归 Point 3 后续统一 gold 复核，不计入算法 KPI。