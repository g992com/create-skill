# Output patterns, examples, and anti-patterns

Use when defining output formats, templates, examples, or avoiding common mistakes. Link from SKILL.md when the skill you're creating needs output-format or quality guidance.

## Output and template patterns

- **Template**: Define output format with a markdown/code template in the skill.
- **Examples**: For quality-sensitive output, give 2–3 input/output examples so the agent can match style.

## Description (frontmatter)

- **Third person** (description is injected into the system prompt): e.g. "Processes Excel files and generates reports" not "I can help you…"
- **Specific with trigger terms**: Include WHAT and WHEN; put all "when to use" in the description.
- **Examples**:
  - PDF: "Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction."
  - Code review: "Review code for quality, security, and maintainability following team standards. Use when reviewing pull requests, examining code changes, or when the user asks for a code review."

## Utility scripts in skills

Pre-made scripts are more reliable than generated code and save tokens. In SKILL.md, state clearly whether the agent should **execute** the script or **read** it. Use forward slashes in paths (e.g. `scripts/helper.py`), not backslashes.

## Anti-patterns

- **Windows-style paths**: Use `scripts/helper.py`, not `scripts\helper.py`.
- **Too many options**: Give one default; add an escape hatch if needed (e.g. "Use pdfplumber; for OCR use pdf2image + pytesseract").
- **Time-sensitive text**: Avoid "before August 2025 use old API." Put current method in main flow; legacy in a collapsed "Old patterns" section.
- **Inconsistent terms**: Pick one (e.g. "API endpoint" or "field") and use it throughout.
- **Vague names**: Prefer `processing-pdfs`, `analyzing-spreadsheets` over `helper`, `utils`, `tools`.
