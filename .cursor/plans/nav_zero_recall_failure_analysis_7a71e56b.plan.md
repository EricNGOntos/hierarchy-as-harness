---
name: Nav 外部相对重排（compose 预览 + group_priority 打包）
overview: 提示词动态裁剪 D* 已完成（depth>0 零非法 D*、零 fallback，回归稳定），失败瓶颈已转移到 COMPOSE 打包 + 子 agent 自报 confidence 通胀。本方案是代码级实现：抽出 compose 预览喂给外部总体 agent，让其在 FINISH 时对「父-子分组」做序数相对重排（G* 排名，非 0-1 打分），写入 NavState.group_priority，驱动 pack_nav_evidence 组序，从形式上消除通胀。子 agent 内部 confidence 退化为可选先验，判别权收敛到外部一次同屏比较。
todos:
  - id: prompt-dispatch-aware
    content: 提示词按 dispatch_available 动态裁剪 D*（已落地并验证 depth>0 零非法 D*/零 fallback）
    status: completed
  - id: verify-replay
    content: 复跑 5 题 + 回归 scope_0030/multi_0032/0048（已完成，隔离出剩余为打包侧+数据侧）
    status: completed
  - id: p2-types
    content: NavState 加 group_priority；NavConfig 加 enable_external_rerank / compose_preview_snippet_chars / compose_preview_max_children；_fork/_merge 处理 group_priority
    status: completed
  - id: p2-preview
    content: nav_compose.build_compose_preview()——复用 _build_groups 输出 [G*] 分组视图（父标题 + 每子节点 owner/首行摘要/字数/unit_score），返回文本 + G*→parent_id 映射
    status: completed
  - id: p2-inject-observation
    content: navigate() 在 depth==0 观测里用 build_compose_preview 替换/增强 reports_context；G* 映射随 state 传给 policy
    status: completed
  - id: p2-parse-rerank
    content: choose_llm_action 解析 FINISH（及可选其它动作）里的 group_rank=[G3,G1,...]，经 G*→parent_id 映射写入 state.group_priority
    status: completed
  - id: p2-prompt-rerank
    content: _system_prompt 加规则——depth==0 且有 compose 预览时，FINISH 须给 group_rank（按能否回答 query 的相对顺序排 G*）；scope_collection 保守充分性提问
    status: completed
  - id: p2-pack-consume
    content: _ParentGroup 加 priority；pack_nav_evidence 组序改为 (-priority, -group_key, doc_order_key)，priority 来自 state.group_priority
    status: completed
  - id: p2-verify
    content: 复跑 scope_0076（目标 recall≥0.6）+ 回归三题不退化 + 抽查 scope_collection
    status: pending
  - id: p1-fallback
    content: 备选轻量（若 P2 暂缓）——批内 conf 衰减 + scope_collection 跨组配额/引言限长；纯打包内解决
    status: pending
  - id: data-side
    content: niche_0068 / scope_0101 / multi_0006 归档数据侧，不在算法侧修
    status: pending
isProject: false
---

# Nav 外部相对重排：compose 预览 + group_priority 打包（代码级）

## 0. 已完成（不再展开）
- **提示词动态裁剪 D***：`nav_policy._system_prompt(*, depth, dispatch_available)` 已按合法动作真源裁剪；depth>0 关闭递归时零非法 D*、零 `rule_fallback`。回归 `scope_0030=1.00 / multi_0032=0.50 / multi_0048=1.00`（`map_nav_trace/replay_20260715_150803/`）。
- **失败定位（结论）**：剩余仍为 0 的题里，`scope_0076`/`multi_0010` 是**打包侧**（gold 已进池，被高分「引言/定义」组独占 500 字预算饿死 + 子 agent 自报 conf 全 0.9 通胀失效）；`niche_0068`/`scope_0101`/`multi_0006` 是**数据/任务侧**（见 §6）。

## 1. 现状机制（实现依据，已核对代码）
- 结束由**外部总体 agent** 决定：子 agent = `navigate(depth>0)` 独立循环；`dispatch()` merge 回根后根续跑、再观测、自己选 FINISH（`nav_navigate.py:345`）。
- 子 agent 证据**直接 merge 进共享单池**：`_merge_nav_state`（`nav_navigate.py:57`）并入 `collected` / `collect_confidence` / `collected_section_ids`。
- 根看到的 `reports_context` **内容盲**：`_format_region_reports`（`nav_navigate.py:139`）只给 `[region i] scope (ok)` + `collected:<前20 sid>` + `reason`。
- 打包**末尾一次性**：`run_nav_episode` → `pack_nav_evidence(_dedupe_scored(state.collected), ...)`（`nav_agent.py:591`）；组序 `(-group_key, doc_order_key)`（`nav_compose.py:263`）。
- **通胀根因**：N 个子 agent 各自「绝对打分」→ 人人 0.9。修法是把判别改成**一次同屏序数比较**（排名/Top-K），而非搬运 0-1 分。

## 2. 目标数据流（改造后）
```
depth0 navigate:
  observe → 若已有收集池: 观测里附 compose 预览([G1]..[Gk] + 每子节点摘要/unit_score)
  act:
    COLLECT / DISPATCH …（照旧）
    FINISH → JSON 带 group_rank=["G3","G1","G2",...]（相对顺序）
             → 解析 G*→parent_id → state.group_priority[parent_id]=派生分
run_nav_episode:
  pack_nav_evidence: 组序 = (-group_priority, -group_key, doc_order_key)
                     → 被排前的 gold 组先渲染、先拿预算
```

## 3. 代码级改动清单

### 3.1 类型与配置（`src/nav/nav_types.py`）
`NavState`（`nav_types.py:155`）新增：
```python
# 外部 agent 对「最近父分组」的相对优先级：parent_id -> priority(越大越先打包)。空=未重排。
group_priority: Dict[str, float] = field(default_factory=dict)
```
`NavConfig`（`nav_types.py:28`）新增：
```python
enable_external_rerank: bool = True          # depth0 compose 预览 + group_rank
compose_preview_snippet_chars: int = 60      # 预览里每个子节点摘要字数
compose_preview_max_children: int = 6        # 每组预览展示的子节点上限
```
（`from_dict` 的 `allowed` 白名单自动覆盖新字段，无需改解析。）

### 3.2 fork/merge 传播（`src/nav/nav_navigate.py`）
- `_fork_nav_state`（`nav_navigate.py:33`）：加 `group_priority=dict(state.group_priority)`。
- `_merge_nav_state`（`nav_navigate.py:57`）：加 `parent.group_priority.update(child.group_priority)`（子 agent 一般不产出，防御性即可）。

### 3.3 compose 预览（`src/nav/nav_compose.py` 新增）
```python
def build_compose_preview(
    collected: Sequence[Tuple[Chunk, float]],
    ts: ToolSpace,
    state: NavState,
    config: NavConfig,
) -> Tuple[str, Dict[str, str]]:
    """把当前收集池组装成 [G*] 分组预览。返回 (文本, {G_id: parent_id})。

    复用 _build_groups(collected, ts, state, config) 得到 List[_ParentGroup]；
    组序沿用 (-group_key, doc_order_key)（此处仅用于给 LLM 稳定编号）。
    每组一行组头 + 至多 compose_preview_max_children 个子节点行：
      [G1] §<parent_title>
        - <owner Lxx> u=<unit_score:.3f> | <body 首行前 snippet_chars 字>… (<chars>字)
    """
```
要点：
- 子行摘要用 `_chunk_body(chunk)` 首行截断到 `compose_preview_snippet_chars`；带 `unit_score`（`unit_score_for_evidence_chunk`）与字数，**不给全文**（控根上下文成本）。
- 返回 `g_map`（`{"G1": parent_id, ...}`）供解析 `group_rank` 用。

### 3.4 注入观测（`src/nav/nav_navigate.py` 的 `navigate`）
- 在 depth==0 的观测构建处（`build_projection` 之后、`choose_llm_action` 之前，约 `nav_navigate.py:309-325`）：
```python
g_map: Dict[str, str] = {}
if depth == 0 and config.enable_external_rerank and state.collected:
    preview, g_map = build_compose_preview(
        _dedupe_scored(list(state.collected)), ts, state, config
    )
    state.reports_context = (
        (state.reports_context + "\n" if state.reports_context else "")
        + "=== Assembled Evidence (rank these on FINISH) ===\n"
        + preview
        + "\n=== End Assembled Evidence ==="
    )
```
- `g_map` 通过 `choose_llm_action(..., group_map=g_map)` 传入（新增关键字参数，默认 `None`）。
- `_dedupe_scored` 目前在 `nav_agent`；为避免环，把它下沉到 `nav_compose`（与 `pack_nav_evidence` 同域），`nav_agent` 改为 re-export。

### 3.5 解析 group_rank（`src/nav/nav_policy.py` 的 `choose_llm_action`）
- 签名加 `group_map: Optional[Dict[str, str]] = None`。
- 在 FINISH 命中分支（`primary.kind == FINISH`，即返回 `primary, meta` 前）解析：
```python
if primary.kind == ActionKind.FINISH and group_map:
    rank = obj.get("group_rank") or obj.get("groups") or []
    if isinstance(rank, list) and rank:
        n = len(rank)
        for i, g in enumerate(rank):
            pid = group_map.get(str(g).strip().upper())
            if pid:
                state.group_priority[pid] = float(n - i)  # 越靠前分越高
        meta["group_rank"] = [str(g).strip().upper() for g in rank]
```
（写 `state.group_priority` 直接生效于末尾打包；FINISH 不影响 legal actions，无需改 `build_legal_actions`。）

### 3.6 提示词（`src/nav/nav_policy.py` 的 `_system_prompt`）
- 新增参数 `has_preview: bool = False`（由 `choose_llm_action` 依 `group_map` 传入）。
- `has_preview` 为真时，在 Rules 追加：
  - `When "Assembled Evidence" is shown, your FINISH MUST include "group_rank": an ordered list of the [G*] ids, most-relevant-to-the-query first.`
  - scope_collection 保守充分性：`For list/coverage queries, FINISH only if the assembled groups already contain ALL required items; otherwise COLLECT the missing ones first.`
- FINISH 示例补：`{"action_id":"F1","group_rank":["G2","G1","G3"],"reason":"..."}`。

### 3.7 打包消费（`src/nav/nav_compose.py`）
- `_ParentGroup`（`nav_compose.py:157`）加字段 `priority: float = 0.0`。
- `_build_groups`（`nav_compose.py:176`）建组后回填：`groups[parent_id].priority = float((state.group_priority or {}).get(parent_id, 0.0))`。
- `pack_nav_evidence` 组序（`nav_compose.py:263`）：
```python
groups.sort(key=lambda g: (-g.priority, -g.group_key, g.doc_order_key))
```
  即：有外部排名的组按排名优先；无排名回退旧的子最终分 max + 文档序。组内排序不变（`(-score, line_key)`）。

### 3.8 子 agent 内部 confidence（P2-4，评估后）
- 现状 `_apply_collect`（`nav_navigate.py:114-115`）写 `state.collect_confidence[sid]`；保留为**先验/tie-break**即可，不再是主判别。
- `_child_final_score`（`nav_compose.py:119`）维持 `own_unit + w_conf·conf`；组间排序已由 `priority` 主导，通胀不再致命。
- 可选清理：把 `compose_confidence_weight` 调小（如 0.05）或将子 agent 提示词的 confidence 要求降级为可选。**本轮先不删 confidence，先上 priority 主导**，验证后再决定是否移除。

## 4. 为何能修好 scope_0076（反事实）
- 预览里根会同屏看到「引言组 G_A（L124/125/127/128，高 unit）」与「要点列表组 G_B（含 gold L141-148，低 unit）」。
- query 是「列出所有事项要点」→ 根 FINISH 给 `group_rank=["G_B","G_A",...]`。
- 打包 `-priority` 使 G_B 先渲染 → gold 组先拿 500 字预算 → recall 0 → ≥0.6。
- multi_0010 同理（前提 L2/L3 成组可见）；niche_0068 无正文仍不可救（数据侧）。

## 5. 备选轻量 P1（若 P2 暂缓，纯打包内解决）
- **P1-D 批内 conf 衰减**：`_apply_collect` 里同一次 multi-collect 选择数 `>k`（k=3）时该批 `collect_confidence` 乘衰减，精挑单选才满权重。
- **P1-E scope_collection 跨组配额**：`pack_nav_evidence` 按 `state.task_type` 分支，各组按 `doc_order_key` 轮转分预算 + 引言超长块限长/降权。
- 关系：P2 为主线；P1-E 单点即可先救 scope_0076，可作过渡。

## 6. 数据侧（归档，不改算法）
- `niche_0068`：gold=`L2` 标题节点、`_chunk_body` 空、无可命中正文。
- `scope_0101`：gold 段标题错译「…水」，agent 判定不在 scope、从未进 gold 枝。
- `multi_0006`：多跳需从「应符合表7.2.1」引用跳到表体 L159+，agent 命中引用句未解析跳转。

## 7. 已放弃（提示词根治后无需）
- ~~P0-A 非法动作打捞 / P0-B D*→C* 降级 / P1-C fallback 兜底 conf~~：非法 D* 已归零、fallback 不触发。换模型/放开递归再现时再回收 P0-A 作保险。

## 8. 验证口径
- 复跑：`PYTHONPATH=src/nav:src/realdata python bin/56_replay_map_nav_traces.py <ids>`。
- LLM cache 按完整 messages 哈希；提示词/观测变了会自动 miss、走真实调用（新 group_rank 生效）。
- 目标：`scope_0076` recall≥0.6；`scope_0030/multi_0032/0048` 不退化；抽查若干 scope_collection 无新回退。
