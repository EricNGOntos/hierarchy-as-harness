# Map-Nav 运行报告

- generated_at: `2026-07-15T12:24:25`
- env: EMBEDDING_MODEL=`text-embedding-v3` · NAV_MAP_MODE=`1` · enable_recursive_dispatch=`False` · map_char_limit=`5000` · max_steps=`8` · navigate_max_steps=`8`
- 汇总: 1 case · PASS 1/1 · mean gold_recall 1.000

| inspect_id | task_type | gold_recall | evidence_chars | steps |
|---|---|---:|---:|---:|
| real_69c60974d4242eda8c47c615_scope_collection_auto_0030 | scope_collection | 1.00 | 460 | 7 |

---

## real_69c60974d4242eda8c47c615_scope_collection_auto_0030  ·  scope_collection

- **Query:** 列出重大事故隐患治理方案必须包含的所有内容要素。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L94, L95, L96, L97, L98, L99

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 460 |
| n_retrieved_nodes | 12 | 11 |
| trajectory_steps | - | 7 |
| elapsed_sec | - | 11.25 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L94` | ✅ | True | False |
| `L95` | ✅ | True | False |
| `L96` | ✅ | True | False |
| `L97` | ✅ | True | False |
| `L98` | ✅ | True | False |
| `L99` | ✅ | True | False |

### 决策 TRACE(因果序)

- `D11` dispatch L92 (depth=0) · regions=[L92] · child_reports=1
  - reason: Dispatch to subagent to collect all elements of major accident hazard governance plan from section 2.4.4.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C2` collect L93 (depth=1) · multi→[L93, L94, L95, L96, L97, L98, L99] · +7
      - reason: Collect the specific 6 elements of the major accident hazard governance plan as listed in the document.
    - `C1` collect L92 (depth=1) · →L92 · +11 · PURGED後代×7
      - reason: Section 2.4.4 explicitly lists the required content elements for the major accident hazard governance plan.
    - `F1` finish - (depth=1)
      - reason: Collected sections L92 and L93 contain the required elements for major accident hazard governance plans.
- `C10` collect L82 (depth=0) · →L82 · +1
  - reason: Collect definition of major accident hazards to ensure governance plan elements are identified.
- `C10` collect L84 (depth=0) · →L84 · +1
  - reason: Collects the definition of major accident hazards, a key element for governance plans.
- `F1` finish - (depth=0)
  - reason: Collected evidence from L92 and L93 contains all required elements for major accident hazard governance plans.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C2` | `L93` | L93, L94, L95, L96, L97, L98, L99 | 7 | 7 | - | ✅ |
| 2 | `C1` | `L92` | - | 11 | 11 | 7 | ✅ |
| 5 | `C10` | `L82` | - | 1 | 1 | - | ✅ |
| 6 | `C10` | `L84` | - | 1 | 1 | - | ✅ |

**水合告警:**
- step 1 整枝水合含 1 个非 gold 叶 (与 gold 争抢 evidence 预算)。
- step 2 `C1` 收父节点 `L92` 时 **purge 掉 7 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60974d4242eda8c47c615:L92 (ok)
collected 12 branch node(s); explicit roots=['real_69c60974d4242eda8c47c615:L93', 'real_69c60974d4242eda8c47c615:L92']
collected: real_69c60974d4242eda8c47c615:L100, real_69c60974d4242eda8c47c615:L101, real_69c60974d4242eda8c47c615:L102, real_69c60974d4242eda8c47c615:L103, real_69c60974d4242eda8c47c615:L92, real_69c60974d4242eda8c47c615:L93, real_69c60974d4242eda8c47c615:L94, real_69c60974d4242eda8c47c615:L95, real_69c60974d4242eda8c47c615:L96, real_69c60974d4242eda8c47c615:L97, real_69c60974d4242eda8c47c615:L98, real_69c60974d4242eda8c47c615:L99
reason: Collected sections L92 and L93 contain the required elements for major accident hazard governance plans.
---
=== End Investigate ===
```

### 最终 evidence(new)

**[E1]** [§ 2.4.4 重大事故隐患整改、复查、销项]
  2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。
  对重大事故隐患，由被检查项目负责整改，整改应制定事故隐患治理方案，该方案由项目经理组织制定和实施。方案包括以下内容：
  1、治理的目标和任务；
  2、采取的方法和措施；
  3、经费和物资的落实；
  4、负责治理的机构和人员；
  5、治理的时限和要求；
  6、安全措施和应急预案。

**[E2]** [§ 2.4 隐患整改]
  2.4.1 事故隐患分为一般事故隐患和重大事故隐患。
  2、重大事故隐患，是指危害和整改难度较大，应当全部或者局部停产停业，并经过一定时间整改治理方能排除的隐患，或者因外部因素影响致使生产经营单位自身难以排除的隐患。

- retrieved_nodes: L92, L102, L93, L94⭐, L95⭐, L96⭐, L97⭐, L98⭐, L99⭐, L82, L84


---

