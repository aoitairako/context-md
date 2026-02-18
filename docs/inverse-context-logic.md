# Inverse Context Logic

**A pattern for bounding CONTEXT.md's exploratory scope using consciousness levels.**

---

## The Concept

In the standard CONTEXT.md pattern, the file answers "Why does this project exist?" — a philosophical foundation that complements AGENTS.md's rules.

**Inverse Context Logic** takes this further. Instead of simply describing _why_ the project exists, CONTEXT.md actively explores what lies _beyond_ the project's defined scope — the possibilities that AGENTS.md deliberately excludes.

The logic flow:

```
Standard:  CONTEXT.md → AGENTS.md → Repository Documents  (narrowing)
Inverse:   CONTEXT.md = All Knowledge − AGENTS.md Scope    (expanding)
```

- **AGENTS.md** defines convergent thinking: "Within this boundary, find the best solution."
- **CONTEXT.md** (inverse) defines divergent thinking: "Beyond this boundary, what should we consider?"

---

## The Problem: Infinite Scope

If CONTEXT.md explores "everything outside AGENTS.md's scope," the search space is infinite. An AI instructed to "consider everything else" will either:

1. **Diverge endlessly** — generating tangential, low-value observations
2. **Freeze** — unable to prioritize in an unbounded space
3. **Default to noise** — surfacing connections that are technically related but practically useless

The inverse logic needs a **bounding framework** — something that limits the exploration space while keeping it genuinely expansive.

---

## The Solution: Consciousness Level Bounding

David R. Hawkins, M.D., Ph.D., developed the **Map of Consciousness** in _Power vs. Force_ (1995) — a hierarchical model of human awareness from 20 (Shame) to 1000 (Enlightenment). Each level represents a qualitatively different way of perceiving and engaging with reality.

Applied to software projects, this framework provides a natural bounding mechanism:

1. **Identify** the consciousness level at which the repository operates
2. **AGENTS.md** covers everything at and within that level
3. **CONTEXT.md** explores **one level above** — bounded but genuinely expansive

### Map of Consciousness Applied to Software

| Level | Name | Software Project Expression | Example |
|-------|------|---------------------------|---------|
| 200 | **Courage** | The project dares to exist. Experimental, MVP. | A weekend prototype, a first open-source release |
| 250 | **Neutrality** | Pragmatic and flexible. Non-dogmatic about implementation. | A utility library that solves one problem well |
| 310 | **Willingness** | Actively growing. Open to contribution and evolution. | A community-driven project accepting PRs |
| 350 | **Acceptance** | Embraces the ecosystem. Acknowledges limitations. | A tool designed to interoperate, not dominate |
| 400 | **Reason** | Well-architected. Logical. Data-driven decisions. | Production infrastructure, optimized systems |
| 500 | **Love** | Unconditional service. Empathetic, user-first design. | Tools designed around human wellbeing, not features |
| 540 | **Joy** | Creates delight. The experience transcends utility. | Software that makes users say "this is beautiful" |
| 600 | **Peace** | Complete and harmonious. Nothing to add, nothing to remove. | Mature, minimal software that simply _works_ |

> **Note**: Levels below 200 (Fear, Anger, Pride, etc.) represent projects driven by reactive forces — competition, ego, or avoidance. These projects can still benefit from CONTEXT.md, but the inverse logic is most effective at 200+, where projects operate from genuine purpose rather than reaction.

---

## How It Works

### Step 1: Identify the Repository's Consciousness Level

This is the most critical step. The precision of this identification determines the quality of CONTEXT.md's exploration.

Ask:

- **What motivates the project's core decisions?** (Logic → Reason. Empathy → Love. Flexibility → Neutrality.)
- **How does the project handle uncertainty?** (Avoidance → Fear. Analysis → Reason. Trust → Acceptance.)
- **What is the project's relationship with its users?** (Transactional → Reason. Empowering → Love.)

### Step 2: AGENTS.md Covers the Current Level

AGENTS.md defines rules, constraints, and behaviors that operate within the identified level. These are convergent: specific, actionable, bounded.

### Step 3: CONTEXT.md Explores One Level Above

CONTEXT.md doesn't repeat or contradict AGENTS.md. Instead, it asks: "What would this project look like if it operated from the _next_ level of awareness?"

| If the repo is at... | CONTEXT.md explores from... | The shift |
|----------------------|---------------------------|-----------|
| Courage (200) | Neutrality (250) | From "daring to exist" to "existing without attachment to outcomes" |
| Neutrality (250) | Willingness (310) | From "pragmatic flexibility" to "active growth and openness" |
| Willingness (310) | Acceptance (350) | From "growing eagerly" to "embracing the whole ecosystem" |
| Acceptance (350) | Reason (400) | From "working with others" to "optimizing the architecture" |
| Reason (400) | Love (500) | From "logical optimization" to "empathetic, human-centered design" |
| Love (500) | Joy (540) | From "serving users" to "creating delight and meaning" |

### The Set-Theoretic Model

```
Let U  = Universal knowledge
Let A  = AGENTS.md scope (repository's consciousness level and below)
Let L₊₁ = One consciousness level above A

CONTEXT.md = (U ∩ L₊₁) \ A
```

CONTEXT.md is not "everything except A" (which is infinite). It is "everything at the next consciousness level that A doesn't cover" — a bounded, meaningful expansion.

---

## Writing an Inverse-Context CONTEXT.md

Add a `consciousness_scope` field to PROJECT_IDENTITY:

```yaml
## PROJECT_IDENTITY
consciousness_scope:
  current_level: "Reason (400)"
  current_expression: "Well-architected, logical, data-driven decisions"
  exploration_level: "Love (500)"
  exploration_expression: |
    What if every design decision prioritized human experience
    over system efficiency?
```

Then, in PROJECT_CONTEXT, let the `aims` section include the exploratory perspective:

```yaml
## PROJECT_CONTEXT
why: |
  [Standard: why the project exists]

aims: |
  [Standard: what the project serves]

inverse_exploration: |
  Beyond the scope of AGENTS.md, this project considers:
  - [Perspective from one level above]
  - [Questions that the current level doesn't ask]
  - [Possibilities visible only from a higher vantage point]
```

---

## AI Behavior with Inverse Context Logic

When an AI reads both files:

1. **AGENTS.md** activates convergent reasoning: "Follow these rules, within this scope"
2. **CONTEXT.md** activates divergent reasoning: "Consider these broader perspectives"
3. **The combination** creates a dual-mode cognitive loop:
   - Explore possibilities from the higher level (divergent)
   - Ground them in the repository's actual constraints (convergent)
   - Output solutions that are both practical and inspired

This mirrors the human creative process: expand (brainstorm), then contract (implement). By encoding this cycle in two files, the AI naturally oscillates between perspectives.

### Behavior Predictions

| Scenario | Without Inverse CONTEXT.md | With Inverse CONTEXT.md |
|----------|---------------------------|------------------------|
| Edge case not covered by rules | AI stops or guesses | AI consults higher-level perspective |
| Feature request | Implements literally | Considers user intent beyond the request |
| Architecture decision | Optimizes for current metrics | Considers human impact alongside metrics |
| Code review | Checks correctness | Also evaluates whether the change serves the project's deeper purpose |

---

## Constraints and Risks

- **Over-exploration**: Without discipline, the AI may spend too much time in the divergent phase. The `consciousness_scope` field explicitly bounds this.
- **Vagueness**: Higher consciousness levels are more abstract. The `exploration_expression` should be concrete enough to be actionable.
- **Misidentification**: If the repository's consciousness level is identified incorrectly, the exploration will be misaligned. This is why Step 1 is the most critical.

---

## References

- Hawkins, D. R. (1995). _Power vs. Force: The Hidden Determinants of Human Behavior_. Hay House.
- CONTEXT.md Standard v1.0.0: [spec/CONTEXT_MD_v1.0.0.md](../spec/CONTEXT_MD_v1.0.0.md)

---

*Inverse Context Logic — A CONTEXT.md pattern*
*CC0 1.0 (Public Domain)*
