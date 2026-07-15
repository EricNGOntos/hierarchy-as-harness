# Map-Nav 运行报告

- generated_at: `2026-07-15T17:43:26`
- env: EMBEDDING_MODEL=`text-embedding-v3` · NAV_MAP_MODE=`1` · enable_recursive_dispatch=`False` · map_char_limit=`5000` · max_steps=`8` · navigate_max_steps=`8`
- 汇总: 5 case · PASS 5/5 · mean gold_recall 0.692

| inspect_id | task_type | gold_recall | evidence_chars | steps |
|---|---|---:|---:|---:|
| real_69cb12d0919452cda2225a0b_scope_collection_auto_0076 | scope_collection | 0.12 | 499 | 2 |
| latest_clean_multi_0010 | multi_hop | 0.50 | 487 | 4 |
| real_69c60974d4242eda8c47c615_scope_collection_auto_0030 | scope_collection | 0.83 | 495 | 3 |
| latest_clean_multi_0032 | multi_hop | 1.00 | 405 | 2 |
| latest_clean_multi_0048 | multi_hop | 1.00 | 491 | 4 |

---

## real_69cb12d0919452cda2225a0b_scope_collection_auto_0076  ·  scope_collection

- **Query:** 列出办理《跨区域涉税事项备案》时需注意的所有事项要点。
- **Doc:** `real_69cb12d0919452cda2225a0b`
- **Gold nodes:** L141, L142, L143, L144, L145, L146, L147, L148

### 结果得分 — **PASS** (new gold_recall=0.12)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.12 |
| evidence_chars | 500 | 499 |
| n_retrieved_nodes | 6 | 8 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 1.32 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L141` | ❌ | False | False |
| `L142` | ❌ | False | False |
| `L143` | ❌ | False | False |
| `L144` | ❌ | False | False |
| `L145` | ✅ | True | False |
| `L146` | ❌ | False | False |
| `L147` | ❌ | False | False |
| `L148` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C6` collect L128 (depth=0) · multi→[L128, L130, L131, L134, L135, L136, L137, L139, L140, L144, L145, L146, L148, L149, L150, L154, L155, L157] · +18
  - reason: Collect all leaf nodes under section 3.2.4 detailing cross-regional tax filing requirements and precautions.
- `F1` finish - (depth=0)
  - reason: Evidence G1 fully covers all key points for cross-regional tax filing requirements.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C6` | `L128` | L128, L130, L131, L134, L135, L136, L137, L139, L140, L144, L145, L146, L148, L149, L150, L154, L155, L157 | 18 | 18 | - | ✅ |

**水合告警:**
- step 1 整枝水合含 14 个非 gold 叶 (与 gold 争抢 evidence 预算)。

### 最终 evidence(new)

**[E1]** [§ **3.2.4** 《跨区域涉税事项报告》管理]
  办理跨区域涉税事项备案需注意事项：
  - 2）项目地址：不是甲方机构所在地，应填写项目所在地省、市、区（县）。（注意：
  - 5）《跨区域涉税事项报告》自办理之日起 30 日内在项目所在地税务机关报验，到
  《跨区域涉税事项报告》办理完成后 30 天之内，项目部应向工程项目所在地主管税 务机关进行报验登记，并按照《中华人民共和国税收征收管理办法》及其实施细则的有 关规定进行经营和纳税。
  在项目所在地税务机关报验时，需提供以下资料：
  - 《跨区域涉税事项报告》初次办理有效期为 360 天，到期日项目未完工的，应于到
  - 5）《跨区域涉税事项报告》所属期间，所有发票复印件以及完税证复印件。
  项目部办理完跨区域涉税事项备案之后，应当留存电子版备案表，并建立《跨区域 涉税事项备案台账》（SJSYJ-CWGL-FJ-005），台账应包括建设单位名称、项目名称、 合同金额、开具日期、到期日期、编号、责任人、核销时间、核销金额，以及已交增值 税、企业所得税、城建税、教育费、地方教育费、水利基金、印花税金额。

- retrieved_nodes: L128, L130, L134, L137, L139, L145⭐, L154, L157


---

## latest_clean_multi_0010  ·  multi_hop

- **Query:** 根据《线上学习平台学习管理方案（修订）》中“十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订）”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c6095ed4242eda8c47c5b2`
- **Gold nodes:** L2, L3

### 结果得分 — **PASS** (new gold_recall=0.50)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.50 |
| evidence_chars | 210 | 487 |
| n_retrieved_nodes | 2 | 11 |
| trajectory_steps | - | 4 |
| elapsed_sec | - | 0.14 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L2` | ❌ | False | False |
| `L3` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C4` collect L4 (depth=0) · multi→[L4, L7] · +2
  - reason: Collect adjacent sections on management structure and office duties to answer the query.
- `C10` collect L14 (depth=0) · →L14 · +1
  - reason: Collect C10 to obtain the second adjacent evidence point regarding employee learning supervision and offline training organization.
- `C1` collect L1 (depth=0) · →L1 · +36 · PURGED後代×3
  - reason: Collect full document to find adjacent evidence sections for the query.
- `F1` finish - (depth=0)
  - reason: Evidence covers management structure and unit responsibilities as requested.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C4` | `L4` | L4, L7 | 2 | 2 | - | ✅ |
| 2 | `C10` | `L14` | - | 1 | 1 | - | ✅ |
| 3 | `C1` | `L1` | - | 36 | 36 | 3 | ✅ |

**水合告警:**
- step 3 `C1` 收父节点 `L1` 时 **purge 掉 3 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。

### 最终 evidence(new)

**[E1]** [§ 一、管理机构及其职责]
  线上学习平台主要为除十一在线各研修班以外一般员工提供学习资源。十一在线平台中心为其最高管理机构负责把握学习方向、整合学习资源，各专家组负责学习内容开发，十一在线平台中心办公室主要负责日常运营管理，集团公司机关各部室及各二级单位负责组织本部室及本单位员工参加学习。各级机构及其职责具体如下：
  （ 一）十一在线平台中心：负责课程体系设计、课程开发计划审批、课程考核标准设定、平台建设费用审批等相关事宜。
  （ 二）各专家组：负责各领域内员工培训需求征集，教材、课件及习题开发，课件修改、适时更新、审核，业务答疑，题库组建等工作，集团对口业务部门负责人为各专业课程开发责任人，统筹推进本业务系统课程开发工作。
  （ 三）十一在线平台中心办公室：负责线上学习平台搭建，维护平台基本信息，监督各专家组及相关部门及时更新学习内容，组织各专家组和二级单位平台管理员进行平台管理培训，并对各专家组课程开发情况、学员学习情况进行跟
  踪和定期调研，反馈十一在线平台中心。

**[E2]** [§ 4.其他事项]
（ 4）其他未尽事宜，另行规定。

- retrieved_nodes: L1, L3⭐, L4, L5, L6, L7, L8, L32, L38, L47, L51


---

## real_69c60974d4242eda8c47c615_scope_collection_auto_0030  ·  scope_collection

- **Query:** 列出重大事故隐患治理方案必须包含的所有内容要素。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L94, L95, L96, L97, L98, L99

### 结果得分 — **PASS** (new gold_recall=0.83)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.83 |
| evidence_chars | 500 | 495 |
| n_retrieved_nodes | 12 | 9 |
| trajectory_steps | - | 3 |
| elapsed_sec | - | 1.7 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L94` | ✅ | True | False |
| `L95` | ✅ | True | False |
| `L96` | ❌ | False | False |
| `L97` | ✅ | True | False |
| `L98` | ✅ | True | False |
| `L99` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C20` collect L93 (depth=0) · multi→[L93, L98] · +2
  - reason: Collect specific content elements of major accident hazard governance plans from section 2.4.4.
- `C19` collect L92 (depth=0) · →L92 · +11 · PURGED後代×2
  - reason: Collect section 2.4.4 to retrieve the full list of required elements for major accident hazard governance plans.
- `F1` finish - (depth=0)
  - reason: Assembled evidence G1 fully lists all required elements for major accident hazard governance plans.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C20` | `L93` | L93, L98 | 2 | 2 | - | ✅ |
| 2 | `C19` | `L92` | - | 11 | 11 | 2 | ✅ |

**水合告警:**
- step 1 整枝水合含 1 个非 gold 叶 (与 gold 争抢 evidence 预算)。
- step 2 `C19` 收父节点 `L92` 时 **purge 掉 2 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。

### 最终 evidence(new)

**[E1]** [§ 2.4.4 重大事故隐患整改、复查、销项]
  2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。
  2.4.6 各项目部应当加强对自然灾害的预防。对于因自然灾害可能导致事故灾难的隐患，应当按照有关法律、法规、标准和本制度的要求排查治理，采取可靠的预防措施，制定应急预案。在接到有关自然灾害预报时，应当及时向有关人员发出预警通知；发生自然灾害可能危及施工和人员安全的情况时，应当采取撤离人员、停止作业、加强监测等安全措施，并及时向当地人民政府有关部门报告。
  对重大事故隐患，由被检查项目负责整改，整改应制定事故隐患治理方案，该方案由项目经理组织制定和实施。方案包括以下内容：
  1、治理的目标和任务；
  2、采取的方法和措施；
  4、负责治理的机构和人员；
  5、治理的时限和要求；
  6、安全措施和应急预案。

- retrieved_nodes: L92, L102, L103, L93, L94⭐, L95⭐, L97⭐, L98⭐, L99⭐


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
| trajectory_steps | - | 2 |
| elapsed_sec | - | 0.1 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L34` | ✅ | True | False |
| `L35` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C24` collect L33 (depth=0) · multi→[L33, L34, L37] · +4
  - reason: Collect adjacent sections under 'Course Development Management' to extract key points as requested.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains the required adjacent points on course development management.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C24` | `L33` | L33, L34, L37 | 4 | 6 | - | ✅ |

**水合告警:**
- step 1 整枝水合含 2 个非 gold 叶 (与 gold 争抢 evidence 预算)。

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
  - reason: Dispatch Chapter 2 to retrieve details on scope and types for the query.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L6 (depth=1) · →L6 · +18
      - reason: Collect Chapter 2 to cover scope, types, and restrictions as requested.
    - `F1` finish - (depth=1)
      - reason: Collected section L6 contains the required content from Chapter 2. Ready to synthesize the two adjacent points.
- `F1` finish - (depth=0)
  - reason: Evidence G1 and G2 cover Chapter 2 scope and types as requested. Ready to synthesize adjacent points.

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
reason: Collected section L6 contains the required content from Chapter 2. Ready to synthesize the two adjacent points.
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

