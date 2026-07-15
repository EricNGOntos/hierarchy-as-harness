# Map-Nav 运行报告

- generated_at: `2026-07-15T17:48:09`
- env: EMBEDDING_MODEL=`text-embedding-v3` · NAV_MAP_MODE=`1` · enable_recursive_dispatch=`False` · map_char_limit=`5000` · max_steps=`8` · navigate_max_steps=`8`
- 汇总: 99 case · PASS 66/99 · mean gold_recall 0.597

| inspect_id | task_type | gold_recall | evidence_chars | steps |
|---|---|---:|---:|---:|
| latest_clean_multi_0010 | multi_hop | 0.50 | 487 | 4 |
| latest_clean_multi_0051 | multi_hop | 1.00 | 243 | 2 |
| latest_clean_multi_0064 | multi_hop | 0.50 | 484 | 2 |
| latest_clean_multi_0075 | multi_hop | 0.00 | 292 | 3 |
| latest_clean_multi_0133 | multi_hop | 1.00 | 488 | 5 |
| latest_clean_multi_0158 | multi_hop | 0.50 | 246 | 3 |
| latest_clean_multi_0180 | multi_hop | 0.00 | 479 | 2 |
| latest_clean_multi_0202 | multi_hop | 1.00 | 490 | 2 |
| latest_clean_multi_0223 | multi_hop | 1.00 | 184 | 2 |
| latest_clean_multi_0226 | multi_hop | 0.50 | 160 | 3 |
| latest_clean_multi_0227 | multi_hop | 1.00 | 239 | 2 |
| latest_clean_multi_0230 | multi_hop | 0.00 | 484 | 2 |
| latest_clean_multi_0296 | multi_hop | 0.00 | 460 | 2 |
| latest_clean_multi_0303 | multi_hop | 1.00 | 485 | 2 |
| latest_clean_multi_0309 | multi_hop | 1.00 | 465 | 4 |
| latest_clean_multi_0324 | multi_hop | 1.00 | 500 | 5 |
| latest_clean_multi_0362 | multi_hop | 1.00 | 445 | 2 |
| latest_clean_multi_0415 | multi_hop | 0.50 | 490 | 2 |
| latest_clean_multi_0462 | multi_hop | 0.50 | 473 | 2 |
| latest_clean_multi_0469 | multi_hop | 1.00 | 492 | 2 |
| latest_clean_multi_0475 | multi_hop | 0.50 | 489 | 2 |
| latest_clean_multi_0484 | multi_hop | 1.00 | 490 | 2 |
| latest_clean_multi_0502 | multi_hop | 1.00 | 390 | 2 |
| latest_clean_multi_0518 | multi_hop | 1.00 | 182 | 2 |
| latest_clean_multi_0521 | multi_hop | 1.00 | 356 | 2 |
| latest_clean_multi_0527 | multi_hop | 1.00 | 414 | 2 |
| latest_clean_multi_0544 | multi_hop | 1.00 | 195 | 2 |
| latest_clean_multi_0552 | multi_hop | 1.00 | 500 | 4 |
| latest_clean_multi_0554 | multi_hop | 0.50 | 461 | 7 |
| latest_clean_multi_0555 | multi_hop | 1.00 | 488 | 3 |
| latest_clean_multi_0568 | multi_hop | 0.00 | 413 | 4 |
| latest_clean_multi_0572 | multi_hop | 0.00 | 476 | 8 |
| latest_clean_multi_0573 | multi_hop | 0.00 | 148 | 3 |
| latest_clean_multi_0712 | multi_hop | 0.50 | 492 | 4 |
| latest_clean_multi_0742 | multi_hop | 1.00 | 489 | 2 |
| latest_clean_multi_0760 | multi_hop | 1.00 | 500 | 2 |
| real_69c6ef484cca74801cb63bb9_multi_hop_auto_0003 | multi_hop | 0.00 | 492 | 7 |
| real_69c6ef484cca74801cb63bb9_multi_hop_auto_0006 | multi_hop | 0.00 | 482 | 8 |
| latest_clean_niche_0036 | niche_fact | 1.00 | 360 | 6 |
| latest_clean_niche_0068 | niche_fact | 1.00 | 465 | 4 |
| latest_clean_niche_0160 | niche_fact | 1.00 | 492 | 2 |
| latest_clean_niche_0175 | niche_fact | 1.00 | 490 | 2 |
| latest_clean_niche_0214 | niche_fact | 1.00 | 464 | 2 |
| latest_clean_niche_0219 | niche_fact | 1.00 | 184 | 2 |
| latest_clean_niche_0222 | niche_fact | 1.00 | 74 | 2 |
| latest_clean_niche_0223 | niche_fact | 1.00 | 239 | 2 |
| latest_clean_niche_0226 | niche_fact | 1.00 | 481 | 2 |
| latest_clean_niche_0249 | niche_fact | 0.00 | 499 | 2 |
| latest_clean_niche_0258 | niche_fact | 1.00 | 470 | 2 |
| latest_clean_niche_0306 | niche_fact | 0.00 | 494 | 5 |
| latest_clean_niche_0321 | niche_fact | 1.00 | 276 | 2 |
| latest_clean_niche_0325 | niche_fact | 1.00 | 492 | 2 |
| latest_clean_niche_0413 | niche_fact | 1.00 | 497 | 2 |
| latest_clean_niche_0460 | niche_fact | 0.00 | 473 | 2 |
| latest_clean_niche_0473 | niche_fact | 0.00 | 489 | 2 |
| latest_clean_niche_0500 | niche_fact | 1.00 | 390 | 2 |
| latest_clean_niche_0510 | niche_fact | 1.00 | 423 | 2 |
| latest_clean_niche_0519 | niche_fact | 1.00 | 356 | 2 |
| latest_clean_niche_0525 | niche_fact | 1.00 | 414 | 2 |
| latest_clean_niche_0531 | niche_fact | 0.00 | 478 | 2 |
| latest_clean_niche_0551 | niche_fact | 1.00 | 498 | 3 |
| latest_clean_niche_0553 | niche_fact | 1.00 | 462 | 8 |
| latest_clean_niche_0554 | niche_fact | 0.00 | 171 | 5 |
| latest_clean_niche_0567 | niche_fact | 1.00 | 304 | 5 |
| latest_clean_niche_0572 | niche_fact | 0.00 | 53 | 2 |
| latest_clean_niche_0600 | niche_fact | 1.00 | 350 | 2 |
| latest_clean_niche_0657 | niche_fact | 1.00 | 496 | 4 |
| latest_clean_niche_0690 | niche_fact | 1.00 | 500 | 2 |
| latest_clean_niche_0711 | niche_fact | 0.00 | 500 | 2 |
| latest_clean_niche_0741 | niche_fact | 1.00 | 490 | 4 |
| latest_clean_niche_0759 | niche_fact | 1.00 | 492 | 2 |
| latest_clean_niche_0795 | niche_fact | 1.00 | 492 | 4 |
| latest_clean_niche_0811 | niche_fact | 1.00 | 500 | 2 |
| latest_clean_niche_0821 | niche_fact | 1.00 | 497 | 2 |
| latest_clean_scope_0053 | scope_collection | 0.00 | 493 | 31 |
| latest_clean_scope_0092 | scope_collection | 0.00 | 215 | 2 |
| latest_clean_scope_0096 | scope_collection | 0.00 | 500 | 7 |
| latest_clean_scope_0097 | scope_collection | 0.00 | 445 | 4 |
| latest_clean_scope_0101 | scope_collection | 0.00 | 158 | 3 |
| latest_clean_scope_0102 | scope_collection | 0.00 | 499 | 3 |
| latest_clean_scope_0110 | scope_collection | 1.00 | 204 | 5 |
| latest_clean_scope_0124 | scope_collection | 0.00 | 494 | 4 |
| latest_clean_scope_0129 | scope_collection | 0.00 | 181 | 2 |
| latest_clean_scope_0132 | scope_collection | 0.00 | 211 | 2 |
| latest_clean_scope_0135 | scope_collection | 0.00 | 181 | 2 |
| latest_clean_scope_0139 | scope_collection | 0.17 | 491 | 6 |
| real_69c6ef4e4cca74801cb63bc6_scope_collection_auto_0061 | scope_collection | 0.00 | 494 | 3 |
| real_69c6ef4e4cca74801cb63bc6_scope_collection_auto_0062 | scope_collection | 0.00 | 443 | 3 |
| real_69c6ef4e4cca74801cb63bc6_scope_collection_auto_0063 | scope_collection | 0.00 | 489 | 2 |
| real_69c6ef4e4cca74801cb63bc6_scope_collection_auto_0064 | scope_collection | 0.00 | 202 | 2 |
| real_69cb12d0919452cda2225a0b_scope_collection_auto_0073 | scope_collection | 0.00 | 493 | 8 |
| real_69cb12d0919452cda2225a0b_scope_collection_auto_0076 | scope_collection | 0.12 | 499 | 2 |
| latest_clean_multi_0032 | multi_hop | 1.00 | 405 | 2 |
| latest_clean_multi_0048 | multi_hop | 1.00 | 491 | 4 |
| latest_clean_niche_0023 | niche_fact | 1.00 | 405 | 3 |
| latest_clean_niche_0043 | niche_fact | 1.00 | 243 | 2 |
| latest_clean_scope_0116 | scope_collection | 0.00 | 499 | 5 |
| latest_clean_scope_0119 | scope_collection | 0.50 | 487 | 14 |
| real_69c60974d4242eda8c47c615_scope_collection_auto_0030 | scope_collection | 0.83 | 495 | 3 |

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
| elapsed_sec | - | 0.21 |

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

## latest_clean_multi_0051  ·  multi_hop

- **Query:** 根据《集团公司对外捐赠管理办法（修订版）》中“第四条 对外捐赠的类型”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60970d4242eda8c47c5fd`
- **Gold nodes:** L11, L12

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 243 |
| n_retrieved_nodes | 11 | 5 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 2.49 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L11` | ✅ | True | False |
| `L12` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C10` collect L10 (depth=0) · →L10 · +4
  - reason: Collect section 4 on donation types to answer the query about adjacent evidence points.
- `F1` finish - (depth=0)
  - reason: Assembled evidence G1 contains the complete content of Article 4 regarding donation types, sufficient to answer the query.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C10` | `L10` | - | 4 | 4 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 第四条  对外捐赠的类型]
  （一）救济性捐赠，即向受灾地区、扶贫地区或者困难的社会弱势群体的救济性捐赠。
  （二）公益性捐赠，即向科技文卫事业和环境保护等社会公益事业的公益性捐赠。
  （三）其他捐赠，即除上述捐赠外，为促进社会发展以及集团公司履行社会责任需要的其他捐赠，含外部各类活动赞助。
  各单位要正确参与社会公益事业，依法依规确定对外捐赠范围和支出规模，规范开展对外捐赠活动，避免无序、随意捐赠等行为。对于有关社会机构、团体的摊派性捐赠，要坚决依法拒绝，

- retrieved_nodes: L10, L11⭐, L12⭐, L13, L14


---

## latest_clean_multi_0064  ·  multi_hop

- **Query:** 根据《集团公司对外捐赠管理办法（修订版）》中“第四章 对外捐赠的审批程序”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60970d4242eda8c47c5fd`
- **Gold nodes:** L35, L36

### 结果得分 — **PASS** (new gold_recall=0.50)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.50 |
| evidence_chars | 236 | 484 |
| n_retrieved_nodes | 3 | 7 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 2.32 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L35` | ❌ | False | False |
| `L36` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C21` collect L34 (depth=0) · multi→[L34, L37, L38] · +8
  - reason: Collect Chapter 4 sections C24 and C25 to explain the two adjacent approval procedure points.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains Chapter 4 approval procedures with all required points for the query.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C21` | `L34` | L34, L37, L38 | 8 | 10 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 第四章  对外捐赠的审批程序]
  凡涉及对外捐赠事宜，不论捐赠支出规模大小，必须经过严格的审批流程，未经批准的捐赠行为一律不得实施。
  （一）各单位需在本单位内部履行“三重一大”决策程序后，以书面请示报送集团公司办公室。请示材料应包括对外捐赠请示（包括捐赠金额、捐赠原因、捐赠类型、捐赠性质和受赠对象的基本情况等）、“三重一大”决策情况、财务部门审核意见等。
  （二）经集团公司党委会前置研究、董事会审议同意后报送陕建控股集团核准。经陕建控股集团研究决定后，给予书面答复。
  （三）所有捐赠事宜得到陕建控股集团批复同意后，由捐赠单位会同集团公司财务管理服务中心办理捐赠有关手续。
  （四）对于突发性重大自然灾害或者其他特殊事项需要紧急安排对外捐赠支出，不论金额大小，各单位在履行内部决策程序后，可先向集团公司办公室口头请示或备案后进行捐赠。并在事后在3个工作日内逐笔履行相应审批程序，并向集团公司报送对外捐赠事项相关情况，由集团公司财务管理服务中心向陕建控股集团履行相应程序。
  （五）集团公司公益基金对外捐赠按照公益基金相关管理办法执行。

- retrieved_nodes: L34, L36⭐, L37, L38, L39, L40, L41


---

## latest_clean_multi_0075  ·  multi_hop

- **Query:** 根据《陕西建工第十一建设集团有限公司印章管理办法（2020版）》中“陕西建工第十一建设集团有限公司印章管理办法（2020版）.docx”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60971d4242eda8c47c605`
- **Gold nodes:** L2, L3

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 292 |
| n_retrieved_nodes | 9 | 4 |
| trajectory_steps | - | 3 |
| elapsed_sec | - | 4.19 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L2` | ❌ | False | False |
| `L3` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C3` collect L19 (depth=0) · multi→[L19, L21] · +2
  - reason: Select adjacent leaf nodes C3 and C4 to extract key points regarding seal creation and project department seal usage procedures.
- `C7` collect L24 (depth=0) · multi→[L24, L56] · +2
  - reason: Collect adjacent sections C7 and C15 to compare their key points as requested.
- `F1` finish - (depth=0)
  - reason: Evidence collected covers both adjacent sections: G2 (Chapter 2) and G1 (Article 12). Ready to answer.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C3` | `L19` | L19, L21 | 2 | 2 | - | ✅ |
| 2 | `C7` | `L24` | L24, L56 | 2 | 2 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 第二章	印章的刻制与启用]
  确因工作需要刻制印章的，由用印单位或部门提出申请，详细说明印章的名称、用途、式样和规格，报集团公司主要领导批准后由办公室制发。
  第七条项目部印章在使用前，项目部应负责将集团公司办公室出具的印章启用文件报送建设单位、监理单位等相关方，以便业务往来确认。并在文件送达后一周内将回执返回集团公司办公室留存。
  印章责任管理单位应将印章遗失报告、遗失声明、告知函回复等相关资料在一月内报集团公司办公室，以备查考。

**[E2]** [§ 第十二条 项目部印章使用范围]
（七）项目印章应在项目负责人审批后用印，用印内容不得违背施工合同要件内容。

- retrieved_nodes: L19, L21, L24, L56


---

## latest_clean_multi_0133  ·  multi_hop

- **Query:** 根据《陕西建工第十一建设集团有限公司印章管理办法（2020版）》中“第五章 印章管理”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60971d4242eda8c47c605`
- **Gold nodes:** L74, L75

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 488 |
| n_retrieved_nodes | 9 | 8 |
| trajectory_steps | - | 5 |
| elapsed_sec | - | 8.14 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L74` | ✅ | True | False |
| `L75` | ✅ | True | False |

### 决策 TRACE(因果序)

- `D6` dispatch L73 (depth=0) · regions=[L73] · child_reports=1
  - reason: Dispatch Chapter 5 to gather evidence for the two adjacent points on seal management.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C2` collect L75 (depth=1) · multi→[L75, L88] · +2
      - reason: Collecting C2 (responsibility management) and C9 (sealing standards) to address the query about adjacent evidence points.
    - `C1` collect L73 (depth=1) · multi→[L73, L74, L77, L80, L81, L82, L84, L85, L89, L92, L95, L96, L98, L99] · +29 · PURGED後代×7
      - reason: Collecting all relevant sections under Chapter 5 to extract key points for the two adjacent evidence items.
    - `F1` finish - (depth=1)
      - reason: Collected evidence from L73 and L75 covers Chapter 5 requirements. Ready to answer query.
- `F1` finish - (depth=0)
  - reason: G3 covers Chapter 5 management responsibilities and G2 covers supervision requirements, addressing the query.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C2` | `L75` | L75, L88 | 2 | 2 | - | ✅ |
| 2 | `C1` | `L73` | L73, L74, L77, L80, L81, L82, L84, L85, L89, L92, L95, L96, L98, L99 | 29 | 41 | 7 | ✅ |

**水合告警:**
- step 1 整枝水合含 1 个非 gold 叶 (与 gold 争抢 evidence 预算)。
- step 2 `C1` 收父节点 `L73` 时 **purge 掉 7 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。
- step 2 整枝水合含 13 个非 gold 叶 (与 gold 争抢 evidence 预算)。

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60971d4242eda8c47c605:L73 (ok)
collected 28 branch node(s); explicit roots=['real_69c60971d4242eda8c47c605:L75', 'real_69c60971d4242eda8c47c605:L73']
collected: real_69c60971d4242eda8c47c605:L100, real_69c60971d4242eda8c47c605:L73, real_69c60971d4242eda8c47c605:L74, real_69c60971d4242eda8c47c605:L75, real_69c60971d4242eda8c47c605:L76, real_69c60971d4242eda8c47c605:L77, real_69c60971d4242eda8c47c605:L78, real_69c60971d4242eda8c47c605:L79, real_69c60971d4242eda8c47c605:L80, real_69c60971d4242eda8c47c605:L81, real_69c60971d4242eda8c47c605:L82, real_69c60971d4242eda8c47c605:L83, real_69c60971d4242eda8c47c605:L84, real_69c60971d4242eda8c47c605:L85, real_69c60971d4242eda8c47c605:L86, real_69c60971d4242eda8c47c605:L87, real_69c60971d4242eda8c47c605:L88, real_69c60971d4242eda8c47c605:L89, real_69c60971d4242eda8c47c605:L90, real_69c60971d4242eda8c47c605:L91
reason: Collected evidence from L73 and L75 covers Chapter 5 requirements. Ready to answer query.
---
=== End Investigate ===
```

### 最终 evidence(new)

**[E1]** [§ 第五章 印章管理]
  第二十条集团公司办公室是集团公司印章的管理部门，负责各类印章的刻制、启用、授权使用、停用、回收及缴销等手续的办理，负责检查各类印章使用情况，负责受理对违反本办法行为的检举、揭发，以及按照本办法对违规行为进行责任追究。
  第二十一条集团公司所有印章实行责任管理。其中集团机关各部门主要负责人为部门印章第一管理责任人；二级单位行政主要负责人为本单位印章第一管理责任人，并为所属项目印章第一监管责任人；项目负责人为项目部印章的第一管理责任人；各印章保管人员为印章管理直接责任人，对集团公司负责。
  第二十二条集团公司财务专用章、总会计师名章、银行预留印鉴章由集团公司财务管理部负责全面管理，包括制定审批流程、审定印章保管人资格、印章交底、检查印章使用情况等。

**[E2]** [§ 第三十条 各印章管理责任单位应认真对印章管理使用情况进行检查监督：]
  2.印章启用函件是否已按规定送达至相关单位，有无业务往来确认；
  4.印章管理使用是否按要求检查，检查是否有记录，对查出的问题是否已整改；
  5.登记用印的内容是否与用印的内容一致；

- retrieved_nodes: L73, L74⭐, L75⭐, L76, L91, L96, L98, L99


---

## latest_clean_multi_0158  ·  multi_hop

- **Query:** 根据《陕西建工第十一建设集团有限公司印章管理办法（2020版）》中“第六章 印章封口、停用与缴销”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60971d4242eda8c47c605`
- **Gold nodes:** L103, L104

### 结果得分 — **PASS** (new gold_recall=0.50)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.50 |
| evidence_chars | 113 | 246 |
| n_retrieved_nodes | 3 | 4 |
| trajectory_steps | - | 3 |
| elapsed_sec | - | 3.95 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L103` | ✅ | True | False |
| `L104` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C23` collect L102 (depth=0) · multi→[L102, L103] · +2
  - reason: Collect Chapter 6 sections on seal sealing and stoppage to answer the query.
- `C25` collect L106 (depth=0) · multi→[L106, L107] · +2
  - reason: Collect two adjacent sections from Chapter 6 regarding seal suspension and cancellation to answer the query.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains the required Section 6 content covering sealing, suspension, and destruction points.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C23` | `L102` | L102, L103 | 2 | 2 | - | ✅ |
| 2 | `C25` | `L106` | L106, L107 | 2 | 2 | - | ✅ |

**水合告警:**
- step 1 整枝水合含 1 个非 gold 叶 (与 gold 争抢 evidence 预算)。

### 最终 evidence(new)

**[E1]** [§ 第六章 印章封口、停用与缴销]
  第三十二条项目部印章封口管理
  （一）在集团公司生产管理部发布的“封口闭合启动令”60日内上交集团公司办公室封存；项目印章回收后不得外借，期间如需要使用印章由原项目经理申请，责任管理单位批准后，在集团公司办公室登记用印。
  第三十三条发生机构名称变更、机构撤销等情况时，相关印章应在相关文件下发之日起停止使用，并在三个工作日内上交集团公司办公室。
  上缴的各类印章，应按要求办理缴销手续，留下印模。印章由集团公司办公室统一封存、销毁。

- retrieved_nodes: L102, L103⭐, L106, L107


---

## latest_clean_multi_0180  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“第一章 安全教育培训规定”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L5, L6

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 479 |
| n_retrieved_nodes | 12 | 12 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 4.62 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L5` | ❌ | False | False |
| `L6` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C1` collect L3 (depth=0) · →L3 · +27
  - reason: Collect Chapter 1 to retrieve content on safety education and training regulations.
- `F1` finish - (depth=0)
  - reason: Query asks for points from two adjacent evidence sections. G1 (§1.2.2) and G3 (§1.3) are adjacent in the hierarchy and cover key training content.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L3` | - | 27 | 27 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 1.2.2 三级安全教育的内容]
  1、二级单位（集团公司级）教育培训的主要内容：国家有关安全生产的法律法规、标准规范和集团公司的安全规章制度；建筑施工的特点和易发生的五大伤害，典型事故案例分析；
  2、项目部教育培训的主要内容：观看《生命之鉴》安全教育警示片，观看率达到100％；施工现场的环境、施工特点及可能存在的危害等；违章指挥、违章作业、违反劳动纪律产生的后果；预防、减少安全风险以及紧急情况下应急救援的基本措施；
  3、班组教育培训的主要内容：本班组作业特点和安全操作规程；如何正确使用劳动防护用品和安全防护装置；本岗位可能存在的危害及防范对策；本岗位的作业环境及使用的机械设备、工具的安全要求等。

**[E2]** [§ 1.3岗前教育]
  新上岗作业人员，作业人员进入新的岗位或者新的施工现场前，离岗一年以上重新上岗时，采用新技术、新工艺、新设备、新材料时，项目部应对作业人员进行相应的岗前教育培训。
  岗前教育培训包括以下内容：
  1、安全生产法律法规和规章制度；
  2、安全操作规程；
  3、针对性的安全防范措施；

- retrieved_nodes: L3, L7, L10, L11, L12, L13, L18, L19, L20, L21, L22, L23


---

## latest_clean_multi_0202  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“第二章 安全检查及隐患排查规定”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L41, L42

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 498 | 490 |
| n_retrieved_nodes | 14 | 11 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 4.32 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L41` | ✅ | True | False |
| `L42` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C1` collect L39 (depth=0) · →L39 · +59
  - reason: Collecting Chapter 2 to find the two adjacent evidence sections regarding safety inspection and hazard investigation.
- `F1` finish - (depth=0)
  - reason: Assembled evidence covers Chapter 2 requirements. G2 (General Provisions) and G1 (Methods) provide the two adjacent sections requested.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L39` | - | 59 | 59 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 2.1总则]
  2.1.1为进一步规范集团公司安全检查及隐患排查治理工作，防止和减少事故发生，贯彻国家“安全第一、预防为主、综合治理”的方针，依据《中华人民共和国安全生产法》、《建设工程安全生产管理条例》、《生产安全事故隐患排查治理暂行规定》等有关法律法规及集团公司相关规定，制定本制度。
  2.1.2 集团公司各级安全检查、隐患整改、回复销项、安全处罚均采用集团公司企业发展部的统一检查表格。

**[E2]** [§ 2.3安全检查及隐患排查的方法]
  2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。
  2.3.2集团公司安全检查及隐患排查的方式包括定期安全检查、专项安全检查、季节性安全检查、日常安全巡查、不定期抽查等。

**[E3]** [§ 2.4.4 重大事故隐患整改、复查、销项]
  对重大事故隐患，由被检查项目负责整改，整改应制定事故隐患治理方案，该方案由项目经理组织制定和实施。方案包括以下内容：
  5、治理的时限和要求；

- retrieved_nodes: L39, L40, L41⭐, L42⭐, L62, L63, L64, L81, L92, L93, L98


---

## latest_clean_multi_0223  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“2.3.4 专项安全检查”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L72, L73

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 184 |
| n_retrieved_nodes | 13 | 4 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 4.32 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L72` | ✅ | True | False |
| `L73` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C6` collect L71 (depth=0) · multi→[L71, L72, L74] · +3
  - reason: Collect section 2.3.4 and its relevant leaf nodes C7 and C9 to answer the query about special safety inspections.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains the required section 2.3.4 content with two adjacent points regarding special safety inspections.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C6` | `L71` | L71, L72, L74 | 3 | 5 | - | ✅ |

**水合告警:**
- step 1 整枝水合含 2 个非 gold 叶 (与 gold 争抢 evidence 预算)。

### 最终 evidence(new)

**[E1]** [§ 2.3.4 专项安全检查]
  定期检查中发现的倾向性问题，安全状况差的项目，集团公司及二级单位安排专项检查。
  对于超过一定规模危险性较大的分部分项工程的施工，二级单位在施工期间必须至少安排一次专项安全检查。
  对于危险性较大的分部分项工程的施工，施工现场临时用电，安全技术措施等，集团公司及二级单位安全监督管理部门应当在必要时安排专项安全检查。

- retrieved_nodes: L71, L72⭐, L73⭐, L74


---

## latest_clean_multi_0226  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“2.3.5 季节性安全检查”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L76, L78

### 结果得分 — **PASS** (new gold_recall=0.50)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.50 |
| evidence_chars | 482 | 160 |
| n_retrieved_nodes | 12 | 3 |
| trajectory_steps | - | 3 |
| elapsed_sec | - | 5.5 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L76` | ✅ | True | False |
| `L78` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C13` collect L75 (depth=0) · →L75 · +1
  - reason: Collect section 2.3.5 on seasonal safety inspections to answer the query.
- `C12` collect L64 (depth=0) · →L64 · +1
  - reason: Collect section 2.3.2 to identify seasonal safety inspection as a method, needed for the query.
- `F1` finish - (depth=0)
  - reason: Evidence collected covers §2.3.5 seasonal inspection requirements and related methods as requested.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C13` | `L75` | - | 1 | 1 | - | ✅ |
| 2 | `C12` | `L64` | - | 1 | 1 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 2.3.5 季节性安全检查]
在冬、雨季及暑期来临前或施工期间，集团公司各级安全监督管理部门根据本单位的施工情况，应组织季节性检查。

**[E2]** [§ 2.3安全检查及隐患排查的方法]
2.3.2集团公司安全检查及隐患排查的方式包括定期安全检查、专项安全检查、季节性安全检查、日常安全巡查、不定期抽查等。

- retrieved_nodes: L75, L76⭐, L64


---

## latest_clean_multi_0227  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“2.3.6 日常安全检查”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L78, L79

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 481 | 239 |
| n_retrieved_nodes | 11 | 4 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 4.36 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L78` | ✅ | True | False |
| `L79` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C14` collect L77 (depth=0) · →L77 · +3
  - reason: Target section 2.3.6 Daily Safety Inspection found; collecting to extract required points.
- `F1` finish - (depth=0)
  - reason: Assembled evidence G1 contains the required points for section 2.3.6 daily safety inspection.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C14` | `L77` | - | 3 | 3 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 2.3.6 日常安全检查]
  1、项目施工管理人员应对施工区域内的安全措施落实情况和作业人员遵章守纪情况进行巡查，对发现的违章行为和事故隐患应及时纠正和整改；
  2、项目经理和安全员要督促分包和设备租赁单位做好作业班组班前、班中和班后的安全岗位检查，发现问题及时整改；
  3、项目专职安全员每日必须深入施工现场巡查，发现事故隐患应及时督促整改，并将检查情况及时报告项目负责人和上级安全监督管理部门，以便落实整改措施。附表2-3-6《安全员日巡查标准化表格》

- retrieved_nodes: L77, L78⭐, L79⭐, L80


---

## latest_clean_multi_0230  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“2.4 隐患整改”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L82, L83

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 484 |
| n_retrieved_nodes | 10 | 12 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 4.05 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L82` | ❌ | False | False |
| `L83` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C11` collect L81 (depth=0) · →L81 · +25
  - reason: Collect section 2.4 Hazard Rectification to find the two adjacent evidence points requested.
- `F1` finish - (depth=0)
  - reason: Evidence G1 and G2 cover general and major hazard rectification points as requested.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C11` | `L81` | - | 25 | 25 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 2.4.4 重大事故隐患整改、复查、销项]
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

- retrieved_nodes: L81, L92, L100, L101, L102, L93, L94, L95, L96, L97, L98, L99


---

## latest_clean_multi_0296  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“第五章 施工机械设备管理规定”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L179, L180

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 460 |
| n_retrieved_nodes | 8 | 12 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 4.44 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L179` | ❌ | False | False |
| `L180` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C9` collect L177 (depth=0) · multi→[L177, L181, L185] · +64
  - reason: Collecting specific leaf nodes under Chapter 5 regarding equipment management and safety signs.
- `F1` finish - (depth=0)
  - reason: Assembled evidence G4 (user unit duties) and G2 (install unit duties) directly address the two adjacent evidence points regarding construction machinery management responsibilities.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C9` | `L177` | L177, L181, L185 | 64 | 66 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 5.4.1 项目部（使用单位）应当履行下列职责：]
  1、报审安装单位编制的建筑机械设备安装、拆卸工程专项施工方案和安全事故应急救援预案并存档；
  2、向安装单位提供拟安装设备位置的基础施工资料；确保机械设备进场安装、拆卸所需的施工条件；
  4、制定机械设备使用安全事故应急救援预案；
  5、指定专职安全管理人员、机管员等相关人员监督检查机械设备安装、拆卸、使用情况，并做好记录；
  6、施工现场有多台塔式起重机作业时，制定并实施防止塔式起重机相互碰撞的安全措施；
  7、根据不同施工阶段、周围环境以及季节、气候的变化，及时督促出租单位采取相应的安全防护措施；
  8、在机械设备活动范围内设置明显的安全警示标志，对集中作业区做好安全防护；
  9、配合出租单位对机械设备及其安全保护装置进行经常性和定期检查，并做好记录；
  10、自机械设备安装验收合格之日起30日内按相关程序向工程所在地、县级以上地方人民政府建设主管部门办理建筑机械使用登记，登记标志置于或者附着于该机械设备的显著位置。

- retrieved_nodes: L177, L233, L234, L235, L236, L238, L239, L240, L241, L242, L243, L244


---

## latest_clean_multi_0303  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“5.2机械设备管理”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L187, L188

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 485 |
| n_retrieved_nodes | 7 | 9 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.73 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L187` | ✅ | True | False |
| `L188` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C12` collect L186 (depth=0) · →L186 · +18
  - reason: Collect section 5.2 Mechanical Equipment Management to find the two adjacent evidence points requested.
- `F1` finish - (depth=0)
  - reason: Evidence collected covers section 5.2 Mechanical Equipment Management requirements and procedures.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C12` | `L186` | - | 18 | 18 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 5.2机械设备管理]
  5.2.1 严禁自行购置的机械设备（如塔式超重机、施工升降机等）直接租赁给项目部或自行购置的机械设备以单位名义对外出租。
  未经单位授权签订的机械租赁合同属个人行为，责任人承担全部责任。
  5.2.2 严禁租赁集团公司《施工现场安全负面清单（2019版）》（见附表5.2-2）中禁止及限制使用的施工机械；租赁机械设备时，要求选择注册资金不小于200万元人民币的租赁单位，拟租起重机械机械使用年限应符合以下规定：
  1、塔式超重机：800KN·M以下(不含800KN·M)塔吊不超过5年；800-1250KN·M(不含1250KN·M)塔吊不超过7年；1250KN·M以上塔吊不超过10年；
  2、SC型施工升降机不超过5年；SC型物料提升机不超过5年；
  3、SS物料提升机不超过3年。

**[E2]** [§ 5.2.5 租用机械设备管理程序：]
8、机械设备在使用过程中需要附着、顶升（加节），必须由原安装单位严格按照专项施工方案实施，并由使用单位组织出租单位、安装单位、监理单位等共同进行验收，验收合格后方可投入使用。

- retrieved_nodes: L186, L187⭐, L188⭐, L189, L190, L191, L192, L197, L205


---

## latest_clean_multi_0309  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“附表5.2.2：《施工现场安全负面清单（2019版）》”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L194, L195

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 465 |
| n_retrieved_nodes | 16 | 5 |
| trajectory_steps | - | 4 |
| elapsed_sec | - | 7.68 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L194` | ✅ | True | False |
| `L195` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C12` collect L193 (depth=0) · →L193 · +3
  - reason: The user query specifically targets '附表5.2.2' which is located under node C12.
- `C33` collect L497 (depth=0) · →L497 · +1
  - reason: Collect the specific section containing the 'Negative List' details to answer the query.
- `C9` collect L189 (depth=0) · →L189 · +1
  - reason: Collects the specific section referencing the 'Negative List' to answer the query about adjacent evidence points.
- `F1` finish - (depth=0)
  - reason: Assembled evidence contains the required negative list content and related management points from sections G1, G2, and G3.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C12` | `L193` | - | 3 | 3 | - | ✅ |
| 2 | `C33` | `L497` | - | 1 | 1 | - | ✅ |
| 3 | `C9` | `L189` | - | 1 | 1 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 附表5.2.2：《施工现场安全负面清单（2019版）》]
  5.2.3 租赁机械设备必须签订租赁和安装、拆卸合同，合同应使用集团公司合同示范文本，同时签订安全协议书（集团公司示范文本，明确总包、使用、租赁、安拆各方的安全责任）。
  租赁、安装单位应提供加盖单位公章的营业执照、资质证书、安全生产许可证、施工机械租赁行业确认书、行业推荐证书等企业资质文件；以及拟租赁设备制造许可证、产品合格证、制造监督检验证明、备案登记、自检合格证明、安装使用说明书等产品证明文件。
  5.2.4 租赁施工升降机和800KN·m及以下的塔式起重机时，应选用租赁安装维修保养一体化的专业承包企业；对800KN·m以上的塔式起重机出租单位，当其不具备相应的起重设备安装工程专业承包资质的，项目经理部必须在签订租赁合同的同时，与出租、安装单位共同签订三方安全管理协议书，并与安装单位签订安拆合同，并明确各方的安全生产权利与义务。

**[E2]** [§ 4.3.2 应急预案演练评价报]
5.2.2：《施工现场安全负面清单（2019版）》

- retrieved_nodes: L193, L194⭐, L195⭐, L196, L497


---

## latest_clean_multi_0324  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“5.3.2 按陕建监总发[2014]04号文要求：”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L211, L212

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 500 |
| n_retrieved_nodes | 19 | 10 |
| trajectory_steps | - | 5 |
| elapsed_sec | - | 8.0 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L211` | ✅ | True | False |
| `L212` | ✅ | True | False |

### 决策 TRACE(因果序)

- `D18` dispatch L262 (depth=0) · regions=[L262] · child_reports=1
  - reason: Dispatch Chapter 6 to locate section 5.3.2 and adjacent evidence.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L262 (depth=1) · →L262 · +64
      - reason: Collect Chapter 6 to locate section 5.3.2 and its referenced documents.
    - `F1` finish - (depth=1)
      - reason: Collected section L262 contains the required content to answer the query about adjacent evidence points.
- `C26` collect L210 (depth=0) · →L210 · +3
  - reason: Section C26 (5.3.2) contains the specific content regarding 'Shan Jian Jian Zong Fa [2014] No. 04' required by the query.
- `F1` finish - (depth=0)
  - reason: Query specifically asks for points from section 5.3.2, which is fully contained in G3.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L262` | - | 64 | 64 | - |  |
| 4 | `C26` | `L210` | - | 3 | 3 | - | ✅ |

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60974d4242eda8c47c615:L262 (ok)
collected 152 branch node(s); explicit roots=['real_69c60974d4242eda8c47c615:L262']
collected: real_69c60974d4242eda8c47c615:L262, real_69c60974d4242eda8c47c615:L263, real_69c60974d4242eda8c47c615:L264, real_69c60974d4242eda8c47c615:L265, real_69c60974d4242eda8c47c615:L266, real_69c60974d4242eda8c47c615:L267, real_69c60974d4242eda8c47c615:L268, real_69c60974d4242eda8c47c615:L269, real_69c60974d4242eda8c47c615:L270, real_69c60974d4242eda8c47c615:L271, real_69c60974d4242eda8c47c615:L272, real_69c60974d4242eda8c47c615:L273, real_69c60974d4242eda8c47c615:L274, real_69c60974d4242eda8c47c615:L275, real_69c60974d4242eda8c47c615:L276, real_69c60974d4242eda8c47c615:L277, real_69c60974d4242eda8c47c615:L278, real_69c60974d4242eda8c47c615:L279, real_69c60974d4242eda8c47c615:L280, real_69c60974d4242eda8c47c615:L281
reason: Collected section L262 contains the required content to answer the query about adjacent evidence points.
---
=== End Investigate ===
```

### 最终 evidence(new)

**[E1]** [§ 5.3.2 按陕建监总发[2014]04号文要求：]
  自2015年1月1日起，附着式升降脚手架外立面、底板、脚手板必须使用具有防火功能的防护产品；
  吊篮的安/拆（包括二次移位）工作，均应由出租单位负责完成，使用单位不得安拆、转租吊篮；
  5.3.3 附着式升降脚手架、高空作业吊篮等工具式脚手架的专项方案由专业分包单位组织编制，方案应符合《建筑施工工具式脚手架安全技术规范》JGJ202-2010（以下简称JGJ202-2010）的相关规定。并经过分包单位具有法人资格企业的技术负责人批准。再按照专项方案审批程序履行审批手续。

**[E2]** [§ 6.6 危险性较大的分部分项工程管理]
  危险性较大的分部分项工程识别清单（见附表6.6.1-1）；超过一定规模的危险性较大的分部分项工程识别清单（见附表6.6.1-2）。
  6.6.2 专项方案编制应当包括的内容，应当组织专家论证的相关内容，参见《危险性较大的分部分项工程安全管理规定》（建办质[2018]31号）执行。审核审批执行集团公司相关要求。

**[E3]** [§ 6.5 分包方安全管理]
3、分包单位安全生产绩效。

- retrieved_nodes: L210, L211⭐, L212⭐, L213, L262, L362, L365, L366, L354, L361


---

## latest_clean_multi_0362  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“5.4.3 项目部监督安装单位履行下列职责：”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L250, L251

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 490 | 445 |
| n_retrieved_nodes | 9 | 9 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 4.35 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L250` | ✅ | True | False |
| `L251` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C19` collect L249 (depth=0) · multi→[L249, L251, L256, L257] · +8
  - reason: Collect section 5.4.3 and its three leaf points regarding installation unit duties as requested.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains all required points from section 5.4.3 regarding installation unit duties.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C19` | `L249` | L249, L251, L256, L257 | 8 | 11 | - | ✅ |

**水合告警:**
- step 1 整枝水合含 3 个非 gold 叶 (与 gold 争抢 evidence 预算)。

### 最终 evidence(new)

**[E1]** [§ 5.4.3 项目部监督安装单位履行下列职责：]
  1、编制机械设备安装、拆卸专项施工方案，并由安装单位技术负责人审核、审批；
  2、按照安全技术标准、安装使用说明书等检查机械设备是否符合安全技术标准，查看现场是否具备安装、拆卸施工条件；
  3、组织进行安全技术交底并签字确认；
  4、制定机械设备安装、拆卸工程安全事故应急救援预案，并经本单位相关技术人员审核审批；
  5、机械设备在安装拆卸前应当将机械安装、拆卸工程专项方案，安装拆卸人员名单，机械安装单位的有关资质，安装拆卸时间等材料报施工总承包单位进行审查；
  6、严格按照专项方案及安全操作规程组织安装、拆卸作业，严禁违章作业，冒险作业；
  7、安装单位的专业技术人员、专职安全生产管理人员应当进行现场监督，技术负责人应当现场指导安装、拆卸作业；
  8、机械设备安装完毕后，安装单位应当按照安全技术标准及安装使用说明书等有关要求对所安装的机械设备进行自检、调试和试运转，自检合格的应当出具自检合格证明。

- retrieved_nodes: L249, L250⭐, L251⭐, L252, L253, L254, L255, L256, L257


---

## latest_clean_multi_0415  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“6.4 安全生产违章行为处罚”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L315, L316

### 结果得分 — **PASS** (new gold_recall=0.50)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.50 |
| evidence_chars | 500 | 490 |
| n_retrieved_nodes | 10 | 13 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 5.64 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L315` | ✅ | True | False |
| `L316` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C18` collect L314 (depth=0) · multi→[L314, L315, L319, L320, L324, L328, L329, L337, L339, L343, L345, L346, L347, L348, L349] · +39
  - reason: Collect section 6.4 to identify two adjacent evidence points regarding safety violation penalties.
- `F1` finish - (depth=0)
  - reason: Evidence G1 fully covers section 6.4 penalties for violations, addressing the user's query.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C18` | `L314` | L314, L315, L319, L320, L324, L328, L329, L337, L339, L343, L345, L346, L347, L348, L349 | 39 | 53 | - | ✅ |

**水合告警:**
- step 1 整枝水合含 14 个非 gold 叶 (与 gold 争抢 evidence 预算)。

### 最终 evidence(new)

**[E1]** [§ 6.4 安全生产违章行为处罚]
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

- retrieved_nodes: L314, L315⭐, L319, L320, L328, L329, L337, L339, L343, L346, L347, L348, L349


---

## latest_clean_multi_0462  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“6.8 危险源监控管理”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L376, L377

### 结果得分 — **PASS** (new gold_recall=0.50)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.50 |
| evidence_chars | 500 | 473 |
| n_retrieved_nodes | 14 | 7 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 5.19 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L376` | ❌ | False | False |
| `L377` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C24` collect L375 (depth=0) · multi→[L375, L376, L377, L378, L379, L380, L381, L382] · +7
  - reason: Collect section 6.8 and all its subsections to extract points on hazard source monitoring management.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains all required points from section 6.8 regarding hazard monitoring management.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C24` | `L375` | L375, L376, L377, L378, L379, L380, L381, L382 | 7 | 14 | - | ✅ |

**水合告警:**
- step 1 整枝水合含 6 个非 gold 叶 (与 gold 争抢 evidence 预算)。

### 最终 evidence(new)

**[E1]** [§ 6.8 危险源监控管理]
  6.8.2 危险源辨识应根据施工作业活动、施工作业流程和施工工艺，采用科学合理的辨识方法，辨识方法见《危险源辨识、风险评价与控制程序》，项目部对管辖区域和施工现场可能存在的危险源进行分析辨识，列出危险源清单。
  6.8.3 对已辨识出来的危险源采用定性和定量评价，分析导致事故发生的可能性和事故后果，确定风险等级及重大危险源，列出重大危险源清单。
  6.8.4 根据重大危险源清单，制定管理方案，明确重大危险源的目标、指标、控制措施，并落实相关部门及专人负责监督、管理。
  6.8.5 加强对重大危险源的巡查和监控，采取相应的预防及控制措施，消除或降低其影响，使其达到可接受的程度，保证集团公司职业健康安全管理目标的实现。
  6.8.6 项目部应在工地醒目位置设立“不可接受风险公示牌”（见集团公司《施工现场标准化管理手册》），公示牌应注明危险源、存在部位、作业时间、防护措施和责任人等内容。
  6.8.7二级单位、项目部应随所管区域变化和工程施工的进度及时进行更新对危险源辨识和风险评价。

- retrieved_nodes: L375, L377⭐, L378, L379, L380, L381, L382


---

## latest_clean_multi_0469  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“6.9 安全设施、安全防护用品管理”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L384, L385

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 492 |
| n_retrieved_nodes | 15 | 6 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.83 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L384` | ✅ | True | False |
| `L385` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C24` collect L383 (depth=0) · multi→[L383, L384, L385] · +6
  - reason: Collect section 6.9 and its two relevant leaf nodes C25 and C26 to answer the query about safety facilities management.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains all required points from section 6.9 regarding safety facilities and PPE management.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C24` | `L383` | L383, L384, L385 | 6 | 8 | - | ✅ |

**水合告警:**
- step 1 整枝水合含 1 个非 gold 叶 (与 gold 争抢 evidence 预算)。

### 最终 evidence(new)

**[E1]** [§ 6.9 安全设施、安全防护用品管理]
  6.9.1 项目部材料组负责安全设施、安全防护用品的采购、进场验收、保管、发放、更新、报废等的管理；项目部专职安全管理人员负责劳动防护用品使用过程的指导、监督和管理。
  6.9.2 实行分包的项目，对分包单位安全设施、劳动防护用品的提供，分包合同应明确约定；项目部负责对分包企业自行劳动防护用品的采购、使用等负责监督指导。
  6.9.3 项目部在采购安全设施、安全防护用品时，必须采购具有生产许可证和产品检验合格证的合格供方供应的产品。发放前材料组应组织项目质检员、安全员等共同验收，确认合格后方可发放使用。安全员负责收集生产许可证、产品合格证、准用证，检测合格证明等资料。
  6.9.4 生产组/施工员在安排操作人员上岗时，应检查安全设施、安全防护用品的使用情况，并指导正确使用。对未按规定使用安全设施、安全防护用品的人员及时纠正，对拒不改正的有权不予安排工作或停止其作业。
  办公、宿舍、库房等临时设施的消防、安全管理应符合《陕西建工集团施工现场临时建筑物安全管理暂行规定》（陕建总通[2013]143号）的要求。

- retrieved_nodes: L383, L384⭐, L385⭐, L386, L387, L389


---

## latest_clean_multi_0475  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“6.10 施工机具管理”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L391, L392

### 结果得分 — **PASS** (new gold_recall=0.50)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.50 |
| evidence_chars | 500 | 489 |
| n_retrieved_nodes | 10 | 7 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.84 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L391` | ❌ | False | False |
| `L392` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C24` collect L390 (depth=0) · →L390 · +9
  - reason: Target section 6.10 contains relevant points on construction tool management.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains all required points from section 6.10 regarding construction tool management.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C24` | `L390` | - | 9 | 9 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 6.10 施工机具管理]
  6.10.2 项目部材料动力组负责施工机具的日常检查及定期检查工作。检查依据：《建筑施工安全检查标准JGJ59-2011》，《建筑机械使用安全技术规程JGJ33-2012》，《施工现场机械设备检查技术规程JGJ160-2008》。
  6.10.3 项目部材料动力组负责施工机具的安装调试，施工机具安装完毕后由项目部组织按规定履行验收程序验收（总包方、分包方、租赁方、安装方、监理方），并应经责任人签字确认。
  6.10.4 项目部自有或租赁的施工机具，负有使用、维护、保养管理工作的义务。但劳务分包，专业分包或租赁的施工机具，合同及安全管理协议书必须明确使用、维护、保养管理工作的责任方。
  6.10.5 施工机具的各种检测仪表及安全装置必须齐全有效，严禁使用安全装置不齐全有效、超过使用年限或技术性能落后耗能高、效率低的施工机具。
  6.10.6 施工机具的现场工作环境必须符合要求，禁止在不适宜的工作环境下使用施工机具。
  6.10.9 施工机具出现故障或异常情况时应立即停机，待故障排除后方可使用，严禁机械带病运转。

- retrieved_nodes: L390, L392⭐, L393, L394, L395, L396, L399


---

## latest_clean_multi_0484  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“6.11 安全标志”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L401, L402

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 490 |
| n_retrieved_nodes | 15 | 11 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 5.3 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L401` | ✅ | True | False |
| `L402` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C29` collect L400 (depth=0) · multi→[L400, L401, L402] · +13
  - reason: Collect section 6.11 and its subsections to extract points on safety signs as requested.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains section 6.11 Safety Signs with all required points for the query.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C29` | `L400` | L400, L401, L402 | 13 | 15 | - | ✅ |

**水合告警:**
- step 1 整枝水合含 1 个非 gold 叶 (与 gold 争抢 evidence 预算)。

### 最终 evidence(new)

**[E1]** [§ 6.11 安全标志]
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

- retrieved_nodes: L400, L401⭐, L402⭐, L405, L406, L407, L408, L409, L410, L412, L413


---

## latest_clean_multi_0502  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“7.2 总平面布局”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L424, L425

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 390 |
| n_retrieved_nodes | 11 | 5 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 4.3 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L424` | ✅ | True | False |
| `L425` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C31` collect L423 (depth=0) · multi→[L423, L424, L426] · +4
  - reason: Collect section 7.2 Total Layout and its two leaf nodes to answer the query about adjacent evidence points.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains all required points from section 7.2 regarding total layout.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C31` | `L423` | L423, L424, L426 | 4 | 6 | - | ✅ |

**水合告警:**
- step 1 整枝水合含 2 个非 gold 叶 (与 gold 争抢 evidence 预算)。

### 最终 evidence(new)

**[E1]** [§ 7.2 总平面布局]
  7.2.1 施工现场出入口的设置必须满足消防车通行的要求，并应布置在不同方向，其数量不宜少于2个。当确有困难只能设置1个出入口时，在施工现场内设置满足消防车通行的环形道路，消防车道的净宽度和净空高度均不应小于4米。
  7.2.2 宿舍、厨房操作间、配电室、可燃材料堆场及其加工场、可燃材料及易燃易爆危险品库房等临时用房、临时设施不能设置于在建工程内。
  7.2.3 固定动火作业场要布置在可燃材料堆场及其加工场、易燃易爆危险品库房等全年最小频率风向的上风侧，并宜布置在临时办公用房、宿舍、可燃材料库房、在建工程等全年最小频率风向的上风侧。
  7.2.4 易燃易爆危险品库房与在建工程的防火间距不小于15m，可燃材料堆场及其加工场、固定动火作业场与在建工程的防火间距不小于10m，其它临时用房、临时设施与在建工程的防火间距不小于6m。

- retrieved_nodes: L423, L424⭐, L425⭐, L426, L427


---

## latest_clean_multi_0518  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“7.6 可燃物及易燃易爆危险品管理”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L444, L445

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 496 | 182 |
| n_retrieved_nodes | 10 | 2 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 4.02 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L444` | ✅ | True | False |
| `L445` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C26` collect L444 (depth=0) · multi→[L444, L445] · +2
  - reason: Collecting sections 7.6.1 and 7.6.2 which directly address the user's query about combustible materials management.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains the two adjacent points (7.6.1 and 7.6.2) from section 7.6 as requested.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C26` | `L444` | L444, L445 | 2 | 2 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 7.6 可燃物及易燃易爆危险品管理]
  7.6.1 用于在建工程的保温、防水、装饰使用的油漆及防腐等可燃物及易燃易爆危险品材料应按规定单独设库存放。
  7.6.2 在施工现场使用油漆及其有机溶剂、乙二胺、冷底子油或其他可燃、易燃易爆危险品的作业时，必须保持良好通风，作业场所严禁明火，并必须避免产生静电，同时设置专人、配备灭火器材进行现场监护。

- retrieved_nodes: L444⭐, L445⭐


---

## latest_clean_multi_0521  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“7.7.1 施工现场用火管理”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L449, L450

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 356 |
| n_retrieved_nodes | 10 | 7 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 4.94 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L449` | ✅ | True | False |
| `L450` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C31` collect L448 (depth=0) · multi→[L448, L449, L450] · +6
  - reason: Collect section 7.7.1 and its leaf nodes to extract key points on fire management as requested.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains all required points for section 7.7.1 regarding fire management.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C31` | `L448` | L448, L449, L450 | 6 | 8 | - | ✅ |

**水合告警:**
- step 1 整枝水合含 1 个非 gold 叶 (与 gold 争抢 evidence 预算)。

### 最终 evidence(new)

**[E1]** [§ 7.7.1 施工现场用火管理]
  1、施工现场动火作业必须办理动火许可证；动火操作人员必须具有相应资格；
  2、施工现场在进行焊接、切割、烘烤或加热等动火作业前，必须对作业现场的可燃物进行清理；对于作业现场及其附近无法移走的可燃物，必须采用不燃材料对其覆盖或隔离；裸露的可燃材料上严禁直接进行动火作业；
  3、焊接、切割、烘烤或加热等动火作业，必须配备灭火器材，并设动火监护人进行现场一对一监护；
  4、五级（含五级）以上风力时，必须停止焊接、切割等室外动火作业，否则必须采取可靠的挡风措施；
  5、动火作业后，必须对现场进行检查，确认无火灾危险后，动火操作人员方可离开；
  6、施工现场不应采用明火取暖；厨房操作间炉灶使用完毕后，必须将炉火熄灭，排油烟机及油烟管道必须定期清理油垢。

- retrieved_nodes: L448, L449⭐, L450⭐, L451, L452, L453, L454


---

## latest_clean_multi_0527  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“7.7.2 施工现场用电管理”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L456, L457

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 414 |
| n_retrieved_nodes | 8 | 7 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.78 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L456` | ✅ | True | False |
| `L457` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C32` collect L455 (depth=0) · →L455 · +6
  - reason: Target section 7.7.2 contains the required points on construction site electricity management.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains all required points from section 7.7.2 regarding construction site electricity management.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C32` | `L455` | - | 6 | 6 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 7.7.2 施工现场用电管理]
  1、电气线路必须具有相应的绝缘强度和机械强度，破损、烧焦的插座、插头应及时更换；
  2、电气设备与可燃、易燃易爆和腐蚀性物品保持一定的安全距离；
  3、有爆炸和火灾危险的场所，按危险等级选用相应的电气设备，电气设备不能超负荷运行或带故障使用；
  4、配电箱内每个电气回路必须设置漏电保护器、过载保护器，距配电箱2m范围内不能堆放可燃物，5m范围内不能设置可能产生较多易燃、易爆气体、粉尘的作业区；
  5、可燃材料库房不能使用高热灯具，易燃易爆危险品库房内必须使用防爆灯具，普通灯具与易燃物距离不小于300mm，聚光灯、碘钨灯等高热灯具与易燃物距离不宜小于500mm；
  6、施工现场办公、生活区和施工区禁止私自改装现场供用电设施，严禁在宿舍使用不合格的电褥子、大功率热水器等电器。项目部必须定期对办公、生活区和施工区安全用电、电气设备和线路的运行及维护情况进行检查。

- retrieved_nodes: L455, L456⭐, L457⭐, L458, L459, L460, L461


---

## latest_clean_multi_0544  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“7.8 其他防火管理”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L478, L479

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 195 |
| n_retrieved_nodes | 12 | 5 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.9 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L478` | ✅ | True | False |
| `L479` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C36` collect L477 (depth=0) · →L477 · +4
  - reason: Collect section 7.8 'Other Fire Management' to find the two adjacent evidence points requested.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains all required points from section 7.8 for the query.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C36` | `L477` | - | 4 | 4 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 7.8 其他防火管理]
  7.8.1 施工单位(项目部)必须做好施工现场临时消防设施的日常维护工作，对已失效、损坏或丢失的消防设施，必须及时更换、修复或补充。
  7.8.2 临时消防车道、临时疏散通道、安全出口必须保持畅通，不得遮挡、挪动疏散指示标识，不得挪用消防设施。
  7.8.3 施工期间，不能拆除临时消防设施及临时疏散设施。
  7.8.4 施工现场严禁吸烟。

- retrieved_nodes: L477, L478⭐, L479⭐, L480, L481


---

## latest_clean_multi_0552  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“3.2 生产安全事故快报”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L493, L494

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 500 |
| n_retrieved_nodes | 11 | 19 |
| trajectory_steps | - | 4 |
| elapsed_sec | - | 7.95 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L493` | ✅ | True | False |
| `L494` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C33` collect L492 (depth=0) · →L492 · +51
  - reason: Section 3.2 contains the required content on production safety accident rapid reports.
- `C14` collect L116 (depth=0) · →L116 · +10
  - reason: Collect section 3.2 to find the two adjacent evidence points regarding accident reporting.
- `C27` collect L147 (depth=0) · →L147 · +1
  - reason: Collect section C27 (Appendix 3.2) to obtain the specific content of the 'Production Safety Accident Quick Report' form required by the query.
- `F1` finish - (depth=0)
  - reason: G2 contains §3.2 content on accident reporting requirements, and G9 contains the specific 'Production Safety Accident Quick Report' form details.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C33` | `L492` | - | 51 | 51 | - | ✅ |
| 2 | `C14` | `L116` | - | 10 | 10 | - | ✅ |
| 3 | `C27` | `L147` | - | 1 | 1 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 3.2 事故报告]
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

**[E2]** [§ 3.2 生产安全事故快报]
  3.7-1 职工伤亡事故月（年）报表
  3.7-3 安全生产信息季（年）度报表
  4.3.1 应急预案演练方案

**[E3]** [§ 3.5 分析改进]
附表3.2：生产安全事故快报；

**[E4]** [§ 附表3.2]
生产安全事故快报

- retrieved_nodes: L116, L117, L118, L119, L120, L121, L122, L123, L124, L125, L126, L492, L493⭐, L494⭐, L495, L147, L501, L534, L535


---

## latest_clean_multi_0554  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“4.3.2 应急预案演练评价报”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L497, L500

### 结果得分 — **PASS** (new gold_recall=0.50)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.50 |
| evidence_chars | 228 | 461 |
| n_retrieved_nodes | 2 | 11 |
| trajectory_steps | - | 7 |
| elapsed_sec | - | 12.94 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L497` | ✅ | True | False |
| `L500` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C15` collect L167 (depth=0) · multi→[L167, L176] · +2
  - reason: Collect section 4.3.2 content and its associated appendix form to answer the query about evaluation report points.
- `C30` collect L496 (depth=0) · →L496 · +1
  - reason: Collect section 4.3.2 to obtain the specific content of the emergency plan drill evaluation report.
- `C37` collect L542 (depth=0) · →L542 · +1
  - reason: Collect section C37 (4.3.2 Evaluation Report) to answer the query about adjacent evidence points.
- `C17` collect L165 (depth=0) · →L165 · +3 · PURGED後代×1
  - reason: Collect section 4.3 to access the full content of 4.3.2 and adjacent sections for comparison.
- `C33` collect L541 (depth=0) · →L541 · +2 · PURGED後代×1
  - reason: Collect section D19 (4.3.2) to retrieve the specific content of the emergency plan drill evaluation report.
- `C26` collect L495 (depth=0) · →L495 · +1
  - reason: Collect section 4.3.1 to find the adjacent evidence for 4.3.2 as requested.
- `F1` finish - (depth=0)
  - reason: Evidence collected covers §4.3.2 content and the associated evaluation report form (G3, G2) required to answer the query.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C15` | `L167` | L167, L176 | 2 | 2 | - | ✅ |
| 2 | `C30` | `L496` | - | 1 | 1 | - | ✅ |
| 3 | `C37` | `L542` | - | 1 | 1 | - | ✅ |
| 4 | `C17` | `L165` | - | 3 | 3 | 1 | ✅ |
| 5 | `C33` | `L541` | - | 2 | 2 | 1 | ✅ |
| 6 | `C26` | `L495` | - | 1 | 1 | - | ✅ |

**水合告警:**
- step 4 `C17` 收父节点 `L165` 时 **purge 掉 1 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。
- step 5 `C33` 收父节点 `L541` 时 **purge 掉 1 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。

### 最终 evidence(new)

**[E1]** [§ 附表4.3.2]
  应急预案演练评价报告
  工程名称：

**[E2]** [§ 4.4 应急响应程序]
附表4.3.2：应急预案演练评价报告。

**[E3]** [§ 4.3 应急救援预案的演练]
  4.3.1 集团公司的综合应急救援预案每二年演练一次；项目部根据工程特点，项目施工（基础，主体，装饰）阶段，每年至少演练一次。演练必须编制演练方案（附表4.3.1：应急预案演练方案），并对参演人员进行宣传培训。
  4.3.2 演练结束后，演练组织部门对应急救援预案和处置程序的有效性、人员宣传培训和需求、设备和资源的充分性、应急救援行动以及是否达到预期目标作出评价报告（附表4.3.2：应急预案演练评价报告），交集团公司安全管理部存档。
  4.3.3 根据规范要求变化，应急预案环境改变，演练评价报告每一到二年修订应急救援预案。

**[E4]** [§ 3.2 生产安全事故快报]
4.3.1 应急预案演练方案

**[E5]** [§ 4.3.2 应急预案演练评价报]
5.2.2：《施工现场安全负面清单（2019版）》

- retrieved_nodes: L541, L542, L543, L176, L165, L166, L167, L168, L495, L496, L497⭐


---

## latest_clean_multi_0555  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“6.7.3 安全技术交底记录”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L505, L506

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 79 | 488 |
| n_retrieved_nodes | 1 | 16 |
| trajectory_steps | - | 3 |
| elapsed_sec | - | 6.24 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L505` | ✅ | True | False |
| `L506` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C24` collect L374 (depth=0) · multi→[L374, L560] · +2
  - reason: Collect section 6.7.3 text and the specific record form to answer the query about adjacent evidence points.
- `C28` collect L501 (depth=0) · →L501 · +47 · PURGED後代×1
  - reason: Collect section 6.7.3 to retrieve the full content of the safety technical disclosure record form.
- `F1` finish - (depth=0)
  - reason: The query asks for points from section 6.7.3 and the associated form (附表6.7.3). G1 contains the text of 6.7.3, and G2 contains the form title/structure. These are the two adjacent relevant sections.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C24` | `L374` | L374, L560 | 2 | 2 | - | ✅ |
| 2 | `C28` | `L501` | - | 47 | 47 | 1 | ✅ |

**水合告警:**
- step 2 `C28` 收父节点 `L501` 时 **purge 掉 1 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。

### 最终 evidence(new)

**[E1]** [§ 6.7 安全技术交底管理]
6.7.3 安全技术交底应由交底人、被交底人、专职安全员进行签字确认。并由项目部专职安全员保存安全技术交底记录（附表6.7.3 安全技术交底记录）。

**[E2]** [§ 附表6.7.3]
  安全技术交底记录
  工程名称：

**[E3]** [§ 附表1.1.1]
  安全教育记录
  编号：
  注：1、本表适用于岗前教育、日常安全教育、年度继续教育等使用。
  2、安全教育形式分为：岗前教育；日常安全教育（班前安全活动、雨季安全教育、暑期安全教育、冬季安全教育、节假日安全教育、消防安全教育、安全警示教育等）；年度继续教育等。

**[E4]** [§ 附件5.2.2                     施工现场安全负面清单（2]
文档列出使用不合格防坠器、超年限设备及维护不到位等问题的分包单位名单，并详细规定了塔吊、升降机、脚手架及临电设施等禁止或淘汰的技术标准与依据。

**[E5]** [§ 附表1.2-3]
  分包单位操作人员三级安全教育记录表
  工程名称
  2、本表适用于公司总承包项目的分包企业操作人员的三级安全教育。

- retrieved_nodes: L374, L501, L559, L560, L561, L502, L503, L504, L505⭐, L506⭐, L544, L545, L522, L523, L524, L528


---

## latest_clean_multi_0568  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“附件5.2.2 施工现场安全负面清单（2019版）”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L545, L547

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 413 |
| n_retrieved_nodes | 18 | 4 |
| trajectory_steps | - | 4 |
| elapsed_sec | - | 6.19 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L545` | ❌ | False | False |
| `L547` | ❌ | False | False |

### 决策 TRACE(因果序)

- `D10` dispatch L193 (depth=0) · regions=[L193] · child_reports=1
  - reason: Dispatch to retrieve the full content of Appendix 5.2.2 Negative List.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L193 (depth=1) · →L193 · +3
      - reason: Collects the full section 5.2.2 to extract the two adjacent evidence points requested.
    - `F1` finish - (depth=1)
      - reason: Collected section L193 contains the required negative list content to answer the query.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains the required negative list content to answer the query.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L193` | - | 3 | 3 | - | ✅ |

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60974d4242eda8c47c615:L193 (ok)
collected 4 branch node(s); explicit roots=['real_69c60974d4242eda8c47c615:L193']
collected: real_69c60974d4242eda8c47c615:L193, real_69c60974d4242eda8c47c615:L194, real_69c60974d4242eda8c47c615:L195, real_69c60974d4242eda8c47c615:L196
reason: Collected section L193 contains the required negative list content to answer the query.
---
=== End Investigate ===
```

### 最终 evidence(new)

**[E1]** [§ 附表5.2.2：《施工现场安全负面清单（2019版）》]
  5.2.3 租赁机械设备必须签订租赁和安装、拆卸合同，合同应使用集团公司合同示范文本，同时签订安全协议书（集团公司示范文本，明确总包、使用、租赁、安拆各方的安全责任）。
  租赁、安装单位应提供加盖单位公章的营业执照、资质证书、安全生产许可证、施工机械租赁行业确认书、行业推荐证书等企业资质文件；以及拟租赁设备制造许可证、产品合格证、制造监督检验证明、备案登记、自检合格证明、安装使用说明书等产品证明文件。
  5.2.4 租赁施工升降机和800KN·m及以下的塔式起重机时，应选用租赁安装维修保养一体化的专业承包企业；对800KN·m以上的塔式起重机出租单位，当其不具备相应的起重设备安装工程专业承包资质的，项目经理部必须在签订租赁合同的同时，与出租、安装单位共同签订三方安全管理协议书，并与安装单位签订安拆合同，并明确各方的安全生产权利与义务。

- retrieved_nodes: L193, L194, L195, L196


---

## latest_clean_multi_0572  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“附表6.6.1-1”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L554, L556

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 495 | 476 |
| n_retrieved_nodes | 16 | 6 |
| trajectory_steps | - | 8 |
| elapsed_sec | - | 10.8 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L554` | ❌ | False | False |
| `L556` | ❌ | False | False |

### 决策 TRACE(因果序)

- `D16` dispatch L362 (depth=0) · regions=[L362] · child_reports=1
  - reason: Dispatch section 6.6 to locate and extract details from Appendix 6.6.1-1.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C4` collect L365 (depth=1) · →L365 · +1
      - reason: Section C4 references Table 6.6.1-1, which is the target of the query.
    - `C2` collect L363 (depth=1) · multi→[L363, L364] · +2
      - reason: Collect C2 and C3 to address the query about adjacent evidence points in section 6.6.1.
    - `C2` collect L366 (depth=1) · multi→[L366, L367] · +2
      - reason: Collect C2 and C3 to address the query about adjacent evidence points in Section 6.6.
    - `C2` collect L368 (depth=1) · →L368 · +1
      - reason: Section C2 (6.6.4) is a leaf node directly relevant to the query about adjacent evidence points in Table 6.6.1-1.
    - `C1` collect L362 (depth=1) · →L362 · +6 · PURGED後代×6
      - reason: Collect section 6.6 to find details on adjacent evidence points in Table 6.6.1-1.
    - `F1` finish - (depth=1)
      - reason: Collected 5 sections covering the required table content; sufficient to answer query.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains §6.6 and Table 6.6.1-1 details required to answer the query.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C4` | `L365` | - | 1 | 1 | - | ✅ |
| 2 | `C2` | `L363` | L363, L364 | 2 | 2 | - | ✅ |
| 3 | `C2` | `L366` | L366, L367 | 2 | 2 | - | ✅ |
| 4 | `C2` | `L368` | - | 1 | 1 | - | ✅ |
| 5 | `C1` | `L362` | - | 6 | 6 | 6 | ✅ |

**水合告警:**
- step 5 `C1` 收父节点 `L362` 时 **purge 掉 6 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60974d4242eda8c47c615:L362 (ok)
collected 7 branch node(s); explicit roots=['real_69c60974d4242eda8c47c615:L365', 'real_69c60974d4242eda8c47c615:L363', 'real_69c60974d4242eda8c47c615:L366', 'real_69c60974d4242eda8c47c615:L368', 'real_69c60974d4242eda8c47c615:L362']
collected: real_69c60974d4242eda8c47c615:L362, real_69c60974d4242eda8c47c615:L363, real_69c60974d4242eda8c47c615:L364, real_69c60974d4242eda8c47c615:L365, real_69c60974d4242eda8c47c615:L366, real_69c60974d4242eda8c47c615:L367, real_69c60974d4242eda8c47c615:L368
reason: Collected 5 sections covering the required table content; sufficient to answer query.
---
=== End Investigate ===
```

### 最终 evidence(new)

**[E1]** [§ 6.6 危险性较大的分部分项工程管理]
  6.6.1 项目部应当在危险性较大的分部分项工程施工前编制专项方案；对于超过一定规模的危险性较大的分部分项工程，项目部应当组织专家对专项方案进行论证。
  危险性较大的分部分项工程识别清单（见附表6.6.1-1）；超过一定规模的危险性较大的分部分项工程识别清单（见附表6.6.1-2）。
  6.6.2 专项方案编制应当包括的内容，应当组织专家论证的相关内容，参见《危险性较大的分部分项工程安全管理规定》（建办质[2018]31号）执行。审核审批执行集团公司相关要求。
  6.6.3 在施工过程中，项目部必须严格执行经批准的安全专项施工方案，不得擅自修改，现场专职安全生产管理人员现场监督实施，项目部指定专人按规定进行监测，若发现现场施工条件和施工环境发生较大改变时，应当立即停止施工，撤离作业人员，并将有关情况及时上报监理单位和方案的审批部门，在采取可靠措施后方可恢复施工。
  6.6.4 超过一定规模的危险性较大的分部分项工程施工时，集团公司委托二级单位负责人对施工现场进行带班检查。

- retrieved_nodes: L362, L363, L365, L366, L367, L368


---

## latest_clean_multi_0573  ·  multi_hop

- **Query:** 根据《附件_安全管理规定（2020版）》中“附表6.6.1-2”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L556, L558

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 148 |
| n_retrieved_nodes | 18 | 2 |
| trajectory_steps | - | 3 |
| elapsed_sec | - | 5.81 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L556` | ❌ | False | False |
| `L558` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C31` collect L412 (depth=0) · →L412 · +1
  - reason: Target section '附表6.6.1-2' is a leaf node containing the specific list required by the query.
- `C25` collect L365 (depth=0) · →L365 · +1
  - reason: Collect section containing reference to Table 6.6.1-2 to retrieve its content.
- `F1` finish - (depth=0)
  - reason: Assembled evidence covers both required sections (G1, G2) for the query regarding 附表6.6.1-2.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C31` | `L412` | - | 1 | 1 | - | ✅ |
| 2 | `C25` | `L365` | - | 1 | 1 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 6.6 危险性较大的分部分项工程管理]
危险性较大的分部分项工程识别清单（见附表6.6.1-1）；超过一定规模的危险性较大的分部分项工程识别清单（见附表6.6.1-2）。

**[E2]** [§ 6.11 安全标志]
附表6.6.1-2：超过一定规模的危险性较大的分部分项工程识别清单；

- retrieved_nodes: L365, L412


---

## latest_clean_multi_0712  ·  multi_hop

- **Query:** 根据《陕西建工第十一建集团有限公司生产安全事故综合应急预案（2025版）》中“2.6 项目部应急救援领导小组成员职责”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c6097ad4242eda8c47c62c`
- **Gold nodes:** L155, L156

### 结果得分 — **PASS** (new gold_recall=0.50)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.50 |
| evidence_chars | 500 | 492 |
| n_retrieved_nodes | 8 | 12 |
| trajectory_steps | - | 4 |
| elapsed_sec | - | 56.39 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L155` | ❌ | False | False |
| `L156` | ✅ | True | False |

### 决策 TRACE(因果序)

- `D5` dispatch L152 (depth=0) · regions=[L152] · child_reports=1
  - reason: Dispatch to section 2.6 to retrieve details on project department emergency leadership group member duties.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L152 (depth=1) · →L152 · +40
      - reason: Collects the full section 2.6 to identify and compare duties of adjacent evidence groups.
    - `F1` finish - (depth=1)
      - reason: Collected section L152 contains the required responsibilities for the project emergency rescue leadership group members.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains the complete list of responsibilities for project emergency rescue leadership group members as requested.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L152` | - | 40 | 40 | - | ✅ |

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c6097ad4242eda8c47c62c:L152 (ok)
collected 41 branch node(s); explicit roots=['real_69c6097ad4242eda8c47c62c:L152']
collected: real_69c6097ad4242eda8c47c62c:L152, real_69c6097ad4242eda8c47c62c:L153, real_69c6097ad4242eda8c47c62c:L154, real_69c6097ad4242eda8c47c62c:L155, real_69c6097ad4242eda8c47c62c:L156, real_69c6097ad4242eda8c47c62c:L157, real_69c6097ad4242eda8c47c62c:L158, real_69c6097ad4242eda8c47c62c:L159, real_69c6097ad4242eda8c47c62c:L160, real_69c6097ad4242eda8c47c62c:L161, real_69c6097ad4242eda8c47c62c:L162, real_69c6097ad4242eda8c47c62c:L163, real_69c6097ad4242eda8c47c62c:L164, real_69c6097ad4242eda8c47c62c:L165, real_69c6097ad4242eda8c47c62c:L166, real_69c6097ad4242eda8c47c62c:L167, real_69c6097ad4242eda8c47c62c:L168, real_69c6097ad4242eda8c47c62c:L169, real_69c6097ad4242eda8c47c62c:L170, real_69c6097ad4242eda8c47c62c:L171
reason: Collected section L152 contains the required responsibilities for the project emergency rescue leadership group members.
---
=== End Investigate ===
```

### 最终 evidence(new)

**[E1]** [§ 2.6 项目部应急救援领导小组成员职责]
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

- retrieved_nodes: L152, L153, L156⭐, L159, L162, L166, L168, L169, L170, L177, L188, L191


---

## latest_clean_multi_0742  ·  multi_hop

- **Query:** 根据《陕西建工第十一建集团有限公司生产安全事故综合应急预案（2025版）》中“2.7 各应急救援小组职责”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c6097ad4242eda8c47c62c`
- **Gold nodes:** L195, L196

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 489 |
| n_retrieved_nodes | 9 | 16 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 4.29 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L195` | ✅ | True | False |
| `L196` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C20` collect L193 (depth=0) · →L193 · +25
  - reason: Section 2.7 contains the required emergency rescue group duties.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains the complete section 2.7 with all group duties required by the query.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C20` | `L193` | - | 25 | 25 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 2.7 各应急救援小组职责]
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

- retrieved_nodes: L193, L194, L195⭐, L196⭐, L197, L198, L200, L201, L204, L205, L206, L208, L210, L211, L216, L217


---

## latest_clean_multi_0760  ·  multi_hop

- **Query:** 根据《陕西建工第十一建集团有限公司生产安全事故综合应急预案（2025版）》中“3.1 信息报告”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c6097ad4242eda8c47c62c`
- **Gold nodes:** L222, L223

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 500 |
| n_retrieved_nodes | 14 | 14 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.79 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L222` | ✅ | True | False |
| `L223` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C10` collect L220 (depth=0) · →L220 · +25
  - reason: Collect section 3.1 Information Reporting to find the two adjacent evidence points requested.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains section 3.1 Information Reporting with all required details for the query.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C10` | `L220` | - | 25 | 25 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 3.1 信息报告]
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

- retrieved_nodes: L220, L221, L222⭐, L223⭐, L224, L229, L232, L233, L234, L235, L236, L239, L240, L241


---

## real_69c6ef484cca74801cb63bb9_multi_hop_auto_0003  ·  multi_hop

- **Query:** 注浆施工的主要材料中，水玻璃的波美度要求是多少？在浆液拌制和泵送过程中，有哪些具体的质量控制措施以防止堵塞或保证均匀性？
- **Doc:** `real_69c6ef484cca74801cb63bb9`
- **Gold nodes:** L141, L167

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 492 |
| n_retrieved_nodes | 13 | 8 |
| trajectory_steps | - | 7 |
| elapsed_sec | - | 11.13 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L141` | ❌ | False | False |
| `L167` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C19` collect L99 (depth=0) · multi→[L99, L133] · +2
  - reason: C19 contains water glass Be'me degree (25-30°). C25 details mixing and pumping quality controls to prevent blockage.
- `C14` collect L62 (depth=0) · →L62 · +1
  - reason: Section C14 explicitly states the specific gravity (Bé度) of sodium silicate required for grouting.
- `C13` collect L60 (depth=0) · →L60 · +7 · PURGED後代×1
  - reason: Section C13 contains the specific sodium silicate Beometer degree (25-30°) and mix ratio required.
- `D12` dispatch L97 (depth=0) · regions=[L97] · child_reports=1
  - reason: Dispatch section 5.2.7 to find specific sodium silicate density and mixing/pumping quality control measures.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L97 (depth=1) · →L97 · +13 · PURGED後代×1
      - reason: Collect section 5.2.7 to find water glass specific gravity and grout quality control measures.
    - `F1` finish - (depth=1)
      - reason: Collected section L97 contains information on sodium silicate density and grout quality control measures.
- `F1` finish - (depth=0)
  - reason: Evidence contains sodium silicate density (Be degrees) and grout quality control measures for mixing/pumping.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C19` | `L99` | L99, L133 | 2 | 2 | - | ✅ |
| 2 | `C14` | `L62` | - | 1 | 1 | - | ✅ |
| 3 | `C13` | `L60` | - | 7 | 7 | 1 | ✅ |
| 4 | `C1` | `L97` | - | 13 | 13 | 1 | ✅ |

**水合告警:**
- step 3 `C13` 收父节点 `L60` 时 **purge 掉 1 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。
- step 4 `C1` 收父节点 `L97` 时 **purge 掉 1 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c6ef484cca74801cb63bb9:L97 (ok)
collected 13 branch node(s); explicit roots=['real_69c6ef484cca74801cb63bb9:L97']
collected: real_69c6ef484cca74801cb63bb9:L100, real_69c6ef484cca74801cb63bb9:L101, real_69c6ef484cca74801cb63bb9:L102, real_69c6ef484cca74801cb63bb9:L103, real_69c6ef484cca74801cb63bb9:L104, real_69c6ef484cca74801cb63bb9:L105, real_69c6ef484cca74801cb63bb9:L106, real_69c6ef484cca74801cb63bb9:L107, real_69c6ef484cca74801cb63bb9:L108, real_69c6ef484cca74801cb63bb9:L109, real_69c6ef484cca74801cb63bb9:L110, real_69c6ef484cca74801cb63bb9:L97, real_69c6ef484cca74801cb63bb9:L98
reason: Collected section L97 contains information on sodium silicate density and grout quality control measures.
---
=== End Investigate ===
```

### 最终 evidence(new)

**[E1]** [§ 配合比：A：B=1：1，其中A液：水泥：水=0.8:1 B液：中性水玻璃，波美度]
式中：Q-浆液总用量L

**[E2]** [§ 7.3 加强施工测量，确保钻杆竖直，位置满足规范要求。]
- 7.6 浆液拌制严格按配合比要求，并在拌浆现场悬挂配比牌。浆体必须经搅拌机充分 搅拌均匀，方可开始压浆，浆体在泵送前经筛网过滤。

**[E3]** [§ 5.2.7 注浆]
  浆液的注入采用钻-灌一体机和空压机配合使用，帷幕注浆注浆压力0.6mpa，根
  据地层及注浆压力进行调整，通过压力表观察注浆压力。注浆管每次上拔高度应为 33cm，为防止注浆管对后续施工产生危害，严禁将注浆管拔断掉落在阀管中。
  注浆前，严格按照配方配料。其中帷幕采用AB液作为注浆材料，A液∶B液=1∶1 ，其中A液：水泥：水=0.8∶1；B液：中性水玻璃，水玻璃为波美度25°～30°；帷 幕中心区采用纯水泥浆作为注浆材料，注浆水泥采用强度等级为Po42.5R普通水泥。 施工用水采用自来水。浆液应搅拌均匀，随拌随注，不得长时间存放已拌好的浆液 。封闭泥浆用泵从钻杆自下而上压入孔内，不准从孔口到入。

- retrieved_nodes: L60, L63, L64, L133, L97, L103, L104, L99


---

## real_69c6ef484cca74801cb63bb9_multi_hop_auto_0006  ·  multi_hop

- **Query:** 根据质量控制要求，注浆允许偏差及检验办法应符合哪张表的规定？该表中列出了哪四个关键检查项目？同时，在浆液拌制过程中有哪些具体的操作要求以确保质量？
- **Doc:** `real_69c6ef484cca74801cb63bb9`
- **Gold nodes:** L159, L162, L167

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 482 |
| n_retrieved_nodes | 12 | 13 |
| trajectory_steps | - | 8 |
| elapsed_sec | - | 12.0 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L159` | ❌ | False | False |
| `L162` | ❌ | False | False |
| `L167` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C20` collect L128 (depth=0) · multi→[L128, L129, L133] · +34
  - reason: Collect table 7.2.1 for deviation/inspection items and section 7.6 for slurry mixing requirements.
- `C31` collect L113 (depth=0) · →L113 · +2
  - reason: Collect section 5.2.9 to find the table number for grouting deviation and inspection methods.
- `C31` collect L126 (depth=0) · →L126 · +2 · PURGED後代×1
  - reason: Collect section C31 to find Table 7.2.1 and its four key inspection items for grouting deviation.
- `C5` collect L21 (depth=0) · →L21 · +56
  - reason: Collect section 5 to find the table for grouting deviation and inspection methods, plus slurry mixing requirements.
- `C34` collect L123 (depth=0) · →L123 · +2
  - reason: Collect section 7 Quality Control to find Table 7.2.1 and slurry mixing requirements.
- `C15` collect L99 (depth=0) · →L99 · +1
  - reason: Collects浆液拌制操作要求 and confirms Table 7.2.1 reference for deviation limits.
- `C14` collect L97 (depth=0) · →L97 · +13 · PURGED後代×1
  - reason: Collect section 5.2.7 to find the table for allowable deviations and inspection methods, and浆液拌制 requirements.
- `C2` collect L2 (depth=0) · multi→[L2, L8, L9] · +8 · PURGED後代×1
  - reason: Need to collect section 7.2 for deviation table and section 7.3 for slurry mixing requirements.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C20` | `L128` | L128, L129, L133 | 34 | 35 | - | ✅ |
| 2 | `C31` | `L113` | - | 2 | 2 | - | ✅ |
| 3 | `C31` | `L126` | - | 2 | 2 | 1 | ✅ |
| 4 | `C5` | `L21` | - | 56 | 56 | - | ✅ |
| 5 | `C34` | `L123` | - | 2 | 2 | - | ✅ |
| 6 | `C15` | `L99` | - | 1 | 1 | - | ✅ |
| 7 | `C14` | `L97` | - | 13 | 13 | 1 | ✅ |
| 8 | `C2` | `L2` | L2, L8, L9 | 8 | 8 | 1 | ✅ |

**水合告警:**
- step 3 `C31` 收父节点 `L126` 时 **purge 掉 1 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。
- step 7 `C14` 收父节点 `L97` 时 **purge 掉 1 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。
- step 8 `C2` 收父节点 `L2` 时 **purge 掉 1 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。

### 最终 evidence(new)

**[E1]** [§ 7.3 加强施工测量，确保钻杆竖直，位置满足规范要求。]
  - 7.4 注浆开始前应充分作好准备工作，包括机械器具、仪表、管路、注浆材料、水和 电等的检查及必要的试验，注浆一经开始即应连续进行，力求避免中断。
  - 7.5 在钻杆钻进过程中，根据不同土质和覆土厚度，结合监测信息，及时调整推力、 推进速度和注浆量的相互关系，合理控制钻进速度，保证土压平衡。
  - 7.6 浆液拌制严格按配合比要求，并在拌浆现场悬挂配比牌。浆体必须经搅拌机充分 搅拌均匀，方可开始压浆，浆体在泵送前经筛网过滤。
  - 7.7 施工过程控制压力，及时观察注浆终压值，防止因压力过大导致浆液外渗。
  - 7.8 注浆结束后及时封孔，防止相邻注浆孔注浆时引起漏浆。
  - 7.9 加强注浆施工人员的培训工作，提高注浆机械人员的操作水平。
  - 7.10 做好注浆设备的维修保养和注浆材料供应工作，定时对注浆管路及设备进行清洗
  - ，保证注浆作业连续不间断的进行。

**[E2]** [§ 7.2 主要控制措施]
注浆允许偏差及检验办法应符合表7.2.1的规定。

- retrieved_nodes: L129, L130, L131, L132, L133, L134, L135, L136, L137, L138, L126, L127, L128


---

## latest_clean_niche_0036  ·  niche_fact

- **Query:** 根据《附件》中“正文”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c6096dd4242eda8c47c5ed`
- **Gold nodes:** L7

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 71 | 360 |
| n_retrieved_nodes | 4 | 15 |
| trajectory_steps | - | 6 |
| elapsed_sec | - | 9.14 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L7` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C1` collect L1 (depth=0) · →L1 · +4
  - reason: Collect Attachment 1 to find the specific regulations or facts in its main text.
- `C1` collect L6 (depth=0) · →L6 · +3
  - reason: Collect '附件2' to find explicit regulations or facts regarding official vehicle usage as requested.
- `C1` collect L10 (depth=0) · →L10 · +2
  - reason: Collect '附件4' to find regulations/facts in the main text as requested.
- `C3` collect L15 (depth=0) · →L15 · +1
  - reason: The user asks for regulations/facts in '正文' (main text). N3 is a leaf node labeled [Hit] under '附件5', likely containing the specific record mentioned.
- `C1` collect L13 (depth=0) · →L13 · +2 · PURGED後代×1
  - reason: Collect §附件5 to find specific regulations or facts as requested.
- `F1` finish - (depth=0)
  - reason: Evidence collected covers all relevant sections of the 'Main Text' in the attachment, detailing vehicle management regulations and forms.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L1` | - | 4 | 4 | - | ✅ |
| 2 | `C1` | `L6` | - | 3 | 3 | - | ✅ |
| 3 | `C1` | `L10` | - | 2 | 2 | - | ✅ |
| 4 | `C3` | `L15` | - | 1 | 1 | - | ✅ |
| 5 | `C1` | `L13` | - | 2 | 2 | 1 | ✅ |

**水合告警:**
- step 5 `C1` 收父节点 `L13` 时 **purge 掉 1 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。

### 最终 evidence(new)

**[E1]** [§ 附件2]
  陕西建工第十一建设集团有限公司的公务用车申请单，包含车型、车号、司机、用车单位、联系人、出车时间、路线及里程等详细信息，并设有满意度调查和签字确认栏。
  服务电话:029-33215789
  陕西建工第十一建设集团有限公司的车辆保养/维修申请单，包含申请人、车牌号、送修及取车日期等信息。表格分为保养和维修两部分，分别记录项目、金额及备注，并规定了不同金额的审批流程。

**[E2]** [§ 附件4]
  陕西建工第十一建设集团有限公司
  车辆加油记录单

**[E3]** [§ 附件5]
  陕西建工第十一建设集团有限公司
  公务车辆节假日封存记录

**[E4]** [§ 附件1]
  陕西建工第十一建设集团有限公司
  车辆租赁审批单
  申请单位（盖章）：
  填报人： 填报日期： 年月日

- retrieved_nodes: L6, L7⭐, L8, L9, L10, L11, L12, L13, L14, L15, L1, L2, L3, L4, L5


---

## latest_clean_niche_0068  ·  niche_fact

- **Query:** 根据《陕西建工第十一建设集团有限公司印章管理办法（2020版）》中“陕西建工第十一建设集团有限公司印章管理办法（2020版）.docx”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60971d4242eda8c47c605`
- **Gold nodes:** L2

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 479 | 465 |
| n_retrieved_nodes | 8 | 6 |
| trajectory_steps | - | 4 |
| elapsed_sec | - | 6.82 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L2` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C1` collect L1 (depth=0) · →L1 · +5
  - reason: Collect Chapter 1 to retrieve the full text of the regulations as requested.
- `C1` collect L7 (depth=0) · →L7 · +17
  - reason: Collect Chapter 2 to retrieve specific regulations on seal carving and activation.
- `C3` collect L42 (depth=0) · multi→[L42, L56, L57, L74, L75, L89, L111, L112] · +8
  - reason: Collect specific rules on seal usage scope, management responsibilities, blank stamping prohibition, and penalties for forgery.
- `F1` finish - (depth=0)
  - reason: Collected evidence covers all key regulations on seal usage, management, and accountability as requested.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L1` | - | 5 | 5 | - | ✅ |
| 2 | `C1` | `L7` | - | 17 | 17 | - | ✅ |
| 3 | `C3` | `L42` | L42, L56, L57, L74, L75, L89, L111, L112 | 8 | 8 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 第一章 总则]
  第一条为规范集团公司及下属单位印章管理工作，有效防范风险，保障经营管理活动的有序开展，特制定本办法。
  第二条本办法所称集团公司印章包括：集团公司法人章、财务专用章、机关部门章，集团公司下属单位印章、项目部章等行使公司职权的法定名称章；集团公司法定代表人章、总会计师章等代表公司实施职务行为的印章。
  第三条印章所刊名称，应为集团公司文件规定的法定名称。印章文字一般应使用宋体简体字。
  集团公司法人章为圆形，直径为4.2CM，中央刊五角星，上环刊单位名称自左向右环排；部门章一律为圆形，直径为3.8CM，上刊集团名称自左向右环排，中央刊五角星，部门名称放在星下方作横排；二级单位公章一律为圆形，直径4.0CM，集团名称自左而右环排，二级单位名称放在星下方作横排。项目部章一律为圆形，直径4.0CM，集团名称和工程名称依次自左而右环排，“工程项目部”字样放在星下方作横排，名称应严格按“陕建十一建集团+工程名称+工程项目部”格式确定。
  印章名称、规格、标准等由集团公司办公室统一审核。

- retrieved_nodes: L1, L2⭐, L3, L4, L5, L6


---

## latest_clean_niche_0160  ·  niche_fact

- **Query:** 根据《陕西建工第十一建设集团有限公司印章管理办法（2020版）》中“第七章 责任追究”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60971d4242eda8c47c605`
- **Gold nodes:** L111

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 479 | 492 |
| n_retrieved_nodes | 5 | 5 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.39 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L111` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C21` collect L110 (depth=0) · →L110 · +7
  - reason: Collect Chapter 7 'Accountability' to extract specific regulations on penalties and responsibilities.
- `F1` finish - (depth=0)
  - reason: Assembled evidence G1 contains all relevant content from Chapter 7 regarding accountability measures.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C21` | `L110` | - | 7 | 7 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 第七章	责任追究]
  第三十五条伪造、私刻集团公司法人章、财务专用章、银行预留印鉴章、领导签名章的，一经发现，对伪造、私刻责任方（单位、项目部、个人）处10万元罚款，并由集团公司组织调查组进行调查，根据情节轻重追究相关责任人的行政、经济责任，通报批评，依法追偿损失；涉嫌犯罪的，报请司法机关依法进行处理。
  第三十六条伪造、私刻集团公司机关部门章、二级单位章、项目部印章的，一经发现，对伪造、私刻责任方（单位、项目部、个人）处于6万元罚款，并由集团公司组织调查组进行调查，根据情节轻重追究相关责任人的行政、经济责任，通报批评，依法追偿损失。涉嫌犯罪的，报请司法机关依法进行处理。
  第四十一条有印章使用审批权限的其他管理人员，超越审批权限使用印章，造成经济损失及不良后果的，由集团公司党委组织部、监察审计部按《管理人员责任追究暂行规定》追究其相关责任。
  第四十二条印章责任管理单位、监管部门未认真履行印章管理、检查监督、封口管理等职责，发生伪造、私刻印章等情节严重，或造成经济损失及不良影响的，对管理责任人按集团公司《管理人员责任追究暂行规定》追究相关责任。

- retrieved_nodes: L110, L111⭐, L112, L116, L117


---

## latest_clean_niche_0175  ·  niche_fact

- **Query:** 根据《附件_安全管理规定（2020版）》中“第一章 安全教育培训规定”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L5

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 490 |
| n_retrieved_nodes | 12 | 11 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 4.04 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L5` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C1` collect L3 (depth=0) · →L3 · +27
  - reason: Collect Chapter 1 to retrieve all safety education and training regulations as requested.
- `F1` finish - (depth=0)
  - reason: All sections of Chapter 1 on safety education and training have been collected and assembled in the evidence groups.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L3` | - | 27 | 27 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 1.2 三级安全教育]
  1.2.1 三级安全教育的对象：新进集团公司的作业人员，在上岗前必须接受集团公司（基层单位）、项目、班组的三级安全教育培训（附表1.2-1：项目管理人员三级安全教育记录表；附表1.2-2：项目操作人员三级安全教育记录表）。
  分包单位的作业人员三级安全教育，由其分包单位进行，项目部履行监督职责，并保存三级安全教育记录（附表1.2-3：分包单位作业人员三级安全教育记录表）。

**[E2]** [§ 1.1 总则]
  1.1.1安全教育和培训的类型应包括三级安全教育、岗前教育、日常教育、年度继续教育，以及各类特种作业人员证书的初审、复审培训（附表1.1.1：安全教育记录）。
  1.1.2集团公司各级安全教育培训计划、安全教育培训工作按集团公司教育培训制度执行。

**[E3]** [§ 1.3岗前教育]
  新上岗作业人员，作业人员进入新的岗位或者新的施工现场前，离岗一年以上重新上岗时，采用新技术、新工艺、新设备、新材料时，项目部应对作业人员进行相应的岗前教育培训。
  岗前教育培训包括以下内容：
  1、安全生产法律法规和规章制度；

- retrieved_nodes: L3, L7, L8, L9, L4, L5⭐, L6, L18, L19, L20, L21


---

## latest_clean_niche_0214  ·  niche_fact

- **Query:** 根据《附件_安全管理规定（2020版）》中“2.3.3 定期安全检查”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L66

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 483 | 464 |
| n_retrieved_nodes | 14 | 10 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 4.01 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L66` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C9` collect L62 (depth=0) · →L62 · +14
  - reason: Section 2.3 covers safety inspection methods, including the target section 2.3.3.
- `F1` finish - (depth=0)
  - reason: Section G4 contains the specific regulations for '2.3.3 Regular Safety Inspections' as requested.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C9` | `L62` | - | 14 | 14 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 2.3.3 定期安全检查]
  1、集团公司每季度进行一次安全检查，重点检查项目部施工现场安全生产管理体系的运行情况、施工现场安全隐患排查和安全防护情况；二级单位对项目部的定期监督检查制度落实情况等（集团公司直属项目每月检查一次）；
  2、集团公司委托二级单位每月组织对所属项目进行一次安全检查及隐患排查。
  3、项目部每周组织各分包单位进行安全检查；
  附表2-3-3《项目周检查标准化表格》
  4、项目因故停工（复工）执行集团公司停复工相关规定，复工前，项目部必须对施工现场安全设施、设备及安全防护进行自查，基层单位复查。

**[E2]** [§ 2.3.5 季节性安全检查]
在冬、雨季及暑期来临前或施工期间，集团公司各级安全监督管理部门根据本单位的施工情况，应组织季节性检查。

**[E3]** [§ 2.3安全检查及隐患排查的方法]
2.3.1安全检查及隐患排查依据《建筑施工安全检查标准》JGJ59-2011、现行建筑施工安全技术规范、标准、规章制度及《集团公司项目综合大检查考核评分标准》相关管理规定。

- retrieved_nodes: L62, L65, L66⭐, L67, L68, L69, L70, L75, L76, L63


---

## latest_clean_niche_0219  ·  niche_fact

- **Query:** 根据《附件_安全管理规定（2020版）》中“2.3.4 专项安全检查”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L72

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 494 | 184 |
| n_retrieved_nodes | 15 | 4 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 4.13 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L72` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C12` collect L71 (depth=0) · →L71 · +3
  - reason: Target section 2.3.4 Special Safety Inspection identified; collect to retrieve full content.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains the specific regulations for section 2.3.4 Special Safety Inspections as requested.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C12` | `L71` | - | 3 | 3 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 2.3.4 专项安全检查]
  定期检查中发现的倾向性问题，安全状况差的项目，集团公司及二级单位安排专项检查。
  对于超过一定规模危险性较大的分部分项工程的施工，二级单位在施工期间必须至少安排一次专项安全检查。
  对于危险性较大的分部分项工程的施工，施工现场临时用电，安全技术措施等，集团公司及二级单位安全监督管理部门应当在必要时安排专项安全检查。

- retrieved_nodes: L71, L72⭐, L73, L74


---

## latest_clean_niche_0222  ·  niche_fact

- **Query:** 根据《附件_安全管理规定（2020版）》中“2.3.5 季节性安全检查”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L76

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 74 |
| n_retrieved_nodes | 16 | 1 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.6 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L76` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C16` collect L76 (depth=0) · →L76 · +1
  - reason: Found section 2.3.5 'Seasonal Safety Inspection' with the specific regulation text.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains the specific regulations for seasonal safety inspections as requested.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C16` | `L76` | - | 1 | 1 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 2.3.5 季节性安全检查]
在冬、雨季及暑期来临前或施工期间，集团公司各级安全监督管理部门根据本单位的施工情况，应组织季节性检查。

- retrieved_nodes: L76⭐


---

## latest_clean_niche_0223  ·  niche_fact

- **Query:** 根据《附件_安全管理规定（2020版）》中“2.3.6 日常安全检查”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L78

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 483 | 239 |
| n_retrieved_nodes | 14 | 4 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.9 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L78` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C10` collect L77 (depth=0) · →L77 · +3
  - reason: Target section 2.3.6 contains the specific rules for daily safety inspections.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains the specific regulations for section 2.3.6 Daily Safety Inspection as requested.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C10` | `L77` | - | 3 | 3 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 2.3.6 日常安全检查]
  1、项目施工管理人员应对施工区域内的安全措施落实情况和作业人员遵章守纪情况进行巡查，对发现的违章行为和事故隐患应及时纠正和整改；
  2、项目经理和安全员要督促分包和设备租赁单位做好作业班组班前、班中和班后的安全岗位检查，发现问题及时整改；
  3、项目专职安全员每日必须深入施工现场巡查，发现事故隐患应及时督促整改，并将检查情况及时报告项目负责人和上级安全监督管理部门，以便落实整改措施。附表2-3-6《安全员日巡查标准化表格》

- retrieved_nodes: L77, L78⭐, L79, L80


---

## latest_clean_niche_0226  ·  niche_fact

- **Query:** 根据《附件_安全管理规定（2020版）》中“2.4 隐患整改”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L82

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 481 |
| n_retrieved_nodes | 8 | 11 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 4.42 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L82` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C10` collect L81 (depth=0) · →L81 · +25
  - reason: Collect section 2.4 '隐患整改' to retrieve all relevant regulations and facts.
- `F1` finish - (depth=0)
  - reason: Assembled evidence fully covers section 2.4 Hazard Rectification including definitions, responsibilities, and procedures.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C10` | `L81` | - | 25 | 25 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 2.4 隐患整改]
  2.4.1 事故隐患分为一般事故隐患和重大事故隐患。
  1、一般事故隐患，是指危害和整改难度较小，发现后能够立即整改排除的隐患；
  2、重大事故隐患，是指危害和整改难度较大，应当全部或者局部停产停业，并经过一定时间整改治理方能排除的隐患，或者因外部因素影响致使生产经营单位自身难以排除的隐患。

**[E2]** [§ 2.4.2 隐患整改的职责]
  1、各项目的项目经理对事故隐患治理负直接全面责任；
  2、各二级单位主要负责人对事故隐患治理负直接管理领导责任；
  3、集团公司相关部门对事故隐患治理负监督管理责任。

**[E3]** [§ 2.4.3 一般事故隐患整改、复查、销项]
  1、一般事故隐患的治理由各项目部根据事故隐患的实际情况，制定针对性的治理措施，落实相关责任人，限期进行整改；
  2、集团公司各级安全检查发现的一般事故隐患，必须建立档案（事故隐患登记台账），由被检查项目负责整改，整改完成后在隐患整改回复单填写自检情况（须附证明材料），项目负责人复查验证，签字确认后上报二级单位，由二级单位复查销项。

- retrieved_nodes: L81, L82⭐, L83, L84, L85, L86, L87, L88, L89, L90, L91


---

## latest_clean_niche_0249  ·  niche_fact

- **Query:** 根据《附件_安全管理规定（2020版）》中“第三章 生产安全事故报告处理规定”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L115

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 499 |
| n_retrieved_nodes | 12 | 16 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.95 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L115` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C7` collect L113 (depth=0) · →L113 · +33
  - reason: Collect Chapter 3 to retrieve all regulations on accident reporting and handling.
- `F1` finish - (depth=0)
  - reason: Evidence covers Chapter 3 accident reporting, handling, investigation, and analysis as requested.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C7` | `L113` | - | 33 | 33 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 3.2 事故报告]
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

**[E2]** [§ 3.4 事故处理]
  3.4.4项目负责人安全事故处理
  1 发生较大及以上事故或暂扣集团公司安全生产许可证的一般事故，对项目部、二级单位、集团公司安全管理部相关责任人进行追责处理。
  3 发生集团公司负非主要责任的一般事故，对项目部相关责任人进行追责处理。

- retrieved_nodes: L113, L116, L117, L118, L119, L120, L121, L122, L123, L124, L125, L126, L130, L134, L139, L141


---

## latest_clean_niche_0258  ·  niche_fact

- **Query:** 根据《附件_安全管理规定（2020版）》中“3.4 事故处理”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L131

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 470 |
| n_retrieved_nodes | 8 | 6 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.93 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L131` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C20` collect L130 (depth=0) · multi→[L130, L131, L139, L142] · +12
  - reason: Collect section 3.4 and its specific rules on accident handling decisions, accountability, and fines.
- `F1` finish - (depth=0)
  - reason: Section G1 contains all relevant content from 3.4 Accident Handling as requested.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C20` | `L130` | L130, L131, L139, L142 | 12 | 15 | - | ✅ |

**水合告警:**
- step 1 整枝水合含 3 个非 gold 叶 (与 gold 争抢 evidence 预算)。

### 最终 evidence(new)

**[E1]** [§ 3.4 事故处理]
  3.4.1 依据事故调查报告，陕建股份《安全生产监督管理暂行办法》，集团公司《管理人员责任追究暂行规定》以及本条相关规定，由集集团公司董事会做出事故处理决定。对于上级组织的事故调查报告未涉及的责任人，由集团公司董事会根据责任人在事故中的具体责任做出处理决定。
  3.4.4项目负责人安全事故处理
  1 发生较大及以上事故或暂扣集团公司安全生产许可证的一般事故，对项目部、二级单位、集团公司安全管理部相关责任人进行追责处理。
  3 发生集团公司负非主要责任的一般事故，对项目部相关责任人进行追责处理。
  4 按照严重未履职（或违章指挥）、一般未履职（或履职不到位）对事故发生负责的主要直接责任人分别处以项目负责人事故罚款60%、30%的罚款处理，对事故发生负责的主要间接责任人分别处以项目负责人事故罚款40%、20%的罚款，对事故发生负责的一般直接负责人或一般间接责任人分别处以20%、10%的罚款。情节严重时按照照集团公司《管理人员责任追究暂行规定》第八条处以组织措施。履职尽责相关人员免责。

- retrieved_nodes: L130, L131⭐, L134, L139, L141, L142


---

## latest_clean_niche_0306  ·  niche_fact

- **Query:** 根据《附件_安全管理规定（2020版）》中“附表5.2.2：《施工现场安全负面清单（2019版）》”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L194

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 494 |
| n_retrieved_nodes | 15 | 12 |
| trajectory_steps | - | 5 |
| elapsed_sec | - | 9.39 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L194` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C32` collect L544 (depth=0) · →L544 · +1
  - reason: Target section contains the specific negative list content requested.
- `C33` collect L497 (depth=0) · →L497 · +1
  - reason: Collect the specific section containing the negative list title and content to answer the query.
- `C13` collect L189 (depth=0) · →L189 · +1
  - reason: Section C13 explicitly references the 'Negative List' and its usage restrictions as required by the query.
- `C35` collect L501 (depth=0) · →L501 · +47 · PURGED後代×1
  - reason: Collect section C35 to retrieve the full content of Appendix 5.2.2 'Construction Site Safety Negative List'.
- `F1` finish - (depth=0)
  - reason: Evidence G3, G1, and G2 directly address the query about '附表5.2.2' content and restrictions.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C32` | `L544` | - | 1 | 1 | - | ✅ |
| 2 | `C33` | `L497` | - | 1 | 1 | - | ✅ |
| 3 | `C13` | `L189` | - | 1 | 1 | - | ✅ |
| 4 | `C35` | `L501` | - | 47 | 47 | 1 | ✅ |

**水合告警:**
- step 4 `C35` 收父节点 `L501` 时 **purge 掉 1 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。

### 最终 evidence(new)

**[E1]** [§ 附件5.2.2                     施工现场安全负面清单（2]
文档列出使用不合格防坠器、超年限设备及维护不到位等问题的分包单位名单，并详细规定了塔吊、升降机、脚手架及临电设施等禁止或淘汰的技术标准与依据。

**[E2]** [§ 5.2机械设备管理]
5.2.2 严禁租赁集团公司《施工现场安全负面清单（2019版）》（见附表5.2-2）中禁止及限制使用的施工机械；租赁机械设备时，要求选择注册资金不小于200万元人民币的租赁单位，拟租起重机械机械使用年限应符合以下规定：

**[E3]** [§ 4.3.2 应急预案演练评价报]
5.2.2：《施工现场安全负面清单（2019版）》

**[E4]** [§ 附表6.6.1-2]
  专项方案应当组织专家论证的危险性较大的分部分项工程识别清单
  工程名称：
  备注：本表中所列工程，若本工程施工中有时在对应的辨识结论栏内打“√”，无时打“×”。

**[E5]** [§ 附表6.6.1-1]
  危险性较大的分部分项工程识别清单
  备注： 本表中所列工程，若本工程施工中有时在对应的辨识结论栏内打“√”，无时打“×”。

- retrieved_nodes: L501, L544, L545, L189, L497, L555, L556, L557, L558, L551, L552, L554


---

## latest_clean_niche_0321  ·  niche_fact

- **Query:** 根据《附件_安全管理规定（2020版）》中“5.3.2 按陕建监总发[2014]04号文要求：”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L211

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 276 |
| n_retrieved_nodes | 16 | 4 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.98 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L211` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C20` collect L210 (depth=0) · →L210 · +3
  - reason: Target section 5.3.2 explicitly mentions the required document and likely contains the specific regulation requested.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains the specific section 5.3.2 and its related requirements as requested.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C20` | `L210` | - | 3 | 3 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 5.3.2 按陕建监总发[2014]04号文要求：]
  自2015年1月1日起，附着式升降脚手架外立面、底板、脚手板必须使用具有防火功能的防护产品；
  吊篮的安/拆（包括二次移位）工作，均应由出租单位负责完成，使用单位不得安拆、转租吊篮；
  5.3.3 附着式升降脚手架、高空作业吊篮等工具式脚手架的专项方案由专业分包单位组织编制，方案应符合《建筑施工工具式脚手架安全技术规范》JGJ202-2010（以下简称JGJ202-2010）的相关规定。并经过分包单位具有法人资格企业的技术负责人批准。再按照专项方案审批程序履行审批手续。

- retrieved_nodes: L210, L211⭐, L212, L213


---

## latest_clean_niche_0325  ·  niche_fact

- **Query:** 根据《附件_安全管理规定（2020版）》中“5.3.4 附着式升降脚手架、高空作业吊篮等管理程序：”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L215

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 492 |
| n_retrieved_nodes | 7 | 9 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 4.91 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L215` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C12` collect L214 (depth=0) · →L214 · +18
  - reason: Section 5.3.4 contains the specific management procedures for the queried equipment.
- `F1` finish - (depth=0)
  - reason: Evidence G1 fully covers the specific regulations for 5.3.4 regarding scaffolding and basket management.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C12` | `L214` | - | 18 | 18 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 5.3.4 附着式升降脚手架、高空作业吊篮等管理程序：]
  1、从集团公司合格供方名单中选取附着式升降脚手架分包单位，选择有资质的高空作业吊篮分包单位；
  5、分包单位按专项施工方案进场安装，附着式升降脚手架安拆/升降作业人员应经专门培训、持有附着式脚手架特种作业操作资格证书，作业前应对所有作业人员进行安全教育和安全技术交底；
  8、吊篮出租单位应当对进入吊篮内作业的人员进行吊篮操作技能和安全知识教育培训、考核，吊篮出租与使用单位均应对操作人员进行相关的安全技术交底；
  1、附着式升降脚手架按JGJ202-2010表8.1.3《附着式升降脚手架首次安装完毕及检查使用前检查验收表》的内容验收；
  2、高处作业吊篮按JGJ202-2010表8.2.2《高处作业吊篮使用验收表》的内容验收。
  5.3.6 附着式升降脚手架使用工况，升降工况管理必须严格按照专项方案实施。
  升降工况作业前按JGJ202-2010表8.1.3《附着式升降脚手架首次安装完毕及检查使用前检查验收表》的内容验收。
  升降工况下，架体上不得有施工荷载，严禁人员在架体上停留。

- retrieved_nodes: L214, L215⭐, L221, L224, L228, L229, L230, L231, L232


---

## latest_clean_niche_0413  ·  niche_fact

- **Query:** 根据《附件_安全管理规定（2020版）》中“6.4 安全生产违章行为处罚”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L315

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 497 |
| n_retrieved_nodes | 10 | 11 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 4.08 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L315` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C17` collect L314 (depth=0) · →L314 · +39
  - reason: Section 6.4 contains the specific penalties for safety violations as requested.
- `F1` finish - (depth=0)
  - reason: Section G1 contains all relevant content from 6.4 regarding penalties for safety violations.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C17` | `L314` | - | 39 | 39 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 6.4 安全生产违章行为处罚]
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

- retrieved_nodes: L314, L315⭐, L320, L324, L329, L337, L345, L346, L347, L348, L349


---

## latest_clean_niche_0460  ·  niche_fact

- **Query:** 根据《附件_安全管理规定（2020版）》中“6.8 危险源监控管理”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L376

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 473 |
| n_retrieved_nodes | 9 | 7 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.99 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L376` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C21` collect L375 (depth=0) · →L375 · +7
  - reason: Collect section 6.8 to retrieve all regulations on hazard source monitoring as requested.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains all relevant sections of 6.8 Hazard Source Monitoring Management.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C21` | `L375` | - | 7 | 7 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 6.8 危险源监控管理]
  6.8.2 危险源辨识应根据施工作业活动、施工作业流程和施工工艺，采用科学合理的辨识方法，辨识方法见《危险源辨识、风险评价与控制程序》，项目部对管辖区域和施工现场可能存在的危险源进行分析辨识，列出危险源清单。
  6.8.3 对已辨识出来的危险源采用定性和定量评价，分析导致事故发生的可能性和事故后果，确定风险等级及重大危险源，列出重大危险源清单。
  6.8.4 根据重大危险源清单，制定管理方案，明确重大危险源的目标、指标、控制措施，并落实相关部门及专人负责监督、管理。
  6.8.5 加强对重大危险源的巡查和监控，采取相应的预防及控制措施，消除或降低其影响，使其达到可接受的程度，保证集团公司职业健康安全管理目标的实现。
  6.8.6 项目部应在工地醒目位置设立“不可接受风险公示牌”（见集团公司《施工现场标准化管理手册》），公示牌应注明危险源、存在部位、作业时间、防护措施和责任人等内容。
  6.8.7二级单位、项目部应随所管区域变化和工程施工的进度及时进行更新对危险源辨识和风险评价。

- retrieved_nodes: L375, L377, L378, L379, L380, L381, L382


---

## latest_clean_niche_0473  ·  niche_fact

- **Query:** 根据《附件_安全管理规定（2020版）》中“6.10 施工机具管理”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L391

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 488 | 489 |
| n_retrieved_nodes | 13 | 7 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.82 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L391` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C22` collect L390 (depth=0) · →L390 · +9
  - reason: Collect section 6.10 Construction Machinery Management to answer the query.
- `F1` finish - (depth=0)
  - reason: Section G1 contains all relevant facts from 6.10 Construction Machinery Management.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C22` | `L390` | - | 9 | 9 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 6.10 施工机具管理]
  6.10.2 项目部材料动力组负责施工机具的日常检查及定期检查工作。检查依据：《建筑施工安全检查标准JGJ59-2011》，《建筑机械使用安全技术规程JGJ33-2012》，《施工现场机械设备检查技术规程JGJ160-2008》。
  6.10.3 项目部材料动力组负责施工机具的安装调试，施工机具安装完毕后由项目部组织按规定履行验收程序验收（总包方、分包方、租赁方、安装方、监理方），并应经责任人签字确认。
  6.10.4 项目部自有或租赁的施工机具，负有使用、维护、保养管理工作的义务。但劳务分包，专业分包或租赁的施工机具，合同及安全管理协议书必须明确使用、维护、保养管理工作的责任方。
  6.10.5 施工机具的各种检测仪表及安全装置必须齐全有效，严禁使用安全装置不齐全有效、超过使用年限或技术性能落后耗能高、效率低的施工机具。
  6.10.6 施工机具的现场工作环境必须符合要求，禁止在不适宜的工作环境下使用施工机具。
  6.10.9 施工机具出现故障或异常情况时应立即停机，待故障排除后方可使用，严禁机械带病运转。

- retrieved_nodes: L390, L392, L393, L394, L395, L396, L399


---

## latest_clean_niche_0500  ·  niche_fact

- **Query:** 根据《附件_安全管理规定（2020版）》中“7.2 总平面布局”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L424

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 481 | 390 |
| n_retrieved_nodes | 8 | 5 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.53 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L424` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C28` collect L423 (depth=0) · →L423 · +4
  - reason: Target section 7.2 Total Layout found with relevant content.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains all required content from section 7.2 regarding total layout regulations.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C28` | `L423` | - | 4 | 4 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 7.2 总平面布局]
  7.2.1 施工现场出入口的设置必须满足消防车通行的要求，并应布置在不同方向，其数量不宜少于2个。当确有困难只能设置1个出入口时，在施工现场内设置满足消防车通行的环形道路，消防车道的净宽度和净空高度均不应小于4米。
  7.2.2 宿舍、厨房操作间、配电室、可燃材料堆场及其加工场、可燃材料及易燃易爆危险品库房等临时用房、临时设施不能设置于在建工程内。
  7.2.3 固定动火作业场要布置在可燃材料堆场及其加工场、易燃易爆危险品库房等全年最小频率风向的上风侧，并宜布置在临时办公用房、宿舍、可燃材料库房、在建工程等全年最小频率风向的上风侧。
  7.2.4 易燃易爆危险品库房与在建工程的防火间距不小于15m，可燃材料堆场及其加工场、固定动火作业场与在建工程的防火间距不小于10m，其它临时用房、临时设施与在建工程的防火间距不小于6m。

- retrieved_nodes: L423, L424⭐, L425, L426, L427


---

## latest_clean_niche_0510  ·  niche_fact

- **Query:** 根据《附件_安全管理规定（2020版）》中“7.5 防火管理一般规定”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L437

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 423 |
| n_retrieved_nodes | 9 | 7 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 4.69 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L437` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C27` collect L436 (depth=0) · multi→[L436, L437, L438, L439, L441, L442] · +6
  - reason: Collect all leaf nodes under section 7.5 to answer the query about fire management regulations.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains all regulations from section 7.5 regarding fire safety management.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C27` | `L436` | L436, L437, L438, L439, L441, L442 | 6 | 11 | - | ✅ |

**水合告警:**
- step 1 整枝水合含 5 个非 gold 叶 (与 gold 争抢 evidence 预算)。

### 最终 evidence(new)

**[E1]** [§ 7.5 防火管理一般规定]
  7.5.1 施工现场的消防安全管理由责任单位统一管理，项目部具体负责落实。
  7.5.2 施工单位(项目部)必须根据建设项目规模、现场消防安全管理的重点，制订消防安全管理制度，建立消防安全管理组织机构及义务消防组织，并确定消防安全负责人和消防安全管理人员，同时落实相关人员的消防安全管理责任。
  7.5.3 施工单位(项目部)必须编制施工现场消防应急预案，定期组织消防演练，并根据现场情况变化及时对其修改、完善和持续改进。
  7.5.4 施工人员进场时，施工现场的消防安全管理人员必须向施工人员进行消防安全教育和培训。施工作业前，必须向作业人员进行消防安全技术交底。
  7.5.5 施工过程中，施工现场的消防安全负责人必须定期组织消防安全管理人员对施工现场的消防安全进行检查。
  7.5.6 施工单位(项目部)必须做好并保存施工现场消防安全管理的相关文件和记录，建立现场消防安全管理档案。

- retrieved_nodes: L436, L437⭐, L438, L439, L440, L441, L442


---

## latest_clean_niche_0519  ·  niche_fact

- **Query:** 根据《附件_安全管理规定（2020版）》中“7.7.1 施工现场用火管理”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L449

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 356 |
| n_retrieved_nodes | 10 | 7 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 4.04 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L449` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C33` collect L448 (depth=0) · →L448 · +6
  - reason: Target section 7.7.1 explicitly contains the required regulations on fire management.
- `F1` finish - (depth=0)
  - reason: Section G1 contains all required regulations for 7.7.1施工现场用火管理.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C33` | `L448` | - | 6 | 6 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 7.7.1 施工现场用火管理]
  1、施工现场动火作业必须办理动火许可证；动火操作人员必须具有相应资格；
  2、施工现场在进行焊接、切割、烘烤或加热等动火作业前，必须对作业现场的可燃物进行清理；对于作业现场及其附近无法移走的可燃物，必须采用不燃材料对其覆盖或隔离；裸露的可燃材料上严禁直接进行动火作业；
  3、焊接、切割、烘烤或加热等动火作业，必须配备灭火器材，并设动火监护人进行现场一对一监护；
  4、五级（含五级）以上风力时，必须停止焊接、切割等室外动火作业，否则必须采取可靠的挡风措施；
  5、动火作业后，必须对现场进行检查，确认无火灾危险后，动火操作人员方可离开；
  6、施工现场不应采用明火取暖；厨房操作间炉灶使用完毕后，必须将炉火熄灭，排油烟机及油烟管道必须定期清理油垢。

- retrieved_nodes: L448, L449⭐, L450, L451, L452, L453, L454


---

## latest_clean_niche_0525  ·  niche_fact

- **Query:** 根据《附件_安全管理规定（2020版）》中“7.7.2 施工现场用电管理”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L456

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 414 |
| n_retrieved_nodes | 10 | 7 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.91 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L456` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C30` collect L455 (depth=0) · →L455 · +6
  - reason: Target section 7.7.2 contains the specific regulations on construction site electricity management requested.
- `F1` finish - (depth=0)
  - reason: Section G1 contains all explicit regulations for 7.7.2施工现场用电管理 as requested.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C30` | `L455` | - | 6 | 6 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 7.7.2 施工现场用电管理]
  1、电气线路必须具有相应的绝缘强度和机械强度，破损、烧焦的插座、插头应及时更换；
  2、电气设备与可燃、易燃易爆和腐蚀性物品保持一定的安全距离；
  3、有爆炸和火灾危险的场所，按危险等级选用相应的电气设备，电气设备不能超负荷运行或带故障使用；
  4、配电箱内每个电气回路必须设置漏电保护器、过载保护器，距配电箱2m范围内不能堆放可燃物，5m范围内不能设置可能产生较多易燃、易爆气体、粉尘的作业区；
  5、可燃材料库房不能使用高热灯具，易燃易爆危险品库房内必须使用防爆灯具，普通灯具与易燃物距离不小于300mm，聚光灯、碘钨灯等高热灯具与易燃物距离不宜小于500mm；
  6、施工现场办公、生活区和施工区禁止私自改装现场供用电设施，严禁在宿舍使用不合格的电褥子、大功率热水器等电器。项目部必须定期对办公、生活区和施工区安全用电、电气设备和线路的运行及维护情况进行检查。

- retrieved_nodes: L455, L456⭐, L457, L458, L459, L460, L461


---

## latest_clean_niche_0531  ·  niche_fact

- **Query:** 根据《附件_安全管理规定（2020版）》中“7.7.3 施工现场用气管理”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L464

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 478 |
| n_retrieved_nodes | 9 | 11 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.91 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L464` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C31` collect L462 (depth=0) · →L462 · +14
  - reason: Target section 7.7.3 contains specific rules on gas management in construction sites.
- `F1` finish - (depth=0)
  - reason: The assembled evidence G1 fully contains the specific regulations for section 7.7.3 regarding site gas management.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C31` | `L462` | - | 14 | 14 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 7.7.3 施工现场用气管理]
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

- retrieved_nodes: L462, L463, L465, L466, L467, L468, L469, L470, L471, L472, L475


---

## latest_clean_niche_0551  ·  niche_fact

- **Query:** 根据《附件_安全管理规定（2020版）》中“3.2 生产安全事故快报”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L493

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 498 |
| n_retrieved_nodes | 11 | 21 |
| trajectory_steps | - | 3 |
| elapsed_sec | - | 5.47 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L493` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C33` collect L492 (depth=0) · →L492 · +51
  - reason: Section 3.2 explicitly contains the 'Production Safety Accident Quick Report' content requested.
- `C15` collect L116 (depth=0) · →L116 · +10
  - reason: Collect section 3.2 to retrieve specific regulations on production safety accident rapid reporting.
- `F1` finish - (depth=0)
  - reason: Evidence G1 and G2 contain the specific regulations for '3.2 生产安全事故快报' including reporting content and the fast report form.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C33` | `L492` | - | 51 | 51 | - | ✅ |
| 2 | `C15` | `L116` | - | 10 | 10 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 3.2 事故报告]
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

**[E2]** [§ 附表3.2]
  生产安全事故快报
  单位名称：

**[E3]** [§ 3.2 生产安全事故快报]
  3.7-1 职工伤亡事故月（年）报表
  3.7-3 安全生产信息季（年）度报表
  4.3.1 应急预案演练方案

**[E4]** [§ 附表1.2-3]
工程名称

- retrieved_nodes: L116, L117, L118, L119, L120, L121, L122, L123, L124, L125, L126, L492, L501, L534, L535, L536, L493⭐, L494, L495, L522, L524


---

## latest_clean_niche_0553  ·  niche_fact

- **Query:** 根据《附件_安全管理规定（2020版）》中“4.3.2 应急预案演练评价报”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L497

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 297 | 462 |
| n_retrieved_nodes | 4 | 11 |
| trajectory_steps | - | 8 |
| elapsed_sec | - | 14.8 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L497` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C13` collect L167 (depth=0) · →L167 · +1
  - reason: Section 4.3.2 explicitly details the requirements for the emergency plan drill evaluation report.
- `C27` collect L496 (depth=0) · →L496 · +1
  - reason: Section N27 explicitly contains the title '4.3.2 应急预案演练评价报' which is the target of the query.
- `C22` collect L176 (depth=0) · →L176 · +1
  - reason: Collect section C22 (4.3.2 Evaluation Report) to retrieve the specific content of the regulation.
- `C37` collect L542 (depth=0) · →L542 · +1
  - reason: Collect section C37 (4.3.2 Evaluation Report) to retrieve the specific regulations requested.
- `C19` collect L168 (depth=0) · →L168 · +1
  - reason: Section C19 (4.3.3) contains the specific rule regarding revision of emergency plans based on evaluation reports.
- `C17` collect L165 (depth=0) · →L165 · +3 · PURGED後代×2
  - reason: Collect section 4.3 to access the full content of 4.3.2 regarding emergency plan evaluation reports.
- `C35` collect L541 (depth=0) · →L541 · +2 · PURGED後代×1
  - reason: Collect section D20 (4.3.2) to retrieve the specific content of the emergency plan drill evaluation report.
- `C31` collect L540 (depth=0) · →L540 · +1
  - reason: Collect section C31 to retrieve the specific content of '4.3.2 应急预案演练评价报' as it is currently missing from evidence.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C13` | `L167` | - | 1 | 1 | - | ✅ |
| 2 | `C27` | `L496` | - | 1 | 1 | - | ✅ |
| 3 | `C22` | `L176` | - | 1 | 1 | - | ✅ |
| 4 | `C37` | `L542` | - | 1 | 1 | - | ✅ |
| 5 | `C19` | `L168` | - | 1 | 1 | - | ✅ |
| 6 | `C17` | `L165` | - | 3 | 3 | 2 | ✅ |
| 7 | `C35` | `L541` | - | 2 | 2 | 1 | ✅ |
| 8 | `C31` | `L540` | - | 1 | 1 | - | ✅ |

**水合告警:**
- step 6 `C17` 收父节点 `L165` 时 **purge 掉 2 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。
- step 7 `C35` 收父节点 `L541` 时 **purge 掉 1 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。

### 最终 evidence(new)

**[E1]** [§ 4.3 应急救援预案的演练]
  4.3.1 集团公司的综合应急救援预案每二年演练一次；项目部根据工程特点，项目施工（基础，主体，装饰）阶段，每年至少演练一次。演练必须编制演练方案（附表4.3.1：应急预案演练方案），并对参演人员进行宣传培训。
  4.3.2 演练结束后，演练组织部门对应急救援预案和处置程序的有效性、人员宣传培训和需求、设备和资源的充分性、应急救援行动以及是否达到预期目标作出评价报告（附表4.3.2：应急预案演练评价报告），交集团公司安全管理部存档。
  4.3.3 根据规范要求变化，应急预案环境改变，演练评价报告每一到二年修订应急救援预案。

**[E2]** [§ 4.4 应急响应程序]
附表4.3.2：应急预案演练评价报告。

**[E3]** [§ 附表4.3.2]
  应急预案演练评价报告
  工程名称：

**[E4]** [§ 附表4.3.1]
注：应急预案演练记录照片或影像资料附后。

**[E5]** [§ 4.3.2 应急预案演练评价报]
5.2.2：《施工现场安全负面清单（2019版）》

- retrieved_nodes: L165, L166, L167, L168, L176, L541, L542, L543, L540, L496, L497⭐


---

## latest_clean_niche_0554  ·  niche_fact

- **Query:** 根据《附件_安全管理规定（2020版）》中“6.7.3 安全技术交底记录”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L505

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 362 | 171 |
| n_retrieved_nodes | 6 | 5 |
| trajectory_steps | - | 5 |
| elapsed_sec | - | 9.39 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L505` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C21` collect L374 (depth=0) · →L374 · +1
  - reason: Section 6.7.3 explicitly states the signing and record-keeping requirements for safety technical disclosure.
- `C37` collect L560 (depth=0) · →L560 · +1
  - reason: Collect section C37 (6.7.3 Safety Technical Disclosure Record) to retrieve the specific content of the regulation.
- `C39` collect L559 (depth=0) · →L559 · +2 · PURGED後代×1
  - reason: Collect section C39 (附表6.7.3) to retrieve the specific content of the safety technical disclosure record form.
- `C27` collect L413 (depth=0) · →L413 · +1
  - reason: Collect section 6.7.3 to retrieve the specific content of the safety technical disclosure record form.
- `F1` finish - (depth=0)
  - reason: Evidence collected covers §6.7.3 requirements: signature confirmation by交底人,被交底人,专职安全员 and record preservation.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C21` | `L374` | - | 1 | 1 | - | ✅ |
| 2 | `C37` | `L560` | - | 1 | 1 | - | ✅ |
| 3 | `C39` | `L559` | - | 2 | 2 | 1 | ✅ |
| 4 | `C27` | `L413` | - | 1 | 1 | - | ✅ |

**水合告警:**
- step 3 `C39` 收父节点 `L559` 时 **purge 掉 1 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。

### 最终 evidence(new)

**[E1]** [§ 6.7 安全技术交底管理]
6.7.3 安全技术交底应由交底人、被交底人、专职安全员进行签字确认。并由项目部专职安全员保存安全技术交底记录（附表6.7.3 安全技术交底记录）。

**[E2]** [§ 6.11 安全标志]
附表6.7.3：安全技术交底记录。

**[E3]** [§ 附表6.7.3]
  安全技术交底记录
  工程名称：

- retrieved_nodes: L374, L413, L559, L560, L561


---

## latest_clean_niche_0567  ·  niche_fact

- **Query:** 根据《附件_安全管理规定（2020版）》中“附件5.2.2 施工现场安全负面清单（2019版）”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L545

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 304 |
| n_retrieved_nodes | 17 | 4 |
| trajectory_steps | - | 5 |
| elapsed_sec | - | 9.72 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L545` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C35` collect L545 (depth=0) · →L545 · +1
  - reason: Directly contains the specific facts and regulations of Appendix 5.2.2 regarding negative list items.
- `C34` collect L544 (depth=0) · →L544 · +1 · PURGED後代×1
  - reason: Collect the specific content of Attachment 5.2.2 to answer the query about explicit regulations.
- `C32` collect L497 (depth=0) · →L497 · +1
  - reason: Collect leaf C32 to retrieve the specific content of 'Attachment 5.2.2' as requested.
- `C13` collect L189 (depth=0) · →L189 · +1
  - reason: Section C13 explicitly references the 'Negative List' and its usage restrictions, directly addressing the query.
- `F1` finish - (depth=0)
  - reason: Evidence collected covers the specific regulations and facts from Attachment 5.2.2 regarding the negative list.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C35` | `L545` | - | 1 | 1 | - | ✅ |
| 2 | `C34` | `L544` | - | 1 | 1 | 1 | ✅ |
| 3 | `C32` | `L497` | - | 1 | 1 | - | ✅ |
| 4 | `C13` | `L189` | - | 1 | 1 | - | ✅ |

**水合告警:**
- step 2 `C34` 收父节点 `L544` 时 **purge 掉 1 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。

### 最终 evidence(new)

**[E1]** [§ 附件5.2.2                     施工现场安全负面清单（2]
文档列出使用不合格防坠器、超年限设备及维护不到位等问题的分包单位名单，并详细规定了塔吊、升降机、脚手架及临电设施等禁止或淘汰的技术标准与依据。

**[E2]** [§ 5.2机械设备管理]
5.2.2 严禁租赁集团公司《施工现场安全负面清单（2019版）》（见附表5.2-2）中禁止及限制使用的施工机械；租赁机械设备时，要求选择注册资金不小于200万元人民币的租赁单位，拟租起重机械机械使用年限应符合以下规定：

**[E3]** [§ 4.3.2 应急预案演练评价报]
5.2.2：《施工现场安全负面清单（2019版）》

- retrieved_nodes: L544, L545⭐, L189, L497


---

## latest_clean_niche_0572  ·  niche_fact

- **Query:** 根据《附件_安全管理规定（2020版）》中“附表6.6.1-2”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60974d4242eda8c47c615`
- **Gold nodes:** L556

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 53 |
| n_retrieved_nodes | 18 | 1 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.88 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L556` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C31` collect L412 (depth=0) · →L412 · +1
  - reason: Target section '附表6.6.1-2' is explicitly listed as a leaf node.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains the specific content of Appendix 6.6.1-2 as requested.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C31` | `L412` | - | 1 | 1 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 6.11 安全标志]
附表6.6.1-2：超过一定规模的危险性较大的分部分项工程识别清单；

- retrieved_nodes: L412


---

## latest_clean_niche_0600  ·  niche_fact

- **Query:** 根据《陕西建工第十一建集团有限公司生产安全事故综合应急预案（2025版）》中“1.2 编制依据”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c6097ad4242eda8c47c62c`
- **Gold nodes:** L6

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 480 | 350 |
| n_retrieved_nodes | 11 | 12 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.56 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L6` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C4` collect L4 (depth=0) · →L4 · +11
  - reason: Collect section 1.2 '编制依据' to retrieve the listed regulations and facts.
- `F1` finish - (depth=0)
  - reason: Section G1 contains the complete list of regulations and facts under '1.2 编制依据' as requested.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C4` | `L4` | - | 11 | 11 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 1.2 编制依据]
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

- retrieved_nodes: L4, L10, L11, L12, L13, L14, L15, L5, L6⭐, L7, L8, L9


---

## latest_clean_niche_0657  ·  niche_fact

- **Query:** 根据《陕西建工第十一建集团有限公司生产安全事故综合应急预案（2025版）》中“2.4 集团公司应急救援总指挥部部门职责”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c6097ad4242eda8c47c62c`
- **Gold nodes:** L79

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 495 | 496 |
| n_retrieved_nodes | 10 | 17 |
| trajectory_steps | - | 4 |
| elapsed_sec | - | 5.83 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L79` | ✅ | True | False |

### 决策 TRACE(因果序)

- `D7` dispatch L77 (depth=0) · regions=[L77] · child_reports=1
  - reason: Dispatch section 2.4 to retrieve all department responsibilities under the emergency command headquarters.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L77 (depth=1) · →L77 · +46
      - reason: Collects the full section 2.4 to retrieve all department responsibilities as requested.
    - `F1` finish - (depth=1)
      - reason: The required section '2.4 集团公司应急救援总指挥部部门职责' has been collected in the previous step. No further collection is needed.
- `F1` finish - (depth=0)
  - reason: Section 2.4 department responsibilities fully collected and ranked by relevance.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L77` | - | 46 | 46 | - | ✅ |

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c6097ad4242eda8c47c62c:L77 (ok)
collected 47 branch node(s); explicit roots=['real_69c6097ad4242eda8c47c62c:L77']
collected: real_69c6097ad4242eda8c47c62c:L100, real_69c6097ad4242eda8c47c62c:L101, real_69c6097ad4242eda8c47c62c:L102, real_69c6097ad4242eda8c47c62c:L103, real_69c6097ad4242eda8c47c62c:L104, real_69c6097ad4242eda8c47c62c:L105, real_69c6097ad4242eda8c47c62c:L106, real_69c6097ad4242eda8c47c62c:L107, real_69c6097ad4242eda8c47c62c:L108, real_69c6097ad4242eda8c47c62c:L109, real_69c6097ad4242eda8c47c62c:L110, real_69c6097ad4242eda8c47c62c:L111, real_69c6097ad4242eda8c47c62c:L112, real_69c6097ad4242eda8c47c62c:L113, real_69c6097ad4242eda8c47c62c:L114, real_69c6097ad4242eda8c47c62c:L115, real_69c6097ad4242eda8c47c62c:L116, real_69c6097ad4242eda8c47c62c:L117, real_69c6097ad4242eda8c47c62c:L118, real_69c6097ad4242eda8c47c62c:L119
reason: The required section '2.4 集团公司应急救援总指挥部部门职责' has been collected in the previous step. No further collection is needed.
---
=== End Investigate ===
```

### 最终 evidence(new)

**[E1]** [§ 2.4 集团公司应急救援总指挥部部门职责]
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

- retrieved_nodes: L77, L100, L102, L106, L108, L110, L115, L117, L121, L79⭐, L81, L82, L83, L85, L89, L90, L94


---

## latest_clean_niche_0690  ·  niche_fact

- **Query:** 根据《陕西建工第十一建集团有限公司生产安全事故综合应急预案（2025版）》中“2.5 二级单位应急救援领导小组成员职责”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c6097ad4242eda8c47c62c`
- **Gold nodes:** L126

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 479 | 500 |
| n_retrieved_nodes | 8 | 13 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.62 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L126` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C14` collect L124 (depth=0) · →L124 · +27
  - reason: Target section 2.5 contains the specific duties of secondary unit emergency rescue leadership group members.
- `F1` finish - (depth=0)
  - reason: The assembled evidence G1 contains the complete content of section 2.5 regarding the responsibilities of the secondary unit emergency rescue leadership group members.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C14` | `L124` | - | 27 | 27 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 2.5 二级单位应急救援领导小组成员职责]
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

- retrieved_nodes: L124, L126⭐, L127, L129, L132, L135, L137, L138, L141, L143, L144, L146, L149


---

## latest_clean_niche_0711  ·  niche_fact

- **Query:** 根据《陕西建工第十一建集团有限公司生产安全事故综合应急预案（2025版）》中“2.6 项目部应急救援领导小组成员职责”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c6097ad4242eda8c47c62c`
- **Gold nodes:** L155

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 490 | 500 |
| n_retrieved_nodes | 9 | 13 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.63 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L155` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C14` collect L152 (depth=0) · →L152 · +40
  - reason: Section 2.6 contains the specific duties of the project department emergency rescue leadership group members as requested.
- `F1` finish - (depth=0)
  - reason: Section G1 contains the complete list of duties for the Project Department Emergency Rescue Leadership Group as requested.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C14` | `L152` | - | 40 | 40 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 2.6 项目部应急救援领导小组成员职责]
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

- retrieved_nodes: L152, L154, L159, L162, L165, L166, L168, L169, L170, L176, L177, L181, L191


---

## latest_clean_niche_0741  ·  niche_fact

- **Query:** 根据《陕西建工第十一建集团有限公司生产安全事故综合应急预案（2025版）》中“2.7 各应急救援小组职责”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c6097ad4242eda8c47c62c`
- **Gold nodes:** L195

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 495 | 490 |
| n_retrieved_nodes | 8 | 16 |
| trajectory_steps | - | 4 |
| elapsed_sec | - | 5.88 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L195` | ✅ | True | False |

### 决策 TRACE(因果序)

- `D10` dispatch L193 (depth=0) · regions=[L193] · child_reports=1
  - reason: Dispatch to section 2.7 to retrieve all specific duties of emergency rescue groups as requested.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L193 (depth=1) · →L193 · +25
      - reason: Collects the full section 2.7 to retrieve all specified duties of emergency rescue groups.
    - `F1` finish - (depth=1)
      - reason: Collected section L193 contains the required content on emergency rescue group duties. Ready to answer.
- `F1` finish - (depth=0)
  - reason: Section G1 contains the complete list of duties for each emergency rescue group as requested.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L193` | - | 25 | 25 | - | ✅ |

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c6097ad4242eda8c47c62c:L193 (ok)
collected 26 branch node(s); explicit roots=['real_69c6097ad4242eda8c47c62c:L193']
collected: real_69c6097ad4242eda8c47c62c:L193, real_69c6097ad4242eda8c47c62c:L194, real_69c6097ad4242eda8c47c62c:L195, real_69c6097ad4242eda8c47c62c:L196, real_69c6097ad4242eda8c47c62c:L197, real_69c6097ad4242eda8c47c62c:L198, real_69c6097ad4242eda8c47c62c:L199, real_69c6097ad4242eda8c47c62c:L200, real_69c6097ad4242eda8c47c62c:L201, real_69c6097ad4242eda8c47c62c:L202, real_69c6097ad4242eda8c47c62c:L203, real_69c6097ad4242eda8c47c62c:L204, real_69c6097ad4242eda8c47c62c:L205, real_69c6097ad4242eda8c47c62c:L206, real_69c6097ad4242eda8c47c62c:L207, real_69c6097ad4242eda8c47c62c:L208, real_69c6097ad4242eda8c47c62c:L209, real_69c6097ad4242eda8c47c62c:L210, real_69c6097ad4242eda8c47c62c:L211, real_69c6097ad4242eda8c47c62c:L212
reason: Collected section L193 contains the required content on emergency rescue group duties. Ready to answer.
---
=== End Investigate ===
```

### 最终 evidence(new)

**[E1]** [§ 2.7 各应急救援小组职责]
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

- retrieved_nodes: L193, L194, L195⭐, L196, L200, L201, L204, L205, L206, L208, L209, L210, L211, L212, L216, L217


---

## latest_clean_niche_0759  ·  niche_fact

- **Query:** 根据《陕西建工第十一建集团有限公司生产安全事故综合应急预案（2025版）》中“3.1 信息报告”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c6097ad4242eda8c47c62c`
- **Gold nodes:** L222

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 495 | 492 |
| n_retrieved_nodes | 13 | 13 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.99 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L222` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C13` collect L220 (depth=0) · →L220 · +25
  - reason: Collect section 3.1 Information Reporting to answer the query about reporting regulations.
- `F1` finish - (depth=0)
  - reason: Section G1 contains the complete '3.1 Information Reporting' content including reporting procedures, timelines, and required information details.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C13` | `L220` | - | 25 | 25 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 3.1 信息报告]
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

- retrieved_nodes: L220, L221, L222⭐, L223, L224, L225, L229, L232, L233, L234, L239, L240, L241


---

## latest_clean_niche_0795  ·  niche_fact

- **Query:** 根据《陕西建工第十一建集团有限公司生产安全事故综合应急预案（2025版）》中“3.5 应急支援”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c6097ad4242eda8c47c62c`
- **Gold nodes:** L280

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 483 | 492 |
| n_retrieved_nodes | 11 | 8 |
| trajectory_steps | - | 4 |
| elapsed_sec | - | 6.38 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L280` | ✅ | True | False |

### 决策 TRACE(因果序)

- `D10` dispatch L219 (depth=0) · regions=[L219] · child_reports=1
  - reason: Dispatch to section 3应急响应 to locate subsection 3.5 应急支援.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L219 (depth=1) · →L219 · +64
      - reason: Collect section 3 to access subsection 3.5 '应急支援' as requested.
    - `F1` finish - (depth=1)
      - reason: The current scope L219 contains the '3.5 应急支援' section, and evidence has been collected to answer the query.
- `F1` finish - (depth=0)
  - reason: Section G10 (§3.5 应急支援) contains the specific regulations requested by the user.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L219` | - | 64 | 64 | - |  |

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c6097ad4242eda8c47c62c:L219 (ok)
collected 150 branch node(s); explicit roots=['real_69c6097ad4242eda8c47c62c:L219']
collected: real_69c6097ad4242eda8c47c62c:L219, real_69c6097ad4242eda8c47c62c:L220, real_69c6097ad4242eda8c47c62c:L221, real_69c6097ad4242eda8c47c62c:L222, real_69c6097ad4242eda8c47c62c:L223, real_69c6097ad4242eda8c47c62c:L224, real_69c6097ad4242eda8c47c62c:L225, real_69c6097ad4242eda8c47c62c:L226, real_69c6097ad4242eda8c47c62c:L227, real_69c6097ad4242eda8c47c62c:L228, real_69c6097ad4242eda8c47c62c:L229, real_69c6097ad4242eda8c47c62c:L230, real_69c6097ad4242eda8c47c62c:L231, real_69c6097ad4242eda8c47c62c:L232, real_69c6097ad4242eda8c47c62c:L233, real_69c6097ad4242eda8c47c62c:L234, real_69c6097ad4242eda8c47c62c:L235, real_69c6097ad4242eda8c47c62c:L236, real_69c6097ad4242eda8c47c62c:L237, real_69c6097ad4242eda8c47c62c:L238
reason: The current scope L219 contains the '3.5 应急支援' section, and evidence has been collected to answer the query.
---
=== End Investigate ===
```

### 最终 evidence(new)

**[E1]** [§ 3.5  应急支援]
  当事态无法控制时，应立即寻求外部力量支持，如当地应急管理部门、 质量安全监督站、医院、公安、消防、救援中心等。
  （ 1 ）当Ⅲ 级（项目经理部）响应事故存在失控可能时，应向事故发生项目所在二级单位应急救援领导小组报告请求支援。在集团公司应急救援指挥部赶到现场后，项目经理部将指挥权移交现场最高领导。
  （3 ） 当I 级（集团公司级）响应事故存在失控可能，由集团公司应急救援办公室按信息报告相关规定报告属地政府应急管理部门，政府应急指挥组织机构赶到现场后，现场指挥权应立即移交政府，并汇报事故情况、 进展、风险以及影响控制事态的关键因素等问题，服从政府统一指挥。

**[E2]** [§ 6.0 其他事项]
  （ 一）本预案是集团公司针对可能发生的生产安全事故，组织实施应急救援工作并协助政府有关部门进行事故调查处理的指导性文件，在实施过程中可根据现场实际情况进行必要的调整。
  （ 二）各项目部必须在开工前，根据各自的实际，分析施工过程中可能发生的生产安全事故的性质、类别，制定针对性的生产安全事故应急预案，上报二级单位、集团公司备案。

- retrieved_nodes: L219, L279, L280⭐, L281, L283, L337, L338, L339


---

## latest_clean_niche_0811  ·  niche_fact

- **Query:** 根据《陕西建工第十一建集团有限公司生产安全事故综合应急预案（2025版）》中“5.3 现场应急物资装备保障”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c6097ad4242eda8c47c62c`
- **Gold nodes:** L307

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 500 |
| n_retrieved_nodes | 15 | 17 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.91 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L307` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C23` collect L306 (depth=0) · →L306 · +18
  - reason: Target section 5.3 contains the specific regulations on emergency material and equipment guarantees.
- `F1` finish - (depth=0)
  - reason: Section G1 contains the specific regulations for §5.3 on emergency material and equipment guarantees.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C23` | `L306` | - | 18 | 18 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 5.3 现场应急物资装备保障]
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

- retrieved_nodes: L306, L307⭐, L308, L309, L310, L311, L312, L313, L315, L316, L317, L318, L320, L321, L322, L323, L324


---

## latest_clean_niche_0821  ·  niche_fact

- **Query:** 根据《陕西建工第十一建集团有限公司生产安全事故综合应急预案（2025版）》中“5.5 其他保障”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c6097ad4242eda8c47c62c`
- **Gold nodes:** L327

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 496 | 497 |
| n_retrieved_nodes | 18 | 12 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.53 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L327` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C25` collect L325 (depth=0) · →L325 · +11
  - reason: Target section 5.5 'Other Guarantees' identified; collect to retrieve specific regulations.
- `F1` finish - (depth=0)
  - reason: Section 5.5 content fully collected and assembled in evidence.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C25` | `L325` | - | 11 | 11 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 5.5 其他保障]
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

- retrieved_nodes: L325, L326, L327⭐, L328, L329, L330, L331, L332, L333, L334, L335, L336


---

## latest_clean_scope_0053  ·  scope_collection

- **Query:** 列举《3.建设工程买卖合同（2025 版）》中“3.建设工程买卖合同（2025 版）.docx”部分的主要条目。
- **Doc:** `real_69c6098dd4242eda8c47c6a2`
- **Gold nodes:** L13, L14, L16, L17

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 493 |
| n_retrieved_nodes | 12 | 13 |
| trajectory_steps | - | 31 |
| elapsed_sec | - | 51.9 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L13` | ❌ | False | False |
| `L14` | ❌ | False | False |
| `L16` | ❌ | False | False |
| `L17` | ❌ | False | False |

### 决策 TRACE(因果序)

- `D1` dispatch L1 (depth=0) · regions=[L1] · child_reports=1
  - reason: Dispatch to collect main entries of the Construction Contract section.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C2` collect L2 (depth=1) · →L2 · +8
      - reason: Collect the main contract section to list its primary entries as requested.
    - `F1` finish - (depth=1)
      - reason: The document root only shows the title and summary. The specific main entries for the 2025 version are not visible in this scope, and no further collection actions are available at this level.
- `D1` dispatch L19 (depth=0) · regions=[L19, L76, L77, L91, L121, L138, L139, L142, L160, L175, L208, L225, L233] · child_reports=13
  - reason: Dispatch all remaining major sections to collect main entries of the contract.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L76 (depth=1) · →L76 · +6
      - reason: Collecting the full section on contract price adjustment and settlement to list main entries.
    - `F1` finish - (depth=1)
      - reason: The current scope L76 has been collected, and no further sections are visible or available for collection in this subtree.
    - `C1` collect L77 (depth=1) · →L77 · +5
      - reason: Collecting section 10.1 to retrieve the main entries regarding contract pricing methods.
    - `F1` finish - (depth=1)
      - reason: The document root L77 has been collected, containing the main entries of the contract.
    - `C1` collect L19 (depth=1) · →L19 · +9
      - reason: Collecting the full section on Article 3 Quality Requirements to list main entries.
    - `F1` finish - (depth=1)
      - reason: The current scope L19 has been collected, and no further sections are visible or available for collection in this subtree.
    - `C1` collect L91 (depth=1) · →L91 · +13
      - reason: Collecting section C1 covers all payment terms (10.4) including methods, ratios, and property offset details.
    - `F1` finish - (depth=1)
      - reason: The target document section has been collected. No further actions needed.
    - `C1` collect L121 (depth=1) · →L121 · +17
      - reason: Collecting the parent section C1 to retrieve all main entries under Article 11 regarding breach of contract and termination.
    - `F1` finish - (depth=1)
      - reason: The target document section has been collected. No further actions needed.
    - `C1` collect L160 (depth=1) · →L160 · +8
      - reason: Collecting the full 'Dispute Resolution' section to list its main entries as requested.
    - `F1` finish - (depth=1)
      - reason: The document root L160 has been collected, providing the main structure of the contract. No further sections are visible or needed.
    - `C1` collect L139 (depth=1) · →L139 · +3
      - reason: Collect section 12.1 to retrieve the main entries regarding authorized personnel and their powers.
    - `F1` finish - (depth=1)
      - reason: The target document section has been collected, providing sufficient evidence to list the main entries.
    - `C1` collect L138 (depth=1) · →L138 · +3
      - reason: Collecting Article 12 to list main entries of the contract authorization section.
    - `F1` finish - (depth=1)
      - reason: The current scope L138 has been collected, and no further sections are visible or available for collection in this subtree. The task is complete.
    - `C1` collect L175 (depth=1) · →L175 · +15
      - reason: Collecting the full 'Other Agreements' section to list all main items as requested.
    - `F1` finish - (depth=1)
      - reason: The target document section has been collected. No further actions needed to list its main entries.
    - `C1` collect L142 (depth=1) · multi→[L142, L143, L144, L145] · +7
      - reason: Collecting all visible sections under the current scope to list main entries of the contract.
    - `F1` finish - (depth=1)
      - reason: The document root L142 has been collected, containing the main entries of the contract. No further collection is needed.
    - `C1` collect L208 (depth=1) · →L208 · +9
      - reason: Collecting the full section '第二条 甲方及其人员的责任' to list its main items as requested.
    - `F1` finish - (depth=1)
      - reason: The document root has been collected, which includes the main structure of the contract. No further collection is needed.
    - `C1` collect L233 (depth=1) · →L233 · +3
      - reason: Collects the full 'Legal Representative Authorization Letter' section to identify its main entries.
    - `F1` finish - (depth=1)
      - reason: The document root has been collected, providing the main structure of the contract. No further collection is needed.
    - `C1` collect L225 (depth=1) · multi→[L225, L226, L227, L228] · +7
      - reason: Collecting all visible sections under the contract to list main entries as requested.
    - `F1` finish - (depth=1)
      - reason: Collected the main section L225 containing the contract title and structure. Ready to list entries.
- `F1` finish - (depth=0)
  - reason: Collected evidence covers all main contract entries including title, parties, quality, pricing, payment, authorization, liability, and dispute resolution.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C2` | `L2` | - | 8 | 8 | - |  |
| 4 | `C1` | `L76` | - | 6 | 6 | - |  |
| 6 | `C1` | `L77` | - | 5 | 5 | - |  |
| 8 | `C1` | `L19` | - | 9 | 9 | - |  |
| 10 | `C1` | `L91` | - | 13 | 13 | - |  |
| 12 | `C1` | `L121` | - | 17 | 17 | - |  |
| 14 | `C1` | `L160` | - | 8 | 8 | - |  |
| 16 | `C1` | `L139` | - | 3 | 3 | - |  |
| 18 | `C1` | `L138` | - | 3 | 3 | - |  |
| 20 | `C1` | `L175` | - | 15 | 15 | - |  |
| 22 | `C1` | `L142` | L142, L143, L144, L145 | 7 | 7 | - | ✅ |
| 24 | `C1` | `L208` | - | 9 | 9 | - |  |
| 26 | `C1` | `L233` | - | 3 | 3 | - |  |
| 28 | `C1` | `L225` | L225, L226, L227, L228 | 7 | 7 | - | ✅ |

### 子 agent reports_context

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

### 最终 evidence(new)

**[E1]** [§ 【         】买卖合同]
  甲方（买受人）：
  乙方（出卖人）：
  签约地点：
  签约时间：
  买受人（以下简称甲方）：
  出卖人（以下简称乙方）：
  根据《中华人民共和国民法典》等有关法律法规之规定，遵循平等、自愿、公平、诚实信用和绿色原则，经双方协商一致，签订本合同，双方共同遵照执行。

**[E2]** [§ 第三条  货物质量要求]
  3.1 质量要求及验收标准的约定：
  执行标准为： ，其他要求为： 。
  3.3 货物的质量要求应符合有关施工图纸及设计文件要求，有关图纸及设计文件作为合同附件。
  3.5 货物质量还应符合乙方承诺的质量标准。乙方报送甲方的书面资料，包括投标文件或单独的报价文件、乙方（或生产厂家）宣传资料及乙方（或生产厂家）公开宣传的内容，均构成其承诺。
  3.6 鉴于甲方对货物质量标准的了解程度不及乙方，本合同所列明的各种质量要求或技术质量标准，应执行最高标准。

**[E3]** [§ 10.1  本合同的价款，按下列第（     ）方式确定：]
（1）固定总价，不可调价，如仅供应部分货物，则按以下方式结算： ；

- retrieved_nodes: L3, L4, L5, L6, L7, L8, L9, L20, L21, L23, L25, L26, L78


---

## latest_clean_scope_0092  ·  scope_collection

- **Query:** 列举《十公司 彬州市城区智慧停车建设项目完工交付复盘报告-6.29》中“亮点H3通过优化工期，地基基础及主体阶段工期提前32天的原因分析”部分的主要条目。
- **Doc:** `real_69c60abfd4242eda8c47c8d9`
- **Gold nodes:** L38, L39, L40, L41, L42

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 243 | 215 |
| n_retrieved_nodes | 5 | 4 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 17.64 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L38` | ❌ | False | False |
| `L39` | ❌ | False | False |
| `L40` | ❌ | False | False |
| `L41` | ❌ | False | False |
| `L42` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C15` collect L32 (depth=0) · multi→[L32, L33, L34, L35, L36] · +9
  - reason: Collecting H3 section and its leaf nodes detailing the 32-day schedule advance reasons.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains the complete list of main items for Highlight H3 as requested.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C15` | `L32` | L32, L33, L34, L35, L36 | 9 | 9 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 亮点H3通过优化工期，地基基础及主体阶段工期提前32天的原因分析]
  ①场地不利因素优化:
  ①场地不利因素优化:
  现场场地狭小，为保证工期，无需加工材料直接卸货至工作面；
  现场场地狭小，为保证工期，无需加工材料直接卸货至工作面；
  除主要通道，周边其余场地利用率>85%;
  除主要通道，周边其余场地利用率>85%;
  利用周边项目加工厂进行材料代加工；
  利用周边项目加工厂进行材料代加工；

- retrieved_nodes: L33, L34, L35, L36


---

## latest_clean_scope_0096  ·  scope_collection

- **Query:** 列举《十公司 彬州市城区智慧停车建设项目完工交付复盘报告-6.29》中“如果出现【变化或意外】，则应该：”部分的主要条目。
- **Doc:** `real_69c60abfd4242eda8c47c8d9`
- **Gold nodes:** L100, L101, L102, L103

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 500 |
| n_retrieved_nodes | 9 | 9 |
| trajectory_steps | - | 7 |
| elapsed_sec | - | 10.75 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L100` | ❌ | False | False |
| `L101` | ❌ | False | False |
| `L102` | ❌ | False | False |
| `L103` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C29` collect L96 (depth=0) · →L96 · +1
  - reason: Target section '如果出现【变化或意外】，则应该：' found at N29, collect to retrieve main items.
- `D2` dispatch L15 (depth=0) · regions=[L15] · child_reports=1
  - reason: Dispatch to find the 'If changes or unexpected events occur' section under Reflection/Analysis.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `F1` finish - (depth=1)
      - reason: The current scope contains only 'Highlights' and 'Capital Recovery' analysis, not the requested 'Changes or Accidents' section.
- `C6` collect L15 (depth=0) · →L15 · +6
  - reason: Dispatch to D2 to explore '复盘反思、分析' section for the requested 'Changes or Accidents' items.
- `C1` collect L2 (depth=0) · →L2 · +7
  - reason: Need to collect the full 'Changes or Accidents' section (N17) to find the specific items requested.
- `C15` collect L55 (depth=0) · →L55 · +9
  - reason: The user query specifically asks for the 'Changes or Accidents' section, which corresponds to node N15 (C15). The previous dispatch to L15 was incorrect as it only contained highlights.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains the specific section '如果出现【变化或意外】，则应该：' with its main item regarding process confirmation adjustments.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C29` | `L96` | - | 1 | 1 | - | ✅ |
| 4 | `C6` | `L15` | - | 6 | 6 | - |  |
| 5 | `C1` | `L2` | - | 7 | 7 | - |  |
| 6 | `C15` | `L55` | - | 9 | 9 | - |  |

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60abfd4242eda8c47c8d9:L15 (ok)
The current scope contains only 'Highlights' and 'Capital Recovery' analysis, not the requested 'Changes or Accidents' section.
reason: The current scope contains only 'Highlights' and 'Capital Recovery' analysis, not the requested 'Changes or Accidents' section.
---
=== End Investigate ===
```

### 最终 evidence(new)

**[E1]** [§ 如果出现【变化或意外】，则应该：]
面对市场需求变化和原材料价格波动等意外情况，需及时调整过程确权工作，以确保数据的准确性和时效性。

**[E2]** [§ 项目完工交付复盘报告]
  单位/项目:彬州市城区智慧停车建设项目
  2024年6月27日，彬州市城区智慧停车建设项目完工交付复盘会在集团公司607会议室举行。会议由解博学引导，蔡伦组织，项目部主要管理人员参与，蔡伦、刘首安、李宝珺编写报告。
  一.复盘事项（或项目当下阶段）背景
  背景阐述：本项目为彬州市政府专项债，项目承包模式为EPC项目，入场时未达到“三通一平”条件。合同签订计划施工日期2022年9月20日，实际进场日期为2022年10月1日，计划完工日期为2023年9月20日，实际完工日期为2024年4月3日，合同总工期为365天。项目劳务分包、专业分包为项目部自行选择，汽车升降设备、客用电梯安装为甲指分包。但项目实际超出计划工期，现针对项目过程实施中的优缺点进行“回头看”。

**[E3]** [§ 三.复盘反思、分析]
  1、亮点H1资金确权及回收情况良好的原因分析
  ①过程确权率好
  ②资金回收情况良好

- retrieved_nodes: L96, L97, L3, L4, L5, L8, L16, L17, L19


---

## latest_clean_scope_0097  ·  scope_collection

- **Query:** 列举《安徽一 医防完工复盘报告6.13》中“7、不足L3（材料损耗过大）的原因分析”部分的主要条目。
- **Doc:** `real_69c60abfd4242eda8c47c8da`
- **Gold nodes:** L49, L50, L59, L61, L62

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 486 | 445 |
| n_retrieved_nodes | 5 | 9 |
| trajectory_steps | - | 4 |
| elapsed_sec | - | 15.2 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L49` | ❌ | False | False |
| `L50` | ❌ | False | False |
| `L59` | ❌ | False | False |
| `L61` | ❌ | False | False |
| `L62` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C20` collect L20 (depth=0) · →L20 · +5
  - reason: Collect section 7 to retrieve the main items regarding material loss causes.
- `C14` collect L14 (depth=0) · →L14 · +4
  - reason: Collect section 7 (L3 material loss) to retrieve the required cause analysis items.
- `C14` collect L18 (depth=0) · →L18 · +1
  - reason: Dispatch D6 to retrieve the full content of section 7 regarding material loss causes.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains the specific section §7 regarding material loss causes as requested.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C20` | `L20` | - | 5 | 5 | - |  |
| 2 | `C14` | `L14` | - | 4 | 4 | - |  |
| 3 | `C14` | `L18` | - | 1 | 1 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 7、不足L3（材料损耗过大）的原因分析]
  分析指出因现场管理不到位导致木工、钢管及抹灰砂浆等材料严重浪费和损耗，分别造成18万、14万及14万的超目标成本损失。
  四.复盘萃取、提炼
  文章总结了项目管理的四大核心经验：加强工程量清单核对、通过商务与技术策划创效、强化安全与质量管理，并详细阐述了工期管控、分包班组及材料管理的具体措施与教训。
  五.复盘转化、应用

**[E2]** [§ 5、不足L1（工期滞后）的原因分析]
  客观原因
  主观原因
  本文分析了导致工期滞后的三大核心问题：一是业主方分包单位进场慢、配合差及我方计划缺乏弹性；二是劳务班组和材料资源选择不当，导致施工延误；三是业主资金链断裂影响工程款支付，进而阻碍项目生产。

**[E3]** [§ 6、不足L2（木工班组管理不善）的原因分析]
项目亏损主因：一是招标前未做市场调研，定标过度参考最低价且忽视班组实力；二是过程管理重进度轻成本，清退及零星用工费用高，导致最终造价超原合同174.3万元。

- retrieved_nodes: L21, L22, L23, L24, L15, L16, L17, L18, L19


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
| trajectory_steps | - | 3 |
| elapsed_sec | - | 15.09 |

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
  - reason: Collect section N4 'Levels And Setting Out Of The Works' to retrieve its main items.
- `C10` collect L751 (depth=0) · →L751 · +1
  - reason: Target section 'Levels And Setting Out Of The Works' is a leaf node C10, directly relevant to the query.
- `F1` finish - (depth=0)
  - reason: Assembled evidence G1 and G2 cover the 'Levels And Setting Out Of The Works' section with relevant items.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C4` | `L110` | - | 1 | 1 | - | ✅ |
| 2 | `C10` | `L751` | - | 1 | 1 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ Levels And Setting Out Of The Works水平和设置]
Setting out设置

**[E2]** [§ 3.0	Contract  Documents,Programme  And]
Levels And Setting Out Of The Works--工程的测量与放样

- retrieved_nodes: L110, L111, L751


---

## latest_clean_scope_0102  ·  scope_collection

- **Query:** 列举《马来西亚合同样本 2006 版 翻译件- Malaysia-PAM-合同翻译稿（4.23二译）》中“Site Agent现场代理”部分的主要条目。
- **Doc:** `real_69c60aeed4242eda8c47c925`
- **Gold nodes:** L125, L126, L127

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 499 |
| n_retrieved_nodes | 19 | 3 |
| trajectory_steps | - | 3 |
| elapsed_sec | - | 14.53 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L125` | ❌ | False | False |
| `L126` | ❌ | False | False |
| `L127` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C1` collect L123 (depth=0) · →L123 · +5
  - reason: Collect the 'Site Agent' section to retrieve its main items as requested.
- `C13` collect L828 (depth=0) · →L828 · +15
  - reason: Collect the full 'Site Agent' section (N13) to retrieve all main items as requested.
- `F1` finish - (depth=0)
  - reason: Assembled evidence G2 and G1 fully cover the 'Site Agent' section requirements.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L123` | - | 5 | 5 | - |  |
| 2 | `C13` | `L828` | - | 15 | 15 | - |  |

### 最终 evidence(new)

**[E1]** [§ 8.0	Site Agent--现场代理人]
  Site Agent
  给现场代理的指示。
  capable of receiving directions or instructions in English or Bahasa Malaysia.The Site Agent shall be deemed to be authorised by the Contractor to receive any directions given by the Site Staff or instructions given by the Architect and any such directions and instructions given shall be deemed to have been given to the Contractor. 承包商应确保现场代理以及相应的助理和监管人员能够理解并接收英文或马来西语的指示或指导。 现场代理应被视为已经得到承包商的授权，去接收来自现场工作人员或建筑师的任何指示，而这些指示和指导应被认为是直接提供给承包商的。

- retrieved_nodes: L834, L835, L836


---

## latest_clean_scope_0110  ·  scope_collection

- **Query:** 列举《马来西亚合同样本 2006 版 翻译件- Malaysia-PAM》中“Site Agent现场代理”部分的主要条目。
- **Doc:** `real_69c60aeed4242eda8c47c926`
- **Gold nodes:** L125, L126, L127

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 204 |
| n_retrieved_nodes | 19 | 4 |
| trajectory_steps | - | 5 |
| elapsed_sec | - | 189.25 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L125` | ✅ | True | False |
| `L126` | ✅ | True | False |
| `L127` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C2` collect L124 (depth=0) · →L124 · +1
  - reason: Collect leaf node N2 directly containing the main items for Site Agent.
- `D1` dispatch L123 (depth=0) · regions=[L123] · child_reports=1
  - reason: Dispatch to collect all chunks under 'Site Agent现场代理' section.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L123 (depth=1) · →L123 · +5 · PURGED後代×1
      - reason: Collect the main 'Site Agent' section to retrieve its primary items as requested.
    - `F1` finish - (depth=1)
      - reason: The 'Site Agent' section has been collected. No further actions needed.
- `F1` finish - (depth=0)
  - reason: Assembled evidence G1 fully covers the 'Site Agent' section main items.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C2` | `L124` | - | 1 | 1 | - | ✅ |
| 2 | `C1` | `L123` | - | 5 | 5 | 1 |  |

**水合告警:**
- step 2 `C1` 收父节点 `L123` 时 **purge 掉 1 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60aeed4242eda8c47c926:L123 (ok)
collected 4 branch node(s); explicit roots=['real_69c60aeed4242eda8c47c926:L123']
collected: real_69c60aeed4242eda8c47c926:L123, real_69c60aeed4242eda8c47c926:L125, real_69c60aeed4242eda8c47c926:L126, real_69c60aeed4242eda8c47c926:L127
reason: The 'Site Agent' section has been collected. No further actions needed.
---
=== End Investigate ===
```

### 最终 evidence(new)

**[E1]** [§ Site Agent现场代理]
  Site Agent现场代理
  Site Agent现场代理
  Instructions to Site Agent对现场代理的说明
  Exclusion of Person employed on the Works排除在工程上被雇用的人
  Access To The Works进入工程的途径Access to the Works进入工程的途径

- retrieved_nodes: L124, L125⭐, L126⭐, L127⭐


---

## latest_clean_scope_0124  ·  scope_collection

- **Query:** 列举《华侨城坪山综合体项目基坑支护工程专项施工方案》中“华侨城坪山综合体项目基坑支护工程专项施工方案.docx”部分的主要条目。
- **Doc:** `real_69c60b0ad4242eda8c47c944`
- **Gold nodes:** L5, L6, L7, L10, L12, L15

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 494 |
| n_retrieved_nodes | 20 | 18 |
| trajectory_steps | - | 4 |
| elapsed_sec | - | 93.21 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L5` | ❌ | False | False |
| `L6` | ❌ | False | False |
| `L7` | ❌ | False | False |
| `L10` | ❌ | False | False |
| `L12` | ❌ | False | False |
| `L15` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C1` collect L1 (depth=0) · multi→[L1, L88, L113, L124, L187] · +24
  - reason: Collect main sections of the plan: Overview, Layout, Risks, Basis, and Schedule.
- `C1` collect L233 (depth=0) · →L233 · +6
- `C32` collect L852 (depth=0) · →L852 · +3
  - reason: Collect 'Calculation and Drawings' section to list main items as requested.
- `F1` finish - (depth=0)
  - reason: Assembled evidence covers all main sections of the special construction plan including overview, basis, plan, technology, and calculations.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L1` | L1, L88, L113, L124, L187 | 24 | 26 | - |  |
| 2 | `C1` | `L233` | - | 6 | 6 | - |  |
| 3 | `C32` | `L852` | - | 3 | 3 | - |  |

### 最终 evidence(new)

**[E1]** [§ 施工工艺技术]
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

**[E2]** [§ 施工计划]
材料与设备计划
主要材料需求计划
表3.2-1 主要材料需求计划表

- retrieved_nodes: L234, L235, L236, L261, L262, L263, L273, L274, L275, L469, L470, L471, L474, L475, L476, L197, L198, L199


---

## latest_clean_scope_0129  ·  scope_collection

- **Query:** 列举《华侨城坪山综合体项目基坑支护工程专项施工方案》中“施工管理及作业人员配备和分工”部分的主要条目。
- **Doc:** `real_69c60b0ad4242eda8c47c944`
- **Gold nodes:** L810, L815, L817, L821, L823, L825

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 286 | 181 |
| n_retrieved_nodes | 11 | 9 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 5.83 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L810` | ❌ | False | False |
| `L815` | ❌ | False | False |
| `L817` | ❌ | False | False |
| `L821` | ❌ | False | False |
| `L823` | ❌ | False | False |
| `L825` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C27` collect L780 (depth=0) · multi→[L780, L781, L787, L789] · +8
  - reason: Collect the main section and its subsections on personnel allocation and division of labor.
- `F1` finish - (depth=0)
  - reason: Assembled evidence covers all required personnel categories: management, safety, and special operations.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C27` | `L780` | L780, L781, L787, L789 | 8 | 9 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 施工管理人员]
  施工项目管理组织机构
  图6.1.1 施工项目管理组织机构
  项目经理部的部门设置和人员配备
  图6.1.2-1 施工项目部人员组成分布图
  表6.1.2-1项目经理部的部门设置和人员配备

**[E2]** [§ 专职安全人员]
表6.2-1 专职安全人员及职责表

**[E3]** [§ 特种作业人员]
表6.3 特种作业人员表

- retrieved_nodes: L782, L783, L784, L785, L786, L787, L788, L789, L790


---

## latest_clean_scope_0132  ·  scope_collection

- **Query:** 列举《陕建丝路创发中心高支模专项施工方案》中“五、施工保证措施”部分的主要条目。
- **Doc:** `real_69c60b33d4242eda8c47c959`
- **Gold nodes:** L278, L282, L283, L284, L285, L286

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 211 |
| n_retrieved_nodes | 20 | 9 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 170.71 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L278` | ❌ | False | False |
| `L282` | ❌ | False | False |
| `L283` | ❌ | False | False |
| `L284` | ❌ | False | False |
| `L285` | ❌ | False | False |
| `L286` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C1` collect L272 (depth=0) · →L272 · +4
  - reason: Collect section 5 to list main items of construction guarantee measures.
- `F1` finish - (depth=0)
  - reason: The assembled evidence [G1] contains the full list of main items under 'V. Construction Guarantee Measures' as requested.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L272` | - | 4 | 4 | - |  |

### 最终 evidence(new)

**[E1]** [§ 五、施工保证措施]
  5.1组织保障措施
  5.1.1安全组织架构
  小组成员组成
  5.2技术措施
  5.2.1安全管理措施
  （1）支撑脚手架搭设作业人员应正确佩戴使用安全帽、安全带和防滑鞋。
  5.3监测监控措施
  5.3.1监测点的设置
  监测点在每次所浇模架周边布点，根据《建筑施工临时支撑结构技术规范》JGJ300-2013中的要求，进行位移监测时，须按照如下要求设置监测点：

- retrieved_nodes: L273, L274, L275, L311, L312, L313, L384, L385, L386


---

## latest_clean_scope_0135  ·  scope_collection

- **Query:** 列举《陕建丝路创发中心高支模专项施工方案》中“八、应急处置措施”部分的主要条目。
- **Doc:** `real_69c60b33d4242eda8c47c959`
- **Gold nodes:** L456, L457, L460, L461, L463, L464

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 181 |
| n_retrieved_nodes | 13 | 6 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 6.26 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L456` | ❌ | False | False |
| `L457` | ❌ | False | False |
| `L460` | ❌ | False | False |
| `L461` | ❌ | False | False |
| `L463` | ❌ | False | False |
| `L464` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C1` collect L452 (depth=0) · →L452 · +3
  - reason: Collect the entire 'Emergency Response Measures' section to list all main items as requested.
- `F1` finish - (depth=0)
  - reason: The assembled evidence [G1] contains the full 'Emergency Response Measures' section with all required items.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L452` | - | 3 | 3 | - |  |

### 最终 evidence(new)

**[E1]** [§ 八、应急处置措施]
  8.1应急领导小组及响应程序
  8.1.1应急领导小组
  （1）组长职责
  8.2应急事件及其应急措施
  8.2.1预防坍塌事故的技术措施
  （1）模板作业前，按设计单位要求，根据施工工艺、作业条件及周边环境，按照安全管理方案、应急预案内容做好施工前期准备，项目经理组织有关部门验收，经验收合格签字后，方可作业。

- retrieved_nodes: L453, L454, L455, L472, L473, L474


---

## latest_clean_scope_0139  ·  scope_collection

- **Query:** 列举《27-设计院-秦都卫生疾控中心项目关于优化策略的复盘报告》中“参与团队：主要设计团队为十一建设计院。 二、回顾目标 项目预期目标：”部分的主要条目。
- **Doc:** `real_69c60b97d4242eda8c47c997`
- **Gold nodes:** L12, L13, L14, L15, L16, L17

### 结果得分 — **PASS** (new gold_recall=0.17)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.17 |
| evidence_chars | 500 | 491 |
| n_retrieved_nodes | 6 | 6 |
| trajectory_steps | - | 6 |
| elapsed_sec | - | 13.47 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L12` | ✅ | True | False |
| `L13` | ❌ | False | False |
| `L14` | ❌ | False | False |
| `L15` | ❌ | False | False |
| `L16` | ❌ | False | False |
| `L17` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C6` collect L7 (depth=0) · →L7 · +1
  - reason: Collect section N6 containing the target team and project goals as requested.
- `C1` collect L1 (depth=0) · →L1 · +6
  - reason: The user query targets the 'Review Objectives' section which is under N1. Dispatching D1 will reveal the full content including the main items.
- `C1` collect L9 (depth=0) · →L9 · +1
  - reason: Collect section C1 to retrieve the 'Review Goals' and 'Project Expected Goals' content.
- `C1` collect L11 (depth=0) · →L11 · +8
  - reason: Collecting Architecture section to find the main items under 'Review Objectives' as requested.
- `C1` collect L19 (depth=0) · →L19 · +6
  - reason: Collect structural optimization details to complete the 'Review Objectives' section content.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains the requested section '参与团队' and '回顾目标' with main items. No other sections needed.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C6` | `L7` | - | 1 | 1 | - | ✅ |
| 2 | `C1` | `L1` | - | 6 | 6 | - |  |
| 3 | `C1` | `L9` | - | 1 | 1 | - | ✅ |
| 4 | `C1` | `L11` | - | 8 | 8 | - |  |
| 5 | `C1` | `L19` | - | 6 | 6 | - |  |

### 最终 evidence(new)

**[E1]** [§ 参与团队：主要设计团队为十一建设计院。
二、回顾目标
项目预期目标：]
二、回顾目标
项目预期目标：]
控制项目造价，从建筑、结构、设备等多方位角度降低工程造价，避免超概风险。建筑、结构、设备分别从不同方向和思路优化现有设计方案及图纸，建筑预期目标为6条优化策略、结构为4条策略、设备为4条策略。

**[E2]** [§ 设计理念：]
  平疫结合：本项目可为医院建筑规划与设计提供一种平疫结合的新思路，提高传染病防控的有效性和效率，使疫情时期可以发挥自身的使命，在疫情结束后可满足社区医院使用要求，避免国家资源的浪费。
  安全与卫生：医疗建筑的安全性和卫生性至关重要。建筑布局和流线设计应能够有效防止交叉感染，保障医护人员和病人的安全。同时，建筑结构和设施应符合相关的安全标准和卫生要求。
  现代感与功能性：医疗建筑应具有现代感和功能性，既要体现医院的形象和特色，又要满足医疗活动的实际需求。建筑设计应简洁大方、新颖独特，同时考虑到医院的功能需求和发展趋势，为未来的扩建和改造提供可能。

**[E3]** [§ 建筑专业：]
a.建筑通过提前与专家沟通，规避规划指标风险。

- retrieved_nodes: L7, L8, L2, L5, L6, L12⭐


---

## real_69c6ef4e4cca74801cb63bc6_scope_collection_auto_0061  ·  scope_collection

- **Query:** 列出文档中提到的所有竖向钢立柱安装的具体步骤及技术要求。
- **Doc:** `real_69c6ef4e4cca74801cb63bc6`
- **Gold nodes:** L79, L80, L82

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 494 |
| n_retrieved_nodes | 8 | 13 |
| trajectory_steps | - | 3 |
| elapsed_sec | - | 23.02 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L79` | ❌ | False | False |
| `L80` | ❌ | False | False |
| `L82` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C15` collect L62 (depth=0) · multi→[L62, L63, L64, L66] · +4
  - reason: Collecting specific steps and technical requirements for vertical steel column installation found in sections C15-C18.
- `C10` collect L32 (depth=0) · →L32 · +64 · PURGED後代×4
  - reason: Collect section 5.2 Operation Points to find all vertical steel column installation steps and requirements.
- `F1` finish - (depth=0)
  - reason: Evidence G1 contains the specific steps and technical requirements for vertical steel column installation.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C15` | `L62` | L62, L63, L64, L66 | 4 | 4 | - | ✅ |
| 2 | `C10` | `L32` | - | 64 | 64 | 4 |  |

**水合告警:**
- step 2 `C10` 收父节点 `L32` 时 **purge 掉 4 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。

### 最终 evidence(new)

**[E1]** [§ 图 **5-2-3-3** 现场预埋件拉拔试验]
  - 2、转接件的安装
  - （1）、根据控制线确定转接件位置，施工时将其焊在预埋件上
  - ，然后对其三维方向尺寸进行复核（垂直误差2mm、水平误差2mm、 进深误差3mm）在复核无误后，进行焊接固定。
  图 **5-2-3-4** 现场预埋件防腐处理
  - 5.2.4 竖向龙骨安装与调整
  （1）、竖向钢立柱安装时，应先将立柱与转接件连接，立柱应带 有活动接头，接头通过芯套连接上下柱，芯套与立柱紧密相接。上 下柱用螺栓固定，上下柱之间留有20mm 的空隙。
  图 **5-2-4-1** 立柱与芯柱连接 （2）、通过镀锌螺栓将竖向龙骨与转接件链接，根据提前策划的 基准线，对竖向龙骨进行调整固定，确保在镂空部位龙骨不外漏， 并使其处于最佳受力状态。
  图 **5-2-4-2** 现场立柱与转接件连接
  - （3）、用多功能水平尺或经纬仪校正钢龙骨的垂直度，必要时将 螺栓松开调整，如仍调整不好必须重新安装。

**[E2]** [§ 5.2.7 铝板安装]
图 **5-2-7-1** 铝板固定龙骨位置

- retrieved_nodes: L32, L57, L58, L59, L60, L61, L62, L63, L64, L65, L66, L95, L98


---

## real_69c6ef4e4cca74801cb63bc6_scope_collection_auto_0062  ·  scope_collection

- **Query:** 列举横向龙骨（钢托板）安装与调整过程中的所有关键操作要点。
- **Doc:** `real_69c6ef4e4cca74801cb63bc6`
- **Gold nodes:** L86, L90, L92

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 443 |
| n_retrieved_nodes | 8 | 9 |
| trajectory_steps | - | 3 |
| elapsed_sec | - | 4.29 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L86` | ❌ | False | False |
| `L90` | ❌ | False | False |
| `L92` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C14` collect L68 (depth=0) · →L68 · +2
  - reason: Section 5.2.5 specifically covers horizontal keel (steel support plate) installation and adjustment.
- `C15` collect L71 (depth=0) · →L71 · +5
  - reason: Collect section 5.2.5 containing all key points for horizontal keel (steel support plate) installation and adjustment.
- `F1` finish - (depth=0)
  - reason: Assembled evidence G1 and G2 fully cover the key operation points for horizontal keel installation and adjustment.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C14` | `L68` | - | 2 | 2 | - | ✅ |
| 2 | `C15` | `L71` | - | 5 | 5 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 5.2.5 横向龙骨（钢托板）安装与调整]
  （1）、横向龙骨（钢托板）安装时，应先在立柱上准确标出横梁 的精确位置，钻出孔位，在角钢上打出连接点的孔位，用角码及螺 栓将角钢横梁与立柱连接在一起，并紧固螺栓。
  图 **5-2-5-1** 横向龙骨（钢托板）安装 **CAD** 优化图

**[E2]** [§ 图 **5-2-5-2** 横向龙骨（钢托板）现场安装图]
  - （2）、用水准仪校正横梁的标高，保证立柱与横梁垂直，误差在 允许范围内，校正无误后，横梁与立柱采用焊接，焊接时要一头焊 接一头螺栓连接,形成应力消减支座。
  - 图 **5-2-5-3** 横向龙骨（钢托板）连接头策划及实施
  - （3）、 横向龙骨（钢托板）应该随陶土砖的砌筑进度同步安装， 不可超前施工 。
  - （4）、层间防火隔离带安装
  按照设计图纸要求，防火岩棉厚度为200mm，防火岩棉容重为 120Kg/m3，防火时间2h；防火岩棉均须单面锡箔，拼接处丁基胶带 密封。

- retrieved_nodes: L68, L69, L70, L71, L72, L73, L74, L75, L76


---

## real_69c6ef4e4cca74801cb63bc6_scope_collection_auto_0063  ·  scope_collection

- **Query:** 列出摞底排砖、挂线砌筑阶段涉及的所有具体施工工艺要求。
- **Doc:** `real_69c6ef4e4cca74801cb63bc6`
- **Gold nodes:** L96, L100, L102, L105, L107

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 489 |
| n_retrieved_nodes | 6 | 7 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.53 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L96` | ❌ | False | False |
| `L100` | ❌ | False | False |
| `L102` | ❌ | False | False |
| `L105` | ❌ | False | False |
| `L107` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C18` collect L77 (depth=0) · →L77 · +15
  - reason: Section 5.2.6 covers stacking, lining, and masonry requirements as requested.
- `F1` finish - (depth=0)
  - reason: Assembled evidence G1 fully covers the specific construction requirements for stacking bricks and string masonry.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C18` | `L77` | - | 15 | 15 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 5.2.6 摞底排砖、挂线砌筑]
  与水平灰缝均衡性。
  - 2、根据排砖位置焊接竖向拉结筋，确保自陶土砖孔穿出。
  3、挂线、立批数杆，开始砌筑。砌筑过程控制线，水平线长度不 宜超过12 米，以防线绳自重下垂影响水平，且墙面长度超过12m 时， 应设置10mm 宽的马牙槎形垂直变形缝，变形缝内采用防水密封胶处 理；考虑一砖一缝，理论尺寸为75mm/250mm，砌筑过程中应先盘头 4/8 层，根据准确盘头放线砌筑，任意4 批砖高度应为300mm。
  图 **5-2-6-3** 现场挂线砌筑以及砌筑模数
  5、镂空砖幕墙部位应考虑主龙骨与镂空部位排砖要求，以保证主 龙骨轮廓不暴露在镂空部位（对于镂空砖位置，内侧墙面需要做JS2 型防水涂料1.5mm 左右）；
  备注：（1）陶土砖本体、（2）左侧壁固定连接左限位块，所述（3） 砖体（1）下表面固定连接下限位块，所述（4）砖体（1）右侧壁固定 连接有右限位块，所述（7）砖体（1）上表面固定连接有上限位块，所 述（5）砖体（1）表面开设有第一镂空花纹、第二镂空花纹（6）和第 三镂空花纹（8）。

- retrieved_nodes: L77, L79, L81, L83, L84, L87, L91


---

## real_69c6ef4e4cca74801cb63bc6_scope_collection_auto_0064  ·  scope_collection

- **Query:** 列举文档中提到的所有施工验收标准名称及其对应的国家标准编号。
- **Doc:** `real_69c6ef4e4cca74801cb63bc6`
- **Gold nodes:** L158, L159, L160, L161, L162, L163

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 202 |
| n_retrieved_nodes | 13 | 6 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 3.08 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L158` | ❌ | False | False |
| `L159` | ❌ | False | False |
| `L160` | ❌ | False | False |
| `L161` | ❌ | False | False |
| `L162` | ❌ | False | False |
| `L163` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C20` collect L120 (depth=0) · multi→[L120, L121, L122, L123, L130, L131] · +6
  - reason: Collect all construction acceptance standards and their national standard numbers from section 7.1.
- `F1` finish - (depth=0)
  - reason: Assembled evidence G1 contains all construction acceptance standards and their national standard numbers.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C20` | `L120` | L120, L121, L122, L123, L130, L131 | 6 | 6 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 7.质量控制]
  7.1 施工验收标准
  - 1、《砌体结构工程施工质量验收规范》GB50203
  - 2、《建筑装饰装修工程质量验收标准》GB50210
  - 3、《建筑节能工程施工质量验收标准》GB50411
  - 10、《外墙外保温工程技术标准》JGJ144
  - 11、《建筑幕墙工程技术标准》DBJ61/T 161 12、《陶板幕墙工程技术规程》Q/TOBSG-03

- retrieved_nodes: L120, L121, L122, L123, L130, L131


---

## real_69cb12d0919452cda2225a0b_scope_collection_auto_0073  ·  scope_collection

- **Query:** 列举收取进项税发票时，关于“票面信息完整性”的具体核查要求。
- **Doc:** `real_69cb12d0919452cda2225a0b`
- **Gold nodes:** L66

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 488 | 493 |
| n_retrieved_nodes | 5 | 6 |
| trajectory_steps | - | 8 |
| elapsed_sec | - | 13.09 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L66` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C4` collect L57 (depth=0) · →L57 · +1
  - reason: Section C4 explicitly details the requirements for 'invoice information completeness' when collecting input VAT invoices.
- `C3` collect L56 (depth=0) · →L56 · +1
  - reason: Section C3 defines input VAT invoices and collection scope, relevant to invoice information completeness requirements.
- `C2` collect L55 (depth=0) · →L55 · +1
  - reason: Section 3.1.2 specifically covers input VAT invoice collection requirements, including completeness checks.
- `C1` collect L54 (depth=0) · →L54 · +3 · PURGED後代×3
  - reason: Section 3.1.1 explicitly mentions verifying 'invoice information completeness' for input VAT invoices.
- `C1` collect L58 (depth=0) · →L58 · +1
  - reason: Collect section 3.1.3 to find specific requirements for invoice information completeness verification.
- `C1` collect L60 (depth=0) · →L60 · +2
  - reason: Collect section 3.1.4 to find specific requirements for invoice information completeness verification.
- `C7` collect L94 (depth=0) · →L94 · +1
  - reason: Section C7 explicitly details the specific invoice information completeness requirements for input VAT invoices, including buyer name and tax ID matching.
- `C1` collect L63 (depth=0) · →L63 · +3
  - reason: Collect section 3.1.5 to find specific requirements for invoice information completeness verification.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C4` | `L57` | - | 1 | 1 | - | ✅ |
| 2 | `C3` | `L56` | - | 1 | 1 | - | ✅ |
| 3 | `C2` | `L55` | - | 1 | 1 | - | ✅ |
| 4 | `C1` | `L54` | - | 3 | 3 | 3 | ✅ |
| 5 | `C1` | `L58` | - | 1 | 1 | - | ✅ |
| 6 | `C1` | `L60` | - | 2 | 2 | - | ✅ |
| 7 | `C7` | `L94` | - | 1 | 1 | - | ✅ |
| 8 | `C1` | `L63` | - | 3 | 3 | - | ✅ |

**水合告警:**
- step 4 `C1` 收父节点 `L54` 时 **purge 掉 3 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。

### 最终 evidence(new)

**[E1]** [§ **3.1.1** 进项税额定义]
  进项税发票，是指集团购进货物、加工修理修配劳务、服务、无形资产或者不动产， 收取的由销售方开具的增值税专用发票、部分增值税普通发票（旅客运输票据、农产品、 苗木等）。进项税发票主要由集团财务管理服务中心以及项目部收集，由集团财务管理 服务中心统一认证，并在当期向集团主管税务机关申报。
  收取进项发票，应核实业务的真实性、票面信息完整性。业务真实性指此笔业务是 否真实发生，确保“货物、劳务及服务流”、“资金流”、“发票流”、“合同流”保 持四流一致。票面信息完整性指发票购买方信息应与集团开票信息一致；发票内容完整、 发票备注栏注明项目名称以及建筑服务发生地所在省、市、区（县）；发票内容清晰可 辨；发票正反两面干净整洁，不允许出现脏、乱及签字的痕迹；发票抵扣联不可折叠， 不能污损，密码区不能出格压线；发票专用章内容应与票面销售方信息一致，不得压盖 发票金额。

**[E2]** [§ **3.1.5** 进项税费抵扣与统计]
  集团财务管理服务中心将当月发票认证完成后，需将各项目当月进项税额如实填列
  财务管理（税务管理）

- retrieved_nodes: L54, L56, L57, L63, L64, L65


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
| elapsed_sec | - | 1.13 |

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
| elapsed_sec | - | 0.09 |

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
| elapsed_sec | - | 0.09 |

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

## latest_clean_niche_0023  ·  niche_fact

- **Query:** 根据《线上学习平台学习管理方案（修订）》中“（ 一）课程开发管理”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c6095ed4242eda8c47c5b2`
- **Gold nodes:** L34

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 207 | 405 |
| n_retrieved_nodes | 3 | 5 |
| trajectory_steps | - | 3 |
| elapsed_sec | - | 3.19 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L34` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C25` collect L34 (depth=0) · →L34 · +1
  - reason: Collects the specific regulations under 'Course Development Management' as requested.
- `C25` collect L33 (depth=0) · →L33 · +4 · PURGED後代×1
  - reason: Collect section (一)课程开发管理 to retrieve specific regulations as requested.
- `F1` finish - (depth=0)
  - reason: Assembled evidence G1 contains all specified regulations under 'Course Development Management'.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C25` | `L34` | - | 1 | 1 | - | ✅ |
| 2 | `C25` | `L33` | - | 4 | 4 | 1 | ✅ |

**水合告警:**
- step 2 `C25` 收父节点 `L33` 时 **purge 掉 1 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。

### 最终 evidence(new)

**[E1]** [§ （ 一）课程开发管理]
  1.课程开发。课程开发依托专家组、各业务线要从有利于组织目标达成、员工履职能力提升等方面，本着“简单、实用、明了”原则进行课程开发。各专家组、各部门应按年度既定课程开发计划，督促、跟进课程开发负责人按时完成课件开发任务。计划外课程开发须明确开发课程名称、学习对象等，经各专家组审核后开发，并向平台中心办公室备案。
  2.课件评审。课件开发完成后，根据课程类别提交各专家组审核，专家组从课件选材、专业度、实用性等方面对课件进行评审，课程评审管理参照《十一在线——员工赋能一体化平台管理办法》执行。
  3.课件上传。评审通过后，平台管理员需在课程计划提交截止时间5 日内完成课件上传和必修岗位指派。计划外开发的课程经各专家组评审通过后5 日完成上传和必修岗位指派。
  4.课酬兑现。开发的课程根据《十一在线——员工赋能一体化平台管理办法》相关规定标准兑现相应课酬。

- retrieved_nodes: L33, L34⭐, L35, L36, L37


---

## latest_clean_niche_0043  ·  niche_fact

- **Query:** 根据《集团公司对外捐赠管理办法（修订版）》中“第四条 对外捐赠的类型”相关内容，该处明确写出的规定或事实是什么？
- **Doc:** `real_69c60970d4242eda8c47c5fd`
- **Gold nodes:** L11

### 结果得分 — **PASS** (new gold_recall=1.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 1.00 |
| evidence_chars | 500 | 243 |
| n_retrieved_nodes | 10 | 5 |
| trajectory_steps | - | 2 |
| elapsed_sec | - | 2.36 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L11` | ✅ | True | False |

### 决策 TRACE(因果序)

- `C9` collect L10 (depth=0) · multi→[L10, L11, L12, L13] · +4
  - reason: Collect Article 4 and its three subtypes of external donations as requested.
- `F1` finish - (depth=0)
  - reason: The assembled evidence G1 contains the full content of Article 4 regarding donation types, sufficient to answer the query.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C9` | `L10` | L10, L11, L12, L13 | 4 | 7 | - | ✅ |

**水合告警:**
- step 1 整枝水合含 3 个非 gold 叶 (与 gold 争抢 evidence 预算)。

### 最终 evidence(new)

**[E1]** [§ 第四条  对外捐赠的类型]
  （一）救济性捐赠，即向受灾地区、扶贫地区或者困难的社会弱势群体的救济性捐赠。
  （二）公益性捐赠，即向科技文卫事业和环境保护等社会公益事业的公益性捐赠。
  （三）其他捐赠，即除上述捐赠外，为促进社会发展以及集团公司履行社会责任需要的其他捐赠，含外部各类活动赞助。
  各单位要正确参与社会公益事业，依法依规确定对外捐赠范围和支出规模，规范开展对外捐赠活动，避免无序、随意捐赠等行为。对于有关社会机构、团体的摊派性捐赠，要坚决依法拒绝，

- retrieved_nodes: L10, L11⭐, L12, L13, L14


---

## latest_clean_scope_0116  ·  scope_collection

- **Query:** 列举《1.临时用电施工组织设计范本》中“1.临时用电施工组织设计范本.docx”部分的主要条目。
- **Doc:** `real_69c60aeed4242eda8c47c928`
- **Gold nodes:** L42, L43, L47, L48, L49, L50

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 499 |
| n_retrieved_nodes | 26 | 26 |
| trajectory_steps | - | 5 |
| elapsed_sec | - | 8.88 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L42` | ❌ | False | False |
| `L43` | ❌ | False | False |
| `L47` | ❌ | False | False |
| `L48` | ❌ | False | False |
| `L49` | ❌ | False | False |
| `L50` | ❌ | False | False |

### 决策 TRACE(因果序)

- `C1` collect L1 (depth=0) · →L1 · +7
  - reason: Collect the main section '工程概况' to retrieve its primary entries as requested.
- `C1` collect L21 (depth=0) · →L21 · +3
- `C1` collect L26 (depth=0) · multi→[L26, L39, L75, L90, L109, L112, L114] · +32
  - reason: Collect main section headers of the template to list all primary entries.
- `C1` collect L20 (depth=0) · →L20 · +1
  - reason: Collect '编制依据' section to list its main entries as requested.
- `F1` finish - (depth=0)
  - reason: All main sections of the temporary power organization design template are now collected and ranked.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L1` | - | 7 | 7 | - |  |
| 2 | `C1` | `L21` | - | 3 | 3 | - |  |
| 3 | `C1` | `L26` | L26, L39, L75, L90, L109, L112, L114 | 32 | 32 | - |  |
| 4 | `C1` | `L20` | - | 1 | 1 | - | ✅ |

### 最终 evidence(new)

**[E1]** [§ 工程概况]
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

**[E2]** [§ 用电容量统计]
  设备功率统计
  表3-1施工现场临时用电设备功率统计表
  施工用电分配表
  表3-2临时用电分配表

**[E3]** [§ 负荷计算]
  总用电量计算
  Ｐｊｓ＝ＫＸ*ＰＳ
  Ｑｊｓ＝Ｐｊｓ*ｔａｎφ
  一级配电柜至各回路二级箱负荷计算
  表4-3一、二级配电负荷计算表

**[E4]** [§ 设计配电系统和装置]
一级配电柜至各二级箱线路设计
备注：设计图中应体现以下信息
1、箱变及各级配电箱名称设计位置及分级。

- retrieved_nodes: L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L18, L19, L22, L23, L24, L25, L27, L28, L29, L37, L38, L76, L77, L78


---

## latest_clean_scope_0119  ·  scope_collection

- **Query:** 列举《9.1土方开挖方案范本》中“9.1土方开挖方案范本.docx”部分的主要条目。
- **Doc:** `real_69c60af6d4242eda8c47c934`
- **Gold nodes:** L5, L7, L8, L13, L16, L19

### 结果得分 — **PASS** (new gold_recall=0.50)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.50 |
| evidence_chars | 500 | 487 |
| n_retrieved_nodes | 28 | 22 |
| trajectory_steps | - | 14 |
| elapsed_sec | - | 8.64 |

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
  - reason: Dispatch major sections to gather main entries of the excavation plan efficiently.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L1 (depth=1) · →L1 · +8
      - reason: Collecting the main section '工程概况' to retrieve all primary entries of the excavation plan.
    - `F1` finish - (depth=1)
      - reason: The document root has been collected, which contains the main entries of the土方开挖方案范本.
    - `C1` collect L56 (depth=1) · →L56 · +4
      - reason: Collects the main 'Construction Guarantee Measures' section containing all required sub-items for the土方开挖方案范本.
    - `F1` finish - (depth=1)
      - reason: The required document section has been collected. Ready to finish.
    - `C1` collect L31 (depth=1) · →L31 · +4
      - reason: Collecting the 'Construction Plan' section to retrieve all main entries including schedule, materials, and labor plans.
    - `F1` finish - (depth=1)
      - reason: The document root L31 has been collected, containing the main entries of the excavation plan. No further collection is needed.
    - `C1` collect L41 (depth=1) · →L41 · +6
      - reason: Collecting the main section '施工工艺技术' to list its primary entries as requested.
    - `F1` finish - (depth=1)
      - reason: The document root L41 has been collected, containing the main entries of the excavation plan. No further collection is needed.
    - `C1` collect L103 (depth=1) · →L103 · +4
      - reason: Collects the main structure of 'Acceptance Requirements' section including standards, procedures, and content.
    - `F1` finish - (depth=1)
      - reason: The target document section has been collected. No further actions needed.
    - `C1` collect L120 (depth=1) · →L120 · +5
      - reason: Collecting the full 'Emergency Response Measures' section to identify main entries of the excavation plan.
    - `F1` finish - (depth=1)
      - reason: The document root L120 has been collected, which contains the target file '9.1土方开挖方案范本.docx'. No further collection is needed.
- `F1` finish - (depth=0)
  - reason: All main entries of the excavation plan have been collected and assembled in evidence groups.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L1` | - | 8 | 8 | - |  |
| 3 | `C1` | `L56` | - | 4 | 4 | - |  |
| 5 | `C1` | `L31` | - | 4 | 4 | - |  |
| 7 | `C1` | `L41` | - | 6 | 6 | - |  |
| 9 | `C1` | `L103` | - | 4 | 4 | - |  |
| 11 | `C1` | `L120` | - | 5 | 5 | - |  |

### 子 agent reports_context

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

### 最终 evidence(new)

**[E1]** [§ 工程概况]
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

**[E2]** [§ 施工计划]
材料及设备计划
表3.2土方开挖材料计划表
表3.3主要设备配置计划

- retrieved_nodes: L2, L3, L4, L11, L12, L13⭐, L15, L16⭐, L17, L18, L19⭐, L22, L23, L24, L25, L26, L27, L28, L29, L35, L36, L37


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
| elapsed_sec | - | 1.59 |

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

