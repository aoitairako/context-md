# CONTEXT.md - The CONTEXT.md Standard
<!-- CONTEXT.md Standard v1.0.0 -->
<!-- Updated: 2026-02-15 -->
<!-- This file is self-referential: the spec eats its own dogfood -->

> **project_identity**: Meta — a standard that defines itself
> **version**: v1.0.0

---

## PROJECT_CONTEXT

```yaml
why: |
  Software projects have files that describe WHAT they do (README.md),
  WHAT AI should do (AGENTS.md), and HOW tools should behave (CLAUDE.md, .cursorrules, etc.).

  But no file answers the most fundamental question:
  WHY does this project exist?

  CONTEXT.md fills this gap. It defines the philosophical foundation,
  purpose, and meaning of a project — readable by both humans and AI.

  The distinction between Content and Context is key:
  - Content = what appears (code, data, features)
  - Context = the field of meaning in which content exists (purpose, philosophy)

  CONTEXT.md is the Context layer for any project.

aims: |
  To establish CONTEXT.md as a universal file convention that:
  1. Any project can adopt (zero cost, place a file)
  2. Any AI can read (markdown, AI-agnostic)
  3. Transcends the repository boundary (gives AI a broader perspective)
  4. Complements existing standards (AGENTS.md, README.md, CLAUDE.md, .cursorrules, etc.)
```

---

## PROJECT_IDENTITY

```yaml
identity: "Meta — a standard that defines itself"

meaning: |
  This repository is the specification for CONTEXT.md.
  The CONTEXT.md you are reading right now IS the standard in action.
  It demonstrates what every project's CONTEXT.md should contain:
  why the project exists, what it aims for, and how it relates to
  the broader ecosystem.
```

---

## RELATIONSHIP

```yaml
ecosystem:
  agents_md: "AGENTS.md (OpenAI/AAIF) — What AI should do"
  readme_md: "README.md — What the project is (for humans)"
  tool_config: "CLAUDE.md, .cursorrules, etc. — How specific tools should behave"
  context_md: "CONTEXT.md — WHY the project exists (this standard)"

hierarchy: "CONTEXT.md (Why) > AGENTS.md (What) > README.md (Doc) > Tool config (How)"

complementary: |
  CONTEXT.md does not replace any existing standard.
  It adds the missing "Why" layer that none of them cover.
  Projects can adopt CONTEXT.md incrementally — it works alongside
  whatever documentation standards are already in place.
```

---

## FOUNDATION

```yaml
foundation:
  project: "The Context Foundation"
  path: "~/context/"
  domain: "thecontextfoundation.org"
  relationship: "The file convention born from The Context Foundation's philosophy"
  future_home: "github.com/the-context-foundation/context-md"
  synced: "v5.0.0"
```

---

*CONTEXT.md Standard v1.0.1*
*The Context Foundation: ~/context/CONTEXT.md v5.0.0*
*Self-referential: this file IS the standard it defines*
