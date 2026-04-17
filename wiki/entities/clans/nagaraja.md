---
type: entity
tags: [clan, legacy, nagaraja, hecata-consolidated, necromancer-bloodline]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Nagaraja

## Overview

Nagaraja is a legacy **Asian necromancer bloodline** — cannibal flesh-eaters tied to the death-lotus Pillar and Eastern necromantic traditions [src-002]. In V5 they have been **consolidated into [[entities/clans/hecata|Hecata]]**, but legacy Nagaraja crypt printings remain legal. Card-db evidence: of 10 Nagaraja vampires, `NEC` (6), `AUS` (5), and `DOM` (3) dominate superior disciplines — Necromancy + Auspex + Dominate is the tight in-clan trio [src-002].

## In-clan disciplines (V5)

Not V5-playable as "Nagaraja" (see V5 relationship below). Legacy signature (from card-db frequency):

- [[entities/disciplines/auspex|Auspex]] — `[aus]`
- [[entities/disciplines/dominate|Dominate]] — `[dom]`
- [[entities/disciplines/necromancy|Necromancy]] — `[nec]`

## V5 / legacy relationship

In V5, Nagaraja is **consolidated into [[entities/clans/hecata|Hecata]]** along with Giovanni, Samedi, Harbinger of Skulls, and Cappadocian [src-001 p. 53]. The card-db keeps the legacy Nagaraja crypt (10 vampires) under their own clan name — all those printings remain legal and can be mixed with V5 Hecata crypt.

## Sect alignment

Printed sect is a mix of Sabbat and Independent; the snapshot shows only 1 Nagaraja prints `Sabbat:` explicitly [src-002]. Many Nagaraja carry no explicit sect tag; some titled printings (e.g. Synesios on Sabbat lists) align by lineage rather than printed sect.

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **10**
- Crypt vampires with `[NEC]` at superior: **6**
- Crypt vampires with `[AUS]` at superior: **5**
- Crypt vampires with `[DOM]` at superior: **3**
- Library cards referencing "Nagaraja" in name or text: **3**

## Notable members

- **Yavu Matebo** (cap 8, group 4) — `abo/AUS/DOM/NEC`; largest Nagaraja.
- **Anu Diptinatpa** (cap 7, group 6) — `aus/vic/DOM/NEC`.
- **Kanimana Belghazi** (cap 7, group 2) — `pro/AUS/DOM/NEC`.

## Typical deck archetypes

- **Nagaraja bleed-bounce** — DOM Deflection bounce + AUS reactions + NEC rituals.
- **Hecata-fused Necromancy stack** — combine Nagaraja with Giovanni + Harbinger to triple down on Necromancy depth while sharing V5 Hecata Oblivion cards.

## Query

Reproducible filters:

```
# All crypt vampires of the clan (legacy name only)
jq '.[] | select(.clans[]? == "Nagaraja") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Nagaraja") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("Nagaraja"; "i")) or (.card_text // "" | test("Nagaraja"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/clans/hecata]] — V5 consolidation parent clan; Nagaraja merged here.
- [[entities/disciplines/necromancy]] — legacy signature; ghost magic.
- [[entities/disciplines/auspex]] — in-clan; intercept.
- [[entities/disciplines/dominate]] — in-clan; bleed-bounce.

## Sources

- src-001 — VTES 5E Rulebook (V5 Hecata consolidation, p. 53).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
