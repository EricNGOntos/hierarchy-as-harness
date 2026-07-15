# Map-Nav 运行报告

- generated_at: `2026-07-15T16:13:55`
- env: EMBEDDING_MODEL=`text-embedding-v3` · NAV_MAP_MODE=`1` · enable_recursive_dispatch=`False` · map_char_limit=`5000` · max_steps=`8` · navigate_max_steps=`8`
- 汇总: 5 case · PASS 4/5 · mean gold_recall 0.700

| inspect_id | task_type | gold_recall | evidence_chars | steps |
|---|---|---:|---:|---:|
| real_69cb12d0919452cda2225a0b_scope_collection_auto_0076 | scope_collection | 0.00 | 401 | 5 |
| real_69c60974d4242eda8c47c615_scope_collection_auto_0030 | scope_collection | 1.00 | 329 | 4 |
| latest_clean_multi_0032 | multi_hop | 1.00 | 405 | 4 |
| latest_clean_multi_0048 | multi_hop | 1.00 | 491 | 4 |
| latest_clean_multi_0010 | multi_hop | 0.50 | 498 | 4 |

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
| trajectory_steps | - | 5 |
| elapsed_sec | - | 1.39 |

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
    - `C4` collect L128 (depth=1) · →L128 · +1
      - reason: Collects the section listing all key points for handling cross-regional tax filing.
    - `C1` collect L124 (depth=1) · multi→[L124, L125, L127, L130, L134, L136, L137, L139, L140, L145, L148, L149, L150, L154, L155, L157] · +33 · PURGED後代×1
      - reason: Collect all remaining sections under C1 to gather complete requirements for cross-regional tax filing.
    - `F1` finish - (depth=1)
      - reason: Collected sections L124 and L128 contain the required points for cross-regional tax filing. Ready to finish.
- `F1` finish - (depth=0)
  - reason: Evidence G1 fully covers all required points for cross-regional tax filing procedures.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C4` | `L128` | - | 1 | 1 | - | ✅ |
| 2 | `C1` | `L124` | L124, L125, L127, L130, L134, L136, L137, L139, L140, L145, L148, L149, L150, L154, L155, L157 | 33 | 48 | 1 | ✅ |

**水合告警:**
- step 2 `C1` 收父节点 `L124` 时 **purge 掉 1 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。
- step 2 整枝水合含 14 个非 gold 叶 (与 gold 争抢 evidence 预算)。

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69cb12d0919452cda2225a0b:L124 (ok)
collected 34 branch node(s); explicit roots=['real_69cb12d0919452cda2225a0b:L128', 'real_69cb12d0919452cda2225a0b:L124']
collected: real_69cb12d0919452cda2225a0b:L124, real_69cb12d0919452cda2225a0b:L125, real_69cb12d0919452cda2225a0b:L126, real_69cb12d0919452cda2225a0b:L127, real_69cb12d0919452cda2225a0b:L128, real_69cb12d0919452cda2225a0b:L129, real_69cb12d0919452cda2225a0b:L130, real_69cb12d0919452cda2225a0b:L131, real_69cb12d0919452cda2225a0b:L132, real_69cb12d0919452cda2225a0b:L133, real_69cb12d0919452cda2225a0b:L134, real_69cb12d0919452cda2225a0b:L135, real_69cb12d0919452cda2225a0b:L136, real_69cb12d0919452cda2225a0b:L137, real_69cb12d0919452cda2225a0b:L138, real_69cb12d0919452cda2225a0b:L139, real_69cb12d0919452cda2225a0b:L140, real_69cb12d0919452cda2225a0b:L141, real_69cb12d0919452cda2225a0b:L142, real_69cb12d0919452cda2225a0b:L143
reason: Collected sections L124 and L128 contain the required points for cross-regional tax filing. Ready to finish.
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

## real_69c60974d4242eda8c47c615_scope_collection_auto_0030  ·  scope_collection

- **Query:** 列出重大事故隐患治理方案必须包含的所有内容要素。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L94, L95, L96, L97, L98, L99

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 329 |
| n_retrieved_nodes | 12 | 9 |
| trajectory_steps | - | 4 |
| elapsed_sec | - | 1.3 |

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
    - `C1` collect L92 (depth=1) · multi→[L92, L93, L94, L95, L96, L97, L98, L99] · +11
      - reason: Collect the section defining the major accident hazard governance plan and its required content elements.
    - `F1` finish - (depth=1)
      - reason: Collected section L92 contains the required elements for major accident hazard governance plans.
- `F1` finish - (depth=0)
  - reason: Evidence G1 fully lists all required elements for major accident hazard governance plans.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L92` | L92, L93, L94, L95, L96, L97, L98, L99 | 11 | 18 | - | ✅ |

**水合告警:**
- step 1 整枝水合含 2 个非 gold 叶 (与 gold 争抢 evidence 预算)。

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60974d4242eda8c47c615:L92 (ok)
collected 12 branch node(s); explicit roots=['real_69c60974d4242eda8c47c615:L92']
collected: real_69c60974d4242eda8c47c615:L100, real_69c60974d4242eda8c47c615:L101, real_69c60974d4242eda8c47c615:L102, real_69c60974d4242eda8c47c615:L103, real_69c60974d4242eda8c47c615:L92, real_69c60974d4242eda8c47c615:L93, real_69c60974d4242eda8c47c615:L94, real_69c60974d4242eda8c47c615:L95, real_69c60974d4242eda8c47c615:L96, real_69c60974d4242eda8c47c615:L97, real_69c60974d4242eda8c47c615:L98, real_69c60974d4242eda8c47c615:L99
reason: Collected section L92 contains the required elements for major accident hazard governance plans.
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

- retrieved_nodes: L92, L102, L93, L94⭐, L95⭐, L96⭐, L97⭐, L98⭐, L99⭐


---

## latest_clean_multi_0032  ·  multi_hop

- **Query:** 根据《线上学习平台学习管理方案（修订）》中“（ 一）课程开发管理”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c6095ed4242eda8c47c5b2`
- **Gold nodes:** L34, L35

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 142 | 405 |
| n_retrieved_nodes | 2 | 5 |
| trajectory_steps | - | 4 |
| elapsed_sec | - | 0.11 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L34` | ✅ | True | False |
| `L35` | ✅ | True | False |

### 决策 TRACE(因果序)

- `D10` dispatch L33 (depth=0) · regions=[L33] · child_reports=1
  - reason: Dispatch to 'Course Development Management' section to find adjacent evidence points.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L33 (depth=1) · multi→[L33, L34, L35] · +4
      - reason: Collect adjacent sections C2 (Course Development) and C3 (Courseware Review) under 'Course Development Management' to answer the query.
    - `F1` finish - (depth=1)
      - reason: The current scope L33 contains the relevant section on course development management. No further collection is needed as the evidence is sufficient to address the query about adjacent points.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains the required adjacent points on course development management: 1. Course Development, 2. Review, 3. Upload, and 4. Remuneration.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L33` | L33, L34, L35 | 4 | 6 | - | ✅ |

**水合告警:**
- step 1 整枝水合含 1 个非 gold 叶 (与 gold 争抢 evidence 预算)。

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c6095ed4242eda8c47c5b2:L33 (ok)
collected 5 branch node(s); explicit roots=['real_69c6095ed4242eda8c47c5b2:L33']
collected: real_69c6095ed4242eda8c47c5b2:L33, real_69c6095ed4242eda8c47c5b2:L34, real_69c6095ed4242eda8c47c5b2:L35, real_69c6095ed4242eda8c47c5b2:L36, real_69c6095ed4242eda8c47c5b2:L37
reason: The current scope L33 contains the relevant section on course development management. No further collection is needed as the evidence is sufficient to address the query about adjacent points.
---
=== End Investigate ===
```

### 最终 evidence(new)

**[E1]** [§ （ 一）课程开发管理]
  1.课程开发。课程开发依托专家组、各业务线要从有利于组织目标达成、员工履职能力提升等方面，本着“简单、实用、明了”原则进行课程开发。各专家组、各部门应按年度既定课程开发计划，督促、跟进课程开发负责人按时完成课件开发任务。计划外课程开发须明确开发课程名称、学习对象等，经各专家组审核后开发，并向平台中心办公室备案。
  2.课件评审。课件开发完成后，根据课程类别提交各专家组审核，专家组从课件选材、专业度、实用性等方面对课件进行评审，课程评审管理参照《十一在线——员工赋能一体化平台管理办法》执行。
  3.课件上传。评审通过后，平台管理员需在课程计划提交截止时间5 日内完成课件上传和必修岗位指派。计划外开发的课程经各专家组评审通过后5 日完成上传和必修岗位指派。
  4.课酬兑现。开发的课程根据《十一在线——员工赋能一体化平台管理办法》相关规定标准兑现相应课酬。

- retrieved_nodes: L33, L34⭐, L35⭐, L36, L37


---

## latest_clean_multi_0048  ·  multi_hop

- **Query:** 根据《集团公司对外捐赠管理办法（修订版）》中“第二章 对外捐赠的范围及类型”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60970d4242eda8c47c5fd`
- **Gold nodes:** L7, L8

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 495 | 491 |
| n_retrieved_nodes | 11 | 16 |
| trajectory_steps | - | 4 |
| elapsed_sec | - | 0.11 |

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
      - reason: Collect Chapter 2 to cover scope, types, and restrictions as requested.
    - `F1` finish - (depth=1)
      - reason: Collected section L6 contains the required content from Chapter 2. Ready to summarize points.
- `F1` finish - (depth=0)
  - reason: Evidence collected covers Chapter 2 scope and types. G1 defines scope/types, G2 details asset restrictions.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L6` | - | 18 | 18 | - | ✅ |

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60970d4242eda8c47c5fd:L6 (ok)
collected 21 branch node(s); explicit roots=['real_69c60970d4242eda8c47c5fd:L6']
collected: real_69c60970d4242eda8c47c5fd:L10, real_69c60970d4242eda8c47c5fd:L11, real_69c60970d4242eda8c47c5fd:L12, real_69c60970d4242eda8c47c5fd:L13, real_69c60970d4242eda8c47c5fd:L14, real_69c60970d4242eda8c47c5fd:L15, real_69c60970d4242eda8c47c5fd:L16, real_69c60970d4242eda8c47c5fd:L17, real_69c60970d4242eda8c47c5fd:L18, real_69c60970d4242eda8c47c5fd:L19, real_69c60970d4242eda8c47c5fd:L20, real_69c60970d4242eda8c47c5fd:L21, real_69c60970d4242eda8c47c5fd:L22, real_69c60970d4242eda8c47c5fd:L23, real_69c60970d4242eda8c47c5fd:L24, real_69c60970d4242eda8c47c5fd:L25, real_69c60970d4242eda8c47c5fd:L26, real_69c60970d4242eda8c47c5fd:L6, real_69c60970d4242eda8c47c5fd:L7, real_69c60970d4242eda8c47c5fd:L8
reason: Collected section L6 contains the required content from Chapter 2. Ready to summarize points.
---
=== End Investigate ===
```

### 最终 evidence(new)

**[E1]** [§ 第二章  对外捐赠的范围及类型]
  第三条本办法所称的“对外捐赠”，是指集团公司及所属各单位自愿将有处分权的合法财产无偿赠送给合法的受赠人（包含无偿捐赠工程），用于与捐赠人生产经营活动没有直接关系的公益事业的行为。
  集团公司所属非法人分支机构、项目部不得以分公司、项目部名义对外捐赠，不得将企业拥有的财产以个人名义对外捐赠。
  对外捐赠原则上以集团公司（陕西建工第十一建设集团有限公司）名义进行捐赠，独立法人单位可根据实际需要以本单位名义进行捐赠。

**[E2]** [§ 第五条  对外捐赠的范围]
  用于对外捐赠的资产应当权属清晰，应为集团公司有权处分的合法财产，包括现金资产和实物资产等。
  不具处分权的财产或者不合格产品不得用于对外捐赠。下列资产不得用于对外捐赠：
  （一）生产经营用的主要固定资产；
  （二）持有的股权和债权；
  （三）国家特准储备物资；
  （四）国家财政拨款；
  （五）受代管财产；
  （六）设定担保物权的财产；
  （七）权属关系不清的财产；
  （八）变质、残损、过期报废的商品物资；
  （九）企业拥有的知识产权。

- retrieved_nodes: L6, L7⭐, L8⭐, L9, L15, L16, L17, L18, L19, L20, L21, L22, L23, L24, L25, L26


---

## latest_clean_multi_0010  ·  multi_hop

- **Query:** 根据《线上学习平台学习管理方案（修订）》中“十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订）”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c6095ed4242eda8c47c5b2`
- **Gold nodes:** L2, L3

### 结果得分 — **PASS** (new gold_recall=0.50)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.50 |
| evidence_chars | 210 | 498 |
| n_retrieved_nodes | 2 | 12 |
| trajectory_steps | - | 4 |
| elapsed_sec | - | 0.1 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L2` | ✅ | True | False |
| `L3` | ❌ | False | False |

### 决策 TRACE(因果序)

- `D1` dispatch L1 (depth=0) · regions=[L1] · child_reports=1
  - reason: Dispatch main section to gather detailed evidence for the query.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L1 (depth=1) · →L1 · +36
      - reason: Collect main document to access full content for multi-hop analysis.
    - `F1` finish - (depth=1)
      - reason: Only one section collected; insufficient evidence to compare two adjacent points as requested.
- `F1` finish - (depth=0)
  - reason: Collected evidence contains the document title and relevant adjacent sections on platform management and other matters.

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

**[E1]** [§ 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订）]
为进一步深化学习型组织建设，整合学习资源，传播最佳实践，有效助力员工工作技能提升和绩效改善。为进一步强化学习效果，规范线上学习管理，特制订本方案。

**[E2]** [§ 4.其他事项]
  （ 1）各管理员在线上学习平台创建线下培训时，应结合本公司培训计划和实际业务需求创建，创建过程中，做好签到设置、学员管理和指派设置，根据实际设置培训学时时长。
  （ 2）线下培训结束后，及时留存培训资料，培训资料包括培训方案、培训签到表、培训教材、培训记录（如照片、学习笔记等）等。
  （ 3 ）十一在线平台中心后期将根据后台创建的线下培训记录，不定期抽查相关学习资料，保证学习的真实性和有效性。如发现有不实情形，获得该门线下培训学时的学员，学时为不合格，并给予相关人员通报。
  （ 4）其他未尽事宜，另行规定。
  附件：xxx 年度线上课程开发计划汇总表（针对非研修班涉及岗位）

**[E3]** [§ （ 一）课程开发管理]
4.课酬兑现。开发的课程根据《十一在线——员工赋能一体化平台管理办法》相关规定标准兑现相应课酬。

- retrieved_nodes: L1, L2⭐, L32, L38, L47, L48, L49, L50, L51, L52, L33, L37


---

