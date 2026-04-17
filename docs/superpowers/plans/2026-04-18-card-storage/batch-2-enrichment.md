# Batch 2 — Selective krcg-ruling enrichment (OPTIONAL, INTERACTIVE)

**Status:** optional. Do NOT run via unattended orchestrator. Requires user judgment on what to surface.

**Goal:** selectively surface krcg `rulings[]` entries into mechanic pages when they add material edge cases beyond the rulebook.

**Depends on:** Batch 0 and batches 1a–1d (so links and formatting are already consistent).

**Commit subject:** `enrich: src-002 krcg rulings — <mechanic>` (per mechanic)

## Why interactive

Deciding whether a krcg ruling "adds material edge case beyond the rulebook" is a judgment call:

- The rulebook covers most baseline cases.
- Some krcg rulings are trivial ("yes the card does what it says") — not worth surfacing.
- Some are genuine edge cases ("what happens if both players play Theft of Vitae simultaneously") — worth a mechanic-page FAQ entry.
- Some reveal playtest disagreements that turned into official rulings — valuable but need careful tier-3 citation.

An autonomous agent will either over-surface (filling pages with noise) or under-surface (missing the valuable stuff).

## Recommended workflow (with user)

For each high-traffic mechanic page:

1. Identify cards most referenced on the page.
2. For each card, read its `rulings[]` from `card-db`.
3. Present the rulings in chat, grouped by category: (a) rulebook-redundant (skip), (b) clarification / edge case (candidate), (c) contradiction with rulebook (flag for `## Conflicting Rulings`).
4. User confirms which to surface.
5. Add a new `## Card-Level Rulings (krcg)` section to the mechanic page with user-approved entries. Each entry cites src-002 and preserves the original reference label from krcg (e.g., `[RTR 20010711]`).
6. If any ruling contradicts the rulebook, follow the "Conflicting Rulings" protocol in CLAUDE.md.
7. Bump `last_verified`.

## Suggested mechanic pages to consider

In decreasing priority:

- `wiki/rulings/bleed.md`
- `wiki/rulings/combat.md`
- `wiki/rulings/block-resolution.md`
- `wiki/rulings/strike.md`
- `wiki/rulings/strike-effects.md`
- `wiki/rulings/damage-resolution.md`
- `wiki/rulings/politics.md`
- `wiki/rulings/voting.md`
- `wiki/rulings/diablerie.md`
- `wiki/rulings/torpor.md`
- `wiki/rulings/target-redirection.md`
- `wiki/rulings/stealth-modifiers.md`

## Commit cadence

One commit per mechanic page to keep history fine-grained.

## Out of scope for this batch

- Do NOT create new card pages. If a card repeatedly shows up as ruling-rich, flag it for a problem-card promotion discussion instead.
- Do NOT import translations or flavor text.
- Do NOT add rulings purely from community discussion — only krcg-embedded `rulings[]` with valid reference labels (RTR, LSJ, ANK, krcg).
