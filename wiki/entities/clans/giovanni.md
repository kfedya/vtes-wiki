---
type: entity
tags: [clan, legacy, giovanni, hecata-consolidated, independent]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Giovanni

## Overview

Giovanni is a legacy **merchant-family bloodline** — Italian necromancers turned into a vampire clan in the Dark Ages [src-002]. In V5 they have been **consolidated into [[entities/clans/hecata|Hecata]]**, but legacy Giovanni crypt printings remain legal under the Giovanni clan name. Card-db evidence: of 62 Giovanni vampires, `NEC` (34), `POT` (33), and `DOM` (32) dominate superior disciplines — Necromancy + Potence + Dominate is the tightly-packed legacy signature, making Giovanni one of the most internally coherent clans in the game [src-002].

## In-clan disciplines (V5)

Not V5-playable as "Giovanni" (see V5 relationship below). Legacy signature (from card-db frequency):

- [[entities/disciplines/dominate|Dominate]] — `[dom]`
- [[entities/disciplines/necromancy|Necromancy]] — `[nec]`
- [[entities/disciplines/potence|Potence]] — `[pot]`

## V5 / legacy relationship

In V5, Giovanni is **consolidated into [[entities/clans/hecata|Hecata]]** along with Samedi, Harbinger of Skulls, Cappadocian, and Nagaraja [src-001 p. 53]. The card-db keeps the legacy Giovanni crypt (62 vampires) under the Giovanni clan name — all those printings remain legal and can be mixed freely with V5 Hecata crypt. New printings use the "Hecata" clan name.

## Sect alignment

Printed sect is dominantly **Independent** — 28 of 62 Giovanni print `Independent.` in card_text [src-002]. The family title structure (Lady, Don, family heads) is reflected in printed vote counts on select Giovanni rather than a sect title.

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **62**
- Crypt vampires with `[NEC]` at superior: **34**
- Crypt vampires with `[POT]` at superior: **33**
- Crypt vampires with `[DOM]` at superior: **32**
- Library cards referencing "Giovanni" in name or text: **20**

## Notable members

- **Augustus Giovanni** (cap 11, group 2) — Antediluvian tier; `cel/pre/AUS/DOM/NEC/POT`.
- **Carmine Giovanni** (cap 10, group 4) — `ani/pre/DOM/NEC/POT/PRO`.
- **Lady Constancia** (cap 10, group 4) — `AUS/DOM/FOR/NEC/POT`.
- **Luna Giovanni** (cap 10, group 5) — `cel/DOM/NEC/OBF/OBT/POT`.
- **Regina Giovanni, The Right Hand of Augustus** (cap 10, group 2) — `aus/for/DOM/NEC/POT`.

## Typical deck archetypes

- **Giovanni bleed-bounce wall** — classic DOM Deflection bounce + NEC reactions (Spectral Divination) + POT combat; extremely resilient.
- **Necromancy wraith combat** — NEC rituals / wraith allies (Masters of Path) for ghost-combat.
- **Giovanni + Hecata fused crypt** — legacy Giovanni with V5 Hecata for Oblivion + Necromancy double-spectrum.

## Query

Reproducible filters:

```
# All crypt vampires of the clan (legacy Giovanni name only)
jq '.[] | select(.clans[]? == "Giovanni") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Giovanni") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("Giovanni"; "i")) or (.card_text // "" | test("Giovanni"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/clans/hecata]] — V5 consolidation parent clan; Giovanni merged here.
- [[entities/sects/independent]] — primary sect alignment.
- [[entities/disciplines/necromancy]] — legacy signature; ghost magic.
- [[entities/disciplines/dominate]] — in-clan; bleed-bounce (Deflection).
- [[entities/disciplines/potence]] — in-clan; hand-strike combat.

## Sources

- src-001 — VTES 5E Rulebook (V5 Hecata consolidation, p. 53).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
