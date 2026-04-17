---
type: entity
tags: [clan, legacy, blood-brother, sabbat-bloodline, sabbat, circle]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Blood Brother

## Overview

Blood Brother is a legacy **Sabbat bloodline** — vitae-fused groups of three or more identical vampires (a "circle") [src-002]. Card-db evidence: of 24 Blood Brother vampires, `SAN` (10), `FOR` (4), `POT` (4), and `VIC` (2) dominate superior disciplines — Sanguinus is single-clan to Blood Brothers and functions only through the Circle trait (see [[traits#Circle]]). Fortitude and Potence round out the in-clan baseline [src-002].

## In-clan disciplines (V5)

Not V5-playable. Legacy signature (from card-db frequency):

- [[entities/disciplines/sanguinus|Sanguinus]] — `[san]`
- [[entities/disciplines/fortitude|Fortitude]] — `[for]`
- [[entities/disciplines/potence|Potence]] — `[pot]`

## Sect alignment

Printed sect is dominantly **Sabbat** — 11 of 24 Blood Brothers print `Sabbat:` or `Sabbat.` in card_text, 1 prints Independent [src-002]. Blood Brothers frequently print named circles (Chicago Circle, etc.). A vampire without a printed circle designation is their own circle [src-001 p. 41].

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **24**
- Crypt vampires with `[SAN]` at superior: **10**
- Crypt vampires with `[FOR]` at superior: **4**
- Crypt vampires with `[POT]` at superior: **4**
- Library cards referencing "Blood Brother" in name or text: **22** (very high for a niche bloodline; reflects the circle/group-combat card pool).

## Notable members

- **Angelo** (cap 7, group 3) — Red List; `pot/vic/CEL/FOR/SAN`; largest Blood Brother.
- **Ilse** (cap 6, group 2) — `for/pro/POT/SAN`.
- **Karl** (cap 6, group 2) — `pre/san/FOR/POT`.
- **Jack** (cap 6, group 2) — `cel/for/pot/san`.
- **Mark** (cap 6, group 2) — `for/obf/pot/SAN`.
- **Truman** (cap 6, group 2) — `dom/pot/FOR/SAN`.

## Typical deck archetypes

- **Sanguinus circle combat** — field a circle of three or more Blood Brothers of the same designation to unlock the multi-minion Sanguinus cards (Revelation of the Serim, Coordinate Attacks). Combat scales with each additional circle-mate.
- **Blood Brother wall** — SAN reactions + FOR damage-prevent for a coordinated-defense posture.
- **Chicago Circle rush** — Potence hand-strike rush powered by the circle's shared-vitae mechanics.

## Query

Reproducible filters:

```
# All crypt vampires of the clan
jq '.[] | select(.clans[]? == "Blood Brother") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Blood Brother") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("Blood Brother"; "i")) or (.card_text // "" | test("Blood Brother"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/sects/sabbat]] — primary sect alignment.
- [[entities/disciplines/sanguinus]] — single-clan signature; Circle-gated.
- [[entities/disciplines/fortitude]] — in-clan.
- [[entities/disciplines/potence]] — in-clan.
- [[traits#Circle]] — circle-designation rule that gates Sanguinus cards.

## Sources

- src-001 — VTES 5E Rulebook (clan list; Circle trait p. 41).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
