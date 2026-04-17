---
type: entity
tags: [clan, legacy, ahrimane, gangrel-bloodline, sabbat]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Ahrimane

## Overview

Ahrimane is a legacy **Gangrel offshoot** — a Sabbat bloodline of spirit-communing shamans [src-002]. Card-db evidence: of 15 Ahrimane vampires, `SPI` (7), `ANI` (6), and `PRE` (6) dominate superior disciplines — Spiritus is effectively single-clan on Ahrimane, with Animalism and Presence rounding out the in-clan trio [src-002].

## In-clan disciplines (V5)

Not V5-playable. Legacy signature (from card-db frequency):

- [[entities/disciplines/animalism|Animalism]] — `[ani]`
- [[entities/disciplines/presence|Presence]] — `[pre]`
- [[entities/disciplines/spiritus|Spiritus]] — `[spi]`

## Sect alignment

Printed sect is almost uniformly **Sabbat** — the card_text on Ahrimanes repeatedly prints `Sabbat:` as the opening tag [src-002]. No Camarilla Ahrimane printings; a handful of older entries carry no explicit sect marker. Several Ahrimanes are also **Black Hand**.

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **15**
- Crypt vampires with `[SPI]` at superior: **7**
- Crypt vampires with `[ANI]` at superior: **6**
- Crypt vampires with `[PRE]` at superior: **6**
- Library cards referencing "Ahrimane" in name or text: **6**

## Notable members

- **Sylvie Helgon** (cap 9, group 6) — `aus/vic/ANI/PRE/PRO/SPI`; largest Ahrimane.
- **Howler** (cap 8, group 2) — Sabbat; `obf/ANI/PRE/SPI`; +1 strength, one optional maneuver.
- **Muricia** (cap 7, group 4) — `ANI/PRE/SPI`; pure in-clan signature.
- **The Siamese** (cap 7, group 2) — `ani/pro/PRE/SPI`.
- **Dovey Ebfwe** (cap 7, group 6) — Sabbat / Black Hand; `ani/for/PRE/SPI`.

## Typical deck archetypes

- **Sabbat Spiritus intercept** — SPI reactions for intercept, ANI for swarm combat, PRE for vote support.
- **Gangrel-Ahrimane mixed wall** — pair Ahrimane with Gangrel antitribu to compound ANI/PRO combat + SPI intercept.

## Query

Reproducible filters:

```
# All crypt vampires of the clan
jq '.[] | select(.clans[]? == "Ahrimane") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Ahrimane") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("Ahrimane"; "i")) or (.card_text // "" | test("Ahrimane"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/sects/sabbat]] — primary sect alignment.
- [[entities/disciplines/spiritus]] — signature single-clan discipline.
- [[entities/disciplines/animalism]] — in-clan; shared with Gangrel parent clan.
- [[entities/disciplines/presence]] — in-clan; vote + majesty combat-ends.
- [[entities/clans/gangrel]] — parent clan (Ahrimane is a Gangrel bloodline).

## Sources

- src-001 — VTES 5E Rulebook (clan list, p. 53 Quick Reference icons).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
