# Map-Nav Trace Replay (recursive DISPATCH)

- generated_at: `2026-07-15T12:24:25`
- nav_map_mode: `1`
- enable_recursive_dispatch: `False`
- embedding: `text-embedding-v3`

## real_69c60974d4242eda8c47c615_scope_collection_auto_0030 (scope_collection)

**Query:** 列出重大事故隐患治理方案必须包含的所有内容要素。

**Doc:** `real_69c60974d4242eda8c47c615`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 460 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 12 | 11 |
| trajectory_steps | n/a | 7 |

### Gold node hits (new)

- `real_69c60974d4242eda8c47c615:L94` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L95` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L96` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L97` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L98` [HIT] retrieved=True in_text=False
- `real_69c60974d4242eda8c47c615:L99` [HIT] retrieved=True in_text=False

### Step decisions

**Step 1** `nav_collect`  id=`C2` kind=`collect` section=`real_69c60974d4242eda8c47c615:L93` scope=`real_69c60974d4242eda8c47c615:L92` depth=`1`
- reason: Collect the specific 6 elements of the major accident hazard governance plan as listed in the document.
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
- reason: Section 2.4.4 explicitly lists the required content elements for the major accident hazard governance plan.
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

**Step 5** `nav_collect`  id=`C10` kind=`collect` section=`real_69c60974d4242eda8c47c615:L82` scope=`None` depth=`0`
- reason: Collect definition of major accident hazards to ensure governance plan elements are identified.
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
- reason: Collects the definition of major accident hazards, a key element for governance plans.
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
- reason: Collected evidence from L92 and L93 contains all required elements for major accident hazard governance plans.
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
