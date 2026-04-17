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

### [2026-04-18] Clan & Discipline entity stubs
**Context:** The wiki index has empty `entities/clans/` and `entities/disciplines/` sections. The 5E rulebook only provides the **names and icons** of the 5 core clans (Malkavian, Nosferatu, Toreador, Tremere, Ventrue) and 9 disciplines (Animalism, Auspex, Blood Sorcery, Celerity, Dominate, Fortitude, Obfuscate, Potence, Presence). No per-clan flavor, clan-specific discipline signatures, or discipline functional descriptions. Generating stubs purely from src-001 would produce near-empty pages.

**Decision for now:** defer clan/discipline entity pages until a proper source lands — either a krcg.org snapshot (per-discipline card lists + rulings) or a 5E set reference.

**Trigger to revisit:** first ingest of krcg snapshot, or when a playgroup discussion requires a clan/discipline page (e.g., "which Tremere rulings differ from other Blood Sorcery users?"). At that point, decide single-page-per-clan vs consolidated.

### [2026-04-17] Card-page storage model
**Context:** During stage 4 ingest (src-001 FAQ rulings) we pushed most card-specific rulings onto their mechanic's ruling page, and reserved `wiki/cards/` for only truly page-worthy cards (cross-mechanic or disputed). Card text itself isn't ingested yet — waiting on a krcg.org snapshot source.

**Questions to revisit:**
- What's the right criterion for "this card deserves its own page"? Current rule of thumb: cross-mechanic interaction or disputed ruling. Does that hold as the wiki grows?
- When krcg.org snapshots land, should every card referenced by a ruling auto-get a stub page (card text + link), or only the ones that accumulate their own rulings?
- How do we avoid fragmentation when a card's rulings end up spread across 3 different ruling pages? (e.g. Theft of Vitae touches strike-effects, damage, torpor.) Currently we duplicate across pages + cross-link; is there a better index structure?
- Should `wiki/cards/` nest by card type (`wiki/cards/combat/`, `wiki/cards/master/`) once it grows past ~20 pages?
- Is there a "card ruling digest" page worth building — a single flat index of all card rulings with deep links to where they live?

**Trigger to revisit:** when the wiki has ≥15 card pages, or when we ingest the first krcg.org snapshot.

## Resolved items

_(none yet)_
