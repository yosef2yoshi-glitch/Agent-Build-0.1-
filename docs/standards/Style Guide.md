# AI Agent Build 0.1 — Markdown Style Guide

**Document Type:** Project Standard  
**Purpose:** Establish one consistent Markdown format for all AI Agent Build 0.1 documentation.  
**Scope:** README files, Build Notes, Development Log, technical references, test notes, architecture notes, and future project documentation.  
**Audience:** Project owner and development assistant  
**Owner:** Project Owner  
**Version:** 1.0  
**Last Updated:** 2026-11-21  
**Status:** Working Standard

---

## 1. Purpose

This guide defines how Markdown documents in AI Agent Build 0.1 must be structured, formatted, updated, and reviewed.

The goal is simple: a reader should be able to open any project document and recognize the same formatting conventions immediately.

**Rule:** Do not introduce a new formatting style in an individual document. Follow this guide unless the project owner approves an exception.

## 2. General Markdown Rules

1. Use standard Markdown syntax.
2. Use one space after heading markers.
3. Do not wrap headings in bold markers.
4. Do not use HTML entities when a normal character will work.
5. Do not use HTML for layout or styling unless there is a documented reason and the project owner approves it.
6. Use actual Markdown lists instead of manually typed bullet symbols.
7. Use blank lines to separate headings, paragraphs, lists, tables, and code blocks.
8. Do not add multiple empty lines to create visual spacing.
9. Do not use decorative Unicode borders or large ASCII banners in normal documentation.
10. Keep formatting consistent across the entire file.

### Correct heading syntax

```markdown
# Document Title

## Major Section

### Subsection

#### Detail
```

### Incorrect heading syntax

```markdown
**## Major Section**
###**Subsection**
```

## 3. Heading Hierarchy

Use headings in order. Do not skip levels simply to make text look larger.

| Level | Use | Example |
|---|---|---|
| `#` | Document title; use once per document | `# AI Agent Build 0.1` |
| `##` | Major document sections | `## Project Overview` |
| `###` | Subsections within a major section | `### Current Architecture` |
| `####` | Small supporting sections, only when needed | `#### Approval State` |

Do not use bold text as a substitute for a heading. Do not use headings only to make a sentence stand out.

## 4. Paragraphs and Lists

### Paragraphs

- Keep paragraphs focused on one idea.
- Prefer short, readable paragraphs.
- Use a blank line between paragraphs.
- Avoid manual line breaks inside ordinary paragraphs unless the line break has meaning.

### Unordered lists

Use hyphens:

```markdown
- First item
- Second item
- Third item
```

Do not mix hyphens, asterisks, and plus signs in the same document.

### Ordered lists

Use numbered lists for sequences and procedures:

```markdown
1. Review the task.
2. Validate the request.
3. Prepare the plan.
4. Request approval when required.
5. Execute only when authorized.
```

Use nested lists only when the relationship between items requires them. Indent nested items consistently by four spaces.

### Checklists

Use GitHub-style task lists for work tracking:

```markdown
- [ ] Not started
- [x] Completed
```

Do not use checklists as decoration.

## 5. Emphasis and Inline Formatting

Use emphasis sparingly and consistently.

- **Bold:** Important terms, labels, and short warnings.
- *Italic:* Occasional emphasis or titles of works.
- `Inline code`: File names, folders, commands, variables, methods, attributes, parameters, and literal values.

Examples:

- The `Agent` class defines the agent's structure.
- The `current_task` attribute stores the task currently being processed.
- Run `python3 -m unittest -v test_agent_` to execute the test suite.
- **Important:** Do not treat a simulated result as proof that a real operation occurred.

Avoid bolding entire paragraphs. Do not use bold and italics together unless there is a clear reason.

## 6. Code and Command Formatting

### Inline code

Use single backticks for short code references:

```markdown
The `validate_rules()` method checks the task against the agent's rules.
```

### Fenced code blocks

Use fenced code blocks with a language identifier whenever possible.

Python:

````markdown
```python
def startup(self):
    print("Agent starting...")
```
````

PowerShell:

````markdown
```powershell
Get-Process
```
````

Bash / terminal:

````markdown
```bash
python3 -m unittest -v test_agent_
```
````

Text output:

````markdown
```text
Ran 4 tests in 0.002s

OK
```
````

Rules:

1. Never remove indentation from code.
2. Do not reformat code in a documentation-only update unless code formatting is the specific task.
3. Keep commands separate from their expected output.
4. Explain what a command does when the intended reader may not know it.
5. Do not place explanatory prose inside a code block.
6. Do not claim code is current unless it has been checked against the current source file.
7. When documenting code changes, identify the file and method. Include line numbers only when verified against the exact source version.

## 7. Tables

Use tables for compact comparisons, metadata, status summaries, and structured reference information.

Example:

| Item | Description | Status |
|---|---|---|
| `agent.py` | Main agent implementation | Active |
| `test_agent_.py` | Agent unit tests | Active |
| `README.md` | Project overview and instructions | Maintained |

Rules:

- Include a header row.
- Keep cells concise.
- Do not put long explanations or large code blocks inside tables.
- Use lists or subsections when table cells become difficult to read.
- Keep status labels consistent throughout a document.

## 8. Warnings, Decisions, and Notes

Use consistent labels. Do not invent a new callout style in each file.

Recommended formats:

```markdown
> **Important:** This behavior is simulated. It does not perform a real file operation.
```

```markdown
> **Safety:** A task must not execute when required approval has not been granted.
```

```markdown
> **Decision:** One human approval authorizes one specific task and its associated plan. A changed task or plan requires fresh approval.
```

Use these labels deliberately:

- **Important:** General information the reader should not miss.
- **Safety:** A risk, safeguard, or execution restriction.
- **Decision:** An agreed project decision.
- **Note:** Supporting information or clarification.
- **Open Question:** A decision that has not yet been made.

Do not use a callout for ordinary paragraphs.

## 9. Dates, Versions, and Status

- Use ISO date format: `YYYY-MM-DD`.
- Use consistent version notation, such as `0.1`, `0.2`, and `1.0`.
- Do not mix date formats within a document.
- Mark proposals as **Proposed** until approved.
- Mark implementation status accurately: **Not Started**, **In Progress**, **Blocked**, or **Complete**.
- A test passing does not prove that untested behavior is safe.

## 10. Standard Document Header

The project-wide Visual Document Header Standard remains authoritative and must be preserved exactly unless the project owner approves a change.

For Markdown documents, use this structure at the beginning of the document:

```markdown
# Document Title

**Document Category:** [Category]  
**Title:** [Document Title]  
**Subtitle:** [Short description]

| Metadata | Details |
|---|---|
| Purpose | [Why this document exists] |
| Scope | [What this document covers] |
| Audience | [Who should use it] |
| Owner | [Document owner] |
| Version | [Version] |
| Last Updated | [YYYY-MM-DD] |

---
```

Do not silently remove, rename, reorder, or replace the established metadata fields. If a document uses a different approved header layout already, preserve it until the project owner approves a controlled standardization.

## 11. Document-Specific Structure

Different documents serve different purposes. They should share formatting, not be forced into identical content structures.

### 11.1 README.md

Recommended structure:

1. Project title
2. Project overview
3. Goals and scope
4. Current status
5. Requirements
6. Setup and installation
7. How to run
8. How to test
9. Project structure
10. Safety and limitations
11. Current checkpoint
12. Next steps
13. Related documentation

The README should help a new reader understand and run the project. It should not become a chronological record of every development conversation.

### 11.2 Build Notes

Recommended structure:

1. Project purpose and vision
2. Design principles
3. Architecture and components
4. Core concepts and terminology
5. Safety model
6. Approved design decisions
7. Proposed designs
8. Known risks and limitations
9. Open questions
10. References to implementation and tests

Build Notes explain **why the system is designed this way** and preserve important technical understanding.

### 11.3 Development Log

Recommended structure:

1. Current project status
2. Chronological entries, newest first or oldest first consistently
3. For each development entry:
   - Date
   - Objective
   - Files affected
   - Work performed
   - Tests and results
   - Decisions made
   - Issues or risks identified
   - Next step

The Development Log records **what happened and when**. Do not rewrite history to make an old decision appear to have been made earlier than it was.

### 11.4 Technical Reference

Recommended structure:

1. Purpose
2. Scope
3. Prerequisites
4. Concepts and terminology
5. Procedure or reference details
6. Examples
7. Troubleshooting
8. Safety considerations
9. Related documentation

## 12. Document Maintenance Rules

When updating an existing Markdown document:

1. Read the existing document before editing it.
2. Identify its current structure and preserve valid content.
3. Apply this guide to the affected sections.
4. Do not append content blindly if it belongs in an existing section.
5. Do not duplicate information already documented elsewhere.
6. Do not delete historical information, decisions, test results, or caveats without approval.
7. Distinguish confirmed implementation from proposals and future work.
8. Update the document's version and `Last Updated` date when appropriate.
9. Review the entire file after editing, not only the new section.
10. Provide the completed file and identify the meaningful changes.

### Documentation-only changes

A formatting cleanup must not silently change program behavior, technical meaning, project decisions, or historical facts.

If a content correction is needed, identify it separately from formatting changes.

## 13. Pre-Delivery Quality Checklist

Before delivering any Markdown file, verify:

- [ ] One clear document title is present.
- [ ] The approved document header is preserved where applicable.
- [ ] Heading levels follow the hierarchy.
- [ ] No headings are wrapped in bold markers.
- [ ] Paragraph spacing is consistent.
- [ ] Lists use consistent markers and indentation.
- [ ] Code blocks have language identifiers where possible.
- [ ] Code indentation and commands are preserved.
- [ ] Tables are readable and have header rows.
- [ ] Dates and version numbers are consistent.
- [ ] Proposed items are not presented as implemented.
- [ ] Historical decisions and test results have not been altered.
- [ ] No accidental HTML entities, malformed Markdown, or stray formatting remain.
- [ ] The complete document has been reviewed after editing.

## 14. Change Control

This guide is the default Markdown standard for AI Agent Build 0.1.

Changes to this guide should be deliberate:

1. Identify the problem with the current standard.
2. Propose the specific change.
3. Explain which documents or workflows it affects.
4. Obtain the project owner's approval.
5. Update the guide's version and date.
6. Apply the approved change consistently.

**Final rule:** Consistency matters more than decoration. Documentation should be easy to read, technically accurate, and maintainable.
