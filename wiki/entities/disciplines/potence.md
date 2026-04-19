---
type: entity
tags: [discipline, 5e-core, potence, strength, combat]
sources: [src-001, src-002]
last_verified: 2026-04-19
status: verified
---

# Potence

**Code:** `[pot]` basic / `[POT]` superior

## Overview

Potence is the discipline of supernatural strength. It boosts **hand-strike damage** and supplies close-range grappling tools that shut down opposing combat cards and equipment [src-001 p. 53]. Most Potence cards are combat cards; action-modifier Potence is a smaller set of intimidation/leverage effects. It is one of the nine 5E core disciplines.

## In-clan

Primary in-clan discipline for (5E-era printings): **Brujah**, **Nosferatu**, **Lasombra**, **Giovanni** (and their antitribu variants).
Also common on: Gargoyle, Guruhi.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[pot]` (basic or superior): **67**
- Crypt vampires with `[pot]` or `[POT]`: **613**

## Typical card roles

Verified against card-db snapshot 2026-04-18 [src-002].

- Hand-strike damage boost — [Undead Strength](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Undead%20Strength) (+1/+2 damage on hand-strike or melee), [Torn Signpost](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Torn%20Signpost) (combat card, strength 2/3 for the combat; printed in 5E Anarch & NB3).
- Grapple / range-lock — [Immortal Grapple](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Immortal%20Grapple) (restricts the round to hand-strikes only).
- Intimidation action modifier — [Unthinkable Humiliation](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Unthinkable%20Humiliation) (blockers burn 1 blood/life; superior also -1 intercept).
- Anti-block action-canceler — [Tangle Atropos' Hand](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Tangle%20Atropos%27%20Hand) (cancels the action and unlocks the acting vampire when a minion attempts to block; superior [TEM] variants also retrieve the card and grant next-action stealth).
- Dual-mode maneuver + post-block tempo — [Shadow Boxing](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Shadow%20Boxing) (combat = close maneuver or continue-combat press; action modifier after block = +1 bleed / +2 press).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "pot")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "pot")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[strike]] — hand-strike and strike-effect rules.
- [[damage-resolution]] — Potence pumps strike damage.
- [[entities/card-types/combat-card]] — most Potence cards are combat cards.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
