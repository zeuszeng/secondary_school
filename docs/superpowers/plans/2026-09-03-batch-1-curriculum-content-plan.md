# 第一批课程内容交付实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 交付可供用户审阅的课程范围、全年知识图谱和人教 A 版必修第一册知识点—例题—练习覆盖清单。

**Architecture:** 事实来源、知识结构和题目覆盖分别维护，避免把课程依据与产品策划混写。知识图谱使用稳定节点编号连接全年依赖；上学期覆盖清单引用这些节点编号，并为每个可考查节点规定例题和练习配置。

**Tech Stack:** Markdown、Mermaid、Git；不修改 React/Vite 应用。

**Spec:** `docs/superpowers/specs/2026-09-03-mya-math-learning-site-design.md`

## Global Constraints

- 使用者只有 Mya；地点为广东惠州；当前为高一第一学期。
- 教材映射采用人教 A 版必修第一册和第二册，课程边界以现行国家课标为准。
- 全年十章建立知识图谱；题目覆盖清单只覆盖必修第一册五章。
- 每个可考查节点至少包含基础例题、基础练习和易错辨析；高频节点增加典型题、变式题和综合题。
- 初期难度比例为基础 70%、巩固 25%、挑战 5%。
- 题面、解析和图形后续优先自编；本批不复制教材、教辅、真题或第三方网站内容。
- 高考重要度只使用“基础支撑、核心高频、综合应用”，不写押题概率或未经核验的精确频率。
- 本批不修改 `src/`、`public/`、依赖或构建配置。

---

### Task 1: 固化第一批范围与节点规则

**Files:**
- Create: `content/batch-1/01-curriculum-scope.md`
- Read: `research/guangdong-grade10-math-scope-and-sources.md`
- Read: `docs/superpowers/specs/2026-09-03-mya-math-learning-site-design.md`

**Interfaces:**
- Consumes: 已核验的国家课标主题、人教 A 版十章目录、Mya 的学习约束。
- Produces: 全年图谱和上学期覆盖清单共同使用的范围、标签定义、节点编号规则与版权边界。

- [ ] **Step 1: 写出范围声明**

  明确全年图谱覆盖必修两册十章，上学期覆盖清单只覆盖必修第一册五章；集合是精简同步内容，函数概念与性质是首个完整单元。

- [ ] **Step 2: 定义节点编号**

  使用 `M1-C01-S01-K01` 格式：`M1/M2` 表示必修册次，`C` 表示章，`S` 表示节，`K` 表示最小可学习知识点。编号一经进入覆盖清单不得重复或复用。

- [ ] **Step 3: 定义标签**

  为“基础支撑、核心高频、综合应用”“前置、直接应用、跨章连接”“基础、巩固、挑战”分别写出判定标准和使用边界。

- [ ] **Step 4: 记录来源与版权规则**

  列出教育部、广东省教育厅、人教社和用户指定第三方目录页的不同证据角色；明确第三方页面不得成为题面或教材图片来源。

- [ ] **Step 5: 校验范围文件**

  Run: `rg -n '必修第一册|必修第二册|五章|十章|基础支撑|核心高频|综合应用|M1-C01-S01-K01|不得' content/batch-1/01-curriculum-scope.md`

  Expected: 每个关键词至少出现一次，且没有任何占位文本或待定范围。

### Task 2: 制作高一全年知识图谱

**Files:**
- Create: `content/batch-1/02-grade-10-knowledge-graph.md`
- Read: `content/batch-1/01-curriculum-scope.md`

**Interfaces:**
- Consumes: Task 1 的节点编号和标签规则。
- Produces: 上学期覆盖清单引用的节点目录、前置依赖和跨章连接。

- [ ] **Step 1: 建立十章节点树**

  按人教 A 版必修第一、第二册十章列出章、节和最小可学习知识点；每个最小节点分配唯一编号。

- [ ] **Step 2: 标注高考重要度**

  每个最小节点标注“基础支撑、核心高频、综合应用”之一，并用一句话解释其长期价值或组合关系。

- [ ] **Step 3: 标注依赖关系**

  为每个非起点节点列出直接前置编号；只记录理解该节点真正需要的直接依赖，不建立无意义的全连接。

- [ ] **Step 4: 添加全局 Mermaid 图**

  用 Mermaid 展示“预备知识 → 函数”“三角函数 → 平面向量及其应用”“集合与函数 → 概率统计语言”等主干关系；详细节点仍以表格为准。

- [ ] **Step 5: 验证编号与十章覆盖**

  Run: `rg -o 'M[12]-C[0-9]{2}-S[0-9]{2}-K[0-9]{2}' content/batch-1/02-grade-10-knowledge-graph.md | sort | uniq -d`

  Expected: 无输出，表示节点编号没有重复。

  Run: `rg -n '^## 第(一|二|三|四|五|六|七|八|九|十)章' content/batch-1/02-grade-10-knowledge-graph.md`

  Expected: 输出十个章标题。

### Task 3: 制作上学期覆盖清单

**Files:**
- Create: `content/batch-1/03-semester-1-coverage-matrix.md`
- Read: `content/batch-1/01-curriculum-scope.md`
- Read: `content/batch-1/02-grade-10-knowledge-graph.md`

**Interfaces:**
- Consumes: Task 2 中 `M1-` 开头的全部最小节点编号。
- Produces: 第二批课程写作可直接采用的例题、练习和易错点需求清单。

- [ ] **Step 1: 为每个上学期节点建立覆盖行**

  每行包含节点编号、学习目标、重要度、基础例题主题、基础练习数量、易错辨析、巩固/变式、挑战/综合、前置补给和建议时长。

- [ ] **Step 2: 写出题目蓝图而非复制题面**

  每个例题或练习用“考查目标 + 情境/数据约束 + 预期方法”描述，避免写入教材、教辅或第三方原题。

- [ ] **Step 3: 突出 Mya 的错误风险**

  对涉及符号、集合边界、运算顺序、分式、根式、不等号方向和定义域的节点标注检查动作；需要初中知识时关联 3–5 分钟基础补给。

- [ ] **Step 4: 检查最低覆盖标准**

  确保每行都有基础例题、至少一组基础练习和易错辨析；只有核心高频或综合应用节点才要求额外变式与挑战，维持初期 70/25/5 的整体难度目标。

- [ ] **Step 5: 比对图谱和覆盖清单编号**

  Run: `comm -23 <(rg -o 'M1-C[0-9]{2}-S[0-9]{2}-K[0-9]{2}' content/batch-1/02-grade-10-knowledge-graph.md | sort -u) <(rg -o 'M1-C[0-9]{2}-S[0-9]{2}-K[0-9]{2}' content/batch-1/03-semester-1-coverage-matrix.md | sort -u)`

  Expected: 无输出，表示图谱中的上学期节点都进入覆盖清单。

### Task 4: 制作审阅入口并完成一致性检查

**Files:**
- Create: `content/batch-1/README.md`
- Verify: `content/batch-1/01-curriculum-scope.md`
- Verify: `content/batch-1/02-grade-10-knowledge-graph.md`
- Verify: `content/batch-1/03-semester-1-coverage-matrix.md`

**Interfaces:**
- Consumes: Tasks 1–3 的全部交付文件。
- Produces: 用户可按顺序审阅的入口、关键决策摘要和明确的批次一审批项。

- [ ] **Step 1: 编写审阅顺序**

  README 先说明本批不含完整题面和页面开发，再依次链接范围、知识图谱和覆盖清单。

- [ ] **Step 2: 列出审批项**

  请用户分别确认课程边界、图谱粒度、重要度标注和题目覆盖蓝图；明确批准本批不会自动批准第二批或代码开发。

- [ ] **Step 3: 扫描占位符与越界文件**

  Run: `rg -n 'T''BD|TO''DO|待补|待定|稍后填写' content/batch-1 docs/superpowers/specs/2026-09-03-mya-math-learning-site-design.md`

  Expected: 无输出。

  Run: `git diff --name-only -- src public package.json package-lock.json vite.config.ts`

  Expected: 无输出，表示本批没有进入应用开发。

- [ ] **Step 4: 检查 Markdown 格式**

  Run: `git diff --check`

  Expected: 无输出。

- [ ] **Step 5: 提交第一批内容**

  Run: `git add content/batch-1 docs/superpowers/plans/2026-09-03-batch-1-curriculum-content-plan.md`

  Run: `git commit -m "docs: add first curriculum planning batch"`

  Expected: 提交仅包含计划和 `content/batch-1` 文件；推送前等待用户完成第一批审阅。
