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

### Imbued mechanics ruling page
Clan, discipline, and creed coverage is now complete for the src-002 snapshot (47 clan pages across 5E-core / V5-playable / legacy / Laibon / antitribu; 38 discipline stubs including Imbued virtues; 7 Imbued creed stubs). The remaining known gap is a `wiki/rulings/` page for Imbued mechanics — True Faith, Convictions (including the Conviction card type's deck-slot role), imbuement process, and the targeting-restriction rules that prevent vampire-only effects from hitting Imbued minions. Every creed page currently flags this gap in its `## Related` section. Suggest sourcing from Black Chantry / krcg / VEKN rules articles on a future ingest.

## Resolved items

### [2026-04-17→2026-04-18] Card-page storage model — RESOLVED
See `docs/superpowers/specs/2026-04-18-card-storage-design.md`. Rolled out as src-002 (card-db snapshot) + schema v2 (four-layer arch, tightened problem-card trigger, new archetype/mechanic-index types).

### [2026-04-18] Clan & Discipline entity stubs — RESOLVED
**Context:** The wiki index had empty `entities/clans/` and `entities/disciplines/` sections. The 5E rulebook only provides the **names and icons** of the 5 core clans (Malkavian, Nosferatu, Toreador, Tremere, Ventrue) and 9 disciplines (Animalism, Auspex, Blood Sorcery, Celerity, Dominate, Fortitude, Obfuscate, Potence, Presence). No per-clan flavor, clan-specific discipline signatures, or discipline functional descriptions. Generating stubs purely from src-001 would produce near-empty pages.

**Resolution — two batches on 2026-04-18:**
- **Batch 1 (disciplines, commit d8c26a8):** src-002 (krcg vtes.json snapshot) landed. 9 discipline stubs filed in `wiki/entities/disciplines/` with card counts, in-clan mapping, and role examples.
- **Batch 2 (clans):** 5 clan stubs filed in `wiki/entities/clans/` (malkavian, nosferatu, toreador, tremere, ventrue) with crypt counts, superior-discipline frequencies, sect alignment, notable members, and archetype hooks. Cross-checked top-3 superior disciplines against the V5 signature set — all five clans match exactly.

**Follow-up (not blocking):** legacy clans frequently used in playgroup (Brujah, Gangrel, Banu Haqim, Lasombra, etc.) can be filed ad-hoc on demand.
