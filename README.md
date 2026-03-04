# create-skill

Cursor Agent Skill: end-to-end guide and scripts for creating, validating, and packaging other skills. When you want to design, write, validate, or package a new skill, the AI follows this skill's process and runs its scripts.

[中文](README_ZH.md)

## Contents

- **SKILL.md** — Full instructions for the AI (6-step process, description and body rules, resource layout, validation and packaging).
- **scripts/** — Standalone Python scripts and unit tests.

## Scripts

| Script | Purpose |
|--------|---------|
| `init_skill.py` | Generate a new skill directory and SKILL.md from a template; optionally create scripts/references/assets |
| `quick_validate.py` | Validate a skill directory (frontmatter, name, description, etc.) |
| `package_skill.py` | Validate then package as a `.skill` (zip) file |
| `test_quick_validate.py` | Unit tests for the validator |
| `test_package_skill.py` | Unit tests for the packager |

## Usage

The skill is usually installed at `~/.cursor/skills/create-skill`. You can call the scripts by absolute path from any directory, for example:

```bash
# Initialize a new skill
python ~/.cursor/skills/create-skill/scripts/init_skill.py my-skill --path .cursor/skills

# Validate an existing skill
python ~/.cursor/skills/create-skill/scripts/quick_validate.py path/to/skill-dir

# Package as .skill
python ~/.cursor/skills/create-skill/scripts/package_skill.py path/to/skill-dir [output-dir]
```

On Windows, replace `~` with your user home directory (e.g. `C:\Users\<user>\`).

## Verifying the scripts

From the `scripts/` directory, run:

```bash
python test_quick_validate.py
python test_package_skill.py
```

## Difference from skill-creator

This project is derived from **skill-creator** (Apache 2.0). Only **functional / logic** differences:

| | skill-creator | create-skill (this repo) |
|---|----------------|---------------------------|
| **Structuring & authoring** | Four structure types in template; Step 4 says when editing the **skill you're creating**, consult that skill’s own `references/workflows.md` and `references/output-patterns.md` (if present) for patterns. | Same four types **plus** Cursor-style content patterns (template, examples, workflow, conditional, feedback loop), **anti-patterns**, and **summary checklist**—all in this skill’s SKILL.md, so the agent doesn’t rely on the output skill having those reference files. |
| **Skill contents** | SKILL.md + scripts + tests; no README in the skill. | SKILL.md + README + LICENSE + scripts + tests; repo-ready. |

## License

Apache License 2.0. This project is derived from and modifies skill-creator (Apache 2.0). See [LICENSE](LICENSE).
