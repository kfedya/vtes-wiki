---
type: entity
tags: [clan, 5e-playable, hecata, v5-consolidation, giovanni, samedi, harbinger-of-skulls, cappadocian, nagaraja, independent]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Hecata

## Overview

Hecata is a V5-playable clan and the V5 consolidation of five legacy death-themed bloodlines: **Giovanni**, **Samedi**, **Harbinger of Skulls**, **Cappadocian**, and **Nagaraja** [src-001 p. 53]. The V5 signature disciplines are Auspex, Fortitude, and Oblivion — the consolidated death-magic identity. Card-db evidence: of 18 vampires printed under the "Hecata" clan name, `OBL` (15), `AUS` (12), and `FOR` (11) dominate superior disciplines [src-002]; the five legacy bloodlines retain their own separate crypt counts (see below) with their legacy signature disciplines (Necromancy, Thanatosis, Daimoinon, etc.).

## V5 consolidation

The V5 Hecata is a union of five legacy bloodlines under a single clan name [src-001 p. 53]. The card-db keeps each legacy bloodline's crypt under its own clan name (Giovanni, Samedi, Harbinger of Skulls, Nagaraja — Cappadocian has 0 entries in the snapshot), while new V5 printings use the "Hecata" clan name directly. All legacy cards remain legal. Deck-builders can mix Hecata with any of the legacy rosters at the crypt level.

Legacy bloodline crypt counts [src-002]:

- Giovanni: **62**
- Samedi: **22**
- Harbinger of Skulls: **21**
- Nagaraja: **10**
- Cappadocian: **0** (no crypt under this name in the current snapshot)

Separate stub pages for each legacy bloodline are tracked for a future batch; cross-reference here when created.

## In-clan disciplines (V5)

- [[entities/disciplines/auspex|Auspex]] — `[aus]`
- [[entities/disciplines/fortitude|Fortitude]] — `[for]`
- [[entities/disciplines/oblivion|Oblivion]] — `[obl]`

Common legacy disciplines on the consolidated bloodlines: [[entities/disciplines/necromancy|Necromancy]] — `[nec]` (Giovanni, Harbinger of Skulls, Nagaraja); [[entities/disciplines/thanatosis|Thanatosis]] — `[thn]` (Samedi).

## Sect alignment

Printed text on V5 Hecata is predominantly **Independent** — 6 of 18 vampires print `Independent.` in full [src-002]. 2 **Sabbat** printings exist, reflecting Hecata factions still aligned with the Sabbat. Legacy Giovanni and kin were canonically Independent.

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires printed as "Hecata" (V5): **18**
- Crypt vampires with `[OBL]` at superior: **15**
- Crypt vampires with `[AUS]` at superior: **12**
- Crypt vampires with `[FOR]` at superior: **11**
- Library cards referencing "Hecata" in name or text: **5**

## Notable members

- **Ashur-uballit, Son of the Abyss** (cap 10, group 6) — methuselah-tier V5 printing; `AUS/DOM/FOR/OBL/THA`.
- **Roger de Camden** (cap 10, group 6) — V5 printing; `AUS/FOR/OBF/OBL/PRE`.
- **Marchesa Liliana** (cap 9, group 6) — V5 printing; `dom/ANI/AUS/FOR/OBL`.
- **Hel-Blá** (cap 9, group 6) — V5 printing; `obf/AUS/FOR/OBL/POT`.
- **"Mother" Anja Giovanni** (cap 8, group 6) — V5-era printing bridging legacy Giovanni flavor.

## Typical deck archetypes

- **Hecata bleed-bounce / wall** — Dominate (via multi-discipline crypt) + Oblivion combat; AUS for intercept.
- **Oblivion death-magic combat** — `OBL` rituals and shadow-combat cards; signature V5 Hecata identity.
- **Mixed Giovanni / Hecata wall** — classic Necromancy bleed-bounce fused with new Oblivion printings.

## Query

Reproducible filters:

```
# All crypt vampires of the clan (Hecata name only)
jq '.[] | select(.clans[]? == "Hecata") | .name' card-db/crypt.json

# Top superior disciplines on Hecata-named crypt
jq -r '[.[] | select(.clans[]? == "Hecata") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Legacy bloodline counts
for c in Giovanni Samedi "Harbinger of Skulls" Nagaraja Cappadocian; do \
  printf "%s: " "$c"; \
  jq "[.[] | select(.clans[]? == \"$c\")] | length" card-db/crypt.json; \
done
```

## Related

- [[entities/sects/independent]] — primary sect alignment.
- [[entities/sects/sabbat]] — secondary contingent.
- [[entities/disciplines/auspex]] — V5 signature; intercept.
- [[entities/disciplines/fortitude]] — V5 signature; damage prevention.
- [[entities/disciplines/oblivion]] — V5 signature; shadow + death consolidation.
- [[entities/disciplines/necromancy]] — legacy discipline common on Giovanni / Harbinger of Skulls / Nagaraja.
- [[entities/disciplines/thanatosis]] — legacy discipline on Samedi.

## Sources

- src-001 — VTES 5E Rulebook (playable-clan list, p. 53 Quick Reference icons).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
