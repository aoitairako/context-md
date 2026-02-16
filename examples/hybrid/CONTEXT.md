# CONTEXT.md - Fieldnote

> **project_identity**: local-first, privacy-respecting note app
> **version**: v1.0.0

## PROJECT_CONTEXT
```yaml
why: >
  Notes are thoughts made tangible. They belong to the person
  who wrote them — not to a server, not to a company, not to
  an algorithm deciding what's "relevant." Fieldnote exists
  because your second brain should live in your house, not
  someone else's cloud.
aims: >
  A note-taking app where the user's data never leaves their
  device unless they explicitly choose otherwise. Every feature
  is designed around the principle that the user owns their data
  completely and permanently.
```

## PROJECT_IDENTITY
```yaml
identity: >
  Local-first, privacy-respecting note application.
  Markdown-native. Works offline by default.
meaning: >
  "Local-first" is not a technical constraint — it's a promise.
  Every design decision prioritizes the user's autonomy over
  developer convenience. If a feature requires a server, it must
  also work without one.
```

## RELATIONSHIP
```yaml
ecosystem: >
  Part of the local-first movement (Ink & Switch, CRDTs, etc.).
  Inspired by Obsidian's vault model and Bear's simplicity.
  Interoperable with any tool that reads Markdown files.
dependencies: >
  Built on Markdown as the universal note format. Optional sync
  uses user-hosted infrastructure (e.g., Syncthing, NAS, git).
  No vendor lock-in by design — notes are plain files on disk.
```
