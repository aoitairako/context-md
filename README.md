<!-- If you're reading the raw markdown instead of the rendered page, you're exactly the kind of person who'd write a CONTEXT.md. -->

# CONTEXT.md

**The one file only you can write.**

> README.md ✓ &nbsp; AGENTS.md ✓
> *...One more thing.*

---

## The Problem

A new team member joins your project. They ask: "Why does this project exist?"

You open the README. Setup instructions, API docs, usage examples — everything about *what* the project does. But nothing about *why*.

You check the wiki. Last updated: 2019. The project started in 2021.

Your project has files that describe **what** it does:

- `README.md` — what the project is (for humans)
- `AGENTS.md` — what AI should do (for AI agents)
- `CLAUDE.md`, `.cursorrules`, etc. — how specific tools should behave

But no standard file answers the most fundamental question: **Why does this project exist?**

## The Solution

**CONTEXT.md** — a single markdown file at the root of any project that answers that question.

- **Why** the project exists (philosophy, purpose)
- **What** the project's identity is
- **How it relates** to the broader ecosystem

```
your-project/
├── CONTEXT.md     ← Why (you are here)
├── AGENTS.md      ← What (AI agent instructions)
├── README.md      ← Doc (often skipped)
├── CLAUDE.md, etc. ← How (tool-specific settings)
└── src/            ← (finally, some actual code)
```

## Quick Start

Every new tool means config files, environment variables, dependencies, a mass on your `node_modules` that rivals a small black hole, and a README you'll read later. *(You won't.)*

CONTEXT.md needs two things: Markdown, and your intention. You already have both.

````markdown
# CONTEXT.md - My Project

## PROJECT_CONTEXT
```yaml
why: "Why this project exists"
aims: "What it ultimately serves"
```

## PROJECT_IDENTITY
```yaml
identity: "What this project is and how it sees itself"
meaning: "What this means for design decisions"
```

## RELATIONSHIP
```yaml
ecosystem: "How this project relates to others"
dependencies: "What it builds upon"
```
````

That's it. If your AI can read markdown — and it can — it now understands your project's purpose.

## Why CONTEXT.md?

### Content vs Context

| | Content | Context |
|--|---------|---------|
| Definition | What appears (code, data, features) | The meaning behind it (purpose, intention) |
| Project files | README, AGENTS, source code | **CONTEXT.md** |
| Question answered | "What does this do?" | "Why does this exist?" |
| **Analogy** | **`git commit -m "fix"`** | **What actually broke and why** |

Two developers can write the exact same function. One is building a toy. The other is building infrastructure that thousands depend on. The code is identical. The *context* is everything.

Imagine setting sail across the ocean. Your compass is one degree off — barely noticeable at the start. A thousand miles later, you're in a completely different place. Your project's "why" works the same way. A small difference in purpose early on leads to vastly different outcomes down the road.

### The One File AI Can't Write

AI writes code. Generates tests. Drafts documentation. Even fixes bugs (and occasionally introduces new ones — we've all been there).

As a Content professional, AI is reshaping how we build software.

But Context — the "why" — is something AI can't create.

In *The Little Prince*, the Fox says: *"What is essential is invisible to the eye."*

AI handles everything visible — code, data, files, documentation. But the essential part — *why* this project exists — is invisible. It lives in the mind of the person who started it. AI can't generate it. Only you can write it down.

"But wait — AI *can* generate a CONTEXT.md. I just tried it."

Sure it can. AI could write Ruby's CONTEXT.md: *"A dynamic, open-source programming language focused on simplicity and productivity."* Technically accurate. But Matz didn't create Ruby for "simplicity and productivity." He created it because he wanted programmers to be happy. That's not a feature request — it's a wish. AI can describe the language. Only Matz could describe the feeling behind it.

The same goes for your project. AI can infer what it does from your code, your commits, your README. But the spark that made you start — that's not in the data.

In a world where AI can generate any codebase, the projects that stand out won't be the ones with the best code. They'll be the ones with the clearest purpose. People don't contribute to repositories. They contribute to something they believe in.

CONTEXT.md is where that "something" becomes words.

*(Yes, this repo was built with AI assistance. An AI helped write a standard about the one thing AI can't write. That's exactly the point.)*

### Beyond the Repository Boundary

"I'm an engineer who improves ad click-through rates by 0.3%" tells you what someone does.
"I became an engineer because I want to build apps that make kids say 'again! again!'" tells you why.

Same person. Completely different impression.

Most project files describe what's *inside* the repository. CONTEXT.md describes where the project sits in the *larger world*. An AI with a CONTEXT.md doesn't just know what to do — it knows *why it matters*.

### The Bridge Pattern

Why not just put your philosophy in AGENTS.md?

Because instruction files speak in rules: *do this, don't do that, use this format.* They're precise, actionable, and machine-readable. That's their job.

Philosophy doesn't work that way. "We believe the user owns their data" isn't a rule — it's a compass bearing. Put it next to `"respond in JSON format"` and the AI treats them as equals. One is a hard constraint. The other is soft guidance. The AI can't tell the difference, and you've just added noise to your rulebook — or worse, created a conflict.

CONTEXT.md solves this by separation:

```
CONTEXT.md (Philosophy)  → soft guidance, direction, no concrete answers
AGENTS.md  (Rules)       → hard constraints, specific actions
```

Both loaded by the AI. Different purposes. No conflict.

When the AI reads your rules *and* your philosophy, something interesting happens. It encounters an edge case your rules don't cover — and instead of stopping or guessing, it has a compass. It might even spot something *you* missed: a request that technically follows your rules but quietly violates your principles. A blind spot you didn't know you had.

That's the bridge: CONTEXT.md gives the AI a perspective your instruction files can't express. Not answers — *direction*.

You can strengthen the connection with `why:` annotations in your instruction files:

```yaml
# In your AGENTS.md or CLAUDE.md
rules:
  - rule: "Never store user data in external services"
    why: "See CONTEXT.md → PROJECT_CONTEXT: user owns their data"

  - rule: "All APIs must support offline mode"
    why: "See CONTEXT.md → DESIGN_PRINCIPLES: persistence over convenience"
```

These pointers connect specific rules to specific philosophies. The AI doesn't just follow the rule — it understands the reasoning, and can apply that reasoning to situations you didn't anticipate.

## Specification

See [spec/CONTEXT_MD_v1.0.0.md](spec/CONTEXT_MD_v1.0.0.md) for the formal specification. It's shorter than most cookie consent popups, and considerably more useful.

## Examples

| Example | Description |
|---------|-------------|
| [minimal](examples/minimal/) | The bare minimum. Three sections. Copy and go. |
| [ai-project](examples/ai-project/) | AI/ML project with a tool ecosystem |
| [personal-data](examples/personal-data/) | Privacy-focused data management |
| [hybrid](examples/hybrid/) | The bridge pattern: AGENTS.md rules with `why:` pointers to CONTEXT.md |

## File Hierarchy

```
CONTEXT.md (Why)     — Philosophy, purpose, the field of meaning
    ↓ contains
AGENTS.md (What)     — Instructions for AI agents
    ↓ alongside
README.md (Doc)      — Human-readable documentation
    ↓ alongside
Tool config (How)    — CLAUDE.md, .cursorrules, etc.
```

CONTEXT.md sits at the top. Not because it's bossy — because "why" is the question that gives meaning to everything below it. Without it, you're just typing.

## Design Principles

### Checklist

| # | Principle | Ask yourself |
|---|-----------|-------------|
| 1 | **Why** | Are you writing Context (why), not Content (what)? |
| 2 | **Foundation** | Does it give meaning and coherence to all other project files? |
| 3 | **Standalone** | Can someone understand your project's purpose from this file alone? |
| 4 | **Timeless** | If the implementation changes, does this "why" still hold? |
| 5 | **Simple** | Is it expressed in the simplest possible words? |
| 6 | **Beyond** | Does it show where the project sits in the larger world, not just the repo? |
| 7 | **Universal** | Is it equally valuable to a human and an AI reading it? |

### What NOT to include

Nobody writes a shopping list in their diary. Wrong place.

Same idea: if a sentence answers "what" or "how" instead of "why," it belongs in a different file.

- ❌ "To install, run `npm install`" — That's a README.
- ❌ "Use Python 3.12 or higher" — README again.
- ❌ "AI should respond in JSON format" — That's an AGENTS.md.
- ✅ "We built this because..." — Now you're writing Context.

## Prior Art

| Project | Approach | Focus |
|---------|----------|-------|
| [llm-context-md](https://github.com/the-michael-toy/llm-context-md) | Hierarchical CONTEXT.md files throughout directories | Technical context (What): architecture, conventions |
| [codebase-context-spec](https://github.com/Agentic-Insights/codebase-context-spec) | `.context/` directory with structured docs (archived) | Architecture documentation (What): design decisions |
| [ADR](https://adr.github.io/) (Architecture Decision Records) | Individual records per technical decision | Decision rationale (What was decided and why) |

These projects focus on **What** — technical context about code and decisions.
This project focuses on **Why** — purpose and meaning that no technical context provides.

ADR and CONTEXT.md are particularly complementary. ADR looks backward: "We chose PostgreSQL because..." — reasoning from a decision already made. CONTEXT.md looks forward: "This project exists because..." — purpose that precedes any decision. A healthy project can check its ADRs against its CONTEXT.md: if the decisions no longer align with the purpose, something drifted.

They solve different problems. A project can use all of them.

## Tooling

### Validate

```bash
python3 tools/validate.py CONTEXT.md
```

### GitHub Action

```yaml
- uses: aoitairako/context-md@v1
```

No dependencies. No configuration. Just the standard.

## FAQ

**Q: Can AI write my CONTEXT.md for me?**
A: Sure. But then ask yourself: why did you just delegate your "why" to an AI?

**Q: What if I don't know my project's "why"?**
A: Then you have a bigger problem than documentation.

**Q: Is this just a README with extra steps?**
A: Is a love letter just a letter with extra feelings?

## Contributing

Contributions welcome. Open an issue, send a PR, or just put a CONTEXT.md in your own project. That's contributing too.

If you adopt it, consider adding the topic `context-md` to your GitHub repository.

If you don't adopt it, no hard feelings. Existential questions take time.

## License

[CC0 1.0 (Public Domain)](LICENSE) — No rights reserved. No attribution required. Use it however you want.

---

Every other file in your project, AI can help you write.
This one? I can't.

Actually, let me try: *"This project exists to deliver value through innovative solutions."*
Perfect, right? ...Right?

*One small file for a project. One giant leap for documentation.*

---

*CONTEXT.md Standard v1.0.0 — Created: 2026-02-15*
*Author: [aoitairako](https://github.com/aoitairako)*
*(Humor setting: 75%)*
