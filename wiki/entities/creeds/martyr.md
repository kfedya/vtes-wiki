---
type: entity
tags: [creed, imbued]
sources: [src-002]
last_verified: 2026-04-18
status: draft
---

# Martyr

## Overview

Martyr is one of seven Imbued **creeds** — the "clan" analogue for Imbued minions (mortals with True Faith) [src-002]. Martyrs embody self-sacrifice and suffering on behalf of others; every Martyr crypt card carries [[entities/disciplines/martyrdom|Martyrdom]] as its signature virtue. Imbued are generally not targetable by vampire-only effects and use Convictions + Power library cards rather than several regular library slots; see the gap flag under Related.

## Virtues (card-db signature)

Of 3 Martyr crypt cards, superior virtue frequencies are:

- [[entities/disciplines/martyrdom|Martyrdom]] — `[mar]` — **3** (universal on Martyr).
- [[entities/disciplines/defense|Defense]] — `[def]` — 1 (cross-creed).
- [[entities/disciplines/innocence|Innocence]] — `[inn]` — 1 (cross-creed).
- [[entities/disciplines/redemption|Redemption]] — `[red]` — 1 (cross-creed).
- [[entities/disciplines/vision|Vision]] — `[viz]` — 1 (cross-creed).

## Card counts (src-002 snapshot 2026-04-18)

- Crypt cards printed as Martyr: **3**
- Crypt cards carrying Martyrdom: 3 (all of them).
- Library cards referencing "Martyr": 2 (name/text hits).

## Notable members

- **Anna "Dictatrix11" Suljic** (cap 6, group 4) — top-capacity Martyr; `mar/red/viz`.
- **Travis "Traveler72" Miller** (cap 5, group 4) — `mar/def`.
- **Maman Boumba** (cap 4, group 4) — `inn/mar`.

## Imbued mechanics (summary)

- Imbued are **mortals with True Faith**, not vampires — vampire-only card effects do not target them [src-002].
- Imbued use **Conviction** and **Power** library card types in combination with virtues, in place of several vampire-discipline card types [src-002].
- No dedicated ruling page for Imbued mechanics (True Faith, Convictions, imbuement, targeting restrictions) exists yet — **gap flag**.

## Query

Reproducible filter:

```
# All Martyr crypt cards
jq '.[] | select(.clans[]? == "Martyr") | .name' card-db/crypt.json

# Superior virtue frequency on Martyr
jq -r '[.[] | select(.clans[]? == "Martyr") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({virtue: .[0], count: length}) | sort_by(-.count) | .[] | "\(.virtue) \(.count)"' card-db/crypt.json
```

## Related

- [[entities/disciplines/martyrdom|Martyrdom]] — creed-defining virtue.
- [[entities/disciplines/defense|Defense]], [[entities/disciplines/innocence|Innocence]], [[entities/disciplines/redemption|Redemption]], [[entities/disciplines/vision|Vision]] — cross-creed virtues.
- [[entities/creeds/avenger|Avenger]], [[entities/creeds/defender|Defender]], [[entities/creeds/innocent|Innocent]], [[entities/creeds/judge|Judge]], [[entities/creeds/redeemer|Redeemer]], [[entities/creeds/visionary|Visionary]] — other six creeds.
- **Gap:** no `wiki/rulings/` page for Imbued / True Faith / Convictions mechanics yet.

## Sources

- src-002 — krcg vtes.json snapshot 2026-04-18 (Imbued crypt, virtue frequencies).
