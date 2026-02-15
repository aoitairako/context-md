# CONTEXT.md - Personal Data Vault

> **project_identity**: Content given meaning by Context
> **version**: v1.0.0

## PROJECT_CONTEXT

```yaml
why: |
  Personal data — health records, legal documents, family information —
  is the most valuable digital asset a person owns. Yet it is often
  scattered across cloud services, local folders, and email attachments
  with no coherent structure or protection strategy.

  This project exists because personal data deserves the same
  architectural care as any production system. Structure IS protection.
  Organization IS preservation.

aims: |
  To create a structured, privacy-first repository for personal and
  family information that:
  - Survives device loss (backed by canonical source)
  - Protects sensitive data at appropriate security levels
  - Provides a single source of truth for life administration
```

## PROJECT_IDENTITY

```yaml
identity: "Content given meaning by Context"

meaning: |
  The data in this project is Content — facts, documents, records.
  Raw data has no inherent meaning. What gives it meaning is Context:

  - The STRUCTURE (how files are organized) is Context
  - The PROTECTION (which data gets what security level) is Context
  - The PURPOSE (why we preserve this data) is Context

  We protect personal data not out of fear, but out of care.
  Privacy is an act of meaning-making, not just security.
```

## RELATIONSHIP

```yaml
ecosystem:
  storage: "Canonical source (NAS, encrypted backup, or trusted storage)"
  tools: "AI assistants can help organize but must respect privacy boundaries"
  legal: "Compliance with data protection principles (GDPR, etc.)"

depends_on:
  - "Reliable storage infrastructure"
  - "Encryption for sensitive categories"
  - "Backup strategy with multiple layers"

serves:
  - "The individual and their family"
  - "Future self — life administration across decades"
```

---

*Example CONTEXT.md for personal data management*
