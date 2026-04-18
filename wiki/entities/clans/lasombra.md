---
type: entity
tags: [clan, 5e-playable, lasombra, sabbat, camarilla]
sources: [src-001, src-002, src-024]
last_verified: 2026-04-18
status: verified
---

# Lasombra

## Overview

Lasombra is a V5-playable clan [src-001 p. 53]. Their V5 signature disciplines are Dominate, Oblivion, and Potence — shadow-and-command aristocrats. Card-db evidence: of 69 Lasombra vampires, `DOM` (42), `POT` (39), and `OBT` (33) dominate superior disciplines; `OBL` (14) is rising from V5 printings that replace the legacy Obtenebration with Oblivion [src-002].

## V5 signature shift

V5 Lasombra drop the legacy **Obtenebration** discipline in favor of **Oblivion** (the V5 consolidation discipline shared with Hecata). Both still appear on crypt: legacy printings keep `OBT`, V5 printings print `OBL`. Cards referencing either remain legal; deck-builders should plan around the mixed pool.

## In-clan disciplines (V5)

- [[entities/disciplines/dominate|Dominate]] — `[dom]`
- [[entities/disciplines/oblivion|Oblivion]] — `[obl]`
- [[entities/disciplines/potence|Potence]] — `[pot]`

Legacy signature (on most pre-V5 crypt): [[entities/disciplines/obtenebration|Obtenebration]] — `[obt]`.

## Sect alignment

Historically **Sabbat** — 13 of 69 vampires print `Sabbat.` in full, reflecting Lasombra as a co-founding pillar of the Sabbat [src-002]. V5 lore defects a Lasombra faction to the Camarilla (3 Camarilla printings); 1 Independent printing exists.

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **69**
- Crypt vampires with `[DOM]` at superior: **42**
- Crypt vampires with `[POT]` at superior: **39**
- Crypt vampires with `[OBT]` at superior (legacy): **33**
- Crypt vampires with `[OBL]` at superior (V5): **14**
- Library cards referencing "Lasombra" in name or text: **14**

## Notable members

- **Ambrosio Luis Monçada, Plenipotentiary** (cap 10, group 2) — `aus/for/DOM/OBT/POT/PRE`; iconic Sabbat cardinal.
- **Angelica, The Canonicus** (cap 10, group 2) — `cel/obf/DOM/OBT/POT`; Sabbat leadership figure.
- **Luca Italicus** (cap 10, group 4) — `tha/DOM/FOR/NEC/OBT/POT`.
- **Marcus Vitel** (cap 10, group 3) — Camarilla prince template; `DOM/FOR/OBF/OBT/POT/PRE`.
- **Appius Claudius Corvus** (cap 10, group 5) — `cel/nec/DOM/OBT/POT`.

## Typical deck archetypes

- **Sabbat Lasombra vote-and-bleed** — DOM bleed + Obtenebration/Oblivion combat; Sabbat title stack (bishop/archbishop/cardinal).
- **Shadow combat wall** — OBT/OBL shadow combat (Shadow Play, Arms of the Abyss) with POT hand-damage when pressed.
- **V5 Camarilla Lasombra** — Dominate bleed-bounce (Deflection) with Oblivion combat cards; Camarilla prince/primogen titles.
- [[archetypes/lasombra-nocturn|Lasombra Nocturn]] — runner-up Lasombra stealth-and-bleed; Nocturn × 12 dual-purpose ally (bleed-boost / combat protection); Govern × 12 ramp + DOM bleed amp (Conditioning, Empowering the Puppet King, Command of the Beast); OBL stealth (Shadow Play, Shroud of Absence) [src-024].

## Query

Reproducible filters:

```
# All crypt vampires of the clan
jq '.[] | select(.clans[]? == "Lasombra") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Lasombra") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("Lasombra"; "i")) or (.card_text // "" | test("Lasombra"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/sects/sabbat]] — primary legacy alignment.
- [[entities/sects/camarilla]] — V5 faction alignment.
- [[entities/disciplines/dominate]] — bleed increase + Deflection bounce.
- [[entities/disciplines/oblivion]] — V5 signature; shadow + death consolidation.
- [[entities/disciplines/obtenebration]] — legacy shadow discipline; partly superseded by Oblivion.
- [[entities/disciplines/potence]] — hand-strike damage.

## Sources

- src-001 — VTES 5E Rulebook (playable-clan list, p. 53 Quick Reference icons).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
- src-024 — Codex of the Damned — Lasombra Nocturn archetype (runner-up Lasombra stealth-and-bleed via Nocturn ally).
