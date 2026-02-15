# CONTEXT.md Specification v1.0.0

**Status**: Draft
**Date**: 2026-02-15
**Author**: [aoitairako](https://github.com/aoitairako)
**License**: CC0 1.0 (Public Domain)

---

## 1. Overview

CONTEXT.md is a markdown file placed at the root of a project that defines **why** the project exists. It is the highest-level documentation file, complementing existing standards:

```
CONTEXT.md (Why)  — Philosophy, purpose, field of meaning
AGENTS.md  (What) — AI agent instructions (OpenAI/AAIF standard)
README.md  (Doc)  — Human-readable documentation
CLAUDE.md  (How)  — Claude Code specific settings (Anthropic)
```

## 2. File Location

CONTEXT.md MUST be placed at the **root directory** of a project, alongside other root-level documentation files.

```
project-root/
├── CONTEXT.md     ← REQUIRED: at project root
├── AGENTS.md      ← optional
├── README.md      ← conventional
├── CLAUDE.md      ← optional
└── ...
```

## 3. File Format

- MUST be valid GitHub-flavored Markdown
- MUST use `.md` extension
- MUST use uppercase filename: `CONTEXT.md`
- SHOULD use YAML code blocks for machine-readable sections
- SHOULD use Python code blocks when executable specifications are needed
- MAY include plain markdown prose for philosophical content

## 4. Required Sections

Every CONTEXT.md MUST include these three sections:

### 4.1 PROJECT_CONTEXT

Answers: **"Why does this project exist?"**

```yaml
## PROJECT_CONTEXT
why: "The philosophical reason for this project's existence"
aims: "What the project ultimately serves or enables"
```

- MUST explain the project's reason for being
- MUST describe the ultimate aim or purpose
- SHOULD NOT include implementation details
- SHOULD NOT include setup instructions

### 4.2 CONSCIOUSNESS_LEVEL

Answers: **"At what level of awareness does this project operate?"**

```yaml
## CONSCIOUSNESS_LEVEL
level: "A description of the project's awareness level"
meaning: "What this level means for the project's design and behavior"
```

- MUST describe the project's level of awareness or sophistication
- MAY use numerical scales, qualitative descriptions, or domain-specific frameworks
- MAY use any framework that fits the project's domain

### 4.3 RELATIONSHIP

Answers: **"How does this project relate to the broader ecosystem?"**

```yaml
## RELATIONSHIP
ecosystem: "Related projects, standards, and communities"
dependencies: "What this project builds upon or serves"
```

- MUST describe the project's position in a larger context
- SHOULD reference related projects or standards
- SHOULD clarify what the project depends on and what depends on it

## 5. Optional Sections

A CONTEXT.md MAY include additional sections:

| Section | Purpose |
|---------|---------|
| `PHILOSOPHICAL_BASIS` | Deeper philosophical grounding |
| `DESIGN_PRINCIPLES` | How philosophy translates to design |
| `INDUSTRY_CONTEXT` | Position in the broader industry |
| `HIERARCHY` | Relationship to parent/child contexts |
| `SOURCES` | References and citations |

## 6. Boundary Rules

CONTEXT.md MUST NOT contain:

| Content Type | Belongs In |
|-------------|-----------|
| Setup instructions | README.md |
| AI agent instructions | AGENTS.md |
| Tool-specific configuration | CLAUDE.md, .editorconfig, etc. |
| API documentation | README.md or dedicated docs/ |
| Code examples | README.md or examples/ |
| Command-line usage | README.md |
| Changelog | CHANGELOG.md |

**Boundary test**: Every statement in CONTEXT.md should answer "Why?" — not "What?" or "How?"

## 7. Machine Readability

- YAML code blocks SHOULD be parseable by standard YAML parsers
- Section headers (##) SHOULD follow a consistent naming pattern
- The file SHOULD be readable by any AI tool that processes markdown
- No tool-specific syntax or extensions are required

## 8. Header Format

The file SHOULD begin with a metadata block:

```markdown
# CONTEXT.md - [Project Name]
<!-- Optional: version, date, standard reference -->

> **consciousness_level**: [level description]
> **version**: v[X.Y.Z]
```

## 9. Versioning

- CONTEXT.md files SHOULD include a version number
- Version follows Semantic Versioning (MAJOR.MINOR.PATCH)
- MAJOR: Fundamental change in project philosophy
- MINOR: New sections or expanded purpose
- PATCH: Clarifications and corrections

## 10. Interoperability

CONTEXT.md is designed to work with:

- Any AI tool that reads markdown (Claude, GPT, Gemini, Cursor, Continue, etc.)
- Any CI/CD system that can parse files
- Any documentation system that processes markdown
- Existing file standards (AGENTS.md, README.md, CLAUDE.md)

No special tooling, SDK, or runtime is required.

## 11. Adoption

To adopt CONTEXT.md:

1. Create a `CONTEXT.md` file at your project root
2. Include the three required sections (PROJECT_CONTEXT, CONSCIOUSNESS_LEVEL, RELATIONSHIP)
3. Optionally reference it from AGENTS.md: `context: CONTEXT.md`
4. Optionally add the `context-md` topic to your GitHub repository

## 12. Content vs Context

The core distinction behind CONTEXT.md:

- **Content**: What appears — code, data, features, files
- **Context**: The field of meaning in which content exists — purpose, philosophy, awareness

Traditional project files describe Content (what the project does). CONTEXT.md describes Context (why the project exists and what meaning it creates).

> The same content, placed in a different context, changes meaning fundamentally.

---

*CONTEXT.md Specification v1.0.0*
*CC0 1.0 (Public Domain)*
