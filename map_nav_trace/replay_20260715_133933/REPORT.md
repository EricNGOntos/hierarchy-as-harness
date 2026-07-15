# Map-Nav 运行报告

- generated_at: `2026-07-15T13:39:33`
- env: EMBEDDING_MODEL=`text-embedding-v3` · NAV_MAP_MODE=`1` · enable_recursive_dispatch=`False` · map_char_limit=`5000` · max_steps=`8` · navigate_max_steps=`8`
- 汇总: 12 case · PASS 7/12 · mean gold_recall 0.528

| inspect_id | task_type | gold_recall | evidence_chars | steps |
|---|---|---:|---:|---:|
| real_69c60974d4242eda8c47c615_scope_collection_auto_0030 | scope_collection | 1.00 | 460 | 7 |
| real_69cb12d0919452cda2225a0b_scope_collection_auto_0076 | scope_collection | 0.00 | 401 | 4 |
| latest_clean_scope_0101 | scope_collection | 0.00 | 158 | 11 |
| latest_clean_scope_0116 | scope_collection | 0.83 | 479 | 52 |
| latest_clean_scope_0119 | scope_collection | 0.50 | 498 | 13 |
| real_69c6ef484cca74801cb63bb9_multi_hop_auto_0006 | multi_hop | 0.00 | 497 | 9 |
| latest_clean_multi_0010 | multi_hop | 0.00 | 476 | 4 |
| latest_clean_multi_0032 | multi_hop | 1.00 | 477 | 8 |
| latest_clean_multi_0048 | multi_hop | 1.00 | 466 | 6 |
| latest_clean_niche_0023 | niche_fact | 1.00 | 483 | 6 |
| latest_clean_niche_0043 | niche_fact | 1.00 | 464 | 8 |
| latest_clean_niche_0068 | niche_fact | 0.00 | 492 | 24 |

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
| elapsed_sec | - | 2.1 |

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

## real_69cb12d0919452cda2225a0b_scope_collection_auto_0076  ·  scope_collection

- **Query:** 列出办理《跨区域涉税事项备案》时需注意的所有事项要点。
- **Doc:** `real_69cb12d0919452cda2225a0b`
- **Gold nodes:** L141, L142, L143, L144, L145, L146, L147, L148

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 401 |
| n_retrieved_nodes | 6 | 4 |
| trajectory_steps | - | 4 |
| elapsed_sec | - | 79.84 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L141` | ❌ | False | False |
| `L142` | ❌ | False | False |
| `L143` | ❌ | False | False |
| `L144` | ❌ | False | False |
| `L145` | ❌ | False | False |
| `L146` | ❌ | False | False |
| `L147` | ❌ | False | False |
| `L148` | ❌ | False | False |

### 决策 TRACE(因果序)

- `D2` dispatch L124 (depth=0) · regions=[L124] · child_reports=1
  - reason: Dispatch section 3.2.4 to collect all details on cross-regional tax filing requirements and precautions.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L124 (depth=1) · →L124 · +33
      - reason: rule_fallback_illegal_action
    - `F1` finish - (depth=1)
      - reason: Collected section L124 contains the required points for cross-regional tax filing. Ready to finish.
- `F1` finish - (depth=0)
  - reason: Collected section L124 contains the required points for cross-regional tax filing.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L124` | - | 33 | 33 | - | ✅ |

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69cb12d0919452cda2225a0b:L124 (ok)
collected 34 branch node(s); explicit roots=['real_69cb12d0919452cda2225a0b:L124']
collected: real_69cb12d0919452cda2225a0b:L124, real_69cb12d0919452cda2225a0b:L125, real_69cb12d0919452cda2225a0b:L126, real_69cb12d0919452cda2225a0b:L127, real_69cb12d0919452cda2225a0b:L128, real_69cb12d0919452cda2225a0b:L129, real_69cb12d0919452cda2225a0b:L130, real_69cb12d0919452cda2225a0b:L131, real_69cb12d0919452cda2225a0b:L132, real_69cb12d0919452cda2225a0b:L133, real_69cb12d0919452cda2225a0b:L134, real_69cb12d0919452cda2225a0b:L135, real_69cb12d0919452cda2225a0b:L136, real_69cb12d0919452cda2225a0b:L137, real_69cb12d0919452cda2225a0b:L138, real_69cb12d0919452cda2225a0b:L139, real_69cb12d0919452cda2225a0b:L140, real_69cb12d0919452cda2225a0b:L141, real_69cb12d0919452cda2225a0b:L142, real_69cb12d0919452cda2225a0b:L143
reason: Collected section L124 contains the required points for cross-regional tax filing. Ready to finish.
---
=== End Investigate ===
```

### 最终 evidence(new)

**[E1]** [§ **3.2.4** 《跨区域涉税事项报告》管理]
  根据《中华人民共和国税收征收管理法实施细则》第二十一条规定：从事生产、经 营的纳税人到外县（市）临时从事生产、经营活动的，应当持税务登记证副本和所在地 税务机关填开的外出经营活动税收管理证明，向营业地税务机关报验登记，接受税务管 理。集团公司注册地址为咸阳市，除在注册地市所辖范围以内区域（渭城区、秦都区） 承接的工程项目不需办理《跨区域涉税事项备案表》，在其他地区承接的工程项目均需 办理《跨区域涉税事项备案表》，并在项目所在地预缴税款。
  《跨区域涉税事项报告》的办理由项目部财务人员发起申请，将所需办理备案项目 的合同扫描件或原件提供至税务业务岗，由税务业务岗在国家税务总局陕西省电子税务 局上进行办理，严格按照合同内容，提交办理《跨区域涉税事项报告》，办理时限不得 超过两个工作日。
  办理跨区域涉税事项备案需注意事项：

- retrieved_nodes: L124, L125, L127, L128


---

## latest_clean_scope_0101  ·  scope_collection

- **Query:** 列举《马来西亚合同样本 2006 版 翻译件- Malaysia-PAM-合同翻译稿（4.23二译）》中“Levels And Setting Out Of The Works水”部分的主要条目。
- **Doc:** `real_69c60aeed4242eda8c47c925`
- **Gold nodes:** L114, L115, L116, L117, L118, L119

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 158 |
| n_retrieved_nodes | 19 | 3 |
| trajectory_steps | - | 11 |
| elapsed_sec | - | 339.68 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L114` | ❌ | False | False |
| `L115` | ❌ | False | False |
| `L116` | ❌ | False | False |
| `L117` | ❌ | False | False |
| `L118` | ❌ | False | False |
| `L119` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C4` collect L110 (depth=0) · →L110 · +1
  - reason: Collect the 'Levels And Setting Out Of The Works' section to retrieve its main items.
- `C10` collect L751 (depth=0) · →L751 · +1
  - reason: Collect the specific leaf node 'Levels And Setting Out Of The Works' to retrieve its main items.
- `D1` dispatch L35 (depth=0) · regions=[L35] · child_reports=1
  - reason: Dispatch N1 to locate 'Levels And Setting Out Of The Works' section.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `F1` finish - (depth=1)
      - reason: The current scope does not contain the 'Levels And Setting Out Of The Works' section. No relevant evidence collected.
- `D1` dispatch L35 (depth=0) · regions=[L35] · child_reports=1
  - reason: Dispatch to find 'Levels And Setting Out Of The Works' section.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `F1` finish - (depth=1)
      - reason: The current scope does not contain the 'Levels And Setting Out Of The Works' section. No relevant evidence collected.
- `D1` dispatch L35 (depth=0) · regions=[L35] · child_reports=1
  - reason: Dispatch to find 'Levels And Setting Out Of The Works' section.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `F1` finish - (depth=1)
      - reason: The current scope does not contain the 'Levels And Setting Out Of The Works' section. No relevant evidence collected.
- `D1` dispatch L35 (depth=0) · regions=[L35] · child_reports=1
  - reason: Dispatch to find 'Levels And Setting Out Of The Works' section as previous attempts failed.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `F1` finish - (depth=1)
      - reason: The current scope does not contain the 'Levels And Setting Out Of The Works' section. No relevant evidence collected.
- `F1` finish - (depth=0)
  - reason: The 'Levels And Setting Out Of The Works' section was not found in the document after investigation. No further collection possible.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C4` | `L110` | - | 1 | 1 | - | ✅ |
| 2 | `C10` | `L751` | - | 1 | 1 | - | ✅ |

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60aeed4242eda8c47c925:L35 (ok)
The current scope does not contain the 'Levels And Setting Out Of The Works' section. No relevant evidence collected.
reason: The current scope does not contain the 'Levels And Setting Out Of The Works' section. No relevant evidence collected.
---
=== End Investigate ===
```

### 最终 evidence(new)

**[E1]** [§ 3.0	Contract  Documents,Programme  And]
Levels And Setting Out Of The Works--工程的测量与放样

**[E2]** [§ Levels And Setting Out Of The Works水平和设置]
Setting out设置

- retrieved_nodes: L751, L110, L111


---

## latest_clean_scope_0116  ·  scope_collection

- **Query:** 列举《1.临时用电施工组织设计范本》中“1.临时用电施工组织设计范本.docx”部分的主要条目。
- **Doc:** `real_69c60aeed4242eda8c47c928`
- **Gold nodes:** L42, L43, L47, L48, L49, L50

### 结果得分 — **PASS** (new gold_recall=0.83)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.83 |
| evidence_chars | 500 | 479 |
| n_retrieved_nodes | 26 | 16 |
| trajectory_steps | - | 52 |
| elapsed_sec | - | 43.22 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L42` | ✅ | True | False |
| `L43` | ✅ | True | False |
| `L47` | ✅ | True | False |
| `L48` | ✅ | True | False |
| `L49` | ✅ | True | False |
| `L50` | ❌ | False | False |

### 决策 TRACE(因果序)

- `D1` dispatch L1 (depth=0) · regions=[L1, L2, L11, L12, L16, L18, L21, L22, L24, L26, L27, L39, L40, L41, L75, L76, L90, L97, L99, L102, L109, L112, L114, L115, L118, L129] · child_reports=26
  - reason: Dispatch all major sections to gather the complete list of main entries in the temporary power organization design template.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L12 (depth=1) · →L12 · +3
      - reason: Collect the entire '临电组织机构图' section to capture its main entries and structure.
    - `F1` finish - (depth=1)
      - reason: The target section has been collected. No further actions needed to list the main entries.
    - `C1` collect L1 (depth=1) · →L1 · +7
      - reason: Collect the main section to retrieve all primary entries of the temporary power organization design template.
    - `F1` finish - (depth=1)
      - reason: The document root has been collected, containing the main structure of the temporary power organization design template. No further collection is needed.
    - `C1` collect L2 (depth=1) · →L2 · +1
      - reason: Collect section N1 to retrieve the main entries of the temporary power organization design template.
    - `F1` finish - (depth=1)
      - reason: The required section has been collected. No further actions needed to list the main entries.
    - `C1` collect L11 (depth=1) · multi→[L11, L12, L13, L14, L15, L16, L17] · +10
      - reason: Collecting all sections under '现场用电管理组织机构' to list main entries as requested.
    - `F1` finish - (depth=1)
      - reason: The target document section has been collected. No further actions needed to list its main entries.
    - `C1` collect L16 (depth=1) · →L16 · +1
      - reason: Collect the main section to retrieve all listed items including the table.
    - `F1` finish - (depth=1)
      - reason: The target section has been collected. No further actions needed to list its main entries.
    - `F1` finish - (depth=1)
      - reason: No actionable sections or content available to collect for the requested document part.
    - `C1` collect L24 (depth=1) · →L24 · +1
      - reason: Collect the main section containing the temporary power distribution table entries.
    - `F1` finish - (depth=1)
      - reason: Collected the target document section containing the required outline. Ready to finish.
    - `C1` collect L21 (depth=1) · →L21 · +3
      - reason: Collect the main section '用电容量统计' to retrieve its primary entries as requested.
    - `F1` finish - (depth=1)
      - reason: The target section has been collected. No further actions needed to list its main entries.
    - `C1` collect L22 (depth=1) · →L22 · +1
      - reason: Collecting the main section to retrieve all primary entries of the template.
    - `F1` finish - (depth=1)
      - reason: Collected the target section containing the main items of the temporary power organization design template.
    - `C1` collect L26 (depth=1) · →L26 · +3
      - reason: Collect the main section '负荷计算' to capture all its sub-items and content for the user's query.
    - `F1` finish - (depth=1)
      - reason: The target document section has been collected. No further actions needed to list its main entries.
    - `F1` finish - (depth=1)
      - reason: No actionable sections or content available to collect for the requested document part.
    - `C1` collect L41 (depth=1) · →L41 · +10
      - reason: Collect the main section to gather all relevant items for the query.
    - `F1` finish - (depth=1)
      - reason: The target document section has been collected. No further actions needed to list its main entries.
    - `C1` collect L40 (depth=1) · →L40 · +4
      - reason: Collect the main section '变压器损耗计算' to capture all listed items and their details.
    - `F1` finish - (depth=1)
      - reason: The required section has been collected. No further actions needed to list the main entries.
    - `C1` collect L75 (depth=1) · →L75 · +5
      - reason: Collect the main section covering distribution system design, grounding, lightning protection, and materials to list all major entries.
    - `F1` finish - (depth=1)
      - reason: Collected the target document section containing the required outline. Ready to finish.
    - `C1` collect L39 (depth=1) · →L39 · +8
      - reason: rule_fallback_illegal_action
    - `F1` finish - (depth=1)
      - reason: The target document section has been collected. No further actions needed to list its main entries.
    - `F1` finish - (depth=1)
      - reason: No actionable sections or content found in the current scope to collect.
    - `C1` collect L99 (depth=1) · →L99 · +3
      - reason: Collecting the parent section to capture all relevant条目 for the temporary power organization design template.
    - `F1` finish - (depth=1)
      - reason: The target document section has been collected. No further actions needed to list its main entries.
    - `C1` collect L90 (depth=1) · →L90 · +8
      - reason: Collecting the main '防护措施' section to retrieve all listed sub-entries as requested.
    - `F1` finish - (depth=1)
      - reason: The document root has been collected, containing the main structure of the temporary power construction organization design template. No further collection is needed.
    - `C1` collect L97 (depth=1) · →L97 · +1
      - reason: Collecting the main section to identify all primary entries in the temporary power organization design template.
    - `F1` finish - (depth=1)
      - reason: The target document section has been collected. No further actions needed to list its main entries.
    - `C1` collect L102 (depth=1) · →L102 · +3
      - reason: Collecting the '电缆防护' section to gather its main entries as requested.
    - `F1` finish - (depth=1)
      - reason: The target document section has been collected. No further actions needed to list its main entries.
    - `C1` collect L112 (depth=1) · →L112 · +1
      - reason: Collect section N1 to retrieve the main entries of the temporary power organization design template.
    - `F1` finish - (depth=1)
      - reason: The target document section has been collected. No further actions needed to list its main entries.
    - `C1` collect L109 (depth=1) · →L109 · +3
      - reason: Collect the main section containing safety measures and fire prevention strategies as requested.
    - `F1` finish - (depth=1)
      - reason: The target document section has been collected. No further actions needed to list its main entries.
    - `C1` collect L115 (depth=1) · →L115 · +5
      - reason: Collecting the main 'Emergency Plan' section to identify its primary entries as requested.
    - `F1` finish - (depth=1)
      - reason: The target document section has been collected. Ready to list main entries based on evidence.
    - `C1` collect L114 (depth=1) · →L114 · +4
      - reason: Collecting the main section '制定应急预案及开展应急演练' to capture its primary structure and sub-items.
    - `F1` finish - (depth=1)
      - reason: The target section has been collected. No further actions needed to list the main entries.
    - `C1` collect L118 (depth=1) · →L118 · +4
      - reason: Collecting the Emergency Rescue Group section to gather all related tables and responsibilities.
    - `F1` finish - (depth=1)
      - reason: The target document section has been collected. No further actions needed to list its main entries.
    - `C1` collect L129 (depth=1) · multi→[L129, L130, L131, L132, L133] · +9
      - reason: Collecting all leaf sections under '相关图纸' to list the main items of the document.
    - `F1` finish - (depth=1)
      - reason: The target document section has been collected. No further actions needed to list its main entries.
- `C1` collect L20 (depth=0) · →L20 · +1
  - reason: Collect the remaining '编制依据' section to complete the document structure for listing main entries.
- `F1` finish - (depth=0)
  - reason: Sufficient evidence collected from 26 regions covering the main entries of the temporary power organization design template.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L12` | - | 3 | 3 | - |  |
| 3 | `C1` | `L1` | - | 7 | 7 | - |  |
| 5 | `C1` | `L2` | - | 1 | 1 | - | ✅ |
| 7 | `C1` | `L11` | L11, L12, L13, L14, L15, L16, L17 | 10 | 12 | - | ✅ |
| 9 | `C1` | `L16` | - | 1 | 1 | - | ✅ |
| 12 | `C1` | `L24` | - | 1 | 1 | - | ✅ |
| 14 | `C1` | `L21` | - | 3 | 3 | - |  |
| 16 | `C1` | `L22` | - | 1 | 1 | - | ✅ |
| 18 | `C1` | `L26` | - | 3 | 3 | - |  |
| 21 | `C1` | `L41` | - | 10 | 10 | - |  |
| 23 | `C1` | `L40` | - | 4 | 4 | - |  |
| 25 | `C1` | `L75` | - | 5 | 5 | - |  |
| 27 | `C1` | `L39` | - | 8 | 8 | - |  |
| 30 | `C1` | `L99` | - | 3 | 3 | - |  |
| 32 | `C1` | `L90` | - | 8 | 8 | - |  |
| 34 | `C1` | `L97` | - | 1 | 1 | - | ✅ |
| 36 | `C1` | `L102` | - | 3 | 3 | - |  |
| 38 | `C1` | `L112` | - | 1 | 1 | - | ✅ |
| 40 | `C1` | `L109` | - | 3 | 3 | - |  |
| 42 | `C1` | `L115` | - | 5 | 5 | - |  |
| 44 | `C1` | `L114` | - | 4 | 4 | - |  |
| 46 | `C1` | `L118` | - | 4 | 4 | - |  |
| 48 | `C1` | `L129` | L129, L130, L131, L132, L133 | 9 | 9 | - | ✅ |
| 51 | `C1` | `L20` | - | 1 | 1 | - | ✅ |

### 子 agent reports_context

```
=== Investigate results (26 region(s)) ===
[region 1] real_69c60aeed4242eda8c47c928:L12 (ok)
collected 3 branch node(s); explicit roots=['real_69c60aeed4242eda8c47c928:L12']
collected: real_69c60aeed4242eda8c47c928:L12, real_69c60aeed4242eda8c47c928:L13, real_69c60aeed4242eda8c47c928:L14
reason: The target section has been collected. No further actions needed to list the main entries.
---
[region 2] real_69c60aeed4242eda8c47c928:L1 (ok)
collected 19 branch node(s); explicit roots=['real_69c60aeed4242eda8c47c928:L1']
collected: real_69c60aeed4242eda8c47c928:L1, real_69c60aeed4242eda8c47c928:L10, real_69c60aeed4242eda8c47c928:L11, real_69c60aeed4242eda8c47c928:L12, real_69c60aeed4242eda8c47c928:L13, real_69c60aeed4242eda8c47c928:L14, real_69c60aeed4242eda8c47c928:L15, real_69c60aeed4242eda8c47c928:L16, real_69c60aeed4242eda8c47c928:L17, real_69c60aeed4242eda8c47c928:L18, real_69c60aeed4242eda8c47c928:L19, real_69c60aeed4242eda8c47c928:L2, real_69c60aeed4242eda8c47c928:L3, real_69c60aeed4242eda8c47c928:L4, real_69c60aeed4242eda8c47c928:L5, real_69c60aeed4242eda8c47c928:L6, real_69c60aeed4242eda8c47c928:L7, real_69c60aeed4242eda8c47c928:L8, real_69c60aeed4242eda8c47c928:L9
reason: The document root has been collected, containing the main structure of the temporary power organization design template. No further collection is needed.
---
[region 3] real_69c60aeed4242eda8c47c928:L2 (ok)
collected 2 branch node(s); explicit roots=['real_69c60aeed4242eda8c47c928:L2']
collected: real_69c60aeed4242eda8c47c928:L2, real_69c60aeed4242eda8c47c928:L3
reason: The required section has been collected. No further actions needed to list the main entries.
---
[region 4] real_69c60aeed4242eda8c47c928:L11 (ok)
collected 7 branch node(s); explicit roots=['real_69c60aeed4242eda8c47c928:L11']
collected: real_69c60aeed4242eda8c47c928:L11, real_69c60aeed4242eda8c47c928:L12, real_69c60aeed4242eda8c47c928:L13, real_69c60aeed4242eda8c47c928:L14, real_69c60aeed4242eda8c47c928:L15, real_69c60aeed424
```

### 最终 evidence(new)

**[E1]** [§ 相关图纸]
  临时用电工程总平面图
  临时用电工程总平面图
  配电装置布置图
  配电装置布置图
  配电系统接线图
  配电系统接线图
  接地装置设计图
  接地装置设计图

**[E2]** [§ 现场用电管理组织机构]
  组织机构人员配备
  组织机构人员配备

**[E3]** [§ 1.临时用电施工组织设计范本.docx]
编制依据

**[E4]** [§ 变压器容量计算要求]
  （1）变压器容量应分阶段计算，如按地基与基础、主体、装饰与机电安装等，取各阶段最大值为项目临时用电的变压器容量。
  （2）所选择的变压器的容量应大于各阶段最大值与变压器的损耗之和。
  （1）变压器容量应分阶段计算，如按地基与基础、主体、装饰与机电安装等，取各阶段最大值为项目临时用电的变压器容量。
  （2）所选择的变压器的容量应大于各阶段最大值与变压器的损耗之和。
  ∆PB≈0.02Sj
  ∆SB＝
  Sj :变压器的计算负荷（单位：kVA）；
  ΔPB :为变压器有功损耗（单位：kW）；
  ΔQB :为变压器无功损耗（单位：kvar）；

- retrieved_nodes: L130, L131, L132, L133, L15, L20, L39, L40, L41, L42⭐, L43⭐, L44, L46, L47⭐, L48⭐, L49⭐


---

## latest_clean_scope_0119  ·  scope_collection

- **Query:** 列举《9.1土方开挖方案范本》中“9.1土方开挖方案范本.docx”部分的主要条目。
- **Doc:** `real_69c60af6d4242eda8c47c934`
- **Gold nodes:** L5, L7, L8, L13, L16, L19

### 结果得分 — **PASS** (new gold_recall=0.50)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.50 |
| evidence_chars | 500 | 498 |
| n_retrieved_nodes | 28 | 20 |
| trajectory_steps | - | 13 |
| elapsed_sec | - | 21.8 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L5` | ❌ | False | False |
| `L7` | ❌ | False | False |
| `L8` | ❌ | False | False |
| `L13` | ✅ | True | False |
| `L16` | ✅ | True | False |
| `L19` | ✅ | True | False |

### 决策 TRACE(因果序)

- `D1` dispatch L1 (depth=0) · regions=[L1, L31, L41, L56, L103, L120] · child_reports=6
  - reason: Dispatch main sections to gather the document's primary structure and content efficiently.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L31 (depth=1) · →L31 · +4
      - reason: Collect the main 'Construction Plan' section to retrieve all its sub-items as requested.
    - `F1` finish - (depth=1)
      - reason: The target section has been collected. No further actions needed to list the main entries.
    - `C1` collect L56 (depth=1) · →L56 · +4
      - reason: Collect the main '施工保证措施' section to identify its primary entries as requested.
    - `F1` finish - (depth=1)
      - reason: The target document section has been collected. No further actions needed to list its main entries.
    - `C1` collect L41 (depth=1) · →L41 · +6
      - reason: rule_fallback_illegal_action
    - `F1` finish - (depth=1)
      - reason: The required section has been collected and contains the main entries of the土方开挖方案范本.
    - `C1` collect L1 (depth=1) · →L1 · +8
      - reason: rule_fallback_illegal_action
    - `F1` finish - (depth=1)
      - reason: The document root has been collected, which contains the main entries of the土方开挖方案范本.
    - `C1` collect L103 (depth=1) · →L103 · +4
      - reason: Collecting the '验收要求' section to retrieve all its sub-items as requested.
    - `F1` finish - (depth=1)
      - reason: The target document section has been collected. No further actions needed to list main entries.
    - `F1` finish - (depth=1)
      - reason: Collected evidence covers the main emergency response sections of the土方开挖方案范本, sufficient to list key items.
- `F1` finish - (depth=0)
  - reason: Sufficient evidence collected from all major sections to list the main entries of the土方开挖方案范本.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L31` | - | 4 | 4 | - |  |
| 3 | `C1` | `L56` | - | 4 | 4 | - |  |
| 5 | `C1` | `L41` | - | 6 | 6 | - |  |
| 7 | `C1` | `L1` | - | 8 | 8 | - |  |
| 9 | `C1` | `L103` | - | 4 | 4 | - |  |

### 子 agent reports_context

```
=== Investigate results (6 region(s)) ===
[region 1] real_69c60af6d4242eda8c47c934:L31 (ok)
collected 10 branch node(s); explicit roots=['real_69c60af6d4242eda8c47c934:L31']
collected: real_69c60af6d4242eda8c47c934:L31, real_69c60af6d4242eda8c47c934:L32, real_69c60af6d4242eda8c47c934:L33, real_69c60af6d4242eda8c47c934:L34, real_69c60af6d4242eda8c47c934:L35, real_69c60af6d4242eda8c47c934:L36, real_69c60af6d4242eda8c47c934:L37, real_69c60af6d4242eda8c47c934:L38, real_69c60af6d4242eda8c47c934:L39, real_69c60af6d4242eda8c47c934:L40
reason: The target section has been collected. No further actions needed to list the main entries.
---
[region 2] real_69c60af6d4242eda8c47c934:L56 (ok)
collected 34 branch node(s); explicit roots=['real_69c60af6d4242eda8c47c934:L56']
collected: real_69c60af6d4242eda8c47c934:L56, real_69c60af6d4242eda8c47c934:L57, real_69c60af6d4242eda8c47c934:L58, real_69c60af6d4242eda8c47c934:L59, real_69c60af6d4242eda8c47c934:L60, real_69c60af6d4242eda8c47c934:L61, real_69c60af6d4242eda8c47c934:L62, real_69c60af6d4242eda8c47c934:L63, real_69c60af6d4242eda8c47c934:L64, real_69c60af6d4242eda8c47c934:L65, real_69c60af6d4242eda8c47c934:L66, real_69c60af6d4242eda8c47c934:L67, real_69c60af6d4242eda8c47c934:L68, real_69c60af6d4242eda8c47c934:L69, real_69c60af6d4242eda8c47c934:L70, real_69c60af6d4242eda8c47c934:L71, real_69c60af6d4242eda8c47c934:L72, real_69c60af6d4242eda8c47c934:L73, real_69c60af6d4242eda8c47c934:L74, real_69c60af6d4242eda8c47c934:L75
reason: The target document section has been collected. No further actions needed to list its main entries.
---
[region 3] real_69c60af6d4242eda8c47c934:L41 (ok)
collected 15 branch node(s); explicit roots=['real_69c60af6d4242eda8c47c934:L41']
collected: real_69c60af6d4242eda8c47c934:L41, real_69c60af6d4242eda8c47c934:L42, real_69c60af6d4242eda8c47c934:L43, real_69c60af6d4242eda8c47c934:L44, real_69c60af6d4242eda8c47c934:L45, real_69c60af6d4242eda8c47c934:L46, real_69c60af6d4242eda8c47c934:L47, real_69c60af6d4242eda
```

### 最终 evidence(new)

**[E1]** [§ 验收要求]
  验收标准
  土方开挖过程中，项目部组织相关人员对土方开挖标高、长度宽度、边坡、原状地基土等进行复核和验收，填写复核记录和质量验收记录表。
  表7.1土方开挖允许偏差及检验方法
  验收程序及人员
  验收程序
  验收人员
  验收内容

**[E2]** [§ 工程概况]
  基坑工程概况和特点
  工程基本情况
  表1.1工程基本情况表
  周边环境条件
  表1.3周边环境统计表
  项目北侧为沣东三路，东侧为科源一路，车流量少且无拥堵；场地周围无河流；无地上地下管线；东侧毗邻沣东第一中学，施工期间扰民影响较小。
  基坑开挖设计
  本工程基坑分A、B、C、D四区流水施工，顺序为A至D。最深处6.8m，分三层开挖（3m、2m、1.8m），预留200-300mm人工清理。支护与开挖同步，待上层强度达70%后挖下层平台并支护。
  施工平面及立面布置
  施工总平面图
  内容涵盖施工总平面图布局、办公区及出入口设置、机械选型、道路布置等，并简述了幼儿园与车库的分区情况及施工顺序。

**[E3]** [§ 施工工艺技术]
技术参数
表4.1技术参数一览表

- retrieved_nodes: L104, L105, L106, L115, L116, L117, L119, L2, L3, L4, L11, L12, L13⭐, L15, L16⭐, L17, L18, L19⭐, L42, L43


---

## real_69c6ef484cca74801cb63bb9_multi_hop_auto_0006  ·  multi_hop

- **Query:** 根据质量控制要求，注浆允许偏差及检验办法应符合哪张表的规定？该表中列出了哪四个关键检查项目？同时，在浆液拌制过程中有哪些具体的操作要求以确保质量？
- **Doc:** `real_69c6ef484cca74801cb63bb9`
- **Gold nodes:** L159, L162, L167

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 497 |
| n_retrieved_nodes | 12 | 11 |
| trajectory_steps | - | 9 |
| elapsed_sec | - | 32.7 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L159` | ❌ | False | False |
| `L162` | ❌ | False | False |
| `L167` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C20` collect L128 (depth=0) · →L128 · +1
  - reason: Identifies the table for grouting deviation and inspection requirements.
- `C20` collect L129 (depth=0) · →L129 · +33
  - reason: Collect table 7.2.1 to identify the four key inspection items and their requirements.
- `D14` dispatch L113 (depth=0) · regions=[L113] · child_reports=1
  - reason: Dispatch to find the table with allowable deviations and inspection methods for grouting.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L113 (depth=1) · →L113 · +2
      - reason: Collect section 5.2.9 to find the table for grouting deviation and inspection methods.
    - `F1` finish - (depth=1)
      - reason: Collected section L113 contains the required table for grouting deviation, inspection items, and slurry mixing requirements.
- `C28` collect L99 (depth=0) · →L99 · +1
  - reason: Collects slurry mixing requirements and material ratios from the 'Grouting' section.
- `C34` collect L127 (depth=0) · →L127 · +1 · PURGED後代×1
  - reason: Collect section L115 under C34 to retrieve the specific table and slurry mixing requirements.
- `C33` collect L126 (depth=0) · →L126 · +2 · PURGED後代×1
  - reason: Collect the referenced standard table for grouting deviation and inspection items.
- `F1` finish - (depth=0)
  - reason: Evidence collected from L113 contains the required table, inspection items, and slurry mixing requirements.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C20` | `L128` | - | 1 | 1 | - | ✅ |
| 2 | `C20` | `L129` | - | 33 | 33 | - | ✅ |
| 3 | `C1` | `L113` | - | 2 | 2 | - | ✅ |
| 6 | `C28` | `L99` | - | 1 | 1 | - | ✅ |
| 7 | `C34` | `L127` | - | 1 | 1 | 1 | ✅ |
| 8 | `C33` | `L126` | - | 2 | 2 | 1 | ✅ |

**水合告警:**
- step 7 `C34` 收父节点 `L127` 时 **purge 掉 1 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。
- step 8 `C33` 收父节点 `L126` 时 **purge 掉 1 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c6ef484cca74801cb63bb9:L113 (ok)
collected 3 branch node(s); explicit roots=['real_69c6ef484cca74801cb63bb9:L113']
collected: real_69c6ef484cca74801cb63bb9:L113, real_69c6ef484cca74801cb63bb9:L114, real_69c6ef484cca74801cb63bb9:L115
reason: Collected section L113 contains the required table for grouting deviation, inspection items, and slurry mixing requirements.
---
=== End Investigate ===
```

### 最终 evidence(new)

**[E1]** [§ 7.2 主要控制措施]
注浆允许偏差及检验办法应符合表7.2.1的规定。

**[E2]** [§ 5.2.7 注浆]
注浆前，严格按照配方配料。其中帷幕采用AB液作为注浆材料，A液∶B液=1∶1 ，其中A液：水泥：水=0.8∶1；B液：中性水玻璃，水玻璃为波美度25°～30°；帷 幕中心区采用纯水泥浆作为注浆材料，注浆水泥采用强度等级为Po42.5R普通水泥。 施工用水采用自来水。浆液应搅拌均匀，随拌随注，不得长时间存放已拌好的浆液 。封闭泥浆用泵从钻杆自下而上压入孔内，不准从孔口到入。

**[E3]** [§ 7.3 加强施工测量，确保钻杆竖直，位置满足规范要求。]
  - 7.4 注浆开始前应充分作好准备工作，包括机械器具、仪表、管路、注浆材料、水和 电等的检查及必要的试验，注浆一经开始即应连续进行，力求避免中断。
  - 7.6 浆液拌制严格按配合比要求，并在拌浆现场悬挂配比牌。浆体必须经搅拌机充分 搅拌均匀，方可开始压浆，浆体在泵送前经筛网过滤。

**[E4]** [§ 8.2安全保证措施]
- 8.2.4 在施工的过程中应定期检查注浆高压管表面有无损伤、裂缝、龟裂等，一经

- retrieved_nodes: L126, L127, L128, L99, L129, L130, L131, L133, L139, L143, L149


---

## latest_clean_multi_0010  ·  multi_hop

- **Query:** 根据《线上学习平台学习管理方案（修订）》中“十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订）”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c6095ed4242eda8c47c5b2`
- **Gold nodes:** L2, L3

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 210 | 476 |
| n_retrieved_nodes | 2 | 12 |
| trajectory_steps | - | 4 |
| elapsed_sec | - | 5.58 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L2` | ❌ | False | False |
| `L3` | ❌ | False | False |

### 决策 TRACE(因果序)

- `D1` dispatch L1 (depth=0) · regions=[L1] · child_reports=1
  - reason: Dispatch main section to gather detailed evidence for the query.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L1 (depth=1) · →L1 · +36
      - reason: rule_fallback_illegal_action
    - `F1` finish - (depth=1)
      - reason: Only one section collected; insufficient evidence to identify two adjacent sections as required.
- `F1` finish - (depth=0)
  - reason: Collected evidence is insufficient to identify two adjacent sections as required by the query.

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
reason: Only one section collected; insufficient evidence to identify two adjacent sections as required.
---
=== End Investigate ===
```

### 最终 evidence(new)

**[E1]** [§ 4.其他事项]
  （ 1）各管理员在线上学习平台创建线下培训时，应结合本公司培训计划和实际业务需求创建，创建过程中，做好签到设置、学员管理和指派设置，根据实际设置培训学时时长。
  （ 2）线下培训结束后，及时留存培训资料，培训资料包括培训方案、培训签到表、培训教材、培训记录（如照片、学习笔记等）等。
  （ 3 ）十一在线平台中心后期将根据后台创建的线下培训记录，不定期抽查相关学习资料，保证学习的真实性和有效性。如发现有不实情形，获得该门线下培训学时的学员，学时为不合格，并给予相关人员通报。
  （ 4）其他未尽事宜，另行规定。
  附件：xxx 年度线上课程开发计划汇总表（针对非研修班涉及岗位）

**[E2]** [§ （ 一）课程开发管理]
  2.课件评审。课件开发完成后，根据课程类别提交各专家组审核，专家组从课件选材、专业度、实用性等方面对课件进行评审，课程评审管理参照《十一在线——员工赋能一体化平台管理办法》执行。
  4.课酬兑现。开发的课程根据《十一在线——员工赋能一体化平台管理办法》相关规定标准兑现相应课酬。

- retrieved_nodes: L1, L32, L38, L47, L48, L49, L50, L51, L52, L33, L35, L37


---

## latest_clean_multi_0032  ·  multi_hop

- **Query:** 根据《线上学习平台学习管理方案（修订）》中“（ 一）课程开发管理”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c6095ed4242eda8c47c5b2`
- **Gold nodes:** L34, L35

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 142 | 477 |
| n_retrieved_nodes | 2 | 6 |
| trajectory_steps | - | 8 |
| elapsed_sec | - | 9.31 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L34` | ✅ | True | False |
| `L35` | ✅ | True | False |

### 决策 TRACE(因果序)

- `D10` dispatch L33 (depth=0) · regions=[L33] · child_reports=1
  - reason: Dispatch to 'Course Development Management' section to find adjacent evidence points.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C2` collect L34 (depth=1) · →L34 · +1
      - reason: Collect first adjacent evidence point on course development principles and planning.
    - `C2` collect L35 (depth=1) · →L35 · +1
      - reason: Collect adjacent section 2 (课件评审) to compare with previously collected section 1.
    - `C2` collect L36 (depth=1) · →L36 · +1
      - reason: Collect adjacent evidence on courseware upload requirements to answer the query.
    - `C1` collect L33 (depth=1) · →L33 · +4 · PURGED後代×3
      - reason: Collects the main 'Course Development Management' section to identify the first adjacent evidence point.
    - `F1` finish - (depth=1)
      - reason: Collected evidence covers the required section on course development management. Ready to answer.
- `C14` collect L20 (depth=0) · →L20 · +1
  - reason: Collect adjacent evidence on course development management requirements.
- `F1` finish - (depth=0)
  - reason: Collected evidence covers the required section on course development management. Ready to answer.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C2` | `L34` | - | 1 | 1 | - | ✅ |
| 2 | `C2` | `L35` | - | 1 | 1 | - | ✅ |
| 3 | `C2` | `L36` | - | 1 | 1 | - | ✅ |
| 4 | `C1` | `L33` | - | 4 | 4 | 3 | ✅ |
| 7 | `C14` | `L20` | - | 1 | 1 | - | ✅ |

**水合告警:**
- step 4 `C1` 收父节点 `L33` 时 **purge 掉 3 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c6095ed4242eda8c47c5b2:L33 (ok)
collected 5 branch node(s); explicit roots=['real_69c6095ed4242eda8c47c5b2:L34', 'real_69c6095ed4242eda8c47c5b2:L35', 'real_69c6095ed4242eda8c47c5b2:L36', 'real_69c6095ed4242eda8c47c5b2:L33']
collected: real_69c6095ed4242eda8c47c5b2:L33, real_69c6095ed4242eda8c47c5b2:L34, real_69c6095ed4242eda8c47c5b2:L35, real_69c6095ed4242eda8c47c5b2:L36, real_69c6095ed4242eda8c47c5b2:L37
reason: Collected evidence covers the required section on course development management. Ready to answer.
---
=== End Investigate ===
```

### 最终 evidence(new)

**[E1]** [§ （ 一）课程类别]
明确课程名称、课程类别、必修岗位、课程开发负责人等信息（见附件），提交十一在线平台中心审批后按计划开发。

**[E2]** [§ （ 一）课程开发管理]
  1.课程开发。课程开发依托专家组、各业务线要从有利于组织目标达成、员工履职能力提升等方面，本着“简单、实用、明了”原则进行课程开发。各专家组、各部门应按年度既定课程开发计划，督促、跟进课程开发负责人按时完成课件开发任务。计划外课程开发须明确开发课程名称、学习对象等，经各专家组审核后开发，并向平台中心办公室备案。
  2.课件评审。课件开发完成后，根据课程类别提交各专家组审核，专家组从课件选材、专业度、实用性等方面对课件进行评审，课程评审管理参照《十一在线——员工赋能一体化平台管理办法》执行。
  3.课件上传。评审通过后，平台管理员需在课程计划提交截止时间5 日内完成课件上传和必修岗位指派。计划外开发的课程经各专家组评审通过后5 日完成上传和必修岗位指派。
  4.课酬兑现。开发的课程根据《十一在线——员工赋能一体化平台管理办法》相关规定标准兑现相应课酬。

- retrieved_nodes: L20, L33, L34⭐, L35⭐, L36, L37


---

## latest_clean_multi_0048  ·  multi_hop

- **Query:** 根据《集团公司对外捐赠管理办法（修订版）》中“第二章 对外捐赠的范围及类型”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60970d4242eda8c47c5fd`
- **Gold nodes:** L7, L8

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 495 | 466 |
| n_retrieved_nodes | 11 | 10 |
| trajectory_steps | - | 6 |
| elapsed_sec | - | 14.68 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L7` | ✅ | True | False |
| `L8` | ✅ | True | False |

### 决策 TRACE(因果序)

- `D3` dispatch L6 (depth=0) · regions=[L6] · child_reports=1
  - reason: Dispatch Chapter 2 to extract details on scope and types for the query.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L6 (depth=1) · →L6 · +18
      - reason: rule_fallback_illegal_action
    - `F1` finish - (depth=1)
      - reason: Collected section L6 contains the required content on donation scope and types to answer the query.
- `C1` collect L2 (depth=0) · →L2 · +1
  - reason: Collect section C1 to obtain the content on donation scope and types required by the query.
- `C1` collect L3 (depth=0) · multi→[L3, L4, L5] · +2
  - reason: Collect Chapter 1 content to identify the two adjacent evidence sections regarding donation scope and types.
- `F1` finish - (depth=0)
  - reason: Collected evidence from L6 (Chapter 2) covers donation scope and types. Ready to answer query.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L6` | - | 18 | 18 | - | ✅ |
| 4 | `C1` | `L2` | - | 1 | 1 | - | ✅ |
| 5 | `C1` | `L3` | L3, L4, L5 | 2 | 4 | - | ✅ |

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60970d4242eda8c47c5fd:L6 (ok)
collected 21 branch node(s); explicit roots=['real_69c60970d4242eda8c47c5fd:L6']
collected: real_69c60970d4242eda8c47c5fd:L10, real_69c60970d4242eda8c47c5fd:L11, real_69c60970d4242eda8c47c5fd:L12, real_69c60970d4242eda8c47c5fd:L13, real_69c60970d4242eda8c47c5fd:L14, real_69c60970d4242eda8c47c5fd:L15, real_69c60970d4242eda8c47c5fd:L16, real_69c60970d4242eda8c47c5fd:L17, real_69c60970d4242eda8c47c5fd:L18, real_69c60970d4242eda8c47c5fd:L19, real_69c60970d4242eda8c47c5fd:L20, real_69c60970d4242eda8c47c5fd:L21, real_69c60970d4242eda8c47c5fd:L22, real_69c60970d4242eda8c47c5fd:L23, real_69c60970d4242eda8c47c5fd:L24, real_69c60970d4242eda8c47c5fd:L25, real_69c60970d4242eda8c47c5fd:L26, real_69c60970d4242eda8c47c5fd:L6, real_69c60970d4242eda8c47c5fd:L7, real_69c60970d4242eda8c47c5fd:L8
reason: Collected section L6 contains the required content on donation scope and types to answer the query.
---
=== End Investigate ===
```

### 最终 evidence(new)

**[E1]** [§ 陕西建工第十一建设集团有限公司]
对外捐赠管理办法（修订版）

**[E2]** [§ 第一章  总则]
  第一条为进一步规范集团公司对外捐赠行为，加强对外捐赠事项的管理，更好地履行社会责任，全面、有效提升和宣传集团公司品牌及企业形象，特制定本办法。
  第二条本办法适用于集团公司及所属各单位对外捐赠行为。

**[E3]** [§ 第二章  对外捐赠的范围及类型]
  第三条本办法所称的“对外捐赠”，是指集团公司及所属各单位自愿将有处分权的合法财产无偿赠送给合法的受赠人（包含无偿捐赠工程），用于与捐赠人生产经营活动没有直接关系的公益事业的行为。
  集团公司所属非法人分支机构、项目部不得以分公司、项目部名义对外捐赠，不得将企业拥有的财产以个人名义对外捐赠。
  对外捐赠原则上以集团公司（陕西建工第十一建设集团有限公司）名义进行捐赠，独立法人单位可根据实际需要以本单位名义进行捐赠。

**[E4]** [§ 第五条  对外捐赠的范围]
用于对外捐赠的资产应当权属清晰，应为集团公司有权处分的合法财产，包括现金资产和实物资产等。

- retrieved_nodes: L2, L3, L4, L5, L6, L7⭐, L8⭐, L9, L15, L16


---

## latest_clean_niche_0023  ·  niche_fact

- **Query:** 根据《线上学习平台学习管理方案（修订）》中“（ 一）课程开发管理”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c6095ed4242eda8c47c5b2`
- **Gold nodes:** L34

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 207 | 483 |
| n_retrieved_nodes | 3 | 6 |
| trajectory_steps | - | 6 |
| elapsed_sec | - | 7.17 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L34` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C24` collect L33 (depth=0) · multi→[L33, L34, L35, L37] · +4
  - reason: Collect section (一)课程开发管理 and its leaf nodes to extract specific regulations.
- `C15` collect L21 (depth=0) · →L21 · +1
  - reason: Collects the specific fact about course development quantity and content requirements under 'Course Development Management'.
- `D6` dispatch L17 (depth=0) · regions=[L17] · child_reports=1
  - reason: Dispatch to 'Course and Assignment Management' section to find regulations on course development.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L17 (depth=1) · →L17 · +12 · PURGED後代×1
      - reason: Collect section II to access 'Course Development Management' details.
    - `F1` finish - (depth=1)
      - reason: The required section '（一）课程开发管理' has been collected. No further actions needed.
- `F1` finish - (depth=0)
  - reason: The required section '（一）课程开发管理' was collected in a previous step (L17). Evidence is sufficient to answer the query.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C24` | `L33` | L33, L34, L35, L37 | 4 | 7 | - | ✅ |
| 2 | `C15` | `L21` | - | 1 | 1 | - | ✅ |
| 3 | `C1` | `L17` | - | 12 | 12 | 1 | ✅ |

**水合告警:**
- step 1 整枝水合含 3 个非 gold 叶 (与 gold 争抢 evidence 预算)。
- step 3 `C1` 收父节点 `L17` 时 **purge 掉 1 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c6095ed4242eda8c47c5b2:L17 (ok)
collected 14 branch node(s); explicit roots=['real_69c6095ed4242eda8c47c5b2:L17']
collected: real_69c6095ed4242eda8c47c5b2:L17, real_69c6095ed4242eda8c47c5b2:L18, real_69c6095ed4242eda8c47c5b2:L19, real_69c6095ed4242eda8c47c5b2:L20, real_69c6095ed4242eda8c47c5b2:L22, real_69c6095ed4242eda8c47c5b2:L23, real_69c6095ed4242eda8c47c5b2:L24, real_69c6095ed4242eda8c47c5b2:L25, real_69c6095ed4242eda8c47c5b2:L26, real_69c6095ed4242eda8c47c5b2:L27, real_69c6095ed4242eda8c47c5b2:L28, real_69c6095ed4242eda8c47c5b2:L29, real_69c6095ed4242eda8c47c5b2:L30, real_69c6095ed4242eda8c47c5b2:L31
reason: The required section '（一）课程开发管理' has been collected. No further actions needed.
---
=== End Investigate ===
```

### 最终 evidence(new)

**[E1]** [§ （ 一）课程开发管理]
  1.课程开发。课程开发依托专家组、各业务线要从有利于组织目标达成、员工履职能力提升等方面，本着“简单、实用、明了”原则进行课程开发。各专家组、各部门应按年度既定课程开发计划，督促、跟进课程开发负责人按时完成课件开发任务。计划外课程开发须明确开发课程名称、学习对象等，经各专家组审核后开发，并向平台中心办公室备案。
  2.课件评审。课件开发完成后，根据课程类别提交各专家组审核，专家组从课件选材、专业度、实用性等方面对课件进行评审，课程评审管理参照《十一在线——员工赋能一体化平台管理办法》执行。
  3.课件上传。评审通过后，平台管理员需在课程计划提交截止时间5 日内完成课件上传和必修岗位指派。计划外开发的课程经各专家组评审通过后5 日完成上传和必修岗位指派。
  4.课酬兑现。开发的课程根据《十一在线——员工赋能一体化平台管理办法》相关规定标准兑现相应课酬。

**[E2]** [§ （ 一）课程类别]
必修课程的开发数量各专家组结合业务和岗位需求实际确定，课程包含内部自主开发和外部引进，保证课程内容的实用性和有效性。

- retrieved_nodes: L33, L34⭐, L35, L36, L37, L21


---

## latest_clean_niche_0043  ·  niche_fact

- **Query:** 根据《集团公司对外捐赠管理办法（修订版）》中“第四条 对外捐赠的类型”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60970d4242eda8c47c5fd`
- **Gold nodes:** L11

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 464 |
| n_retrieved_nodes | 10 | 8 |
| trajectory_steps | - | 8 |
| elapsed_sec | - | 10.04 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L11` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C9` collect L10 (depth=0) · multi→[L10, L11, L12, L13] · +4
  - reason: Collect Article 4 types of external donations as requested.
- `D3` dispatch L6 (depth=0) · regions=[L6] · child_reports=1
  - reason: Dispatch to Chapter 2 to find Article 4 on donation types.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L7 (depth=1) · →L7 · +1
      - reason: Collects the definition of external donation from Article 3, which is part of the scope and types section.
    - `F1` finish - (depth=1)
      - reason: The document does not contain 'Article 4' or its content on donation types. Collected evidence confirms this section is missing.
- `C7` collect L15 (depth=0) · →L15 · +11
  - reason: The subagent report confirms Article 4 is missing. Collecting Chapter 2 (N9) to verify if 'types' are defined elsewhere or confirm absence.
- `C1` collect L2 (depth=0) · →L2 · +1
  - reason: Collect the document title to verify if Article 4 content exists within the full text.
- `C5` collect L9 (depth=0) · →L9 · +1
  - reason: Section N7 explicitly states the rule regarding donation names, which is the only content found under 'types' in this document.
- `F1` finish - (depth=0)
  - reason: Subagent report confirms Article 4 on donation types is missing from the document. No further collection needed.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C9` | `L10` | L10, L11, L12, L13 | 4 | 7 | - | ✅ |
| 2 | `C1` | `L7` | - | 1 | 1 | - | ✅ |
| 5 | `C7` | `L15` | - | 11 | 11 | - | ✅ |
| 6 | `C1` | `L2` | - | 1 | 1 | - | ✅ |
| 7 | `C5` | `L9` | - | 1 | 1 | - | ✅ |

**水合告警:**
- step 1 整枝水合含 3 个非 gold 叶 (与 gold 争抢 evidence 预算)。

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60970d4242eda8c47c5fd:L6 (ok)
collected 1 branch node(s); explicit roots=['real_69c60970d4242eda8c47c5fd:L7']
collected: real_69c60970d4242eda8c47c5fd:L7
reason: The document does not contain 'Article 4' or its content on donation types. Collected evidence confirms this section is missing.
---
=== End Investigate ===
```

### 最终 evidence(new)

**[E1]** [§ 第二章  对外捐赠的范围及类型]
  第三条本办法所称的“对外捐赠”，是指集团公司及所属各单位自愿将有处分权的合法财产无偿赠送给合法的受赠人（包含无偿捐赠工程），用于与捐赠人生产经营活动没有直接关系的公益事业的行为。
  对外捐赠原则上以集团公司（陕西建工第十一建设集团有限公司）名义进行捐赠，独立法人单位可根据实际需要以本单位名义进行捐赠。

**[E2]** [§ 第四条  对外捐赠的类型]
  （一）救济性捐赠，即向受灾地区、扶贫地区或者困难的社会弱势群体的救济性捐赠。
  （二）公益性捐赠，即向科技文卫事业和环境保护等社会公益事业的公益性捐赠。
  （三）其他捐赠，即除上述捐赠外，为促进社会发展以及集团公司履行社会责任需要的其他捐赠，含外部各类活动赞助。
  各单位要正确参与社会公益事业，依法依规确定对外捐赠范围和支出规模，规范开展对外捐赠活动，避免无序、随意捐赠等行为。对于有关社会机构、团体的摊派性捐赠，要坚决依法拒绝，

**[E3]** [§ 陕西建工第十一建设集团有限公司]
对外捐赠管理办法（修订版）

- retrieved_nodes: L7, L9, L10, L11⭐, L12, L13, L14, L2


---

## latest_clean_niche_0068  ·  niche_fact

- **Query:** 根据《陕西建工第十一建设集团有限公司印章管理办法（2020版）》中“陕西建工第十一建设集团有限公司印章管理办法（2020版）.docx”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60971d4242eda8c47c605`
- **Gold nodes:** L2

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 479 | 492 |
| n_retrieved_nodes | 8 | 5 |
| trajectory_steps | - | 24 |
| elapsed_sec | - | 31.25 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L2` | ❌ | False | False |

### 决策 TRACE(因果序)

- `D1` dispatch L1 (depth=0) · regions=[L1, L7, L25, L36, L49, L58, L73, L83, L91, L110, L118] · child_reports=11
  - reason: Dispatch all chapters to gather comprehensive regulations on seal management, usage, and penalties.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L1 (depth=1) · →L1 · +5
      - reason: Collect Chapter 1 to gather all relevant regulations on seal management.
    - `F1` finish - (depth=1)
      - reason: Evidence collected is sufficient to answer the query about the seal management regulations.
    - `C1` collect L36 (depth=1) · →L36 · +6
      - reason: Collecting Article 10 to capture all specified seal usage scopes for the query.
    - `F1` finish - (depth=1)
      - reason: Evidence collected from the relevant section is sufficient to answer the query about the seal management regulations.
    - `C1` collect L7 (depth=1) · →L7 · +17
      - reason: Collect Chapter 2 to gather all regulations on seal carving and activation.
    - `F1` finish - (depth=1)
      - reason: Evidence collected from the dispatched region is sufficient to answer the query about the seal management regulations.
    - `C1` collect L25 (depth=1) · →L25 · +29
      - reason: rule_fallback_illegal_action
    - `F1` finish - (depth=1)
      - reason: Evidence collected from the relevant section is sufficient to answer the query about the seal management regulations.
    - `C1` collect L49 (depth=1) · →L49 · +8
      - reason: Collecting Article 12 to capture all specified scope and rules for project department seals.
    - `F1` finish - (depth=1)
      - reason: Evidence collected from the relevant section is sufficient to answer the query about the seal management regulations.
    - `C1` collect L91 (depth=1) · →L91 · +9
      - reason: Collecting Article 30 to capture all inspection and supervision regulations regarding seal management.
    - `F1` finish - (depth=1)
      - reason: Evidence collected from the relevant section is sufficient to answer the query about the seal management regulations.
    - `C1` collect L58 (depth=1) · →L58 · +14
      - reason: Collect Chapter 4 to gather all seal approval procedures and regulations.
    - `F1` finish - (depth=1)
      - reason: Evidence collected from the relevant section is sufficient to answer the query about the seal management regulations.
    - `C3` collect L75 (depth=1) · →L75 · +1
      - reason: Collects Article 21 defining seal management responsibilities as required by the query.
    - `F1` finish - (depth=1)
      - reason: Collected evidence covers key regulations on seal management, custody, usage, and supervision as required.
    - `C1` collect L83 (depth=1) · →L83 · +7
      - reason: Collecting the full section on seal registration and record keeping to answer the query about specific regulations.
    - `F1` finish - (depth=1)
      - reason: Evidence collected from the relevant section is sufficient to answer the query about the seal management regulations.
    - `C1` collect L110 (depth=1) · multi→[L110, L111, L112, L113, L114, L115, L116, L117] · +7
      - reason: Collect all articles in Chapter 7 to extract specific regulations on seal management violations and penalties.
    - `F1` finish - (depth=1)
      - reason: Evidence collected from the relevant section is sufficient to answer the query about the seal management regulations.
    - `C1` collect L118 (depth=1) · →L118 · +17
      - reason: Collect Chapter 8 to gather all relevant regulations and facts from the document.
    - `F1` finish - (depth=1)
      - reason: Evidence collected from the relevant section is sufficient to answer the query about the seal management regulations.
- `F1` finish - (depth=0)
  - reason: Sufficient evidence collected from 11 regions covering seal management regulations to answer the query.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L1` | - | 5 | 5 | - | ✅ |
| 3 | `C1` | `L36` | - | 6 | 6 | - | ✅ |
| 5 | `C1` | `L7` | - | 17 | 17 | - | ✅ |
| 7 | `C1` | `L25` | - | 29 | 29 | - | ✅ |
| 9 | `C1` | `L49` | - | 8 | 8 | - | ✅ |
| 11 | `C1` | `L91` | - | 9 | 9 | - | ✅ |
| 13 | `C1` | `L58` | - | 14 | 14 | - | ✅ |
| 15 | `C3` | `L75` | - | 1 | 1 | - | ✅ |
| 17 | `C1` | `L83` | - | 7 | 7 | - | ✅ |
| 19 | `C1` | `L110` | L110, L111, L112, L113, L114, L115, L116, L117 | 7 | 14 | - | ✅ |
| 21 | `C1` | `L118` | - | 17 | 17 | - | ✅ |

### 子 agent reports_context

```
=== Investigate results (11 region(s)) ===
[region 1] real_69c60971d4242eda8c47c605:L1 (ok)
collected 6 branch node(s); explicit roots=['real_69c60971d4242eda8c47c605:L1']
collected: real_69c60971d4242eda8c47c605:L1, real_69c60971d4242eda8c47c605:L2, real_69c60971d4242eda8c47c605:L3, real_69c60971d4242eda8c47c605:L4, real_69c60971d4242eda8c47c605:L5, real_69c60971d4242eda8c47c605:L6
reason: Evidence collected is sufficient to answer the query about the seal management regulations.
---
[region 2] real_69c60971d4242eda8c47c605:L36 (ok)
collected 7 branch node(s); explicit roots=['real_69c60971d4242eda8c47c605:L36']
collected: real_69c60971d4242eda8c47c605:L36, real_69c60971d4242eda8c47c605:L37, real_69c60971d4242eda8c47c605:L38, real_69c60971d4242eda8c47c605:L39, real_69c60971d4242eda8c47c605:L40, real_69c60971d4242eda8c47c605:L41, real_69c60971d4242eda8c47c605:L42
reason: Evidence collected from the relevant section is sufficient to answer the query about the seal management regulations.
---
[region 3] real_69c60971d4242eda8c47c605:L7 (ok)
collected 18 branch node(s); explicit roots=['real_69c60971d4242eda8c47c605:L7']
collected: real_69c60971d4242eda8c47c605:L10, real_69c60971d4242eda8c47c605:L11, real_69c60971d4242eda8c47c605:L12, real_69c60971d4242eda8c47c605:L13, real_69c60971d4242eda8c47c605:L14, real_69c60971d4242eda8c47c605:L15, real_69c60971d4242eda8c47c605:L16, real_69c60971d4242eda8c47c605:L17, real_69c60971d4242eda8c47c605:L18, real_69c60971d4242eda8c47c605:L19, real_69c60971d4242eda8c47c605:L20, real_69c60971d4242eda8c47c605:L21, real_69c60971d4242eda8c47c605:L22, real_69c60971d4242eda8c47c605:L23, real_69c60971d4242eda8c47c605:L24, real_69c60971d4242eda8c47c605:L7, real_69c60971d4242eda8c47c605:L8, real_69c60971d4242eda8c47c605:L9
reason: Evidence collected from the dispatched region is sufficient to answer the query about the seal management regulations.
---
[region 4] real_69c60971d4242eda8c47c605:L25 (ok)
collected 33 branch node(s); explicit roots=['
```

### 最终 evidence(new)

**[E1]** [§ 第七章	责任追究]
  第三十五条伪造、私刻集团公司法人章、财务专用章、银行预留印鉴章、领导签名章的，一经发现，对伪造、私刻责任方（单位、项目部、个人）处10万元罚款，并由集团公司组织调查组进行调查，根据情节轻重追究相关责任人的行政、经济责任，通报批评，依法追偿损失；涉嫌犯罪的，报请司法机关依法进行处理。
  第三十六条伪造、私刻集团公司机关部门章、二级单位章、项目部印章的，一经发现，对伪造、私刻责任方（单位、项目部、个人）处于6万元罚款，并由集团公司组织调查组进行调查，根据情节轻重追究相关责任人的行政、经济责任，通报批评，依法追偿损失。涉嫌犯罪的，报请司法机关依法进行处理。
  第四十一条有印章使用审批权限的其他管理人员，超越审批权限使用印章，造成经济损失及不良后果的，由集团公司党委组织部、监察审计部按《管理人员责任追究暂行规定》追究其相关责任。
  第四十二条印章责任管理单位、监管部门未认真履行印章管理、检查监督、封口管理等职责，发生伪造、私刻印章等情节严重，或造成经济损失及不良影响的，对管理责任人按集团公司《管理人员责任追究暂行规定》追究相关责任。

- retrieved_nodes: L110, L111, L112, L116, L117


---

