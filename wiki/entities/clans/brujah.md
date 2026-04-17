---
type: entity
tags: [clan, 5e-playable, brujah, camarilla, anarch]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Brujah

## Overview

Brujah is a V5-playable clan [src-001 p. 53]. Their in-clan disciplines of Celerity, Potence, and Presence define the archetypal "rabble" — fast-striking combat with hand-damage enhancement and vote pressure via Presence. Card-db evidence: of 94 Brujah vampires, `CEL` (53), `PRE` (48), and `POT` (46) are the most common superior disciplines, confirming the V5 signature set [src-002].

## In-clan disciplines (V5)

- [[entities/disciplines/celerity|Celerity]] — `[cel]`
- [[entities/disciplines/potence|Potence]] — `[pot]`
- [[entities/disciplines/presence|Presence]] — `[pre]`

## Sect alignment

Split across sects. Printed text shows **Camarilla** (20 vampires) as the plurality, with a significant **Anarch** contingent (6) and historical **Sabbat** loyalists (1 printed; plus the 43-vampire **Brujah antitribu** lineage that hosts the Sabbat offshoot) [src-002]. Legacy lore places Brujah at the heart of the Anarch Revolt, and V5-era printings lean increasingly Anarch.

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **94**
- Brujah antitribu crypt vampires: **43**
- Crypt vampires with `[CEL]` at superior: **53**
- Crypt vampires with `[PRE]` at superior: **48**
- Crypt vampires with `[POT]` at superior: **46**
- Library cards referencing "Brujah" in name or text: **22**

## Notable members

- **Gwendolyn** (cap 11, group 2) — `aus/tha/CEL/FOR/POT/PRE`.
- **Adana de Sforza** (cap 11, group 4) — `aus/CEL/OBF/POT/PRE/PRO`.
- **Appolonius** (cap 10, group 1) — `for/pot/CEL/PRE`; methuselah-tier baseline.
- **Jaroslav Pascek** (cap 10, group 3) — Camarilla justicar template; `for/obf/CEL/POT/PRE`.
- **Don Cruez, The Idealist** (cap 10, group 1) — `ani/dom/pro/CEL/POT/PRE`.

## Typical deck archetypes

- **Brujah rush / bruise** — CEL-enabled extra strikes + POT hand-strike damage; Immortal Grapple + Torn Signpost-style wrestling (where legal). Fast combat finishers.
- **Vote / presence-control** — PRE vote boost (Voter Captivation, Majesty), paired with CEL reactions for defense.
- **Anarch Brujah** — 5E-era tilt toward the Anarch sect; 2 votes per baron + CEL/POT aggression.

## Query

Reproducible filters:

```
# All crypt vampires of the clan
jq '.[] | select(.clans[]? == "Brujah") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Brujah") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("Brujah"; "i")) or (.card_text // "" | test("Brujah"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/sects/camarilla]] — historical sect alignment.
- [[entities/sects/anarch]] — 5E-era tilt; 2 votes per baron.
- [[entities/disciplines/celerity]] — extra strikes + dodges.
- [[entities/disciplines/potence]] — hand-strike damage + grapple.
- [[entities/disciplines/presence]] — vote boost + Majesty.

## Sources

- src-001 — VTES 5E Rulebook (playable-clan list, p. 53 Quick Reference icons).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
