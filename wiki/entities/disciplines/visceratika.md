---
type: entity
tags: [discipline, legacy, visceratika, gargoyle, stone]
sources: [src-001, src-002]
last_verified: 2026-04-19
status: verified
---

# Visceratika

**Code:** `[vis]` basic / `[VIS]` superior

## Overview

Visceratika is the legacy **Gargoyle** discipline of stone — merging with rock, growing stony armour, and turning rubble into weapons. Mechanically a defence-first combat pool: armour, damage-prevention, and strength-of-stone strikes, plus a handful of castle-flavoured reactions. A small, single-clan-flavoured discipline concentrated on Gargoyle crypt cards.

> Note: the three-letter code `vis` refers specifically to **Visceratika** (vampire discipline), not to the Imbued virtue **Vision**. Vision uses a different shard of cards and is handled separately.

## In-clan

Primary in-clan discipline for (legacy printings): **Gargoyle**.
No other clans carry Visceratika in the current snapshot.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[vis]` (basic or superior): **17**
- Crypt vampires with `[vis]` or `[VIS]`: **23**

## Typical card roles

- Stone armour / damage-prevent combat — [Rockheart](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Rockheart), [Stonestrength](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Stonestrength), [Bond with the Mountain](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Bond%20with%20the%20Mountain), [Flow Within the Mountain](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Flow%20Within%20the%20Mountain).
- Stone-based strikes — [Lead Fist](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Lead%20Fist), [Stone Quills](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Stone%20Quills), [Brick by Brick](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Brick%20by%20Brick), [Collapse the Arches](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Collapse%20the%20Arches), [Crawling Chamber](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Crawling%20Chamber).
- Stone-meld / terrain actions — [Armor of Terra](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Armor%20of%20Terra), [Children of Stone](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Children%20of%20Stone), [Ensconced](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Ensconced).
- Scry / castle reactions — [Scry the Hearthstone](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Scry%20the%20Hearthstone), [Voices of the Castle](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Voices%20of%20the%20Castle).
- Stealth / camouflage modifiers — [Skin of the Chameleon](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Skin%20of%20the%20Chameleon).
- Block-response / combat setup modifier — [Conscripted Statue](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Conscripted%20Statue) (only on block: basic = opposing minion takes 1 damage each close round; superior = cancel combat and put 2/2 ally into play).
- Bleed modifier — [Unleash the Hounds](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Unleash%20the%20Hounds) (VIS/DOM, +1 bleed (limited); superior enslaver-Gargoyle gets +1 per ready vampire of enslaving clan).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "vis")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "vis")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[combat]] — Visceratika damage-prevent combat package.
- [[damage-resolution]] — armour / prevent interactions.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
