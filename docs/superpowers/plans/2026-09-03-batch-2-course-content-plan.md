# 第二批课程内容交付实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 完成集合精简同步课程、函数概念与性质完整单元、公开视频筛选清单，以及一份可打印的 Mya 周中练习样例。

**Architecture:** 先固定统一的课程写作契约，再分别制作集合和函数内容；每个知识节点使用永久 ID 与第一批覆盖矩阵对齐。视频只作为节点补充索引，打印材料从已完成题目中选取并独立提供答案，所有交付通过批次 README 汇总审阅。

**Tech Stack:** Markdown、KaTeX/LaTeX 数学记法、Mermaid、PDF；不修改 React/Vite 应用。

**Spec:** `docs/superpowers/specs/2026-09-03-mya-math-learning-site-design.md`

## Global Constraints

- 使用者只有 Mya；广东惠州高一第一学期；人教 A 版必修第一册；当前进度为集合。
- 每周电脑学习 30–60 分钟；单段任务不超过 20 分钟；单节点 5–8 分钟。
- 集合课程覆盖第一批图谱中全部 13 个 `M1-C01-` 节点，按学校进度逐步开放。
- 函数完整单元覆盖第一批图谱中全部 15 个 `M1-C03-` 节点。
- 每个节点至少有 1 道自编基础例题、4 道自编基础练习和 1 道原子化易错辨析；按第一批矩阵补齐巩固、共享题和挑战题。
- 例题解析采用“审题线索 → 尝试入口 → 分步推理 → 方法总结 → 易错点 → 变式”。
- 提示采用“方向 → 关键步骤 → 完整解析”三级；挑战失败不降低基础掌握度。
- 趣味来自真实情境、猜想、图像操作和即时验证；不使用排行榜、强剧情、幼儿化表达或无关动画。
- 题面、解析和图形全部自编；不复制教材、教辅、真题、第三方网页或视频内容。
- 视频单段目标为 3–6 分钟，优先官方资源；只使用原页链接或平台明确支持的官方嵌入，不下载、剪辑或重新托管。
- A4 样例须黑白打印清楚，预计 10–15 分钟完成，包含 1 个核心结论、1 个易错提醒、3–5 道题、演算空间及独立答案区。
- 第二批不修改 `src/`、`public/`、依赖或构建配置；不进入页面开发。
- 第一批最终裁定：`M1-C03-S03-K02` 的实际易错题只能选择一个具体错误来源；本批采用“未先确认两个比较量位于同一合法单调区间”，定义域问题保留为答后诊断候选。

---

### Task 1: 固定课程写作与题目契约

**Files:**
- Create: `content/batch-2/00-authoring-contract.md`
- Read: `content/batch-1/01-curriculum-scope.md`
- Read: `content/batch-1/03-semester-1-coverage-matrix.md`
- Read: `docs/superpowers/specs/2026-09-03-mya-math-learning-site-design.md`

**Interfaces:**
- Consumes: 第一批节点、题目蓝图、难度与错因规则。
- Produces: Tasks 2–4 共用的节点模板、题目编号、答案与提示格式、掌握度出口。

- [ ] **Step 1: 定义节点正文模板**

  每个节点按固定顺序包含：节点元数据、情境问题、尝试作答、可视化探索说明、概念归纳、基础例题、四道基础练习、原子化易错辨析、按矩阵要求的巩固/挑战、三级提示、答案与节点总结。无实际价值的可视化必须明确写“本节点不设置互动”，不能虚构游戏。

- [ ] **Step 2: 定义稳定题目编号**

  使用 `<NODE>-EX01`、`<NODE>-B01..B04`、`<NODE>-M01`、`<NODE>-C01..`；`EX/B/M/C` 分别表示例题、基础、易错、巩固或挑战。共享题沿用第一批 `SP-Cxx-xx`，并明确唯一归属节点。

- [ ] **Step 3: 定义答案与反馈契约**

  每题记录唯一答案或完整可接受答案集合、三级提示、关键步骤、原子错因和提交前检查；选择题干扰项必须对应可说明的错误，不以刁钻文字制造难度。

- [ ] **Step 4: 定义完成标准**

  节点基础题稳定通过后为“初步掌握”；间隔复习通过后为“稳定掌握”。用提示完成和独立完成必须分开记录，挑战题只记录“正在挑战/完成”。

- [ ] **Step 5: 验证契约完整性**

  Run: `rg -n '情境问题|尝试作答|可视化探索|概念归纳|审题线索|分步推理|方法总结|方向提示|关键步骤提示|完整解析|初步掌握|稳定掌握|EX01|B01|M01' content/batch-2/00-authoring-contract.md`

  Expected: 每项契约均有明确规则，没有占位内容。

### Task 2: 完成集合精简同步课程

**Files:**
- Create: `content/batch-2/01-set-sync-course.md`
- Read: `content/batch-2/00-authoring-contract.md`
- Read: `content/batch-1/02-grade-10-knowledge-graph.md`
- Read: `content/batch-1/03-semester-1-coverage-matrix.md`

**Interfaces:**
- Consumes: 13 个 `M1-C01-` 节点及对应题目蓝图。
- Produces: 可直接进入后续页面录入的集合课程、题目、提示和答案。

- [ ] **Step 1: 编排同步开放顺序**

  按 1.1 至 1.5 排列 13 个节点，并在开头给出“本周老师教到哪里”的开放映射；当前默认只开放 1.1 已学内容，其他内容标为随学校进度开放，不强制锁定。

- [ ] **Step 2: 写完 13 个学习节点**

  每个节点严格使用 Task 1 模板，时长为 5–8 分钟；情境简洁，不用与数学目标无关的故事。集合表示、子集、空集、并交补和区间端点必须强化符号检查。

- [ ] **Step 3: 写完全部题目与解析**

  按第一批矩阵逐节点实现基础例题、4 道基础练习、1 道易错辨析以及要求的巩固/挑战。所有题目写出答案与三级提示；不得用“略”“同理”替代解析。

- [ ] **Step 4: 设置 20 分钟周末路线**

  至少提供“刚学集合概念”“学到集合关系”“学到集合运算”三条周末路线，每条含 2–3 个节点和明确停靠点；优先顺序是本周错误、当前核心、必要补给、少量预习。

- [ ] **Step 5: 验证集合覆盖**

  Run: `comm -3 <(awk -F'|' '$2 ~ /^[[:space:]]*定义[[:space:]]*$/ {id=$3; gsub(/[[:space:]]/,"",id); if(id~/^M1-C01-/)print id}' content/batch-1/02-grade-10-knowledge-graph.md | sort -u) <(rg -o '^## M1-C01-[A-Z0-9-]+' content/batch-2/01-set-sync-course.md | sed 's/^## //' | sort -u)`

  Expected: 无输出；13 个节点一一对应。

### Task 3: 完成函数 3.1 与 3.2 课程

**Files:**
- Create: `content/batch-2/function/README.md`
- Create: `content/batch-2/function/01-concept-and-representation.md`
- Create: `content/batch-2/function/02-properties.md`
- Read: `content/batch-2/00-authoring-contract.md`
- Read: `content/batch-1/03-semester-1-coverage-matrix.md`

**Interfaces:**
- Consumes: `M1-C03-S01-K01..K06` 与 `M1-C03-S02-K01..K05` 的蓝图。
- Produces: 函数单元前 11 个节点和后续 3.3/3.4 使用的表示、定义域、单调性、最值、奇偶性接口。

- [ ] **Step 1: 写单元入口与前置诊断**

  `function/README.md` 说明 15 节点路线、集合/不等式前置补给、10–15 分钟诊断和三种学习入口；诊断不显示排名或强制倒计时。

- [ ] **Step 2: 完成 3.1 六个节点**

  覆盖函数对应唯一性、定义域、函数值与值域、同一函数判断、三种表示互译、分段函数。定义域和分段边界必须包含提交前检查。

- [ ] **Step 3: 完成 3.2 五个节点**

  覆盖单调性定义、单调区间、最值、奇偶性和性质综合。需要互动的节点写出参数、初始状态、可操作动作、即时反馈和认知目标；不写实现代码。

- [ ] **Step 4: 完成题目与解析**

  每节点按契约和第一批矩阵实现全部例题、练习、错因、巩固/挑战、提示与答案；所有跨节点题引用永久节点 ID。

- [ ] **Step 5: 验证 11 节点覆盖**

  Run: `rg -o '^## M1-C03-S0[12]-[A-Z0-9-]+' content/batch-2/function/0*.md | sed 's/.*:## //' | sort -u | wc -l`

  Expected: `11`。

### Task 4: 完成函数 3.3、3.4 与单元整合

**Files:**
- Create: `content/batch-2/function/03-power-functions.md`
- Create: `content/batch-2/function/04-applications.md`
- Modify: `content/batch-2/function/README.md`
- Read: `content/batch-2/00-authoring-contract.md`
- Read: `content/batch-1/03-semester-1-coverage-matrix.md`

**Interfaces:**
- Consumes: Task 3 的函数前 11 节点及 `M1-C03-S03-K01..K02`、`M1-C03-S04-K01..K02` 蓝图。
- Produces: 15 节点完整函数单元、单元结束挑战和周末短路线。

- [ ] **Step 1: 完成 3.3 两个节点**

  覆盖幂函数识别和性质应用。`M1-C03-S03-K02-M01` 只考查“未先确认两个比较量位于同一合法单调区间”，不得同时嵌入独立的定义域错误。

- [ ] **Step 2: 完成 3.4 两个节点**

  覆盖函数模型识别和实际问题解释；每题明确变量、单位、定义域、连续/离散性和现实可行范围。

- [ ] **Step 3: 完成单元整合**

  在 `function/README.md` 添加不少于四条 20 分钟内路线、单元结束挑战、掌握度出口和“需要复习”回路。挑战失败只标记“正在挑战”。

- [ ] **Step 4: 校验函数全覆盖与交叉引用**

  Run: `comm -3 <(awk -F'|' '$2 ~ /^[[:space:]]*定义[[:space:]]*$/ {id=$3; gsub(/[[:space:]]/,"",id); if(id~/^M1-C03-/)print id}' content/batch-1/02-grade-10-knowledge-graph.md | sort -u) <(rg -h -o '^## M1-C03-[A-Z0-9-]+' content/batch-2/function/*.md | sed 's/^## //' | sort -u)`

  Expected: 无输出；15 个节点一一对应。

- [ ] **Step 5: 核验题目数量与答案**

  为每个节点统计 `EX01`、`B01..B04`、`M01` 和矩阵规定的额外题目；每个题目 ID 全局唯一，且均能在同一文件找到答案与提示。

### Task 5: 筛选视频并建立节点索引

**Files:**
- Create: `content/batch-2/02-video-resources.md`
- Read: `research/batch-2-video-candidates.md`
- Read: `content/batch-2/01-set-sync-course.md`
- Read: `content/batch-2/function/*.md`

**Interfaces:**
- Consumes: 后台调查核验的官方/原创视频候选和完成后的 28 个课程节点。
- Produces: 学生可见的精选视频卡片、节点映射与失效回退规则。

- [ ] **Step 1: 逐项复核候选**

  仅保留标题、机构/作者、URL、知识点和可用性均可核验的候选。无法核验时长时写“时长未由官方页面公开”，不得估算。

- [ ] **Step 2: 限制视频角色**

  每个节点最多推荐一个视频；没有合适视频时明确不推荐，不为追求覆盖率降低质量。较长视频只标记官方提供的章节或时间定位；否则只链接完整原页。

- [ ] **Step 3: 写版权与回退规则**

  明确不自动播放、不下载、不剪辑、不转存；嵌入必须使用平台官方能力。失效时展示标题、来源、知识点和原页链接，站内课程仍能独立完成。

- [ ] **Step 4: 验证链接与节点**

  检查每个 URL 使用 HTTPS、每个节点 ID 存在于集合或函数课程、同一 URL 不重复堆叠。

### Task 6: 制作 A4 黑白打印样例

**Files:**
- Create: `content/batch-2/print/weekly-set-review-source.md`
- Create: `content/batch-2/print/mya-weekly-set-review.pdf`
- Read: `content/batch-2/01-set-sync-course.md`

**Interfaces:**
- Consumes: 集合课程中已完成且自编的题目与易错提醒。
- Produces: 一份可直接打印的周中练习 PDF 及可审阅的内容源稿。

- [ ] **Step 1: 选择本周目标**

  主题限定为“集合概念、属于关系与表示法”，包含 1 个核心结论、1 个 `∈/⊆` 易错提醒和 4 道预计 10–15 分钟完成的题；不提前使用未学的集合运算。

- [ ] **Step 2: 编排 A4 页面**

  第一页放学习卡、四道题和充分演算空间；第二页放分级提示与答案。黑白打印时层级必须依靠字号、边框和线型，而非颜色。

- [ ] **Step 3: 生成 PDF**

  使用 PDF 技能规定的生成方式，嵌入可用中文字体，确保公式、集合符号和上下标不乱码。

- [ ] **Step 4: 渲染并目视检查**

  将 PDF 每页渲染为 PNG，检查裁切、换行、字体、公式、演算空间和答案隔离；发现问题后重新生成并复查。

- [ ] **Step 5: 检查 PDF**

  Run: `pdfinfo content/batch-2/print/mya-weekly-set-review.pdf`

  Expected: A4，2 页，无加密；标题和作者元数据正确。

### Task 7: 建立第二批审阅入口并完成整体验收

**Files:**
- Create: `content/batch-2/README.md`
- Verify: `content/batch-2/00-authoring-contract.md`
- Verify: `content/batch-2/01-set-sync-course.md`
- Verify: `content/batch-2/function/*.md`
- Verify: `content/batch-2/02-video-resources.md`
- Verify: `content/batch-2/print/*`

**Interfaces:**
- Consumes: Tasks 1–6 的全部交付文件。
- Produces: 用户可按课程、题目、视频和打印材料四个维度审批的入口。

- [ ] **Step 1: 编写审阅入口**

  README 明确本批包含完整自编题面、解析、视频索引和打印样例，但不包含页面开发；按“集合 → 函数 → 视频 → PDF”顺序链接文件。

- [ ] **Step 2: 列出四项审批**

  分别请求确认：课程节奏与语气、题目质量与难度、视频选择与外链方式、A4 打印效果。说明第二批获批不自动批准第三批或代码开发。

- [ ] **Step 3: 扫描范围与占位内容**

  确认没有修改 `src/`、`public/`、依赖或构建配置；扫描空答案、“略”“同理可得”、临时标记和未解析题目引用。

- [ ] **Step 4: 完成内容一致性检查**

  验证 13 个集合节点、15 个函数节点、全部题目 ID 唯一、每题有提示与答案、视频节点可解析、PDF 源题可追溯至集合课程。

- [ ] **Step 5: 完成项目检查并提交**

  Run: `git diff --check`

  Run: `npm run build`

  Run: `npm run lint`

  Expected: 全部退出码为 0，且提交只包含第二批计划、研究文件和 `content/batch-2`。
