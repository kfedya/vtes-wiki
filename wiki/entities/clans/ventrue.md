---
type: entity
tags: [clan, 5e-core, ventrue, camarilla]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Ventrue

## Overview

Ventrue is one of the five core 5E clans [src-001 p. 53]. Their in-clan disciplines of Dominate, Fortitude, and Presence give the clan the most durable bleed-and-vote profile in the 5E core — Dominate drives bleed and bounce, Fortitude eats damage, Presence pushes votes. Card-db evidence: of 94 Ventrue vampires, `PRE` (56), `FOR` (49), and `DOM` (47) are the most common superior disciplines, confirming the V5 signature set [src-002].

## In-clan disciplines (V5)

- [[entities/disciplines/dominate|Dominate]] — `[dom]`
- [[entities/disciplines/fortitude|Fortitude]] — `[for]`
- [[entities/disciplines/presence|Presence]] — `[pre]`

## Sect alignment

Primarily **Camarilla** — 22 of 94 Ventrue vampires print `Camarilla.` in full, with numerous Camarilla princes and primogens (Atlanta, Amsterdam, etc.). A handful of **Anarch** Ventrue (including the flavor-famous `Callihan` line) appear post-V5. No Ventrue antitribu exist in 5E; the legacy **Ventrue antitribu** (43 crypt entries) is the Sabbat offshoot [src-002].

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **94**
- Crypt vampires with `[PRE]` at superior: **56**
- Crypt vampires with `[FOR]` at superior: **49**
- Crypt vampires with `[DOM]` at superior: **47**
- Library cards referencing "Ventrue" in name or text: **23**

## Notable members

- **Mithras** (cap 11, group 3 / group 6) — methuselah prince of London; `DOM / FOR / POT / PRE / QUI` (or `/ THA` for the G6 reprint).
- **Hardestadt** (cap 11, group 4) — Camarilla founder line; `cel / pro / DOM / FOR / POT / PRE`.
- **Arika** (cap 11, group 2) — Camarilla Inner Circle; `aus / cel / DOM / FOR / OBF / PRE`.
- **Marcus Vitel** (cap 10, group 3) — Camarilla prince; `DOM / FOR / OBF / OBT / PRE`.
- **Lucinde, Alastor** (cap 10, groups 3 & 7) — Alastor archetype; `obf / pot / tha / DOM / FOR / PRE`.
- 5E-era printing: **Alexa Draper** (cap 8, group 6).

## Typical deck archetypes

- **Ventrue grinder / princes** — classic Camarilla Ventrue prince deck: DOM bleed + PRE vote push + FOR damage prevention. Extremely resilient; slow win condition.
- **Kiasyd / Ventrue vote** — PRE-heavy vote backbone with DOM backup for bounce (Deflection).
- **Ventrue wall** — mid-cap vampires with FOR damage prevention and AUS/DOM reaction intercept; strong prey-lock.

## Query

Reproducible filters:

```
# All crypt vampires of the clan
jq '.[] | select(.clans[]? == "Ventrue") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Ventrue") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("Ventrue"; "i")) or (.card_text // "" | test("Ventrue"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/sects/camarilla]] — primary sect alignment.
- [[entities/disciplines/dominate]] — bleed increase + Deflection bounce.
- [[entities/disciplines/fortitude]] — damage prevention + sun-cover.
- [[entities/disciplines/presence]] — vote boost + Majesty combat-ends.
- [[voting]] — title-vote table; Ventrue field many princes and justicars.

## Sources

- src-001 — VTES 5E Rulebook (core-5 clan list, p. 53 Quick Reference icons).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
