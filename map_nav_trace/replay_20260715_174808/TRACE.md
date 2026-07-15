# Map-Nav Trace Replay (recursive DISPATCH)

- generated_at: `2026-07-15T17:48:09`
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
| evidence_chars | 210 | 487 |
| gold_node_recall | 0.0 | 0.5 |
| n_retrieved_nodes | 2 | 11 |
| trajectory_steps | n/a | 4 |

### Gold node hits (new)

- `real_69c6095ed4242eda8c47c5b2:L2` [MISS] retrieved=False in_text=False
- `real_69c6095ed4242eda8c47c5b2:L3` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C4` kind=`collect` section=`real_69c6095ed4242eda8c47c5b2:L4` scope=`None` depth=`0`
- reason: Collect adjacent sections on management structure and office duties to answer the query.
- collect_section_ids: ['real_69c6095ed4242eda8c47c5b2:L4', 'real_69c6095ed4242eda8c47c5b2:L7']
- collect added=2 hits=2 branch_selected=True collect_full=True
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

**Step 2** `nav_collect`  id=`C10` kind=`collect` section=`real_69c6095ed4242eda8c47c5b2:L14` scope=`None` depth=`0`
- reason: Collect C10 to obtain the second adjacent evidence point regarding employee learning supervision and offline training organization.
- collect_section_ids: ['real_69c6095ed4242eda8c47c5b2:L14']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (50):
  - C1 | COLLECT | real_69c6095ed4242eda8c47c5b2:L1 | 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） | score=0.0722
  - D1 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L1 | 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） | score=0.0722
  - C2 | COLLECT | real_69c6095ed4242eda8c47c5b2:L2 | 为进一步深化学习型组织建设，整合学习资源，传播最佳实践，有效助力员工工作技能提升和绩效改善。为进一步强化学习效果，规范线上学习管理，特制订本方案。 | score=0.0616
  - C3 | COLLECT | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0697
  - D2 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0697
  - C4 | COLLECT | real_69c6095ed4242eda8c47c5b2:L5 | （ 一）十一在线平台中心：负责课程体系设计、课程开发计划审批、课程考核标准设定、平台建设费用审批等相关事宜。 | score=0.0587
  - C5 | COLLECT | real_69c6095ed4242eda8c47c5b2:L8 | 踪和定期调研，反馈十一在线平台中心。 | score=0.0589
  - C6 | COLLECT | real_69c6095ed4242eda8c47c5b2:L9 | （ 四）平台管理员 | score=0.0599
  - D3 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L9 | （ 四）平台管理员 | score=0.0599
  - C7 | COLLECT | real_69c6095ed4242eda8c47c5b2:L11 | 2.各二级单位平台管理员：负责督促本单位各类课件指定人员在线学习，按时完成学习计划，并向各专家组及十一在线平台中心办公室反馈学习情况。 | score=0.0599
  - C8 | COLLECT | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0697
  - D4 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0697
  - C9 | COLLECT | real_69c6095ed4242eda8c47c5b2:L13 | 1.协同做好线上学习平台的推广、使用和维护等日常管理工作，配合各专家组完成本业务条线培训课程开发、选配工作。 | score=0.0565
  - C10 | COLLECT | real_69c6095ed4242eda8c47c5b2:L14 | 2.督促本部室及本单位员工开展在线学习，并结合线上学习内容和业务实际，组织本部室及本单位开展线下探讨、分享、集中培训等。 | score=0.0697
  - C11 | COLLECT | real_69c6095ed4242eda8c47c5b2:L15 | （ 六 ）学员 | score=0.0599
  - D5 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L15 | （ 六 ）学员 | score=0.0599
- projection_chars: 3541

**Step 3** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6095ed4242eda8c47c5b2:L1` scope=`None` depth=`0`
- reason: Collect full document to find adjacent evidence sections for the query.
- collect_section_ids: ['real_69c6095ed4242eda8c47c5b2:L1']
- collect added=36 hits=36 branch_selected=True collect_full=True
- legal_actions (50):
  - C1 | COLLECT | real_69c6095ed4242eda8c47c5b2:L1 | 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） | score=0.0722
  - D1 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L1 | 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） | score=0.0722
  - C2 | COLLECT | real_69c6095ed4242eda8c47c5b2:L2 | 为进一步深化学习型组织建设，整合学习资源，传播最佳实践，有效助力员工工作技能提升和绩效改善。为进一步强化学习效果，规范线上学习管理，特制订本方案。 | score=0.0616
  - C3 | COLLECT | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0697
  - D2 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0697
  - C4 | COLLECT | real_69c6095ed4242eda8c47c5b2:L5 | （ 一）十一在线平台中心：负责课程体系设计、课程开发计划审批、课程考核标准设定、平台建设费用审批等相关事宜。 | score=0.0587
  - C5 | COLLECT | real_69c6095ed4242eda8c47c5b2:L8 | 踪和定期调研，反馈十一在线平台中心。 | score=0.0589
  - C6 | COLLECT | real_69c6095ed4242eda8c47c5b2:L9 | （ 四）平台管理员 | score=0.0599
  - D3 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L9 | （ 四）平台管理员 | score=0.0599
  - C7 | COLLECT | real_69c6095ed4242eda8c47c5b2:L11 | 2.各二级单位平台管理员：负责督促本单位各类课件指定人员在线学习，按时完成学习计划，并向各专家组及十一在线平台中心办公室反馈学习情况。 | score=0.0599
  - C8 | COLLECT | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0697
  - D4 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0697
  - C9 | COLLECT | real_69c6095ed4242eda8c47c5b2:L13 | 1.协同做好线上学习平台的推广、使用和维护等日常管理工作，配合各专家组完成本业务条线培训课程开发、选配工作。 | score=0.0565
  - C10 | COLLECT | real_69c6095ed4242eda8c47c5b2:L15 | （ 六 ）学员 | score=0.0599
  - D5 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L15 | （ 六 ）学员 | score=0.0599
  - C11 | COLLECT | real_69c6095ed4242eda8c47c5b2:L16 | 根据课程设置及时完成相应必修课程学习，根据岗位和个人能力的发展规划，合理选修相应课程，积极学以致用，改进工作绩效。 | score=0.0599
- projection_chars: 3543

**Step 4** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence covers management structure and unit responsibilities as requested.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 171

### Evidence text (new)

```
[E1]
[§ 一、管理机构及其职责]
  线上学习平台主要为除十一在线各研修班以外一般员工提供学习资源。十一在线平台中心为其最高管理机构负责把握学习方向、整合学习资源，各专家组负责学习内容开发，十一在线平台中心办公室主要负责日常运营管理，集团公司机关各部室及各二级单位负责组织本部室及本单位员工参加学习。各级机构及其职责具体如下：
  （ 一）十一在线平台中心：负责课程体系设计、课程开发计划审批、课程考核标准设定、平台建设费用审批等相关事宜。
  （ 二）各专家组：负责各领域内员工培训需求征集，教材、课件及习题开发，课件修改、适时更新、审核，业务答疑，题库组建等工作，集团对口业务部门负责人为各专业课程开发责任人，统筹推进本业务系统课程开发工作。
  （ 三）十一在线平台中心办公室：负责线上学习平台搭建，维护平台基本信息，监督各专家组及相关部门及时更新学习内容，组织各专家组和二级单位平台管理员进行平台管理培训，并对各专家组课程开发情况、学员学习情况进行跟
  踪和定期调研，反馈十一在线平台中心。

[E2]
[§ 4.其他事项]
（ 4）其他未尽事宜，另行规定。
```

### Evidence text (old)

```
[E1]
线上学习平台主要为除十一在线各研修班以外一般员工提供学习资源。十一在线平台中心为其最高管理机构负责把握学习方向、整合学习资源，各专家组负责学习内容开发，十一在线平台中心办公室主要负责日常运营管理，集团公司机关各部室及各二级单位负责组织本部室及本单位员工参加学习。各级机构及其职责具体如下：

[E2]
（ 一）十一在线平台中心：负责课程体系设计、课程开发计划审批、课程考核标准设定、平台建设费用审批等相关事宜。
```

## latest_clean_multi_0051 (multi_hop)

**Query:** 根据《集团公司对外捐赠管理办法（修订版）》中“第四条 对外捐赠的类型”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60970d4242eda8c47c5fd`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 243 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 11 | 5 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60970d4242eda8c47c5fd:L11` [HIT] retrieved=True in_text=False
- `real_69c60970d4242eda8c47c5fd:L12` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C10` kind=`collect` section=`real_69c60970d4242eda8c47c5fd:L10` scope=`None` depth=`0`
- reason: Collect section 4 on donation types to answer the query about adjacent evidence points.
- collect_section_ids: ['real_69c60970d4242eda8c47c5fd:L10']
- collect added=4 hits=4 branch_selected=True collect_full=True
- legal_actions (42):
  - C1 | COLLECT | real_69c60970d4242eda8c47c5fd:L1 | 陕西建工第十一建设集团有限公司 | score=0.0721
  - D1 | DISPATCH | real_69c60970d4242eda8c47c5fd:L1 | 陕西建工第十一建设集团有限公司 | score=0.0721
  - C2 | COLLECT | real_69c60970d4242eda8c47c5fd:L2 | 对外捐赠管理办法（修订版） | score=0.0589
  - C3 | COLLECT | real_69c60970d4242eda8c47c5fd:L3 | 第一章  总则 | score=0.0574
  - D2 | DISPATCH | real_69c60970d4242eda8c47c5fd:L3 | 第一章  总则 | score=0.0574
  - C4 | COLLECT | real_69c60970d4242eda8c47c5fd:L4 | 第一条为进一步规范集团公司对外捐赠行为，加强对外捐赠事项的管理，更好地履行社会责任，全面、有效提升和宣传集团公司品牌及企业形象，特制定本办法。 | score=0.0551
  - C5 | COLLECT | real_69c60970d4242eda8c47c5fd:L5 | 第二条本办法适用于集团公司及所属各单位对外捐赠行为。 | score=0.0574
  - C6 | COLLECT | real_69c60970d4242eda8c47c5fd:L6 | 第二章  对外捐赠的范围及类型 | score=0.0721
  - D3 | DISPATCH | real_69c60970d4242eda8c47c5fd:L6 | 第二章  对外捐赠的范围及类型 | score=0.0721
  - C7 | COLLECT | real_69c60970d4242eda8c47c5fd:L7 | 第三条本办法所称的“对外捐赠”，是指集团公司及所属各单位自愿将有处分权的合法财产无偿赠送给合法的受赠人（包含无偿捐赠工程），用于与捐赠人生产经营活动没有直接关系的公益事业的行为。 | score=0.0721
  - C8 | COLLECT | real_69c60970d4242eda8c47c5fd:L8 | 集团公司所属非法人分支机构、项目部不得以分公司、项目部名义对外捐赠，不得将企业拥有的财产以个人名义对外捐赠。 | score=0.0550
  - C9 | COLLECT | real_69c60970d4242eda8c47c5fd:L9 | 对外捐赠原则上以集团公司（陕西建工第十一建设集团有限公司）名义进行捐赠，独立法人单位可根据实际需要以本单位名义进行捐赠。 | score=0.0690
  - C10 | COLLECT | real_69c60970d4242eda8c47c5fd:L10 | 第四条  对外捐赠的类型 | score=0.0659
  - D4 | DISPATCH | real_69c60970d4242eda8c47c5fd:L10 | 第四条  对外捐赠的类型 | score=0.0659
  - C11 | COLLECT | real_69c60970d4242eda8c47c5fd:L11 | （一）救济性捐赠，即向受灾地区、扶贫地区或者困难的社会弱势群体的救济性捐赠。 | score=0.0566
  - C12 | COLLECT | real_69c60970d4242eda8c47c5fd:L12 | （二）公益性捐赠，即向科技文卫事业和环境保护等社会公益事业的公益性捐赠。 | score=0.0572
- projection_chars: 3437

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Assembled evidence G1 contains the complete content of Article 4 regarding donation types, sufficient to answer the query.
- legal_actions (41):
  - D1 | DISPATCH | real_69c60970d4242eda8c47c5fd:L1 | 陕西建工第十一建设集团有限公司 | score=0.0721
  - C1 | COLLECT | real_69c60970d4242eda8c47c5fd:L2 | 对外捐赠管理办法（修订版） | score=0.0589
  - C2 | COLLECT | real_69c60970d4242eda8c47c5fd:L3 | 第一章  总则 | score=0.0574
  - D2 | DISPATCH | real_69c60970d4242eda8c47c5fd:L3 | 第一章  总则 | score=0.0574
  - C3 | COLLECT | real_69c60970d4242eda8c47c5fd:L4 | 第一条为进一步规范集团公司对外捐赠行为，加强对外捐赠事项的管理，更好地履行社会责任，全面、有效提升和宣传集团公司品牌及企业形象，特制定本办法。 | score=0.0551
  - C4 | COLLECT | real_69c60970d4242eda8c47c5fd:L5 | 第二条本办法适用于集团公司及所属各单位对外捐赠行为。 | score=0.0574
  - D3 | DISPATCH | real_69c60970d4242eda8c47c5fd:L6 | 第二章  对外捐赠的范围及类型 | score=0.0721
  - C5 | COLLECT | real_69c60970d4242eda8c47c5fd:L7 | 第三条本办法所称的“对外捐赠”，是指集团公司及所属各单位自愿将有处分权的合法财产无偿赠送给合法的受赠人（包含无偿捐赠工程），用于与捐赠人生产经营活动没有直接关系的公益事业的行为。 | score=0.0721
  - C6 | COLLECT | real_69c60970d4242eda8c47c5fd:L8 | 集团公司所属非法人分支机构、项目部不得以分公司、项目部名义对外捐赠，不得将企业拥有的财产以个人名义对外捐赠。 | score=0.0550
  - C7 | COLLECT | real_69c60970d4242eda8c47c5fd:L9 | 对外捐赠原则上以集团公司（陕西建工第十一建设集团有限公司）名义进行捐赠，独立法人单位可根据实际需要以本单位名义进行捐赠。 | score=0.0690
  - C8 | COLLECT | real_69c60970d4242eda8c47c5fd:L15 | 第五条  对外捐赠的范围 | score=0.0676
  - D4 | DISPATCH | real_69c60970d4242eda8c47c5fd:L15 | 第五条  对外捐赠的范围 | score=0.0676
  - C9 | COLLECT | real_69c60970d4242eda8c47c5fd:L16 | 用于对外捐赠的资产应当权属清晰，应为集团公司有权处分的合法财产，包括现金资产和实物资产等。 | score=0.0676
  - C10 | COLLECT | real_69c60970d4242eda8c47c5fd:L17 | 不具处分权的财产或者不合格产品不得用于对外捐赠。下列资产不得用于对外捐赠： | score=0.0596
  - C11 | COLLECT | real_69c60970d4242eda8c47c5fd:L18 | （一）生产经营用的主要固定资产； | score=0.0565
  - C12 | COLLECT | real_69c60970d4242eda8c47c5fd:L19 | （二）持有的股权和债权； | score=0.0540
- projection_chars: 3489

### Evidence text (new)

```
[E1]
[§ 第四条  对外捐赠的类型]
  （一）救济性捐赠，即向受灾地区、扶贫地区或者困难的社会弱势群体的救济性捐赠。
  （二）公益性捐赠，即向科技文卫事业和环境保护等社会公益事业的公益性捐赠。
  （三）其他捐赠，即除上述捐赠外，为促进社会发展以及集团公司履行社会责任需要的其他捐赠，含外部各类活动赞助。
  各单位要正确参与社会公益事业，依法依规确定对外捐赠范围和支出规模，规范开展对外捐赠活动，避免无序、随意捐赠等行为。对于有关社会机构、团体的摊派性捐赠，要坚决依法拒绝，
```

### Evidence text (old)

```
[E1]
[§ 陕西建工第十一建设集团有限公司 / 第一章  总则]
第二条本办法适用于集团公司及所属各单位对外捐赠行为。

[E2]
[§ 陕西建工第十一建设集团有限公司]
对外捐赠管理办法（修订版）

[E3]
[§ 陕西建工第十一建设集团有限公司 / 第二章  对外捐赠的范围及类型 / 第四条  对外捐赠的类型]
（三）其他捐赠，即除上述捐赠外，为促进社会发展以及集团公司履行社会责任需要的其他捐赠，含外部各类活动赞助。

[E4]
[§ 陕西建工第十一建设集团有限公司 / 第二章  对外捐赠的范围及类型 / 第五条  对外捐赠的范围]
用于对外捐赠的资产应当权属清晰，应为集团公司有权处分的合法财产，包括现金资产和实物资产等。

[E5]
[§ 陕西建工第十一建设集团有限公司 / 第二章  对外捐赠的范围及类型 / 第五条  对外捐赠的范围]
（四）国家财政拨款；

[E6]
[§ 陕西建工第十一建设集团有限公司 / 第二章  对外捐赠的范围及类型 / 第四条  对外捐赠的类型]
各单位要正确参与社会公益事业，依法依规确定对外捐赠范围和支出规模，规范开展对外捐赠活动，避免无序、随意
```

## latest_clean_multi_0064 (multi_hop)

**Query:** 根据《集团公司对外捐赠管理办法（修订版）》中“第四章 对外捐赠的审批程序”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60970d4242eda8c47c5fd`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 236 | 484 |
| gold_node_recall | 0.0 | 0.5 |
| n_retrieved_nodes | 3 | 7 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60970d4242eda8c47c5fd:L35` [MISS] retrieved=False in_text=False
- `real_69c60970d4242eda8c47c5fd:L36` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C21` kind=`collect` section=`real_69c60970d4242eda8c47c5fd:L34` scope=`None` depth=`0`
- reason: Collect Chapter 4 sections C24 and C25 to explain the two adjacent approval procedure points.
- collect_section_ids: ['real_69c60970d4242eda8c47c5fd:L34', 'real_69c60970d4242eda8c47c5fd:L37', 'real_69c60970d4242eda8c47c5fd:L38']
- collect added=8 hits=10 branch_selected=False collect_full=True
- legal_actions (42):
  - C1 | COLLECT | real_69c60970d4242eda8c47c5fd:L1 | 陕西建工第十一建设集团有限公司 | score=0.0731
  - D1 | DISPATCH | real_69c60970d4242eda8c47c5fd:L1 | 陕西建工第十一建设集团有限公司 | score=0.0731
  - C2 | COLLECT | real_69c60970d4242eda8c47c5fd:L2 | 对外捐赠管理办法（修订版） | score=0.0586
  - C3 | COLLECT | real_69c60970d4242eda8c47c5fd:L3 | 第一章  总则 | score=0.0568
  - D2 | DISPATCH | real_69c60970d4242eda8c47c5fd:L3 | 第一章  总则 | score=0.0568
  - C4 | COLLECT | real_69c60970d4242eda8c47c5fd:L4 | 第一条为进一步规范集团公司对外捐赠行为，加强对外捐赠事项的管理，更好地履行社会责任，全面、有效提升和宣传集团公司品牌及企业形象，特制定本办法。 | score=0.0551
  - C5 | COLLECT | real_69c60970d4242eda8c47c5fd:L5 | 第二条本办法适用于集团公司及所属各单位对外捐赠行为。 | score=0.0568
  - C6 | COLLECT | real_69c60970d4242eda8c47c5fd:L6 | 第二章  对外捐赠的范围及类型 | score=0.0657
  - D3 | DISPATCH | real_69c60970d4242eda8c47c5fd:L6 | 第二章  对外捐赠的范围及类型 | score=0.0657
  - C7 | COLLECT | real_69c60970d4242eda8c47c5fd:L7 | 第三条本办法所称的“对外捐赠”，是指集团公司及所属各单位自愿将有处分权的合法财产无偿赠送给合法的受赠人（包含无偿捐赠工程），用于与捐赠人生产经营活动没有直接关系的公益事业的行为。 | score=0.0657
  - C8 | COLLECT | real_69c60970d4242eda8c47c5fd:L9 | 对外捐赠原则上以集团公司（陕西建工第十一建设集团有限公司）名义进行捐赠，独立法人单位可根据实际需要以本单位名义进行捐赠。 | score=0.0633
  - C9 | COLLECT | real_69c60970d4242eda8c47c5fd:L10 | 第四条  对外捐赠的类型 | score=0.0609
  - D4 | DISPATCH | real_69c60970d4242eda8c47c5fd:L10 | 第四条  对外捐赠的类型 | score=0.0609
  - C10 | COLLECT | real_69c60970d4242eda8c47c5fd:L13 | （三）其他捐赠，即除上述捐赠外，为促进社会发展以及集团公司履行社会责任需要的其他捐赠，含外部各类活动赞助。 | score=0.0568
  - C11 | COLLECT | real_69c60970d4242eda8c47c5fd:L14 | 各单位要正确参与社会公益事业，依法依规确定对外捐赠范围和支出规模，规范开展对外捐赠活动，避免无序、随意捐赠等行为。对于有关社会机构、团体的摊派性捐赠，要坚决依法拒绝， | score=0.0609
  - C12 | COLLECT | real_69c60970d4242eda8c47c5fd:L15 | 第五条  对外捐赠的范围 | score=0.0634
- projection_chars: 3590

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains Chapter 4 approval procedures with all required points for the query.
- legal_actions (44):
  - D1 | DISPATCH | real_69c60970d4242eda8c47c5fd:L1 | 陕西建工第十一建设集团有限公司 | score=0.0731
  - C1 | COLLECT | real_69c60970d4242eda8c47c5fd:L2 | 对外捐赠管理办法（修订版） | score=0.0586
  - C2 | COLLECT | real_69c60970d4242eda8c47c5fd:L3 | 第一章  总则 | score=0.0568
  - D2 | DISPATCH | real_69c60970d4242eda8c47c5fd:L3 | 第一章  总则 | score=0.0568
  - C3 | COLLECT | real_69c60970d4242eda8c47c5fd:L4 | 第一条为进一步规范集团公司对外捐赠行为，加强对外捐赠事项的管理，更好地履行社会责任，全面、有效提升和宣传集团公司品牌及企业形象，特制定本办法。 | score=0.0551
  - C4 | COLLECT | real_69c60970d4242eda8c47c5fd:L5 | 第二条本办法适用于集团公司及所属各单位对外捐赠行为。 | score=0.0568
  - C5 | COLLECT | real_69c60970d4242eda8c47c5fd:L6 | 第二章  对外捐赠的范围及类型 | score=0.0657
  - D3 | DISPATCH | real_69c60970d4242eda8c47c5fd:L6 | 第二章  对外捐赠的范围及类型 | score=0.0657
  - C6 | COLLECT | real_69c60970d4242eda8c47c5fd:L7 | 第三条本办法所称的“对外捐赠”，是指集团公司及所属各单位自愿将有处分权的合法财产无偿赠送给合法的受赠人（包含无偿捐赠工程），用于与捐赠人生产经营活动没有直接关系的公益事业的行为。 | score=0.0657
  - C7 | COLLECT | real_69c60970d4242eda8c47c5fd:L8 | 集团公司所属非法人分支机构、项目部不得以分公司、项目部名义对外捐赠，不得将企业拥有的财产以个人名义对外捐赠。 | score=0.0529
  - C8 | COLLECT | real_69c60970d4242eda8c47c5fd:L9 | 对外捐赠原则上以集团公司（陕西建工第十一建设集团有限公司）名义进行捐赠，独立法人单位可根据实际需要以本单位名义进行捐赠。 | score=0.0633
  - C9 | COLLECT | real_69c60970d4242eda8c47c5fd:L10 | 第四条  对外捐赠的类型 | score=0.0609
  - D4 | DISPATCH | real_69c60970d4242eda8c47c5fd:L10 | 第四条  对外捐赠的类型 | score=0.0609
  - C10 | COLLECT | real_69c60970d4242eda8c47c5fd:L11 | （一）救济性捐赠，即向受灾地区、扶贫地区或者困难的社会弱势群体的救济性捐赠。 | score=0.0510
  - C11 | COLLECT | real_69c60970d4242eda8c47c5fd:L12 | （二）公益性捐赠，即向科技文卫事业和环境保护等社会公益事业的公益性捐赠。 | score=0.0514
  - C12 | COLLECT | real_69c60970d4242eda8c47c5fd:L13 | （三）其他捐赠，即除上述捐赠外，为促进社会发展以及集团公司履行社会责任需要的其他捐赠，含外部各类活动赞助。 | score=0.0568
- projection_chars: 3460

### Evidence text (new)

```
[E1]
[§ 第四章  对外捐赠的审批程序]
  凡涉及对外捐赠事宜，不论捐赠支出规模大小，必须经过严格的审批流程，未经批准的捐赠行为一律不得实施。
  （一）各单位需在本单位内部履行“三重一大”决策程序后，以书面请示报送集团公司办公室。请示材料应包括对外捐赠请示（包括捐赠金额、捐赠原因、捐赠类型、捐赠性质和受赠对象的基本情况等）、“三重一大”决策情况、财务部门审核意见等。
  （二）经集团公司党委会前置研究、董事会审议同意后报送陕建控股集团核准。经陕建控股集团研究决定后，给予书面答复。
  （三）所有捐赠事宜得到陕建控股集团批复同意后，由捐赠单位会同集团公司财务管理服务中心办理捐赠有关手续。
  （四）对于突发性重大自然灾害或者其他特殊事项需要紧急安排对外捐赠支出，不论金额大小，各单位在履行内部决策程序后，可先向集团公司办公室口头请示或备案后进行捐赠。并在事后在3个工作日内逐笔履行相应审批程序，并向集团公司报送对外捐赠事项相关情况，由集团公司财务管理服务中心向陕建控股集团履行相应程序。
  （五）集团公司公益基金对外捐赠按照公益基金相关管理办法执行。
```

### Evidence text (old)

```
[E1]
（一）各单位需在本单位内部履行“三重一大”决策程序后，以书面请示报送集团公司办公室。请示材料应包括对外捐赠请示（包括捐赠金额、捐赠原因、捐赠类型、捐赠性质和受赠对象的基本情况等）、“三重一大”决策情况、财务部门审核意见等。

[E2]
（三）所有捐赠事宜得到陕建控股集团批复同意后，由捐赠单位会同集团公司财务管理服务中心办理捐赠有关手续。

[E3]
（二）经集团公司党委会前置研究、董事会审议同意后报送陕建控股集团核准。经陕建控股集团研究决定后，给予书面答复。
```

## latest_clean_multi_0075 (multi_hop)

**Query:** 根据《陕西建工第十一建设集团有限公司印章管理办法（2020版）》中“陕西建工第十一建设集团有限公司印章管理办法（2020版）.docx”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60971d4242eda8c47c605`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 292 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 9 | 4 |
| trajectory_steps | n/a | 3 |

### Gold node hits (new)

- `real_69c60971d4242eda8c47c605:L2` [MISS] retrieved=False in_text=False
- `real_69c60971d4242eda8c47c605:L3` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C3` kind=`collect` section=`real_69c60971d4242eda8c47c605:L19` scope=`None` depth=`0`
- reason: Select adjacent leaf nodes C3 and C4 to extract key points regarding seal creation and project department seal usage procedures.
- collect_section_ids: ['real_69c60971d4242eda8c47c605:L19', 'real_69c60971d4242eda8c47c605:L21']
- collect added=2 hits=2 branch_selected=True collect_full=True
- legal_actions (44):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0646
  - D1 | DISPATCH | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0646
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L9 | （一）集团公司机关各部门章，二级单位章，由集团办公室根据集团公司或上级有关部门批准成立该机构的文件制发。 | score=0.0539
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L19 | 确因工作需要刻制印章的，由用印单位或部门提出申请，详细说明印章的名称、用途、式样和规格，报集团公司主要领导批准后由办公室制发。 | score=0.0646
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L21 | 第七条项目部印章在使用前，项目部应负责将集团公司办公室出具的印章启用文件报送建设单位、监理单位等相关方，以便业务往来确认。并在文件送达后一周内将回执返回集团公司办公室留存。 | score=0.0634
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L22 | 第八条印章使用过程中，如应变更或者因损坏需要重新刻制的，由使用单位或部门提出申请，经单位或部门负责人审批后，报集团公司办公室进行重新刻制。新印章需重新办理启用手续，原印章同时交回集团公司办公室。 | score=0.0502
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L23 | 第九条发生印章遗失，印章责任管理单位应在24小时内向集团公司和当地公安机关报告；在3个工作日内在省级以上报刊办理遗失声明，并向集团公司申请出具告知函，及时通知相关单位。印章遗失处理流程见附件。 | score=0.0594
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L24 | 印章责任管理单位应将印章遗失报告、遗失声明、告知函回复等相关资料在一月内报集团公司办公室，以备查考。 | score=0.0628
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0654
  - D2 | DISPATCH | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0654
  - C9 | COLLECT | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0545
  - D3 | DISPATCH | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0545
  - C10 | COLLECT | real_69c60971d4242eda8c47c605:L41 | （五）集团公司内部专业分包合同签订； | score=0.0498
  - C11 | COLLECT | real_69c60971d4242eda8c47c605:L42 | （六）集团公司法人明确授权或者委托对外使用印章的事项。 | score=0.0545
  - C12 | COLLECT | real_69c60971d4242eda8c47c605:L49 | 第十二条 项目部印章使用范围 | score=0.0654
  - D4 | DISPATCH | real_69c60971d4242eda8c47c605:L49 | 第十二条 项目部印章使用范围 | score=0.0654
- projection_chars: 3578

**Step 2** `nav_collect`  id=`C7` kind=`collect` section=`real_69c60971d4242eda8c47c605:L24` scope=`None` depth=`0`
- reason: Collect adjacent sections C7 and C15 to compare their key points as requested.
- collect_section_ids: ['real_69c60971d4242eda8c47c605:L24', 'real_69c60971d4242eda8c47c605:L56']
- collect added=2 hits=2 branch_selected=True collect_full=True
- legal_actions (46):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L1 | 第一章 总则 | score=0.0497
  - D1 | DISPATCH | real_69c60971d4242eda8c47c605:L1 | 第一章 总则 | score=0.0497
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L2 | 第一条为规范集团公司及下属单位印章管理工作，有效防范风险，保障经营管理活动的有序开展，特制定本办法。 | score=0.0497
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0646
  - D2 | DISPATCH | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0646
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L9 | （一）集团公司机关各部门章，二级单位章，由集团办公室根据集团公司或上级有关部门批准成立该机构的文件制发。 | score=0.0539
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L22 | 第八条印章使用过程中，如应变更或者因损坏需要重新刻制的，由使用单位或部门提出申请，经单位或部门负责人审批后，报集团公司办公室进行重新刻制。新印章需重新办理启用手续，原印章同时交回集团公司办公室。 | score=0.0502
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L23 | 第九条发生印章遗失，印章责任管理单位应在24小时内向集团公司和当地公安机关报告；在3个工作日内在省级以上报刊办理遗失声明，并向集团公司申请出具告知函，及时通知相关单位。印章遗失处理流程见附件。 | score=0.0594
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L24 | 印章责任管理单位应将印章遗失报告、遗失声明、告知函回复等相关资料在一月内报集团公司办公室，以备查考。 | score=0.0628
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0654
  - D3 | DISPATCH | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0654
  - C9 | COLLECT | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0545
  - D4 | DISPATCH | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0545
  - C10 | COLLECT | real_69c60971d4242eda8c47c605:L41 | （五）集团公司内部专业分包合同签订； | score=0.0498
  - C11 | COLLECT | real_69c60971d4242eda8c47c605:L42 | （六）集团公司法人明确授权或者委托对外使用印章的事项。 | score=0.0545
  - C12 | COLLECT | real_69c60971d4242eda8c47c605:L49 | 第十二条 项目部印章使用范围 | score=0.0654
- projection_chars: 3507

**Step 3** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence collected covers both adjacent sections: G2 (Chapter 2) and G1 (Article 12). Ready to answer.
- legal_actions (45):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L1 | 第一章 总则 | score=0.0497
  - D1 | DISPATCH | real_69c60971d4242eda8c47c605:L1 | 第一章 总则 | score=0.0497
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L2 | 第一条为规范集团公司及下属单位印章管理工作，有效防范风险，保障经营管理活动的有序开展，特制定本办法。 | score=0.0497
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L5 | 集团公司法人章为圆形，直径为4.2CM，中央刊五角星，上环刊单位名称自左向右环排；部门章一律为圆形，直径为3.8CM，上刊集团名称自左向右环排，中央刊五角星，部门名称放在星下方作横排；二级单位公章一律为圆形，直径4.0CM，集团名称自左而右环排，二级单位名称放在星下方作横排。项目部章一律为圆形，直径4.0CM，集团名称和工程名称依次自左而右环排，“工程项目部”字样放在星下方作横排，名称应严格按“陕 | score=0.0483
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0646
  - D2 | DISPATCH | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0646
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L9 | （一）集团公司机关各部门章，二级单位章，由集团办公室根据集团公司或上级有关部门批准成立该机构的文件制发。 | score=0.0539
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L22 | 第八条印章使用过程中，如应变更或者因损坏需要重新刻制的，由使用单位或部门提出申请，经单位或部门负责人审批后，报集团公司办公室进行重新刻制。新印章需重新办理启用手续，原印章同时交回集团公司办公室。 | score=0.0502
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L23 | 第九条发生印章遗失，印章责任管理单位应在24小时内向集团公司和当地公安机关报告；在3个工作日内在省级以上报刊办理遗失声明，并向集团公司申请出具告知函，及时通知相关单位。印章遗失处理流程见附件。 | score=0.0594
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0654
  - D3 | DISPATCH | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0654
  - C9 | COLLECT | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0545
  - D4 | DISPATCH | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0545
  - C10 | COLLECT | real_69c60971d4242eda8c47c605:L41 | （五）集团公司内部专业分包合同签订； | score=0.0498
  - C11 | COLLECT | real_69c60971d4242eda8c47c605:L42 | （六）集团公司法人明确授权或者委托对外使用印章的事项。 | score=0.0545
  - C12 | COLLECT | real_69c60971d4242eda8c47c605:L49 | 第十二条 项目部印章使用范围 | score=0.0654
- projection_chars: 3558

### Evidence text (new)

```
[E1]
[§ 第二章	印章的刻制与启用]
  确因工作需要刻制印章的，由用印单位或部门提出申请，详细说明印章的名称、用途、式样和规格，报集团公司主要领导批准后由办公室制发。
  第七条项目部印章在使用前，项目部应负责将集团公司办公室出具的印章启用文件报送建设单位、监理单位等相关方，以便业务往来确认。并在文件送达后一周内将回执返回集团公司办公室留存。
  印章责任管理单位应将印章遗失报告、遗失声明、告知函回复等相关资料在一月内报集团公司办公室，以备查考。

[E2]
[§ 第十二条 项目部印章使用范围]
（七）项目印章应在项目负责人审批后用印，用印内容不得违背施工合同要件内容。
```

### Evidence text (old)

```
[E1]
[§ 第三章	印章的使用范围 / 第十二条 项目部印章使用范围]
（七）项目印章应在项目负责人审批后用印，用印内容不得违背施工合同要件内容。

[E2]
[§ 第三章	印章的使用范围 / 第十二条 项目部印章使用范围]
（一）项目施工过程中涉及的生产、技术、质量、安全管理等工程资料；

[E3]
[§ 第三章	印章的使用范围 / 第十二条 项目部印章使用范围]
（六）项目部行政后勤相关资料；

[E4]
[§ 第三章	印章的使用范围 / 第十二条 项目部印章使用范围]
（四）项目施工变更资料及签证，项目施工计划及完成统计报表、进度款支付报审资料、认质认价单，与分包分供方各类结算单等；

[E5]
[§ 第三章	印章的使用范围 / 第十二条 项目部印章使用范围]
（五）项目部与两级机关部门业务沟通的相关内部资料，如开复工备案、专项方案、整改回复等资料；

[E6]
[§ 第三章	印章的使用范围 / 第十二条 项目部印章使用范围]
（二）以项目部名义向建设单位、监理单位等出具的有关技术质量和安全生产的业务函件、工作联系单；

[E7]
[§ 第三章	印章的使用范围 / 第十条 机
```

## latest_clean_multi_0133 (multi_hop)

**Query:** 根据《陕西建工第十一建设集团有限公司印章管理办法（2020版）》中“第五章 印章管理”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60971d4242eda8c47c605`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 488 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 9 | 8 |
| trajectory_steps | n/a | 5 |

### Gold node hits (new)

- `real_69c60971d4242eda8c47c605:L74` [HIT] retrieved=True in_text=False
- `real_69c60971d4242eda8c47c605:L75` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C2` kind=`collect` section=`real_69c60971d4242eda8c47c605:L75` scope=`real_69c60971d4242eda8c47c605:L73` depth=`1`
- reason: Collecting C2 (responsibility management) and C9 (sealing standards) to address the query about adjacent evidence points.
- collect_section_ids: ['real_69c60971d4242eda8c47c605:L75', 'real_69c60971d4242eda8c47c605:L88']
- collect added=2 hits=2 branch_selected=True collect_full=True
- legal_actions (17):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L73 | 第五章 印章管理 | score=0.0688
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L75 | 第二十一条集团公司所有印章实行责任管理。其中集团机关各部门主要负责人为部门印章第一管理责任人；二级单位行政主要负责人为本单位印章第一管理责任人，并为所属项目印章第一监管责任人；项目负责人为项目部印章的第一管理责任人；各印章保管人员为印章管理直接责任人，对集团公司负责。 | score=0.0584
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L77 | 第二十三条 集团公司所有印章管理实行严格的专人管理制，印章保管人员须具备以下条件： | score=0.0469
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L80 | （三）正式保管印章前，应接受集团公司或责任管理单位有关印章管理及使用的培训。 | score=0.0409
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L82 | 第二十五条印章保管人发生变更的，印章责任管理单位应填写《集团公司印章管理移交单》（见附件），办理印章移交手续。同时，在变更后三个工作日内报集团公司办公室更新备案。 | score=0.0469
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L83 | 第二十六条 用印登记及资料备存： | score=0.0688
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L84 | 印章保管人在用印前要认真审阅用印内容，检查审批程序，用印后要认真做好用印登记，重要资料做好留存。 | score=0.0469
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L85 | 登记项目包括：时间、用印编号、用印单位（部门）、用印事项说明、份数、经办人、审批人、审批编号、备注等。一般需要留存的材料有： | score=0.0460
  - C9 | COLLECT | real_69c60971d4242eda8c47c605:L88 | 第二十七条符合用印要求的，要规范加盖印章，盖印要端正、清晰、美观、完整，便于识别，印章文字不能歪斜或颠倒。 | score=0.0590
  - C10 | COLLECT | real_69c60971d4242eda8c47c605:L89 | 第二十八条所有印章一律不得在任何空白表格、证明、介绍信、白（稿）纸上加盖印章。确因工作需要的，应由用印单位或部门提出申请，经办公室报集团公司分管领导批准后用印。经办人员应跟踪用印文件使用全过程，事后向集团公司办公室提供用印文件复印件；未使用的，应及时退回集团公司办公室销毁。 | score=0.0688
  - C11 | COLLECT | real_69c60971d4242eda8c47c605:L91 | 第三十条 各印章管理责任单位应认真对印章管理使用情况进行检查监督： | score=0.0663
  - C12 | COLLECT | real_69c60971d4242eda8c47c605:L92 | （一）集团公司办公室应采用定期检查和不定期抽查等方式，对集团公司法人章、机关部门章、二级单位公章、项目章等进行每年不少于两次的检查；二级单位对其所属项目部应进行每年不少于两次的检查。 | score=0.0471
  - C13 | COLLECT | real_69c60971d4242eda8c47c605:L94 | （二）检查监督内容应包括但不限于以下： | score=0.0416
  - C14 | COLLECT | real_69c60971d4242eda8c47c605:L95 | 1.印章保管人责任是否明确、用印交底是否清晰； | score=0.0412
  - C15 | COLLECT | real_69c60971d4242eda8c47c605:L96 | 2.印章启用函件是否已按规定送达至相关单位，有无业务往来确认； | score=0.0452
  - C16 | COLLECT | real_69c60971d4242eda8c47c605:L98 | 4.印章管理使用是否按要求检查，检查是否有记录，对查出的问题是否已整改； | score=0.0539
- projection_chars: 3376

**Step 2** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60971d4242eda8c47c605:L73` scope=`real_69c60971d4242eda8c47c605:L73` depth=`1`
- reason: Collecting all relevant sections under Chapter 5 to extract key points for the two adjacent evidence items.
- collect_section_ids: ['real_69c60971d4242eda8c47c605:L73', 'real_69c60971d4242eda8c47c605:L74', 'real_69c60971d4242eda8c47c605:L77', 'real_69c60971d4242eda8c47c605:L80', 'real_69c60971d4242eda8c47c605:L81', 'real_69c60971d4242eda8c47c605:L82', 'real_69c60971d4242eda8c47c605:L84', 'real_69c60971d4242eda8c47c605:L85', 'real_69c60971d4242eda8c47c605:L89', 'real_69c60971d4242eda8c47c605:L92', 'real_69c60971d4242eda8c47c605:L95', 'real_69c60971d4242eda8c47c605:L96', 'real_69c60971d4242eda8c47c605:L98', 'real_69c60971d4242eda8c47c605:L99']
- collect added=29 hits=41 branch_selected=False collect_full=True
- legal_actions (18):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L73 | 第五章 印章管理 | score=0.0688
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L74 | 第二十条集团公司办公室是集团公司印章的管理部门，负责各类印章的刻制、启用、授权使用、停用、回收及缴销等手续的办理，负责检查各类印章使用情况，负责受理对违反本办法行为的检举、揭发，以及按照本办法对违规行为进行责任追究。 | score=0.0390
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L77 | 第二十三条 集团公司所有印章管理实行严格的专人管理制，印章保管人员须具备以下条件： | score=0.0469
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L80 | （三）正式保管印章前，应接受集团公司或责任管理单位有关印章管理及使用的培训。 | score=0.0409
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L81 | 第二十四条集团公司各类印章保管人资格由其第一管理责任人审查，在集团公司办公室统一备案。 | score=0.0400
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L82 | 第二十五条印章保管人发生变更的，印章责任管理单位应填写《集团公司印章管理移交单》（见附件），办理印章移交手续。同时，在变更后三个工作日内报集团公司办公室更新备案。 | score=0.0469
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L83 | 第二十六条 用印登记及资料备存： | score=0.0688
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L84 | 印章保管人在用印前要认真审阅用印内容，检查审批程序，用印后要认真做好用印登记，重要资料做好留存。 | score=0.0469
  - C9 | COLLECT | real_69c60971d4242eda8c47c605:L85 | 登记项目包括：时间、用印编号、用印单位（部门）、用印事项说明、份数、经办人、审批人、审批编号、备注等。一般需要留存的材料有： | score=0.0460
  - C10 | COLLECT | real_69c60971d4242eda8c47c605:L89 | 第二十八条所有印章一律不得在任何空白表格、证明、介绍信、白（稿）纸上加盖印章。确因工作需要的，应由用印单位或部门提出申请，经办公室报集团公司分管领导批准后用印。经办人员应跟踪用印文件使用全过程，事后向集团公司办公室提供用印文件复印件；未使用的，应及时退回集团公司办公室销毁。 | score=0.0688
  - C11 | COLLECT | real_69c60971d4242eda8c47c605:L91 | 第三十条 各印章管理责任单位应认真对印章管理使用情况进行检查监督： | score=0.0663
  - C12 | COLLECT | real_69c60971d4242eda8c47c605:L92 | （一）集团公司办公室应采用定期检查和不定期抽查等方式，对集团公司法人章、机关部门章、二级单位公章、项目章等进行每年不少于两次的检查；二级单位对其所属项目部应进行每年不少于两次的检查。 | score=0.0471
  - C13 | COLLECT | real_69c60971d4242eda8c47c605:L94 | （二）检查监督内容应包括但不限于以下： | score=0.0416
  - C14 | COLLECT | real_69c60971d4242eda8c47c605:L95 | 1.印章保管人责任是否明确、用印交底是否清晰； | score=0.0412
  - C15 | COLLECT | real_69c60971d4242eda8c47c605:L96 | 2.印章启用函件是否已按规定送达至相关单位，有无业务往来确认； | score=0.0452
  - C16 | COLLECT | real_69c60971d4242eda8c47c605:L98 | 4.印章管理使用是否按要求检查，检查是否有记录，对查出的问题是否已整改； | score=0.0539
- projection_chars: 3347

**Step 3** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60971d4242eda8c47c605:L73` depth=`1`
- reason: Collected evidence from L73 and L75 covers Chapter 5 requirements. Ready to answer query.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 189

**Step 4** `nav_dispatch`  id=`D6` kind=`dispatch` section=`real_69c60971d4242eda8c47c605:L73` scope=`None` depth=`0`
- reason: Dispatch Chapter 5 to gather evidence for the two adjacent points on seal management.
- dispatch_regions: ['real_69c60971d4242eda8c47c605:L73']
- child_reports=1 skipped=0
- legal_actions (44):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0649
  - D1 | DISPATCH | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0649
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L9 | （一）集团公司机关各部门章，二级单位章，由集团办公室根据集团公司或上级有关部门批准成立该机构的文件制发。 | score=0.0523
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L19 | 确因工作需要刻制印章的，由用印单位或部门提出申请，详细说明印章的名称、用途、式样和规格，报集团公司主要领导批准后由办公室制发。 | score=0.0649
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L21 | 第七条项目部印章在使用前，项目部应负责将集团公司办公室出具的印章启用文件报送建设单位、监理单位等相关方，以便业务往来确认。并在文件送达后一周内将回执返回集团公司办公室留存。 | score=0.0637
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L22 | 第八条印章使用过程中，如应变更或者因损坏需要重新刻制的，由使用单位或部门提出申请，经单位或部门负责人审批后，报集团公司办公室进行重新刻制。新印章需重新办理启用手续，原印章同时交回集团公司办公室。 | score=0.0506
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L23 | 第九条发生印章遗失，印章责任管理单位应在24小时内向集团公司和当地公安机关报告；在3个工作日内在省级以上报刊办理遗失声明，并向集团公司申请出具告知函，及时通知相关单位。印章遗失处理流程见附件。 | score=0.0607
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L24 | 印章责任管理单位应将印章遗失报告、遗失声明、告知函回复等相关资料在一月内报集团公司办公室，以备查考。 | score=0.0616
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0627
  - D2 | DISPATCH | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0627
  - C9 | COLLECT | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0519
  - D3 | DISPATCH | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0519
  - C10 | COLLECT | real_69c60971d4242eda8c47c605:L41 | （五）集团公司内部专业分包合同签订； | score=0.0519
  - C11 | COLLECT | real_69c60971d4242eda8c47c605:L42 | （六）集团公司法人明确授权或者委托对外使用印章的事项。 | score=0.0513
  - C12 | COLLECT | real_69c60971d4242eda8c47c605:L49 | 第十二条 项目部印章使用范围 | score=0.0627
  - D4 | DISPATCH | real_69c60971d4242eda8c47c605:L49 | 第十二条 项目部印章使用范围 | score=0.0627
- projection_chars: 3528

**Step 5** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: G3 covers Chapter 5 management responsibilities and G2 covers supervision requirements, addressing the query.
- legal_actions (42):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L1 | 第一章 总则 | score=0.0468
  - D1 | DISPATCH | real_69c60971d4242eda8c47c605:L1 | 第一章 总则 | score=0.0468
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L5 | 集团公司法人章为圆形，直径为4.2CM，中央刊五角星，上环刊单位名称自左向右环排；部门章一律为圆形，直径为3.8CM，上刊集团名称自左向右环排，中央刊五角星，部门名称放在星下方作横排；二级单位公章一律为圆形，直径4.0CM，集团名称自左而右环排，二级单位名称放在星下方作横排。项目部章一律为圆形，直径4.0CM，集团名称和工程名称依次自左而右环排，“工程项目部”字样放在星下方作横排，名称应严格按“陕 | score=0.0468
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0649
  - D2 | DISPATCH | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0649
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L9 | （一）集团公司机关各部门章，二级单位章，由集团办公室根据集团公司或上级有关部门批准成立该机构的文件制发。 | score=0.0523
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L13 | （五）集团公司所属二级子公司法人章、法定代表人章、财务专用章，由该公司携带集团公司的批文和营业执照等资料，到注册所在地的公安机关申报、登记、制印；启用印章前，印模及印章管理人信息报集团公司办公室备案。 | score=0.0486
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L19 | 确因工作需要刻制印章的，由用印单位或部门提出申请，详细说明印章的名称、用途、式样和规格，报集团公司主要领导批准后由办公室制发。 | score=0.0649
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L21 | 第七条项目部印章在使用前，项目部应负责将集团公司办公室出具的印章启用文件报送建设单位、监理单位等相关方，以便业务往来确认。并在文件送达后一周内将回执返回集团公司办公室留存。 | score=0.0637
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L22 | 第八条印章使用过程中，如应变更或者因损坏需要重新刻制的，由使用单位或部门提出申请，经单位或部门负责人审批后，报集团公司办公室进行重新刻制。新印章需重新办理启用手续，原印章同时交回集团公司办公室。 | score=0.0506
  - C9 | COLLECT | real_69c60971d4242eda8c47c605:L23 | 第九条发生印章遗失，印章责任管理单位应在24小时内向集团公司和当地公安机关报告；在3个工作日内在省级以上报刊办理遗失声明，并向集团公司申请出具告知函，及时通知相关单位。印章遗失处理流程见附件。 | score=0.0607
  - C10 | COLLECT | real_69c60971d4242eda8c47c605:L24 | 印章责任管理单位应将印章遗失报告、遗失声明、告知函回复等相关资料在一月内报集团公司办公室，以备查考。 | score=0.0616
  - C11 | COLLECT | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0627
  - D3 | DISPATCH | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0627
  - C12 | COLLECT | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0519
  - D4 | DISPATCH | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0519
- projection_chars: 3647

### Subagent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60971d4242eda8c47c605:L73 (ok)
collected 28 branch node(s); explicit roots=['real_69c60971d4242eda8c47c605:L75', 'real_69c60971d4242eda8c47c605:L73']
collected: real_69c60971d4242eda8c47c605:L100, real_69c60971d4242eda8c47c605:L73, real_69c60971d4242eda8c47c605:L74, real_69c60971d4242eda8c47c605:L75, real_69c60971d4242eda8c47c605:L76, real_69c60971d4242eda8c47c605:L77, real_69c60971d4242eda8c47c605:L78, real_69c60971d4242eda8c47c605:L79, real_69c60971d4242eda8c47c605:L80, real_69c60971d4242eda8c47c605:L81, real_69c60971d4242eda8c47c605:L82, real_69c60971d4242eda8c47c605:L83, real_69c60971d4242eda8c47c605:L84, real_69c60971d4242eda8c47c605:L85, real_69c60971d4242eda8c47c605:L86, real_69c60971d4242eda8c47c605:L87, real_69c60971d4242eda8c47c605:L88, real_69c60971d4242eda8c47c605:L89, real_69c60971d4242eda8c47c605:L90, real_69c60971d4242eda8c47c605:L91
reason: Collected evidence from L73 and L75 covers Chapter 5 requirements. Ready to answer query.
---
=== End Investigate ===
```

### Evidence text (new)

```
[E1]
[§ 第五章 印章管理]
  第二十条集团公司办公室是集团公司印章的管理部门，负责各类印章的刻制、启用、授权使用、停用、回收及缴销等手续的办理，负责检查各类印章使用情况，负责受理对违反本办法行为的检举、揭发，以及按照本办法对违规行为进行责任追究。
  第二十一条集团公司所有印章实行责任管理。其中集团机关各部门主要负责人为部门印章第一管理责任人；二级单位行政主要负责人为本单位印章第一管理责任人，并为所属项目印章第一监管责任人；项目负责人为项目部印章的第一管理责任人；各印章保管人员为印章管理直接责任人，对集团公司负责。
  第二十二条集团公司财务专用章、总会计师名章、银行预留印鉴章由集团公司财务管理部负责全面管理，包括制定审批流程、审定印章保管人资格、印章交底、检查印章使用情况等。

[E2]
[§ 第三十条 各印章管理责任单位应认真对印章管理使用情况进行检查监督：]
  2.印章启用函件是否已按规定送达至相关单位，有无业务往来确认；
  4.印章管理使用是否按要求检查，检查是否有记录，对查出的问题是否已整改；
  5.登记用印的内容是否与用印的内容一致；
```

### Evidence text (old)

```
[E1]
[§ 第五章 印章管理 / 第二十六条 用印登记及资料备存：]
第二十七条符合用印要求的，要规范加盖印章，盖印要端正、清晰、美观、完整，便于识别，印章文字不能歪斜或颠倒。

[E2]
[§ 第五章 印章管理 / 第三十条 各印章管理责任单位应认真对印章管理使用情况进行检查监督：]
5.登记用印的内容是否与用印的内容一致；

[E3]
[§ 第五章 印章管理 / 第三十条 各印章管理责任单位应认真对印章管理使用情况进行检查监督：]
2.印章启用函件是否已按规定送达至相关单位，有无业务往来确认；

[E4]
[§ 第五章 印章管理 / 第三十条 各印章管理责任单位应认真对印章管理使用情况进行检查监督：]
1.印章保管人责任是否明确、用印交底是否清晰；

[E5]
[§ 第五章 印章管理 / 第三十条 各印章管理责任单位应认真对印章管理使用情况进行检查监督：]
3.日常用印是否有审批，审批是否符合规定，用印登记是否齐全；

[E6]
[§ 第五章 印章管理 / 第三十条 各印章管理责任单位应认真对印章管理使用情况进行检查监督：]
4.印章管理使用是否按要求检查，检查是否有记录，对查
```

## latest_clean_multi_0158 (multi_hop)

**Query:** 根据《陕西建工第十一建设集团有限公司印章管理办法（2020版）》中“第六章 印章封口、停用与缴销”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60971d4242eda8c47c605`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 113 | 246 |
| gold_node_recall | 0.0 | 0.5 |
| n_retrieved_nodes | 3 | 4 |
| trajectory_steps | n/a | 3 |

### Gold node hits (new)

- `real_69c60971d4242eda8c47c605:L103` [HIT] retrieved=True in_text=False
- `real_69c60971d4242eda8c47c605:L104` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C23` kind=`collect` section=`real_69c60971d4242eda8c47c605:L102` scope=`None` depth=`0`
- reason: Collect Chapter 6 sections on seal sealing and stoppage to answer the query.
- collect_section_ids: ['real_69c60971d4242eda8c47c605:L102', 'real_69c60971d4242eda8c47c605:L103']
- collect added=2 hits=2 branch_selected=True collect_full=True
- legal_actions (43):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0626
  - D1 | DISPATCH | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0626
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L19 | 确因工作需要刻制印章的，由用印单位或部门提出申请，详细说明印章的名称、用途、式样和规格，报集团公司主要领导批准后由办公室制发。 | score=0.0610
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L21 | 第七条项目部印章在使用前，项目部应负责将集团公司办公室出具的印章启用文件报送建设单位、监理单位等相关方，以便业务往来确认。并在文件送达后一周内将回执返回集团公司办公室留存。 | score=0.0626
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L22 | 第八条印章使用过程中，如应变更或者因损坏需要重新刻制的，由使用单位或部门提出申请，经单位或部门负责人审批后，报集团公司办公室进行重新刻制。新印章需重新办理启用手续，原印章同时交回集团公司办公室。 | score=0.0527
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L23 | 第九条发生印章遗失，印章责任管理单位应在24小时内向集团公司和当地公安机关报告；在3个工作日内在省级以上报刊办理遗失声明，并向集团公司申请出具告知函，及时通知相关单位。印章遗失处理流程见附件。 | score=0.0572
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L24 | 印章责任管理单位应将印章遗失报告、遗失声明、告知函回复等相关资料在一月内报集团公司办公室，以备查考。 | score=0.0594
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0573
  - D2 | DISPATCH | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0573
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0571
  - D3 | DISPATCH | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0571
  - C9 | COLLECT | real_69c60971d4242eda8c47c605:L42 | （六）集团公司法人明确授权或者委托对外使用印章的事项。 | score=0.0571
  - C10 | COLLECT | real_69c60971d4242eda8c47c605:L49 | 第十二条 项目部印章使用范围 | score=0.0573
  - D4 | DISPATCH | real_69c60971d4242eda8c47c605:L49 | 第十二条 项目部印章使用范围 | score=0.0573
  - C11 | COLLECT | real_69c60971d4242eda8c47c605:L54 | （五）项目部与两级机关部门业务沟通的相关内部资料，如开复工备案、专项方案、整改回复等资料； | score=0.0520
  - C12 | COLLECT | real_69c60971d4242eda8c47c605:L56 | （七）项目印章应在项目负责人审批后用印，用印内容不得违背施工合同要件内容。 | score=0.0573
- projection_chars: 3518

**Step 2** `nav_collect`  id=`C25` kind=`collect` section=`real_69c60971d4242eda8c47c605:L106` scope=`None` depth=`0`
- reason: Collect two adjacent sections from Chapter 6 regarding seal suspension and cancellation to answer the query.
- collect_section_ids: ['real_69c60971d4242eda8c47c605:L106', 'real_69c60971d4242eda8c47c605:L107']
- collect added=2 hits=2 branch_selected=True collect_full=True
- legal_actions (45):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0626
  - D1 | DISPATCH | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0626
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L19 | 确因工作需要刻制印章的，由用印单位或部门提出申请，详细说明印章的名称、用途、式样和规格，报集团公司主要领导批准后由办公室制发。 | score=0.0610
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L21 | 第七条项目部印章在使用前，项目部应负责将集团公司办公室出具的印章启用文件报送建设单位、监理单位等相关方，以便业务往来确认。并在文件送达后一周内将回执返回集团公司办公室留存。 | score=0.0626
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L22 | 第八条印章使用过程中，如应变更或者因损坏需要重新刻制的，由使用单位或部门提出申请，经单位或部门负责人审批后，报集团公司办公室进行重新刻制。新印章需重新办理启用手续，原印章同时交回集团公司办公室。 | score=0.0527
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L23 | 第九条发生印章遗失，印章责任管理单位应在24小时内向集团公司和当地公安机关报告；在3个工作日内在省级以上报刊办理遗失声明，并向集团公司申请出具告知函，及时通知相关单位。印章遗失处理流程见附件。 | score=0.0572
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L24 | 印章责任管理单位应将印章遗失报告、遗失声明、告知函回复等相关资料在一月内报集团公司办公室，以备查考。 | score=0.0594
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0573
  - D2 | DISPATCH | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0573
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0571
  - D3 | DISPATCH | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0571
  - C9 | COLLECT | real_69c60971d4242eda8c47c605:L42 | （六）集团公司法人明确授权或者委托对外使用印章的事项。 | score=0.0571
  - C10 | COLLECT | real_69c60971d4242eda8c47c605:L49 | 第十二条 项目部印章使用范围 | score=0.0573
  - D4 | DISPATCH | real_69c60971d4242eda8c47c605:L49 | 第十二条 项目部印章使用范围 | score=0.0573
  - C11 | COLLECT | real_69c60971d4242eda8c47c605:L54 | （五）项目部与两级机关部门业务沟通的相关内部资料，如开复工备案、专项方案、整改回复等资料； | score=0.0520
  - C12 | COLLECT | real_69c60971d4242eda8c47c605:L56 | （七）项目印章应在项目负责人审批后用印，用印内容不得违背施工合同要件内容。 | score=0.0573
- projection_chars: 3503

**Step 3** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains the required Section 6 content covering sealing, suspension, and destruction points.
- legal_actions (45):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0626
  - D1 | DISPATCH | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0626
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L19 | 确因工作需要刻制印章的，由用印单位或部门提出申请，详细说明印章的名称、用途、式样和规格，报集团公司主要领导批准后由办公室制发。 | score=0.0610
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L21 | 第七条项目部印章在使用前，项目部应负责将集团公司办公室出具的印章启用文件报送建设单位、监理单位等相关方，以便业务往来确认。并在文件送达后一周内将回执返回集团公司办公室留存。 | score=0.0626
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L22 | 第八条印章使用过程中，如应变更或者因损坏需要重新刻制的，由使用单位或部门提出申请，经单位或部门负责人审批后，报集团公司办公室进行重新刻制。新印章需重新办理启用手续，原印章同时交回集团公司办公室。 | score=0.0527
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L23 | 第九条发生印章遗失，印章责任管理单位应在24小时内向集团公司和当地公安机关报告；在3个工作日内在省级以上报刊办理遗失声明，并向集团公司申请出具告知函，及时通知相关单位。印章遗失处理流程见附件。 | score=0.0572
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L24 | 印章责任管理单位应将印章遗失报告、遗失声明、告知函回复等相关资料在一月内报集团公司办公室，以备查考。 | score=0.0594
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0573
  - D2 | DISPATCH | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0573
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0571
  - D3 | DISPATCH | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0571
  - C9 | COLLECT | real_69c60971d4242eda8c47c605:L42 | （六）集团公司法人明确授权或者委托对外使用印章的事项。 | score=0.0571
  - C10 | COLLECT | real_69c60971d4242eda8c47c605:L49 | 第十二条 项目部印章使用范围 | score=0.0573
  - D4 | DISPATCH | real_69c60971d4242eda8c47c605:L49 | 第十二条 项目部印章使用范围 | score=0.0573
  - C11 | COLLECT | real_69c60971d4242eda8c47c605:L54 | （五）项目部与两级机关部门业务沟通的相关内部资料，如开复工备案、专项方案、整改回复等资料； | score=0.0520
  - C12 | COLLECT | real_69c60971d4242eda8c47c605:L56 | （七）项目印章应在项目负责人审批后用印，用印内容不得违背施工合同要件内容。 | score=0.0573
- projection_chars: 3531

### Evidence text (new)

```
[E1]
[§ 第六章 印章封口、停用与缴销]
  第三十二条项目部印章封口管理
  （一）在集团公司生产管理部发布的“封口闭合启动令”60日内上交集团公司办公室封存；项目印章回收后不得外借，期间如需要使用印章由原项目经理申请，责任管理单位批准后，在集团公司办公室登记用印。
  第三十三条发生机构名称变更、机构撤销等情况时，相关印章应在相关文件下发之日起停止使用，并在三个工作日内上交集团公司办公室。
  上缴的各类印章，应按要求办理缴销手续，留下印模。印章由集团公司办公室统一封存、销毁。
```

### Evidence text (old)

```
[E1]
第三十二条项目部印章封口管理

[E2]
（三）印章收回时，用印登记本一并收回。

[E3]
第三十三条发生机构名称变更、机构撤销等情况时，相关印章应在相关文件下发之日起停止使用，并在三个工作日内上交集团公司办公室。
```

## latest_clean_multi_0180 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“第一章 安全教育培训规定”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 479 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 12 | 12 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L5` [MISS] retrieved=False in_text=False
- `real_69c60974d4242eda8c47c615:L6` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60974d4242eda8c47c615:L3` scope=`None` depth=`0`
- reason: Collect Chapter 1 to retrieve content on safety education and training regulations.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L3']
- collect added=27 hits=27 branch_selected=True collect_full=True
- legal_actions (55):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0732
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0732
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L4 | 1.1 总则 | score=0.0636
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L4 | 1.1 总则 | score=0.0636
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L5 | 1.1.1安全教育和培训的类型应包括三级安全教育、岗前教育、日常教育、年度继续教育，以及各类特种作业人员证书的初审、复审培训（附表1.1.1：安全教育记录）。 | score=0.0636
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L6 | 1.1.2集团公司各级安全教育培训计划、安全教育培训工作按集团公司教育培训制度执行。 | score=0.0544
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0732
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0732
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L9 | 分包单位的作业人员三级安全教育，由其分包单位进行，项目部履行监督职责，并保存三级安全教育记录（附表1.2-3：分包单位作业人员三级安全教育记录表）。 | score=0.0519
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0732
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0732
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0732
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L12 | 2、项目部教育培训的主要内容：观看《生命之鉴》安全教育警示片，观看率达到100％；施工现场的环境、施工特点及可能存在的危害等；违章指挥、违章作业、违反劳动纪律产生的后果；预防、减少安全风险以及紧急情况下应急救援的基本措施； | score=0.0703
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L13 | 3、班组教育培训的主要内容：本班组作业特点和安全操作规程；如何正确使用劳动防护用品和安全防护装置；本岗位可能存在的危害及防范对策；本岗位的作业环境及使用的机械设备、工具的安全要求等。 | score=0.0691
  - C11 | COLLECT | real_69c60974d4242eda8c47c615:L14 | 1.2.3 三级安全教育的主控部门： | score=0.0592
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L14 | 1.2.3 三级安全教育的主控部门： | score=0.0592
- projection_chars: 3465

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Query asks for points from two adjacent evidence sections. G1 (§1.2.2) and G3 (§1.3) are adjacent in the hierarchy and cover key training content.
- legal_actions (60):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0496
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0496
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0496
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0496
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0496
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0442
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0442
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0442
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0542
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0542
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0507
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0507
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0507
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L142 | 4 按照严重未履职（或违章指挥）、一般未履职（或履职不到位）对事故发生负责的主要直接责任人分别处以项目负责人事故罚款60%、30%的罚款处理，对事故发生负责的主要间接责任人分别处以项目负责人事故罚款40%、20%的罚款，对事故发生负责的一般直接负责人或一般间接责任人分别处以20%、10%的罚款。情节严重时按照照集团公司《管理人员责任追究暂行规定》第八条处以组织措施。履职尽责相关人员免责。 | score=0.0440
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0542
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0542
- projection_chars: 3505

### Evidence text (new)

```
[E1]
[§ 1.2.2 三级安全教育的内容]
  1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析；
  2、项目部教育培训的主要内容：观看《生命之鉴》安全教育警示片，观看率达到100％；施工现场的环境、施工特点及可能存在的危害等；违章指挥、违章作业、违反劳动纪律产生的后果；预防、减少安全风险以及紧急情况下应急救援的基本措施；
  3、班组教育培训的主要内容：本班组作业特点和安全操作规程；如何正确使用劳动防护用品和安全防护装置；本岗位可能存在的危害及防范对策；本岗位的作业环境及使用的机械设备、工具的安全要求等。

[E2]
[§ 1.3岗前教育]
  新上岗作业人员，作业人员进入新的岗位或者新的施工现场前，离岗一年以上重新上岗时，采用新技术、新工艺、新设备、新材料时，项目部应对作业人员进行相应的岗前教育培训。
  岗前教育培训包括以下内容：
  1、安全生产法律法规和规章制度；
  2、安全操作规程；
  3、针对性的安全防范措施；
```

### Evidence text (old)

```
[E1]
[§ 第一章　安全教育培训规定 / 1.7 附则]
附表1：安全教育记录；

[E2]
第一章　安全教育培训规定
1.1 总则

[E3]
[§ 第一章　安全教育培训规定 / 1.3岗前教育]
2、安全操作规程；

[E4]
[§ 第一章　安全教育培训规定 / 1.7 附则]
附表1.2-1：项目管理人员三级安全教育记录表；

[E5]
[§ 第一章　安全教育培训规定 / 1.7 附则]
附表1.2-3：分包单位作业人员三级安全教育记录表。

[E6]
[§ 第一章　安全教育培训规定 / 1.7 附则]
附表1.2-2：项目操作人员三级安全教育记录表；

[E7]
[§ 第一章　安全教育培训规定 / 1.3岗前教育]
1、安全生产法律法规和规章制度；

[E8]
[§ 第一章　安全教育培训规定 / 1.4 日常安全教育：]
1.4.1作业人员进场施工每个月或者作业工种、作业环境发生改变，安全员组织施工员配合进行安全教育培训，其内容包括观看《生命之鉴》安全教育警示片、岗位安全教育、专项安全教育、日常教育等，施工员组织安全员参与做好针对性的安全技术交底，强化、规范作业人员作业行为
```

## latest_clean_multi_0202 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“第二章 安全检查及隐患排查规定”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 498 | 490 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 14 | 11 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L41` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L42` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60974d4242eda8c47c615:L39` scope=`None` depth=`0`
- reason: Collecting Chapter 2 to find the two adjacent evidence sections regarding safety inspection and hazard investigation.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L39']
- collect added=59 hits=59 branch_selected=True collect_full=True
- legal_actions (49):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0713
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0713
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0687
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0687
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0687
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L42 | 2.1.2 集团公司各级安全检查、隐患整改、回复销项、安全处罚均采用集团公司企业发展部的统一检查表格。 | score=0.0502
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0605
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0605
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0605
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0605
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L45 | 1、安全生产法律法规、标准规范和其他要求的执行情况； | score=0.0559
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L49 | 5、施工现场管理行为和实物状况（安全隐患排查、安全设施及安全防护等各项措施和落实情况）； | score=0.0605
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0578
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0578
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L61 | 6、其他应检查的内容。 | score=0.0578
  - C11 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0713
- projection_chars: 3552

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Assembled evidence covers Chapter 2 requirements. G2 (General Provisions) and G1 (Methods) provide the two adjacent sections requested.
- legal_actions (55):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L2 | 安全管理规定（2020版） | score=0.0406
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0484
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0484
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0484
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0484
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0484
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0484
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0484
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0494
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0494
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L127 | 3.3 事故调查 | score=0.0398
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L127 | 3.3 事故调查 | score=0.0398
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L128 | 发生一般及以上事故，依据《生产安全事故报告和调查处理条例》（中华人民共和国国务院令第493号），经县级以上有关部门组织事故调查组进行调查。 | score=0.0398
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0494
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0494
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0494
- projection_chars: 3318

### Evidence text (new)

```
[E1]
[§ 2.1总则]
  2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。
  2.1.2 集团公司各级安全检查、隐患整改、回复销项、安全处罚均采用集团公司企业发展部的统一检查表格。

[E2]
[§ 2.3安全检查及隐患排查的方法]
  2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。
  2.3.2集团公司安全检查及隐患排查的方式包括定期安全检查、专项安全检查、季节性安全检查、日常安全巡查、不定期抽查等。

[E3]
[§ 2.4.4 重大事故隐患整改、复查、销项]
  对重大事故隐患，由被检查项目负责整改，整改应制定事故隐患治理方案，该方案由项目经理组织制定和实施。方案包括以下内容：
  5、治理的时限和要求；
```

### Evidence text (old)

```
[E1]
[§ 2.3安全检查及隐患排查的方法]
2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。

[E2]
[§ 2.2  安全检查及隐患排查内容 / 2.2.2班组安全检查的内容：]
2、安全“三宝”的使用情况；

[E3]
[§ 2.2  安全检查及隐患排查内容 / 2.2.2班组安全检查的内容：]
1、安全技术交底、安全措施是否落实到施工作业中；

[E4]
[§ 2.2  安全检查及隐患排查内容 / 2.2.2班组安全检查的内容：]
6、其他应检查的内容。

[E5]
[§ 2.2  安全检查及隐患排查内容 / 2.2.1集团公司、二级单位、项目部安全检查的主要内容：]
1、安全生产法律法规、标准规范和其他要求的执行情况；

[E6]
[§ 2.4 隐患整改 / 2.4.4 重大事故隐患整改、复查、销项]
2、采取的方法和措施；

[E7]
[§ 2.3安全检查及隐患排查的方法 / 2.3.3 定期安全检查]
附表2-3-3《项目周检查标准化表格》
```

## latest_clean_multi_0223 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“2.3.4 专项安全检查”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 184 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 13 | 4 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L72` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L73` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C6` kind=`collect` section=`real_69c60974d4242eda8c47c615:L71` scope=`None` depth=`0`
- reason: Collect section 2.3.4 and its relevant leaf nodes C7 and C9 to answer the query about special safety inspections.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L71', 'real_69c60974d4242eda8c47c615:L72', 'real_69c60974d4242eda8c47c615:L74']
- collect added=3 hits=5 branch_selected=False collect_full=True
- legal_actions (55):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0682
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0682
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0558
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0558
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0558
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0682
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0682
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0682
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L71 | 2.3.4 专项安全检查 | score=0.0638
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L71 | 2.3.4 专项安全检查 | score=0.0638
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L72 | 定期检查中发现的倾向性问题，安全状况差的项目，集团公司及二级单位安排专项检查。 | score=0.0638
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L73 | 对于超过一定规模危险性较大的分部分项工程的施工，二级单位在施工期间必须至少安排一次专项安全检查。 | score=0.0581
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L74 | 对于危险性较大的分部分项工程的施工，施工现场临时用电，安全技术措施等，集团公司及二级单位安全监督管理部门应当在必要时安排专项安全检查。 | score=0.0625
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L77 | 2.3.6 日常安全检查 | score=0.0554
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L77 | 2.3.6 日常安全检查 | score=0.0554
  - C11 | COLLECT | real_69c60974d4242eda8c47c615:L79 | 2、项目经理和安全员要督促分包和设备租赁单位做好作业班组班前、班中和班后的安全岗位检查，发现问题及时整改； | score=0.0554
- projection_chars: 3392

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains the required section 2.3.4 content with two adjacent points regarding special safety inspections.
- legal_actions (57):
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0682
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0558
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0558
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0558
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0500
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0500
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0500
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0500
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L45 | 1、安全生产法律法规、标准规范和其他要求的执行情况； | score=0.0500
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0497
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0497
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L61 | 6、其他应检查的内容。 | score=0.0497
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0682
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0682
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L77 | 2.3.6 日常安全检查 | score=0.0554
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L77 | 2.3.6 日常安全检查 | score=0.0554
- projection_chars: 3375

### Evidence text (new)

```
[E1]
[§ 2.3.4 专项安全检查]
  定期检查中发现的倾向性问题，安全状况差的项目，集团公司及二级单位安排专项检查。
  对于超过一定规模危险性较大的分部分项工程的施工，二级单位在施工期间必须至少安排一次专项安全检查。
  对于危险性较大的分部分项工程的施工，施工现场临时用电，安全技术措施等，集团公司及二级单位安全监督管理部门应当在必要时安排专项安全检查。
```

### Evidence text (old)

```
[E1]
附件_安全管理规定（2020版）.docx

[E2]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.4 隐患整改 / 2.4.4 重大事故隐患整改、复查、销项]
3、经费和物资的落实；

[E3]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.2  安全检查及隐患排查内容 / 2.2.2班组安全检查的内容：]
3、施工工具、设备是否完好无损；

[E4]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.2  安全检查及隐患排查内容 / 2.2.1集团公司、二级单位、项目部安全检查的主要内容：]
7、专业工程、劳务、机械租赁等分包方管理情况；

[E5]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.4 隐患整改 / 2.4.4 重大事故隐患整改、复查、销项]
6、安全措施和应急预案。

[E6]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事
```

## latest_clean_multi_0226 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“2.3.5 季节性安全检查”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 482 | 160 |
| gold_node_recall | 0.0 | 0.5 |
| n_retrieved_nodes | 12 | 3 |
| trajectory_steps | n/a | 3 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L76` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L78` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C13` kind=`collect` section=`real_69c60974d4242eda8c47c615:L75` scope=`None` depth=`0`
- reason: Collect section 2.3.5 on seasonal safety inspections to answer the query.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L75']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (57):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0714
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0714
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0570
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0570
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0570
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0636
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0636
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0636
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0636
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L53 | 9、根据季节变化，防雷、防暑降温、防火、防台、防汛、防冻保温、防滑等措施的落实情况； | score=0.0636
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0714
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0714
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0666
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L64 | 2.3.2集团公司安全检查及隐患排查的方式包括定期安全检查、专项安全检查、季节性安全检查、日常安全巡查、不定期抽查等。 | score=0.0641
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L71 | 2.3.4 专项安全检查 | score=0.0550
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L71 | 2.3.4 专项安全检查 | score=0.0550
- projection_chars: 3468

**Step 2** `nav_collect`  id=`C12` kind=`collect` section=`real_69c60974d4242eda8c47c615:L64` scope=`None` depth=`0`
- reason: Collect section 2.3.2 to identify seasonal safety inspection as a method, needed for the query.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L64']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (60):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0512
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0512
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L26 | 1.4 日常安全教育： | score=0.0512
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L26 | 1.4 日常安全教育： | score=0.0512
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L28 | 1.4.2项目部依据项目实际情况组织雨季、暑期、冬季等季节性安全教育；节假日安全、消防安全等专项安全教育。 | score=0.0512
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0714
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0714
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0570
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0570
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0570
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0636
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0636
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0636
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0636
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L53 | 9、根据季节变化，防雷、防暑降温、防火、防台、防汛、防冻保温、防滑等措施的落实情况； | score=0.0636
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0714
- projection_chars: 3553

**Step 3** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence collected covers §2.3.5 seasonal inspection requirements and related methods as requested.
- legal_actions (59):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0512
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0512
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L26 | 1.4 日常安全教育： | score=0.0512
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L26 | 1.4 日常安全教育： | score=0.0512
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L28 | 1.4.2项目部依据项目实际情况组织雨季、暑期、冬季等季节性安全教育；节假日安全、消防安全等专项安全教育。 | score=0.0512
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0714
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0714
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0570
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0570
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0570
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0636
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0636
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0636
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0636
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L53 | 9、根据季节变化，防雷、防暑降温、防火、防台、防汛、防冻保温、防滑等措施的落实情况； | score=0.0636
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0714
- projection_chars: 3438

### Evidence text (new)

```
[E1]
[§ 2.3.5 季节性安全检查]
在冬、雨季及暑期来临前或施工期间，集团公司各级安全监督管理部门根据本单位的施工情况，应组织季节性检查。

[E2]
[§ 2.3安全检查及隐患排查的方法]
2.3.2集团公司安全检查及隐患排查的方式包括定期安全检查、专项安全检查、季节性安全检查、日常安全巡查、不定期抽查等。
```

### Evidence text (old)

```
[E1]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.2  安全检查及隐患排查内容 / 2.2.2班组安全检查的内容：]
3、施工工具、设备是否完好无损；

[E2]
附件_安全管理规定（2020版）.docx

[E3]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表6.6.1-1]
备注： 本表中所列工程，若本工程施工中有时在对应的辨识结论栏内打“√”，无时打“×”。

[E4]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.2  安全检查及隐患排查内容 / 2.2.2班组安全检查的内容：]
5、劳动保护用品配备是否齐全、使用是否规范；

[E5]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.2  安全检查及隐患排查内容 / 2.2.2班组安全检查的内容：]
1、安全技术交底、安全措施是否落实到施工作业中；
```

## latest_clean_multi_0227 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“2.3.6 日常安全检查”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 481 | 239 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 11 | 4 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L78` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L79` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C14` kind=`collect` section=`real_69c60974d4242eda8c47c615:L77` scope=`None` depth=`0`
- reason: Target section 2.3.6 Daily Safety Inspection found; collecting to extract required points.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L77']
- collect added=3 hits=3 branch_selected=True collect_full=True
- legal_actions (58):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0542
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0542
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0542
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0542
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0542
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0542
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0542
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0680
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0680
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0618
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0618
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0618
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0572
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0572
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0572
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0572
- projection_chars: 3482

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Assembled evidence G1 contains the required points for section 2.3.6 daily safety inspection.
- legal_actions (57):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0542
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0542
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0542
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0542
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0542
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0542
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0542
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0680
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0618
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0618
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0618
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0572
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0572
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0501
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0501
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L45 | 1、安全生产法律法规、标准规范和其他要求的执行情况； | score=0.0501
- projection_chars: 3469

### Evidence text (new)

```
[E1]
[§ 2.3.6 日常安全检查]
  1、项目施工管理人员应对施工区域内的安全措施落实情况和作业人员遵章守纪情况进行巡查，对发现的违章行为和事故隐患应及时纠正和整改；
  2、项目经理和安全员要督促分包和设备租赁单位做好作业班组班前、班中和班后的安全岗位检查，发现问题及时整改；
  3、项目专职安全员每日必须深入施工现场巡查，发现事故隐患应及时督促整改，并将检查情况及时报告项目负责人和上级安全监督管理部门，以便落实整改措施。附表2-3-6《安全员日巡查标准化表格》
```

### Evidence text (old)

```
[E1]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.2  安全检查及隐患排查内容 / 2.2.2班组安全检查的内容：]
3、施工工具、设备是否完好无损；

[E2]
附件_安全管理规定（2020版）.docx

[E3]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.2  安全检查及隐患排查内容 / 2.2.1集团公司、二级单位、项目部安全检查的主要内容：]
3、各项安全管理制度的执行情况，各级安全生产职责的履行情况，安全管理目标的实现程度；

[E4]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.4 隐患整改 / 2.4.4 重大事故隐患整改、复查、销项]
2、采取的方法和措施；

[E5]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.2  安全检查及隐患排查内容 / 2.2.2班组安全检查的内容：]
1、安全技术交底、安全措施是否落实到施工作业中；
```

## latest_clean_multi_0230 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“2.4 隐患整改”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 484 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 10 | 12 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L82` [MISS] retrieved=False in_text=False
- `real_69c60974d4242eda8c47c615:L83` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C11` kind=`collect` section=`real_69c60974d4242eda8c47c615:L81` scope=`None` depth=`0`
- reason: Collect section 2.4 Hazard Rectification to find the two adjacent evidence points requested.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L81']
- collect added=25 hits=25 branch_selected=True collect_full=True
- legal_actions (52):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0728
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0728
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0567
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0567
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0567
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0558
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0558
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0558
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0558
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L59 | 4、施工作业环境是否整洁安全，符合施工作业要求； | score=0.0558
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0610
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0610
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0602
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L77 | 2.3.6 日常安全检查 | score=0.0610
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L77 | 2.3.6 日常安全检查 | score=0.0610
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L79 | 2、项目经理和安全员要督促分包和设备租赁单位做好作业班组班前、班中和班后的安全岗位检查，发现问题及时整改； | score=0.0610
- projection_chars: 3541

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 and G2 cover general and major hazard rectification points as requested.
- legal_actions (54):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0486
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0486
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0486
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0486
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0486
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0486
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0486
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0728
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0567
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0567
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0567
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L42 | 2.1.2 集团公司各级安全检查、隐患整改、回复销项、安全处罚均采用集团公司企业发展部的统一检查表格。 | score=0.0500
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0558
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0558
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0558
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0558
- projection_chars: 3224

### Evidence text (new)

```
[E1]
[§ 2.4.4 重大事故隐患整改、复查、销项]
  隐患程度严重或整改难度大者，二级单位必须按带班检查制度指派二级单位负责人（总经理或生产、技术总工）监督整改。整改完成后在隐患整改回复单填写自检情况（须附证明材料），项目负责人复查验证，签字确认后上报二级单位，由二级单位复查确认后上报集团公司安全管理部。
  集团公司安全管理部依据整改情况决定验证，销项。
  2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。
  对重大事故隐患，由被检查项目负责整改，整改应制定事故隐患治理方案，该方案由项目经理组织制定和实施。方案包括以下内容：
  1、治理的目标和任务；
  2、采取的方法和措施；
  3、经费和物资的落实；
  4、负责治理的机构和人员；
  5、治理的时限和要求；
  6、安全措施和应急预案。
```

### Evidence text (old)

```
[E1]
[§ 2.4 隐患整改 / 2.4.4 重大事故隐患整改、复查、销项]
2、采取的方法和措施；

[E2]
[§ 2.4 隐患整改 / 2.4.7 隐患整改（控制或变更降低安全风险）措施的优先顺序：]
4、标志、警告和管理控制措施：安全标志、危险区域标识、警告器或警告灯、报警器、安全规程、设备检修、作业安全制度、操作牌和作业许可证等；

[E3]
[§ 2.4 隐患整改 / 2.4.4 重大事故隐患整改、复查、销项]
3、经费和物资的落实；

[E4]
[§ 2.4 隐患整改 / 2.4.4 重大事故隐患整改、复查、销项]
1、治理的目标和任务；

[E5]
[§ 2.4 隐患整改 / 2.4.7 隐患整改（控制或变更降低安全风险）措施的优先顺序：]
1、消除：改变施工方法或工艺以消除危险源；

[E6]
[§ 2.4 隐患整改 / 2.4.7 隐患整改（控制或变更降低安全风险）措施的优先顺序：]
5、个体防护装备：为操作者配备必要的个体防护装备；

[E7]
[§ 2.4 隐患整改 / 2.4.7 隐患整改（控制或变更降低安全风险）措施的优先顺序：]
2、替代：用低危害物质
```

## latest_clean_multi_0296 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“第五章 施工机械设备管理规定”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 460 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 8 | 12 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L179` [MISS] retrieved=False in_text=False
- `real_69c60974d4242eda8c47c615:L180` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C9` kind=`collect` section=`real_69c60974d4242eda8c47c615:L177` scope=`None` depth=`0`
- reason: Collecting specific leaf nodes under Chapter 5 regarding equipment management and safety signs.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L177', 'real_69c60974d4242eda8c47c615:L181', 'real_69c60974d4242eda8c47c615:L185']
- collect added=64 hits=66 branch_selected=False collect_full=True
- legal_actions (52):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0551
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0551
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0551
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0551
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0551
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0551
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0551
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0547
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0547
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0547
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0547
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0547
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0547
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L52 | 8、机械设备安全管理情况； | score=0.0547
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0734
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0734
- projection_chars: 3476

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Assembled evidence G4 (user unit duties) and G2 (install unit duties) directly address the two adjacent evidence points regarding construction machinery management responsibilities.
- legal_actions (57):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L2 | 安全管理规定（2020版） | score=0.0382
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0551
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0551
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0551
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0551
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0551
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0551
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0551
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L13 | 3、班组教育培训的主要内容：本班组作业特点和安全操作规程；如何正确使用劳动防护用品和安全防护装置；本岗位可能存在的危害及防范对策；本岗位的作业环境及使用的机械设备、工具的安全要求等。 | score=0.0439
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0547
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0547
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0547
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0547
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0547
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0547
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L52 | 8、机械设备安全管理情况； | score=0.0547
- projection_chars: 3598

### Evidence text (new)

```
[E1]
[§ 5.4.1 项目部（使用单位）应当履行下列职责：]
  1、报审安装单位编制的建筑机械设备安装、拆卸工程专项施工方案和安全事故应急救援预案并存档；
  2、向安装单位提供拟安装设备位置的基础施工资料；确保机械设备进场安装、拆卸所需的施工条件；
  4、制定机械设备使用安全事故应急救援预案；
  5、指定专职安全管理人员、机管员等相关人员监督检查机械设备安装、拆卸、使用情况，并做好记录；
  6、施工现场有多台塔式起重机作业时，制定并实施防止塔式起重机相互碰撞的安全措施；
  7、根据不同施工阶段、周围环境以及季节、气候的变化，及时督促出租单位采取相应的安全防护措施；
  8、在机械设备活动范围内设置明显的安全警示标志，对集中作业区做好安全防护；
  9、配合出租单位对机械设备及其安全保护装置进行经常性和定期检查，并做好记录；
  10、自机械设备安装验收合格之日起30日内按相关程序向工程所在地、县级以上地方人民政府建设主管部门办理建筑机械使用登记，登记标志置于或者附着于该机械设备的显著位置。
```

### Evidence text (old)

```
[E1]
第五章　施工机械设备管理规定
5.1 总则

[E2]
[§ 第五章　施工机械设备管理规定 / 5.4 职责 / 5.4.1 项目部（使用单位）应当履行下列职责：]
9、配合出租单位对机械设备及其安全保护装置进行经常性和定期检查，并做好记录；

[E3]
[§ 第五章　施工机械设备管理规定 / 5.4 职责 / 5.4.1 项目部（使用单位）应当履行下列职责：]
8、在机械设备活动范围内设置明显的安全警示标志，对集中作业区做好安全防护；

[E4]
[§ 第五章　施工机械设备管理规定 / 5.4 职责 / 5.4.1 项目部（使用单位）应当履行下列职责：]
2、向安装单位提供拟安装设备位置的基础施工资料；确保机械设备进场安装、拆卸所需的施工条件；

[E5]
[§ 第五章　施工机械设备管理规定 / 5.4 职责 / 5.4.1 项目部（使用单位）应当履行下列职责：]
5、指定专职安全管理人员、机管员等相关人员监督检查机械设备安装、拆卸、使用情况，并做好记录；

[E6]
[§ 第五章　施工机械设备管理规定 / 5.4 职责 / 5.4.1 项目部（使用单位）应当履行下列职责：
```

## latest_clean_multi_0303 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“5.2机械设备管理”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 485 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 7 | 9 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L187` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L188` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C12` kind=`collect` section=`real_69c60974d4242eda8c47c615:L186` scope=`None` depth=`0`
- reason: Collect section 5.2 Mechanical Equipment Management to find the two adjacent evidence points requested.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L186']
- collect added=18 hits=18 branch_selected=True collect_full=True
- legal_actions (52):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0620
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0620
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0620
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0620
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0620
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0620
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L52 | 8、机械设备安全管理情况； | score=0.0620
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0545
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0545
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0545
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0545
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0545
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0723
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0723
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0723
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0723
- projection_chars: 3512

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence collected covers section 5.2 Mechanical Equipment Management requirements and procedures.
- legal_actions (50):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0620
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0620
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0620
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0620
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0620
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0620
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L52 | 8、机械设备安全管理情况； | score=0.0620
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0545
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0545
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0545
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0545
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0545
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0723
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0723
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0723
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L181 | 5.1.3 项目部（使用单位）必须在机械租赁合同中明确约定：建筑机械的检查、维护、保养由机械出租方负责。 | score=0.0630
- projection_chars: 3397

### Evidence text (new)

```
[E1]
[§ 5.2机械设备管理]
  5.2.1 严禁自行购置的机械设备（如塔式超重机、施工升降机等）直接租赁给项目部或自行购置的机械设备以单位名义对外出租。
  未经单位授权签订的机械租赁合同属个人行为，责任人承担全部责任。
  5.2.2 严禁租赁集团公司《施工现场安全负面清单（2019版）》（见附表5.2-2）中禁止及限制使用的施工机械；租赁机械设备时，要求选择注册资金不小于200万元人民币的租赁单位，拟租起重机械机械使用年限应符合以下规定：
  1、塔式超重机：800KN·M以下(不含800KN·M)塔吊不超过5年；800-1250KN·M(不含1250KN·M)塔吊不超过7年；1250KN·M以上塔吊不超过10年；
  2、SC型施工升降机不超过5年；SC型物料提升机不超过5年；
  3、SS物料提升机不超过3年。

[E2]
[§ 5.2.5 租用机械设备管理程序：]
8、机械设备在使用过程中需要附着、顶升（加节），必须由原安装单位严格按照专项施工方案实施，并由使用单位组织出租单位、安装单位、监理单位等共同进行验收，验收合格后方可投入使用。
```

### Evidence text (old)

```
[E1]
[§ 5.2机械设备管理 / 5.2.5 租用机械设备管理程序：]
7、项目部编写使用过程应急预案和群塔作业防碰撞措施，到质监站办理使用登记。

[E2]
[§ 5.2机械设备管理 / 5.2.5 租用机械设备管理程序：]
8、机械设备在使用过程中需要附着、顶升（加节），必须由原安装单位严格按照专项施工方案实施，并由使用单位组织出租单位、安装单位、监理单位等共同进行验收，验收合格后方可投入使用。

[E3]
[§ 5.2机械设备管理 / 5.2.5 租用机械设备管理程序：]
2、签订机械租赁合同，机械安装、拆卸合同及安全协议书。

[E4]
[§ 5.2机械设备管理 / 附表5.2.2：《施工现场安全负面清单（2019版）》]
租赁、安装单位应提供加盖单位公章的营业执照、资质证书、安全生产许可证、施工机械租赁行业确认书、行业推荐证书等企业资质文件；以及拟租赁设备制造许可证、产品合格证、制造监督检验证明、备案登记、自检合格证明、安装使用说明书等产品证明文件。

[E5]
[§ 5.2机械设备管理 / 5.2.5 租用机械设备管理程序：]
5、机械设备安装完毕后进行安装单位自检合
```

## latest_clean_multi_0309 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“附表5.2.2：《施工现场安全负面清单（2019版）》”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 465 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 16 | 5 |
| trajectory_steps | n/a | 4 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L194` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L195` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C12` kind=`collect` section=`real_69c60974d4242eda8c47c615:L193` scope=`None` depth=`0`
- reason: The user query specifically targets '附表5.2.2' which is located under node C12.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L193']
- collect added=3 hits=3 branch_selected=True collect_full=True
- legal_actions (57):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0615
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0615
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0615
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0615
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0615
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0615
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L49 | 5、施工现场管理行为和实物状况（安全隐患排查、安全设施及安全防护等各项措施和落实情况）； | score=0.0615
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0601
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0601
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0601
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0691
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0691
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0628
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0628
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L185 | 根据工程特点及周围环境制定机械设备安全技术操作规程，设置安全警示标志；安全技术操作规程及警示标志应按照《施工现场标准化管理手册》要求制成标志牌悬挂在相应机械设备的醒目位置。 | score=0.0628
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0691
- projection_chars: 3481

**Step 2** `nav_collect`  id=`C33` kind=`collect` section=`real_69c60974d4242eda8c47c615:L497` scope=`None` depth=`0`
- reason: Collect the specific section containing the 'Negative List' details to answer the query.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L497']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (54):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0615
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0615
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0615
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0615
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0615
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0615
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L49 | 5、施工现场管理行为和实物状况（安全隐患排查、安全设施及安全防护等各项措施和落实情况）； | score=0.0615
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0601
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0601
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0601
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0691
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0628
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0628
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L185 | 根据工程特点及周围环境制定机械设备安全技术操作规程，设置安全警示标志；安全技术操作规程及警示标志应按照《施工现场标准化管理手册》要求制成标志牌悬挂在相应机械设备的醒目位置。 | score=0.0628
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0691
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L189 | 5.2.2 严禁租赁集团公司《施工现场安全负面清单（2019版）》（见附表5.2-2）中禁止及限制使用的施工机械；租赁机械设备时，要求选择注册资金不小于200万元人民币的租赁单位，拟租起重机械机械使用年限应符合以下规定： | score=0.0691
- projection_chars: 3407

**Step 3** `nav_collect`  id=`C9` kind=`collect` section=`real_69c60974d4242eda8c47c615:L189` scope=`None` depth=`0`
- reason: Collects the specific section referencing the 'Negative List' to answer the query about adjacent evidence points.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L189']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (52):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0615
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0615
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0615
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0615
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0615
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0615
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L49 | 5、施工现场管理行为和实物状况（安全隐患排查、安全设施及安全防护等各项措施和落实情况）； | score=0.0615
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0601
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0601
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0601
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0691
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0628
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0628
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L185 | 根据工程特点及周围环境制定机械设备安全技术操作规程，设置安全警示标志；安全技术操作规程及警示标志应按照《施工现场标准化管理手册》要求制成标志牌悬挂在相应机械设备的醒目位置。 | score=0.0628
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0691
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L189 | 5.2.2 严禁租赁集团公司《施工现场安全负面清单（2019版）》（见附表5.2-2）中禁止及限制使用的施工机械；租赁机械设备时，要求选择注册资金不小于200万元人民币的租赁单位，拟租起重机械机械使用年限应符合以下规定： | score=0.0691
- projection_chars: 3317

**Step 4** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Assembled evidence contains the required negative list content and related management points from sections G1, G2, and G3.
- legal_actions (56):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0615
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0615
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0615
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0615
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0615
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0615
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L49 | 5、施工现场管理行为和实物状况（安全隐患排查、安全设施及安全防护等各项措施和落实情况）； | score=0.0615
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0601
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0601
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0601
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0536
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0536
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0536
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0536
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0536
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0691
- projection_chars: 3494

### Evidence text (new)

```
[E1]
[§ 附表5.2.2：《施工现场安全负面清单（2019版）》]
  5.2.3 租赁机械设备必须签订租赁和安装、拆卸合同，合同应使用集团公司合同示范文本，同时签订安全协议书（集团公司示范文本，明确总包、使用、租赁、安拆各方的安全责任）。
  租赁、安装单位应提供加盖单位公章的营业执照、资质证书、安全生产许可证、施工机械租赁行业确认书、行业推荐证书等企业资质文件；以及拟租赁设备制造许可证、产品合格证、制造监督检验证明、备案登记、自检合格证明、安装使用说明书等产品证明文件。
  5.2.4 租赁施工升降机和800KN·m及以下的塔式起重机时，应选用租赁安装维修保养一体化的专业承包企业；对800KN·m以上的塔式起重机出租单位，当其不具备相应的起重设备安装工程专业承包资质的，项目经理部必须在签订租赁合同的同时，与出租、安装单位共同签订三方安全管理协议书，并与安装单位签订安拆合同，并明确各方的安全生产权利与义务。

[E2]
[§ 4.3.2 应急预案演练评价报]
5.2.2：《施工现场安全负面清单（2019版）》
```

### Evidence text (old)

```
[E1]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表6.6.1-1]
备注： 本表中所列工程，若本工程施工中有时在对应的辨识结论栏内打“√”，无时打“×”。

[E2]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表1.2-3]
工程名称

[E3]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表3.2]
单位名称：

[E4]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.3安全检查及隐患排查的方法 / 2.3.3 定期安全检查]
附表2-3-3《项目周检查标准化表格》

[E5]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表4.3.1]
注：应急预案演
```

## latest_clean_multi_0324 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“5.3.2 按陕建监总发[2014]04号文要求：”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 500 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 19 | 10 |
| trajectory_steps | n/a | 5 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L211` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L212` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60974d4242eda8c47c615:L262` scope=`real_69c60974d4242eda8c47c615:L262` depth=`1`
- reason: Collect Chapter 6 to locate section 5.3.2 and its referenced documents.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L262']
- collect added=64 hits=64 branch_selected=True collect_full=False
- legal_actions (17):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L262 | 第六章　项目安全管理规定 | score=0.0693
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L263 | 6.1 总则 | score=0.0434
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L269 | 6.1.5 项目开工前，项目部必须向当地政府建设主管部门办理安全备案手续和团体意外伤害保险（陕西省内强制购买建筑施工安全责任保险代替团体意外伤害保险）。 | score=0.0434
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L282 | 6.2 专职安全生产管理人员配备 | score=0.0491
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L283 | 6.2.1 根据建设部《建筑施工企业安全生产管理机构设置及专职安全生产管理人员配备办法》（建质[2008]91号）规定，项目部按照如下标准配备专职安全管理人员。 | score=0.0491
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L314 | 6.4 安全生产违章行为处罚 | score=0.0454
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L337 | 6.4.4 项目部管理人员或作业人员有下列行为之一的，按“违反安全相关规定”论处，责令改正，并处以罚款500～1000元罚款。 | score=0.0454
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L343 | 7、未按规定在施工现场危险部位设置明显的安全警示标志； | score=0.0417
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L354 | 6.5 分包方安全管理 | score=0.0429
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L357 | 6.5.2 项目部必须与分包单位签订《安全协议》（集团公司示范文本），明确各自的安全生产责任和义务。 | score=0.0429
  - C11 | COLLECT | real_69c60974d4242eda8c47c615:L362 | 6.6 危险性较大的分部分项工程管理 | score=0.0693
  - C12 | COLLECT | real_69c60974d4242eda8c47c615:L366 | 6.6.2 专项方案编制应当包括的内容，应当组织专家论证的相关内容，参见《危险性较大的分部分项工程安全管理规定》（建办质[2018]31号）执行。审核审批执行集团公司相关要求。 | score=0.0693
  - C13 | COLLECT | real_69c60974d4242eda8c47c615:L367 | 6.6.3 在施工过程中，项目部必须严格执行经批准的安全专项施工方案，不得擅自修改，现场专职安全生产管理人员现场监督实施，项目部指定专人按规定进行监测，若发现现场施工条件和施工环境发生较大改变时，应当立即停止施工，撤离作业人员，并将有关情况及时上报监理单位和方案的审批部门，在采取可靠措施后方可恢复施工。 | score=0.0457
  - C14 | COLLECT | real_69c60974d4242eda8c47c615:L383 | 6.9 安全设施、安全防护用品管理 | score=0.0677
  - C15 | COLLECT | real_69c60974d4242eda8c47c615:L389 | 办公、宿舍、库房等临时设施的消防、安全管理应符合《陕西建工集团施工现场临时建筑物安全管理暂行规定》（陕建总通[2013]143号）的要求。 | score=0.0677
  - C16 | COLLECT | real_69c60974d4242eda8c47c615:L400 | 6.11 安全标志 | score=0.0503
- projection_chars: 3577

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60974d4242eda8c47c615:L262` depth=`1`
- reason: Collected section L262 contains the required content to answer the query about adjacent evidence points.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 190

**Step 3** `nav_dispatch`  id=`D18` kind=`dispatch` section=`real_69c60974d4242eda8c47c615:L262` scope=`None` depth=`0`
- reason: Dispatch Chapter 6 to locate section 5.3.2 and adjacent evidence.
- dispatch_regions: ['real_69c60974d4242eda8c47c615:L262']
- child_reports=1 skipped=0
- legal_actions (57):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0556
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0556
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0556
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0556
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0556
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0556
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0556
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0620
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0620
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0568
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0568
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0568
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0620
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0620
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0620
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0585
- projection_chars: 3598

**Step 4** `nav_collect`  id=`C26` kind=`collect` section=`real_69c60974d4242eda8c47c615:L210` scope=`None` depth=`0`
- reason: Section C26 (5.3.2) contains the specific content regarding 'Shan Jian Jian Zong Fa [2014] No. 04' required by the query.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L210']
- collect added=3 hits=3 branch_selected=True collect_full=True
- legal_actions (56):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0556
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0556
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0556
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0556
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0556
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0556
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0556
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0620
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0620
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0568
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0568
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0568
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0620
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0620
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0620
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0585
- projection_chars: 3596

**Step 5** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Query specifically asks for points from section 5.3.2, which is fully contained in G3.
- legal_actions (54):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0556
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0556
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0556
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0556
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0556
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0556
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0556
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0620
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0620
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0568
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0568
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0568
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0620
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0620
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0620
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0585
- projection_chars: 3490

### Subagent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60974d4242eda8c47c615:L262 (ok)
collected 152 branch node(s); explicit roots=['real_69c60974d4242eda8c47c615:L262']
collected: real_69c60974d4242eda8c47c615:L262, real_69c60974d4242eda8c47c615:L263, real_69c60974d4242eda8c47c615:L264, real_69c60974d4242eda8c47c615:L265, real_69c60974d4242eda8c47c615:L266, real_69c60974d4242eda8c47c615:L267, real_69c60974d4242eda8c47c615:L268, real_69c60974d4242eda8c47c615:L269, real_69c60974d4242eda8c47c615:L270, real_69c60974d4242eda8c47c615:L271, real_69c60974d4242eda8c47c615:L272, real_69c60974d4242eda8c47c615:L273, real_69c60974d4242eda8c47c615:L274, real_69c60974d4242eda8c47c615:L275, real_69c60974d4242eda8c47c615:L276, real_69c60974d4242eda8c47c615:L277, real_69c60974d4242eda8c47c615:L278, real_69c60974d4242eda8c47c615:L279, real_69c60974d4242eda8c47c615:L280, real_69c60974d4242eda8c47c615:L281
reason: Collected section L262 contains the required content to answer the query about adjacent evidence points.
---
=== End Investigate ===
```

### Evidence text (new)

```
[E1]
[§ 5.3.2 按陕建监总发[2014]04号文要求：]
  自2015年1月1日起，附着式升降脚手架外立面、底板、脚手板必须使用具有防火功能的防护产品；
  吊篮的安/拆（包括二次移位）工作，均应由出租单位负责完成，使用单位不得安拆、转租吊篮；
  5.3.3 附着式升降脚手架、高空作业吊篮等工具式脚手架的专项方案由专业分包单位组织编制，方案应符合《建筑施工工具式脚手架安全技术规范》JGJ202-2010（以下简称JGJ202-2010）的相关规定。并经过分包单位具有法人资格企业的技术负责人批准。再按照专项方案审批程序履行审批手续。

[E2]
[§ 6.6 危险性较大的分部分项工程管理]
  危险性较大的分部分项工程识别清单（见附表6.6.1-1）；超过一定规模的危险性较大的分部分项工程识别清单（见附表6.6.1-2）。
  6.6.2 专项方案编制应当包括的内容，应当组织专家论证的相关内容，参见《危险性较大的分部分项工程安全管理规定》（建办质[2018]31号）执行。审核审批执行集团公司相关要求。

[E3]
[§ 6.5 分包方安全管理]
3、分包单位安全生产绩效。
```

### Evidence text (old)

```
[E1]
[§ 附件_安全管理规定（2020版）.docx]
陕西建工第十一建设集团有限公司

[E2]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.4 隐患整改 / 2.4.4 重大事故隐患整改、复查、销项]
3、经费和物资的落实；

[E3]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表3.2]
单位名称：

[E4]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.3安全检查及隐患排查的方法 / 2.3.3 定期安全检查]
附表2-3-3《项目周检查标准化表格》

[E5]
[§ 附件_安全管理规定（2020版）.docx / 第六章　项目安全管理规定 / 6.11 安全标志]
附表6.7.3：安全技术交底记录。

[E6]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.2  安全检查及隐患排查内容 / 2.2.1集团公司、二级单位、项目部安
```

## latest_clean_multi_0362 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“5.4.3 项目部监督安装单位履行下列职责：”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 490 | 445 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 9 | 9 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L250` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L251` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C19` kind=`collect` section=`real_69c60974d4242eda8c47c615:L249` scope=`None` depth=`0`
- reason: Collect section 5.4.3 and its three leaf points regarding installation unit duties as requested.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L249', 'real_69c60974d4242eda8c47c615:L251', 'real_69c60974d4242eda8c47c615:L256', 'real_69c60974d4242eda8c47c615:L257']
- collect added=8 hits=11 branch_selected=False collect_full=True
- legal_actions (53):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0563
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0563
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0563
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0563
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L9 | 分包单位的作业人员三级安全教育，由其分包单位进行，项目部履行监督职责，并保存三级安全教育记录（附表1.2-3：分包单位作业人员三级安全教育记录表）。 | score=0.0563
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0565
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0565
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0565
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0565
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0554
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L142 | 4 按照严重未履职（或违章指挥）、一般未履职（或履职不到位）对事故发生负责的主要直接责任人分别处以项目负责人事故罚款60%、30%的罚款处理，对事故发生负责的主要间接责任人分别处以项目负责人事故罚款40%、20%的罚款，对事故发生负责的一般直接负责人或一般间接责任人分别处以20%、10%的罚款。情节严重时按照照集团公司《管理人员责任追究暂行规定》第八条处以组织措施。履职尽责相关人员免责。 | score=0.0565
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0699
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0699
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0548
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0548
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L193 | 附表5.2.2：《施工现场安全负面清单（2019版）》 | score=0.0548
- projection_chars: 3583

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains all required points from section 5.4.3 regarding installation unit duties.
- legal_actions (53):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0563
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0563
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0563
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0563
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L9 | 分包单位的作业人员三级安全教育，由其分包单位进行，项目部履行监督职责，并保存三级安全教育记录（附表1.2-3：分包单位作业人员三级安全教育记录表）。 | score=0.0563
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0565
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0565
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0565
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0565
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0554
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L142 | 4 按照严重未履职（或违章指挥）、一般未履职（或履职不到位）对事故发生负责的主要直接责任人分别处以项目负责人事故罚款60%、30%的罚款处理，对事故发生负责的主要间接责任人分别处以项目负责人事故罚款40%、20%的罚款，对事故发生负责的一般直接负责人或一般间接责任人分别处以20%、10%的罚款。情节严重时按照照集团公司《管理人员责任追究暂行规定》第八条处以组织措施。履职尽责相关人员免责。 | score=0.0565
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0699
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0548
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0548
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L193 | 附表5.2.2：《施工现场安全负面清单（2019版）》 | score=0.0548
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L193 | 附表5.2.2：《施工现场安全负面清单（2019版）》 | score=0.0548
- projection_chars: 3525

### Evidence text (new)

```
[E1]
[§ 5.4.3 项目部监督安装单位履行下列职责：]
  1、编制机械设备安装、拆卸专项施工方案，并由安装单位技术负责人审核、审批；
  2、按照安全技术标准、安装使用说明书等检查机械设备是否符合安全技术标准，查看现场是否具备安装、拆卸施工条件；
  3、组织进行安全技术交底并签字确认；
  4、制定机械设备安装、拆卸工程安全事故应急救援预案，并经本单位相关技术人员审核审批；
  5、机械设备在安装拆卸前应当将机械安装、拆卸工程专项方案，安装拆卸人员名单，机械安装单位的有关资质，安装拆卸时间等材料报施工总承包单位进行审查；
  6、严格按照专项方案及安全操作规程组织安装、拆卸作业，严禁违章作业，冒险作业；
  7、安装单位的专业技术人员、专职安全生产管理人员应当进行现场监督，技术负责人应当现场指导安装、拆卸作业；
  8、机械设备安装完毕后，安装单位应当按照安全技术标准及安装使用说明书等有关要求对所安装的机械设备进行自检、调试和试运转，自检合格的应当出具自检合格证明。
```

### Evidence text (old)

```
[E1]
[§ 第五章　施工机械设备管理规定 / 5.4 职责 / 5.4.1 项目部（使用单位）应当履行下列职责：]
1、报审安装单位编制的建筑机械设备安装、拆卸工程专项施工方案和安全事故应急救援预案并存档；

[E2]
[§ 第五章　施工机械设备管理规定 / 5.4 职责 / 5.4.1 项目部（使用单位）应当履行下列职责：]
7、根据不同施工阶段、周围环境以及季节、气候的变化，及时督促出租单位采取相应的安全防护措施；

[E3]
[§ 第五章　施工机械设备管理规定 / 5.4 职责 / 5.4.1 项目部（使用单位）应当履行下列职责：]
8、在机械设备活动范围内设置明显的安全警示标志，对集中作业区做好安全防护；

[E4]
[§ 第五章　施工机械设备管理规定 / 5.4 职责 / 5.4.2 项目部监督出租单位履行下列职责：]
1、出租的机械设备必须是安全技术档案齐全且安全技术标准达标的合格产品；

[E5]
[§ 第五章　施工机械设备管理规定 / 5.4 职责 / 5.4.1 项目部（使用单位）应当履行下列职责：]
4、制定机械设备使用安全事故应急救援预案；
```

## latest_clean_multi_0415 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“6.4 安全生产违章行为处罚”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 490 |
| gold_node_recall | 0.0 | 0.5 |
| n_retrieved_nodes | 10 | 13 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L315` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L316` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C18` kind=`collect` section=`real_69c60974d4242eda8c47c615:L314` scope=`None` depth=`0`
- reason: Collect section 6.4 to identify two adjacent evidence points regarding safety violation penalties.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L314', 'real_69c60974d4242eda8c47c615:L315', 'real_69c60974d4242eda8c47c615:L319', 'real_69c60974d4242eda8c47c615:L320', 'real_69c60974d4242eda8c47c615:L324', 'real_69c60974d4242eda8c47c615:L328', 'real_69c60974d4242eda8c47c615:L329', 'real_69c60974d4242eda8c47c615:L337', 'real_69c60974d4242eda8c47c615:L339', 'real_69c60974d4242eda8c47c615:L343', 'real_69c60974d4242eda8c47c615:L345', 'real_69c60974d4242eda8c47c615:L346', 'real_69c60974d4242eda8c47c615:L347', 'real_69c60974d4242eda8c47c615:L348', 'real_69c60974d4242eda8c47c615:L349']
- collect added=39 hits=53 branch_selected=False collect_full=True
- legal_actions (46):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0534
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0534
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0534
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0534
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0534
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0534
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0534
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L12 | 2、项目部教育培训的主要内容：观看《生命之鉴》安全教育警示片，观看率达到100％；施工现场的环境、施工特点及可能存在的危害等；违章指挥、违章作业、违反劳动纪律产生的后果；预防、减少安全风险以及紧急情况下应急救援的基本措施； | score=0.0471
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0520
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0520
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0520
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0520
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0520
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0503
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0503
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0503
- projection_chars: 3533

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 fully covers section 6.4 penalties for violations, addressing the user's query.
- legal_actions (48):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0534
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0534
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0534
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0534
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0534
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0534
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0534
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L12 | 2、项目部教育培训的主要内容：观看《生命之鉴》安全教育警示片，观看率达到100％；施工现场的环境、施工特点及可能存在的危害等；违章指挥、违章作业、违反劳动纪律产生的后果；预防、减少安全风险以及紧急情况下应急救援的基本措施； | score=0.0471
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L18 | 1.3岗前教育 | score=0.0436
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L18 | 1.3岗前教育 | score=0.0436
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L24 | 4、违章指挥、违章作业、违反劳动纪律产生的后果； | score=0.0436
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0520
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0520
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0520
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0520
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0520
- projection_chars: 3263

### Evidence text (new)

```
[E1]
[§ 6.4 安全生产违章行为处罚]
  6.4.1 项目部管理人员或作业队伍班组长有下列行为之一的，按“违章指挥”论处，责令整改，并处以罚款500～1000元罚款。
  4、其他违章指挥行为。
  6.4.2 项目部管理人员或作业人员有下列行为之一的，按“违章作业”论处，责令立即停止作业，并处以罚款50～500元罚款。
  8、其他违章作业行为。
  6.4.3 项目部管理人员或作业人员有下列行为之一的，按“违反劳动纪律“论处，责令改正，并处以罚款100～500元罚款。
  6.4.4 项目部管理人员或作业人员有下列行为之一的，按“违反安全相关规定”论处，责令改正，并处以罚款500～1000元罚款。
  2、安全生产责任未分解到人的；
  7、未按规定在施工现场危险部位设置明显的安全警示标志；
  10、其他违反安全规范的现象或行为。
  6.4.5 集团公司在检查中发现项目的违章行为，对二级单位和项目部同时进行处罚；
  二级单位在检查中发现项目的违章行为，对项目部进行处罚；
  项目部在检查中发现的违章行为，对项目管理人员或作业班组（人员）进行处罚。
```

### Evidence text (old)

```
[E1]
[§ 6.4 安全生产违章行为处罚]
二级单位在检查中发现项目的违章行为，对项目部进行处罚；

[E2]
[§ 6.4 安全生产违章行为处罚]
10、其他违反安全规范的现象或行为。

[E3]
[§ 6.4 安全生产违章行为处罚]
2、被地市级建设行政部门通报，媒体曝光，罚款人民币20000元；

[E4]
[§ 6.4 安全生产违章行为处罚]
6.4.5 集团公司在检查中发现项目的违章行为，对二级单位和项目部同时进行处罚；

[E5]
[§ 6.4 安全生产违章行为处罚]
1、被县级建设行政部门（或同级别的其它行政部门，下同）通报，媒体曝光，罚款人民币10000元；

[E6]
[§ 6.4 安全生产违章行为处罚]
7、未按规定在施工现场危险部位设置明显的安全警示标志；

[E7]
[§ 6.4 安全生产违章行为处罚]
4、其他违章指挥行为。

[E8]
[§ 6.4 安全生产违章行为处罚]
2、擅自离岗，玩忽职守；

[E9]
[§ 6.4 安全生产违章行为处罚]
6.4.4 项目部管理人员或作业人员有下列行为之一的，按“违反安全相关规定”论处，责令改正，并处以罚款500
```

## latest_clean_multi_0462 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“6.8 危险源监控管理”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 473 |
| gold_node_recall | 0.0 | 0.5 |
| n_retrieved_nodes | 14 | 7 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L376` [MISS] retrieved=False in_text=False
- `real_69c60974d4242eda8c47c615:L377` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C24` kind=`collect` section=`real_69c60974d4242eda8c47c615:L375` scope=`None` depth=`0`
- reason: Collect section 6.8 and all its subsections to extract points on hazard source monitoring management.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L375', 'real_69c60974d4242eda8c47c615:L376', 'real_69c60974d4242eda8c47c615:L377', 'real_69c60974d4242eda8c47c615:L378', 'real_69c60974d4242eda8c47c615:L379', 'real_69c60974d4242eda8c47c615:L380', 'real_69c60974d4242eda8c47c615:L381', 'real_69c60974d4242eda8c47c615:L382']
- collect added=7 hits=14 branch_selected=False collect_full=True
- legal_actions (51):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0496
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0496
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0496
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0496
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0496
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0496
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0496
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0619
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0619
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0619
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0619
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0619
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0619
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0619
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L104 | 2.4.7 隐患整改（控制或变更降低安全风险）措施的优先顺序： | score=0.0518
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L104 | 2.4.7 隐患整改（控制或变更降低安全风险）措施的优先顺序： | score=0.0518
- projection_chars: 3547

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains all required points from section 6.8 regarding hazard monitoring management.
- legal_actions (52):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0496
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0496
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0496
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0496
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0496
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0496
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0496
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L12 | 2、项目部教育培训的主要内容：观看《生命之鉴》安全教育警示片，观看率达到100％；施工现场的环境、施工特点及可能存在的危害等；违章指挥、违章作业、违反劳动纪律产生的后果；预防、减少安全风险以及紧急情况下应急救援的基本措施； | score=0.0449
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0619
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0619
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0476
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0476
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0476
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0491
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0491
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0491
- projection_chars: 3453

### Evidence text (new)

```
[E1]
[§ 6.8 危险源监控管理]
  6.8.2 危险源辨识应根据施工作业活动、施工作业流程和施工工艺，采用科学合理的辨识方法，辨识方法见《危险源辨识、风险评价与控制程序》，项目部对管辖区域和施工现场可能存在的危险源进行分析辨识，列出危险源清单。
  6.8.3 对已辨识出来的危险源采用定性和定量评价，分析导致事故发生的可能性和事故后果，确定风险等级及重大危险源，列出重大危险源清单。
  6.8.4 根据重大危险源清单，制定管理方案，明确重大危险源的目标、指标、控制措施，并落实相关部门及专人负责监督、管理。
  6.8.5 加强对重大危险源的巡查和监控，采取相应的预防及控制措施，消除或降低其影响，使其达到可接受的程度，保证集团公司职业健康安全管理目标的实现。
  6.8.6 项目部应在工地醒目位置设立“不可接受风险公示牌”（见集团公司《施工现场标准化管理手册》），公示牌应注明危险源、存在部位、作业时间、防护措施和责任人等内容。
  6.8.7二级单位、项目部应随所管区域变化和工程施工的进度及时进行更新对危险源辨识和风险评价。
```

### Evidence text (old)

```
[E1]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表1.1.1]
编号：

[E2]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表1.1.1]
安全教育记录

[E3]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表6.7.3]
安全技术交底记录

[E4]
附件_安全管理规定（2020版）.docx

[E5]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.2  安全检查及隐患排查内容 / 2.2.2班组安全检查的内容：]
6、其他应检查的内容。

[E6]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表6.6.1-1]
备注： 本表中所列工程，若本工程
```

## latest_clean_multi_0469 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“6.9 安全设施、安全防护用品管理”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 492 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 15 | 6 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L384` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L385` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C24` kind=`collect` section=`real_69c60974d4242eda8c47c615:L383` scope=`None` depth=`0`
- reason: Collect section 6.9 and its two relevant leaf nodes C25 and C26 to answer the query about safety facilities management.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L383', 'real_69c60974d4242eda8c47c615:L384', 'real_69c60974d4242eda8c47c615:L385']
- collect added=6 hits=8 branch_selected=False collect_full=True
- legal_actions (50):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0664
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0664
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0664
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0664
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0664
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0664
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L13 | 3、班组教育培训的主要内容：本班组作业特点和安全操作规程；如何正确使用劳动防护用品和安全防护装置；本岗位可能存在的危害及防范对策；本岗位的作业环境及使用的机械设备、工具的安全要求等。 | score=0.0664
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0654
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0654
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0654
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0654
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0654
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0654
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0654
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0665
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0665
- projection_chars: 3422

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains all required points from section 6.9 regarding safety facilities and PPE management.
- legal_actions (59):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0664
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0664
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0664
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0664
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0664
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0664
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L13 | 3、班组教育培训的主要内容：本班组作业特点和安全操作规程；如何正确使用劳动防护用品和安全防护装置；本岗位可能存在的危害及防范对策；本岗位的作业环境及使用的机械设备、工具的安全要求等。 | score=0.0664
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0654
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0654
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0654
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0654
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0654
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0654
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0654
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0665
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0665
- projection_chars: 3504

### Evidence text (new)

```
[E1]
[§ 6.9 安全设施、安全防护用品管理]
  6.9.1 项目部材料组负责安全设施、安全防护用品的采购、进场验收、保管、发放、更新、报废等的管理；项目部专职安全管理人员负责劳动防护用品使用过程的指导、监督和管理。
  6.9.2 实行分包的项目，对分包单位安全设施、劳动防护用品的提供，分包合同应明确约定；项目部负责对分包企业自行劳动防护用品的采购、使用等负责监督指导。
  6.9.3 项目部在采购安全设施、安全防护用品时，必须采购具有生产许可证和产品检验合格证的合格供方供应的产品。发放前材料组应组织项目质检员、安全员等共同验收，确认合格后方可发放使用。安全员负责收集生产许可证、产品合格证、准用证，检测合格证明等资料。
  6.9.4 生产组/施工员在安排操作人员上岗时，应检查安全设施、安全防护用品的使用情况，并指导正确使用。对未按规定使用安全设施、安全防护用品的人员及时纠正，对拒不改正的有权不予安排工作或停止其作业。
  办公、宿舍、库房等临时设施的消防、安全管理应符合《陕西建工集团施工现场临时建筑物安全管理暂行规定》（陕建总通[2013]143号）的要求。
```

### Evidence text (old)

```
[E1]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表3.2]
单位名称：

[E2]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.2  安全检查及隐患排查内容 / 2.2.2班组安全检查的内容：]
5、劳动保护用品配备是否齐全、使用是否规范；

[E3]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表6.6.1-1]
备注： 本表中所列工程，若本工程施工中有时在对应的辨识结论栏内打“√”，无时打“×”。

[E4]
附件_安全管理规定（2020版）.docx

[E5]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.4 隐患整改 / 2.4.4 重大事故隐患整改、复查、销项]
2、采取的方法和措施；

[E6]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 
```

## latest_clean_multi_0475 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“6.10 施工机具管理”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 489 |
| gold_node_recall | 0.0 | 0.5 |
| n_retrieved_nodes | 10 | 7 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L391` [MISS] retrieved=False in_text=False
- `real_69c60974d4242eda8c47c615:L392` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C24` kind=`collect` section=`real_69c60974d4242eda8c47c615:L390` scope=`None` depth=`0`
- reason: Target section 6.10 contains relevant points on construction tool management.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L390']
- collect added=9 hits=9 branch_selected=True collect_full=True
- legal_actions (47):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0697
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0697
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0685
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0685
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L181 | 5.1.3 项目部（使用单位）必须在机械租赁合同中明确约定：建筑机械的检查、维护、保养由机械出租方负责。 | score=0.0517
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L185 | 根据工程特点及周围环境制定机械设备安全技术操作规程，设置安全警示标志；安全技术操作规程及警示标志应按照《施工现场标准化管理手册》要求制成标志牌悬挂在相应机械设备的醒目位置。 | score=0.0685
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0594
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0594
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L193 | 附表5.2.2：《施工现场安全负面清单（2019版）》 | score=0.0594
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L193 | 附表5.2.2：《施工现场安全负面清单（2019版）》 | score=0.0594
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L195 | 租赁、安装单位应提供加盖单位公章的营业执照、资质证书、安全生产许可证、施工机械租赁行业确认书、行业推荐证书等企业资质文件；以及拟租赁设备制造许可证、产品合格证、制造监督检验证明、备案登记、自检合格证明、安装使用说明书等产品证明文件。 | score=0.0594
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L207 | 5.3 工具式脚手架管理 | score=0.0664
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L207 | 5.3 工具式脚手架管理 | score=0.0664
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L214 | 5.3.4 附着式升降脚手架、高空作业吊篮等管理程序： | score=0.0664
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L214 | 5.3.4 附着式升降脚手架、高空作业吊篮等管理程序： | score=0.0664
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L227 | 5.3.5 分包单位做好工具式脚手架自检及出具自检合格证明，向项目部（使用单位）进行安全使用说明，办理验收手续并签字确认。 | score=0.0664
- projection_chars: 3477

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains all required points from section 6.10 regarding construction tool management.
- legal_actions (54):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0502
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0502
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0502
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0502
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0502
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0502
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0502
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0495
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0495
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0495
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0495
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0495
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0697
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0697
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0685
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0685
- projection_chars: 3553

### Evidence text (new)

```
[E1]
[§ 6.10 施工机具管理]
  6.10.2 项目部材料动力组负责施工机具的日常检查及定期检查工作。检查依据：《建筑施工安全检查标准JGJ59-2011》，《建筑机械使用安全技术规程JGJ33-2012》，《施工现场机械设备检查技术规程JGJ160-2008》。
  6.10.3 项目部材料动力组负责施工机具的安装调试，施工机具安装完毕后由项目部组织按规定履行验收程序验收（总包方、分包方、租赁方、安装方、监理方），并应经责任人签字确认。
  6.10.4 项目部自有或租赁的施工机具，负有使用、维护、保养管理工作的义务。但劳务分包，专业分包或租赁的施工机具，合同及安全管理协议书必须明确使用、维护、保养管理工作的责任方。
  6.10.5 施工机具的各种检测仪表及安全装置必须齐全有效，严禁使用安全装置不齐全有效、超过使用年限或技术性能落后耗能高、效率低的施工机具。
  6.10.6 施工机具的现场工作环境必须符合要求，禁止在不适宜的工作环境下使用施工机具。
  6.10.9 施工机具出现故障或异常情况时应立即停机，待故障排除后方可使用，严禁机械带病运转。
```

### Evidence text (old)

```
[E1]
[§ 第五章　施工机械设备管理规定 / 5.4 职责 / 5.4.1 项目部（使用单位）应当履行下列职责：]
9、配合出租单位对机械设备及其安全保护装置进行经常性和定期检查，并做好记录；

[E2]
[§ 第五章　施工机械设备管理规定 / 5.4 职责 / 5.4.1 项目部（使用单位）应当履行下列职责：]
2、向安装单位提供拟安装设备位置的基础施工资料；确保机械设备进场安装、拆卸所需的施工条件；

[E3]
[§ 第五章　施工机械设备管理规定 / 5.4 职责 / 5.4.1 项目部（使用单位）应当履行下列职责：]
6、施工现场有多台塔式起重机作业时，制定并实施防止塔式起重机相互碰撞的安全措施；

[E4]
[§ 第五章　施工机械设备管理规定 / 5.4 职责 / 5.4.1 项目部（使用单位）应当履行下列职责：]
7、根据不同施工阶段、周围环境以及季节、气候的变化，及时督促出租单位采取相应的安全防护措施；

[E5]
[§ 第五章　施工机械设备管理规定 / 5.2机械设备管理 / 5.2.5 租用机械设备管理程序：]
7、项目部编写使用过程应急预案和群塔作业防碰撞措施，到
```

## latest_clean_multi_0484 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“6.11 安全标志”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 490 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 15 | 11 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L401` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L402` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C29` kind=`collect` section=`real_69c60974d4242eda8c47c615:L400` scope=`None` depth=`0`
- reason: Collect section 6.11 and its subsections to extract points on safety signs as requested.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L400', 'real_69c60974d4242eda8c47c615:L401', 'real_69c60974d4242eda8c47c615:L402']
- collect added=13 hits=15 branch_selected=False collect_full=True
- legal_actions (58):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0606
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0606
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0606
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0606
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0606
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0606
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0606
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0631
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0631
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0631
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0631
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0631
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0625
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0625
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0625
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0625
- projection_chars: 3524

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains section 6.11 Safety Signs with all required points for the query.
- legal_actions (58):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0606
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0606
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0606
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0606
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0606
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0606
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0606
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0631
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0631
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0631
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0631
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0631
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0625
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0625
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0625
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0625
- projection_chars: 3487

### Evidence text (new)

```
[E1]
[§ 6.11 安全标志]
  6.11.1 项目部应在施工现场入口处、施工机械、临时用电设施、脚手架、出入通道口、楼梯口、电梯井口、孔洞口、基坑边沿、爆破物及有害危险气体和液体存放处、易燃物料存放处等危险部位和产生粉尘或可能产生职业灼伤的作业场所，设置明显的警示标志，绘制安全标志平面布置图。
  6.11.2 标志牌的设置要求：
  3、标志牌应设在醒目、明亮与安全有关处，并使人们看到后有足够的时间来注意它所表示的内容；
  4、标志牌不应设在门、窗、架等可移动的物体上；
  5、设置在有触电危险场所的标志牌，应使用绝缘材料制作；
  6、在较大场所，必须设置多个标志牌，不同类型的标志牌同时设置时，应按警告、禁止、指令、提示的顺序，从左到右，从上到下排列；
  7、自行制作的标志牌必须满足集团公司VIS视觉识别系统的文件要求。
  6.11.3 施工现场的安全标志牌应每月检查一次，如发现有变形、破损或图形符号脱落以及变色时，应及时修整或更换。
  附表6.6.1-2：超过一定规模的危险性较大的分部分项工程识别清单；
  附表6.7.3：安全技术交底记录。
```

### Evidence text (old)

```
[E1]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表6.6.1-1]
备注： 本表中所列工程，若本工程施工中有时在对应的辨识结论栏内打“√”，无时打“×”。

[E2]
附件_安全管理规定（2020版）.docx

[E3]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.2  安全检查及隐患排查内容 / 2.2.2班组安全检查的内容：]
6、其他应检查的内容。

[E4]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表1.1.1]
编号：

[E5]
[§ 附件_安全管理规定（2020版）.docx / 第六章　项目安全管理规定 / 6.11 安全标志]
4、标志牌不应设在门、窗、架等可移动的物体上；

[E6]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 
```

## latest_clean_multi_0502 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“7.2 总平面布局”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 390 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 11 | 5 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L424` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L425` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C31` kind=`collect` section=`real_69c60974d4242eda8c47c615:L423` scope=`None` depth=`0`
- reason: Collect section 7.2 Total Layout and its two leaf nodes to answer the query about adjacent evidence points.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L423', 'real_69c60974d4242eda8c47c615:L424', 'real_69c60974d4242eda8c47c615:L426']
- collect added=4 hits=6 branch_selected=False collect_full=True
- legal_actions (56):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0556
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0556
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0556
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0556
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0556
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0556
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0556
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0582
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0582
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0573
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0573
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0573
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0580
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0580
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0580
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0582
- projection_chars: 3603

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains all required points from section 7.2 regarding total layout.
- legal_actions (52):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0556
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0556
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0556
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0556
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0556
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0556
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0556
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0582
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0582
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0573
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0573
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0573
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0580
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0580
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0580
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0582
- projection_chars: 3250

### Evidence text (new)

```
[E1]
[§ 7.2 总平面布局]
  7.2.1 施工现场出入口的设置必须满足消防车通行的要求，并应布置在不同方向，其数量不宜少于2个。当确有困难只能设置1个出入口时，在施工现场内设置满足消防车通行的环形道路，消防车道的净宽度和净空高度均不应小于4米。
  7.2.2 宿舍、厨房操作间、配电室、可燃材料堆场及其加工场、可燃材料及易燃易爆危险品库房等临时用房、临时设施不能设置于在建工程内。
  7.2.3 固定动火作业场要布置在可燃材料堆场及其加工场、易燃易爆危险品库房等全年最小频率风向的上风侧，并宜布置在临时办公用房、宿舍、可燃材料库房、在建工程等全年最小频率风向的上风侧。
  7.2.4 易燃易爆危险品库房与在建工程的防火间距不小于15m，可燃材料堆场及其加工场、固定动火作业场与在建工程的防火间距不小于10m，其它临时用房、临时设施与在建工程的防火间距不小于6m。
```

### Evidence text (old)

```
[E1]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.8 其他防火管理]
7.8.2 临时消防车道、临时疏散通道、安全出口必须保持畅通，不得遮挡、挪动疏散指示标识，不得挪用消防设施。

[E2]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.7 用火、用电、用气管理 / 7.7.2 施工现场用电管理]
2、电气设备与可燃、易燃易爆和腐蚀性物品保持一定的安全距离；

[E3]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.5 防火管理一般规定]
7.5.6 施工单位(项目部)必须做好并保存施工现场消防安全管理的相关文件和记录，建立现场消防安全管理档案。

[E4]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.1 总  则]
7.1.6 定期对施工的各类人员进行消防安全教育，提高防火灭火技能。定期进行防火安全大检查，消除火险隐患。

[E5]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.7 用火、用电、用气管理 / 7.7.2 施工现场用电管理]
4、配电箱内每个电气回路必须设置漏电保护器、过载保护器，距配电箱2m范围内不能堆放可燃物，5m范围内不能设置
```

## latest_clean_multi_0518 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“7.6 可燃物及易燃易爆危险品管理”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 496 | 182 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 10 | 2 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L444` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L445` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C26` kind=`collect` section=`real_69c60974d4242eda8c47c615:L444` scope=`None` depth=`0`
- reason: Collecting sections 7.6.1 and 7.6.2 which directly address the user's query about combustible materials management.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L444', 'real_69c60974d4242eda8c47c615:L445']
- collect added=2 hits=2 branch_selected=True collect_full=True
- legal_actions (48):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0588
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0588
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0588
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0588
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0588
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0588
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0588
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L262 | 第六章　项目安全管理规定 | score=0.0679
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L262 | 第六章　项目安全管理规定 | score=0.0679
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L314 | 6.4 安全生产违章行为处罚 | score=0.0605
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L314 | 6.4 安全生产违章行为处罚 | score=0.0605
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L342 | 5、易燃易爆品未单独设置仓库的；或未按有关规定在施工现场设置消防通道、配备消防设施和灭火器材的； | score=0.0605
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L362 | 6.6 危险性较大的分部分项工程管理 | score=0.0657
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L362 | 6.6 危险性较大的分部分项工程管理 | score=0.0657
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L366 | 6.6.2 专项方案编制应当包括的内容，应当组织专家论证的相关内容，参见《危险性较大的分部分项工程安全管理规定》（建办质[2018]31号）执行。审核审批执行集团公司相关要求。 | score=0.0657
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L375 | 6.8 危险源监控管理 | score=0.0646
- projection_chars: 3563

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains the two adjacent points (7.6.1 and 7.6.2) from section 7.6 as requested.
- legal_actions (52):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0588
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0588
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0588
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0588
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0588
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0588
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0588
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0525
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0525
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0525
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0525
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0525
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L262 | 第六章　项目安全管理规定 | score=0.0679
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L262 | 第六章　项目安全管理规定 | score=0.0679
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L314 | 6.4 安全生产违章行为处罚 | score=0.0605
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L314 | 6.4 安全生产违章行为处罚 | score=0.0605
- projection_chars: 3643

### Evidence text (new)

```
[E1]
[§ 7.6 可燃物及易燃易爆危险品管理]
  7.6.1 用于在建工程的保温、防水、装饰使用的油漆及防腐等可燃物及易燃易爆危险品材料应按规定单独设库存放。
  7.6.2 在施工现场使用油漆及其有机溶剂、乙二胺、冷底子油或其他可燃、易燃易爆危险品的作业时，必须保持良好通风，作业场所严禁明火，并必须避免产生静电，同时设置专人、配备灭火器材进行现场监护。
```

### Evidence text (old)

```
[E1]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.7 用火、用电、用气管理 / 7.7.2 施工现场用电管理]
4、配电箱内每个电气回路必须设置漏电保护器、过载保护器，距配电箱2m范围内不能堆放可燃物，5m范围内不能设置可能产生较多易燃、易爆气体、粉尘的作业区；

[E2]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.7 用火、用电、用气管理 / 7.7.3 施工现场用气管理]
（2）气瓶的钢印和颜色标记清晰，确保瓶帽和防震圈的完好，禁止粘有油脂。

[E3]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.5 防火管理一般规定]
7.5.6 施工单位(项目部)必须做好并保存施工现场消防安全管理的相关文件和记录，建立现场消防安全管理档案。

[E4]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.7 用火、用电、用气管理 / 7.7.1 施工现场用火管理]
2、施工现场在进行焊接、切割、烘烤或加热等动火作业前，必须对作业现场的可燃物进行清理；对于作业现场及其附近无法移走的可燃物，必须采用不燃材料对其覆盖或隔离；裸露的可燃材料上严禁直接进行动火作业；
```

## latest_clean_multi_0521 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“7.7.1 施工现场用火管理”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 356 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 10 | 7 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L449` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L450` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C31` kind=`collect` section=`real_69c60974d4242eda8c47c615:L448` scope=`None` depth=`0`
- reason: Collect section 7.7.1 and its leaf nodes to extract key points on fire management as requested.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L448', 'real_69c60974d4242eda8c47c615:L449', 'real_69c60974d4242eda8c47c615:L450']
- collect added=6 hits=8 branch_selected=False collect_full=True
- legal_actions (50):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0601
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0601
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0601
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0601
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L185 | 根据工程特点及周围环境制定机械设备安全技术操作规程，设置安全警示标志；安全技术操作规程及警示标志应按照《施工现场标准化管理手册》要求制成标志牌悬挂在相应机械设备的醒目位置。 | score=0.0601
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0519
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0519
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L193 | 附表5.2.2：《施工现场安全负面清单（2019版）》 | score=0.0519
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L193 | 附表5.2.2：《施工现场安全负面清单（2019版）》 | score=0.0519
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L195 | 租赁、安装单位应提供加盖单位公章的营业执照、资质证书、安全生产许可证、施工机械租赁行业确认书、行业推荐证书等企业资质文件；以及拟租赁设备制造许可证、产品合格证、制造监督检验证明、备案登记、自检合格证明、安装使用说明书等产品证明文件。 | score=0.0519
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L233 | 5.4 职责 | score=0.0592
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L233 | 5.4 职责 | score=0.0592
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L234 | 5.4.1 项目部（使用单位）应当履行下列职责： | score=0.0592
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L234 | 5.4.1 项目部（使用单位）应当履行下列职责： | score=0.0592
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L241 | 7、根据不同施工阶段、周围环境以及季节、气候的变化，及时督促出租单位采取相应的安全防护措施； | score=0.0592
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L262 | 第六章　项目安全管理规定 | score=0.0580
- projection_chars: 3487

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains all required points for section 7.7.1 regarding fire management.
- legal_actions (48):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0601
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0601
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0601
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0601
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L185 | 根据工程特点及周围环境制定机械设备安全技术操作规程，设置安全警示标志；安全技术操作规程及警示标志应按照《施工现场标准化管理手册》要求制成标志牌悬挂在相应机械设备的醒目位置。 | score=0.0601
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0519
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0519
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L193 | 附表5.2.2：《施工现场安全负面清单（2019版）》 | score=0.0519
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L193 | 附表5.2.2：《施工现场安全负面清单（2019版）》 | score=0.0519
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L195 | 租赁、安装单位应提供加盖单位公章的营业执照、资质证书、安全生产许可证、施工机械租赁行业确认书、行业推荐证书等企业资质文件；以及拟租赁设备制造许可证、产品合格证、制造监督检验证明、备案登记、自检合格证明、安装使用说明书等产品证明文件。 | score=0.0519
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L233 | 5.4 职责 | score=0.0592
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L233 | 5.4 职责 | score=0.0592
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L234 | 5.4.1 项目部（使用单位）应当履行下列职责： | score=0.0592
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L234 | 5.4.1 项目部（使用单位）应当履行下列职责： | score=0.0592
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L241 | 7、根据不同施工阶段、周围环境以及季节、气候的变化，及时督促出租单位采取相应的安全防护措施； | score=0.0592
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L262 | 第六章　项目安全管理规定 | score=0.0580
- projection_chars: 3431

### Evidence text (new)

```
[E1]
[§ 7.7.1 施工现场用火管理]
  1、施工现场动火作业必须办理动火许可证；动火操作人员必须具有相应资格；
  2、施工现场在进行焊接、切割、烘烤或加热等动火作业前，必须对作业现场的可燃物进行清理；对于作业现场及其附近无法移走的可燃物，必须采用不燃材料对其覆盖或隔离；裸露的可燃材料上严禁直接进行动火作业；
  3、焊接、切割、烘烤或加热等动火作业，必须配备灭火器材，并设动火监护人进行现场一对一监护；
  4、五级（含五级）以上风力时，必须停止焊接、切割等室外动火作业，否则必须采取可靠的挡风措施；
  5、动火作业后，必须对现场进行检查，确认无火灾危险后，动火操作人员方可离开；
  6、施工现场不应采用明火取暖；厨房操作间炉灶使用完毕后，必须将炉火熄灭，排油烟机及油烟管道必须定期清理油垢。
```

### Evidence text (old)

```
[E1]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.7 用火、用电、用气管理 / 7.7.2 施工现场用电管理]
2、电气设备与可燃、易燃易爆和腐蚀性物品保持一定的安全距离；

[E2]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.1 总  则]
7.1.6 定期对施工的各类人员进行消防安全教育，提高防火灭火技能。定期进行防火安全大检查，消除火险隐患。

[E3]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.1 总  则]
7.1.1 本规定适用于集团公司所有在建项目工程施工现场的消防安全管理。

[E4]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.5 防火管理一般规定]
7.5.6 施工单位(项目部)必须做好并保存施工现场消防安全管理的相关文件和记录，建立现场消防安全管理档案。

[E5]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.5 防火管理一般规定]
7.5.1 施工现场的消防安全管理由责任单位统一管理，项目部具体负责落实。

[E6]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.7 用火、用电、用气管理 / 7.7.1 施工
```

## latest_clean_multi_0527 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“7.7.2 施工现场用电管理”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 414 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 8 | 7 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L456` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L457` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C32` kind=`collect` section=`real_69c60974d4242eda8c47c615:L455` scope=`None` depth=`0`
- reason: Target section 7.7.2 contains the required points on construction site electricity management.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L455']
- collect added=6 hits=6 branch_selected=True collect_full=True
- legal_actions (53):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0631
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0631
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0622
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0622
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L185 | 根据工程特点及周围环境制定机械设备安全技术操作规程，设置安全警示标志；安全技术操作规程及警示标志应按照《施工现场标准化管理手册》要求制成标志牌悬挂在相应机械设备的醒目位置。 | score=0.0622
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0584
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0584
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L193 | 附表5.2.2：《施工现场安全负面清单（2019版）》 | score=0.0584
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L193 | 附表5.2.2：《施工现场安全负面清单（2019版）》 | score=0.0584
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L195 | 租赁、安装单位应提供加盖单位公章的营业执照、资质证书、安全生产许可证、施工机械租赁行业确认书、行业推荐证书等企业资质文件；以及拟租赁设备制造许可证、产品合格证、制造监督检验证明、备案登记、自检合格证明、安装使用说明书等产品证明文件。 | score=0.0584
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L233 | 5.4 职责 | score=0.0631
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L233 | 5.4 职责 | score=0.0631
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L234 | 5.4.1 项目部（使用单位）应当履行下列职责： | score=0.0631
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L234 | 5.4.1 项目部（使用单位）应当履行下列职责： | score=0.0631
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L241 | 7、根据不同施工阶段、周围环境以及季节、气候的变化，及时督促出租单位采取相应的安全防护措施； | score=0.0631
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L249 | 5.4.3 项目部监督安装单位履行下列职责： | score=0.0536
- projection_chars: 3498

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains all required points from section 7.7.2 regarding construction site electricity management.
- legal_actions (53):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0631
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0631
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0622
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0622
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L185 | 根据工程特点及周围环境制定机械设备安全技术操作规程，设置安全警示标志；安全技术操作规程及警示标志应按照《施工现场标准化管理手册》要求制成标志牌悬挂在相应机械设备的醒目位置。 | score=0.0622
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0584
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0584
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L193 | 附表5.2.2：《施工现场安全负面清单（2019版）》 | score=0.0584
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L193 | 附表5.2.2：《施工现场安全负面清单（2019版）》 | score=0.0584
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L195 | 租赁、安装单位应提供加盖单位公章的营业执照、资质证书、安全生产许可证、施工机械租赁行业确认书、行业推荐证书等企业资质文件；以及拟租赁设备制造许可证、产品合格证、制造监督检验证明、备案登记、自检合格证明、安装使用说明书等产品证明文件。 | score=0.0584
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L207 | 5.3 工具式脚手架管理 | score=0.0517
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L207 | 5.3 工具式脚手架管理 | score=0.0517
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L214 | 5.3.4 附着式升降脚手架、高空作业吊篮等管理程序： | score=0.0517
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L214 | 5.3.4 附着式升降脚手架、高空作业吊篮等管理程序： | score=0.0517
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L227 | 5.3.5 分包单位做好工具式脚手架自检及出具自检合格证明，向项目部（使用单位）进行安全使用说明，办理验收手续并签字确认。 | score=0.0517
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L233 | 5.4 职责 | score=0.0631
- projection_chars: 3458

### Evidence text (new)

```
[E1]
[§ 7.7.2 施工现场用电管理]
  1、电气线路必须具有相应的绝缘强度和机械强度，破损、烧焦的插座、插头应及时更换；
  2、电气设备与可燃、易燃易爆和腐蚀性物品保持一定的安全距离；
  3、有爆炸和火灾危险的场所，按危险等级选用相应的电气设备，电气设备不能超负荷运行或带故障使用；
  4、配电箱内每个电气回路必须设置漏电保护器、过载保护器，距配电箱2m范围内不能堆放可燃物，5m范围内不能设置可能产生较多易燃、易爆气体、粉尘的作业区；
  5、可燃材料库房不能使用高热灯具，易燃易爆危险品库房内必须使用防爆灯具，普通灯具与易燃物距离不小于300mm，聚光灯、碘钨灯等高热灯具与易燃物距离不宜小于500mm；
  6、施工现场办公、生活区和施工区禁止私自改装现场供用电设施，严禁在宿舍使用不合格的电褥子、大功率热水器等电器。项目部必须定期对办公、生活区和施工区安全用电、电气设备和线路的运行及维护情况进行检查。
```

### Evidence text (old)

```
[E1]
[§ 第七章　施工现场消防安全管理暂行规定]
为了加强集团公司在建项目施工现场消防管理，保障施工现场生活区、办公区和施工区施工人员生命安全和财产安全。依据《中华人民共和国消防法》、《建设工程施工现场消防安全技术规范》（GB50720—2011）及其他有关消防法规，结合施工现场实际，特制定《集团公司施工现场消防安全管理暂行规定》。

[E2]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.7 用火、用电、用气管理 / 7.7.1 施工现场用火管理]
5、动火作业后，必须对现场进行检查，确认无火灾危险后，动火操作人员方可离开；

[E3]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.7 用火、用电、用气管理 / 7.7.1 施工现场用火管理]
3、焊接、切割、烘烤或加热等动火作业，必须配备灭火器材，并设动火监护人进行现场一对一监护；

[E4]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.5 防火管理一般规定]
7.5.1 施工现场的消防安全管理由责任单位统一管理，项目部具体负责落实。

[E5]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.7 用火
```

## latest_clean_multi_0544 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“7.8 其他防火管理”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 195 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 12 | 5 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L478` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L479` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C36` kind=`collect` section=`real_69c60974d4242eda8c47c615:L477` scope=`None` depth=`0`
- reason: Collect section 7.8 'Other Fire Management' to find the two adjacent evidence points requested.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L477']
- collect added=4 hits=4 branch_selected=True collect_full=True
- legal_actions (58):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0614
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0614
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0555
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0555
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0555
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0555
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L45 | 1、安全生产法律法规、标准规范和其他要求的执行情况； | score=0.0555
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L53 | 9、根据季节变化，防雷、防暑降温、防火、防台、防汛、防冻保温、防滑等措施的落实情况； | score=0.0548
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0540
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0540
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L61 | 6、其他应检查的内容。 | score=0.0540
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0614
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0614
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0614
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0614
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0614
- projection_chars: 3524

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains all required points from section 7.8 for the query.
- legal_actions (55):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0614
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0614
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0555
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0555
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0555
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0555
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L45 | 1、安全生产法律法规、标准规范和其他要求的执行情况； | score=0.0555
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L53 | 9、根据季节变化，防雷、防暑降温、防火、防台、防汛、防冻保温、防滑等措施的落实情况； | score=0.0548
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0540
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0540
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L61 | 6、其他应检查的内容。 | score=0.0540
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0614
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0614
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0614
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0614
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0614
- projection_chars: 3371

### Evidence text (new)

```
[E1]
[§ 7.8 其他防火管理]
  7.8.1 施工单位(项目部)必须做好施工现场临时消防设施的日常维护工作，对已失效、损坏或丢失的消防设施，必须及时更换、修复或补充。
  7.8.2 临时消防车道、临时疏散通道、安全出口必须保持畅通，不得遮挡、挪动疏散指示标识，不得挪用消防设施。
  7.8.3 施工期间，不能拆除临时消防设施及临时疏散设施。
  7.8.4 施工现场严禁吸烟。
```

### Evidence text (old)

```
[E1]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.1 总  则]
7.1.6 定期对施工的各类人员进行消防安全教育，提高防火灭火技能。定期进行防火安全大检查，消除火险隐患。

[E2]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.5 防火管理一般规定]
7.5.6 施工单位(项目部)必须做好并保存施工现场消防安全管理的相关文件和记录，建立现场消防安全管理档案。

[E3]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.7 用火、用电、用气管理 / 7.7.3 施工现场用气管理]
2、二保焊用二氧化碳气瓶

[E4]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.5 防火管理一般规定]
7.5.1 施工现场的消防安全管理由责任单位统一管理，项目部具体负责落实。

[E5]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.7 用火、用电、用气管理 / 7.7.2 施工现场用电管理]
2、电气设备与可燃、易燃易爆和腐蚀性物品保持一定的安全距离；

[E6]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.3 建筑防火]
7.3.3 作业场所要设置明显的
```

## latest_clean_multi_0552 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“3.2 生产安全事故快报”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 500 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 11 | 19 |
| trajectory_steps | n/a | 4 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L493` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L494` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C33` kind=`collect` section=`real_69c60974d4242eda8c47c615:L492` scope=`None` depth=`0`
- reason: Section 3.2 contains the required content on production safety accident rapid reports.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L492']
- collect added=51 hits=51 branch_selected=True collect_full=True
- legal_actions (55):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0617
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0617
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0617
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0617
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0617
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0617
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0617
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0640
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0640
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0527
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0527
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0527
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0640
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0640
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0640
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0640
- projection_chars: 3429

**Step 2** `nav_collect`  id=`C14` kind=`collect` section=`real_69c60974d4242eda8c47c615:L116` scope=`None` depth=`0`
- reason: Collect section 3.2 to find the two adjacent evidence points regarding accident reporting.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L116']
- collect added=10 hits=10 branch_selected=True collect_full=True
- legal_actions (50):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0617
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0617
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0617
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0617
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0617
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0617
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0617
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0640
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0640
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0527
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0527
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0527
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0640
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0640
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0640
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0640
- projection_chars: 3581

**Step 3** `nav_collect`  id=`C27` kind=`collect` section=`real_69c60974d4242eda8c47c615:L147` scope=`None` depth=`0`
- reason: Collect section C27 (Appendix 3.2) to obtain the specific content of the 'Production Safety Accident Quick Report' form required by the query.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L147']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (48):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0617
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0617
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0617
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0617
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0617
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0617
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0617
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0640
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0640
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0527
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0527
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0527
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0640
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0640
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0640
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0640
- projection_chars: 3490

**Step 4** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: G2 contains §3.2 content on accident reporting requirements, and G9 contains the specific 'Production Safety Accident Quick Report' form details.
- legal_actions (48):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0617
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0617
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0617
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0617
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0617
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0617
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0617
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0640
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0640
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0527
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0527
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0527
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0640
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0640
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0640
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0640
- projection_chars: 3615

### Evidence text (new)

```
[E1]
[§ 3.2 事故报告]
  事故发生后，事故现场负责人应当立即向集团公司负责人报告；集团公司负责人接到报告后，按照《生产安全事故报告和调查处理条例》的规定，在1小时内向事故发生地安全生产监督管理局、建设主管部门、陕建集团总公司等部门逐级报告。
  在报告的同时，应当及时编制《生产安全事故快报表》（见附表3.2）报陕建集团总公司安全监管部门。
  生产安全事故报告的内容应包括：
  1 事故的时间、地点和工程项目有关单位名称；
  2 事故的简要经过；
  3 事故已经造成或者可能造成的伤亡人数（包括下落不明的人数）和初步估计的直接经济损失；
  4 事故的初步原因；
  5 事故发生后采取的措施及事故控制情况；
  6 事故报告单位或报告人员；
  生产安全事故报告后出现新情况的，应及时补报。

[E2]
[§ 3.2 生产安全事故快报]
  3.7-1 职工伤亡事故月（年）报表
  3.7-3 安全生产信息季（年）度报表
  4.3.1 应急预案演练方案

[E3]
[§ 3.5 分析改进]
附表3.2：生产安全事故快报；

[E4]
[§ 附表3.2]
生产安全事故快报
```

### Evidence text (old)

```
[E1]
[§ 3.2 事故报告]
在报告的同时，应当及时编制《生产安全事故快报表》（见附表3.2）报陕建集团总公司安全监管部门。

[E2]
[§ 3.2 事故报告]
生产安全事故报告后出现新情况的，应及时补报。

[E3]
[§ 3.2 事故报告]
2 事故的简要经过；

[E4]
[§ 3.2 事故报告]
1 事故的时间、地点和工程项目有关单位名称；

[E5]
[§ 3.2 事故报告]
5 事故发生后采取的措施及事故控制情况；

[E6]
[§ 3.2 事故报告]
生产安全事故报告的内容应包括：

[E7]
[§ 3.2 事故报告]
4 事故的初步原因；

[E8]
[§ 3.2 事故报告]
事故发生后，事故现场负责人应当立即向集团公司负责人报告；集团公司负责人接到报告后，按照《生产安全事故报告和调查处理条例》的规定，在1小时内向事故发生地安全生产监督管理局、建设主管部门、陕建集团总公司等部门逐级报告。

[E9]
[§ 3.2 事故报告]
6 事故报告单位或报告人员；

[E10]
[§ 3.2 事故报告]
3 事故已经造成或者可能造成的伤亡人数（包括下落不明的人数）和初步估
```

## latest_clean_multi_0554 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“4.3.2 应急预案演练评价报”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 228 | 461 |
| gold_node_recall | 0.0 | 0.5 |
| n_retrieved_nodes | 2 | 11 |
| trajectory_steps | n/a | 7 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L497` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L500` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C15` kind=`collect` section=`real_69c60974d4242eda8c47c615:L167` scope=`None` depth=`0`
- reason: Collect section 4.3.2 content and its associated appendix form to answer the query about evaluation report points.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L167', 'real_69c60974d4242eda8c47c615:L176']
- collect added=2 hits=2 branch_selected=True collect_full=True
- legal_actions (57):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0564
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0564
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0564
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0564
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0564
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0564
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L103 | 2.4.6 各项目部应当加强对自然灾害的预防。对于因自然灾害可能导致事故灾难的隐患，应当按照有关法律、法规、标准和本制度的要求排查治理，采取可靠的预防措施，制定应急预案。在接到有关自然灾害预报时，应当及时向有关人员发出预警通知；发生自然灾害可能危及施工和人员安全的情况时，应当采取撤离人员、停止作业、加强监测等安全措施，并及时向当地人民政府有关部门报告。 | score=0.0564
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0558
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0558
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0558
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0558
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0558
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L151 | 第四章　安全生产事故应急救援管理规定 | score=0.0732
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L151 | 第四章　安全生产事故应急救援管理规定 | score=0.0732
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L152 | 4.1 组织机构与职责 | score=0.0578
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L152 | 4.1 组织机构与职责 | score=0.0578
- projection_chars: 3365

**Step 2** `nav_collect`  id=`C30` kind=`collect` section=`real_69c60974d4242eda8c47c615:L496` scope=`None` depth=`0`
- reason: Collect section 4.3.2 to obtain the specific content of the emergency plan drill evaluation report.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L496']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (59):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0564
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0564
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0540
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0540
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0540
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0564
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0564
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0564
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0564
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L103 | 2.4.6 各项目部应当加强对自然灾害的预防。对于因自然灾害可能导致事故灾难的隐患，应当按照有关法律、法规、标准和本制度的要求排查治理，采取可靠的预防措施，制定应急预案。在接到有关自然灾害预报时，应当及时向有关人员发出预警通知；发生自然灾害可能危及施工和人员安全的情况时，应当采取撤离人员、停止作业、加强监测等安全措施，并及时向当地人民政府有关部门报告。 | score=0.0564
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0558
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0558
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0558
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0558
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0558
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L151 | 第四章　安全生产事故应急救援管理规定 | score=0.0732
- projection_chars: 3359

**Step 3** `nav_collect`  id=`C37` kind=`collect` section=`real_69c60974d4242eda8c47c615:L542` scope=`None` depth=`0`
- reason: Collect section C37 (4.3.2 Evaluation Report) to answer the query about adjacent evidence points.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L542']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (58):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0564
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0564
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0540
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0540
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0540
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0564
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0564
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0564
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0564
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0532
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L103 | 2.4.6 各项目部应当加强对自然灾害的预防。对于因自然灾害可能导致事故灾难的隐患，应当按照有关法律、法规、标准和本制度的要求排查治理，采取可靠的预防措施，制定应急预案。在接到有关自然灾害预报时，应当及时向有关人员发出预警通知；发生自然灾害可能危及施工和人员安全的情况时，应当采取撤离人员、停止作业、加强监测等安全措施，并及时向当地人民政府有关部门报告。 | score=0.0564
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0558
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0558
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0558
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0558
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0558
- projection_chars: 3535

**Step 4** `nav_collect`  id=`C17` kind=`collect` section=`real_69c60974d4242eda8c47c615:L165` scope=`None` depth=`0`
- reason: Collect section 4.3 to access the full content of 4.3.2 and adjacent sections for comparison.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L165']
- collect added=3 hits=3 branch_selected=True collect_full=True
- legal_actions (57):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0564
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0564
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0540
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0540
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0540
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0564
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0564
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0564
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0564
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0532
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L103 | 2.4.6 各项目部应当加强对自然灾害的预防。对于因自然灾害可能导致事故灾难的隐患，应当按照有关法律、法规、标准和本制度的要求排查治理，采取可靠的预防措施，制定应急预案。在接到有关自然灾害预报时，应当及时向有关人员发出预警通知；发生自然灾害可能危及施工和人员安全的情况时，应当采取撤离人员、停止作业、加强监测等安全措施，并及时向当地人民政府有关部门报告。 | score=0.0564
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0558
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0558
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0558
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0558
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0558
- projection_chars: 3465

**Step 5** `nav_collect`  id=`C33` kind=`collect` section=`real_69c60974d4242eda8c47c615:L541` scope=`None` depth=`0`
- reason: Collect section D19 (4.3.2) to retrieve the specific content of the emergency plan drill evaluation report.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L541']
- collect added=2 hits=2 branch_selected=True collect_full=True
- legal_actions (53):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0564
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0564
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0540
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0540
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0540
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0564
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0564
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0564
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0564
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0532
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L103 | 2.4.6 各项目部应当加强对自然灾害的预防。对于因自然灾害可能导致事故灾难的隐患，应当按照有关法律、法规、标准和本制度的要求排查治理，采取可靠的预防措施，制定应急预案。在接到有关自然灾害预报时，应当及时向有关人员发出预警通知；发生自然灾害可能危及施工和人员安全的情况时，应当采取撤离人员、停止作业、加强监测等安全措施，并及时向当地人民政府有关部门报告。 | score=0.0564
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0558
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0558
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0558
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0558
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0558
- projection_chars: 3255

**Step 6** `nav_collect`  id=`C26` kind=`collect` section=`real_69c60974d4242eda8c47c615:L495` scope=`None` depth=`0`
- reason: Collect section 4.3.1 to find the adjacent evidence for 4.3.2 as requested.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L495']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (48):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0564
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0564
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0540
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0540
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0540
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0564
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0564
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0564
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0564
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0532
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L103 | 2.4.6 各项目部应当加强对自然灾害的预防。对于因自然灾害可能导致事故灾难的隐患，应当按照有关法律、法规、标准和本制度的要求排查治理，采取可靠的预防措施，制定应急预案。在接到有关自然灾害预报时，应当及时向有关人员发出预警通知；发生自然灾害可能危及施工和人员安全的情况时，应当采取撤离人员、停止作业、加强监测等安全措施，并及时向当地人民政府有关部门报告。 | score=0.0564
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0558
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0558
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0558
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0558
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0558
- projection_chars: 3150

**Step 7** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence collected covers §4.3.2 content and the associated evaluation report form (G3, G2) required to answer the query.
- legal_actions (54):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0483
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0483
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0483
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0483
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0483
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0483
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0483
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0564
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0564
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0540
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0540
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0540
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0564
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0564
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0564
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0564
- projection_chars: 3415

### Evidence text (new)

```
[E1]
[§ 附表4.3.2]
  应急预案演练评价报告
  工程名称：

[E2]
[§ 4.4 应急响应程序]
附表4.3.2：应急预案演练评价报告。

[E3]
[§ 4.3 应急救援预案的演练]
  4.3.1 集团公司的综合应急救援预案每二年演练一次；项目部根据工程特点，项目施工（基础，主体，装饰）阶段，每年至少演练一次。演练必须编制演练方案（附表4.3.1：应急预案演练方案），并对参演人员进行宣传培训。
  4.3.2 演练结束后，演练组织部门对应急救援预案和处置程序的有效性、人员宣传培训和需求、设备和资源的充分性、应急救援行动以及是否达到预期目标作出评价报告（附表4.3.2：应急预案演练评价报告），交集团公司安全管理部存档。
  4.3.3 根据规范要求变化，应急预案环境改变，演练评价报告每一到二年修订应急救援预案。

[E4]
[§ 3.2 生产安全事故快报]
4.3.1 应急预案演练方案

[E5]
[§ 4.3.2 应急预案演练评价报]
5.2.2：《施工现场安全负面清单（2019版）》
```

### Evidence text (old)

```
[E1]
4.3.2 演练结束后，演练组织部门对应急救援预案和处置程序的有效性、人员宣传培训和需求、设备和资源的充分性、应急救援行动以及是否达到预期目标作出评价报告（附表4.3.2：应急预案演练评价报告），交集团公司安全管理部存档。

[E2]
4.3.1 集团公司的综合应急救援预案每二年演练一次；项目部根据工程特点，项目施工（基础，主体，装饰）阶段，每年至少演练一次。演练必须编制演练方案（附表4.3.1：应急预案演练方案），并对参演人员进行宣传培训。
```

## latest_clean_multi_0555 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“6.7.3 安全技术交底记录”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 79 | 488 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 1 | 16 |
| trajectory_steps | n/a | 3 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L505` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L506` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C24` kind=`collect` section=`real_69c60974d4242eda8c47c615:L374` scope=`None` depth=`0`
- reason: Collect section 6.7.3 text and the specific record form to answer the query about adjacent evidence points.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L374', 'real_69c60974d4242eda8c47c615:L560']
- collect added=2 hits=2 branch_selected=True collect_full=True
- legal_actions (61):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0565
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0565
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0565
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0565
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0565
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0565
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L56 | 1、安全技术交底、安全措施是否落实到施工作业中； | score=0.0565
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0527
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0527
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0499
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0499
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L185 | 根据工程特点及周围环境制定机械设备安全技术操作规程，设置安全警示标志；安全技术操作规程及警示标志应按照《施工现场标准化管理手册》要求制成标志牌悬挂在相应机械设备的醒目位置。 | score=0.0499
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L207 | 5.3 工具式脚手架管理 | score=0.0527
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L207 | 5.3 工具式脚手架管理 | score=0.0527
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L214 | 5.3.4 附着式升降脚手架、高空作业吊篮等管理程序： | score=0.0527
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L214 | 5.3.4 附着式升降脚手架、高空作业吊篮等管理程序： | score=0.0527
- projection_chars: 3391

**Step 2** `nav_collect`  id=`C28` kind=`collect` section=`real_69c60974d4242eda8c47c615:L501` scope=`None` depth=`0`
- reason: Collect section 6.7.3 to retrieve the full content of the safety technical disclosure record form.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L501']
- collect added=47 hits=47 branch_selected=True collect_full=True
- legal_actions (63):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0565
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0565
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0565
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0565
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0565
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0565
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L56 | 1、安全技术交底、安全措施是否落实到施工作业中； | score=0.0565
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0527
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0527
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0499
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0499
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L185 | 根据工程特点及周围环境制定机械设备安全技术操作规程，设置安全警示标志；安全技术操作规程及警示标志应按照《施工现场标准化管理手册》要求制成标志牌悬挂在相应机械设备的醒目位置。 | score=0.0499
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L207 | 5.3 工具式脚手架管理 | score=0.0527
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L207 | 5.3 工具式脚手架管理 | score=0.0527
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L214 | 5.3.4 附着式升降脚手架、高空作业吊篮等管理程序： | score=0.0527
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L214 | 5.3.4 附着式升降脚手架、高空作业吊篮等管理程序： | score=0.0527
- projection_chars: 3357

**Step 3** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: The query asks for points from section 6.7.3 and the associated form (附表6.7.3). G1 contains the text of 6.7.3, and G2 contains the form title/structure. These are the two adjacent relevant sections.
- legal_actions (58):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0565
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0565
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0565
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0565
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0565
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0565
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L56 | 1、安全技术交底、安全措施是否落实到施工作业中； | score=0.0565
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0477
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0477
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0477
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0471
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0471
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0462
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0462
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0462
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0471
- projection_chars: 3304

### Evidence text (new)

```
[E1]
[§ 6.7 安全技术交底管理]
6.7.3 安全技术交底应由交底人、被交底人、专职安全员进行签字确认。并由项目部专职安全员保存安全技术交底记录（附表6.7.3 安全技术交底记录）。

[E2]
[§ 附表6.7.3]
  安全技术交底记录
  工程名称：

[E3]
[§ 附表1.1.1]
  安全教育记录
  编号：
  注：1、本表适用于岗前教育、日常安全教育、年度继续教育等使用。
  2、安全教育形式分为：岗前教育；日常安全教育（班前安全活动、雨季安全教育、暑期安全教育、冬季安全教育、节假日安全教育、消防安全教育、安全警示教育等）；年度继续教育等。

[E4]
[§ 附件5.2.2                     施工现场安全负面清单（2]
文档列出使用不合格防坠器、超年限设备及维护不到位等问题的分包单位名单，并详细规定了塔吊、升降机、脚手架及临电设施等禁止或淘汰的技术标准与依据。

[E5]
[§ 附表1.2-3]
  分包单位操作人员三级安全教育记录表
  工程名称
  2、本表适用于公司总承包项目的分包企业操作人员的三级安全教育。
```

### Evidence text (old)

```
[E1]
6.7.3 安全技术交底应由交底人、被交底人、专职安全员进行签字确认。并由项目部专职安全员保存安全技术交底记录（附表6.7.3 安全技术交底记录）。
```

## latest_clean_multi_0568 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“附件5.2.2 施工现场安全负面清单（2019版）”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 413 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 18 | 4 |
| trajectory_steps | n/a | 4 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L545` [MISS] retrieved=False in_text=False
- `real_69c60974d4242eda8c47c615:L547` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60974d4242eda8c47c615:L193` scope=`real_69c60974d4242eda8c47c615:L193` depth=`1`
- reason: Collects the full section 5.2.2 to extract the two adjacent evidence points requested.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L193']
- collect added=3 hits=3 branch_selected=True collect_full=True
- legal_actions (4):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L193 | 附表5.2.2：《施工现场安全负面清单（2019版）》 | score=0.0613
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L194 | 5.2.3 租赁机械设备必须签订租赁和安装、拆卸合同，合同应使用集团公司合同示范文本，同时签订安全协议书（集团公司示范文本，明确总包、使用、租赁、安拆各方的安全责任）。 | score=0.0429
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L195 | 租赁、安装单位应提供加盖单位公章的营业执照、资质证书、安全生产许可证、施工机械租赁行业确认书、行业推荐证书等企业资质文件；以及拟租赁设备制造许可证、产品合格证、制造监督检验证明、备案登记、自检合格证明、安装使用说明书等产品证明文件。 | score=0.0613
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L196 | 5.2.4 租赁施工升降机和800KN·m及以下的塔式起重机时，应选用租赁安装维修保养一体化的专业承包企业；对800KN·m以上的塔式起重机出租单位，当其不具备相应的起重设备安装工程专业承包资质的，项目经理部必须在签订租赁合同的同时，与出租、安装单位共同签订三方安全管理协议书，并与安装单位签订安拆合同，并明确各方的安全生产权利与义务。 | score=0.0437
- projection_chars: 1251

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60974d4242eda8c47c615:L193` depth=`1`
- reason: Collected section L193 contains the required negative list content to answer the query.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 190

**Step 3** `nav_dispatch`  id=`D10` kind=`dispatch` section=`real_69c60974d4242eda8c47c615:L193` scope=`None` depth=`0`
- reason: Dispatch to retrieve the full content of Appendix 5.2.2 Negative List.
- dispatch_regions: ['real_69c60974d4242eda8c47c615:L193']
- child_reports=1 skipped=0
- legal_actions (55):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0619
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0619
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0611
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0611
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0611
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0611
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L49 | 5、施工现场管理行为和实物状况（安全隐患排查、安全设施及安全防护等各项措施和落实情况）； | score=0.0611
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0619
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0619
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0619
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0560
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0560
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0560
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0560
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0560
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0670
- projection_chars: 3430

**Step 4** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains the required negative list content to answer the query.
- legal_actions (57):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0619
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0619
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0611
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0611
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0611
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0611
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L49 | 5、施工现场管理行为和实物状况（安全隐患排查、安全设施及安全防护等各项措施和落实情况）； | score=0.0611
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0619
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0619
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0619
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0560
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0560
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0560
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0560
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0560
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0670
- projection_chars: 3557

### Subagent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60974d4242eda8c47c615:L193 (ok)
collected 4 branch node(s); explicit roots=['real_69c60974d4242eda8c47c615:L193']
collected: real_69c60974d4242eda8c47c615:L193, real_69c60974d4242eda8c47c615:L194, real_69c60974d4242eda8c47c615:L195, real_69c60974d4242eda8c47c615:L196
reason: Collected section L193 contains the required negative list content to answer the query.
---
=== End Investigate ===
```

### Evidence text (new)

```
[E1]
[§ 附表5.2.2：《施工现场安全负面清单（2019版）》]
  5.2.3 租赁机械设备必须签订租赁和安装、拆卸合同，合同应使用集团公司合同示范文本，同时签订安全协议书（集团公司示范文本，明确总包、使用、租赁、安拆各方的安全责任）。
  租赁、安装单位应提供加盖单位公章的营业执照、资质证书、安全生产许可证、施工机械租赁行业确认书、行业推荐证书等企业资质文件；以及拟租赁设备制造许可证、产品合格证、制造监督检验证明、备案登记、自检合格证明、安装使用说明书等产品证明文件。
  5.2.4 租赁施工升降机和800KN·m及以下的塔式起重机时，应选用租赁安装维修保养一体化的专业承包企业；对800KN·m以上的塔式起重机出租单位，当其不具备相应的起重设备安装工程专业承包资质的，项目经理部必须在签订租赁合同的同时，与出租、安装单位共同签订三方安全管理协议书，并与安装单位签订安拆合同，并明确各方的安全生产权利与义务。
```

### Evidence text (old)

```
[E1]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.2  安全检查及隐患排查内容 / 2.2.2班组安全检查的内容：]
3、施工工具、设备是否完好无损；

[E2]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表1.2-3]
工程名称

[E3]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表3.2]
单位名称：

[E4]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.3安全检查及隐患排查的方法 / 2.3.3 定期安全检查]
附表2-3-3《项目周检查标准化表格》

[E5]
[§ 附件_安全管理规定（2020版）.docx / 第三章　生产安全事故报告处理规定 / 3.2 事故报告]
1 事故的时间、地点和工程项目有关单位名称；

[E6]
[§ 附件_安全管理规定（2020版）.docx /
```

## latest_clean_multi_0572 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“附表6.6.1-1”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 495 | 476 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 16 | 6 |
| trajectory_steps | n/a | 8 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L554` [MISS] retrieved=False in_text=False
- `real_69c60974d4242eda8c47c615:L556` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C4` kind=`collect` section=`real_69c60974d4242eda8c47c615:L365` scope=`real_69c60974d4242eda8c47c615:L362` depth=`1`
- reason: Section C4 references Table 6.6.1-1, which is the target of the query.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L365']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (7):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L362 | 6.6 危险性较大的分部分项工程管理 | score=0.0725
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L363 | 6.6.1 项目部应当在危险性较大的分部分项工程施工前编制专项方案；对于超过一定规模的危险性较大的分部分项工程，项目部应当组织专家对专项方案进行论证。 | score=0.0295
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L364 | 其中，起重机械安装拆卸工程、深基坑工程、附着式升降脚手架等专业工程实行分包的，其专项方案可由专业承包单位组织编制，并经过分包单位具有法人资格企业的技术负责人批准。 | score=0.0142
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L365 | 危险性较大的分部分项工程识别清单（见附表6.6.1-1）；超过一定规模的危险性较大的分部分项工程识别清单（见附表6.6.1-2）。 | score=0.0609
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L366 | 6.6.2 专项方案编制应当包括的内容，应当组织专家论证的相关内容，参见《危险性较大的分部分项工程安全管理规定》（建办质[2018]31号）执行。审核审批执行集团公司相关要求。 | score=0.0725
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L367 | 6.6.3 在施工过程中，项目部必须严格执行经批准的安全专项施工方案，不得擅自修改，现场专职安全生产管理人员现场监督实施，项目部指定专人按规定进行监测，若发现现场施工条件和施工环境发生较大改变时，应当立即停止施工，撤离作业人员，并将有关情况及时上报监理单位和方案的审批部门，在采取可靠措施后方可恢复施工。 | score=0.0270
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L368 | 6.6.4 超过一定规模的危险性较大的分部分项工程施工时，集团公司委托二级单位负责人对施工现场进行带班检查。 | score=0.0223
- projection_chars: 1756

**Step 2** `nav_collect`  id=`C2` kind=`collect` section=`real_69c60974d4242eda8c47c615:L363` scope=`real_69c60974d4242eda8c47c615:L362` depth=`1`
- reason: Collect C2 and C3 to address the query about adjacent evidence points in section 6.6.1.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L363', 'real_69c60974d4242eda8c47c615:L364']
- collect added=2 hits=2 branch_selected=True collect_full=True
- legal_actions (7):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L362 | 6.6 危险性较大的分部分项工程管理 | score=0.0725
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L363 | 6.6.1 项目部应当在危险性较大的分部分项工程施工前编制专项方案；对于超过一定规模的危险性较大的分部分项工程，项目部应当组织专家对专项方案进行论证。 | score=0.0295
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L364 | 其中，起重机械安装拆卸工程、深基坑工程、附着式升降脚手架等专业工程实行分包的，其专项方案可由专业承包单位组织编制，并经过分包单位具有法人资格企业的技术负责人批准。 | score=0.0142
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L366 | 6.6.2 专项方案编制应当包括的内容，应当组织专家论证的相关内容，参见《危险性较大的分部分项工程安全管理规定》（建办质[2018]31号）执行。审核审批执行集团公司相关要求。 | score=0.0725
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L367 | 6.6.3 在施工过程中，项目部必须严格执行经批准的安全专项施工方案，不得擅自修改，现场专职安全生产管理人员现场监督实施，项目部指定专人按规定进行监测，若发现现场施工条件和施工环境发生较大改变时，应当立即停止施工，撤离作业人员，并将有关情况及时上报监理单位和方案的审批部门，在采取可靠措施后方可恢复施工。 | score=0.0270
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L368 | 6.6.4 超过一定规模的危险性较大的分部分项工程施工时，集团公司委托二级单位负责人对施工现场进行带班检查。 | score=0.0223
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 1587

**Step 3** `nav_collect`  id=`C2` kind=`collect` section=`real_69c60974d4242eda8c47c615:L366` scope=`real_69c60974d4242eda8c47c615:L362` depth=`1`
- reason: Collect C2 and C3 to address the query about adjacent evidence points in Section 6.6.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L366', 'real_69c60974d4242eda8c47c615:L367']
- collect added=2 hits=2 branch_selected=True collect_full=True
- legal_actions (5):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L362 | 6.6 危险性较大的分部分项工程管理 | score=0.0725
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L366 | 6.6.2 专项方案编制应当包括的内容，应当组织专家论证的相关内容，参见《危险性较大的分部分项工程安全管理规定》（建办质[2018]31号）执行。审核审批执行集团公司相关要求。 | score=0.0725
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L367 | 6.6.3 在施工过程中，项目部必须严格执行经批准的安全专项施工方案，不得擅自修改，现场专职安全生产管理人员现场监督实施，项目部指定专人按规定进行监测，若发现现场施工条件和施工环境发生较大改变时，应当立即停止施工，撤离作业人员，并将有关情况及时上报监理单位和方案的审批部门，在采取可靠措施后方可恢复施工。 | score=0.0270
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L368 | 6.6.4 超过一定规模的危险性较大的分部分项工程施工时，集团公司委托二级单位负责人对施工现场进行带班检查。 | score=0.0223
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 1139

**Step 4** `nav_collect`  id=`C2` kind=`collect` section=`real_69c60974d4242eda8c47c615:L368` scope=`real_69c60974d4242eda8c47c615:L362` depth=`1`
- reason: Section C2 (6.6.4) is a leaf node directly relevant to the query about adjacent evidence points in Table 6.6.1-1.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L368']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (3):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L362 | 6.6 危险性较大的分部分项工程管理 | score=0.0725
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L368 | 6.6.4 超过一定规模的危险性较大的分部分项工程施工时，集团公司委托二级单位负责人对施工现场进行带班检查。 | score=0.0223
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 555

**Step 5** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60974d4242eda8c47c615:L362` scope=`real_69c60974d4242eda8c47c615:L362` depth=`1`
- reason: Collect section 6.6 to find details on adjacent evidence points in Table 6.6.1-1.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L362']
- collect added=6 hits=6 branch_selected=True collect_full=True
- legal_actions (2):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L362 | 6.6 危险性较大的分部分项工程管理 | score=0.0725
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 392

**Step 6** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60974d4242eda8c47c615:L362` depth=`1`
- reason: Collected 5 sections covering the required table content; sufficient to answer query.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 190

**Step 7** `nav_dispatch`  id=`D16` kind=`dispatch` section=`real_69c60974d4242eda8c47c615:L362` scope=`None` depth=`0`
- reason: Dispatch section 6.6 to locate and extract details from Appendix 6.6.1-1.
- dispatch_regions: ['real_69c60974d4242eda8c47c615:L362']
- child_reports=1 skipped=0
- legal_actions (57):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0560
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0560
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0560
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0560
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0560
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0560
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0560
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0557
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0557
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0557
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0557
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0557
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0571
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0571
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0571
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0571
- projection_chars: 3282

**Step 8** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains §6.6 and Table 6.6.1-1 details required to answer the query.
- legal_actions (58):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0560
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0560
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0560
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0560
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0560
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0560
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0560
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0557
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0557
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0557
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0557
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0557
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0571
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0571
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0571
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0571
- projection_chars: 3226

### Subagent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60974d4242eda8c47c615:L362 (ok)
collected 7 branch node(s); explicit roots=['real_69c60974d4242eda8c47c615:L365', 'real_69c60974d4242eda8c47c615:L363', 'real_69c60974d4242eda8c47c615:L366', 'real_69c60974d4242eda8c47c615:L368', 'real_69c60974d4242eda8c47c615:L362']
collected: real_69c60974d4242eda8c47c615:L362, real_69c60974d4242eda8c47c615:L363, real_69c60974d4242eda8c47c615:L364, real_69c60974d4242eda8c47c615:L365, real_69c60974d4242eda8c47c615:L366, real_69c60974d4242eda8c47c615:L367, real_69c60974d4242eda8c47c615:L368
reason: Collected 5 sections covering the required table content; sufficient to answer query.
---
=== End Investigate ===
```

### Evidence text (new)

```
[E1]
[§ 6.6 危险性较大的分部分项工程管理]
  6.6.1 项目部应当在危险性较大的分部分项工程施工前编制专项方案；对于超过一定规模的危险性较大的分部分项工程，项目部应当组织专家对专项方案进行论证。
  危险性较大的分部分项工程识别清单（见附表6.6.1-1）；超过一定规模的危险性较大的分部分项工程识别清单（见附表6.6.1-2）。
  6.6.2 专项方案编制应当包括的内容，应当组织专家论证的相关内容，参见《危险性较大的分部分项工程安全管理规定》（建办质[2018]31号）执行。审核审批执行集团公司相关要求。
  6.6.3 在施工过程中，项目部必须严格执行经批准的安全专项施工方案，不得擅自修改，现场专职安全生产管理人员现场监督实施，项目部指定专人按规定进行监测，若发现现场施工条件和施工环境发生较大改变时，应当立即停止施工，撤离作业人员，并将有关情况及时上报监理单位和方案的审批部门，在采取可靠措施后方可恢复施工。
  6.6.4 超过一定规模的危险性较大的分部分项工程施工时，集团公司委托二级单位负责人对施工现场进行带班检查。
```

### Evidence text (old)

```
[E1]
附件_安全管理规定（2020版）.docx

[E2]
[§ 附件_安全管理规定（2020版）.docx / 第一章　安全教育培训规定 / 1.7 附则]
附表1：安全教育记录；

[E3]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表1.1.1]
编号：

[E4]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表6.3.5]
注：本表后附各类开支的发票、收据、结算单封面等证明材料的复印件，按季度统计结转。

[E5]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表1.1.1]
安全教育记录

[E6]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.4 隐患整改 / 2.4.4 重大事故隐患整改、复查、销项]
6、安全措施和应急预案。
```

## latest_clean_multi_0573 (multi_hop)

**Query:** 根据《附件_安全管理规定（2020版）》中“附表6.6.1-2”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 148 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 18 | 2 |
| trajectory_steps | n/a | 3 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L556` [MISS] retrieved=False in_text=False
- `real_69c60974d4242eda8c47c615:L558` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C31` kind=`collect` section=`real_69c60974d4242eda8c47c615:L412` scope=`None` depth=`0`
- reason: Target section '附表6.6.1-2' is a leaf node containing the specific list required by the query.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L412']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (59):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0561
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0561
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0561
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0561
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0561
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0561
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0561
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0566
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0566
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0566
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0566
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0566
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0507
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0507
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0507
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0507
- projection_chars: 3423

**Step 2** `nav_collect`  id=`C25` kind=`collect` section=`real_69c60974d4242eda8c47c615:L365` scope=`None` depth=`0`
- reason: Collect section containing reference to Table 6.6.1-2 to retrieve its content.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L365']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (59):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0561
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0561
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0561
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0561
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0561
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0561
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0561
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0566
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0566
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0566
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0566
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0566
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0507
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0507
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0507
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0507
- projection_chars: 3362

**Step 3** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Assembled evidence covers both required sections (G1, G2) for the query regarding 附表6.6.1-2.
- legal_actions (63):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0561
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0561
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0561
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0561
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0561
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0561
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0561
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0566
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0566
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0566
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0566
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0566
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0507
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0507
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0507
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0507
- projection_chars: 3537

### Evidence text (new)

```
[E1]
[§ 6.6 危险性较大的分部分项工程管理]
危险性较大的分部分项工程识别清单（见附表6.6.1-1）；超过一定规模的危险性较大的分部分项工程识别清单（见附表6.6.1-2）。

[E2]
[§ 6.11 安全标志]
附表6.6.1-2：超过一定规模的危险性较大的分部分项工程识别清单；
```

### Evidence text (old)

```
[E1]
附件_安全管理规定（2020版）.docx

[E2]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表6.6.1-1]
备注： 本表中所列工程，若本工程施工中有时在对应的辨识结论栏内打“√”，无时打“×”。

[E3]
[§ 附件_安全管理规定（2020版）.docx / 第一章　安全教育培训规定 / 1.7 附则]
附表1：安全教育记录；

[E4]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表1.1.1]
编号：

[E5]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.2  安全检查及隐患排查内容 / 2.2.2班组安全检查的内容：]
2、安全“三宝”的使用情况；

[E6]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.4 隐患整改 / 2.4.4 重大事故隐患整改、复查、销项]
6
```

## latest_clean_multi_0712 (multi_hop)

**Query:** 根据《陕西建工第十一建集团有限公司生产安全事故综合应急预案（2025版）》中“2.6 项目部应急救援领导小组成员职责”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c6097ad4242eda8c47c62c`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 492 |
| gold_node_recall | 0.0 | 0.5 |
| n_retrieved_nodes | 8 | 12 |
| trajectory_steps | n/a | 4 |

### Gold node hits (new)

- `real_69c6097ad4242eda8c47c62c:L155` [MISS] retrieved=False in_text=False
- `real_69c6097ad4242eda8c47c62c:L156` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6097ad4242eda8c47c62c:L152` scope=`real_69c6097ad4242eda8c47c62c:L152` depth=`1`
- reason: Collects the full section 2.6 to identify and compare duties of adjacent evidence groups.
- collect_section_ids: ['real_69c6097ad4242eda8c47c62c:L152']
- collect added=40 hits=40 branch_selected=True collect_full=True
- legal_actions (17):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L152 | 2.6 项目部应急救援领导小组成员职责 | score=0.0643
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L154 | 1 、负责制定本项目应急救援预案； | score=0.0430
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L156 | 3 、负责向二级单位应急救援领导小组，必要时可直接向集团公司应急救援总指挥部、当地辖区政府部门报告事故的伤亡和损失情况； | score=0.0542
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L157 | 4 、负责建立项目部与相关应急救援部门、组织和机构（如：急救120、 消防119）的应急救援通信平台，并保障通信畅通； | score=0.0447
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L159 | 6 、负责项目部应急救援所需物资、设备的储备。 | score=0.0474
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L162 | 2 、负责保持与事故现场相关抢救抢险组员的直接联络； | score=0.0533
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L165 | 5 、负责组织项目部相关技术和管理人员对施工现场生产过程各危险源进行风险辨识、评价，落实对重大危险源的有效管控； | score=0.0463
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L166 | 6 、负责项目部与当地医疗机构、抢险救援机构建立应急救援网络和签订应急救援协议，保障相关机构在事故应急救援中的及时性和有效性。 | score=0.0615
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L168 | 1 、负责项目部生产安全事故应急救援预案的演练，发生事故后立即实施现场应急救援； | score=0.0488
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L169 | 2 、负责向项目部应急救援领导小组报告事故现场人员伤亡和财产损失情况； | score=0.0588
  - C11 | COLLECT | real_69c6097ad4242eda8c47c62c:L170 | 3 、组织实施项目部生产安全事故应急救援预案的人员、材料、设备和其他资源的相互配合； | score=0.0643
  - C12 | COLLECT | real_69c6097ad4242eda8c47c62c:L176 | 1 、编制项目部生产安全事故应急救援预案，并参与演练及实施； | score=0.0465
  - C13 | COLLECT | real_69c6097ad4242eda8c47c62c:L177 | 2 、负责生产安全事故现场处置过程中的技术支持。 | score=0.0504
  - C14 | COLLECT | real_69c6097ad4242eda8c47c62c:L181 | 1 、负责项目部安装人员应急救援预案的教育培训、演练及实施； | score=0.0415
  - C15 | COLLECT | real_69c6097ad4242eda8c47c62c:L185 | 负责事故应急处理中法律法规资料的收集，为事故处理提供法律支持。 | score=0.0413
  - C16 | COLLECT | real_69c6097ad4242eda8c47c62c:L188 | 2、负责收集相关单位、部门的通信方式，保证与集团公司、二级单位、 所辖区域当地政府各级部门和附近相关救助机构的通讯联络工作； | score=0.0478
- projection_chars: 2692

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c6097ad4242eda8c47c62c:L152` depth=`1`
- reason: Collected section L152 contains the required responsibilities for the project emergency rescue leadership group members.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 190

**Step 3** `nav_dispatch`  id=`D5` kind=`dispatch` section=`real_69c6097ad4242eda8c47c62c:L152` scope=`None` depth=`0`
- reason: Dispatch to section 2.6 to retrieve details on project department emergency leadership group member duties.
- dispatch_regions: ['real_69c6097ad4242eda8c47c62c:L152']
- child_reports=1 skipped=0
- legal_actions (41):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0643
  - D1 | DISPATCH | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0643
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L38 | 2.1 应急组织体系 | score=0.0515
  - D2 | DISPATCH | real_69c6097ad4242eda8c47c62c:L38 | 2.1 应急组织体系 | score=0.0515
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L39 | 生产安全事故应急救援工作在集团公司统一领导下，各二级单位、各有关职能部门分工合作、各司其职、密切配合，迅速、高效、有序开展。 集团设立生产安全事故应急救援指挥部，其组成如下： | score=0.0489
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L51 | 各二级单位成立相应的生产安全事故应急救援领导小组，下设抢救抢险组、技术支持组、医疗救护组、通信联络组、后勤保障组和善后处置组。 组长由二级单位总经理担任，副组长由总工程师、生产副总经理（安全总监）担任，组员由生产安全管理部、经营预算部、技术管理部、综合办公室、财务管理服务中心各工程公司财务部等职能部门负责人组成。 | score=0.0515
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L53 | 项目部成立生产安全事故应急救援领导（处置）小组，下设抢救抢险组、技术支持组、医疗救护组、通信联络组、后勤保障组和善后处置组。 组长由项目经理担任，副组长由项目总工程师（ 生产副经理）和安全总监担任，成员由生产安全管理组、材料动力组、技术管理组、商务预算组、 安装管理组、行政后勤组、财务专员等部门负责人组成。 | score=0.0452
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L59 | 项目部应急救援领导小组 | score=0.0497
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L69 | 2.3 集团公司应急救援副总指挥的职责 | score=0.0455
  - D3 | DISPATCH | real_69c6097ad4242eda8c47c62c:L69 | 2.3 集团公司应急救援副总指挥的职责 | score=0.0455
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L72 | 3 、保持与事故现场二级单位或项目部应急救援领导小组的直接联络； | score=0.0455
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L124 | 2.5 二级单位应急救援领导小组成员职责 | score=0.0549
  - D4 | DISPATCH | real_69c6097ad4242eda8c47c62c:L124 | 2.5 二级单位应急救援领导小组成员职责 | score=0.0549
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L128 | 3 、督促项目部与相关应急救援部门、组织和机构（如：急救120 、消防119）建立应急救援通信平台； | score=0.0475
  - C11 | COLLECT | real_69c6097ad4242eda8c47c62c:L135 | 5 、监督项目部与当地医疗机构、抢险救援机构建立应急救援网络和签订应急救援协议，保障相关机构在事故应急救援中的及时性和有效性。 | score=0.0549
  - C12 | COLLECT | real_69c6097ad4242eda8c47c62c:L137 | 1 、负责指导项目部建立现场生产安全事故应急救援预案并实施； | score=0.0535
- projection_chars: 3517

**Step 4** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains the complete list of responsibilities for project emergency rescue leadership group members as requested.
- legal_actions (43):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0432
  - D1 | DISPATCH | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0432
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0432
  - D2 | DISPATCH | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0432
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L19 | 根据国务院第493 号令《生产安全事故报告和调查处理条例》规定， 结合集团公司实际，按照“企业自救、行业互救、社会联动、逐级响应、分级负责”的原则，建立集团公司、二级单位、项目经理部三级响应的应急救援体系。 | score=0.0432
  - D3 | DISPATCH | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0643
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L38 | 2.1 应急组织体系 | score=0.0515
  - D4 | DISPATCH | real_69c6097ad4242eda8c47c62c:L38 | 2.1 应急组织体系 | score=0.0515
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L39 | 生产安全事故应急救援工作在集团公司统一领导下，各二级单位、各有关职能部门分工合作、各司其职、密切配合，迅速、高效、有序开展。 集团设立生产安全事故应急救援指挥部，其组成如下： | score=0.0489
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L51 | 各二级单位成立相应的生产安全事故应急救援领导小组，下设抢救抢险组、技术支持组、医疗救护组、通信联络组、后勤保障组和善后处置组。 组长由二级单位总经理担任，副组长由总工程师、生产副总经理（安全总监）担任，组员由生产安全管理部、经营预算部、技术管理部、综合办公室、财务管理服务中心各工程公司财务部等职能部门负责人组成。 | score=0.0515
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L53 | 项目部成立生产安全事故应急救援领导（处置）小组，下设抢救抢险组、技术支持组、医疗救护组、通信联络组、后勤保障组和善后处置组。 组长由项目经理担任，副组长由项目总工程师（ 生产副经理）和安全总监担任，成员由生产安全管理组、材料动力组、技术管理组、商务预算组、 安装管理组、行政后勤组、财务专员等部门负责人组成。 | score=0.0452
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L59 | 项目部应急救援领导小组 | score=0.0497
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L69 | 2.3 集团公司应急救援副总指挥的职责 | score=0.0455
  - D5 | DISPATCH | real_69c6097ad4242eda8c47c62c:L69 | 2.3 集团公司应急救援副总指挥的职责 | score=0.0455
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L72 | 3 、保持与事故现场二级单位或项目部应急救援领导小组的直接联络； | score=0.0455
  - C11 | COLLECT | real_69c6097ad4242eda8c47c62c:L76 | 7 、根据各施工场区的实际条件，协调集团公司与周边有条件的企业在事故应急处理中共享资源、相互帮助、建立共同应急救援网络和制定应急救援协议。 | score=0.0430
- projection_chars: 3452

### Subagent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c6097ad4242eda8c47c62c:L152 (ok)
collected 41 branch node(s); explicit roots=['real_69c6097ad4242eda8c47c62c:L152']
collected: real_69c6097ad4242eda8c47c62c:L152, real_69c6097ad4242eda8c47c62c:L153, real_69c6097ad4242eda8c47c62c:L154, real_69c6097ad4242eda8c47c62c:L155, real_69c6097ad4242eda8c47c62c:L156, real_69c6097ad4242eda8c47c62c:L157, real_69c6097ad4242eda8c47c62c:L158, real_69c6097ad4242eda8c47c62c:L159, real_69c6097ad4242eda8c47c62c:L160, real_69c6097ad4242eda8c47c62c:L161, real_69c6097ad4242eda8c47c62c:L162, real_69c6097ad4242eda8c47c62c:L163, real_69c6097ad4242eda8c47c62c:L164, real_69c6097ad4242eda8c47c62c:L165, real_69c6097ad4242eda8c47c62c:L166, real_69c6097ad4242eda8c47c62c:L167, real_69c6097ad4242eda8c47c62c:L168, real_69c6097ad4242eda8c47c62c:L169, real_69c6097ad4242eda8c47c62c:L170, real_69c6097ad4242eda8c47c62c:L171
reason: Collected section L152 contains the required responsibilities for the project emergency rescue leadership group members.
---
=== End Investigate ===
```

### Evidence text (new)

```
[E1]
[§ 2.6 项目部应急救援领导小组成员职责]
  （ 一）组长
  3 、负责向二级单位应急救援领导小组，必要时可直接向集团公司应急救援总指挥部、当地辖区政府部门报告事故的伤亡和损失情况；
  6 、负责项目部应急救援所需物资、设备的储备。
  2 、负责保持与事故现场相关抢救抢险组员的直接联络；
  6 、负责项目部与当地医疗机构、抢险救援机构建立应急救援网络和签订应急救援协议，保障相关机构在事故应急救援中的及时性和有效性。
  1 、负责项目部生产安全事故应急救援预案的演练，发生事故后立即实施现场应急救援；
  2 、负责向项目部应急救援领导小组报告事故现场人员伤亡和财产损失情况；
  3 、组织实施项目部生产安全事故应急救援预案的人员、材料、设备和其他资源的相互配合；
  2 、负责生产安全事故现场处置过程中的技术支持。
  2、负责收集相关单位、部门的通信方式，保证与集团公司、二级单位、 所辖区域当地政府各级部门和附近相关救助机构的通讯联络工作；
  5 、负责依据相关安全生产法律法规、工伤保险条例的规定，与工伤保险部门办理伤亡人员相关赔偿处理事宜；
```

### Evidence text (old)

```
[E1]
[§ 2.6 项目部应急救援领导小组成员职责]
2 、负责保持与事故现场相关抢救抢险组员的直接联络；

[E2]
[§ 2.6 项目部应急救援领导小组成员职责]
1 、编制项目部生产安全事故应急救援预案，并参与演练及实施；

[E3]
[§ 2.6 项目部应急救援领导小组成员职责]
5 、负责依据相关安全生产法律法规、工伤保险条例的规定，与工伤保险部门办理伤亡人员相关赔偿处理事宜；

[E4]
[§ 2.6 项目部应急救援领导小组成员职责]
2 、负责向项目部应急救援领导小组报告事故现场人员伤亡和财产损失情况；

[E5]
[§ 2.6 项目部应急救援领导小组成员职责]
1 、负责项目部生产安全事故应急救援预案的演练，发生事故后立即实施现场应急救援；

[E6]
[§ 2.6 项目部应急救援领导小组成员职责]
3 、组织实施项目部生产安全事故应急救援预案的人员、材料、设备和其他资源的相互配合；

[E7]
[§ 2.6 项目部应急救援领导小组成员职责]
2、负责收集相关单位、部门的通信方式，保证与集团公司、二级单位、 所辖区域当地政府各级部门和附近相关救助机构的通讯联络工作；
```

## latest_clean_multi_0742 (multi_hop)

**Query:** 根据《陕西建工第十一建集团有限公司生产安全事故综合应急预案（2025版）》中“2.7 各应急救援小组职责”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c6097ad4242eda8c47c62c`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 489 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 9 | 16 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c6097ad4242eda8c47c62c:L195` [HIT] retrieved=True in_text=False
- `real_69c6097ad4242eda8c47c62c:L196` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C20` kind=`collect` section=`real_69c6097ad4242eda8c47c62c:L193` scope=`None` depth=`0`
- reason: Section 2.7 contains the required emergency rescue group duties.
- collect_section_ids: ['real_69c6097ad4242eda8c47c62c:L193']
- collect added=25 hits=25 branch_selected=True collect_full=True
- legal_actions (46):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0563
  - D1 | DISPATCH | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0563
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0563
  - D2 | DISPATCH | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0563
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L19 | 根据国务院第493 号令《生产安全事故报告和调查处理条例》规定， 结合集团公司实际，按照“企业自救、行业互救、社会联动、逐级响应、分级负责”的原则，建立集团公司、二级单位、项目经理部三级响应的应急救援体系。 | score=0.0505
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L25 | （4）超出自身应急救援能力范围的事故，上级部门要求集团公司配合进行应急处置的各类安全生产事故。 | score=0.0531
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L29 | （3 ）超出自身应急救援能力范围的事故，上级部门要求集团公司配合进行应急处置的各类安全生产事故。 | score=0.0515
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L32 | （2）超出自身应急救援能力范围的事故，上级部门要求集团公司配合进行应急处置的各类安全生产事故。 | score=0.0563
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0704
  - D3 | DISPATCH | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0704
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L38 | 2.1 应急组织体系 | score=0.0529
  - D4 | DISPATCH | real_69c6097ad4242eda8c47c62c:L38 | 2.1 应急组织体系 | score=0.0529
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L39 | 生产安全事故应急救援工作在集团公司统一领导下，各二级单位、各有关职能部门分工合作、各司其职、密切配合，迅速、高效、有序开展。 集团设立生产安全事故应急救援指挥部，其组成如下： | score=0.0529
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L51 | 各二级单位成立相应的生产安全事故应急救援领导小组，下设抢救抢险组、技术支持组、医疗救护组、通信联络组、后勤保障组和善后处置组。 组长由二级单位总经理担任，副组长由总工程师、生产副总经理（安全总监）担任，组员由生产安全管理部、经营预算部、技术管理部、综合办公室、财务管理服务中心各工程公司财务部等职能部门负责人组成。 | score=0.0525
  - C11 | COLLECT | real_69c6097ad4242eda8c47c62c:L69 | 2.3 集团公司应急救援副总指挥的职责 | score=0.0704
  - D5 | DISPATCH | real_69c6097ad4242eda8c47c62c:L69 | 2.3 集团公司应急救援副总指挥的职责 | score=0.0704
- projection_chars: 3594

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains the complete section 2.7 with all group duties required by the query.
- legal_actions (45):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0563
  - D1 | DISPATCH | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0563
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0563
  - D2 | DISPATCH | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0563
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L19 | 根据国务院第493 号令《生产安全事故报告和调查处理条例》规定， 结合集团公司实际，按照“企业自救、行业互救、社会联动、逐级响应、分级负责”的原则，建立集团公司、二级单位、项目经理部三级响应的应急救援体系。 | score=0.0505
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L25 | （4）超出自身应急救援能力范围的事故，上级部门要求集团公司配合进行应急处置的各类安全生产事故。 | score=0.0531
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L29 | （3 ）超出自身应急救援能力范围的事故，上级部门要求集团公司配合进行应急处置的各类安全生产事故。 | score=0.0515
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L32 | （2）超出自身应急救援能力范围的事故，上级部门要求集团公司配合进行应急处置的各类安全生产事故。 | score=0.0563
  - D3 | DISPATCH | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0704
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L38 | 2.1 应急组织体系 | score=0.0529
  - D4 | DISPATCH | real_69c6097ad4242eda8c47c62c:L38 | 2.1 应急组织体系 | score=0.0529
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L39 | 生产安全事故应急救援工作在集团公司统一领导下，各二级单位、各有关职能部门分工合作、各司其职、密切配合，迅速、高效、有序开展。 集团设立生产安全事故应急救援指挥部，其组成如下： | score=0.0529
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L51 | 各二级单位成立相应的生产安全事故应急救援领导小组，下设抢救抢险组、技术支持组、医疗救护组、通信联络组、后勤保障组和善后处置组。 组长由二级单位总经理担任，副组长由总工程师、生产副总经理（安全总监）担任，组员由生产安全管理部、经营预算部、技术管理部、综合办公室、财务管理服务中心各工程公司财务部等职能部门负责人组成。 | score=0.0525
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0461
  - D5 | DISPATCH | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0461
  - C11 | COLLECT | real_69c6097ad4242eda8c47c62c:L62 | 2 、根据事故发生情况，决定是否发布启动或终止预案的命令，统一部署应急救援预案的实施工作，并对应急救援工作中发生的争议采取紧急处置措施； | score=0.0461
- projection_chars: 3568

### Evidence text (new)

```
[E1]
[§ 2.7 各应急救援小组职责]
  （ 一）抢险抢救组
  1 、组织应急救援的演练和应急处置实施抢险行动方案的执行；
  2 、协调有关部门的抢险行动；
  3 、及时向应急救援领导小组报告抢险进展情况；
  4 、做好现场的应急救援过程中的记录和现场的保护，在事故调查、取证完成后及时清理事故现场。
  1 、制定其可能出现而必须运用建筑工程技术解决的应急处置方案；
  2 、负责事故应急处置中及时向应急救援领导小组提供科学的工程技术方案和技术支持，解决应急处置中行动中的技术问题；
  1 、保障事故处置过程中所需资金的储备；
  2 、负责现场应急救援材料、物资的购置、储备和分发；
  3 、负责现场应急处置期间抢险器材、设备的调集；
  （ 四）善后处置组
  2 、做好受伤人员医疗救护的跟踪工作，协调处理医疗救护过程中的人员值班工作；
  3 、依据相关安全生产法律法规、工伤保险条例的规定，做好伤亡人员相关赔偿处理事宜。
  1 、负责生产安全事故处理过程中信息发布和媒体接待；
  2 、负责收集相关单位部门的通信方式，保证各级通讯联系畅通；
```

### Evidence text (old)

```
[E1]
[§ 2.7 各应急救援小组职责]
4 、做好现场的应急救援过程中的记录和现场的保护，在事故调查、取证完成后及时清理事故现场。

[E2]
[§ 2.7 各应急救援小组职责]
3 、依据相关安全生产法律法规、工伤保险条例的规定，做好伤亡人员相关赔偿处理事宜。

[E3]
[§ 2.7 各应急救援小组职责]
1 、制定其可能出现而必须运用建筑工程技术解决的应急处置方案；

[E4]
[§ 2.7 各应急救援小组职责]
1 、通知伤亡人员的家属并安排食、住、行等活动，做好伤亡人员及其家属的稳定工作，确保事故发生后伤亡人员及其家属思想稳定；

[E5]
[§ 2.7 各应急救援小组职责]
2 、负责事故应急处置中及时向应急救援领导小组提供科学的工程技术方案和技术支持，解决应急处置中行动中的技术问题；

[E6]
[§ 2.7 各应急救援小组职责]
1 、做好现场应急救援药品、医疗器械等方面的储存、发放和使用；

[E7]
[§ 2.7 各应急救援小组职责]
1 、负责生产安全事故处理过程中信息发布和媒体接待；

[E8]
[§ 2.7 各应急救援小组职责]
2 、负责现场应急救援材
```

## latest_clean_multi_0760 (multi_hop)

**Query:** 根据《陕西建工第十一建集团有限公司生产安全事故综合应急预案（2025版）》中“3.1 信息报告”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c6097ad4242eda8c47c62c`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 500 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 14 | 14 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c6097ad4242eda8c47c62c:L222` [HIT] retrieved=True in_text=False
- `real_69c6097ad4242eda8c47c62c:L223` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C10` kind=`collect` section=`real_69c6097ad4242eda8c47c62c:L220` scope=`None` depth=`0`
- reason: Collect section 3.1 Information Reporting to find the two adjacent evidence points requested.
- collect_section_ids: ['real_69c6097ad4242eda8c47c62c:L220']
- collect added=25 hits=25 branch_selected=True collect_full=True
- legal_actions (47):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0603
  - D1 | DISPATCH | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0603
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L4 | 1.2 编制依据 | score=0.0582
  - D2 | DISPATCH | real_69c6097ad4242eda8c47c62c:L4 | 1.2 编制依据 | score=0.0582
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L8 | 4 、《生产安全事故报告和调查处理条例》 | score=0.0518
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L14 | 10 、《陕西建工第十一建设集团有限公司生产安全事故风险评估报告》 | score=0.0560
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L15 | 11 、《陕西建工第十一建设集团有限公司生产安全事故应急资源调查报告》 | score=0.0582
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0603
  - D3 | DISPATCH | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0603
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L19 | 根据国务院第493 号令《生产安全事故报告和调查处理条例》规定， 结合集团公司实际，按照“企业自救、行业互救、社会联动、逐级响应、分级负责”的原则，建立集团公司、二级单位、项目经理部三级响应的应急救援体系。 | score=0.0603
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L29 | （3 ）超出自身应急救援能力范围的事故，上级部门要求集团公司配合进行应急处置的各类安全生产事故。 | score=0.0515
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L219 | 3.应急响应 | score=0.0654
  - D4 | DISPATCH | real_69c6097ad4242eda8c47c62c:L219 | 3.应急响应 | score=0.0654
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L220 | 3.1 信息报告 | score=0.0654
  - D5 | DISPATCH | real_69c6097ad4242eda8c47c62c:L220 | 3.1 信息报告 | score=0.0654
  - C11 | COLLECT | real_69c6097ad4242eda8c47c62c:L221 | 3.1.1 信息接报与上报 | score=0.0563
- projection_chars: 3544

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains section 3.1 Information Reporting with all required details for the query.
- legal_actions (47):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0603
  - D1 | DISPATCH | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0603
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L4 | 1.2 编制依据 | score=0.0582
  - D2 | DISPATCH | real_69c6097ad4242eda8c47c62c:L4 | 1.2 编制依据 | score=0.0582
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L8 | 4 、《生产安全事故报告和调查处理条例》 | score=0.0518
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L13 | 9 、《陕西建工集团股份有限公司生产安全事故综合应急预案》 | score=0.0498
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L14 | 10 、《陕西建工第十一建设集团有限公司生产安全事故风险评估报告》 | score=0.0560
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L15 | 11 、《陕西建工第十一建设集团有限公司生产安全事故应急资源调查报告》 | score=0.0582
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L16 | 1.3 适用范围 | score=0.0487
  - D3 | DISPATCH | real_69c6097ad4242eda8c47c62c:L16 | 1.3 适用范围 | score=0.0487
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L17 | 本《预案》适用于集团公司、二级单位及项目经理部所承建工程施工现场发生的坍塌、高处坠落、物体打击、触电、起重伤害、机械伤害、车辆伤害、中毒与窒息、火灾、灼烫、容器爆炸、其他伤害等较大及其以上各类生产安全事故，同时包括有重大社会影响、涉及公共安全或突发事件应急处置工作的应急救援。 | score=0.0487
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0603
  - D4 | DISPATCH | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0603
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L19 | 根据国务院第493 号令《生产安全事故报告和调查处理条例》规定， 结合集团公司实际，按照“企业自救、行业互救、社会联动、逐级响应、分级负责”的原则，建立集团公司、二级单位、项目经理部三级响应的应急救援体系。 | score=0.0603
  - C11 | COLLECT | real_69c6097ad4242eda8c47c62c:L29 | （3 ）超出自身应急救援能力范围的事故，上级部门要求集团公司配合进行应急处置的各类安全生产事故。 | score=0.0515
  - C12 | COLLECT | real_69c6097ad4242eda8c47c62c:L32 | （2）超出自身应急救援能力范围的事故，上级部门要求集团公司配合进行应急处置的各类安全生产事故。 | score=0.0465
- projection_chars: 3604

### Evidence text (new)

```
[E1]
[§ 3.1 信息报告]
  3.1.1 信息接报与上报
  值班人员在接到事故报告信息后，及时确认事故信息， 并在第一时间向应急救援总指挥报告， 由总指挥根据事故情况决定是否启动本预案和通知人员的范围。
  发生生产安全事故后，项目经理部应当立即启动现场处置预案，并将发生事故的有关信息及时、准确地通过电话、传真等形式报告至集团应急
  救援指挥部办公室和总指挥， 由集团根据事故分级，在1 小时内上报事故发生地县级以上应急管理部门负有安全生产监督管理职责的有关部门。事故信息发生变化时，应及时以书面形式补报有关变化情况。
  陕西建工股份集团有
  负有安全生产监督管理职责的有关部门
  报告事故应当包括以下内容：
  （ 一）事故发生项目概况；
  （ 二）事故发生的时间、地点以及事故现场情况；
  （ 三）事故的简要经过；
  （ 六）其他应当报告的情况。
  3.1.2 信息处置与研判
  集团公司应急救援指挥办公室接到报告后，按照分级响应的原则，根据事故的性质、严重程度、影响范围和可控性，对事故进行预判，并报告给集团应急救援总指挥，由总指挥做出预警或应急响应启动的决策。
```

### Evidence text (old)

```
[E1]
[§ 3.1 信息报告]
（ 一）事故发生项目概况；

[E2]
[§ 3.1 信息报告]
（ 二）事故发生的时间、地点以及事故现场情况；

[E3]
[§ 3.1 信息报告]
陕西建工股份集团有

[E4]
[§ 3.1 信息报告]
（ 三）事故的简要经过；

[E5]
[§ 3.1 信息报告]
（ 五）已经采取的措施；

[E6]
[§ 3.1 信息报告]
报告事故应当包括以下内容：

[E7]
[§ 3.1 信息报告]
当地政府安全监管部门

[E8]
[§ 3.1 信息报告]
限公司应急救援指挥部

[E9]
[§ 3.1 信息报告]
（ 六）其他应当报告的情况。

[E10]
[§ 3.1 信息报告]
报告流程如下：

[E11]
[§ 3.1 信息报告]
负有安全生产监督管理职责的有关部门

[E12]
[§ 3.1 信息报告]
（ 四）事故已经造成或者可能造成的伤亡人数（包括下落不明的人数） 和初步估计的直接经济损失；

[E13]
[§ 3.1 信息报告]
（4）事故造成严重不良社会影响的，应提高一个响应级别。

[E14]
[§ 3.1 信息报告]
发生生产
```

## real_69c6ef484cca74801cb63bb9_multi_hop_auto_0003 (multi_hop)

**Query:** 注浆施工的主要材料中，水玻璃的波美度要求是多少？在浆液拌制和泵送过程中，有哪些具体的质量控制措施以防止堵塞或保证均匀性？

**Doc:** `real_69c6ef484cca74801cb63bb9`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 492 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 13 | 8 |
| trajectory_steps | n/a | 7 |

### Gold node hits (new)

- `real_69c6ef484cca74801cb63bb9:L141` [MISS] retrieved=False in_text=False
- `real_69c6ef484cca74801cb63bb9:L167` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C19` kind=`collect` section=`real_69c6ef484cca74801cb63bb9:L99` scope=`None` depth=`0`
- reason: C19 contains water glass Be'me degree (25-30°). C25 details mixing and pumping quality controls to prevent blockage.
- collect_section_ids: ['real_69c6ef484cca74801cb63bb9:L99', 'real_69c6ef484cca74801cb63bb9:L133']
- collect added=2 hits=2 branch_selected=True collect_full=True
- legal_actions (53):
  - C1 | COLLECT | real_69c6ef484cca74801cb63bb9:L5 | 帷幕式注浆土体加固地基施工工法_2 | score=0.0619
  - D1 | DISPATCH | real_69c6ef484cca74801cb63bb9:L5 | 帷幕式注浆土体加固地基施工工法_2 | score=0.0619
  - C2 | COLLECT | real_69c6ef484cca74801cb63bb9:L7 | 传统注浆加固地基技术存在材料水泥水化反应慢、凝胶时间长、强度可靠性差 、串浆跑浆严重、加固影响区难以控制等缺陷。陕西建工第十一建设集团有限公司 根据深厚杂填土及地基处理的特性，采用帷幕式注浆+跳仓施工工艺解决了传统注浆 加固的强度可靠性差、串浆跑浆严重等问题，提高加固土体密实度，确保加固后地 面满足使用要求。 | score=0.0619
  - C3 | COLLECT | real_69c6ef484cca74801cb63bb9:L8 | 2.工法特点 | score=0.0606
  - D2 | DISPATCH | real_69c6ef484cca74801cb63bb9:L8 | 2.工法特点 | score=0.0606
  - C4 | COLLECT | real_69c6ef484cca74801cb63bb9:L11 | 2.2 施工便捷 | score=0.0606
  - D3 | DISPATCH | real_69c6ef484cca74801cb63bb9:L11 | 2.2 施工便捷 | score=0.0606
  - C5 | COLLECT | real_69c6ef484cca74801cb63bb9:L12 | 帷幕施工使用普通水泥和水玻璃，材料简单、来源广泛，不受地域限制，施工 机械轻巧便捷。 | score=0.0606
  - C6 | COLLECT | real_69c6ef484cca74801cb63bb9:L18 | 4.工艺原理 | score=0.0602
  - D4 | DISPATCH | real_69c6ef484cca74801cb63bb9:L18 | 4.工艺原理 | score=0.0602
  - C7 | COLLECT | real_69c6ef484cca74801cb63bb9:L19 | 本工法将待施工区划分为若干施工小仓，在每个小仓格四周环形布置帷幕式水 泥-水玻璃双液注浆孔，利用水泥-水玻璃双液浆快凝特点，在小仓格四周快速形成 封闭帷幕，有效避免串浆及跑浆现象。同时采用跳仓施工工艺，减少相邻区域变形 | score=0.0602
  - C8 | COLLECT | real_69c6ef484cca74801cb63bb9:L21 | 5.工艺流程及操作要点 | score=0.0609
  - D5 | DISPATCH | real_69c6ef484cca74801cb63bb9:L21 | 5.工艺流程及操作要点 | score=0.0609
  - C9 | COLLECT | real_69c6ef484cca74801cb63bb9:L22 | 5.1 工艺流程： | score=0.0609
  - D6 | DISPATCH | real_69c6ef484cca74801cb63bb9:L22 | 5.1 工艺流程： | score=0.0609
  - C10 | COLLECT | real_69c6ef484cca74801cb63bb9:L25 | 5.2.1 施工准备 | score=0.0609
- projection_chars: 3404

**Step 2** `nav_collect`  id=`C14` kind=`collect` section=`real_69c6ef484cca74801cb63bb9:L62` scope=`None` depth=`0`
- reason: Section C14 explicitly states the specific gravity (Bé度) of sodium silicate required for grouting.
- collect_section_ids: ['real_69c6ef484cca74801cb63bb9:L62']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (58):
  - C1 | COLLECT | real_69c6ef484cca74801cb63bb9:L5 | 帷幕式注浆土体加固地基施工工法_2 | score=0.0619
  - D1 | DISPATCH | real_69c6ef484cca74801cb63bb9:L5 | 帷幕式注浆土体加固地基施工工法_2 | score=0.0619
  - C2 | COLLECT | real_69c6ef484cca74801cb63bb9:L7 | 传统注浆加固地基技术存在材料水泥水化反应慢、凝胶时间长、强度可靠性差 、串浆跑浆严重、加固影响区难以控制等缺陷。陕西建工第十一建设集团有限公司 根据深厚杂填土及地基处理的特性，采用帷幕式注浆+跳仓施工工艺解决了传统注浆 加固的强度可靠性差、串浆跑浆严重等问题，提高加固土体密实度，确保加固后地 面满足使用要求。 | score=0.0619
  - C3 | COLLECT | real_69c6ef484cca74801cb63bb9:L8 | 2.工法特点 | score=0.0606
  - D2 | DISPATCH | real_69c6ef484cca74801cb63bb9:L8 | 2.工法特点 | score=0.0606
  - C4 | COLLECT | real_69c6ef484cca74801cb63bb9:L11 | 2.2 施工便捷 | score=0.0606
  - D3 | DISPATCH | real_69c6ef484cca74801cb63bb9:L11 | 2.2 施工便捷 | score=0.0606
  - C5 | COLLECT | real_69c6ef484cca74801cb63bb9:L12 | 帷幕施工使用普通水泥和水玻璃，材料简单、来源广泛，不受地域限制，施工 机械轻巧便捷。 | score=0.0606
  - C6 | COLLECT | real_69c6ef484cca74801cb63bb9:L18 | 4.工艺原理 | score=0.0602
  - D4 | DISPATCH | real_69c6ef484cca74801cb63bb9:L18 | 4.工艺原理 | score=0.0602
  - C7 | COLLECT | real_69c6ef484cca74801cb63bb9:L19 | 本工法将待施工区划分为若干施工小仓，在每个小仓格四周环形布置帷幕式水 泥-水玻璃双液注浆孔，利用水泥-水玻璃双液浆快凝特点，在小仓格四周快速形成 封闭帷幕，有效避免串浆及跑浆现象。同时采用跳仓施工工艺，减少相邻区域变形 | score=0.0602
  - C8 | COLLECT | real_69c6ef484cca74801cb63bb9:L21 | 5.工艺流程及操作要点 | score=0.0609
  - D5 | DISPATCH | real_69c6ef484cca74801cb63bb9:L21 | 5.工艺流程及操作要点 | score=0.0609
  - C9 | COLLECT | real_69c6ef484cca74801cb63bb9:L22 | 5.1 工艺流程： | score=0.0609
  - D6 | DISPATCH | real_69c6ef484cca74801cb63bb9:L22 | 5.1 工艺流程： | score=0.0609
  - C10 | COLLECT | real_69c6ef484cca74801cb63bb9:L25 | 5.2.1 施工准备 | score=0.0609
- projection_chars: 3464

**Step 3** `nav_collect`  id=`C13` kind=`collect` section=`real_69c6ef484cca74801cb63bb9:L60` scope=`None` depth=`0`
- reason: Section C13 contains the specific sodium silicate Beometer degree (25-30°) and mix ratio required.
- collect_section_ids: ['real_69c6ef484cca74801cb63bb9:L60']
- collect added=7 hits=7 branch_selected=True collect_full=True
- legal_actions (57):
  - C1 | COLLECT | real_69c6ef484cca74801cb63bb9:L5 | 帷幕式注浆土体加固地基施工工法_2 | score=0.0619
  - D1 | DISPATCH | real_69c6ef484cca74801cb63bb9:L5 | 帷幕式注浆土体加固地基施工工法_2 | score=0.0619
  - C2 | COLLECT | real_69c6ef484cca74801cb63bb9:L7 | 传统注浆加固地基技术存在材料水泥水化反应慢、凝胶时间长、强度可靠性差 、串浆跑浆严重、加固影响区难以控制等缺陷。陕西建工第十一建设集团有限公司 根据深厚杂填土及地基处理的特性，采用帷幕式注浆+跳仓施工工艺解决了传统注浆 加固的强度可靠性差、串浆跑浆严重等问题，提高加固土体密实度，确保加固后地 面满足使用要求。 | score=0.0619
  - C3 | COLLECT | real_69c6ef484cca74801cb63bb9:L8 | 2.工法特点 | score=0.0606
  - D2 | DISPATCH | real_69c6ef484cca74801cb63bb9:L8 | 2.工法特点 | score=0.0606
  - C4 | COLLECT | real_69c6ef484cca74801cb63bb9:L11 | 2.2 施工便捷 | score=0.0606
  - D3 | DISPATCH | real_69c6ef484cca74801cb63bb9:L11 | 2.2 施工便捷 | score=0.0606
  - C5 | COLLECT | real_69c6ef484cca74801cb63bb9:L12 | 帷幕施工使用普通水泥和水玻璃，材料简单、来源广泛，不受地域限制，施工 机械轻巧便捷。 | score=0.0606
  - C6 | COLLECT | real_69c6ef484cca74801cb63bb9:L18 | 4.工艺原理 | score=0.0602
  - D4 | DISPATCH | real_69c6ef484cca74801cb63bb9:L18 | 4.工艺原理 | score=0.0602
  - C7 | COLLECT | real_69c6ef484cca74801cb63bb9:L19 | 本工法将待施工区划分为若干施工小仓，在每个小仓格四周环形布置帷幕式水 泥-水玻璃双液注浆孔，利用水泥-水玻璃双液浆快凝特点，在小仓格四周快速形成 封闭帷幕，有效避免串浆及跑浆现象。同时采用跳仓施工工艺，减少相邻区域变形 | score=0.0602
  - C8 | COLLECT | real_69c6ef484cca74801cb63bb9:L21 | 5.工艺流程及操作要点 | score=0.0609
  - D5 | DISPATCH | real_69c6ef484cca74801cb63bb9:L21 | 5.工艺流程及操作要点 | score=0.0609
  - C9 | COLLECT | real_69c6ef484cca74801cb63bb9:L22 | 5.1 工艺流程： | score=0.0609
  - D6 | DISPATCH | real_69c6ef484cca74801cb63bb9:L22 | 5.1 工艺流程： | score=0.0609
  - C10 | COLLECT | real_69c6ef484cca74801cb63bb9:L25 | 5.2.1 施工准备 | score=0.0609
- projection_chars: 3391

**Step 4** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6ef484cca74801cb63bb9:L97` scope=`real_69c6ef484cca74801cb63bb9:L97` depth=`1`
- reason: Collect section 5.2.7 to find water glass specific gravity and grout quality control measures.
- collect_section_ids: ['real_69c6ef484cca74801cb63bb9:L97']
- collect added=13 hits=13 branch_selected=True collect_full=True
- legal_actions (14):
  - C1 | COLLECT | real_69c6ef484cca74801cb63bb9:L97 | 5.2.7 注浆 | score=0.0738
  - C2 | COLLECT | real_69c6ef484cca74801cb63bb9:L98 | - 1、水泥浆搅拌 | score=0.0365
  - C3 | COLLECT | real_69c6ef484cca74801cb63bb9:L100 | - 2、注浆泵试运转 | score=0.0336
  - C4 | COLLECT | real_69c6ef484cca74801cb63bb9:L101 | 确定注浆系统各部分连接无误后，开动注浆泵压水试验，检查注浆泵液压情况 ，系统管路有否漏浆，管路是否畅通。 | score=0.0487
  - C5 | COLLECT | real_69c6ef484cca74801cb63bb9:L102 | - 3、浆液注入 | score=0.0316
  - C6 | COLLECT | real_69c6ef484cca74801cb63bb9:L103 | 浆液的注入采用钻-灌一体机和空压机配合使用，帷幕注浆注浆压力0.6mpa，根 | score=0.0447
  - C7 | COLLECT | real_69c6ef484cca74801cb63bb9:L104 | 据地层及注浆压力进行调整，通过压力表观察注浆压力。注浆管每次上拔高度应为 33cm，为防止注浆管对后续施工产生危害，严禁将注浆管拔断掉落在阀管中。 | score=0.0571
  - C8 | COLLECT | real_69c6ef484cca74801cb63bb9:L105 | 图-8 注浆（1） | score=0.0297
  - C9 | COLLECT | real_69c6ef484cca74801cb63bb9:L106 | 图-9 注浆（2） | score=0.0291
  - C10 | COLLECT | real_69c6ef484cca74801cb63bb9:L107 | 4、注浆终孔标准 | score=0.0323
  - C11 | COLLECT | real_69c6ef484cca74801cb63bb9:L108 | 单根当达到以下条件之一，即可结束注浆： | score=0.0308
  - C12 | COLLECT | real_69c6ef484cca74801cb63bb9:L109 | ①注浆压力达到注浆终压； | score=0.0344
  - C13 | COLLECT | real_69c6ef484cca74801cb63bb9:L110 | ②注浆压力上升缓慢，当注浆量达到设计要求，并确认未发生跑浆或漏浆； ③循环达到下述条件可结束注浆：设计的注浆孔均满足单根结束标准结束注浆 ，无漏注现象。 | score=0.0512
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 1803

**Step 5** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c6ef484cca74801cb63bb9:L97` depth=`1`
- reason: Collected section L97 contains information on sodium silicate density and grout quality control measures.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 189

**Step 6** `nav_dispatch`  id=`D12` kind=`dispatch` section=`real_69c6ef484cca74801cb63bb9:L97` scope=`None` depth=`0`
- reason: Dispatch section 5.2.7 to find specific sodium silicate density and mixing/pumping quality control measures.
- dispatch_regions: ['real_69c6ef484cca74801cb63bb9:L97']
- child_reports=1 skipped=0
- legal_actions (53):
  - D1 | DISPATCH | real_69c6ef484cca74801cb63bb9:L5 | 帷幕式注浆土体加固地基施工工法_2 | score=0.0619
  - C1 | COLLECT | real_69c6ef484cca74801cb63bb9:L7 | 传统注浆加固地基技术存在材料水泥水化反应慢、凝胶时间长、强度可靠性差 、串浆跑浆严重、加固影响区难以控制等缺陷。陕西建工第十一建设集团有限公司 根据深厚杂填土及地基处理的特性，采用帷幕式注浆+跳仓施工工艺解决了传统注浆 加固的强度可靠性差、串浆跑浆严重等问题，提高加固土体密实度，确保加固后地 面满足使用要求。 | score=0.0619
  - C2 | COLLECT | real_69c6ef484cca74801cb63bb9:L8 | 2.工法特点 | score=0.0606
  - D2 | DISPATCH | real_69c6ef484cca74801cb63bb9:L8 | 2.工法特点 | score=0.0606
  - C3 | COLLECT | real_69c6ef484cca74801cb63bb9:L11 | 2.2 施工便捷 | score=0.0606
  - D3 | DISPATCH | real_69c6ef484cca74801cb63bb9:L11 | 2.2 施工便捷 | score=0.0606
  - C4 | COLLECT | real_69c6ef484cca74801cb63bb9:L12 | 帷幕施工使用普通水泥和水玻璃，材料简单、来源广泛，不受地域限制，施工 机械轻巧便捷。 | score=0.0606
  - C5 | COLLECT | real_69c6ef484cca74801cb63bb9:L18 | 4.工艺原理 | score=0.0602
  - D4 | DISPATCH | real_69c6ef484cca74801cb63bb9:L18 | 4.工艺原理 | score=0.0602
  - C6 | COLLECT | real_69c6ef484cca74801cb63bb9:L19 | 本工法将待施工区划分为若干施工小仓，在每个小仓格四周环形布置帷幕式水 泥-水玻璃双液注浆孔，利用水泥-水玻璃双液浆快凝特点，在小仓格四周快速形成 封闭帷幕，有效避免串浆及跑浆现象。同时采用跳仓施工工艺，减少相邻区域变形 | score=0.0602
  - D5 | DISPATCH | real_69c6ef484cca74801cb63bb9:L21 | 5.工艺流程及操作要点 | score=0.0609
  - D6 | DISPATCH | real_69c6ef484cca74801cb63bb9:L22 | 5.1 工艺流程： | score=0.0609
  - D7 | DISPATCH | real_69c6ef484cca74801cb63bb9:L25 | 5.2.1 施工准备 | score=0.0609
  - C7 | COLLECT | real_69c6ef484cca74801cb63bb9:L38 | 1、注浆压力的确定： | score=0.0560
  - D8 | DISPATCH | real_69c6ef484cca74801cb63bb9:L38 | 1、注浆压力的确定： | score=0.0560
  - C8 | COLLECT | real_69c6ef484cca74801cb63bb9:L48 | 0.11mpa，为保证加固区域浆液密实，3m注浆深度范围内注浆压力取值范围为0.4～ 0.6MPa。 | score=0.0560
- projection_chars: 3446

**Step 7** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence contains sodium silicate density (Be degrees) and grout quality control measures for mixing/pumping.
- legal_actions (52):
  - D1 | DISPATCH | real_69c6ef484cca74801cb63bb9:L5 | 帷幕式注浆土体加固地基施工工法_2 | score=0.0619
  - C1 | COLLECT | real_69c6ef484cca74801cb63bb9:L7 | 传统注浆加固地基技术存在材料水泥水化反应慢、凝胶时间长、强度可靠性差 、串浆跑浆严重、加固影响区难以控制等缺陷。陕西建工第十一建设集团有限公司 根据深厚杂填土及地基处理的特性，采用帷幕式注浆+跳仓施工工艺解决了传统注浆 加固的强度可靠性差、串浆跑浆严重等问题，提高加固土体密实度，确保加固后地 面满足使用要求。 | score=0.0619
  - C2 | COLLECT | real_69c6ef484cca74801cb63bb9:L8 | 2.工法特点 | score=0.0606
  - D2 | DISPATCH | real_69c6ef484cca74801cb63bb9:L8 | 2.工法特点 | score=0.0606
  - C3 | COLLECT | real_69c6ef484cca74801cb63bb9:L11 | 2.2 施工便捷 | score=0.0606
  - D3 | DISPATCH | real_69c6ef484cca74801cb63bb9:L11 | 2.2 施工便捷 | score=0.0606
  - C4 | COLLECT | real_69c6ef484cca74801cb63bb9:L12 | 帷幕施工使用普通水泥和水玻璃，材料简单、来源广泛，不受地域限制，施工 机械轻巧便捷。 | score=0.0606
  - C5 | COLLECT | real_69c6ef484cca74801cb63bb9:L18 | 4.工艺原理 | score=0.0602
  - D4 | DISPATCH | real_69c6ef484cca74801cb63bb9:L18 | 4.工艺原理 | score=0.0602
  - C6 | COLLECT | real_69c6ef484cca74801cb63bb9:L19 | 本工法将待施工区划分为若干施工小仓，在每个小仓格四周环形布置帷幕式水 泥-水玻璃双液注浆孔，利用水泥-水玻璃双液浆快凝特点，在小仓格四周快速形成 封闭帷幕，有效避免串浆及跑浆现象。同时采用跳仓施工工艺，减少相邻区域变形 | score=0.0602
  - D5 | DISPATCH | real_69c6ef484cca74801cb63bb9:L21 | 5.工艺流程及操作要点 | score=0.0609
  - D6 | DISPATCH | real_69c6ef484cca74801cb63bb9:L22 | 5.1 工艺流程： | score=0.0609
  - D7 | DISPATCH | real_69c6ef484cca74801cb63bb9:L25 | 5.2.1 施工准备 | score=0.0609
  - C7 | COLLECT | real_69c6ef484cca74801cb63bb9:L38 | 1、注浆压力的确定： | score=0.0560
  - D8 | DISPATCH | real_69c6ef484cca74801cb63bb9:L38 | 1、注浆压力的确定： | score=0.0560
  - C8 | COLLECT | real_69c6ef484cca74801cb63bb9:L48 | 0.11mpa，为保证加固区域浆液密实，3m注浆深度范围内注浆压力取值范围为0.4～ 0.6MPa。 | score=0.0560
- projection_chars: 3418

### Subagent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c6ef484cca74801cb63bb9:L97 (ok)
collected 13 branch node(s); explicit roots=['real_69c6ef484cca74801cb63bb9:L97']
collected: real_69c6ef484cca74801cb63bb9:L100, real_69c6ef484cca74801cb63bb9:L101, real_69c6ef484cca74801cb63bb9:L102, real_69c6ef484cca74801cb63bb9:L103, real_69c6ef484cca74801cb63bb9:L104, real_69c6ef484cca74801cb63bb9:L105, real_69c6ef484cca74801cb63bb9:L106, real_69c6ef484cca74801cb63bb9:L107, real_69c6ef484cca74801cb63bb9:L108, real_69c6ef484cca74801cb63bb9:L109, real_69c6ef484cca74801cb63bb9:L110, real_69c6ef484cca74801cb63bb9:L97, real_69c6ef484cca74801cb63bb9:L98
reason: Collected section L97 contains information on sodium silicate density and grout quality control measures.
---
=== End Investigate ===
```

### Evidence text (new)

```
[E1]
[§ 配合比：A：B=1：1，其中A液：水泥：水=0.8:1 B液：中性水玻璃，波美度]
式中：Q-浆液总用量L

[E2]
[§ 7.3 加强施工测量，确保钻杆竖直，位置满足规范要求。]
- 7.6 浆液拌制严格按配合比要求，并在拌浆现场悬挂配比牌。浆体必须经搅拌机充分 搅拌均匀，方可开始压浆，浆体在泵送前经筛网过滤。

[E3]
[§ 5.2.7 注浆]
  浆液的注入采用钻-灌一体机和空压机配合使用，帷幕注浆注浆压力0.6mpa，根
  据地层及注浆压力进行调整，通过压力表观察注浆压力。注浆管每次上拔高度应为 33cm，为防止注浆管对后续施工产生危害，严禁将注浆管拔断掉落在阀管中。
  注浆前，严格按照配方配料。其中帷幕采用AB液作为注浆材料，A液∶B液=1∶1 ，其中A液：水泥：水=0.8∶1；B液：中性水玻璃，水玻璃为波美度25°～30°；帷 幕中心区采用纯水泥浆作为注浆材料，注浆水泥采用强度等级为Po42.5R普通水泥。 施工用水采用自来水。浆液应搅拌均匀，随拌随注，不得长时间存放已拌好的浆液 。封闭泥浆用泵从钻杆自下而上压入孔内，不准从孔口到入。
```

### Evidence text (old)

```
[E1]
[§ 帷幕式注浆土体加固地基施工工法（终版）合并.pdf / 表7.2.1注浆检查项目要求及检验方法 / 9.环保措施 / 9.2 环境保护措施]
9.2.4 配置浆液用水玻璃为化工产品，严禁随意倾倒，需储存在专用的容器中，剩 余材料需退回，严禁私自倾倒在雨水或污水管网中。

[E2]
[§ 帷幕式注浆土体加固地基施工工法（终版）合并.pdf / 图-5 放线、标记点位 / 5.2.7 注浆]
注浆前，严格按照配方配料。其中帷幕采用AB液作为注浆材料，A液∶B液=1∶1 ，其中A液：水泥：水=0.8∶1；B液：中性水玻璃，水玻璃为波美度25°～30°；帷 幕中心区采用纯水泥浆作为注浆材料，注浆水泥采用强度等级为Po42.5R普通水泥。 施工用水采用自来水。浆液应搅拌均匀，随拌随注，不得长时间存放已拌好的浆液 。封闭泥浆用泵从钻杆自下而上压入孔内，不准从孔口到入。

[E3]
[§ 帷幕式注浆土体加固地基施工工法（终版）合并.pdf / 帷幕式注浆土体加固地基施工工法_2 / 5.工艺流程及操作要点 / 5.1 工艺流程： / 5.2.1 施工准备 / 3、注浆料配合比确定]

```

## real_69c6ef484cca74801cb63bb9_multi_hop_auto_0006 (multi_hop)

**Query:** 根据质量控制要求，注浆允许偏差及检验办法应符合哪张表的规定？该表中列出了哪四个关键检查项目？同时，在浆液拌制过程中有哪些具体的操作要求以确保质量？

**Doc:** `real_69c6ef484cca74801cb63bb9`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 482 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 12 | 13 |
| trajectory_steps | n/a | 8 |

### Gold node hits (new)

- `real_69c6ef484cca74801cb63bb9:L159` [MISS] retrieved=False in_text=False
- `real_69c6ef484cca74801cb63bb9:L162` [MISS] retrieved=False in_text=False
- `real_69c6ef484cca74801cb63bb9:L167` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C20` kind=`collect` section=`real_69c6ef484cca74801cb63bb9:L128` scope=`None` depth=`0`
- reason: Collect table 7.2.1 for deviation/inspection items and section 7.6 for slurry mixing requirements.
- collect_section_ids: ['real_69c6ef484cca74801cb63bb9:L128', 'real_69c6ef484cca74801cb63bb9:L129', 'real_69c6ef484cca74801cb63bb9:L133']
- collect added=34 hits=35 branch_selected=False collect_full=True
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

**Step 2** `nav_collect`  id=`C31` kind=`collect` section=`real_69c6ef484cca74801cb63bb9:L113` scope=`None` depth=`0`
- reason: Collect section 5.2.9 to find the table number for grouting deviation and inspection methods.
- collect_section_ids: ['real_69c6ef484cca74801cb63bb9:L113']
- collect added=2 hits=2 branch_selected=True collect_full=True
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

**Step 3** `nav_collect`  id=`C31` kind=`collect` section=`real_69c6ef484cca74801cb63bb9:L126` scope=`None` depth=`0`
- reason: Collect section C31 to find Table 7.2.1 and its four key inspection items for grouting deviation.
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

**Step 4** `nav_collect`  id=`C5` kind=`collect` section=`real_69c6ef484cca74801cb63bb9:L21` scope=`None` depth=`0`
- reason: Collect section 5 to find the table for grouting deviation and inspection methods, plus slurry mixing requirements.
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

**Step 5** `nav_collect`  id=`C34` kind=`collect` section=`real_69c6ef484cca74801cb63bb9:L123` scope=`None` depth=`0`
- reason: Collect section 7 Quality Control to find Table 7.2.1 and slurry mixing requirements.
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

**Step 6** `nav_collect`  id=`C15` kind=`collect` section=`real_69c6ef484cca74801cb63bb9:L99` scope=`None` depth=`0`
- reason: Collects浆液拌制操作要求 and confirms Table 7.2.1 reference for deviation limits.
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

**Step 7** `nav_collect`  id=`C14` kind=`collect` section=`real_69c6ef484cca74801cb63bb9:L97` scope=`None` depth=`0`
- reason: Collect section 5.2.7 to find the table for allowable deviations and inspection methods, and浆液拌制 requirements.
- collect_section_ids: ['real_69c6ef484cca74801cb63bb9:L97']
- collect added=13 hits=13 branch_selected=True collect_full=True
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
- projection_chars: 3208

**Step 8** `nav_collect`  id=`C2` kind=`collect` section=`real_69c6ef484cca74801cb63bb9:L2` scope=`None` depth=`0`
- reason: Need to collect section 7.2 for deviation table and section 7.3 for slurry mixing requirements.
- collect_section_ids: ['real_69c6ef484cca74801cb63bb9:L2', 'real_69c6ef484cca74801cb63bb9:L8', 'real_69c6ef484cca74801cb63bb9:L9']
- collect added=8 hits=8 branch_selected=True collect_full=True
- legal_actions (39):
  - C1 | COLLECT | real_69c6ef484cca74801cb63bb9:L1 | 帷幕式注浆土体加固地基施工工法 | score=0.0288
  - C2 | COLLECT | real_69c6ef484cca74801cb63bb9:L2 | **陕西建工第十一建设集团有限公司** | score=0.0256
  - C3 | COLLECT | real_69c6ef484cca74801cb63bb9:L3 | 2020-11-06实施 | score=0.0256
  - C4 | COLLECT | real_69c6ef484cca74801cb63bb9:L7 | 传统注浆加固地基技术存在材料水泥水化反应慢、凝胶时间长、强度可靠性差 、串浆跑浆严重、加固影响区难以控制等缺陷。陕西建工第十一建设集团有限公司 根据深厚杂填土及地基处理的特性，采用帷幕式注浆+跳仓施工工艺解决了传统注浆 加固的强度可靠性差、串浆跑浆严重等问题，提高加固土体密实度，确保加固后地 面满足使用要求。 | score=0.0574
  - C5 | COLLECT | real_69c6ef484cca74801cb63bb9:L8 | 2.工法特点 | score=0.0353
  - C6 | COLLECT | real_69c6ef484cca74801cb63bb9:L9 | 2.1 帷幕内部施工，影响范围小 | score=0.0257
  - C7 | COLLECT | real_69c6ef484cca74801cb63bb9:L10 | 本工法将施工区域划分成若干小仓，形成帷幕。作业影响范围小，不影响其余 部位使用。 | score=0.0257
  - C8 | COLLECT | real_69c6ef484cca74801cb63bb9:L11 | 2.2 施工便捷 | score=0.0253
  - C9 | COLLECT | real_69c6ef484cca74801cb63bb9:L12 | 帷幕施工使用普通水泥和水玻璃，材料简单、来源广泛，不受地域限制，施工 机械轻巧便捷。 | score=0.0253
  - C10 | COLLECT | real_69c6ef484cca74801cb63bb9:L13 | 2.3 跳仓施工 | score=0.0353
  - C11 | COLLECT | real_69c6ef484cca74801cb63bb9:L14 | 采用跳仓施工，隔孔注入，避免相邻分仓的注浆互相影响，保证施工质量。 2.4 适用性强 | score=0.0353
  - C12 | COLLECT | real_69c6ef484cca74801cb63bb9:L15 | 可用于已投入使用、无法停工停产、不能进行开挖处理或大型施工机械无法施 工的地面下土体加固施工。 | score=0.0271
  - C13 | COLLECT | real_69c6ef484cca74801cb63bb9:L16 | 3.适用范围 | score=0.0272
  - C14 | COLLECT | real_69c6ef484cca74801cb63bb9:L17 | 本工法适用于深厚杂填土地区建筑地基加固及地基土土体孔隙较大等环境地面 下土体加固的施工。 | score=0.0272
  - C15 | COLLECT | real_69c6ef484cca74801cb63bb9:L18 | 4.工艺原理 | score=0.0450
  - C16 | COLLECT | real_69c6ef484cca74801cb63bb9:L19 | 本工法将待施工区划分为若干施工小仓，在每个小仓格四周环形布置帷幕式水 泥-水玻璃双液注浆孔，利用水泥-水玻璃双液浆快凝特点，在小仓格四周快速形成 封闭帷幕，有效避免串浆及跑浆现象。同时采用跳仓施工工艺，减少相邻区域变形 | score=0.0450
- projection_chars: 3100

### Evidence text (new)

```
[E1]
[§ 7.3 加强施工测量，确保钻杆竖直，位置满足规范要求。]
  - 7.4 注浆开始前应充分作好准备工作，包括机械器具、仪表、管路、注浆材料、水和 电等的检查及必要的试验，注浆一经开始即应连续进行，力求避免中断。
  - 7.5 在钻杆钻进过程中，根据不同土质和覆土厚度，结合监测信息，及时调整推力、 推进速度和注浆量的相互关系，合理控制钻进速度，保证土压平衡。
  - 7.6 浆液拌制严格按配合比要求，并在拌浆现场悬挂配比牌。浆体必须经搅拌机充分 搅拌均匀，方可开始压浆，浆体在泵送前经筛网过滤。
  - 7.7 施工过程控制压力，及时观察注浆终压值，防止因压力过大导致浆液外渗。
  - 7.8 注浆结束后及时封孔，防止相邻注浆孔注浆时引起漏浆。
  - 7.9 加强注浆施工人员的培训工作，提高注浆机械人员的操作水平。
  - 7.10 做好注浆设备的维修保养和注浆材料供应工作，定时对注浆管路及设备进行清洗
  - ，保证注浆作业连续不间断的进行。

[E2]
[§ 7.2 主要控制措施]
注浆允许偏差及检验办法应符合表7.2.1的规定。
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

## latest_clean_niche_0036 (niche_fact)

**Query:** 根据《附件》中“正文”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c6096dd4242eda8c47c5ed`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 71 | 360 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 4 | 15 |
| trajectory_steps | n/a | 6 |

### Gold node hits (new)

- `real_69c6096dd4242eda8c47c5ed:L7` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6096dd4242eda8c47c5ed:L1` scope=`None` depth=`0`
- reason: Collect Attachment 1 to find the specific regulations or facts in its main text.
- collect_section_ids: ['real_69c6096dd4242eda8c47c5ed:L1']
- collect added=4 hits=4 branch_selected=True collect_full=True
- legal_actions (19):
  - C1 | COLLECT | real_69c6096dd4242eda8c47c5ed:L1 | 附件1 | score=0.0695
  - D1 | DISPATCH | real_69c6096dd4242eda8c47c5ed:L1 | 附件1 | score=0.0695
  - C2 | COLLECT | real_69c6096dd4242eda8c47c5ed:L2 | 陕西建工第十一建设集团有限公司 | score=0.0663
  - C3 | COLLECT | real_69c6096dd4242eda8c47c5ed:L3 | 车辆租赁审批单 | score=0.0676
  - C4 | COLLECT | real_69c6096dd4242eda8c47c5ed:L4 | 申请单位（盖章）： | score=0.0695
  - C5 | COLLECT | real_69c6096dd4242eda8c47c5ed:L5 | 填报人： 填报日期： 年月日 | score=0.0688
  - C6 | COLLECT | real_69c6096dd4242eda8c47c5ed:L6 | 附件2 | score=0.0708
  - D2 | DISPATCH | real_69c6096dd4242eda8c47c5ed:L6 | 附件2 | score=0.0708
  - C7 | COLLECT | real_69c6096dd4242eda8c47c5ed:L7 | 陕西建工第十一建设集团有限公司的公务用车申请单，包含车型、车号、司机、用车单位、联系人、出车时间、路线及里程等详细信息，并设有满意度调查和签字确认栏。 | score=0.0708
  - C8 | COLLECT | real_69c6096dd4242eda8c47c5ed:L8 | 服务电话:029-33215789 | score=0.0352
  - C9 | COLLECT | real_69c6096dd4242eda8c47c5ed:L9 | 陕西建工第十一建设集团有限公司的车辆保养/维修申请单，包含申请人、车牌号、送修及取车日期等信息。表格分为保养和维修两部分，分别记录项目、金额及备注，并规定了不同金额的审批流程。 | score=0.0704
  - C10 | COLLECT | real_69c6096dd4242eda8c47c5ed:L10 | 附件4 | score=0.0689
  - D3 | DISPATCH | real_69c6096dd4242eda8c47c5ed:L10 | 附件4 | score=0.0689
  - C11 | COLLECT | real_69c6096dd4242eda8c47c5ed:L11 | 陕西建工第十一建设集团有限公司 | score=0.0688
  - C12 | COLLECT | real_69c6096dd4242eda8c47c5ed:L12 | 车辆加油记录单 | score=0.0689
  - C13 | COLLECT | real_69c6096dd4242eda8c47c5ed:L13 | 附件5 | score=0.0690
- projection_chars: 1181

**Step 2** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6096dd4242eda8c47c5ed:L6` scope=`None` depth=`0`
- reason: Collect '附件2' to find explicit regulations or facts regarding official vehicle usage as requested.
- collect_section_ids: ['real_69c6096dd4242eda8c47c5ed:L6']
- collect added=3 hits=3 branch_selected=True collect_full=True
- legal_actions (14):
  - C1 | COLLECT | real_69c6096dd4242eda8c47c5ed:L6 | 附件2 | score=0.0708
  - D1 | DISPATCH | real_69c6096dd4242eda8c47c5ed:L6 | 附件2 | score=0.0708
  - C2 | COLLECT | real_69c6096dd4242eda8c47c5ed:L7 | 陕西建工第十一建设集团有限公司的公务用车申请单，包含车型、车号、司机、用车单位、联系人、出车时间、路线及里程等详细信息，并设有满意度调查和签字确认栏。 | score=0.0708
  - C3 | COLLECT | real_69c6096dd4242eda8c47c5ed:L8 | 服务电话:029-33215789 | score=0.0352
  - C4 | COLLECT | real_69c6096dd4242eda8c47c5ed:L9 | 陕西建工第十一建设集团有限公司的车辆保养/维修申请单，包含申请人、车牌号、送修及取车日期等信息。表格分为保养和维修两部分，分别记录项目、金额及备注，并规定了不同金额的审批流程。 | score=0.0704
  - C5 | COLLECT | real_69c6096dd4242eda8c47c5ed:L10 | 附件4 | score=0.0689
  - D2 | DISPATCH | real_69c6096dd4242eda8c47c5ed:L10 | 附件4 | score=0.0689
  - C6 | COLLECT | real_69c6096dd4242eda8c47c5ed:L11 | 陕西建工第十一建设集团有限公司 | score=0.0688
  - C7 | COLLECT | real_69c6096dd4242eda8c47c5ed:L12 | 车辆加油记录单 | score=0.0689
  - C8 | COLLECT | real_69c6096dd4242eda8c47c5ed:L13 | 附件5 | score=0.0690
  - D3 | DISPATCH | real_69c6096dd4242eda8c47c5ed:L13 | 附件5 | score=0.0690
  - C9 | COLLECT | real_69c6096dd4242eda8c47c5ed:L14 | 陕西建工第十一建设集团有限公司 | score=0.0682
  - C10 | COLLECT | real_69c6096dd4242eda8c47c5ed:L15 | 公务车辆节假日封存记录 | score=0.0690
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 912

**Step 3** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6096dd4242eda8c47c5ed:L10` scope=`None` depth=`0`
- reason: Collect '附件4' to find regulations/facts in the main text as requested.
- collect_section_ids: ['real_69c6096dd4242eda8c47c5ed:L10']
- collect added=2 hits=2 branch_selected=True collect_full=True
- legal_actions (9):
  - C1 | COLLECT | real_69c6096dd4242eda8c47c5ed:L10 | 附件4 | score=0.0689
  - D1 | DISPATCH | real_69c6096dd4242eda8c47c5ed:L10 | 附件4 | score=0.0689
  - C2 | COLLECT | real_69c6096dd4242eda8c47c5ed:L11 | 陕西建工第十一建设集团有限公司 | score=0.0688
  - C3 | COLLECT | real_69c6096dd4242eda8c47c5ed:L12 | 车辆加油记录单 | score=0.0689
  - C4 | COLLECT | real_69c6096dd4242eda8c47c5ed:L13 | 附件5 | score=0.0690
  - D2 | DISPATCH | real_69c6096dd4242eda8c47c5ed:L13 | 附件5 | score=0.0690
  - C5 | COLLECT | real_69c6096dd4242eda8c47c5ed:L14 | 陕西建工第十一建设集团有限公司 | score=0.0682
  - C6 | COLLECT | real_69c6096dd4242eda8c47c5ed:L15 | 公务车辆节假日封存记录 | score=0.0690
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 527

**Step 4** `nav_collect`  id=`C3` kind=`collect` section=`real_69c6096dd4242eda8c47c5ed:L15` scope=`None` depth=`0`
- reason: The user asks for regulations/facts in '正文' (main text). N3 is a leaf node labeled [Hit] under '附件5', likely containing the specific record mentioned.
- collect_section_ids: ['real_69c6096dd4242eda8c47c5ed:L15']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (5):
  - C1 | COLLECT | real_69c6096dd4242eda8c47c5ed:L13 | 附件5 | score=0.0690
  - D1 | DISPATCH | real_69c6096dd4242eda8c47c5ed:L13 | 附件5 | score=0.0690
  - C2 | COLLECT | real_69c6096dd4242eda8c47c5ed:L14 | 陕西建工第十一建设集团有限公司 | score=0.0682
  - C3 | COLLECT | real_69c6096dd4242eda8c47c5ed:L15 | 公务车辆节假日封存记录 | score=0.0690
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 348

**Step 5** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6096dd4242eda8c47c5ed:L13` scope=`None` depth=`0`
- reason: Collect §附件5 to find specific regulations or facts as requested.
- collect_section_ids: ['real_69c6096dd4242eda8c47c5ed:L13']
- collect added=2 hits=2 branch_selected=True collect_full=True
- legal_actions (4):
  - C1 | COLLECT | real_69c6096dd4242eda8c47c5ed:L13 | 附件5 | score=0.0690
  - D1 | DISPATCH | real_69c6096dd4242eda8c47c5ed:L13 | 附件5 | score=0.0690
  - C2 | COLLECT | real_69c6096dd4242eda8c47c5ed:L14 | 陕西建工第十一建设集团有限公司 | score=0.0682
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 285

**Step 6** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence collected covers all relevant sections of the 'Main Text' in the attachment, detailing vehicle management regulations and forms.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 171

### Evidence text (new)

```
[E1]
[§ 附件2]
  陕西建工第十一建设集团有限公司的公务用车申请单，包含车型、车号、司机、用车单位、联系人、出车时间、路线及里程等详细信息，并设有满意度调查和签字确认栏。
  服务电话:029-33215789
  陕西建工第十一建设集团有限公司的车辆保养/维修申请单，包含申请人、车牌号、送修及取车日期等信息。表格分为保养和维修两部分，分别记录项目、金额及备注，并规定了不同金额的审批流程。

[E2]
[§ 附件4]
  陕西建工第十一建设集团有限公司
  车辆加油记录单

[E3]
[§ 附件5]
  陕西建工第十一建设集团有限公司
  公务车辆节假日封存记录

[E4]
[§ 附件1]
  陕西建工第十一建设集团有限公司
  车辆租赁审批单
  申请单位（盖章）：
  填报人： 填报日期： 年月日
```

### Evidence text (old)

```
[E1]
申请单位（盖章）：

[E2]
车辆租赁审批单

[E3]
填报人： 填报日期： 年月日

[E4]
陕西建工第十一建设集团有限公司
```

## latest_clean_niche_0068 (niche_fact)

**Query:** 根据《陕西建工第十一建设集团有限公司印章管理办法（2020版）》中“陕西建工第十一建设集团有限公司印章管理办法（2020版）.docx”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60971d4242eda8c47c605`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 479 | 465 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 8 | 6 |
| trajectory_steps | n/a | 4 |

### Gold node hits (new)

- `real_69c60971d4242eda8c47c605:L2` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60971d4242eda8c47c605:L1` scope=`None` depth=`0`
- reason: Collect Chapter 1 to retrieve the full text of the regulations as requested.
- collect_section_ids: ['real_69c60971d4242eda8c47c605:L1']
- collect added=5 hits=5 branch_selected=True collect_full=True
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

**Step 2** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60971d4242eda8c47c605:L7` scope=`None` depth=`0`
- reason: Collect Chapter 2 to retrieve specific regulations on seal carving and activation.
- collect_section_ids: ['real_69c60971d4242eda8c47c605:L7']
- collect added=17 hits=17 branch_selected=True collect_full=True
- legal_actions (44):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0641
  - D1 | DISPATCH | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0641
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L9 | （一）集团公司机关各部门章，二级单位章，由集团办公室根据集团公司或上级有关部门批准成立该机构的文件制发。 | score=0.0641
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L19 | 确因工作需要刻制印章的，由用印单位或部门提出申请，详细说明印章的名称、用途、式样和规格，报集团公司主要领导批准后由办公室制发。 | score=0.0634
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L21 | 第七条项目部印章在使用前，项目部应负责将集团公司办公室出具的印章启用文件报送建设单位、监理单位等相关方，以便业务往来确认。并在文件送达后一周内将回执返回集团公司办公室留存。 | score=0.0607
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L23 | 第九条发生印章遗失，印章责任管理单位应在24小时内向集团公司和当地公安机关报告；在3个工作日内在省级以上报刊办理遗失声明，并向集团公司申请出具告知函，及时通知相关单位。印章遗失处理流程见附件。 | score=0.0534
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L24 | 印章责任管理单位应将印章遗失报告、遗失声明、告知函回复等相关资料在一月内报集团公司办公室，以备查考。 | score=0.0501
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0710
  - D2 | DISPATCH | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0710
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0710
  - D3 | DISPATCH | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0710
  - C9 | COLLECT | real_69c60971d4242eda8c47c605:L42 | （六）集团公司法人明确授权或者委托对外使用印章的事项。 | score=0.0710
  - C10 | COLLECT | real_69c60971d4242eda8c47c605:L49 | 第十二条 项目部印章使用范围 | score=0.0702
  - D4 | DISPATCH | real_69c60971d4242eda8c47c605:L49 | 第十二条 项目部印章使用范围 | score=0.0702
  - C11 | COLLECT | real_69c60971d4242eda8c47c605:L56 | （七）项目印章应在项目负责人审批后用印，用印内容不得违背施工合同要件内容。 | score=0.0521
  - C12 | COLLECT | real_69c60971d4242eda8c47c605:L57 | 第十四条集团公司法人章之外的其它印章，是公司法人授予的内部职能性标示。除公司法人授权或委托外，严禁用于签订合同、协议、借贷、担保、工程决算书等具有设定义务的实体行为。 | score=0.0702
- projection_chars: 3548

**Step 3** `nav_collect`  id=`C3` kind=`collect` section=`real_69c60971d4242eda8c47c605:L42` scope=`None` depth=`0`
- reason: Collect specific rules on seal usage scope, management responsibilities, blank stamping prohibition, and penalties for forgery.
- collect_section_ids: ['real_69c60971d4242eda8c47c605:L42', 'real_69c60971d4242eda8c47c605:L56', 'real_69c60971d4242eda8c47c605:L57', 'real_69c60971d4242eda8c47c605:L74', 'real_69c60971d4242eda8c47c605:L75', 'real_69c60971d4242eda8c47c605:L89', 'real_69c60971d4242eda8c47c605:L111', 'real_69c60971d4242eda8c47c605:L112']
- collect added=8 hits=8 branch_selected=True collect_full=True
- legal_actions (45):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0710
  - D1 | DISPATCH | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0710
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0710
  - D2 | DISPATCH | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0710
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L42 | （六）集团公司法人明确授权或者委托对外使用印章的事项。 | score=0.0710
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L49 | 第十二条 项目部印章使用范围 | score=0.0702
  - D3 | DISPATCH | real_69c60971d4242eda8c47c605:L49 | 第十二条 项目部印章使用范围 | score=0.0702
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L56 | （七）项目印章应在项目负责人审批后用印，用印内容不得违背施工合同要件内容。 | score=0.0521
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L57 | 第十四条集团公司法人章之外的其它印章，是公司法人授予的内部职能性标示。除公司法人授权或委托外，严禁用于签订合同、协议、借贷、担保、工程决算书等具有设定义务的实体行为。 | score=0.0702
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L58 | 第四章 用印审批程序 | score=0.0587
  - D4 | DISPATCH | real_69c60971d4242eda8c47c605:L58 | 第四章 用印审批程序 | score=0.0587
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L61 | （一）集团公司经营工作用印，按照《集团公司经营管理规定》的规定办理。 | score=0.0525
  - C9 | COLLECT | real_69c60971d4242eda8c47c605:L67 | （七）颁发证书、奖状等需加盖集团公司印章或钢印的，根据相关表彰文件用印，无文件由经办部门发起审批，经部门负责人、分管领导审批，办公室登记后用印。 | score=0.0587
  - C10 | COLLECT | real_69c60971d4242eda8c47c605:L69 | 第十六条二级单位应参照集团公司法人章审批程序，自行建立合理规范的用印审批程序。 | score=0.0451
  - C11 | COLLECT | real_69c60971d4242eda8c47c605:L73 | 第五章 印章管理 | score=0.0602
  - D5 | DISPATCH | real_69c60971d4242eda8c47c605:L73 | 第五章 印章管理 | score=0.0602
- projection_chars: 3547

**Step 4** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Collected evidence covers all key regulations on seal usage, management, and accountability as requested.
- legal_actions (49):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0710
  - D1 | DISPATCH | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0710
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0710
  - D2 | DISPATCH | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0710
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L37 | （一）以本单位、部门名义向集团公司提出的工作计划、总结、统计报表等； | score=0.0412
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L41 | （五）集团公司内部专业分包合同签订； | score=0.0414
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L43 | 第十一条 集团公司财务专用章使用范围 | score=0.0428
  - D3 | DISPATCH | real_69c60971d4242eda8c47c605:L43 | 第十一条 集团公司财务专用章使用范围 | score=0.0428
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L45 | （二）对外收取、支付款项时所用票据的确认盖章； | score=0.0428
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L49 | 第十二条 项目部印章使用范围 | score=0.0702
  - D4 | DISPATCH | real_69c60971d4242eda8c47c605:L49 | 第十二条 项目部印章使用范围 | score=0.0702
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L51 | （二）以项目部名义向建设单位、监理单位等出具的有关技术质量和安全生产的业务函件、工作联系单； | score=0.0420
  - C9 | COLLECT | real_69c60971d4242eda8c47c605:L58 | 第四章 用印审批程序 | score=0.0587
  - D5 | DISPATCH | real_69c60971d4242eda8c47c605:L58 | 第四章 用印审批程序 | score=0.0587
  - C10 | COLLECT | real_69c60971d4242eda8c47c605:L61 | （一）集团公司经营工作用印，按照《集团公司经营管理规定》的规定办理。 | score=0.0525
  - C11 | COLLECT | real_69c60971d4242eda8c47c605:L67 | （七）颁发证书、奖状等需加盖集团公司印章或钢印的，根据相关表彰文件用印，无文件由经办部门发起审批，经部门负责人、分管领导审批，办公室登记后用印。 | score=0.0587
- projection_chars: 3366

### Evidence text (new)

```
[E1]
[§ 第一章 总则]
  第一条为规范集团公司及下属单位印章管理工作，有效防范风险，保障经营管理活动的有序开展，特制定本办法。
  第二条本办法所称集团公司印章包括：集团公司法人章、财务专用章、机关部门章，集团公司下属单位印章、项目部章等行使公司职权的法定名称章；集团公司法定代表人章、总会计师章等代表公司实施职务行为的印章。
  第三条印章所刊名称，应为集团公司文件规定的法定名称。印章文字一般应使用宋体简体字。
  集团公司法人章为圆形，直径为4.2CM，中央刊五角星，上环刊单位名称自左向右环排；部门章一律为圆形，直径为3.8CM，上刊集团名称自左向右环排，中央刊五角星，部门名称放在星下方作横排；二级单位公章一律为圆形，直径4.0CM，集团名称自左而右环排，二级单位名称放在星下方作横排。项目部章一律为圆形，直径4.0CM，集团名称和工程名称依次自左而右环排，“工程项目部”字样放在星下方作横排，名称应严格按“陕建十一建集团+工程名称+工程项目部”格式确定。
  印章名称、规格、标准等由集团公司办公室统一审核。
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

## latest_clean_niche_0160 (niche_fact)

**Query:** 根据《陕西建工第十一建设集团有限公司印章管理办法（2020版）》中“第七章 责任追究”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60971d4242eda8c47c605`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 479 | 492 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 5 | 5 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60971d4242eda8c47c605:L111` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C21` kind=`collect` section=`real_69c60971d4242eda8c47c605:L110` scope=`None` depth=`0`
- reason: Collect Chapter 7 'Accountability' to extract specific regulations on penalties and responsibilities.
- collect_section_ids: ['real_69c60971d4242eda8c47c605:L110']
- collect added=7 hits=7 branch_selected=True collect_full=True
- legal_actions (40):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0644
  - D1 | DISPATCH | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0644
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L21 | 第七条项目部印章在使用前，项目部应负责将集团公司办公室出具的印章启用文件报送建设单位、监理单位等相关方，以便业务往来确认。并在文件送达后一周内将回执返回集团公司办公室留存。 | score=0.0644
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L23 | 第九条发生印章遗失，印章责任管理单位应在24小时内向集团公司和当地公安机关报告；在3个工作日内在省级以上报刊办理遗失声明，并向集团公司申请出具告知函，及时通知相关单位。印章遗失处理流程见附件。 | score=0.0615
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L24 | 印章责任管理单位应将印章遗失报告、遗失声明、告知函回复等相关资料在一月内报集团公司办公室，以备查考。 | score=0.0613
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0615
  - D2 | DISPATCH | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0615
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0615
  - D3 | DISPATCH | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0615
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L42 | （六）集团公司法人明确授权或者委托对外使用印章的事项。 | score=0.0615
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L49 | 第十二条 项目部印章使用范围 | score=0.0606
  - D4 | DISPATCH | real_69c60971d4242eda8c47c605:L49 | 第十二条 项目部印章使用范围 | score=0.0606
  - C9 | COLLECT | real_69c60971d4242eda8c47c605:L56 | （七）项目印章应在项目负责人审批后用印，用印内容不得违背施工合同要件内容。 | score=0.0573
  - C10 | COLLECT | real_69c60971d4242eda8c47c605:L57 | 第十四条集团公司法人章之外的其它印章，是公司法人授予的内部职能性标示。除公司法人授权或委托外，严禁用于签订合同、协议、借贷、担保、工程决算书等具有设定义务的实体行为。 | score=0.0606
  - C11 | COLLECT | real_69c60971d4242eda8c47c605:L58 | 第四章 用印审批程序 | score=0.0602
  - D5 | DISPATCH | real_69c60971d4242eda8c47c605:L58 | 第四章 用印审批程序 | score=0.0602
- projection_chars: 3444

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Assembled evidence G1 contains all relevant content from Chapter 7 regarding accountability measures.
- legal_actions (46):
  - C1 | COLLECT | real_69c60971d4242eda8c47c605:L1 | 第一章 总则 | score=0.0527
  - D1 | DISPATCH | real_69c60971d4242eda8c47c605:L1 | 第一章 总则 | score=0.0527
  - C2 | COLLECT | real_69c60971d4242eda8c47c605:L2 | 第一条为规范集团公司及下属单位印章管理工作，有效防范风险，保障经营管理活动的有序开展，特制定本办法。 | score=0.0527
  - C3 | COLLECT | real_69c60971d4242eda8c47c605:L3 | 第二条本办法所称集团公司印章包括：集团公司法人章、财务专用章、机关部门章，集团公司下属单位印章、项目部章等行使公司职权的法定名称章；集团公司法定代表人章、总会计师章等代表公司实施职务行为的印章。 | score=0.0501
  - C4 | COLLECT | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0644
  - D2 | DISPATCH | real_69c60971d4242eda8c47c605:L7 | 第二章	印章的刻制与启用 | score=0.0644
  - C5 | COLLECT | real_69c60971d4242eda8c47c605:L9 | （一）集团公司机关各部门章，二级单位章，由集团办公室根据集团公司或上级有关部门批准成立该机构的文件制发。 | score=0.0544
  - C6 | COLLECT | real_69c60971d4242eda8c47c605:L19 | 确因工作需要刻制印章的，由用印单位或部门提出申请，详细说明印章的名称、用途、式样和规格，报集团公司主要领导批准后由办公室制发。 | score=0.0518
  - C7 | COLLECT | real_69c60971d4242eda8c47c605:L21 | 第七条项目部印章在使用前，项目部应负责将集团公司办公室出具的印章启用文件报送建设单位、监理单位等相关方，以便业务往来确认。并在文件送达后一周内将回执返回集团公司办公室留存。 | score=0.0644
  - C8 | COLLECT | real_69c60971d4242eda8c47c605:L23 | 第九条发生印章遗失，印章责任管理单位应在24小时内向集团公司和当地公安机关报告；在3个工作日内在省级以上报刊办理遗失声明，并向集团公司申请出具告知函，及时通知相关单位。印章遗失处理流程见附件。 | score=0.0615
  - C9 | COLLECT | real_69c60971d4242eda8c47c605:L24 | 印章责任管理单位应将印章遗失报告、遗失声明、告知函回复等相关资料在一月内报集团公司办公室，以备查考。 | score=0.0613
  - C10 | COLLECT | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0615
  - D3 | DISPATCH | real_69c60971d4242eda8c47c605:L25 | 第三章	印章的使用范围 | score=0.0615
  - C11 | COLLECT | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0615
  - D4 | DISPATCH | real_69c60971d4242eda8c47c605:L36 | 第十条 机关各部门章、二级单位印章使用范围 | score=0.0615
  - C12 | COLLECT | real_69c60971d4242eda8c47c605:L42 | （六）集团公司法人明确授权或者委托对外使用印章的事项。 | score=0.0615
- projection_chars: 3517

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
[§ 第七章	责任追究]
第四十二条印章责任管理单位、监管部门未认真履行印章管理、检查监督、封口管理等职责，发生伪造、私刻印章等情节严重，或造成经济损失及不良影响的，对管理责任人按集团公司《管理人员责任追究暂行规定》追究相关责任。

[E2]
[§ 第七章	责任追究]
第四十一条有印章使用审批权限的其他管理人员，超越审批权限使用印章，造成经济损失及不良后果的，由集团公司党委组织部、监察审计部按《管理人员责任追究暂行规定》追究其相关责任。

[E3]
[§ 第七章	责任追究]
第三十九条印章第一管理责任人违反本办法相关条款，由上级主管单位予以通报批评，责令整改，并不得评选或考核为A级；造成经济损失及不良后果的，将追究其相关管理责任。

[E4]
[§ 第七章	责任追究]
第三十六条伪造、私刻集团公司机关部门章、二级单位章、项目部印章的，一经发现，对伪造、私刻责任方（单位、项目部、个人）处于6万元罚款，并由集团公司组织调查组进行调查，根据情节轻重追究相关责任人的行政、经济责任，通报批评，依法追偿损失。涉嫌犯罪的，报请司法机关依法进行处理。
```

## latest_clean_niche_0175 (niche_fact)

**Query:** 根据《附件_安全管理规定（2020版）》中“第一章 安全教育培训规定”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 490 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 12 | 11 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L5` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60974d4242eda8c47c615:L3` scope=`None` depth=`0`
- reason: Collect Chapter 1 to retrieve all safety education and training regulations as requested.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L3']
- collect added=27 hits=27 branch_selected=True collect_full=True
- legal_actions (55):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0715
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0715
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L4 | 1.1 总则 | score=0.0600
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L4 | 1.1 总则 | score=0.0600
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L5 | 1.1.1安全教育和培训的类型应包括三级安全教育、岗前教育、日常教育、年度继续教育，以及各类特种作业人员证书的初审、复审培训（附表1.1.1：安全教育记录）。 | score=0.0600
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L6 | 1.1.2集团公司各级安全教育培训计划、安全教育培训工作按集团公司教育培训制度执行。 | score=0.0574
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0715
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0715
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0715
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0715
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0715
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L12 | 2、项目部教育培训的主要内容：观看《生命之鉴》安全教育警示片，观看率达到100％；施工现场的环境、施工特点及可能存在的危害等；违章指挥、违章作业、违反劳动纪律产生的后果；预防、减少安全风险以及紧急情况下应急救援的基本措施； | score=0.0619
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L13 | 3、班组教育培训的主要内容：本班组作业特点和安全操作规程；如何正确使用劳动防护用品和安全防护装置；本岗位可能存在的危害及防范对策；本岗位的作业环境及使用的机械设备、工具的安全要求等。 | score=0.0644
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L14 | 1.2.3 三级安全教育的主控部门： | score=0.0593
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L14 | 1.2.3 三级安全教育的主控部门： | score=0.0593
  - C11 | COLLECT | real_69c60974d4242eda8c47c615:L17 | 临时务工人员，入场安全培训可采用班前教育与书面教育相结合等方式，每日入场前必须进行安全教育培训，仅限当日有效，安全员负责收集存档。 | score=0.0593
- projection_chars: 3464

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: All sections of Chapter 1 on safety education and training have been collected and assembled in the evidence groups.
- legal_actions (59):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0565
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0565
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0565
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0565
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0565
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0532
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0532
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0532
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0532
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L90 | 1、一般事故隐患的治理由各项目部根据事故隐患的实际情况，制定针对性的治理措施，落实相关责任人，限期进行整改； | score=0.0532
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0477
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0477
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0477
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0550
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0550
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0550
- projection_chars: 3494

### Evidence text (new)

```
[E1]
[§ 1.2 三级安全教育]
  1.2.1 三级安全教育的对象：新进集团公司的作业人员，在上岗前必须接受集团公司（基层单位）、项目、班组的三级安全教育培训（附表1.2-1：项目管理人员三级安全教育记录表；附表1.2-2：项目操作人员三级安全教育记录表）。
  分包单位的作业人员三级安全教育，由其分包单位进行，项目部履行监督职责，并保存三级安全教育记录（附表1.2-3：分包单位作业人员三级安全教育记录表）。

[E2]
[§ 1.1 总则]
  1.1.1安全教育和培训的类型应包括三级安全教育、岗前教育、日常教育、年度继续教育，以及各类特种作业人员证书的初审、复审培训（附表1.1.1：安全教育记录）。
  1.1.2集团公司各级安全教育培训计划、安全教育培训工作按集团公司教育培训制度执行。

[E3]
[§ 1.3岗前教育]
  新上岗作业人员，作业人员进入新的岗位或者新的施工现场前，离岗一年以上重新上岗时，采用新技术、新工艺、新设备、新材料时，项目部应对作业人员进行相应的岗前教育培训。
  岗前教育培训包括以下内容：
  1、安全生产法律法规和规章制度；
```

### Evidence text (old)

```
[E1]
第一章　安全教育培训规定
1.1 总则

[E2]
[§ 第一章　安全教育培训规定 / 1.7 附则]
附表1：安全教育记录；

[E3]
[§ 第一章　安全教育培训规定 / 1.3岗前教育]
2、安全操作规程；

[E4]
[§ 第一章　安全教育培训规定 / 1.4 日常安全教育：]
1.4.1作业人员进场施工每个月或者作业工种、作业环境发生改变，安全员组织施工员配合进行安全教育培训，其内容包括观看《生命之鉴》安全教育警示片、岗位安全教育、专项安全教育、日常教育等，施工员组织安全员参与做好针对性的安全技术交底，强化、规范作业人员作业行为。

[E5]
[§ 第一章　安全教育培训规定 / 1.3岗前教育]
1、安全生产法律法规和规章制度；

[E6]
[§ 第一章　安全教育培训规定 / 1.2 三级安全教育 / 1.2.2 三级安全教育的内容]
1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析；

[E7]
[§ 第一章　安全教育培训规定 / 1.7 附则]
附表1.
```

## latest_clean_niche_0214 (niche_fact)

**Query:** 根据《附件_安全管理规定（2020版）》中“2.3.3 定期安全检查”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 483 | 464 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 14 | 10 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L66` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C9` kind=`collect` section=`real_69c60974d4242eda8c47c615:L62` scope=`None` depth=`0`
- reason: Section 2.3 covers safety inspection methods, including the target section 2.3.3.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L62']
- collect added=14 hits=14 branch_selected=True collect_full=True
- legal_actions (55):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0680
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0680
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0680
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0680
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0680
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0557
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0557
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0534
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0534
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L47 | 3、各项安全管理制度的执行情况，各级安全生产职责的履行情况，安全管理目标的实现程度； | score=0.0534
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0557
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0557
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L56 | 1、安全技术交底、安全措施是否落实到施工作业中； | score=0.0557
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0634
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0634
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0618
- projection_chars: 3531

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Section G4 contains the specific regulations for '2.3.3 Regular Safety Inspections' as requested.
- legal_actions (53):
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0680
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0680
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0680
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0680
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0557
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0557
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0534
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0534
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L47 | 3、各项安全管理制度的执行情况，各级安全生产职责的履行情况，安全管理目标的实现程度； | score=0.0534
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L54 | 10、各类事故是否按“四不放过”的原则进行处理，是否有隐瞒不报情况。 | score=0.0513
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0557
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0557
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L56 | 1、安全技术交底、安全措施是否落实到施工作业中； | score=0.0557
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0645
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0645
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0645
- projection_chars: 3455

### Evidence text (new)

```
[E1]
[§ 2.3.3 定期安全检查]
  1、集团公司每季度进行一次安全检查，重点检查项目部施工现场安全生产管理体系的运行情况、施工现场安全隐患排查和安全防护情况；二级单位对项目部的定期监督检查制度落实情况等（集团公司直属项目每月检查一次）；
  2、集团公司委托二级单位每月组织对所属项目进行一次安全检查及隐患排查。
  3、项目部每周组织各分包单位进行安全检查；
  附表2-3-3《项目周检查标准化表格》
  4、项目因故停工（复工）执行集团公司停复工相关规定，复工前，项目部必须对施工现场安全设施、设备及安全防护进行自查，基层单位复查。

[E2]
[§ 2.3.5 季节性安全检查]
在冬、雨季及暑期来临前或施工期间，集团公司各级安全监督管理部门根据本单位的施工情况，应组织季节性检查。

[E3]
[§ 2.3安全检查及隐患排查的方法]
2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。
```

### Evidence text (old)

```
[E1]
[§ 第二章　安全检查及隐患排查规定 / 2.3安全检查及隐患排查的方法 / 2.3.4 专项安全检查]
对于危险性较大的分部分项工程的施工，施工现场临时用电，安全技术措施等，集团公司及二级单位安全监督管理部门应当在必要时安排专项安全检查。

[E2]
[§ 第二章　安全检查及隐患排查规定 / 2.2  安全检查及隐患排查内容 / 2.2.1集团公司、二级单位、项目部安全检查的主要内容：]
1、安全生产法律法规、标准规范和其他要求的执行情况；

[E3]
[§ 第二章　安全检查及隐患排查规定 / 2.4 隐患整改 / 2.4.4 重大事故隐患整改、复查、销项]
3、经费和物资的落实；

[E4]
[§ 第二章　安全检查及隐患排查规定 / 2.3安全检查及隐患排查的方法 / 2.3.3 定期安全检查]
2、集团公司委托二级单位每月组织对所属项目进行一次安全检查及隐患排查。

[E5]
[§ 第二章　安全检查及隐患排查规定 / 2.2  安全检查及隐患排查内容 / 2.2.2班组安全检查的内容：]
1、安全技术交底、安全措施是否落实到施工作业中；
```

## latest_clean_niche_0219 (niche_fact)

**Query:** 根据《附件_安全管理规定（2020版）》中“2.3.4 专项安全检查”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 494 | 184 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 15 | 4 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L72` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C12` kind=`collect` section=`real_69c60974d4242eda8c47c615:L71` scope=`None` depth=`0`
- reason: Target section 2.3.4 Special Safety Inspection identified; collect to retrieve full content.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L71']
- collect added=3 hits=3 branch_selected=True collect_full=True
- legal_actions (50):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0617
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0617
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0615
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0615
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0615
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0511
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0511
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0511
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0511
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L47 | 3、各项安全管理制度的执行情况，各级安全生产职责的履行情况，安全管理目标的实现程度； | score=0.0511
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L54 | 10、各类事故是否按“四不放过”的原则进行处理，是否有隐瞒不报情况。 | score=0.0510
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0509
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0509
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L56 | 1、安全技术交底、安全措施是否落实到施工作业中； | score=0.0509
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0616
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0616
- projection_chars: 3541

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains the specific regulations for section 2.3.4 Special Safety Inspections as requested.
- legal_actions (46):
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0617
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0615
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0615
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0615
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0511
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0511
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0511
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0511
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L47 | 3、各项安全管理制度的执行情况，各级安全生产职责的履行情况，安全管理目标的实现程度； | score=0.0511
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L54 | 10、各类事故是否按“四不放过”的原则进行处理，是否有隐瞒不报情况。 | score=0.0510
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0509
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0509
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L56 | 1、安全技术交底、安全措施是否落实到施工作业中； | score=0.0509
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0616
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0609
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0617
- projection_chars: 3378

### Evidence text (new)

```
[E1]
[§ 2.3.4 专项安全检查]
  定期检查中发现的倾向性问题，安全状况差的项目，集团公司及二级单位安排专项检查。
  对于超过一定规模危险性较大的分部分项工程的施工，二级单位在施工期间必须至少安排一次专项安全检查。
  对于危险性较大的分部分项工程的施工，施工现场临时用电，安全技术措施等，集团公司及二级单位安全监督管理部门应当在必要时安排专项安全检查。
```

### Evidence text (old)

```
[E1]
附件_安全管理规定（2020版）.docx

[E2]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.2  安全检查及隐患排查内容 / 2.2.1集团公司、二级单位、项目部安全检查的主要内容：]
3、各项安全管理制度的执行情况，各级安全生产职责的履行情况，安全管理目标的实现程度；

[E3]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.4 隐患整改 / 2.4.4 重大事故隐患整改、复查、销项]
2、采取的方法和措施；

[E4]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.2  安全检查及隐患排查内容 / 2.2.2班组安全检查的内容：]
6、其他应检查的内容。

[E5]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表6.6.1-1]
备注： 本表中所列工程，若本工程施工中有时在对应的辨识结论栏内打“√”，无时打“×”。
```

## latest_clean_niche_0222 (niche_fact)

**Query:** 根据《附件_安全管理规定（2020版）》中“2.3.5 季节性安全检查”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 74 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 16 | 1 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L76` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C16` kind=`collect` section=`real_69c60974d4242eda8c47c615:L76` scope=`None` depth=`0`
- reason: Found section 2.3.5 'Seasonal Safety Inspection' with the specific regulation text.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L76']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (56):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0560
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0560
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L26 | 1.4 日常安全教育： | score=0.0560
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L26 | 1.4 日常安全教育： | score=0.0560
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L28 | 1.4.2项目部依据项目实际情况组织雨季、暑期、冬季等季节性安全教育；节假日安全、消防安全等专项安全教育。 | score=0.0560
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0721
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0721
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0628
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0628
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0628
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0670
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0670
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0670
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0670
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L53 | 9、根据季节变化，防雷、防暑降温、防火、防台、防汛、防冻保温、防滑等措施的落实情况； | score=0.0670
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0721
- projection_chars: 3518

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains the specific regulations for seasonal safety inspections as requested.
- legal_actions (58):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0560
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0560
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L26 | 1.4 日常安全教育： | score=0.0560
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L26 | 1.4 日常安全教育： | score=0.0560
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L28 | 1.4.2项目部依据项目实际情况组织雨季、暑期、冬季等季节性安全教育；节假日安全、消防安全等专项安全教育。 | score=0.0560
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0721
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0721
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0628
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0628
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0628
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0670
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0670
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0670
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0670
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L53 | 9、根据季节变化，防雷、防暑降温、防火、防台、防汛、防冻保温、防滑等措施的落实情况； | score=0.0670
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0721
- projection_chars: 3594

### Evidence text (new)

```
[E1]
[§ 2.3.5 季节性安全检查]
在冬、雨季及暑期来临前或施工期间，集团公司各级安全监督管理部门根据本单位的施工情况，应组织季节性检查。
```

### Evidence text (old)

```
[E1]
附件_安全管理规定（2020版）.docx

[E2]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.2  安全检查及隐患排查内容 / 2.2.1集团公司、二级单位、项目部安全检查的主要内容：]
3、各项安全管理制度的执行情况，各级安全生产职责的履行情况，安全管理目标的实现程度；

[E3]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.3安全检查及隐患排查的方法 / 2.3.4 专项安全检查]
对于危险性较大的分部分项工程的施工，施工现场临时用电，安全技术措施等，集团公司及二级单位安全监督管理部门应当在必要时安排专项安全检查。

[E4]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表3.2]
单位名称：

[E5]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.4 隐患整改 / 2.4.4 重大事故隐患整改、复查、销项]
3、经费和物资
```

## latest_clean_niche_0223 (niche_fact)

**Query:** 根据《附件_安全管理规定（2020版）》中“2.3.6 日常安全检查”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 483 | 239 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 14 | 4 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L78` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C10` kind=`collect` section=`real_69c60974d4242eda8c47c615:L77` scope=`None` depth=`0`
- reason: Target section 2.3.6 contains the specific rules for daily safety inspections.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L77']
- collect added=3 hits=3 branch_selected=True collect_full=True
- legal_actions (53):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0651
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0651
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0651
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0651
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0651
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0541
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0541
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0541
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0541
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L56 | 1、安全技术交底、安全措施是否落实到施工作业中； | score=0.0541
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0619
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0619
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0604
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L64 | 2.3.2集团公司安全检查及隐患排查的方式包括定期安全检查、专项安全检查、季节性安全检查、日常安全巡查、不定期抽查等。 | score=0.0555
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L77 | 2.3.6 日常安全检查 | score=0.0619
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L77 | 2.3.6 日常安全检查 | score=0.0619
- projection_chars: 3544

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains the specific regulations for section 2.3.6 Daily Safety Inspection as requested.
- legal_actions (51):
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0651
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0651
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0651
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0651
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0541
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0541
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0541
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0541
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L56 | 1、安全技术交底、安全措施是否落实到施工作业中； | score=0.0541
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L61 | 6、其他应检查的内容。 | score=0.0514
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0619
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0604
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L64 | 2.3.2集团公司安全检查及隐患排查的方式包括定期安全检查、专项安全检查、季节性安全检查、日常安全巡查、不定期抽查等。 | score=0.0555
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0574
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0574
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0574
- projection_chars: 3501

### Evidence text (new)

```
[E1]
[§ 2.3.6 日常安全检查]
  1、项目施工管理人员应对施工区域内的安全措施落实情况和作业人员遵章守纪情况进行巡查，对发现的违章行为和事故隐患应及时纠正和整改；
  2、项目经理和安全员要督促分包和设备租赁单位做好作业班组班前、班中和班后的安全岗位检查，发现问题及时整改；
  3、项目专职安全员每日必须深入施工现场巡查，发现事故隐患应及时督促整改，并将检查情况及时报告项目负责人和上级安全监督管理部门，以便落实整改措施。附表2-3-6《安全员日巡查标准化表格》
```

### Evidence text (old)

```
[E1]
[§ 第二章　安全检查及隐患排查规定 / 2.2  安全检查及隐患排查内容 / 2.2.1集团公司、二级单位、项目部安全检查的主要内容：]
1、安全生产法律法规、标准规范和其他要求的执行情况；

[E2]
[§ 第二章　安全检查及隐患排查规定 / 2.3安全检查及隐患排查的方法 / 2.3.4 专项安全检查]
对于危险性较大的分部分项工程的施工，施工现场临时用电，安全技术措施等，集团公司及二级单位安全监督管理部门应当在必要时安排专项安全检查。

[E3]
[§ 第二章　安全检查及隐患排查规定 / 2.2  安全检查及隐患排查内容 / 2.2.2班组安全检查的内容：]
1、安全技术交底、安全措施是否落实到施工作业中；

[E4]
[§ 第二章　安全检查及隐患排查规定 / 2.4 隐患整改 / 2.4.4 重大事故隐患整改、复查、销项]
3、经费和物资的落实；

[E5]
[§ 第二章　安全检查及隐患排查规定 / 2.3安全检查及隐患排查的方法 / 2.3.3 定期安全检查]
2、集团公司委托二级单位每月组织对所属项目进行一次安全检查及隐患排查。
```

## latest_clean_niche_0226 (niche_fact)

**Query:** 根据《附件_安全管理规定（2020版）》中“2.4 隐患整改”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 481 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 8 | 11 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L82` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C10` kind=`collect` section=`real_69c60974d4242eda8c47c615:L81` scope=`None` depth=`0`
- reason: Collect section 2.4 '隐患整改' to retrieve all relevant regulations and facts.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L81']
- collect added=25 hits=25 branch_selected=True collect_full=True
- legal_actions (50):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0723
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0723
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0596
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0596
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0596
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0535
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0535
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0535
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0535
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L54 | 10、各类事故是否按“四不放过”的原则进行处理，是否有隐瞒不报情况。 | score=0.0535
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0541
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0541
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L77 | 2.3.6 日常安全检查 | score=0.0541
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L77 | 2.3.6 日常安全检查 | score=0.0541
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L78 | 1、项目施工管理人员应对施工区域内的安全措施落实情况和作业人员遵章守纪情况进行巡查，对发现的违章行为和事故隐患应及时纠正和整改； | score=0.0541
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0723
- projection_chars: 3620

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Assembled evidence fully covers section 2.4 Hazard Rectification including definitions, responsibilities, and procedures.
- legal_actions (52):
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0723
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0596
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0596
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0596
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L42 | 2.1.2 集团公司各级安全检查、隐患整改、回复销项、安全处罚均采用集团公司企业发展部的统一检查表格。 | score=0.0477
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0535
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0535
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0535
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0535
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L54 | 10、各类事故是否按“四不放过”的原则进行处理，是否有隐瞒不报情况。 | score=0.0535
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0509
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0509
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L56 | 1、安全技术交底、安全措施是否落实到施工作业中； | score=0.0509
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L59 | 4、施工作业环境是否整洁安全，符合施工作业要求； | score=0.0502
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0541
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0541
- projection_chars: 3548

### Evidence text (new)

```
[E1]
[§ 2.4 隐患整改]
  2.4.1 事故隐患分为一般事故隐患和重大事故隐患。
  1、一般事故隐患，是指危害和整改难度较小，发现后能够立即整改排除的隐患；
  2、重大事故隐患，是指危害和整改难度较大，应当全部或者局部停产停业，并经过一定时间整改治理方能排除的隐患，或者因外部因素影响致使生产经营单位自身难以排除的隐患。

[E2]
[§ 2.4.2 隐患整改的职责]
  1、各项目的项目经理对事故隐患治理负直接全面责任；
  2、各二级单位主要负责人对事故隐患治理负直接管理领导责任；
  3、集团公司相关部门对事故隐患治理负监督管理责任。

[E3]
[§ 2.4.3 一般事故隐患整改、复查、销项]
  1、一般事故隐患的治理由各项目部根据事故隐患的实际情况，制定针对性的治理措施，落实相关责任人，限期进行整改；
  2、集团公司各级安全检查发现的一般事故隐患，必须建立档案（事故隐患登记台账），由被检查项目负责整改，整改完成后在隐患整改回复单填写自检情况（须附证明材料），项目负责人复查验证，签字确认后上报二级单位，由二级单位复查销项。
```

### Evidence text (old)

```
[E1]
[§ 2.4 隐患整改 / 2.4.7 隐患整改（控制或变更降低安全风险）措施的优先顺序：]
4、标志、警告和管理控制措施：安全标志、危险区域标识、警告器或警告灯、报警器、安全规程、设备检修、作业安全制度、操作牌和作业许可证等；

[E2]
[§ 2.4 隐患整改 / 2.4.4 重大事故隐患整改、复查、销项]
2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。

[E3]
[§ 2.4 隐患整改 / 2.4.2 隐患整改的职责]
2、各二级单位主要负责人对事故隐患治理负直接管理领导责任；

[E4]
[§ 2.4 隐患整改 / 2.4.7 隐患整改（控制或变更降低安全风险）措施的优先顺序：]
5、个体防护装备：为操作者配备必要的个体防护装备；

[E5]
[§ 2.4 隐患整改 / 2.4.7 隐患整改（控制或变更降低安全风险）措
```

## latest_clean_niche_0249 (niche_fact)

**Query:** 根据《附件_安全管理规定（2020版）》中“第三章 生产安全事故报告处理规定”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 499 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 12 | 16 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L115` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C7` kind=`collect` section=`real_69c60974d4242eda8c47c615:L113` scope=`None` depth=`0`
- reason: Collect Chapter 3 to retrieve all regulations on accident reporting and handling.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L113']
- collect added=33 hits=33 branch_selected=True collect_full=True
- legal_actions (45):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0579
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0579
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0548
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0548
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0548
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0579
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0579
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0579
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0579
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0579
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0720
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0720
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L114 | 3.1总则 | score=0.0676
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L114 | 3.1总则 | score=0.0676
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L115 | 生产安全事故管理应包括报告、调查、处理、分析改进、统计等工作内容。 | score=0.0676
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L116 | 3.2 事故报告 | score=0.0716
- projection_chars: 3548

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence covers Chapter 3 accident reporting, handling, investigation, and analysis as requested.
- legal_actions (60):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0448
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L3 | 第一章　安全教育培训规定 | score=0.0448
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0448
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L7 | 1.2 三级安全教育 | score=0.0448
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0448
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L10 | 1.2.2 三级安全教育的内容 | score=0.0448
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L11 | 1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析； | score=0.0448
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0579
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0579
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0548
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0548
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0548
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0479
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0479
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0479
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0479
- projection_chars: 3388

### Evidence text (new)

```
[E1]
[§ 3.2 事故报告]
  事故发生后，事故现场负责人应当立即向集团公司负责人报告；集团公司负责人接到报告后，按照《生产安全事故报告和调查处理条例》的规定，在1小时内向事故发生地安全生产监督管理局、建设主管部门、陕建集团总公司等部门逐级报告。
  在报告的同时，应当及时编制《生产安全事故快报表》（见附表3.2）报陕建集团总公司安全监管部门。
  生产安全事故报告的内容应包括：
  1 事故的时间、地点和工程项目有关单位名称；
  2 事故的简要经过；
  3 事故已经造成或者可能造成的伤亡人数（包括下落不明的人数）和初步估计的直接经济损失；
  4 事故的初步原因；
  5 事故发生后采取的措施及事故控制情况；
  6 事故报告单位或报告人员；
  生产安全事故报告后出现新情况的，应及时补报。

[E2]
[§ 3.4 事故处理]
  3.4.4项目负责人安全事故处理
  1 发生较大及以上事故或暂扣集团公司安全生产许可证的一般事故，对项目部、二级单位、集团公司安全管理部相关责任人进行追责处理。
  3 发生集团公司负非主要责任的一般事故，对项目部相关责任人进行追责处理。
```

### Evidence text (old)

```
[E1]
第三章　生产安全事故报告处理规定
3.1总则

[E2]
[§ 第三章　生产安全事故报告处理规定 / 3.5 分析改进]
附表3.2：生产安全事故快报；

[E3]
[§ 第三章　生产安全事故报告处理规定 / 3.2 事故报告]
5 事故发生后采取的措施及事故控制情况；

[E4]
[§ 第三章　生产安全事故报告处理规定 / 3.5 分析改进]
附表3.7-3：安全生产信息统计报表。

[E5]
[§ 第三章　生产安全事故报告处理规定 / 3.4 事故处理]
3.4.4项目负责人安全事故处理

[E6]
[§ 第三章　生产安全事故报告处理规定 / 3.3 事故调查]
发生一般及以上事故，依据《生产安全事故报告和调查处理条例》（中华人民共和国国务院令第493号），经县级以上有关部门组织事故调查组进行调查。

[E7]
[§ 第三章　生产安全事故报告处理规定 / 3.5 分析改进]
根据事故调查报告，总结事故教训，在本项目提出防范和整改措施。并在集团公司范围内宣贯。

[E8]
[§ 第三章　生产安全事故报告处理规定 / 3.5 分析改进]
3.7 集团公司生产安全事故实行月度报
```

## latest_clean_niche_0258 (niche_fact)

**Query:** 根据《附件_安全管理规定（2020版）》中“3.4 事故处理”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 470 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 8 | 6 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L131` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C20` kind=`collect` section=`real_69c60974d4242eda8c47c615:L130` scope=`None` depth=`0`
- reason: Collect section 3.4 and its specific rules on accident handling decisions, accountability, and fines.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L130', 'real_69c60974d4242eda8c47c615:L131', 'real_69c60974d4242eda8c47c615:L139', 'real_69c60974d4242eda8c47c615:L142']
- collect added=12 hits=15 branch_selected=False collect_full=True
- legal_actions (50):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0701
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0701
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0556
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0556
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0556
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0581
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0581
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0581
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0581
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L54 | 10、各类事故是否按“四不放过”的原则进行处理，是否有隐瞒不报情况。 | score=0.0581
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0701
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0701
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0701
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0701
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L90 | 1、一般事故隐患的治理由各项目部根据事故隐患的实际情况，制定针对性的治理措施，落实相关责任人，限期进行整改； | score=0.0701
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0686
- projection_chars: 3480

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Section G1 contains all relevant content from 3.4 Accident Handling as requested.
- legal_actions (54):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0701
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0701
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0556
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0556
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0556
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0581
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0581
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0581
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0581
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L54 | 10、各类事故是否按“四不放过”的原则进行处理，是否有隐瞒不报情况。 | score=0.0581
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0701
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0701
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L85 | 2.4.2 隐患整改的职责 | score=0.0520
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L85 | 2.4.2 隐患整改的职责 | score=0.0520
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L88 | 3、集团公司相关部门对事故隐患治理负监督管理责任。 | score=0.0520
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0701
- projection_chars: 3455

### Evidence text (new)

```
[E1]
[§ 3.4 事故处理]
  3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。
  3.4.4项目负责人安全事故处理
  1 发生较大及以上事故或暂扣集团公司安全生产许可证的一般事故，对项目部、二级单位、集团公司安全管理部相关责任人进行追责处理。
  3 发生集团公司负非主要责任的一般事故，对项目部相关责任人进行追责处理。
  4 按照严重未履职（或违章指挥）、一般未履职（或履职不到位）对事故发生负责的主要直接责任人分别处以项目负责人事故罚款60%、30%的罚款处理，对事故发生负责的主要间接责任人分别处以项目负责人事故罚款40%、20%的罚款，对事故发生负责的一般直接负责人或一般间接责任人分别处以20%、10%的罚款。情节严重时按照照集团公司《管理人员责任追究暂行规定》第八条处以组织措施。履职尽责相关人员免责。
```

### Evidence text (old)

```
[E1]
[§ 3.4 事故处理]
3.4.4项目负责人安全事故处理

[E2]
[§ 4.4 应急响应程序]
4.4.1施工现场一旦发生生产安全事故，项目部应采取措施疏散人员、抢救伤者、控制事故的扩大，并将事故的信息立即向集团公司生产安全事故应急救援总指挥报告。

[E3]
[§ 3.4 事故处理]
1 发生较大及以上事故或暂扣集团公司安全生产许可证的一般事故，对项目部、二级单位、集团公司安全管理部相关责任人进行追责处理。

[E4]
[§ 3.4 事故处理]
3.4.2 项目部承担事故造成的一切损失及罚款。发生重伤以上责任安全生产事故，当期项目季度过程考核直接计入排名最后一名，项目最终过程性考核认定未完成项目目标责任管理的安全目标。

[E5]
[§ 3.4 事故处理]
3.4.3发生重伤以上责任安全生产事故，二级单位年度安全考核指标认定为未完成安全目标，为安全考核指标的否决项。

[E6]
[§ 3.4 事故处理]
3.4.5对事故发生直接负责的直接负责人员和间接责任人员，按照尽职免责，失职追责的原则处理。直接责任人包括项目部项目生产副经理、技术负责人、主管施工员、安全员、其他相
```

## latest_clean_niche_0306 (niche_fact)

**Query:** 根据《附件_安全管理规定（2020版）》中“附表5.2.2：《施工现场安全负面清单（2019版）》”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 494 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 15 | 12 |
| trajectory_steps | n/a | 5 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L194` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C32` kind=`collect` section=`real_69c60974d4242eda8c47c615:L544` scope=`None` depth=`0`
- reason: Target section contains the specific negative list content requested.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L544']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (53):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0645
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0645
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0645
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0645
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0645
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0645
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L49 | 5、施工现场管理行为和实物状况（安全隐患排查、安全设施及安全防护等各项措施和落实情况）； | score=0.0645
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0562
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0562
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0562
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0562
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0562
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0598
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0598
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0598
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0598
- projection_chars: 3406

**Step 2** `nav_collect`  id=`C33` kind=`collect` section=`real_69c60974d4242eda8c47c615:L497` scope=`None` depth=`0`
- reason: Collect the specific section containing the negative list title and content to answer the query.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L497']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (56):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0645
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0645
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0645
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0645
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0645
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0645
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L49 | 5、施工现场管理行为和实物状况（安全隐患排查、安全设施及安全防护等各项措施和落实情况）； | score=0.0645
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0562
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0562
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0562
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0562
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0562
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0598
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0598
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0598
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0598
- projection_chars: 3448

**Step 3** `nav_collect`  id=`C13` kind=`collect` section=`real_69c60974d4242eda8c47c615:L189` scope=`None` depth=`0`
- reason: Section C13 explicitly references the 'Negative List' and its usage restrictions as required by the query.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L189']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (57):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0645
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0645
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0645
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0645
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0645
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0645
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L49 | 5、施工现场管理行为和实物状况（安全隐患排查、安全设施及安全防护等各项措施和落实情况）； | score=0.0645
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0562
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0562
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0562
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0562
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0562
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0598
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0598
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0598
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0598
- projection_chars: 3633

**Step 4** `nav_collect`  id=`C35` kind=`collect` section=`real_69c60974d4242eda8c47c615:L501` scope=`None` depth=`0`
- reason: Collect section C35 to retrieve the full content of Appendix 5.2.2 'Construction Site Safety Negative List'.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L501']
- collect added=47 hits=47 branch_selected=True collect_full=True
- legal_actions (57):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0645
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0645
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0645
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0645
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0645
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0645
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L49 | 5、施工现场管理行为和实物状况（安全隐患排查、安全设施及安全防护等各项措施和落实情况）； | score=0.0645
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0562
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0562
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0562
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0562
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0562
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0598
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0598
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0598
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0598
- projection_chars: 3544

**Step 5** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G3, G1, and G2 directly address the query about '附表5.2.2' content and restrictions.
- legal_actions (53):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0645
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0645
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0645
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0645
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0645
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0645
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L49 | 5、施工现场管理行为和实物状况（安全隐患排查、安全设施及安全防护等各项措施和落实情况）； | score=0.0645
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0562
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0562
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0562
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0562
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0562
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0598
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0598
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0598
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0598
- projection_chars: 3446

### Evidence text (new)

```
[E1]
[§ 附件5.2.2                     施工现场安全负面清单（2]
文档列出使用不合格防坠器、超年限设备及维护不到位等问题的分包单位名单，并详细规定了塔吊、升降机、脚手架及临电设施等禁止或淘汰的技术标准与依据。

[E2]
[§ 5.2机械设备管理]
5.2.2 严禁租赁集团公司《施工现场安全负面清单（2019版）》（见附表5.2-2）中禁止及限制使用的施工机械；租赁机械设备时，要求选择注册资金不小于200万元人民币的租赁单位，拟租起重机械机械使用年限应符合以下规定：

[E3]
[§ 4.3.2 应急预案演练评价报]
5.2.2：《施工现场安全负面清单（2019版）》

[E4]
[§ 附表6.6.1-2]
  专项方案应当组织专家论证的危险性较大的分部分项工程识别清单
  工程名称：
  备注：本表中所列工程，若本工程施工中有时在对应的辨识结论栏内打“√”，无时打“×”。

[E5]
[§ 附表6.6.1-1]
  危险性较大的分部分项工程识别清单
  备注： 本表中所列工程，若本工程施工中有时在对应的辨识结论栏内打“√”，无时打“×”。
```

### Evidence text (old)

```
[E1]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表6.6.1-1]
备注： 本表中所列工程，若本工程施工中有时在对应的辨识结论栏内打“√”，无时打“×”。

[E2]
附件_安全管理规定（2020版）.docx

[E3]
[§ 附件_安全管理规定（2020版）.docx / 第三章　生产安全事故报告处理规定 / 3.5 分析改进]
附表3.7-3：安全生产信息统计报表。

[E4]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表4.3.1]
工程名称：

[E5]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.2  安全检查及隐患排查内容 / 2.2.2班组安全检查的内容：]
4、施工作业环境是否整洁安全，符合施工作业要求；

[E6]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6
```

## latest_clean_niche_0321 (niche_fact)

**Query:** 根据《附件_安全管理规定（2020版）》中“5.3.2 按陕建监总发[2014]04号文要求：”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 276 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 16 | 4 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L211` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C20` kind=`collect` section=`real_69c60974d4242eda8c47c615:L210` scope=`None` depth=`0`
- reason: Target section 5.3.2 explicitly mentions the required document and likely contains the specific regulation requested.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L210']
- collect added=3 hits=3 branch_selected=True collect_full=True
- legal_actions (49):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0623
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0623
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0600
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0600
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0600
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0623
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0623
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0623
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0623
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0623
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L103 | 2.4.6 各项目部应当加强对自然灾害的预防。对于因自然灾害可能导致事故灾难的隐患，应当按照有关法律、法规、标准和本制度的要求排查治理，采取可靠的预防措施，制定应急预案。在接到有关自然灾害预报时，应当及时向有关人员发出预警通知；发生自然灾害可能危及施工和人员安全的情况时，应当采取撤离人员、停止作业、加强监测等安全措施，并及时向当地人民政府有关部门报告。 | score=0.0535
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0700
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0700
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L116 | 3.2 事故报告 | score=0.0650
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L116 | 3.2 事故报告 | score=0.0650
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L117 | 事故发生后，事故现场负责人应当立即向集团公司负责人报告；集团公司负责人接到报告后，按照《生产安全事故报告和调查处理条例》的规定，在1小时内向事故发生地安全生产监督管理局、建设主管部门、陕建集团总公司等部门逐级报告。 | score=0.0638
- projection_chars: 3534

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains the specific section 5.3.2 and its related requirements as requested.
- legal_actions (51):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0623
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0623
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0600
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0600
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0600
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0524
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0524
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L63 | 2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。 | score=0.0524
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0623
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0623
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0623
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0623
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0623
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L103 | 2.4.6 各项目部应当加强对自然灾害的预防。对于因自然灾害可能导致事故灾难的隐患，应当按照有关法律、法规、标准和本制度的要求排查治理，采取可靠的预防措施，制定应急预案。在接到有关自然灾害预报时，应当及时向有关人员发出预警通知；发生自然灾害可能危及施工和人员安全的情况时，应当采取撤离人员、停止作业、加强监测等安全措施，并及时向当地人民政府有关部门报告。 | score=0.0535
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0700
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0700
- projection_chars: 3668

### Evidence text (new)

```
[E1]
[§ 5.3.2 按陕建监总发[2014]04号文要求：]
  自2015年1月1日起，附着式升降脚手架外立面、底板、脚手板必须使用具有防火功能的防护产品；
  吊篮的安/拆（包括二次移位）工作，均应由出租单位负责完成，使用单位不得安拆、转租吊篮；
  5.3.3 附着式升降脚手架、高空作业吊篮等工具式脚手架的专项方案由专业分包单位组织编制，方案应符合《建筑施工工具式脚手架安全技术规范》JGJ202-2010（以下简称JGJ202-2010）的相关规定。并经过分包单位具有法人资格企业的技术负责人批准。再按照专项方案审批程序履行审批手续。
```

### Evidence text (old)

```
[E1]
[§ 附件_安全管理规定（2020版）.docx]
陕西建工第十一建设集团有限公司

[E2]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.4 隐患整改 / 2.4.4 重大事故隐患整改、复查、销项]
5、治理的时限和要求；

[E3]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表3.2]
单位名称：

[E4]
附件_安全管理规定（2020版）.docx

[E5]
[§ 附件_安全管理规定（2020版）.docx / 第六章　项目安全管理规定 / 6.1 总则]
6.1.1 为了规范集团公司项目安全管理，明确项目安全管理责任，预防和减少生产安全事故，促进企业稳定发展，制定本规定。

[E6]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表6.6.1-1]
备注： 本表中所列工程，若本工程施工中有时在对应的辨识结论栏内打“√”，无时打
```

## latest_clean_niche_0325 (niche_fact)

**Query:** 根据《附件_安全管理规定（2020版）》中“5.3.4 附着式升降脚手架、高空作业吊篮等管理程序：”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 492 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 7 | 9 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L215` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C12` kind=`collect` section=`real_69c60974d4242eda8c47c615:L214` scope=`None` depth=`0`
- reason: Section 5.3.4 contains the specific management procedures for the queried equipment.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L214']
- collect added=18 hits=18 branch_selected=True collect_full=True
- legal_actions (43):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0700
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0700
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0658
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0658
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L179 | 5.1.1本规定适用于集团公司塔式超重机、施工升降机、物料提升机等大型施工机械设备及附着式升降脚手架、高空作业吊篮等工具式脚手架（自升式设施）管理。 | score=0.0658
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L180 | 5.1.2 集团公司对塔式超重机、施工升降机、附着式升降脚手架等起重设备建立合格供方名册，项目部使用的特种设备必须从集团公司合格供方名册内选择。 | score=0.0536
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L182 | 塔式起重机、施工升降机、高处作业吊篮的出租单位和附着式升降脚手架专业承包单位，应每月对在用的机械设备进行一次检查，并将检查记录报送施工总承包单位、监理单位签字确认，维修保养记录归集于机械设备安全技术档案。 | score=0.0597
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L184 | 起重机械及附着式升降脚手架单位对进入施工现场的人员，必须以文件形式任命项目负责人、专职机械设备管理人员、专职安全生产管理人员和特种作业人员等；现场人员变更时，应出具变更通知书，并经总包和监理单位同意，否则不得进行人员变更。 | score=0.0547
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L207 | 5.3 工具式脚手架管理 | score=0.0700
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L207 | 5.3 工具式脚手架管理 | score=0.0700
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L208 | 5.3.1 附着式升降脚手架、高空作业吊篮等工具式脚手架必须以独立分包形式与其专业公司签订专业分包合同和安全生产管理协议书（集团公司示范文本），明确各自的安全责任。 | score=0.0685
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L210 | 5.3.2 按陕建监总发[2014]04号文要求： | score=0.0700
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L210 | 5.3.2 按陕建监总发[2014]04号文要求： | score=0.0700
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L211 | 自2015年1月1日起，附着式升降脚手架外立面、底板、脚手板必须使用具有防火功能的防护产品； | score=0.0555
  - C11 | COLLECT | real_69c60974d4242eda8c47c615:L213 | 5.3.3 附着式升降脚手架、高空作业吊篮等工具式脚手架的专项方案由专业分包单位组织编制，方案应符合《建筑施工工具式脚手架安全技术规范》JGJ202-2010（以下简称JGJ202-2010）的相关规定。并经过分包单位具有法人资格企业的技术负责人批准。再按照专项方案审批程序履行审批手续。 | score=0.0700
  - C12 | COLLECT | real_69c60974d4242eda8c47c615:L214 | 5.3.4 附着式升降脚手架、高空作业吊篮等管理程序： | score=0.0693
- projection_chars: 3573

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 fully covers the specific regulations for 5.3.4 regarding scaffolding and basket management.
- legal_actions (48):
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0700
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0658
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0658
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L179 | 5.1.1本规定适用于集团公司塔式超重机、施工升降机、物料提升机等大型施工机械设备及附着式升降脚手架、高空作业吊篮等工具式脚手架（自升式设施）管理。 | score=0.0658
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L180 | 5.1.2 集团公司对塔式超重机、施工升降机、附着式升降脚手架等起重设备建立合格供方名册，项目部使用的特种设备必须从集团公司合格供方名册内选择。 | score=0.0536
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L182 | 塔式起重机、施工升降机、高处作业吊篮的出租单位和附着式升降脚手架专业承包单位，应每月对在用的机械设备进行一次检查，并将检查记录报送施工总承包单位、监理单位签字确认，维修保养记录归集于机械设备安全技术档案。 | score=0.0597
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L184 | 起重机械及附着式升降脚手架单位对进入施工现场的人员，必须以文件形式任命项目负责人、专职机械设备管理人员、专职安全生产管理人员和特种作业人员等；现场人员变更时，应出具变更通知书，并经总包和监理单位同意，否则不得进行人员变更。 | score=0.0547
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0516
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0516
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L187 | 5.2.1 严禁自行购置的机械设备（如塔式超重机、施工升降机等）直接租赁给项目部或自行购置的机械设备以单位名义对外出租。 | score=0.0462
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L193 | 附表5.2.2：《施工现场安全负面清单（2019版）》 | score=0.0516
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L193 | 附表5.2.2：《施工现场安全负面清单（2019版）》 | score=0.0516
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L196 | 5.2.4 租赁施工升降机和800KN·m及以下的塔式起重机时，应选用租赁安装维修保养一体化的专业承包企业；对800KN·m以上的塔式起重机出租单位，当其不具备相应的起重设备安装工程专业承包资质的，项目经理部必须在签订租赁合同的同时，与出租、安装单位共同签订三方安全管理协议书，并与安装单位签订安拆合同，并明确各方的安全生产权利与义务。 | score=0.0516
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L197 | 5.2.5 租用机械设备管理程序： | score=0.0475
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L197 | 5.2.5 租用机械设备管理程序： | score=0.0475
  - C11 | COLLECT | real_69c60974d4242eda8c47c615:L205 | 8、机械设备在使用过程中需要附着、顶升（加节），必须由原安装单位严格按照专项施工方案实施，并由使用单位组织出租单位、安装单位、监理单位等共同进行验收，验收合格后方可投入使用。 | score=0.0475
- projection_chars: 3456

### Evidence text (new)

```
[E1]
[§ 5.3.4 附着式升降脚手架、高空作业吊篮等管理程序：]
  1、从集团公司合格供方名单中选取附着式升降脚手架分包单位，选择有资质的高空作业吊篮分包单位；
  5、分包单位按专项施工方案进场安装，附着式升降脚手架安拆/升降作业人员应经专门培训、持有附着式脚手架特种作业操作资格证书，作业前应对所有作业人员进行安全教育和安全技术交底；
  8、吊篮出租单位应当对进入吊篮内作业的人员进行吊篮操作技能和安全知识教育培训、考核，吊篮出租与使用单位均应对操作人员进行相关的安全技术交底；
  1、附着式升降脚手架按JGJ202-2010表8.1.3《附着式升降脚手架首次安装完毕及检查使用前检查验收表》的内容验收；
  2、高处作业吊篮按JGJ202-2010表8.2.2《高处作业吊篮使用验收表》的内容验收。
  5.3.6 附着式升降脚手架使用工况，升降工况管理必须严格按照专项方案实施。
  升降工况作业前按JGJ202-2010表8.1.3《附着式升降脚手架首次安装完毕及检查使用前检查验收表》的内容验收。
  升降工况下，架体上不得有施工荷载，严禁人员在架体上停留。
```

### Evidence text (old)

```
[E1]
[§ 5.3.4 附着式升降脚手架、高空作业吊篮等管理程序：]
5.3.6 附着式升降脚手架使用工况，升降工况管理必须严格按照专项方案实施。

[E2]
[§ 5.3.4 附着式升降脚手架、高空作业吊篮等管理程序：]
2、签订专业分包合同，专业分包安全协议书；

[E3]
[§ 5.3.4 附着式升降脚手架、高空作业吊篮等管理程序：]
1、附着式升降脚手架按JGJ202-2010表8.1.3《附着式升降脚手架首次安装完毕及检查使用前检查验收表》的内容验收；

[E4]
[§ 5.3.4 附着式升降脚手架、高空作业吊篮等管理程序：]
升降工况作业前按JGJ202-2010表8.1.3《附着式升降脚手架首次安装完毕及检查使用前检查验收表》的内容验收。

[E5]
[§ 5.3.4 附着式升降脚手架、高空作业吊篮等管理程序：]
2、高处作业吊篮按JGJ202-2010表8.2.2《高处作业吊篮使用验收表》的内容验收。

[E6]
[§ 5.3.4 附着式升降脚手架、高空作业吊篮等管理程序：]
5、分包单位按专项施工方案进场安装，附着式升降脚手架安拆/升降作业人员应经专门培训、持有附
```

## latest_clean_niche_0413 (niche_fact)

**Query:** 根据《附件_安全管理规定（2020版）》中“6.4 安全生产违章行为处罚”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 497 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 10 | 11 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L315` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C17` kind=`collect` section=`real_69c60974d4242eda8c47c615:L314` scope=`None` depth=`0`
- reason: Section 6.4 contains the specific penalties for safety violations as requested.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L314']
- collect added=39 hits=39 branch_selected=True collect_full=True
- legal_actions (44):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0544
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0544
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0544
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0544
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0544
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0507
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0507
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0507
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0507
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0507
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0609
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0609
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0609
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0609
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0607
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L139 | 1 发生较大及以上事故或暂扣集团公司安全生产许可证的一般事故，对项目部、二级单位、集团公司安全管理部相关责任人进行追责处理。 | score=0.0537
- projection_chars: 3518

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Section G1 contains all relevant content from 6.4 regarding penalties for safety violations.
- legal_actions (49):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0544
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0544
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0544
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0544
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0544
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0453
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L62 | 2.3安全检查及隐患排查的方法 | score=0.0453
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L77 | 2.3.6 日常安全检查 | score=0.0453
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L77 | 2.3.6 日常安全检查 | score=0.0453
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L78 | 1、项目施工管理人员应对施工区域内的安全措施落实情况和作业人员遵章守纪情况进行巡查，对发现的违章行为和事故隐患应及时纠正和整改； | score=0.0453
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0507
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0507
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0442
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0442
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L90 | 1、一般事故隐患的治理由各项目部根据事故隐患的实际情况，制定针对性的治理措施，落实相关责任人，限期进行整改； | score=0.0442
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0507
- projection_chars: 3653

### Evidence text (new)

```
[E1]
[§ 6.4 安全生产违章行为处罚]
  6.4.1 项目部管理人员或作业队伍班组长有下列行为之一的，按“违章指挥”论处，责令整改，并处以罚款500～1000元罚款。
  6.4.2 项目部管理人员或作业人员有下列行为之一的，按“违章作业”论处，责令立即停止作业，并处以罚款50～500元罚款。
  4、私自拆除、损坏安全设施，或施工中拆除安全设施未及时恢复的；
  6.4.3 项目部管理人员或作业人员有下列行为之一的，按“违反劳动纪律“论处，责令改正，并处以罚款100～500元罚款。
  6.4.4 项目部管理人员或作业人员有下列行为之一的，按“违反安全相关规定”论处，责令改正，并处以罚款500～1000元罚款。
  9、对政府行政主管部门、上级及相关方安全检查或项目安全员发现的事故隐患不及时采取措施整改的；
  10、其他违反安全规范的现象或行为。
  6.4.5 集团公司在检查中发现项目的违章行为，对二级单位和项目部同时进行处罚；
  二级单位在检查中发现项目的违章行为，对项目部进行处罚；
  项目部在检查中发现的违章行为，对项目管理人员或作业班组（人员）进行处罚。
```

### Evidence text (old)

```
[E1]
[§ 6.4 安全生产违章行为处罚]
项目部在检查中发现的违章行为，对项目管理人员或作业班组（人员）进行处罚。

[E2]
安全管理规定（2020版）

[E3]
[§ 6.4 安全生产违章行为处罚]
6.4.4 项目部管理人员或作业人员有下列行为之一的，按“违反安全相关规定”论处，责令改正，并处以罚款500～1000元罚款。

[E4]
[§ 6.4 安全生产违章行为处罚]
二级单位在检查中发现项目的违章行为，对项目部进行处罚；

[E5]
[§ 6.4 安全生产违章行为处罚]
6.4.5 集团公司在检查中发现项目的违章行为，对二级单位和项目部同时进行处罚；

[E6]
[§ 6.4 安全生产违章行为处罚]
1、在安全条件不具备的情况下，强令作业人员冒险作业的；

[E7]
[§ 6.4 安全生产违章行为处罚]
5、易燃易爆品未单独设置仓库的；或未按有关规定在施工现场设置消防通道、配备消防设施和灭火器材的；

[E8]
[§ 6.4 安全生产违章行为处罚]
7、未按规定在施工现场危险部位设置明显的安全警示标志；

[E9]
[§ 6.4 安全生产违章行为处罚]
1、未对本项
```

## latest_clean_niche_0460 (niche_fact)

**Query:** 根据《附件_安全管理规定（2020版）》中“6.8 危险源监控管理”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 473 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 9 | 7 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L376` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C21` kind=`collect` section=`real_69c60974d4242eda8c47c615:L375` scope=`None` depth=`0`
- reason: Collect section 6.8 to retrieve all regulations on hazard source monitoring as requested.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L375']
- collect added=7 hits=7 branch_selected=True collect_full=True
- legal_actions (49):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0632
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0632
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0534
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0534
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0534
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0632
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0632
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0632
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0632
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0632
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0611
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0611
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0575
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0575
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0575
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0611
- projection_chars: 3591

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains all relevant sections of 6.8 Hazard Source Monitoring Management.
- legal_actions (49):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0632
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0632
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0534
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0534
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0534
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0632
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0632
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0632
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0632
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0632
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L104 | 2.4.7 隐患整改（控制或变更降低安全风险）措施的优先顺序： | score=0.0487
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L104 | 2.4.7 隐患整改（控制或变更降低安全风险）措施的优先顺序： | score=0.0487
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L108 | 4、标志、警告和管理控制措施：安全标志、危险区域标识、警告器或警告灯、报警器、安全规程、设备检修、作业安全制度、操作牌和作业许可证等； | score=0.0487
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0611
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0611
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0575
- projection_chars: 3580

### Evidence text (new)

```
[E1]
[§ 6.8 危险源监控管理]
  6.8.2 危险源辨识应根据施工作业活动、施工作业流程和施工工艺，采用科学合理的辨识方法，辨识方法见《危险源辨识、风险评价与控制程序》，项目部对管辖区域和施工现场可能存在的危险源进行分析辨识，列出危险源清单。
  6.8.3 对已辨识出来的危险源采用定性和定量评价，分析导致事故发生的可能性和事故后果，确定风险等级及重大危险源，列出重大危险源清单。
  6.8.4 根据重大危险源清单，制定管理方案，明确重大危险源的目标、指标、控制措施，并落实相关部门及专人负责监督、管理。
  6.8.5 加强对重大危险源的巡查和监控，采取相应的预防及控制措施，消除或降低其影响，使其达到可接受的程度，保证集团公司职业健康安全管理目标的实现。
  6.8.6 项目部应在工地醒目位置设立“不可接受风险公示牌”（见集团公司《施工现场标准化管理手册》），公示牌应注明危险源、存在部位、作业时间、防护措施和责任人等内容。
  6.8.7二级单位、项目部应随所管区域变化和工程施工的进度及时进行更新对危险源辨识和风险评价。
```

### Evidence text (old)

```
[E1]
[§ 第六章　项目安全管理规定 / 6.8 危险源监控管理]
6.8.5 加强对重大危险源的巡查和监控，采取相应的预防及控制措施，消除或降低其影响，使其达到可接受的程度，保证集团公司职业健康安全管理目标的实现。

[E2]
安全管理规定（2020版）

[E3]
[§ 第六章　项目安全管理规定 / 6.8 危险源监控管理]
6.8.4 根据重大危险源清单，制定管理方案，明确重大危险源的目标、指标、控制措施，并落实相关部门及专人负责监督、管理。

[E4]
[§ 第六章　项目安全管理规定 / 6.8 危险源监控管理]
6.8.7二级单位、项目部应随所管区域变化和工程施工的进度及时进行更新对危险源辨识和风险评价。

[E5]
[§ 第六章　项目安全管理规定 / 6.8 危险源监控管理]
6.8.3 对已辨识出来的危险源采用定性和定量评价，分析导致事故发生的可能性和事故后果，确定风险等级及重大危险源，列出重大危险源清单。

[E6]
[§ 第八章　附　则]
8.1本规定由集团公司安全管理部负责持续改进及解释。

[E7]
[§ 第六章　项目安全管理规定 / 6.8 危险源监控管理]
```

## latest_clean_niche_0473 (niche_fact)

**Query:** 根据《附件_安全管理规定（2020版）》中“6.10 施工机具管理”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 488 | 489 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 13 | 7 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L391` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C22` kind=`collect` section=`real_69c60974d4242eda8c47c615:L390` scope=`None` depth=`0`
- reason: Collect section 6.10 Construction Machinery Management to answer the query.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L390']
- collect added=9 hits=9 branch_selected=True collect_full=True
- legal_actions (46):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0526
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0526
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0526
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0526
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0526
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0655
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0655
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0592
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L178 | 5.1 总则 | score=0.0592
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L181 | 5.1.3 项目部（使用单位）必须在机械租赁合同中明确约定：建筑机械的检查、维护、保养由机械出租方负责。 | score=0.0592
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L185 | 根据工程特点及周围环境制定机械设备安全技术操作规程，设置安全警示标志；安全技术操作规程及警示标志应按照《施工现场标准化管理手册》要求制成标志牌悬挂在相应机械设备的醒目位置。 | score=0.0533
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0526
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0526
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L193 | 附表5.2.2：《施工现场安全负面清单（2019版）》 | score=0.0526
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L193 | 附表5.2.2：《施工现场安全负面清单（2019版）》 | score=0.0526
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L196 | 5.2.4 租赁施工升降机和800KN·m及以下的塔式起重机时，应选用租赁安装维修保养一体化的专业承包企业；对800KN·m以上的塔式起重机出租单位，当其不具备相应的起重设备安装工程专业承包资质的，项目经理部必须在签订租赁合同的同时，与出租、安装单位共同签订三方安全管理协议书，并与安装单位签订安拆合同，并明确各方的安全生产权利与义务。 | score=0.0526
- projection_chars: 3508

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Section G1 contains all relevant facts from 6.10 Construction Machinery Management.
- legal_actions (52):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0525
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0525
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0525
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0525
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0525
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0525
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L56 | 1、安全技术交底、安全措施是否落实到施工作业中； | score=0.0525
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0512
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0512
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0512
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0512
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0512
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0526
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0526
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0526
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0526
- projection_chars: 3316

### Evidence text (new)

```
[E1]
[§ 6.10 施工机具管理]
  6.10.2 项目部材料动力组负责施工机具的日常检查及定期检查工作。检查依据：《建筑施工安全检查标准JGJ59-2011》，《建筑机械使用安全技术规程JGJ33-2012》，《施工现场机械设备检查技术规程JGJ160-2008》。
  6.10.3 项目部材料动力组负责施工机具的安装调试，施工机具安装完毕后由项目部组织按规定履行验收程序验收（总包方、分包方、租赁方、安装方、监理方），并应经责任人签字确认。
  6.10.4 项目部自有或租赁的施工机具，负有使用、维护、保养管理工作的义务。但劳务分包，专业分包或租赁的施工机具，合同及安全管理协议书必须明确使用、维护、保养管理工作的责任方。
  6.10.5 施工机具的各种检测仪表及安全装置必须齐全有效，严禁使用安全装置不齐全有效、超过使用年限或技术性能落后耗能高、效率低的施工机具。
  6.10.6 施工机具的现场工作环境必须符合要求，禁止在不适宜的工作环境下使用施工机具。
  6.10.9 施工机具出现故障或异常情况时应立即停机，待故障排除后方可使用，严禁机械带病运转。
```

### Evidence text (old)

```
[E1]
[§ 第五章　施工机械设备管理规定 / 5.4 职责 / 5.4.1 项目部（使用单位）应当履行下列职责：]
8、在机械设备活动范围内设置明显的安全警示标志，对集中作业区做好安全防护；

[E2]
[§ 第五章　施工机械设备管理规定 / 5.3 工具式脚手架管理 / 5.3.4 附着式升降脚手架、高空作业吊篮等管理程序：]
5.3.6 附着式升降脚手架使用工况，升降工况管理必须严格按照专项方案实施。

[E3]
[§ 第五章　施工机械设备管理规定 / 5.5 机械操作]
5.5.3 机械设备出现故障或异常情况时，应当立即停止使用，待故障和安全隐患消除后，方可重新投入使用，严禁机械带病运转。

[E4]
[§ 第五章　施工机械设备管理规定 / 5.2机械设备管理]
5.2.1 严禁自行购置的机械设备（如塔式超重机、施工升降机等）直接租赁给项目部或自行购置的机械设备以单位名义对外出租。

[E5]
[§ 第五章　施工机械设备管理规定 / 5.1 总则]
5.1.3 项目部（使用单位）必须在机械租赁合同中明确约定：建筑机械的检查、维护、保养由机械出租方负责。
```

## latest_clean_niche_0500 (niche_fact)

**Query:** 根据《附件_安全管理规定（2020版）》中“7.2 总平面布局”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 481 | 390 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 8 | 5 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L424` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C28` kind=`collect` section=`real_69c60974d4242eda8c47c615:L423` scope=`None` depth=`0`
- reason: Target section 7.2 Total Layout found with relevant content.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L423']
- collect added=4 hits=4 branch_selected=True collect_full=True
- legal_actions (50):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0647
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0647
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0647
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0647
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0647
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0623
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0623
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0581
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0581
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L90 | 1、一般事故隐患的治理由各项目部根据事故隐患的实际情况，制定针对性的治理措施，落实相关责任人，限期进行整改； | score=0.0581
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0623
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0623
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0623
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0662
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0662
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0585
- projection_chars: 3473

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains all required content from section 7.2 regarding total layout regulations.
- legal_actions (54):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0647
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0647
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0647
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0647
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0647
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0527
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0527
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0527
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0527
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L56 | 1、安全技术交底、安全措施是否落实到施工作业中； | score=0.0527
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0623
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0623
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0581
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0581
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L90 | 1、一般事故隐患的治理由各项目部根据事故隐患的实际情况，制定针对性的治理措施，落实相关责任人，限期进行整改； | score=0.0581
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0623
- projection_chars: 3511

### Evidence text (new)

```
[E1]
[§ 7.2 总平面布局]
  7.2.1 施工现场出入口的设置必须满足消防车通行的要求，并应布置在不同方向，其数量不宜少于2个。当确有困难只能设置1个出入口时，在施工现场内设置满足消防车通行的环形道路，消防车道的净宽度和净空高度均不应小于4米。
  7.2.2 宿舍、厨房操作间、配电室、可燃材料堆场及其加工场、可燃材料及易燃易爆危险品库房等临时用房、临时设施不能设置于在建工程内。
  7.2.3 固定动火作业场要布置在可燃材料堆场及其加工场、易燃易爆危险品库房等全年最小频率风向的上风侧，并宜布置在临时办公用房、宿舍、可燃材料库房、在建工程等全年最小频率风向的上风侧。
  7.2.4 易燃易爆危险品库房与在建工程的防火间距不小于15m，可燃材料堆场及其加工场、固定动火作业场与在建工程的防火间距不小于10m，其它临时用房、临时设施与在建工程的防火间距不小于6m。
```

### Evidence text (old)

```
[E1]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.5 防火管理一般规定]
7.5.3 施工单位(项目部)必须编制施工现场消防应急预案，定期组织消防演练，并根据现场情况变化及时对其修改、完善和持续改进。

[E2]
[§ 第七章　施工现场消防安全管理暂行规定]
为了加强集团公司在建项目施工现场消防管理，保障施工现场生活区、办公区和施工区施工人员生命安全和财产安全。依据《中华人民共和国消防法》、《建设工程施工现场消防安全技术规范》（GB50720—2011）及其他有关消防法规，结合施工现场实际，特制定《集团公司施工现场消防安全管理暂行规定》。

[E3]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.1 总  则]
7.1.6 定期对施工的各类人员进行消防安全教育，提高防火灭火技能。定期进行防火安全大检查，消除火险隐患。

[E4]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.8 其他防火管理]
7.8.1 施工单位(项目部)必须做好施工现场临时消防设施的日常维护工作，对已失效、损坏或丢失的消防设施，必须及时更换、修复或补充。
```

## latest_clean_niche_0510 (niche_fact)

**Query:** 根据《附件_安全管理规定（2020版）》中“7.5 防火管理一般规定”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 423 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 9 | 7 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L437` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C27` kind=`collect` section=`real_69c60974d4242eda8c47c615:L436` scope=`None` depth=`0`
- reason: Collect all leaf nodes under section 7.5 to answer the query about fire management regulations.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L436', 'real_69c60974d4242eda8c47c615:L437', 'real_69c60974d4242eda8c47c615:L438', 'real_69c60974d4242eda8c47c615:L439', 'real_69c60974d4242eda8c47c615:L441', 'real_69c60974d4242eda8c47c615:L442']
- collect added=6 hits=11 branch_selected=False collect_full=True
- legal_actions (49):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0646
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0646
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0580
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0580
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0580
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0646
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0646
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0646
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0646
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L90 | 1、一般事故隐患的治理由各项目部根据事故隐患的实际情况，制定针对性的治理措施，落实相关责任人，限期进行整改； | score=0.0646
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0579
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0579
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0579
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0561
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0561
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0561
- projection_chars: 3390

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains all regulations from section 7.5 regarding fire safety management.
- legal_actions (51):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0646
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0646
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0580
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0580
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0580
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0555
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0555
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0555
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0555
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L53 | 9、根据季节变化，防雷、防暑降温、防火、防台、防汛、防冻保温、防滑等措施的落实情况； | score=0.0555
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0646
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0646
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0646
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0646
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L90 | 1、一般事故隐患的治理由各项目部根据事故隐患的实际情况，制定针对性的治理措施，落实相关责任人，限期进行整改； | score=0.0646
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0579
- projection_chars: 3486

### Evidence text (new)

```
[E1]
[§ 7.5 防火管理一般规定]
  7.5.1 施工现场的消防安全管理由责任单位统一管理，项目部具体负责落实。
  7.5.2 施工单位(项目部)必须根据建设项目规模、现场消防安全管理的重点，制订消防安全管理制度，建立消防安全管理组织机构及义务消防组织，并确定消防安全负责人和消防安全管理人员，同时落实相关人员的消防安全管理责任。
  7.5.3 施工单位(项目部)必须编制施工现场消防应急预案，定期组织消防演练，并根据现场情况变化及时对其修改、完善和持续改进。
  7.5.4 施工人员进场时，施工现场的消防安全管理人员必须向施工人员进行消防安全教育和培训。施工作业前，必须向作业人员进行消防安全技术交底。
  7.5.5 施工过程中，施工现场的消防安全负责人必须定期组织消防安全管理人员对施工现场的消防安全进行检查。
  7.5.6 施工单位(项目部)必须做好并保存施工现场消防安全管理的相关文件和记录，建立现场消防安全管理档案。
```

### Evidence text (old)

```
[E1]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.1 总  则]
7.1.1 本规定适用于集团公司所有在建项目工程施工现场的消防安全管理。

[E2]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.5 防火管理一般规定]
7.5.2 施工单位(项目部)必须根据建设项目规模、现场消防安全管理的重点，制订消防安全管理制度，建立消防安全管理组织机构及义务消防组织，并确定消防安全负责人和消防安全管理人员，同时落实相关人员的消防安全管理责任。

[E3]
[§ 第七章　施工现场消防安全管理暂行规定]
为了加强集团公司在建项目施工现场消防管理，保障施工现场生活区、办公区和施工区施工人员生命安全和财产安全。依据《中华人民共和国消防法》、《建设工程施工现场消防安全技术规范》（GB50720—2011）及其他有关消防法规，结合施工现场实际，特制定《集团公司施工现场消防安全管理暂行规定》。

[E4]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.7 用火、用电、用气管理 / 7.7.1 施工现场用火管理]
3、焊接、切割、烘烤或加热等动火作业，必须配备灭火器材，并设动火监护人进行
```

## latest_clean_niche_0519 (niche_fact)

**Query:** 根据《附件_安全管理规定（2020版）》中“7.7.1 施工现场用火管理”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 356 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 10 | 7 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L449` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C33` kind=`collect` section=`real_69c60974d4242eda8c47c615:L448` scope=`None` depth=`0`
- reason: Target section 7.7.1 explicitly contains the required regulations on fire management.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L448']
- collect added=6 hits=6 branch_selected=True collect_full=True
- legal_actions (51):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0537
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0537
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0537
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0537
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0537
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0616
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0616
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L233 | 5.4 职责 | score=0.0616
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L233 | 5.4 职责 | score=0.0616
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L234 | 5.4.1 项目部（使用单位）应当履行下列职责： | score=0.0616
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L234 | 5.4.1 项目部（使用单位）应当履行下列职责： | score=0.0616
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L241 | 7、根据不同施工阶段、周围环境以及季节、气候的变化，及时督促出租单位采取相应的安全防护措施； | score=0.0616
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L262 | 第六章　项目安全管理规定 | score=0.0572
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L262 | 第六章　项目安全管理规定 | score=0.0572
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L314 | 6.4 安全生产违章行为处罚 | score=0.0522
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L314 | 6.4 安全生产违章行为处罚 | score=0.0522
- projection_chars: 3496

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Section G1 contains all required regulations for 7.7.1施工现场用火管理.
- legal_actions (46):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0537
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0537
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0537
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0537
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0537
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0616
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0616
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L233 | 5.4 职责 | score=0.0616
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L233 | 5.4 职责 | score=0.0616
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L234 | 5.4.1 项目部（使用单位）应当履行下列职责： | score=0.0616
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L234 | 5.4.1 项目部（使用单位）应当履行下列职责： | score=0.0616
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L241 | 7、根据不同施工阶段、周围环境以及季节、气候的变化，及时督促出租单位采取相应的安全防护措施； | score=0.0616
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L262 | 第六章　项目安全管理规定 | score=0.0572
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L262 | 第六章　项目安全管理规定 | score=0.0572
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L314 | 6.4 安全生产违章行为处罚 | score=0.0522
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L314 | 6.4 安全生产违章行为处罚 | score=0.0522
- projection_chars: 3192

### Evidence text (new)

```
[E1]
[§ 7.7.1 施工现场用火管理]
  1、施工现场动火作业必须办理动火许可证；动火操作人员必须具有相应资格；
  2、施工现场在进行焊接、切割、烘烤或加热等动火作业前，必须对作业现场的可燃物进行清理；对于作业现场及其附近无法移走的可燃物，必须采用不燃材料对其覆盖或隔离；裸露的可燃材料上严禁直接进行动火作业；
  3、焊接、切割、烘烤或加热等动火作业，必须配备灭火器材，并设动火监护人进行现场一对一监护；
  4、五级（含五级）以上风力时，必须停止焊接、切割等室外动火作业，否则必须采取可靠的挡风措施；
  5、动火作业后，必须对现场进行检查，确认无火灾危险后，动火操作人员方可离开；
  6、施工现场不应采用明火取暖；厨房操作间炉灶使用完毕后，必须将炉火熄灭，排油烟机及油烟管道必须定期清理油垢。
```

### Evidence text (old)

```
[E1]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.1 总  则]
7.1.1 本规定适用于集团公司所有在建项目工程施工现场的消防安全管理。

[E2]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.7 用火、用电、用气管理 / 7.7.1 施工现场用火管理]
3、焊接、切割、烘烤或加热等动火作业，必须配备灭火器材，并设动火监护人进行现场一对一监护；

[E3]
[§ 第七章　施工现场消防安全管理暂行规定]
为了加强集团公司在建项目施工现场消防管理，保障施工现场生活区、办公区和施工区施工人员生命安全和财产安全。依据《中华人民共和国消防法》、《建设工程施工现场消防安全技术规范》（GB50720—2011）及其他有关消防法规，结合施工现场实际，特制定《集团公司施工现场消防安全管理暂行规定》。

[E4]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.5 防火管理一般规定]
7.5.1 施工现场的消防安全管理由责任单位统一管理，项目部具体负责落实。

[E5]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.7 用火、用电、用气管理 / 7.7.2 施工现场用电管理
```

## latest_clean_niche_0525 (niche_fact)

**Query:** 根据《附件_安全管理规定（2020版）》中“7.7.2 施工现场用电管理”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 414 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 10 | 7 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L456` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C30` kind=`collect` section=`real_69c60974d4242eda8c47c615:L455` scope=`None` depth=`0`
- reason: Target section 7.7.2 contains the specific regulations on construction site electricity management requested.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L455']
- collect added=6 hits=6 branch_selected=True collect_full=True
- legal_actions (49):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0561
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0561
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0561
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0561
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L146 | 3.7 集团公司生产安全事故实行月度报告制度。各基层单位的安全管理部门应当每月、年度末及时填报《职工伤亡事故月（年）报表》（附表3.7-1）；每月报送《工程项目安全跟踪监控记录表》（附表3.7-2）；每季度、年度末对安全生产情况进行统计分析并填写《安全生产信息统计报表》（附表3.7-3）。经本单位负责人签字确认后，上报集团公司安全管理部（电子版事故报表经电子签名后通过梦龙发送至集团公司安全管理部相 | score=0.0561
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0627
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0627
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L233 | 5.4 职责 | score=0.0627
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L233 | 5.4 职责 | score=0.0627
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L234 | 5.4.1 项目部（使用单位）应当履行下列职责： | score=0.0627
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L234 | 5.4.1 项目部（使用单位）应当履行下列职责： | score=0.0627
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L241 | 7、根据不同施工阶段、周围环境以及季节、气候的变化，及时督促出租单位采取相应的安全防护措施； | score=0.0627
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L262 | 第六章　项目安全管理规定 | score=0.0644
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L262 | 第六章　项目安全管理规定 | score=0.0644
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L314 | 6.4 安全生产违章行为处罚 | score=0.0644
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L314 | 6.4 安全生产违章行为处罚 | score=0.0644
- projection_chars: 3261

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Section G1 contains all explicit regulations for 7.7.2施工现场用电管理 as requested.
- legal_actions (52):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0529
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0529
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0529
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0529
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0529
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0529
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0529
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0561
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0561
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0561
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0561
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L146 | 3.7 集团公司生产安全事故实行月度报告制度。各基层单位的安全管理部门应当每月、年度末及时填报《职工伤亡事故月（年）报表》（附表3.7-1）；每月报送《工程项目安全跟踪监控记录表》（附表3.7-2）；每季度、年度末对安全生产情况进行统计分析并填写《安全生产信息统计报表》（附表3.7-3）。经本单位负责人签字确认后，上报集团公司安全管理部（电子版事故报表经电子签名后通过梦龙发送至集团公司安全管理部相 | score=0.0561
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0627
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0627
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L233 | 5.4 职责 | score=0.0627
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L233 | 5.4 职责 | score=0.0627
- projection_chars: 3443

### Evidence text (new)

```
[E1]
[§ 7.7.2 施工现场用电管理]
  1、电气线路必须具有相应的绝缘强度和机械强度，破损、烧焦的插座、插头应及时更换；
  2、电气设备与可燃、易燃易爆和腐蚀性物品保持一定的安全距离；
  3、有爆炸和火灾危险的场所，按危险等级选用相应的电气设备，电气设备不能超负荷运行或带故障使用；
  4、配电箱内每个电气回路必须设置漏电保护器、过载保护器，距配电箱2m范围内不能堆放可燃物，5m范围内不能设置可能产生较多易燃、易爆气体、粉尘的作业区；
  5、可燃材料库房不能使用高热灯具，易燃易爆危险品库房内必须使用防爆灯具，普通灯具与易燃物距离不小于300mm，聚光灯、碘钨灯等高热灯具与易燃物距离不宜小于500mm；
  6、施工现场办公、生活区和施工区禁止私自改装现场供用电设施，严禁在宿舍使用不合格的电褥子、大功率热水器等电器。项目部必须定期对办公、生活区和施工区安全用电、电气设备和线路的运行及维护情况进行检查。
```

### Evidence text (old)

```
[E1]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.5 防火管理一般规定]
7.5.1 施工现场的消防安全管理由责任单位统一管理，项目部具体负责落实。

[E2]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.7 用火、用电、用气管理 / 7.7.1 施工现场用火管理]
2、施工现场在进行焊接、切割、烘烤或加热等动火作业前，必须对作业现场的可燃物进行清理；对于作业现场及其附近无法移走的可燃物，必须采用不燃材料对其覆盖或隔离；裸露的可燃材料上严禁直接进行动火作业；

[E3]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.4 临时消防设施]
7.4.1 施工现场必须设置灭火器、临时消防给水系统和临时消防应急照明等临时消防设施。

[E4]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.7 用火、用电、用气管理 / 7.7.3 施工现场用气管理]
（4）储装气体的罐瓶及其附件应合格、完好和有效；严禁使用减压器及其他附件缺损的氧气瓶，严禁使用乙炔专用减压器、回火防止器及其他附件缺损的乙炔瓶（强条）。

[E5]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.
```

## latest_clean_niche_0531 (niche_fact)

**Query:** 根据《附件_安全管理规定（2020版）》中“7.7.3 施工现场用气管理”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 478 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 9 | 11 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L464` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C31` kind=`collect` section=`real_69c60974d4242eda8c47c615:L462` scope=`None` depth=`0`
- reason: Target section 7.7.3 contains specific rules on gas management in construction sites.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L462']
- collect added=14 hits=14 branch_selected=True collect_full=True
- legal_actions (52):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0529
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0529
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0529
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0529
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0529
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0529
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0529
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0561
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0561
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0561
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0561
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0561
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0550
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0550
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L146 | 3.7 集团公司生产安全事故实行月度报告制度。各基层单位的安全管理部门应当每月、年度末及时填报《职工伤亡事故月（年）报表》（附表3.7-1）；每月报送《工程项目安全跟踪监控记录表》（附表3.7-2）；每季度、年度末对安全生产情况进行统计分析并填写《安全生产信息统计报表》（附表3.7-3）。经本单位负责人签字确认后，上报集团公司安全管理部（电子版事故报表经电子签名后通过梦龙发送至集团公司安全管理部相 | score=0.0550
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0672
- projection_chars: 3583

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: The assembled evidence G1 fully contains the specific regulations for section 7.7.3 regarding site gas management.
- legal_actions (53):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0529
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0529
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0529
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0529
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0529
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0529
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0529
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0561
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0561
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0561
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0561
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0561
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0550
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0550
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L146 | 3.7 集团公司生产安全事故实行月度报告制度。各基层单位的安全管理部门应当每月、年度末及时填报《职工伤亡事故月（年）报表》（附表3.7-1）；每月报送《工程项目安全跟踪监控记录表》（附表3.7-2）；每季度、年度末对安全生产情况进行统计分析并填写《安全生产信息统计报表》（附表3.7-3）。经本单位负责人签字确认后，上报集团公司安全管理部（电子版事故报表经电子签名后通过梦龙发送至集团公司安全管理部相 | score=0.0550
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0672
- projection_chars: 3544

### Evidence text (new)

```
[E1]
[§ 7.7.3 施工现场用气管理]
  1、 焊接、切割用氧气、乙炔瓶
  （2）气瓶的钢印和颜色标记清晰，确保瓶帽和防震圈的完好，禁止粘有油脂。
  （3）气瓶间安全距离不少于5米，与明火安全距离不应少于10米。
  （4）储装气体的罐瓶及其附件应合格、完好和有效；严禁使用减压器及其他附件缺损的氧气瓶，严禁使用乙炔专用减压器、回火防止器及其他附件缺损的乙炔瓶（强条）。
  （5）使用时乙炔瓶与氧气瓶应直立放置，采取可靠防倾倒措施。防止乙炔瓶倾倒丙酮流出。
  （6）气瓶内的气体不能全部用完，氧气瓶的氧气要留有0.1MPa以上压力，乙炔瓶内的乙炔最后必须留有0.05MPa以上压力，并将瓶阀关紧，防止漏气或可燃气体进入。
  （7）搬运气瓶时，必须使用专用的小车并固定牢固，严禁碰撞、敲打、抛掷、滚动。不得将氧气瓶放在地上滚动；乙炔瓶不应受到剧烈震动和撞击，避免引起乙炔瓶爆炸。
  2、二保焊用二氧化碳气瓶
  （1）应放在阴凉、干燥的地方，不得超过30摄氏度，远离明火等热源。
  （4）不得超量充装，填充量不要超过钢瓶溶积的75％。
```

### Evidence text (old)

```
[E1]
[§ 第七章　施工现场消防安全管理暂行规定]
为了加强集团公司在建项目施工现场消防管理，保障施工现场生活区、办公区和施工区施工人员生命安全和财产安全。依据《中华人民共和国消防法》、《建设工程施工现场消防安全技术规范》（GB50720—2011）及其他有关消防法规，结合施工现场实际，特制定《集团公司施工现场消防安全管理暂行规定》。

[E2]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.7 用火、用电、用气管理 / 7.7.3 施工现场用气管理]
（6）气瓶内的气体不能全部用完，氧气瓶的氧气要留有0.1MPa以上压力，乙炔瓶内的乙炔最后必须留有0.05MPa以上压力，并将瓶阀关紧，防止漏气或可燃气体进入。

[E3]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.5 防火管理一般规定]
7.5.3 施工单位(项目部)必须编制施工现场消防应急预案，定期组织消防演练，并根据现场情况变化及时对其修改、完善和持续改进。

[E4]
[§ 第七章　施工现场消防安全管理暂行规定 / 7.7 用火、用电、用气管理 / 7.7.2 施工现场用电管理]
2、电气设备与可燃、易燃易爆
```

## latest_clean_niche_0551 (niche_fact)

**Query:** 根据《附件_安全管理规定（2020版）》中“3.2 生产安全事故快报”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 498 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 11 | 21 |
| trajectory_steps | n/a | 3 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L493` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C33` kind=`collect` section=`real_69c60974d4242eda8c47c615:L492` scope=`None` depth=`0`
- reason: Section 3.2 explicitly contains the 'Production Safety Accident Quick Report' content requested.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L492']
- collect added=51 hits=51 branch_selected=True collect_full=True
- legal_actions (55):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0629
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0629
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0545
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0545
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0545
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0505
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0505
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0505
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0505
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L54 | 10、各类事故是否按“四不放过”的原则进行处理，是否有隐瞒不报情况。 | score=0.0505
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0629
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0629
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0540
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0540
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L90 | 1、一般事故隐患的治理由各项目部根据事故隐患的实际情况，制定针对性的治理措施，落实相关责任人，限期进行整改； | score=0.0540
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0629
- projection_chars: 3481

**Step 2** `nav_collect`  id=`C15` kind=`collect` section=`real_69c60974d4242eda8c47c615:L116` scope=`None` depth=`0`
- reason: Collect section 3.2 to retrieve specific regulations on production safety accident rapid reporting.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L116']
- collect added=10 hits=10 branch_selected=True collect_full=True
- legal_actions (53):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0629
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0629
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0545
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0545
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0545
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0505
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0505
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0505
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0505
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L54 | 10、各类事故是否按“四不放过”的原则进行处理，是否有隐瞒不报情况。 | score=0.0505
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0629
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0629
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0540
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0540
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L90 | 1、一般事故隐患的治理由各项目部根据事故隐患的实际情况，制定针对性的治理措施，落实相关责任人，限期进行整改； | score=0.0540
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0629
- projection_chars: 3527

**Step 3** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 and G2 contain the specific regulations for '3.2 生产安全事故快报' including reporting content and the fast report form.
- legal_actions (50):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0629
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0629
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0545
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0545
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0545
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0505
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0505
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0505
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0505
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L54 | 10、各类事故是否按“四不放过”的原则进行处理，是否有隐瞒不报情况。 | score=0.0505
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0629
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0629
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0540
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0540
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L90 | 1、一般事故隐患的治理由各项目部根据事故隐患的实际情况，制定针对性的治理措施，落实相关责任人，限期进行整改； | score=0.0540
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0629
- projection_chars: 3576

### Evidence text (new)

```
[E1]
[§ 3.2 事故报告]
  事故发生后，事故现场负责人应当立即向集团公司负责人报告；集团公司负责人接到报告后，按照《生产安全事故报告和调查处理条例》的规定，在1小时内向事故发生地安全生产监督管理局、建设主管部门、陕建集团总公司等部门逐级报告。
  在报告的同时，应当及时编制《生产安全事故快报表》（见附表3.2）报陕建集团总公司安全监管部门。
  生产安全事故报告的内容应包括：
  1 事故的时间、地点和工程项目有关单位名称；
  2 事故的简要经过；
  3 事故已经造成或者可能造成的伤亡人数（包括下落不明的人数）和初步估计的直接经济损失；
  4 事故的初步原因；
  5 事故发生后采取的措施及事故控制情况；
  6 事故报告单位或报告人员；
  生产安全事故报告后出现新情况的，应及时补报。

[E2]
[§ 附表3.2]
  生产安全事故快报
  单位名称：

[E3]
[§ 3.2 生产安全事故快报]
  3.7-1 职工伤亡事故月（年）报表
  3.7-3 安全生产信息季（年）度报表
  4.3.1 应急预案演练方案

[E4]
[§ 附表1.2-3]
工程名称
```

### Evidence text (old)

```
[E1]
[§ 3.2 事故报告]
生产安全事故报告后出现新情况的，应及时补报。

[E2]
[§ 3.2 事故报告]
在报告的同时，应当及时编制《生产安全事故快报表》（见附表3.2）报陕建集团总公司安全监管部门。

[E3]
[§ 3.2 事故报告]
5 事故发生后采取的措施及事故控制情况；

[E4]
[§ 3.2 事故报告]
生产安全事故报告的内容应包括：

[E5]
[§ 3.2 事故报告]
1 事故的时间、地点和工程项目有关单位名称；

[E6]
[§ 3.2 事故报告]
事故发生后，事故现场负责人应当立即向集团公司负责人报告；集团公司负责人接到报告后，按照《生产安全事故报告和调查处理条例》的规定，在1小时内向事故发生地安全生产监督管理局、建设主管部门、陕建集团总公司等部门逐级报告。

[E7]
[§ 3.2 事故报告]
3 事故已经造成或者可能造成的伤亡人数（包括下落不明的人数）和初步估计的直接经济损失；

[E8]
[§ 3.2 事故报告]
6 事故报告单位或报告人员；

[E9]
[§ 3.2 事故报告]
2 事故的简要经过；

[E10]
[§ 3.2 事故报告]
4
```

## latest_clean_niche_0553 (niche_fact)

**Query:** 根据《附件_安全管理规定（2020版）》中“4.3.2 应急预案演练评价报”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 297 | 462 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 4 | 11 |
| trajectory_steps | n/a | 8 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L497` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C13` kind=`collect` section=`real_69c60974d4242eda8c47c615:L167` scope=`None` depth=`0`
- reason: Section 4.3.2 explicitly details the requirements for the emergency plan drill evaluation report.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L167']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (53):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0595
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0595
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0595
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0595
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0595
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0578
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0578
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L146 | 3.7 集团公司生产安全事故实行月度报告制度。各基层单位的安全管理部门应当每月、年度末及时填报《职工伤亡事故月（年）报表》（附表3.7-1）；每月报送《工程项目安全跟踪监控记录表》（附表3.7-2）；每季度、年度末对安全生产情况进行统计分析并填写《安全生产信息统计报表》（附表3.7-3）。经本单位负责人签字确认后，上报集团公司安全管理部（电子版事故报表经电子签名后通过梦龙发送至集团公司安全管理部相 | score=0.0578
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L151 | 第四章　安全生产事故应急救援管理规定 | score=0.0732
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L151 | 第四章　安全生产事故应急救援管理规定 | score=0.0732
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L152 | 4.1 组织机构与职责 | score=0.0624
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L152 | 4.1 组织机构与职责 | score=0.0624
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L153 | 4.1.1集团公司应急救援管理包括建立组织机构，应急预案编制、审批、演练、评价、完善和应急救援响应工作程序。 | score=0.0624
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L157 | 4.2 应急救援预案 | score=0.0582
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L157 | 4.2 应急救援预案 | score=0.0582
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L158 | 4.2.1 应急救援预案应包括以下内容： | score=0.0582
- projection_chars: 3203

**Step 2** `nav_collect`  id=`C27` kind=`collect` section=`real_69c60974d4242eda8c47c615:L496` scope=`None` depth=`0`
- reason: Section N27 explicitly contains the title '4.3.2 应急预案演练评价报' which is the target of the query.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L496']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (53):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0595
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0595
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0595
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0595
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0595
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0578
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0578
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L146 | 3.7 集团公司生产安全事故实行月度报告制度。各基层单位的安全管理部门应当每月、年度末及时填报《职工伤亡事故月（年）报表》（附表3.7-1）；每月报送《工程项目安全跟踪监控记录表》（附表3.7-2）；每季度、年度末对安全生产情况进行统计分析并填写《安全生产信息统计报表》（附表3.7-3）。经本单位负责人签字确认后，上报集团公司安全管理部（电子版事故报表经电子签名后通过梦龙发送至集团公司安全管理部相 | score=0.0578
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L151 | 第四章　安全生产事故应急救援管理规定 | score=0.0732
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L151 | 第四章　安全生产事故应急救援管理规定 | score=0.0732
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L152 | 4.1 组织机构与职责 | score=0.0624
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L152 | 4.1 组织机构与职责 | score=0.0624
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L153 | 4.1.1集团公司应急救援管理包括建立组织机构，应急预案编制、审批、演练、评价、完善和应急救援响应工作程序。 | score=0.0624
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L157 | 4.2 应急救援预案 | score=0.0582
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L157 | 4.2 应急救援预案 | score=0.0582
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L158 | 4.2.1 应急救援预案应包括以下内容： | score=0.0582
- projection_chars: 3065

**Step 3** `nav_collect`  id=`C22` kind=`collect` section=`real_69c60974d4242eda8c47c615:L176` scope=`None` depth=`0`
- reason: Collect section C22 (4.3.2 Evaluation Report) to retrieve the specific content of the regulation.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L176']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (58):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0540
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0540
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0540
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0540
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0540
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0540
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L103 | 2.4.6 各项目部应当加强对自然灾害的预防。对于因自然灾害可能导致事故灾难的隐患，应当按照有关法律、法规、标准和本制度的要求排查治理，采取可靠的预防措施，制定应急预案。在接到有关自然灾害预报时，应当及时向有关人员发出预警通知；发生自然灾害可能危及施工和人员安全的情况时，应当采取撤离人员、停止作业、加强监测等安全措施，并及时向当地人民政府有关部门报告。 | score=0.0540
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0595
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0595
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0595
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0595
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0595
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0578
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0578
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L146 | 3.7 集团公司生产安全事故实行月度报告制度。各基层单位的安全管理部门应当每月、年度末及时填报《职工伤亡事故月（年）报表》（附表3.7-1）；每月报送《工程项目安全跟踪监控记录表》（附表3.7-2）；每季度、年度末对安全生产情况进行统计分析并填写《安全生产信息统计报表》（附表3.7-3）。经本单位负责人签字确认后，上报集团公司安全管理部（电子版事故报表经电子签名后通过梦龙发送至集团公司安全管理部相 | score=0.0578
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L151 | 第四章　安全生产事故应急救援管理规定 | score=0.0732
- projection_chars: 3480

**Step 4** `nav_collect`  id=`C37` kind=`collect` section=`real_69c60974d4242eda8c47c615:L542` scope=`None` depth=`0`
- reason: Collect section C37 (4.3.2 Evaluation Report) to retrieve the specific regulations requested.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L542']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (58):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0540
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0540
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0540
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0540
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0540
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0540
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L103 | 2.4.6 各项目部应当加强对自然灾害的预防。对于因自然灾害可能导致事故灾难的隐患，应当按照有关法律、法规、标准和本制度的要求排查治理，采取可靠的预防措施，制定应急预案。在接到有关自然灾害预报时，应当及时向有关人员发出预警通知；发生自然灾害可能危及施工和人员安全的情况时，应当采取撤离人员、停止作业、加强监测等安全措施，并及时向当地人民政府有关部门报告。 | score=0.0540
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0595
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0595
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0595
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0595
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0595
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0578
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0578
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L146 | 3.7 集团公司生产安全事故实行月度报告制度。各基层单位的安全管理部门应当每月、年度末及时填报《职工伤亡事故月（年）报表》（附表3.7-1）；每月报送《工程项目安全跟踪监控记录表》（附表3.7-2）；每季度、年度末对安全生产情况进行统计分析并填写《安全生产信息统计报表》（附表3.7-3）。经本单位负责人签字确认后，上报集团公司安全管理部（电子版事故报表经电子签名后通过梦龙发送至集团公司安全管理部相 | score=0.0578
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L151 | 第四章　安全生产事故应急救援管理规定 | score=0.0732
- projection_chars: 3514

**Step 5** `nav_collect`  id=`C19` kind=`collect` section=`real_69c60974d4242eda8c47c615:L168` scope=`None` depth=`0`
- reason: Section C19 (4.3.3) contains the specific rule regarding revision of emergency plans based on evaluation reports.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L168']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (57):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0540
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0540
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0540
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0540
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0540
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0540
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L103 | 2.4.6 各项目部应当加强对自然灾害的预防。对于因自然灾害可能导致事故灾难的隐患，应当按照有关法律、法规、标准和本制度的要求排查治理，采取可靠的预防措施，制定应急预案。在接到有关自然灾害预报时，应当及时向有关人员发出预警通知；发生自然灾害可能危及施工和人员安全的情况时，应当采取撤离人员、停止作业、加强监测等安全措施，并及时向当地人民政府有关部门报告。 | score=0.0540
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0595
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0595
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0595
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0595
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0595
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0578
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0578
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L146 | 3.7 集团公司生产安全事故实行月度报告制度。各基层单位的安全管理部门应当每月、年度末及时填报《职工伤亡事故月（年）报表》（附表3.7-1）；每月报送《工程项目安全跟踪监控记录表》（附表3.7-2）；每季度、年度末对安全生产情况进行统计分析并填写《安全生产信息统计报表》（附表3.7-3）。经本单位负责人签字确认后，上报集团公司安全管理部（电子版事故报表经电子签名后通过梦龙发送至集团公司安全管理部相 | score=0.0578
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L151 | 第四章　安全生产事故应急救援管理规定 | score=0.0732
- projection_chars: 3444

**Step 6** `nav_collect`  id=`C17` kind=`collect` section=`real_69c60974d4242eda8c47c615:L165` scope=`None` depth=`0`
- reason: Collect section 4.3 to access the full content of 4.3.2 regarding emergency plan evaluation reports.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L165']
- collect added=3 hits=3 branch_selected=True collect_full=True
- legal_actions (56):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0540
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0540
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0540
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0540
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0540
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0540
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L103 | 2.4.6 各项目部应当加强对自然灾害的预防。对于因自然灾害可能导致事故灾难的隐患，应当按照有关法律、法规、标准和本制度的要求排查治理，采取可靠的预防措施，制定应急预案。在接到有关自然灾害预报时，应当及时向有关人员发出预警通知；发生自然灾害可能危及施工和人员安全的情况时，应当采取撤离人员、停止作业、加强监测等安全措施，并及时向当地人民政府有关部门报告。 | score=0.0540
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0595
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0595
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0595
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0595
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0595
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0578
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0578
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L146 | 3.7 集团公司生产安全事故实行月度报告制度。各基层单位的安全管理部门应当每月、年度末及时填报《职工伤亡事故月（年）报表》（附表3.7-1）；每月报送《工程项目安全跟踪监控记录表》（附表3.7-2）；每季度、年度末对安全生产情况进行统计分析并填写《安全生产信息统计报表》（附表3.7-3）。经本单位负责人签字确认后，上报集团公司安全管理部（电子版事故报表经电子签名后通过梦龙发送至集团公司安全管理部相 | score=0.0578
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L151 | 第四章　安全生产事故应急救援管理规定 | score=0.0732
- projection_chars: 3344

**Step 7** `nav_collect`  id=`C35` kind=`collect` section=`real_69c60974d4242eda8c47c615:L541` scope=`None` depth=`0`
- reason: Collect section D20 (4.3.2) to retrieve the specific content of the emergency plan drill evaluation report.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L541']
- collect added=2 hits=2 branch_selected=True collect_full=True
- legal_actions (56):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0540
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0540
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0540
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0540
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0540
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0540
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0507
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L103 | 2.4.6 各项目部应当加强对自然灾害的预防。对于因自然灾害可能导致事故灾难的隐患，应当按照有关法律、法规、标准和本制度的要求排查治理，采取可靠的预防措施，制定应急预案。在接到有关自然灾害预报时，应当及时向有关人员发出预警通知；发生自然灾害可能危及施工和人员安全的情况时，应当采取撤离人员、停止作业、加强监测等安全措施，并及时向当地人民政府有关部门报告。 | score=0.0540
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0595
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0595
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0595
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0595
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0595
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0578
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0578
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L146 | 3.7 集团公司生产安全事故实行月度报告制度。各基层单位的安全管理部门应当每月、年度末及时填报《职工伤亡事故月（年）报表》（附表3.7-1）；每月报送《工程项目安全跟踪监控记录表》（附表3.7-2）；每季度、年度末对安全生产情况进行统计分析并填写《安全生产信息统计报表》（附表3.7-3）。经本单位负责人签字确认后，上报集团公司安全管理部（电子版事故报表经电子签名后通过梦龙发送至集团公司安全管理部相 | score=0.0578
- projection_chars: 3514

**Step 8** `nav_collect`  id=`C31` kind=`collect` section=`real_69c60974d4242eda8c47c615:L540` scope=`None` depth=`0`
- reason: Collect section C31 to retrieve the specific content of '4.3.2 应急预案演练评价报' as it is currently missing from evidence.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L540']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (32):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0540
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0540
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0540
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0507
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L103 | 2.4.6 各项目部应当加强对自然灾害的预防。对于因自然灾害可能导致事故灾难的隐患，应当按照有关法律、法规、标准和本制度的要求排查治理，采取可靠的预防措施，制定应急预案。在接到有关自然灾害预报时，应当及时向有关人员发出预警通知；发生自然灾害可能危及施工和人员安全的情况时，应当采取撤离人员、停止作业、加强监测等安全措施，并及时向当地人民政府有关部门报告。 | score=0.0540
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0595
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0595
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0595
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0578
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L146 | 3.7 集团公司生产安全事故实行月度报告制度。各基层单位的安全管理部门应当每月、年度末及时填报《职工伤亡事故月（年）报表》（附表3.7-1）；每月报送《工程项目安全跟踪监控记录表》（附表3.7-2）；每季度、年度末对安全生产情况进行统计分析并填写《安全生产信息统计报表》（附表3.7-3）。经本单位负责人签字确认后，上报集团公司安全管理部（电子版事故报表经电子签名后通过梦龙发送至集团公司安全管理部相 | score=0.0578
  - C11 | COLLECT | real_69c60974d4242eda8c47c615:L152 | 4.1 组织机构与职责 | score=0.0624
  - C12 | COLLECT | real_69c60974d4242eda8c47c615:L153 | 4.1.1集团公司应急救援管理包括建立组织机构，应急预案编制、审批、演练、评价、完善和应急救援响应工作程序。 | score=0.0624
  - C13 | COLLECT | real_69c60974d4242eda8c47c615:L156 | 4.1.4 集团公司编制生产安全事故的综合应急救援预案，二级单位编制本单位的应急救援预案，项目部编制项目应急救援预案。 | score=0.0519
  - C14 | COLLECT | real_69c60974d4242eda8c47c615:L157 | 4.2 应急救援预案 | score=0.0582
  - C15 | COLLECT | real_69c60974d4242eda8c47c615:L158 | 4.2.1 应急救援预案应包括以下内容： | score=0.0582
  - C16 | COLLECT | real_69c60974d4242eda8c47c615:L164 | 4.2.2 集团公司的综合应急救援预案经集团公司正式发布后生效。二级单位应急救援预案报集团公司安全管理部备案，项目部各种应急救援预案报二级单位备案。 | score=0.0539
- projection_chars: 3176

### Evidence text (new)

```
[E1]
[§ 4.3 应急救援预案的演练]
  4.3.1 集团公司的综合应急救援预案每二年演练一次；项目部根据工程特点，项目施工（基础，主体，装饰）阶段，每年至少演练一次。演练必须编制演练方案（附表4.3.1：应急预案演练方案），并对参演人员进行宣传培训。
  4.3.2 演练结束后，演练组织部门对应急救援预案和处置程序的有效性、人员宣传培训和需求、设备和资源的充分性、应急救援行动以及是否达到预期目标作出评价报告（附表4.3.2：应急预案演练评价报告），交集团公司安全管理部存档。
  4.3.3 根据规范要求变化，应急预案环境改变，演练评价报告每一到二年修订应急救援预案。

[E2]
[§ 4.4 应急响应程序]
附表4.3.2：应急预案演练评价报告。

[E3]
[§ 附表4.3.2]
  应急预案演练评价报告
  工程名称：

[E4]
[§ 附表4.3.1]
注：应急预案演练记录照片或影像资料附后。

[E5]
[§ 4.3.2 应急预案演练评价报]
5.2.2：《施工现场安全负面清单（2019版）》
```

### Evidence text (old)

```
[E1]
4.3.2 演练结束后，演练组织部门对应急救援预案和处置程序的有效性、人员宣传培训和需求、设备和资源的充分性、应急救援行动以及是否达到预期目标作出评价报告（附表4.3.2：应急预案演练评价报告），交集团公司安全管理部存档。

[E2]
[§ 4.3 应急救援预案的演练]
4.3.3 根据规范要求变化，应急预案环境改变，演练评价报告每一到二年修订应急救援预案。

[E3]
4.3.1 集团公司的综合应急救援预案每二年演练一次；项目部根据工程特点，项目施工（基础，主体，装饰）阶段，每年至少演练一次。演练必须编制演练方案（附表4.3.1：应急预案演练方案），并对参演人员进行宣传培训。
```

## latest_clean_niche_0554 (niche_fact)

**Query:** 根据《附件_安全管理规定（2020版）》中“6.7.3 安全技术交底记录”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 362 | 171 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 6 | 5 |
| trajectory_steps | n/a | 5 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L505` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C21` kind=`collect` section=`real_69c60974d4242eda8c47c615:L374` scope=`None` depth=`0`
- reason: Section 6.7.3 explicitly states the signing and record-keeping requirements for safety technical disclosure.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L374']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (60):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0600
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0600
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0600
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0600
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0600
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0600
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L56 | 1、安全技术交底、安全措施是否落实到施工作业中； | score=0.0600
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0593
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0593
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0491
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0491
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0491
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0593
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0593
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L146 | 3.7 集团公司生产安全事故实行月度报告制度。各基层单位的安全管理部门应当每月、年度末及时填报《职工伤亡事故月（年）报表》（附表3.7-1）；每月报送《工程项目安全跟踪监控记录表》（附表3.7-2）；每季度、年度末对安全生产情况进行统计分析并填写《安全生产信息统计报表》（附表3.7-3）。经本单位负责人签字确认后，上报集团公司安全管理部（电子版事故报表经电子签名后通过梦龙发送至集团公司安全管理部相 | score=0.0593
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0520
- projection_chars: 3415

**Step 2** `nav_collect`  id=`C37` kind=`collect` section=`real_69c60974d4242eda8c47c615:L560` scope=`None` depth=`0`
- reason: Collect section C37 (6.7.3 Safety Technical Disclosure Record) to retrieve the specific content of the regulation.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L560']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (60):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0600
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0600
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0600
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0600
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0600
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0600
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L56 | 1、安全技术交底、安全措施是否落实到施工作业中； | score=0.0600
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0593
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0593
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0491
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0491
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0491
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0593
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0593
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L146 | 3.7 集团公司生产安全事故实行月度报告制度。各基层单位的安全管理部门应当每月、年度末及时填报《职工伤亡事故月（年）报表》（附表3.7-1）；每月报送《工程项目安全跟踪监控记录表》（附表3.7-2）；每季度、年度末对安全生产情况进行统计分析并填写《安全生产信息统计报表》（附表3.7-3）。经本单位负责人签字确认后，上报集团公司安全管理部（电子版事故报表经电子签名后通过梦龙发送至集团公司安全管理部相 | score=0.0593
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0520
- projection_chars: 3314

**Step 3** `nav_collect`  id=`C39` kind=`collect` section=`real_69c60974d4242eda8c47c615:L559` scope=`None` depth=`0`
- reason: Collect section C39 (附表6.7.3) to retrieve the specific content of the safety technical disclosure record form.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L559']
- collect added=2 hits=2 branch_selected=True collect_full=True
- legal_actions (64):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0600
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0600
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0600
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0600
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0600
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0600
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L56 | 1、安全技术交底、安全措施是否落实到施工作业中； | score=0.0600
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0593
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0593
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0491
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0491
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0491
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0593
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0593
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L146 | 3.7 集团公司生产安全事故实行月度报告制度。各基层单位的安全管理部门应当每月、年度末及时填报《职工伤亡事故月（年）报表》（附表3.7-1）；每月报送《工程项目安全跟踪监控记录表》（附表3.7-2）；每季度、年度末对安全生产情况进行统计分析并填写《安全生产信息统计报表》（附表3.7-3）。经本单位负责人签字确认后，上报集团公司安全管理部（电子版事故报表经电子签名后通过梦龙发送至集团公司安全管理部相 | score=0.0593
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0520
- projection_chars: 3457

**Step 4** `nav_collect`  id=`C27` kind=`collect` section=`real_69c60974d4242eda8c47c615:L413` scope=`None` depth=`0`
- reason: Collect section 6.7.3 to retrieve the specific content of the safety technical disclosure record form.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L413']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (59):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0600
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0600
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0600
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0600
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0600
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0600
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L56 | 1、安全技术交底、安全措施是否落实到施工作业中； | score=0.0600
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0593
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0593
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0491
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0491
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0491
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0593
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0593
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L146 | 3.7 集团公司生产安全事故实行月度报告制度。各基层单位的安全管理部门应当每月、年度末及时填报《职工伤亡事故月（年）报表》（附表3.7-1）；每月报送《工程项目安全跟踪监控记录表》（附表3.7-2）；每季度、年度末对安全生产情况进行统计分析并填写《安全生产信息统计报表》（附表3.7-3）。经本单位负责人签字确认后，上报集团公司安全管理部（电子版事故报表经电子签名后通过梦龙发送至集团公司安全管理部相 | score=0.0593
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0520
- projection_chars: 3352

**Step 5** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence collected covers §6.7.3 requirements: signature confirmation by交底人,被交底人,专职安全员 and record preservation.
- legal_actions (59):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0600
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0600
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0600
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0600
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0600
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0600
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L56 | 1、安全技术交底、安全措施是否落实到施工作业中； | score=0.0600
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0593
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0593
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0491
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L130 | 3.4 事故处理 | score=0.0491
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L131 | 3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。 | score=0.0491
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0593
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0593
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L146 | 3.7 集团公司生产安全事故实行月度报告制度。各基层单位的安全管理部门应当每月、年度末及时填报《职工伤亡事故月（年）报表》（附表3.7-1）；每月报送《工程项目安全跟踪监控记录表》（附表3.7-2）；每季度、年度末对安全生产情况进行统计分析并填写《安全生产信息统计报表》（附表3.7-3）。经本单位负责人签字确认后，上报集团公司安全管理部（电子版事故报表经电子签名后通过梦龙发送至集团公司安全管理部相 | score=0.0593
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0520
- projection_chars: 3358

### Evidence text (new)

```
[E1]
[§ 6.7 安全技术交底管理]
6.7.3 安全技术交底应由交底人、被交底人、专职安全员进行签字确认。并由项目部专职安全员保存安全技术交底记录（附表6.7.3 安全技术交底记录）。

[E2]
[§ 6.11 安全标志]
附表6.7.3：安全技术交底记录。

[E3]
[§ 附表6.7.3]
  安全技术交底记录
  工程名称：
```

### Evidence text (old)

```
[E1]
6.7.3 安全技术交底应由交底人、被交底人、专职安全员进行签字确认。并由项目部专职安全员保存安全技术交底记录（附表6.7.3 安全技术交底记录）。

[E2]
[§ 6.7 安全技术交底管理]
6.7.2 施工负责人（项目生产经理、施工员等）在分派生产任务时，应对相关管理人员、施工作业人员进行书面安全技术交底。

[E3]
安全技术交底应结合施工季节、施工作业场所状况、工程特点、工序，对危险因素、施工方案、规范标准、操作规程和应急措施进行交底。

[E4]
[§ 6.7 安全技术交底管理]
6.7.1 工程开工前，以及结构复杂的分部分项工程实施前，项目部的技术负责人应对项目管理人员进行安全技术交底。

[E5]
[§ 6.7 安全技术交底管理]
安全技术交底应按施工工序、施工部位、施工栋号分部分项进行。
```

## latest_clean_niche_0567 (niche_fact)

**Query:** 根据《附件_安全管理规定（2020版）》中“附件5.2.2 施工现场安全负面清单（2019版）”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 304 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 17 | 4 |
| trajectory_steps | n/a | 5 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L545` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C35` kind=`collect` section=`real_69c60974d4242eda8c47c615:L545` scope=`None` depth=`0`
- reason: Directly contains the specific facts and regulations of Appendix 5.2.2 regarding negative list items.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L545']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (56):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0640
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0640
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0640
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0640
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0640
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0640
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L49 | 5、施工现场管理行为和实物状况（安全隐患排查、安全设施及安全防护等各项措施和落实情况）； | score=0.0640
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0586
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0586
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0586
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0586
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0586
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0683
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0683
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0683
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0683
- projection_chars: 3540

**Step 2** `nav_collect`  id=`C34` kind=`collect` section=`real_69c60974d4242eda8c47c615:L544` scope=`None` depth=`0`
- reason: Collect the specific content of Attachment 5.2.2 to answer the query about explicit regulations.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L544']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (55):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0640
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0640
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0640
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0640
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0640
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0640
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L49 | 5、施工现场管理行为和实物状况（安全隐患排查、安全设施及安全防护等各项措施和落实情况）； | score=0.0640
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0586
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0586
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0586
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0586
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0586
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0683
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0683
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0683
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0683
- projection_chars: 3437

**Step 3** `nav_collect`  id=`C32` kind=`collect` section=`real_69c60974d4242eda8c47c615:L497` scope=`None` depth=`0`
- reason: Collect leaf C32 to retrieve the specific content of 'Attachment 5.2.2' as requested.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L497']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (54):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0640
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0640
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0640
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0640
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0640
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0640
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L49 | 5、施工现场管理行为和实物状况（安全隐患排查、安全设施及安全防护等各项措施和落实情况）； | score=0.0640
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0586
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0586
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0586
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0586
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0586
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0683
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L177 | 第五章　施工机械设备管理规定 | score=0.0683
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0683
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L186 | 5.2机械设备管理 | score=0.0683
- projection_chars: 3340

**Step 4** `nav_collect`  id=`C13` kind=`collect` section=`real_69c60974d4242eda8c47c615:L189` scope=`None` depth=`0`
- reason: Section C13 explicitly references the 'Negative List' and its usage restrictions, directly addressing the query.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L189']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (57):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0640
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0640
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0640
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0640
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0640
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0640
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L49 | 5、施工现场管理行为和实物状况（安全隐患排查、安全设施及安全防护等各项措施和落实情况）； | score=0.0640
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0586
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0586
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0586
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0586
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0586
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0549
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0549
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0549
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0549
- projection_chars: 3633

**Step 5** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence collected covers the specific regulations and facts from Attachment 5.2.2 regarding the negative list.
- legal_actions (57):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0640
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0640
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0640
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0640
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0640
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L44 | 2.2.1集团公司、二级单位、项目部安全检查的主要内容： | score=0.0640
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L49 | 5、施工现场管理行为和实物状况（安全隐患排查、安全设施及安全防护等各项措施和落实情况）； | score=0.0640
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0586
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0586
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0586
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0586
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L102 | 2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。 | score=0.0586
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0549
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L113 | 第三章　生产安全事故报告处理规定 | score=0.0549
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0549
  - D7 | DISPATCH | real_69c60974d4242eda8c47c615:L143 | 3.5 分析改进 | score=0.0549
- projection_chars: 3570

### Evidence text (new)

```
[E1]
[§ 附件5.2.2                     施工现场安全负面清单（2]
文档列出使用不合格防坠器、超年限设备及维护不到位等问题的分包单位名单，并详细规定了塔吊、升降机、脚手架及临电设施等禁止或淘汰的技术标准与依据。

[E2]
[§ 5.2机械设备管理]
5.2.2 严禁租赁集团公司《施工现场安全负面清单（2019版）》（见附表5.2-2）中禁止及限制使用的施工机械；租赁机械设备时，要求选择注册资金不小于200万元人民币的租赁单位，拟租起重机械机械使用年限应符合以下规定：

[E3]
[§ 4.3.2 应急预案演练评价报]
5.2.2：《施工现场安全负面清单（2019版）》
```

### Evidence text (old)

```
[E1]
附件_安全管理规定（2020版）.docx

[E2]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表6.6.1-1]
备注： 本表中所列工程，若本工程施工中有时在对应的辨识结论栏内打“√”，无时打“×”。

[E3]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表4.3.1]
工程名称：

[E4]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.4 隐患整改 / 2.4.4 重大事故隐患整改、复查、销项]
5、治理的时限和要求；

[E5]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表3.2]
单位名称：

[E6]
[§ 附件_安全管理规定（2020版）.docx / 第三章　生产安全事故报告处理规定 / 3.5 分析改进]
附表3.2：生
```

## latest_clean_niche_0572 (niche_fact)

**Query:** 根据《附件_安全管理规定（2020版）》中“附表6.6.1-2”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 53 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 18 | 1 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L556` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C31` kind=`collect` section=`real_69c60974d4242eda8c47c615:L412` scope=`None` depth=`0`
- reason: Target section '附表6.6.1-2' is explicitly listed as a leaf node.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L412']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (53):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0573
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0573
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0573
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0573
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0573
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0536
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0536
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0536
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0536
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L56 | 1、安全技术交底、安全措施是否落实到施工作业中； | score=0.0536
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0519
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0519
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0478
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0478
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L90 | 1、一般事故隐患的治理由各项目部根据事故隐患的实际情况，制定针对性的治理措施，落实相关责任人，限期进行整改； | score=0.0478
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0519
- projection_chars: 3474

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains the specific content of Appendix 6.6.1-2 as requested.
- legal_actions (54):
  - C1 | COLLECT | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0573
  - D1 | DISPATCH | real_69c60974d4242eda8c47c615:L39 | 第二章　安全检查及隐患排查规定 | score=0.0573
  - C2 | COLLECT | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0573
  - D2 | DISPATCH | real_69c60974d4242eda8c47c615:L40 | 2.1总则 | score=0.0573
  - C3 | COLLECT | real_69c60974d4242eda8c47c615:L41 | 2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。 | score=0.0573
  - C4 | COLLECT | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0536
  - D3 | DISPATCH | real_69c60974d4242eda8c47c615:L43 | 2.2  安全检查及隐患排查内容 | score=0.0536
  - C5 | COLLECT | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0536
  - D4 | DISPATCH | real_69c60974d4242eda8c47c615:L55 | 2.2.2班组安全检查的内容： | score=0.0536
  - C6 | COLLECT | real_69c60974d4242eda8c47c615:L56 | 1、安全技术交底、安全措施是否落实到施工作业中； | score=0.0536
  - C7 | COLLECT | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0519
  - D5 | DISPATCH | real_69c60974d4242eda8c47c615:L81 | 2.4 隐患整改 | score=0.0519
  - C8 | COLLECT | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0478
  - D6 | DISPATCH | real_69c60974d4242eda8c47c615:L89 | 2.4.3 一般事故隐患整改、复查、销项 | score=0.0478
  - C9 | COLLECT | real_69c60974d4242eda8c47c615:L90 | 1、一般事故隐患的治理由各项目部根据事故隐患的实际情况，制定针对性的治理措施，落实相关责任人，限期进行整改； | score=0.0478
  - C10 | COLLECT | real_69c60974d4242eda8c47c615:L92 | 2.4.4 重大事故隐患整改、复查、销项 | score=0.0519
- projection_chars: 3609

### Evidence text (new)

```
[E1]
[§ 6.11 安全标志]
附表6.6.1-2：超过一定规模的危险性较大的分部分项工程识别清单；
```

### Evidence text (old)

```
[E1]
附件_安全管理规定（2020版）.docx

[E2]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表6.6.1-1]
工程名称：

[E3]
[§ 附件_安全管理规定（2020版）.docx / 第一章　安全教育培训规定 / 1.7 附则]
附表1：安全教育记录；

[E4]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.2  安全检查及隐患排查内容 / 2.2.2班组安全检查的内容：]
6、其他应检查的内容。

[E5]
[§ 附件_安全管理规定（2020版）.docx / 第二章　安全检查及隐患排查规定 / 2.3安全检查及隐患排查的方法 / 2.3.3 定期安全检查]
附表2-3-3《项目周检查标准化表格》

[E6]
[§ 附件_安全管理规定（2020版）.docx / 第八章　附　则 / 3.2 生产安全事故快报 / 6.7.3 安全技术交底记录 / 附表1.1.1]
编号：

[E7]
[§ 附件_安全管理规定（2020
```

## latest_clean_niche_0600 (niche_fact)

**Query:** 根据《陕西建工第十一建集团有限公司生产安全事故综合应急预案（2025版）》中“1.2 编制依据”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c6097ad4242eda8c47c62c`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 480 | 350 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 11 | 12 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c6097ad4242eda8c47c62c:L6` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C4` kind=`collect` section=`real_69c6097ad4242eda8c47c62c:L4` scope=`None` depth=`0`
- reason: Collect section 1.2 '编制依据' to retrieve the listed regulations and facts.
- collect_section_ids: ['real_69c6097ad4242eda8c47c62c:L4']
- collect added=11 hits=11 branch_selected=True collect_full=True
- legal_actions (50):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0656
  - D1 | DISPATCH | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0656
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L2 | 1.1 编制目的 | score=0.0558
  - D2 | DISPATCH | real_69c6097ad4242eda8c47c62c:L2 | 1.1 编制目的 | score=0.0558
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L3 | 为加强集团公司处置生产安全事故的能力，提高应对突发事件的反应速度和协调水平，确保集团公司应急体系有效运行，及时迅速处置各类生产安全事故，将损失降至最低程度，保障人员生命财产安全，维护集团公司正常的生产秩序和社会秩序，促进企业可持续发展，特制定本《预案》。 | score=0.0558
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L4 | 1.2 编制依据 | score=0.0656
  - D3 | DISPATCH | real_69c6097ad4242eda8c47c62c:L4 | 1.2 编制依据 | score=0.0656
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L9 | 5 、《陕西省突发公共事件总体应急预案》 | score=0.0570
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L11 | 7、《生产经营单位安全生产事故应急预案编制导则》（GB/T29639-2020） | score=0.0582
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L12 | 8 、《生产安全事故应急演练评估规范》（AQ/T9009-2015 ） | score=0.0519
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L13 | 9 、《陕西建工集团股份有限公司生产安全事故综合应急预案》 | score=0.0656
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L14 | 10 、《陕西建工第十一建设集团有限公司生产安全事故风险评估报告》 | score=0.0634
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L15 | 11 、《陕西建工第十一建设集团有限公司生产安全事故应急资源调查报告》 | score=0.0637
  - C11 | COLLECT | real_69c6097ad4242eda8c47c62c:L16 | 1.3 适用范围 | score=0.0537
  - D4 | DISPATCH | real_69c6097ad4242eda8c47c62c:L16 | 1.3 适用范围 | score=0.0537
  - C12 | COLLECT | real_69c6097ad4242eda8c47c62c:L17 | 本《预案》适用于集团公司、二级单位及项目经理部所承建工程施工现场发生的坍塌、高处坠落、物体打击、触电、起重伤害、机械伤害、车辆伤害、中毒与窒息、火灾、灼烫、容器爆炸、其他伤害等较大及其以上各类生产安全事故，同时包括有重大社会影响、涉及公共安全或突发事件应急处置工作的应急救援。 | score=0.0537
- projection_chars: 3424

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Section G1 contains the complete list of regulations and facts under '1.2 编制依据' as requested.
- legal_actions (49):
  - D1 | DISPATCH | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0656
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L2 | 1.1 编制目的 | score=0.0558
  - D2 | DISPATCH | real_69c6097ad4242eda8c47c62c:L2 | 1.1 编制目的 | score=0.0558
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L3 | 为加强集团公司处置生产安全事故的能力，提高应对突发事件的反应速度和协调水平，确保集团公司应急体系有效运行，及时迅速处置各类生产安全事故，将损失降至最低程度，保障人员生命财产安全，维护集团公司正常的生产秩序和社会秩序，促进企业可持续发展，特制定本《预案》。 | score=0.0558
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L16 | 1.3 适用范围 | score=0.0537
  - D3 | DISPATCH | real_69c6097ad4242eda8c47c62c:L16 | 1.3 适用范围 | score=0.0537
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L17 | 本《预案》适用于集团公司、二级单位及项目经理部所承建工程施工现场发生的坍塌、高处坠落、物体打击、触电、起重伤害、机械伤害、车辆伤害、中毒与窒息、火灾、灼烫、容器爆炸、其他伤害等较大及其以上各类生产安全事故，同时包括有重大社会影响、涉及公共安全或突发事件应急处置工作的应急救援。 | score=0.0537
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0638
  - D4 | DISPATCH | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0638
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L19 | 根据国务院第493 号令《生产安全事故报告和调查处理条例》规定， 结合集团公司实际，按照“企业自救、行业互救、社会联动、逐级响应、分级负责”的原则，建立集团公司、二级单位、项目经理部三级响应的应急救援体系。 | score=0.0638
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0626
  - D5 | DISPATCH | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0626
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0615
  - D6 | DISPATCH | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0615
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L61 | 1 、组织有关部门制定生产安全事故应急预案、演练计划及应急能力评估； | score=0.0495
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L62 | 2 、根据事故发生情况，决定是否发布启动或终止预案的命令，统一部署应急救援预案的实施工作，并对应急救援工作中发生的争议采取紧急处置措施； | score=0.0615
- projection_chars: 3523

### Evidence text (new)

```
[E1]
[§ 1.2 编制依据]
  6 、《咸阳市突发公共事件总体应急预案》
  7、《生产经营单位安全生产事故应急预案编制导则》（GB/T29639-2020）
  8 、《生产安全事故应急演练评估规范》（AQ/T9009-2015 ）
  9 、《陕西建工集团股份有限公司生产安全事故综合应急预案》
  10 、《陕西建工第十一建设集团有限公司生产安全事故风险评估报告》
  11 、《陕西建工第十一建设集团有限公司生产安全事故应急资源调查报告》
  1 、《中华人民共和国安全生产法》
  2 、《中华人民共和国突发事件应对法》
  3 、《生产安全事故应急演练指南》（AQ/T9007-2019）
  4 、《生产安全事故报告和调查处理条例》
  5 、《陕西省突发公共事件总体应急预案》
```

### Evidence text (old)

```
[E1]
[§ 1.2 编制依据]
11 、《陕西建工第十一建设集团有限公司生产安全事故应急资源调查报告》

[E2]
[§ 1.2 编制依据]
9 、《陕西建工集团股份有限公司生产安全事故综合应急预案》

[E3]
[§ 1.2 编制依据]
10 、《陕西建工第十一建设集团有限公司生产安全事故风险评估报告》

[E4]
[§ 1.2 编制依据]
5 、《陕西省突发公共事件总体应急预案》

[E5]
[§ 1.2 编制依据]
4 、《生产安全事故报告和调查处理条例》

[E6]
[§ 1.2 编制依据]
1 、《中华人民共和国安全生产法》

[E7]
[§ 1.2 编制依据]
7、《生产经营单位安全生产事故应急预案编制导则》（GB/T29639-2020）

[E8]
[§ 1.2 编制依据]
8 、《生产安全事故应急演练评估规范》（AQ/T9009-2015 ）

[E9]
[§ 1.2 编制依据]
3 、《生产安全事故应急演练指南》（AQ/T9007-2019）

[E10]
[§ 1.2 编制依据]
6 、《咸阳市突发公共事件总体应急预案》
```

## latest_clean_niche_0657 (niche_fact)

**Query:** 根据《陕西建工第十一建集团有限公司生产安全事故综合应急预案（2025版）》中“2.4 集团公司应急救援总指挥部部门职责”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c6097ad4242eda8c47c62c`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 495 | 496 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 10 | 17 |
| trajectory_steps | n/a | 4 |

### Gold node hits (new)

- `real_69c6097ad4242eda8c47c62c:L79` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6097ad4242eda8c47c62c:L77` scope=`real_69c6097ad4242eda8c47c62c:L77` depth=`1`
- reason: Collects the full section 2.4 to retrieve all department responsibilities as requested.
- collect_section_ids: ['real_69c6097ad4242eda8c47c62c:L77']
- collect added=46 hits=46 branch_selected=True collect_full=True
- legal_actions (18):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L77 | 2.4 集团公司应急救援总指挥部部门职责 | score=0.0607
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L79 | 1 、负责配合政府有关部门做好事故的调查处理工作； | score=0.0468
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L81 | 3 、负责指导项目部建立现场生产安全事故应急救援预案； | score=0.0476
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L82 | 4 、协调解决预案执行过程中出现的问题； | score=0.0429
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L83 | 5 、负责协调集团公司较大及其以上生产安全事故、火灾、爆炸事故的 | score=0.0439
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L85 | 6 、负责协调生产安全事故中受伤人员的抢救治疗工作； | score=0.0436
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L89 | 1 、协助组织实施集团公司生产安全事故应急救援预案； | score=0.0541
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L90 | 2、组织、调度实施集团公司生产安全事故应急救援预案的人员、材料、 设备和其他资源的相互配合； | score=0.0607
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L94 | 2 、负责集团公司生产安全事故现场处置、现场恢复的技术支持。 | score=0.0474
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L100 | 3 、负责确定事故伤亡人数和伤亡人员的姓名、身份； | score=0.0451
  - C11 | COLLECT | real_69c6097ad4242eda8c47c62c:L102 | 1 、参与事故的应急救援和事故处理工作； | score=0.0426
  - C12 | COLLECT | real_69c6097ad4242eda8c47c62c:L105 | 1 、负责配合政府有关部门维持现场秩序、做好事故区域的警戒，有关人员的紧急疏散、撤离等； | score=0.0395
  - C13 | COLLECT | real_69c6097ad4242eda8c47c62c:L106 | 2 、负责有关事故直接责任人的监护； | score=0.0415
  - C14 | COLLECT | real_69c6097ad4242eda8c47c62c:L108 | 4 、负责与相关救助机构的联系工作。 | score=0.0449
  - C15 | COLLECT | real_69c6097ad4242eda8c47c62c:L110 | 负责事故应急处理中法律法规资料的收集，为事故处理提供法律支持。 | score=0.0476
  - C16 | COLLECT | real_69c6097ad4242eda8c47c62c:L115 | 负责协调处理生产安全事故对企业可能造成影响的内外部沟通工作。 | score=0.0475
- projection_chars: 2385

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c6097ad4242eda8c47c62c:L77` depth=`1`
- reason: The required section '2.4 集团公司应急救援总指挥部部门职责' has been collected in the previous step. No further collection is needed.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 189

**Step 3** `nav_dispatch`  id=`D7` kind=`dispatch` section=`real_69c6097ad4242eda8c47c62c:L77` scope=`None` depth=`0`
- reason: Dispatch section 2.4 to retrieve all department responsibilities under the emergency command headquarters.
- dispatch_regions: ['real_69c6097ad4242eda8c47c62c:L77']
- child_reports=1 skipped=0
- legal_actions (49):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0584
  - D1 | DISPATCH | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0584
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0584
  - D2 | DISPATCH | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0584
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L19 | 根据国务院第493 号令《生产安全事故报告和调查处理条例》规定， 结合集团公司实际，按照“企业自救、行业互救、社会联动、逐级响应、分级负责”的原则，建立集团公司、二级单位、项目经理部三级响应的应急救援体系。 | score=0.0584
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0688
  - D3 | DISPATCH | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0688
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L38 | 2.1 应急组织体系 | score=0.0493
  - D4 | DISPATCH | real_69c6097ad4242eda8c47c62c:L38 | 2.1 应急组织体系 | score=0.0493
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L39 | 生产安全事故应急救援工作在集团公司统一领导下，各二级单位、各有关职能部门分工合作、各司其职、密切配合，迅速、高效、有序开展。 集团设立生产安全事故应急救援指挥部，其组成如下： | score=0.0493
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0688
  - D5 | DISPATCH | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0688
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L61 | 1 、组织有关部门制定生产安全事故应急预案、演练计划及应急能力评估； | score=0.0526
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L62 | 2 、根据事故发生情况，决定是否发布启动或终止预案的命令，统一部署应急救援预案的实施工作，并对应急救援工作中发生的争议采取紧急处置措施； | score=0.0688
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L69 | 2.3 集团公司应急救援副总指挥的职责 | score=0.0610
  - D6 | DISPATCH | real_69c6097ad4242eda8c47c62c:L69 | 2.3 集团公司应急救援副总指挥的职责 | score=0.0610
- projection_chars: 3432

**Step 4** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Section 2.4 department responsibilities fully collected and ranked by relevance.
- legal_actions (49):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0584
  - D1 | DISPATCH | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0584
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0584
  - D2 | DISPATCH | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0584
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L19 | 根据国务院第493 号令《生产安全事故报告和调查处理条例》规定， 结合集团公司实际，按照“企业自救、行业互救、社会联动、逐级响应、分级负责”的原则，建立集团公司、二级单位、项目经理部三级响应的应急救援体系。 | score=0.0584
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L25 | （4）超出自身应急救援能力范围的事故，上级部门要求集团公司配合进行应急处置的各类安全生产事故。 | score=0.0445
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L32 | （2）超出自身应急救援能力范围的事故，上级部门要求集团公司配合进行应急处置的各类安全生产事故。 | score=0.0438
  - D3 | DISPATCH | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0688
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L38 | 2.1 应急组织体系 | score=0.0493
  - D4 | DISPATCH | real_69c6097ad4242eda8c47c62c:L38 | 2.1 应急组织体系 | score=0.0493
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L39 | 生产安全事故应急救援工作在集团公司统一领导下，各二级单位、各有关职能部门分工合作、各司其职、密切配合，迅速、高效、有序开展。 集团设立生产安全事故应急救援指挥部，其组成如下： | score=0.0493
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L57 | 集团公司应急救援总指挥部 | score=0.0445
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0688
  - D5 | DISPATCH | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0688
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L61 | 1 、组织有关部门制定生产安全事故应急预案、演练计划及应急能力评估； | score=0.0526
  - C11 | COLLECT | real_69c6097ad4242eda8c47c62c:L62 | 2 、根据事故发生情况，决定是否发布启动或终止预案的命令，统一部署应急救援预案的实施工作，并对应急救援工作中发生的争议采取紧急处置措施； | score=0.0688
- projection_chars: 3589

### Subagent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c6097ad4242eda8c47c62c:L77 (ok)
collected 47 branch node(s); explicit roots=['real_69c6097ad4242eda8c47c62c:L77']
collected: real_69c6097ad4242eda8c47c62c:L100, real_69c6097ad4242eda8c47c62c:L101, real_69c6097ad4242eda8c47c62c:L102, real_69c6097ad4242eda8c47c62c:L103, real_69c6097ad4242eda8c47c62c:L104, real_69c6097ad4242eda8c47c62c:L105, real_69c6097ad4242eda8c47c62c:L106, real_69c6097ad4242eda8c47c62c:L107, real_69c6097ad4242eda8c47c62c:L108, real_69c6097ad4242eda8c47c62c:L109, real_69c6097ad4242eda8c47c62c:L110, real_69c6097ad4242eda8c47c62c:L111, real_69c6097ad4242eda8c47c62c:L112, real_69c6097ad4242eda8c47c62c:L113, real_69c6097ad4242eda8c47c62c:L114, real_69c6097ad4242eda8c47c62c:L115, real_69c6097ad4242eda8c47c62c:L116, real_69c6097ad4242eda8c47c62c:L117, real_69c6097ad4242eda8c47c62c:L118, real_69c6097ad4242eda8c47c62c:L119
reason: The required section '2.4 集团公司应急救援总指挥部部门职责' has been collected in the previous step. No further collection is needed.
---
=== End Investigate ===
```

### Evidence text (new)

```
[E1]
[§ 2.4 集团公司应急救援总指挥部部门职责]
  3 、负责确定事故伤亡人数和伤亡人员的姓名、身份；
  1 、参与事故的应急救援和事故处理工作；
  2 、负责有关事故直接责任人的监护；
  4 、负责与相关救助机构的联系工作。
  负责事故应急处理中法律法规资料的收集，为事故处理提供法律支持。
  负责协调处理生产安全事故对企业可能造成影响的内外部沟通工作。
  1 、参与生产安全事故的应急处置工作；
  1 、参与配合实施集团总部生产安全事故应急救援预案；
  1 、负责配合政府有关部门做好事故的调查处理工作；
  3 、负责指导项目部建立现场生产安全事故应急救援预案；
  4 、协调解决预案执行过程中出现的问题；
  5 、负责协调集团公司较大及其以上生产安全事故、火灾、爆炸事故的
  6 、负责协调生产安全事故中受伤人员的抢救治疗工作；
  1 、协助组织实施集团公司生产安全事故应急救援预案；
  2、组织、调度实施集团公司生产安全事故应急救援预案的人员、材料、 设备和其他资源的相互配合；
  2 、负责集团公司生产安全事故现场处置、现场恢复的技术支持。
```

### Evidence text (old)

```
[E1]
[§ 2.4 集团公司应急救援总指挥部部门职责]
1 、协助组织实施集团公司生产安全事故应急救援预案；

[E2]
[§ 2.2 集团公司应急救援总指挥的职责]
1 、组织有关部门制定生产安全事故应急预案、演练计划及应急能力评估；

[E3]
[§ 2.4 集团公司应急救援总指挥部部门职责]
1 、协助组织审核生产安全事故应急救援预案；

[E4]
[§ 2.4 集团公司应急救援总指挥部部门职责]
1 、参与配合实施集团总部生产安全事故应急救援预案；

[E5]
[§ 2.4 集团公司应急救援总指挥部部门职责]
5 、负责协调集团公司较大及其以上生产安全事故、火灾、爆炸事故的

[E6]
[§ 2.4 集团公司应急救援总指挥部部门职责]
2、组织、调度实施集团公司生产安全事故应急救援预案的人员、材料、 设备和其他资源的相互配合；

[E7]
[§ 2.4 集团公司应急救援总指挥部部门职责]
负责协调处理生产安全事故对企业可能造成影响的内外部沟通工作。

[E8]
[§ 2.4 集团公司应急救援总指挥部部门职责]
3 、负责指导项目部建立现场生产安全事故应急救援预案；
```

## latest_clean_niche_0690 (niche_fact)

**Query:** 根据《陕西建工第十一建集团有限公司生产安全事故综合应急预案（2025版）》中“2.5 二级单位应急救援领导小组成员职责”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c6097ad4242eda8c47c62c`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 479 | 500 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 8 | 13 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c6097ad4242eda8c47c62c:L126` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C14` kind=`collect` section=`real_69c6097ad4242eda8c47c62c:L124` scope=`None` depth=`0`
- reason: Target section 2.5 contains the specific duties of secondary unit emergency rescue leadership group members.
- collect_section_ids: ['real_69c6097ad4242eda8c47c62c:L124']
- collect added=27 hits=27 branch_selected=True collect_full=True
- legal_actions (44):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0570
  - D1 | DISPATCH | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0570
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0570
  - D2 | DISPATCH | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0570
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L19 | 根据国务院第493 号令《生产安全事故报告和调查处理条例》规定， 结合集团公司实际，按照“企业自救、行业互救、社会联动、逐级响应、分级负责”的原则，建立集团公司、二级单位、项目经理部三级响应的应急救援体系。 | score=0.0570
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0670
  - D3 | DISPATCH | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0670
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L38 | 2.1 应急组织体系 | score=0.0637
  - D4 | DISPATCH | real_69c6097ad4242eda8c47c62c:L38 | 2.1 应急组织体系 | score=0.0637
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L39 | 生产安全事故应急救援工作在集团公司统一领导下，各二级单位、各有关职能部门分工合作、各司其职、密切配合，迅速、高效、有序开展。 集团设立生产安全事故应急救援指挥部，其组成如下： | score=0.0527
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L51 | 各二级单位成立相应的生产安全事故应急救援领导小组，下设抢救抢险组、技术支持组、医疗救护组、通信联络组、后勤保障组和善后处置组。 组长由二级单位总经理担任，副组长由总工程师、生产副总经理（安全总监）担任，组员由生产安全管理部、经营预算部、技术管理部、综合办公室、财务管理服务中心各工程公司财务部等职能部门负责人组成。 | score=0.0637
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L52 | 二级单位抢救抢险组组员为生产安全管理部成员；技术支持组组员为技术管理部成员； 医疗救护组、通信联络组组员为综合办公室成员；善后处置组组员为综合办公室、经营预算部、财务管理服务中心各工程公司财务部成员；后勤保障组组员为综合办公室、经营预算部成员。 | score=0.0478
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L58 | 二级单位应急救援领导小组 | score=0.0542
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0527
  - D5 | DISPATCH | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0527
  - C11 | COLLECT | real_69c6097ad4242eda8c47c62c:L62 | 2 、根据事故发生情况，决定是否发布启动或终止预案的命令，统一部署应急救援预案的实施工作，并对应急救援工作中发生的争议采取紧急处置措施； | score=0.0527
- projection_chars: 3427

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: The assembled evidence G1 contains the complete content of section 2.5 regarding the responsibilities of the secondary unit emergency rescue leadership group members.
- legal_actions (48):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0570
  - D1 | DISPATCH | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0570
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0570
  - D2 | DISPATCH | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0570
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L19 | 根据国务院第493 号令《生产安全事故报告和调查处理条例》规定， 结合集团公司实际，按照“企业自救、行业互救、社会联动、逐级响应、分级负责”的原则，建立集团公司、二级单位、项目经理部三级响应的应急救援体系。 | score=0.0570
  - D3 | DISPATCH | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0670
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L38 | 2.1 应急组织体系 | score=0.0637
  - D4 | DISPATCH | real_69c6097ad4242eda8c47c62c:L38 | 2.1 应急组织体系 | score=0.0637
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L39 | 生产安全事故应急救援工作在集团公司统一领导下，各二级单位、各有关职能部门分工合作、各司其职、密切配合，迅速、高效、有序开展。 集团设立生产安全事故应急救援指挥部，其组成如下： | score=0.0527
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L51 | 各二级单位成立相应的生产安全事故应急救援领导小组，下设抢救抢险组、技术支持组、医疗救护组、通信联络组、后勤保障组和善后处置组。 组长由二级单位总经理担任，副组长由总工程师、生产副总经理（安全总监）担任，组员由生产安全管理部、经营预算部、技术管理部、综合办公室、财务管理服务中心各工程公司财务部等职能部门负责人组成。 | score=0.0637
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L52 | 二级单位抢救抢险组组员为生产安全管理部成员；技术支持组组员为技术管理部成员； 医疗救护组、通信联络组组员为综合办公室成员；善后处置组组员为综合办公室、经营预算部、财务管理服务中心各工程公司财务部成员；后勤保障组组员为综合办公室、经营预算部成员。 | score=0.0478
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L58 | 二级单位应急救援领导小组 | score=0.0542
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0527
  - D5 | DISPATCH | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0527
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L62 | 2 、根据事故发生情况，决定是否发布启动或终止预案的命令，统一部署应急救援预案的实施工作，并对应急救援工作中发生的争议采取紧急处置措施； | score=0.0527
  - C11 | COLLECT | real_69c6097ad4242eda8c47c62c:L69 | 2.3 集团公司应急救援副总指挥的职责 | score=0.0525
- projection_chars: 3503

### Evidence text (new)

```
[E1]
[§ 2.5 二级单位应急救援领导小组成员职责]
  1 、负责本单位事故救援的全面指挥，协调应急救援行动，独立法人单位总经理负责制定本单位应急救援预案；
  2 、负责向集团公司应急救援总指挥部、相关政府部门报告事故的伤亡和损失情况；
  4 、协调、组织本单位内部应急救援所需的资源、人员、设备等。
  2 、保持与事故现场相关抢救抢险组员的直接联络；
  5 、监督项目部与当地医疗机构、抢险救援机构建立应急救援网络和签订应急救援协议，保障相关机构在事故应急救援中的及时性和有效性。
  1 、负责指导项目部建立现场生产安全事故应急救援预案并实施；
  2、组织、调度实施二级单位生产安全事故应急救援预案的人员、材料、 设备和其他资源的相互配合；
  负责事故抢险和事故处理资金的保障工作。
  1 、协助组织审核生产安全事故应急救援预案；
  2 、负责二级单位生产安全事故现场处置的技术支持。
  负责事故应急处理中法律法规资料的收集，为事故处理提供法律支持。
  2 、负责收集相关单位、部门的通信方式，保证与集团公司、所辖区域当地政府各级部门和附近相关救助机构的通讯联络工作；
```

### Evidence text (old)

```
[E1]
[§ 2.5 二级单位应急救援领导小组成员职责]
1 、负责指导项目部建立现场生产安全事故应急救援预案并实施；

[E2]
[§ 2.5 二级单位应急救援领导小组成员职责]
1 、协助组织审核生产安全事故应急救援预案；

[E3]
[§ 2.5 二级单位应急救援领导小组成员职责]
2、组织、调度实施二级单位生产安全事故应急救援预案的人员、材料、 设备和其他资源的相互配合；

[E4]
[§ 2.5 二级单位应急救援领导小组成员职责]
5 、监督项目部与当地医疗机构、抢险救援机构建立应急救援网络和签订应急救援协议，保障相关机构在事故应急救援中的及时性和有效性。

[E5]
[§ 2.5 二级单位应急救援领导小组成员职责]
1 、负责指导、协助项目部维持事故现场秩序、做好事故区域的警戒， 有关人员的紧急疏散、撤离等；

[E6]
[§ 2.5 二级单位应急救援领导小组成员职责]
（ 一）生产安全管理部

[E7]
[§ 2.5 二级单位应急救援领导小组成员职责]
2 、负责向集团公司应急救援总指挥部、相关政府部门报告事故的伤亡和损失情况；
```

## latest_clean_niche_0711 (niche_fact)

**Query:** 根据《陕西建工第十一建集团有限公司生产安全事故综合应急预案（2025版）》中“2.6 项目部应急救援领导小组成员职责”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c6097ad4242eda8c47c62c`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 490 | 500 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 9 | 13 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c6097ad4242eda8c47c62c:L155` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C14` kind=`collect` section=`real_69c6097ad4242eda8c47c62c:L152` scope=`None` depth=`0`
- reason: Section 2.6 contains the specific duties of the project department emergency rescue leadership group members as requested.
- collect_section_ids: ['real_69c6097ad4242eda8c47c62c:L152']
- collect added=40 hits=40 branch_selected=True collect_full=True
- legal_actions (43):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0502
  - D1 | DISPATCH | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0502
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0502
  - D2 | DISPATCH | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0502
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L19 | 根据国务院第493 号令《生产安全事故报告和调查处理条例》规定， 结合集团公司实际，按照“企业自救、行业互救、社会联动、逐级响应、分级负责”的原则，建立集团公司、二级单位、项目经理部三级响应的应急救援体系。 | score=0.0502
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0642
  - D3 | DISPATCH | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0642
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L38 | 2.1 应急组织体系 | score=0.0504
  - D4 | DISPATCH | real_69c6097ad4242eda8c47c62c:L38 | 2.1 应急组织体系 | score=0.0504
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L39 | 生产安全事故应急救援工作在集团公司统一领导下，各二级单位、各有关职能部门分工合作、各司其职、密切配合，迅速、高效、有序开展。 集团设立生产安全事故应急救援指挥部，其组成如下： | score=0.0466
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L51 | 各二级单位成立相应的生产安全事故应急救援领导小组，下设抢救抢险组、技术支持组、医疗救护组、通信联络组、后勤保障组和善后处置组。 组长由二级单位总经理担任，副组长由总工程师、生产副总经理（安全总监）担任，组员由生产安全管理部、经营预算部、技术管理部、综合办公室、财务管理服务中心各工程公司财务部等职能部门负责人组成。 | score=0.0504
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L59 | 项目部应急救援领导小组 | score=0.0493
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0551
  - D5 | DISPATCH | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0551
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L62 | 2 、根据事故发生情况，决定是否发布启动或终止预案的命令，统一部署应急救援预案的实施工作，并对应急救援工作中发生的争议采取紧急处置措施； | score=0.0551
  - C11 | COLLECT | real_69c6097ad4242eda8c47c62c:L124 | 2.5 二级单位应急救援领导小组成员职责 | score=0.0585
- projection_chars: 3327

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Section G1 contains the complete list of duties for the Project Department Emergency Rescue Leadership Group as requested.
- legal_actions (45):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0502
  - D1 | DISPATCH | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0502
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0502
  - D2 | DISPATCH | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0502
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L19 | 根据国务院第493 号令《生产安全事故报告和调查处理条例》规定， 结合集团公司实际，按照“企业自救、行业互救、社会联动、逐级响应、分级负责”的原则，建立集团公司、二级单位、项目经理部三级响应的应急救援体系。 | score=0.0502
  - D3 | DISPATCH | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0642
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L38 | 2.1 应急组织体系 | score=0.0504
  - D4 | DISPATCH | real_69c6097ad4242eda8c47c62c:L38 | 2.1 应急组织体系 | score=0.0504
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L39 | 生产安全事故应急救援工作在集团公司统一领导下，各二级单位、各有关职能部门分工合作、各司其职、密切配合，迅速、高效、有序开展。 集团设立生产安全事故应急救援指挥部，其组成如下： | score=0.0466
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L51 | 各二级单位成立相应的生产安全事故应急救援领导小组，下设抢救抢险组、技术支持组、医疗救护组、通信联络组、后勤保障组和善后处置组。 组长由二级单位总经理担任，副组长由总工程师、生产副总经理（安全总监）担任，组员由生产安全管理部、经营预算部、技术管理部、综合办公室、财务管理服务中心各工程公司财务部等职能部门负责人组成。 | score=0.0504
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L53 | 项目部成立生产安全事故应急救援领导（处置）小组，下设抢救抢险组、技术支持组、医疗救护组、通信联络组、后勤保障组和善后处置组。 组长由项目经理担任，副组长由项目总工程师（ 生产副经理）和安全总监担任，成员由生产安全管理组、材料动力组、技术管理组、商务预算组、 安装管理组、行政后勤组、财务专员等部门负责人组成。 | score=0.0451
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L59 | 项目部应急救援领导小组 | score=0.0493
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0551
  - D5 | DISPATCH | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0551
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L62 | 2 、根据事故发生情况，决定是否发布启动或终止预案的命令，统一部署应急救援预案的实施工作，并对应急救援工作中发生的争议采取紧急处置措施； | score=0.0551
  - C11 | COLLECT | real_69c6097ad4242eda8c47c62c:L69 | 2.3 集团公司应急救援副总指挥的职责 | score=0.0448
- projection_chars: 3476

### Evidence text (new)

```
[E1]
[§ 2.6 项目部应急救援领导小组成员职责]
  1 、负责制定本项目应急救援预案；
  6 、负责项目部应急救援所需物资、设备的储备。
  2 、负责保持与事故现场相关抢救抢险组员的直接联络；
  5 、负责组织项目部相关技术和管理人员对施工现场生产过程各危险源进行风险辨识、评价，落实对重大危险源的有效管控；
  6 、负责项目部与当地医疗机构、抢险救援机构建立应急救援网络和签订应急救援协议，保障相关机构在事故应急救援中的及时性和有效性。
  1 、负责项目部生产安全事故应急救援预案的演练，发生事故后立即实施现场应急救援；
  2 、负责向项目部应急救援领导小组报告事故现场人员伤亡和财产损失情况；
  3 、组织实施项目部生产安全事故应急救援预案的人员、材料、设备和其他资源的相互配合；
  1 、编制项目部生产安全事故应急救援预案，并参与演练及实施；
  2 、负责生产安全事故现场处置过程中的技术支持。
  1 、负责项目部安装人员应急救援预案的教育培训、演练及实施；
  5 、负责依据相关安全生产法律法规、工伤保险条例的规定，与工伤保险部门办理伤亡人员相关赔偿处理事宜；
```

### Evidence text (old)

```
[E1]
[§ 2.6 项目部应急救援领导小组成员职责]
1 、编制项目部生产安全事故应急救援预案，并参与演练及实施；

[E2]
[§ 2.5 二级单位应急救援领导小组成员职责]
1 、负责指导项目部建立现场生产安全事故应急救援预案并实施；

[E3]
[§ 2.6 项目部应急救援领导小组成员职责]
1 、负责项目部生产安全事故应急救援预案的演练，发生事故后立即实施现场应急救援；

[E4]
[§ 2.6 项目部应急救援领导小组成员职责]
1 、负责制定本项目应急救援预案；

[E5]
[§ 2.6 项目部应急救援领导小组成员职责]
1 、负责项目部安装人员应急救援预案的教育培训、演练及实施；

[E6]
[§ 2.6 项目部应急救援领导小组成员职责]
5 、负责组织项目部相关技术和管理人员对施工现场生产过程各危险源进行风险辨识、评价，落实对重大危险源的有效管控；

[E7]
[§ 2.6 项目部应急救援领导小组成员职责]
1 、负责项目部应急救援物资、设备的储备、维修、保养和管理，确保应急救援器材及设备数量充足、状态良好，保证遇到突发事件时各项救援工作正常运转；
```

## latest_clean_niche_0741 (niche_fact)

**Query:** 根据《陕西建工第十一建集团有限公司生产安全事故综合应急预案（2025版）》中“2.7 各应急救援小组职责”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c6097ad4242eda8c47c62c`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 495 | 490 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 8 | 16 |
| trajectory_steps | n/a | 4 |

### Gold node hits (new)

- `real_69c6097ad4242eda8c47c62c:L195` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6097ad4242eda8c47c62c:L193` scope=`real_69c6097ad4242eda8c47c62c:L193` depth=`1`
- reason: Collects the full section 2.7 to retrieve all specified duties of emergency rescue groups.
- collect_section_ids: ['real_69c6097ad4242eda8c47c62c:L193']
- collect added=25 hits=25 branch_selected=True collect_full=True
- legal_actions (18):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L193 | 2.7 各应急救援小组职责 | score=0.0616
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L194 | （ 一）抢险抢救组 | score=0.0347
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L195 | 1 、组织应急救援的演练和应急处置实施抢险行动方案的执行； | score=0.0461
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L196 | 2 、协调有关部门的抢险行动； | score=0.0410
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L197 | 3 、及时向应急救援领导小组报告抢险进展情况； | score=0.0308
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L198 | 4 、做好现场的应急救援过程中的记录和现场的保护，在事故调查、取证完成后及时清理事故现场。 | score=0.0314
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L200 | 1 、制定其可能出现而必须运用建筑工程技术解决的应急处置方案； | score=0.0508
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L201 | 2 、负责事故应急处置中及时向应急救援领导小组提供科学的工程技术方案和技术支持，解决应急处置中行动中的技术问题； | score=0.0531
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L204 | 1 、保障事故处置过程中所需资金的储备； | score=0.0441
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L205 | 2 、负责现场应急救援材料、物资的购置、储备和分发； | score=0.0347
  - C11 | COLLECT | real_69c6097ad4242eda8c47c62c:L206 | 3 、负责现场应急处置期间抢险器材、设备的调集； | score=0.0369
  - C12 | COLLECT | real_69c6097ad4242eda8c47c62c:L207 | 4 、负责解决全体参加抢险救援工作人员的食宿问题。 | score=0.0308
  - C13 | COLLECT | real_69c6097ad4242eda8c47c62c:L208 | （ 四）善后处置组 | score=0.0350
  - C14 | COLLECT | real_69c6097ad4242eda8c47c62c:L209 | 1 、通知伤亡人员的家属并安排食、住、行等活动，做好伤亡人员及其家属的稳定工作，确保事故发生后伤亡人员及其家属思想稳定； | score=0.0384
  - C15 | COLLECT | real_69c6097ad4242eda8c47c62c:L210 | 2 、做好受伤人员医疗救护的跟踪工作，协调处理医疗救护过程中的人员值班工作； | score=0.0360
  - C16 | COLLECT | real_69c6097ad4242eda8c47c62c:L211 | 3 、依据相关安全生产法律法规、工伤保险条例的规定，做好伤亡人员相关赔偿处理事宜。 | score=0.0616
- projection_chars: 2468

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c6097ad4242eda8c47c62c:L193` depth=`1`
- reason: Collected section L193 contains the required content on emergency rescue group duties. Ready to answer.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 190

**Step 3** `nav_dispatch`  id=`D10` kind=`dispatch` section=`real_69c6097ad4242eda8c47c62c:L193` scope=`None` depth=`0`
- reason: Dispatch to section 2.7 to retrieve all specific duties of emergency rescue groups as requested.
- dispatch_regions: ['real_69c6097ad4242eda8c47c62c:L193']
- child_reports=1 skipped=0
- legal_actions (49):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0618
  - D1 | DISPATCH | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0618
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0618
  - D2 | DISPATCH | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0618
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L19 | 根据国务院第493 号令《生产安全事故报告和调查处理条例》规定， 结合集团公司实际，按照“企业自救、行业互救、社会联动、逐级响应、分级负责”的原则，建立集团公司、二级单位、项目经理部三级响应的应急救援体系。 | score=0.0618
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0702
  - D3 | DISPATCH | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0702
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L38 | 2.1 应急组织体系 | score=0.0509
  - D4 | DISPATCH | real_69c6097ad4242eda8c47c62c:L38 | 2.1 应急组织体系 | score=0.0509
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L39 | 生产安全事故应急救援工作在集团公司统一领导下，各二级单位、各有关职能部门分工合作、各司其职、密切配合，迅速、高效、有序开展。 集团设立生产安全事故应急救援指挥部，其组成如下： | score=0.0478
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L51 | 各二级单位成立相应的生产安全事故应急救援领导小组，下设抢救抢险组、技术支持组、医疗救护组、通信联络组、后勤保障组和善后处置组。 组长由二级单位总经理担任，副组长由总工程师、生产副总经理（安全总监）担任，组员由生产安全管理部、经营预算部、技术管理部、综合办公室、财务管理服务中心各工程公司财务部等职能部门负责人组成。 | score=0.0509
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0671
  - D5 | DISPATCH | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0671
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L62 | 2 、根据事故发生情况，决定是否发布启动或终止预案的命令，统一部署应急救援预案的实施工作，并对应急救援工作中发生的争议采取紧急处置措施； | score=0.0671
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L69 | 2.3 集团公司应急救援副总指挥的职责 | score=0.0702
  - D6 | DISPATCH | real_69c6097ad4242eda8c47c62c:L69 | 2.3 集团公司应急救援副总指挥的职责 | score=0.0702
- projection_chars: 3596

**Step 4** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Section G1 contains the complete list of duties for each emergency rescue group as requested.
- legal_actions (48):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0618
  - D1 | DISPATCH | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0618
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0618
  - D2 | DISPATCH | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0618
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L19 | 根据国务院第493 号令《生产安全事故报告和调查处理条例》规定， 结合集团公司实际，按照“企业自救、行业互救、社会联动、逐级响应、分级负责”的原则，建立集团公司、二级单位、项目经理部三级响应的应急救援体系。 | score=0.0618
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L32 | （2）超出自身应急救援能力范围的事故，上级部门要求集团公司配合进行应急处置的各类安全生产事故。 | score=0.0450
  - D3 | DISPATCH | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0702
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L38 | 2.1 应急组织体系 | score=0.0509
  - D4 | DISPATCH | real_69c6097ad4242eda8c47c62c:L38 | 2.1 应急组织体系 | score=0.0509
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L39 | 生产安全事故应急救援工作在集团公司统一领导下，各二级单位、各有关职能部门分工合作、各司其职、密切配合，迅速、高效、有序开展。 集团设立生产安全事故应急救援指挥部，其组成如下： | score=0.0478
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L51 | 各二级单位成立相应的生产安全事故应急救援领导小组，下设抢救抢险组、技术支持组、医疗救护组、通信联络组、后勤保障组和善后处置组。 组长由二级单位总经理担任，副组长由总工程师、生产副总经理（安全总监）担任，组员由生产安全管理部、经营预算部、技术管理部、综合办公室、财务管理服务中心各工程公司财务部等职能部门负责人组成。 | score=0.0509
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0671
  - D5 | DISPATCH | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0671
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L62 | 2 、根据事故发生情况，决定是否发布启动或终止预案的命令，统一部署应急救援预案的实施工作，并对应急救援工作中发生的争议采取紧急处置措施； | score=0.0671
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L69 | 2.3 集团公司应急救援副总指挥的职责 | score=0.0702
  - D6 | DISPATCH | real_69c6097ad4242eda8c47c62c:L69 | 2.3 集团公司应急救援副总指挥的职责 | score=0.0702
- projection_chars: 3622

### Subagent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c6097ad4242eda8c47c62c:L193 (ok)
collected 26 branch node(s); explicit roots=['real_69c6097ad4242eda8c47c62c:L193']
collected: real_69c6097ad4242eda8c47c62c:L193, real_69c6097ad4242eda8c47c62c:L194, real_69c6097ad4242eda8c47c62c:L195, real_69c6097ad4242eda8c47c62c:L196, real_69c6097ad4242eda8c47c62c:L197, real_69c6097ad4242eda8c47c62c:L198, real_69c6097ad4242eda8c47c62c:L199, real_69c6097ad4242eda8c47c62c:L200, real_69c6097ad4242eda8c47c62c:L201, real_69c6097ad4242eda8c47c62c:L202, real_69c6097ad4242eda8c47c62c:L203, real_69c6097ad4242eda8c47c62c:L204, real_69c6097ad4242eda8c47c62c:L205, real_69c6097ad4242eda8c47c62c:L206, real_69c6097ad4242eda8c47c62c:L207, real_69c6097ad4242eda8c47c62c:L208, real_69c6097ad4242eda8c47c62c:L209, real_69c6097ad4242eda8c47c62c:L210, real_69c6097ad4242eda8c47c62c:L211, real_69c6097ad4242eda8c47c62c:L212
reason: Collected section L193 contains the required content on emergency rescue group duties. Ready to answer.
---
=== End Investigate ===
```

### Evidence text (new)

```
[E1]
[§ 2.7 各应急救援小组职责]
  （ 一）抢险抢救组
  1 、组织应急救援的演练和应急处置实施抢险行动方案的执行；
  2 、协调有关部门的抢险行动；
  1 、制定其可能出现而必须运用建筑工程技术解决的应急处置方案；
  2 、负责事故应急处置中及时向应急救援领导小组提供科学的工程技术方案和技术支持，解决应急处置中行动中的技术问题；
  1 、保障事故处置过程中所需资金的储备；
  2 、负责现场应急救援材料、物资的购置、储备和分发；
  3 、负责现场应急处置期间抢险器材、设备的调集；
  （ 四）善后处置组
  1 、通知伤亡人员的家属并安排食、住、行等活动，做好伤亡人员及其家属的稳定工作，确保事故发生后伤亡人员及其家属思想稳定；
  2 、做好受伤人员医疗救护的跟踪工作，协调处理医疗救护过程中的人员值班工作；
  3 、依据相关安全生产法律法规、工伤保险条例的规定，做好伤亡人员相关赔偿处理事宜。
  （ 五）医疗救护组
  1 、负责生产安全事故处理过程中信息发布和媒体接待；
  2 、负责收集相关单位部门的通信方式，保证各级通讯联系畅通；
```

### Evidence text (old)

```
[E1]
[§ 2.7 各应急救援小组职责]
1 、制定其可能出现而必须运用建筑工程技术解决的应急处置方案；

[E2]
[§ 2.7 各应急救援小组职责]
1 、保障事故处置过程中所需资金的储备；

[E3]
[§ 2.7 各应急救援小组职责]
1 、负责生产安全事故处理过程中信息发布和媒体接待；

[E4]
[§ 2.7 各应急救援小组职责]
2 、负责事故应急处置中及时向应急救援领导小组提供科学的工程技术方案和技术支持，解决应急处置中行动中的技术问题；

[E5]
[§ 2.7 各应急救援小组职责]
1 、通知伤亡人员的家属并安排食、住、行等活动，做好伤亡人员及其家属的稳定工作，确保事故发生后伤亡人员及其家属思想稳定；

[E6]
[§ 2.1 应急组织体系]
各二级单位成立相应的生产安全事故应急救援领导小组，下设抢救抢险组、技术支持组、医疗救护组、通信联络组、后勤保障组和善后处置组。 组长由二级单位总经理担任，副组长由总工程师、生产副总经理（安全总监）担任，组员由生产安全管理部、经营预算部、技术管理部、综合办公室、财务管理服务中心各工程公司财务部等职能部门负责人组成。
```

## latest_clean_niche_0759 (niche_fact)

**Query:** 根据《陕西建工第十一建集团有限公司生产安全事故综合应急预案（2025版）》中“3.1 信息报告”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c6097ad4242eda8c47c62c`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 495 | 492 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 13 | 13 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c6097ad4242eda8c47c62c:L222` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C13` kind=`collect` section=`real_69c6097ad4242eda8c47c62c:L220` scope=`None` depth=`0`
- reason: Collect section 3.1 Information Reporting to answer the query about reporting regulations.
- collect_section_ids: ['real_69c6097ad4242eda8c47c62c:L220']
- collect added=25 hits=25 branch_selected=True collect_full=True
- legal_actions (47):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0663
  - D1 | DISPATCH | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0663
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L4 | 1.2 编制依据 | score=0.0559
  - D2 | DISPATCH | real_69c6097ad4242eda8c47c62c:L4 | 1.2 编制依据 | score=0.0559
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L14 | 10 、《陕西建工第十一建设集团有限公司生产安全事故风险评估报告》 | score=0.0557
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L15 | 11 、《陕西建工第十一建设集团有限公司生产安全事故应急资源调查报告》 | score=0.0559
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L16 | 1.3 适用范围 | score=0.0540
  - D3 | DISPATCH | real_69c6097ad4242eda8c47c62c:L16 | 1.3 适用范围 | score=0.0540
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L17 | 本《预案》适用于集团公司、二级单位及项目经理部所承建工程施工现场发生的坍塌、高处坠落、物体打击、触电、起重伤害、机械伤害、车辆伤害、中毒与窒息、火灾、灼烫、容器爆炸、其他伤害等较大及其以上各类生产安全事故，同时包括有重大社会影响、涉及公共安全或突发事件应急处置工作的应急救援。 | score=0.0540
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0663
  - D4 | DISPATCH | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0663
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L19 | 根据国务院第493 号令《生产安全事故报告和调查处理条例》规定， 结合集团公司实际，按照“企业自救、行业互救、社会联动、逐级响应、分级负责”的原则，建立集团公司、二级单位、项目经理部三级响应的应急救援体系。 | score=0.0663
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0549
  - D5 | DISPATCH | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0549
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L193 | 2.7 各应急救援小组职责 | score=0.0549
  - D6 | DISPATCH | real_69c6097ad4242eda8c47c62c:L193 | 2.7 各应急救援小组职责 | score=0.0549
- projection_chars: 3527

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Section G1 contains the complete '3.1 Information Reporting' content including reporting procedures, timelines, and required information details.
- legal_actions (49):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0663
  - D1 | DISPATCH | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0663
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L4 | 1.2 编制依据 | score=0.0559
  - D2 | DISPATCH | real_69c6097ad4242eda8c47c62c:L4 | 1.2 编制依据 | score=0.0559
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L8 | 4 、《生产安全事故报告和调查处理条例》 | score=0.0485
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L13 | 9 、《陕西建工集团股份有限公司生产安全事故综合应急预案》 | score=0.0485
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L14 | 10 、《陕西建工第十一建设集团有限公司生产安全事故风险评估报告》 | score=0.0557
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L15 | 11 、《陕西建工第十一建设集团有限公司生产安全事故应急资源调查报告》 | score=0.0559
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L16 | 1.3 适用范围 | score=0.0540
  - D3 | DISPATCH | real_69c6097ad4242eda8c47c62c:L16 | 1.3 适用范围 | score=0.0540
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L17 | 本《预案》适用于集团公司、二级单位及项目经理部所承建工程施工现场发生的坍塌、高处坠落、物体打击、触电、起重伤害、机械伤害、车辆伤害、中毒与窒息、火灾、灼烫、容器爆炸、其他伤害等较大及其以上各类生产安全事故，同时包括有重大社会影响、涉及公共安全或突发事件应急处置工作的应急救援。 | score=0.0540
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0663
  - D4 | DISPATCH | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0663
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L19 | 根据国务院第493 号令《生产安全事故报告和调查处理条例》规定， 结合集团公司实际，按照“企业自救、行业互救、社会联动、逐级响应、分级负责”的原则，建立集团公司、二级单位、项目经理部三级响应的应急救援体系。 | score=0.0663
  - C11 | COLLECT | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0549
  - D5 | DISPATCH | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0549
- projection_chars: 3489

### Evidence text (new)

```
[E1]
[§ 3.1 信息报告]
  3.1.1 信息接报与上报
  值班人员在接到事故报告信息后，及时确认事故信息， 并在第一时间向应急救援总指挥报告， 由总指挥根据事故情况决定是否启动本预案和通知人员的范围。
  发生生产安全事故后，项目经理部应当立即启动现场处置预案，并将发生事故的有关信息及时、准确地通过电话、传真等形式报告至集团应急
  救援指挥部办公室和总指挥， 由集团根据事故分级，在1 小时内上报事故发生地县级以上应急管理部门负有安全生产监督管理职责的有关部门。事故信息发生变化时，应及时以书面形式补报有关变化情况。
  集团公司生产安全事故应急救援总指挥部办公室设在集团公司安全管
  陕西建工股份集团有
  负有安全生产监督管理职责的有关部门
  报告事故应当包括以下内容：
  （ 一）事故发生项目概况；
  （ 六）其他应当报告的情况。
  3.1.2 信息处置与研判
  集团公司应急救援指挥办公室接到报告后，按照分级响应的原则，根据事故的性质、严重程度、影响范围和可控性，对事故进行预判，并报告给集团应急救援总指挥，由总指挥做出预警或应急响应启动的决策。
```

### Evidence text (old)

```
[E1]
[§ 3.1 信息报告]
陕西建工股份集团有

[E2]
[§ 3.1 信息报告]
（ 一）事故发生项目概况；

[E3]
[§ 3.1 信息报告]
（ 五）已经采取的措施；

[E4]
[§ 3.1 信息报告]
限公司应急救援指挥部

[E5]
[§ 3.1 信息报告]
（ 二）事故发生的时间、地点以及事故现场情况；

[E6]
[§ 3.1 信息报告]
（ 三）事故的简要经过；

[E7]
[§ 3.1 信息报告]
负有安全生产监督管理职责的有关部门

[E8]
[§ 3.1 信息报告]
当地政府安全监管部门

[E9]
[§ 3.1 信息报告]
发生生产安全事故后，项目经理部应当立即启动现场处置预案，并将发生事故的有关信息及时、准确地通过电话、传真等形式报告至集团应急

[E10]
[§ 3.1 信息报告]
（4）事故造成严重不良社会影响的，应提高一个响应级别。

[E11]
[§ 3.1 信息报告]
报告事故应当包括以下内容：

[E12]
[§ 3.1 信息报告]
（ 四）事故已经造成或者可能造成的伤亡人数（包括下落不明的人数） 和初步估计的直接经济损失；
```

## latest_clean_niche_0795 (niche_fact)

**Query:** 根据《陕西建工第十一建集团有限公司生产安全事故综合应急预案（2025版）》中“3.5 应急支援”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c6097ad4242eda8c47c62c`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 483 | 492 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 11 | 8 |
| trajectory_steps | n/a | 4 |

### Gold node hits (new)

- `real_69c6097ad4242eda8c47c62c:L280` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6097ad4242eda8c47c62c:L219` scope=`real_69c6097ad4242eda8c47c62c:L219` depth=`1`
- reason: Collect section 3 to access subsection 3.5 '应急支援' as requested.
- collect_section_ids: ['real_69c6097ad4242eda8c47c62c:L219']
- collect added=64 hits=64 branch_selected=True collect_full=False
- legal_actions (15):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L219 | 3.应急响应 | score=0.0692
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L220 | 3.1 信息报告 | score=0.0491
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L222 | 值班人员在接到事故报告信息后，及时确认事故信息， 并在第一时间向应急救援总指挥报告， 由总指挥根据事故情况决定是否启动本预案和通知人员的范围。 | score=0.0491
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L224 | 救援指挥部办公室和总指挥， 由集团根据事故分级，在1 小时内上报事故发生地县级以上应急管理部门负有安全生产监督管理职责的有关部门。事故信息发生变化时，应及时以书面形式补报有关变化情况。 | score=0.0475
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L246 | 3.2 预警 | score=0.0560
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L255 | 应急救援指挥部办公室根据集团公司发布的事故响应级别( Ⅰ 、 Ⅱ 、 Ⅲ级），结合现场应急事件的危害程度、紧急程度和发展趋势，做出是否启动的判断。 | score=0.0560
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L267 | 3.3 响应启动 | score=0.0638
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L268 | （ 1 ）集团应急救援指挥部办公室接到I 级生产安全事故响应报告后， 应立即报告集团公司应急救援指挥部总指挥， 由总指挥按照规定程序启动本预案。集团公司应急救援指挥部办公室负责通知各应急救援小组组长迅速到位履行职责，总指挥与各部门联系人及时组织实施相应事故应急预案， 通知有关成员迅速赶赴事故现场，指导实施现场救援，并根据事故情况必要时请求事故发生地政府专业应急救援组织支援。 | score=0.0589
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L270 | 批准的生产安全事故应急预案，实施现场救援，并根据事故情况，必要时请求事故发生地政府、集团应急救援组织支援。 | score=0.0638
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L337 | 6.0 其他事项 | score=0.0692
  - C11 | COLLECT | real_69c6097ad4242eda8c47c62c:L338 | （ 一）本预案是集团公司针对可能发生的生产安全事故，组织实施应急救援工作并协助政府有关部门进行事故调查处理的指导性文件，在实施过程中可根据现场实际情况进行必要的调整。 | score=0.0692
  - C12 | COLLECT | real_69c6097ad4242eda8c47c62c:L339 | （ 二）各项目部必须在开工前，根据各自的实际，分析施工过程中可能发生的生产安全事故的性质、类别，制定针对性的生产安全事故应急预案，上报二级单位、集团公司备案。 | score=0.0539
  - C13 | COLLECT | real_69c6097ad4242eda8c47c62c:L340 | （ 三）各二级单位、项目部要根据条件和环境的变化及时修改补充和完善预案的内容，并组织有关人员认真学习，掌握预案的内容和相关措施， 定期组织演练，确保在紧急情况下按照预案的要求，有条不紊地开展事故应急救援工作。 | score=0.0679
  - C14 | COLLECT | real_69c6097ad4242eda8c47c62c:L364 | 7.4  应急预案备案 | score=0.0627
  - C15 | COLLECT | real_69c6097ad4242eda8c47c62c:L365 | 按照陕西省安全生产委员会《关于印发〈陕西省生产安全事故应急预案管理工作实施意见〉的通知》（陕安委会发[2010]9 号）要求，本应急预案经集团主要负责人批准实施后，按规定报上级行政主管部门及陕西建工集团股份有限公司备案。 | score=0.0627
- projection_chars: 3530

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c6097ad4242eda8c47c62c:L219` depth=`1`
- reason: The current scope L219 contains the '3.5 应急支援' section, and evidence has been collected to answer the query.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 190

**Step 3** `nav_dispatch`  id=`D10` kind=`dispatch` section=`real_69c6097ad4242eda8c47c62c:L219` scope=`None` depth=`0`
- reason: Dispatch to section 3应急响应 to locate subsection 3.5 应急支援.
- dispatch_regions: ['real_69c6097ad4242eda8c47c62c:L219']
- child_reports=1 skipped=0
- legal_actions (48):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0678
  - D1 | DISPATCH | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0678
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L4 | 1.2 编制依据 | score=0.0486
  - D2 | DISPATCH | real_69c6097ad4242eda8c47c62c:L4 | 1.2 编制依据 | score=0.0486
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L13 | 9 、《陕西建工集团股份有限公司生产安全事故综合应急预案》 | score=0.0486
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L16 | 1.3 适用范围 | score=0.0558
  - D3 | DISPATCH | real_69c6097ad4242eda8c47c62c:L16 | 1.3 适用范围 | score=0.0558
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L17 | 本《预案》适用于集团公司、二级单位及项目经理部所承建工程施工现场发生的坍塌、高处坠落、物体打击、触电、起重伤害、机械伤害、车辆伤害、中毒与窒息、火灾、灼烫、容器爆炸、其他伤害等较大及其以上各类生产安全事故，同时包括有重大社会影响、涉及公共安全或突发事件应急处置工作的应急救援。 | score=0.0558
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0678
  - D4 | DISPATCH | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0678
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L19 | 根据国务院第493 号令《生产安全事故报告和调查处理条例》规定， 结合集团公司实际，按照“企业自救、行业互救、社会联动、逐级响应、分级负责”的原则，建立集团公司、二级单位、项目经理部三级响应的应急救援体系。 | score=0.0678
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L29 | （3 ）超出自身应急救援能力范围的事故，上级部门要求集团公司配合进行应急处置的各类安全生产事故。 | score=0.0555
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0655
  - D5 | DISPATCH | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0655
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0655
  - D6 | DISPATCH | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0655
- projection_chars: 3477

**Step 4** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Section G10 (§3.5 应急支援) contains the specific regulations requested by the user.
- legal_actions (51):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0678
  - D1 | DISPATCH | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0678
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L4 | 1.2 编制依据 | score=0.0486
  - D2 | DISPATCH | real_69c6097ad4242eda8c47c62c:L4 | 1.2 编制依据 | score=0.0486
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L9 | 5 、《陕西省突发公共事件总体应急预案》 | score=0.0429
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L13 | 9 、《陕西建工集团股份有限公司生产安全事故综合应急预案》 | score=0.0486
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L14 | 10 、《陕西建工第十一建设集团有限公司生产安全事故风险评估报告》 | score=0.0439
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L15 | 11 、《陕西建工第十一建设集团有限公司生产安全事故应急资源调查报告》 | score=0.0466
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L16 | 1.3 适用范围 | score=0.0558
  - D3 | DISPATCH | real_69c6097ad4242eda8c47c62c:L16 | 1.3 适用范围 | score=0.0558
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L17 | 本《预案》适用于集团公司、二级单位及项目经理部所承建工程施工现场发生的坍塌、高处坠落、物体打击、触电、起重伤害、机械伤害、车辆伤害、中毒与窒息、火灾、灼烫、容器爆炸、其他伤害等较大及其以上各类生产安全事故，同时包括有重大社会影响、涉及公共安全或突发事件应急处置工作的应急救援。 | score=0.0558
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0678
  - D4 | DISPATCH | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0678
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L19 | 根据国务院第493 号令《生产安全事故报告和调查处理条例》规定， 结合集团公司实际，按照“企业自救、行业互救、社会联动、逐级响应、分级负责”的原则，建立集团公司、二级单位、项目经理部三级响应的应急救援体系。 | score=0.0678
  - C11 | COLLECT | real_69c6097ad4242eda8c47c62c:L25 | （4）超出自身应急救援能力范围的事故，上级部门要求集团公司配合进行应急处置的各类安全生产事故。 | score=0.0457
  - C12 | COLLECT | real_69c6097ad4242eda8c47c62c:L29 | （3 ）超出自身应急救援能力范围的事故，上级部门要求集团公司配合进行应急处置的各类安全生产事故。 | score=0.0555
- projection_chars: 3417

### Subagent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c6097ad4242eda8c47c62c:L219 (ok)
collected 150 branch node(s); explicit roots=['real_69c6097ad4242eda8c47c62c:L219']
collected: real_69c6097ad4242eda8c47c62c:L219, real_69c6097ad4242eda8c47c62c:L220, real_69c6097ad4242eda8c47c62c:L221, real_69c6097ad4242eda8c47c62c:L222, real_69c6097ad4242eda8c47c62c:L223, real_69c6097ad4242eda8c47c62c:L224, real_69c6097ad4242eda8c47c62c:L225, real_69c6097ad4242eda8c47c62c:L226, real_69c6097ad4242eda8c47c62c:L227, real_69c6097ad4242eda8c47c62c:L228, real_69c6097ad4242eda8c47c62c:L229, real_69c6097ad4242eda8c47c62c:L230, real_69c6097ad4242eda8c47c62c:L231, real_69c6097ad4242eda8c47c62c:L232, real_69c6097ad4242eda8c47c62c:L233, real_69c6097ad4242eda8c47c62c:L234, real_69c6097ad4242eda8c47c62c:L235, real_69c6097ad4242eda8c47c62c:L236, real_69c6097ad4242eda8c47c62c:L237, real_69c6097ad4242eda8c47c62c:L238
reason: The current scope L219 contains the '3.5 应急支援' section, and evidence has been collected to answer the query.
---
=== End Investigate ===
```

### Evidence text (new)

```
[E1]
[§ 3.5  应急支援]
  当事态无法控制时，应立即寻求外部力量支持，如当地应急管理部门、 质量安全监督站、医院、公安、消防、救援中心等。
  （ 1 ）当Ⅲ 级（项目经理部）响应事故存在失控可能时，应向事故发生项目所在二级单位应急救援领导小组报告请求支援。在集团公司应急救援指挥部赶到现场后，项目经理部将指挥权移交现场最高领导。
  （3 ） 当I 级（集团公司级）响应事故存在失控可能，由集团公司应急救援办公室按信息报告相关规定报告属地政府应急管理部门，政府应急指挥组织机构赶到现场后，现场指挥权应立即移交政府，并汇报事故情况、 进展、风险以及影响控制事态的关键因素等问题，服从政府统一指挥。

[E2]
[§ 6.0 其他事项]
  （ 一）本预案是集团公司针对可能发生的生产安全事故，组织实施应急救援工作并协助政府有关部门进行事故调查处理的指导性文件，在实施过程中可根据现场实际情况进行必要的调整。
  （ 二）各项目部必须在开工前，根据各自的实际，分析施工过程中可能发生的生产安全事故的性质、类别，制定针对性的生产安全事故应急预案，上报二级单位、集团公司备案。
```

### Evidence text (old)

```
[E1]
[§ 3.3 响应启动]
批准的生产安全事故应急预案，实施现场救援，并根据事故情况，必要时请求事故发生地政府、集团应急救援组织支援。

[E2]
[§ 3.1 信息报告]
限公司应急救援指挥部

[E3]
[§ 1.3 适用范围]
本《预案》适用于集团公司、二级单位及项目经理部所承建工程施工现场发生的坍塌、高处坠落、物体打击、触电、起重伤害、机械伤害、车辆伤害、中毒与窒息、火灾、灼烫、容器爆炸、其他伤害等较大及其以上各类生产安全事故，同时包括有重大社会影响、涉及公共安全或突发事件应急处置工作的应急救援。

[E4]
[§ 2.5 二级单位应急救援领导小组成员职责]
4 、监督、检查项目部对施工场区生产过程各危险源进行风险辨识、评价，以及对重大危险源进行有效管控；

[E5]
[§ 3.1 信息报告]
陕西建工股份集团有

[E6]
[§ 3.5  应急支援]
（ 1 ）当Ⅲ 级（项目经理部）响应事故存在失控可能时，应向事故发生项目所在二级单位应急救援领导小组报告请求支援。在集团公司应急救援指挥部赶到现场后，项目经理部将指挥权移交现场最高领导。
```

## latest_clean_niche_0811 (niche_fact)

**Query:** 根据《陕西建工第十一建集团有限公司生产安全事故综合应急预案（2025版）》中“5.3 现场应急物资装备保障”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c6097ad4242eda8c47c62c`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 500 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 15 | 17 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c6097ad4242eda8c47c62c:L307` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C23` kind=`collect` section=`real_69c6097ad4242eda8c47c62c:L306` scope=`None` depth=`0`
- reason: Target section 5.3 contains the specific regulations on emergency material and equipment guarantees.
- collect_section_ids: ['real_69c6097ad4242eda8c47c62c:L306']
- collect added=18 hits=18 branch_selected=True collect_full=True
- legal_actions (48):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0554
  - D1 | DISPATCH | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0554
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L16 | 1.3 适用范围 | score=0.0554
  - D2 | DISPATCH | real_69c6097ad4242eda8c47c62c:L16 | 1.3 适用范围 | score=0.0554
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L17 | 本《预案》适用于集团公司、二级单位及项目经理部所承建工程施工现场发生的坍塌、高处坠落、物体打击、触电、起重伤害、机械伤害、车辆伤害、中毒与窒息、火灾、灼烫、容器爆炸、其他伤害等较大及其以上各类生产安全事故，同时包括有重大社会影响、涉及公共安全或突发事件应急处置工作的应急救援。 | score=0.0554
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0545
  - D3 | DISPATCH | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0545
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L19 | 根据国务院第493 号令《生产安全事故报告和调查处理条例》规定， 结合集团公司实际，按照“企业自救、行业互救、社会联动、逐级响应、分级负责”的原则，建立集团公司、二级单位、项目经理部三级响应的应急救援体系。 | score=0.0545
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0593
  - D4 | DISPATCH | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0593
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0501
  - D5 | DISPATCH | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0501
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L62 | 2 、根据事故发生情况，决定是否发布启动或终止预案的命令，统一部署应急救援预案的实施工作，并对应急救援工作中发生的争议采取紧急处置措施； | score=0.0501
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L69 | 2.3 集团公司应急救援副总指挥的职责 | score=0.0593
  - D6 | DISPATCH | real_69c6097ad4242eda8c47c62c:L69 | 2.3 集团公司应急救援副总指挥的职责 | score=0.0593
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L76 | 7 、根据各施工场区的实际条件，协调集团公司与周边有条件的企业在事故应急处理中共享资源、相互帮助、建立共同应急救援网络和制定应急救援协议。 | score=0.0593
- projection_chars: 3451

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Section G1 contains the specific regulations for §5.3 on emergency material and equipment guarantees.
- legal_actions (48):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0554
  - D1 | DISPATCH | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0554
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L4 | 1.2 编制依据 | score=0.0473
  - D2 | DISPATCH | real_69c6097ad4242eda8c47c62c:L4 | 1.2 编制依据 | score=0.0473
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L13 | 9 、《陕西建工集团股份有限公司生产安全事故综合应急预案》 | score=0.0465
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L15 | 11 、《陕西建工第十一建设集团有限公司生产安全事故应急资源调查报告》 | score=0.0473
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L16 | 1.3 适用范围 | score=0.0554
  - D3 | DISPATCH | real_69c6097ad4242eda8c47c62c:L16 | 1.3 适用范围 | score=0.0554
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L17 | 本《预案》适用于集团公司、二级单位及项目经理部所承建工程施工现场发生的坍塌、高处坠落、物体打击、触电、起重伤害、机械伤害、车辆伤害、中毒与窒息、火灾、灼烫、容器爆炸、其他伤害等较大及其以上各类生产安全事故，同时包括有重大社会影响、涉及公共安全或突发事件应急处置工作的应急救援。 | score=0.0554
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0545
  - D4 | DISPATCH | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0545
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L19 | 根据国务院第493 号令《生产安全事故报告和调查处理条例》规定， 结合集团公司实际，按照“企业自救、行业互救、社会联动、逐级响应、分级负责”的原则，建立集团公司、二级单位、项目经理部三级响应的应急救援体系。 | score=0.0545
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0593
  - D5 | DISPATCH | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0593
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0501
  - D6 | DISPATCH | real_69c6097ad4242eda8c47c62c:L60 | 2.2 集团公司应急救援总指挥的职责 | score=0.0501
- projection_chars: 3452

### Evidence text (new)

```
[E1]
[§ 5.3 现场应急物资装备保障]
  各项目部生产安全事故应急救援指挥部， 由项目部按照危害辨识和风险评价的结果，结合项目部可能发生的事故情况设立，但应至少具备如下条件：
  （ 一）数量充足的内线和外线电话；无线电和其他通讯设备；
  （ 二）有救援物资数据库：明确应急物资和设备名称、数量、型号大小、存放地点、负责人及调动方式等；
  （ 三）重大危险源示意图，图中应注明：
  ——大量危险材料堆放处；
  ——救援设备存放点；
  ——消防系统和附近水源；
  ——重大危险源的进口和道路状况；
  ——安全区；
  ——重大危险源的位置与周边地区的关系；
  ——施工现场的地质资料；
  （ 五）施工现场从业人员名单及分布情况；
  （ 六）关键岗位人员的住址和联系方式（如登高架设工、塔吊司机、 电气焊工、厂内车辆驾驶等特殊岗位作业人员和指挥部各成员、司机、急救人员等）；
  （ 七）当地政府和应急服务机构地址及联系方式（如安全生产监督管理局、质量安全监督站、医院、消防中心、救援中心等）；
  （八）应急与事故处理法规、标准等资料；
  （九）事故现场的其他人员名单。
```

### Evidence text (old)

```
[E1]
[§ 3.应急响应 / 5.3 现场应急物资装备保障]
（ 五）施工现场从业人员名单及分布情况；

[E2]
[§ 1 总则 / 1.2 编制依据]
11 、《陕西建工第十一建设集团有限公司生产安全事故应急资源调查报告》

[E3]
[§ 3.应急响应 / 3.1 信息报告]
陕西建工股份集团有

[E4]
[§ 3.应急响应 / 5.3 现场应急物资装备保障]
——安全区；

[E5]
[§ 3.应急响应 / 7.4  应急预案备案]
按照陕西省安全生产委员会《关于印发〈陕西省生产安全事故应急预案管理工作实施意见〉的通知》（陕安委会发[2010]9 号）要求，本应急预案经集团主要负责人批准实施后，按规定报上级行政主管部门及陕西建工集团股份有限公司备案。

[E6]
[§ 3.应急响应 / 5.3 现场应急物资装备保障]
——施工现场的地质资料；

[E7]
[§ 3.应急响应 / 5.5 其他保障]
5.5.1 经费保障

[E8]
[§ 3.应急响应 / 5.3 现场应急物资装备保障]
——消防系统和附近水源；

[E9]
[§ 3.应急响应 / 5.3 现场应急物资装备
```

## latest_clean_niche_0821 (niche_fact)

**Query:** 根据《陕西建工第十一建集团有限公司生产安全事故综合应急预案（2025版）》中“5.5 其他保障”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c6097ad4242eda8c47c62c`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 496 | 497 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 18 | 12 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c6097ad4242eda8c47c62c:L327` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C25` kind=`collect` section=`real_69c6097ad4242eda8c47c62c:L325` scope=`None` depth=`0`
- reason: Target section 5.5 'Other Guarantees' identified; collect to retrieve specific regulations.
- collect_section_ids: ['real_69c6097ad4242eda8c47c62c:L325']
- collect added=11 hits=11 branch_selected=True collect_full=True
- legal_actions (53):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0629
  - D1 | DISPATCH | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0629
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L2 | 1.1 编制目的 | score=0.0511
  - D2 | DISPATCH | real_69c6097ad4242eda8c47c62c:L2 | 1.1 编制目的 | score=0.0511
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L3 | 为加强集团公司处置生产安全事故的能力，提高应对突发事件的反应速度和协调水平，确保集团公司应急体系有效运行，及时迅速处置各类生产安全事故，将损失降至最低程度，保障人员生命财产安全，维护集团公司正常的生产秩序和社会秩序，促进企业可持续发展，特制定本《预案》。 | score=0.0511
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L4 | 1.2 编制依据 | score=0.0514
  - D3 | DISPATCH | real_69c6097ad4242eda8c47c62c:L4 | 1.2 编制依据 | score=0.0514
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L13 | 9 、《陕西建工集团股份有限公司生产安全事故综合应急预案》 | score=0.0514
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L16 | 1.3 适用范围 | score=0.0629
  - D4 | DISPATCH | real_69c6097ad4242eda8c47c62c:L16 | 1.3 适用范围 | score=0.0629
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L17 | 本《预案》适用于集团公司、二级单位及项目经理部所承建工程施工现场发生的坍塌、高处坠落、物体打击、触电、起重伤害、机械伤害、车辆伤害、中毒与窒息、火灾、灼烫、容器爆炸、其他伤害等较大及其以上各类生产安全事故，同时包括有重大社会影响、涉及公共安全或突发事件应急处置工作的应急救援。 | score=0.0629
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0587
  - D5 | DISPATCH | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0587
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L19 | 根据国务院第493 号令《生产安全事故报告和调查处理条例》规定， 结合集团公司实际，按照“企业自救、行业互救、社会联动、逐级响应、分级负责”的原则，建立集团公司、二级单位、项目经理部三级响应的应急救援体系。 | score=0.0587
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0657
  - D6 | DISPATCH | real_69c6097ad4242eda8c47c62c:L37 | 2.应急组织机构及职责 | score=0.0657
- projection_chars: 3501

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Section 5.5 content fully collected and assembled in evidence.
- legal_actions (52):
  - C1 | COLLECT | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0629
  - D1 | DISPATCH | real_69c6097ad4242eda8c47c62c:L1 | 1 总则 | score=0.0629
  - C2 | COLLECT | real_69c6097ad4242eda8c47c62c:L2 | 1.1 编制目的 | score=0.0511
  - D2 | DISPATCH | real_69c6097ad4242eda8c47c62c:L2 | 1.1 编制目的 | score=0.0511
  - C3 | COLLECT | real_69c6097ad4242eda8c47c62c:L3 | 为加强集团公司处置生产安全事故的能力，提高应对突发事件的反应速度和协调水平，确保集团公司应急体系有效运行，及时迅速处置各类生产安全事故，将损失降至最低程度，保障人员生命财产安全，维护集团公司正常的生产秩序和社会秩序，促进企业可持续发展，特制定本《预案》。 | score=0.0511
  - C4 | COLLECT | real_69c6097ad4242eda8c47c62c:L4 | 1.2 编制依据 | score=0.0514
  - D3 | DISPATCH | real_69c6097ad4242eda8c47c62c:L4 | 1.2 编制依据 | score=0.0514
  - C5 | COLLECT | real_69c6097ad4242eda8c47c62c:L13 | 9 、《陕西建工集团股份有限公司生产安全事故综合应急预案》 | score=0.0514
  - C6 | COLLECT | real_69c6097ad4242eda8c47c62c:L14 | 10 、《陕西建工第十一建设集团有限公司生产安全事故风险评估报告》 | score=0.0477
  - C7 | COLLECT | real_69c6097ad4242eda8c47c62c:L15 | 11 、《陕西建工第十一建设集团有限公司生产安全事故应急资源调查报告》 | score=0.0475
  - C8 | COLLECT | real_69c6097ad4242eda8c47c62c:L16 | 1.3 适用范围 | score=0.0629
  - D4 | DISPATCH | real_69c6097ad4242eda8c47c62c:L16 | 1.3 适用范围 | score=0.0629
  - C9 | COLLECT | real_69c6097ad4242eda8c47c62c:L17 | 本《预案》适用于集团公司、二级单位及项目经理部所承建工程施工现场发生的坍塌、高处坠落、物体打击、触电、起重伤害、机械伤害、车辆伤害、中毒与窒息、火灾、灼烫、容器爆炸、其他伤害等较大及其以上各类生产安全事故，同时包括有重大社会影响、涉及公共安全或突发事件应急处置工作的应急救援。 | score=0.0629
  - C10 | COLLECT | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0587
  - D5 | DISPATCH | real_69c6097ad4242eda8c47c62c:L18 | 1.4 响应分级 | score=0.0587
  - C11 | COLLECT | real_69c6097ad4242eda8c47c62c:L19 | 根据国务院第493 号令《生产安全事故报告和调查处理条例》规定， 结合集团公司实际，按照“企业自救、行业互救、社会联动、逐级响应、分级负责”的原则，建立集团公司、二级单位、项目经理部三级响应的应急救援体系。 | score=0.0587
- projection_chars: 3561

### Evidence text (new)

```
[E1]
[§ 5.5 其他保障]
  5.5.1 经费保障
  集团公司财务管理服务中心负责保障应急状态时应急经费的及时到位， 并对事故应急保障资金的使用效果进行监管和评估。在应急状态下资金无法及时到位的情况下，应及时申请动用企业安全生产风险抵押金应急，确保应急资金到位。
  5.5.2 交通运输保障
  集团公司应急救援总指挥部组织和调集足够的交通运输工具，为应急救援工作提供交通运输保障。集团公司保卫部协助当地交管部门对事故现场进行交通管制，确保应急救援车辆优先通行。
  5.5.3 治安保障
  集团公司党政办公室组织安保人员做好事故现场的治安警戒和治安管
  理，加强对重点区域、重点场所、重点人群、重要物资和设备的保护，维持现场秩序，及时疏散群众，动员和组织群众开展群防联防，协助当地公安部门做好治安保卫工作。
  5.5.4 医疗卫生保障
  施工现场按照规定配备专兼职急救人员和必需的急救药品，急救人员组织应急救援队伍和当地医疗机构进入事故现场开展救援。
  5.5.5 后勤保障
  事故发生项目的责任管理单位，负责伤者家属、调查组和应急人员的住宿、用餐及交通等保障工作。
```

### Evidence text (old)

```
[E1]
[§ 1 总则 / 1.2 编制依据]
9 、《陕西建工集团股份有限公司生产安全事故综合应急预案》

[E2]
[§ 3.应急响应 / 5.5 其他保障]
5.5.1 经费保障

[E3]
[§ 3.应急响应 / 3.1 信息报告]
陕西建工股份集团有

[E4]
[§ 1 总则 / 1.2 编制依据]
10 、《陕西建工第十一建设集团有限公司生产安全事故风险评估报告》

[E5]
[§ 1 总则 / 1.2 编制依据]
5 、《陕西省突发公共事件总体应急预案》

[E6]
[§ 3.应急响应 / 5.5 其他保障]
5.5.5 后勤保障

[E7]
[§ 1 总则 / 1.2 编制依据]
11 、《陕西建工第十一建设集团有限公司生产安全事故应急资源调查报告》

[E8]
[§ 3.应急响应 / 5.5 其他保障]
5.5.2 交通运输保障

[E9]
[§ 3.应急响应]
5.0 应急保障

[E10]
[§ 8 附件 / 8.1  单位概况]
隶属关系：陕西建工集团股份有限公司子集团。

[E11]
[§ 3.应急响应 / 5.5 其他保障]
5.5.3 治安保障
```

## latest_clean_scope_0053 (scope_collection)

**Query:** 列举《3.建设工程买卖合同（2025 版）》中“3.建设工程买卖合同（2025 版）.docx”部分的主要条目。

**Doc:** `real_69c6098dd4242eda8c47c6a2`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 493 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 12 | 13 |
| trajectory_steps | n/a | 31 |

### Gold node hits (new)

- `real_69c6098dd4242eda8c47c6a2:L13` [MISS] retrieved=False in_text=False
- `real_69c6098dd4242eda8c47c6a2:L14` [MISS] retrieved=False in_text=False
- `real_69c6098dd4242eda8c47c6a2:L16` [MISS] retrieved=False in_text=False
- `real_69c6098dd4242eda8c47c6a2:L17` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C2` kind=`collect` section=`real_69c6098dd4242eda8c47c6a2:L2` scope=`real_69c6098dd4242eda8c47c6a2:L1` depth=`1`
- reason: Collect the main contract section to list its primary entries as requested.
- collect_section_ids: ['real_69c6098dd4242eda8c47c6a2:L2']
- collect added=8 hits=8 branch_selected=True collect_full=False
- legal_actions (9):
  - C1 | COLLECT | real_69c6098dd4242eda8c47c6a2:L1 | 【         】工程 | score=0.0502
  - C2 | COLLECT | real_69c6098dd4242eda8c47c6a2:L2 | 【         】买卖合同 | score=0.0502
  - C3 | COLLECT | real_69c6098dd4242eda8c47c6a2:L3 | 甲方（买受人）： | score=0.0502
  - C4 | COLLECT | real_69c6098dd4242eda8c47c6a2:L4 | 乙方（出卖人）： | score=0.0420
  - C5 | COLLECT | real_69c6098dd4242eda8c47c6a2:L5 | 签约地点： | score=0.0340
  - C6 | COLLECT | real_69c6098dd4242eda8c47c6a2:L6 | 签约时间： | score=0.0329
  - C7 | COLLECT | real_69c6098dd4242eda8c47c6a2:L7 | 买受人（以下简称甲方）： | score=0.0482
  - C8 | COLLECT | real_69c6098dd4242eda8c47c6a2:L8 | 出卖人（以下简称乙方）： | score=0.0390
  - C9 | COLLECT | real_69c6098dd4242eda8c47c6a2:L9 | 根据《中华人民共和国民法典》等有关法律法规之规定，遵循平等、自愿、公平、诚实信用和绿色原则，经双方协商一致，签订本合同，双方共同遵照执行。 | score=0.0292
- projection_chars: 1183

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c6098dd4242eda8c47c6a2:L1` depth=`1`
- reason: The document root only shows the title and summary. The specific main entries for the 2025 version are not visible in this scope, and no further collection actions are available at this level.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 293

**Step 3** `nav_dispatch`  id=`D1` kind=`dispatch` section=`real_69c6098dd4242eda8c47c6a2:L1` scope=`None` depth=`0`
- reason: Dispatch to collect main entries of the Construction Contract section.
- dispatch_regions: ['real_69c6098dd4242eda8c47c6a2:L1']
- child_reports=1 skipped=0
- legal_actions (49):
  - C1 | COLLECT | real_69c6098dd4242eda8c47c6a2:L1 | 【         】工程 | score=0.0502
  - D1 | DISPATCH | real_69c6098dd4242eda8c47c6a2:L1 | 【         】工程 | score=0.0502
  - C2 | COLLECT | real_69c6098dd4242eda8c47c6a2:L2 | 【         】买卖合同 | score=0.0502
  - D2 | DISPATCH | real_69c6098dd4242eda8c47c6a2:L2 | 【         】买卖合同 | score=0.0502
  - C3 | COLLECT | real_69c6098dd4242eda8c47c6a2:L3 | 甲方（买受人）： | score=0.0502
  - C4 | COLLECT | real_69c6098dd4242eda8c47c6a2:L19 | 第三条  货物质量要求 | score=0.0577
  - D3 | DISPATCH | real_69c6098dd4242eda8c47c6a2:L19 | 第三条  货物质量要求 | score=0.0577
  - C5 | COLLECT | real_69c6098dd4242eda8c47c6a2:L20 | 3.1 质量要求及验收标准的约定： | score=0.0493
  - C6 | COLLECT | real_69c6098dd4242eda8c47c6a2:L23 | 3.3 货物的质量要求应符合有关施工图纸及设计文件要求，有关图纸及设计文件作为合同附件。 | score=0.0577
  - C7 | COLLECT | real_69c6098dd4242eda8c47c6a2:L26 | 3.6 鉴于甲方对货物质量标准的了解程度不及乙方，本合同所列明的各种质量要求或技术质量标准，应执行最高标准。 | score=0.0524
  - C8 | COLLECT | real_69c6098dd4242eda8c47c6a2:L76 | 第十条  合同价款的调整与确定、结算、发票及付款 | score=0.0579
  - D4 | DISPATCH | real_69c6098dd4242eda8c47c6a2:L76 | 第十条  合同价款的调整与确定、结算、发票及付款 | score=0.0579
  - C9 | COLLECT | real_69c6098dd4242eda8c47c6a2:L77 | 10.1  本合同的价款，按下列第（     ）方式确定： | score=0.0579
  - D5 | DISPATCH | real_69c6098dd4242eda8c47c6a2:L77 | 10.1  本合同的价款，按下列第（     ）方式确定： | score=0.0579
  - C10 | COLLECT | real_69c6098dd4242eda8c47c6a2:L78 | （1）固定总价，不可调价，如仅供应部分货物，则按以下方式结算： ； | score=0.0579
  - C11 | COLLECT | real_69c6098dd4242eda8c47c6a2:L91 | 10.4  付款 | score=0.0518
- projection_chars: 3529

**Step 4** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6098dd4242eda8c47c6a2:L76` scope=`real_69c6098dd4242eda8c47c6a2:L76` depth=`1`
- reason: Collecting the full section on contract price adjustment and settlement to list main entries.
- collect_section_ids: ['real_69c6098dd4242eda8c47c6a2:L76']
- collect added=6 hits=6 branch_selected=True collect_full=False
- legal_actions (18):
  - C1 | COLLECT | real_69c6098dd4242eda8c47c6a2:L76 | 第十条  合同价款的调整与确定、结算、发票及付款 | score=0.0579
  - C2 | COLLECT | real_69c6098dd4242eda8c47c6a2:L77 | 10.1  本合同的价款，按下列第（     ）方式确定： | score=0.0579
  - C3 | COLLECT | real_69c6098dd4242eda8c47c6a2:L78 | （1）固定总价，不可调价，如仅供应部分货物，则按以下方式结算： ； | score=0.0579
  - C4 | COLLECT | real_69c6098dd4242eda8c47c6a2:L80 | （3）可调价，调整因素包括： ，调价方式为。 | score=0.0380
  - C5 | COLLECT | real_69c6098dd4242eda8c47c6a2:L91 | 10.4  付款 | score=0.0518
  - C6 | COLLECT | real_69c6098dd4242eda8c47c6a2:L95 | （2）商业承兑汇票、陕建筑信、保理、信用证、付款比例的约定为30 %，如涉及贴现费用，贴现费用由乙方承担； | score=0.0364
  - C7 | COLLECT | real_69c6098dd4242eda8c47c6a2:L98 | 合同履行过程中，甲方有权根据项目实际情况调整付款方式及比例，乙方不得拒绝。 | score=0.0518
  - C8 | COLLECT | real_69c6098dd4242eda8c47c6a2:L99 | 10.4.2 乙方接受以物抵债方式受偿工程款的最低限额不低于本合同结算价款的30%（同上一条）。 | score=0.0427
  - C9 | COLLECT | real_69c6098dd4242eda8c47c6a2:L101 | 当甲方或其上游持有存量商品房的价值小于最低限额的，对于乙方暂未以物抵债受偿的部分，甲方作为债务人应当积极寻找存量商品房进行以物抵债，且有权延后履行该部分债务并不视为甲方违约。 | score=0.0389
  - C10 | COLLECT | real_69c6098dd4242eda8c47c6a2:L110 | 10.5  履约保证金的交付与返还 | score=0.0389
  - C11 | COLLECT | real_69c6098dd4242eda8c47c6a2:L111 | 10.5.1 乙方应在合同签订后日内向甲方提供履约保证金，履约保证金数额： ，缴纳方式：银行转账。履约保证金不计利息。乙方逾期不缴纳履约保证金的，甲方按照履约保证金的2倍，在后续支付合同价款中扣除，直至扣清为止。 | score=0.0347
  - C12 | COLLECT | real_69c6098dd4242eda8c47c6a2:L112 | 10.5.2 履约保证金的返还： 。 | score=0.0349
  - C13 | COLLECT | real_69c6098dd4242eda8c47c6a2:L113 | 10.5.3 甲方有权从履约保证金中直接扣除违约金、赔偿款或罚款等，乙方对此不得提出异议。履约过程中，乙方发生事故（含工伤、伤亡等）不积极处理的，甲方有权代为处理，并按照赔偿金额120%直接从履约保证金中扣除；履约保证金不足的，由乙方另行补足或甲方在支付下次货款中扣除，仍然不足的，甲方有权追偿。 | score=0.0389
  - C14 | COLLECT | real_69c6098dd4242eda8c47c6a2:L115 | 10.6  结算 | score=0.0401
  - C15 | COLLECT | real_69c6098dd4242eda8c47c6a2:L117 | 10.6.2 完工结算：乙方在供货结束后30天内向甲方提出完工结算申请，并提供完整的结算资料，资料清单及份数要求如下。 | score=0.0401
  - C16 | COLLECT | real_69c6098dd4242eda8c47c6a2:L118 | 10.6.3 甲方在收到完工结算申请及完整的结算资料后3个月内完成结算审核，甲方对结算申请有异议的，有权要求乙方进行修正和提供补充资料，甲方审核期限自收到补正或补充资料后重新起算。 | score=0.0358
- projection_chars: 3518

**Step 5** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c6098dd4242eda8c47c6a2:L76` depth=`1`
- reason: The current scope L76 has been collected, and no further sections are visible or available for collection in this subtree.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 189

**Step 6** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6098dd4242eda8c47c6a2:L77` scope=`real_69c6098dd4242eda8c47c6a2:L77` depth=`1`
- reason: Collecting section 10.1 to retrieve the main entries regarding contract pricing methods.
- collect_section_ids: ['real_69c6098dd4242eda8c47c6a2:L77']
- collect added=5 hits=5 branch_selected=True collect_full=False
- legal_actions (6):
  - C1 | COLLECT | real_69c6098dd4242eda8c47c6a2:L77 | 10.1  本合同的价款，按下列第（     ）方式确定： | score=0.0579
  - C2 | COLLECT | real_69c6098dd4242eda8c47c6a2:L78 | （1）固定总价，不可调价，如仅供应部分货物，则按以下方式结算： ； | score=0.0579
  - C3 | COLLECT | real_69c6098dd4242eda8c47c6a2:L79 | （2）固定单价，不可调价； | score=0.0314
  - C4 | COLLECT | real_69c6098dd4242eda8c47c6a2:L80 | （3）可调价，调整因素包括： ，调价方式为。 | score=0.0380
  - C5 | COLLECT | real_69c6098dd4242eda8c47c6a2:L81 | 10.2 如乙方所供货物不能完全符合合同约定，甲方愿意降低标准接收的，货物价格相应予以降低，具体调整方式为： 。 | score=0.0286
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 909

**Step 7** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c6098dd4242eda8c47c6a2:L77` depth=`1`
- reason: The document root L77 has been collected, containing the main entries of the contract.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 189

**Step 8** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6098dd4242eda8c47c6a2:L19` scope=`real_69c6098dd4242eda8c47c6a2:L19` depth=`1`
- reason: Collecting the full section on Article 3 Quality Requirements to list main entries.
- collect_section_ids: ['real_69c6098dd4242eda8c47c6a2:L19']
- collect added=9 hits=9 branch_selected=True collect_full=False
- legal_actions (10):
  - C1 | COLLECT | real_69c6098dd4242eda8c47c6a2:L19 | 第三条  货物质量要求 | score=0.0577
  - C2 | COLLECT | real_69c6098dd4242eda8c47c6a2:L20 | 3.1 质量要求及验收标准的约定： | score=0.0493
  - C3 | COLLECT | real_69c6098dd4242eda8c47c6a2:L21 | 执行标准为： ，其他要求为： 。 | score=0.0325
  - C4 | COLLECT | real_69c6098dd4242eda8c47c6a2:L22 | 3.2 货物质量应符合国家、行业、地方性规范（标准）要求；无国家、行业、地方性规范（标准）的，应符合企业标准，乙方应当提交企业标准，作为合同附件。上述规范（标准）均不存在的，应满足其正常的使用性能要求。 | score=0.0367
  - C5 | COLLECT | real_69c6098dd4242eda8c47c6a2:L23 | 3.3 货物的质量要求应符合有关施工图纸及设计文件要求，有关图纸及设计文件作为合同附件。 | score=0.0577
  - C6 | COLLECT | real_69c6098dd4242eda8c47c6a2:L24 | 3.4 对于甲方要求提前送样的货物，乙方送审的样品获甲方认可且封存后，乙方正式交货时货物的质量、外观、品牌、商标、规格、型号、花色、标识、生产厂家、产品准用证、技术质量检验报告、质量保证书、生产许可证等其他相关技术质量资料应保持和样品一致，否则乙方需承担违约责任，并赔偿甲方的经济损失。 | score=0.0278
  - C7 | COLLECT | real_69c6098dd4242eda8c47c6a2:L25 | 3.5 货物质量还应符合乙方承诺的质量标准。乙方报送甲方的书面资料，包括投标文件或单独的报价文件、乙方（或生产厂家）宣传资料及乙方（或生产厂家）公开宣传的内容，均构成其承诺。 | score=0.0420
  - C8 | COLLECT | real_69c6098dd4242eda8c47c6a2:L26 | 3.6 鉴于甲方对货物质量标准的了解程度不及乙方，本合同所列明的各种质量要求或技术质量标准，应执行最高标准。 | score=0.0524
  - C9 | COLLECT | real_69c6098dd4242eda8c47c6a2:L27 | 3.7 乙方须以书面方式单独向甲方告知货物的贮存、使用条件和方式方法，附随货物清单一并交由甲方指定人员。否则，因此导致货物毁损、灭失或给甲方造成损失的，由乙方承担。 | score=0.0272
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 1968

**Step 9** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c6098dd4242eda8c47c6a2:L19` depth=`1`
- reason: The current scope L19 has been collected, and no further sections are visible or available for collection in this subtree.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 189

**Step 10** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6098dd4242eda8c47c6a2:L91` scope=`real_69c6098dd4242eda8c47c6a2:L91` depth=`1`
- reason: Collecting section C1 covers all payment terms (10.4) including methods, ratios, and property offset details.
- collect_section_ids: ['real_69c6098dd4242eda8c47c6a2:L91']
- collect added=13 hits=13 branch_selected=True collect_full=False
- legal_actions (19):
  - C1 | COLLECT | real_69c6098dd4242eda8c47c6a2:L91 | 10.4  付款 | score=0.0518
  - C2 | COLLECT | real_69c6098dd4242eda8c47c6a2:L92 | 10.4.1 具体付款时间、比例、金额： 。 | score=0.0309
  - C3 | COLLECT | real_69c6098dd4242eda8c47c6a2:L93 | 乙方接受多种付款方式，包括但不限于： | score=0.0232
  - C4 | COLLECT | real_69c6098dd4242eda8c47c6a2:L94 | （1）银行转账、银行承兑汇票，付款比例的约定为10%； | score=0.0274
  - C5 | COLLECT | real_69c6098dd4242eda8c47c6a2:L95 | （2）商业承兑汇票、陕建筑信、保理、信用证、付款比例的约定为30 %，如涉及贴现费用，贴现费用由乙方承担； | score=0.0364
  - C6 | COLLECT | real_69c6098dd4242eda8c47c6a2:L96 | （3）确权贷、供应链融资，或者其他金融产品，付款比例的约定为20%；如涉及贴现费用，贴现费用由乙方承担； | score=0.0246
  - C7 | COLLECT | real_69c6098dd4242eda8c47c6a2:L98 | 合同履行过程中，甲方有权根据项目实际情况调整付款方式及比例，乙方不得拒绝。 | score=0.0518
  - C8 | COLLECT | real_69c6098dd4242eda8c47c6a2:L99 | 10.4.2 乙方接受以物抵债方式受偿工程款的最低限额不低于本合同结算价款的30%（同上一条）。 | score=0.0427
  - C9 | COLLECT | real_69c6098dd4242eda8c47c6a2:L100 | 当甲方或其上游持有存量商品房的价值大于最低限额的，乙方有权自行选择存量商品房（最少为1套，且须同时满足不低于本合同约定的以物抵债最低限额）进行以物抵债。 | score=0.0235
  - C10 | COLLECT | real_69c6098dd4242eda8c47c6a2:L101 | 当甲方或其上游持有存量商品房的价值小于最低限额的，对于乙方暂未以物抵债受偿的部分，甲方作为债务人应当积极寻找存量商品房进行以物抵债，且有权延后履行该部分债务并不视为甲方违约。 | score=0.0389
  - C11 | COLLECT | real_69c6098dd4242eda8c47c6a2:L102 | 10.4.3  乙方指定的财务相关手续的接收、办理人员： | score=0.0278
  - C12 | COLLECT | real_69c6098dd4242eda8c47c6a2:L103 | 姓名： 身份证号： 职务： | score=0.0278
  - C13 | COLLECT | real_69c6098dd4242eda8c47c6a2:L104 | 乙方指定的接收人或银行账户信息错误或发生任何变更的，应立即书面告知甲方。否则，因此给双方造成的一切损失由乙方承担。 | score=0.0227
  - C14 | COLLECT | real_69c6098dd4242eda8c47c6a2:L105 | 10.4.4 甲方支付至乙方指定的企业收款账户及乙方指定的实名制人员收款账户的款项均视为甲方向乙方支付的合同价款，甲方仅对以上支付约定的总金额负责。 | score=0.0257
  - C15 | COLLECT | real_69c6098dd4242eda8c47c6a2:L106 | 10.4.5  乙方指定的企业收款账户为： | score=0.0275
  - C16 | COLLECT | real_69c6098dd4242eda8c47c6a2:L107 | 户名（乙方）： ， | score=0.0275
- projection_chars: 2890

**Step 11** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c6098dd4242eda8c47c6a2:L91` depth=`1`
- reason: The target document section has been collected. No further actions needed.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 189

**Step 12** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6098dd4242eda8c47c6a2:L121` scope=`real_69c6098dd4242eda8c47c6a2:L121` depth=`1`
- reason: Collecting the parent section C1 to retrieve all main entries under Article 11 regarding breach of contract and termination.
- collect_section_ids: ['real_69c6098dd4242eda8c47c6a2:L121']
- collect added=17 hits=17 branch_selected=True collect_full=False
- legal_actions (16):
  - C1 | COLLECT | real_69c6098dd4242eda8c47c6a2:L121 | 第十一条  违约责任及合同的解除 | score=0.0633
  - C2 | COLLECT | real_69c6098dd4242eda8c47c6a2:L122 | 11.1 甲方不能按照本合同约定时间支付乙方合同款项，应自应付相关款项之日起，以应付未付款为基数，按照同期中国人民银行授权全国银行间同业拆借中心公布的贷款市场报价利率（LPR）向乙方承担违约责任。甲方违约行为应承担的违约赔偿责任（含违约金或赔偿金），总额以10000（约定违约金总额不得超过合同暂定总价的1%）元为上限。 | score=0.0289
  - C3 | COLLECT | real_69c6098dd4242eda8c47c6a2:L123 | 11.2 乙方未按合同约定的时间履行其交货义务（包括安装、调试、检测等义务）的，每迟延一日，按元/日的标准承担迟延违约金；甲方工地停工待料产生的费用（包括但不限于：机械租赁费、设施材料租赁费、项目部管理人员工资、待工工人工资及建设单位罚款）等实际损失高于该标准的，按实际损失赔偿。乙方迟延供货超过日，甲方有权解除合同。 | score=0.0556
  - C4 | COLLECT | real_69c6098dd4242eda8c47c6a2:L124 | 乙方供应的货物质量不符合约定或产权不合法，甲方要求或同意更换货物的，执行上款规定，如乙方拒绝退、换货物，或在天以内不予退、换货的，甲方有权解除本合同。乙方应按不合格货物价款的%向甲方承担违约金。 | score=0.0321
  - C5 | COLLECT | real_69c6098dd4242eda8c47c6a2:L125 | 11.3 因乙方违约，甲方解除合同的，乙方除按第11.2条款约定承担迟延供货违约金外，还应额外承担元违约金，以弥补甲方另行购买所发生的误工及其他损失。 | score=0.0338
  - C6 | COLLECT | real_69c6098dd4242eda8c47c6a2:L126 | 11.4 乙方应保证在任何情况下甲方免受任何因乙方原因引起的协助执行及相关司法协助，否则视为乙方违约，并向甲方承担合同暂定含税总价3%的违约金。 | score=0.0271
  - C7 | COLLECT | real_69c6098dd4242eda8c47c6a2:L128 | 11.6 乙方违约的，甲方可从当期应付款中直接扣除相应的违约金，或在结算中扣减相应价款，也可另行追偿。 | score=0.0294
  - C8 | COLLECT | real_69c6098dd4242eda8c47c6a2:L129 | 11.7 因乙方原因引起的诉讼、仲裁牵连甲方的，法律责任由乙方实际承担。因司法既判力导致甲方代乙方履行的，甲方可在应支付乙方款项中直接扣除或追偿。 | score=0.0271
  - C9 | COLLECT | real_69c6098dd4242eda8c47c6a2:L130 | 乙方同时应确保甲方免受任何因乙方原因引起的诉讼、仲裁，否则视为乙方违约，每次乙方需向甲方承担合同含税总价3%的违约金，并承担甲方因诉讼、仲裁所产生的相关费用（包括但不限于：诉讼/仲裁费、律师费、保全费、公证费、差旅费等），且甲方可在应支付乙方款项中直接扣除或追偿。 | score=0.0319
  - C10 | COLLECT | real_69c6098dd4242eda8c47c6a2:L131 | 11.8 因非甲方问题造成退换货的，退换货所需的运费、吊装费等相关费用由乙方承担。由此造成相应损失，如返工、工期延误等经济和工期损失由乙方承担。在任何情况下，甲方均有权单方解除本合同。甲方解除本合同时，尚未发生的货款不再支付且甲方无须承担违约责任。乙方应按照本合同相关条款规定办理退还及结算手续。 | score=0.0251
  - C11 | COLLECT | real_69c6098dd4242eda8c47c6a2:L132 | 11.9 为进一步畅通双方的沟通渠道，保障洽商畅通，双方在履约过程中产生争议的，乙方通过下列方式依次与甲方相关人员、部门取得联系以解决争议： | score=0.0535
  - C12 | COLLECT | real_69c6098dd4242eda8c47c6a2:L133 | （1）甲方项目部联系人： ，联系电话： ； | score=0.0633
  - C13 | COLLECT | real_69c6098dd4242eda8c47c6a2:L135 | （3）前述人员仍未协调一致的，可联系甲方工程管理部协调解决，联系电话：029-33268142； | score=0.0449
  - C14 | COLLECT | real_69c6098dd4242eda8c47c6a2:L136 | （4）上述渠道均未能协调解决的，可联系甲方法务部门组织调解，联系电话：029-33270772。 | score=0.0295
  - C15 | COLLECT | real_69c6098dd4242eda8c47c6a2:L137 | 乙方未通过上述方式依次联系甲方积极协商解决争议，而直接通过其他方式上访(信访)、投诉(举报)或通过诉讼、仲裁手段提起解决争议或因乙方原因（含恶意上访(信访）、恶意投诉(举报)等对甲方产生不良影响或导致甲方承担行政处罚的，均视为乙方违约，乙方应当承担合同签约含税总价5%的违约金及甲方因诉讼、仲裁所产生的诉讼费、仲裁费、律师代理费、保全费、差旅费等相关费用。 | score=0.0327
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 3781

**Step 13** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c6098dd4242eda8c47c6a2:L121` depth=`1`
- reason: The target document section has been collected. No further actions needed.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 190

**Step 14** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6098dd4242eda8c47c6a2:L160` scope=`real_69c6098dd4242eda8c47c6a2:L160` depth=`1`
- reason: Collecting the full 'Dispute Resolution' section to list its main entries as requested.
- collect_section_ids: ['real_69c6098dd4242eda8c47c6a2:L160']
- collect added=8 hits=8 branch_selected=True collect_full=False
- legal_actions (9):
  - C1 | COLLECT | real_69c6098dd4242eda8c47c6a2:L160 | 第十四条  争议解决 | score=0.0584
  - C2 | COLLECT | real_69c6098dd4242eda8c47c6a2:L161 | (一)本合同各方一致同意将因本合同产生或与本合同履行有关的任何争议或分歧在与甲方协调未果后，先行提交陕西省司法局下设陕西正和商事调解中心按当时实行的调解规则调解,且该调解规则自动并入本条款。此约定与调解可能达成的共识,对各方均有约束力。（注：陕西正和商事调解中心是在深入贯彻落实中央关于坚持和发展新时代“枫桥经验"重要指示精神,由陕西省司法厅业务主管、陕西省民政厅依法登记设立的省属调解机构。该机构在 | score=0.0492
  - C3 | COLLECT | real_69c6098dd4242eda8c47c6a2:L162 | (二)调解成功的,双方可以将调解协议通过有管辖权的人民法院进行司法确认、通过咸阳仲裁委员会申请仲裁确认或通过双方约定的公证机构出具公证书，也可以其他方式使得调解文书具备强制执行的效力。 | score=0.0208
  - C4 | COLLECT | real_69c6098dd4242eda8c47c6a2:L163 | (三)调解未果的，由陕西正和商事调解中心出具《结案报告》。持该《结案报告》， 按下列第1种方式办理立案手续，解决争议： | score=0.0397
  - C5 | COLLECT | real_69c6098dd4242eda8c47c6a2:L164 | （1）提交咸阳仲裁委员会仲裁，按照申请时行之有效的仲裁规则进行仲裁。仲裁裁决是终局的，对双方均有约束力。 | score=0.0215
  - C6 | COLLECT | real_69c6098dd4242eda8c47c6a2:L165 | （2）向甲方法人住所地人民法院起诉。 | score=0.0204
  - C7 | COLLECT | real_69c6098dd4242eda8c47c6a2:L166 | 本协议特别约定争议先行调解机制，系落实新时代"枫桥经验"的具体举措。任何一方若未经该中心调解，直接提起诉讼或者选择仲裁，构成重大违约，需按照原合同金额的1%向对方承担违约责任，该金额由法院或者仲裁委在作出裁判时予以扣减。 | score=0.0353
  - C8 | COLLECT | real_69c6098dd4242eda8c47c6a2:L167 | 双方已对本协议各条款进行了仔细阅读，双方已就全部内容向对方进行了解释说明，就其中的工程款支付条款、谅解期条款、诉前争议解决条款等免除或减轻甲方责任条款的概念、内容和法律后果作了明确说明，双方完全理解并接受，同意签约。 | score=0.0584
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 2039

**Step 15** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c6098dd4242eda8c47c6a2:L160` depth=`1`
- reason: The document root L160 has been collected, providing the main structure of the contract. No further sections are visible or needed.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 190

**Step 16** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6098dd4242eda8c47c6a2:L139` scope=`real_69c6098dd4242eda8c47c6a2:L139` depth=`1`
- reason: Collect section 12.1 to retrieve the main entries regarding authorized personnel and their powers.
- collect_section_ids: ['real_69c6098dd4242eda8c47c6a2:L139']
- collect added=3 hits=3 branch_selected=True collect_full=False
- legal_actions (8):
  - C1 | COLLECT | real_69c6098dd4242eda8c47c6a2:L139 | 12.1  甲方授权以下人员行使履约过程中的各项职权： | score=0.0542
  - C2 | COLLECT | real_69c6098dd4242eda8c47c6a2:L140 | （1）     （身份证号码     联系电话     ） | score=0.0345
  - C3 | COLLECT | real_69c6098dd4242eda8c47c6a2:L141 | 职权：收货、接收乙方提交的发票和货物的技术质量证明资料； | score=0.0345
  - C4 | COLLECT | real_69c6098dd4242eda8c47c6a2:L142 | （2）     （身份证号码     联系电话     ） | score=0.0542
  - C5 | COLLECT | real_69c6098dd4242eda8c47c6a2:L143 | 职权：签署结算单据，依据本合同约定处理索赔事宜。 | score=0.0340
  - C6 | COLLECT | real_69c6098dd4242eda8c47c6a2:L144 | 甲方对上述人员的授权，有效期最长不超过2年或者乙方全部供货完成后3个月（以最先到达日为准）。 | score=0.0448
  - C7 | COLLECT | real_69c6098dd4242eda8c47c6a2:L145 | 未取得甲方书面授权的人员所签署的任何文件、协议，以及获得授权的人员超越书面授权范围所签署的任何文件、协议，即便加盖有甲方项目部印章或分公司印章，均一概无效，甲方对此不承担责任。乙方经认真阅读充分理解并承诺认可：任何形式的逾期付款加价条款均非甲方真实意思表示，任何单位或个人与乙方达成的与本合同有关的逾期付款加价条款的约定均系合同诈骗行为，与甲方无关。 | score=0.0542
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 1486

**Step 17** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c6098dd4242eda8c47c6a2:L139` depth=`1`
- reason: The target document section has been collected, providing sufficient evidence to list the main entries.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 190

**Step 18** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6098dd4242eda8c47c6a2:L138` scope=`real_69c6098dd4242eda8c47c6a2:L138` depth=`1`
- reason: Collecting Article 12 to list main entries of the contract authorization section.
- collect_section_ids: ['real_69c6098dd4242eda8c47c6a2:L138']
- collect added=3 hits=3 branch_selected=True collect_full=False
- legal_actions (13):
  - C1 | COLLECT | real_69c6098dd4242eda8c47c6a2:L138 | 第十二条  合同授权 | score=0.0542
  - C2 | COLLECT | real_69c6098dd4242eda8c47c6a2:L139 | 12.1  甲方授权以下人员行使履约过程中的各项职权： | score=0.0542
  - C3 | COLLECT | real_69c6098dd4242eda8c47c6a2:L140 | （1）     （身份证号码     联系电话     ） | score=0.0345
  - C4 | COLLECT | real_69c6098dd4242eda8c47c6a2:L141 | 职权：收货、接收乙方提交的发票和货物的技术质量证明资料； | score=0.0345
  - C5 | COLLECT | real_69c6098dd4242eda8c47c6a2:L142 | （2）     （身份证号码     联系电话     ） | score=0.0542
  - C6 | COLLECT | real_69c6098dd4242eda8c47c6a2:L143 | 职权：签署结算单据，依据本合同约定处理索赔事宜。 | score=0.0340
  - C7 | COLLECT | real_69c6098dd4242eda8c47c6a2:L144 | 甲方对上述人员的授权，有效期最长不超过2年或者乙方全部供货完成后3个月（以最先到达日为准）。 | score=0.0448
  - C8 | COLLECT | real_69c6098dd4242eda8c47c6a2:L145 | 未取得甲方书面授权的人员所签署的任何文件、协议，以及获得授权的人员超越书面授权范围所签署的任何文件、协议，即便加盖有甲方项目部印章或分公司印章，均一概无效，甲方对此不承担责任。乙方经认真阅读充分理解并承诺认可：任何形式的逾期付款加价条款均非甲方真实意思表示，任何单位或个人与乙方达成的与本合同有关的逾期付款加价条款的约定均系合同诈骗行为，与甲方无关。 | score=0.0542
  - C9 | COLLECT | real_69c6098dd4242eda8c47c6a2:L146 | 12.2  乙方授权以下人员行使履约过程中的各项职权： | score=0.0395
  - C10 | COLLECT | real_69c6098dd4242eda8c47c6a2:L147 | （1） （身份证号码联系电话微信号），全权负责本合同的履行，包括但不限于：签署发料单，签收甲方发出的各类通知，确认结算金额，变更合同条款，处理索赔事宜等。 | score=0.0352
  - C11 | COLLECT | real_69c6098dd4242eda8c47c6a2:L148 | 12.3 甲方的任何人员及分支机构均无权对外实施借贷、融资、担保及收取保证金行为，乙方对此已知悉，若发生此类行为，乙方自行承担相应后果，与甲方无关。 | score=0.0395
  - C12 | COLLECT | real_69c6098dd4242eda8c47c6a2:L149 | 12.4 合同履行过程中，任何一方变更合同授权人员或权限的，必须提前7 天书面通知对方，以保证货物交接顺利。 | score=0.0299
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 2488

**Step 19** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c6098dd4242eda8c47c6a2:L138` depth=`1`
- reason: The current scope L138 has been collected, and no further sections are visible or available for collection in this subtree. The task is complete.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 190

**Step 20** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6098dd4242eda8c47c6a2:L175` scope=`real_69c6098dd4242eda8c47c6a2:L175` depth=`1`
- reason: Collecting the full 'Other Agreements' section to list all main items as requested.
- collect_section_ids: ['real_69c6098dd4242eda8c47c6a2:L175']
- collect added=15 hits=15 branch_selected=True collect_full=False
- legal_actions (16):
  - C1 | COLLECT | real_69c6098dd4242eda8c47c6a2:L175 | 第十八条  其他约定 | score=0.0625
  - C2 | COLLECT | real_69c6098dd4242eda8c47c6a2:L176 | 18.1 甲方项目公章仅用于双方往来函件、会议纪要、工程洽商变更、工程签证、结算、索赔等，用于担保、抵押、融资及经济合同无效。 | score=0.0482
  - C3 | COLLECT | real_69c6098dd4242eda8c47c6a2:L177 | 18.2 双方或一方签认的单据上（包括但不限于验收单、结算单、催款函等单据）如有与本合同条款约定不一致的内容，均以本合同条款为准。 | score=0.0342
  - C4 | COLLECT | real_69c6098dd4242eda8c47c6a2:L178 | 18.3 本合同约定的违约金一经甲方签认，凭照片、处罚通知单等即可在当月兑现/扣除，无需乙方书面签字同意。 | score=0.0231
  - C5 | COLLECT | real_69c6098dd4242eda8c47c6a2:L179 | 18.4 为保障项目实施，乙方选择的下游供应商，应当经过甲方考察并书面同意后，方可签约并用于本项目。同时，乙方与下游供应商之间的所有合同，应当将争议管辖约定为“因本合同引起的或与本合同有关的任何争议，均提请西安仲裁委员会按照其仲裁规则进行仲裁”。若乙方未遵从本条款，致使甲方在诉讼中被列为被告、第三人、或者其他诉讼当事人的，视为乙方违约，乙方需向甲方承担原合同含税总价3%的违约金并承担甲方的律师费。 | score=0.0513
  - C6 | COLLECT | real_69c6098dd4242eda8c47c6a2:L180 | 18.5 乙方已对本合同各条款进行了仔细阅读（特别是加粗的条款），甲方已就合同全部内容进行了解释说明，就其中的工程款支付条款、谅解期条款、诉前争议解决条款等免除或减轻甲方责任条款的概念、内容和法律后果作了明确说明，双方完全理解并接受，同意签约。 | score=0.0582
  - C7 | COLLECT | real_69c6098dd4242eda8c47c6a2:L181 | 18.6 补充约定： | score=0.0267
  - C8 | COLLECT | real_69c6098dd4242eda8c47c6a2:L182 | 双方共同确认：甲方在该项目投入的资金来自建设单位支付的工程款，项目建设过程中建设单位存在迟延支付工程款的可能，双方愿共担风险。 | score=0.0625
  - C9 | COLLECT | real_69c6098dd4242eda8c47c6a2:L183 | 进度付款比例及方式：依据双方确认的过程报量单预结算价款，按照支付节点支付过程价款；具体约定为： 。 | score=0.0283
  - C10 | COLLECT | real_69c6098dd4242eda8c47c6a2:L184 | 谅解期约定：若因甲方资金暂时困难，未能按原合同约定比例、付款方式支付款项，乙方同意给予甲方3 个月的谅解期。谅解期内，甲方未足额支付款项不视为违约，乙方不得追究违约责任，乙方需保证连续正常施工（供货），不影响项目进度，甲方以原合同约定支付比例的应付未付款项为基数按照中国人民银行同期活期存款利率给予乙方适当的经济补偿。 | score=0.0402
  - C11 | COLLECT | real_69c6098dd4242eda8c47c6a2:L185 | 逾期利息补偿：超过谅解期3个月的：自谅解期届满之日起，甲方以原合同约定支付比例的应付未付款项为基数，按照全国银行间同业拆借中心公布的一年期贷款市场报价利率（LPR）向乙方支付逾期利息。利息计算起始日为谅解期届满次日。 | score=0.0252
  - C12 | COLLECT | real_69c6098dd4242eda8c47c6a2:L186 | 特别支付条款：工程（货物）检验验收合格且结算完成后满1 年的，甲方对乙方的付款比例不低于已结算价款的60%。满2 年的，甲方对乙方的付款比例不低于已结算价款的80%。满3 年的：甲方对乙方的付款比例不低于已结算价款的90%。 | score=0.0401
  - C13 | COLLECT | real_69c6098dd4242eda8c47c6a2:L187 | 若乙方提出关键经济条件变动（非因自然灾害、政策调整等不可抗力导致），包括：提前支付、提高支付比例、提高现金支付比例（不含农民工工资专用账户支付部分）、减少以房抵债比例（不低于合同约定的最低接受限额），需经双方签订补充协议书面确认后执行，但每变动一项，对应结算单价下浮3%， 多项变动累加计算，累计下浮比例最高不超过15%，补充协议需明确变动后的支付条件、单价调整期限及计算基数，确保变动过程透明合规。 | score=0.0459
  - C14 | COLLECT | real_69c6098dd4242eda8c47c6a2:L188 | 本合同文件的优先解释顺序为：本合同及其附件、招标文件、中标通知书、其他相关文件。 | score=0.0510
  - C15 | COLLECT | real_69c6098dd4242eda8c47c6a2:L189 | 其他约定： 。 | score=0.0283
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 3589

**Step 21** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c6098dd4242eda8c47c6a2:L175` depth=`1`
- reason: The target document section has been collected. No further actions needed to list its main entries.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 190

**Step 22** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6098dd4242eda8c47c6a2:L142` scope=`real_69c6098dd4242eda8c47c6a2:L142` depth=`1`
- reason: Collecting all visible sections under the current scope to list main entries of the contract.
- collect_section_ids: ['real_69c6098dd4242eda8c47c6a2:L142', 'real_69c6098dd4242eda8c47c6a2:L143', 'real_69c6098dd4242eda8c47c6a2:L144', 'real_69c6098dd4242eda8c47c6a2:L145']
- collect added=7 hits=7 branch_selected=True collect_full=True
- legal_actions (5):
  - C1 | COLLECT | real_69c6098dd4242eda8c47c6a2:L142 | （2）     （身份证号码     联系电话     ） | score=0.0542
  - C2 | COLLECT | real_69c6098dd4242eda8c47c6a2:L143 | 职权：签署结算单据，依据本合同约定处理索赔事宜。 | score=0.0340
  - C3 | COLLECT | real_69c6098dd4242eda8c47c6a2:L144 | 甲方对上述人员的授权，有效期最长不超过2年或者乙方全部供货完成后3个月（以最先到达日为准）。 | score=0.0448
  - C4 | COLLECT | real_69c6098dd4242eda8c47c6a2:L145 | 未取得甲方书面授权的人员所签署的任何文件、协议，以及获得授权的人员超越书面授权范围所签署的任何文件、协议，即便加盖有甲方项目部印章或分公司印章，均一概无效，甲方对此不承担责任。乙方经认真阅读充分理解并承诺认可：任何形式的逾期付款加价条款均非甲方真实意思表示，任何单位或个人与乙方达成的与本合同有关的逾期付款加价条款的约定均系合同诈骗行为，与甲方无关。 | score=0.0542
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 1029

**Step 23** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c6098dd4242eda8c47c6a2:L142` depth=`1`
- reason: The document root L142 has been collected, containing the main entries of the contract. No further collection is needed.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 190

**Step 24** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6098dd4242eda8c47c6a2:L208` scope=`real_69c6098dd4242eda8c47c6a2:L208` depth=`1`
- reason: Collecting the full section '第二条 甲方及其人员的责任' to list its main items as requested.
- collect_section_ids: ['real_69c6098dd4242eda8c47c6a2:L208']
- collect added=9 hits=9 branch_selected=True collect_full=False
- legal_actions (10):
  - C1 | COLLECT | real_69c6098dd4242eda8c47c6a2:L208 | 第二条 甲方及其人员的责任 | score=0.0496
  - C2 | COLLECT | real_69c6098dd4242eda8c47c6a2:L209 | （一）不得索要或接受乙方及其相关单位和人员提供的回扣、礼金、预付卡、电子红包、贵重物品等。 | score=0.0272
  - C3 | COLLECT | real_69c6098dd4242eda8c47c6a2:L210 | （二）不得在乙方及其相关单位报销任何应由甲方或个人支付的费用。 | score=0.0226
  - C4 | COLLECT | real_69c6098dd4242eda8c47c6a2:L211 | （三）不得违反规定在乙方及其相关单位投资入股，不得向乙方及其人员借款或委托买卖股票、债券等。 | score=0.0386
  - C5 | COLLECT | real_69c6098dd4242eda8c47c6a2:L212 | （四）不得要求、暗示和接受乙方及其相关单位和个人为其购买或装修住房、婚丧嫁娶、配偶和子女的上学或工作安排以及出国境、旅游等提供方便。 | score=0.0392
  - C6 | COLLECT | real_69c6098dd4242eda8c47c6a2:L213 | （五）不得参加乙方及其相关单位安排的工作宴请及健身、娱乐等活动。 | score=0.0236
  - C7 | COLLECT | real_69c6098dd4242eda8c47c6a2:L214 | （六）不得接受乙方及其相关单位购置或提供的通讯工具、交通工具和高档办公用品。 | score=0.0262
  - C8 | COLLECT | real_69c6098dd4242eda8c47c6a2:L215 | （七）甲方工作人员不得向乙方介绍家属或亲友从事与甲方工程有关的材料设备供应、工程分包等经济活动。 | score=0.0496
  - C9 | COLLECT | real_69c6098dd4242eda8c47c6a2:L216 | （八）不得利用职权和工作之便向乙方提出上述各项规定禁止事项或要求之外的与工作业务无关的事项或要求。 | score=0.0317
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 1616

**Step 25** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c6098dd4242eda8c47c6a2:L208` depth=`1`
- reason: The document root has been collected, which includes the main structure of the contract. No further collection is needed.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 190

**Step 26** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6098dd4242eda8c47c6a2:L233` scope=`real_69c6098dd4242eda8c47c6a2:L233` depth=`1`
- reason: Collects the full 'Legal Representative Authorization Letter' section to identify its main entries.
- collect_section_ids: ['real_69c6098dd4242eda8c47c6a2:L233']
- collect added=3 hits=3 branch_selected=True collect_full=False
- legal_actions (4):
  - C1 | COLLECT | real_69c6098dd4242eda8c47c6a2:L233 | 法定代表人授权委托书 | score=0.0513
  - C2 | COLLECT | real_69c6098dd4242eda8c47c6a2:L234 | 本授权委托书声明：本人（法人姓名）系（乙方公司名称）的法定代表人，现授权委托（代理人姓名）为我公司代理人，以本公司的名义签署工程的编号为（合同编号）的项目分供合同，代理一切文件签署和有关的一切事务，我司均予以承认。 | score=0.0513
  - C3 | COLLECT | real_69c6098dd4242eda8c47c6a2:L235 | 代理人无权出具委托书。 | score=0.0209
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 743

**Step 27** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c6098dd4242eda8c47c6a2:L233` depth=`1`
- reason: The document root has been collected, providing the main structure of the contract. No further collection is needed.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 190

**Step 28** `nav_collect`  id=`C1` kind=`collect` section=`real_69c6098dd4242eda8c47c6a2:L225` scope=`real_69c6098dd4242eda8c47c6a2:L225` depth=`1`
- reason: Collecting all visible sections under the contract to list main entries as requested.
- collect_section_ids: ['real_69c6098dd4242eda8c47c6a2:L225', 'real_69c6098dd4242eda8c47c6a2:L226', 'real_69c6098dd4242eda8c47c6a2:L227', 'real_69c6098dd4242eda8c47c6a2:L228']
- collect added=7 hits=7 branch_selected=True collect_full=True
- legal_actions (5):
  - C1 | COLLECT | real_69c6098dd4242eda8c47c6a2:L225 | 第四条 违约责任 | score=0.0591
  - C2 | COLLECT | real_69c6098dd4242eda8c47c6a2:L226 | （一）甲方及其人员有违反本协议书第一条、第二条规定的，按照管理权限，依据有关法律法规和规定给予有关人员纪律处分或组织处理；涉嫌犯罪的，移交司法机关追究刑事责任。 | score=0.0340
  - C3 | COLLECT | real_69c6098dd4242eda8c47c6a2:L227 | （二）乙方及其人员有违反本协议书第一条、第三条规定的，甲方有权要求乙方赔偿由此给甲方造成的损失，有权将乙方列入陕建集团黑名单，并有权解除合同；涉嫌犯罪的，建议司法机关追究刑事责任。 | score=0.0591
  - C4 | COLLECT | real_69c6098dd4242eda8c47c6a2:L228 | 第五条本协议书一式陆份，甲方肆份，乙方贰份，其中一份由甲方报甲方公司纪委办公室备案。 | score=0.0397
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 997

**Step 29** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c6098dd4242eda8c47c6a2:L225` depth=`1`
- reason: Collected the main section L225 containing the contract title and structure. Ready to list entries.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 190

**Step 30** `nav_dispatch`  id=`D1` kind=`dispatch` section=`real_69c6098dd4242eda8c47c6a2:L19` scope=`None` depth=`0`
- reason: Dispatch all remaining major sections to collect main entries of the contract.
- dispatch_regions: ['real_69c6098dd4242eda8c47c6a2:L19', 'real_69c6098dd4242eda8c47c6a2:L76', 'real_69c6098dd4242eda8c47c6a2:L77', 'real_69c6098dd4242eda8c47c6a2:L91', 'real_69c6098dd4242eda8c47c6a2:L121', 'real_69c6098dd4242eda8c47c6a2:L138', 'real_69c6098dd4242eda8c47c6a2:L139', 'real_69c6098dd4242eda8c47c6a2:L142', 'real_69c6098dd4242eda8c47c6a2:L160', 'real_69c6098dd4242eda8c47c6a2:L175', 'real_69c6098dd4242eda8c47c6a2:L208', 'real_69c6098dd4242eda8c47c6a2:L225', 'real_69c6098dd4242eda8c47c6a2:L233']
- child_reports=13 skipped=0
- legal_actions (45):
  - C1 | COLLECT | real_69c6098dd4242eda8c47c6a2:L19 | 第三条  货物质量要求 | score=0.0577
  - D1 | DISPATCH | real_69c6098dd4242eda8c47c6a2:L19 | 第三条  货物质量要求 | score=0.0577
  - C2 | COLLECT | real_69c6098dd4242eda8c47c6a2:L20 | 3.1 质量要求及验收标准的约定： | score=0.0493
  - C3 | COLLECT | real_69c6098dd4242eda8c47c6a2:L23 | 3.3 货物的质量要求应符合有关施工图纸及设计文件要求，有关图纸及设计文件作为合同附件。 | score=0.0577
  - C4 | COLLECT | real_69c6098dd4242eda8c47c6a2:L26 | 3.6 鉴于甲方对货物质量标准的了解程度不及乙方，本合同所列明的各种质量要求或技术质量标准，应执行最高标准。 | score=0.0524
  - C5 | COLLECT | real_69c6098dd4242eda8c47c6a2:L76 | 第十条  合同价款的调整与确定、结算、发票及付款 | score=0.0579
  - D2 | DISPATCH | real_69c6098dd4242eda8c47c6a2:L76 | 第十条  合同价款的调整与确定、结算、发票及付款 | score=0.0579
  - C6 | COLLECT | real_69c6098dd4242eda8c47c6a2:L77 | 10.1  本合同的价款，按下列第（     ）方式确定： | score=0.0579
  - D3 | DISPATCH | real_69c6098dd4242eda8c47c6a2:L77 | 10.1  本合同的价款，按下列第（     ）方式确定： | score=0.0579
  - C7 | COLLECT | real_69c6098dd4242eda8c47c6a2:L78 | （1）固定总价，不可调价，如仅供应部分货物，则按以下方式结算： ； | score=0.0579
  - C8 | COLLECT | real_69c6098dd4242eda8c47c6a2:L91 | 10.4  付款 | score=0.0518
  - D4 | DISPATCH | real_69c6098dd4242eda8c47c6a2:L91 | 10.4  付款 | score=0.0518
  - C9 | COLLECT | real_69c6098dd4242eda8c47c6a2:L98 | 合同履行过程中，甲方有权根据项目实际情况调整付款方式及比例，乙方不得拒绝。 | score=0.0518
  - C10 | COLLECT | real_69c6098dd4242eda8c47c6a2:L121 | 第十一条  违约责任及合同的解除 | score=0.0633
  - D5 | DISPATCH | real_69c6098dd4242eda8c47c6a2:L121 | 第十一条  违约责任及合同的解除 | score=0.0633
  - C11 | COLLECT | real_69c6098dd4242eda8c47c6a2:L123 | 11.2 乙方未按合同约定的时间履行其交货义务（包括安装、调试、检测等义务）的，每迟延一日，按元/日的标准承担迟延违约金；甲方工地停工待料产生的费用（包括但不限于：机械租赁费、设施材料租赁费、项目部管理人员工资、待工工人工资及建设单位罚款）等实际损失高于该标准的，按实际损失赔偿。乙方迟延供货超过日，甲方有权解除合同。 | score=0.0556
- projection_chars: 3416

**Step 31** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Collected evidence covers all main contract entries including title, parties, quality, pricing, payment, authorization, liability, and dispute resolution.
- legal_actions (46):
  - C1 | COLLECT | real_69c6098dd4242eda8c47c6a2:L10 | 第一条  概况 | score=0.0431
  - D1 | DISPATCH | real_69c6098dd4242eda8c47c6a2:L10 | 第一条  概况 | score=0.0431
  - C2 | COLLECT | real_69c6098dd4242eda8c47c6a2:L11 | 1.1  工程概况 | score=0.0431
  - D2 | DISPATCH | real_69c6098dd4242eda8c47c6a2:L11 | 1.1  工程概况 | score=0.0431
  - C3 | COLLECT | real_69c6098dd4242eda8c47c6a2:L12 | 工程名称： ； | score=0.0431
  - C4 | COLLECT | real_69c6098dd4242eda8c47c6a2:L13 | 工程施工地点： 省市县（区） 街道（乡/镇） 路号（地点需详尽） ； | score=0.0422
  - C5 | COLLECT | real_69c6098dd4242eda8c47c6a2:L18 | 第二条  货物名称、规格型号、材质、单价及计划数量等 | score=0.0457
  - C6 | COLLECT | real_69c6098dd4242eda8c47c6a2:L28 | 第四条  交货时间按下列第（     ）种方式确定 | score=0.0368
  - D3 | DISPATCH | real_69c6098dd4242eda8c47c6a2:L28 | 第四条  交货时间按下列第（     ）种方式确定 | score=0.0368
  - C7 | COLLECT | real_69c6098dd4242eda8c47c6a2:L31 | （3）其他： 。 | score=0.0368
  - C8 | COLLECT | real_69c6098dd4242eda8c47c6a2:L36 | 第六条  货物数量及质量的验收 | score=0.0434
  - D4 | DISPATCH | real_69c6098dd4242eda8c47c6a2:L36 | 第六条  货物数量及质量的验收 | score=0.0434
  - C9 | COLLECT | real_69c6098dd4242eda8c47c6a2:L42 | 6.3 交货时，乙方应向甲方一并提交满足货物使用的有关工程竣工验收资料的规定及符合要求的货物质量证明资料，包括但不限于：《产品合格证明》、《质量检验报告》、《产品质量保证书》、《产品准用证》、其他及相应保存和使用说明等，如提供复印件的，需加盖乙方公章。若乙方未能随货交付前述资料，视为货物交付未完成，直至提供前述合格资料后起算租赁费。备品、配件工具及数量按照合同清单及约定要求提供。 | score=0.0391
  - C10 | COLLECT | real_69c6098dd4242eda8c47c6a2:L45 | 6.6 甲方采取抽样验收合格的，不能视为乙方全部货物质量合格。如在使用时或使用后发现确实因该货物质量未达到规定要求而造成相应损失，如返工、工期延误等经济和工期损失由乙方承担。所造成的经济损失，甲方可直接从应付款中扣除。对于由该质量问题引起的工程坍塌、人员伤亡等质量及安全事故，乙方应承担经济和法律责任。 | score=0.0434
  - C11 | COLLECT | real_69c6098dd4242eda8c47c6a2:L48 | 第七条  包装、运输及附件 | score=0.0432
  - D5 | DISPATCH | real_69c6098dd4242eda8c47c6a2:L48 | 第七条  包装、运输及附件 | score=0.0432
- projection_chars: 3552

### Subagent reports_context

```
=== Investigate results (13 region(s)) ===
[region 1] real_69c6098dd4242eda8c47c6a2:L76 (ok)
collected 45 branch node(s); explicit roots=['real_69c6098dd4242eda8c47c6a2:L76']
collected: real_69c6098dd4242eda8c47c6a2:L100, real_69c6098dd4242eda8c47c6a2:L101, real_69c6098dd4242eda8c47c6a2:L102, real_69c6098dd4242eda8c47c6a2:L103, real_69c6098dd4242eda8c47c6a2:L104, real_69c6098dd4242eda8c47c6a2:L105, real_69c6098dd4242eda8c47c6a2:L106, real_69c6098dd4242eda8c47c6a2:L107, real_69c6098dd4242eda8c47c6a2:L108, real_69c6098dd4242eda8c47c6a2:L109, real_69c6098dd4242eda8c47c6a2:L110, real_69c6098dd4242eda8c47c6a2:L111, real_69c6098dd4242eda8c47c6a2:L112, real_69c6098dd4242eda8c47c6a2:L113, real_69c6098dd4242eda8c47c6a2:L114, real_69c6098dd4242eda8c47c6a2:L115, real_69c6098dd4242eda8c47c6a2:L116, real_69c6098dd4242eda8c47c6a2:L117, real_69c6098dd4242eda8c47c6a2:L118, real_69c6098dd4242eda8c47c6a2:L119
reason: The current scope L76 has been collected, and no further sections are visible or available for collection in this subtree.
---
[region 2] real_69c6098dd4242eda8c47c6a2:L77 (ok)
collected 5 branch node(s); explicit roots=['real_69c6098dd4242eda8c47c6a2:L77']
collected: real_69c6098dd4242eda8c47c6a2:L77, real_69c6098dd4242eda8c47c6a2:L78, real_69c6098dd4242eda8c47c6a2:L79, real_69c6098dd4242eda8c47c6a2:L80, real_69c6098dd4242eda8c47c6a2:L81
reason: The document root L77 has been collected, containing the main entries of the contract.
---
[region 3] real_69c6098dd4242eda8c47c6a2:L19 (ok)
collected 9 branch node(s); explicit roots=['real_69c6098dd4242eda8c47c6a2:L19']
collected: real_69c6098dd4242eda8c47c6a2:L19, real_69c6098dd4242eda8c47c6a2:L20, real_69c6098dd4242eda8c47c6a2:L21, real_69c6098dd4242eda8c47c6a2:L22, real_69c6098dd4242eda8c47c6a2:L23, real_69c6098dd4242eda8c47c6a2:L24, real_69c6098dd4242eda8c47c6a2:L25, real_69c6098dd4242eda8c47c6a2:L26, real_69c6098dd4242eda8c47c6a2:L27
reason: The current scope L19 has been collected, and no further sections are visible or 
```

### Evidence text (new)

```
[E1]
[§ 【         】买卖合同]
  甲方（买受人）：
  乙方（出卖人）：
  签约地点：
  签约时间：
  买受人（以下简称甲方）：
  出卖人（以下简称乙方）：
  根据《中华人民共和国民法典》等有关法律法规之规定，遵循平等、自愿、公平、诚实信用和绿色原则，经双方协商一致，签订本合同，双方共同遵照执行。

[E2]
[§ 第三条  货物质量要求]
  3.1 质量要求及验收标准的约定：
  执行标准为： ，其他要求为： 。
  3.3 货物的质量要求应符合有关施工图纸及设计文件要求，有关图纸及设计文件作为合同附件。
  3.5 货物质量还应符合乙方承诺的质量标准。乙方报送甲方的书面资料，包括投标文件或单独的报价文件、乙方（或生产厂家）宣传资料及乙方（或生产厂家）公开宣传的内容，均构成其承诺。
  3.6 鉴于甲方对货物质量标准的了解程度不及乙方，本合同所列明的各种质量要求或技术质量标准，应执行最高标准。

[E3]
[§ 10.1  本合同的价款，按下列第（     ）方式确定：]
（1）固定总价，不可调价，如仅供应部分货物，则按以下方式结算： ；
```

### Evidence text (old)

```
[E1]
第十二条  合同授权

[E2]
第十条  合同价款的调整与确定、结算、发票及付款

[E3]
第十一条  违约责任及合同的解除

[E4]
12.1  甲方授权以下人员行使履约过程中的各项职权：
（1）     （身份证号码     联系电话     ）
职权：收货、接收乙方提交的发票和货物的技术质量证明资料；

[E5]
10.1  本合同的价款，按下列第（     ）方式确定：
（1）固定总价，不可调价，如仅供应部分货物，则按以下方式结算： ；
（2）固定单价，不可调价；

[E6]
11.1 甲方不能按照本合同约定时间支付乙方合同款项，应自应付相关款项之日起，以应付未付款为基数，按照同期中国人民银行授权全国银行间同业拆借中心公布的贷款市场报价利率（LPR）向乙方承担违约责任。甲方违约行为应承担的违约赔偿责任（含违约金或赔偿金），总额以10000（约定违约金总额不得超过合同暂定总价的1%）元为上限。

[E7]
12.2  乙方授权以下人员行使履约过程中的各项职权：
（1） （身份证号码联系电话微信号），全权负责本合同的履行，包括但不限于：签署发料单，签收甲方发出的各类
```

## latest_clean_scope_0092 (scope_collection)

**Query:** 列举《十公司 彬州市城区智慧停车建设项目完工交付复盘报告-6.29》中“亮点H3通过优化工期，地基基础及主体阶段工期提前32天的原因分析”部分的主要条目。

**Doc:** `real_69c60abfd4242eda8c47c8d9`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 243 | 215 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 5 | 4 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60abfd4242eda8c47c8d9:L38` [MISS] retrieved=False in_text=False
- `real_69c60abfd4242eda8c47c8d9:L39` [MISS] retrieved=False in_text=False
- `real_69c60abfd4242eda8c47c8d9:L40` [MISS] retrieved=False in_text=False
- `real_69c60abfd4242eda8c47c8d9:L41` [MISS] retrieved=False in_text=False
- `real_69c60abfd4242eda8c47c8d9:L42` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C15` kind=`collect` section=`real_69c60abfd4242eda8c47c8d9:L32` scope=`None` depth=`0`
- reason: Collecting H3 section and its leaf nodes detailing the 32-day schedule advance reasons.
- collect_section_ids: ['real_69c60abfd4242eda8c47c8d9:L32', 'real_69c60abfd4242eda8c47c8d9:L33', 'real_69c60abfd4242eda8c47c8d9:L34', 'real_69c60abfd4242eda8c47c8d9:L35', 'real_69c60abfd4242eda8c47c8d9:L36']
- collect added=9 hits=9 branch_selected=True collect_full=True
- legal_actions (49):
  - C1 | COLLECT | real_69c60abfd4242eda8c47c8d9:L2 | 项目完工交付复盘报告 | score=0.0621
  - D1 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L2 | 项目完工交付复盘报告 | score=0.0621
  - C2 | COLLECT | real_69c60abfd4242eda8c47c8d9:L3 | 单位/项目:彬州市城区智慧停车建设项目 | score=0.0541
  - C3 | COLLECT | real_69c60abfd4242eda8c47c8d9:L4 | 2024年6月27日，彬州市城区智慧停车建设项目完工交付复盘会在集团公司607会议室举行。会议由解博学引导，蔡伦组织，项目部主要管理人员参与，蔡伦、刘首安、李宝珺编写报告。 | score=0.0610
  - C4 | COLLECT | real_69c60abfd4242eda8c47c8d9:L5 | 一.复盘事项（或项目当下阶段）背景 | score=0.0539
  - C5 | COLLECT | real_69c60abfd4242eda8c47c8d9:L8 | 背景阐述：本项目为彬州市政府专项债，项目承包模式为EPC项目，入场时未达到“三通一平”条件。合同签订计划施工日期2022年9月20日，实际进场日期为2022年10月1日，计划完工日期为2023年9月20日，实际完工日期为2024年4月3日，合同总工期为365天。项目劳务分包、专业分包为项目部自行选择，汽车升降设备、客用电梯安装为甲指分包。但项目实际超出计划工期，现针对项目过程实施中的优缺点进行“回 | score=0.0621
  - C6 | COLLECT | real_69c60abfd4242eda8c47c8d9:L9 | 二.复盘回顾、评估 | score=0.0681
  - D2 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L9 | 二.复盘回顾、评估 | score=0.0681
  - C7 | COLLECT | real_69c60abfd4242eda8c47c8d9:L12 | 3、亮点与不足 | score=0.0681
  - D3 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L12 | 3、亮点与不足 | score=0.0681
  - C8 | COLLECT | real_69c60abfd4242eda8c47c8d9:L13 | 亮点包括资金确权回收良好、商务策划落地及主体工期提前32天。不足在于汽车升降设备分包管理失控导致延误185天，且质量过程管控效果不佳。 | score=0.0681
  - C9 | COLLECT | real_69c60abfd4242eda8c47c8d9:L15 | 三.复盘反思、分析 | score=0.0589
  - D4 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L15 | 三.复盘反思、分析 | score=0.0589
  - C10 | COLLECT | real_69c60abfd4242eda8c47c8d9:L16 | 1、亮点H1资金确权及回收情况良好的原因分析 | score=0.0589
  - C11 | COLLECT | real_69c60abfd4242eda8c47c8d9:L21 | 亮点H2项目商务策划管理实施落地，达到策划预期目标的原因分析 | score=0.0635
  - D5 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L21 | 亮点H2项目商务策划管理实施落地，达到策划预期目标的原因分析 | score=0.0635
- projection_chars: 3383

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains the complete list of main items for Highlight H3 as requested.
- legal_actions (50):
  - C1 | COLLECT | real_69c60abfd4242eda8c47c8d9:L2 | 项目完工交付复盘报告 | score=0.0621
  - D1 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L2 | 项目完工交付复盘报告 | score=0.0621
  - C2 | COLLECT | real_69c60abfd4242eda8c47c8d9:L3 | 单位/项目:彬州市城区智慧停车建设项目 | score=0.0541
  - C3 | COLLECT | real_69c60abfd4242eda8c47c8d9:L4 | 2024年6月27日，彬州市城区智慧停车建设项目完工交付复盘会在集团公司607会议室举行。会议由解博学引导，蔡伦组织，项目部主要管理人员参与，蔡伦、刘首安、李宝珺编写报告。 | score=0.0610
  - C4 | COLLECT | real_69c60abfd4242eda8c47c8d9:L5 | 一.复盘事项（或项目当下阶段）背景 | score=0.0539
  - C5 | COLLECT | real_69c60abfd4242eda8c47c8d9:L8 | 背景阐述：本项目为彬州市政府专项债，项目承包模式为EPC项目，入场时未达到“三通一平”条件。合同签订计划施工日期2022年9月20日，实际进场日期为2022年10月1日，计划完工日期为2023年9月20日，实际完工日期为2024年4月3日，合同总工期为365天。项目劳务分包、专业分包为项目部自行选择，汽车升降设备、客用电梯安装为甲指分包。但项目实际超出计划工期，现针对项目过程实施中的优缺点进行“回 | score=0.0621
  - C6 | COLLECT | real_69c60abfd4242eda8c47c8d9:L9 | 二.复盘回顾、评估 | score=0.0681
  - D2 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L9 | 二.复盘回顾、评估 | score=0.0681
  - C7 | COLLECT | real_69c60abfd4242eda8c47c8d9:L12 | 3、亮点与不足 | score=0.0681
  - D3 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L12 | 3、亮点与不足 | score=0.0681
  - C8 | COLLECT | real_69c60abfd4242eda8c47c8d9:L13 | 亮点包括资金确权回收良好、商务策划落地及主体工期提前32天。不足在于汽车升降设备分包管理失控导致延误185天，且质量过程管控效果不佳。 | score=0.0681
  - C9 | COLLECT | real_69c60abfd4242eda8c47c8d9:L15 | 三.复盘反思、分析 | score=0.0589
  - D4 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L15 | 三.复盘反思、分析 | score=0.0589
  - C10 | COLLECT | real_69c60abfd4242eda8c47c8d9:L16 | 1、亮点H1资金确权及回收情况良好的原因分析 | score=0.0589
  - C11 | COLLECT | real_69c60abfd4242eda8c47c8d9:L21 | 亮点H2项目商务策划管理实施落地，达到策划预期目标的原因分析 | score=0.0635
  - D5 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L21 | 亮点H2项目商务策划管理实施落地，达到策划预期目标的原因分析 | score=0.0635
- projection_chars: 3565

### Evidence text (new)

```
[E1]
[§ 亮点H3通过优化工期，地基基础及主体阶段工期提前32天的原因分析]
  ①场地不利因素优化:
  ①场地不利因素优化:
  现场场地狭小，为保证工期，无需加工材料直接卸货至工作面；
  现场场地狭小，为保证工期，无需加工材料直接卸货至工作面；
  除主要通道，周边其余场地利用率>85%;
  除主要通道，周边其余场地利用率>85%;
  利用周边项目加工厂进行材料代加工；
  利用周边项目加工厂进行材料代加工；
```

### Evidence text (old)

```
[E1]
亮点H3通过优化工期，地基基础及主体阶段工期提前32天的原因分析

[E2]
①场地不利因素优化:

[E3]
现场场地狭小，为保证工期，无需加工材料直接卸货至工作面；

[E4]
除主要通道，周边其余场地利用率>85%;

[E5]
利用周边项目加工厂进行材料代加工；

[E6]
①场地不利因素优化:

[E7]
现场场地狭小，为保证工期，无需加工材料直接卸货至工作面；

[E8]
利用周边项目加工厂进行材料代加工；

[E9]
除主要通道，周边其余场地利用率>85%;
```

## latest_clean_scope_0096 (scope_collection)

**Query:** 列举《十公司 彬州市城区智慧停车建设项目完工交付复盘报告-6.29》中“如果出现【变化或意外】，则应该：”部分的主要条目。

**Doc:** `real_69c60abfd4242eda8c47c8d9`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 500 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 9 | 9 |
| trajectory_steps | n/a | 7 |

### Gold node hits (new)

- `real_69c60abfd4242eda8c47c8d9:L100` [MISS] retrieved=False in_text=False
- `real_69c60abfd4242eda8c47c8d9:L101` [MISS] retrieved=False in_text=False
- `real_69c60abfd4242eda8c47c8d9:L102` [MISS] retrieved=False in_text=False
- `real_69c60abfd4242eda8c47c8d9:L103` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C29` kind=`collect` section=`real_69c60abfd4242eda8c47c8d9:L96` scope=`None` depth=`0`
- reason: Target section '如果出现【变化或意外】，则应该：' found at N29, collect to retrieve main items.
- collect_section_ids: ['real_69c60abfd4242eda8c47c8d9:L96']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (47):
  - C1 | COLLECT | real_69c60abfd4242eda8c47c8d9:L2 | 项目完工交付复盘报告 | score=0.0657
  - D1 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L2 | 项目完工交付复盘报告 | score=0.0657
  - C2 | COLLECT | real_69c60abfd4242eda8c47c8d9:L3 | 单位/项目:彬州市城区智慧停车建设项目 | score=0.0580
  - C3 | COLLECT | real_69c60abfd4242eda8c47c8d9:L4 | 2024年6月27日，彬州市城区智慧停车建设项目完工交付复盘会在集团公司607会议室举行。会议由解博学引导，蔡伦组织，项目部主要管理人员参与，蔡伦、刘首安、李宝珺编写报告。 | score=0.0657
  - C4 | COLLECT | real_69c60abfd4242eda8c47c8d9:L5 | 一.复盘事项（或项目当下阶段）背景 | score=0.0535
  - C5 | COLLECT | real_69c60abfd4242eda8c47c8d9:L8 | 背景阐述：本项目为彬州市政府专项债，项目承包模式为EPC项目，入场时未达到“三通一平”条件。合同签订计划施工日期2022年9月20日，实际进场日期为2022年10月1日，计划完工日期为2023年9月20日，实际完工日期为2024年4月3日，合同总工期为365天。项目劳务分包、专业分包为项目部自行选择，汽车升降设备、客用电梯安装为甲指分包。但项目实际超出计划工期，现针对项目过程实施中的优缺点进行“回 | score=0.0606
  - C6 | COLLECT | real_69c60abfd4242eda8c47c8d9:L15 | 三.复盘反思、分析 | score=0.0562
  - D2 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L15 | 三.复盘反思、分析 | score=0.0562
  - C7 | COLLECT | real_69c60abfd4242eda8c47c8d9:L20 | 项目施工过程中，每达到付款条件，项目及时报送进度款支付申请，对应收进度款及时催清，应收账款符合当期申请金额。 | score=0.0562
  - C8 | COLLECT | real_69c60abfd4242eda8c47c8d9:L21 | 亮点H2项目商务策划管理实施落地，达到策划预期目标的原因分析 | score=0.0546
  - D3 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L21 | 亮点H2项目商务策划管理实施落地，达到策划预期目标的原因分析 | score=0.0546
  - C9 | COLLECT | real_69c60abfd4242eda8c47c8d9:L24 | 2）现场施工大门及市政围挡使用业主收购场地遗留，符合现场施工要求，节约成本。 | score=0.0533
  - C10 | COLLECT | real_69c60abfd4242eda8c47c8d9:L25 | 3）场地内使用原场地内已硬化基础作为项目部办公室基础，未硬化部分采用烧结砖铺设作为临时硬化，该部分烧结砖后期用于室外砖井砌筑，节约成本。 | score=0.0546
  - C11 | COLLECT | real_69c60abfd4242eda8c47c8d9:L31 | 3）现场办公家具及箱式房使用之前项目剩余，使用完成后立即周转出场 | score=0.0518
  - C12 | COLLECT | real_69c60abfd4242eda8c47c8d9:L43 | 不足L1甲指分包管理失控，工期延误185天的原因分析 | score=0.0633
  - D4 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L43 | 不足L1甲指分包管理失控，工期延误185天的原因分析 | score=0.0633
- projection_chars: 3585

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60abfd4242eda8c47c8d9:L15` depth=`1`
- reason: The current scope contains only 'Highlights' and 'Capital Recovery' analysis, not the requested 'Changes or Accidents' section.
- legal_actions (7):
  - C1 | COLLECT | real_69c60abfd4242eda8c47c8d9:L15 | 三.复盘反思、分析 | score=0.0562
  - C2 | COLLECT | real_69c60abfd4242eda8c47c8d9:L16 | 1、亮点H1资金确权及回收情况良好的原因分析 | score=0.0416
  - C3 | COLLECT | real_69c60abfd4242eda8c47c8d9:L17 | ①过程确权率好 | score=0.0403
  - C4 | COLLECT | real_69c60abfd4242eda8c47c8d9:L18 | 项目施工过程按月严格确认现场已完工程量，按时报送工程形象进度确认。合同外签证及时签字确认，并计入当期甲批量内。每月过程确权率100%。 | score=0.0473
  - C5 | COLLECT | real_69c60abfd4242eda8c47c8d9:L19 | ②资金回收情况良好 | score=0.0414
  - C6 | COLLECT | real_69c60abfd4242eda8c47c8d9:L20 | 项目施工过程中，每达到付款条件，项目及时报送进度款支付申请，对应收进度款及时催清，应收账款符合当期申请金额。 | score=0.0562
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 1027

**Step 3** `nav_dispatch`  id=`D2` kind=`dispatch` section=`real_69c60abfd4242eda8c47c8d9:L15` scope=`None` depth=`0`
- reason: Dispatch to find the 'If changes or unexpected events occur' section under Reflection/Analysis.
- dispatch_regions: ['real_69c60abfd4242eda8c47c8d9:L15']
- child_reports=1 skipped=0
- legal_actions (47):
  - C1 | COLLECT | real_69c60abfd4242eda8c47c8d9:L2 | 项目完工交付复盘报告 | score=0.0657
  - D1 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L2 | 项目完工交付复盘报告 | score=0.0657
  - C2 | COLLECT | real_69c60abfd4242eda8c47c8d9:L3 | 单位/项目:彬州市城区智慧停车建设项目 | score=0.0580
  - C3 | COLLECT | real_69c60abfd4242eda8c47c8d9:L4 | 2024年6月27日，彬州市城区智慧停车建设项目完工交付复盘会在集团公司607会议室举行。会议由解博学引导，蔡伦组织，项目部主要管理人员参与，蔡伦、刘首安、李宝珺编写报告。 | score=0.0657
  - C4 | COLLECT | real_69c60abfd4242eda8c47c8d9:L5 | 一.复盘事项（或项目当下阶段）背景 | score=0.0535
  - C5 | COLLECT | real_69c60abfd4242eda8c47c8d9:L8 | 背景阐述：本项目为彬州市政府专项债，项目承包模式为EPC项目，入场时未达到“三通一平”条件。合同签订计划施工日期2022年9月20日，实际进场日期为2022年10月1日，计划完工日期为2023年9月20日，实际完工日期为2024年4月3日，合同总工期为365天。项目劳务分包、专业分包为项目部自行选择，汽车升降设备、客用电梯安装为甲指分包。但项目实际超出计划工期，现针对项目过程实施中的优缺点进行“回 | score=0.0606
  - C6 | COLLECT | real_69c60abfd4242eda8c47c8d9:L15 | 三.复盘反思、分析 | score=0.0562
  - D2 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L15 | 三.复盘反思、分析 | score=0.0562
  - C7 | COLLECT | real_69c60abfd4242eda8c47c8d9:L20 | 项目施工过程中，每达到付款条件，项目及时报送进度款支付申请，对应收进度款及时催清，应收账款符合当期申请金额。 | score=0.0562
  - C8 | COLLECT | real_69c60abfd4242eda8c47c8d9:L21 | 亮点H2项目商务策划管理实施落地，达到策划预期目标的原因分析 | score=0.0546
  - D3 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L21 | 亮点H2项目商务策划管理实施落地，达到策划预期目标的原因分析 | score=0.0546
  - C9 | COLLECT | real_69c60abfd4242eda8c47c8d9:L24 | 2）现场施工大门及市政围挡使用业主收购场地遗留，符合现场施工要求，节约成本。 | score=0.0533
  - C10 | COLLECT | real_69c60abfd4242eda8c47c8d9:L25 | 3）场地内使用原场地内已硬化基础作为项目部办公室基础，未硬化部分采用烧结砖铺设作为临时硬化，该部分烧结砖后期用于室外砖井砌筑，节约成本。 | score=0.0546
  - C11 | COLLECT | real_69c60abfd4242eda8c47c8d9:L31 | 3）现场办公家具及箱式房使用之前项目剩余，使用完成后立即周转出场 | score=0.0518
  - C12 | COLLECT | real_69c60abfd4242eda8c47c8d9:L43 | 不足L1甲指分包管理失控，工期延误185天的原因分析 | score=0.0633
  - D4 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L43 | 不足L1甲指分包管理失控，工期延误185天的原因分析 | score=0.0633
- projection_chars: 3606

**Step 4** `nav_collect`  id=`C6` kind=`collect` section=`real_69c60abfd4242eda8c47c8d9:L15` scope=`None` depth=`0`
- reason: Dispatch to D2 to explore '复盘反思、分析' section for the requested 'Changes or Accidents' items.
- collect_section_ids: ['real_69c60abfd4242eda8c47c8d9:L15']
- collect added=6 hits=6 branch_selected=True collect_full=False
- legal_actions (47):
  - C1 | COLLECT | real_69c60abfd4242eda8c47c8d9:L2 | 项目完工交付复盘报告 | score=0.0657
  - D1 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L2 | 项目完工交付复盘报告 | score=0.0657
  - C2 | COLLECT | real_69c60abfd4242eda8c47c8d9:L3 | 单位/项目:彬州市城区智慧停车建设项目 | score=0.0580
  - C3 | COLLECT | real_69c60abfd4242eda8c47c8d9:L4 | 2024年6月27日，彬州市城区智慧停车建设项目完工交付复盘会在集团公司607会议室举行。会议由解博学引导，蔡伦组织，项目部主要管理人员参与，蔡伦、刘首安、李宝珺编写报告。 | score=0.0657
  - C4 | COLLECT | real_69c60abfd4242eda8c47c8d9:L5 | 一.复盘事项（或项目当下阶段）背景 | score=0.0535
  - C5 | COLLECT | real_69c60abfd4242eda8c47c8d9:L8 | 背景阐述：本项目为彬州市政府专项债，项目承包模式为EPC项目，入场时未达到“三通一平”条件。合同签订计划施工日期2022年9月20日，实际进场日期为2022年10月1日，计划完工日期为2023年9月20日，实际完工日期为2024年4月3日，合同总工期为365天。项目劳务分包、专业分包为项目部自行选择，汽车升降设备、客用电梯安装为甲指分包。但项目实际超出计划工期，现针对项目过程实施中的优缺点进行“回 | score=0.0606
  - C6 | COLLECT | real_69c60abfd4242eda8c47c8d9:L15 | 三.复盘反思、分析 | score=0.0562
  - D2 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L15 | 三.复盘反思、分析 | score=0.0562
  - C7 | COLLECT | real_69c60abfd4242eda8c47c8d9:L20 | 项目施工过程中，每达到付款条件，项目及时报送进度款支付申请，对应收进度款及时催清，应收账款符合当期申请金额。 | score=0.0562
  - C8 | COLLECT | real_69c60abfd4242eda8c47c8d9:L21 | 亮点H2项目商务策划管理实施落地，达到策划预期目标的原因分析 | score=0.0546
  - D3 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L21 | 亮点H2项目商务策划管理实施落地，达到策划预期目标的原因分析 | score=0.0546
  - C9 | COLLECT | real_69c60abfd4242eda8c47c8d9:L24 | 2）现场施工大门及市政围挡使用业主收购场地遗留，符合现场施工要求，节约成本。 | score=0.0533
  - C10 | COLLECT | real_69c60abfd4242eda8c47c8d9:L25 | 3）场地内使用原场地内已硬化基础作为项目部办公室基础，未硬化部分采用烧结砖铺设作为临时硬化，该部分烧结砖后期用于室外砖井砌筑，节约成本。 | score=0.0546
  - C11 | COLLECT | real_69c60abfd4242eda8c47c8d9:L31 | 3）现场办公家具及箱式房使用之前项目剩余，使用完成后立即周转出场 | score=0.0518
  - C12 | COLLECT | real_69c60abfd4242eda8c47c8d9:L43 | 不足L1甲指分包管理失控，工期延误185天的原因分析 | score=0.0633
  - D4 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L43 | 不足L1甲指分包管理失控，工期延误185天的原因分析 | score=0.0633
- projection_chars: 3606

**Step 5** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60abfd4242eda8c47c8d9:L2` scope=`None` depth=`0`
- reason: Need to collect the full 'Changes or Accidents' section (N17) to find the specific items requested.
- collect_section_ids: ['real_69c60abfd4242eda8c47c8d9:L2']
- collect added=7 hits=7 branch_selected=True collect_full=False
- legal_actions (45):
  - C1 | COLLECT | real_69c60abfd4242eda8c47c8d9:L2 | 项目完工交付复盘报告 | score=0.0657
  - D1 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L2 | 项目完工交付复盘报告 | score=0.0657
  - C2 | COLLECT | real_69c60abfd4242eda8c47c8d9:L3 | 单位/项目:彬州市城区智慧停车建设项目 | score=0.0580
  - C3 | COLLECT | real_69c60abfd4242eda8c47c8d9:L4 | 2024年6月27日，彬州市城区智慧停车建设项目完工交付复盘会在集团公司607会议室举行。会议由解博学引导，蔡伦组织，项目部主要管理人员参与，蔡伦、刘首安、李宝珺编写报告。 | score=0.0657
  - C4 | COLLECT | real_69c60abfd4242eda8c47c8d9:L5 | 一.复盘事项（或项目当下阶段）背景 | score=0.0535
  - C5 | COLLECT | real_69c60abfd4242eda8c47c8d9:L8 | 背景阐述：本项目为彬州市政府专项债，项目承包模式为EPC项目，入场时未达到“三通一平”条件。合同签订计划施工日期2022年9月20日，实际进场日期为2022年10月1日，计划完工日期为2023年9月20日，实际完工日期为2024年4月3日，合同总工期为365天。项目劳务分包、专业分包为项目部自行选择，汽车升降设备、客用电梯安装为甲指分包。但项目实际超出计划工期，现针对项目过程实施中的优缺点进行“回 | score=0.0606
  - C6 | COLLECT | real_69c60abfd4242eda8c47c8d9:L21 | 亮点H2项目商务策划管理实施落地，达到策划预期目标的原因分析 | score=0.0546
  - D2 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L21 | 亮点H2项目商务策划管理实施落地，达到策划预期目标的原因分析 | score=0.0546
  - C7 | COLLECT | real_69c60abfd4242eda8c47c8d9:L24 | 2）现场施工大门及市政围挡使用业主收购场地遗留，符合现场施工要求，节约成本。 | score=0.0533
  - C8 | COLLECT | real_69c60abfd4242eda8c47c8d9:L25 | 3）场地内使用原场地内已硬化基础作为项目部办公室基础，未硬化部分采用烧结砖铺设作为临时硬化，该部分烧结砖后期用于室外砖井砌筑，节约成本。 | score=0.0546
  - C9 | COLLECT | real_69c60abfd4242eda8c47c8d9:L31 | 3）现场办公家具及箱式房使用之前项目剩余，使用完成后立即周转出场 | score=0.0518
  - C10 | COLLECT | real_69c60abfd4242eda8c47c8d9:L43 | 不足L1甲指分包管理失控，工期延误185天的原因分析 | score=0.0633
  - D3 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L43 | 不足L1甲指分包管理失控，工期延误185天的原因分析 | score=0.0633
  - C11 | COLLECT | real_69c60abfd4242eda8c47c8d9:L45 | 1）汽车升降设备分包: | score=0.0633
  - D4 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L45 | 1）汽车升降设备分包: | score=0.0633
  - C12 | COLLECT | real_69c60abfd4242eda8c47c8d9:L47 | 2、汽车升降设备分包单位深化图未考虑汽车转运平台与停车区高度问题，采用人工破除我方已施工面层，严重影响后续工艺施工。 | score=0.0514
- projection_chars: 3561

**Step 6** `nav_collect`  id=`C15` kind=`collect` section=`real_69c60abfd4242eda8c47c8d9:L55` scope=`None` depth=`0`
- reason: The user query specifically asks for the 'Changes or Accidents' section, which corresponds to node N15 (C15). The previous dispatch to L15 was incorrect as it only contained highlights.
- collect_section_ids: ['real_69c60abfd4242eda8c47c8d9:L55']
- collect added=9 hits=9 branch_selected=True collect_full=False
- legal_actions (47):
  - C1 | COLLECT | real_69c60abfd4242eda8c47c8d9:L21 | 亮点H2项目商务策划管理实施落地，达到策划预期目标的原因分析 | score=0.0546
  - D1 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L21 | 亮点H2项目商务策划管理实施落地，达到策划预期目标的原因分析 | score=0.0546
  - C2 | COLLECT | real_69c60abfd4242eda8c47c8d9:L24 | 2）现场施工大门及市政围挡使用业主收购场地遗留，符合现场施工要求，节约成本。 | score=0.0533
  - C3 | COLLECT | real_69c60abfd4242eda8c47c8d9:L25 | 3）场地内使用原场地内已硬化基础作为项目部办公室基础，未硬化部分采用烧结砖铺设作为临时硬化，该部分烧结砖后期用于室外砖井砌筑，节约成本。 | score=0.0546
  - C4 | COLLECT | real_69c60abfd4242eda8c47c8d9:L31 | 3）现场办公家具及箱式房使用之前项目剩余，使用完成后立即周转出场 | score=0.0518
  - C5 | COLLECT | real_69c60abfd4242eda8c47c8d9:L32 | 亮点H3通过优化工期，地基基础及主体阶段工期提前32天的原因分析 | score=0.0503
  - D2 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L32 | 亮点H3通过优化工期，地基基础及主体阶段工期提前32天的原因分析 | score=0.0503
  - C6 | COLLECT | real_69c60abfd4242eda8c47c8d9:L35 | 除主要通道，周边其余场地利用率>85%; | score=0.0503
  - C7 | COLLECT | real_69c60abfd4242eda8c47c8d9:L43 | 不足L1甲指分包管理失控，工期延误185天的原因分析 | score=0.0633
  - D3 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L43 | 不足L1甲指分包管理失控，工期延误185天的原因分析 | score=0.0633
  - C8 | COLLECT | real_69c60abfd4242eda8c47c8d9:L45 | 1）汽车升降设备分包: | score=0.0633
  - D4 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L45 | 1）汽车升降设备分包: | score=0.0633
  - C9 | COLLECT | real_69c60abfd4242eda8c47c8d9:L47 | 2、汽车升降设备分包单位深化图未考虑汽车转运平台与停车区高度问题，采用人工破除我方已施工面层，严重影响后续工艺施工。 | score=0.0514
  - C10 | COLLECT | real_69c60abfd4242eda8c47c8d9:L48 | 3、汽车升降设备分包单位接受业主委托后，设备未能及时进场，影响我方室外工程施工。 | score=0.0519
  - C11 | COLLECT | real_69c60abfd4242eda8c47c8d9:L50 | 5、汽车升降在停车区设置停车平台，深化图纸中未体现该部分做法。因我方已基本完成施工内容，且该部分未计入预算清单，平台部分由汽车升降设备安装单位自行施工。施工过程中该单位多次停工，因该事项未完成，业主拒绝接收，故影响交付时间。 | score=0.0633
  - C12 | COLLECT | real_69c60abfd4242eda8c47c8d9:L52 | 3）热力管网：入场时，业主未提供周边地下管线相关资料，现场原有基础破除过程中，主楼基坑部位发现两根热力管网，对热力管网完成改线后，进行桩基工程施工 | score=0.0501
- projection_chars: 3588

**Step 7** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains the specific section '如果出现【变化或意外】，则应该：' with its main item regarding process confirmation adjustments.
- legal_actions (46):
  - C1 | COLLECT | real_69c60abfd4242eda8c47c8d9:L21 | 亮点H2项目商务策划管理实施落地，达到策划预期目标的原因分析 | score=0.0546
  - D1 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L21 | 亮点H2项目商务策划管理实施落地，达到策划预期目标的原因分析 | score=0.0546
  - C2 | COLLECT | real_69c60abfd4242eda8c47c8d9:L23 | 1）临建设施使用业主收购场地遗留部分临建，包括卫生间一间、K式房12间用做项目库房、劳务办公室等功能用房，节约成本。 | score=0.0487
  - C3 | COLLECT | real_69c60abfd4242eda8c47c8d9:L24 | 2）现场施工大门及市政围挡使用业主收购场地遗留，符合现场施工要求，节约成本。 | score=0.0533
  - C4 | COLLECT | real_69c60abfd4242eda8c47c8d9:L25 | 3）场地内使用原场地内已硬化基础作为项目部办公室基础，未硬化部分采用烧结砖铺设作为临时硬化，该部分烧结砖后期用于室外砖井砌筑，节约成本。 | score=0.0546
  - C5 | COLLECT | real_69c60abfd4242eda8c47c8d9:L30 | 2）现场钢筋棚周转周边项目，使用完成后立即周转出场。 | score=0.0491
  - C6 | COLLECT | real_69c60abfd4242eda8c47c8d9:L31 | 3）现场办公家具及箱式房使用之前项目剩余，使用完成后立即周转出场 | score=0.0518
  - C7 | COLLECT | real_69c60abfd4242eda8c47c8d9:L32 | 亮点H3通过优化工期，地基基础及主体阶段工期提前32天的原因分析 | score=0.0503
  - D2 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L32 | 亮点H3通过优化工期，地基基础及主体阶段工期提前32天的原因分析 | score=0.0503
  - C8 | COLLECT | real_69c60abfd4242eda8c47c8d9:L33 | ①场地不利因素优化: | score=0.0490
  - C9 | COLLECT | real_69c60abfd4242eda8c47c8d9:L35 | 除主要通道，周边其余场地利用率>85%; | score=0.0503
  - C10 | COLLECT | real_69c60abfd4242eda8c47c8d9:L43 | 不足L1甲指分包管理失控，工期延误185天的原因分析 | score=0.0633
  - D3 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L43 | 不足L1甲指分包管理失控，工期延误185天的原因分析 | score=0.0633
  - C11 | COLLECT | real_69c60abfd4242eda8c47c8d9:L45 | 1）汽车升降设备分包: | score=0.0633
  - D4 | DISPATCH | real_69c60abfd4242eda8c47c8d9:L45 | 1）汽车升降设备分包: | score=0.0633
  - C12 | COLLECT | real_69c60abfd4242eda8c47c8d9:L46 | 1、项目性质为EPC项目，汽车升降设备单位应由我方选择。因价格问题，业主方直接选择供应商。业主方确认供应商周期过长，影响施工进度。 | score=0.0482
- projection_chars: 3419

### Subagent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60abfd4242eda8c47c8d9:L15 (ok)
The current scope contains only 'Highlights' and 'Capital Recovery' analysis, not the requested 'Changes or Accidents' section.
reason: The current scope contains only 'Highlights' and 'Capital Recovery' analysis, not the requested 'Changes or Accidents' section.
---
=== End Investigate ===
```

### Evidence text (new)

```
[E1]
[§ 如果出现【变化或意外】，则应该：]
面对市场需求变化和原材料价格波动等意外情况，需及时调整过程确权工作，以确保数据的准确性和时效性。

[E2]
[§ 项目完工交付复盘报告]
  单位/项目:彬州市城区智慧停车建设项目
  2024年6月27日，彬州市城区智慧停车建设项目完工交付复盘会在集团公司607会议室举行。会议由解博学引导，蔡伦组织，项目部主要管理人员参与，蔡伦、刘首安、李宝珺编写报告。
  一.复盘事项（或项目当下阶段）背景
  背景阐述：本项目为彬州市政府专项债，项目承包模式为EPC项目，入场时未达到“三通一平”条件。合同签订计划施工日期2022年9月20日，实际进场日期为2022年10月1日，计划完工日期为2023年9月20日，实际完工日期为2024年4月3日，合同总工期为365天。项目劳务分包、专业分包为项目部自行选择，汽车升降设备、客用电梯安装为甲指分包。但项目实际超出计划工期，现针对项目过程实施中的优缺点进行“回头看”。

[E3]
[§ 三.复盘反思、分析]
  1、亮点H1资金确权及回收情况良好的原因分析
  ①过程确权率好
  ②资金回收情况良好
```

### Evidence text (old)

```
[E1]
[§ 如果出现【变化或意外】，则应该：]
面对市场需求变化和原材料价格波动等意外情况，需及时调整过程确权工作，以确保数据的准确性和时效性。

[E2]
[§ 项目完工交付复盘报告]
单位/项目:彬州市城区智慧停车建设项目

[E3]
[§ 复盘分析单]
时间：2024年6月27日地点：集团公司607室事项：彬州市城区智慧停车建设项目完工交付复盘参加人：解博学、贺磊、蔡伦、刘首安、李宝珺

[E4]
[§ 项目复盘策划单]
2024年6月27日，解博学等人在集团公司召开彬州市城区智慧停车建设项目完工交付复盘会。会议历时8小时，通过鱼骨图、头脑风暴等方法，深入分析项目过程优缺点及成因，旨在总结经验教训，为后续项目提供参考。

[E5]
[§ 项目完工交付复盘报告]
2024年6月27日，彬州市城区智慧停车建设项目完工交付复盘会在集团公司607会议室举行。会议由解博学引导，蔡伦组织，项目部主要管理人员参与，蔡伦、刘首安、李宝珺编写报告。

[E6]
[§ 项目完工交付复盘报告]
本项目彬州市智慧停车建设项目，位于彬州市实验小学以北老消防队，处于北大街与创新西路交汇处.基地东西长约3
```

## latest_clean_scope_0097 (scope_collection)

**Query:** 列举《安徽一 医防完工复盘报告6.13》中“7、不足L3（材料损耗过大）的原因分析”部分的主要条目。

**Doc:** `real_69c60abfd4242eda8c47c8da`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 486 | 445 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 5 | 9 |
| trajectory_steps | n/a | 4 |

### Gold node hits (new)

- `real_69c60abfd4242eda8c47c8da:L49` [MISS] retrieved=False in_text=False
- `real_69c60abfd4242eda8c47c8da:L50` [MISS] retrieved=False in_text=False
- `real_69c60abfd4242eda8c47c8da:L59` [MISS] retrieved=False in_text=False
- `real_69c60abfd4242eda8c47c8da:L61` [MISS] retrieved=False in_text=False
- `real_69c60abfd4242eda8c47c8da:L62` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C20` kind=`collect` section=`real_69c60abfd4242eda8c47c8da:L20` scope=`None` depth=`0`
- reason: Collect section 7 to retrieve the main items regarding material loss causes.
- collect_section_ids: ['real_69c60abfd4242eda8c47c8da:L20']
- collect added=5 hits=5 branch_selected=True collect_full=False
- legal_actions (47):
  - C1 | COLLECT | real_69c60abfd4242eda8c47c8da:L1 | 1、目标回顾 | score=0.0560
  - D1 | DISPATCH | real_69c60abfd4242eda8c47c8da:L1 | 1、目标回顾 | score=0.0560
  - C2 | COLLECT | real_69c60abfd4242eda8c47c8da:L2 | 项目利润目标完成，超额收益36.40万元；工期严重滞后，超期427天；质量和安全文明施工目标均完成，并创建市标准化工地。 | score=0.0560
  - C3 | COLLECT | real_69c60abfd4242eda8c47c8da:L3 | 实际过程 | score=0.0525
  - C4 | COLLECT | real_69c60abfd4242eda8c47c8da:L4 | 3、亮点与不足 | score=0.0675
  - D2 | DISPATCH | real_69c60abfd4242eda8c47c8da:L4 | 3、亮点与不足 | score=0.0675
  - C5 | COLLECT | real_69c60abfd4242eda8c47c8da:L5 | 项目通过清单核对及设计优化实现净增收入524.2万元，并获安全质量双标化工地。但工期严重超期427天，导致间接费、机械费等增加273万元；木工班组及材料损耗管理不善，分别超目标成本33.3万和46万元。 | score=0.0675
  - C6 | COLLECT | real_69c60abfd4242eda8c47c8da:L6 | 三.复盘反思、分析 | score=0.0660
  - C7 | COLLECT | real_69c60abfd4242eda8c47c8da:L7 | 1、亮点H1（清单核对、增加收入）的原因分析 | score=0.0638
  - C8 | COLLECT | real_69c60abfd4242eda8c47c8da:L8 | 2、亮点H2（设计及技术策划增加收入）的原因分析 | score=0.0681
  - D3 | DISPATCH | real_69c60abfd4242eda8c47c8da:L8 | 2、亮点H2（设计及技术策划增加收入）的原因分析 | score=0.0681
  - C9 | COLLECT | real_69c60abfd4242eda8c47c8da:L9 | 内容分析了项目变更的客观与主观原因。客观上需建立信任；主观上针对亏损项目集中策划并寻找需求促成变更，同时参考医疗项目经验重点策划变更与答疑。 | score=0.0681
  - C10 | COLLECT | real_69c60abfd4242eda8c47c8da:L10 | 3、亮点H2（质量目标：工程质量验收合格）的原因分析 | score=0.0610
  - D4 | DISPATCH | real_69c60abfd4242eda8c47c8da:L10 | 3、亮点H2（质量目标：工程质量验收合格）的原因分析 | score=0.0610
  - C11 | COLLECT | real_69c60abfd4242eda8c47c8da:L11 | 内容阐述了四项工程质量管控措施：提前制定策划、材料进场举牌验收、实行样板先行制度以及落实三检与隐蔽工程联合验收，旨在提升施工工艺质量。 | score=0.0610
  - C12 | COLLECT | real_69c60abfd4242eda8c47c8da:L12 | 4、亮点H2（安全文明施工目标：杜绝重伤以上生产安全事故）的原因分析 | score=0.0582
- projection_chars: 3414

**Step 2** `nav_collect`  id=`C14` kind=`collect` section=`real_69c60abfd4242eda8c47c8da:L14` scope=`None` depth=`0`
- reason: Collect section 7 (L3 material loss) to retrieve the required cause analysis items.
- collect_section_ids: ['real_69c60abfd4242eda8c47c8da:L14']
- collect added=4 hits=4 branch_selected=True collect_full=False
- legal_actions (48):
  - C1 | COLLECT | real_69c60abfd4242eda8c47c8da:L1 | 1、目标回顾 | score=0.0560
  - D1 | DISPATCH | real_69c60abfd4242eda8c47c8da:L1 | 1、目标回顾 | score=0.0560
  - C2 | COLLECT | real_69c60abfd4242eda8c47c8da:L2 | 项目利润目标完成，超额收益36.40万元；工期严重滞后，超期427天；质量和安全文明施工目标均完成，并创建市标准化工地。 | score=0.0560
  - C3 | COLLECT | real_69c60abfd4242eda8c47c8da:L3 | 实际过程 | score=0.0525
  - C4 | COLLECT | real_69c60abfd4242eda8c47c8da:L4 | 3、亮点与不足 | score=0.0675
  - D2 | DISPATCH | real_69c60abfd4242eda8c47c8da:L4 | 3、亮点与不足 | score=0.0675
  - C5 | COLLECT | real_69c60abfd4242eda8c47c8da:L5 | 项目通过清单核对及设计优化实现净增收入524.2万元，并获安全质量双标化工地。但工期严重超期427天，导致间接费、机械费等增加273万元；木工班组及材料损耗管理不善，分别超目标成本33.3万和46万元。 | score=0.0675
  - C6 | COLLECT | real_69c60abfd4242eda8c47c8da:L6 | 三.复盘反思、分析 | score=0.0660
  - C7 | COLLECT | real_69c60abfd4242eda8c47c8da:L7 | 1、亮点H1（清单核对、增加收入）的原因分析 | score=0.0638
  - C8 | COLLECT | real_69c60abfd4242eda8c47c8da:L8 | 2、亮点H2（设计及技术策划增加收入）的原因分析 | score=0.0681
  - D3 | DISPATCH | real_69c60abfd4242eda8c47c8da:L8 | 2、亮点H2（设计及技术策划增加收入）的原因分析 | score=0.0681
  - C9 | COLLECT | real_69c60abfd4242eda8c47c8da:L9 | 内容分析了项目变更的客观与主观原因。客观上需建立信任；主观上针对亏损项目集中策划并寻找需求促成变更，同时参考医疗项目经验重点策划变更与答疑。 | score=0.0681
  - C10 | COLLECT | real_69c60abfd4242eda8c47c8da:L10 | 3、亮点H2（质量目标：工程质量验收合格）的原因分析 | score=0.0610
  - D4 | DISPATCH | real_69c60abfd4242eda8c47c8da:L10 | 3、亮点H2（质量目标：工程质量验收合格）的原因分析 | score=0.0610
  - C11 | COLLECT | real_69c60abfd4242eda8c47c8da:L11 | 内容阐述了四项工程质量管控措施：提前制定策划、材料进场举牌验收、实行样板先行制度以及落实三检与隐蔽工程联合验收，旨在提升施工工艺质量。 | score=0.0610
  - C12 | COLLECT | real_69c60abfd4242eda8c47c8da:L12 | 4、亮点H2（安全文明施工目标：杜绝重伤以上生产安全事故）的原因分析 | score=0.0582
- projection_chars: 3400

**Step 3** `nav_collect`  id=`C14` kind=`collect` section=`real_69c60abfd4242eda8c47c8da:L18` scope=`None` depth=`0`
- reason: Dispatch D6 to retrieve the full content of section 7 regarding material loss causes.
- collect_section_ids: ['real_69c60abfd4242eda8c47c8da:L18']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (47):
  - C1 | COLLECT | real_69c60abfd4242eda8c47c8da:L1 | 1、目标回顾 | score=0.0560
  - D1 | DISPATCH | real_69c60abfd4242eda8c47c8da:L1 | 1、目标回顾 | score=0.0560
  - C2 | COLLECT | real_69c60abfd4242eda8c47c8da:L2 | 项目利润目标完成，超额收益36.40万元；工期严重滞后，超期427天；质量和安全文明施工目标均完成，并创建市标准化工地。 | score=0.0560
  - C3 | COLLECT | real_69c60abfd4242eda8c47c8da:L3 | 实际过程 | score=0.0525
  - C4 | COLLECT | real_69c60abfd4242eda8c47c8da:L4 | 3、亮点与不足 | score=0.0675
  - D2 | DISPATCH | real_69c60abfd4242eda8c47c8da:L4 | 3、亮点与不足 | score=0.0675
  - C5 | COLLECT | real_69c60abfd4242eda8c47c8da:L5 | 项目通过清单核对及设计优化实现净增收入524.2万元，并获安全质量双标化工地。但工期严重超期427天，导致间接费、机械费等增加273万元；木工班组及材料损耗管理不善，分别超目标成本33.3万和46万元。 | score=0.0675
  - C6 | COLLECT | real_69c60abfd4242eda8c47c8da:L6 | 三.复盘反思、分析 | score=0.0660
  - C7 | COLLECT | real_69c60abfd4242eda8c47c8da:L7 | 1、亮点H1（清单核对、增加收入）的原因分析 | score=0.0638
  - C8 | COLLECT | real_69c60abfd4242eda8c47c8da:L8 | 2、亮点H2（设计及技术策划增加收入）的原因分析 | score=0.0681
  - D3 | DISPATCH | real_69c60abfd4242eda8c47c8da:L8 | 2、亮点H2（设计及技术策划增加收入）的原因分析 | score=0.0681
  - C9 | COLLECT | real_69c60abfd4242eda8c47c8da:L9 | 内容分析了项目变更的客观与主观原因。客观上需建立信任；主观上针对亏损项目集中策划并寻找需求促成变更，同时参考医疗项目经验重点策划变更与答疑。 | score=0.0681
  - C10 | COLLECT | real_69c60abfd4242eda8c47c8da:L10 | 3、亮点H2（质量目标：工程质量验收合格）的原因分析 | score=0.0610
  - D4 | DISPATCH | real_69c60abfd4242eda8c47c8da:L10 | 3、亮点H2（质量目标：工程质量验收合格）的原因分析 | score=0.0610
  - C11 | COLLECT | real_69c60abfd4242eda8c47c8da:L11 | 内容阐述了四项工程质量管控措施：提前制定策划、材料进场举牌验收、实行样板先行制度以及落实三检与隐蔽工程联合验收，旨在提升施工工艺质量。 | score=0.0610
  - C12 | COLLECT | real_69c60abfd4242eda8c47c8da:L12 | 4、亮点H2（安全文明施工目标：杜绝重伤以上生产安全事故）的原因分析 | score=0.0582
- projection_chars: 3316

**Step 4** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains the specific section §7 regarding material loss causes as requested.
- legal_actions (47):
  - C1 | COLLECT | real_69c60abfd4242eda8c47c8da:L1 | 1、目标回顾 | score=0.0560
  - D1 | DISPATCH | real_69c60abfd4242eda8c47c8da:L1 | 1、目标回顾 | score=0.0560
  - C2 | COLLECT | real_69c60abfd4242eda8c47c8da:L2 | 项目利润目标完成，超额收益36.40万元；工期严重滞后，超期427天；质量和安全文明施工目标均完成，并创建市标准化工地。 | score=0.0560
  - C3 | COLLECT | real_69c60abfd4242eda8c47c8da:L3 | 实际过程 | score=0.0525
  - C4 | COLLECT | real_69c60abfd4242eda8c47c8da:L4 | 3、亮点与不足 | score=0.0675
  - D2 | DISPATCH | real_69c60abfd4242eda8c47c8da:L4 | 3、亮点与不足 | score=0.0675
  - C5 | COLLECT | real_69c60abfd4242eda8c47c8da:L5 | 项目通过清单核对及设计优化实现净增收入524.2万元，并获安全质量双标化工地。但工期严重超期427天，导致间接费、机械费等增加273万元；木工班组及材料损耗管理不善，分别超目标成本33.3万和46万元。 | score=0.0675
  - C6 | COLLECT | real_69c60abfd4242eda8c47c8da:L6 | 三.复盘反思、分析 | score=0.0660
  - C7 | COLLECT | real_69c60abfd4242eda8c47c8da:L7 | 1、亮点H1（清单核对、增加收入）的原因分析 | score=0.0638
  - C8 | COLLECT | real_69c60abfd4242eda8c47c8da:L8 | 2、亮点H2（设计及技术策划增加收入）的原因分析 | score=0.0681
  - D3 | DISPATCH | real_69c60abfd4242eda8c47c8da:L8 | 2、亮点H2（设计及技术策划增加收入）的原因分析 | score=0.0681
  - C9 | COLLECT | real_69c60abfd4242eda8c47c8da:L9 | 内容分析了项目变更的客观与主观原因。客观上需建立信任；主观上针对亏损项目集中策划并寻找需求促成变更，同时参考医疗项目经验重点策划变更与答疑。 | score=0.0681
  - C10 | COLLECT | real_69c60abfd4242eda8c47c8da:L10 | 3、亮点H2（质量目标：工程质量验收合格）的原因分析 | score=0.0610
  - D4 | DISPATCH | real_69c60abfd4242eda8c47c8da:L10 | 3、亮点H2（质量目标：工程质量验收合格）的原因分析 | score=0.0610
  - C11 | COLLECT | real_69c60abfd4242eda8c47c8da:L11 | 内容阐述了四项工程质量管控措施：提前制定策划、材料进场举牌验收、实行样板先行制度以及落实三检与隐蔽工程联合验收，旨在提升施工工艺质量。 | score=0.0610
  - C12 | COLLECT | real_69c60abfd4242eda8c47c8da:L12 | 4、亮点H2（安全文明施工目标：杜绝重伤以上生产安全事故）的原因分析 | score=0.0582
- projection_chars: 3291

### Evidence text (new)

```
[E1]
[§ 7、不足L3（材料损耗过大）的原因分析]
  分析指出因现场管理不到位导致木工、钢管及抹灰砂浆等材料严重浪费和损耗，分别造成18万、14万及14万的超目标成本损失。
  四.复盘萃取、提炼
  文章总结了项目管理的四大核心经验：加强工程量清单核对、通过商务与技术策划创效、强化安全与质量管理，并详细阐述了工期管控、分包班组及材料管理的具体措施与教训。
  五.复盘转化、应用

[E2]
[§ 5、不足L1（工期滞后）的原因分析]
  客观原因
  主观原因
  本文分析了导致工期滞后的三大核心问题：一是业主方分包单位进场慢、配合差及我方计划缺乏弹性；二是劳务班组和材料资源选择不当，导致施工延误；三是业主资金链断裂影响工程款支付，进而阻碍项目生产。

[E3]
[§ 6、不足L2（木工班组管理不善）的原因分析]
项目亏损主因：一是招标前未做市场调研，定标过度参考最低价且忽视班组实力；二是过程管理重进度轻成本，清退及零星用工费用高，导致最终造价超原合同174.3万元。
```

### Evidence text (old)

```
[E1]
7、不足L3（材料损耗过大）的原因分析

[E2]
分析指出因现场管理不到位导致木工、钢管及抹灰砂浆等材料严重浪费和损耗，分别造成18万、14万及14万的超目标成本损失。

[E3]
四.复盘萃取、提炼

[E4]
文章总结了项目管理的四大核心经验：加强工程量清单核对、通过商务与技术策划创效、强化安全与质量管理，并详细阐述了工期管控、分包班组及材料管理的具体措施与教训。

[E5]
五.复盘转化、应用

[E6]
[§ 7、不足L3（材料损耗过大）的原因分析]
五.复盘转化、应用

[E7]
[§ 7、不足L3（材料损耗过大）的原因分析]
四.复盘萃取、提炼

[E8]
[§ 7、不足L3（材料损耗过大）的原因分析]
分析指出因现场管理不到位导致木工、钢管及抹灰砂浆等材料严重浪费和损耗，分别造成18万、14万及14万的超目标成本损失。

[E9]
[§ 7、不足L3（材料损耗过大）的原因分析]
文章总结了项目管理的四大核心经验：加强工程量清单核对、通过商务与技术策划创效、强化安全与质量管理，并详细阐述了工期管控、分包班组及材料管理的具体措施与教训。
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
| trajectory_steps | n/a | 3 |

### Gold node hits (new)

- `real_69c60aeed4242eda8c47c925:L114` [MISS] retrieved=False in_text=False
- `real_69c60aeed4242eda8c47c925:L115` [MISS] retrieved=False in_text=False
- `real_69c60aeed4242eda8c47c925:L116` [MISS] retrieved=False in_text=False
- `real_69c60aeed4242eda8c47c925:L117` [MISS] retrieved=False in_text=False
- `real_69c60aeed4242eda8c47c925:L118` [MISS] retrieved=False in_text=False
- `real_69c60aeed4242eda8c47c925:L119` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C4` kind=`collect` section=`real_69c60aeed4242eda8c47c925:L110` scope=`None` depth=`0`
- reason: Collect section N4 'Levels And Setting Out Of The Works' to retrieve its main items.
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
- reason: Target section 'Levels And Setting Out Of The Works' is a leaf node C10, directly relevant to the query.
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

**Step 3** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Assembled evidence G1 and G2 cover the 'Levels And Setting Out Of The Works' section with relevant items.
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

### Evidence text (new)

```
[E1]
[§ Levels And Setting Out Of The Works水平和设置]
Setting out设置

[E2]
[§ 3.0	Contract  Documents,Programme  And]
Levels And Setting Out Of The Works--工程的测量与放样
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

## latest_clean_scope_0102 (scope_collection)

**Query:** 列举《马来西亚合同样本 2006 版 翻译件- Malaysia-PAM-合同翻译稿（4.23二译）》中“Site Agent现场代理”部分的主要条目。

**Doc:** `real_69c60aeed4242eda8c47c925`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 499 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 19 | 3 |
| trajectory_steps | n/a | 3 |

### Gold node hits (new)

- `real_69c60aeed4242eda8c47c925:L125` [MISS] retrieved=False in_text=False
- `real_69c60aeed4242eda8c47c925:L126` [MISS] retrieved=False in_text=False
- `real_69c60aeed4242eda8c47c925:L127` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60aeed4242eda8c47c925:L123` scope=`None` depth=`0`
- reason: Collect the 'Site Agent' section to retrieve its main items as requested.
- collect_section_ids: ['real_69c60aeed4242eda8c47c925:L123']
- collect added=5 hits=5 branch_selected=True collect_full=False
- legal_actions (46):
  - C1 | COLLECT | real_69c60aeed4242eda8c47c925:L123 | Site Agent现场代理 | score=0.0710
  - D1 | DISPATCH | real_69c60aeed4242eda8c47c925:L123 | Site Agent现场代理 | score=0.0710
  - C2 | COLLECT | real_69c60aeed4242eda8c47c925:L124 | Site Agent现场代理 | score=0.0662
  - C3 | COLLECT | real_69c60aeed4242eda8c47c925:L125 | Instructions to Site Agent对现场代理的说明 | score=0.0710
  - C4 | COLLECT | real_69c60aeed4242eda8c47c925:L128 | Site Staff现场工作人员 | score=0.0448
  - D2 | DISPATCH | real_69c60aeed4242eda8c47c925:L128 | Site Staff现场工作人员 | score=0.0448
  - C5 | COLLECT | real_69c60aeed4242eda8c47c925:L129 | Duty of Site Staff现场工作人员职责 | score=0.0448
  - C6 | COLLECT | real_69c60aeed4242eda8c47c925:L130 | Directions given by Site Staff现场工作人员给出的指示 | score=0.0442
  - C7 | COLLECT | real_69c60aeed4242eda8c47c925:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0658
  - D3 | DISPATCH | real_69c60aeed4242eda8c47c925:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0658
  - C8 | COLLECT | real_69c60aeed4242eda8c47c925:L390 | Article 3 | score=0.0658
  - D4 | DISPATCH | real_69c60aeed4242eda8c47c925:L390 | Article 3 | score=0.0658
  - C9 | COLLECT | real_69c60aeed4242eda8c47c925:L487 | (z) | score=0.0583
  - D5 | DISPATCH | real_69c60aeed4242eda8c47c925:L487 | (z) | score=0.0583
  - C10 | COLLECT | real_69c60aeed4242eda8c47c925:L488 | (z) part 1 | score=0.0418
  - D6 | DISPATCH | real_69c60aeed4242eda8c47c925:L488 | (z) part 1 | score=0.0418
- projection_chars: 3600

**Step 2** `nav_collect`  id=`C13` kind=`collect` section=`real_69c60aeed4242eda8c47c925:L828` scope=`None` depth=`0`
- reason: Collect the full 'Site Agent' section (N13) to retrieve all main items as requested.
- collect_section_ids: ['real_69c60aeed4242eda8c47c925:L828']
- collect added=15 hits=15 branch_selected=True collect_full=False
- legal_actions (45):
  - C1 | COLLECT | real_69c60aeed4242eda8c47c925:L128 | Site Staff现场工作人员 | score=0.0448
  - D1 | DISPATCH | real_69c60aeed4242eda8c47c925:L128 | Site Staff现场工作人员 | score=0.0448
  - C2 | COLLECT | real_69c60aeed4242eda8c47c925:L129 | Duty of Site Staff现场工作人员职责 | score=0.0448
  - C3 | COLLECT | real_69c60aeed4242eda8c47c925:L130 | Directions given by Site Staff现场工作人员给出的指示 | score=0.0442
  - C4 | COLLECT | real_69c60aeed4242eda8c47c925:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0658
  - D2 | DISPATCH | real_69c60aeed4242eda8c47c925:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0658
  - C5 | COLLECT | real_69c60aeed4242eda8c47c925:L390 | Article 3 | score=0.0658
  - D3 | DISPATCH | real_69c60aeed4242eda8c47c925:L390 | Article 3 | score=0.0658
  - C6 | COLLECT | real_69c60aeed4242eda8c47c925:L487 | (z) | score=0.0583
  - D4 | DISPATCH | real_69c60aeed4242eda8c47c925:L487 | (z) | score=0.0583
  - C7 | COLLECT | real_69c60aeed4242eda8c47c925:L488 | (z) part 1 | score=0.0418
  - D5 | DISPATCH | real_69c60aeed4242eda8c47c925:L488 | (z) part 1 | score=0.0418
  - C8 | COLLECT | real_69c60aeed4242eda8c47c925:L515 | agreement of the Contractor;雇主系指本协议条款中所列的一方，包括雇主的法定继承人或个人代表，或根据承包商的协议将雇主的权利和义务转让给的任何人; | score=0.0418
  - C9 | COLLECT | real_69c60aeed4242eda8c47c925:L547 | (z) part 2 | score=0.0583
  - D6 | DISPATCH | real_69c60aeed4242eda8c47c925:L547 | (z) part 2 | score=0.0583
  - C10 | COLLECT | real_69c60aeed4242eda8c47c925:L572 | (ba) Site Agent means the person appointed under Clause 8.1 | score=0.0407
- projection_chars: 3596

**Step 3** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Assembled evidence G2 and G1 fully cover the 'Site Agent' section requirements.
- legal_actions (48):
  - C1 | COLLECT | real_69c60aeed4242eda8c47c925:L128 | Site Staff现场工作人员 | score=0.0448
  - D1 | DISPATCH | real_69c60aeed4242eda8c47c925:L128 | Site Staff现场工作人员 | score=0.0448
  - C2 | COLLECT | real_69c60aeed4242eda8c47c925:L129 | Duty of Site Staff现场工作人员职责 | score=0.0448
  - C3 | COLLECT | real_69c60aeed4242eda8c47c925:L130 | Directions given by Site Staff现场工作人员给出的指示 | score=0.0442
  - D2 | DISPATCH | real_69c60aeed4242eda8c47c925:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0658
  - D3 | DISPATCH | real_69c60aeed4242eda8c47c925:L390 | Article 3 | score=0.0658
  - C4 | COLLECT | real_69c60aeed4242eda8c47c925:L487 | (z) | score=0.0583
  - D4 | DISPATCH | real_69c60aeed4242eda8c47c925:L487 | (z) | score=0.0583
  - C5 | COLLECT | real_69c60aeed4242eda8c47c925:L488 | (z) part 1 | score=0.0418
  - D5 | DISPATCH | real_69c60aeed4242eda8c47c925:L488 | (z) part 1 | score=0.0418
  - C6 | COLLECT | real_69c60aeed4242eda8c47c925:L515 | agreement of the Contractor;雇主系指本协议条款中所列的一方，包括雇主的法定继承人或个人代表，或根据承包商的协议将雇主的权利和义务转让给的任何人; | score=0.0418
  - C7 | COLLECT | real_69c60aeed4242eda8c47c925:L547 | (z) part 2 | score=0.0583
  - D6 | DISPATCH | real_69c60aeed4242eda8c47c925:L547 | (z) part 2 | score=0.0583
  - C8 | COLLECT | real_69c60aeed4242eda8c47c925:L571 | ，包括承包商取得并且得到雇主认可作为工地一部分的其他土地和场所。 | score=0.0406
  - C9 | COLLECT | real_69c60aeed4242eda8c47c925:L572 | (ba) Site Agent means the person appointed under Clause 8.1 | score=0.0407
  - C10 | COLLECT | real_69c60aeed4242eda8c47c925:L573 | 现场代理是指根据第8.1条任命的人员 | score=0.0583
- projection_chars: 3616

### Evidence text (new)

```
[E1]
[§ 8.0	Site Agent--现场代理人]
  Site Agent
  给现场代理的指示。
  capable of receiving directions or instructions in English or Bahasa Malaysia.The Site Agent shall be deemed to be authorised by the Contractor to receive any directions given by the Site Staff or instructions given by the Architect and any such directions and instructions given shall be deemed to have been given to the Contractor. 承包商应确保现场代理以及相应的助理和监管人员能够理解并接收英文或马来西语的指示或指导。 现场代理应被视为已经得到承包商的授权，去接收来自现场工作人员或建筑师的任何指示，而这些指示和指导应被认为是直接提供给承包商的。
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

## latest_clean_scope_0110 (scope_collection)

**Query:** 列举《马来西亚合同样本 2006 版 翻译件- Malaysia-PAM》中“Site Agent现场代理”部分的主要条目。

**Doc:** `real_69c60aeed4242eda8c47c926`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 204 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 19 | 4 |
| trajectory_steps | n/a | 5 |

### Gold node hits (new)

- `real_69c60aeed4242eda8c47c926:L125` [HIT] retrieved=True in_text=False
- `real_69c60aeed4242eda8c47c926:L126` [HIT] retrieved=True in_text=False
- `real_69c60aeed4242eda8c47c926:L127` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C2` kind=`collect` section=`real_69c60aeed4242eda8c47c926:L124` scope=`None` depth=`0`
- reason: Collect leaf node N2 directly containing the main items for Site Agent.
- collect_section_ids: ['real_69c60aeed4242eda8c47c926:L124']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (44):
  - C1 | COLLECT | real_69c60aeed4242eda8c47c926:L123 | Site Agent现场代理 | score=0.0708
  - D1 | DISPATCH | real_69c60aeed4242eda8c47c926:L123 | Site Agent现场代理 | score=0.0708
  - C2 | COLLECT | real_69c60aeed4242eda8c47c926:L124 | Site Agent现场代理 | score=0.0664
  - C3 | COLLECT | real_69c60aeed4242eda8c47c926:L125 | Instructions to Site Agent对现场代理的说明 | score=0.0708
  - C4 | COLLECT | real_69c60aeed4242eda8c47c926:L128 | Site Staff现场工作人员 | score=0.0452
  - D2 | DISPATCH | real_69c60aeed4242eda8c47c926:L128 | Site Staff现场工作人员 | score=0.0452
  - C5 | COLLECT | real_69c60aeed4242eda8c47c926:L129 | Duty of Site Staff现场工作人员职责 | score=0.0443
  - C6 | COLLECT | real_69c60aeed4242eda8c47c926:L130 | Directions given by Site Staff现场工作人员给出的指示 | score=0.0452
  - C7 | COLLECT | real_69c60aeed4242eda8c47c926:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0653
  - D3 | DISPATCH | real_69c60aeed4242eda8c47c926:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0653
  - C8 | COLLECT | real_69c60aeed4242eda8c47c926:L390 | Article 3 | score=0.0653
  - D4 | DISPATCH | real_69c60aeed4242eda8c47c926:L390 | Article 3 | score=0.0653
  - C9 | COLLECT | real_69c60aeed4242eda8c47c926:L487 | (z) | score=0.0583
  - D5 | DISPATCH | real_69c60aeed4242eda8c47c926:L487 | (z) | score=0.0583
  - C10 | COLLECT | real_69c60aeed4242eda8c47c926:L547 | (z) part 2 | score=0.0583
  - D6 | DISPATCH | real_69c60aeed4242eda8c47c926:L547 | (z) part 2 | score=0.0583
- projection_chars: 3467

**Step 2** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60aeed4242eda8c47c926:L123` scope=`real_69c60aeed4242eda8c47c926:L123` depth=`1`
- reason: Collect the main 'Site Agent' section to retrieve its primary items as requested.
- collect_section_ids: ['real_69c60aeed4242eda8c47c926:L123']
- collect added=5 hits=5 branch_selected=True collect_full=False
- legal_actions (5):
  - C1 | COLLECT | real_69c60aeed4242eda8c47c926:L123 | Site Agent现场代理 | score=0.0708
  - C2 | COLLECT | real_69c60aeed4242eda8c47c926:L125 | Instructions to Site Agent对现场代理的说明 | score=0.0708
  - C3 | COLLECT | real_69c60aeed4242eda8c47c926:L126 | Exclusion of Person employed on the Works排除在工程上被雇用的人 | score=0.0392
  - C4 | COLLECT | real_69c60aeed4242eda8c47c926:L127 | Access To The Works进入工程的途径Access to the Works进入工程的途径 | score=0.0380
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 855

**Step 3** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60aeed4242eda8c47c926:L123` depth=`1`
- reason: The 'Site Agent' section has been collected. No further actions needed.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 190

**Step 4** `nav_dispatch`  id=`D1` kind=`dispatch` section=`real_69c60aeed4242eda8c47c926:L123` scope=`None` depth=`0`
- reason: Dispatch to collect all chunks under 'Site Agent现场代理' section.
- dispatch_regions: ['real_69c60aeed4242eda8c47c926:L123']
- child_reports=1 skipped=0
- legal_actions (44):
  - C1 | COLLECT | real_69c60aeed4242eda8c47c926:L123 | Site Agent现场代理 | score=0.0708
  - D1 | DISPATCH | real_69c60aeed4242eda8c47c926:L123 | Site Agent现场代理 | score=0.0708
  - C2 | COLLECT | real_69c60aeed4242eda8c47c926:L125 | Instructions to Site Agent对现场代理的说明 | score=0.0708
  - C3 | COLLECT | real_69c60aeed4242eda8c47c926:L128 | Site Staff现场工作人员 | score=0.0452
  - D2 | DISPATCH | real_69c60aeed4242eda8c47c926:L128 | Site Staff现场工作人员 | score=0.0452
  - C4 | COLLECT | real_69c60aeed4242eda8c47c926:L129 | Duty of Site Staff现场工作人员职责 | score=0.0443
  - C5 | COLLECT | real_69c60aeed4242eda8c47c926:L130 | Directions given by Site Staff现场工作人员给出的指示 | score=0.0452
  - C6 | COLLECT | real_69c60aeed4242eda8c47c926:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0653
  - D3 | DISPATCH | real_69c60aeed4242eda8c47c926:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0653
  - C7 | COLLECT | real_69c60aeed4242eda8c47c926:L390 | Article 3 | score=0.0653
  - D4 | DISPATCH | real_69c60aeed4242eda8c47c926:L390 | Article 3 | score=0.0653
  - C8 | COLLECT | real_69c60aeed4242eda8c47c926:L487 | (z) | score=0.0583
  - D5 | DISPATCH | real_69c60aeed4242eda8c47c926:L487 | (z) | score=0.0583
  - C9 | COLLECT | real_69c60aeed4242eda8c47c926:L547 | (z) part 2 | score=0.0583
  - D6 | DISPATCH | real_69c60aeed4242eda8c47c926:L547 | (z) part 2 | score=0.0583
  - C10 | COLLECT | real_69c60aeed4242eda8c47c926:L573 | 现场代理是指根据第8.1条任命的人员 | score=0.0583
- projection_chars: 3428

**Step 5** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Assembled evidence G1 fully covers the 'Site Agent' section main items.
- legal_actions (47):
  - C1 | COLLECT | real_69c60aeed4242eda8c47c926:L128 | Site Staff现场工作人员 | score=0.0452
  - D1 | DISPATCH | real_69c60aeed4242eda8c47c926:L128 | Site Staff现场工作人员 | score=0.0452
  - C2 | COLLECT | real_69c60aeed4242eda8c47c926:L129 | Duty of Site Staff现场工作人员职责 | score=0.0443
  - C3 | COLLECT | real_69c60aeed4242eda8c47c926:L130 | Directions given by Site Staff现场工作人员给出的指示 | score=0.0452
  - C4 | COLLECT | real_69c60aeed4242eda8c47c926:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0653
  - D2 | DISPATCH | real_69c60aeed4242eda8c47c926:L338 | Adjudication And Arbitration裁决和仲裁 | score=0.0653
  - C5 | COLLECT | real_69c60aeed4242eda8c47c926:L390 | Article 3 | score=0.0653
  - D3 | DISPATCH | real_69c60aeed4242eda8c47c926:L390 | Article 3 | score=0.0653
  - C6 | COLLECT | real_69c60aeed4242eda8c47c926:L487 | (z) | score=0.0583
  - D4 | DISPATCH | real_69c60aeed4242eda8c47c926:L487 | (z) | score=0.0583
  - C7 | COLLECT | real_69c60aeed4242eda8c47c926:L547 | (z) part 2 | score=0.0583
  - D5 | DISPATCH | real_69c60aeed4242eda8c47c926:L547 | (z) part 2 | score=0.0583
  - C8 | COLLECT | real_69c60aeed4242eda8c47c926:L571 | ，包括承包商取得并且得到雇主认可作为工地一部分的其他土地和场所。 | score=0.0411
  - C9 | COLLECT | real_69c60aeed4242eda8c47c926:L573 | 现场代理是指根据第8.1条任命的人员 | score=0.0583
  - C10 | COLLECT | real_69c60aeed4242eda8c47c926:L575 | 现场工作人员指的是依据第10.1条款任命的人员 | score=0.0423
  - C11 | COLLECT | real_69c60aeed4242eda8c47c926:L828 | 8.0	Site Agent--现场代理人 | score=0.0653
- projection_chars: 3592

### Subagent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60aeed4242eda8c47c926:L123 (ok)
collected 4 branch node(s); explicit roots=['real_69c60aeed4242eda8c47c926:L123']
collected: real_69c60aeed4242eda8c47c926:L123, real_69c60aeed4242eda8c47c926:L125, real_69c60aeed4242eda8c47c926:L126, real_69c60aeed4242eda8c47c926:L127
reason: The 'Site Agent' section has been collected. No further actions needed.
---
=== End Investigate ===
```

### Evidence text (new)

```
[E1]
[§ Site Agent现场代理]
  Site Agent现场代理
  Site Agent现场代理
  Instructions to Site Agent对现场代理的说明
  Exclusion of Person employed on the Works排除在工程上被雇用的人
  Access To The Works进入工程的途径Access to the Works进入工程的途径
```

### Evidence text (old)

```
[E1]
马来西亚合同样本 2006 版 翻译件- Malaysia-PAM.docx

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
Materials,Goods And Workmanship To Conform To Descri
```

## latest_clean_scope_0124 (scope_collection)

**Query:** 列举《华侨城坪山综合体项目基坑支护工程专项施工方案》中“华侨城坪山综合体项目基坑支护工程专项施工方案.docx”部分的主要条目。

**Doc:** `real_69c60b0ad4242eda8c47c944`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 494 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 20 | 18 |
| trajectory_steps | n/a | 4 |

### Gold node hits (new)

- `real_69c60b0ad4242eda8c47c944:L5` [MISS] retrieved=False in_text=False
- `real_69c60b0ad4242eda8c47c944:L6` [MISS] retrieved=False in_text=False
- `real_69c60b0ad4242eda8c47c944:L7` [MISS] retrieved=False in_text=False
- `real_69c60b0ad4242eda8c47c944:L10` [MISS] retrieved=False in_text=False
- `real_69c60b0ad4242eda8c47c944:L12` [MISS] retrieved=False in_text=False
- `real_69c60b0ad4242eda8c47c944:L15` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60b0ad4242eda8c47c944:L1` scope=`None` depth=`0`
- reason: Collect main sections of the plan: Overview, Layout, Risks, Basis, and Schedule.
- collect_section_ids: ['real_69c60b0ad4242eda8c47c944:L1', 'real_69c60b0ad4242eda8c47c944:L88', 'real_69c60b0ad4242eda8c47c944:L113', 'real_69c60b0ad4242eda8c47c944:L124', 'real_69c60b0ad4242eda8c47c944:L187']
- collect added=24 hits=26 branch_selected=True collect_full=False
- legal_actions (47):
  - C1 | COLLECT | real_69c60b0ad4242eda8c47c944:L1 | 工程概况 | score=0.0498
  - D1 | DISPATCH | real_69c60b0ad4242eda8c47c944:L1 | 工程概况 | score=0.0498
  - C2 | COLLECT | real_69c60b0ad4242eda8c47c944:L2 | 基坑工程概况和特点 | score=0.0426
  - D2 | DISPATCH | real_69c60b0ad4242eda8c47c944:L2 | 基坑工程概况和特点 | score=0.0426
  - C3 | COLLECT | real_69c60b0ad4242eda8c47c944:L69 | 周边环境条件 | score=0.0426
  - D3 | DISPATCH | real_69c60b0ad4242eda8c47c944:L69 | 周边环境条件 | score=0.0426
  - C4 | COLLECT | real_69c60b0ad4242eda8c47c944:L72 | 根据设计图纸说明本项目基坑北侧支护工程施工范围划分为： | score=0.0426
  - C5 | COLLECT | real_69c60b0ad4242eda8c47c944:L88 | 施工平面布置 | score=0.0426
  - D4 | DISPATCH | real_69c60b0ad4242eda8c47c944:L88 | 施工平面布置 | score=0.0426
  - C6 | COLLECT | real_69c60b0ad4242eda8c47c944:L94 | 1.2.2 施工部署综述 | score=0.0426
  - D5 | DISPATCH | real_69c60b0ad4242eda8c47c944:L94 | 1.2.2 施工部署综述 | score=0.0426
  - C7 | COLLECT | real_69c60b0ad4242eda8c47c944:L95 | 施工区段划分：根据施工范围、施工图纸与建设单位的工期要求等综合情况，详细勘察了周围环境，确定了现场大门开设两个出入口，根据现场大门开设位置和三维工况模拟，将基坑分为一、二、三、四共四个生产区，其中一区为主塔楼区，二区为裙楼区域，三区为副塔楼区域，四区为裙楼区。 | score=0.0426
  - C8 | COLLECT | real_69c60b0ad4242eda8c47c944:L113 | 1.4 风险辨识与分级 | score=0.0498
  - D6 | DISPATCH | real_69c60b0ad4242eda8c47c944:L113 | 1.4 风险辨识与分级 | score=0.0498
  - C9 | COLLECT | real_69c60b0ad4242eda8c47c944:L120 | 依据设计图纸要求，根据建办质［2018］31号文及我单位关于《危险性较大的分部分项工程安全专项施工方案管理制度》 的要求：1、开挖深度超过5m（含5m）的基坑（槽）的土方开挖、支护、降水工程；2、开挖深度虽未超过5m，但地质条件、周围环境和地下管线复杂或影响毗邻建筑（构筑）物安全的基坑（槽）的土方开挖、支护、降水工程；这两项都属于“超过一定规模的危险性较大的分部分项工程”，拟建工程基坑开挖深度为2 | score=0.0498
  - C10 | COLLECT | real_69c60b0ad4242eda8c47c944:L121 | 综上可知，根据住房城乡建设部办公厅关于实施《危险性较大的分部分项工程安全管理规定》有关问题的通知建办质（2018）31号，此基坑工程属“超过一定规模的危险性较大的分部分项工程”，住建部37号令条文规定：施工单位应当组织专家对专项方案进行论证。施工单位应当根据论证报告修改完善专项方案，专项施工方案应当由施工单位技术负责人审核签字、加盖单位公章，并由总监理工程师审查签字、加盖执业印章后方可实施。 | score=0.0487
- projection_chars: 3028

**Step 2** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60b0ad4242eda8c47c944:L233` scope=`None` depth=`0`
- collect_section_ids: ['real_69c60b0ad4242eda8c47c944:L233']
- collect added=6 hits=6 branch_selected=True collect_full=False
- legal_actions (58):
  - C1 | COLLECT | real_69c60b0ad4242eda8c47c944:L233 | 施工工艺技术 | score=0.0363
  - D1 | DISPATCH | real_69c60b0ad4242eda8c47c944:L233 | 施工工艺技术 | score=0.0363
  - C2 | COLLECT | real_69c60b0ad4242eda8c47c944:L273 | 施工方法及操作要求 | score=0.0363
  - D2 | DISPATCH | real_69c60b0ad4242eda8c47c944:L273 | 施工方法及操作要求 | score=0.0363
  - C3 | COLLECT | real_69c60b0ad4242eda8c47c944:L281 | 咬合桩施工 | score=0.0363
  - D3 | DISPATCH | real_69c60b0ad4242eda8c47c944:L281 | 咬合桩施工 | score=0.0363
  - C4 | COLLECT | real_69c60b0ad4242eda8c47c944:L299 | 成孔： | score=0.0342
  - D4 | DISPATCH | real_69c60b0ad4242eda8c47c944:L299 | 成孔： | score=0.0342
  - C5 | COLLECT | real_69c60b0ad4242eda8c47c944:L306 | 分段施工接头处理：在不同施工段间设置砂桩（成孔后用砂灌满），待施工到此接头时挖出砂灌满混凝土即可。桩的排列方式为钢筋砼桩（B桩）和素桩（A桩）间隔布置（见图示）。 | score=0.0342
  - C6 | COLLECT | real_69c60b0ad4242eda8c47c944:L326 | 钢筋笼安装 | score=0.0363
  - D5 | DISPATCH | real_69c60b0ad4242eda8c47c944:L326 | 钢筋笼安装 | score=0.0363
  - C7 | COLLECT | real_69c60b0ad4242eda8c47c944:L329 | 总结：图片展示了一个建筑工地，几栋高层住宅楼正在建设中。画面中央有一台起重机正在吊装一根长柱，周围有其他施工设备和材料。背景是晴朗的蓝天，工地地面为裸露的泥土，周围有绿色植被和部分已建成的楼房。整体场景体现了城市建筑项目的进行状态。 | score=0.0363
  - C8 | COLLECT | real_69c60b0ad4242eda8c47c944:L518 | 施工保证措施 | score=0.0407
  - D6 | DISPATCH | real_69c60b0ad4242eda8c47c944:L518 | 施工保证措施 | score=0.0407
  - C9 | COLLECT | real_69c60b0ad4242eda8c47c944:L568 | 技术措施 | score=0.0398
  - D7 | DISPATCH | real_69c60b0ad4242eda8c47c944:L568 | 技术措施 | score=0.0398
- projection_chars: 3431

**Step 3** `nav_collect`  id=`C32` kind=`collect` section=`real_69c60b0ad4242eda8c47c944:L852` scope=`None` depth=`0`
- reason: Collect 'Calculation and Drawings' section to list main items as requested.
- collect_section_ids: ['real_69c60b0ad4242eda8c47c944:L852']
- collect added=3 hits=3 branch_selected=True collect_full=False
- legal_actions (55):
  - C1 | COLLECT | real_69c60b0ad4242eda8c47c944:L518 | 施工保证措施 | score=0.0407
  - D1 | DISPATCH | real_69c60b0ad4242eda8c47c944:L518 | 施工保证措施 | score=0.0407
  - C2 | COLLECT | real_69c60b0ad4242eda8c47c944:L519 | 组织保障措施 | score=0.0312
  - D2 | DISPATCH | real_69c60b0ad4242eda8c47c944:L519 | 组织保障措施 | score=0.0312
  - C3 | COLLECT | real_69c60b0ad4242eda8c47c944:L520 | 坚决执行企业管生产必须管安全的原则。必须坚持“安全第一，预防为主，综合治理”的方针。肯定安全在建筑生产活动中为首要位置和重要性。当安全与生产发生矛盾的时候，应该服从安全，消灭隐患，保证建设工程在安全的条件下生产。 | score=0.0312
  - C4 | COLLECT | real_69c60b0ad4242eda8c47c944:L568 | 技术措施 | score=0.0398
  - D3 | DISPATCH | real_69c60b0ad4242eda8c47c944:L568 | 技术措施 | score=0.0398
  - C5 | COLLECT | real_69c60b0ad4242eda8c47c944:L569 | 安全保证措施 | score=0.0398
  - D4 | DISPATCH | real_69c60b0ad4242eda8c47c944:L569 | 安全保证措施 | score=0.0398
  - C6 | COLLECT | real_69c60b0ad4242eda8c47c944:L570 | 危险源辨识及风险评价 | score=0.0398
  - D5 | DISPATCH | real_69c60b0ad4242eda8c47c944:L570 | 危险源辨识及风险评价 | score=0.0398
  - C7 | COLLECT | real_69c60b0ad4242eda8c47c944:L571 | 本工程安全薄弱环节主要集中在深基坑支护工程、深基坑土方开挖及外运、基坑检测、降水工程、基坑安全防护、起重设备安装使用、加工棚机械作业、动火作业等。具体表现在以下几个方面： | score=0.0379
  - C8 | COLLECT | real_69c60b0ad4242eda8c47c944:L580 | 土方开挖运输施工保护措施 | score=0.0398
  - D6 | DISPATCH | real_69c60b0ad4242eda8c47c944:L580 | 土方开挖运输施工保护措施 | score=0.0398
  - C9 | COLLECT | real_69c60b0ad4242eda8c47c944:L584 | 项目部编制专项的交通策划方案，针对本工程地理位置，策划项目东侧有一个主出入口，南侧有一个次出入口，主出入口和次出入口全部作为土方开挖施工阶段的车辆出土口，制定专门的土方运输路线，确保土方开挖过程中的交通运输安全。如下图： | score=0.0398
  - C10 | COLLECT | real_69c60b0ad4242eda8c47c944:L629 | 各类地上地下管线及设施的安全保护 | score=0.0355
- projection_chars: 3498

**Step 4** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Assembled evidence covers all main sections of the special construction plan including overview, basis, plan, technology, and calculations.
- legal_actions (54):
  - C1 | COLLECT | real_69c60b0ad4242eda8c47c944:L518 | 施工保证措施 | score=0.0407
  - D1 | DISPATCH | real_69c60b0ad4242eda8c47c944:L518 | 施工保证措施 | score=0.0407
  - C2 | COLLECT | real_69c60b0ad4242eda8c47c944:L519 | 组织保障措施 | score=0.0312
  - D2 | DISPATCH | real_69c60b0ad4242eda8c47c944:L519 | 组织保障措施 | score=0.0312
  - C3 | COLLECT | real_69c60b0ad4242eda8c47c944:L520 | 坚决执行企业管生产必须管安全的原则。必须坚持“安全第一，预防为主，综合治理”的方针。肯定安全在建筑生产活动中为首要位置和重要性。当安全与生产发生矛盾的时候，应该服从安全，消灭隐患，保证建设工程在安全的条件下生产。 | score=0.0312
  - C4 | COLLECT | real_69c60b0ad4242eda8c47c944:L568 | 技术措施 | score=0.0398
  - D3 | DISPATCH | real_69c60b0ad4242eda8c47c944:L568 | 技术措施 | score=0.0398
  - C5 | COLLECT | real_69c60b0ad4242eda8c47c944:L569 | 安全保证措施 | score=0.0398
  - D4 | DISPATCH | real_69c60b0ad4242eda8c47c944:L569 | 安全保证措施 | score=0.0398
  - C6 | COLLECT | real_69c60b0ad4242eda8c47c944:L570 | 危险源辨识及风险评价 | score=0.0398
  - D5 | DISPATCH | real_69c60b0ad4242eda8c47c944:L570 | 危险源辨识及风险评价 | score=0.0398
  - C7 | COLLECT | real_69c60b0ad4242eda8c47c944:L571 | 本工程安全薄弱环节主要集中在深基坑支护工程、深基坑土方开挖及外运、基坑检测、降水工程、基坑安全防护、起重设备安装使用、加工棚机械作业、动火作业等。具体表现在以下几个方面： | score=0.0379
  - C8 | COLLECT | real_69c60b0ad4242eda8c47c944:L580 | 土方开挖运输施工保护措施 | score=0.0398
  - D6 | DISPATCH | real_69c60b0ad4242eda8c47c944:L580 | 土方开挖运输施工保护措施 | score=0.0398
  - C9 | COLLECT | real_69c60b0ad4242eda8c47c944:L584 | 项目部编制专项的交通策划方案，针对本工程地理位置，策划项目东侧有一个主出入口，南侧有一个次出入口，主出入口和次出入口全部作为土方开挖施工阶段的车辆出土口，制定专门的土方运输路线，确保土方开挖过程中的交通运输安全。如下图： | score=0.0398
  - C10 | COLLECT | real_69c60b0ad4242eda8c47c944:L629 | 各类地上地下管线及设施的安全保护 | score=0.0355
- projection_chars: 3632

### Evidence text (new)

```
[E1]
[§ 施工工艺技术]
  技术参数
  咬合桩
  （1）咬合桩共计688根，其中荤桩344根，素桩344根。采用“软咬合”施工工艺，全套管全回转钻机成孔施工。
  工艺流程
  基坑工程总的施工工艺流程
  测量放线→咬合桩施工→立柱桩施工→槽钢桩施工→袖阀管施工→支撑梁施工→土方开挖→支撑梁施工（随着土方开挖逐层进行施工）
  施工方法及操作要求
  施工准备
  （1）组织项目人员熟悉图纸，完成作业工人培训及技术及安全交底。
  检查要求
  （1）支护结构施工现场使用的砂、水泥、钢筋、混凝土等原材料和加工的成品，应按有关设计规范及施工验收标准进行检验。
  （2）咬合桩检测：咬合桩采用超声波透射法检测桩身完整性，检测数量不小于荤桩总桩数的20%，且不应少于10 根。当桩身完整性类别为Ⅲ类、Ⅳ类时，应采用钻芯法补充检测，钻芯法检测数量不小于荤桩总桩数的1%，且不少于3 根。
  常见问题及预防、处理措施
  1）护坡桩常见问题及预防处理措施：
  （1）桩位偏差

[E2]
[§ 施工计划]
材料与设备计划
主要材料需求计划
表3.2-1 主要材料需求计划表
```

### Evidence text (old)

```
[E1]
工程概况

[E2]
编制依据

[E3]
施工计划

[E4]
施工工艺技术

[E5]
施工保证措施

[E6]
基坑工程概况和特点
工程基本情况
表1.1-1 基坑工程概况表

[E7]
法律法规
《建筑地基基础工程施工质量验收规范》GB 50202-2018
《混凝土结构工程施工规范》GB 50666-2011

[E8]
施工进度计划
施工总进度计划
图表展示了华侨城坪山综合体项目地基基础工程施工的总进度计划，详细列出了从2020年6月至2021年5月各阶段的施工任务和时间安排。计划分为五个阶段，每个阶段包含多个具体工程项，如护坡施工、土方开挖、支撑施工等，并通过线条和节点表示各任务的开始、结束时间和相互关系。

[E9]
技术参数
咬合桩
（1）咬合桩共计688根，其中荤桩344根，素桩344根。采用“软咬合”施工工艺，全套管全回转钻机成孔施工。

[E10]
组织保障措施
坚决执行企业管生产必须管安全的原则。必须坚持“安全第一，预防为主，综合治理”的方针。肯定安全在建筑生产活动中为首要位置和重要性。当安全与生产发生矛盾的时候，应该服从安全，消灭隐患，保证建设工程
```

## latest_clean_scope_0129 (scope_collection)

**Query:** 列举《华侨城坪山综合体项目基坑支护工程专项施工方案》中“施工管理及作业人员配备和分工”部分的主要条目。

**Doc:** `real_69c60b0ad4242eda8c47c944`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 286 | 181 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 11 | 9 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60b0ad4242eda8c47c944:L810` [MISS] retrieved=False in_text=False
- `real_69c60b0ad4242eda8c47c944:L815` [MISS] retrieved=False in_text=False
- `real_69c60b0ad4242eda8c47c944:L817` [MISS] retrieved=False in_text=False
- `real_69c60b0ad4242eda8c47c944:L821` [MISS] retrieved=False in_text=False
- `real_69c60b0ad4242eda8c47c944:L823` [MISS] retrieved=False in_text=False
- `real_69c60b0ad4242eda8c47c944:L825` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C27` kind=`collect` section=`real_69c60b0ad4242eda8c47c944:L780` scope=`None` depth=`0`
- reason: Collect the main section and its subsections on personnel allocation and division of labor.
- collect_section_ids: ['real_69c60b0ad4242eda8c47c944:L780', 'real_69c60b0ad4242eda8c47c944:L781', 'real_69c60b0ad4242eda8c47c944:L787', 'real_69c60b0ad4242eda8c47c944:L789']
- collect added=8 hits=9 branch_selected=True collect_full=True
- legal_actions (61):
  - C1 | COLLECT | real_69c60b0ad4242eda8c47c944:L1 | 工程概况 | score=0.0616
  - D1 | DISPATCH | real_69c60b0ad4242eda8c47c944:L1 | 工程概况 | score=0.0616
  - C2 | COLLECT | real_69c60b0ad4242eda8c47c944:L88 | 施工平面布置 | score=0.0616
  - D2 | DISPATCH | real_69c60b0ad4242eda8c47c944:L88 | 施工平面布置 | score=0.0616
  - C3 | COLLECT | real_69c60b0ad4242eda8c47c944:L89 | 布置原则 | score=0.0616
  - D3 | DISPATCH | real_69c60b0ad4242eda8c47c944:L89 | 布置原则 | score=0.0616
  - C4 | COLLECT | real_69c60b0ad4242eda8c47c944:L92 | （3）根据现场实际情况和工期要求，基坑支护、土方挖运采用分层分段施工。配备足够的劳动力和施工管理人员，做到连续、均衡施工。 | score=0.0616
  - C5 | COLLECT | real_69c60b0ad4242eda8c47c944:L94 | 1.2.2 施工部署综述 | score=0.0552
  - D4 | DISPATCH | real_69c60b0ad4242eda8c47c944:L94 | 1.2.2 施工部署综述 | score=0.0552
  - C6 | COLLECT | real_69c60b0ad4242eda8c47c944:L97 | 从各工序的逻辑关系和机械、设备、材料、人员的相互关联关系出发，使各工种、工序以及各协调配合专业单位都能实现紧密的交叉流水搭接施工，我们将整个地基基础施工划分为五个施工阶段施工，如下表： | score=0.0552
  - C7 | COLLECT | real_69c60b0ad4242eda8c47c944:L113 | 1.4 风险辨识与分级 | score=0.0496
  - D5 | DISPATCH | real_69c60b0ad4242eda8c47c944:L113 | 1.4 风险辨识与分级 | score=0.0496
  - C8 | COLLECT | real_69c60b0ad4242eda8c47c944:L120 | 依据设计图纸要求，根据建办质［2018］31号文及我单位关于《危险性较大的分部分项工程安全专项施工方案管理制度》 的要求：1、开挖深度超过5m（含5m）的基坑（槽）的土方开挖、支护、降水工程；2、开挖深度虽未超过5m，但地质条件、周围环境和地下管线复杂或影响毗邻建筑（构筑）物安全的基坑（槽）的土方开挖、支护、降水工程；这两项都属于“超过一定规模的危险性较大的分部分项工程”，拟建工程基坑开挖深度为2 | score=0.0482
  - C9 | COLLECT | real_69c60b0ad4242eda8c47c944:L121 | 综上可知，根据住房城乡建设部办公厅关于实施《危险性较大的分部分项工程安全管理规定》有关问题的通知建办质（2018）31号，此基坑工程属“超过一定规模的危险性较大的分部分项工程”，住建部37号令条文规定：施工单位应当组织专家对专项方案进行论证。施工单位应当根据论证报告修改完善专项方案，专项施工方案应当由施工单位技术负责人审核签字、加盖单位公章，并由总监理工程师审查签字、加盖执业印章后方可实施。 | score=0.0496
  - C10 | COLLECT | real_69c60b0ad4242eda8c47c944:L124 | 编制依据 | score=0.0483
  - D6 | DISPATCH | real_69c60b0ad4242eda8c47c944:L124 | 编制依据 | score=0.0483
- projection_chars: 3227

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Assembled evidence covers all required personnel categories: management, safety, and special operations.
- legal_actions (59):
  - C1 | COLLECT | real_69c60b0ad4242eda8c47c944:L1 | 工程概况 | score=0.0616
  - D1 | DISPATCH | real_69c60b0ad4242eda8c47c944:L1 | 工程概况 | score=0.0616
  - C2 | COLLECT | real_69c60b0ad4242eda8c47c944:L88 | 施工平面布置 | score=0.0616
  - D2 | DISPATCH | real_69c60b0ad4242eda8c47c944:L88 | 施工平面布置 | score=0.0616
  - C3 | COLLECT | real_69c60b0ad4242eda8c47c944:L89 | 布置原则 | score=0.0616
  - D3 | DISPATCH | real_69c60b0ad4242eda8c47c944:L89 | 布置原则 | score=0.0616
  - C4 | COLLECT | real_69c60b0ad4242eda8c47c944:L92 | （3）根据现场实际情况和工期要求，基坑支护、土方挖运采用分层分段施工。配备足够的劳动力和施工管理人员，做到连续、均衡施工。 | score=0.0616
  - C5 | COLLECT | real_69c60b0ad4242eda8c47c944:L94 | 1.2.2 施工部署综述 | score=0.0552
  - D4 | DISPATCH | real_69c60b0ad4242eda8c47c944:L94 | 1.2.2 施工部署综述 | score=0.0552
  - C6 | COLLECT | real_69c60b0ad4242eda8c47c944:L97 | 从各工序的逻辑关系和机械、设备、材料、人员的相互关联关系出发，使各工种、工序以及各协调配合专业单位都能实现紧密的交叉流水搭接施工，我们将整个地基基础施工划分为五个施工阶段施工，如下表： | score=0.0552
  - C7 | COLLECT | real_69c60b0ad4242eda8c47c944:L113 | 1.4 风险辨识与分级 | score=0.0496
  - D5 | DISPATCH | real_69c60b0ad4242eda8c47c944:L113 | 1.4 风险辨识与分级 | score=0.0496
  - C8 | COLLECT | real_69c60b0ad4242eda8c47c944:L120 | 依据设计图纸要求，根据建办质［2018］31号文及我单位关于《危险性较大的分部分项工程安全专项施工方案管理制度》 的要求：1、开挖深度超过5m（含5m）的基坑（槽）的土方开挖、支护、降水工程；2、开挖深度虽未超过5m，但地质条件、周围环境和地下管线复杂或影响毗邻建筑（构筑）物安全的基坑（槽）的土方开挖、支护、降水工程；这两项都属于“超过一定规模的危险性较大的分部分项工程”，拟建工程基坑开挖深度为2 | score=0.0482
  - C9 | COLLECT | real_69c60b0ad4242eda8c47c944:L121 | 综上可知，根据住房城乡建设部办公厅关于实施《危险性较大的分部分项工程安全管理规定》有关问题的通知建办质（2018）31号，此基坑工程属“超过一定规模的危险性较大的分部分项工程”，住建部37号令条文规定：施工单位应当组织专家对专项方案进行论证。施工单位应当根据论证报告修改完善专项方案，专项施工方案应当由施工单位技术负责人审核签字、加盖单位公章，并由总监理工程师审查签字、加盖执业印章后方可实施。 | score=0.0496
  - C10 | COLLECT | real_69c60b0ad4242eda8c47c944:L124 | 编制依据 | score=0.0483
  - D6 | DISPATCH | real_69c60b0ad4242eda8c47c944:L124 | 编制依据 | score=0.0483
- projection_chars: 3545

### Evidence text (new)

```
[E1]
[§ 施工管理人员]
  施工项目管理组织机构
  图6.1.1 施工项目管理组织机构
  项目经理部的部门设置和人员配备
  图6.1.2-1 施工项目部人员组成分布图
  表6.1.2-1项目经理部的部门设置和人员配备

[E2]
[§ 专职安全人员]
表6.2-1 专职安全人员及职责表

[E3]
[§ 特种作业人员]
表6.3 特种作业人员表
```

### Evidence text (old)

```
[E1]
施工管理及作业人员配备和分工

[E2]
施工管理人员
施工项目管理组织机构
图6.1.1 施工项目管理组织机构

[E3]
专职安全人员
表6.2-1 专职安全人员及职责表

[E4]
特种作业人员
表6.3 特种作业人员表

[E5]
项目经理部的部门设置和人员配备
图6.1.2-1 施工项目部人员组成分布图
表6.1.2-1项目经理部的部门设置和人员配备

[E6]
施工项目管理组织机构
图6.1.1 施工项目管理组织机构

[E7]
[§ 特种作业人员]
表6.3 特种作业人员表

[E8]
[§ 专职安全人员]
表6.2-1 专职安全人员及职责表
```

## latest_clean_scope_0132 (scope_collection)

**Query:** 列举《陕建丝路创发中心高支模专项施工方案》中“五、施工保证措施”部分的主要条目。

**Doc:** `real_69c60b33d4242eda8c47c959`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 211 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 20 | 9 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60b33d4242eda8c47c959:L278` [MISS] retrieved=False in_text=False
- `real_69c60b33d4242eda8c47c959:L282` [MISS] retrieved=False in_text=False
- `real_69c60b33d4242eda8c47c959:L283` [MISS] retrieved=False in_text=False
- `real_69c60b33d4242eda8c47c959:L284` [MISS] retrieved=False in_text=False
- `real_69c60b33d4242eda8c47c959:L285` [MISS] retrieved=False in_text=False
- `real_69c60b33d4242eda8c47c959:L286` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60b33d4242eda8c47c959:L272` scope=`None` depth=`0`
- reason: Collect section 5 to list main items of construction guarantee measures.
- collect_section_ids: ['real_69c60b33d4242eda8c47c959:L272']
- collect added=4 hits=4 branch_selected=True collect_full=False
- legal_actions (48):
  - C1 | COLLECT | real_69c60b33d4242eda8c47c959:L272 | 五、施工保证措施 | score=0.0622
  - D1 | DISPATCH | real_69c60b33d4242eda8c47c959:L272 | 五、施工保证措施 | score=0.0622
  - C2 | COLLECT | real_69c60b33d4242eda8c47c959:L273 | 5.1组织保障措施 | score=0.0622
  - D2 | DISPATCH | real_69c60b33d4242eda8c47c959:L273 | 5.1组织保障措施 | score=0.0622
  - C3 | COLLECT | real_69c60b33d4242eda8c47c959:L274 | 5.1.1安全组织架构 | score=0.0622
  - D3 | DISPATCH | real_69c60b33d4242eda8c47c959:L274 | 5.1.1安全组织架构 | score=0.0622
  - C4 | COLLECT | real_69c60b33d4242eda8c47c959:L294 | ①对本项目安全生产、文明施工工作的技术方面负全面责任贯彻执行国家在安全方面的技术法规和各项安全规定。 | score=0.0518
  - C5 | COLLECT | real_69c60b33d4242eda8c47c959:L297 | ④组织并进行安全技术教育工作，从技术方面指导和支持项目专职安全员的工作。 | score=0.0469
  - C6 | COLLECT | real_69c60b33d4242eda8c47c959:L298 | ⑤组织编制项目技术革新和施工新技术、新工艺中的安全施工措施，并促其实现。 | score=0.0622
  - C7 | COLLECT | real_69c60b33d4242eda8c47c959:L303 | ②参加定期、不定期安全检查，检查项目施工场所的安全施工文明施工情况，对查出的事故隐患，下发整改通知单，限期整改，并督促落实，在生产中遇到重大险情时，有权下令停产整顿，并向主管领导汇报。 | score=0.0462
  - C8 | COLLECT | real_69c60b33d4242eda8c47c959:L304 | ③参加工地重要施工项目和危险作业项目开工前的安全技术措施交底，检查开工安全施工条件，监督安全交底的执行，监督班组的安全活动，检查班组的安全活动记录。 | score=0.0606
  - C9 | COLLECT | real_69c60b33d4242eda8c47c959:L310 | 5.1.2安全保证体系 | score=0.0481
  - C10 | COLLECT | real_69c60b33d4242eda8c47c959:L311 | 5.2技术措施 | score=0.0607
  - D4 | DISPATCH | real_69c60b33d4242eda8c47c959:L311 | 5.2技术措施 | score=0.0607
  - C11 | COLLECT | real_69c60b33d4242eda8c47c959:L312 | 5.2.1安全管理措施 | score=0.0474
  - D5 | DISPATCH | real_69c60b33d4242eda8c47c959:L312 | 5.2.1安全管理措施 | score=0.0474
- projection_chars: 3107

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: The assembled evidence [G1] contains the full list of main items under 'V. Construction Guarantee Measures' as requested.
- legal_actions (63):
  - C1 | COLLECT | real_69c60b33d4242eda8c47c959:L1 | 一、工程概况 | score=0.0382
  - D1 | DISPATCH | real_69c60b33d4242eda8c47c959:L1 | 一、工程概况 | score=0.0382
  - C2 | COLLECT | real_69c60b33d4242eda8c47c959:L2 | 1.1模板支撑体系工程概况和特点 | score=0.0382
  - D2 | DISPATCH | real_69c60b33d4242eda8c47c959:L2 | 1.1模板支撑体系工程概况和特点 | score=0.0382
  - C3 | COLLECT | real_69c60b33d4242eda8c47c959:L3 | 1.1.1工程基本情况 | score=0.0382
  - D3 | DISPATCH | real_69c60b33d4242eda8c47c959:L3 | 1.1.1工程基本情况 | score=0.0382
  - C4 | COLLECT | real_69c60b33d4242eda8c47c959:L4 | 陕建丝路创发中心位于西安能源金贸区，含3栋楼及地下车库。总建筑面积约29.47万㎡，最高楼211m。采用型钢混凝土框架-核心筒结构，桩筏基础，地上层数分别为43、42、20层，地下3层。 | score=0.0382
  - C5 | COLLECT | real_69c60b33d4242eda8c47c959:L11 | 1.2施工平面布置及立面布置 | score=0.0350
  - D4 | DISPATCH | real_69c60b33d4242eda8c47c959:L11 | 1.2施工平面布置及立面布置 | score=0.0350
  - C6 | COLLECT | real_69c60b33d4242eda8c47c959:L12 | 2#楼地上高支模区域平面图（填充部分） | score=0.0350
  - C7 | COLLECT | real_69c60b33d4242eda8c47c959:L14 | 3#楼地上高支模区域平面图（填充部分） | score=0.0345
  - C8 | COLLECT | real_69c60b33d4242eda8c47c959:L38 | 四、施工工艺技术 | score=0.0448
  - D5 | DISPATCH | real_69c60b33d4242eda8c47c959:L38 | 四、施工工艺技术 | score=0.0448
  - C9 | COLLECT | real_69c60b33d4242eda8c47c959:L99 | 4.2工艺流程 | score=0.0448
  - D6 | DISPATCH | real_69c60b33d4242eda8c47c959:L99 | 4.2工艺流程 | score=0.0448
  - C10 | COLLECT | real_69c60b33d4242eda8c47c959:L116 | 4.2.2施工要点 | score=0.0448
- projection_chars: 3417

### Evidence text (new)

```
[E1]
[§ 五、施工保证措施]
  5.1组织保障措施
  5.1.1安全组织架构
  小组成员组成
  5.2技术措施
  5.2.1安全管理措施
  （1）支撑脚手架搭设作业人员应正确佩戴使用安全帽、安全带和防滑鞋。
  5.3监测监控措施
  5.3.1监测点的设置
  监测点在每次所浇模架周边布点，根据《建筑施工临时支撑结构技术规范》JGJ300-2013中的要求，进行位移监测时，须按照如下要求设置监测点：
```

### Evidence text (old)

```
[E1]
五、施工保证措施

[E2]
5.1组织保障措施
5.1.1安全组织架构
小组成员组成

[E3]
5.2技术措施
5.2.1安全管理措施
（1）支撑脚手架搭设作业人员应正确佩戴使用安全帽、安全带和防滑鞋。

[E4]
5.3监测监控措施
5.3.1监测点的设置
监测点在每次所浇模架周边布点，根据《建筑施工临时支撑结构技术规范》JGJ300-2013中的要求，进行位移监测时，须按照如下要求设置监测点：

[E5]
5.1.2安全保证体系

[E6]
5.2.2质量技术保证措施
（1）制定以项目经理为首的质量保证机构。
（2）质量总监编制质量方面的各种管理制度、工作程序、验收程序、验收标准、创优计划，检查各部门、各分包质量保证体系的运行情况，抽查各分项工程质量状况，执行情况。

[E7]
5.3.1监测仪器设备和人员的配备
（1）监测仪器设备
（2）人员配备

[E8]
5.2.4环境保护措施
（1）加强对易燃易爆物品的管理,设立专用仓库存放,在存放处外挂明显警示牌,对此类材料严格执行限额领料制度
（2）加强对电气焊的管理,操作人员必须持证上岗,严格按规程进行操作,并办理动火证
```

## latest_clean_scope_0135 (scope_collection)

**Query:** 列举《陕建丝路创发中心高支模专项施工方案》中“八、应急处置措施”部分的主要条目。

**Doc:** `real_69c60b33d4242eda8c47c959`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 181 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 13 | 6 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60b33d4242eda8c47c959:L456` [MISS] retrieved=False in_text=False
- `real_69c60b33d4242eda8c47c959:L457` [MISS] retrieved=False in_text=False
- `real_69c60b33d4242eda8c47c959:L460` [MISS] retrieved=False in_text=False
- `real_69c60b33d4242eda8c47c959:L461` [MISS] retrieved=False in_text=False
- `real_69c60b33d4242eda8c47c959:L463` [MISS] retrieved=False in_text=False
- `real_69c60b33d4242eda8c47c959:L464` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60b33d4242eda8c47c959:L452` scope=`None` depth=`0`
- reason: Collect the entire 'Emergency Response Measures' section to list all main items as requested.
- collect_section_ids: ['real_69c60b33d4242eda8c47c959:L452']
- collect added=3 hits=3 branch_selected=True collect_full=False
- legal_actions (53):
  - C1 | COLLECT | real_69c60b33d4242eda8c47c959:L452 | 八、应急处置措施 | score=0.0673
  - D1 | DISPATCH | real_69c60b33d4242eda8c47c959:L452 | 八、应急处置措施 | score=0.0673
  - C2 | COLLECT | real_69c60b33d4242eda8c47c959:L453 | 8.1应急领导小组及响应程序 | score=0.0667
  - D2 | DISPATCH | real_69c60b33d4242eda8c47c959:L453 | 8.1应急领导小组及响应程序 | score=0.0667
  - C3 | COLLECT | real_69c60b33d4242eda8c47c959:L454 | 8.1.1应急领导小组 | score=0.0667
  - D3 | DISPATCH | real_69c60b33d4242eda8c47c959:L454 | 8.1.1应急领导小组 | score=0.0667
  - C4 | COLLECT | real_69c60b33d4242eda8c47c959:L455 | （1）组长职责 | score=0.0667
  - D4 | DISPATCH | real_69c60b33d4242eda8c47c959:L455 | （1）组长职责 | score=0.0667
  - C5 | COLLECT | real_69c60b33d4242eda8c47c959:L456 | ①紧急情况发生后，负责紧急救援现场的总指挥工作，批准本预案的启动与终止。 | score=0.0457
  - C6 | COLLECT | real_69c60b33d4242eda8c47c959:L457 | ②统一部署应急预案的实施工作，并对应急工作中发生的争议采取紧急处理措施。 | score=0.0667
  - C7 | COLLECT | real_69c60b33d4242eda8c47c959:L458 | （2）副组长职责 | score=0.0567
  - D5 | DISPATCH | real_69c60b33d4242eda8c47c959:L458 | （2）副组长职责 | score=0.0567
  - C8 | COLLECT | real_69c60b33d4242eda8c47c959:L460 | ②对架体倒塌、物体打击、高处坠落事故进行评估，建立应急步骤，减少人员伤亡和财产损失。 | score=0.0504
  - C9 | COLLECT | real_69c60b33d4242eda8c47c959:L461 | ③设立与应急中心的通讯联络，为应急机构提供建议和信息。 | score=0.0567
  - C10 | COLLECT | real_69c60b33d4242eda8c47c959:L462 | （3）成员职责 | score=0.0478
  - D6 | DISPATCH | real_69c60b33d4242eda8c47c959:L462 | （3）成员职责 | score=0.0478
- projection_chars: 3407

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: The assembled evidence [G1] contains the full 'Emergency Response Measures' section with all required items.
- legal_actions (64):
  - C1 | COLLECT | real_69c60b33d4242eda8c47c959:L1 | 一、工程概况 | score=0.0380
  - D1 | DISPATCH | real_69c60b33d4242eda8c47c959:L1 | 一、工程概况 | score=0.0380
  - C2 | COLLECT | real_69c60b33d4242eda8c47c959:L2 | 1.1模板支撑体系工程概况和特点 | score=0.0380
  - D2 | DISPATCH | real_69c60b33d4242eda8c47c959:L2 | 1.1模板支撑体系工程概况和特点 | score=0.0380
  - C3 | COLLECT | real_69c60b33d4242eda8c47c959:L3 | 1.1.1工程基本情况 | score=0.0380
  - D3 | DISPATCH | real_69c60b33d4242eda8c47c959:L3 | 1.1.1工程基本情况 | score=0.0380
  - C4 | COLLECT | real_69c60b33d4242eda8c47c959:L4 | 陕建丝路创发中心位于西安能源金贸区，含3栋楼及地下车库。总建筑面积约29.47万㎡，最高楼211m。采用型钢混凝土框架-核心筒结构，桩筏基础，地上层数分别为43、42、20层，地下3层。 | score=0.0380
  - C5 | COLLECT | real_69c60b33d4242eda8c47c959:L38 | 四、施工工艺技术 | score=0.0430
  - D4 | DISPATCH | real_69c60b33d4242eda8c47c959:L38 | 四、施工工艺技术 | score=0.0430
  - C6 | COLLECT | real_69c60b33d4242eda8c47c959:L99 | 4.2工艺流程 | score=0.0430
  - D5 | DISPATCH | real_69c60b33d4242eda8c47c959:L99 | 4.2工艺流程 | score=0.0430
  - C7 | COLLECT | real_69c60b33d4242eda8c47c959:L116 | 4.2.2施工要点 | score=0.0430
  - D6 | DISPATCH | real_69c60b33d4242eda8c47c959:L116 | 4.2.2施工要点 | score=0.0430
  - C8 | COLLECT | real_69c60b33d4242eda8c47c959:L135 | （2）立杆及其他杆件 | score=0.0430
  - D7 | DISPATCH | real_69c60b33d4242eda8c47c959:L135 | （2）立杆及其他杆件 | score=0.0430
  - C9 | COLLECT | real_69c60b33d4242eda8c47c959:L142 | 5.支撑架立杆搭设位置应按专项施工方案放线确定。 | score=0.0430
- projection_chars: 3360

### Evidence text (new)

```
[E1]
[§ 八、应急处置措施]
  8.1应急领导小组及响应程序
  8.1.1应急领导小组
  （1）组长职责
  8.2应急事件及其应急措施
  8.2.1预防坍塌事故的技术措施
  （1）模板作业前，按设计单位要求，根据施工工艺、作业条件及周边环境，按照安全管理方案、应急预案内容做好施工前期准备，项目经理组织有关部门验收，经验收合格签字后，方可作业。
```

### Evidence text (old)

```
[E1]
八、应急处置措施

[E2]
8.1应急领导小组及响应程序
8.1.1应急领导小组
（1）组长职责

[E3]
8.2应急事件及其应急措施
8.2.1预防坍塌事故的技术措施
（1）模板作业前，按设计单位要求，根据施工工艺、作业条件及周边环境，按照安全管理方案、应急预案内容做好施工前期准备，项目经理组织有关部门验收，经验收合格签字后，方可作业。

[E4]
8.1.2应急响应程序
展示发现人、项目经理或现场负责人、下属单位工程部门经理、公司工程部和安全生产委员会在应急处理中的职责与流程，包括报告、判断、协助处理及后续评审修订等步骤。

[E5]
8.2.2预防高空坠落事故安全技术措施
（1）高大模板工程应按相关规定编制施工方案，经分公司总工、项目总工审批签字；高支模安装完毕后，需经安全部、质量部、技术部等有关部门验收，
验收合格后，方可绑扎钢筋等下道工序的施工作业。支、拆模板时应保证作业人员有可靠立足点，作业面应按规定设置安全防护设施。模板及其支撑体系的施工荷载应均匀堆置，并不得超过设计计算要求。

[E6]
8.2.3预防机械伤害事故安全技术措施
（1）遇有创伤性出血的伤员，
```

## latest_clean_scope_0139 (scope_collection)

**Query:** 列举《27-设计院-秦都卫生疾控中心项目关于优化策略的复盘报告》中“参与团队：主要设计团队为十一建设计院。 二、回顾目标 项目预期目标：”部分的主要条目。

**Doc:** `real_69c60b97d4242eda8c47c997`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 491 |
| gold_node_recall | 0.0 | 0.1667 |
| n_retrieved_nodes | 6 | 6 |
| trajectory_steps | n/a | 6 |

### Gold node hits (new)

- `real_69c60b97d4242eda8c47c997:L12` [HIT] retrieved=True in_text=False
- `real_69c60b97d4242eda8c47c997:L13` [MISS] retrieved=False in_text=False
- `real_69c60b97d4242eda8c47c997:L14` [MISS] retrieved=False in_text=False
- `real_69c60b97d4242eda8c47c997:L15` [MISS] retrieved=False in_text=False
- `real_69c60b97d4242eda8c47c997:L16` [MISS] retrieved=False in_text=False
- `real_69c60b97d4242eda8c47c997:L17` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C6` kind=`collect` section=`real_69c60b97d4242eda8c47c997:L7` scope=`None` depth=`0`
- reason: Collect section N6 containing the target team and project goals as requested.
- collect_section_ids: ['real_69c60b97d4242eda8c47c997:L7']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (41):
  - C1 | COLLECT | real_69c60b97d4242eda8c47c997:L1 | 设计理念： | score=0.0716
  - D1 | DISPATCH | real_69c60b97d4242eda8c47c997:L1 | 设计理念： | score=0.0716
  - C2 | COLLECT | real_69c60b97d4242eda8c47c997:L2 | 平疫结合：本项目可为医院建筑规划与设计提供一种平疫结合的新思路，提高传染病防控的有效性和效率，使疫情时期可以发挥自身的使命，在疫情结束后可满足社区医院使用要求，避免国家资源的浪费。 | score=0.0716
  - C3 | COLLECT | real_69c60b97d4242eda8c47c997:L3 | 以病人为中心：这是医疗建筑设计的核心理念，意味着建筑的布局、功能和设施都应以满足病人的需求为出发点。除了满足基本医疗需求外，医疗建筑还应注重人的心理和社会需求。例如，为病人和家属提供温馨、舒适的就诊和等候环境，为医护人员提供便捷的工作空间和休息设施，同时考虑到不同人群的特殊需求，如老年人、残障人士等。 | score=0.0572
  - C4 | COLLECT | real_69c60b97d4242eda8c47c997:L5 | 安全与卫生：医疗建筑的安全性和卫生性至关重要。建筑布局和流线设计应能够有效防止交叉感染，保障医护人员和病人的安全。同时，建筑结构和设施应符合相关的安全标准和卫生要求。 | score=0.0646
  - C5 | COLLECT | real_69c60b97d4242eda8c47c997:L6 | 现代感与功能性：医疗建筑应具有现代感和功能性，既要体现医院的形象和特色，又要满足医疗活动的实际需求。建筑设计应简洁大方、新颖独特，同时考虑到医院的功能需求和发展趋势，为未来的扩建和改造提供可能。 | score=0.0567
  - C6 | COLLECT | real_69c60b97d4242eda8c47c997:L7 | 参与团队：主要设计团队为十一建设计院。 二、回顾目标 项目预期目标： | score=0.0732
  - D2 | DISPATCH | real_69c60b97d4242eda8c47c997:L7 | 参与团队：主要设计团队为十一建设计院。 二、回顾目标 项目预期目标： | score=0.0732
  - C7 | COLLECT | real_69c60b97d4242eda8c47c997:L8 | 控制项目造价，从建筑、结构、设备等多方位角度降低工程造价，避免超概风险。建筑、结构、设备分别从不同方向和思路优化现有设计方案及图纸，建筑预期目标为6条优化策略、结构为4条策略、设备为4条策略。 | score=0.0732
  - C8 | COLLECT | real_69c60b97d4242eda8c47c997:L9 | 目标对应策略： | score=0.0611
  - D3 | DISPATCH | real_69c60b97d4242eda8c47c997:L9 | 目标对应策略： | score=0.0611
  - C9 | COLLECT | real_69c60b97d4242eda8c47c997:L10 | 1.控制造价各专业策略 | score=0.0611
  - C10 | COLLECT | real_69c60b97d4242eda8c47c997:L11 | 建筑专业： | score=0.0632
  - D4 | DISPATCH | real_69c60b97d4242eda8c47c997:L11 | 建筑专业： | score=0.0632
  - C11 | COLLECT | real_69c60b97d4242eda8c47c997:L12 | a.建筑通过提前与专家沟通，规避规划指标风险。 | score=0.0598
  - C12 | COLLECT | real_69c60b97d4242eda8c47c997:L13 | b.优化建筑层高，因该限高为规划限高不可调整，后经各专业商讨、精确测算，将三至七层住院用房高度降低100mm，八层住院高度增加200mm以保证横向排气管道；对病房走道各种管线精心排布，结构采用宽扁梁设计最终优化做到净高最优；住院采用分体空调，利用外立面造型巧妙布置外机位；利用一层5.4m层高手术室设于一层，净化机组同层布置；优化垂直交通问题，修改电梯尺寸。 | score=0.0632
- projection_chars: 3489

**Step 2** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60b97d4242eda8c47c997:L1` scope=`None` depth=`0`
- reason: The user query targets the 'Review Objectives' section which is under N1. Dispatching D1 will reveal the full content including the main items.
- collect_section_ids: ['real_69c60b97d4242eda8c47c997:L1']
- collect added=6 hits=6 branch_selected=True collect_full=False
- legal_actions (41):
  - C1 | COLLECT | real_69c60b97d4242eda8c47c997:L1 | 设计理念： | score=0.0716
  - D1 | DISPATCH | real_69c60b97d4242eda8c47c997:L1 | 设计理念： | score=0.0716
  - C2 | COLLECT | real_69c60b97d4242eda8c47c997:L2 | 平疫结合：本项目可为医院建筑规划与设计提供一种平疫结合的新思路，提高传染病防控的有效性和效率，使疫情时期可以发挥自身的使命，在疫情结束后可满足社区医院使用要求，避免国家资源的浪费。 | score=0.0716
  - C3 | COLLECT | real_69c60b97d4242eda8c47c997:L3 | 以病人为中心：这是医疗建筑设计的核心理念，意味着建筑的布局、功能和设施都应以满足病人的需求为出发点。除了满足基本医疗需求外，医疗建筑还应注重人的心理和社会需求。例如，为病人和家属提供温馨、舒适的就诊和等候环境，为医护人员提供便捷的工作空间和休息设施，同时考虑到不同人群的特殊需求，如老年人、残障人士等。 | score=0.0572
  - C4 | COLLECT | real_69c60b97d4242eda8c47c997:L5 | 安全与卫生：医疗建筑的安全性和卫生性至关重要。建筑布局和流线设计应能够有效防止交叉感染，保障医护人员和病人的安全。同时，建筑结构和设施应符合相关的安全标准和卫生要求。 | score=0.0646
  - C5 | COLLECT | real_69c60b97d4242eda8c47c997:L6 | 现代感与功能性：医疗建筑应具有现代感和功能性，既要体现医院的形象和特色，又要满足医疗活动的实际需求。建筑设计应简洁大方、新颖独特，同时考虑到医院的功能需求和发展趋势，为未来的扩建和改造提供可能。 | score=0.0567
  - C6 | COLLECT | real_69c60b97d4242eda8c47c997:L9 | 目标对应策略： | score=0.0611
  - D2 | DISPATCH | real_69c60b97d4242eda8c47c997:L9 | 目标对应策略： | score=0.0611
  - C7 | COLLECT | real_69c60b97d4242eda8c47c997:L10 | 1.控制造价各专业策略 | score=0.0611
  - C8 | COLLECT | real_69c60b97d4242eda8c47c997:L11 | 建筑专业： | score=0.0632
  - D3 | DISPATCH | real_69c60b97d4242eda8c47c997:L11 | 建筑专业： | score=0.0632
  - C9 | COLLECT | real_69c60b97d4242eda8c47c997:L12 | a.建筑通过提前与专家沟通，规避规划指标风险。 | score=0.0598
  - C10 | COLLECT | real_69c60b97d4242eda8c47c997:L13 | b.优化建筑层高，因该限高为规划限高不可调整，后经各专业商讨、精确测算，将三至七层住院用房高度降低100mm，八层住院高度增加200mm以保证横向排气管道；对病房走道各种管线精心排布，结构采用宽扁梁设计最终优化做到净高最优；住院采用分体空调，利用外立面造型巧妙布置外机位；利用一层5.4m层高手术室设于一层，净化机组同层布置；优化垂直交通问题，修改电梯尺寸。 | score=0.0632
  - C11 | COLLECT | real_69c60b97d4242eda8c47c997:L15 | d.将卫生间布局进行调整，满足卫生间洁具数量及规范尺寸要求的前提下优化卫生间，减少不必要的面积浪费，合理位置增设洁具间。 | score=0.0594
  - C12 | COLLECT | real_69c60b97d4242eda8c47c997:L17 | f.优化楼层功能布局，调整交通核，优化流线，简化人员流程。 | score=0.0539
  - C13 | COLLECT | real_69c60b97d4242eda8c47c997:L18 | g.外立面造型优化，墙身节点优化，外窗系统优化，保证外立面造型还原方案设计效果施工便捷高效。 | score=0.0534
- projection_chars: 3457

**Step 3** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60b97d4242eda8c47c997:L9` scope=`None` depth=`0`
- reason: Collect section C1 to retrieve the 'Review Goals' and 'Project Expected Goals' content.
- collect_section_ids: ['real_69c60b97d4242eda8c47c997:L9']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (43):
  - C1 | COLLECT | real_69c60b97d4242eda8c47c997:L9 | 目标对应策略： | score=0.0611
  - D1 | DISPATCH | real_69c60b97d4242eda8c47c997:L9 | 目标对应策略： | score=0.0611
  - C2 | COLLECT | real_69c60b97d4242eda8c47c997:L10 | 1.控制造价各专业策略 | score=0.0611
  - C3 | COLLECT | real_69c60b97d4242eda8c47c997:L11 | 建筑专业： | score=0.0632
  - D2 | DISPATCH | real_69c60b97d4242eda8c47c997:L11 | 建筑专业： | score=0.0632
  - C4 | COLLECT | real_69c60b97d4242eda8c47c997:L12 | a.建筑通过提前与专家沟通，规避规划指标风险。 | score=0.0598
  - C5 | COLLECT | real_69c60b97d4242eda8c47c997:L13 | b.优化建筑层高，因该限高为规划限高不可调整，后经各专业商讨、精确测算，将三至七层住院用房高度降低100mm，八层住院高度增加200mm以保证横向排气管道；对病房走道各种管线精心排布，结构采用宽扁梁设计最终优化做到净高最优；住院采用分体空调，利用外立面造型巧妙布置外机位；利用一层5.4m层高手术室设于一层，净化机组同层布置；优化垂直交通问题，修改电梯尺寸。 | score=0.0632
  - C6 | COLLECT | real_69c60b97d4242eda8c47c997:L14 | c.仔细核算消防用水量,调整原设计消防水池大小,避免后续返工。同时对汽车坡道不满足转弯半径要求的地方进行调整，避免后续图纸审查及消防、交通验收过程中的返工。 | score=0.0493
  - C7 | COLLECT | real_69c60b97d4242eda8c47c997:L15 | d.将卫生间布局进行调整，满足卫生间洁具数量及规范尺寸要求的前提下优化卫生间，减少不必要的面积浪费，合理位置增设洁具间。 | score=0.0594
  - C8 | COLLECT | real_69c60b97d4242eda8c47c997:L16 | e.对原有病房卫生间进行优化布置。在不影响卫生间布局及使用的前提下、在保证病房尺寸满足后续床位扩展情况下，减少卫生间及病房进深尺寸，走道尺寸扩大至3米宽。 | score=0.0533
  - C9 | COLLECT | real_69c60b97d4242eda8c47c997:L17 | f.优化楼层功能布局，调整交通核，优化流线，简化人员流程。 | score=0.0539
  - C10 | COLLECT | real_69c60b97d4242eda8c47c997:L18 | g.外立面造型优化，墙身节点优化，外窗系统优化，保证外立面造型还原方案设计效果施工便捷高效。 | score=0.0534
  - C11 | COLLECT | real_69c60b97d4242eda8c47c997:L19 | 结构专业： | score=0.0559
  - D3 | DISPATCH | real_69c60b97d4242eda8c47c997:L19 | 结构专业： | score=0.0559
  - C12 | COLLECT | real_69c60b97d4242eda8c47c997:L20 | 结构优化主体荷载，做到不缺不漏的同时尽可能采用轻质材料，如ALC内隔墙等手段，将荷载降低约1.5%左右。 | score=0.0546
  - C13 | COLLECT | real_69c60b97d4242eda8c47c997:L21 | 优化设计模型参数，充分考虑梁翼缘刚度、考虑弹性板、优化型钢截面等措施，约混凝土及钢含量。混凝土节约2.3%，钢筋节约1.8%。 | score=0.0559
- projection_chars: 3500

**Step 4** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60b97d4242eda8c47c997:L11` scope=`None` depth=`0`
- reason: Collecting Architecture section to find the main items under 'Review Objectives' as requested.
- collect_section_ids: ['real_69c60b97d4242eda8c47c997:L11']
- collect added=8 hits=8 branch_selected=True collect_full=False
- legal_actions (43):
  - C1 | COLLECT | real_69c60b97d4242eda8c47c997:L11 | 建筑专业： | score=0.0632
  - D1 | DISPATCH | real_69c60b97d4242eda8c47c997:L11 | 建筑专业： | score=0.0632
  - C2 | COLLECT | real_69c60b97d4242eda8c47c997:L12 | a.建筑通过提前与专家沟通，规避规划指标风险。 | score=0.0598
  - C3 | COLLECT | real_69c60b97d4242eda8c47c997:L13 | b.优化建筑层高，因该限高为规划限高不可调整，后经各专业商讨、精确测算，将三至七层住院用房高度降低100mm，八层住院高度增加200mm以保证横向排气管道；对病房走道各种管线精心排布，结构采用宽扁梁设计最终优化做到净高最优；住院采用分体空调，利用外立面造型巧妙布置外机位；利用一层5.4m层高手术室设于一层，净化机组同层布置；优化垂直交通问题，修改电梯尺寸。 | score=0.0632
  - C4 | COLLECT | real_69c60b97d4242eda8c47c997:L14 | c.仔细核算消防用水量,调整原设计消防水池大小,避免后续返工。同时对汽车坡道不满足转弯半径要求的地方进行调整，避免后续图纸审查及消防、交通验收过程中的返工。 | score=0.0493
  - C5 | COLLECT | real_69c60b97d4242eda8c47c997:L15 | d.将卫生间布局进行调整，满足卫生间洁具数量及规范尺寸要求的前提下优化卫生间，减少不必要的面积浪费，合理位置增设洁具间。 | score=0.0594
  - C6 | COLLECT | real_69c60b97d4242eda8c47c997:L16 | e.对原有病房卫生间进行优化布置。在不影响卫生间布局及使用的前提下、在保证病房尺寸满足后续床位扩展情况下，减少卫生间及病房进深尺寸，走道尺寸扩大至3米宽。 | score=0.0533
  - C7 | COLLECT | real_69c60b97d4242eda8c47c997:L17 | f.优化楼层功能布局，调整交通核，优化流线，简化人员流程。 | score=0.0539
  - C8 | COLLECT | real_69c60b97d4242eda8c47c997:L18 | g.外立面造型优化，墙身节点优化，外窗系统优化，保证外立面造型还原方案设计效果施工便捷高效。 | score=0.0534
  - C9 | COLLECT | real_69c60b97d4242eda8c47c997:L19 | 结构专业： | score=0.0559
  - D2 | DISPATCH | real_69c60b97d4242eda8c47c997:L19 | 结构专业： | score=0.0559
  - C10 | COLLECT | real_69c60b97d4242eda8c47c997:L20 | 结构优化主体荷载，做到不缺不漏的同时尽可能采用轻质材料，如ALC内隔墙等手段，将荷载降低约1.5%左右。 | score=0.0546
  - C11 | COLLECT | real_69c60b97d4242eda8c47c997:L21 | 优化设计模型参数，充分考虑梁翼缘刚度、考虑弹性板、优化型钢截面等措施，约混凝土及钢含量。混凝土节约2.3%，钢筋节约1.8%。 | score=0.0559
  - C12 | COLLECT | real_69c60b97d4242eda8c47c997:L23 | 对比基础方案，灌注桩、CFG素混凝土桩，选取经济合力方案，单基础部分节约近200万。 | score=0.0515
  - C13 | COLLECT | real_69c60b97d4242eda8c47c997:L25 | 水专业： | score=0.0511
  - D3 | DISPATCH | real_69c60b97d4242eda8c47c997:L25 | 水专业： | score=0.0511
- projection_chars: 3502

**Step 5** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60b97d4242eda8c47c997:L19` scope=`None` depth=`0`
- reason: Collect structural optimization details to complete the 'Review Objectives' section content.
- collect_section_ids: ['real_69c60b97d4242eda8c47c997:L19']
- collect added=6 hits=6 branch_selected=True collect_full=False
- legal_actions (44):
  - C1 | COLLECT | real_69c60b97d4242eda8c47c997:L19 | 结构专业： | score=0.0559
  - D1 | DISPATCH | real_69c60b97d4242eda8c47c997:L19 | 结构专业： | score=0.0559
  - C2 | COLLECT | real_69c60b97d4242eda8c47c997:L20 | 结构优化主体荷载，做到不缺不漏的同时尽可能采用轻质材料，如ALC内隔墙等手段，将荷载降低约1.5%左右。 | score=0.0546
  - C3 | COLLECT | real_69c60b97d4242eda8c47c997:L21 | 优化设计模型参数，充分考虑梁翼缘刚度、考虑弹性板、优化型钢截面等措施，约混凝土及钢含量。混凝土节约2.3%，钢筋节约1.8%。 | score=0.0559
  - C4 | COLLECT | real_69c60b97d4242eda8c47c997:L22 | 优化结构布置，根据装配式方案调整结构平面及模型，以方便装配式安装吊装。 | score=0.0473
  - C5 | COLLECT | real_69c60b97d4242eda8c47c997:L23 | 对比基础方案，灌注桩、CFG素混凝土桩，选取经济合力方案，单基础部分节约近200万。 | score=0.0515
  - C6 | COLLECT | real_69c60b97d4242eda8c47c997:L24 | 对比减隔震方案，最终选择隔震方案，控制隔震造价为单平米180元。 | score=0.0457
  - C7 | COLLECT | real_69c60b97d4242eda8c47c997:L25 | 水专业： | score=0.0511
  - D2 | DISPATCH | real_69c60b97d4242eda8c47c997:L25 | 水专业： | score=0.0511
  - C8 | COLLECT | real_69c60b97d4242eda8c47c997:L26 | a.消防水泵房内消防泵组可采用立式泵，相较卧式泵占地面积小节省土建成本，立式泵组顶处可设置吊钩极大的方便现场施工。 | score=0.0449
  - C9 | COLLECT | real_69c60b97d4242eda8c47c997:L28 | 暖通专业： | score=0.0481
  - C10 | COLLECT | real_69c60b97d4242eda8c47c997:L30 | b.防排烟管道风速控制在18m/s，节省成本；排烟风口采用单层百叶风口，降低成本。 | score=0.0448
  - C11 | COLLECT | real_69c60b97d4242eda8c47c997:L31 | 电气专业； | score=0.0476
  - C12 | COLLECT | real_69c60b97d4242eda8c47c997:L32 | 配电干线采用放射式和树干式结合的方式，重要位置负荷均采用放射式，提高供电可靠性。树干配电方式，不采用预分支电缆及T接箱接线，而采用集成T接端子，便于施工安装，节省成本。 | score=0.0501
  - C13 | COLLECT | real_69c60b97d4242eda8c47c997:L33 | 通过更为精准的末端用电负荷统计与计算，供电电缆及导体截面积合理选择，不过度保守而选择截面积更大一级线缆，而造成资源浪费和成本的提升。 | score=0.0511
  - C14 | COLLECT | real_69c60b97d4242eda8c47c997:L34 | 三、评估结果在采取多级措施后，效果较为明显。 | score=0.0485
- projection_chars: 3343

**Step 6** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains the requested section '参与团队' and '回顾目标' with main items. No other sections needed.
- legal_actions (39):
  - C1 | COLLECT | real_69c60b97d4242eda8c47c997:L25 | 水专业： | score=0.0511
  - D1 | DISPATCH | real_69c60b97d4242eda8c47c997:L25 | 水专业： | score=0.0511
  - C2 | COLLECT | real_69c60b97d4242eda8c47c997:L26 | a.消防水泵房内消防泵组可采用立式泵，相较卧式泵占地面积小节省土建成本，立式泵组顶处可设置吊钩极大的方便现场施工。 | score=0.0449
  - C3 | COLLECT | real_69c60b97d4242eda8c47c997:L27 | b.室内消火栓系统除消防泵进出水管、人防等位置设置明杆闸阀外，其他均可采用普通蝶阀，即方便现场安装又节省造价 | score=0.0431
  - C4 | COLLECT | real_69c60b97d4242eda8c47c997:L28 | 暖通专业： | score=0.0481
  - C5 | COLLECT | real_69c60b97d4242eda8c47c997:L29 | a.1-2层空调采用多联机空调系统，控制灵活。 | score=0.0446
  - C6 | COLLECT | real_69c60b97d4242eda8c47c997:L30 | b.防排烟管道风速控制在18m/s，节省成本；排烟风口采用单层百叶风口，降低成本。 | score=0.0448
  - C7 | COLLECT | real_69c60b97d4242eda8c47c997:L31 | 电气专业； | score=0.0476
  - C8 | COLLECT | real_69c60b97d4242eda8c47c997:L32 | 配电干线采用放射式和树干式结合的方式，重要位置负荷均采用放射式，提高供电可靠性。树干配电方式，不采用预分支电缆及T接箱接线，而采用集成T接端子，便于施工安装，节省成本。 | score=0.0501
  - C9 | COLLECT | real_69c60b97d4242eda8c47c997:L33 | 通过更为精准的末端用电负荷统计与计算，供电电缆及导体截面积合理选择，不过度保守而选择截面积更大一级线缆，而造成资源浪费和成本的提升。 | score=0.0511
  - C10 | COLLECT | real_69c60b97d4242eda8c47c997:L34 | 三、评估结果在采取多级措施后，效果较为明显。 | score=0.0485
  - C11 | COLLECT | real_69c60b97d4242eda8c47c997:L35 | 项目的亮点： | score=0.0608
  - D2 | DISPATCH | real_69c60b97d4242eda8c47c997:L35 | 项目的亮点： | score=0.0608
  - C12 | COLLECT | real_69c60b97d4242eda8c47c997:L36 | 建筑、设备专业考虑多项功能转换。 | score=0.0543
  - C13 | COLLECT | real_69c60b97d4242eda8c47c997:L37 | 总体含结构经济指标控制较好，在本项目为中震且需要考虑不利地段的情况下，整体项目含钢量控制在83kg/m2，混凝土含量为0.45m3/m2。 | score=0.0608
  - C14 | COLLECT | real_69c60b97d4242eda8c47c997:L38 | 项目不足： | score=0.0487
- projection_chars: 2995

### Evidence text (new)

```
[E1]
[§ 参与团队：主要设计团队为十一建设计院。
二、回顾目标
项目预期目标：]
二、回顾目标
项目预期目标：]
控制项目造价，从建筑、结构、设备等多方位角度降低工程造价，避免超概风险。建筑、结构、设备分别从不同方向和思路优化现有设计方案及图纸，建筑预期目标为6条优化策略、结构为4条策略、设备为4条策略。

[E2]
[§ 设计理念：]
  平疫结合：本项目可为医院建筑规划与设计提供一种平疫结合的新思路，提高传染病防控的有效性和效率，使疫情时期可以发挥自身的使命，在疫情结束后可满足社区医院使用要求，避免国家资源的浪费。
  安全与卫生：医疗建筑的安全性和卫生性至关重要。建筑布局和流线设计应能够有效防止交叉感染，保障医护人员和病人的安全。同时，建筑结构和设施应符合相关的安全标准和卫生要求。
  现代感与功能性：医疗建筑应具有现代感和功能性，既要体现医院的形象和特色，又要满足医疗活动的实际需求。建筑设计应简洁大方、新颖独特，同时考虑到医院的功能需求和发展趋势，为未来的扩建和改造提供可能。

[E3]
[§ 建筑专业：]
a.建筑通过提前与专家沟通，规避规划指标风险。
```

### Evidence text (old)

```
[E1]
设计理念：

[E2]
平疫结合：本项目可为医院建筑规划与设计提供一种平疫结合的新思路，提高传染病防控的有效性和效率，使疫情时期可以发挥自身的使命，在疫情结束后可满足社区医院使用要求，避免国家资源的浪费。

[E3]
以病人为中心：这是医疗建筑设计的核心理念，意味着建筑的布局、功能和设施都应以满足病人的需求为出发点。除了满足基本医疗需求外，医疗建筑还应注重人的心理和社会需求。例如，为病人和家属提供温馨、舒适的就诊和等候环境，为医护人员提供便捷的工作空间和休息设施，同时考虑到不同人群的特殊需求，如老年人、残障人士等。

[E4]
绿色环保与可持续发展：医疗建筑应注重节能、环保和可持续发展。采用高效节能的建筑材料和设备，合理利用自然光和通风，采用装配式建筑以减少能源消耗和环境污染，为患者和医护人员提供宜人的室内外环境。

[E5]
安全与卫生：医疗建筑的安全性和卫生性至关重要。建筑布局和流线设计应能够有效防止交叉感染，保障医护人员和病人的安全。同时，建筑结构和设施应符合相关的安全标准和卫生要求。

[E6]
现代感与功能性：医疗建筑应具有现代感和功能性，既要体现医院的形象和特色，
```

## real_69c6ef4e4cca74801cb63bc6_scope_collection_auto_0061 (scope_collection)

**Query:** 列出文档中提到的所有竖向钢立柱安装的具体步骤及技术要求。

**Doc:** `real_69c6ef4e4cca74801cb63bc6`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 494 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 8 | 13 |
| trajectory_steps | n/a | 3 |

### Gold node hits (new)

- `real_69c6ef4e4cca74801cb63bc6:L79` [MISS] retrieved=False in_text=False
- `real_69c6ef4e4cca74801cb63bc6:L80` [MISS] retrieved=False in_text=False
- `real_69c6ef4e4cca74801cb63bc6:L82` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C15` kind=`collect` section=`real_69c6ef4e4cca74801cb63bc6:L62` scope=`None` depth=`0`
- reason: Collecting specific steps and technical requirements for vertical steel column installation found in sections C15-C18.
- collect_section_ids: ['real_69c6ef4e4cca74801cb63bc6:L62', 'real_69c6ef4e4cca74801cb63bc6:L63', 'real_69c6ef4e4cca74801cb63bc6:L64', 'real_69c6ef4e4cca74801cb63bc6:L66']
- collect added=4 hits=4 branch_selected=True collect_full=True
- legal_actions (46):
  - C1 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L12 | 1.前言 | score=0.0633
  - D1 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L12 | 1.前言 | score=0.0633
  - C2 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L13 | 非承重清水烧结陶土砖镂空幕墙体系中镂空幕墙对整体性、牢固性 及测量精度要求特别高。实际施工中往往采用单一的结构体系会造成施 工困难、日常维护局限性大、对施工人员技术要求高。陕西建工沣西建 设有限公司依据多年对此类工程的施工，并总结形成了非承重清水烧结 陶土砖镂空幕墙施工方法。在多个项目得到成功应用的同时，还获得国 家专利1 项《一种外墙砌筑镂空陶土砖的结构》专利申请号： | score=0.0633
  - C3 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L15 | 2.工法特点 | score=0.0585
  - D2 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L15 | 2.工法特点 | score=0.0585
  - C4 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L16 | 2.1 工厂化加工 | score=0.0585
  - D3 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L16 | 2.1 工厂化加工 | score=0.0585
  - C5 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L17 | 陶土砖采用先进的工艺设备，采用流水线加工，使得每一块具有精 准的外形，降低人工损耗，降低对工人的技术要求。 2.2 构造方式的独特性 | score=0.0585
  - C6 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L26 | 4.工艺原理 | score=0.0661
  - D4 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L26 | 4.工艺原理 | score=0.0661
  - C7 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L27 | 采用构件式幕墙系统，根据镂空幕墙分隔将龙骨与主体结构上的连 接件、清水陶土砖的砌筑单元构件、铝板等进行连接固定，形成安全可 靠的外墙装饰和围护结构。纵、横主龙骨采用应力消减支座进行连接， 陶土砖有自带的空腔，其内设有锚固钢筋，并形成砌筑单元构件，在利 用孔内竖向钢筋固定在龙骨上且竖向需设有分封胶条。通过铝板与固定 角钢连接，保证幕墙与建筑物交界处的封口闭合。 | score=0.0661
  - C8 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L28 | 5.施工工艺流程及操作要点 | score=0.0738
  - D5 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L28 | 5.施工工艺流程及操作要点 | score=0.0738
  - C9 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L32 | 5.2 操作要点 | score=0.0738
  - D6 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L32 | 5.2 操作要点 | score=0.0738
  - C10 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L41 | 图 **5-2-1-2-2 BIM** 对镂空部分进行建模 | score=0.0599
- projection_chars: 3606

**Step 2** `nav_collect`  id=`C10` kind=`collect` section=`real_69c6ef4e4cca74801cb63bc6:L32` scope=`None` depth=`0`
- reason: Collect section 5.2 Operation Points to find all vertical steel column installation steps and requirements.
- collect_section_ids: ['real_69c6ef4e4cca74801cb63bc6:L32']
- collect added=64 hits=64 branch_selected=True collect_full=False
- legal_actions (48):
  - C1 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L12 | 1.前言 | score=0.0633
  - D1 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L12 | 1.前言 | score=0.0633
  - C2 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L13 | 非承重清水烧结陶土砖镂空幕墙体系中镂空幕墙对整体性、牢固性 及测量精度要求特别高。实际施工中往往采用单一的结构体系会造成施 工困难、日常维护局限性大、对施工人员技术要求高。陕西建工沣西建 设有限公司依据多年对此类工程的施工，并总结形成了非承重清水烧结 陶土砖镂空幕墙施工方法。在多个项目得到成功应用的同时，还获得国 家专利1 项《一种外墙砌筑镂空陶土砖的结构》专利申请号： | score=0.0633
  - C3 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L15 | 2.工法特点 | score=0.0585
  - D2 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L15 | 2.工法特点 | score=0.0585
  - C4 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L16 | 2.1 工厂化加工 | score=0.0585
  - D3 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L16 | 2.1 工厂化加工 | score=0.0585
  - C5 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L17 | 陶土砖采用先进的工艺设备，采用流水线加工，使得每一块具有精 准的外形，降低人工损耗，降低对工人的技术要求。 2.2 构造方式的独特性 | score=0.0585
  - C6 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L18 | 外叶砌体墙采用清水陶土砖砌筑，内叶墙根据工程的位置不同采用 混凝土实体墙或加气混凝土砌块砌筑。在内叶墙的外侧有连续的防水层， 外叶墙作为装饰和雨屏墙（采用自保温砌体只在混凝土构件上按照图纸 要求做保温）。 | score=0.0524
  - C7 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L26 | 4.工艺原理 | score=0.0661
  - D4 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L26 | 4.工艺原理 | score=0.0661
  - C8 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L27 | 采用构件式幕墙系统，根据镂空幕墙分隔将龙骨与主体结构上的连 接件、清水陶土砖的砌筑单元构件、铝板等进行连接固定，形成安全可 靠的外墙装饰和围护结构。纵、横主龙骨采用应力消减支座进行连接， 陶土砖有自带的空腔，其内设有锚固钢筋，并形成砌筑单元构件，在利 用孔内竖向钢筋固定在龙骨上且竖向需设有分封胶条。通过铝板与固定 角钢连接，保证幕墙与建筑物交界处的封口闭合。 | score=0.0661
  - C9 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L28 | 5.施工工艺流程及操作要点 | score=0.0738
  - D5 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L28 | 5.施工工艺流程及操作要点 | score=0.0738
  - C10 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L32 | 5.2 操作要点 | score=0.0738
  - D6 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L32 | 5.2 操作要点 | score=0.0738
- projection_chars: 3600

**Step 3** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains the specific steps and technical requirements for vertical steel column installation.
- legal_actions (50):
  - C1 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L12 | 1.前言 | score=0.0633
  - D1 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L12 | 1.前言 | score=0.0633
  - C2 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L13 | 非承重清水烧结陶土砖镂空幕墙体系中镂空幕墙对整体性、牢固性 及测量精度要求特别高。实际施工中往往采用单一的结构体系会造成施 工困难、日常维护局限性大、对施工人员技术要求高。陕西建工沣西建 设有限公司依据多年对此类工程的施工，并总结形成了非承重清水烧结 陶土砖镂空幕墙施工方法。在多个项目得到成功应用的同时，还获得国 家专利1 项《一种外墙砌筑镂空陶土砖的结构》专利申请号： | score=0.0633
  - C3 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L14 | 202021699897.9；2021 年3 月份《陕西省住房和城乡建设厅关于下达 2021 年度工程建设标准制定计划的通知》且同意立项，进行陕西省地 方标准的编制。在此基础上，经过进一步提炼，形成了《非承重清水烧 结陶土砖镂空幕墙施工工法》。 | score=0.0469
  - C4 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L15 | 2.工法特点 | score=0.0585
  - D2 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L15 | 2.工法特点 | score=0.0585
  - C5 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L16 | 2.1 工厂化加工 | score=0.0585
  - D3 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L16 | 2.1 工厂化加工 | score=0.0585
  - C6 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L17 | 陶土砖采用先进的工艺设备，采用流水线加工，使得每一块具有精 准的外形，降低人工损耗，降低对工人的技术要求。 2.2 构造方式的独特性 | score=0.0585
  - C7 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L18 | 外叶砌体墙采用清水陶土砖砌筑，内叶墙根据工程的位置不同采用 混凝土实体墙或加气混凝土砌块砌筑。在内叶墙的外侧有连续的防水层， 外叶墙作为装饰和雨屏墙（采用自保温砌体只在混凝土构件上按照图纸 要求做保温）。 | score=0.0524
  - C8 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L21 | 2.3 工艺简单、施工方便 | score=0.0408
  - D4 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L21 | 2.3 工艺简单、施工方便 | score=0.0408
  - C9 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L22 | 镂空陶土砖幕墙施工采用应力消减支座与竖向龙骨进行可靠连接， 从而降低应力变形产生的位移量。 | score=0.0408
  - C10 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L23 | 3.适用范围 | score=0.0386
  - D5 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L23 | 3.适用范围 | score=0.0386
  - C11 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L24 | 本工法适用于50m 以下的住宅、纪念馆、中、小学校建筑的外墙饰 | score=0.0386
- projection_chars: 3409

### Evidence text (new)

```
[E1]
[§ 图 **5-2-3-3** 现场预埋件拉拔试验]
  - 2、转接件的安装
  - （1）、根据控制线确定转接件位置，施工时将其焊在预埋件上
  - ，然后对其三维方向尺寸进行复核（垂直误差2mm、水平误差2mm、 进深误差3mm）在复核无误后，进行焊接固定。
  图 **5-2-3-4** 现场预埋件防腐处理
  - 5.2.4 竖向龙骨安装与调整
  （1）、竖向钢立柱安装时，应先将立柱与转接件连接，立柱应带 有活动接头，接头通过芯套连接上下柱，芯套与立柱紧密相接。上 下柱用螺栓固定，上下柱之间留有20mm 的空隙。
  图 **5-2-4-1** 立柱与芯柱连接 （2）、通过镀锌螺栓将竖向龙骨与转接件链接，根据提前策划的 基准线，对竖向龙骨进行调整固定，确保在镂空部位龙骨不外漏， 并使其处于最佳受力状态。
  图 **5-2-4-2** 现场立柱与转接件连接
  - （3）、用多功能水平尺或经纬仪校正钢龙骨的垂直度，必要时将 螺栓松开调整，如仍调整不好必须重新安装。

[E2]
[§ 5.2.7 铝板安装]
图 **5-2-7-1** 铝板固定龙骨位置
```

### Evidence text (old)

```
[E1]
[§ 5.施工工艺流程及操作要点 / 5.2 操作要点 / 图 **5-2-3-3** 现场预埋件拉拔试验]
（1）、竖向钢立柱安装时，应先将立柱与转接件连接，立柱应带 有活动接头，接头通过芯套连接上下柱，芯套与立柱紧密相接。上 下柱用螺栓固定，上下柱之间留有20mm 的空隙。

[E2]
[§ 5.施工工艺流程及操作要点 / 5.2 操作要点 / 5.2.5 横向龙骨（钢托板）安装与调整]
（1）、横向龙骨（钢托板）安装时，应先在立柱上准确标出横梁 的精确位置，钻出孔位，在角钢上打出连接点的孔位，用角码及螺 栓将角钢横梁与立柱连接在一起，并紧固螺栓。

[E3]
[§ 5.施工工艺流程及操作要点 / 5.2 操作要点 / 图 **5-2-3-3** 现场预埋件拉拔试验]
- 5.2.4 竖向龙骨安装与调整

[E4]
[§ 5.施工工艺流程及操作要点 / 5.2 操作要点 / 5.2.5 横向龙骨（钢托板）安装与调整]
图 **5-2-5-1** 横向龙骨（钢托板）安装 **CAD** 优化图

[E5]
[§ 5.施工工艺流程及操作要点 / 5.2 操作要点]
图 **5
```

## real_69c6ef4e4cca74801cb63bc6_scope_collection_auto_0062 (scope_collection)

**Query:** 列举横向龙骨（钢托板）安装与调整过程中的所有关键操作要点。

**Doc:** `real_69c6ef4e4cca74801cb63bc6`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.6667 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 443 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 8 | 9 |
| trajectory_steps | n/a | 3 |

### Gold node hits (new)

- `real_69c6ef4e4cca74801cb63bc6:L86` [MISS] retrieved=False in_text=False
- `real_69c6ef4e4cca74801cb63bc6:L90` [MISS] retrieved=False in_text=False
- `real_69c6ef4e4cca74801cb63bc6:L92` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C14` kind=`collect` section=`real_69c6ef4e4cca74801cb63bc6:L68` scope=`None` depth=`0`
- reason: Section 5.2.5 specifically covers horizontal keel (steel support plate) installation and adjustment.
- collect_section_ids: ['real_69c6ef4e4cca74801cb63bc6:L68']
- collect added=2 hits=2 branch_selected=True collect_full=True
- legal_actions (45):
  - C1 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L26 | 4.工艺原理 | score=0.0641
  - D1 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L26 | 4.工艺原理 | score=0.0641
  - C2 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L27 | 采用构件式幕墙系统，根据镂空幕墙分隔将龙骨与主体结构上的连 接件、清水陶土砖的砌筑单元构件、铝板等进行连接固定，形成安全可 靠的外墙装饰和围护结构。纵、横主龙骨采用应力消减支座进行连接， 陶土砖有自带的空腔，其内设有锚固钢筋，并形成砌筑单元构件，在利 用孔内竖向钢筋固定在龙骨上且竖向需设有分封胶条。通过铝板与固定 角钢连接，保证幕墙与建筑物交界处的封口闭合。 | score=0.0641
  - C3 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L28 | 5.施工工艺流程及操作要点 | score=0.0732
  - D2 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L28 | 5.施工工艺流程及操作要点 | score=0.0732
  - C4 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L32 | 5.2 操作要点 | score=0.0732
  - D3 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L32 | 5.2 操作要点 | score=0.0732
  - C5 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L50 | 图 **5-2-2-1-1** 立面马牙槎垂直变形缝示意图 | score=0.0540
  - D4 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L50 | 图 **5-2-2-1-1** 立面马牙槎垂直变形缝示意图 | score=0.0540
  - C6 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L52 | - 5.2.3 安装后置埋件与转接件 | score=0.0540
  - C7 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L57 | 图 **5-2-3-3** 现场预埋件拉拔试验 | score=0.0692
  - D5 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L57 | 图 **5-2-3-3** 现场预埋件拉拔试验 | score=0.0692
  - C8 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L58 | - 2、转接件的安装 | score=0.0541
  - C9 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L62 | - 5.2.4 竖向龙骨安装与调整 | score=0.0692
  - C10 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L63 | （1）、竖向钢立柱安装时，应先将立柱与转接件连接，立柱应带 有活动接头，接头通过芯套连接上下柱，芯套与立柱紧密相接。上 下柱用螺栓固定，上下柱之间留有20mm 的空隙。 | score=0.0644
  - C11 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L64 | 图 **5-2-4-1** 立柱与芯柱连接 （2）、通过镀锌螺栓将竖向龙骨与转接件链接，根据提前策划的 基准线，对竖向龙骨进行调整固定，确保在镂空部位龙骨不外漏， 并使其处于最佳受力状态。 | score=0.0662
- projection_chars: 3496

**Step 2** `nav_collect`  id=`C15` kind=`collect` section=`real_69c6ef4e4cca74801cb63bc6:L71` scope=`None` depth=`0`
- reason: Collect section 5.2.5 containing all key points for horizontal keel (steel support plate) installation and adjustment.
- collect_section_ids: ['real_69c6ef4e4cca74801cb63bc6:L71']
- collect added=5 hits=5 branch_selected=True collect_full=True
- legal_actions (45):
  - C1 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L15 | 2.工法特点 | score=0.0520
  - D1 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L15 | 2.工法特点 | score=0.0520
  - C2 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L21 | 2.3 工艺简单、施工方便 | score=0.0520
  - D2 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L21 | 2.3 工艺简单、施工方便 | score=0.0520
  - C3 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L22 | 镂空陶土砖幕墙施工采用应力消减支座与竖向龙骨进行可靠连接， 从而降低应力变形产生的位移量。 | score=0.0520
  - C4 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L26 | 4.工艺原理 | score=0.0641
  - D3 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L26 | 4.工艺原理 | score=0.0641
  - C5 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L27 | 采用构件式幕墙系统，根据镂空幕墙分隔将龙骨与主体结构上的连 接件、清水陶土砖的砌筑单元构件、铝板等进行连接固定，形成安全可 靠的外墙装饰和围护结构。纵、横主龙骨采用应力消减支座进行连接， 陶土砖有自带的空腔，其内设有锚固钢筋，并形成砌筑单元构件，在利 用孔内竖向钢筋固定在龙骨上且竖向需设有分封胶条。通过铝板与固定 角钢连接，保证幕墙与建筑物交界处的封口闭合。 | score=0.0641
  - D4 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L28 | 5.施工工艺流程及操作要点 | score=0.0732
  - D5 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L32 | 5.2 操作要点 | score=0.0732
  - C6 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L50 | 图 **5-2-2-1-1** 立面马牙槎垂直变形缝示意图 | score=0.0540
  - D6 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L50 | 图 **5-2-2-1-1** 立面马牙槎垂直变形缝示意图 | score=0.0540
  - C7 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L52 | - 5.2.3 安装后置埋件与转接件 | score=0.0540
  - C8 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L57 | 图 **5-2-3-3** 现场预埋件拉拔试验 | score=0.0692
  - D7 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L57 | 图 **5-2-3-3** 现场预埋件拉拔试验 | score=0.0692
  - C9 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L58 | - 2、转接件的安装 | score=0.0541
- projection_chars: 3410

**Step 3** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Assembled evidence G1 and G2 fully cover the key operation points for horizontal keel installation and adjustment.
- legal_actions (44):
  - C1 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L15 | 2.工法特点 | score=0.0520
  - D1 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L15 | 2.工法特点 | score=0.0520
  - C2 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L21 | 2.3 工艺简单、施工方便 | score=0.0520
  - D2 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L21 | 2.3 工艺简单、施工方便 | score=0.0520
  - C3 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L22 | 镂空陶土砖幕墙施工采用应力消减支座与竖向龙骨进行可靠连接， 从而降低应力变形产生的位移量。 | score=0.0520
  - C4 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L26 | 4.工艺原理 | score=0.0641
  - D3 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L26 | 4.工艺原理 | score=0.0641
  - C5 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L27 | 采用构件式幕墙系统，根据镂空幕墙分隔将龙骨与主体结构上的连 接件、清水陶土砖的砌筑单元构件、铝板等进行连接固定，形成安全可 靠的外墙装饰和围护结构。纵、横主龙骨采用应力消减支座进行连接， 陶土砖有自带的空腔，其内设有锚固钢筋，并形成砌筑单元构件，在利 用孔内竖向钢筋固定在龙骨上且竖向需设有分封胶条。通过铝板与固定 角钢连接，保证幕墙与建筑物交界处的封口闭合。 | score=0.0641
  - D4 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L28 | 5.施工工艺流程及操作要点 | score=0.0732
  - D5 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L32 | 5.2 操作要点 | score=0.0732
  - C6 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L50 | 图 **5-2-2-1-1** 立面马牙槎垂直变形缝示意图 | score=0.0540
  - D6 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L50 | 图 **5-2-2-1-1** 立面马牙槎垂直变形缝示意图 | score=0.0540
  - C7 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L52 | - 5.2.3 安装后置埋件与转接件 | score=0.0540
  - C8 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L53 | - 1、安装后置埋件 | score=0.0492
  - C9 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L55 | 度与螺栓的紧固程度直接影响幕墙的安全； | score=0.0491
  - C10 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L57 | 图 **5-2-3-3** 现场预埋件拉拔试验 | score=0.0692
- projection_chars: 3433

### Evidence text (new)

```
[E1]
[§ 5.2.5 横向龙骨（钢托板）安装与调整]
  （1）、横向龙骨（钢托板）安装时，应先在立柱上准确标出横梁 的精确位置，钻出孔位，在角钢上打出连接点的孔位，用角码及螺 栓将角钢横梁与立柱连接在一起，并紧固螺栓。
  图 **5-2-5-1** 横向龙骨（钢托板）安装 **CAD** 优化图

[E2]
[§ 图 **5-2-5-2** 横向龙骨（钢托板）现场安装图]
  - （2）、用水准仪校正横梁的标高，保证立柱与横梁垂直，误差在 允许范围内，校正无误后，横梁与立柱采用焊接，焊接时要一头焊 接一头螺栓连接,形成应力消减支座。
  - 图 **5-2-5-3** 横向龙骨（钢托板）连接头策划及实施
  - （3）、 横向龙骨（钢托板）应该随陶土砖的砌筑进度同步安装， 不可超前施工 。
  - （4）、层间防火隔离带安装
  按照设计图纸要求，防火岩棉厚度为200mm，防火岩棉容重为 120Kg/m3，防火时间2h；防火岩棉均须单面锡箔，拼接处丁基胶带 密封。
```

### Evidence text (old)

```
[E1]
[§ 5.施工工艺流程及操作要点 / 5.2 操作要点 / 5.2.5 横向龙骨（钢托板）安装与调整]
（1）、横向龙骨（钢托板）安装时，应先在立柱上准确标出横梁 的精确位置，钻出孔位，在角钢上打出连接点的孔位，用角码及螺 栓将角钢横梁与立柱连接在一起，并紧固螺栓。

[E2]
[§ 5.施工工艺流程及操作要点 / 5.2 操作要点 / 5.2.5 横向龙骨（钢托板）安装与调整]
图 **5-2-5-1** 横向龙骨（钢托板）安装 **CAD** 优化图

[E3]
[§ 5.施工工艺流程及操作要点 / 5.2 操作要点 / 图 **5-2-5-2** 横向龙骨（钢托板）现场安装图]
- 图 **5-2-5-3** 横向龙骨（钢托板）连接头策划及实施

[E4]
[§ 5.施工工艺流程及操作要点 / 5.2 操作要点 / 图 **5-2-5-2** 横向龙骨（钢托板）现场安装图]
- （3）、 横向龙骨（钢托板）应该随陶土砖的砌筑进度同步安装， 不可超前施工 。

[E5]
[§ 5.施工工艺流程及操作要点 / 5.2 操作要点 / 图 **5-2-5-2** 横向龙骨（钢托
```

## real_69c6ef4e4cca74801cb63bc6_scope_collection_auto_0063 (scope_collection)

**Query:** 列出摞底排砖、挂线砌筑阶段涉及的所有具体施工工艺要求。

**Doc:** `real_69c6ef4e4cca74801cb63bc6`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.1429 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 489 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 6 | 7 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c6ef4e4cca74801cb63bc6:L96` [MISS] retrieved=False in_text=False
- `real_69c6ef4e4cca74801cb63bc6:L100` [MISS] retrieved=False in_text=False
- `real_69c6ef4e4cca74801cb63bc6:L102` [MISS] retrieved=False in_text=False
- `real_69c6ef4e4cca74801cb63bc6:L105` [MISS] retrieved=False in_text=False
- `real_69c6ef4e4cca74801cb63bc6:L107` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C18` kind=`collect` section=`real_69c6ef4e4cca74801cb63bc6:L77` scope=`None` depth=`0`
- reason: Section 5.2.6 covers stacking, lining, and masonry requirements as requested.
- collect_section_ids: ['real_69c6ef4e4cca74801cb63bc6:L77']
- collect added=15 hits=15 branch_selected=True collect_full=True
- legal_actions (44):
  - C1 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L12 | 1.前言 | score=0.0587
  - D1 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L12 | 1.前言 | score=0.0587
  - C2 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L13 | 非承重清水烧结陶土砖镂空幕墙体系中镂空幕墙对整体性、牢固性 及测量精度要求特别高。实际施工中往往采用单一的结构体系会造成施 工困难、日常维护局限性大、对施工人员技术要求高。陕西建工沣西建 设有限公司依据多年对此类工程的施工，并总结形成了非承重清水烧结 陶土砖镂空幕墙施工方法。在多个项目得到成功应用的同时，还获得国 家专利1 项《一种外墙砌筑镂空陶土砖的结构》专利申请号： | score=0.0587
  - C3 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L15 | 2.工法特点 | score=0.0637
  - D2 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L15 | 2.工法特点 | score=0.0637
  - C4 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L16 | 2.1 工厂化加工 | score=0.0637
  - D3 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L16 | 2.1 工厂化加工 | score=0.0637
  - C5 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L17 | 陶土砖采用先进的工艺设备，采用流水线加工，使得每一块具有精 准的外形，降低人工损耗，降低对工人的技术要求。 2.2 构造方式的独特性 | score=0.0637
  - C6 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L18 | 外叶砌体墙采用清水陶土砖砌筑，内叶墙根据工程的位置不同采用 混凝土实体墙或加气混凝土砌块砌筑。在内叶墙的外侧有连续的防水层， 外叶墙作为装饰和雨屏墙（采用自保温砌体只在混凝土构件上按照图纸 要求做保温）。 | score=0.0614
  - C7 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L26 | 4.工艺原理 | score=0.0561
  - D4 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L26 | 4.工艺原理 | score=0.0561
  - C8 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L27 | 采用构件式幕墙系统，根据镂空幕墙分隔将龙骨与主体结构上的连 接件、清水陶土砖的砌筑单元构件、铝板等进行连接固定，形成安全可 靠的外墙装饰和围护结构。纵、横主龙骨采用应力消减支座进行连接， 陶土砖有自带的空腔，其内设有锚固钢筋，并形成砌筑单元构件，在利 用孔内竖向钢筋固定在龙骨上且竖向需设有分封胶条。通过铝板与固定 角钢连接，保证幕墙与建筑物交界处的封口闭合。 | score=0.0561
  - C9 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L28 | 5.施工工艺流程及操作要点 | score=0.0698
  - D5 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L28 | 5.施工工艺流程及操作要点 | score=0.0698
  - C10 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L30 | 图 **5-1** 深化设计工艺流程图 | score=0.0605
  - D6 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L30 | 图 **5-1** 深化设计工艺流程图 | score=0.0605
- projection_chars: 3625

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Assembled evidence G1 fully covers the specific construction requirements for stacking bricks and string masonry.
- legal_actions (53):
  - C1 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L12 | 1.前言 | score=0.0587
  - D1 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L12 | 1.前言 | score=0.0587
  - C2 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L13 | 非承重清水烧结陶土砖镂空幕墙体系中镂空幕墙对整体性、牢固性 及测量精度要求特别高。实际施工中往往采用单一的结构体系会造成施 工困难、日常维护局限性大、对施工人员技术要求高。陕西建工沣西建 设有限公司依据多年对此类工程的施工，并总结形成了非承重清水烧结 陶土砖镂空幕墙施工方法。在多个项目得到成功应用的同时，还获得国 家专利1 项《一种外墙砌筑镂空陶土砖的结构》专利申请号： | score=0.0587
  - C3 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L15 | 2.工法特点 | score=0.0637
  - D2 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L15 | 2.工法特点 | score=0.0637
  - C4 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L16 | 2.1 工厂化加工 | score=0.0637
  - D3 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L16 | 2.1 工厂化加工 | score=0.0637
  - C5 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L17 | 陶土砖采用先进的工艺设备，采用流水线加工，使得每一块具有精 准的外形，降低人工损耗，降低对工人的技术要求。 2.2 构造方式的独特性 | score=0.0637
  - C6 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L18 | 外叶砌体墙采用清水陶土砖砌筑，内叶墙根据工程的位置不同采用 混凝土实体墙或加气混凝土砌块砌筑。在内叶墙的外侧有连续的防水层， 外叶墙作为装饰和雨屏墙（采用自保温砌体只在混凝土构件上按照图纸 要求做保温）。 | score=0.0614
  - C7 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L26 | 4.工艺原理 | score=0.0561
  - D4 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L26 | 4.工艺原理 | score=0.0561
  - C8 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L27 | 采用构件式幕墙系统，根据镂空幕墙分隔将龙骨与主体结构上的连 接件、清水陶土砖的砌筑单元构件、铝板等进行连接固定，形成安全可 靠的外墙装饰和围护结构。纵、横主龙骨采用应力消减支座进行连接， 陶土砖有自带的空腔，其内设有锚固钢筋，并形成砌筑单元构件，在利 用孔内竖向钢筋固定在龙骨上且竖向需设有分封胶条。通过铝板与固定 角钢连接，保证幕墙与建筑物交界处的封口闭合。 | score=0.0561
  - D5 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L28 | 5.施工工艺流程及操作要点 | score=0.0698
  - C9 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L29 | - 5.1 施工工艺流程 | score=0.0483
  - C10 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L30 | 图 **5-1** 深化设计工艺流程图 | score=0.0605
  - D6 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L30 | 图 **5-1** 深化设计工艺流程图 | score=0.0605
- projection_chars: 3422

### Evidence text (new)

```
[E1]
[§ 5.2.6 摞底排砖、挂线砌筑]
  与水平灰缝均衡性。
  - 2、根据排砖位置焊接竖向拉结筋，确保自陶土砖孔穿出。
  3、挂线、立批数杆，开始砌筑。砌筑过程控制线，水平线长度不 宜超过12 米，以防线绳自重下垂影响水平，且墙面长度超过12m 时， 应设置10mm 宽的马牙槎形垂直变形缝，变形缝内采用防水密封胶处 理；考虑一砖一缝，理论尺寸为75mm/250mm，砌筑过程中应先盘头 4/8 层，根据准确盘头放线砌筑，任意4 批砖高度应为300mm。
  图 **5-2-6-3** 现场挂线砌筑以及砌筑模数
  5、镂空砖幕墙部位应考虑主龙骨与镂空部位排砖要求，以保证主 龙骨轮廓不暴露在镂空部位（对于镂空砖位置，内侧墙面需要做JS2 型防水涂料1.5mm 左右）；
  备注：（1）陶土砖本体、（2）左侧壁固定连接左限位块，所述（3） 砖体（1）下表面固定连接下限位块，所述（4）砖体（1）右侧壁固定 连接有右限位块，所述（7）砖体（1）上表面固定连接有上限位块，所 述（5）砖体（1）表面开设有第一镂空花纹、第二镂空花纹（6）和第 三镂空花纹（8）。
```

### Evidence text (old)

```
[E1]
[§ 5.施工工艺流程及操作要点 / 5.2 操作要点 / 5.2.6 摞底排砖、挂线砌筑]
- 图 **5-2-6-1** 现场选砖、打磨及灰缝的均匀性

[E2]
[§ 5.施工工艺流程及操作要点 / 5.2 操作要点 / 5.2.6 摞底排砖、挂线砌筑]
图 **5-2-6-3** 现场挂线砌筑以及砌筑模数

[E3]
[§ 5.施工工艺流程及操作要点 / 5.2 操作要点 / 5.2.6 摞底排砖、挂线砌筑]
备注：（1）陶土砖本体、（2）左侧壁固定连接左限位块，所述（3） 砖体（1）下表面固定连接下限位块，所述（4）砖体（1）右侧壁固定 连接有右限位块，所述（7）砖体（1）上表面固定连接有上限位块，所 述（5）砖体（1）表面开设有第一镂空花纹、第二镂空花纹（6）和第 三

[E4]
[§ 5.施工工艺流程及操作要点 / 5.2 操作要点 / 5.2.6 摞底排砖、挂线砌筑]
3、挂线、立批数杆，开始砌筑。砌筑过程控制线，水平线长度不 宜超过12 米，以防线绳自重下垂影响水平，且墙面长度超过12m 时， 应设置10mm 宽的马牙槎形垂直变形缝，变形缝内采用防水密封胶处
```

## real_69c6ef4e4cca74801cb63bc6_scope_collection_auto_0064 (scope_collection)

**Query:** 列举文档中提到的所有施工验收标准名称及其对应的国家标准编号。

**Doc:** `real_69c6ef4e4cca74801cb63bc6`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.1349 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 202 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 13 | 6 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c6ef4e4cca74801cb63bc6:L158` [MISS] retrieved=False in_text=False
- `real_69c6ef4e4cca74801cb63bc6:L159` [MISS] retrieved=False in_text=False
- `real_69c6ef4e4cca74801cb63bc6:L160` [MISS] retrieved=False in_text=False
- `real_69c6ef4e4cca74801cb63bc6:L161` [MISS] retrieved=False in_text=False
- `real_69c6ef4e4cca74801cb63bc6:L162` [MISS] retrieved=False in_text=False
- `real_69c6ef4e4cca74801cb63bc6:L163` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C20` kind=`collect` section=`real_69c6ef4e4cca74801cb63bc6:L120` scope=`None` depth=`0`
- reason: Collect all construction acceptance standards and their national standard numbers from section 7.1.
- collect_section_ids: ['real_69c6ef4e4cca74801cb63bc6:L120', 'real_69c6ef4e4cca74801cb63bc6:L121', 'real_69c6ef4e4cca74801cb63bc6:L122', 'real_69c6ef4e4cca74801cb63bc6:L123', 'real_69c6ef4e4cca74801cb63bc6:L130', 'real_69c6ef4e4cca74801cb63bc6:L131']
- collect added=6 hits=6 branch_selected=True collect_full=True
- legal_actions (46):
  - C1 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L12 | 1.前言 | score=0.0701
  - D1 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L12 | 1.前言 | score=0.0701
  - C2 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L13 | 非承重清水烧结陶土砖镂空幕墙体系中镂空幕墙对整体性、牢固性 及测量精度要求特别高。实际施工中往往采用单一的结构体系会造成施 工困难、日常维护局限性大、对施工人员技术要求高。陕西建工沣西建 设有限公司依据多年对此类工程的施工，并总结形成了非承重清水烧结 陶土砖镂空幕墙施工方法。在多个项目得到成功应用的同时，还获得国 家专利1 项《一种外墙砌筑镂空陶土砖的结构》专利申请号： | score=0.0701
  - C3 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L14 | 202021699897.9；2021 年3 月份《陕西省住房和城乡建设厅关于下达 2021 年度工程建设标准制定计划的通知》且同意立项，进行陕西省地 方标准的编制。在此基础上，经过进一步提炼，形成了《非承重清水烧 结陶土砖镂空幕墙施工工法》。 | score=0.0688
  - C4 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L28 | 5.施工工艺流程及操作要点 | score=0.0681
  - D2 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L28 | 5.施工工艺流程及操作要点 | score=0.0681
  - C5 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L32 | 5.2 操作要点 | score=0.0681
  - D3 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L32 | 5.2 操作要点 | score=0.0681
  - C6 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L33 | 5.2.1 施工准备 | score=0.0603
  - D4 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L33 | 5.2.1 施工准备 | score=0.0603
  - C7 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L35 | 施工图纸，编制专项施工方案并采用“一张纸工作法”进行点对点交底， | score=0.0603
  - C8 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L41 | 图 **5-2-1-2-2 BIM** 对镂空部分进行建模 | score=0.0597
  - D5 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L41 | 图 **5-2-1-2-2 BIM** 对镂空部分进行建模 | score=0.0597
  - C9 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L42 | - 3、保证进场原材料满足设计要求，尤其是陶土砖应具有足够的强 | score=0.0597
  - C10 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L50 | 图 **5-2-2-1-1** 立面马牙槎垂直变形缝示意图 | score=0.0621
  - D6 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L50 | 图 **5-2-2-1-1** 立面马牙槎垂直变形缝示意图 | score=0.0621
- projection_chars: 3386

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Assembled evidence G1 contains all construction acceptance standards and their national standard numbers.
- legal_actions (48):
  - C1 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L12 | 1.前言 | score=0.0701
  - D1 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L12 | 1.前言 | score=0.0701
  - C2 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L13 | 非承重清水烧结陶土砖镂空幕墙体系中镂空幕墙对整体性、牢固性 及测量精度要求特别高。实际施工中往往采用单一的结构体系会造成施 工困难、日常维护局限性大、对施工人员技术要求高。陕西建工沣西建 设有限公司依据多年对此类工程的施工，并总结形成了非承重清水烧结 陶土砖镂空幕墙施工方法。在多个项目得到成功应用的同时，还获得国 家专利1 项《一种外墙砌筑镂空陶土砖的结构》专利申请号： | score=0.0701
  - C3 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L14 | 202021699897.9；2021 年3 月份《陕西省住房和城乡建设厅关于下达 2021 年度工程建设标准制定计划的通知》且同意立项，进行陕西省地 方标准的编制。在此基础上，经过进一步提炼，形成了《非承重清水烧 结陶土砖镂空幕墙施工工法》。 | score=0.0688
  - C4 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L28 | 5.施工工艺流程及操作要点 | score=0.0681
  - D2 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L28 | 5.施工工艺流程及操作要点 | score=0.0681
  - C5 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L32 | 5.2 操作要点 | score=0.0681
  - D3 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L32 | 5.2 操作要点 | score=0.0681
  - C6 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L33 | 5.2.1 施工准备 | score=0.0603
  - D4 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L33 | 5.2.1 施工准备 | score=0.0603
  - C7 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L35 | 施工图纸，编制专项施工方案并采用“一张纸工作法”进行点对点交底， | score=0.0603
  - C8 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L41 | 图 **5-2-1-2-2 BIM** 对镂空部分进行建模 | score=0.0597
  - D5 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L41 | 图 **5-2-1-2-2 BIM** 对镂空部分进行建模 | score=0.0597
  - C9 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L42 | - 3、保证进场原材料满足设计要求，尤其是陶土砖应具有足够的强 | score=0.0597
  - C10 | COLLECT | real_69c6ef4e4cca74801cb63bc6:L50 | 图 **5-2-2-1-1** 立面马牙槎垂直变形缝示意图 | score=0.0621
  - D6 | DISPATCH | real_69c6ef4e4cca74801cb63bc6:L50 | 图 **5-2-2-1-1** 立面马牙槎垂直变形缝示意图 | score=0.0621
- projection_chars: 3459

### Evidence text (new)

```
[E1]
[§ 7.质量控制]
  7.1 施工验收标准
  - 1、《砌体结构工程施工质量验收规范》GB50203
  - 2、《建筑装饰装修工程质量验收标准》GB50210
  - 3、《建筑节能工程施工质量验收标准》GB50411
  - 10、《外墙外保温工程技术标准》JGJ144
  - 11、《建筑幕墙工程技术标准》DBJ61/T 161 12、《陶板幕墙工程技术规程》Q/TOBSG-03
```

### Evidence text (old)

```
[E1]
[§ 5.施工工艺流程及操作要点 / 5.2 操作要点 / 5.2.8 勾缝、墙面清理]
图 **5-2-8** 勾缝、清理

[E2]
[§ 5.施工工艺流程及操作要点 / 5.2 操作要点 / 5.2.9 防护剂喷涂（28d 后）]
砌筑完成15 天后，墙面应用10%草酸清洗，随后28 天喷憎水剂（甲

[E3]
[§ 5.施工工艺流程及操作要点 / 5.2 操作要点 / 5.2.2 测量放线]
- （1）、对建筑物的外形尺寸进行偏差测量，对结构误差较大部分 进行处理；

[E4]
[§ 1.前言]
非承重清水烧结陶土砖镂空幕墙体系中镂空幕墙对整体性、牢固性 及测量精度要求特别高。实际施工中往往采用单一的结构体系会造成施 工困难、日常维护局限性大、对施工人员技术要求高。陕西建工沣西建 设有限公司依据多年对此类工程的施工，并总结形成了非承重清水烧结 陶土砖镂空幕墙施工方法。在多个项目得到成功应用的同时，还获得国 家专利1 项《一种外墙砌筑

[E5]
[§ 7.质量控制]
7.1 施工验收标准

[E6]
[§ 7.质量控制]
- 3、《建筑节能工程施工质量验收标准》GB5
```

## real_69cb12d0919452cda2225a0b_scope_collection_auto_0073 (scope_collection)

**Query:** 列举收取进项税发票时，关于“票面信息完整性”的具体核查要求。

**Doc:** `real_69cb12d0919452cda2225a0b`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 488 | 493 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 5 | 6 |
| trajectory_steps | n/a | 8 |

### Gold node hits (new)

- `real_69cb12d0919452cda2225a0b:L66` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C4` kind=`collect` section=`real_69cb12d0919452cda2225a0b:L57` scope=`None` depth=`0`
- reason: Section C4 explicitly details the requirements for 'invoice information completeness' when collecting input VAT invoices.
- collect_section_ids: ['real_69cb12d0919452cda2225a0b:L57']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (38):
  - C1 | COLLECT | real_69cb12d0919452cda2225a0b:L54 | **3.1.1** 进项税额定义 | score=0.0734
  - D1 | DISPATCH | real_69cb12d0919452cda2225a0b:L54 | **3.1.1** 进项税额定义 | score=0.0734
  - C2 | COLLECT | real_69cb12d0919452cda2225a0b:L55 | 增值税进项税额，是指集团购进货物、加工修理修配劳务、服务、无形资产或者不 动产，支付或者负担的增值税，进项税额的大小直接关系到项目税负的大小。 **3.1.2** 进项税发票收取 | score=0.0544
  - C3 | COLLECT | real_69cb12d0919452cda2225a0b:L56 | 进项税发票，是指集团购进货物、加工修理修配劳务、服务、无形资产或者不动产， 收取的由销售方开具的增值税专用发票、部分增值税普通发票（旅客运输票据、农产品、 苗木等）。进项税发票主要由集团财务管理服务中心以及项目部收集，由集团财务管理 服务中心统一认证，并在当期向集团主管税务机关申报。 | score=0.0663
  - C4 | COLLECT | real_69cb12d0919452cda2225a0b:L57 | 收取进项发票，应核实业务的真实性、票面信息完整性。业务真实性指此笔业务是 否真实发生，确保“货物、劳务及服务流”、“资金流”、“发票流”、“合同流”保 持四流一致。票面信息完整性指发票购买方信息应与集团开票信息一致；发票内容完整、 发票备注栏注明项目名称以及建筑服务发生地所在省、市、区（县）；发票内容清晰可 辨；发票正反两面干净整洁，不允许出现脏、乱及签字的痕迹；发票抵扣联不可折叠， 不能污损，密 | score=0.0734
  - C5 | COLLECT | real_69cb12d0919452cda2225a0b:L58 | **3.1.3** 进项税发票传递 | score=0.0662
  - D2 | DISPATCH | real_69cb12d0919452cda2225a0b:L58 | **3.1.3** 进项税发票传递 | score=0.0662
  - C6 | COLLECT | real_69cb12d0919452cda2225a0b:L59 | 传递进项税发票时，应登记进项税发票传递单（SJSYJ-CWGL-FJ-001），传递单内 应按照集团公司统一格式要求，内容包括所属公司、项目名称、是否勾选、发票代码、 发票号码、开票日期、税额、有效抵扣税额、销方名称、销方税号、金额、用途、发票 类型，确保当月所有入账的进项税发票与台账中列明的进项税发票以及进项税发票抵扣 联金额、份数相一致后，于当月最后一个工作日之前，将发票台账以及发票抵扣联传递 | score=0.0662
  - C7 | COLLECT | real_69cb12d0919452cda2225a0b:L60 | **3.1.4** 进项税发票认证 | score=0.0655
  - D3 | DISPATCH | real_69cb12d0919452cda2225a0b:L60 | **3.1.4** 进项税发票认证 | score=0.0655
  - C8 | COLLECT | real_69cb12d0919452cda2225a0b:L61 | 集团财务管理服务中心收到进项税发票台账以及发票抵扣联之后，应对所有台账进 行汇总，并进入国家税务总局发票管理平台进行勾选认证发票，确保台账内列明的发票 份数、金额、税额与发票管理平台内认证的相一致后，方可提交认证。如出现不一致现 象，应对发票逐一进行核对，至台账与平台认证信息一致为止。 | score=0.0655
  - C9 | COLLECT | real_69cb12d0919452cda2225a0b:L79 | 税额： | score=0.0674
  - D4 | DISPATCH | real_69cb12d0919452cda2225a0b:L79 | 税额： | score=0.0674
  - C10 | COLLECT | real_69cb12d0919452cda2225a0b:L87 | - b 取得注明旅客身份信息的航空运输电子客票行程单的，为按照下列公司计算进项税 | score=0.0621
  - C11 | COLLECT | real_69cb12d0919452cda2225a0b:L90 | - c 取得注明旅客身份信息的铁路车票的，为按照下列公式计算的进项税额： 铁路旅客运输进项税额=票面金额÷（1+9%）×9% | score=0.0674
  - C12 | COLLECT | real_69cb12d0919452cda2225a0b:L91 | - d 取得注明旅客身份信息的公路、水路等其他客票的，按照下列公式计算进项税额： 公路、水路等其他旅客运输进项税额=票面金额÷（1+3%）×3% | score=0.0664
- projection_chars: 3752

**Step 2** `nav_collect`  id=`C3` kind=`collect` section=`real_69cb12d0919452cda2225a0b:L56` scope=`None` depth=`0`
- reason: Section C3 defines input VAT invoices and collection scope, relevant to invoice information completeness requirements.
- collect_section_ids: ['real_69cb12d0919452cda2225a0b:L56']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (41):
  - C1 | COLLECT | real_69cb12d0919452cda2225a0b:L54 | **3.1.1** 进项税额定义 | score=0.0734
  - D1 | DISPATCH | real_69cb12d0919452cda2225a0b:L54 | **3.1.1** 进项税额定义 | score=0.0734
  - C2 | COLLECT | real_69cb12d0919452cda2225a0b:L55 | 增值税进项税额，是指集团购进货物、加工修理修配劳务、服务、无形资产或者不 动产，支付或者负担的增值税，进项税额的大小直接关系到项目税负的大小。 **3.1.2** 进项税发票收取 | score=0.0544
  - C3 | COLLECT | real_69cb12d0919452cda2225a0b:L56 | 进项税发票，是指集团购进货物、加工修理修配劳务、服务、无形资产或者不动产， 收取的由销售方开具的增值税专用发票、部分增值税普通发票（旅客运输票据、农产品、 苗木等）。进项税发票主要由集团财务管理服务中心以及项目部收集，由集团财务管理 服务中心统一认证，并在当期向集团主管税务机关申报。 | score=0.0663
  - C4 | COLLECT | real_69cb12d0919452cda2225a0b:L58 | **3.1.3** 进项税发票传递 | score=0.0662
  - D2 | DISPATCH | real_69cb12d0919452cda2225a0b:L58 | **3.1.3** 进项税发票传递 | score=0.0662
  - C5 | COLLECT | real_69cb12d0919452cda2225a0b:L59 | 传递进项税发票时，应登记进项税发票传递单（SJSYJ-CWGL-FJ-001），传递单内 应按照集团公司统一格式要求，内容包括所属公司、项目名称、是否勾选、发票代码、 发票号码、开票日期、税额、有效抵扣税额、销方名称、销方税号、金额、用途、发票 类型，确保当月所有入账的进项税发票与台账中列明的进项税发票以及进项税发票抵扣 联金额、份数相一致后，于当月最后一个工作日之前，将发票台账以及发票抵扣联传递 | score=0.0662
  - C6 | COLLECT | real_69cb12d0919452cda2225a0b:L60 | **3.1.4** 进项税发票认证 | score=0.0655
  - D3 | DISPATCH | real_69cb12d0919452cda2225a0b:L60 | **3.1.4** 进项税发票认证 | score=0.0655
  - C7 | COLLECT | real_69cb12d0919452cda2225a0b:L61 | 集团财务管理服务中心收到进项税发票台账以及发票抵扣联之后，应对所有台账进 行汇总，并进入国家税务总局发票管理平台进行勾选认证发票，确保台账内列明的发票 份数、金额、税额与发票管理平台内认证的相一致后，方可提交认证。如出现不一致现 象，应对发票逐一进行核对，至台账与平台认证信息一致为止。 | score=0.0655
  - C8 | COLLECT | real_69cb12d0919452cda2225a0b:L63 | **3.1.5** 进项税费抵扣与统计 | score=0.0531
  - D4 | DISPATCH | real_69cb12d0919452cda2225a0b:L63 | **3.1.5** 进项税费抵扣与统计 | score=0.0531
  - C9 | COLLECT | real_69cb12d0919452cda2225a0b:L64 | 集团财务管理服务中心将当月发票认证完成后，需将各项目当月进项税额如实填列 | score=0.0531
  - C10 | COLLECT | real_69cb12d0919452cda2225a0b:L79 | 税额： | score=0.0674
  - D5 | DISPATCH | real_69cb12d0919452cda2225a0b:L79 | 税额： | score=0.0674
  - C11 | COLLECT | real_69cb12d0919452cda2225a0b:L87 | - b 取得注明旅客身份信息的航空运输电子客票行程单的，为按照下列公司计算进项税 | score=0.0621
- projection_chars: 3683

**Step 3** `nav_collect`  id=`C2` kind=`collect` section=`real_69cb12d0919452cda2225a0b:L55` scope=`None` depth=`0`
- reason: Section 3.1.2 specifically covers input VAT invoice collection requirements, including completeness checks.
- collect_section_ids: ['real_69cb12d0919452cda2225a0b:L55']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (42):
  - C1 | COLLECT | real_69cb12d0919452cda2225a0b:L54 | **3.1.1** 进项税额定义 | score=0.0734
  - D1 | DISPATCH | real_69cb12d0919452cda2225a0b:L54 | **3.1.1** 进项税额定义 | score=0.0734
  - C2 | COLLECT | real_69cb12d0919452cda2225a0b:L55 | 增值税进项税额，是指集团购进货物、加工修理修配劳务、服务、无形资产或者不 动产，支付或者负担的增值税，进项税额的大小直接关系到项目税负的大小。 **3.1.2** 进项税发票收取 | score=0.0544
  - C3 | COLLECT | real_69cb12d0919452cda2225a0b:L58 | **3.1.3** 进项税发票传递 | score=0.0662
  - D2 | DISPATCH | real_69cb12d0919452cda2225a0b:L58 | **3.1.3** 进项税发票传递 | score=0.0662
  - C4 | COLLECT | real_69cb12d0919452cda2225a0b:L59 | 传递进项税发票时，应登记进项税发票传递单（SJSYJ-CWGL-FJ-001），传递单内 应按照集团公司统一格式要求，内容包括所属公司、项目名称、是否勾选、发票代码、 发票号码、开票日期、税额、有效抵扣税额、销方名称、销方税号、金额、用途、发票 类型，确保当月所有入账的进项税发票与台账中列明的进项税发票以及进项税发票抵扣 联金额、份数相一致后，于当月最后一个工作日之前，将发票台账以及发票抵扣联传递 | score=0.0662
  - C5 | COLLECT | real_69cb12d0919452cda2225a0b:L60 | **3.1.4** 进项税发票认证 | score=0.0655
  - D3 | DISPATCH | real_69cb12d0919452cda2225a0b:L60 | **3.1.4** 进项税发票认证 | score=0.0655
  - C6 | COLLECT | real_69cb12d0919452cda2225a0b:L61 | 集团财务管理服务中心收到进项税发票台账以及发票抵扣联之后，应对所有台账进 行汇总，并进入国家税务总局发票管理平台进行勾选认证发票，确保台账内列明的发票 份数、金额、税额与发票管理平台内认证的相一致后，方可提交认证。如出现不一致现 象，应对发票逐一进行核对，至台账与平台认证信息一致为止。 | score=0.0655
  - C7 | COLLECT | real_69cb12d0919452cda2225a0b:L63 | **3.1.5** 进项税费抵扣与统计 | score=0.0531
  - D4 | DISPATCH | real_69cb12d0919452cda2225a0b:L63 | **3.1.5** 进项税费抵扣与统计 | score=0.0531
  - C8 | COLLECT | real_69cb12d0919452cda2225a0b:L64 | 集团财务管理服务中心将当月发票认证完成后，需将各项目当月进项税额如实填列 | score=0.0531
  - C9 | COLLECT | real_69cb12d0919452cda2225a0b:L79 | 税额： | score=0.0674
  - D5 | DISPATCH | real_69cb12d0919452cda2225a0b:L79 | 税额： | score=0.0674
  - C10 | COLLECT | real_69cb12d0919452cda2225a0b:L87 | - b 取得注明旅客身份信息的航空运输电子客票行程单的，为按照下列公司计算进项税 | score=0.0621
  - C11 | COLLECT | real_69cb12d0919452cda2225a0b:L90 | - c 取得注明旅客身份信息的铁路车票的，为按照下列公式计算的进项税额： 铁路旅客运输进项税额=票面金额÷（1+9%）×9% | score=0.0674
- projection_chars: 3746

**Step 4** `nav_collect`  id=`C1` kind=`collect` section=`real_69cb12d0919452cda2225a0b:L54` scope=`None` depth=`0`
- reason: Section 3.1.1 explicitly mentions verifying 'invoice information completeness' for input VAT invoices.
- collect_section_ids: ['real_69cb12d0919452cda2225a0b:L54']
- collect added=3 hits=3 branch_selected=True collect_full=True
- legal_actions (40):
  - C1 | COLLECT | real_69cb12d0919452cda2225a0b:L54 | **3.1.1** 进项税额定义 | score=0.0734
  - C2 | COLLECT | real_69cb12d0919452cda2225a0b:L58 | **3.1.3** 进项税发票传递 | score=0.0662
  - D1 | DISPATCH | real_69cb12d0919452cda2225a0b:L58 | **3.1.3** 进项税发票传递 | score=0.0662
  - C3 | COLLECT | real_69cb12d0919452cda2225a0b:L59 | 传递进项税发票时，应登记进项税发票传递单（SJSYJ-CWGL-FJ-001），传递单内 应按照集团公司统一格式要求，内容包括所属公司、项目名称、是否勾选、发票代码、 发票号码、开票日期、税额、有效抵扣税额、销方名称、销方税号、金额、用途、发票 类型，确保当月所有入账的进项税发票与台账中列明的进项税发票以及进项税发票抵扣 联金额、份数相一致后，于当月最后一个工作日之前，将发票台账以及发票抵扣联传递 | score=0.0662
  - C4 | COLLECT | real_69cb12d0919452cda2225a0b:L60 | **3.1.4** 进项税发票认证 | score=0.0655
  - D2 | DISPATCH | real_69cb12d0919452cda2225a0b:L60 | **3.1.4** 进项税发票认证 | score=0.0655
  - C5 | COLLECT | real_69cb12d0919452cda2225a0b:L61 | 集团财务管理服务中心收到进项税发票台账以及发票抵扣联之后，应对所有台账进 行汇总，并进入国家税务总局发票管理平台进行勾选认证发票，确保台账内列明的发票 份数、金额、税额与发票管理平台内认证的相一致后，方可提交认证。如出现不一致现 象，应对发票逐一进行核对，至台账与平台认证信息一致为止。 | score=0.0655
  - C6 | COLLECT | real_69cb12d0919452cda2225a0b:L63 | **3.1.5** 进项税费抵扣与统计 | score=0.0531
  - D3 | DISPATCH | real_69cb12d0919452cda2225a0b:L63 | **3.1.5** 进项税费抵扣与统计 | score=0.0531
  - C7 | COLLECT | real_69cb12d0919452cda2225a0b:L64 | 集团财务管理服务中心将当月发票认证完成后，需将各项目当月进项税额如实填列 | score=0.0531
  - C8 | COLLECT | real_69cb12d0919452cda2225a0b:L79 | 税额： | score=0.0674
  - D4 | DISPATCH | real_69cb12d0919452cda2225a0b:L79 | 税额： | score=0.0674
  - C9 | COLLECT | real_69cb12d0919452cda2225a0b:L87 | - b 取得注明旅客身份信息的航空运输电子客票行程单的，为按照下列公司计算进项税 | score=0.0621
  - C10 | COLLECT | real_69cb12d0919452cda2225a0b:L90 | - c 取得注明旅客身份信息的铁路车票的，为按照下列公式计算的进项税额： 铁路旅客运输进项税额=票面金额÷（1+9%）×9% | score=0.0674
  - C11 | COLLECT | real_69cb12d0919452cda2225a0b:L91 | - d 取得注明旅客身份信息的公路、水路等其他客票的，按照下列公式计算进项税额： 公路、水路等其他旅客运输进项税额=票面金额÷（1+3%）×3% | score=0.0664
  - C12 | COLLECT | real_69cb12d0919452cda2225a0b:L94 | 纳税人购进国内旅客运输服务，以取得的增值税电子普通发票上注明的税额为进项 税额的，增值税电子普通发票上注明的购买方“名称”“纳税人识别号”等信息，应当 与实际抵扣税款的纳税人一致，否则不予抵扣。 | score=0.0577
- projection_chars: 3602

**Step 5** `nav_collect`  id=`C1` kind=`collect` section=`real_69cb12d0919452cda2225a0b:L58` scope=`None` depth=`0`
- reason: Collect section 3.1.3 to find specific requirements for invoice information completeness verification.
- collect_section_ids: ['real_69cb12d0919452cda2225a0b:L58']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (39):
  - C1 | COLLECT | real_69cb12d0919452cda2225a0b:L58 | **3.1.3** 进项税发票传递 | score=0.0662
  - D1 | DISPATCH | real_69cb12d0919452cda2225a0b:L58 | **3.1.3** 进项税发票传递 | score=0.0662
  - C2 | COLLECT | real_69cb12d0919452cda2225a0b:L59 | 传递进项税发票时，应登记进项税发票传递单（SJSYJ-CWGL-FJ-001），传递单内 应按照集团公司统一格式要求，内容包括所属公司、项目名称、是否勾选、发票代码、 发票号码、开票日期、税额、有效抵扣税额、销方名称、销方税号、金额、用途、发票 类型，确保当月所有入账的进项税发票与台账中列明的进项税发票以及进项税发票抵扣 联金额、份数相一致后，于当月最后一个工作日之前，将发票台账以及发票抵扣联传递 | score=0.0662
  - C3 | COLLECT | real_69cb12d0919452cda2225a0b:L60 | **3.1.4** 进项税发票认证 | score=0.0655
  - D2 | DISPATCH | real_69cb12d0919452cda2225a0b:L60 | **3.1.4** 进项税发票认证 | score=0.0655
  - C4 | COLLECT | real_69cb12d0919452cda2225a0b:L61 | 集团财务管理服务中心收到进项税发票台账以及发票抵扣联之后，应对所有台账进 行汇总，并进入国家税务总局发票管理平台进行勾选认证发票，确保台账内列明的发票 份数、金额、税额与发票管理平台内认证的相一致后，方可提交认证。如出现不一致现 象，应对发票逐一进行核对，至台账与平台认证信息一致为止。 | score=0.0655
  - C5 | COLLECT | real_69cb12d0919452cda2225a0b:L63 | **3.1.5** 进项税费抵扣与统计 | score=0.0531
  - D3 | DISPATCH | real_69cb12d0919452cda2225a0b:L63 | **3.1.5** 进项税费抵扣与统计 | score=0.0531
  - C6 | COLLECT | real_69cb12d0919452cda2225a0b:L64 | 集团财务管理服务中心将当月发票认证完成后，需将各项目当月进项税额如实填列 | score=0.0531
  - C7 | COLLECT | real_69cb12d0919452cda2225a0b:L79 | 税额： | score=0.0674
  - D4 | DISPATCH | real_69cb12d0919452cda2225a0b:L79 | 税额： | score=0.0674
  - C8 | COLLECT | real_69cb12d0919452cda2225a0b:L87 | - b 取得注明旅客身份信息的航空运输电子客票行程单的，为按照下列公司计算进项税 | score=0.0621
  - C9 | COLLECT | real_69cb12d0919452cda2225a0b:L90 | - c 取得注明旅客身份信息的铁路车票的，为按照下列公式计算的进项税额： 铁路旅客运输进项税额=票面金额÷（1+9%）×9% | score=0.0674
  - C10 | COLLECT | real_69cb12d0919452cda2225a0b:L91 | - d 取得注明旅客身份信息的公路、水路等其他客票的，按照下列公式计算进项税额： 公路、水路等其他旅客运输进项税额=票面金额÷（1+3%）×3% | score=0.0664
  - C11 | COLLECT | real_69cb12d0919452cda2225a0b:L94 | 纳税人购进国内旅客运输服务，以取得的增值税电子普通发票上注明的税额为进项 税额的，增值税电子普通发票上注明的购买方“名称”“纳税人识别号”等信息，应当 与实际抵扣税款的纳税人一致，否则不予抵扣。 | score=0.0577
  - C12 | COLLECT | real_69cb12d0919452cda2225a0b:L114 | **3.2.3** 销项税发票的领用及保管 | score=0.0582
- projection_chars: 3540

**Step 6** `nav_collect`  id=`C1` kind=`collect` section=`real_69cb12d0919452cda2225a0b:L60` scope=`None` depth=`0`
- reason: Collect section 3.1.4 to find specific requirements for invoice information completeness verification.
- collect_section_ids: ['real_69cb12d0919452cda2225a0b:L60']
- collect added=2 hits=2 branch_selected=True collect_full=True
- legal_actions (42):
  - C1 | COLLECT | real_69cb12d0919452cda2225a0b:L60 | **3.1.4** 进项税发票认证 | score=0.0655
  - D1 | DISPATCH | real_69cb12d0919452cda2225a0b:L60 | **3.1.4** 进项税发票认证 | score=0.0655
  - C2 | COLLECT | real_69cb12d0919452cda2225a0b:L61 | 集团财务管理服务中心收到进项税发票台账以及发票抵扣联之后，应对所有台账进 行汇总，并进入国家税务总局发票管理平台进行勾选认证发票，确保台账内列明的发票 份数、金额、税额与发票管理平台内认证的相一致后，方可提交认证。如出现不一致现 象，应对发票逐一进行核对，至台账与平台认证信息一致为止。 | score=0.0655
  - C3 | COLLECT | real_69cb12d0919452cda2225a0b:L63 | **3.1.5** 进项税费抵扣与统计 | score=0.0531
  - D2 | DISPATCH | real_69cb12d0919452cda2225a0b:L63 | **3.1.5** 进项税费抵扣与统计 | score=0.0531
  - C4 | COLLECT | real_69cb12d0919452cda2225a0b:L64 | 集团财务管理服务中心将当月发票认证完成后，需将各项目当月进项税额如实填列 | score=0.0531
  - C5 | COLLECT | real_69cb12d0919452cda2225a0b:L79 | 税额： | score=0.0674
  - D3 | DISPATCH | real_69cb12d0919452cda2225a0b:L79 | 税额： | score=0.0674
  - C6 | COLLECT | real_69cb12d0919452cda2225a0b:L87 | - b 取得注明旅客身份信息的航空运输电子客票行程单的，为按照下列公司计算进项税 | score=0.0621
  - C7 | COLLECT | real_69cb12d0919452cda2225a0b:L90 | - c 取得注明旅客身份信息的铁路车票的，为按照下列公式计算的进项税额： 铁路旅客运输进项税额=票面金额÷（1+9%）×9% | score=0.0674
  - C8 | COLLECT | real_69cb12d0919452cda2225a0b:L91 | - d 取得注明旅客身份信息的公路、水路等其他客票的，按照下列公式计算进项税额： 公路、水路等其他旅客运输进项税额=票面金额÷（1+3%）×3% | score=0.0664
  - C9 | COLLECT | real_69cb12d0919452cda2225a0b:L94 | 纳税人购进国内旅客运输服务，以取得的增值税电子普通发票上注明的税额为进项 税额的，增值税电子普通发票上注明的购买方“名称”“纳税人识别号”等信息，应当 与实际抵扣税款的纳税人一致，否则不予抵扣。 | score=0.0577
  - C10 | COLLECT | real_69cb12d0919452cda2225a0b:L114 | **3.2.3** 销项税发票的领用及保管 | score=0.0582
  - D4 | DISPATCH | real_69cb12d0919452cda2225a0b:L114 | **3.2.3** 销项税发票的领用及保管 | score=0.0582
  - C11 | COLLECT | real_69cb12d0919452cda2225a0b:L120 | - （4）税务业务岗开具发票时需向税务核算岗领取空白发票，并做管理登记。 | score=0.0582
  - C12 | COLLECT | real_69cb12d0919452cda2225a0b:L122 | - 同时对已开具发票登记台账，未开具的发票当日下班前交回税务核算岗保管。 | score=0.0519
- projection_chars: 3772

**Step 7** `nav_collect`  id=`C7` kind=`collect` section=`real_69cb12d0919452cda2225a0b:L94` scope=`None` depth=`0`
- reason: Section C7 explicitly details the specific invoice information completeness requirements for input VAT invoices, including buyer name and tax ID matching.
- collect_section_ids: ['real_69cb12d0919452cda2225a0b:L94']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (40):
  - C1 | COLLECT | real_69cb12d0919452cda2225a0b:L63 | **3.1.5** 进项税费抵扣与统计 | score=0.0531
  - D1 | DISPATCH | real_69cb12d0919452cda2225a0b:L63 | **3.1.5** 进项税费抵扣与统计 | score=0.0531
  - C2 | COLLECT | real_69cb12d0919452cda2225a0b:L64 | 集团财务管理服务中心将当月发票认证完成后，需将各项目当月进项税额如实填列 | score=0.0531
  - C3 | COLLECT | real_69cb12d0919452cda2225a0b:L79 | 税额： | score=0.0674
  - D2 | DISPATCH | real_69cb12d0919452cda2225a0b:L79 | 税额： | score=0.0674
  - C4 | COLLECT | real_69cb12d0919452cda2225a0b:L87 | - b 取得注明旅客身份信息的航空运输电子客票行程单的，为按照下列公司计算进项税 | score=0.0621
  - C5 | COLLECT | real_69cb12d0919452cda2225a0b:L90 | - c 取得注明旅客身份信息的铁路车票的，为按照下列公式计算的进项税额： 铁路旅客运输进项税额=票面金额÷（1+9%）×9% | score=0.0674
  - C6 | COLLECT | real_69cb12d0919452cda2225a0b:L91 | - d 取得注明旅客身份信息的公路、水路等其他客票的，按照下列公式计算进项税额： 公路、水路等其他旅客运输进项税额=票面金额÷（1+3%）×3% | score=0.0664
  - C7 | COLLECT | real_69cb12d0919452cda2225a0b:L94 | 纳税人购进国内旅客运输服务，以取得的增值税电子普通发票上注明的税额为进项 税额的，增值税电子普通发票上注明的购买方“名称”“纳税人识别号”等信息，应当 与实际抵扣税款的纳税人一致，否则不予抵扣。 | score=0.0577
  - C8 | COLLECT | real_69cb12d0919452cda2225a0b:L114 | **3.2.3** 销项税发票的领用及保管 | score=0.0582
  - D3 | DISPATCH | real_69cb12d0919452cda2225a0b:L114 | **3.2.3** 销项税发票的领用及保管 | score=0.0582
  - C9 | COLLECT | real_69cb12d0919452cda2225a0b:L120 | - （4）税务业务岗开具发票时需向税务核算岗领取空白发票，并做管理登记。 | score=0.0582
  - C10 | COLLECT | real_69cb12d0919452cda2225a0b:L121 | - （5）税务业务岗对各项目财务人员提供的完税证明与已开具的发票进行归档管理， | score=0.0508
  - C11 | COLLECT | real_69cb12d0919452cda2225a0b:L122 | - 同时对已开具发票登记台账，未开具的发票当日下班前交回税务核算岗保管。 | score=0.0519
  - C12 | COLLECT | real_69cb12d0919452cda2225a0b:L177 | **3.2.6** 发票开具 | score=0.0715
  - D4 | DISPATCH | real_69cb12d0919452cda2225a0b:L177 | **3.2.6** 发票开具 | score=0.0715
- projection_chars: 3598

**Step 8** `nav_collect`  id=`C1` kind=`collect` section=`real_69cb12d0919452cda2225a0b:L63` scope=`None` depth=`0`
- reason: Collect section 3.1.5 to find specific requirements for invoice information completeness verification.
- collect_section_ids: ['real_69cb12d0919452cda2225a0b:L63']
- collect added=3 hits=3 branch_selected=True collect_full=True
- legal_actions (31):
  - C1 | COLLECT | real_69cb12d0919452cda2225a0b:L63 | **3.1.5** 进项税费抵扣与统计 | score=0.0531
  - C2 | COLLECT | real_69cb12d0919452cda2225a0b:L64 | 集团财务管理服务中心将当月发票认证完成后，需将各项目当月进项税额如实填列 | score=0.0531
  - C3 | COLLECT | real_69cb12d0919452cda2225a0b:L79 | 税额： | score=0.0674
  - C4 | COLLECT | real_69cb12d0919452cda2225a0b:L87 | - b 取得注明旅客身份信息的航空运输电子客票行程单的，为按照下列公司计算进项税 | score=0.0621
  - C5 | COLLECT | real_69cb12d0919452cda2225a0b:L90 | - c 取得注明旅客身份信息的铁路车票的，为按照下列公式计算的进项税额： 铁路旅客运输进项税额=票面金额÷（1+9%）×9% | score=0.0674
  - C6 | COLLECT | real_69cb12d0919452cda2225a0b:L91 | - d 取得注明旅客身份信息的公路、水路等其他客票的，按照下列公式计算进项税额： 公路、水路等其他旅客运输进项税额=票面金额÷（1+3%）×3% | score=0.0664
  - C7 | COLLECT | real_69cb12d0919452cda2225a0b:L114 | **3.2.3** 销项税发票的领用及保管 | score=0.0582
  - C8 | COLLECT | real_69cb12d0919452cda2225a0b:L120 | - （4）税务业务岗开具发票时需向税务核算岗领取空白发票，并做管理登记。 | score=0.0582
  - C9 | COLLECT | real_69cb12d0919452cda2225a0b:L121 | - （5）税务业务岗对各项目财务人员提供的完税证明与已开具的发票进行归档管理， | score=0.0508
  - C10 | COLLECT | real_69cb12d0919452cda2225a0b:L122 | - 同时对已开具发票登记台账，未开具的发票当日下班前交回税务核算岗保管。 | score=0.0519
  - C11 | COLLECT | real_69cb12d0919452cda2225a0b:L124 | **3.2.4** 《跨区域涉税事项报告》管理 | score=0.0500
  - C12 | COLLECT | real_69cb12d0919452cda2225a0b:L147 | - 工程竣工结算完成且发票全部开具后，应在工程项目所在地税务机关办理核销手续， | score=0.0500
  - C13 | COLLECT | real_69cb12d0919452cda2225a0b:L177 | **3.2.6** 发票开具 | score=0.0715
  - C14 | COLLECT | real_69cb12d0919452cda2225a0b:L178 | 项目部预缴税款之后，需携带完税证明复印件或扫描件，在集团财务管理服务中心 办理发票开具业务。开具发票之前，项目部应确保发票开具的内容是真实发生的业务， 必须是经过企业合同评审程序通过的合同，发票开具内容与实际交易内容相符。项目部 应负责核对购买方开票信息、含税金额、税率以及类型应与合同签订时约定一致。 | score=0.0642
  - C15 | COLLECT | real_69cb12d0919452cda2225a0b:L179 | 集团财务管理服务中心应确保录入发票信息与项目部提供内容一致，发票备注栏严格 按照合同约定注明项目名称以及建筑服务发生地所在省、市、区（县）；发票内容清晰可 辨；任何区域不能压线、错格、错行、歪斜、颠倒；发票开出后，应当场核对发票信息， 确认无误后，在开具的发票联和抵扣联规定位置加盖发票专用章，且用印清晰，端正，符 合要求不得压盖发票金额，最后完成开票台账登记相关信息后领取发票。发票填开必须按 照号 | score=0.0715
  - C16 | COLLECT | real_69cb12d0919452cda2225a0b:L180 | 发票开具有财务管理服务中心核算员发起开票申请，财务负责人、二级单位项目经理、 总经理审核后，提出付款申请，由财务负责人审核后，进行税款缴纳，税款缴纳完毕后由 集团公司税务核算岗进行审核，审核通过后，税务管理岗执行开票。 **3.2.7** 发票冲红与作废 | score=0.0528
- projection_chars: 3472

### Evidence text (new)

```
[E1]
[§ **3.1.1** 进项税额定义]
  进项税发票，是指集团购进货物、加工修理修配劳务、服务、无形资产或者不动产， 收取的由销售方开具的增值税专用发票、部分增值税普通发票（旅客运输票据、农产品、 苗木等）。进项税发票主要由集团财务管理服务中心以及项目部收集，由集团财务管理 服务中心统一认证，并在当期向集团主管税务机关申报。
  收取进项发票，应核实业务的真实性、票面信息完整性。业务真实性指此笔业务是 否真实发生，确保“货物、劳务及服务流”、“资金流”、“发票流”、“合同流”保 持四流一致。票面信息完整性指发票购买方信息应与集团开票信息一致；发票内容完整、 发票备注栏注明项目名称以及建筑服务发生地所在省、市、区（县）；发票内容清晰可 辨；发票正反两面干净整洁，不允许出现脏、乱及签字的痕迹；发票抵扣联不可折叠， 不能污损，密码区不能出格压线；发票专用章内容应与票面销售方信息一致，不得压盖 发票金额。

[E2]
[§ **3.1.5** 进项税费抵扣与统计]
  集团财务管理服务中心将当月发票认证完成后，需将各项目当月进项税额如实填列
  财务管理（税务管理）
```

### Evidence text (old)

```
[E1]
[§ **3.1.3** 进项税发票传递]
传递进项税发票时，应登记进项税发票传递单（SJSYJ-CWGL-FJ-001），传递单内 应按照集团公司统一格式要求，内容包括所属公司、项目名称、是否勾选、发票代码、 发票号码、开票日期、税额、有效抵扣税额、销方名称、销方税号、金额、用途、发票 类型，确保当月所有入账的进项税发票与台账中列明的进项税发票以及进项税发

[E2]
[§ **3.1.4** 进项税发票认证]
集团财务管理服务中心收到进项税发票台账以及发票抵扣联之后，应对所有台账进 行汇总，并进入国家税务总局发票管理平台进行勾选认证发票，确保台账内列明的发票 份数、金额、税额与发票管理平台内认证的相一致后，方可提交认证。如出现不一致现 象，应对发票逐一进行核对，至台账与平台认证信息一致为止。

[E3]
[§ **3.1.4** 进项税发票认证]
集团财务管理服务中心当月所有发票认证完毕后，应将正确无误的台账以及有问题 的发票返还至财务管理服务中心税管员，各税管员保存台账留底。集团财务管理服务中 心须按月将收集的进项税发票抵扣联装订成册，统一保存。
```

## real_69cb12d0919452cda2225a0b_scope_collection_auto_0076 (scope_collection)

**Query:** 列出办理《跨区域涉税事项备案》时需注意的所有事项要点。

**Doc:** `real_69cb12d0919452cda2225a0b`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 499 |
| gold_node_recall | 0.0 | 0.125 |
| n_retrieved_nodes | 6 | 8 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69cb12d0919452cda2225a0b:L141` [MISS] retrieved=False in_text=False
- `real_69cb12d0919452cda2225a0b:L142` [MISS] retrieved=False in_text=False
- `real_69cb12d0919452cda2225a0b:L143` [MISS] retrieved=False in_text=False
- `real_69cb12d0919452cda2225a0b:L144` [MISS] retrieved=False in_text=False
- `real_69cb12d0919452cda2225a0b:L145` [HIT] retrieved=True in_text=False
- `real_69cb12d0919452cda2225a0b:L146` [MISS] retrieved=False in_text=False
- `real_69cb12d0919452cda2225a0b:L147` [MISS] retrieved=False in_text=False
- `real_69cb12d0919452cda2225a0b:L148` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C6` kind=`collect` section=`real_69cb12d0919452cda2225a0b:L128` scope=`None` depth=`0`
- reason: Collect all leaf nodes under section 3.2.4 detailing cross-regional tax filing requirements and precautions.
- collect_section_ids: ['real_69cb12d0919452cda2225a0b:L128', 'real_69cb12d0919452cda2225a0b:L130', 'real_69cb12d0919452cda2225a0b:L131', 'real_69cb12d0919452cda2225a0b:L134', 'real_69cb12d0919452cda2225a0b:L135', 'real_69cb12d0919452cda2225a0b:L136', 'real_69cb12d0919452cda2225a0b:L137', 'real_69cb12d0919452cda2225a0b:L139', 'real_69cb12d0919452cda2225a0b:L140', 'real_69cb12d0919452cda2225a0b:L144', 'real_69cb12d0919452cda2225a0b:L145', 'real_69cb12d0919452cda2225a0b:L146', 'real_69cb12d0919452cda2225a0b:L148', 'real_69cb12d0919452cda2225a0b:L149', 'real_69cb12d0919452cda2225a0b:L150', 'real_69cb12d0919452cda2225a0b:L154', 'real_69cb12d0919452cda2225a0b:L155', 'real_69cb12d0919452cda2225a0b:L157']
- collect added=18 hits=18 branch_selected=True collect_full=True
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

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 fully covers all key points for cross-regional tax filing requirements.
- legal_actions (41):
  - C1 | COLLECT | real_69cb12d0919452cda2225a0b:L26 | **1.4.2** 专业术语和定义 | score=0.0637
  - D1 | DISPATCH | real_69cb12d0919452cda2225a0b:L26 | **1.4.2** 专业术语和定义 | score=0.0637
  - C2 | COLLECT | real_69cb12d0919452cda2225a0b:L32 | 《跨区域涉税事项报告》：在集团注册地以外地区承接的工程项目，办理的异地经 营许可证明。 | score=0.0637
  - C3 | COLLECT | real_69cb12d0919452cda2225a0b:L54 | **3.1.1** 进项税额定义 | score=0.0448
  - D2 | DISPATCH | real_69cb12d0919452cda2225a0b:L54 | **3.1.1** 进项税额定义 | score=0.0448
  - C4 | COLLECT | real_69cb12d0919452cda2225a0b:L57 | 收取进项发票，应核实业务的真实性、票面信息完整性。业务真实性指此笔业务是 否真实发生，确保“货物、劳务及服务流”、“资金流”、“发票流”、“合同流”保 持四流一致。票面信息完整性指发票购买方信息应与集团开票信息一致；发票内容完整、 发票备注栏注明项目名称以及建筑服务发生地所在省、市、区（县）；发票内容清晰可 辨；发票正反两面干净整洁，不允许出现脏、乱及签字的痕迹；发票抵扣联不可折叠， 不能污损，密 | score=0.0448
  - C5 | COLLECT | real_69cb12d0919452cda2225a0b:L58 | **3.1.3** 进项税发票传递 | score=0.0497
  - D3 | DISPATCH | real_69cb12d0919452cda2225a0b:L58 | **3.1.3** 进项税发票传递 | score=0.0497
  - C6 | COLLECT | real_69cb12d0919452cda2225a0b:L59 | 传递进项税发票时，应登记进项税发票传递单（SJSYJ-CWGL-FJ-001），传递单内 应按照集团公司统一格式要求，内容包括所属公司、项目名称、是否勾选、发票代码、 发票号码、开票日期、税额、有效抵扣税额、销方名称、销方税号、金额、用途、发票 类型，确保当月所有入账的进项税发票与台账中列明的进项税发票以及进项税发票抵扣 联金额、份数相一致后，于当月最后一个工作日之前，将发票台账以及发票抵扣联传递 | score=0.0497
  - C7 | COLLECT | real_69cb12d0919452cda2225a0b:L79 | 税额： | score=0.0438
  - D4 | DISPATCH | real_69cb12d0919452cda2225a0b:L79 | 税额： | score=0.0438
  - C8 | COLLECT | real_69cb12d0919452cda2225a0b:L92 | 注意事项： | score=0.0438
  - C9 | COLLECT | real_69cb12d0919452cda2225a0b:L124 | **3.2.4** 《跨区域涉税事项报告》管理 | score=0.0730
  - D5 | DISPATCH | real_69cb12d0919452cda2225a0b:L124 | **3.2.4** 《跨区域涉税事项报告》管理 | score=0.0730
  - C10 | COLLECT | real_69cb12d0919452cda2225a0b:L125 | 根据《中华人民共和国税收征收管理法实施细则》第二十一条规定：从事生产、经 营的纳税人到外县（市）临时从事生产、经营活动的，应当持税务登记证副本和所在地 税务机关填开的外出经营活动税收管理证明，向营业地税务机关报验登记，接受税务管 理。集团公司注册地址为咸阳市，除在注册地市所辖范围以内区域（渭城区、秦都区） 承接的工程项目不需办理《跨区域涉税事项备案表》，在其他地区承接的工程项目均需 办理《跨区域涉 | score=0.0715
  - C11 | COLLECT | real_69cb12d0919452cda2225a0b:L127 | 《跨区域涉税事项报告》的办理由项目部财务人员发起申请，将所需办理备案项目 的合同扫描件或原件提供至税务业务岗，由税务业务岗在国家税务总局陕西省电子税务 局上进行办理，严格按照合同内容，提交办理《跨区域涉税事项报告》，办理时限不得 超过两个工作日。 | score=0.0716
- projection_chars: 3656

### Evidence text (new)

```
[E1]
[§ **3.2.4** 《跨区域涉税事项报告》管理]
  办理跨区域涉税事项备案需注意事项：
  - 2）项目地址：不是甲方机构所在地，应填写项目所在地省、市、区（县）。（注意：
  - 5）《跨区域涉税事项报告》自办理之日起 30 日内在项目所在地税务机关报验，到
  《跨区域涉税事项报告》办理完成后 30 天之内，项目部应向工程项目所在地主管税 务机关进行报验登记，并按照《中华人民共和国税收征收管理办法》及其实施细则的有 关规定进行经营和纳税。
  在项目所在地税务机关报验时，需提供以下资料：
  - 《跨区域涉税事项报告》初次办理有效期为 360 天，到期日项目未完工的，应于到
  - 5）《跨区域涉税事项报告》所属期间，所有发票复印件以及完税证复印件。
  项目部办理完跨区域涉税事项备案之后，应当留存电子版备案表，并建立《跨区域 涉税事项备案台账》（SJSYJ-CWGL-FJ-005），台账应包括建设单位名称、项目名称、 合同金额、开具日期、到期日期、编号、责任人、核销时间、核销金额，以及已交增值 税、企业所得税、城建税、教育费、地方教育费、水利基金、印花税金额。
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

## latest_clean_multi_0032 (multi_hop)

**Query:** 根据《线上学习平台学习管理方案（修订）》中“（ 一）课程开发管理”相关内容，分别说明两处相邻证据给出的要点。

**Doc:** `real_69c6095ed4242eda8c47c5b2`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 142 | 405 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 2 | 5 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c6095ed4242eda8c47c5b2:L34` [HIT] retrieved=True in_text=False
- `real_69c6095ed4242eda8c47c5b2:L35` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C24` kind=`collect` section=`real_69c6095ed4242eda8c47c5b2:L33` scope=`None` depth=`0`
- reason: Collect adjacent sections under 'Course Development Management' to extract key points as requested.
- collect_section_ids: ['real_69c6095ed4242eda8c47c5b2:L33', 'real_69c6095ed4242eda8c47c5b2:L34', 'real_69c6095ed4242eda8c47c5b2:L37']
- collect added=4 hits=6 branch_selected=False collect_full=True
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

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains the required adjacent points on course development management.
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

### Evidence text (new)

```
[E1]
[§ （ 一）课程开发管理]
  1.课程开发。课程开发依托专家组、各业务线要从有利于组织目标达成、员工履职能力提升等方面，本着“简单、实用、明了”原则进行课程开发。各专家组、各部门应按年度既定课程开发计划，督促、跟进课程开发负责人按时完成课件开发任务。计划外课程开发须明确开发课程名称、学习对象等，经各专家组审核后开发，并向平台中心办公室备案。
  2.课件评审。课件开发完成后，根据课程类别提交各专家组审核，专家组从课件选材、专业度、实用性等方面对课件进行评审，课程评审管理参照《十一在线——员工赋能一体化平台管理办法》执行。
  3.课件上传。评审通过后，平台管理员需在课程计划提交截止时间5 日内完成课件上传和必修岗位指派。计划外开发的课程经各专家组评审通过后5 日完成上传和必修岗位指派。
  4.课酬兑现。开发的课程根据《十一在线——员工赋能一体化平台管理办法》相关规定标准兑现相应课酬。
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
- reason: Collected section L6 contains the required content from Chapter 2. Ready to synthesize the two adjacent points.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 188

**Step 3** `nav_dispatch`  id=`D3` kind=`dispatch` section=`real_69c60970d4242eda8c47c5fd:L6` scope=`None` depth=`0`
- reason: Dispatch Chapter 2 to retrieve details on scope and types for the query.
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
- reason: Evidence G1 and G2 cover Chapter 2 scope and types as requested. Ready to synthesize adjacent points.
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
reason: Collected section L6 contains the required content from Chapter 2. Ready to synthesize the two adjacent points.
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

## latest_clean_niche_0023 (niche_fact)

**Query:** 根据《线上学习平台学习管理方案（修订）》中“（ 一）课程开发管理”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c6095ed4242eda8c47c5b2`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 207 | 405 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 3 | 5 |
| trajectory_steps | n/a | 3 |

### Gold node hits (new)

- `real_69c6095ed4242eda8c47c5b2:L34` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C25` kind=`collect` section=`real_69c6095ed4242eda8c47c5b2:L34` scope=`None` depth=`0`
- reason: Collects the specific regulations under 'Course Development Management' as requested.
- collect_section_ids: ['real_69c6095ed4242eda8c47c5b2:L34']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (46):
  - C1 | COLLECT | real_69c6095ed4242eda8c47c5b2:L1 | 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） | score=0.0712
  - D1 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L1 | 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） | score=0.0712
  - C2 | COLLECT | real_69c6095ed4242eda8c47c5b2:L2 | 为进一步深化学习型组织建设，整合学习资源，传播最佳实践，有效助力员工工作技能提升和绩效改善。为进一步强化学习效果，规范线上学习管理，特制订本方案。 | score=0.0599
  - C3 | COLLECT | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0663
  - D2 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0663
  - C4 | COLLECT | real_69c6095ed4242eda8c47c5b2:L5 | （ 一）十一在线平台中心：负责课程体系设计、课程开发计划审批、课程考核标准设定、平台建设费用审批等相关事宜。 | score=0.0663
  - C5 | COLLECT | real_69c6095ed4242eda8c47c5b2:L7 | （ 三）十一在线平台中心办公室：负责线上学习平台搭建，维护平台基本信息，监督各专家组及相关部门及时更新学习内容，组织各专家组和二级单位平台管理员进行平台管理培训，并对各专家组课程开发情况、学员学习情况进行跟 | score=0.0618
  - C6 | COLLECT | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0574
  - D3 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0574
  - C7 | COLLECT | real_69c6095ed4242eda8c47c5b2:L13 | 1.协同做好线上学习平台的推广、使用和维护等日常管理工作，配合各专家组完成本业务条线培训课程开发、选配工作。 | score=0.0574
  - C8 | COLLECT | real_69c6095ed4242eda8c47c5b2:L14 | 2.督促本部室及本单位员工开展在线学习，并结合线上学习内容和业务实际，组织本部室及本单位开展线下探讨、分享、集中培训等。 | score=0.0573
  - C9 | COLLECT | real_69c6095ed4242eda8c47c5b2:L15 | （ 六 ）学员 | score=0.0622
  - D4 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L15 | （ 六 ）学员 | score=0.0622
  - C10 | COLLECT | real_69c6095ed4242eda8c47c5b2:L16 | 根据课程设置及时完成相应必修课程学习，根据岗位和个人能力的发展规划，合理选修相应课程，积极学以致用，改进工作绩效。 | score=0.0622
  - C11 | COLLECT | real_69c6095ed4242eda8c47c5b2:L17 | 二、课程及指派管理 | score=0.0706
  - D5 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L17 | 二、课程及指派管理 | score=0.0706
- projection_chars: 3584

**Step 2** `nav_collect`  id=`C25` kind=`collect` section=`real_69c6095ed4242eda8c47c5b2:L33` scope=`None` depth=`0`
- reason: Collect section (一)课程开发管理 to retrieve specific regulations as requested.
- collect_section_ids: ['real_69c6095ed4242eda8c47c5b2:L33']
- collect added=4 hits=4 branch_selected=True collect_full=True
- legal_actions (47):
  - C1 | COLLECT | real_69c6095ed4242eda8c47c5b2:L1 | 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） | score=0.0712
  - D1 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L1 | 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） | score=0.0712
  - C2 | COLLECT | real_69c6095ed4242eda8c47c5b2:L2 | 为进一步深化学习型组织建设，整合学习资源，传播最佳实践，有效助力员工工作技能提升和绩效改善。为进一步强化学习效果，规范线上学习管理，特制订本方案。 | score=0.0599
  - C3 | COLLECT | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0663
  - D2 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0663
  - C4 | COLLECT | real_69c6095ed4242eda8c47c5b2:L4 | 线上学习平台主要为除十一在线各研修班以外一般员工提供学习资源。十一在线平台中心为其最高管理机构负责把握学习方向、整合学习资源，各专家组负责学习内容开发，十一在线平台中心办公室主要负责日常运营管理，集团公司机关各部室及各二级单位负责组织本部室及本单位员工参加学习。各级机构及其职责具体如下： | score=0.0567
  - C5 | COLLECT | real_69c6095ed4242eda8c47c5b2:L5 | （ 一）十一在线平台中心：负责课程体系设计、课程开发计划审批、课程考核标准设定、平台建设费用审批等相关事宜。 | score=0.0663
  - C6 | COLLECT | real_69c6095ed4242eda8c47c5b2:L7 | （ 三）十一在线平台中心办公室：负责线上学习平台搭建，维护平台基本信息，监督各专家组及相关部门及时更新学习内容，组织各专家组和二级单位平台管理员进行平台管理培训，并对各专家组课程开发情况、学员学习情况进行跟 | score=0.0618
  - C7 | COLLECT | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0574
  - D3 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0574
  - C8 | COLLECT | real_69c6095ed4242eda8c47c5b2:L13 | 1.协同做好线上学习平台的推广、使用和维护等日常管理工作，配合各专家组完成本业务条线培训课程开发、选配工作。 | score=0.0574
  - C9 | COLLECT | real_69c6095ed4242eda8c47c5b2:L14 | 2.督促本部室及本单位员工开展在线学习，并结合线上学习内容和业务实际，组织本部室及本单位开展线下探讨、分享、集中培训等。 | score=0.0573
  - C10 | COLLECT | real_69c6095ed4242eda8c47c5b2:L15 | （ 六 ）学员 | score=0.0622
  - D4 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L15 | （ 六 ）学员 | score=0.0622
  - C11 | COLLECT | real_69c6095ed4242eda8c47c5b2:L16 | 根据课程设置及时完成相应必修课程学习，根据岗位和个人能力的发展规划，合理选修相应课程，积极学以致用，改进工作绩效。 | score=0.0622
  - C12 | COLLECT | real_69c6095ed4242eda8c47c5b2:L17 | 二、课程及指派管理 | score=0.0706
- projection_chars: 3593

**Step 3** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Assembled evidence G1 contains all specified regulations under 'Course Development Management'.
- legal_actions (43):
  - D1 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L1 | 十一在线——员工赋能一体化平台线上学习平台学习管理方案（修订） | score=0.0712
  - C1 | COLLECT | real_69c6095ed4242eda8c47c5b2:L2 | 为进一步深化学习型组织建设，整合学习资源，传播最佳实践，有效助力员工工作技能提升和绩效改善。为进一步强化学习效果，规范线上学习管理，特制订本方案。 | score=0.0599
  - C2 | COLLECT | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0663
  - D2 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L3 | 一、管理机构及其职责 | score=0.0663
  - C3 | COLLECT | real_69c6095ed4242eda8c47c5b2:L4 | 线上学习平台主要为除十一在线各研修班以外一般员工提供学习资源。十一在线平台中心为其最高管理机构负责把握学习方向、整合学习资源，各专家组负责学习内容开发，十一在线平台中心办公室主要负责日常运营管理，集团公司机关各部室及各二级单位负责组织本部室及本单位员工参加学习。各级机构及其职责具体如下： | score=0.0567
  - C4 | COLLECT | real_69c6095ed4242eda8c47c5b2:L5 | （ 一）十一在线平台中心：负责课程体系设计、课程开发计划审批、课程考核标准设定、平台建设费用审批等相关事宜。 | score=0.0663
  - C5 | COLLECT | real_69c6095ed4242eda8c47c5b2:L7 | （ 三）十一在线平台中心办公室：负责线上学习平台搭建，维护平台基本信息，监督各专家组及相关部门及时更新学习内容，组织各专家组和二级单位平台管理员进行平台管理培训，并对各专家组课程开发情况、学员学习情况进行跟 | score=0.0618
  - C6 | COLLECT | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0574
  - D3 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L12 | （ 五）机关各部室及各二级单位 | score=0.0574
  - C7 | COLLECT | real_69c6095ed4242eda8c47c5b2:L13 | 1.协同做好线上学习平台的推广、使用和维护等日常管理工作，配合各专家组完成本业务条线培训课程开发、选配工作。 | score=0.0574
  - C8 | COLLECT | real_69c6095ed4242eda8c47c5b2:L14 | 2.督促本部室及本单位员工开展在线学习，并结合线上学习内容和业务实际，组织本部室及本单位开展线下探讨、分享、集中培训等。 | score=0.0573
  - C9 | COLLECT | real_69c6095ed4242eda8c47c5b2:L15 | （ 六 ）学员 | score=0.0622
  - D4 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L15 | （ 六 ）学员 | score=0.0622
  - C10 | COLLECT | real_69c6095ed4242eda8c47c5b2:L16 | 根据课程设置及时完成相应必修课程学习，根据岗位和个人能力的发展规划，合理选修相应课程，积极学以致用，改进工作绩效。 | score=0.0622
  - C11 | COLLECT | real_69c6095ed4242eda8c47c5b2:L17 | 二、课程及指派管理 | score=0.0706
  - D5 | DISPATCH | real_69c6095ed4242eda8c47c5b2:L17 | 二、课程及指派管理 | score=0.0706
- projection_chars: 3414

### Evidence text (new)

```
[E1]
[§ （ 一）课程开发管理]
  1.课程开发。课程开发依托专家组、各业务线要从有利于组织目标达成、员工履职能力提升等方面，本着“简单、实用、明了”原则进行课程开发。各专家组、各部门应按年度既定课程开发计划，督促、跟进课程开发负责人按时完成课件开发任务。计划外课程开发须明确开发课程名称、学习对象等，经各专家组审核后开发，并向平台中心办公室备案。
  2.课件评审。课件开发完成后，根据课程类别提交各专家组审核，专家组从课件选材、专业度、实用性等方面对课件进行评审，课程评审管理参照《十一在线——员工赋能一体化平台管理办法》执行。
  3.课件上传。评审通过后，平台管理员需在课程计划提交截止时间5 日内完成课件上传和必修岗位指派。计划外开发的课程经各专家组评审通过后5 日完成上传和必修岗位指派。
  4.课酬兑现。开发的课程根据《十一在线——员工赋能一体化平台管理办法》相关规定标准兑现相应课酬。
```

### Evidence text (old)

```
[E1]
明确课程名称、课程类别、必修岗位、课程开发负责人等信息（见附件），提交十一在线平台中心审批后按计划开发。

[E2]
必修课程的开发数量各专家组结合业务和岗位需求实际确定，课程包含内部自主开发和外部引进，保证课程内容的实用性和有效性。

[E3]
1.必修课程。必修课程需涵盖各专业系统内所有一般管理岗位。 由各专家组主持，根据所辖领域内各岗位职责制定课程开发计划、确定各系统岗位的必修课。课程开发计划需
```

## latest_clean_niche_0043 (niche_fact)

**Query:** 根据《集团公司对外捐赠管理办法（修订版）》中“第四条 对外捐赠的类型”相关内容，该处明确写出的规定或事实是什么？

**Doc:** `real_69c60970d4242eda8c47c5fd`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 243 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 10 | 5 |
| trajectory_steps | n/a | 2 |

### Gold node hits (new)

- `real_69c60970d4242eda8c47c5fd:L11` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C9` kind=`collect` section=`real_69c60970d4242eda8c47c5fd:L10` scope=`None` depth=`0`
- reason: Collect Article 4 and its three subtypes of external donations as requested.
- collect_section_ids: ['real_69c60970d4242eda8c47c5fd:L10', 'real_69c60970d4242eda8c47c5fd:L11', 'real_69c60970d4242eda8c47c5fd:L12', 'real_69c60970d4242eda8c47c5fd:L13']
- collect added=4 hits=7 branch_selected=False collect_full=True
- legal_actions (41):
  - C1 | COLLECT | real_69c60970d4242eda8c47c5fd:L1 | 陕西建工第十一建设集团有限公司 | score=0.0715
  - D1 | DISPATCH | real_69c60970d4242eda8c47c5fd:L1 | 陕西建工第十一建设集团有限公司 | score=0.0715
  - C2 | COLLECT | real_69c60970d4242eda8c47c5fd:L2 | 对外捐赠管理办法（修订版） | score=0.0586
  - C3 | COLLECT | real_69c60970d4242eda8c47c5fd:L3 | 第一章  总则 | score=0.0625
  - D2 | DISPATCH | real_69c60970d4242eda8c47c5fd:L3 | 第一章  总则 | score=0.0625
  - C4 | COLLECT | real_69c60970d4242eda8c47c5fd:L4 | 第一条为进一步规范集团公司对外捐赠行为，加强对外捐赠事项的管理，更好地履行社会责任，全面、有效提升和宣传集团公司品牌及企业形象，特制定本办法。 | score=0.0625
  - C5 | COLLECT | real_69c60970d4242eda8c47c5fd:L5 | 第二条本办法适用于集团公司及所属各单位对外捐赠行为。 | score=0.0544
  - C6 | COLLECT | real_69c60970d4242eda8c47c5fd:L6 | 第二章  对外捐赠的范围及类型 | score=0.0715
  - D3 | DISPATCH | real_69c60970d4242eda8c47c5fd:L6 | 第二章  对外捐赠的范围及类型 | score=0.0715
  - C7 | COLLECT | real_69c60970d4242eda8c47c5fd:L7 | 第三条本办法所称的“对外捐赠”，是指集团公司及所属各单位自愿将有处分权的合法财产无偿赠送给合法的受赠人（包含无偿捐赠工程），用于与捐赠人生产经营活动没有直接关系的公益事业的行为。 | score=0.0715
  - C8 | COLLECT | real_69c60970d4242eda8c47c5fd:L9 | 对外捐赠原则上以集团公司（陕西建工第十一建设集团有限公司）名义进行捐赠，独立法人单位可根据实际需要以本单位名义进行捐赠。 | score=0.0651
  - C9 | COLLECT | real_69c60970d4242eda8c47c5fd:L10 | 第四条  对外捐赠的类型 | score=0.0696
  - D4 | DISPATCH | real_69c60970d4242eda8c47c5fd:L10 | 第四条  对外捐赠的类型 | score=0.0696
  - C10 | COLLECT | real_69c60970d4242eda8c47c5fd:L11 | （一）救济性捐赠，即向受灾地区、扶贫地区或者困难的社会弱势群体的救济性捐赠。 | score=0.0595
  - C11 | COLLECT | real_69c60970d4242eda8c47c5fd:L12 | （二）公益性捐赠，即向科技文卫事业和环境保护等社会公益事业的公益性捐赠。 | score=0.0591
  - C12 | COLLECT | real_69c60970d4242eda8c47c5fd:L13 | （三）其他捐赠，即除上述捐赠外，为促进社会发展以及集团公司履行社会责任需要的其他捐赠，含外部各类活动赞助。 | score=0.0593
- projection_chars: 3480

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: The assembled evidence G1 contains the full content of Article 4 regarding donation types, sufficient to answer the query.
- legal_actions (39):
  - D1 | DISPATCH | real_69c60970d4242eda8c47c5fd:L1 | 陕西建工第十一建设集团有限公司 | score=0.0715
  - C1 | COLLECT | real_69c60970d4242eda8c47c5fd:L2 | 对外捐赠管理办法（修订版） | score=0.0586
  - C2 | COLLECT | real_69c60970d4242eda8c47c5fd:L3 | 第一章  总则 | score=0.0625
  - D2 | DISPATCH | real_69c60970d4242eda8c47c5fd:L3 | 第一章  总则 | score=0.0625
  - C3 | COLLECT | real_69c60970d4242eda8c47c5fd:L4 | 第一条为进一步规范集团公司对外捐赠行为，加强对外捐赠事项的管理，更好地履行社会责任，全面、有效提升和宣传集团公司品牌及企业形象，特制定本办法。 | score=0.0625
  - C4 | COLLECT | real_69c60970d4242eda8c47c5fd:L5 | 第二条本办法适用于集团公司及所属各单位对外捐赠行为。 | score=0.0544
  - D3 | DISPATCH | real_69c60970d4242eda8c47c5fd:L6 | 第二章  对外捐赠的范围及类型 | score=0.0715
  - C5 | COLLECT | real_69c60970d4242eda8c47c5fd:L7 | 第三条本办法所称的“对外捐赠”，是指集团公司及所属各单位自愿将有处分权的合法财产无偿赠送给合法的受赠人（包含无偿捐赠工程），用于与捐赠人生产经营活动没有直接关系的公益事业的行为。 | score=0.0715
  - C6 | COLLECT | real_69c60970d4242eda8c47c5fd:L8 | 集团公司所属非法人分支机构、项目部不得以分公司、项目部名义对外捐赠，不得将企业拥有的财产以个人名义对外捐赠。 | score=0.0521
  - C7 | COLLECT | real_69c60970d4242eda8c47c5fd:L9 | 对外捐赠原则上以集团公司（陕西建工第十一建设集团有限公司）名义进行捐赠，独立法人单位可根据实际需要以本单位名义进行捐赠。 | score=0.0651
  - C8 | COLLECT | real_69c60970d4242eda8c47c5fd:L15 | 第五条  对外捐赠的范围 | score=0.0644
  - D4 | DISPATCH | real_69c60970d4242eda8c47c5fd:L15 | 第五条  对外捐赠的范围 | score=0.0644
  - C9 | COLLECT | real_69c60970d4242eda8c47c5fd:L16 | 用于对外捐赠的资产应当权属清晰，应为集团公司有权处分的合法财产，包括现金资产和实物资产等。 | score=0.0644
  - C10 | COLLECT | real_69c60970d4242eda8c47c5fd:L17 | 不具处分权的财产或者不合格产品不得用于对外捐赠。下列资产不得用于对外捐赠： | score=0.0579
  - C11 | COLLECT | real_69c60970d4242eda8c47c5fd:L18 | （一）生产经营用的主要固定资产； | score=0.0545
  - C12 | COLLECT | real_69c60970d4242eda8c47c5fd:L21 | （四）国家财政拨款； | score=0.0545
- projection_chars: 3514

### Evidence text (new)

```
[E1]
[§ 第四条  对外捐赠的类型]
  （一）救济性捐赠，即向受灾地区、扶贫地区或者困难的社会弱势群体的救济性捐赠。
  （二）公益性捐赠，即向科技文卫事业和环境保护等社会公益事业的公益性捐赠。
  （三）其他捐赠，即除上述捐赠外，为促进社会发展以及集团公司履行社会责任需要的其他捐赠，含外部各类活动赞助。
  各单位要正确参与社会公益事业，依法依规确定对外捐赠范围和支出规模，规范开展对外捐赠活动，避免无序、随意捐赠等行为。对于有关社会机构、团体的摊派性捐赠，要坚决依法拒绝，
```

### Evidence text (old)

```
[E1]
[§ 陕西建工第十一建设集团有限公司 / 第二章  对外捐赠的范围及类型]
第三条本办法所称的“对外捐赠”，是指集团公司及所属各单位自愿将有处分权的合法财产无偿赠送给合法的受赠人（包含无偿捐赠工程），用于与捐赠人生产经营活动没有直接关系的公益事业的行为。

[E2]
[§ 陕西建工第十一建设集团有限公司]
对外捐赠管理办法（修订版）

[E3]
[§ 陕西建工第十一建设集团有限公司 / 第一章  总则]
第二条本办法适用于集团公司及所属各单位对外捐赠行为。

[E4]
[§ 陕西建工第十一建设集团有限公司 / 第二章  对外捐赠的范围及类型 / 第五条  对外捐赠的范围]
用于对外捐赠的资产应当权属清晰，应为集团公司有权处分的合法财产，包括现金资产和实物资产等。

[E5]
[§ 陕西建工第十一建设集团有限公司 / 第二章  对外捐赠的范围及类型 / 第四条  对外捐赠的类型]
（三）其他捐赠，即除上述捐赠外，为促进社会发展以及集团公司履行社会责任需要的其他捐赠，含外部各类活动赞助。

[E6]
[§ 陕西建工第十一建设集团有限公司 / 第三章  对外捐赠的原则]
（二）量力
```

## latest_clean_scope_0116 (scope_collection)

**Query:** 列举《1.临时用电施工组织设计范本》中“1.临时用电施工组织设计范本.docx”部分的主要条目。

**Doc:** `real_69c60aeed4242eda8c47c928`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 499 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 26 | 26 |
| trajectory_steps | n/a | 5 |

### Gold node hits (new)

- `real_69c60aeed4242eda8c47c928:L42` [MISS] retrieved=False in_text=False
- `real_69c60aeed4242eda8c47c928:L43` [MISS] retrieved=False in_text=False
- `real_69c60aeed4242eda8c47c928:L47` [MISS] retrieved=False in_text=False
- `real_69c60aeed4242eda8c47c928:L48` [MISS] retrieved=False in_text=False
- `real_69c60aeed4242eda8c47c928:L49` [MISS] retrieved=False in_text=False
- `real_69c60aeed4242eda8c47c928:L50` [MISS] retrieved=False in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60aeed4242eda8c47c928:L1` scope=`None` depth=`0`
- reason: Collect the main section '工程概况' to retrieve its primary entries as requested.
- collect_section_ids: ['real_69c60aeed4242eda8c47c928:L1']
- collect added=7 hits=7 branch_selected=True collect_full=False
- legal_actions (68):
  - C1 | COLLECT | real_69c60aeed4242eda8c47c928:L1 | 工程概况 | score=0.0681
  - D1 | DISPATCH | real_69c60aeed4242eda8c47c928:L1 | 工程概况 | score=0.0681
  - C2 | COLLECT | real_69c60aeed4242eda8c47c928:L2 | 项目概况 | score=0.0643
  - D2 | DISPATCH | real_69c60aeed4242eda8c47c928:L2 | 项目概况 | score=0.0643
  - C3 | COLLECT | real_69c60aeed4242eda8c47c928:L3 | 表1-1项目基本情况表 | score=0.0643
  - C4 | COLLECT | real_69c60aeed4242eda8c47c928:L11 | 现场用电管理组织机构 | score=0.0681
  - D3 | DISPATCH | real_69c60aeed4242eda8c47c928:L11 | 现场用电管理组织机构 | score=0.0681
  - C5 | COLLECT | real_69c60aeed4242eda8c47c928:L12 | 临电组织机构图 | score=0.0681
  - D4 | DISPATCH | real_69c60aeed4242eda8c47c928:L12 | 临电组织机构图 | score=0.0681
  - C6 | COLLECT | real_69c60aeed4242eda8c47c928:L13 | 图表展示临电项目组织结构，以项目经理为核心，下设商务、技术生产和安全管理三大分支，分别管理各自职能组，最终连接至分包单位。 | score=0.0681
  - C7 | COLLECT | real_69c60aeed4242eda8c47c928:L16 | 现场临时用电管理职责 | score=0.0565
  - D5 | DISPATCH | real_69c60aeed4242eda8c47c928:L16 | 现场临时用电管理职责 | score=0.0565
  - C8 | COLLECT | real_69c60aeed4242eda8c47c928:L17 | 表1-6现场临时用电管理职责表 | score=0.0565
  - C9 | COLLECT | real_69c60aeed4242eda8c47c928:L18 | 施工现场临电布置平面图 | score=0.0546
  - D6 | DISPATCH | real_69c60aeed4242eda8c47c928:L18 | 施工现场临电布置平面图 | score=0.0546
  - C10 | COLLECT | real_69c60aeed4242eda8c47c928:L19 | 表1-7施工现场临电布置表 | score=0.0546
- projection_chars: 3253

**Step 2** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60aeed4242eda8c47c928:L21` scope=`None` depth=`0`
- collect_section_ids: ['real_69c60aeed4242eda8c47c928:L21']
- collect added=3 hits=3 branch_selected=True collect_full=False
- legal_actions (63):
  - C1 | COLLECT | real_69c60aeed4242eda8c47c928:L21 | 用电容量统计 | score=0.0674
  - D1 | DISPATCH | real_69c60aeed4242eda8c47c928:L21 | 用电容量统计 | score=0.0674
  - C2 | COLLECT | real_69c60aeed4242eda8c47c928:L22 | 设备功率统计 | score=0.0591
  - D2 | DISPATCH | real_69c60aeed4242eda8c47c928:L22 | 设备功率统计 | score=0.0591
  - C3 | COLLECT | real_69c60aeed4242eda8c47c928:L23 | 表3-1施工现场临时用电设备功率统计表 | score=0.0591
  - C4 | COLLECT | real_69c60aeed4242eda8c47c928:L24 | 施工用电分配表 | score=0.0674
  - D3 | DISPATCH | real_69c60aeed4242eda8c47c928:L24 | 施工用电分配表 | score=0.0674
  - C5 | COLLECT | real_69c60aeed4242eda8c47c928:L25 | 表3-2临时用电分配表 | score=0.0674
  - C6 | COLLECT | real_69c60aeed4242eda8c47c928:L26 | 负荷计算 | score=0.0702
  - D4 | DISPATCH | real_69c60aeed4242eda8c47c928:L26 | 负荷计算 | score=0.0702
  - C7 | COLLECT | real_69c60aeed4242eda8c47c928:L27 | 总用电量计算 | score=0.0702
  - D5 | DISPATCH | real_69c60aeed4242eda8c47c928:L27 | 总用电量计算 | score=0.0702
  - C8 | COLLECT | real_69c60aeed4242eda8c47c928:L33 | 式中： Pjs—有功计算负荷，kW； Qjs一无功计算负荷，kvar； Sjs一视在计算负荷，kVA； Ijs一计算电流，A； PS—用电设备的总容量，kW： KX一需要系数，参考《民用建筑设计手册》（第二版）100-101页；《临时用电施工组织设计编制指南》附录3；《施工现场临时用电安全技术》JGJ/T46-2024 211页； | score=0.0702
  - C9 | COLLECT | real_69c60aeed4242eda8c47c928:L39 | 选择变压器 | score=0.0687
  - D6 | DISPATCH | real_69c60aeed4242eda8c47c928:L39 | 选择变压器 | score=0.0687
  - C10 | COLLECT | real_69c60aeed4242eda8c47c928:L40 | 变压器损耗计算 | score=0.0687
- projection_chars: 3355

**Step 3** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60aeed4242eda8c47c928:L26` scope=`None` depth=`0`
- reason: Collect main section headers of the template to list all primary entries.
- collect_section_ids: ['real_69c60aeed4242eda8c47c928:L26', 'real_69c60aeed4242eda8c47c928:L39', 'real_69c60aeed4242eda8c47c928:L75', 'real_69c60aeed4242eda8c47c928:L90', 'real_69c60aeed4242eda8c47c928:L109', 'real_69c60aeed4242eda8c47c928:L112', 'real_69c60aeed4242eda8c47c928:L114']
- collect added=32 hits=32 branch_selected=True collect_full=False
- legal_actions (60):
  - C1 | COLLECT | real_69c60aeed4242eda8c47c928:L26 | 负荷计算 | score=0.0702
  - D1 | DISPATCH | real_69c60aeed4242eda8c47c928:L26 | 负荷计算 | score=0.0702
  - C2 | COLLECT | real_69c60aeed4242eda8c47c928:L27 | 总用电量计算 | score=0.0702
  - D2 | DISPATCH | real_69c60aeed4242eda8c47c928:L27 | 总用电量计算 | score=0.0702
  - C3 | COLLECT | real_69c60aeed4242eda8c47c928:L33 | 式中： Pjs—有功计算负荷，kW； Qjs一无功计算负荷，kvar； Sjs一视在计算负荷，kVA； Ijs一计算电流，A； PS—用电设备的总容量，kW： KX一需要系数，参考《民用建筑设计手册》（第二版）100-101页；《临时用电施工组织设计编制指南》附录3；《施工现场临时用电安全技术》JGJ/T46-2024 211页； | score=0.0702
  - C4 | COLLECT | real_69c60aeed4242eda8c47c928:L39 | 选择变压器 | score=0.0687
  - D3 | DISPATCH | real_69c60aeed4242eda8c47c928:L39 | 选择变压器 | score=0.0687
  - C5 | COLLECT | real_69c60aeed4242eda8c47c928:L40 | 变压器损耗计算 | score=0.0687
  - D4 | DISPATCH | real_69c60aeed4242eda8c47c928:L40 | 变压器损耗计算 | score=0.0687
  - C6 | COLLECT | real_69c60aeed4242eda8c47c928:L41 | 变压器容量计算要求 | score=0.0687
  - D5 | DISPATCH | real_69c60aeed4242eda8c47c928:L41 | 变压器容量计算要求 | score=0.0687
  - C7 | COLLECT | real_69c60aeed4242eda8c47c928:L42 | （1）变压器容量应分阶段计算，如按地基与基础、主体、装饰与机电安装等，取各阶段最大值为项目临时用电的变压器容量。 | score=0.0687
  - C8 | COLLECT | real_69c60aeed4242eda8c47c928:L47 | Sj :变压器的计算负荷（单位：kVA）； | score=0.0504
  - C9 | COLLECT | real_69c60aeed4242eda8c47c928:L75 | 设计配电系统和装置 | score=0.0584
  - D6 | DISPATCH | real_69c60aeed4242eda8c47c928:L75 | 设计配电系统和装置 | score=0.0584
  - C10 | COLLECT | real_69c60aeed4242eda8c47c928:L76 | 一级配电柜至各二级箱线路设计 | score=0.0584
- projection_chars: 3321

**Step 4** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60aeed4242eda8c47c928:L20` scope=`None` depth=`0`
- reason: Collect '编制依据' section to list its main entries as requested.
- collect_section_ids: ['real_69c60aeed4242eda8c47c928:L20']
- collect added=1 hits=1 branch_selected=True collect_full=True
- legal_actions (8):
  - C1 | COLLECT | real_69c60aeed4242eda8c47c928:L20 | 编制依据 | score=0.0447
  - C2 | COLLECT | real_69c60aeed4242eda8c47c928:L129 | 相关图纸 | score=0.0619
  - D1 | DISPATCH | real_69c60aeed4242eda8c47c928:L129 | 相关图纸 | score=0.0619
  - C3 | COLLECT | real_69c60aeed4242eda8c47c928:L130 | 临时用电工程总平面图 | score=0.0619
  - C4 | COLLECT | real_69c60aeed4242eda8c47c928:L131 | 配电装置布置图 | score=0.0499
  - C5 | COLLECT | real_69c60aeed4242eda8c47c928:L132 | 配电系统接线图 | score=0.0457
  - C6 | COLLECT | real_69c60aeed4242eda8c47c928:L133 | 接地装置设计图 | score=0.0495
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 488

**Step 5** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: All main sections of the temporary power organization design template are now collected and ranked.
- legal_actions (7):
  - C1 | COLLECT | real_69c60aeed4242eda8c47c928:L129 | 相关图纸 | score=0.0619
  - D1 | DISPATCH | real_69c60aeed4242eda8c47c928:L129 | 相关图纸 | score=0.0619
  - C2 | COLLECT | real_69c60aeed4242eda8c47c928:L130 | 临时用电工程总平面图 | score=0.0619
  - C3 | COLLECT | real_69c60aeed4242eda8c47c928:L131 | 配电装置布置图 | score=0.0499
  - C4 | COLLECT | real_69c60aeed4242eda8c47c928:L132 | 配电系统接线图 | score=0.0457
  - C5 | COLLECT | real_69c60aeed4242eda8c47c928:L133 | 接地装置设计图 | score=0.0495
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 440

### Evidence text (new)

```
[E1]
[§ 工程概况]
  项目概况
  表1-1项目基本情况表
  施工现场概况
  表1-2施工现场情况表
  施工地的气候特征和季节性天气
  表1-3施工现场当地气候统计表
  风险识别
  表1-4风险识别统计表
  备注：LEC法评分标准参考陕建总SJGF-QBA/T001-2022；
  现场用电管理组织机构
  临电组织机构图
  图表展示临电项目组织结构，以项目经理为核心，下设商务、技术生产和安全管理三大分支，分别管理各自职能组，最终连接至分包单位。
  施工现场临电布置平面图
  表1-7施工现场临电布置表

[E2]
[§ 用电容量统计]
  设备功率统计
  表3-1施工现场临时用电设备功率统计表
  施工用电分配表
  表3-2临时用电分配表

[E3]
[§ 负荷计算]
  总用电量计算
  Ｐｊｓ＝ＫＸ*ＰＳ
  Ｑｊｓ＝Ｐｊｓ*ｔａｎφ
  一级配电柜至各回路二级箱负荷计算
  表4-3一、二级配电负荷计算表

[E4]
[§ 设计配电系统和装置]
一级配电柜至各二级箱线路设计
备注：设计图中应体现以下信息
1、箱变及各级配电箱名称设计位置及分级。
```

### Evidence text (old)

```
[E1]
工程概况

[E2]
制定安全用电措施和电气防火措施

[E3]
用电容量统计

[E4]
负荷计算

[E5]
项目概况
表1-1项目基本情况表

[E6]
表8-1安全用电及防火措施统计表

[E7]
设备功率统计
表3-1施工现场临时用电设备功率统计表

[E8]
总用电量计算
Ｐｊｓ＝ＫＸ*ＰＳ
Ｑｊｓ＝Ｐｊｓ*ｔａｎφ

[E9]
施工现场概况
表1-2施工现场情况表

[E10]
内容涵盖安全用电的技术与组织措施，包括保护接地、接零、漏电保护及分级管理；同时详述了电气火灾的成因分析与预防策略，并提供了不同火灾类型的灭火器材选择及操作要点。

[E11]
施工用电分配表
表3-2临时用电分配表

[E12]
一级配电柜至各回路二级箱负荷计算
表4-3一、二级配电负荷计算表

[E13]
施工地的气候特征和季节性天气
表1-3施工现场当地气候统计表

[E14]
风险识别
表1-4风险识别统计表
备注：LEC法评分标准参考陕建总SJGF-QBA/T001-2022；

[E15]
现场用电管理组织机构
临电组织机构图
图表展示临电项目组织结构，以项目经理为核心，下设商
```

## latest_clean_scope_0119 (scope_collection)

**Query:** 列举《9.1土方开挖方案范本》中“9.1土方开挖方案范本.docx”部分的主要条目。

**Doc:** `real_69c60af6d4242eda8c47c934`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 487 |
| gold_node_recall | 0.0 | 0.5 |
| n_retrieved_nodes | 28 | 22 |
| trajectory_steps | n/a | 14 |

### Gold node hits (new)

- `real_69c60af6d4242eda8c47c934:L5` [MISS] retrieved=False in_text=False
- `real_69c60af6d4242eda8c47c934:L7` [MISS] retrieved=False in_text=False
- `real_69c60af6d4242eda8c47c934:L8` [MISS] retrieved=False in_text=False
- `real_69c60af6d4242eda8c47c934:L13` [HIT] retrieved=True in_text=False
- `real_69c60af6d4242eda8c47c934:L16` [HIT] retrieved=True in_text=False
- `real_69c60af6d4242eda8c47c934:L19` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60af6d4242eda8c47c934:L1` scope=`real_69c60af6d4242eda8c47c934:L1` depth=`1`
- reason: Collecting the main section '工程概况' to retrieve all primary entries of the excavation plan.
- collect_section_ids: ['real_69c60af6d4242eda8c47c934:L1']
- collect added=8 hits=8 branch_selected=True collect_full=False
- legal_actions (18):
  - C1 | COLLECT | real_69c60af6d4242eda8c47c934:L1 | 工程概况 | score=0.0655
  - C2 | COLLECT | real_69c60af6d4242eda8c47c934:L2 | 基坑工程概况和特点 | score=0.0527
  - C3 | COLLECT | real_69c60af6d4242eda8c47c934:L3 | 工程基本情况 | score=0.0490
  - C4 | COLLECT | real_69c60af6d4242eda8c47c934:L4 | 表1.1工程基本情况表 | score=0.0490
  - C5 | COLLECT | real_69c60af6d4242eda8c47c934:L6 | 工程地质及水文情况 | score=0.0527
  - C6 | COLLECT | real_69c60af6d4242eda8c47c934:L7 | 根据勘察报告，拟建场地地貌单元属沣河右岸一级阶地，场地地层开挖范围内地层自上而下依次由第四系全新统人工填土、冲洪积黄土状土、砂土、粉质黏土等组成，基坑开挖范围内各层土的野外特征分述如下： | score=0.0527
  - C7 | COLLECT | real_69c60af6d4242eda8c47c934:L11 | 周边环境条件 | score=0.0539
  - C8 | COLLECT | real_69c60af6d4242eda8c47c934:L13 | 项目北侧为沣东三路，东侧为科源一路，车流量少且无拥堵；场地周围无河流；无地上地下管线；东侧毗邻沣东第一中学，施工期间扰民影响较小。 | score=0.0473
  - C9 | COLLECT | real_69c60af6d4242eda8c47c934:L14 | 表1.4项目气候统计表 | score=0.0539
  - C10 | COLLECT | real_69c60af6d4242eda8c47c934:L17 | 施工平面及立面布置 | score=0.0537
  - C11 | COLLECT | real_69c60af6d4242eda8c47c934:L20 | 土方开挖平面图及剖面图 | score=0.0537
  - C12 | COLLECT | real_69c60af6d4242eda8c47c934:L21 | 该文档包含多张基坑土方开挖的平面图与剖面图，涵盖A1-A2、B1-B2/B3-B5、C1-C2及D段等区域。内容涉及开挖顺序、运输路线、自然放坡、支护结构（如喷射混凝土、土钉）、土层物理参数及地质信息，比例尺多为1:100。 | score=0.0537
  - C13 | COLLECT | real_69c60af6d4242eda8c47c934:L22 | 施工要求 | score=0.0655
  - C14 | COLLECT | real_69c60af6d4242eda8c47c934:L23 | 表1.5工程目标及基坑分项工程目标表 | score=0.0655
  - C15 | COLLECT | real_69c60af6d4242eda8c47c934:L24 | 表1.6土方开挖施工周期表 | score=0.0557
  - C16 | COLLECT | real_69c60af6d4242eda8c47c934:L27 | 参建各方责任主体单位 | score=0.0505
- projection_chars: 2862

**Step 2** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60af6d4242eda8c47c934:L1` depth=`1`
- reason: The document root has been collected, which contains the main entries of the土方开挖方案范本.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 188

**Step 3** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60af6d4242eda8c47c934:L56` scope=`real_69c60af6d4242eda8c47c934:L56` depth=`1`
- reason: Collects the main 'Construction Guarantee Measures' section containing all required sub-items for the土方开挖方案范本.
- collect_section_ids: ['real_69c60af6d4242eda8c47c934:L56']
- collect added=4 hits=4 branch_selected=True collect_full=False
- legal_actions (17):
  - C1 | COLLECT | real_69c60af6d4242eda8c47c934:L56 | 施工保证措施 | score=0.0713
  - C2 | COLLECT | real_69c60af6d4242eda8c47c934:L57 | 组织保障措施 | score=0.0389
  - C3 | COLLECT | real_69c60af6d4242eda8c47c934:L59 | 安全保证体系及人员安全职责 | score=0.0389
  - C4 | COLLECT | real_69c60af6d4242eda8c47c934:L60 | 表5.1总承包单位人员及安全职责表 | score=0.0375
  - C5 | COLLECT | real_69c60af6d4242eda8c47c934:L61 | 表5.2专业分包单位人员及安全职责表 | score=0.0389
  - C6 | COLLECT | real_69c60af6d4242eda8c47c934:L62 | 技术保障措施 | score=0.0713
  - C7 | COLLECT | real_69c60af6d4242eda8c47c934:L63 | 安全保证措施 | score=0.0713
  - C8 | COLLECT | real_69c60af6d4242eda8c47c934:L66 | 本文档详细列出了施工中的三大安全类别：防高坠、临时用电及土方开挖的具体技术保障措施，涵盖人员资质、设备检查、防护设施搭建及操作规范等要求。 | score=0.0713
  - C9 | COLLECT | real_69c60af6d4242eda8c47c934:L71 | 监测监控措施 | score=0.0550
  - C10 | COLLECT | real_69c60af6d4242eda8c47c934:L72 | 监测点的设置 | score=0.0550
  - C11 | COLLECT | real_69c60af6d4242eda8c47c934:L73 | 根据GB 50497-2019标准及设计要求，沿基坑周边布置监测点，重点监测开挖对基坑及周边环境的影响。点位间距不大于20m，每边不少于3个，涵盖中部、阳角及邻近对象处，并包含监测平面图指导施工。 | score=0.0550
  - C12 | COLLECT | real_69c60af6d4242eda8c47c934:L80 | 监测方式方法 | score=0.0378
  - C13 | COLLECT | real_69c60af6d4242eda8c47c934:L83 | （3）监测监控方法 | score=0.0377
  - C14 | COLLECT | real_69c60af6d4242eda8c47c934:L84 | 内容涵盖竖向位移（沉降）和水平位移的监测方法，包括围护墙、周边建筑及管线等对象。沉降宜用水准测量，水平位移可用视准线、极坐标等方法。另附超危大基坑监测系统图说明。 | score=0.0377
  - C15 | COLLECT | real_69c60af6d4242eda8c47c934:L85 | （4）监测频率及要求 | score=0.0378
  - C16 | COLLECT | real_69c60af6d4242eda8c47c934:L86 | 信息反馈 | score=0.0420
- projection_chars: 2970

**Step 4** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60af6d4242eda8c47c934:L56` depth=`1`
- reason: The required document section has been collected. Ready to finish.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 189

**Step 5** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60af6d4242eda8c47c934:L31` scope=`real_69c60af6d4242eda8c47c934:L31` depth=`1`
- reason: Collecting the 'Construction Plan' section to retrieve all main entries including schedule, materials, and labor plans.
- collect_section_ids: ['real_69c60af6d4242eda8c47c934:L31']
- collect added=4 hits=4 branch_selected=True collect_full=False
- legal_actions (10):
  - C1 | COLLECT | real_69c60af6d4242eda8c47c934:L31 | 施工计划 | score=0.0584
  - C2 | COLLECT | real_69c60af6d4242eda8c47c934:L32 | 施工进度计划 | score=0.0430
  - C3 | COLLECT | real_69c60af6d4242eda8c47c934:L33 | 基坑工程计划于2025年5月15日开始施工，2025年7月30日施工完成，总工期为76日历天。 | score=0.0346
  - C4 | COLLECT | real_69c60af6d4242eda8c47c934:L34 | 表3.1施工进度计划表 | score=0.0430
  - C5 | COLLECT | real_69c60af6d4242eda8c47c934:L35 | 材料及设备计划 | score=0.0584
  - C6 | COLLECT | real_69c60af6d4242eda8c47c934:L36 | 表3.2土方开挖材料计划表 | score=0.0533
  - C7 | COLLECT | real_69c60af6d4242eda8c47c934:L37 | 表3.3主要设备配置计划 | score=0.0584
  - C8 | COLLECT | real_69c60af6d4242eda8c47c934:L38 | 表3.4 测量设备配置计划表 | score=0.0358
  - C9 | COLLECT | real_69c60af6d4242eda8c47c934:L39 | 劳动力计划 | score=0.0378
  - C10 | COLLECT | real_69c60af6d4242eda8c47c934:L40 | 表3.5劳动力计划表 | score=0.0378
- projection_chars: 1291

**Step 6** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60af6d4242eda8c47c934:L31` depth=`1`
- reason: The document root L31 has been collected, containing the main entries of the excavation plan. No further collection is needed.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 189

**Step 7** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60af6d4242eda8c47c934:L41` scope=`real_69c60af6d4242eda8c47c934:L41` depth=`1`
- reason: Collecting the main section '施工工艺技术' to list its primary entries as requested.
- collect_section_ids: ['real_69c60af6d4242eda8c47c934:L41']
- collect added=6 hits=6 branch_selected=True collect_full=False
- legal_actions (15):
  - C1 | COLLECT | real_69c60af6d4242eda8c47c934:L41 | 施工工艺技术 | score=0.0616
  - C2 | COLLECT | real_69c60af6d4242eda8c47c934:L42 | 技术参数 | score=0.0395
  - C3 | COLLECT | real_69c60af6d4242eda8c47c934:L43 | 表4.1技术参数一览表 | score=0.0395
  - C4 | COLLECT | real_69c60af6d4242eda8c47c934:L44 | 工艺流程 | score=0.0501
  - C5 | COLLECT | real_69c60af6d4242eda8c47c934:L45 | 土方开挖遵循分层分段、自上而下、严禁超挖的原则，与基坑支护施工紧密配合。具体顺序为：测量放线→环基坑一周开挖→支护施工与盆心挖土交替进行（重复上述顺序施工至桩基施工作业面）→桩基施工→下一层支护面开挖、支护施工与盆心挖土（重复至褥垫层工作面）。 | score=0.0501
  - C6 | COLLECT | real_69c60af6d4242eda8c47c934:L46 | 施工方法及操作要求 | score=0.0616
  - C7 | COLLECT | real_69c60af6d4242eda8c47c934:L47 | 施工准备 | score=0.0499
  - C8 | COLLECT | real_69c60af6d4242eda8c47c934:L48 | 内容涵盖基坑开挖前的专项方案编制与审批、技术交底、机械验收、监测方案制定、临时设施布置、现场环保验收及精确测量放样等关键准备工作。 | score=0.0499
  - C9 | COLLECT | real_69c60af6d4242eda8c47c934:L49 | 土方开挖 | score=0.0616
  - C10 | COLLECT | real_69c60af6d4242eda8c47c934:L50 | 本文档详细规定了土方开挖前的排水措施、机械操作规范、人工配合清坡要求。工程分A/B/C/D四区流水施工，分三层开挖至6.8m深，强调雨季防护、边坡监测及严禁超挖等关键安全与质量控制点。 | score=0.0616
  - C11 | COLLECT | real_69c60af6d4242eda8c47c934:L51 | 基坑使用要求 | score=0.0432
  - C12 | COLLECT | real_69c60af6d4242eda8c47c934:L52 | 表4.2基坑使用安全要求 | score=0.0432
  - C13 | COLLECT | real_69c60af6d4242eda8c47c934:L53 | 基坑开挖需巡视边坡稳定，发现异常立即停工撤离。基坑边1.5米内严禁堆载，3米内控制堆载，6米内禁止长时间大量堆载。使用期间应委托第三方监测，达到报警值时及时报告并采取措施，发现险情立即组织人员撤离。 | score=0.0386
  - C14 | COLLECT | real_69c60af6d4242eda8c47c934:L54 | 检查要求 | score=0.0489
  - C15 | COLLECT | real_69c60af6d4242eda8c47c934:L55 | 表4.3基坑土方开挖允许偏差表 | score=0.0489
- projection_chars: 2598

**Step 8** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60af6d4242eda8c47c934:L41` depth=`1`
- reason: The document root L41 has been collected, containing the main entries of the excavation plan. No further collection is needed.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 189

**Step 9** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60af6d4242eda8c47c934:L103` scope=`real_69c60af6d4242eda8c47c934:L103` depth=`1`
- reason: Collects the main structure of 'Acceptance Requirements' section including standards, procedures, and content.
- collect_section_ids: ['real_69c60af6d4242eda8c47c934:L103']
- collect added=4 hits=4 branch_selected=True collect_full=False
- legal_actions (18):
  - C1 | COLLECT | real_69c60af6d4242eda8c47c934:L103 | 验收要求 | score=0.0697
  - C2 | COLLECT | real_69c60af6d4242eda8c47c934:L104 | 验收标准 | score=0.0697
  - C3 | COLLECT | real_69c60af6d4242eda8c47c934:L105 | 土方开挖过程中，项目部组织相关人员对土方开挖标高、长度宽度、边坡、原状地基土等进行复核和验收，填写复核记录和质量验收记录表。 | score=0.0697
  - C4 | COLLECT | real_69c60af6d4242eda8c47c934:L106 | 表7.1土方开挖允许偏差及检验方法 | score=0.0562
  - C5 | COLLECT | real_69c60af6d4242eda8c47c934:L107 | 验收条件 | score=0.0606
  - C6 | COLLECT | real_69c60af6d4242eda8c47c934:L108 | ①分层或分段开挖完成； | score=0.0606
  - C7 | COLLECT | real_69c60af6d4242eda8c47c934:L109 | ②边坡修整完成； | score=0.0457
  - C8 | COLLECT | real_69c60af6d4242eda8c47c934:L110 | ③整体土方开挖完成; | score=0.0594
  - C9 | COLLECT | real_69c60af6d4242eda8c47c934:L111 | ④基坑底控制轴线测设完成； | score=0.0434
  - C10 | COLLECT | real_69c60af6d4242eda8c47c934:L112 | ⑤基坑普探完成； | score=0.0494
  - C11 | COLLECT | real_69c60af6d4242eda8c47c934:L113 | ⑥施工资料齐全有效； | score=0.0494
  - C12 | COLLECT | real_69c60af6d4242eda8c47c934:L114 | ⑦自检合格。 | score=0.0436
  - C13 | COLLECT | real_69c60af6d4242eda8c47c934:L115 | 验收程序及人员 | score=0.0474
  - C14 | COLLECT | real_69c60af6d4242eda8c47c934:L116 | 验收程序 | score=0.0404
  - C15 | COLLECT | real_69c60af6d4242eda8c47c934:L117 | 验收人员 | score=0.0474
  - C16 | COLLECT | real_69c60af6d4242eda8c47c934:L118 | 表7.9验收人员表 | score=0.0474
- projection_chars: 2025

**Step 10** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60af6d4242eda8c47c934:L103` depth=`1`
- reason: The target document section has been collected. No further actions needed.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 190

**Step 11** `nav_collect`  id=`C1` kind=`collect` section=`real_69c60af6d4242eda8c47c934:L120` scope=`real_69c60af6d4242eda8c47c934:L120` depth=`1`
- reason: Collecting the full 'Emergency Response Measures' section to identify main entries of the excavation plan.
- collect_section_ids: ['real_69c60af6d4242eda8c47c934:L120']
- collect added=5 hits=5 branch_selected=True collect_full=False
- legal_actions (18):
  - C1 | COLLECT | real_69c60af6d4242eda8c47c934:L120 | 应急处置措施 | score=0.0670
  - C2 | COLLECT | real_69c60af6d4242eda8c47c934:L121 | 应急处置组织机构及职责分工 | score=0.0670
  - C3 | COLLECT | real_69c60af6d4242eda8c47c934:L122 | 应急处置领导小组 | score=0.0670
  - C4 | COLLECT | real_69c60af6d4242eda8c47c934:L123 | 本工程土方开挖施工最重大的危险源为施工过程中的土方坍塌，会造成严重的后果和影响，因此项目部针对土方开挖坍塌事故成立应急处置领导小组，组长由项目经理担任，副组长由项目总工程师、安全负责人担任，成员由项目部管理人员与劳务分包单位管理人员等组成，应急处置领导小组组织机构如下： | score=0.0670
  - C5 | COLLECT | real_69c60af6d4242eda8c47c934:L124 | 表8.1项目部应急处置领导小组职责 | score=0.0602
  - C6 | COLLECT | real_69c60af6d4242eda8c47c934:L126 | 应急救援小组 | score=0.0589
  - C7 | COLLECT | real_69c60af6d4242eda8c47c934:L127 | 项目部针对土方开挖事故成立应急救援小组，组长由项目经理担任，副组长由项目总工程师、安全负责人担任，成员由项目部管理人员组成，应急救援小组成员名单为： | score=0.0578
  - C8 | COLLECT | real_69c60af6d4242eda8c47c934:L128 | 表8.3项目部应急救援小组成员及联系方式 | score=0.0589
  - C9 | COLLECT | real_69c60af6d4242eda8c47c934:L129 | 表8.4施工单位应急救援小组成员及联系方式 | score=0.0403
  - C10 | COLLECT | real_69c60af6d4242eda8c47c934:L130 | 表8.5应急救援外部单位及联系方式 | score=0.0507
  - C11 | COLLECT | real_69c60af6d4242eda8c47c934:L133 | 应急事件及其应急措施 | score=0.0503
  - C12 | COLLECT | real_69c60af6d4242eda8c47c934:L134 | 高处坠落事故应急措施 | score=0.0412
  - C13 | COLLECT | real_69c60af6d4242eda8c47c934:L135 | 针对基坑边防护缺失导致的坠落事故，内容涵盖危害后果（致命风险）、应急措施（现场急救、警戒通讯、后续处置）及注意事项（禁止不当搬动、防失温），强调规范操作与安全防护。 | score=0.0412
  - C14 | COLLECT | real_69c60af6d4242eda8c47c934:L136 | 物体打击事故应急措施 | score=0.0491
  - C15 | COLLECT | real_69c60af6d4242eda8c47c934:L137 | 针对构配件堆放超高及抛掷引发的物体打击事故，摘要了危害后果、紧急处置流程（如停止作业、侧卧防窒息）、伤情分级处理方案及后续隐患排查与注意事项。 | score=0.0491
  - C16 | COLLECT | real_69c60af6d4242eda8c47c934:L138 | 土方坍塌事故应急措施 | score=0.0503
- projection_chars: 3273

**Step 12** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`real_69c60af6d4242eda8c47c934:L120` depth=`1`
- reason: The document root L120 has been collected, which contains the target file '9.1土方开挖方案范本.docx'. No further collection is needed.
- legal_actions (1):
  - F1 | FINISH | finish navigation and pack final evidence budget
- projection_chars: 190

**Step 13** `nav_dispatch`  id=`D1` kind=`dispatch` section=`real_69c60af6d4242eda8c47c934:L1` scope=`None` depth=`0`
- reason: Dispatch major sections to gather main entries of the excavation plan efficiently.
- dispatch_regions: ['real_69c60af6d4242eda8c47c934:L1', 'real_69c60af6d4242eda8c47c934:L31', 'real_69c60af6d4242eda8c47c934:L41', 'real_69c60af6d4242eda8c47c934:L56', 'real_69c60af6d4242eda8c47c934:L103', 'real_69c60af6d4242eda8c47c934:L120']
- child_reports=6 skipped=0
- legal_actions (63):
  - C1 | COLLECT | real_69c60af6d4242eda8c47c934:L1 | 工程概况 | score=0.0655
  - D1 | DISPATCH | real_69c60af6d4242eda8c47c934:L1 | 工程概况 | score=0.0655
  - C2 | COLLECT | real_69c60af6d4242eda8c47c934:L11 | 周边环境条件 | score=0.0539
  - D2 | DISPATCH | real_69c60af6d4242eda8c47c934:L11 | 周边环境条件 | score=0.0539
  - C3 | COLLECT | real_69c60af6d4242eda8c47c934:L14 | 表1.4项目气候统计表 | score=0.0539
  - C4 | COLLECT | real_69c60af6d4242eda8c47c934:L22 | 施工要求 | score=0.0655
  - D3 | DISPATCH | real_69c60af6d4242eda8c47c934:L22 | 施工要求 | score=0.0655
  - C5 | COLLECT | real_69c60af6d4242eda8c47c934:L23 | 表1.5工程目标及基坑分项工程目标表 | score=0.0655
  - C6 | COLLECT | real_69c60af6d4242eda8c47c934:L24 | 表1.6土方开挖施工周期表 | score=0.0557
  - C7 | COLLECT | real_69c60af6d4242eda8c47c934:L31 | 施工计划 | score=0.0584
  - D4 | DISPATCH | real_69c60af6d4242eda8c47c934:L31 | 施工计划 | score=0.0584
  - C8 | COLLECT | real_69c60af6d4242eda8c47c934:L35 | 材料及设备计划 | score=0.0584
  - D5 | DISPATCH | real_69c60af6d4242eda8c47c934:L35 | 材料及设备计划 | score=0.0584
  - C9 | COLLECT | real_69c60af6d4242eda8c47c934:L37 | 表3.3主要设备配置计划 | score=0.0584
  - C10 | COLLECT | real_69c60af6d4242eda8c47c934:L41 | 施工工艺技术 | score=0.0616
  - D6 | DISPATCH | real_69c60af6d4242eda8c47c934:L41 | 施工工艺技术 | score=0.0616
- projection_chars: 3199

**Step 14** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: All main entries of the excavation plan have been collected and assembled in evidence groups.
- legal_actions (36):
  - C1 | COLLECT | real_69c60af6d4242eda8c47c934:L30 | 编制依据 | score=0.0391
  - C2 | COLLECT | real_69c60af6d4242eda8c47c934:L90 | 施工管理及作业人员配备及分工 | score=0.0564
  - D1 | DISPATCH | real_69c60af6d4242eda8c47c934:L90 | 施工管理及作业人员配备及分工 | score=0.0564
  - C3 | COLLECT | real_69c60af6d4242eda8c47c934:L91 | 施工管理人员 | score=0.0539
  - D2 | DISPATCH | real_69c60af6d4242eda8c47c934:L91 | 施工管理人员 | score=0.0539
  - C4 | COLLECT | real_69c60af6d4242eda8c47c934:L92 | 在土方开挖施工管理中，应建立专职组织管理机构进行重点管理，合理设置岗位，明确岗位职责，确保施工进度、质量、安全满足要求。具体如下表： | score=0.0539
  - C5 | COLLECT | real_69c60af6d4242eda8c47c934:L93 | 表6.1管理人员及分工计划表 | score=0.0422
  - C6 | COLLECT | real_69c60af6d4242eda8c47c934:L94 | 专职安全生产管理人员 | score=0.0362
  - D3 | DISPATCH | real_69c60af6d4242eda8c47c934:L94 | 专职安全生产管理人员 | score=0.0362
  - C7 | COLLECT | real_69c60af6d4242eda8c47c934:L95 | 表6.2专职安全生产管理人员计划表 | score=0.0362
  - C8 | COLLECT | real_69c60af6d4242eda8c47c934:L96 | 特种作业人员 | score=0.0564
  - D4 | DISPATCH | real_69c60af6d4242eda8c47c934:L96 | 特种作业人员 | score=0.0564
  - C9 | COLLECT | real_69c60af6d4242eda8c47c934:L97 | 为确保工程进度的需要，同时根据本工程的特征和土方开挖的工程量，确定本工程土方开挖按下表配置人力资源，特种作业人员均需持证上岗。 | score=0.0564
  - C10 | COLLECT | real_69c60af6d4242eda8c47c934:L98 | 表6.3特种作业人员计划表 | score=0.0372
  - C11 | COLLECT | real_69c60af6d4242eda8c47c934:L99 | 表6.4特种作业人员证件统计表 | score=0.0341
  - C12 | COLLECT | real_69c60af6d4242eda8c47c934:L100 | 其他作业人员 | score=0.0553
- projection_chars: 1951

### Subagent reports_context

```
=== Investigate results (6 region(s)) ===
[region 1] real_69c60af6d4242eda8c47c934:L1 (ok)
collected 29 branch node(s); explicit roots=['real_69c60af6d4242eda8c47c934:L1']
collected: real_69c60af6d4242eda8c47c934:L1, real_69c60af6d4242eda8c47c934:L10, real_69c60af6d4242eda8c47c934:L11, real_69c60af6d4242eda8c47c934:L12, real_69c60af6d4242eda8c47c934:L13, real_69c60af6d4242eda8c47c934:L14, real_69c60af6d4242eda8c47c934:L15, real_69c60af6d4242eda8c47c934:L16, real_69c60af6d4242eda8c47c934:L17, real_69c60af6d4242eda8c47c934:L18, real_69c60af6d4242eda8c47c934:L19, real_69c60af6d4242eda8c47c934:L2, real_69c60af6d4242eda8c47c934:L20, real_69c60af6d4242eda8c47c934:L21, real_69c60af6d4242eda8c47c934:L22, real_69c60af6d4242eda8c47c934:L23, real_69c60af6d4242eda8c47c934:L24, real_69c60af6d4242eda8c47c934:L25, real_69c60af6d4242eda8c47c934:L26, real_69c60af6d4242eda8c47c934:L27
reason: The document root has been collected, which contains the main entries of the土方开挖方案范本.
---
[region 2] real_69c60af6d4242eda8c47c934:L56 (ok)
collected 34 branch node(s); explicit roots=['real_69c60af6d4242eda8c47c934:L56']
collected: real_69c60af6d4242eda8c47c934:L56, real_69c60af6d4242eda8c47c934:L57, real_69c60af6d4242eda8c47c934:L58, real_69c60af6d4242eda8c47c934:L59, real_69c60af6d4242eda8c47c934:L60, real_69c60af6d4242eda8c47c934:L61, real_69c60af6d4242eda8c47c934:L62, real_69c60af6d4242eda8c47c934:L63, real_69c60af6d4242eda8c47c934:L64, real_69c60af6d4242eda8c47c934:L65, real_69c60af6d4242eda8c47c934:L66, real_69c60af6d4242eda8c47c934:L67, real_69c60af6d4242eda8c47c934:L68, real_69c60af6d4242eda8c47c934:L69, real_69c60af6d4242eda8c47c934:L70, real_69c60af6d4242eda8c47c934:L71, real_69c60af6d4242eda8c47c934:L72, real_69c60af6d4242eda8c47c934:L73, real_69c60af6d4242eda8c47c934:L74, real_69c60af6d4242eda8c47c934:L75
reason: The required document section has been collected. Ready to finish.
---
[region 3] real_69c60af6d4242eda8c47c934:L31 (ok)
collected 10 branch node(s); explicit roots=['real_
```

### Evidence text (new)

```
[E1]
[§ 工程概况]
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
  施工要求
  表1.5工程目标及基坑分项工程目标表
  表1.6土方开挖施工周期表
  风险辨识与分级
  表1.7风险辨识与分级
  参建各方责任主体单位
  表1.8参建单位责任主体名称
  表1.9质量监督单位

[E2]
[§ 施工计划]
材料及设备计划
表3.2土方开挖材料计划表
表3.3主要设备配置计划
```

### Evidence text (old)

```
[E1]
9.1土方开挖方案范本.docx

[E2]
工程概况
基坑工程概况和特点
工程基本情况

[E3]
编制依据

[E4]
施工计划
施工进度计划
基坑工程计划于2025年5月15日开始施工，2025年7月30日施工完成，总工期为76日历天。

[E5]
施工工艺技术
技术参数
表4.1技术参数一览表

[E6]
施工保证措施
组织保障措施
安全组织机构

[E7]
施工管理及作业人员配备及分工
施工管理人员
在土方开挖施工管理中，应建立专职组织管理机构进行重点管理，合理设置岗位，明确岗位职责，确保施工进度、质量、安全满足要求。具体如下表：

[E8]
验收要求
验收标准
土方开挖过程中，项目部组织相关人员对土方开挖标高、长度宽度、边坡、原状地基土等进行复核和验收，填写复核记录和质量验收记录表。

[E9]
应急处置措施
应急处置组织机构及职责分工
应急处置领导小组

[E10]
计算书及相关图纸
计算书
计算书内容应明确以下主要内容：（自然放坡计算边坡稳定性）

[E11]
附件：方案报批，专业分包需提供资料

[E12]
周边环境条件
表1.3周边环境统计表
项目北侧为沣
```

## real_69c60974d4242eda8c47c615_scope_collection_auto_0030 (scope_collection)

**Query:** 列出重大事故隐患治理方案必须包含的所有内容要素。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 495 |
| gold_node_recall | 0.0 | 0.8333 |
| n_retrieved_nodes | 12 | 9 |
| trajectory_steps | n/a | 3 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L94` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L95` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L96` [MISS] retrieved=False in_text=False
- `real_69c60974d4242eda8c47c615:L97` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L98` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L99` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C20` kind=`collect` section=`real_69c60974d4242eda8c47c615:L93` scope=`None` depth=`0`
- reason: Collect specific content elements of major accident hazard governance plans from section 2.4.4.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L93', 'real_69c60974d4242eda8c47c615:L98']
- collect added=2 hits=2 branch_selected=True collect_full=True
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

**Step 2** `nav_collect`  id=`C19` kind=`collect` section=`real_69c60974d4242eda8c47c615:L92` scope=`None` depth=`0`
- reason: Collect section 2.4.4 to retrieve the full list of required elements for major accident hazard governance plans.
- collect_section_ids: ['real_69c60974d4242eda8c47c615:L92']
- collect added=11 hits=11 branch_selected=True collect_full=True
- legal_actions (57):
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
- projection_chars: 3552

**Step 3** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Assembled evidence G1 fully lists all required elements for major accident hazard governance plans.
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

### Evidence text (new)

```
[E1]
[§ 2.4.4 重大事故隐患整改、复查、销项]
  2.4.5 各项目在事故隐患治理过程中，应当采取相应的安全防范措施，防止事故发生。事故隐患排除前或者排除过程中无法保证安全的，应当从危险区域内撤出作业人员，并疏散可能危及的其他人员，设置警戒标志，暂时停工；对暂时难以停工或者停止使用的相关生产储存装置、设施、设备，应当加强维护和保养，防止事故发生。
  2.4.6 各项目部应当加强对自然灾害的预防。对于因自然灾害可能导致事故灾难的隐患，应当按照有关法律、法规、标准和本制度的要求排查治理，采取可靠的预防措施，制定应急预案。在接到有关自然灾害预报时，应当及时向有关人员发出预警通知；发生自然灾害可能危及施工和人员安全的情况时，应当采取撤离人员、停止作业、加强监测等安全措施，并及时向当地人民政府有关部门报告。
  对重大事故隐患，由被检查项目负责整改，整改应制定事故隐患治理方案，该方案由项目经理组织制定和实施。方案包括以下内容：
  1、治理的目标和任务；
  2、采取的方法和措施；
  4、负责治理的机构和人员；
  5、治理的时限和要求；
  6、安全措施和应急预案。
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
