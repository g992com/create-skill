# create-skill 工作备忘

记录本技能设计与迭代过程中的经验与结论，便于后续维护和复盘。

---

## 来源与许可

- 基于 **skill-creator**（Apache 2.0）衍生并修改。
- 采用 Apache 2.0，并在 LICENSE 中注明对 skill-creator 的归属与修改说明。

---

## 与 skill-creator 的差异（仅功能逻辑）

| 维度 | skill-creator | create-skill |
|------|----------------|--------------|
| **Structuring & authoring** | 四类结构 + Step 4 建议：编辑「正在创建的那门技能」时，参考**该技能自己的** `references/workflows.md`、`references/output-patterns.md`（若存在）。 | 四类结构 + Cursor 式内容模式 + 反模式 + 收尾清单，全部写在本技能的 SKILL.md 及本技能的 `references/workflows.md`、`references/output-patterns.md` 中；不依赖被创建技能是否带这两份文件。 |
| **Skill contents** | SKILL.md + scripts + tests，技能内不含 README。 | SKILL.md + README + LICENSE + scripts + tests，适合当独立仓库发布。 |

- 不比较 Platform、Language、Tests 等与“创建技能”功能逻辑无关的维度。
- skill-creator 在使用时也是安装到 Claude/Open Claw 内部，无外部路径依赖，因此不做“自包含 vs 依赖外部”的对比。

---

## references/workflows.md 与 references/output-patterns.md

- **在「被创建的那门技能」里**：这两份文件指**该技能自己的** references，不是 skill-creator 或 create-skill 仓库里的文件。Step 4 的“Consult references/workflows.md”等，意思是编辑**你正在做的那门技能**时，可参考**那门技能**自己的 references（若已建）。
- **在 create-skill 自身**：本技能也采用同样设计——把工作流/结构模式放到 `references/workflows.md`，把输出格式/示例/反模式放到 `references/output-patterns.md`，SKILL.md 中只保留主流程与链接，实现渐进披露。
- **在创建/编辑技能的逻辑中**：Step 2（规划）和 Step 4（编辑）中已明确建议：被创建技能可以包含 `references/workflows.md` 与 `references/output-patterns.md`，并在其 SKILL.md 中链接，由 agent 按需加载。

---

## 脚本与测试

- **init_skill.py / quick_validate.py / package_skill.py**：内置于本技能 `scripts/`，用于初始化、校验、打包**任意**技能（包括用户新建的技能）。
- **test_quick_validate.py、test_package_skill.py**：用于验证**本技能自己的** quick_validate、package_skill 行为正确，不是用来校验用户制作的那门技能。校验用户技能用 `quick_validate.py <技能目录>`。

---

## 文档与语言

- 当前 README、SKILL.md、脚本说明均为英文；对比表中不再写“create-skill 为中文”以免误导。
- 若后续改为中文版，需同步更新 README 中的对比说明。

---

## 修订记录

- 初版：建立 create-skill，整合 skill-creator 流程与脚本，自包含脚本与测试；增加 README、LICENSE（Apache 2.0）；厘清与 skill-creator 的差异（仅功能逻辑）；引入 references/workflows.md、output-patterns.md 设计于本技能及「创建/编辑技能」流程中；整理本备忘。
