# Map-Nav Trace Replay (recursive DISPATCH)

- generated_at: `2026-07-14T21:06:30`
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
| evidence_chars | 210 | 500 |
| gold_node_recall | 0.0 | 0.5 |
| n_retrieved_nodes | 2 | 12 |
| trajectory_steps | n/a | 4 |

### Gold node hits (new)

- `real_69c6095ed4242eda8c47c5b2:L2` [MISS] retrieved=False in_text=False
- `real_69c6095ed4242eda8c47c5b2:L3` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6095ed4242eda8c47c5b2:L1` scope=`real_69c6095ed4242eda8c47c5b2:L1` depth=`1`
- reason: rule_fallback_illegal_action
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
- reason: Dispatch main section to gather all relevant content for the query.
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
[§ 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） / 三、考核管理及结果应用 / （ 二 ）学员学习考核管理 / 4.其他事项]
（ 3 ）十一在线平台中心后期将根据后台创建的线下培训记录，不定期抽查相关学习资料，保证学习的真实性和有效性。如发现有不实情形，获得该门线下培训学时的学员，学时为不合格，并给予相关人员通报。

[E2]
[§ 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） / 一、管理机构及其职责 / （ 五）机关各部室及各二级单位]
2.督促本部室及本单位员工开展在线学习，并结合线上学习内容和业务实际，组织本部室及本单位开展线下探讨、分享、集中培训等。

[E3]
[§ 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） / 二、课程及指派管理 / （ 一）课程类别]
明确课程名称、课程类别、必修岗位、课程开发负责人等信息（见附件），提交十一在线平台中心审批后按计划开发。

[E4]
[§ 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） / 三、考核管理及结果应用 / （ 一）课程开发管理]
4.课
```

### Evidence text (old)

```
[E1]
线上学习平台主要为除十一在线各研修班以外一般员工提供学习资源。十一在线平台中心为其最高管理机构负责把握学习方向、整合学习资源，各专家组负责学习内容开发，十一在线平台中心办公室主要负责日常运营管理，集团公司机关各部室及各二级单位负责组织本部室及本单位员工参加学习。各级机构及其职责具体如下：

[E2]
（ 一）十一在线平台中心：负责课程体系设计、课程开发计划审批、课程考核标准设定、平台建设费用审批等相关事宜。
```

## real_69c60974d4242eda8c47c615_scope_collection_auto_0030 (scope_collection)

**Query:** 列出重大事故隐患治理方案必须包含的所有内容要素。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 500 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 12 | 5 |
| trajectory_steps | n/a | 7 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L94` [MISS] retrieved=False in_text=False
- `real_69c60974d4242eda8c47c615:L95` [MISS] retrieved=False in_text=False
- `real_69c60974d4242eda8c47c615:L96` [MISS] retrieved=False in_text=False
- `real_69c60974d4242eda8c47c615:L97` [MISS] retrieved=False in_text=False
- `real_69c60974d4242eda8c47c615:L98` [MISS] retrieved=False in_text=False
- `real_69c60974d4242eda8c47c615:L99` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C2` kind=`collect` section=`real_69c60974d4242eda8c47c615:L93` scope=`real_69c60974d4242eda8c47c615:L92` depth=`1`
- reason: Collect all listed elements of the major accident hazard governance plan.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L93', 'real_69c60974d4242eda8c47c615:L94', 'real_69c60974d4242eda8c47c615:L95', 'real_69c60974d4242eda8c47c615:L96', 'real_69c60974d4242eda8c47c615:L97', 'real_69c60974d4242eda8c47c615:L98', 'real_69c60974d4242eda8c47c615:L99']
- collect added=7 hits=7 branch_selected=True collect_full=True
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

**Step 2** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60974d4242eda8c47c615:L92` scope=`real_69c60974d4242eda8c47c615:L92` depth=`1`
- reason: Collect section 2.4.4 which details the required elements of the major accident hazard governance plan.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L92']
- collect added=11 hits=11 branch_selected=True collect_full=True
- legal_actions (6):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0734
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L100 | 隐患程度严重或整改难度大者，二级单位必须按带班检查制度指派二级单位负责人（总经理或生产、技术总工）监督整改。整改完成后在隐患整改回复单填写自检情况（须附证明材料），项目负责人复查验证，签字确认后上报二级单位，由二级单位复查确认后上报集团公司安全管理部。 | score=0.0529
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L101 | 集团公司安全管理部依据整改情况决定验证，销项。 | score=0.0302
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0660
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L103 | 2.4.6 各项目部应当加强对自然灾害的预防。对于因自然灾害可能导致事故灾难的隐患，应当按照有关法律、法规、标准和本制度的要求排查治理，采取可靠的预防措施，制定应急预案。在接到有关自然灾害预报时，应当及时向有关人员发出预警通知；发生自然灾害可能危及施工和人员安全的情况时，应当采取撤离人员、停止作业、加强监测等安全措施，并及时向当地人民政府有关部门报告。 | score=0.0639
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 1511

**Step 3** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60974d4242eda8c47c615:L92` depth=`1`
- reason: Collected sections L92 and L93 contain the required elements for major accident hazard governance plans.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 189

**Step 4** `nav_dispatch`  id=`D11` kind=`dispatch` section=`real_69c60974d4242eda8c47c615:L92` scope=`None` depth=`0`
- reason: Dispatch to collect the full list of elements required in a major accident hazard governance plan.
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

**Step 5** `nav_collect`  id=`C10` kind=`collect` section=`real_69c60974d4242eda8c47c615:L82` scope=`None` depth=`0`
- reason: Collect definition of major accident hazards to ensure completeness of governance plan elements.
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

**Step 6** `nav_collect`  id=`C10` kind=`collect` section=`real_69c60974d4242eda8c47c615:L84` scope=`None` depth=`0`
- reason: Collect definition of major accident hazards to ensure governance plan elements are complete.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L84']
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
- projection_chars: 3382

**Step 7** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Collected evidence from L92 and L93 contains the required elements for major accident hazard governance plans.
- legal_actions (55):
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
- projection_chars: 3246

### Subagent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60974d4242eda8c47c615:L92 (ok)
collected 12 branch node(s); explicit roots=['real_69c60974d4242eda8c47c615:L93', 'real_69c60974d4242eda8c47c615:L92']
collected: real_69c60974d4242eda8c47c615:L100, real_69c60974d4242eda8c47c615:L101, real_69c60974d4242eda8c47c615:L102, real_69c60974d4242eda8c47c615:L103, real_69c60974d4242eda8c47c615:L92, real_69c60974d4242eda8c47c615:L93, real_69c60974d4242eda8c47c615:L94, real_69c60974d4242eda8c47c615:L95, real_69c60974d4242eda8c47c615:L96, real_69c60974d4242eda8c47c615:L97, real_69c60974d4242eda8c47c615:L98, real_69c60974d4242eda8c47c615:L99
reason: Collected sections L92 and L93 contain the required elements for major accident hazard governance plans.
---
=== End Investigate ===
```

### Evidence text (new)

```
[E1]
[§ 2.4.4 重大事故隐患整改、复查、销项]
对重大事故隐患，由被检查项目负责整改，整改应制定事故隐患治理方案，该方案由项目经理组织制定和实施。方案包括以下内容：

[E2]
2、重大事故隐患，是指危害和整改难度较大，应当全部或者局部停产停业，并经过一定时间整改治理方能排除的隐患，或者因外部因素影响致使生产经营单位自身难以排除的隐患。

[E3]
[§ 2.4.4 重大事故隐患整改、复查、销项]
2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。

[E4]
[§ 2.4.4 重大事故隐患整改、复查、销项]
2.4.6 各项目部应当加强对自然灾害的预防。对于因自然灾害可能导致事故灾难的隐患，应当按照有关法律、法规、标准和本制度的要求排查治理，采取可靠的预防措施，制定应急预案。在接到有关自然灾害预报时，应当及时向有关人员发出预警通
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
