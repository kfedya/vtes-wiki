---
type: entity
tags: [clan, 5e-playable, salubri, independent]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Salubri

## Overview

Salubri is a V5-playable clan [src-001 p. 53]. Their V5 signature disciplines are Auspex, Dominate, and Fortitude — the surviving healer-and-defender fragment of the clan. Card-db evidence: of 22 Salubri vampires, `AUS` (16), `FOR` (15), and `DOM`/`OBE` (7 each) dominate superior disciplines; legacy `VAL` (Valeren) appears at superior on 2 crypt only [src-002].

## In-clan disciplines (V5)

- [[entities/disciplines/auspex|Auspex]] — `[aus]`
- [[entities/disciplines/dominate|Dominate]] — `[dom]`
- [[entities/disciplines/fortitude|Fortitude]] — `[for]`

Legacy traditions (still on crypt, still legal): [[entities/disciplines/obeah|Obeah]] — `[obe]` (healer tradition, 7 superior printings); [[entities/disciplines/valeren|Valeren]] — `[val]` (warrior tradition, 2 superior printings; found on the 19-vampire **Salubri antitribu** lineage).

## Sect alignment

Printed sect text is sparse — only 2 of 22 Salubri print `Independent.` in full [src-002]. Lore places the clan as reclusive / almost extinct; most Salubri carry no printed sect. The 19 **Salubri antitribu** crypt entries represent the Sabbat warrior offshoot with Valeren as signature.

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **22**
- Salubri antitribu crypt vampires: **19**
- Crypt vampires with `[AUS]` at superior: **16**
- Crypt vampires with `[FOR]` at superior: **15**
- Crypt vampires with `[DOM]` at superior: **7**
- Crypt vampires with `[OBE]` at superior: **7**
- Library cards referencing "Salubri" in name or text: **16**

## Notable members

- **Saulot, The Wanderer** (cap 11, group 4) — Antediluvian; `dai/AUS/FOR/OBE/THA/VAL`.
- **Nahum Enosh** (cap 10, group 6) — `for/pre/AUS/OBE/OBF/VAL`.
- **Djeneba** (cap 9, group 7) — 5E-era printing; `obf/ANI/AUS/DOM/FOR`.
- **Barachiel** (cap 7, group 7) — V5 printing.
- **Castellan** (cap 6, group 7) — V5 printing.

## Typical deck archetypes

- **Salubri wall** — AUS intercept reactions + FOR damage-prevent; small-but-tanky crypt.
- **Healer / Obeah control** — legacy OBE blood-return + damage-prevent; pacifist toolbox.
- **Salubri antitribu warrior** — VAL aggravated-damage combat; Sabbat-aligned aggression.

## Query

Reproducible filters:

```
# All crypt vampires of the clan
jq '.[] | select(.clans[]? == "Salubri") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Salubri") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("Salubri"; "i")) or (.card_text // "" | test("Salubri"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/sects/independent]] — primary sect alignment.
- [[entities/disciplines/auspex]] — V5 signature; intercept.
- [[entities/disciplines/dominate]] — V5 signature.
- [[entities/disciplines/fortitude]] — V5 signature; damage prevention.
- [[entities/disciplines/obeah]] — legacy healer tradition.
- [[entities/disciplines/valeren]] — legacy warrior tradition; Salubri antitribu signature.

## Sources

- src-001 — VTES 5E Rulebook (playable-clan list, p. 53 Quick Reference icons).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
