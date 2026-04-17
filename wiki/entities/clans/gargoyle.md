---
type: entity
tags: [clan, legacy, gargoyle, tremere-bloodline, flight, single-clan-discipline]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Gargoyle

## Overview

Gargoyle is a legacy **Tremere-created bloodline** — stone-flesh combat vampires engineered by Tremere in the Dark Ages [src-002]. Card-db evidence: of 23 Gargoyles, `VIS` (14), `POT` (11), and `FOR` (10) dominate superior disciplines — Visceratika is near-single-clan, paired with the Fortitude + Potence combat baseline [src-002]. Most Gargoyles also print the **Flight trait** (see [[traits#Flight]]), unlocking the FLIGHT library-card pool.

## In-clan disciplines (V5)

Not V5-playable. Legacy signature (from card-db frequency):

- [[entities/disciplines/fortitude|Fortitude]] — `[for]`
- [[entities/disciplines/potence|Potence]] — `[pot]`
- [[entities/disciplines/visceratika|Visceratika]] — `[vis]`

## Sect alignment

Printed sect is mixed: several **Camarilla** Gargoyles (many printed as **Tremere slave** due to their creation lore), several **Sabbat** Gargoyles, a handful of **Anarch** and **Independent** (Alabástrom, Ferox) [src-002]. Slave trait on many Gargoyles means they are owned by their Tremere master for transfer/rescue purposes.

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **23**
- Crypt vampires with `[VIS]` at superior: **14**
- Crypt vampires with `[POT]` at superior: **11**
- Crypt vampires with `[FOR]` at superior: **10**
- Library cards referencing "Gargoyle" in name or text: **19**

## Notable members

- **Chaundice** (cap 8, group 4) — Sabbat; `vic/FOR/POT/VIS`.
- **Rocia** (cap 8, group 4) — `obf/FOR/POT/VIS`.
- **Alabástrom** (cap 7, group 6) — Anarch; `aus/cel/for/POT/VIS`.
- **Chalcedony** (cap 7, group 6) — Camarilla; `FOR/POT/THA/VIS`; Gargoyle-cost reducer.
- **Ferox, The Rock Lord** (cap 7, group 2) — Independent; `ani/FOR/POT/VIS`; advanced printing available.

## Typical deck archetypes

- **Gargoyle wall / stone-combat** — VIS damage-prevent combat (Earth Meld, Stone Strength) + POT hand-strike; ANI / Create Gargoyle allies for swarm support.
- **Flight beat-stick** — stack FLIGHT library cards (Soar, Swoop, Pounce) for hyper-mobile combat.
- **Tremere-Gargoyle combined crypt** — use Tremere master to anchor Tremere-slave Gargoyles; THA + VIS combat overlap.

## Query

Reproducible filters:

```
# All crypt vampires of the clan
jq '.[] | select(.clans[]? == "Gargoyle") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Gargoyle") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("Gargoyle"; "i")) or (.card_text // "" | test("Gargoyle"; "i")))] | length' card-db/library/*.json

# Gargoyles with Flight trait
jq -r '.[] | select(.clans[]? == "Gargoyle") | select(.card_text // "" | test("Flight")) | .name' card-db/crypt.json
```

## Related

- [[entities/disciplines/visceratika]] — single-clan signature; stone discipline.
- [[entities/disciplines/potence]] — in-clan; hand-strike combat.
- [[entities/disciplines/fortitude]] — in-clan; damage prevention.
- [[entities/clans/tremere]] — creator clan; many Gargoyles are Tremere slaves.
- [[traits#Flight]] — Flight-trait rule + FLIGHT library-card list.

## Sources

- src-001 — VTES 5E Rulebook (clan list; Flight trait p. 41).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
