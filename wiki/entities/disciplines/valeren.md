---
type: entity
tags: [discipline, legacy, valeren, salubri, warrior]
sources: [src-001, src-002]
last_verified: 2026-04-19
status: verified
---

# Valeren

**Code:** `[val]` basic / `[VAL]` superior

## Overview

Valeren is the legacy **Salubri warrior** tradition discipline — the martial counterpart to [[entities/disciplines/obeah|Obeah]] (the healer tradition). Where Obeah mends, Valeren smites: righteous combat strikes, aggravated-damage swords, and reactions that punish deceivers. Mechanically a combat-heavy pool with a handful of supporting actions and reactions. A small discipline concentrated on Salubri antitribu crypt cards.

## In-clan

Primary in-clan discipline for (legacy printings): **Salubri antitribu** (warrior caste).
Rare on regular Salubri (who favour Obeah instead).

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[val]` (basic or superior): **18**
- Crypt vampires with `[val]` or `[VAL]`: **23**

## Typical card roles

- Aggravated-damage combat — [Sword of the Righteous](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Sword%20of%20the%20Righteous), [Vengeance of Samiel](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Vengeance%20of%20Samiel), [Blessed Blade](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Blessed%20Blade).
- Action modifier (val side) — [Burning Touch](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Burning%20Touch) (basic val = on-block, blocker burns blood & others may decline to block; superior VAL = +1 bleed (limited) on a bleed action — NB: the aggravated-damage strike on this card is the `[tha]` Combat mode, not Valeren).
- Pain / agony combat — [Blissful Agony](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Blissful%20Agony), [Loving Agony](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Loving%20Agony), [Morphean Blow](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Morphean%20Blow).
- Protective armour / defence — [Armor of Caine's Fury](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Armor%20of%20Caine%27s%20Fury), [Eye of Unforgiving Heaven](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Eye%20of%20Unforgiving%20Heaven).
- Truth / reaction — [Hide the Heart](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Hide%20the%20Heart), [Aversion](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Aversion).
- Warding / sensing actions — [Sense Vitality](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Sense%20Vitality), [Sense Death](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Sense%20Death), [Warding the Beast](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Warding%20the%20Beast), [Shadow of Taint](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Shadow%20of%20Taint).

## Relationship to Obeah

Valeren and [[entities/disciplines/obeah|Obeah]] are the two Salubri traditions — warrior (Valeren) and healer (Obeah). They share flavour and some defensive tech, but a given Salubri crypt card almost always carries one or the other, not both. Check the crypt disciplines line when building mixed-tradition Salubri decks.

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "val")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "val")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[entities/disciplines/obeah|obeah]] — sibling Salubri healer tradition.
- [[combat]] — Valeren combat package.
- [[damage-resolution]] — aggravated-damage rules.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
