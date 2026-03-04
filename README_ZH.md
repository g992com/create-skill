# create-skill

Cursor Agent Skill：用于创建、校验和打包其他技能的端到端指南与脚本。当需要设计、编写、校验或打包新技能时，AI 会按本技能的流程执行并调用其脚本。

[English](README.md)

## 目录

- **SKILL.md** — 给 AI 的完整说明（6 步流程、description 与正文规则、资源布局、校验与打包）。
- **scripts/** — 可独立运行的 Python 脚本与单元测试。

## 脚本

| 脚本 | 用途 |
|------|------|
| `init_skill.py` | 从模板生成新技能目录和 SKILL.md；可选创建 scripts/references/assets |
| `quick_validate.py` | 校验技能目录（frontmatter、name、description 等） |
| `package_skill.py` | 先校验再打包为 `.skill`（zip） |
| `test_quick_validate.py` | 校验脚本的单元测试 |
| `test_package_skill.py` | 打包脚本的单元测试 |

## 使用方式

本技能通常安装在 `~/.cursor/skills/create-skill`。可在任意目录下用绝对路径调用脚本，例如：

```bash
# 初始化新技能
python ~/.cursor/skills/create-skill/scripts/init_skill.py my-skill --path .cursor/skills

# 校验已有技能
python ~/.cursor/skills/create-skill/scripts/quick_validate.py path/to/skill-dir

# 打包为 .skill
python ~/.cursor/skills/create-skill/scripts/package_skill.py path/to/skill-dir [output-dir]
```

Windows 下请将 `~` 替换为当前用户主目录（如 `C:\Users\<用户名>\`）。

## 验证脚本

在 `scripts/` 目录下执行：

```bash
python test_quick_validate.py
python test_package_skill.py
```

## 与 skill-creator 的差异

本项目衍生自 **skill-creator**（Apache 2.0），仅列出**功能/逻辑**层面的差异：

| | skill-creator | create-skill（本仓库） |
|---|----------------|---------------------------|
| **结构与写作** | 模板含四类结构；Step 4 建议在编辑**正在创建的那门技能**时，参考该技能自己的 `references/workflows.md` 和 `references/output-patterns.md`（若存在）。 | 同样四类结构，**另加** Cursor 式内容模式（模板、示例、工作流、条件、反馈循环）、**反模式**和**收尾清单**，均写在本技能的 SKILL.md 中，因此不依赖被创建技能是否自带这些参考文件。 |
| **技能内容** | SKILL.md + scripts + tests；技能内不含 README。 | SKILL.md + README + LICENSE + scripts + tests；适合作为独立仓库发布。 |

## 许可证

Apache License 2.0。本项目衍生并修改自 skill-creator（Apache 2.0）。详见 [LICENSE](LICENSE)。
