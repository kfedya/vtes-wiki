---
type: entity
tags: [creed, imbued]
sources: [src-002]
last_verified: 2026-04-18
status: draft
---

# Visionary

## Overview

Visionary is one of seven Imbued **creeds** — the "clan" analogue for Imbued minions (mortals with True Faith) [src-002]. Visionaries embody foresight and prophetic guidance; every Visionary crypt card carries [[entities/disciplines/vision|Vision]] as its signature virtue. Imbued are generally not targetable by vampire-only effects and use Convictions + Power library cards rather than several regular library slots; see the gap flag under Related.

## Virtues (card-db signature)

Of 3 Visionary crypt cards, superior virtue frequencies are:

- [[entities/disciplines/vision|Vision]] — `[viz]` — **3** (universal on Visionary).
- [[entities/disciplines/judgment|Judgment]] — `[jud]` — 2 (cross-creed).
- [[entities/disciplines/defense|Defense]] — `[def]` — 1 (cross-creed).
- [[entities/disciplines/innocence|Innocence]] — `[inn]` — 1 (cross-creed).
- [[entities/disciplines/martyrdom|Martyrdom]] — `[mar]` — 1 (cross-creed).

## Card counts (src-002 snapshot 2026-04-18)

- Crypt cards printed as Visionary: **3**
- Crypt cards carrying Vision: 3 (all of them).
- Library cards referencing "Visionary": 0 (no name/text hits — Visionary identity is virtue-gated).

## Notable members

- **Earl "Shaka74" Deams** (cap 6, group 4) — top-capacity Visionary; `jud/mar/viz`.
- **Jennie "Cassie247" Orne** (cap 5, group 4) — `inn/jud/viz`.
- **Paul "Sixofswords29" Moreton** (cap 4, group 4) — `def/viz`.

## Imbued mechanics (summary)

- Imbued are **mortals with True Faith**, not vampires — vampire-only card effects do not target them [src-002].
- Imbued use **Conviction** and **Power** library card types in combination with virtues, in place of several vampire-discipline card types [src-002].
- No dedicated ruling page for Imbued mechanics (True Faith, Convictions, imbuement, targeting restrictions) exists yet — **gap flag**.

## Query

Reproducible filter:

```
# All Visionary crypt cards
jq '.[] | select(.clans[]? == "Visionary") | .name' card-db/crypt.json

# Superior virtue frequency on Visionary
jq -r '[.[] | select(.clans[]? == "Visionary") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({virtue: .[0], count: length}) | sort_by(-.count) | .[] | "\(.virtue) \(.count)"' card-db/crypt.json
```

## Related

- [[entities/disciplines/vision|Vision]] — creed-defining virtue.
- [[entities/disciplines/defense|Defense]], [[entities/disciplines/innocence|Innocence]], [[entities/disciplines/judgment|Judgment]], [[entities/disciplines/martyrdom|Martyrdom]] — cross-creed virtues.
- [[entities/creeds/avenger|Avenger]], [[entities/creeds/defender|Defender]], [[entities/creeds/innocent|Innocent]], [[entities/creeds/judge|Judge]], [[entities/creeds/martyr|Martyr]], [[entities/creeds/redeemer|Redeemer]] — other six creeds.
- **Gap:** no `wiki/rulings/` page for Imbued / True Faith / Convictions mechanics yet.

## Sources

- src-002 — krcg vtes.json snapshot 2026-04-18 (Imbued crypt, virtue frequencies).
