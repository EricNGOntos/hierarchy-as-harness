# Map-Nav 运行报告

- generated_at: `2026-07-15T15:08:03`
- env: EMBEDDING_MODEL=`text-embedding-v3` · NAV_MAP_MODE=`1` · enable_recursive_dispatch=`False` · map_char_limit=`5000` · max_steps=`8` · navigate_max_steps=`8`
- 汇总: 8 case · PASS 3/8 · mean gold_recall 0.312

| inspect_id | task_type | gold_recall | evidence_chars | steps |
|---|---|---:|---:|---:|
| latest_clean_multi_0010 | multi_hop | 0.00 | 476 | 4 |
| latest_clean_niche_0068 | niche_fact | 0.00 | 492 | 24 |
| latest_clean_scope_0101 | scope_collection | 0.00 | 158 | 11 |
| real_69c6ef484cca74801cb63bb9_multi_hop_auto_0006 | multi_hop | 0.00 | 486 | 10 |
| real_69cb12d0919452cda2225a0b_scope_collection_auto_0076 | scope_collection | 0.00 | 401 | 5 |
| real_69c60974d4242eda8c47c615_scope_collection_auto_0030 | scope_collection | 1.00 | 499 | 13 |
| latest_clean_multi_0032 | multi_hop | 0.50 | 484 | 8 |
| latest_clean_multi_0048 | multi_hop | 1.00 | 491 | 4 |

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
| elapsed_sec | - | 2.99 |

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
      - reason: Collect main document to access full content for multi-hop analysis.
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
| elapsed_sec | - | 18.3 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L2` | ❌ | False | False |

### 决策 TRACE(因果序)

- `D1` dispatch L1 (depth=0) · regions=[L1, L7, L25, L36, L49, L58, L73, L83, L91, L110, L118] · child_reports=11
  - reason: Dispatch all chapters to gather comprehensive regulations on seal management, usage, and penalties.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L36 (depth=1) · →L36 · +6
      - reason: Collecting Article 10 to retrieve the full regulations on seal usage scope.
    - `F1` finish - (depth=1)
      - reason: Evidence collected from the relevant section is sufficient to answer the query about the seal management regulations.
    - `C1` collect L7 (depth=1) · →L7 · +17
      - reason: Collect Chapter 2 to gather all regulations on seal carving and activation.
    - `F1` finish - (depth=1)
      - reason: Evidence collected is sufficient to answer the query regarding the seal management regulations.
    - `C1` collect L1 (depth=1) · →L1 · +5
      - reason: Collect Chapter 1 to gather all relevant regulations on seal management.
    - `F1` finish - (depth=1)
      - reason: The document root has been collected, providing the necessary context to answer the query about the seal management regulations.
    - `C1` collect L25 (depth=1) · →L25 · +29
      - reason: Collect Chapter 3 to gather all seal usage scope regulations.
    - `F1` finish - (depth=1)
      - reason: The relevant section has been collected. No further actions needed to answer the query.
    - `C1` collect L49 (depth=1) · →L49 · +8
      - reason: Collecting Article 12 to capture all regulations on project department seal usage scope.
    - `F1` finish - (depth=1)
      - reason: Collected section L49 contains the relevant regulations. No further collection needed.
    - `C1` collect L91 (depth=1) · →L91 · +9
      - reason: Collects the full section on seal management inspection and supervision requirements.
    - `F1` finish - (depth=1)
      - reason: Collected section L91 contains the relevant regulations. Ready to answer query.
    - `C1` collect L83 (depth=1) · →L83 · +7
      - reason: Collects the full section on seal registration and record keeping (Article 26) to answer the query.
    - `F1` finish - (depth=1)
      - reason: Collected section L83 contains the relevant regulations. Ready to answer query.
    - `C1` collect L73 (depth=1) · →L73 · +24
      - reason: Collect Chapter 5 to gather all relevant seal management regulations.
    - `F1` finish - (depth=1)
      - reason: Collected section L73 contains the relevant regulations. Ready to finish.
    - `C1` collect L58 (depth=1) · multi→[L58, L59, L60, L61, L62, L63, L64, L65, L66, L67, L68, L69, L70, L71, L72] · +14
      - reason: Collect all sections under Chapter 4 to extract specific seal usage regulations and facts.
    - `F1` finish - (depth=1)
      - reason: Collected section L58 contains the relevant regulations. No further collection needed.
    - `C1` collect L110 (depth=1) · multi→[L110, L111, L112, L113, L114, L115, L116, L117] · +7
      - reason: Collect all articles in Chapter 7 regarding seal management regulations and penalties.
    - `F1` finish - (depth=1)
      - reason: The required section has been collected and contains the relevant regulations. Ready to finish.
    - `C1` collect L118 (depth=1) · →L118 · +17
      - reason: Collect Chapter 8 to retrieve all relevant regulations and facts from the document.
    - `F1` finish - (depth=1)
      - reason: Collected section L118 contains the relevant regulations. No further collection needed.
- `F1` finish - (depth=0)
  - reason: Sufficient evidence collected from all relevant sections to answer the query about seal management regulations.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L36` | - | 6 | 6 | - | ✅ |
| 3 | `C1` | `L7` | - | 17 | 17 | - | ✅ |
| 5 | `C1` | `L1` | - | 5 | 5 | - | ✅ |
| 7 | `C1` | `L25` | - | 29 | 29 | - | ✅ |
| 9 | `C1` | `L49` | - | 8 | 8 | - | ✅ |
| 11 | `C1` | `L91` | - | 9 | 9 | - | ✅ |
| 13 | `C1` | `L83` | - | 7 | 7 | - | ✅ |
| 15 | `C1` | `L73` | - | 24 | 24 | - | ✅ |
| 17 | `C1` | `L58` | L58, L59, L60, L61, L62, L63, L64, L65, L66, L67, L68, L69, L70, L71, L72 | 14 | 28 | - | ✅ |
| 19 | `C1` | `L110` | L110, L111, L112, L113, L114, L115, L116, L117 | 7 | 14 | - | ✅ |
| 21 | `C1` | `L118` | - | 17 | 17 | - | ✅ |

### 子 agent reports_context

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

### 最终 evidence(new)

**[E1]** [§ 第七章	责任追究]
  第三十五条伪造、私刻集团公司法人章、财务专用章、银行预留印鉴章、领导签名章的，一经发现，对伪造、私刻责任方（单位、项目部、个人）处10万元罚款，并由集团公司组织调查组进行调查，根据情节轻重追究相关责任人的行政、经济责任，通报批评，依法追偿损失；涉嫌犯罪的，报请司法机关依法进行处理。
  第三十六条伪造、私刻集团公司机关部门章、二级单位章、项目部印章的，一经发现，对伪造、私刻责任方（单位、项目部、个人）处于6万元罚款，并由集团公司组织调查组进行调查，根据情节轻重追究相关责任人的行政、经济责任，通报批评，依法追偿损失。涉嫌犯罪的，报请司法机关依法进行处理。
  第四十一条有印章使用审批权限的其他管理人员，超越审批权限使用印章，造成经济损失及不良后果的，由集团公司党委组织部、监察审计部按《管理人员责任追究暂行规定》追究其相关责任。
  第四十二条印章责任管理单位、监管部门未认真履行印章管理、检查监督、封口管理等职责，发生伪造、私刻印章等情节严重，或造成经济损失及不良影响的，对管理责任人按集团公司《管理人员责任追究暂行规定》追究相关责任。

- retrieved_nodes: L110, L111, L112, L116, L117


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
| elapsed_sec | - | 26.22 |

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
      - reason: The current scope does not contain the 'Levels And Setting Out Of The Works' section. No relevant evidence can be collected here.
- `D1` dispatch L35 (depth=0) · regions=[L35] · child_reports=1
  - reason: Dispatch to find 'Levels And Setting Out Of The Works' section.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `F1` finish - (depth=1)
      - reason: The current scope does not contain the 'Levels And Setting Out Of The Works' section. No relevant evidence can be collected here.
- `D1` dispatch L35 (depth=0) · regions=[L35] · child_reports=1
  - reason: Dispatch to find 'Levels And Setting Out Of The Works' section.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `F1` finish - (depth=1)
      - reason: The current scope does not contain the 'Levels And Setting Out Of The Works' section. No relevant evidence can be collected here.
- `D1` dispatch L35 (depth=0) · regions=[L35] · child_reports=1
  - reason: Dispatch to find 'Levels And Setting Out Of The Works' section.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `F1` finish - (depth=1)
      - reason: The current scope does not contain the 'Levels And Setting Out Of The Works' section. No relevant evidence can be collected here.
- `F1` finish - (depth=0)
  - reason: The 'Levels And Setting Out Of The Works' section was not found in the investigated regions or current map. No further steps available to locate it.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C4` | `L110` | - | 1 | 1 | - | ✅ |
| 2 | `C10` | `L751` | - | 1 | 1 | - | ✅ |

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60aeed4242eda8c47c925:L35 (ok)
The current scope does not contain the 'Levels And Setting Out Of The Works' section. No relevant evidence can be collected here.
reason: The current scope does not contain the 'Levels And Setting Out Of The Works' section. No relevant evidence can be collected here.
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

## real_69c6ef484cca74801cb63bb9_multi_hop_auto_0006  ·  multi_hop

- **Query:** 根据质量控制要求，注浆允许偏差及检验办法应符合哪张表的规定？该表中列出了哪四个关键检查项目？同时，在浆液拌制过程中有哪些具体的操作要求以确保质量？
- **Doc:** `real_69c6ef484cca74801cb63bb9`
- **Gold nodes:** L159, L162, L167

### 结果得分 — **FAIL** (new gold_recall=0.00)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.00 |
| evidence_chars | 500 | 486 |
| n_retrieved_nodes | 12 | 10 |
| trajectory_steps | - | 10 |
| elapsed_sec | - | 8.74 |

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
      - reason: No further sections available to collect; insufficient evidence to answer query about specific tables and浆液拌制 requirements.
- `C31` collect L126 (depth=0) · →L126 · +2 · PURGED後代×1
  - reason: Need to collect the JGJ79-2012 section to find the specific table for grouting deviation and inspection methods.
- `C5` collect L21 (depth=0) · →L21 · +56
  - reason: Section 5 contains process details,浆液拌制 requirements, and likely the quality control table.
- `C34` collect L123 (depth=0) · →L123 · +2
  - reason: Collect Quality Control section to find the required table for grouting deviation and slurry mixing requirements.
- `C15` collect L99 (depth=0) · →L99 · +1
  - reason: Collects浆液拌制操作要求 and injection material specs needed for the query.
- `C14` collect L97 (depth=0) · multi→[L97, L98, L107] · +13 · PURGED後代×1
  - reason: Collect浆液拌制操作要求(C15)和注浆终孔标准/检验表相关部分(C23) to answer query.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C20` | `L128` | - | 1 | 1 | - | ✅ |
| 2 | `C20` | `L129` | - | 33 | 33 | - | ✅ |
| 3 | `C1` | `L113` | - | 2 | 2 | - | ✅ |
| 6 | `C31` | `L126` | - | 2 | 2 | 1 | ✅ |
| 7 | `C5` | `L21` | - | 56 | 56 | - | ✅ |
| 8 | `C34` | `L123` | - | 2 | 2 | - | ✅ |
| 9 | `C15` | `L99` | - | 1 | 1 | - | ✅ |
| 10 | `C14` | `L97` | L97, L98, L107 | 13 | 15 | 1 | ✅ |

**水合告警:**
- step 6 `C31` 收父节点 `L126` 时 **purge 掉 1 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。
- step 10 `C14` 收父节点 `L97` 时 **purge 掉 1 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c6ef484cca74801cb63bb9:L113 (ok)
collected 3 branch node(s); explicit roots=['real_69c6ef484cca74801cb63bb9:L113']
collected: real_69c6ef484cca74801cb63bb9:L113, real_69c6ef484cca74801cb63bb9:L114, real_69c6ef484cca74801cb63bb9:L115
reason: No further sections available to collect; insufficient evidence to answer query about specific tables and浆液拌制 requirements.
---
=== End Investigate ===
```

### 最终 evidence(new)

**[E1]** [§ 7.2 主要控制措施]
注浆允许偏差及检验办法应符合表7.2.1的规定。

**[E2]** [§ 5.2.7 注浆]
  确定注浆系统各部分连接无误后，开动注浆泵压水试验，检查注浆泵液压情况 ，系统管路有否漏浆，管路是否畅通。
  据地层及注浆压力进行调整，通过压力表观察注浆压力。注浆管每次上拔高度应为 33cm，为防止注浆管对后续施工产生危害，严禁将注浆管拔断掉落在阀管中。
  4、注浆终孔标准
  ②注浆压力上升缓慢，当注浆量达到设计要求，并确认未发生跑浆或漏浆； ③循环达到下述条件可结束注浆：设计的注浆孔均满足单根结束标准结束注浆 ，无漏注现象。
  - 1、水泥浆搅拌
  注浆前，严格按照配方配料。其中帷幕采用AB液作为注浆材料，A液∶B液=1∶1 ，其中A液：水泥：水=0.8∶1；B液：中性水玻璃，水玻璃为波美度25°～30°；帷 幕中心区采用纯水泥浆作为注浆材料，注浆水泥采用强度等级为Po42.5R普通水泥。 施工用水采用自来水。浆液应搅拌均匀，随拌随注，不得长时间存放已拌好的浆液 。封闭泥浆用泵从钻杆自下而上压入孔内，不准从孔口到入。

- retrieved_nodes: L126, L127, L128, L97, L101, L104, L107, L110, L98, L99


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
| elapsed_sec | - | 7.3 |

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
  - reason: Collected sections L124 and L128 contain the required points for cross-regional tax filing.

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
| evidence_chars | 500 | 499 |
| n_retrieved_nodes | 12 | 12 |
| trajectory_steps | - | 13 |
| elapsed_sec | - | 17.09 |

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
- `C10` collect L82 (depth=0) · →L82 · +1
  - reason: Collect definition of major accident hazards to ensure governance plan scope is understood.
- `D8` dispatch L81 (depth=0) · regions=[L81] · child_reports=1
  - reason: Dispatch to collect the full content of Section 2.4 'Hazard Rectification' which defines major accident hazards and likely contains governance plan requirements.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C10` collect L104 (depth=1) · →L104 · +6
      - reason: Section C10 covers risk control measures priority, which is a key element of major hazard governance plans.
    - `C2` collect L84 (depth=1) · →L84 · +1
      - reason: Collects definition of major accident hazards, relevant to the query about governance plans.
    - `C2` collect L85 (depth=1) · →L85 · +3
      - reason: Section 2.4.2 covers responsibilities for hazard rectification, relevant to the query.
    - `C1` collect L83 (depth=1) · →L83 · +1
      - reason: Collects definition of major accident hazards to identify relevant content elements.
    - `F1` finish - (depth=1)
      - reason: Collected sections cover general hazard rectification but lack specific elements for major accident hazard governance plans. No further relevant sections found in current scope.
- `C27` collect L304 (depth=0) · →L304 · +1
  - reason: Collect leaf C27 which explicitly mentions 'major hazard and accident hazard assessment, monitoring, and rectification' expenses, a key element of governance plans.
- `C28` collect L366 (depth=0) · →L366 · +1
  - reason: Section C28 explicitly references the required content for special plans regarding major hazard projects, directly addressing the query.
- `F1` finish - (depth=0)
  - reason: Collected evidence from L92 and L81 regions covers the required elements for major accident hazard governance plans. Sufficient to answer query.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L92` | L92, L93, L94, L95, L96, L97, L98, L99 | 11 | 18 | - | ✅ |
| 4 | `C10` | `L82` | - | 1 | 1 | - | ✅ |
| 5 | `C10` | `L104` | - | 6 | 6 | - | ✅ |
| 6 | `C2` | `L84` | - | 1 | 1 | - | ✅ |
| 7 | `C2` | `L85` | - | 3 | 3 | - | ✅ |
| 8 | `C1` | `L83` | - | 1 | 1 | - | ✅ |
| 11 | `C27` | `L304` | - | 1 | 1 | - | ✅ |
| 12 | `C28` | `L366` | - | 1 | 1 | - | ✅ |

**水合告警:**
- step 1 整枝水合含 2 个非 gold 叶 (与 gold 争抢 evidence 预算)。

### 子 agent reports_context

```
=== Investigate results (1 region(s)) ===
[region 1] real_69c60974d4242eda8c47c615:L81 (ok)
collected 13 branch node(s); explicit roots=['real_69c60974d4242eda8c47c615:L104', 'real_69c60974d4242eda8c47c615:L84', 'real_69c60974d4242eda8c47c615:L85', 'real_69c60974d4242eda8c47c615:L83']
collected: real_69c60974d4242eda8c47c615:L104, real_69c60974d4242eda8c47c615:L105, real_69c60974d4242eda8c47c615:L106, real_69c60974d4242eda8c47c615:L107, real_69c60974d4242eda8c47c615:L108, real_69c60974d4242eda8c47c615:L109, real_69c60974d4242eda8c47c615:L110, real_69c60974d4242eda8c47c615:L83, real_69c60974d4242eda8c47c615:L84, real_69c60974d4242eda8c47c615:L85, real_69c60974d4242eda8c47c615:L86, real_69c60974d4242eda8c47c615:L87, real_69c60974d4242eda8c47c615:L88
reason: Collected sections cover general hazard rectification but lack specific elements for major accident hazard governance plans. No further relevant sections found in current scope.
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
  1、一般事故隐患，是指危害和整改难度较小，发现后能够立即整改排除的隐患；
  2、重大事故隐患，是指危害和整改难度较大，应当全部或者局部停产停业，并经过一定时间整改治理方能排除的隐患，或者因外部因素影响致使生产经营单位自身难以排除的隐患。

- retrieved_nodes: L92, L102, L93, L94⭐, L95⭐, L96⭐, L97⭐, L98⭐, L99⭐, L82, L83, L84


---

## latest_clean_multi_0032  ·  multi_hop

- **Query:** 根据《线上学习平台学习管理方案（修订）》中“（ 一）课程开发管理”相关内容，分别说明两处相邻证据给出的要点。
- **Doc:** `real_69c6095ed4242eda8c47c5b2`
- **Gold nodes:** L34, L35

### 结果得分 — **PASS** (new gold_recall=0.50)

| 指标 | old(baseline) | new(map-nav) |
|---|---:|---:|
| gold_recall | 0.00 | 0.50 |
| evidence_chars | 142 | 484 |
| n_retrieved_nodes | 2 | 8 |
| trajectory_steps | - | 8 |
| elapsed_sec | - | 8.98 |

### Gold 命中审计

| gold | 命中 | in_retrieved | in_evidence_text |
|---|:--:|:--:|:--:|
| `L34` | ✅ | True | False |
| `L35` | ❌ | False | False |

### 决策 TRACE(因果序)

- `D10` dispatch L33 (depth=0) · regions=[L33] · child_reports=1
  - reason: Dispatch to 'Course Development Management' section to find adjacent evidence points.
  - ↳ 子 agent 步骤(dispatch 期间运行):
    - `C1` collect L33 (depth=1) · multi→[L33, L34, L35] · +4
      - reason: Collect adjacent sections C2 (Course Development) and C3 (Courseware Review) under 'Course Development Management' to answer the query.
    - `F1` finish - (depth=1)
      - reason: The current scope L33 contains the relevant section on course development management. No further collection is needed as the evidence is sufficient to address the query about adjacent points.
- `C14` collect L20 (depth=0) · →L20 · +1
  - reason: Collect adjacent evidence point regarding course development plan approval details.
- `C13` collect L19 (depth=0) · →L19 · +1
  - reason: Collect section on compulsory course development to identify adjacent points as requested.
- `C14` collect L18 (depth=0) · multi→[L18, L21] · +5 · PURGED後代×2
  - reason: Collect section on course categories and development to identify adjacent points in course development management.
- `C14` collect L24 (depth=0) · multi→[L24, L25] · +3
  - reason: Collect section on course development management and video course details to answer the query.
- `F1` finish - (depth=0)
  - reason: Evidence collected from L33 region covers 'Course Development Management' with sufficient adjacent points to answer the query.

### 水合审计(COLLECT)

| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |
|---:|---|---|---|---:|---:|---:|:--:|
| 1 | `C1` | `L33` | L33, L34, L35 | 4 | 6 | - | ✅ |
| 4 | `C14` | `L20` | - | 1 | 1 | - | ✅ |
| 5 | `C13` | `L19` | - | 1 | 1 | - | ✅ |
| 6 | `C14` | `L18` | L18, L21 | 5 | 6 | 2 | ✅ |
| 7 | `C14` | `L24` | L24, L25 | 3 | 4 | - | ✅ |

**水合告警:**
- step 1 整枝水合含 1 个非 gold 叶 (与 gold 争抢 evidence 预算)。
- step 6 `C14` 收父节点 `L18` 时 **purge 掉 2 条后代证据**(整枝重水合,可能销毁子 agent 的精选)。

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

**[E1]** [§ （ 一）课程类别]
  1.必修课程。必修课程需涵盖各专业系统内所有一般管理岗位。 由各专家组主持，根据所辖领域内各岗位职责制定课程开发计划、确定各系统岗位的必修课。课程开发计划需
  明确课程名称、课程类别、必修岗位、课程开发负责人等信息（见附件），提交十一在线平台中心审批后按计划开发。
  必修课程的开发数量各专家组结合业务和岗位需求实际确定，课程包含内部自主开发和外部引进，保证课程内容的实用性和有效性。
  岗位必修课程为各岗位年底技能测评的内容和依据。
  2.选修课程。员工自行选择需要学习的课程。 由员工结合本岗位履职需要、个人兴趣和其他能力提升需要， 自行选择相应选修课程学习。

**[E2]** [§ （ 一）课程开发管理]
1.课程开发。课程开发依托专家组、各业务线要从有利于组织目标达成、员工履职能力提升等方面，本着“简单、实用、明了”原则进行课程开发。各专家组、各部门应按年度既定课程开发计划，督促、跟进课程开发负责人按时完成课件开发任务。计划外课程开发须明确开发课程名称、学习对象等，经各专家组审核后开发，并向平台中心办公室备案。

- retrieved_nodes: L18, L19, L20, L21, L22, L23, L33, L34⭐


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
| elapsed_sec | - | 3.12 |

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
  - reason: Chapter 2 content collected in L6. Ready to summarize the two adjacent evidence points.

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

