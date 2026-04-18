---
type: entity
tags: [clan, legacy, harbinger-of-skulls, cappadocian-descendants, hecata-consolidated, sabbat-bloodline]
sources: [src-001, src-002, src-020]
last_verified: 2026-04-18
status: verified
---

# Harbinger of Skulls

## Overview

Harbinger of Skulls is a legacy **Sabbat necromancy bloodline** — returned descendants of the slaughtered Cappadocian clan [src-002]. In V5 they have been **consolidated into [[entities/clans/hecata|Hecata]]**, but legacy Harbinger printings remain legal. Card-db evidence: of 21 Harbingers, `NEC` (19), `AUS` (17), and `FOR` (15) dominate superior disciplines — Necromancy + Auspex + Fortitude is a wall-style signature (skeletal intercept-and-prevent) [src-002].

## In-clan disciplines (V5)

Not V5-playable as "Harbinger of Skulls" (see V5 relationship below). Legacy signature (from card-db frequency):

- [[entities/disciplines/auspex|Auspex]] — `[aus]`
- [[entities/disciplines/fortitude|Fortitude]] — `[for]`
- [[entities/disciplines/necromancy|Necromancy]] — `[nec]`

## V5 / legacy relationship

In V5, Harbinger of Skulls is **consolidated into [[entities/clans/hecata|Hecata]]** along with Giovanni, Samedi, Cappadocian, and Nagaraja [src-001 p. 53]. The card-db keeps the legacy Harbinger crypt (21 vampires) under their own clan name — all those printings remain legal and can be mixed with V5 Hecata crypt.

## Sect alignment

Printed sect is dominantly **Sabbat** — most Harbinger card_text opens with `Sabbat:` or `Sabbat priscus:` [src-002]. A couple of outliers print Independent (Erebus). This contrasts with Giovanni's Independent baseline — Harbingers are the Sabbat-aligned wing of the Hecata legacy.

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **21**
- Crypt vampires with `[NEC]` at superior: **19**
- Crypt vampires with `[AUS]` at superior: **17**
- Crypt vampires with `[FOR]` at superior: **15**
- Library cards referencing "Harbinger of Skulls" in name or text: **6**

## Notable members

- **The Capuchin** (cap 11, group 5) — methuselah-tier; `AUS/DOM/FOR/NEC/THA/THN`.
- **Byzar** (cap 10, group 6) — Sabbat; `dom/pre/AUS/FOR/NEC/OBF`.
- **Erlik** (cap 10, group 3) — Sabbat; `AUS/CEL/FOR/NEC/THN`.
- **Angelique** (cap 9, group 6) — Sabbat; `AUS/FOR/NEC/SER/THA`.
- **Unre, Keeper of Golgotha** (cap 9, group 2) — `dom/ser/thn/AUS/FOR/NEC`.

## Typical deck archetypes

- **Harbinger wall / intercept** — NEC reactions (Spectral Divination) + AUS reactions + FOR damage-prevent; extremely resilient.
- **Sabbat Necromancy combat** — NEC rituals with Sabbat title support (bishop/archbishop/priscus printed on Harbingers).
- **Harbinger + Hecata fusion** — legacy Harbingers paired with V5 Hecata for double-spectrum Necromancy + Oblivion.
- [[archetypes/capuchin-toolbox|Capuchin Toolbox]] — runner-up multi-clan endurance toolbox headlined by The Capuchin (cap 11, AUS/DOM/NEC); 10 bounces + 11 intercept + Bonding/Under My Skin bleed escalation; hand over 10 cards [src-020].

## Query

Reproducible filters:

```
# All crypt vampires of the clan (legacy name only)
jq '.[] | select(.clans[]? == "Harbinger of Skulls") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Harbinger of Skulls") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("Harbinger of Skulls"; "i")) or (.card_text // "" | test("Harbinger of Skulls"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/clans/hecata]] — V5 consolidation parent clan; Harbingers merged here.
- [[entities/sects/sabbat]] — primary sect alignment.
- [[entities/disciplines/necromancy]] — legacy signature; ghost magic.
- [[entities/disciplines/auspex]] — in-clan; intercept.
- [[entities/disciplines/fortitude]] — in-clan; damage prevention.

## Sources

- src-001 — VTES 5E Rulebook (V5 Hecata consolidation, p. 53).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
- src-020 — Codex of the Damned — Capuchin Toolbox archetype (runner-up multi-clan endurance toolbox led by The Capuchin).
