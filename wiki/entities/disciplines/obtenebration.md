---
type: entity
tags: [discipline, legacy, obtenebration, lasombra, shadow]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Obtenebration

**Code:** `[obt]` basic / `[OBT]` superior

## Overview

Obtenebration is the legacy Lasombra discipline of living shadow — coiling tendrils of dark that grapple prey, drown the field in night, and hide the vampire from sight [src-002]. Mechanically it is one of the deepest legacy combat pools: shadow-arms grapple combat, stealth action modifiers, and entombment / oubliette-style removal cards. In V5 it is partly replaced by [[entities/disciplines/oblivion|Oblivion]] — see the relationship note below.

## In-clan

Primary in-clan discipline for (legacy printings): **Lasombra**, **Kiasyd**.
Scattered appearances on: Toreador antitribu, Baali, Giovanni.

## V5 / legacy relationship

- V5 introduced [[entities/disciplines/oblivion|Oblivion]] (`obl`) as the modern Lasombra/Hecata shadow-and-death discipline.
- Oblivion **does not errata or invalidate** `[obt]` cards — legacy Obtenebration cards remain fully legal.
- Many V5 Lasombra crypt cards still print `[obt]` (or both `[obt]` and `[obl]`), letting legacy and V5 pools mix in a single deck.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[obt]` (basic or superior): **34**
- Crypt vampires with `[obt]` or `[OBT]`: **115**

## Typical card roles

- Shadow-arms grapple combat — [Arms of the Abyss](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Arms%20of%20the%20Abyss), [Ahriman's Demesne](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Ahriman%27s%20Demesne).
- Entombment / removal combat — [Entombment](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Entombment), [Oubliette](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Oubliette), [Shadow Body](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Shadow%20Body).
- Stealth / shadow action modifiers — [Shroud of Absence](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Shroud%20of%20Absence), [Shroud of Night](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Shroud%20of%20Night), [Shadow Play](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Shadow%20Play).
- Shadow-themed actions — [Black Metamorphosis](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Black%20Metamorphosis), [Summon the Abyss](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Summon%20the%20Abyss).
- Intercept reactions — [Eyes of the Night](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Eyes%20of%20the%20Night), [Darksight](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Darksight).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "obt")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "obt")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[entities/disciplines/oblivion]] — V5 successor that partly consolidates Obtenebration.
- [[stealth-modifiers]] — Obtenebration contributes Shroud-series +stealth modifiers.
- [[combat]] — most iconic Obtenebration cards are combat cards.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
