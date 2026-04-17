---
type: entity
tags: [discipline, 5e-core, presence, bleed, votes, combat]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Presence

**Code:** `[pre]` basic / `[PRE]` superior

## Overview

Presence is the discipline of charisma and supernatural allure — drawing votes, swaying mortals, and walking out of combat unharmed. It is the main **vote-boost** discipline and also a staple bleed-bounce / bleed-bypass discipline for Toreador/Ventrue/Brujah archetypes [src-001 p. 53]. It is one of the nine 5E core disciplines.

## In-clan

Primary in-clan discipline for (5E-era printings): **Ventrue**, **Toreador**, **Brujah**, **Ministry** (and their antitribu variants).
Also common on: Guruhi, Ravnos.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[pre]` (basic or superior): **91**
- Crypt vampires with `[pre]` or `[PRE]`: **664**

## Typical card roles

- Vote-count boost — [Bewitching Oration](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Bewitching%20Oration), [Awe](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Awe), [Voter Captivation](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Voter%20Captivation).
- Combat-ends / walk-away — [Majesty](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Majesty).
- Bleed increase — [Aire of Elation](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Aire%20of%20Elation).
- Pool-gain action — [Enchant Kindred](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Enchant%20Kindred).
- Charm-based intercept / bounce — [Enchanting Gaze](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Enchanting%20Gaze).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "pre")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "pre")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[voting]] — Presence is the main way to multiply votes.
- [[post-combat-effects]] — Voter Captivation timing after successful bleed.
- [[bleed]] — Aire of Elation boosts bleed.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
