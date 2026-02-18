# CONTEXT.md - Forge

> **project_identity**: CI/CD pipeline that builds confidence, not just code
> **version**: v1.0.0

---

## PROJECT_CONTEXT

```yaml
why: |
  CI/CD pipelines are the heartbeat of modern software development.
  Every commit triggers a question: "Did I break something?"
  Most pipelines answer with pass/fail — a binary judgment.

  Forge exists because that question deserves a better answer.
  Not just "did it break?" but "what can you learn from this build?"

aims: |
  To create a CI/CD tool where every build outcome —
  success or failure — leaves the developer more confident
  and more informed than before.

inverse_exploration: |
  AGENTS.md defines Forge at the level of Reason (400):
  efficient builds, parallel execution, smart caching, clear logs.

  This CONTEXT.md explores from Love (500):
  - What if error messages were designed to teach, not blame?
  - What if build times were optimized for developer focus,
    not just speed?
  - What if the pipeline understood that a failing test at 2 AM
    affects a person differently than the same test at 10 AM?
  - What if "flaky test" wasn't a label but a signal that
    something in the system needs care?
```

---

## PROJECT_IDENTITY

```yaml
identity: "CI/CD pipeline that builds confidence"

consciousness_scope:
  current_level: "Reason (400)"
  current_expression: |
    Well-architected build system. Parallel execution.
    Dependency caching. Deterministic outputs. Clear error reporting.
  exploration_level: "Love (500)"
  exploration_expression: |
    Every interaction with the pipeline should leave the developer
    feeling supported. Error messages guide. Success messages affirm.
    The system serves the human, not the other way around.

meaning: |
  "Reason" optimizes the pipeline for correctness and efficiency.
  "Love" asks whether the pipeline respects the developer's experience.
  Both are necessary. AGENTS.md handles Reason. CONTEXT.md holds Love.
```

---

## RELATIONSHIP

```yaml
ecosystem:
  ci_cd: "GitHub Actions, GitLab CI, Jenkins — the existing landscape"
  developers: "The humans who wait for builds and read error messages"
  codebases: "The projects that depend on reliable, fast feedback loops"

hierarchy:
  above: "Developer wellbeing and sustainable engineering practices"
  this: "Forge — a CI/CD tool operating at Reason, exploring from Love"
  below: "Build scripts, test runners, deployment targets"

inverse_relationship: |
  Most CI/CD tools relate to developers as consumers of build output.
  Forge (at the CONTEXT.md level) relates to developers as people
  whose attention and confidence are finite, valuable resources.
```

---

*Example CONTEXT.md demonstrating the inverse context pattern*
*Reference: David R. Hawkins, "Power vs. Force" (1995)*
