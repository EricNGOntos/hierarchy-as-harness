# Map-Nav Trace Replay (recursive DISPATCH)

- generated_at: `2026-07-15T16:04:36`
- nav_map_mode: `1`
- enable_recursive_dispatch: `False`
- embedding: `text-embedding-v3`

## real_69cb12d0919452cda2225a0b_scope_collection_auto_0076 (scope_collection)

**Query:** 列出办理《跨区域涉税事项备案》时需注意的所有事项要点。

**Doc:** `real_69cb12d0919452cda2225a0b`

### Evidence comparison

| | old Gold Nav | new Map-Nav |
|---|---:|---:|
| score_task | 0.0 | None |
| score_evidence | 0.0 | None |
| evidence_chars | 500 | 492 |
| gold_node_recall | 0.0 | 0.5 |
| n_retrieved_nodes | 6 | 18 |
| trajectory_steps | n/a | 5 |

### Gold node hits (new)

- `real_69cb12d0919452cda2225a0b:L141` [MISS] retrieved=False in_text=False
- `real_69cb12d0919452cda2225a0b:L142` [HIT] retrieved=True in_text=False
- `real_69cb12d0919452cda2225a0b:L143` [HIT] retrieved=True in_text=False
- `real_69cb12d0919452cda2225a0b:L144` [MISS] retrieved=False in_text=False
- `real_69cb12d0919452cda2225a0b:L145` [HIT] retrieved=True in_text=False
- `real_69cb12d0919452cda2225a0b:L146` [MISS] retrieved=False in_text=False
- `real_69cb12d0919452cda2225a0b:L147` [MISS] retrieved=False in_text=False
- `real_69cb12d0919452cda2225a0b:L148` [HIT] retrieved=True in_text=False

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
- reason: Evidence G1 fully covers all required points for cross-regional tax filing procedures.
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
  （1）开具与报验
  办理跨区域涉税事项备案需注意事项：
  - 2）项目地址：不是甲方机构所在地，应填写项目所在地省、市、区（县）。（注意：
  - 5）《跨区域涉税事项报告》自办理之日起 30 日内在项目所在地税务机关报验，到
  - 6）《跨区域涉税事项报告》政策如有变化，依照国家税务总局政策适时调整。 （2）延期与核销
  在项目所在地税务机关报验时，需提供以下资料：
  - 1）《跨区域涉税事项报告》
  - 3）营业执照复印件
  - 4）法人与经办人身份复印件
  - 《跨区域涉税事项报告》初次办理有效期为 360 天，到期日项目未完工的，应于到
  - 并将已核销的备案表交回集团财务管理服务中心留存。
  - 办理核销，需向项目所在地税务机关提供以下资料：
  - 1）《跨区域涉税事项报告》
  - 3）营业执照复印件
  - 5）《跨区域涉税事项报告》所属期间，所有发票复印件以及完税证复印件。
  - 上述所有向税务机关提供的资料，必须都要加盖集团公章。
  3.2.4.3 台账管理
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
| evidence_chars | 500 | 484 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 12 | 11 |
| trajectory_steps | n/a | 4 |

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

**Step 4** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
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

### Subagent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60974d4242eda8c47c615:L92 (ok)
collected 12 branch node(s); explicit roots=['real_69c60974d4242eda8c47c615:L92']
collected: real_69c60974d4242eda8c47c615:L100, real_69c60974d4242eda8c47c615:L101, real_69c60974d4242eda8c47c615:L102, real_69c60974d4242eda8c47c615:L103, real_69c60974d4242eda8c47c615:L92, real_69c60974d4242eda8c47c615:L93, real_69c60974d4242eda8c47c615:L94, real_69c60974d4242eda8c47c615:L95, real_69c60974d4242eda8c47c615:L96, real_69c60974d4242eda8c47c615:L97, real_69c60974d4242eda8c47c615:L98, real_69c60974d4242eda8c47c615:L99
reason: Collected section L92 contains the required elements for major accident hazard governance plans.
---
=== End Investigate ===
```

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
| evidence_chars | 142 | 405 |
| gold_node_recall | 0.0 | 1.0 |
| n_retrieved_nodes | 2 | 5 |
| trajectory_steps | n/a | 4 |

### Gold node hits (new)

- `real_69c6095ed4242eda8c47c5b2:L34` [HIT] retrieved=True in_text=False
- `real_69c6095ed4242eda8c47c5b2:L35` [HIT] retrieved=True in_text=False

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

**Step 4** `nav_finish`  id=`F1` kind=`finish` section=`None` scope=`None` depth=`0`
- reason: Evidence G1 contains the complete 'Course Development Management' section with all adjacent points (development, review, upload, remuneration).
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
| evidence_chars | 495 | 498 |
| gold_node_recall | 0.0 | 0.0 |
| n_retrieved_nodes | 11 | 18 |
| trajectory_steps | n/a | 4 |

### Gold node hits (new)

- `real_69c60970d4242eda8c47c5fd:L7` [MISS] retrieved=False in_text=False
- `real_69c60970d4242eda8c47c5fd:L8` [MISS] retrieved=False in_text=False

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
- reason: Evidence collected covers Chapter 2 scope and types. G2 details prohibited assets (scope), G1 details donation categories (types).
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

[E2]
[§ 第四条  对外捐赠的类型]
  （一）救济性捐赠，即向受灾地区、扶贫地区或者困难的社会弱势群体的救济性捐赠。
  （二）公益性捐赠，即向科技文卫事业和环境保护等社会公益事业的公益性捐赠。
  （三）其他捐赠，即除上述捐赠外，为促进社会发展以及集团公司履行社会责任需要的其他捐赠，含外部各类活动赞助。
  各单位要正确参与社会公益事业，依法依规确定对外捐赠范围和支出规模，规范开展对外捐赠活动，避免无序、随意捐赠等行为。对于有关社会机构、团体的摊派性捐赠，要坚决依法拒绝，
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
- reason: All relevant sections regarding the learning management scheme have been collected and assembled.
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
