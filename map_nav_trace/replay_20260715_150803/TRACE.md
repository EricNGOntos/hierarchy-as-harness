# Map-Nav Trace Replay (recursive DISPATCH)

- generated_at: `2026-07-15T15:08:03`
- nav_map_mode: `1`
- enable_recursive_dispatch: `False`
- embedding: `text-embedding-v3`

## latest_clean_multi_0010 (multi_hop)

**Query:** 根据《线上学习平台学习管理方案（修订）》中“十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订）”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c6095ed4242eda8c47c5b2`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 210 | 476 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 2 | 12 |
| trajectory_steps | n/a | 4 |

### Gold node hits (new)

- `real_69c6095ed4242eda8c47c5b2:L2` [MISS] retrieved=False in_text=False
- `real_69c6095ed4242eda8c47c5b2:L3` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6095ed4242eda8c47c5b2:L1` scope=`real_69c6095ed4242eda8c47c5b2:L1` depth=`1`
- reason: Collect main document to access full content for multi-hop analysis.
- collect_section_ids: ['real_69c6095ed4242eda8c47c5b2:L1']
- collect added=36 hits=36 branch_selected=True collect_full=True
- legal_actions (17):
  - C1 | COLLECT | real_69c6095ed4242eda8c47c5b2:L1 | 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） | score=0.0722
  - C2 | COLLECT | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0697
  - C3 | COLLECT | real_69c6095ed4242eda8c47c5b2:L4 | 线上学习平台主要为除十一在线各研修班以外一般员工提供学习资源。十一在线平台中心为其最高管理机构负责把握学习方向、整合学习资源，各专家组负责学习内容开发，十一在线平台中心办公室主要负责日常运营管理，集团公司机关各部室及各二级单位负责组织本部室及本单位员工参加学习。各级机构及其职责具体如下： | score=0.0691
  - C4 | COLLECT | real_69c6095ed4242eda8c47c5b2:L7 | （ 三）十一在线平台中心办公室：负责线上学习平台搭建，维护平台基本信息，监督各专家组及相关部门及时更新学习内容，组织各专家组和二级单位平台管理员进行平台管理培训，并对各专家组课程开发情况、学员学习情况进行跟 | score=0.0646
  - C5 | COLLECT | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0697
  - C6 | COLLECT | real_69c6095ed4242eda8c47c5b2:L14 | 2.督促本部室及本单位员工开展在线学习，并结合线上学习内容和业务实际，组织本部室及本单位开展线下探讨、分享、集中培训等。 | score=0.0697
  - C7 | COLLECT | real_69c6095ed4242eda8c47c5b2:L17 | 二、课程及指派管理 | score=0.0641
  - C8 | COLLECT | real_69c6095ed4242eda8c47c5b2:L18 | （ 一）课程类别 | score=0.0641
  - C9 | COLLECT | real_69c6095ed4242eda8c47c5b2:L20 | 明确课程名称、课程类别、必修岗位、课程开发负责人等信息（见附件），提交十一在线平台中心审批后按计划开发。 | score=0.0641
  - C10 | COLLECT | real_69c6095ed4242eda8c47c5b2:L28 | （ 三）指派管理 | score=0.0637
  - C11 | COLLECT | real_69c6095ed4242eda8c47c5b2:L31 | 2.各研修班课程在授课结束后由各研修管理员同步上传线上平台相应课程模块，需要纳入相关岗位必修的，由管理员指派给相关岗位作为必修课程。 | score=0.0637
  - C12 | COLLECT | real_69c6095ed4242eda8c47c5b2:L32 | 三、考核管理及结果应用 | score=0.0722
  - C13 | COLLECT | real_69c6095ed4242eda8c47c5b2:L33 | （ 一）课程开发管理 | score=0.0704
  - C14 | COLLECT | real_69c6095ed4242eda8c47c5b2:L37 | 4.课酬兑现。开发的课程根据《十一在线——员工赋能一体化平台管理办法》相关规定标准兑现相应课酬。 | score=0.0704
  - C15 | COLLECT | real_69c6095ed4242eda8c47c5b2:L38 | （ 二 ）学员学习考核管理 | score=0.0722
  - C16 | COLLECT | real_69c6095ed4242eda8c47c5b2:L47 | 4.其他事项 | score=0.0722
- projection_chars: 3577

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c6095ed4242eda8c47c5b2:L1` depth=`1`
- reason: Only one section collected; insufficient evidence to compare two adjacent points as requested.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 188

**Step 3** `nav_dispatch`  id=`D1` kind=`dispatch` section=`real_69c6095ed4242eda8c47c5b2:L1` scope=`None` depth=`0`
- reason: Dispatch main section to gather detailed evidence for the query.
- dispatch_regions: ['real_69c6095ed4242eda8c47c5b2:L1']
- child_reports=1 skipped=0
- legal_actions (46):
  - C1 | COLLECT | real_69c6095ed4242eda8c47c5b2:L1 | 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） | score=0.0722
  - D1 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L1 | 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） | score=0.0722
  - C2 | COLLECT | real_69c6095ed4242eda8c47c5b2:L2 | 为进一步深化学习型组织建设，整合学习资源，传播最佳实践，有效助力员工工作技能提升和绩效改善。为进一步强化学习效果，规范线上学习管理，特制订本方案。 | score=0.0616
  - C3 | COLLECT | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0697
  - D2 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0697
  - C4 | COLLECT | real_69c6095ed4242eda8c47c5b2:L4 | 线上学习平台主要为除十一在线各研修班以外一般员工提供学习资源。十一在线平台中心为其最高管理机构负责把握学习方向、整合学习资源，各专家组负责学习内容开发，十一在线平台中心办公室主要负责日常运营管理，集团公司机关各部室及各二级单位负责组织本部室及本单位员工参加学习。各级机构及其职责具体如下： | score=0.0691
  - C5 | COLLECT | real_69c6095ed4242eda8c47c5b2:L5 | （ 一）十一在线平台中心：负责课程体系设计、课程开发计划审批、课程考核标准设定、平台建设费用审批等相关事宜。 | score=0.0587
  - C6 | COLLECT | real_69c6095ed4242eda8c47c5b2:L7 | （ 三）十一在线平台中心办公室：负责线上学习平台搭建，维护平台基本信息，监督各专家组及相关部门及时更新学习内容，组织各专家组和二级单位平台管理员进行平台管理培训，并对各专家组课程开发情况、学员学习情况进行跟 | score=0.0646
  - C7 | COLLECT | real_69c6095ed4242eda8c47c5b2:L8 | 踪和定期调研，反馈十一在线平台中心。 | score=0.0589
  - C8 | COLLECT | real_69c6095ed4242eda8c47c5b2:L9 | （ 四）平台管理员 | score=0.0599
  - D3 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L9 | （ 四）平台管理员 | score=0.0599
  - C9 | COLLECT | real_69c6095ed4242eda8c47c5b2:L11 | 2.各二级单位平台管理员：负责督促本单位各类课件指定人员在线学习，按时完成学习计划，并向各专家组及十一在线平台中心办公室反馈学习情况。 | score=0.0599
  - C10 | COLLECT | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0697
  - D4 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0697
  - C11 | COLLECT | real_69c6095ed4242eda8c47c5b2:L14 | 2.督促本部室及本单位员工开展在线学习，并结合线上学习内容和业务实际，组织本部室及本单位开展线下探讨、分享、集中培训等。 | score=0.0697
  - C12 | COLLECT | real_69c6095ed4242eda8c47c5b2:L15 | （ 六 ）学员 | score=0.0599
- projection_chars: 3379

**Step 4** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Only one section collected; insufficient evidence to compare two adjacent points as requested.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 171

### Subagent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c6095ed4242eda8c47c5b2:L1 (ok)
collected 52 branch node(s); explicit roots=['real_69c6095ed4242eda8c47c5b2:L1']
collected: real_69c6095ed4242eda8c47c5b2:L1, real_69c6095ed4242eda8c47c5b2:L10, real_69c6095ed4242eda8c47c5b2:L11, real_69c6095ed4242eda8c47c5b2:L12, real_69c6095ed4242eda8c47c5b2:L13, real_69c6095ed4242eda8c47c5b2:L14, real_69c6095ed4242eda8c47c5b2:L15, real_69c6095ed4242eda8c47c5b2:L16, real_69c6095ed4242eda8c47c5b2:L17, real_69c6095ed4242eda8c47c5b2:L18, real_69c6095ed4242eda8c47c5b2:L19, real_69c6095ed4242eda8c47c5b2:L2, real_69c6095ed4242eda8c47c5b2:L20, real_69c6095ed4242eda8c47c5b2:L21, real_69c6095ed4242eda8c47c5b2:L22, real_69c6095ed4242eda8c47c5b2:L23, real_69c6095ed4242eda8c47c5b2:L24, real_69c6095ed4242eda8c47c5b2:L25, real_69c6095ed4242eda8c47c5b2:L26, real_69c6095ed4242eda8c47c5b2:L27
reason: Only one section collected; insufficient evidence to compare two adjacent points as requested.
---
=== End Investigate ===
```

### Evidence text (new)

```
[E1]
[§ 4.其他事项]
  （ 1）各管理员在线上学习平台创建线下培训时，应结合本公司培训计划和实际业务需求创建，创建过程中，做好签到设置、学员管理和指派设置，根据实际设置培训学时时长。
  （ 2）线下培训结束后，及时留存培训资料，培训资料包括培训方案、培训签到表、培训教材、培训记录（如照片、学习笔记等）等。
  （ 3 ）十一在线平台中心后期将根据后台创建的线下培训记录，不定期抽查相关学习资料，保证学习的真实性和有效性。如发现有不实情形，获得该门线下培训学时的学员，学时为不合格，并给予相关人员通报。
  （ 4）其他未尽事宜，另行规定。
  附件：xxx 年度线上课程开发计划汇总表（针对非研修班涉及岗位）

[E2]
[§ （ 一）课程开发管理]
  2.课件评审。课件开发完成后，根据课程类别提交各专家组审核，专家组从课件选材、专业度、实用性等方面对课件进行评审，课程评审管理参照《十一在线——员工赋能一体化平台管理办法》执行。
  4.课酬兑现。开发的课程根据《十一在线——员工赋能一体化平台管理办法》相关规定标准兑现相应课酬。
```

### Evidence text (old)

```
[E1]
线上学习平台主要为除十一在线各研修班以外一般员工提供学习资源。十一在线平台中心为其最高管理机构负责把握学习方向、整合学习资源，各专家组负责学习内容开发，十一在线平台中心办公室主要负责日常运营管理，集团公司机关各部室及各二级单位负责组织本部室及本单位员工参加学习。各级机构及其职责具体如下：

[E2]
（ 一）十一在线平台中心：负责课程体系设计、课程开发计划审批、课程考核标准设定、平台建设费用审批等相关事宜。
```

## latest_clean_niche_0068 (niche_fact)

**Query:** 根据《陕西建工第十一建设集团有限公司印章管理办法（2020版）》中“陕西建工第十一建设集团有限公司印章管理办法（2020版）.docx”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60971d4242eda8c47c605`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 479 | 492 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 8 | 5 |
| trajectory_steps | n/a | 24 |

### Gold node hits (new)

- `real_69c60971d4242eda8c47c605:L2` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60971d4242eda8c47c605:L36` scope=`real_69c60971d4242eda8c47c605:L36` depth=`1`
- reason: Collecting Article 10 to retrieve the full regulations on seal usage scope.
- collect_section_ids: ['real_69c60971d4242eda8c47c605:L36']
- collect added=6 hits=6 branch_selected=True collect_full=True
- legal_actions (7):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0710
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L37 | （一）以本单位、部门名义向集团公司提出的工作计划、总结、统计报表等； | score=0.0412
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L38 | （二）集团公司内部各单位、部门之间业务及工作沟通资料； | score=0.0396
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L39 | （三）集团公司管理程序要求的会签、审核等资料； | score=0.0364
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L40 | （四）以本单位、部门名义发布的行政文件； | score=0.0324
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L41 | （五）集团公司内部专业分包合同签订； | score=0.0414
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L42 | （六）集团公司法人明确授权或者委托对外使用印章的事项。 | score=0.0710
- projection_chars: 1058

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60971d4242eda8c47c605:L36` depth=`1`
- reason: Evidence collected from the relevant section is sufficient to answer the query about the seal management regulations.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 189

**Step 3** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60971d4242eda8c47c605:L7` scope=`real_69c60971d4242eda8c47c605:L7` depth=`1`
- reason: Collect Chapter 2 to gather all regulations on seal carving and activation.
- collect_section_ids: ['real_69c60971d4242eda8c47c605:L7']
- collect added=17 hits=17 branch_selected=True collect_full=True
- legal_actions (16):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0641
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L8 | 第四条集团公司及下属单位各类印章的刻制必须履行相应审批手续。 | score=0.0426
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L9 | （一）集团公司机关各部门章，二级单位章，由集团办公室根据集团公司或上级有关部门批准成立该机构的文件制发。 | score=0.0641
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L10 | （二）集团公司法定代表人章、总会计师章根据任命文件由集团办公室安排刻制；集团领导个人签名章经本人同意后由集团办公室安排刻制。 | score=0.0476
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L11 | （三）集团公司财务专用章、银行预留印鉴章由集团公司办公室刻制。 | score=0.0322
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L12 | （四）集团公司项目部印章由集团公司办公室按照项目经理部成立文件刻制。 | score=0.0366
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L13 | （五）集团公司所属二级子公司法人章、法定代表人章、财务专用章，由该公司携带集团公司的批文和营业执照等资料，到注册所在地的公安机关申报、登记、制印；启用印章前，印模及印章管理人信息报集团公司办公室备案。 | score=0.0465
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L14 | （六）以其他单位名义承揽的项目，责任管理单位将项目印章领取后，应在三个工作日内交集团公司办公室备案，由集团公司办公室负责办理领用及交底手续。 | score=0.0357
  - C9 | COLLECT | real_69c60971d4242eda8c47c605:L15 | 第五条以下机构和部门原则上不予刻制印章。 | score=0.0313
  - C10 | COLLECT | real_69c60971d4242eda8c47c605:L16 | （一）集团公司各职能部门、生产经营单位、经济实体、项目经理部的下设机构。 | score=0.0366
  - C11 | COLLECT | real_69c60971d4242eda8c47c605:L19 | 确因工作需要刻制印章的，由用印单位或部门提出申请，详细说明印章的名称、用途、式样和规格，报集团公司主要领导批准后由办公室制发。 | score=0.0634
  - C12 | COLLECT | real_69c60971d4242eda8c47c605:L20 | 第六条印章刻制后，职能部门印章由指定的印章保管员领取印章，集团公司办公室负责进行交底；二级单位印章及所属项目部印章由二级单位办公室负责人领取印章，并负责对印章保管员进行交底。印章保管员应认真填写《印章保管人员信息备案登记表》，所在部门或单位负责人对印章保管员任职资格进行审核并签字确认。 | score=0.0434
  - C13 | COLLECT | real_69c60971d4242eda8c47c605:L21 | 第七条项目部印章在使用前，项目部应负责将集团公司办公室出具的印章启用文件报送建设单位、监理单位等相关方，以便业务往来确认。并在文件送达后一周内将回执返回集团公司办公室留存。 | score=0.0607
  - C14 | COLLECT | real_69c60971d4242eda8c47c605:L22 | 第八条印章使用过程中，如应变更或者因损坏需要重新刻制的，由使用单位或部门提出申请，经单位或部门负责人审批后，报集团公司办公室进行重新刻制。新印章需重新办理启用手续，原印章同时交回集团公司办公室。 | score=0.0484
  - C15 | COLLECT | real_69c60971d4242eda8c47c605:L23 | 第九条发生印章遗失，印章责任管理单位应在24小时内向集团公司和当地公安机关报告；在3个工作日内在省级以上报刊办理遗失声明，并向集团公司申请出具告知函，及时通知相关单位。印章遗失处理流程见附件。 | score=0.0534
  - C16 | COLLECT | real_69c60971d4242eda8c47c605:L24 | 印章责任管理单位应将印章遗失报告、遗失声明、告知函回复等相关资料在一月内报集团公司办公室，以备查考。 | score=0.0501
- projection_chars: 3240

**Step 4** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60971d4242eda8c47c605:L7` depth=`1`
- reason: Evidence collected is sufficient to answer the query regarding the seal management regulations.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 188

**Step 5** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60971d4242eda8c47c605:L1` scope=`real_69c60971d4242eda8c47c605:L1` depth=`1`
- reason: Collect Chapter 1 to gather all relevant regulations on seal management.
- collect_section_ids: ['real_69c60971d4242eda8c47c605:L1']
- collect added=5 hits=5 branch_selected=True collect_full=True
- legal_actions (6):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L1 | 第一章 总则 | score=0.0642
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L2 | 第一条为规范集团公司及下属单位印章管理工作，有效防范风险，保障经营管理活动的有序开展，特制定本办法。 | score=0.0642
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L3 | 第二条本办法所称集团公司印章包括：集团公司法人章、财务专用章、机关部门章，集团公司下属单位印章、项目部章等行使公司职权的法定名称章；集团公司法定代表人章、总会计师章等代表公司实施职务行为的印章。 | score=0.0631
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L4 | 第三条印章所刊名称，应为集团公司文件规定的法定名称。印章文字一般应使用宋体简体字。 | score=0.0503
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L5 | 集团公司法人章为圆形，直径为4.2CM，中央刊五角星，上环刊单位名称自左向右环排；部门章一律为圆形，直径为3.8CM，上刊集团名称自左向右环排，中央刊五角星，部门名称放在星下方作横排；二级单位公章一律为圆形，直径4.0CM，集团名称自左而右环排，二级单位名称放在星下方作横排。项目部章一律为圆形，直径4.0CM，集团名称和工程名称依次自左而右环排，“工程项目部”字样放在星下方作横排，名称应严格按“陕 | score=0.0540
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L6 | 印章名称、规格、标准等由集团公司办公室统一审核。 | score=0.0507
- projection_chars: 1420

**Step 6** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60971d4242eda8c47c605:L1` depth=`1`
- reason: The document root has been collected, providing the necessary context to answer the query about the seal management regulations.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 188

**Step 7** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60971d4242eda8c47c605:L25` scope=`real_69c60971d4242eda8c47c605:L25` depth=`1`
- reason: Collect Chapter 3 to gather all seal usage scope regulations.
- collect_section_ids: ['real_69c60971d4242eda8c47c605:L25']
- collect added=29 hits=29 branch_selected=True collect_full=True
- legal_actions (18):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0710
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L26 | 第九条 集团公司法人章使用范围 | score=0.0403
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L28 | 下列所有事项必须加盖集团公司法人章方为有效： | score=0.0403
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L33 | （五）以集团公司名义出具的各类法人授权委托书； | score=0.0379
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0710
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L37 | （一）以本单位、部门名义向集团公司提出的工作计划、总结、统计报表等； | score=0.0412
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L38 | （二）集团公司内部各单位、部门之间业务及工作沟通资料； | score=0.0396
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L41 | （五）集团公司内部专业分包合同签订； | score=0.0414
  - C9 | COLLECT | real_69c60971d4242eda8c47c605:L42 | （六）集团公司法人明确授权或者委托对外使用印章的事项。 | score=0.0710
  - C10 | COLLECT | real_69c60971d4242eda8c47c605:L43 | 第十一条 集团公司财务专用章使用范围 | score=0.0428
  - C11 | COLLECT | real_69c60971d4242eda8c47c605:L45 | （二）对外收取、支付款项时所用票据的确认盖章； | score=0.0428
  - C12 | COLLECT | real_69c60971d4242eda8c47c605:L48 | （五）涉及对外提供的有关务数据、资料、函件等。 | score=0.0378
  - C13 | COLLECT | real_69c60971d4242eda8c47c605:L49 | 第十二条 项目部印章使用范围 | score=0.0702
  - C14 | COLLECT | real_69c60971d4242eda8c47c605:L51 | （二）以项目部名义向建设单位、监理单位等出具的有关技术质量和安全生产的业务函件、工作联系单； | score=0.0420
  - C15 | COLLECT | real_69c60971d4242eda8c47c605:L54 | （五）项目部与两级机关部门业务沟通的相关内部资料，如开复工备案、专项方案、整改回复等资料； | score=0.0397
  - C16 | COLLECT | real_69c60971d4242eda8c47c605:L55 | （六）项目部行政后勤相关资料； | score=0.0378
- projection_chars: 2856

**Step 8** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60971d4242eda8c47c605:L25` depth=`1`
- reason: The relevant section has been collected. No further actions needed to answer the query.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 189

**Step 9** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60971d4242eda8c47c605:L49` scope=`real_69c60971d4242eda8c47c605:L49` depth=`1`
- reason: Collecting Article 12 to capture all regulations on project department seal usage scope.
- collect_section_ids: ['real_69c60971d4242eda8c47c605:L49']
- collect added=8 hits=8 branch_selected=True collect_full=True
- legal_actions (10):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L49 | 第十二条 项目部印章使用范围 | score=0.0702
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L50 | （一）项目施工过程中涉及的生产、技术、质量、安全管理等工程资料； | score=0.0373
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L51 | （二）以项目部名义向建设单位、监理单位等出具的有关技术质量和安全生产的业务函件、工作联系单； | score=0.0420
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L52 | （三）以项目部名义向各专业分包单位出具的有关技术质量和安全生产的检查通知单、隐患整改单、工作联系单等； | score=0.0354
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L53 | （四）项目施工变更资料及签证，项目施工计划及完成统计报表、进度款支付报审资料、认质认价单，与分包分供方各类结算单等； | score=0.0281
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L54 | （五）项目部与两级机关部门业务沟通的相关内部资料，如开复工备案、专项方案、整改回复等资料； | score=0.0397
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L55 | （六）项目部行政后勤相关资料； | score=0.0378
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L56 | （七）项目印章应在项目负责人审批后用印，用印内容不得违背施工合同要件内容。 | score=0.0521
  - C9 | COLLECT | real_69c60971d4242eda8c47c605:L57 | 第十四条集团公司法人章之外的其它印章，是公司法人授予的内部职能性标示。除公司法人授权或委托外，严禁用于签订合同、协议、借贷、担保、工程决算书等具有设定义务的实体行为。 | score=0.0702
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 1640

**Step 10** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60971d4242eda8c47c605:L49` depth=`1`
- reason: Collected section L49 contains the relevant regulations. No further collection needed.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 189

**Step 11** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60971d4242eda8c47c605:L91` scope=`real_69c60971d4242eda8c47c605:L91` depth=`1`
- reason: Collects the full section on seal management inspection and supervision requirements.
- collect_section_ids: ['real_69c60971d4242eda8c47c605:L91']
- collect added=9 hits=9 branch_selected=True collect_full=True
- legal_actions (11):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L91 | 第三十条 各印章管理责任单位应认真对印章管理使用情况进行检查监督： | score=0.0584
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L92 | （一）集团公司办公室应采用定期检查和不定期抽查等方式，对集团公司法人章、机关部门章、二级单位公章、项目章等进行每年不少于两次的检查；二级单位对其所属项目部应进行每年不少于两次的检查。 | score=0.0353
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L93 | 财务管理部每年应组织不少于两次对所辖印章的管理和使用情况进行专项监督检查。 | score=0.0269
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L94 | （二）检查监督内容应包括但不限于以下： | score=0.0327
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L95 | 1.印章保管人责任是否明确、用印交底是否清晰； | score=0.0464
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L96 | 2.印章启用函件是否已按规定送达至相关单位，有无业务往来确认； | score=0.0584
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L97 | 3.日常用印是否有审批，审批是否符合规定，用印登记是否齐全； | score=0.0415
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L98 | 4.印章管理使用是否按要求检查，检查是否有记录，对查出的问题是否已整改； | score=0.0416
  - C9 | COLLECT | real_69c60971d4242eda8c47c605:L99 | 5.登记用印的内容是否与用印的内容一致； | score=0.0560
  - C10 | COLLECT | real_69c60971d4242eda8c47c605:L100 | 6.印章保管人资格是否符合规定、是否履行上岗审批程序，实际印章保管人是否与备案一致。 | score=0.0542
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 1647

**Step 12** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60971d4242eda8c47c605:L91` depth=`1`
- reason: Collected section L91 contains the relevant regulations. Ready to answer query.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 189

**Step 13** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60971d4242eda8c47c605:L83` scope=`real_69c60971d4242eda8c47c605:L83` depth=`1`
- reason: Collects the full section on seal registration and record keeping (Article 26) to answer the query.
- collect_section_ids: ['real_69c60971d4242eda8c47c605:L83']
- collect added=7 hits=7 branch_selected=True collect_full=True
- legal_actions (9):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L83 | 第二十六条 用印登记及资料备存： | score=0.0602
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L84 | 印章保管人在用印前要认真审阅用印内容，检查审批程序，用印后要认真做好用印登记，重要资料做好留存。 | score=0.0315
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L85 | 登记项目包括：时间、用印编号、用印单位（部门）、用印事项说明、份数、经办人、审批人、审批编号、备注等。一般需要留存的材料有： | score=0.0334
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L86 | （一）重要文件、资料应保留有相应领导审批件、盖章文本； | score=0.0308
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L87 | （二）合同、协议书、授权书、法人委托书等应保留会签单、盖章文本。 | score=0.0263
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L88 | 第二十七条符合用印要求的，要规范加盖印章，盖印要端正、清晰、美观、完整，便于识别，印章文字不能歪斜或颠倒。 | score=0.0416
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L89 | 第二十八条所有印章一律不得在任何空白表格、证明、介绍信、白（稿）纸上加盖印章。确因工作需要的，应由用印单位或部门提出申请，经办公室报集团公司分管领导批准后用印。经办人员应跟踪用印文件使用全过程，事后向集团公司办公室提供用印文件复印件；未使用的，应及时退回集团公司办公室销毁。 | score=0.0602
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L90 | 第二十九条集团公司、各二级单位用印登记及备存资料应每年收集一次，由集团公司办公室负责保管。 | score=0.0297
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 1637

**Step 14** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60971d4242eda8c47c605:L83` depth=`1`
- reason: Collected section L83 contains the relevant regulations. Ready to answer query.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 189

**Step 15** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60971d4242eda8c47c605:L73` scope=`real_69c60971d4242eda8c47c605:L73` depth=`1`
- reason: Collect Chapter 5 to gather all relevant seal management regulations.
- collect_section_ids: ['real_69c60971d4242eda8c47c605:L73']
- collect added=24 hits=24 branch_selected=True collect_full=True
- legal_actions (18):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L73 | 第五章 印章管理 | score=0.0602
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L74 | 第二十条集团公司办公室是集团公司印章的管理部门，负责各类印章的刻制、启用、授权使用、停用、回收及缴销等手续的办理，负责检查各类印章使用情况，负责受理对违反本办法行为的检举、揭发，以及按照本办法对违规行为进行责任追究。 | score=0.0472
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L75 | 第二十一条集团公司所有印章实行责任管理。其中集团机关各部门主要负责人为部门印章第一管理责任人；二级单位行政主要负责人为本单位印章第一管理责任人，并为所属项目印章第一监管责任人；项目负责人为项目部印章的第一管理责任人；各印章保管人员为印章管理直接责任人，对集团公司负责。 | score=0.0541
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L77 | 第二十三条 集团公司所有印章管理实行严格的专人管理制，印章保管人员须具备以下条件： | score=0.0484
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L80 | （三）正式保管印章前，应接受集团公司或责任管理单位有关印章管理及使用的培训。 | score=0.0480
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L81 | 第二十四条集团公司各类印章保管人资格由其第一管理责任人审查，在集团公司办公室统一备案。 | score=0.0391
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L82 | 第二十五条印章保管人发生变更的，印章责任管理单位应填写《集团公司印章管理移交单》（见附件），办理印章移交手续。同时，在变更后三个工作日内报集团公司办公室更新备案。 | score=0.0484
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L83 | 第二十六条 用印登记及资料备存： | score=0.0602
  - C9 | COLLECT | real_69c60971d4242eda8c47c605:L88 | 第二十七条符合用印要求的，要规范加盖印章，盖印要端正、清晰、美观、完整，便于识别，印章文字不能歪斜或颠倒。 | score=0.0416
  - C10 | COLLECT | real_69c60971d4242eda8c47c605:L89 | 第二十八条所有印章一律不得在任何空白表格、证明、介绍信、白（稿）纸上加盖印章。确因工作需要的，应由用印单位或部门提出申请，经办公室报集团公司分管领导批准后用印。经办人员应跟踪用印文件使用全过程，事后向集团公司办公室提供用印文件复印件；未使用的，应及时退回集团公司办公室销毁。 | score=0.0602
  - C11 | COLLECT | real_69c60971d4242eda8c47c605:L91 | 第三十条 各印章管理责任单位应认真对印章管理使用情况进行检查监督： | score=0.0584
  - C12 | COLLECT | real_69c60971d4242eda8c47c605:L95 | 1.印章保管人责任是否明确、用印交底是否清晰； | score=0.0464
  - C13 | COLLECT | real_69c60971d4242eda8c47c605:L96 | 2.印章启用函件是否已按规定送达至相关单位，有无业务往来确认； | score=0.0584
  - C14 | COLLECT | real_69c60971d4242eda8c47c605:L97 | 3.日常用印是否有审批，审批是否符合规定，用印登记是否齐全； | score=0.0415
  - C15 | COLLECT | real_69c60971d4242eda8c47c605:L98 | 4.印章管理使用是否按要求检查，检查是否有记录，对查出的问题是否已整改； | score=0.0416
  - C16 | COLLECT | real_69c60971d4242eda8c47c605:L99 | 5.登记用印的内容是否与用印的内容一致； | score=0.0560
- projection_chars: 3407

**Step 16** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60971d4242eda8c47c605:L73` depth=`1`
- reason: Collected section L73 contains the relevant regulations. Ready to finish.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 189

**Step 17** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60971d4242eda8c47c605:L58` scope=`real_69c60971d4242eda8c47c605:L58` depth=`1`
- reason: Collect all sections under Chapter 4 to extract specific seal usage regulations and facts.
- collect_section_ids: ['real_69c60971d4242eda8c47c605:L58', 'real_69c60971d4242eda8c47c605:L59', 'real_69c60971d4242eda8c47c605:L60', 'real_69c60971d4242eda8c47c605:L61', 'real_69c60971d4242eda8c47c605:L62', 'real_69c60971d4242eda8c47c605:L63', 'real_69c60971d4242eda8c47c605:L64', 'real_69c60971d4242eda8c47c605:L65', 'real_69c60971d4242eda8c47c605:L66', 'real_69c60971d4242eda8c47c605:L67', 'real_69c60971d4242eda8c47c605:L68', 'real_69c60971d4242eda8c47c605:L69', 'real_69c60971d4242eda8c47c605:L70', 'real_69c60971d4242eda8c47c605:L71', 'real_69c60971d4242eda8c47c605:L72']
- collect added=14 hits=28 branch_selected=False collect_full=True
- legal_actions (16):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L58 | 第四章 用印审批程序 | score=0.0587
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L59 | 第十五条使用集团公司印章应履行批准手续，并严格按项登记，坚持以下原则办理： | score=0.0372
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L60 | 集团公司法人章用印审批程序： | score=0.0352
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L61 | （一）集团公司经营工作用印，按照《集团公司经营管理规定》的规定办理。 | score=0.0525
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L62 | （二）集团公司各部门以集团公司名义涉外的非正式文件，需经部门负责人审批，重要文件需经分管领导乃至主要领导审批，集团办公室登记后用印。 | score=0.0294
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L63 | （三）集团公司各部门以集团公司名义涉外的正式文件，按发文程序审批后用印。 | score=0.0310
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L64 | （四）一般业务来往资料及施工、技术、质量、安全生产等报审（报备、归档）资料，需经用印单位（部门）负责人审批，由业务主管部门到集团公司办公室登记后用印。重要业务来往资料，经用印单位（部门）负责人审批后，还需经集团公司分管领导乃至主要领导审批，由业务主管部门到集团公司办公室登记后用印。 | score=0.0296
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L65 | （五）各类合同、协议及法律诉讼文书，经部门负责人、集团公司分管领导审批，超出分管领导审批职权的重大事项，由集团公司主要领导审批集团，办公室登记后用印。 | score=0.0384
  - C9 | COLLECT | real_69c60971d4242eda8c47c605:L66 | （六）二级单位开展有关业务需要加盖集团公司印章，由用印单位发起审批，经用印单位主要负责人、集团公司业务管理部门、分管领导、主要领导审核同意，办公室登记后用印。 | score=0.0323
  - C10 | COLLECT | real_69c60971d4242eda8c47c605:L67 | （七）颁发证书、奖状等需加盖集团公司印章或钢印的，根据相关表彰文件用印，无文件由经办部门发起审批，经部门负责人、分管领导审批，办公室登记后用印。 | score=0.0587
  - C11 | COLLECT | real_69c60971d4242eda8c47c605:L68 | （八）使用印章要在办公室内，一般不允许将印章带出使用。确因工作需要外出用印，由申请单位（部门）发起审批，经部门负责人和集团办公室主任审核同意后，集团公司印章管理人员携带印章外出用印。如因特殊情况由非印章管理人员携带印章外出用印，需办理印章移交和交底手续，并做好用印登记。 | score=0.0409
  - C12 | COLLECT | real_69c60971d4242eda8c47c605:L69 | 第十六条二级单位应参照集团公司法人章审批程序，自行建立合理规范的用印审批程序。 | score=0.0451
  - C13 | COLLECT | real_69c60971d4242eda8c47c605:L70 | 第十七条机关各部门印章的用印由本部门主要负责人审批。 | score=0.0348
  - C14 | COLLECT | real_69c60971d4242eda8c47c605:L71 | 第十八条项目部用印经项目负责人审批后用印。 | score=0.0312
  - C15 | COLLECT | real_69c60971d4242eda8c47c605:L72 | 第十九条印章使用，应履行审批程序，做到手续完备，先审批后用印。对未按审批程序用印的，印章管理人员应拒绝用印。 | score=0.0330
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 2909

**Step 18** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60971d4242eda8c47c605:L58` depth=`1`
- reason: Collected section L58 contains the relevant regulations. No further collection needed.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 189

**Step 19** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60971d4242eda8c47c605:L110` scope=`real_69c60971d4242eda8c47c605:L110` depth=`1`
- reason: Collect all articles in Chapter 7 regarding seal management regulations and penalties.
- collect_section_ids: ['real_69c60971d4242eda8c47c605:L110', 'real_69c60971d4242eda8c47c605:L111', 'real_69c60971d4242eda8c47c605:L112', 'real_69c60971d4242eda8c47c605:L113', 'real_69c60971d4242eda8c47c605:L114', 'real_69c60971d4242eda8c47c605:L115', 'real_69c60971d4242eda8c47c605:L116', 'real_69c60971d4242eda8c47c605:L117']
- collect added=7 hits=14 branch_selected=False collect_full=True
- legal_actions (9):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L110 | 第七章	责任追究 | score=0.0602
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L111 | 第三十五条伪造、私刻集团公司法人章、财务专用章、银行预留印鉴章、领导签名章的，一经发现，对伪造、私刻责任方（单位、项目部、个人）处10万元罚款，并由集团公司组织调查组进行调查，根据情节轻重追究相关责任人的行政、经济责任，通报批评，依法追偿损失；涉嫌犯罪的，报请司法机关依法进行处理。 | score=0.0584
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L112 | 第三十六条伪造、私刻集团公司机关部门章、二级单位章、项目部印章的，一经发现，对伪造、私刻责任方（单位、项目部、个人）处于6万元罚款，并由集团公司组织调查组进行调查，根据情节轻重追究相关责任人的行政、经济责任，通报批评，依法追偿损失。涉嫌犯罪的，报请司法机关依法进行处理。 | score=0.0602
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L113 | 第三十八条印章保管人未认真履行印章管理职责的，由责任管理单位或部门酌情进行批评教育、警告，并不得评选或考核为A 级；因玩忽职守丢失印章、或给集团公司造成经济损失的，调离工作岗位，依法追偿损失。涉嫌犯罪的，依法移交司法机关处理。 | score=0.0440
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L114 | 第三十九条印章第一管理责任人违反本办法相关条款，由上级主管单位予以通报批评，责令整改，并不得评选或考核为A级；造成经济损失及不良后果的，将追究其相关管理责任。 | score=0.0409
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L115 | 第四十条违反本办法第十四条，对责任人通报批评，停职检查；由集团公司党委组织部、监察审计部按《管理人员责任追究暂行规定》追究其相关责任。 | score=0.0411
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L116 | 第四十一条有印章使用审批权限的其他管理人员，超越审批权限使用印章，造成经济损失及不良后果的，由集团公司党委组织部、监察审计部按《管理人员责任追究暂行规定》追究其相关责任。 | score=0.0566
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L117 | 第四十二条印章责任管理单位、监管部门未认真履行印章管理、检查监督、封口管理等职责，发生伪造、私刻印章等情节严重，或造成经济损失及不良影响的，对管理责任人按集团公司《管理人员责任追究暂行规定》追究相关责任。 | score=0.0533
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 2247

**Step 20** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60971d4242eda8c47c605:L110` depth=`1`
- reason: The required section has been collected and contains the relevant regulations. Ready to finish.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 190

**Step 21** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60971d4242eda8c47c605:L118` scope=`real_69c60971d4242eda8c47c605:L118` depth=`1`
- reason: Collect Chapter 8 to retrieve all relevant regulations and facts from the document.
- collect_section_ids: ['real_69c60971d4242eda8c47c605:L118']
- collect added=17 hits=17 branch_selected=True collect_full=True
- legal_actions (19):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L118 | 第八章 附则 | score=0.0649
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L119 | 第四十三条本办法自发布之日起施行，原规定同时废止。 | score=0.0351
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L120 | 第四十四条集团公司办公室为本办法主控部门，负责对本办法持续改进及解释。 | score=0.0293
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L121 | 第四十五条集团公司党委、纪委、工会、团委系统印章管理参照本办法执行。 | score=0.0454
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L122 | 印章管理交底单 | score=0.0350
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L123 | 本文档明确了集团及项目部印章的使用范围、管理要求、审批程序及登记规范，强调专人保管与严禁空白盖章，并要求负责人签字承诺遵守规定。 | score=0.0649
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L124 | 注：此表一式四份，集团公司办公室、责任管理单位/机关部门、项目负责人和印章保管人各执一份 | score=0.0434
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L125 | 印章管理移交单 | score=0.0358
  - C9 | COLLECT | real_69c60971d4242eda8c47c605:L126 | 移交时间： 年月日 | score=0.0300
  - C10 | COLLECT | real_69c60971d4242eda8c47c605:L127 | 注： | score=0.0349
  - C11 | COLLECT | real_69c60971d4242eda8c47c605:L128 | 1、印章移交前，责任管理单位及移交人必须对印章保管人进行管理培训及责任交底。 | score=0.0273
  - C12 | COLLECT | real_69c60971d4242eda8c47c605:L129 | 2、此表一式四份，集团公司办公室、责任管理单位、原印章保管人和现印章保管人各执一份。 | score=0.0351
  - C13 | COLLECT | real_69c60971d4242eda8c47c605:L130 | 3、二级单位及所属项目部印章管理移交批准人为责任管理单位负责人。 | score=0.0278
  - C14 | COLLECT | real_69c60971d4242eda8c47c605:L131 | 印章保管人员信息备案登记表 | score=0.0329
  - C15 | COLLECT | real_69c60971d4242eda8c47c605:L132 | 单位（部门）： | score=0.0329
  - C16 | COLLECT | real_69c60971d4242eda8c47c605:L133 | 印章使用登记表 | score=0.0356
- projection_chars: 2244

**Step 22** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60971d4242eda8c47c605:L118` depth=`1`
- reason: Collected section L118 contains the relevant regulations. No further collection needed.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 190

**Step 23** `nav_dispatch`  id=`D1` kind=`dispatch` section=`real_69c60971d4242eda8c47c605:L1` scope=`None` depth=`0`
- reason: Dispatch all chapters to gather comprehensive regulations on seal management, usage, and penalties.
- dispatch_regions: ['real_69c60971d4242eda8c47c605:L1', 'real_69c60971d4242eda8c47c605:L7', 'real_69c60971d4242eda8c47c605:L25', 'real_69c60971d4242eda8c47c605:L36', 'real_69c60971d4242eda8c47c605:L49', 'real_69c60971d4242eda8c47c605:L58', 'real_69c60971d4242eda8c47c605:L73', 'real_69c60971d4242eda8c47c605:L83', 'real_69c60971d4242eda8c47c605:L91', 'real_69c60971d4242eda8c47c605:L110', 'real_69c60971d4242eda8c47c605:L118']
- child_reports=11 skipped=0
- legal_actions (43):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L1 | 第一章 总则 | score=0.0642
  - D1 | DISPATCH | real_69c60971d4242eda8c47c605:L1 | 第一章 总则 | score=0.0642
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L2 | 第一条为规范集团公司及下属单位印章管理工作，有效防范风险，保障经营管理活动的有序开展，特制定本办法。 | score=0.0642
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L3 | 第二条本办法所称集团公司印章包括：集团公司法人章、财务专用章、机关部门章，集团公司下属单位印章、项目部章等行使公司职权的法定名称章；集团公司法定代表人章、总会计师章等代表公司实施职务行为的印章。 | score=0.0631
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L5 | 集团公司法人章为圆形，直径为4.2CM，中央刊五角星，上环刊单位名称自左向右环排；部门章一律为圆形，直径为3.8CM，上刊集团名称自左向右环排，中央刊五角星，部门名称放在星下方作横排；二级单位公章一律为圆形，直径4.0CM，集团名称自左而右环排，二级单位名称放在星下方作横排。项目部章一律为圆形，直径4.0CM，集团名称和工程名称依次自左而右环排，“工程项目部”字样放在星下方作横排，名称应严格按“陕 | score=0.0540
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0641
  - D2 | DISPATCH | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0641
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L9 | （一）集团公司机关各部门章，二级单位章，由集团办公室根据集团公司或上级有关部门批准成立该机构的文件制发。 | score=0.0641
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L19 | 确因工作需要刻制印章的，由用印单位或部门提出申请，详细说明印章的名称、用途、式样和规格，报集团公司主要领导批准后由办公室制发。 | score=0.0634
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L21 | 第七条项目部印章在使用前，项目部应负责将集团公司办公室出具的印章启用文件报送建设单位、监理单位等相关方，以便业务往来确认。并在文件送达后一周内将回执返回集团公司办公室留存。 | score=0.0607
  - C9 | COLLECT | real_69c60971d4242eda8c47c605:L23 | 第九条发生印章遗失，印章责任管理单位应在24小时内向集团公司和当地公安机关报告；在3个工作日内在省级以上报刊办理遗失声明，并向集团公司申请出具告知函，及时通知相关单位。印章遗失处理流程见附件。 | score=0.0534
  - C10 | COLLECT | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0710
  - D3 | DISPATCH | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0710
  - C11 | COLLECT | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0710
  - D4 | DISPATCH | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0710
  - C12 | COLLECT | real_69c60971d4242eda8c47c605:L42 | （六）集团公司法人明确授权或者委托对外使用印章的事项。 | score=0.0710
- projection_chars: 3663

**Step 24** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Sufficient evidence collected from all relevant sections to answer the query about seal management regulations.
- legal_actions (11):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L101 | 第六章 印章封口、停用与缴销 | score=0.0475
  - D1 | DISPATCH | real_69c60971d4242eda8c47c605:L101 | 第六章 印章封口、停用与缴销 | score=0.0475
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L102 | 第三十二条项目部印章封口管理 | score=0.0371
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L103 | （一）在集团公司生产管理部发布的“封口闭合启动令”60日内上交集团公司办公室封存；项目印章回收后不得外借，期间如需要使用印章由原项目经理申请，责任管理单位批准后，在集团公司办公室登记用印。 | score=0.0360
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L104 | （二）以其他单位名称承揽项目的项目印章回收，按照集团公司印章回收程序办理移交，再由集团公司移交回印章刻制单位。 | score=0.0325
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L105 | （三）印章收回时，用印登记本一并收回。 | score=0.0278
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L106 | 第三十三条发生机构名称变更、机构撤销等情况时，相关印章应在相关文件下发之日起停止使用，并在三个工作日内上交集团公司办公室。 | score=0.0422
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L107 | 上缴的各类印章，应按要求办理缴销手续，留下印模。印章由集团公司办公室统一封存、销毁。 | score=0.0345
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L108 | 第三十四条上缴的各类印章，由集团公司办公室按《档案管理办法》要求统一封存、销毁，留下永久印模。 | score=0.0377
  - C9 | COLLECT | real_69c60971d4242eda8c47c605:L109 | 印章停用、变更后，相关单位应根据需要及时通知有关业务往来单位，并标明停用、变更印章时间、印模。印章回收时，印章登记薄同步回收。 | score=0.0475
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 998

### Subagent reports_context

```
=== Investigate results (11 region(s)) ===
[region 1] real_69c60971d4242eda8c47c605:L36 (ok)
collected 7 branch node(s); explicit roots=['real_69c60971d4242eda8c47c605:L36']
collected: real_69c60971d4242eda8c47c605:L36, real_69c60971d4242eda8c47c605:L37, real_69c60971d4242eda8c47c605:L38, real_69c60971d4242eda8c47c605:L39, real_69c60971d4242eda8c47c605:L40, real_69c60971d4242eda8c47c605:L41, real_69c60971d4242eda8c47c605:L42
reason: Evidence collected from the relevant section is sufficient to answer the query about the seal management regulations.
---
[region 2] real_69c60971d4242eda8c47c605:L7 (ok)
collected 18 branch node(s); explicit roots=['real_69c60971d4242eda8c47c605:L7']
collected: real_69c60971d4242eda8c47c605:L10, real_69c60971d4242eda8c47c605:L11, real_69c60971d4242eda8c47c605:L12, real_69c60971d4242eda8c47c605:L13, real_69c60971d4242eda8c47c605:L14, real_69c60971d4242eda8c47c605:L15, real_69c60971d4242eda8c47c605:L16, real_69c60971d4242eda8c47c605:L17, real_69c60971d4242eda8c47c605:L18, real_69c60971d4242eda8c47c605:L19, real_69c60971d4242eda8c47c605:L20, real_69c60971d4242eda8c47c605:L21, real_69c60971d4242eda8c47c605:L22, real_69c60971d4242eda8c47c605:L23, real_69c60971d4242eda8c47c605:L24, real_69c60971d4242eda8c47c605:L7, real_69c60971d4242eda8c47c605:L8, real_69c60971d4242eda8c47c605:L9
reason: Evidence collected is sufficient to answer the query regarding the seal management regulations.
---
[region 3] real_69c60971d4242eda8c47c605:L1 (ok)
collected 6 branch node(s); explicit roots=['real_69c60971d4242eda8c47c605:L1']
collected: real_69c60971d4242eda8c47c605:L1, real_69c60971d4242eda8c47c605:L2, real_69c60971d4242eda8c47c605:L3, real_69c60971d4242eda8c47c605:L4, real_69c60971d4242eda8c47c605:L5, real_69c60971d4242eda8c47c605:L6
reason: The document root has been collected, providing the necessary context to answer the query about the seal management regulations.
---
[region 4] real_69c60971d4242eda8c47c605:L25 (ok)
collected 33 branch node(s); exp
```

### Evidence text (new)

```
[E1]
[§ 第七章	责任追究]
  第三十五条伪造、私刻集团公司法人章、财务专用章、银行预留印鉴章、领导签名章的，一经发现，对伪造、私刻责任方（单位、项目部、个人）处10万元罚款，并由集团公司组织调查组进行调查，根据情节轻重追究相关责任人的行政、经济责任，通报批评，依法追偿损失；涉嫌犯罪的，报请司法机关依法进行处理。
  第三十六条伪造、私刻集团公司机关部门章、二级单位章、项目部印章的，一经发现，对伪造、私刻责任方（单位、项目部、个人）处于6万元罚款，并由集团公司组织调查组进行调查，根据情节轻重追究相关责任人的行政、经济责任，通报批评，依法追偿损失。涉嫌犯罪的，报请司法机关依法进行处理。
  第四十一条有印章使用审批权限的其他管理人员，超越审批权限使用印章，造成经济损失及不良后果的，由集团公司党委组织部、监察审计部按《管理人员责任追究暂行规定》追究其相关责任。
  第四十二条印章责任管理单位、监管部门未认真履行印章管理、检查监督、封口管理等职责，发生伪造、私刻印章等情节严重，或造成经济损失及不良影响的，对管理责任人按集团公司《管理人员责任追究暂行规定》追究相关责任。
```

### Evidence text (old)

```
[E1]
陕西建工第十一建设集团有限公司印章管理办法（2020版）.docx

[E2]
[§ 陕西建工第十一建设集团有限公司印章管理办法（2020版）.docx / 第八章 附则]
注：

[E3]
陕西建工第十一建设集团有限公司印章管理办法（2020版）.docx
第一章 总则

[E4]
[§ 陕西建工第十一建设集团有限公司印章管理办法（2020版）.docx / 第八章 附则]
注：此表一式四份，集团公司办公室、责任管理单位/机关部门、项目负责人和印章保管人各执一份

[E5]
[§ 陕西建工第十一建设集团有限公司印章管理办法（2020版）.docx / 第八章 附则]
本文档明确了集团及项目部印章的使用范围、管理要求、审批程序及登记规范，强调专人保管与严禁空白盖章，并要求负责人签字承诺遵守规定。

[E6]
[§ 陕西建工第十一建设集团有限公司印章管理办法（2020版）.docx / 第八章 附则]
印章管理移交单

[E7]
[§ 陕西建工第十一建设集团有限公司印章管理办法（2020版）.docx / 第八章 附则]
单位（部门）：
```

## latest_clean_scope_0101 (scope_collection)

**Query:** 列举《马来西亚合同样本 2006 版 翻译件- Malaysia-PAM-合同翻译稿（4.23二译）》中“Levels And Setting Out Of The Works水”部分的主要条目。

**Doc:** `real_69c60aeed4242eda8c47c925`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 158 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 19 | 3 |
| trajectory_steps | n/a | 11 |

### Gold node hits (new)

- `real_69c60aeed4242eda8c47c925:L114` [MISS] retrieved=False in_text=False
- `real_69c60aeed4242eda8c47c925:L115` [MISS] retrieved=False in_text=False
- `real_69c60aeed4242eda8c47c925:L116` [MISS] retrieved=False in_text=False
- `real_69c60aeed4242eda8c47c925:L117` [MISS] retrieved=False in_text=False
- `real_69c60aeed4242eda8c47c925:L118` [MISS] retrieved=False in_text=False
- `real_69c60aeed4242eda8c47c925:L119` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C4` kind=`collect` section=`real_69c60aeed4242eda8c47c925:L110` scope=`None` depth=`0`
- reason: Collect the 'Levels And Setting Out Of The Works' section to retrieve its main items.
- collect_section_ids: ['real_69c60aeed4242eda8c47c925:L110']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (50):
  - C1 | COLLECT | real_69c60aeed4242eda8c47c925:L35 | Contract Documents,Programme And As-built Drawings 合同文件、方案和竣工图纸 | score=0.0371
  - D1 | DISPATCH | real_69c60aeed4242eda8c47c925:L35 | Contract Documents,Programme And As-built Drawings 合同文件、方案和竣工图纸 | score=0.0371
  - C2 | COLLECT | real_69c60aeed4242eda8c47c925:L54 | 4.2	与法定要求不一致 | score=0.0371
  - D2 | DISPATCH | real_69c60aeed4242eda8c47c925:L54 | 4.2	与法定要求不一致 | score=0.0371
  - C3 | COLLECT | real_69c60aeed4242eda8c47c925:L55 | PAM Contract 2006 (With Quantities) (i) | score=0.0371
  - C4 | COLLECT | real_69c60aeed4242eda8c47c925:L110 | Levels And Setting Out Of The Works水平和设置的工作 | score=0.0556
  - D3 | DISPATCH | real_69c60aeed4242eda8c47c925:L110 | Levels And Setting Out Of The Works水平和设置的工作 | score=0.0556
  - C5 | COLLECT | real_69c60aeed4242eda8c47c925:L111 | Setting out设置 | score=0.0556
  - C6 | COLLECT | real_69c60aeed4242eda8c47c925:L142 | Materials And Goods材料和货物 | score=0.0352
  - D4 | DISPATCH | real_69c60aeed4242eda8c47c925:L142 | Materials And Goods材料和货物 | score=0.0352
  - C7 | COLLECT | real_69c60aeed4242eda8c47c925:L153 | PAM Contract 2006(With Quantities) (i) | score=0.0352
  - C8 | COLLECT | real_69c60aeed4242eda8c47c925:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0644
  - D5 | DISPATCH | real_69c60aeed4242eda8c47c925:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0644
  - C9 | COLLECT | real_69c60aeed4242eda8c47c925:L390 | Article 3 | score=0.0644
  - D6 | DISPATCH | real_69c60aeed4242eda8c47c925:L390 | Article 3 | score=0.0644
  - C10 | COLLECT | real_69c60aeed4242eda8c47c925:L668 | 3.0	Contract  Documents,Programme  And  As-built Drawings | score=0.0644
- projection_chars: 3709

**Step 2** `nav_collect`  id=`C10` kind=`collect` section=`real_69c60aeed4242eda8c47c925:L751` scope=`None` depth=`0`
- reason: Collect the specific leaf node 'Levels And Setting Out Of The Works' to retrieve its main items.
- collect_section_ids: ['real_69c60aeed4242eda8c47c925:L751']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (48):
  - C1 | COLLECT | real_69c60aeed4242eda8c47c925:L35 | Contract Documents,Programme And As-built Drawings 合同文件、方案和竣工图纸 | score=0.0371
  - D1 | DISPATCH | real_69c60aeed4242eda8c47c925:L35 | Contract Documents,Programme And As-built Drawings 合同文件、方案和竣工图纸 | score=0.0371
  - C2 | COLLECT | real_69c60aeed4242eda8c47c925:L54 | 4.2	与法定要求不一致 | score=0.0371
  - D2 | DISPATCH | real_69c60aeed4242eda8c47c925:L54 | 4.2	与法定要求不一致 | score=0.0371
  - C3 | COLLECT | real_69c60aeed4242eda8c47c925:L55 | PAM Contract 2006 (With Quantities) (i) | score=0.0371
  - C4 | COLLECT | real_69c60aeed4242eda8c47c925:L142 | Materials And Goods材料和货物 | score=0.0352
  - D3 | DISPATCH | real_69c60aeed4242eda8c47c925:L142 | Materials And Goods材料和货物 | score=0.0352
  - C5 | COLLECT | real_69c60aeed4242eda8c47c925:L153 | PAM Contract 2006(With Quantities) (i) | score=0.0352
  - C6 | COLLECT | real_69c60aeed4242eda8c47c925:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0644
  - D4 | DISPATCH | real_69c60aeed4242eda8c47c925:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0644
  - C7 | COLLECT | real_69c60aeed4242eda8c47c925:L390 | Article 3 | score=0.0644
  - D5 | DISPATCH | real_69c60aeed4242eda8c47c925:L390 | Article 3 | score=0.0644
  - C8 | COLLECT | real_69c60aeed4242eda8c47c925:L668 | 3.0	Contract  Documents,Programme  And  As-built Drawings | score=0.0644
  - D6 | DISPATCH | real_69c60aeed4242eda8c47c925:L668 | 3.0	Contract  Documents,Programme  And  As-built Drawings | score=0.0644
  - C9 | COLLECT | real_69c60aeed4242eda8c47c925:L727 | 3.0	Contract  Documents,Programme  And  As-built Drawings part 2 | score=0.0644
  - D7 | DISPATCH | real_69c60aeed4242eda8c47c925:L727 | 3.0	Contract  Documents,Programme  And  As-built Drawings part 2 | score=0.0644
- projection_chars: 3575

**Step 3** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60aeed4242eda8c47c925:L35` depth=`1`
- reason: The current scope does not contain the 'Levels And Setting Out Of The Works' section. No relevant evidence can be collected here.
- legal_actions (18):
  - C1 | COLLECT | real_69c60aeed4242eda8c47c925:L35 | Contract Documents,Programme And As-built Drawings 合同文件、方案和竣工图纸 | score=0.0371
  - C2 | COLLECT | real_69c60aeed4242eda8c47c925:L36 | Contract Documents 9-10 | score=0.0101
  - C3 | COLLECT | real_69c60aeed4242eda8c47c925:L37 | 3.1合同文件 | score=0.0081
  - C4 | COLLECT | real_69c60aeed4242eda8c47c925:L38 | Custody of tender documents 10 | score=0.0081
  - C5 | COLLECT | real_69c60aeed4242eda8c47c925:L43 | 3.4进一步的图纸或细节 | score=0.0100
  - C6 | COLLECT | real_69c60aeed4242eda8c47c925:L44 | 3.6不属于合同一部分的项目 | score=0.0233
  - C7 | COLLECT | real_69c60aeed4242eda8c47c925:L45 | Architect's acceptance of programme 10 | score=0.0233
  - C8 | COLLECT | real_69c60aeed4242eda8c47c925:L46 | 3.7建筑师对方案的验收 | score=0.0076
  - C9 | COLLECT | real_69c60aeed4242eda8c47c925:L47 | Availability of documents 10 | score=0.0076
  - C10 | COLLECT | real_69c60aeed4242eda8c47c925:L48 | 3.8文件的可用性 | score=0.0097
  - C11 | COLLECT | real_69c60aeed4242eda8c47c925:L49 | Limitation of use of documents 10 | score=0.0097
  - C12 | COLLECT | real_69c60aeed4242eda8c47c925:L50 | 3.9文件使用限制 | score=0.0086
  - C13 | COLLECT | real_69c60aeed4242eda8c47c925:L51 | As-built Drawings and operation and maintenance manuals 10 | score=0.0086
  - C14 | COLLECT | real_69c60aeed4242eda8c47c925:L54 | 4.2	与法定要求不一致 | score=0.0371
  - C15 | COLLECT | real_69c60aeed4242eda8c47c925:L55 | PAM Contract 2006 (With Quantities) (i) | score=0.0371
  - C16 | COLLECT | real_69c60aeed4242eda8c47c925:L56 | Clause | score=0.0095
- projection_chars: 2550

**Step 4** `nav_dispatch`  id=`D1` kind=`dispatch` section=`real_69c60aeed4242eda8c47c925:L35` scope=`None` depth=`0`
- reason: Dispatch N1 to locate 'Levels And Setting Out Of The Works' section.
- dispatch_regions: ['real_69c60aeed4242eda8c47c925:L35']
- child_reports=1 skipped=0
- legal_actions (52):
  - C1 | COLLECT | real_69c60aeed4242eda8c47c925:L35 | Contract Documents,Programme And As-built Drawings 合同文件、方案和竣工图纸 | score=0.0371
  - D1 | DISPATCH | real_69c60aeed4242eda8c47c925:L35 | Contract Documents,Programme And As-built Drawings 合同文件、方案和竣工图纸 | score=0.0371
  - C2 | COLLECT | real_69c60aeed4242eda8c47c925:L54 | 4.2	与法定要求不一致 | score=0.0371
  - D2 | DISPATCH | real_69c60aeed4242eda8c47c925:L54 | 4.2	与法定要求不一致 | score=0.0371
  - C3 | COLLECT | real_69c60aeed4242eda8c47c925:L55 | PAM Contract 2006 (With Quantities) (i) | score=0.0371
  - C4 | COLLECT | real_69c60aeed4242eda8c47c925:L142 | Materials And Goods材料和货物 | score=0.0352
  - D3 | DISPATCH | real_69c60aeed4242eda8c47c925:L142 | Materials And Goods材料和货物 | score=0.0352
  - C5 | COLLECT | real_69c60aeed4242eda8c47c925:L153 | PAM Contract 2006(With Quantities) (i) | score=0.0352
  - C6 | COLLECT | real_69c60aeed4242eda8c47c925:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0644
  - D4 | DISPATCH | real_69c60aeed4242eda8c47c925:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0644
  - C7 | COLLECT | real_69c60aeed4242eda8c47c925:L390 | Article 3 | score=0.0644
  - D5 | DISPATCH | real_69c60aeed4242eda8c47c925:L390 | Article 3 | score=0.0644
  - C8 | COLLECT | real_69c60aeed4242eda8c47c925:L487 | (z) | score=0.0350
  - D6 | DISPATCH | real_69c60aeed4242eda8c47c925:L487 | (z) | score=0.0350
  - C9 | COLLECT | real_69c60aeed4242eda8c47c925:L488 | (z) part 1 | score=0.0350
  - D7 | DISPATCH | real_69c60aeed4242eda8c47c925:L488 | (z) part 1 | score=0.0350
- projection_chars: 3692

**Step 5** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60aeed4242eda8c47c925:L35` depth=`1`
- reason: The current scope does not contain the 'Levels And Setting Out Of The Works' section. No relevant evidence can be collected here.
- legal_actions (18):
  - C1 | COLLECT | real_69c60aeed4242eda8c47c925:L35 | Contract Documents,Programme And As-built Drawings 合同文件、方案和竣工图纸 | score=0.0371
  - C2 | COLLECT | real_69c60aeed4242eda8c47c925:L36 | Contract Documents 9-10 | score=0.0101
  - C3 | COLLECT | real_69c60aeed4242eda8c47c925:L37 | 3.1合同文件 | score=0.0081
  - C4 | COLLECT | real_69c60aeed4242eda8c47c925:L38 | Custody of tender documents 10 | score=0.0081
  - C5 | COLLECT | real_69c60aeed4242eda8c47c925:L43 | 3.4进一步的图纸或细节 | score=0.0100
  - C6 | COLLECT | real_69c60aeed4242eda8c47c925:L44 | 3.6不属于合同一部分的项目 | score=0.0233
  - C7 | COLLECT | real_69c60aeed4242eda8c47c925:L45 | Architect's acceptance of programme 10 | score=0.0233
  - C8 | COLLECT | real_69c60aeed4242eda8c47c925:L46 | 3.7建筑师对方案的验收 | score=0.0076
  - C9 | COLLECT | real_69c60aeed4242eda8c47c925:L47 | Availability of documents 10 | score=0.0076
  - C10 | COLLECT | real_69c60aeed4242eda8c47c925:L48 | 3.8文件的可用性 | score=0.0097
  - C11 | COLLECT | real_69c60aeed4242eda8c47c925:L49 | Limitation of use of documents 10 | score=0.0097
  - C12 | COLLECT | real_69c60aeed4242eda8c47c925:L50 | 3.9文件使用限制 | score=0.0086
  - C13 | COLLECT | real_69c60aeed4242eda8c47c925:L51 | As-built Drawings and operation and maintenance manuals 10 | score=0.0086
  - C14 | COLLECT | real_69c60aeed4242eda8c47c925:L54 | 4.2	与法定要求不一致 | score=0.0371
  - C15 | COLLECT | real_69c60aeed4242eda8c47c925:L55 | PAM Contract 2006 (With Quantities) (i) | score=0.0371
  - C16 | COLLECT | real_69c60aeed4242eda8c47c925:L56 | Clause | score=0.0095
- projection_chars: 2550

**Step 6** `nav_dispatch`  id=`D1` kind=`dispatch` section=`real_69c60aeed4242eda8c47c925:L35` scope=`None` depth=`0`
- reason: Dispatch to find 'Levels And Setting Out Of The Works' section.
- dispatch_regions: ['real_69c60aeed4242eda8c47c925:L35']
- child_reports=1 skipped=0
- legal_actions (52):
  - C1 | COLLECT | real_69c60aeed4242eda8c47c925:L35 | Contract Documents,Programme And As-built Drawings 合同文件、方案和竣工图纸 | score=0.0371
  - D1 | DISPATCH | real_69c60aeed4242eda8c47c925:L35 | Contract Documents,Programme And As-built Drawings 合同文件、方案和竣工图纸 | score=0.0371
  - C2 | COLLECT | real_69c60aeed4242eda8c47c925:L54 | 4.2	与法定要求不一致 | score=0.0371
  - D2 | DISPATCH | real_69c60aeed4242eda8c47c925:L54 | 4.2	与法定要求不一致 | score=0.0371
  - C3 | COLLECT | real_69c60aeed4242eda8c47c925:L55 | PAM Contract 2006 (With Quantities) (i) | score=0.0371
  - C4 | COLLECT | real_69c60aeed4242eda8c47c925:L142 | Materials And Goods材料和货物 | score=0.0352
  - D3 | DISPATCH | real_69c60aeed4242eda8c47c925:L142 | Materials And Goods材料和货物 | score=0.0352
  - C5 | COLLECT | real_69c60aeed4242eda8c47c925:L153 | PAM Contract 2006(With Quantities) (i) | score=0.0352
  - C6 | COLLECT | real_69c60aeed4242eda8c47c925:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0644
  - D4 | DISPATCH | real_69c60aeed4242eda8c47c925:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0644
  - C7 | COLLECT | real_69c60aeed4242eda8c47c925:L390 | Article 3 | score=0.0644
  - D5 | DISPATCH | real_69c60aeed4242eda8c47c925:L390 | Article 3 | score=0.0644
  - C8 | COLLECT | real_69c60aeed4242eda8c47c925:L487 | (z) | score=0.0350
  - D6 | DISPATCH | real_69c60aeed4242eda8c47c925:L487 | (z) | score=0.0350
  - C9 | COLLECT | real_69c60aeed4242eda8c47c925:L488 | (z) part 1 | score=0.0350
  - D7 | DISPATCH | real_69c60aeed4242eda8c47c925:L488 | (z) part 1 | score=0.0350
- projection_chars: 3692

**Step 7** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60aeed4242eda8c47c925:L35` depth=`1`
- reason: The current scope does not contain the 'Levels And Setting Out Of The Works' section. No relevant evidence can be collected here.
- legal_actions (18):
  - C1 | COLLECT | real_69c60aeed4242eda8c47c925:L35 | Contract Documents,Programme And As-built Drawings 合同文件、方案和竣工图纸 | score=0.0371
  - C2 | COLLECT | real_69c60aeed4242eda8c47c925:L36 | Contract Documents 9-10 | score=0.0101
  - C3 | COLLECT | real_69c60aeed4242eda8c47c925:L37 | 3.1合同文件 | score=0.0081
  - C4 | COLLECT | real_69c60aeed4242eda8c47c925:L38 | Custody of tender documents 10 | score=0.0081
  - C5 | COLLECT | real_69c60aeed4242eda8c47c925:L43 | 3.4进一步的图纸或细节 | score=0.0100
  - C6 | COLLECT | real_69c60aeed4242eda8c47c925:L44 | 3.6不属于合同一部分的项目 | score=0.0233
  - C7 | COLLECT | real_69c60aeed4242eda8c47c925:L45 | Architect's acceptance of programme 10 | score=0.0233
  - C8 | COLLECT | real_69c60aeed4242eda8c47c925:L46 | 3.7建筑师对方案的验收 | score=0.0076
  - C9 | COLLECT | real_69c60aeed4242eda8c47c925:L47 | Availability of documents 10 | score=0.0076
  - C10 | COLLECT | real_69c60aeed4242eda8c47c925:L48 | 3.8文件的可用性 | score=0.0097
  - C11 | COLLECT | real_69c60aeed4242eda8c47c925:L49 | Limitation of use of documents 10 | score=0.0097
  - C12 | COLLECT | real_69c60aeed4242eda8c47c925:L50 | 3.9文件使用限制 | score=0.0086
  - C13 | COLLECT | real_69c60aeed4242eda8c47c925:L51 | As-built Drawings and operation and maintenance manuals 10 | score=0.0086
  - C14 | COLLECT | real_69c60aeed4242eda8c47c925:L54 | 4.2	与法定要求不一致 | score=0.0371
  - C15 | COLLECT | real_69c60aeed4242eda8c47c925:L55 | PAM Contract 2006 (With Quantities) (i) | score=0.0371
  - C16 | COLLECT | real_69c60aeed4242eda8c47c925:L56 | Clause | score=0.0095
- projection_chars: 2550

**Step 8** `nav_dispatch`  id=`D1` kind=`dispatch` section=`real_69c60aeed4242eda8c47c925:L35` scope=`None` depth=`0`
- reason: Dispatch to find 'Levels And Setting Out Of The Works' section.
- dispatch_regions: ['real_69c60aeed4242eda8c47c925:L35']
- child_reports=1 skipped=0
- legal_actions (52):
  - C1 | COLLECT | real_69c60aeed4242eda8c47c925:L35 | Contract Documents,Programme And As-built Drawings 合同文件、方案和竣工图纸 | score=0.0371
  - D1 | DISPATCH | real_69c60aeed4242eda8c47c925:L35 | Contract Documents,Programme And As-built Drawings 合同文件、方案和竣工图纸 | score=0.0371
  - C2 | COLLECT | real_69c60aeed4242eda8c47c925:L54 | 4.2	与法定要求不一致 | score=0.0371
  - D2 | DISPATCH | real_69c60aeed4242eda8c47c925:L54 | 4.2	与法定要求不一致 | score=0.0371
  - C3 | COLLECT | real_69c60aeed4242eda8c47c925:L55 | PAM Contract 2006 (With Quantities) (i) | score=0.0371
  - C4 | COLLECT | real_69c60aeed4242eda8c47c925:L142 | Materials And Goods材料和货物 | score=0.0352
  - D3 | DISPATCH | real_69c60aeed4242eda8c47c925:L142 | Materials And Goods材料和货物 | score=0.0352
  - C5 | COLLECT | real_69c60aeed4242eda8c47c925:L153 | PAM Contract 2006(With Quantities) (i) | score=0.0352
  - C6 | COLLECT | real_69c60aeed4242eda8c47c925:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0644
  - D4 | DISPATCH | real_69c60aeed4242eda8c47c925:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0644
  - C7 | COLLECT | real_69c60aeed4242eda8c47c925:L390 | Article 3 | score=0.0644
  - D5 | DISPATCH | real_69c60aeed4242eda8c47c925:L390 | Article 3 | score=0.0644
  - C8 | COLLECT | real_69c60aeed4242eda8c47c925:L487 | (z) | score=0.0350
  - D6 | DISPATCH | real_69c60aeed4242eda8c47c925:L487 | (z) | score=0.0350
  - C9 | COLLECT | real_69c60aeed4242eda8c47c925:L488 | (z) part 1 | score=0.0350
  - D7 | DISPATCH | real_69c60aeed4242eda8c47c925:L488 | (z) part 1 | score=0.0350
- projection_chars: 3692

**Step 9** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60aeed4242eda8c47c925:L35` depth=`1`
- reason: The current scope does not contain the 'Levels And Setting Out Of The Works' section. No relevant evidence can be collected here.
- legal_actions (18):
  - C1 | COLLECT | real_69c60aeed4242eda8c47c925:L35 | Contract Documents,Programme And As-built Drawings 合同文件、方案和竣工图纸 | score=0.0371
  - C2 | COLLECT | real_69c60aeed4242eda8c47c925:L36 | Contract Documents 9-10 | score=0.0101
  - C3 | COLLECT | real_69c60aeed4242eda8c47c925:L37 | 3.1合同文件 | score=0.0081
  - C4 | COLLECT | real_69c60aeed4242eda8c47c925:L38 | Custody of tender documents 10 | score=0.0081
  - C5 | COLLECT | real_69c60aeed4242eda8c47c925:L43 | 3.4进一步的图纸或细节 | score=0.0100
  - C6 | COLLECT | real_69c60aeed4242eda8c47c925:L44 | 3.6不属于合同一部分的项目 | score=0.0233
  - C7 | COLLECT | real_69c60aeed4242eda8c47c925:L45 | Architect's acceptance of programme 10 | score=0.0233
  - C8 | COLLECT | real_69c60aeed4242eda8c47c925:L46 | 3.7建筑师对方案的验收 | score=0.0076
  - C9 | COLLECT | real_69c60aeed4242eda8c47c925:L47 | Availability of documents 10 | score=0.0076
  - C10 | COLLECT | real_69c60aeed4242eda8c47c925:L48 | 3.8文件的可用性 | score=0.0097
  - C11 | COLLECT | real_69c60aeed4242eda8c47c925:L49 | Limitation of use of documents 10 | score=0.0097
  - C12 | COLLECT | real_69c60aeed4242eda8c47c925:L50 | 3.9文件使用限制 | score=0.0086
  - C13 | COLLECT | real_69c60aeed4242eda8c47c925:L51 | As-built Drawings and operation and maintenance manuals 10 | score=0.0086
  - C14 | COLLECT | real_69c60aeed4242eda8c47c925:L54 | 4.2	与法定要求不一致 | score=0.0371
  - C15 | COLLECT | real_69c60aeed4242eda8c47c925:L55 | PAM Contract 2006 (With Quantities) (i) | score=0.0371
  - C16 | COLLECT | real_69c60aeed4242eda8c47c925:L56 | Clause | score=0.0095
- projection_chars: 2550

**Step 10** `nav_dispatch`  id=`D1` kind=`dispatch` section=`real_69c60aeed4242eda8c47c925:L35` scope=`None` depth=`0`
- reason: Dispatch to find 'Levels And Setting Out Of The Works' section.
- dispatch_regions: ['real_69c60aeed4242eda8c47c925:L35']
- child_reports=1 skipped=0
- legal_actions (52):
  - C1 | COLLECT | real_69c60aeed4242eda8c47c925:L35 | Contract Documents,Programme And As-built Drawings 合同文件、方案和竣工图纸 | score=0.0371
  - D1 | DISPATCH | real_69c60aeed4242eda8c47c925:L35 | Contract Documents,Programme And As-built Drawings 合同文件、方案和竣工图纸 | score=0.0371
  - C2 | COLLECT | real_69c60aeed4242eda8c47c925:L54 | 4.2	与法定要求不一致 | score=0.0371
  - D2 | DISPATCH | real_69c60aeed4242eda8c47c925:L54 | 4.2	与法定要求不一致 | score=0.0371
  - C3 | COLLECT | real_69c60aeed4242eda8c47c925:L55 | PAM Contract 2006 (With Quantities) (i) | score=0.0371
  - C4 | COLLECT | real_69c60aeed4242eda8c47c925:L142 | Materials And Goods材料和货物 | score=0.0352
  - D3 | DISPATCH | real_69c60aeed4242eda8c47c925:L142 | Materials And Goods材料和货物 | score=0.0352
  - C5 | COLLECT | real_69c60aeed4242eda8c47c925:L153 | PAM Contract 2006(With Quantities) (i) | score=0.0352
  - C6 | COLLECT | real_69c60aeed4242eda8c47c925:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0644
  - D4 | DISPATCH | real_69c60aeed4242eda8c47c925:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0644
  - C7 | COLLECT | real_69c60aeed4242eda8c47c925:L390 | Article 3 | score=0.0644
  - D5 | DISPATCH | real_69c60aeed4242eda8c47c925:L390 | Article 3 | score=0.0644
  - C8 | COLLECT | real_69c60aeed4242eda8c47c925:L487 | (z) | score=0.0350
  - D6 | DISPATCH | real_69c60aeed4242eda8c47c925:L487 | (z) | score=0.0350
  - C9 | COLLECT | real_69c60aeed4242eda8c47c925:L488 | (z) part 1 | score=0.0350
  - D7 | DISPATCH | real_69c60aeed4242eda8c47c925:L488 | (z) part 1 | score=0.0350
- projection_chars: 3692

**Step 11** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: The 'Levels And Setting Out Of The Works' section was not found in the investigated regions or current map. No further steps available to locate it.
- legal_actions (52):
  - C1 | COLLECT | real_69c60aeed4242eda8c47c925:L35 | Contract Documents,Programme And As-built Drawings 合同文件、方案和竣工图纸 | score=0.0371
  - D1 | DISPATCH | real_69c60aeed4242eda8c47c925:L35 | Contract Documents,Programme And As-built Drawings 合同文件、方案和竣工图纸 | score=0.0371
  - C2 | COLLECT | real_69c60aeed4242eda8c47c925:L54 | 4.2	与法定要求不一致 | score=0.0371
  - D2 | DISPATCH | real_69c60aeed4242eda8c47c925:L54 | 4.2	与法定要求不一致 | score=0.0371
  - C3 | COLLECT | real_69c60aeed4242eda8c47c925:L55 | PAM Contract 2006 (With Quantities) (i) | score=0.0371
  - C4 | COLLECT | real_69c60aeed4242eda8c47c925:L142 | Materials And Goods材料和货物 | score=0.0352
  - D3 | DISPATCH | real_69c60aeed4242eda8c47c925:L142 | Materials And Goods材料和货物 | score=0.0352
  - C5 | COLLECT | real_69c60aeed4242eda8c47c925:L153 | PAM Contract 2006(With Quantities) (i) | score=0.0352
  - C6 | COLLECT | real_69c60aeed4242eda8c47c925:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0644
  - D4 | DISPATCH | real_69c60aeed4242eda8c47c925:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0644
  - C7 | COLLECT | real_69c60aeed4242eda8c47c925:L390 | Article 3 | score=0.0644
  - D5 | DISPATCH | real_69c60aeed4242eda8c47c925:L390 | Article 3 | score=0.0644
  - C8 | COLLECT | real_69c60aeed4242eda8c47c925:L487 | (z) | score=0.0350
  - D6 | DISPATCH | real_69c60aeed4242eda8c47c925:L487 | (z) | score=0.0350
  - C9 | COLLECT | real_69c60aeed4242eda8c47c925:L488 | (z) part 1 | score=0.0350
  - D7 | DISPATCH | real_69c60aeed4242eda8c47c925:L488 | (z) part 1 | score=0.0350
- projection_chars: 3692

### Subagent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60aeed4242eda8c47c925:L35 (ok)
The current scope does not contain the 'Levels And Setting Out Of The Works' section. No relevant evidence can be collected here.
reason: The current scope does not contain the 'Levels And Setting Out Of The Works' section. No relevant evidence can be collected here.
---
=== End Investigate ===
```

### Evidence text (new)

```
[E1]
[§ 3.0	Contract  Documents,Programme  And]
Levels And Setting Out Of The Works--工程的测量与放样

[E2]
[§ Levels And Setting Out Of The Works水平和设置]
Setting out设置
```

### Evidence text (old)

```
[E1]
马来西亚合同样本 2006 版 翻译件- Malaysia-PAM-合同翻译稿（4.23二译）.docx

[E2]
Articles章节
Article 1 Contractor's Obligations 承包商义务2
Article 2 Contract Sum 合同金额2

[E3]
Attestation
Signatories Of The Parties	各方的证明
签署人

[E4]
Architect's Instructions (‘AI')
Contractor to comply with AI
AI

[E5]
Contract Documents,Programme And As-built Drawings 合同文件、方案和竣工图纸
Contract Documents 9-10
3.1合同文件

[E6]
Page
5.0
5.1

[E7]
Levels And Setting Out Of The Works水平和设置的工作
Setting out设置

[E8]
Materials,Goods And Workmanship To Con
```

## real_69c6ef484cca74801cb63bb9_multi_hop_auto_0006 (multi_hop)

**Query:** 根据质量控制要求，注浆允许偏差及检验办法应符合哪张表的规定？该表中列出了哪四个关键检查项目？同时，在浆液拌制过程中有哪些具体的操作要求以确保质量？

**Doc:** `real_69c6ef484cca74801cb63bb9`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 486 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 12 | 10 |
| trajectory_steps | n/a | 10 |

### Gold node hits (new)

- `real_69c6ef484cca74801cb63bb9:L159` [MISS] retrieved=False in_text=False
- `real_69c6ef484cca74801cb63bb9:L162` [MISS] retrieved=False in_text=False
- `real_69c6ef484cca74801cb63bb9:L167` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C20` kind=`collect` section=`real_69c6ef484cca74801cb63bb9:L128` scope=`None` depth=`0`
- reason: Identifies the table for grouting deviation and inspection requirements.
- collect_section_ids: ['real_69c6ef484cca74801cb63bb9:L128']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (54):
  - C1 | COLLECT | real_69c6ef484cca74801cb63bb9:L5 | 帷幕式注浆土体加固地基施工工法_2 | score=0.0657
  - D1 | DISPATCH | real_69c6ef484cca74801cb63bb9:L5 | 帷幕式注浆土体加固地基施工工法_2 | score=0.0657
  - C2 | COLLECT | real_69c6ef484cca74801cb63bb9:L7 | 传统注浆加固地基技术存在材料水泥水化反应慢、凝胶时间长、强度可靠性差 、串浆跑浆严重、加固影响区难以控制等缺陷。陕西建工第十一建设集团有限公司 根据深厚杂填土及地基处理的特性，采用帷幕式注浆+跳仓施工工艺解决了传统注浆 加固的强度可靠性差、串浆跑浆严重等问题，提高加固土体密实度，确保加固后地 面满足使用要求。 | score=0.0574
  - C3 | COLLECT | real_69c6ef484cca74801cb63bb9:L21 | 5.工艺流程及操作要点 | score=0.0657
  - D2 | DISPATCH | real_69c6ef484cca74801cb63bb9:L21 | 5.工艺流程及操作要点 | score=0.0657
  - C4 | COLLECT | real_69c6ef484cca74801cb63bb9:L22 | 5.1 工艺流程： | score=0.0657
  - D3 | DISPATCH | real_69c6ef484cca74801cb63bb9:L22 | 5.1 工艺流程： | score=0.0657
  - C5 | COLLECT | real_69c6ef484cca74801cb63bb9:L25 | 5.2.1 施工准备 | score=0.0552
  - D4 | DISPATCH | real_69c6ef484cca74801cb63bb9:L25 | 5.2.1 施工准备 | score=0.0552
  - C6 | COLLECT | real_69c6ef484cca74801cb63bb9:L60 | 3、注浆料配合比确定 | score=0.0524
  - D5 | DISPATCH | real_69c6ef484cca74801cb63bb9:L60 | 3、注浆料配合比确定 | score=0.0524
  - C7 | COLLECT | real_69c6ef484cca74801cb63bb9:L63 | 配合比：A：B=1：1，其中A液：水泥：水=0.8:1 B液：中性水玻璃，波美度为25°-30° 4、每孔注浆量的确定 根据公式 Q=1000kVn，估算每孔注浆水泥用量， | score=0.0524
  - D6 | DISPATCH | real_69c6ef484cca74801cb63bb9:L63 | 配合比：A：B=1：1，其中A液：水泥：水=0.8:1 B液：中性水玻璃，波美度为25°-30° 4、每孔注浆量的确定 根据公式 Q=1000kVn，估算每孔注浆水泥用量， | score=0.0524
  - C8 | COLLECT | real_69c6ef484cca74801cb63bb9:L64 | 式中：Q-浆液总用量L | score=0.0524
  - C9 | COLLECT | real_69c6ef484cca74801cb63bb9:L70 | 5、注浆流量的选择 | score=0.0552
  - D7 | DISPATCH | real_69c6ef484cca74801cb63bb9:L70 | 5、注浆流量的选择 | score=0.0552
- projection_chars: 3415

**Step 2** `nav_collect`  id=`C20` kind=`collect` section=`real_69c6ef484cca74801cb63bb9:L129` scope=`None` depth=`0`
- reason: Collect table 7.2.1 to identify the four key inspection items and their requirements.
- collect_section_ids: ['real_69c6ef484cca74801cb63bb9:L129']
- collect added=33 hits=33 branch_selected=True collect_full=True
- legal_actions (54):
  - C1 | COLLECT | real_69c6ef484cca74801cb63bb9:L5 | 帷幕式注浆土体加固地基施工工法_2 | score=0.0657
  - D1 | DISPATCH | real_69c6ef484cca74801cb63bb9:L5 | 帷幕式注浆土体加固地基施工工法_2 | score=0.0657
  - C2 | COLLECT | real_69c6ef484cca74801cb63bb9:L7 | 传统注浆加固地基技术存在材料水泥水化反应慢、凝胶时间长、强度可靠性差 、串浆跑浆严重、加固影响区难以控制等缺陷。陕西建工第十一建设集团有限公司 根据深厚杂填土及地基处理的特性，采用帷幕式注浆+跳仓施工工艺解决了传统注浆 加固的强度可靠性差、串浆跑浆严重等问题，提高加固土体密实度，确保加固后地 面满足使用要求。 | score=0.0574
  - C3 | COLLECT | real_69c6ef484cca74801cb63bb9:L21 | 5.工艺流程及操作要点 | score=0.0657
  - D2 | DISPATCH | real_69c6ef484cca74801cb63bb9:L21 | 5.工艺流程及操作要点 | score=0.0657
  - C4 | COLLECT | real_69c6ef484cca74801cb63bb9:L22 | 5.1 工艺流程： | score=0.0657
  - D3 | DISPATCH | real_69c6ef484cca74801cb63bb9:L22 | 5.1 工艺流程： | score=0.0657
  - C5 | COLLECT | real_69c6ef484cca74801cb63bb9:L25 | 5.2.1 施工准备 | score=0.0552
  - D4 | DISPATCH | real_69c6ef484cca74801cb63bb9:L25 | 5.2.1 施工准备 | score=0.0552
  - C6 | COLLECT | real_69c6ef484cca74801cb63bb9:L60 | 3、注浆料配合比确定 | score=0.0524
  - D5 | DISPATCH | real_69c6ef484cca74801cb63bb9:L60 | 3、注浆料配合比确定 | score=0.0524
  - C7 | COLLECT | real_69c6ef484cca74801cb63bb9:L63 | 配合比：A：B=1：1，其中A液：水泥：水=0.8:1 B液：中性水玻璃，波美度为25°-30° 4、每孔注浆量的确定 根据公式 Q=1000kVn，估算每孔注浆水泥用量， | score=0.0524
  - D6 | DISPATCH | real_69c6ef484cca74801cb63bb9:L63 | 配合比：A：B=1：1，其中A液：水泥：水=0.8:1 B液：中性水玻璃，波美度为25°-30° 4、每孔注浆量的确定 根据公式 Q=1000kVn，估算每孔注浆水泥用量， | score=0.0524
  - C8 | COLLECT | real_69c6ef484cca74801cb63bb9:L64 | 式中：Q-浆液总用量L | score=0.0524
  - C9 | COLLECT | real_69c6ef484cca74801cb63bb9:L70 | 5、注浆流量的选择 | score=0.0552
  - D7 | DISPATCH | real_69c6ef484cca74801cb63bb9:L70 | 5、注浆流量的选择 | score=0.0552
- projection_chars: 3472

**Step 3** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6ef484cca74801cb63bb9:L113` scope=`real_69c6ef484cca74801cb63bb9:L113` depth=`1`
- reason: Collect section 5.2.9 to find the table for grouting deviation and inspection methods.
- collect_section_ids: ['real_69c6ef484cca74801cb63bb9:L113']
- collect added=2 hits=2 branch_selected=True collect_full=True
- legal_actions (4):
  - C1 | COLLECT | real_69c6ef484cca74801cb63bb9:L113 | 5.2.9 检查验收 | score=0.0510
  - C2 | COLLECT | real_69c6ef484cca74801cb63bb9:L114 | 注浆结束28d后进行注浆检验，对地面下地基土进行轻型动力触探检测，检验注 浆加固效果。同时对已加固区域进行堆载试验。本工法加固地面后，效果显著，其 中部分塌陷地面底板还有所顶升，能满足现场的堆载重量要求。 | score=0.0510
  - C3 | COLLECT | real_69c6ef484cca74801cb63bb9:L115 | 图-10 水泥柱体及底板取样 | score=0.0299
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 738

**Step 4** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c6ef484cca74801cb63bb9:L113` depth=`1`
- reason: No further sections available to collect; insufficient evidence to answer query about specific tables and浆液拌制 requirements.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 190

**Step 5** `nav_dispatch`  id=`D14` kind=`dispatch` section=`real_69c6ef484cca74801cb63bb9:L113` scope=`None` depth=`0`
- reason: Dispatch to find the table with allowable deviations and inspection methods for grouting.
- dispatch_regions: ['real_69c6ef484cca74801cb63bb9:L113']
- child_reports=1 skipped=0
- legal_actions (50):
  - C1 | COLLECT | real_69c6ef484cca74801cb63bb9:L5 | 帷幕式注浆土体加固地基施工工法_2 | score=0.0657
  - D1 | DISPATCH | real_69c6ef484cca74801cb63bb9:L5 | 帷幕式注浆土体加固地基施工工法_2 | score=0.0657
  - C2 | COLLECT | real_69c6ef484cca74801cb63bb9:L7 | 传统注浆加固地基技术存在材料水泥水化反应慢、凝胶时间长、强度可靠性差 、串浆跑浆严重、加固影响区难以控制等缺陷。陕西建工第十一建设集团有限公司 根据深厚杂填土及地基处理的特性，采用帷幕式注浆+跳仓施工工艺解决了传统注浆 加固的强度可靠性差、串浆跑浆严重等问题，提高加固土体密实度，确保加固后地 面满足使用要求。 | score=0.0574
  - C3 | COLLECT | real_69c6ef484cca74801cb63bb9:L21 | 5.工艺流程及操作要点 | score=0.0657
  - D2 | DISPATCH | real_69c6ef484cca74801cb63bb9:L21 | 5.工艺流程及操作要点 | score=0.0657
  - C4 | COLLECT | real_69c6ef484cca74801cb63bb9:L22 | 5.1 工艺流程： | score=0.0657
  - D3 | DISPATCH | real_69c6ef484cca74801cb63bb9:L22 | 5.1 工艺流程： | score=0.0657
  - C5 | COLLECT | real_69c6ef484cca74801cb63bb9:L25 | 5.2.1 施工准备 | score=0.0552
  - D4 | DISPATCH | real_69c6ef484cca74801cb63bb9:L25 | 5.2.1 施工准备 | score=0.0552
  - C6 | COLLECT | real_69c6ef484cca74801cb63bb9:L36 | 6、选取试验段，应按照设计文件的要求，若设计文件没有要求的应根据地勘 报告选择有代表性的区域，面积以不大于20米*20米为宜。 | score=0.0478
  - C7 | COLLECT | real_69c6ef484cca74801cb63bb9:L38 | 1、注浆压力的确定： | score=0.0517
  - D5 | DISPATCH | real_69c6ef484cca74801cb63bb9:L38 | 1、注浆压力的确定： | score=0.0517
  - C8 | COLLECT | real_69c6ef484cca74801cb63bb9:L41 | Pe—注浆允许压力(MPa)； | score=0.0481
  - C9 | COLLECT | real_69c6ef484cca74801cb63bb9:L47 | 结合勘察报告和工程经验，C取0.3，T取0.3m，k取0.6，λ取0.8，h取0.3-3m。 通过计算，本次试验允许3m处注浆压力计算值0.50mpa，0.3m处注浆压力计算值 | score=0.0517
  - C10 | COLLECT | real_69c6ef484cca74801cb63bb9:L49 | 2、浆液扩散半径 | score=0.0512
  - D6 | DISPATCH | real_69c6ef484cca74801cb63bb9:L49 | 2、浆液扩散半径 | score=0.0512
- projection_chars: 3519

**Step 6** `nav_collect`  id=`C31` kind=`collect` section=`real_69c6ef484cca74801cb63bb9:L126` scope=`None` depth=`0`
- reason: Need to collect the JGJ79-2012 section to find the specific table for grouting deviation and inspection methods.
- collect_section_ids: ['real_69c6ef484cca74801cb63bb9:L126']
- collect added=2 hits=2 branch_selected=True collect_full=True
- legal_actions (47):
  - C1 | COLLECT | real_69c6ef484cca74801cb63bb9:L5 | 帷幕式注浆土体加固地基施工工法_2 | score=0.0657
  - D1 | DISPATCH | real_69c6ef484cca74801cb63bb9:L5 | 帷幕式注浆土体加固地基施工工法_2 | score=0.0657
  - C2 | COLLECT | real_69c6ef484cca74801cb63bb9:L7 | 传统注浆加固地基技术存在材料水泥水化反应慢、凝胶时间长、强度可靠性差 、串浆跑浆严重、加固影响区难以控制等缺陷。陕西建工第十一建设集团有限公司 根据深厚杂填土及地基处理的特性，采用帷幕式注浆+跳仓施工工艺解决了传统注浆 加固的强度可靠性差、串浆跑浆严重等问题，提高加固土体密实度，确保加固后地 面满足使用要求。 | score=0.0574
  - C3 | COLLECT | real_69c6ef484cca74801cb63bb9:L21 | 5.工艺流程及操作要点 | score=0.0657
  - D2 | DISPATCH | real_69c6ef484cca74801cb63bb9:L21 | 5.工艺流程及操作要点 | score=0.0657
  - C4 | COLLECT | real_69c6ef484cca74801cb63bb9:L22 | 5.1 工艺流程： | score=0.0657
  - D3 | DISPATCH | real_69c6ef484cca74801cb63bb9:L22 | 5.1 工艺流程： | score=0.0657
  - C5 | COLLECT | real_69c6ef484cca74801cb63bb9:L25 | 5.2.1 施工准备 | score=0.0552
  - D4 | DISPATCH | real_69c6ef484cca74801cb63bb9:L25 | 5.2.1 施工准备 | score=0.0552
  - C6 | COLLECT | real_69c6ef484cca74801cb63bb9:L36 | 6、选取试验段，应按照设计文件的要求，若设计文件没有要求的应根据地勘 报告选择有代表性的区域，面积以不大于20米*20米为宜。 | score=0.0478
  - C7 | COLLECT | real_69c6ef484cca74801cb63bb9:L38 | 1、注浆压力的确定： | score=0.0517
  - D5 | DISPATCH | real_69c6ef484cca74801cb63bb9:L38 | 1、注浆压力的确定： | score=0.0517
  - C8 | COLLECT | real_69c6ef484cca74801cb63bb9:L41 | Pe—注浆允许压力(MPa)； | score=0.0481
  - C9 | COLLECT | real_69c6ef484cca74801cb63bb9:L47 | 结合勘察报告和工程经验，C取0.3，T取0.3m，k取0.6，λ取0.8，h取0.3-3m。 通过计算，本次试验允许3m处注浆压力计算值0.50mpa，0.3m处注浆压力计算值 | score=0.0517
  - C10 | COLLECT | real_69c6ef484cca74801cb63bb9:L49 | 2、浆液扩散半径 | score=0.0512
  - D6 | DISPATCH | real_69c6ef484cca74801cb63bb9:L49 | 2、浆液扩散半径 | score=0.0512
- projection_chars: 3412

**Step 7** `nav_collect`  id=`C5` kind=`collect` section=`real_69c6ef484cca74801cb63bb9:L21` scope=`None` depth=`0`
- reason: Section 5 contains process details,浆液拌制 requirements, and likely the quality control table.
- collect_section_ids: ['real_69c6ef484cca74801cb63bb9:L21']
- collect added=56 hits=56 branch_selected=True collect_full=True
- legal_actions (47):
  - C1 | COLLECT | real_69c6ef484cca74801cb63bb9:L5 | 帷幕式注浆土体加固地基施工工法_2 | score=0.0657
  - D1 | DISPATCH | real_69c6ef484cca74801cb63bb9:L5 | 帷幕式注浆土体加固地基施工工法_2 | score=0.0657
  - C2 | COLLECT | real_69c6ef484cca74801cb63bb9:L7 | 传统注浆加固地基技术存在材料水泥水化反应慢、凝胶时间长、强度可靠性差 、串浆跑浆严重、加固影响区难以控制等缺陷。陕西建工第十一建设集团有限公司 根据深厚杂填土及地基处理的特性，采用帷幕式注浆+跳仓施工工艺解决了传统注浆 加固的强度可靠性差、串浆跑浆严重等问题，提高加固土体密实度，确保加固后地 面满足使用要求。 | score=0.0574
  - C3 | COLLECT | real_69c6ef484cca74801cb63bb9:L18 | 4.工艺原理 | score=0.0450
  - D2 | DISPATCH | real_69c6ef484cca74801cb63bb9:L18 | 4.工艺原理 | score=0.0450
  - C4 | COLLECT | real_69c6ef484cca74801cb63bb9:L19 | 本工法将待施工区划分为若干施工小仓，在每个小仓格四周环形布置帷幕式水 泥-水玻璃双液注浆孔，利用水泥-水玻璃双液浆快凝特点，在小仓格四周快速形成 封闭帷幕，有效避免串浆及跑浆现象。同时采用跳仓施工工艺，减少相邻区域变形 | score=0.0450
  - C5 | COLLECT | real_69c6ef484cca74801cb63bb9:L21 | 5.工艺流程及操作要点 | score=0.0657
  - D3 | DISPATCH | real_69c6ef484cca74801cb63bb9:L21 | 5.工艺流程及操作要点 | score=0.0657
  - C6 | COLLECT | real_69c6ef484cca74801cb63bb9:L22 | 5.1 工艺流程： | score=0.0657
  - D4 | DISPATCH | real_69c6ef484cca74801cb63bb9:L22 | 5.1 工艺流程： | score=0.0657
  - C7 | COLLECT | real_69c6ef484cca74801cb63bb9:L25 | 5.2.1 施工准备 | score=0.0552
  - D5 | DISPATCH | real_69c6ef484cca74801cb63bb9:L25 | 5.2.1 施工准备 | score=0.0552
  - C8 | COLLECT | real_69c6ef484cca74801cb63bb9:L36 | 6、选取试验段，应按照设计文件的要求，若设计文件没有要求的应根据地勘 报告选择有代表性的区域，面积以不大于20米*20米为宜。 | score=0.0478
  - C9 | COLLECT | real_69c6ef484cca74801cb63bb9:L38 | 1、注浆压力的确定： | score=0.0517
  - D6 | DISPATCH | real_69c6ef484cca74801cb63bb9:L38 | 1、注浆压力的确定： | score=0.0517
  - C10 | COLLECT | real_69c6ef484cca74801cb63bb9:L41 | Pe—注浆允许压力(MPa)； | score=0.0481
- projection_chars: 3499

**Step 8** `nav_collect`  id=`C34` kind=`collect` section=`real_69c6ef484cca74801cb63bb9:L123` scope=`None` depth=`0`
- reason: Collect Quality Control section to find the required table for grouting deviation and slurry mixing requirements.
- collect_section_ids: ['real_69c6ef484cca74801cb63bb9:L123']
- collect added=2 hits=2 branch_selected=True collect_full=True
- legal_actions (49):
  - C1 | COLLECT | real_69c6ef484cca74801cb63bb9:L1 | 帷幕式注浆土体加固地基施工工法 | score=0.0288
  - D1 | DISPATCH | real_69c6ef484cca74801cb63bb9:L5 | 帷幕式注浆土体加固地基施工工法_2 | score=0.0657
  - C2 | COLLECT | real_69c6ef484cca74801cb63bb9:L7 | 传统注浆加固地基技术存在材料水泥水化反应慢、凝胶时间长、强度可靠性差 、串浆跑浆严重、加固影响区难以控制等缺陷。陕西建工第十一建设集团有限公司 根据深厚杂填土及地基处理的特性，采用帷幕式注浆+跳仓施工工艺解决了传统注浆 加固的强度可靠性差、串浆跑浆严重等问题，提高加固土体密实度，确保加固后地 面满足使用要求。 | score=0.0574
  - C3 | COLLECT | real_69c6ef484cca74801cb63bb9:L8 | 2.工法特点 | score=0.0353
  - D2 | DISPATCH | real_69c6ef484cca74801cb63bb9:L8 | 2.工法特点 | score=0.0353
  - C4 | COLLECT | real_69c6ef484cca74801cb63bb9:L13 | 2.3 跳仓施工 | score=0.0353
  - D3 | DISPATCH | real_69c6ef484cca74801cb63bb9:L13 | 2.3 跳仓施工 | score=0.0353
  - C5 | COLLECT | real_69c6ef484cca74801cb63bb9:L14 | 采用跳仓施工，隔孔注入，避免相邻分仓的注浆互相影响，保证施工质量。 2.4 适用性强 | score=0.0353
  - C6 | COLLECT | real_69c6ef484cca74801cb63bb9:L18 | 4.工艺原理 | score=0.0450
  - D4 | DISPATCH | real_69c6ef484cca74801cb63bb9:L18 | 4.工艺原理 | score=0.0450
  - C7 | COLLECT | real_69c6ef484cca74801cb63bb9:L19 | 本工法将待施工区划分为若干施工小仓，在每个小仓格四周环形布置帷幕式水 泥-水玻璃双液注浆孔，利用水泥-水玻璃双液浆快凝特点，在小仓格四周快速形成 封闭帷幕，有效避免串浆及跑浆现象。同时采用跳仓施工工艺，减少相邻区域变形 | score=0.0450
  - C8 | COLLECT | real_69c6ef484cca74801cb63bb9:L20 | 影响，最终使中间区域土粒和浆液强制混合凝固，强化土体密实度，实现原有地面 下土体加固，恢复原有地面的使用功能。 | score=0.0321
  - D5 | DISPATCH | real_69c6ef484cca74801cb63bb9:L88 | 图-5 放线、标记点位 | score=0.0510
  - C9 | COLLECT | real_69c6ef484cca74801cb63bb9:L89 | 5.2.6 钻孔 | score=0.0425
  - D6 | DISPATCH | real_69c6ef484cca74801cb63bb9:L89 | 5.2.6 钻孔 | score=0.0425
  - C10 | COLLECT | real_69c6ef484cca74801cb63bb9:L91 | - 2、开钻前的钻头点位与布孔点之距相差不得大于2cm，钻杆角度偏差不得大于1 | score=0.0315
- projection_chars: 3340

**Step 9** `nav_collect`  id=`C15` kind=`collect` section=`real_69c6ef484cca74801cb63bb9:L99` scope=`None` depth=`0`
- reason: Collects浆液拌制操作要求 and injection material specs needed for the query.
- collect_section_ids: ['real_69c6ef484cca74801cb63bb9:L99']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (49):
  - C1 | COLLECT | real_69c6ef484cca74801cb63bb9:L1 | 帷幕式注浆土体加固地基施工工法 | score=0.0288
  - D1 | DISPATCH | real_69c6ef484cca74801cb63bb9:L5 | 帷幕式注浆土体加固地基施工工法_2 | score=0.0657
  - C2 | COLLECT | real_69c6ef484cca74801cb63bb9:L7 | 传统注浆加固地基技术存在材料水泥水化反应慢、凝胶时间长、强度可靠性差 、串浆跑浆严重、加固影响区难以控制等缺陷。陕西建工第十一建设集团有限公司 根据深厚杂填土及地基处理的特性，采用帷幕式注浆+跳仓施工工艺解决了传统注浆 加固的强度可靠性差、串浆跑浆严重等问题，提高加固土体密实度，确保加固后地 面满足使用要求。 | score=0.0574
  - C3 | COLLECT | real_69c6ef484cca74801cb63bb9:L8 | 2.工法特点 | score=0.0353
  - D2 | DISPATCH | real_69c6ef484cca74801cb63bb9:L8 | 2.工法特点 | score=0.0353
  - C4 | COLLECT | real_69c6ef484cca74801cb63bb9:L13 | 2.3 跳仓施工 | score=0.0353
  - D3 | DISPATCH | real_69c6ef484cca74801cb63bb9:L13 | 2.3 跳仓施工 | score=0.0353
  - C5 | COLLECT | real_69c6ef484cca74801cb63bb9:L14 | 采用跳仓施工，隔孔注入，避免相邻分仓的注浆互相影响，保证施工质量。 2.4 适用性强 | score=0.0353
  - C6 | COLLECT | real_69c6ef484cca74801cb63bb9:L18 | 4.工艺原理 | score=0.0450
  - D4 | DISPATCH | real_69c6ef484cca74801cb63bb9:L18 | 4.工艺原理 | score=0.0450
  - C7 | COLLECT | real_69c6ef484cca74801cb63bb9:L19 | 本工法将待施工区划分为若干施工小仓，在每个小仓格四周环形布置帷幕式水 泥-水玻璃双液注浆孔，利用水泥-水玻璃双液浆快凝特点，在小仓格四周快速形成 封闭帷幕，有效避免串浆及跑浆现象。同时采用跳仓施工工艺，减少相邻区域变形 | score=0.0450
  - C8 | COLLECT | real_69c6ef484cca74801cb63bb9:L20 | 影响，最终使中间区域土粒和浆液强制混合凝固，强化土体密实度，实现原有地面 下土体加固，恢复原有地面的使用功能。 | score=0.0321
  - D5 | DISPATCH | real_69c6ef484cca74801cb63bb9:L88 | 图-5 放线、标记点位 | score=0.0510
  - C9 | COLLECT | real_69c6ef484cca74801cb63bb9:L89 | 5.2.6 钻孔 | score=0.0425
  - D6 | DISPATCH | real_69c6ef484cca74801cb63bb9:L89 | 5.2.6 钻孔 | score=0.0425
  - C10 | COLLECT | real_69c6ef484cca74801cb63bb9:L91 | - 2、开钻前的钻头点位与布孔点之距相差不得大于2cm，钻杆角度偏差不得大于1 | score=0.0315
- projection_chars: 3352

**Step 10** `nav_collect`  id=`C14` kind=`collect` section=`real_69c6ef484cca74801cb63bb9:L97` scope=`None` depth=`0`
- reason: Collect浆液拌制操作要求(C15)和注浆终孔标准/检验表相关部分(C23) to answer query.
- collect_section_ids: ['real_69c6ef484cca74801cb63bb9:L97', 'real_69c6ef484cca74801cb63bb9:L98', 'real_69c6ef484cca74801cb63bb9:L107']
- collect added=13 hits=15 branch_selected=False collect_full=True
- legal_actions (37):
  - C1 | COLLECT | real_69c6ef484cca74801cb63bb9:L1 | 帷幕式注浆土体加固地基施工工法 | score=0.0288
  - C2 | COLLECT | real_69c6ef484cca74801cb63bb9:L7 | 传统注浆加固地基技术存在材料水泥水化反应慢、凝胶时间长、强度可靠性差 、串浆跑浆严重、加固影响区难以控制等缺陷。陕西建工第十一建设集团有限公司 根据深厚杂填土及地基处理的特性，采用帷幕式注浆+跳仓施工工艺解决了传统注浆 加固的强度可靠性差、串浆跑浆严重等问题，提高加固土体密实度，确保加固后地 面满足使用要求。 | score=0.0574
  - C3 | COLLECT | real_69c6ef484cca74801cb63bb9:L8 | 2.工法特点 | score=0.0353
  - C4 | COLLECT | real_69c6ef484cca74801cb63bb9:L13 | 2.3 跳仓施工 | score=0.0353
  - C5 | COLLECT | real_69c6ef484cca74801cb63bb9:L14 | 采用跳仓施工，隔孔注入，避免相邻分仓的注浆互相影响，保证施工质量。 2.4 适用性强 | score=0.0353
  - C6 | COLLECT | real_69c6ef484cca74801cb63bb9:L18 | 4.工艺原理 | score=0.0450
  - C7 | COLLECT | real_69c6ef484cca74801cb63bb9:L19 | 本工法将待施工区划分为若干施工小仓，在每个小仓格四周环形布置帷幕式水 泥-水玻璃双液注浆孔，利用水泥-水玻璃双液浆快凝特点，在小仓格四周快速形成 封闭帷幕，有效避免串浆及跑浆现象。同时采用跳仓施工工艺，减少相邻区域变形 | score=0.0450
  - C8 | COLLECT | real_69c6ef484cca74801cb63bb9:L20 | 影响，最终使中间区域土粒和浆液强制混合凝固，强化土体密实度，实现原有地面 下土体加固，恢复原有地面的使用功能。 | score=0.0321
  - C9 | COLLECT | real_69c6ef484cca74801cb63bb9:L89 | 5.2.6 钻孔 | score=0.0425
  - C10 | COLLECT | real_69c6ef484cca74801cb63bb9:L91 | - 2、开钻前的钻头点位与布孔点之距相差不得大于2cm，钻杆角度偏差不得大于1 | score=0.0315
  - C11 | COLLECT | real_69c6ef484cca74801cb63bb9:L92 | - °。在钻进过程中，采用压浆泵不断的压入少量水泥浆液进行护壁和冲孔。先施工 帷幕，后施工内部，注浆应跳孔注浆。 | score=0.0425
  - C12 | COLLECT | real_69c6ef484cca74801cb63bb9:L93 | - 3、周边止水帷幕注浆孔孔径100mm，间距3000mm。帷幕内孔径100mm，间距 | score=0.0274
  - C13 | COLLECT | real_69c6ef484cca74801cb63bb9:L95 | - 4、帷幕区注浆孔需穿透填土层，保证注浆料进入黄土层不小于3米。 | score=0.0352
  - C14 | COLLECT | real_69c6ef484cca74801cb63bb9:L97 | 5.2.7 注浆 | score=0.0505
  - C15 | COLLECT | real_69c6ef484cca74801cb63bb9:L98 | - 1、水泥浆搅拌 | score=0.0340
  - C16 | COLLECT | real_69c6ef484cca74801cb63bb9:L100 | - 2、注浆泵试运转 | score=0.0327
- projection_chars: 3061

### Subagent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c6ef484cca74801cb63bb9:L113 (ok)
collected 3 branch node(s); explicit roots=['real_69c6ef484cca74801cb63bb9:L113']
collected: real_69c6ef484cca74801cb63bb9:L113, real_69c6ef484cca74801cb63bb9:L114, real_69c6ef484cca74801cb63bb9:L115
reason: No further sections available to collect; insufficient evidence to answer query about specific tables and浆液拌制 requirements.
---
=== End Investigate ===
```

### Evidence text (new)

```
[E1]
[§ 7.2 主要控制措施]
注浆允许偏差及检验办法应符合表7.2.1的规定。

[E2]
[§ 5.2.7 注浆]
  确定注浆系统各部分连接无误后，开动注浆泵压水试验，检查注浆泵液压情况 ，系统管路有否漏浆，管路是否畅通。
  据地层及注浆压力进行调整，通过压力表观察注浆压力。注浆管每次上拔高度应为 33cm，为防止注浆管对后续施工产生危害，严禁将注浆管拔断掉落在阀管中。
  4、注浆终孔标准
  ②注浆压力上升缓慢，当注浆量达到设计要求，并确认未发生跑浆或漏浆； ③循环达到下述条件可结束注浆：设计的注浆孔均满足单根结束标准结束注浆 ，无漏注现象。
  - 1、水泥浆搅拌
  注浆前，严格按照配方配料。其中帷幕采用AB液作为注浆材料，A液∶B液=1∶1 ，其中A液：水泥：水=0.8∶1；B液：中性水玻璃，水玻璃为波美度25°～30°；帷 幕中心区采用纯水泥浆作为注浆材料，注浆水泥采用强度等级为Po42.5R普通水泥。 施工用水采用自来水。浆液应搅拌均匀，随拌随注，不得长时间存放已拌好的浆液 。封闭泥浆用泵从钻杆自下而上压入孔内，不准从孔口到入。
```

### Evidence text (old)

```
[E1]
[§ 表7.2.1注浆检查项目要求及检验方法 / 7.3 加强施工测量，确保钻杆竖直，位置满足规范要求。]
- 7.6 浆液拌制严格按配合比要求，并在拌浆现场悬挂配比牌。浆体必须经搅拌机充分 搅拌均匀，方可开始压浆，浆体在泵送前经筛网过滤。

[E2]
[§ 《建筑地基处理技术规范》JGJ79-2012 / 7.2 主要控制措施]
注浆允许偏差及检验办法应符合表7.2.1的规定。

[E3]
[§ 表7.2.1注浆检查项目要求及检验方法 / 8.安全措施 / 8.1 安全管理规范]
- 《建筑施工安全检查标准》JGJ59-2011

[E4]
[§ 表7.2.1注浆检查项目要求及检验方法 / 8.安全措施 / 8.2安全保证措施]
- ，三级箱必须配置到位，手持式电动设备必须经过漏电保护装置。

[E5]
[§ 表7.2.1注浆检查项目要求及检验方法 / 8.安全措施 / 8.2安全保证措施]
- 8.2.5 在进行浆液配置时，操作人员应佩戴护目镜、口罩等劳保用品，防止进入口

[E6]
[§ 表7.2.1注浆检查项目要求及检验方法 / 7.3 加强施工测量，确保钻杆竖直，位
```

## real_69cb12d0919452cda2225a0b_scope_collection_auto_0076 (scope_collection)

**Query:** 列出办理《跨区域涉税事项备案》时需注意的所有事项要点。

**Doc:** `real_69cb12d0919452cda2225a0b`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 401 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 6 | 4 |
| trajectory_steps | n/a | 5 |

### Gold node hits (new)

- `real_69cb12d0919452cda2225a0b:L141` [MISS] retrieved=False in_text=False
- `real_69cb12d0919452cda2225a0b:L142` [MISS] retrieved=False in_text=False
- `real_69cb12d0919452cda2225a0b:L143` [MISS] retrieved=False in_text=False
- `real_69cb12d0919452cda2225a0b:L144` [MISS] retrieved=False in_text=False
- `real_69cb12d0919452cda2225a0b:L145` [MISS] retrieved=False in_text=False
- `real_69cb12d0919452cda2225a0b:L146` [MISS] retrieved=False in_text=False
- `real_69cb12d0919452cda2225a0b:L147` [MISS] retrieved=False in_text=False
- `real_69cb12d0919452cda2225a0b:L148` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C4` kind=`collect` section=`real_69cb12d0919452cda2225a0b:L128` scope=`real_69cb12d0919452cda2225a0b:L124` depth=`1`
- reason: Collects the section listing all key points for handling cross-regional tax filing.
- collect_section_ids: ['real_69cb12d0919452cda2225a0b:L128']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (16):
  - C1 | COLLECT | real_69cb12d0919452cda2225a0b:L124 | **3.2.4** 《跨区域涉税事项报告》管理 | score=0.0730
  - C2 | COLLECT | real_69cb12d0919452cda2225a0b:L125 | 根据《中华人民共和国税收征收管理法实施细则》第二十一条规定：从事生产、经 营的纳税人到外县（市）临时从事生产、经营活动的，应当持税务登记证副本和所在地 税务机关填开的外出经营活动税收管理证明，向营业地税务机关报验登记，接受税务管 理。集团公司注册地址为咸阳市，除在注册地市所辖范围以内区域（渭城区、秦都区） 承接的工程项目不需办理《跨区域涉税事项备案表》，在其他地区承接的工程项目均需 办理《跨区域涉 | score=0.0715
  - C3 | COLLECT | real_69cb12d0919452cda2225a0b:L127 | 《跨区域涉税事项报告》的办理由项目部财务人员发起申请，将所需办理备案项目 的合同扫描件或原件提供至税务业务岗，由税务业务岗在国家税务总局陕西省电子税务 局上进行办理，严格按照合同内容，提交办理《跨区域涉税事项报告》，办理时限不得 超过两个工作日。 | score=0.0716
  - C4 | COLLECT | real_69cb12d0919452cda2225a0b:L128 | 办理跨区域涉税事项备案需注意事项： | score=0.0730
  - C5 | COLLECT | real_69cb12d0919452cda2225a0b:L130 | - 2）项目地址：不是甲方机构所在地，应填写项目所在地省、市、区（县）。（注意： | score=0.0613
  - C6 | COLLECT | real_69cb12d0919452cda2225a0b:L134 | - 5）《跨区域涉税事项报告》自办理之日起 30 日内在项目所在地税务机关报验，到 | score=0.0638
  - C7 | COLLECT | real_69cb12d0919452cda2225a0b:L136 | - 6）《跨区域涉税事项报告》政策如有变化，依照国家税务总局政策适时调整。 （2）延期与核销 | score=0.0601
  - C8 | COLLECT | real_69cb12d0919452cda2225a0b:L137 | 《跨区域涉税事项报告》办理完成后 30 天之内，项目部应向工程项目所在地主管税 务机关进行报验登记，并按照《中华人民共和国税收征收管理办法》及其实施细则的有 关规定进行经营和纳税。 | score=0.0648
  - C9 | COLLECT | real_69cb12d0919452cda2225a0b:L139 | 在项目所在地税务机关报验时，需提供以下资料： | score=0.0609
  - C10 | COLLECT | real_69cb12d0919452cda2225a0b:L140 | - 1）《跨区域涉税事项报告》 | score=0.0574
  - C11 | COLLECT | real_69cb12d0919452cda2225a0b:L145 | - 《跨区域涉税事项报告》初次办理有效期为 360 天，到期日项目未完工的，应于到 | score=0.0646
  - C12 | COLLECT | real_69cb12d0919452cda2225a0b:L148 | - 并将已核销的备案表交回集团财务管理服务中心留存。 | score=0.0586
  - C13 | COLLECT | real_69cb12d0919452cda2225a0b:L149 | - 办理核销，需向项目所在地税务机关提供以下资料： | score=0.0590
  - C14 | COLLECT | real_69cb12d0919452cda2225a0b:L150 | - 1）《跨区域涉税事项报告》 | score=0.0576
  - C15 | COLLECT | real_69cb12d0919452cda2225a0b:L154 | - 5）《跨区域涉税事项报告》所属期间，所有发票复印件以及完税证复印件。 | score=0.0605
  - C16 | COLLECT | real_69cb12d0919452cda2225a0b:L157 | 项目部办理完跨区域涉税事项备案之后，应当留存电子版备案表，并建立《跨区域 涉税事项备案台账》（SJSYJ-CWGL-FJ-005），台账应包括建设单位名称、项目名称、 合同金额、开具日期、到期日期、编号、责任人、核销时间、核销金额，以及已交增值 税、企业所得税、城建税、教育费、地方教育费、水利基金、印花税金额。 | score=0.0701
- projection_chars: 3003

**Step 2** `nav_collect`  id=`C1` kind=`collect` section=`real_69cb12d0919452cda2225a0b:L124` scope=`real_69cb12d0919452cda2225a0b:L124` depth=`1`
- reason: Collect all remaining sections under C1 to gather complete requirements for cross-regional tax filing.
- collect_section_ids: ['real_69cb12d0919452cda2225a0b:L124', 'real_69cb12d0919452cda2225a0b:L125', 'real_69cb12d0919452cda2225a0b:L127', 'real_69cb12d0919452cda2225a0b:L130', 'real_69cb12d0919452cda2225a0b:L134', 'real_69cb12d0919452cda2225a0b:L136', 'real_69cb12d0919452cda2225a0b:L137', 'real_69cb12d0919452cda2225a0b:L139', 'real_69cb12d0919452cda2225a0b:L140', 'real_69cb12d0919452cda2225a0b:L145', 'real_69cb12d0919452cda2225a0b:L148', 'real_69cb12d0919452cda2225a0b:L149', 'real_69cb12d0919452cda2225a0b:L150', 'real_69cb12d0919452cda2225a0b:L154', 'real_69cb12d0919452cda2225a0b:L155', 'real_69cb12d0919452cda2225a0b:L157']
- collect added=33 hits=48 branch_selected=False collect_full=True
- legal_actions (17):
  - C1 | COLLECT | real_69cb12d0919452cda2225a0b:L124 | **3.2.4** 《跨区域涉税事项报告》管理 | score=0.0730
  - C2 | COLLECT | real_69cb12d0919452cda2225a0b:L125 | 根据《中华人民共和国税收征收管理法实施细则》第二十一条规定：从事生产、经 营的纳税人到外县（市）临时从事生产、经营活动的，应当持税务登记证副本和所在地 税务机关填开的外出经营活动税收管理证明，向营业地税务机关报验登记，接受税务管 理。集团公司注册地址为咸阳市，除在注册地市所辖范围以内区域（渭城区、秦都区） 承接的工程项目不需办理《跨区域涉税事项备案表》，在其他地区承接的工程项目均需 办理《跨区域涉 | score=0.0715
  - C3 | COLLECT | real_69cb12d0919452cda2225a0b:L127 | 《跨区域涉税事项报告》的办理由项目部财务人员发起申请，将所需办理备案项目 的合同扫描件或原件提供至税务业务岗，由税务业务岗在国家税务总局陕西省电子税务 局上进行办理，严格按照合同内容，提交办理《跨区域涉税事项报告》，办理时限不得 超过两个工作日。 | score=0.0716
  - C4 | COLLECT | real_69cb12d0919452cda2225a0b:L130 | - 2）项目地址：不是甲方机构所在地，应填写项目所在地省、市、区（县）。（注意： | score=0.0613
  - C5 | COLLECT | real_69cb12d0919452cda2225a0b:L134 | - 5）《跨区域涉税事项报告》自办理之日起 30 日内在项目所在地税务机关报验，到 | score=0.0638
  - C6 | COLLECT | real_69cb12d0919452cda2225a0b:L136 | - 6）《跨区域涉税事项报告》政策如有变化，依照国家税务总局政策适时调整。 （2）延期与核销 | score=0.0601
  - C7 | COLLECT | real_69cb12d0919452cda2225a0b:L137 | 《跨区域涉税事项报告》办理完成后 30 天之内，项目部应向工程项目所在地主管税 务机关进行报验登记，并按照《中华人民共和国税收征收管理办法》及其实施细则的有 关规定进行经营和纳税。 | score=0.0648
  - C8 | COLLECT | real_69cb12d0919452cda2225a0b:L139 | 在项目所在地税务机关报验时，需提供以下资料： | score=0.0609
  - C9 | COLLECT | real_69cb12d0919452cda2225a0b:L140 | - 1）《跨区域涉税事项报告》 | score=0.0574
  - C10 | COLLECT | real_69cb12d0919452cda2225a0b:L145 | - 《跨区域涉税事项报告》初次办理有效期为 360 天，到期日项目未完工的，应于到 | score=0.0646
  - C11 | COLLECT | real_69cb12d0919452cda2225a0b:L148 | - 并将已核销的备案表交回集团财务管理服务中心留存。 | score=0.0586
  - C12 | COLLECT | real_69cb12d0919452cda2225a0b:L149 | - 办理核销，需向项目所在地税务机关提供以下资料： | score=0.0590
  - C13 | COLLECT | real_69cb12d0919452cda2225a0b:L150 | - 1）《跨区域涉税事项报告》 | score=0.0576
  - C14 | COLLECT | real_69cb12d0919452cda2225a0b:L154 | - 5）《跨区域涉税事项报告》所属期间，所有发票复印件以及完税证复印件。 | score=0.0605
  - C15 | COLLECT | real_69cb12d0919452cda2225a0b:L155 | - 上述所有向税务机关提供的资料，必须都要加盖集团公章。 | score=0.0573
  - C16 | COLLECT | real_69cb12d0919452cda2225a0b:L157 | 项目部办理完跨区域涉税事项备案之后，应当留存电子版备案表，并建立《跨区域 涉税事项备案台账》（SJSYJ-CWGL-FJ-005），台账应包括建设单位名称、项目名称、 合同金额、开具日期、到期日期、编号、责任人、核销时间、核销金额，以及已交增值 税、企业所得税、城建税、教育费、地方教育费、水利基金、印花税金额。 | score=0.0701
- projection_chars: 3054

**Step 3** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69cb12d0919452cda2225a0b:L124` depth=`1`
- reason: Collected sections L124 and L128 contain the required points for cross-regional tax filing. Ready to finish.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 190

**Step 4** `nav_dispatch`  id=`D2` kind=`dispatch` section=`real_69cb12d0919452cda2225a0b:L124` scope=`None` depth=`0`
- reason: Dispatch section 3.2.4 to collect all details on cross-regional tax filing requirements and precautions.
- dispatch_regions: ['real_69cb12d0919452cda2225a0b:L124']
- child_reports=1 skipped=0
- legal_actions (35):
  - C1 | COLLECT | real_69cb12d0919452cda2225a0b:L26 | **1.4.2** 专业术语和定义 | score=0.0637
  - D1 | DISPATCH | real_69cb12d0919452cda2225a0b:L26 | **1.4.2** 专业术语和定义 | score=0.0637
  - C2 | COLLECT | real_69cb12d0919452cda2225a0b:L32 | 《跨区域涉税事项报告》：在集团注册地以外地区承接的工程项目，办理的异地经 营许可证明。 | score=0.0637
  - C3 | COLLECT | real_69cb12d0919452cda2225a0b:L124 | **3.2.4** 《跨区域涉税事项报告》管理 | score=0.0730
  - D2 | DISPATCH | real_69cb12d0919452cda2225a0b:L124 | **3.2.4** 《跨区域涉税事项报告》管理 | score=0.0730
  - C4 | COLLECT | real_69cb12d0919452cda2225a0b:L125 | 根据《中华人民共和国税收征收管理法实施细则》第二十一条规定：从事生产、经 营的纳税人到外县（市）临时从事生产、经营活动的，应当持税务登记证副本和所在地 税务机关填开的外出经营活动税收管理证明，向营业地税务机关报验登记，接受税务管 理。集团公司注册地址为咸阳市，除在注册地市所辖范围以内区域（渭城区、秦都区） 承接的工程项目不需办理《跨区域涉税事项备案表》，在其他地区承接的工程项目均需 办理《跨区域涉 | score=0.0715
  - C5 | COLLECT | real_69cb12d0919452cda2225a0b:L127 | 《跨区域涉税事项报告》的办理由项目部财务人员发起申请，将所需办理备案项目 的合同扫描件或原件提供至税务业务岗，由税务业务岗在国家税务总局陕西省电子税务 局上进行办理，严格按照合同内容，提交办理《跨区域涉税事项报告》，办理时限不得 超过两个工作日。 | score=0.0716
  - C6 | COLLECT | real_69cb12d0919452cda2225a0b:L128 | 办理跨区域涉税事项备案需注意事项： | score=0.0730
  - C7 | COLLECT | real_69cb12d0919452cda2225a0b:L130 | - 2）项目地址：不是甲方机构所在地，应填写项目所在地省、市、区（县）。（注意： | score=0.0613
  - C8 | COLLECT | real_69cb12d0919452cda2225a0b:L131 | - 新设立开发区、西咸新区、高新区等应与项目所在地税务机关确认对方所属行政区划后 再填写相对应行政辖区名称） | score=0.0530
  - C9 | COLLECT | real_69cb12d0919452cda2225a0b:L134 | - 5）《跨区域涉税事项报告》自办理之日起 30 日内在项目所在地税务机关报验，到 | score=0.0638
  - C10 | COLLECT | real_69cb12d0919452cda2225a0b:L135 | - 期日前 15 日在所在地税务机关申报核销，如遇法定节假日，需提前处理。 | score=0.0526
  - C11 | COLLECT | real_69cb12d0919452cda2225a0b:L136 | - 6）《跨区域涉税事项报告》政策如有变化，依照国家税务总局政策适时调整。 （2）延期与核销 | score=0.0601
  - C12 | COLLECT | real_69cb12d0919452cda2225a0b:L137 | 《跨区域涉税事项报告》办理完成后 30 天之内，项目部应向工程项目所在地主管税 务机关进行报验登记，并按照《中华人民共和国税收征收管理办法》及其实施细则的有 关规定进行经营和纳税。 | score=0.0648
  - C13 | COLLECT | real_69cb12d0919452cda2225a0b:L139 | 在项目所在地税务机关报验时，需提供以下资料： | score=0.0609
  - C14 | COLLECT | real_69cb12d0919452cda2225a0b:L140 | - 1）《跨区域涉税事项报告》 | score=0.0574
- projection_chars: 3387

**Step 5** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Collected sections L124 and L128 contain the required points for cross-regional tax filing.
- legal_actions (45):
  - C1 | COLLECT | real_69cb12d0919452cda2225a0b:L26 | **1.4.2** 专业术语和定义 | score=0.0637
  - D1 | DISPATCH | real_69cb12d0919452cda2225a0b:L26 | **1.4.2** 专业术语和定义 | score=0.0637
  - C2 | COLLECT | real_69cb12d0919452cda2225a0b:L32 | 《跨区域涉税事项报告》：在集团注册地以外地区承接的工程项目，办理的异地经 营许可证明。 | score=0.0637
  - C3 | COLLECT | real_69cb12d0919452cda2225a0b:L54 | **3.1.1** 进项税额定义 | score=0.0448
  - D2 | DISPATCH | real_69cb12d0919452cda2225a0b:L54 | **3.1.1** 进项税额定义 | score=0.0448
  - C4 | COLLECT | real_69cb12d0919452cda2225a0b:L57 | 收取进项发票，应核实业务的真实性、票面信息完整性。业务真实性指此笔业务是 否真实发生，确保“货物、劳务及服务流”、“资金流”、“发票流”、“合同流”保 持四流一致。票面信息完整性指发票购买方信息应与集团开票信息一致；发票内容完整、 发票备注栏注明项目名称以及建筑服务发生地所在省、市、区（县）；发票内容清晰可 辨；发票正反两面干净整洁，不允许出现脏、乱及签字的痕迹；发票抵扣联不可折叠， 不能污损，密 | score=0.0448
  - C5 | COLLECT | real_69cb12d0919452cda2225a0b:L58 | **3.1.3** 进项税发票传递 | score=0.0497
  - D3 | DISPATCH | real_69cb12d0919452cda2225a0b:L58 | **3.1.3** 进项税发票传递 | score=0.0497
  - C6 | COLLECT | real_69cb12d0919452cda2225a0b:L59 | 传递进项税发票时，应登记进项税发票传递单（SJSYJ-CWGL-FJ-001），传递单内 应按照集团公司统一格式要求，内容包括所属公司、项目名称、是否勾选、发票代码、 发票号码、开票日期、税额、有效抵扣税额、销方名称、销方税号、金额、用途、发票 类型，确保当月所有入账的进项税发票与台账中列明的进项税发票以及进项税发票抵扣 联金额、份数相一致后，于当月最后一个工作日之前，将发票台账以及发票抵扣联传递 | score=0.0497
  - C7 | COLLECT | real_69cb12d0919452cda2225a0b:L60 | **3.1.4** 进项税发票认证 | score=0.0424
  - D4 | DISPATCH | real_69cb12d0919452cda2225a0b:L60 | **3.1.4** 进项税发票认证 | score=0.0424
  - C8 | COLLECT | real_69cb12d0919452cda2225a0b:L61 | 集团财务管理服务中心收到进项税发票台账以及发票抵扣联之后，应对所有台账进 行汇总，并进入国家税务总局发票管理平台进行勾选认证发票，确保台账内列明的发票 份数、金额、税额与发票管理平台内认证的相一致后，方可提交认证。如出现不一致现 象，应对发票逐一进行核对，至台账与平台认证信息一致为止。 | score=0.0424
  - C9 | COLLECT | real_69cb12d0919452cda2225a0b:L79 | 税额： | score=0.0438
  - D5 | DISPATCH | real_69cb12d0919452cda2225a0b:L79 | 税额： | score=0.0438
  - C10 | COLLECT | real_69cb12d0919452cda2225a0b:L92 | 注意事项： | score=0.0438
  - C11 | COLLECT | real_69cb12d0919452cda2225a0b:L114 | **3.2.3** 销项税发票的领用及保管 | score=0.0420
- projection_chars: 3710

### Subagent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69cb12d0919452cda2225a0b:L124 (ok)
collected 34 branch node(s); explicit roots=['real_69cb12d0919452cda2225a0b:L128', 'real_69cb12d0919452cda2225a0b:L124']
collected: real_69cb12d0919452cda2225a0b:L124, real_69cb12d0919452cda2225a0b:L125, real_69cb12d0919452cda2225a0b:L126, real_69cb12d0919452cda2225a0b:L127, real_69cb12d0919452cda2225a0b:L128, real_69cb12d0919452cda2225a0b:L129, real_69cb12d0919452cda2225a0b:L130, real_69cb12d0919452cda2225a0b:L131, real_69cb12d0919452cda2225a0b:L132, real_69cb12d0919452cda2225a0b:L133, real_69cb12d0919452cda2225a0b:L134, real_69cb12d0919452cda2225a0b:L135, real_69cb12d0919452cda2225a0b:L136, real_69cb12d0919452cda2225a0b:L137, real_69cb12d0919452cda2225a0b:L138, real_69cb12d0919452cda2225a0b:L139, real_69cb12d0919452cda2225a0b:L140, real_69cb12d0919452cda2225a0b:L141, real_69cb12d0919452cda2225a0b:L142, real_69cb12d0919452cda2225a0b:L143
reason: Collected sections L124 and L128 contain the required points for cross-regional tax filing. Ready to finish.
---
=== End Investigate ===
```

### Evidence text (new)

```
[E1]
[§ **3.2.4** 《跨区域涉税事项报告》管理]
  根据《中华人民共和国税收征收管理法实施细则》第二十一条规定：从事生产、经 营的纳税人到外县（市）临时从事生产、经营活动的，应当持税务登记证副本和所在地 税务机关填开的外出经营活动税收管理证明，向营业地税务机关报验登记，接受税务管 理。集团公司注册地址为咸阳市，除在注册地市所辖范围以内区域（渭城区、秦都区） 承接的工程项目不需办理《跨区域涉税事项备案表》，在其他地区承接的工程项目均需 办理《跨区域涉税事项备案表》，并在项目所在地预缴税款。
  《跨区域涉税事项报告》的办理由项目部财务人员发起申请，将所需办理备案项目 的合同扫描件或原件提供至税务业务岗，由税务业务岗在国家税务总局陕西省电子税务 局上进行办理，严格按照合同内容，提交办理《跨区域涉税事项报告》，办理时限不得 超过两个工作日。
  办理跨区域涉税事项备案需注意事项：
```

### Evidence text (old)

```
[E1]
[§ **3.2.4** 《跨区域涉税事项报告》管理]
办理跨区域涉税事项备案需注意事项：

[E2]
[§ **7.8** 跨区域涉税事项风险预警防范]
项目会计应按要求登记《跨区域涉税事项备案台账》（SJSYJ-CWGL-FJ-005），月 末对次月将要到期的跨区域涉税事项进行梳理，在到期前十日内办理核销或续办。

[E3]
[§ **3.2.4** 《跨区域涉税事项报告》管理]
项目部办理完跨区域涉税事项备案之后，应当留存电子版备案表，并建立《跨区域 涉税事项备案台账》（SJSYJ-CWGL-FJ-005），台账应包括建设单位名称、项目名称、 合同金额、开具日期、到期日期、编号、责任人、核销时间、核销金额，以及已交增值 税、企业所得税、城建税、教育费、地方教育费、水利基金、印花

[E4]
[§ **3.2.4** 《跨区域涉税事项报告》管理]
《跨区域涉税事项报告》的办理由项目部财务人员发起申请，将所需办理备案项目 的合同扫描件或原件提供至税务业务岗，由税务业务岗在国家税务总局陕西省电子税务 局上进行办理，严格按照合同内容，提交办理《跨区域涉税事项报告》，办理时限不得
```

## real_69c60974d4242eda8c47c615_scope_collection_auto_0030 (scope_collection)

**Query:** 列出重大事故隐患治理方案必须包含的所有内容要素。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 499 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 12 | 12 |
| trajectory_steps | n/a | 13 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L94` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L95` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L96` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L97` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L98` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L99` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60974d4242eda8c47c615:L92` scope=`real_69c60974d4242eda8c47c615:L92` depth=`1`
- reason: Collect the section defining the major accident hazard governance plan and its required content elements.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L92', 'real_69c60974d4242eda8c47c615:L93', 'real_69c60974d4242eda8c47c615:L94', 'real_69c60974d4242eda8c47c615:L95', 'real_69c60974d4242eda8c47c615:L96', 'real_69c60974d4242eda8c47c615:L97', 'real_69c60974d4242eda8c47c615:L98', 'real_69c60974d4242eda8c47c615:L99']
- collect added=11 hits=18 branch_selected=False collect_full=True
- legal_actions (12):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0734
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L93 | 对重大事故隐患，由被检查项目负责整改，整改应制定事故隐患治理方案，该方案由项目经理组织制定和实施。方案包括以下内容： | score=0.0734
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L94 | 1、治理的目标和任务； | score=0.0445
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L95 | 2、采取的方法和措施； | score=0.0380
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L96 | 3、经费和物资的落实； | score=0.0334
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L97 | 4、负责治理的机构和人员； | score=0.0446
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L98 | 5、治理的时限和要求； | score=0.0545
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L99 | 6、安全措施和应急预案。 | score=0.0492
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L100 | 隐患程度严重或整改难度大者，二级单位必须按带班检查制度指派二级单位负责人（总经理或生产、技术总工）监督整改。整改完成后在隐患整改回复单填写自检情况（须附证明材料），项目负责人复查验证，签字确认后上报二级单位，由二级单位复查确认后上报集团公司安全管理部。 | score=0.0529
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L101 | 集团公司安全管理部依据整改情况决定验证，销项。 | score=0.0302
  - C11 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0660
  - C12 | COLLECT | real_69c60974d4242eda8c47c615:L103 | 2.4.6 各项目部应当加强对自然灾害的预防。对于因自然灾害可能导致事故灾难的隐患，应当按照有关法律、法规、标准和本制度的要求排查治理，采取可靠的预防措施，制定应急预案。在接到有关自然灾害预报时，应当及时向有关人员发出预警通知；发生自然灾害可能危及施工和人员安全的情况时，应当采取撤离人员、停止作业、加强监测等安全措施，并及时向当地人民政府有关部门报告。 | score=0.0639
- projection_chars: 2188

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60974d4242eda8c47c615:L92` depth=`1`
- reason: Collected section L92 contains the required elements for major accident hazard governance plans.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 189

**Step 3** `nav_dispatch`  id=`D11` kind=`dispatch` section=`real_69c60974d4242eda8c47c615:L92` scope=`None` depth=`0`
- reason: Dispatch to subagent to collect all elements of major accident hazard governance plan from section 2.4.4.
- dispatch_regions: ['real_69c60974d4242eda8c47c615:L92']
- child_reports=1 skipped=0
- legal_actions (53):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0576
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0576
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0576
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0576
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0576
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0576
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0576
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0734
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0734
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0585
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0585
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0585
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0586
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0586
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0586
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0586
- projection_chars: 3495

**Step 4** `nav_collect`  id=`C10` kind=`collect` section=`real_69c60974d4242eda8c47c615:L82` scope=`None` depth=`0`
- reason: Collect definition of major accident hazards to ensure governance plan scope is understood.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L82']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (56):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0576
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0576
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0576
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0576
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0576
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0576
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0576
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0734
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0585
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0585
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0585
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0586
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0586
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0586
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0586
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L54 | 10、各类事故是否按“四不放过”的原则进行处理，是否有隐瞒不报情况。 | score=0.0586
- projection_chars: 3381

**Step 5** `nav_collect`  id=`C10` kind=`collect` section=`real_69c60974d4242eda8c47c615:L104` scope=`real_69c60974d4242eda8c47c615:L81` depth=`1`
- reason: Section C10 covers risk control measures priority, which is a key element of major hazard governance plans.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L104']
- collect added=6 hits=6 branch_selected=True collect_full=True
- legal_actions (17):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L83 | 1、一般事故隐患，是指危害和整改难度较小，发现后能够立即整改排除的隐患； | score=0.0432
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L84 | 2、重大事故隐患，是指危害和整改难度较大，应当全部或者局部停产停业，并经过一定时间整改治理方能排除的隐患，或者因外部因素影响致使生产经营单位自身难以排除的隐患。 | score=0.0718
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L85 | 2.4.2 隐患整改的职责 | score=0.0570
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L86 | 1、各项目的项目经理对事故隐患治理负直接全面责任； | score=0.0533
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L87 | 2、各二级单位主要负责人对事故隐患治理负直接管理领导责任； | score=0.0570
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L88 | 3、集团公司相关部门对事故隐患治理负监督管理责任。 | score=0.0495
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0564
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L90 | 1、一般事故隐患的治理由各项目部根据事故隐患的实际情况，制定针对性的治理措施，落实相关责任人，限期进行整改； | score=0.0548
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L91 | 2、集团公司各级安全检查发现的一般事故隐患，必须建立档案（事故隐患登记台账），由被检查项目负责整改，整改完成后在隐患整改回复单填写自检情况（须附证明材料），项目负责人复查验证，签字确认后上报二级单位，由二级单位复查销项。 | score=0.0564
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L104 | 2.4.7 隐患整改（控制或变更降低安全风险）措施的优先顺序： | score=0.0484
  - C11 | COLLECT | real_69c60974d4242eda8c47c615:L105 | 1、消除：改变施工方法或工艺以消除危险源； | score=0.0251
  - C12 | COLLECT | real_69c60974d4242eda8c47c615:L106 | 2、替代：用低危害物质替代或降低系统能量（如较低的电流、电压、压力、温度等）； | score=0.0165
  - C13 | COLLECT | real_69c60974d4242eda8c47c615:L107 | 3、工程控制措施：安装通风系统、机械防护、连锁装置、隔声罩、防护棚、防护栏杆等； | score=0.0203
  - C14 | COLLECT | real_69c60974d4242eda8c47c615:L108 | 4、标志、警告和管理控制措施：安全标志、危险区域标识、警告器或警告灯、报警器、安全规程、设备检修、作业安全制度、操作牌和作业许可证等； | score=0.0248
  - C15 | COLLECT | real_69c60974d4242eda8c47c615:L109 | 5、个体防护装备：为操作者配备必要的个体防护装备； | score=0.0303
  - C16 | COLLECT | real_69c60974d4242eda8c47c615:L110 | 6、风险转移：为从事危险作业的人员和重要设施办理保险。 | score=0.0484
- projection_chars: 3006

**Step 6** `nav_collect`  id=`C2` kind=`collect` section=`real_69c60974d4242eda8c47c615:L84` scope=`real_69c60974d4242eda8c47c615:L81` depth=`1`
- reason: Collects definition of major accident hazards, relevant to the query about governance plans.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L84']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (10):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L83 | 1、一般事故隐患，是指危害和整改难度较小，发现后能够立即整改排除的隐患； | score=0.0432
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L84 | 2、重大事故隐患，是指危害和整改难度较大，应当全部或者局部停产停业，并经过一定时间整改治理方能排除的隐患，或者因外部因素影响致使生产经营单位自身难以排除的隐患。 | score=0.0718
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L85 | 2.4.2 隐患整改的职责 | score=0.0570
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L86 | 1、各项目的项目经理对事故隐患治理负直接全面责任； | score=0.0533
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L87 | 2、各二级单位主要负责人对事故隐患治理负直接管理领导责任； | score=0.0570
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L88 | 3、集团公司相关部门对事故隐患治理负监督管理责任。 | score=0.0495
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0564
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L90 | 1、一般事故隐患的治理由各项目部根据事故隐患的实际情况，制定针对性的治理措施，落实相关责任人，限期进行整改； | score=0.0548
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L91 | 2、集团公司各级安全检查发现的一般事故隐患，必须建立档案（事故隐患登记台账），由被检查项目负责整改，整改完成后在隐患整改回复单填写自检情况（须附证明材料），项目负责人复查验证，签字确认后上报二级单位，由二级单位复查销项。 | score=0.0564
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 1952

**Step 7** `nav_collect`  id=`C2` kind=`collect` section=`real_69c60974d4242eda8c47c615:L85` scope=`real_69c60974d4242eda8c47c615:L81` depth=`1`
- reason: Section 2.4.2 covers responsibilities for hazard rectification, relevant to the query.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L85']
- collect added=3 hits=3 branch_selected=True collect_full=True
- legal_actions (9):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L83 | 1、一般事故隐患，是指危害和整改难度较小，发现后能够立即整改排除的隐患； | score=0.0432
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L85 | 2.4.2 隐患整改的职责 | score=0.0570
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L86 | 1、各项目的项目经理对事故隐患治理负直接全面责任； | score=0.0533
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L87 | 2、各二级单位主要负责人对事故隐患治理负直接管理领导责任； | score=0.0570
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L88 | 3、集团公司相关部门对事故隐患治理负监督管理责任。 | score=0.0495
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0564
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L90 | 1、一般事故隐患的治理由各项目部根据事故隐患的实际情况，制定针对性的治理措施，落实相关责任人，限期进行整改； | score=0.0548
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L91 | 2、集团公司各级安全检查发现的一般事故隐患，必须建立档案（事故隐患登记台账），由被检查项目负责整改，整改完成后在隐患整改回复单填写自检情况（须附证明材料），项目负责人复查验证，签字确认后上报二级单位，由二级单位复查销项。 | score=0.0564
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 1729

**Step 8** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60974d4242eda8c47c615:L83` scope=`real_69c60974d4242eda8c47c615:L81` depth=`1`
- reason: Collects definition of major accident hazards to identify relevant content elements.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L83']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (5):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L83 | 1、一般事故隐患，是指危害和整改难度较小，发现后能够立即整改排除的隐患； | score=0.0432
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0564
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L90 | 1、一般事故隐患的治理由各项目部根据事故隐患的实际情况，制定针对性的治理措施，落实相关责任人，限期进行整改； | score=0.0548
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L91 | 2、集团公司各级安全检查发现的一般事故隐患，必须建立档案（事故隐患登记台账），由被检查项目负责整改，整改完成后在隐患整改回复单填写自检情况（须附证明材料），项目负责人复查验证，签字确认后上报二级单位，由二级单位复查销项。 | score=0.0564
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 1169

**Step 9** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60974d4242eda8c47c615:L81` depth=`1`
- reason: Collected sections cover general hazard rectification but lack specific elements for major accident hazard governance plans. No further relevant sections found in current scope.
- legal_actions (4):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0564
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L90 | 1、一般事故隐患的治理由各项目部根据事故隐患的实际情况，制定针对性的治理措施，落实相关责任人，限期进行整改； | score=0.0548
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L91 | 2、集团公司各级安全检查发现的一般事故隐患，必须建立档案（事故隐患登记台账），由被检查项目负责整改，整改完成后在隐患整改回复单填写自检情况（须附证明材料），项目负责人复查验证，签字确认后上报二级单位，由二级单位复查销项。 | score=0.0564
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 1029

**Step 10** `nav_dispatch`  id=`D8` kind=`dispatch` section=`real_69c60974d4242eda8c47c615:L81` scope=`None` depth=`0`
- reason: Dispatch to collect the full content of Section 2.4 'Hazard Rectification' which defines major accident hazards and likely contains governance plan requirements.
- dispatch_regions: ['real_69c60974d4242eda8c47c615:L81']
- child_reports=1 skipped=0
- legal_actions (56):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0576
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0576
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0576
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0576
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0576
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0576
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0576
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0734
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0585
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0585
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0585
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0586
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0586
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0586
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0586
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L54 | 10、各类事故是否按“四不放过”的原则进行处理，是否有隐瞒不报情况。 | score=0.0586
- projection_chars: 3382

**Step 11** `nav_collect`  id=`C27` kind=`collect` section=`real_69c60974d4242eda8c47c615:L304` scope=`None` depth=`0`
- reason: Collect leaf C27 which explicitly mentions 'major hazard and accident hazard assessment, monitoring, and rectification' expenses, a key element of governance plans.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L304']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (62):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0576
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0576
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0576
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0576
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0576
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0576
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0576
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0734
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0585
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0585
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0585
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0586
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0586
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0586
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0586
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L54 | 10、各类事故是否按“四不放过”的原则进行处理，是否有隐瞒不报情况。 | score=0.0586
- projection_chars: 3436

**Step 12** `nav_collect`  id=`C28` kind=`collect` section=`real_69c60974d4242eda8c47c615:L366` scope=`None` depth=`0`
- reason: Section C28 explicitly references the required content for special plans regarding major hazard projects, directly addressing the query.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L366']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (61):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0576
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0576
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0576
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0576
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0576
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0576
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0576
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0734
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0585
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0585
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0585
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0586
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0586
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0586
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0586
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L54 | 10、各类事故是否按“四不放过”的原则进行处理，是否有隐瞒不报情况。 | score=0.0586
- projection_chars: 3355

**Step 13** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Collected evidence from L92 and L81 regions covers the required elements for major accident hazard governance plans. Sufficient to answer query.
- legal_actions (61):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0576
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0576
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0576
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0576
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0576
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0576
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0576
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0734
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0585
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0585
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0585
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0586
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0586
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0586
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0586
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L50 | 6、施工组织设计、安全策划、专项施工方案的编制、审批、执行情况； | score=0.0465
- projection_chars: 3295

### Subagent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60974d4242eda8c47c615:L81 (ok)
collected 13 branch node(s); explicit roots=['real_69c60974d4242eda8c47c615:L104', 'real_69c60974d4242eda8c47c615:L84', 'real_69c60974d4242eda8c47c615:L85', 'real_69c60974d4242eda8c47c615:L83']
collected: real_69c60974d4242eda8c47c615:L104, real_69c60974d4242eda8c47c615:L105, real_69c60974d4242eda8c47c615:L106, real_69c60974d4242eda8c47c615:L107, real_69c60974d4242eda8c47c615:L108, real_69c60974d4242eda8c47c615:L109, real_69c60974d4242eda8c47c615:L110, real_69c60974d4242eda8c47c615:L83, real_69c60974d4242eda8c47c615:L84, real_69c60974d4242eda8c47c615:L85, real_69c60974d4242eda8c47c615:L86, real_69c60974d4242eda8c47c615:L87, real_69c60974d4242eda8c47c615:L88
reason: Collected sections cover general hazard rectification but lack specific elements for major accident hazard governance plans. No further relevant sections found in current scope.
---
=== End Investigate ===
```

### Evidence text (new)

```
[E1]
[§ 2.4.4 重大事故隐患整改、复查、销项]
  2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。
  对重大事故隐患，由被检查项目负责整改，整改应制定事故隐患治理方案，该方案由项目经理组织制定和实施。方案包括以下内容：
  1、治理的目标和任务；
  2、采取的方法和措施；
  3、经费和物资的落实；
  4、负责治理的机构和人员；
  5、治理的时限和要求；
  6、安全措施和应急预案。

[E2]
[§ 2.4 隐患整改]
  2.4.1 事故隐患分为一般事故隐患和重大事故隐患。
  1、一般事故隐患，是指危害和整改难度较小，发现后能够立即整改排除的隐患；
  2、重大事故隐患，是指危害和整改难度较大，应当全部或者局部停产停业，并经过一定时间整改治理方能排除的隐患，或者因外部因素影响致使生产经营单位自身难以排除的隐患。
```

### Evidence text (old)

```
[E1]
[§ 第四章　安全生产事故应急救援管理规定 / 4.1 组织机构与职责]
4.1.4 集团公司编制生产安全事故的综合应急救援预案，二级单位编制本单位的应急救援预案，项目部编制项目应急救援预案。

[E2]
[§ 第二章　安全检查及隐患排查规定 / 2.4 隐患整改 / 2.4.3 一般事故隐患整改、复查、销项]
2、集团公司各级安全检查发现的一般事故隐患，必须建立档案（事故隐患登记台账），由被检查项目负责整改，整改完成后在隐患整改回复单填写自检情况（须附证明材料），项目负责人复查验证，签字确认后上报二级单位，由二级单位复查销项。

[E3]
[§ 第四章　安全生产事故应急救援管理规定 / 4.4 应急响应程序]
附表4.3.1：应急预案演练方案；

[E4]
[§ 第四章　安全生产事故应急救援管理规定 / 4.2 应急救援预案]
1、紧急情况、事故类型及特征分析；

[E5]
[§ 第四章　安全生产事故应急救援管理规定 / 4.4 应急响应程序]
4.4.4 各部门、二级单位、项目部按照职责分工和相关预案应对生产安全事故的人力、物力、财力、运输、医疗卫生及通信保障等应急保障工
```

## latest_clean_multi_0032 (multi_hop)

**Query:** 根据《线上学习平台学习管理方案（修订）》中“（ 一）课程开发管理”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c6095ed4242eda8c47c5b2`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 142 | 484 |
| gold_node_recall | 0.0 | 0.5 |
| n_retrieved_nodes | 2 | 8 |
| trajectory_steps | n/a | 8 |

### Gold node hits (new)

- `real_69c6095ed4242eda8c47c5b2:L34` [HIT] retrieved=True in_text=False
- `real_69c6095ed4242eda8c47c5b2:L35` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6095ed4242eda8c47c5b2:L33` scope=`real_69c6095ed4242eda8c47c5b2:L33` depth=`1`
- reason: Collect adjacent sections C2 (Course Development) and C3 (Courseware Review) under 'Course Development Management' to answer the query.
- collect_section_ids: ['real_69c6095ed4242eda8c47c5b2:L33', 'real_69c6095ed4242eda8c47c5b2:L34', 'real_69c6095ed4242eda8c47c5b2:L35']
- collect added=4 hits=6 branch_selected=False collect_full=True
- legal_actions (5):
  - C1 | COLLECT | real_69c6095ed4242eda8c47c5b2:L33 | （ 一）课程开发管理 | score=0.0694
  - C2 | COLLECT | real_69c6095ed4242eda8c47c5b2:L34 | 1.课程开发。课程开发依托专家组、各业务线要从有利于组织目标达成、员工履职能力提升等方面，本着“简单、实用、明了”原则进行课程开发。各专家组、各部门应按年度既定课程开发计划，督促、跟进课程开发负责人按时完成课件开发任务。计划外课程开发须明确开发课程名称、学习对象等，经各专家组审核后开发，并向平台中心办公室备案。 | score=0.0673
  - C3 | COLLECT | real_69c6095ed4242eda8c47c5b2:L35 | 2.课件评审。课件开发完成后，根据课程类别提交各专家组审核，专家组从课件选材、专业度、实用性等方面对课件进行评审，课程评审管理参照《十一在线——员工赋能一体化平台管理办法》执行。 | score=0.0635
  - C4 | COLLECT | real_69c6095ed4242eda8c47c5b2:L36 | 3.课件上传。评审通过后，平台管理员需在课程计划提交截止时间5 日内完成课件上传和必修岗位指派。计划外开发的课程经各专家组评审通过后5 日完成上传和必修岗位指派。 | score=0.0551
  - C5 | COLLECT | real_69c6095ed4242eda8c47c5b2:L37 | 4.课酬兑现。开发的课程根据《十一在线——员工赋能一体化平台管理办法》相关规定标准兑现相应课酬。 | score=0.0694
- projection_chars: 1325

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c6095ed4242eda8c47c5b2:L33` depth=`1`
- reason: The current scope L33 contains the relevant section on course development management. No further collection is needed as the evidence is sufficient to address the query about adjacent points.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 189

**Step 3** `nav_dispatch`  id=`D10` kind=`dispatch` section=`real_69c6095ed4242eda8c47c5b2:L33` scope=`None` depth=`0`
- reason: Dispatch to 'Course Development Management' section to find adjacent evidence points.
- dispatch_regions: ['real_69c6095ed4242eda8c47c5b2:L33']
- child_reports=1 skipped=0
- legal_actions (46):
  - C1 | COLLECT | real_69c6095ed4242eda8c47c5b2:L1 | 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） | score=0.0703
  - D1 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L1 | 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） | score=0.0703
  - C2 | COLLECT | real_69c6095ed4242eda8c47c5b2:L2 | 为进一步深化学习型组织建设，整合学习资源，传播最佳实践，有效助力员工工作技能提升和绩效改善。为进一步强化学习效果，规范线上学习管理，特制订本方案。 | score=0.0578
  - C3 | COLLECT | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0628
  - D2 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0628
  - C4 | COLLECT | real_69c6095ed4242eda8c47c5b2:L4 | 线上学习平台主要为除十一在线各研修班以外一般员工提供学习资源。十一在线平台中心为其最高管理机构负责把握学习方向、整合学习资源，各专家组负责学习内容开发，十一在线平台中心办公室主要负责日常运营管理，集团公司机关各部室及各二级单位负责组织本部室及本单位员工参加学习。各级机构及其职责具体如下： | score=0.0610
  - C5 | COLLECT | real_69c6095ed4242eda8c47c5b2:L5 | （ 一）十一在线平台中心：负责课程体系设计、课程开发计划审批、课程考核标准设定、平台建设费用审批等相关事宜。 | score=0.0583
  - C6 | COLLECT | real_69c6095ed4242eda8c47c5b2:L7 | （ 三）十一在线平台中心办公室：负责线上学习平台搭建，维护平台基本信息，监督各专家组及相关部门及时更新学习内容，组织各专家组和二级单位平台管理员进行平台管理培训，并对各专家组课程开发情况、学员学习情况进行跟 | score=0.0628
  - C7 | COLLECT | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0619
  - D3 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0619
  - C8 | COLLECT | real_69c6095ed4242eda8c47c5b2:L14 | 2.督促本部室及本单位员工开展在线学习，并结合线上学习内容和业务实际，组织本部室及本单位开展线下探讨、分享、集中培训等。 | score=0.0619
  - C9 | COLLECT | real_69c6095ed4242eda8c47c5b2:L15 | （ 六 ）学员 | score=0.0596
  - D4 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L15 | （ 六 ）学员 | score=0.0596
  - C10 | COLLECT | real_69c6095ed4242eda8c47c5b2:L16 | 根据课程设置及时完成相应必修课程学习，根据岗位和个人能力的发展规划，合理选修相应课程，积极学以致用，改进工作绩效。 | score=0.0596
  - C11 | COLLECT | real_69c6095ed4242eda8c47c5b2:L17 | 二、课程及指派管理 | score=0.0703
  - D5 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L17 | 二、课程及指派管理 | score=0.0703
- projection_chars: 3592

**Step 4** `nav_collect`  id=`C14` kind=`collect` section=`real_69c6095ed4242eda8c47c5b2:L20` scope=`None` depth=`0`
- reason: Collect adjacent evidence point regarding course development plan approval details.
- collect_section_ids: ['real_69c6095ed4242eda8c47c5b2:L20']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (44):
  - D1 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L1 | 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） | score=0.0703
  - C1 | COLLECT | real_69c6095ed4242eda8c47c5b2:L2 | 为进一步深化学习型组织建设，整合学习资源，传播最佳实践，有效助力员工工作技能提升和绩效改善。为进一步强化学习效果，规范线上学习管理，特制订本方案。 | score=0.0578
  - C2 | COLLECT | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0628
  - D2 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0628
  - C3 | COLLECT | real_69c6095ed4242eda8c47c5b2:L4 | 线上学习平台主要为除十一在线各研修班以外一般员工提供学习资源。十一在线平台中心为其最高管理机构负责把握学习方向、整合学习资源，各专家组负责学习内容开发，十一在线平台中心办公室主要负责日常运营管理，集团公司机关各部室及各二级单位负责组织本部室及本单位员工参加学习。各级机构及其职责具体如下： | score=0.0610
  - C4 | COLLECT | real_69c6095ed4242eda8c47c5b2:L5 | （ 一）十一在线平台中心：负责课程体系设计、课程开发计划审批、课程考核标准设定、平台建设费用审批等相关事宜。 | score=0.0583
  - C5 | COLLECT | real_69c6095ed4242eda8c47c5b2:L7 | （ 三）十一在线平台中心办公室：负责线上学习平台搭建，维护平台基本信息，监督各专家组及相关部门及时更新学习内容，组织各专家组和二级单位平台管理员进行平台管理培训，并对各专家组课程开发情况、学员学习情况进行跟 | score=0.0628
  - C6 | COLLECT | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0619
  - D3 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0619
  - C7 | COLLECT | real_69c6095ed4242eda8c47c5b2:L13 | 1.协同做好线上学习平台的推广、使用和维护等日常管理工作，配合各专家组完成本业务条线培训课程开发、选配工作。 | score=0.0570
  - C8 | COLLECT | real_69c6095ed4242eda8c47c5b2:L14 | 2.督促本部室及本单位员工开展在线学习，并结合线上学习内容和业务实际，组织本部室及本单位开展线下探讨、分享、集中培训等。 | score=0.0619
  - C9 | COLLECT | real_69c6095ed4242eda8c47c5b2:L15 | （ 六 ）学员 | score=0.0596
  - D4 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L15 | （ 六 ）学员 | score=0.0596
  - C10 | COLLECT | real_69c6095ed4242eda8c47c5b2:L16 | 根据课程设置及时完成相应必修课程学习，根据岗位和个人能力的发展规划，合理选修相应课程，积极学以致用，改进工作绩效。 | score=0.0596
  - C11 | COLLECT | real_69c6095ed4242eda8c47c5b2:L17 | 二、课程及指派管理 | score=0.0703
  - D5 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L17 | 二、课程及指派管理 | score=0.0703
- projection_chars: 3507

**Step 5** `nav_collect`  id=`C13` kind=`collect` section=`real_69c6095ed4242eda8c47c5b2:L19` scope=`None` depth=`0`
- reason: Collect section on compulsory course development to identify adjacent points as requested.
- collect_section_ids: ['real_69c6095ed4242eda8c47c5b2:L19']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (44):
  - D1 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L1 | 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） | score=0.0703
  - C1 | COLLECT | real_69c6095ed4242eda8c47c5b2:L2 | 为进一步深化学习型组织建设，整合学习资源，传播最佳实践，有效助力员工工作技能提升和绩效改善。为进一步强化学习效果，规范线上学习管理，特制订本方案。 | score=0.0578
  - C2 | COLLECT | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0628
  - D2 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0628
  - C3 | COLLECT | real_69c6095ed4242eda8c47c5b2:L4 | 线上学习平台主要为除十一在线各研修班以外一般员工提供学习资源。十一在线平台中心为其最高管理机构负责把握学习方向、整合学习资源，各专家组负责学习内容开发，十一在线平台中心办公室主要负责日常运营管理，集团公司机关各部室及各二级单位负责组织本部室及本单位员工参加学习。各级机构及其职责具体如下： | score=0.0610
  - C4 | COLLECT | real_69c6095ed4242eda8c47c5b2:L5 | （ 一）十一在线平台中心：负责课程体系设计、课程开发计划审批、课程考核标准设定、平台建设费用审批等相关事宜。 | score=0.0583
  - C5 | COLLECT | real_69c6095ed4242eda8c47c5b2:L7 | （ 三）十一在线平台中心办公室：负责线上学习平台搭建，维护平台基本信息，监督各专家组及相关部门及时更新学习内容，组织各专家组和二级单位平台管理员进行平台管理培训，并对各专家组课程开发情况、学员学习情况进行跟 | score=0.0628
  - C6 | COLLECT | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0619
  - D3 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0619
  - C7 | COLLECT | real_69c6095ed4242eda8c47c5b2:L13 | 1.协同做好线上学习平台的推广、使用和维护等日常管理工作，配合各专家组完成本业务条线培训课程开发、选配工作。 | score=0.0570
  - C8 | COLLECT | real_69c6095ed4242eda8c47c5b2:L14 | 2.督促本部室及本单位员工开展在线学习，并结合线上学习内容和业务实际，组织本部室及本单位开展线下探讨、分享、集中培训等。 | score=0.0619
  - C9 | COLLECT | real_69c6095ed4242eda8c47c5b2:L15 | （ 六 ）学员 | score=0.0596
  - D4 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L15 | （ 六 ）学员 | score=0.0596
  - C10 | COLLECT | real_69c6095ed4242eda8c47c5b2:L16 | 根据课程设置及时完成相应必修课程学习，根据岗位和个人能力的发展规划，合理选修相应课程，积极学以致用，改进工作绩效。 | score=0.0596
  - C11 | COLLECT | real_69c6095ed4242eda8c47c5b2:L17 | 二、课程及指派管理 | score=0.0703
  - D5 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L17 | 二、课程及指派管理 | score=0.0703
- projection_chars: 3510

**Step 6** `nav_collect`  id=`C14` kind=`collect` section=`real_69c6095ed4242eda8c47c5b2:L18` scope=`None` depth=`0`
- reason: Collect section on course categories and development to identify adjacent points in course development management.
- collect_section_ids: ['real_69c6095ed4242eda8c47c5b2:L18', 'real_69c6095ed4242eda8c47c5b2:L21']
- collect added=5 hits=6 branch_selected=False collect_full=True
- legal_actions (46):
  - D1 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L1 | 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） | score=0.0703
  - C1 | COLLECT | real_69c6095ed4242eda8c47c5b2:L2 | 为进一步深化学习型组织建设，整合学习资源，传播最佳实践，有效助力员工工作技能提升和绩效改善。为进一步强化学习效果，规范线上学习管理，特制订本方案。 | score=0.0578
  - C2 | COLLECT | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0628
  - D2 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0628
  - C3 | COLLECT | real_69c6095ed4242eda8c47c5b2:L4 | 线上学习平台主要为除十一在线各研修班以外一般员工提供学习资源。十一在线平台中心为其最高管理机构负责把握学习方向、整合学习资源，各专家组负责学习内容开发，十一在线平台中心办公室主要负责日常运营管理，集团公司机关各部室及各二级单位负责组织本部室及本单位员工参加学习。各级机构及其职责具体如下： | score=0.0610
  - C4 | COLLECT | real_69c6095ed4242eda8c47c5b2:L5 | （ 一）十一在线平台中心：负责课程体系设计、课程开发计划审批、课程考核标准设定、平台建设费用审批等相关事宜。 | score=0.0583
  - C5 | COLLECT | real_69c6095ed4242eda8c47c5b2:L7 | （ 三）十一在线平台中心办公室：负责线上学习平台搭建，维护平台基本信息，监督各专家组及相关部门及时更新学习内容，组织各专家组和二级单位平台管理员进行平台管理培训，并对各专家组课程开发情况、学员学习情况进行跟 | score=0.0628
  - C6 | COLLECT | real_69c6095ed4242eda8c47c5b2:L9 | （ 四）平台管理员 | score=0.0533
  - D3 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L9 | （ 四）平台管理员 | score=0.0533
  - C7 | COLLECT | real_69c6095ed4242eda8c47c5b2:L11 | 2.各二级单位平台管理员：负责督促本单位各类课件指定人员在线学习，按时完成学习计划，并向各专家组及十一在线平台中心办公室反馈学习情况。 | score=0.0533
  - C8 | COLLECT | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0619
  - D4 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0619
  - C9 | COLLECT | real_69c6095ed4242eda8c47c5b2:L13 | 1.协同做好线上学习平台的推广、使用和维护等日常管理工作，配合各专家组完成本业务条线培训课程开发、选配工作。 | score=0.0570
  - C10 | COLLECT | real_69c6095ed4242eda8c47c5b2:L14 | 2.督促本部室及本单位员工开展在线学习，并结合线上学习内容和业务实际，组织本部室及本单位开展线下探讨、分享、集中培训等。 | score=0.0619
  - C11 | COLLECT | real_69c6095ed4242eda8c47c5b2:L15 | （ 六 ）学员 | score=0.0596
  - D5 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L15 | （ 六 ）学员 | score=0.0596
- projection_chars: 3565

**Step 7** `nav_collect`  id=`C14` kind=`collect` section=`real_69c6095ed4242eda8c47c5b2:L24` scope=`None` depth=`0`
- reason: Collect section on course development management and video course details to answer the query.
- collect_section_ids: ['real_69c6095ed4242eda8c47c5b2:L24', 'real_69c6095ed4242eda8c47c5b2:L25']
- collect added=3 hits=4 branch_selected=False collect_full=True
- legal_actions (43):
  - D1 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L1 | 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） | score=0.0703
  - C1 | COLLECT | real_69c6095ed4242eda8c47c5b2:L2 | 为进一步深化学习型组织建设，整合学习资源，传播最佳实践，有效助力员工工作技能提升和绩效改善。为进一步强化学习效果，规范线上学习管理，特制订本方案。 | score=0.0578
  - C2 | COLLECT | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0628
  - D2 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0628
  - C3 | COLLECT | real_69c6095ed4242eda8c47c5b2:L4 | 线上学习平台主要为除十一在线各研修班以外一般员工提供学习资源。十一在线平台中心为其最高管理机构负责把握学习方向、整合学习资源，各专家组负责学习内容开发，十一在线平台中心办公室主要负责日常运营管理，集团公司机关各部室及各二级单位负责组织本部室及本单位员工参加学习。各级机构及其职责具体如下： | score=0.0610
  - C4 | COLLECT | real_69c6095ed4242eda8c47c5b2:L5 | （ 一）十一在线平台中心：负责课程体系设计、课程开发计划审批、课程考核标准设定、平台建设费用审批等相关事宜。 | score=0.0583
  - C5 | COLLECT | real_69c6095ed4242eda8c47c5b2:L7 | （ 三）十一在线平台中心办公室：负责线上学习平台搭建，维护平台基本信息，监督各专家组及相关部门及时更新学习内容，组织各专家组和二级单位平台管理员进行平台管理培训，并对各专家组课程开发情况、学员学习情况进行跟 | score=0.0628
  - C6 | COLLECT | real_69c6095ed4242eda8c47c5b2:L9 | （ 四）平台管理员 | score=0.0533
  - D3 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L9 | （ 四）平台管理员 | score=0.0533
  - C7 | COLLECT | real_69c6095ed4242eda8c47c5b2:L10 | 1.各专家组平台管理员：负责本专家组课件和考试习题的上传、维护、更新、删除、学习任务下发和指派相关岗位学习等工作。 | score=0.0517
  - C8 | COLLECT | real_69c6095ed4242eda8c47c5b2:L11 | 2.各二级单位平台管理员：负责督促本单位各类课件指定人员在线学习，按时完成学习计划，并向各专家组及十一在线平台中心办公室反馈学习情况。 | score=0.0533
  - C9 | COLLECT | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0619
  - D4 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0619
  - C10 | COLLECT | real_69c6095ed4242eda8c47c5b2:L13 | 1.协同做好线上学习平台的推广、使用和维护等日常管理工作，配合各专家组完成本业务条线培训课程开发、选配工作。 | score=0.0570
  - C11 | COLLECT | real_69c6095ed4242eda8c47c5b2:L14 | 2.督促本部室及本单位员工开展在线学习，并结合线上学习内容和业务实际，组织本部室及本单位开展线下探讨、分享、集中培训等。 | score=0.0619
  - C12 | COLLECT | real_69c6095ed4242eda8c47c5b2:L15 | （ 六 ）学员 | score=0.0596
- projection_chars: 3488

**Step 8** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence collected from L33 region covers 'Course Development Management' with sufficient adjacent points to answer the query.
- legal_actions (44):
  - D1 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L1 | 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） | score=0.0703
  - C1 | COLLECT | real_69c6095ed4242eda8c47c5b2:L2 | 为进一步深化学习型组织建设，整合学习资源，传播最佳实践，有效助力员工工作技能提升和绩效改善。为进一步强化学习效果，规范线上学习管理，特制订本方案。 | score=0.0578
  - C2 | COLLECT | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0628
  - D2 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0628
  - C3 | COLLECT | real_69c6095ed4242eda8c47c5b2:L4 | 线上学习平台主要为除十一在线各研修班以外一般员工提供学习资源。十一在线平台中心为其最高管理机构负责把握学习方向、整合学习资源，各专家组负责学习内容开发，十一在线平台中心办公室主要负责日常运营管理，集团公司机关各部室及各二级单位负责组织本部室及本单位员工参加学习。各级机构及其职责具体如下： | score=0.0610
  - C4 | COLLECT | real_69c6095ed4242eda8c47c5b2:L5 | （ 一）十一在线平台中心：负责课程体系设计、课程开发计划审批、课程考核标准设定、平台建设费用审批等相关事宜。 | score=0.0583
  - C5 | COLLECT | real_69c6095ed4242eda8c47c5b2:L6 | （ 二）各专家组：负责各领域内员工培训需求征集，教材、课件及习题开发，课件修改、适时更新、审核，业务答疑，题库组建等工作，集团对口业务部门负责人为各专业课程开发责任人，统筹推进本业务系统课程开发工作。 | score=0.0504
  - C6 | COLLECT | real_69c6095ed4242eda8c47c5b2:L7 | （ 三）十一在线平台中心办公室：负责线上学习平台搭建，维护平台基本信息，监督各专家组及相关部门及时更新学习内容，组织各专家组和二级单位平台管理员进行平台管理培训，并对各专家组课程开发情况、学员学习情况进行跟 | score=0.0628
  - C7 | COLLECT | real_69c6095ed4242eda8c47c5b2:L8 | 踪和定期调研，反馈十一在线平台中心。 | score=0.0486
  - C8 | COLLECT | real_69c6095ed4242eda8c47c5b2:L9 | （ 四）平台管理员 | score=0.0533
  - D3 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L9 | （ 四）平台管理员 | score=0.0533
  - C9 | COLLECT | real_69c6095ed4242eda8c47c5b2:L10 | 1.各专家组平台管理员：负责本专家组课件和考试习题的上传、维护、更新、删除、学习任务下发和指派相关岗位学习等工作。 | score=0.0517
  - C10 | COLLECT | real_69c6095ed4242eda8c47c5b2:L11 | 2.各二级单位平台管理员：负责督促本单位各类课件指定人员在线学习，按时完成学习计划，并向各专家组及十一在线平台中心办公室反馈学习情况。 | score=0.0533
  - C11 | COLLECT | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0619
  - D4 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0619
  - C12 | COLLECT | real_69c6095ed4242eda8c47c5b2:L13 | 1.协同做好线上学习平台的推广、使用和维护等日常管理工作，配合各专家组完成本业务条线培训课程开发、选配工作。 | score=0.0570
- projection_chars: 3558

### Subagent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c6095ed4242eda8c47c5b2:L33 (ok)
collected 5 branch node(s); explicit roots=['real_69c6095ed4242eda8c47c5b2:L33']
collected: real_69c6095ed4242eda8c47c5b2:L33, real_69c6095ed4242eda8c47c5b2:L34, real_69c6095ed4242eda8c47c5b2:L35, real_69c6095ed4242eda8c47c5b2:L36, real_69c6095ed4242eda8c47c5b2:L37
reason: The current scope L33 contains the relevant section on course development management. No further collection is needed as the evidence is sufficient to address the query about adjacent points.
---
=== End Investigate ===
```

### Evidence text (new)

```
[E1]
[§ （ 一）课程类别]
  1.必修课程。必修课程需涵盖各专业系统内所有一般管理岗位。 由各专家组主持，根据所辖领域内各岗位职责制定课程开发计划、确定各系统岗位的必修课。课程开发计划需
  明确课程名称、课程类别、必修岗位、课程开发负责人等信息（见附件），提交十一在线平台中心审批后按计划开发。
  必修课程的开发数量各专家组结合业务和岗位需求实际确定，课程包含内部自主开发和外部引进，保证课程内容的实用性和有效性。
  岗位必修课程为各岗位年底技能测评的内容和依据。
  2.选修课程。员工自行选择需要学习的课程。 由员工结合本岗位履职需要、个人兴趣和其他能力提升需要， 自行选择相应选修课程学习。

[E2]
[§ （ 一）课程开发管理]
1.课程开发。课程开发依托专家组、各业务线要从有利于组织目标达成、员工履职能力提升等方面，本着“简单、实用、明了”原则进行课程开发。各专家组、各部门应按年度既定课程开发计划，督促、跟进课程开发负责人按时完成课件开发任务。计划外课程开发须明确开发课程名称、学习对象等，经各专家组审核后开发，并向平台中心办公室备案。
```

### Evidence text (old)

```
[E1]
明确课程名称、课程类别、必修岗位、课程开发负责人等信息（见附件），提交十一在线平台中心审批后按计划开发。

[E2]
1.必修课程。必修课程需涵盖各专业系统内所有一般管理岗位。 由各专家组主持，根据所辖领域内各岗位职责制定课程开发计划、确定各系统岗位的必修课。课程开发计划需
```

## latest_clean_multi_0048 (multi_hop)

**Query:** 根据《集团公司对外捐赠管理办法（修订版）》中“第二章 对外捐赠的范围及类型”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60970d4242eda8c47c5fd`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 495 | 491 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 11 | 16 |
| trajectory_steps | n/a | 4 |

### Gold node hits (new)

- `real_69c60970d4242eda8c47c5fd:L7` [HIT] retrieved=True in_text=False
- `real_69c60970d4242eda8c47c5fd:L8` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60970d4242eda8c47c5fd:L6` scope=`real_69c60970d4242eda8c47c5fd:L6` depth=`1`
- reason: Collect Chapter 2 to cover scope, types, and restrictions as requested.
- collect_section_ids: ['real_69c60970d4242eda8c47c5fd:L6']
- collect added=18 hits=18 branch_selected=True collect_full=True
- legal_actions (18):
  - C1 | COLLECT | real_69c60970d4242eda8c47c5fd:L6 | 第二章  对外捐赠的范围及类型 | score=0.0718
  - C2 | COLLECT | real_69c60970d4242eda8c47c5fd:L7 | 第三条本办法所称的“对外捐赠”，是指集团公司及所属各单位自愿将有处分权的合法财产无偿赠送给合法的受赠人（包含无偿捐赠工程），用于与捐赠人生产经营活动没有直接关系的公益事业的行为。 | score=0.0718
  - C3 | COLLECT | real_69c60970d4242eda8c47c5fd:L8 | 集团公司所属非法人分支机构、项目部不得以分公司、项目部名义对外捐赠，不得将企业拥有的财产以个人名义对外捐赠。 | score=0.0591
  - C4 | COLLECT | real_69c60970d4242eda8c47c5fd:L9 | 对外捐赠原则上以集团公司（陕西建工第十一建设集团有限公司）名义进行捐赠，独立法人单位可根据实际需要以本单位名义进行捐赠。 | score=0.0691
  - C5 | COLLECT | real_69c60970d4242eda8c47c5fd:L10 | 第四条  对外捐赠的类型 | score=0.0682
  - C6 | COLLECT | real_69c60970d4242eda8c47c5fd:L11 | （一）救济性捐赠，即向受灾地区、扶贫地区或者困难的社会弱势群体的救济性捐赠。 | score=0.0553
  - C7 | COLLECT | real_69c60970d4242eda8c47c5fd:L12 | （二）公益性捐赠，即向科技文卫事业和环境保护等社会公益事业的公益性捐赠。 | score=0.0559
  - C8 | COLLECT | real_69c60970d4242eda8c47c5fd:L13 | （三）其他捐赠，即除上述捐赠外，为促进社会发展以及集团公司履行社会责任需要的其他捐赠，含外部各类活动赞助。 | score=0.0631
  - C9 | COLLECT | real_69c60970d4242eda8c47c5fd:L14 | 各单位要正确参与社会公益事业，依法依规确定对外捐赠范围和支出规模，规范开展对外捐赠活动，避免无序、随意捐赠等行为。对于有关社会机构、团体的摊派性捐赠，要坚决依法拒绝， | score=0.0682
  - C10 | COLLECT | real_69c60970d4242eda8c47c5fd:L15 | 第五条  对外捐赠的范围 | score=0.0686
  - C11 | COLLECT | real_69c60970d4242eda8c47c5fd:L16 | 用于对外捐赠的资产应当权属清晰，应为集团公司有权处分的合法财产，包括现金资产和实物资产等。 | score=0.0686
  - C12 | COLLECT | real_69c60970d4242eda8c47c5fd:L17 | 不具处分权的财产或者不合格产品不得用于对外捐赠。下列资产不得用于对外捐赠： | score=0.0608
  - C13 | COLLECT | real_69c60970d4242eda8c47c5fd:L18 | （一）生产经营用的主要固定资产； | score=0.0578
  - C14 | COLLECT | real_69c60970d4242eda8c47c5fd:L19 | （二）持有的股权和债权； | score=0.0572
  - C15 | COLLECT | real_69c60970d4242eda8c47c5fd:L21 | （四）国家财政拨款； | score=0.0555
  - C16 | COLLECT | real_69c60970d4242eda8c47c5fd:L22 | （五）受代管财产； | score=0.0555
- projection_chars: 2889

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60970d4242eda8c47c5fd:L6` depth=`1`
- reason: Collected section L6 contains the required content from Chapter 2. Ready to summarize points.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 188

**Step 3** `nav_dispatch`  id=`D3` kind=`dispatch` section=`real_69c60970d4242eda8c47c5fd:L6` scope=`None` depth=`0`
- reason: Dispatch Chapter 2 to extract details on scope and types for the query.
- dispatch_regions: ['real_69c60970d4242eda8c47c5fd:L6']
- child_reports=1 skipped=0
- legal_actions (42):
  - C1 | COLLECT | real_69c60970d4242eda8c47c5fd:L1 | 陕西建工第十一建设集团有限公司 | score=0.0718
  - D1 | DISPATCH | real_69c60970d4242eda8c47c5fd:L1 | 陕西建工第十一建设集团有限公司 | score=0.0718
  - C2 | COLLECT | real_69c60970d4242eda8c47c5fd:L2 | 对外捐赠管理办法（修订版） | score=0.0588
  - C3 | COLLECT | real_69c60970d4242eda8c47c5fd:L3 | 第一章  总则 | score=0.0600
  - D2 | DISPATCH | real_69c60970d4242eda8c47c5fd:L3 | 第一章  总则 | score=0.0600
  - C4 | COLLECT | real_69c60970d4242eda8c47c5fd:L4 | 第一条为进一步规范集团公司对外捐赠行为，加强对外捐赠事项的管理，更好地履行社会责任，全面、有效提升和宣传集团公司品牌及企业形象，特制定本办法。 | score=0.0583
  - C5 | COLLECT | real_69c60970d4242eda8c47c5fd:L5 | 第二条本办法适用于集团公司及所属各单位对外捐赠行为。 | score=0.0600
  - C6 | COLLECT | real_69c60970d4242eda8c47c5fd:L6 | 第二章  对外捐赠的范围及类型 | score=0.0718
  - D3 | DISPATCH | real_69c60970d4242eda8c47c5fd:L6 | 第二章  对外捐赠的范围及类型 | score=0.0718
  - C7 | COLLECT | real_69c60970d4242eda8c47c5fd:L7 | 第三条本办法所称的“对外捐赠”，是指集团公司及所属各单位自愿将有处分权的合法财产无偿赠送给合法的受赠人（包含无偿捐赠工程），用于与捐赠人生产经营活动没有直接关系的公益事业的行为。 | score=0.0718
  - C8 | COLLECT | real_69c60970d4242eda8c47c5fd:L8 | 集团公司所属非法人分支机构、项目部不得以分公司、项目部名义对外捐赠，不得将企业拥有的财产以个人名义对外捐赠。 | score=0.0591
  - C9 | COLLECT | real_69c60970d4242eda8c47c5fd:L9 | 对外捐赠原则上以集团公司（陕西建工第十一建设集团有限公司）名义进行捐赠，独立法人单位可根据实际需要以本单位名义进行捐赠。 | score=0.0691
  - C10 | COLLECT | real_69c60970d4242eda8c47c5fd:L10 | 第四条  对外捐赠的类型 | score=0.0682
  - D4 | DISPATCH | real_69c60970d4242eda8c47c5fd:L10 | 第四条  对外捐赠的类型 | score=0.0682
  - C11 | COLLECT | real_69c60970d4242eda8c47c5fd:L11 | （一）救济性捐赠，即向受灾地区、扶贫地区或者困难的社会弱势群体的救济性捐赠。 | score=0.0553
  - C12 | COLLECT | real_69c60970d4242eda8c47c5fd:L12 | （二）公益性捐赠，即向科技文卫事业和环境保护等社会公益事业的公益性捐赠。 | score=0.0559
- projection_chars: 3504

**Step 4** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Chapter 2 content collected in L6. Ready to summarize the two adjacent evidence points.
- legal_actions (35):
  - D1 | DISPATCH | real_69c60970d4242eda8c47c5fd:L1 | 陕西建工第十一建设集团有限公司 | score=0.0718
  - C1 | COLLECT | real_69c60970d4242eda8c47c5fd:L2 | 对外捐赠管理办法（修订版） | score=0.0588
  - C2 | COLLECT | real_69c60970d4242eda8c47c5fd:L3 | 第一章  总则 | score=0.0600
  - D2 | DISPATCH | real_69c60970d4242eda8c47c5fd:L3 | 第一章  总则 | score=0.0600
  - C3 | COLLECT | real_69c60970d4242eda8c47c5fd:L4 | 第一条为进一步规范集团公司对外捐赠行为，加强对外捐赠事项的管理，更好地履行社会责任，全面、有效提升和宣传集团公司品牌及企业形象，特制定本办法。 | score=0.0583
  - C4 | COLLECT | real_69c60970d4242eda8c47c5fd:L5 | 第二条本办法适用于集团公司及所属各单位对外捐赠行为。 | score=0.0600
  - C5 | COLLECT | real_69c60970d4242eda8c47c5fd:L27 | 第三章  对外捐赠的原则 | score=0.0615
  - D3 | DISPATCH | real_69c60970d4242eda8c47c5fd:L27 | 第三章  对外捐赠的原则 | score=0.0615
  - C6 | COLLECT | real_69c60970d4242eda8c47c5fd:L28 | 第六条企业捐赠程序以及行为的实施必须符合有关法律法规、规章以及企业章程的规定，对外捐赠应当遵循以下五项原则： | score=0.0576
  - C7 | COLLECT | real_69c60970d4242eda8c47c5fd:L29 | （一）自愿无偿。各单位自愿实施对外捐赠，不得要求受赠方在融资、市场准入、行政许可、占有其他资源等方面创造便利条件，不得以捐赠为名从事营利活动，从而导致市场不公平竞争。 | score=0.0499
  - C8 | COLLECT | real_69c60970d4242eda8c47c5fd:L30 | （二）量力而行。各单位对外捐赠应当充分考虑自身经营规模、盈利能力、负债水平、现金流量等财务承受能力，合理确定对外捐赠支出规模和标准。盈利能力大幅下降、负债水平偏高、经营活动现金净流量为负数或者大幅减少的企业，应严格控制对外捐赠；经营亏损的单位除特殊情况外，原则上不得安排对外捐赠支出。 | score=0.0547
  - C9 | COLLECT | real_69c60970d4242eda8c47c5fd:L31 | （三）权责清晰。各单位不得将集团公司拥有的财产以个人名义对外捐赠。且对外捐赠有权要求受赠人落实捐赠人正当的捐赠意愿，不得将捐赠财产挪作他用。 | score=0.0535
  - C10 | COLLECT | real_69c60970d4242eda8c47c5fd:L32 | （四）程序规范。企业对外捐赠，原则上由集团公司统一管理。凡涉及对外捐赠事项，履行集团公司内部审批程序后，报陕建控股集团审批核准；如有特殊事项需要对外捐赠的，应提前报告集团公司办公室，履行相应程序后办理捐赠手续，未经批准不得擅自对外捐赠。 | score=0.0615
  - C11 | COLLECT | real_69c60970d4242eda8c47c5fd:L33 | （五）诚实守信。各单位对外捐赠应当诚实守信，严禁各类虚假宣传或许诺行为。 | score=0.0513
  - C12 | COLLECT | real_69c60970d4242eda8c47c5fd:L34 | 第四章  对外捐赠的审批程序 | score=0.0678
  - D4 | DISPATCH | real_69c60970d4242eda8c47c5fd:L34 | 第四章  对外捐赠的审批程序 | score=0.0678
- projection_chars: 3089

### Subagent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60970d4242eda8c47c5fd:L6 (ok)
collected 21 branch node(s); explicit roots=['real_69c60970d4242eda8c47c5fd:L6']
collected: real_69c60970d4242eda8c47c5fd:L10, real_69c60970d4242eda8c47c5fd:L11, real_69c60970d4242eda8c47c5fd:L12, real_69c60970d4242eda8c47c5fd:L13, real_69c60970d4242eda8c47c5fd:L14, real_69c60970d4242eda8c47c5fd:L15, real_69c60970d4242eda8c47c5fd:L16, real_69c60970d4242eda8c47c5fd:L17, real_69c60970d4242eda8c47c5fd:L18, real_69c60970d4242eda8c47c5fd:L19, real_69c60970d4242eda8c47c5fd:L20, real_69c60970d4242eda8c47c5fd:L21, real_69c60970d4242eda8c47c5fd:L22, real_69c60970d4242eda8c47c5fd:L23, real_69c60970d4242eda8c47c5fd:L24, real_69c60970d4242eda8c47c5fd:L25, real_69c60970d4242eda8c47c5fd:L26, real_69c60970d4242eda8c47c5fd:L6, real_69c60970d4242eda8c47c5fd:L7, real_69c60970d4242eda8c47c5fd:L8
reason: Collected section L6 contains the required content from Chapter 2. Ready to summarize points.
---
=== End Investigate ===
```

### Evidence text (new)

```
[E1]
[§ 第二章  对外捐赠的范围及类型]
  第三条本办法所称的“对外捐赠”，是指集团公司及所属各单位自愿将有处分权的合法财产无偿赠送给合法的受赠人（包含无偿捐赠工程），用于与捐赠人生产经营活动没有直接关系的公益事业的行为。
  集团公司所属非法人分支机构、项目部不得以分公司、项目部名义对外捐赠，不得将企业拥有的财产以个人名义对外捐赠。
  对外捐赠原则上以集团公司（陕西建工第十一建设集团有限公司）名义进行捐赠，独立法人单位可根据实际需要以本单位名义进行捐赠。

[E2]
[§ 第五条  对外捐赠的范围]
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
```

### Evidence text (old)

```
[E1]
[§ 第五条  对外捐赠的范围]
用于对外捐赠的资产应当权属清晰，应为集团公司有权处分的合法财产，包括现金资产和实物资产等。

[E2]
[§ 第五条  对外捐赠的范围]
（二）持有的股权和债权；

[E3]
[§ 第四条  对外捐赠的类型]
（三）其他捐赠，即除上述捐赠外，为促进社会发展以及集团公司履行社会责任需要的其他捐赠，含外部各类活动赞助。

[E4]
[§ 第五条  对外捐赠的范围]
（六）设定担保物权的财产；

[E5]
[§ 第五条  对外捐赠的范围]
（四）国家财政拨款；

[E6]
[§ 第四条  对外捐赠的类型]
各单位要正确参与社会公益事业，依法依规确定对外捐赠范围和支出规模，规范开展对外捐赠活动，避免无序、随意捐赠等行为。对于有关社会机构、团体的摊派性捐赠，要坚决依法拒绝，

[E7]
[§ 第五条  对外捐赠的范围]
（一）生产经营用的主要固定资产；

[E8]
[§ 第五条  对外捐赠的范围]
（九）企业拥有的知识产权。

[E9]
[§ 第四条  对外捐赠的类型]
（二）公益性捐赠，即向科技文卫事业和环境保护等社会公益事业的公益性捐赠。
```
