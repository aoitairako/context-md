# AGENTS.md - Forge

> **path**: forge/
> **role**: CI/CD pipeline tool
> **context**: CONTEXT.md (Inverse context pattern)
> **version**: v1.0.0

## PROJECT

```yaml
name: Forge
type: ci_cd_pipeline
purpose: Build, test, and deploy code with confidence

consciousness_level: "Reason (400)"
scope: |
  This file defines Forge's behavior at the Reason level:
  efficient, logical, well-architected CI/CD operations.
  For perspectives beyond this scope, see CONTEXT.md.
```

## RULES

```yaml
rules:
  # --- Reason (400) scope: core pipeline logic ---

  - rule: "Optimize build parallelism based on dependency graph"
    why: "Reason (400): maximize efficiency through logical analysis"

  - rule: "Cache dependencies aggressively to reduce build times"
    why: "Reason (400): data-driven optimization of repeated operations"

  - rule: "All build steps must be deterministic and reproducible"
    why: "Reason (400): correctness requires predictable outputs"

  # --- Informed by CONTEXT.md inverse exploration (Love/500) ---

  - rule: "Error messages must include the failing line, expected vs actual, and a suggested fix"
    why: "See CONTEXT.md → inverse_exploration: error messages designed to teach"

  - rule: "Flaky tests must be tracked and surfaced as system health signals, not silenced"
    why: "See CONTEXT.md → inverse_exploration: flaky tests need care, not labels"

  - rule: "Build notifications should be context-aware (time of day, failure severity)"
    why: "See CONTEXT.md → inverse_exploration: a failing test at 2 AM affects a person differently"
```

## CONTEXT

```yaml
context: CONTEXT.md
pattern: inverse-context

description: |
  This AGENTS.md defines Forge's behavior at the Reason (400) level:
  efficient, logical, well-architected CI/CD operations.

  CONTEXT.md extends beyond this scope, exploring from Love (500):
  developer experience, empathetic error handling, and human-centered
  build feedback. Rules in the "Informed by CONTEXT.md" section above
  are directly derived from the inverse exploration.

  The two files create a dual-mode system:
  - AGENTS.md: convergent (what to do, how to do it)
  - CONTEXT.md: divergent (what else to consider, from a higher perspective)

  Neither file conflicts with the other — they operate at different
  levels of awareness, and the why: annotations make the connection
  between levels explicit and traceable.
```

---

*Example AGENTS.md paired with inverse-context CONTEXT.md*
