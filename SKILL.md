---
name: create-skill
description: End-to-end guide for creating Agent Skills. Use when designing, writing, structuring, validating, or packaging skills; when the user wants to create a new skill, author SKILL.md, or learn skill structure, best practices, and format.
---

# Creating Skills in Cursor

This skill guides you through creating effective Agent Skills: from understanding requirements through initialization, authoring, validation, and packaging. Skills are directories with a `SKILL.md` that teach the agent specialized workflows, domain knowledge, and tool use.

**Built-in scripts**: This skill includes its own scripts in `scripts/` (init_skill.py, quick_validate.py, package_skill.py). **Always use these scripts** when initializing, validating, or packaging skills—they make the process reliable and consistent. The create-skill skill is installed at `~/.cursor/skills/create-skill`; run the scripts from there (e.g. `python ~/.cursor/skills/create-skill/scripts/init_skill.py ...`). On Windows, expand `~` to the user's home directory (e.g. `C:\Users\<user>\.cursor\skills\create-skill\scripts\init_skill.py`).

**Verifying the scripts**: To check that the validator and packager behave correctly, run the unit tests (from the create-skill `scripts/` directory or with it on PATH):

```bash
python ~/.cursor/skills/create-skill/scripts/test_quick_validate.py
python ~/.cursor/skills/create-skill/scripts/test_package_skill.py
```

These tests validate the *scripts* (e.g. frontmatter parsing, symlink handling, path escape); they do not validate a user-made skill—use `quick_validate.py <skill-dir>` for that.

## Skill Creation Process (6 Steps)

1. **Understand** the skill with concrete examples
2. **Plan** reusable contents (scripts, references, assets)
3. **Initialize** the skill (create directory and SKILL.md template)
4. **Edit** the skill (implement resources and write instructions)
5. **Validate** the skill (checklist before distribution)
6. **Package** (optional) and **iterate** after real use

---

## Step 1: Understand with Concrete Examples

Before writing, clarify:

- What exact task or workflow should this skill support?
- What would a user say that should trigger this skill?
- Target location: personal (`~/.cursor/skills/skill-name/`) or project (`.cursor/skills/skill-name/`)?
- Get 2–3 example requests from the user, or propose examples and confirm.

If context already makes the use case clear, you can skip. Conclude when you have a clear sense of functionality and triggers. Never create skills in `~/.cursor/skills-cursor/` (reserved for Cursor).

---

## Step 2: Plan Reusable Contents

For each use case, decide what to bundle:

| Resource | When to include | Examples |
|----------|------------------|----------|
| **scripts/** | Same code rewritten often, or need deterministic behavior | `rotate_pdf.py`, `validate.py`, `fill_form.py` |
| **references/** | Docs the agent should load when needed (schemas, APIs, policies) | `schema.md`, `api_docs.md`, `policies.md` |
| **assets/** | Files used in output, not loaded into context | Templates (.pptx, .docx), boilerplate dirs, fonts, logos |

- **scripts/**: Executable code (Python/Bash). Saves tokens and ensures consistency. Document how to run and what they do.
- **references/**: Keep SKILL.md lean; link from SKILL.md and describe when to read. One level deep only. The skill you're creating can use **references/workflows.md** (multi-step and conditional workflows) and **references/output-patterns.md** (output formats, templates, examples, anti-patterns); link from that skill's SKILL.md so the agent loads them when needed (progressive disclosure).
- **assets/**: Templates, images, fonts, starter projects—referenced in instructions, not read into context.

Produce a short list: which scripts, which reference files, which assets.

---

## Step 3: Initialize the Skill

**Use this skill's init script** (reliable and consistent):

```bash
python ~/.cursor/skills/create-skill/scripts/init_skill.py <skill-name> --path <output-dir> [--resources scripts,references,assets] [--examples]
```

- `<output-dir>`: folder where the new skill should live (e.g. project `.cursor/skills` or `~/.cursor/skills`); the script creates `<output-dir>/<skill-name>/`.
- `--resources`: comma-separated: `scripts`, `references`, `assets`.
- `--examples`: add placeholder files in those dirs (replace or delete later).

On Windows use the full path to the script, e.g. `C:\Users\<user>\.cursor\skills\create-skill\scripts\init_skill.py`.

**If the script cannot be run**, create the skill directory and SKILL.md manually using the template below.

**Directory layout:**

```
skill-name/
├── SKILL.md              # Required
├── scripts/              # Optional
├── references/           # Optional (e.g. workflows.md, output-patterns.md, schema.md)
└── assets/               # Optional
```

**SKILL.md template** (use when creating a new skill):

```markdown
---
name: skill-name
description: [TODO: What the skill does and when to use it. Include trigger scenarios, file types, or keywords.]
---

# Skill Title

## Overview

[TODO: 1–2 sentences on what this skill enables]

## [Main section]

[TODO: Instructions, workflows, or links to references/scripts]
```

- **Storage**: Personal `~/.cursor/skills/skill-name/` or project `.cursor/skills/skill-name/`.
- Create only the resource directories (scripts/, references/, assets/) that the skill actually needs.

---

## Step 4: Edit the Skill

When editing the skill you're creating, you can keep its SKILL.md lean by putting workflow and output-pattern detail in reference files. Optionally add **references/workflows.md** (sequential and conditional workflows, structure patterns) and **references/output-patterns.md** (templates, examples, anti-patterns) to that skill, and link from its SKILL.md (e.g. "For workflow patterns see [references/workflows.md](references/workflows.md). For output formats and examples see [references/output-patterns.md](references/output-patterns.md)."). The agent will load those files when needed.

### Frontmatter (required)

- **name**: Lowercase, letters/digits/hyphens only, max 64 chars. Normalize titles to hyphen-case (e.g. "Plan Mode" → `plan-mode`).
- **description**: Non-empty, max 1024 chars. **Critical for triggering**—the agent uses only name + description to decide when to apply the skill.

### Writing the description

1. **Third person** (description is injected into the system prompt):
   - ✅ "Processes Excel files and generates reports"
   - ❌ "I can help you process Excel files"

2. **Specific with trigger terms**:
   - ✅ "Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction."
   - ❌ "Helps with documents"

3. **Include WHAT and WHEN**: What the skill does + when the agent should use it (scenarios, file types, keywords). Put all "when to use" in the description; the body is only loaded after trigger.

**Description examples:**

```yaml
# PDF
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.

# Code review
description: Review code for quality, security, and maintainability following team standards. Use when reviewing pull requests, examining code changes, or when the user asks for a code review.
```

### Body

- Keep SKILL.md under 500 lines. Put details in references/ and link from SKILL.md.
- Use imperative/infinitive. Be concise; assume the agent is capable. Only add context it doesn’t already have.
- Link to reference files one level deep only (e.g. `[reference.md](references/schema.md)`).

### What NOT to include in a skill

Do not add README.md, INSTALLATION_GUIDE.md, QUICK_REFERENCE.md, CHANGELOG.md, or human-facing setup/testing docs. The skill is for the agent only.

### Patterns and anti-patterns (progressive disclosure)

- **Workflow and structure**: See [references/workflows.md](references/workflows.md) for structure patterns (workflow-based, task-based, etc.), content patterns (conditional workflow, feedback loop), and authoring principles.
- **Output formats, examples, anti-patterns**: See [references/output-patterns.md](references/output-patterns.md) for templates, description examples, utility-script guidance, and anti-patterns.

---

## Step 5: Validate

**Use this skill's validator** before considering the skill done:

```bash
python ~/.cursor/skills/create-skill/scripts/quick_validate.py <path/to/skill-folder>
```

On Windows use the full path to the script. If it reports errors, fix them. Then run through the checklist below.

**Checklist:**

- **Frontmatter**: `name` and `description` present; name matches `^[a-z0-9-]+$`, length ≤ 64; description non-empty, ≤ 1024 chars, no angle brackets.
- **Structure**: SKILL.md exists; references only one level deep; no README/CHANGELOG/install docs inside the skill.
- **Quality**: Description is specific, third-person, and includes WHAT and WHEN; SKILL.md under 500 lines; consistent terminology; no time-sensitive dates in main flow.
- **Scripts** (if any): Paths use slashes; run vs. read is clear; required packages and error handling documented.

Fix any issue before packaging or distributing.

---

## Step 6: Package (optional) and Iterate

**Package for distribution:** Use this skill's packager (it validates first, then creates the .skill zip):

```bash
python ~/.cursor/skills/create-skill/scripts/package_skill.py <path/to/skill-folder> [output-dir]
```

On Windows use the full path to the script. Do not package until validation passes. If the script cannot be run, zip the skill directory manually (exclude `.git`, `__pycache__`, `node_modules`) and name the archive `skill-name.skill`.

**Iterate**: After real use, improve SKILL.md or resources based on where the agent struggled or was inefficient.

---

## Complete Example

**Directory:**

```
code-review/
├── SKILL.md
├── STANDARDS.md
└── examples.md
```

**SKILL.md:**

```markdown
---
name: code-review
description: Review code for quality, security, and maintainability following team standards. Use when reviewing pull requests, examining code changes, or when the user asks for a code review.
---

# Code Review

## Quick Start

1. Check correctness and potential bugs
2. Verify security best practices
3. Assess readability and maintainability
4. Ensure tests are adequate

## Review Checklist

- [ ] Logic correct, edge cases handled
- [ ] No security issues (SQL injection, XSS, etc.)
- [ ] Follows project style; functions focused; errors handled; tests cover changes

## Feedback format

- 🔴 **Critical**: Must fix before merge
- 🟡 **Suggestion**: Consider improving
- 🟢 **Nice to have**: Optional

## Additional resources

- [STANDARDS.md](STANDARDS.md) — coding standards
- [examples.md](examples.md) — example reviews
```

---

## Summary Checklist

Before finalizing:

- [ ] Description specific, third-person, WHAT + WHEN
- [ ] SKILL.md under 500 lines; references one level deep
- [ ] No README/CHANGELOG/install docs in the skill
- [ ] Consistent terminology; no Windows backslash paths
- [ ] Validation passed (run this skill's `scripts/quick_validate.py`)
- [ ] If distributing: run this skill's `scripts/package_skill.py`, else zip as `skill-name.skill`
