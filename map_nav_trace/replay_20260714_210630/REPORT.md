# Map-Nav 运行报告

- generated_at: `2026-07-14T21:06:30`
- env: EMBEDDING_MODEL=`text-embedding-v3` · NAV_MAP_MODE=`1` · enable_recursive_dispatch=`False` · map_char_limit=`5000` · max_steps=`8` · navigate_max_steps=`8`
- 汇总: 2 case · PASS 1/2 · mean gold_recall 0.250

| inspect_id | task_type | gold_recall | evidence_chars | steps |
|---|---|---:|---:|---:|
| latest_clean_multi_0010 | multi_hop | 0.50 | 500 | 4 |
| real_69c60974d4242eda8c47c615_scope_collection_auto_0030 | scope_collection | 0.00 | 500 | 7 |

---

## latest_clean_multi_0010  ·  multi_hop

- **Query:** 根据《线上学习平台学习管理方案（修订）》中“十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订）”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c6095ed4242eda8c47c5b2`
- **Gold nodes:** L2, L3

### 结果得分 — **PASS** (new gold_recall=0.50)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.50 |
| evidence_chars | 210 | 500 |
| n_retrieved_nodes | 2 | 12 |
| trajectory_steps | - | 4 |
| elapsed_sec | - | 1.4 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L2` | ❌ | False | False |
| `L3` | ✅ | True | False |

### 决策 TRACE(因果序)

- `D1` dispatch L1 (depth=0) · regions=[L1] · child_reports=1
  - reason: Dispatch main section to gather all relevant content for the query.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L1 (depth=1) · →L1 · +36
      - reason: rule_fallback_illegal_action
    - `F1` finish - (depth=1)
      - reason: Only one section collected; insufficient evidence to compare two adjacent points as requested.
- `F1` finish - (depth=0)
  - reason: Only one section collected; insufficient evidence to compare two adjacent points as requested.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L1` | - | 36 | 36 | - | ✅ |

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c6095ed4242eda8c47c5b2:L1 (ok)
collected 52 branch node(s); explicit roots=['real_69c6095ed4242eda8c47c5b2:L1']
collected: real_69c6095ed4242eda8c47c5b2:L1, real_69c6095ed4242eda8c47c5b2:L10, real_69c6095ed4242eda8c47c5b2:L11, real_69c6095ed4242eda8c47c5b2:L12, real_69c6095ed4242eda8c47c5b2:L13, real_69c6095ed4242eda8c47c5b2:L14, real_69c6095ed4242eda8c47c5b2:L15, real_69c6095ed4242eda8c47c5b2:L16, real_69c6095ed4242eda8c47c5b2:L17, real_69c6095ed4242eda8c47c5b2:L18, real_69c6095ed4242eda8c47c5b2:L19, real_69c6095ed4242eda8c47c5b2:L2, real_69c6095ed4242eda8c47c5b2:L20, real_69c6095ed4242eda8c47c5b2:L21, real_69c6095ed4242eda8c47c5b2:L22, real_69c6095ed4242eda8c47c5b2:L23, real_69c6095ed4242eda8c47c5b2:L24, real_69c6095ed4242eda8c47c5b2:L25, real_69c6095ed4242eda8c47c5b2:L26, real_69c6095ed4242eda8c47c5b2:L27
reason: Only one section collected; insufficient evidence to compare two adjacent points as requested.
---
=== End Investigate ===
```

### 最终 evidence(new)

**[E1]** [§ 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） / 三、考核管理及结果应用 / （ 二 ）学员学习考核管理 / 4.其他事项]
（ 3 ）十一在线平台中心后期将根据后台创建的线下培训记录，不定期抽查相关学习资料，保证学习的真实性和有效性。如发现有不实情形，获得该门线下培训学时的学员，学时为不合格，并给予相关人员通报。

**[E2]** [§ 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） / 一、管理机构及其职责 / （ 五）机关各部室及各二级单位]
2.督促本部室及本单位员工开展在线学习，并结合线上学习内容和业务实际，组织本部室及本单位开展线下探讨、分享、集中培训等。

**[E3]** [§ 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） / 二、课程及指派管理 / （ 一）课程类别]
明确课程名称、课程类别、必修岗位、课程开发负责人等信息（见附件），提交十一在线平台中心审批后按计划开发。

**[E4]** [§ 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） / 三、考核管理及结果应用 / （ 一）课程开发管理]
4.课

- retrieved_nodes: L1, L32, L38, L47, L50, L3⭐, L12, L14, L17, L18, L20, L33


---

## real_69c60974d4242eda8c47c615_scope_collection_auto_0030  ·  scope_collection

- **Query:** 列出重大事故隐患治理方案必须包含的所有内容要素。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L94, L95, L96, L97, L98, L99

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 500 |
| n_retrieved_nodes | 12 | 5 |
| trajectory_steps | - | 7 |
| elapsed_sec | - | 2.57 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L94` | ❌ | False | False |
| `L95` | ❌ | False | False |
| `L96` | ❌ | False | False |
| `L97` | ❌ | False | False |
| `L98` | ❌ | False | False |
| `L99` | ❌ | False | False |

### 决策 TRACE(因果序)

- `D11` dispatch L92 (depth=0) · regions=[L92] · child_reports=1
  - reason: Dispatch to collect the full list of elements required in a major accident hazard governance plan.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C2` collect L93 (depth=1) · multi→[L93, L94, L95, L96, L97, L98, L99] · +7
      - reason: Collect all listed elements of the major accident hazard governance plan.
    - `C1` collect L92 (depth=1) · →L92 · +11 · PURGED後代×7
      - reason: Collect section 2.4.4 which details the required elements of the major accident hazard governance plan.
    - `F1` finish - (depth=1)
      - reason: Collected sections L92 and L93 contain the required elements for major accident hazard governance plans.
- `C10` collect L82 (depth=0) · →L82 · +1
  - reason: Collect definition of major accident hazards to ensure completeness of governance plan elements.
- `C10` collect L84 (depth=0) · →L84 · +1
  - reason: Collect definition of major accident hazards to ensure governance plan elements are complete.
- `F1` finish - (depth=0)
  - reason: Collected evidence from L92 and L93 contains the required elements for major accident hazard governance plans.

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
对重大事故隐患，由被检查项目负责整改，整改应制定事故隐患治理方案，该方案由项目经理组织制定和实施。方案包括以下内容：

**[E2]** 2、重大事故隐患，是指危害和整改难度较大，应当全部或者局部停产停业，并经过一定时间整改治理方能排除的隐患，或者因外部因素影响致使生产经营单位自身难以排除的隐患。

**[E3]** [§ 2.4.4 重大事故隐患整改、复查、销项]
2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。

**[E4]** [§ 2.4.4 重大事故隐患整改、复查、销项]
2.4.6 各项目部应当加强对自然灾害的预防。对于因自然灾害可能导致事故灾难的隐患，应当按照有关法律、法规、标准和本制度的要求排查治理，采取可靠的预防措施，制定应急预案。在接到有关自然灾害预报时，应当及时向有关人员发出预警通

- retrieved_nodes: L92, L93, L84, L102, L103


---

