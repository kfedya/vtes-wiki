---
type: meta
tags: [backlog, design, todo]
sources: []
last_verified: 2026-04-18
status: draft
---

# Wiki Backlog

Forward-looking design questions and deferred work. Not bugs — open questions worth revisiting.

## Open questions

### [2026-04-18] Clan entity stubs (disciplines — DONE)
**Context:** The wiki index had empty `entities/clans/` and `entities/disciplines/` sections. The 5E rulebook only provides the **names and icons** of the 5 core clans (Malkavian, Nosferatu, Toreador, Tremere, Ventrue) and 9 disciplines (Animalism, Auspex, Blood Sorcery, Celerity, Dominate, Fortitude, Obfuscate, Potence, Presence). No per-clan flavor, clan-specific discipline signatures, or discipline functional descriptions. Generating stubs purely from src-001 would produce near-empty pages.

**Original decision:** defer clan/discipline entity pages until a proper source lands — either a krcg.org snapshot (per-discipline card lists + rulings) or a 5E set reference.

**Status update [2026-04-18]:** src-002 (krcg vtes.json snapshot) landed. **Discipline half is DONE** — 9 stubs filed in `wiki/entities/disciplines/` with card counts, in-clan mapping, and role examples. Still open: clan stubs (`wiki/entities/clans/`) for the 5E core 5 plus any legacy clans that frequently appear in playgroup discussion. Next batch will address clans.

**Trigger to revisit clans:** next scheduled batch, or when a playgroup discussion requires a clan page.

## Resolved items

### [2026-04-17→2026-04-18] Card-page storage model — RESOLVED
See `docs/superpowers/specs/2026-04-18-card-storage-design.md`. Rolled out as src-002 (card-db snapshot) + schema v2 (four-layer arch, tightened problem-card trigger, new archetype/mechanic-index types).
