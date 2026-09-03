# Task 1 报告：固定课程写作与题目契约

## 交付结果

新增 [`content/batch-2/00-authoring-contract.md`](../../../../content/batch-2/00-authoring-contract.md)，供 Task 2–4 按同一规则写作集合与函数节点。

契约固定了以下接口：

- 节点正文的 11 个有序部分，以及可视化必须为“本节点不设置互动”或完整、可验证的互动说明二选一；
- 例题 `EX01`、四道基础题 `B01`–`B04`、原子错题 `M01`、本地巩固 `R01`/`R02`、挑战 `X01` 的全局唯一编号；
- 共享综合题沿用第一批 `SP-Cxx-yy`，完整题面只在唯一归属节点出现，覆盖节点仅引用；
- 每题的题面、可接受答案、关键步骤、三级提示、原子错因、选择题干扰项和提交前检查记录；
- 提示使用与独立完成的分离记录，及“初步掌握”“稳定掌握”“需要复习”和挑战状态的明确出口。

## 关键裁定

计划草案中的 `<NODE>-C01..` 同时可以指巩固或挑战，不能让后续作者或录入层可靠判定难度。因此本批不发放本地 `C` 题号：巩固固定为 `R`，挑战固定为 `X`。这只改变新增题目代码的表达，不改变第一批任何 `M1-Cxx-Sxx-Kxx` 永久节点 ID，也不改变共享池的稳定 `SP-Cxx-yy` ID。

`M01` 始终只承载矩阵的一个“计数错因”；诊断候选只在答后以“可能错因”供 Mya 确认。基础掌握只计算未使用提示的独立基础作答；挑战失败不降低基础掌握度。

## 自审

- 对照第一批范围规则、覆盖矩阵的三要素蓝图/共享池/错因规则，以及产品规格的节点闭环、三级提示和掌握度要求完成交叉检查。
- 确认成稿没有 `TODO`、`TBD`、`待补`、`略`、`同理可得` 或“见上题”式占位；这些词只作为禁止项在契约中出现一次。
- 确认未修改 `src/`、`public/`、依赖或构建配置；本任务仅新增课程契约和本报告。

## 验证记录

| 检查 | 结果 |
|---|---|
| brief 要求的 `rg -n '情境问题|尝试作答|可视化探索|概念归纳|审题线索|分步推理|方法总结|方向提示|关键步骤提示|完整解析|初步掌握|稳定掌握|EX01|B01|M01' content/batch-2/00-authoring-contract.md` | 通过；所有契约词均有明确规则。 |
| 占位语扫描 | 通过；未发现实际占位内容。 |
| `git diff --check` | 通过；无空白错误。 |
| `npm run build` | 通过；`tsc -b && vite build` 退出码 0。 |
| `npm run lint` | 通过；`eslint .` 退出码 0。 |

## 后续任务关注点

Task 2–4 应直接采用 `R`/`X` 题号，而不是复用草案的歧义 `C` 题号；共享题要遵守唯一归属与唯一计数。每个节点的所有题号都要在同一课程稿中找到三级提示和完整答案，且 `M01` 不得叠加第二个实际错因。

## 计划接口对齐补充（2026-09-03）

控制器裁定保留 `R`（巩固）与 `X`（挑战）。已将实施计划 Task 1 Step 2 从歧义的本地 `C` 题号改为 `EX/B/M/R/X`，与课程契约和后续任务一致；没有扩大改动范围。

本轮执行的精确命令与输出如下。

```text
$ rg -n '<NODE>-(EX01|B01|M01|R01|X01|C01)|EX/B/M/R/X|不使用歧义的本地 `C`|本地巩固|节点挑战' docs/superpowers/plans/2026-09-03-batch-2-course-content-plan.md content/batch-2/00-authoring-contract.md && ! rg -n '<NODE>-C01|EX/B/M/C' docs/superpowers/plans/2026-09-03-batch-2-course-content-plan.md && git diff --check
docs/superpowers/plans/2026-09-03-batch-2-course-content-plan.md:49:  使用 `<NODE>-EX01`、`<NODE>-B01..B04`、`<NODE>-M01`、`<NODE>-R01..R02`、`<NODE>-X01`；`EX/B/M/R/X` 分别表示例题、基础、易错、巩固、挑战。本批不使用歧义的本地 `C` 题号。共享题沿用第一批 `SP-Cxx-xx`，并明确唯一归属节点。
content/batch-2/00-authoring-contract.md:37:| 基础例题 | `<NODE>-EX01` | 每节点恰 1 道；用于完整示范。 |
content/batch-2/00-authoring-contract.md:38:| 基础练习 | `<NODE>-B01` 至 `<NODE>-B04` | 每节点恰 4 道；各自考查一个可独立验证的基础动作。 |
content/batch-2/00-authoring-contract.md:39:| 易错辨析 | `<NODE>-M01` | 每节点恰 1 道；只诊断一个计数错因。 |
content/batch-2/00-authoring-contract.md:40:| 本地巩固 | `<NODE>-R01`、`<NODE>-R02` | 只在矩阵要求巩固时使用；用常见变式或少量明确前置稳定方法。 |
content/batch-2/00-authoring-contract.md:41:| 节点挑战 | `<NODE>-X01` | 只在矩阵要求挑战时使用；必须保留矩阵写明的跨节点连接。 |
content/batch-2/00-authoring-contract.md:43:本批**不发放**形如 `<NODE>-C01` 的本地题号。计划草案中的 `C` 同时指“巩固或挑战”会造成难度歧义；这里以 `R`（reinforcement，巩固）和 `X`（challenge，挑战）消除歧义，不改变任何永久节点 ID。
content/batch-2/00-authoring-contract.md:47:- 有共享题的归属节点写一题本地巩固 `R01`，再引用该 `SP` 题；共享题只在归属节点计数一次。
content/batch-2/00-authoring-contract.md:113:- 本地巩固只用 `R`，挑战只用 `X`；共享题只用稳定 `SP-Cxx-yy`，且完整内容仅出现在唯一归属节点。
```

```text
$ npm run build

> secondary_school@0.0.0 build
> tsc -b && vite build

vite v8.2.2 building client environment for production...
transforming...
✓ 22 modules transformed.
rendering chunks...
computing gzip size...
dist/index.html                   0.46 kB │ gzip:  0.29 kB
dist/assets/react-CHdo91hT.svg    4.12 kB │ gzip:  2.06 kB
dist/assets/vite-BF8QNONU.svg     8.70 kB │ gzip:  2.06 kB
dist/assets/hero-CLDdwZDr.png    13.05 kB
dist/assets/index-D64VDMd1.css    4.10 kB │ gzip:  1.47 kB
dist/assets/index-DaeTyWji.js   194.73 kB │ gzip: 61.21 kB

✓ built in 162ms
```

```text
$ npm run lint

> secondary_school@0.0.0 lint
> eslint .
```
