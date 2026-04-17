---
type: entity
tags: [clan, legacy, samedi, hecata-consolidated, independent]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Samedi

## Overview

Samedi is a legacy **Haitian voodoo bloodline** — decaying corpse-vampires tied to death-magic traditions of the Caribbean [src-002]. In V5 they have been **consolidated into [[entities/clans/hecata|Hecata]]**, but legacy Samedi crypt printings remain legal. Card-db evidence: of 22 Samedi, `THN` (16), `OBF` (11), `FOR` (10), and `NEC` (8) dominate superior disciplines — Thanatosis + Obfuscate + Fortitude is the Samedi signature, with Necromancy appearing on bridging printings to other death-bloodlines [src-002].

## In-clan disciplines (V5)

Not V5-playable as "Samedi" (see V5 relationship below). Legacy signature (from card-db frequency):

- [[entities/disciplines/fortitude|Fortitude]] — `[for]`
- [[entities/disciplines/obfuscate|Obfuscate]] — `[obf]`
- [[entities/disciplines/thanatosis|Thanatosis]] — `[thn]`

## V5 / legacy relationship

In V5, Samedi is **consolidated into [[entities/clans/hecata|Hecata]]** along with Giovanni, Harbinger of Skulls, Cappadocian, and Nagaraja [src-001 p. 53]. The card-db keeps the legacy Samedi crypt (22 vampires) under their own clan name — all those printings remain legal and can be mixed with V5 Hecata crypt.

## Sect alignment

Printed sect is dominantly **Independent** — 5 of 22 Samedi print `Independent.` in card_text; 2 print `Camarilla.` [src-002]. Most Samedi are untitled loners, which fits the lore-flavor of Caribbean necromancers.

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **22**
- Crypt vampires with `[THN]` at superior: **16**
- Crypt vampires with `[OBF]` at superior: **11**
- Crypt vampires with `[FOR]` at superior: **10**
- Crypt vampires with `[NEC]` at superior: **8**
- Library cards referencing "Samedi" in name or text: **6**

## Notable members

- **Troglodytia** (cap 10, group 4) — `obf/pot/AUS/FOR/NEC/THN`; largest Samedi.
- **Mambo Jeanne** (cap 9, group 6) — `FOR/NEC/OBF/THN`.
- **The Baron** (cap 9, group 2) — `dom/FOR/NEC/OBF/THN`; iconic namesake.
- **Genina, The Red Poet** (cap 8, group 3) — `aus/cel/for/CHI/OBF/THN`.
- **Jack Dawson** (cap 8, group 2) — `cel/nec/qui/thn/FOR/OBF`; advanced printing available.

## Typical deck archetypes

- **Thanatosis disease combat** — THN rot/disease combat cards (Hand of Pestilence) + OBF stealth-bleed engine.
- **Samedi + Hecata fusion** — legacy Samedi for THN depth, modern Hecata for Oblivion / Auspex intercept.
- **Samedi wall** — FOR damage-prevent + THN decay combat; resilient mid-cap shell.

## Query

Reproducible filters:

```
# All crypt vampires of the clan (legacy name only)
jq '.[] | select(.clans[]? == "Samedi") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Samedi") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("Samedi"; "i")) or (.card_text // "" | test("Samedi"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/clans/hecata]] — V5 consolidation parent clan; Samedi merged here.
- [[entities/sects/independent]] — primary sect alignment.
- [[entities/disciplines/thanatosis]] — signature decay discipline.
- [[entities/disciplines/obfuscate]] — in-clan; stealth-bleed.
- [[entities/disciplines/fortitude]] — in-clan; damage prevention.

## Sources

- src-001 — VTES 5E Rulebook (V5 Hecata consolidation, p. 53).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
