# Workflow and structure patterns

Use when the skill you're creating has multi-step processes, decision points, or needs a clear structure. Keep SKILL.md lean; link from SKILL.md to this file (or to the output skill's own references) when the agent needs workflow detail.

## Structure patterns (choose as needed)

- **Workflow-based**: Overview → Decision tree → Step 1 → Step 2…
- **Task-based**: Overview → Quick start → Task A → Task B…
- **Reference/guidelines**: Overview → Guidelines → Specs → Usage
- **Template + examples**: Output format template plus 2–3 concrete examples

## Content patterns (workflows)

- **Workflow**: Numbered steps and a checklist; say whether the agent should **execute** scripts or **read** them.
- **Conditional workflow**: Decision points (e.g. "Creating new? → Creation workflow; Editing? → Editing workflow").
- **Feedback loop**: For quality-critical tasks, validate after edits (e.g. run a script) and repeat until pass.

## Core authoring principles

- **Concise**: Challenge every paragraph—does the agent really need it?
- **Progressive disclosure**: Essentials in SKILL.md; details in reference files the agent loads when needed.
- **Degrees of freedom**: High (text) when many valid approaches; medium (templates) when a preferred pattern exists; low (fixed scripts) when operations are fragile or consistency is critical.
