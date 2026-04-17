---
type: entity
tags: [clan, legacy, kiasyd, lasombra-bloodline, sabbat, single-clan-discipline]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Kiasyd

## Overview

Kiasyd is a legacy **Lasombra-Fae bloodline** — vampires infused with faerie blood, gaining otherworldly knowledge and Mytherceria [src-002]. Card-db evidence: of 16 Kiasyd, `MYT` (12), `OBT` (9), and `DOM` (8) dominate superior disciplines — Mytherceria is single-clan to Kiasyd, paired with Obtenebration (from Lasombra heritage) and Dominate [src-002].

## In-clan disciplines (V5)

Not V5-playable. Legacy signature (from card-db frequency):

- [[entities/disciplines/dominate|Dominate]] — `[dom]`
- [[entities/disciplines/mytherceria|Mytherceria]] — `[myt]`
- [[entities/disciplines/obtenebration|Obtenebration]] — `[obt]`

## Sect alignment

Printed sect is dominantly **Sabbat** — at least 3 Kiasyd print `Sabbat:` or `Sabbat.` as the lead sect marker [src-002]. A few untitled entries exist. Kiasyd lore places them as a semi-hidden Sabbat bloodline tied to Lasombra lineage.

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **16**
- Crypt vampires with `[MYT]` at superior: **12**
- Crypt vampires with `[OBT]` at superior: **9**
- Crypt vampires with `[DOM]` at superior: **8**
- Library cards referencing "Kiasyd" in name or text: **9**

## Notable members

- **Marconius** (cap 9, group 2) — `pot/DOM/MYT/OBT`.
- **Myrna Goldman** (cap 9, group 6) — `ANI/DOM/MYT/OBT`.
- **Bartholomew** (cap 8, group 2) — Sabbat; `dom/obt/AUS/MYT/NEC`.
- **Pherydima** (cap 8, group 4) — `obt/pot/DOM/MYT/NEC`.
- **The Arcadian** (cap 8, group 5) — `chi/for/DOM/MYT/OBT`.

## Typical deck archetypes

- **Kiasyd wall / control** — MYT cold-iron / location cards + OBT shadow-combat for a stealth-and-intercept wall.
- **Kiasyd bleed** — DOM bleed modifiers + MYT faerie-location denial (Faerie Wards).
- **Mixed Lasombra-Kiasyd Sabbat** — shared OBT card pool; Kiasyd supply MYT and DOM.

## Query

Reproducible filters:

```
# All crypt vampires of the clan
jq '.[] | select(.clans[]? == "Kiasyd") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Kiasyd") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("Kiasyd"; "i")) or (.card_text // "" | test("Kiasyd"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/sects/sabbat]] — primary sect alignment.
- [[entities/disciplines/mytherceria]] — single-clan signature; faerie-tainted discipline.
- [[entities/disciplines/obtenebration]] — in-clan; shared with Lasombra.
- [[entities/disciplines/dominate]] — in-clan.
- [[entities/clans/lasombra]] — parent clan (Kiasyd is a Lasombra-Fae hybrid bloodline).

## Sources

- src-001 — VTES 5E Rulebook (clan list, p. 53 Quick Reference icons).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
