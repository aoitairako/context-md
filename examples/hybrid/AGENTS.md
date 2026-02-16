# AGENTS.md - Fieldnote

## Rules

```yaml
rules:
  - rule: "Never send note content to external APIs"
    why: "See CONTEXT.md → PROJECT_CONTEXT: user's data never leaves their device"

  - rule: "All features must work offline"
    why: "See CONTEXT.md → PROJECT_CONTEXT: every feature works without a server"

  - rule: "Default storage is the user's home directory"
    why: "See CONTEXT.md → PROJECT_IDENTITY: local-first is a promise, not a constraint"

  - rule: "Sync must be opt-in and use user-hosted infrastructure"
    why: "See CONTEXT.md → PROJECT_IDENTITY: user autonomy over developer convenience"
```

## Context

```yaml
context: CONTEXT.md
pattern: bridge
description: >
  Each rule above includes a why: annotation pointing back to
  CONTEXT.md. This gives AI tools both the rule and the reasoning
  behind it, enabling better judgment on edge cases.
```
