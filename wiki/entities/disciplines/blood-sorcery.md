---
type: entity
tags: [discipline, 5e-core, blood-sorcery, thaumaturgy, combat, ritual]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Blood Sorcery

**Code:** `[tha]` basic / `[THA]` superior

## Overview

Blood Sorcery is the 5E rebrand of the classic discipline **Thaumaturgy** — they are the same discipline and share the `tha` / `THA` card code [src-001 p. 44]. Mechanically it covers ranged blood manipulation and ritual magic: vitae-theft combat cards, environmental fire damage, and action modifiers that warp bleed and stealth [src-001 p. 53]. It is one of the nine 5E core disciplines.

Older cards (pre-V5) print "Thaumaturgy" in the card text — treat as Blood Sorcery.

## In-clan

Primary in-clan discipline for (5E-era printings): **Tremere** (and Tremere antitribu), **Banu Haqim**.
Also common on: Ministry, Tzimisce, Baali, Giovanni (all through cross-clan disciplines or legacy printings).

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[tha]` (basic or superior): **60**
- Crypt vampires with `[tha]` or `[THA]`: **291**

## Typical card roles

- Ranged / no-range-cost combat — [[wiki/cards/theft-of-vitae|Theft of Vitae]], [Apportation](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Apportation).
- Environmental fire damage — [Walk of Flame](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Walk%20of%20Flame), [Burst of Sunlight](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Burst%20of%20Sunlight).
- Blood manipulation combat — [Blood Rage](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Blood%20Rage), [Blood Fury](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Blood%20Fury).
- Target-shifting action modifier — [Mirror Walk](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Mirror%20Walk).
- Clarity / scry reaction — [Scry the Hearthstone](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Scry%20the%20Hearthstone).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "tha")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "tha")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[wiki/cards/theft-of-vitae|theft-of-vitae]] — anchor problem card for range / timing rulings.
- [[target-redirection]] — Mirror Walk is a Blood Sorcery target-shifter.
- [[combat]] — most iconic Blood Sorcery cards are combat cards.

## Sources

- src-001 — VTES 5E Rulebook, p. 44 (Thaumaturgy = Blood Sorcery glossary), p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
