---
type: entity
tags: [discipline, legacy, spiritus, ahrimane, spirits]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Spiritus

**Code:** `[spi]` basic / `[SPI]` superior

## Overview

Spiritus is the legacy **Ahrimane** discipline of spirit communion — summoning totem spirits for intercept, animal-spirit combat buffs, and supernatural scrying. Mechanically a support pool leaning on reactions (intercept / wake), spirit-flavoured combat cards, and animal-totem action modifiers. A small, single-clan-flavoured discipline.

## In-clan

Primary in-clan discipline for (legacy printings): **Ahrimane**.
Rare on other clans (occasional Guruhi printings).

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[spi]` (basic or superior): **17**
- Crypt vampires with `[spi]` or `[SPI]`: **16**

## Typical card roles

- Spirit-intercept / scry reactions — [Speak with Spirits](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Speak%20with%20Spirits), [Ears of the Hare](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Ears%20of%20the%20Hare), [Falcon's Eye](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Falcon%27s%20Eye).
- Animal-totem action modifiers — [Mole's Tunneling](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Mole%27s%20Tunneling), [Squirrel Balance](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Squirrel%20Balance), [Swiftness of the Stag](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Swiftness%20of%20the%20Stag).
- Spirit combat — [Chameleon's Colors](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Chameleon%27s%20Colors), [Strength of the Bear](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Strength%20of%20the%20Bear), [Leapfrog](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Leapfrog), [Summon Spirit Beast](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Summon%20Spirit%20Beast).
- Hunt / bleed actions — [Charge of the Buffalo](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Charge%20of%20the%20Buffalo), [Nose of the Hound](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Nose%20of%20the%20Hound), [Vulture's Buffet](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Vulture%27s%20Buffet).
- Ritual / Muricia — [Muricia's Call](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Muricia%27s%20Call), [New Moon Sigil](https://codex-of-the-damned.org/en/card-search/library/index.html?card=New%20Moon%20Sigil).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "spi")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "spi")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[entities/disciplines/animalism|animalism]] — sibling totem/animal discipline.
- [[block-resolution]] — Spiritus reactions add intercept.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
