---
type: entity
tags: [creed, imbued]
sources: [src-002]
last_verified: 2026-04-18
status: draft
---

# Defender

## Overview

Defender is one of seven Imbued **creeds** — the "clan" analogue for Imbued minions (mortals with True Faith) [src-002]. Defenders embody protection and guardianship of the innocent; every Defender crypt card carries [[entities/disciplines/defense|Defense]] as its signature virtue. Imbued are generally not targetable by vampire-only effects and use Convictions + Power library cards rather than several regular library slots; see the gap flag under Related.

## Virtues (card-db signature)

Of 3 Defender crypt cards, superior virtue frequencies are:

- [[entities/disciplines/defense|Defense]] — `[def]` — **3** (universal on Defender).
- [[entities/disciplines/innocence|Innocence]] — `[inn]` — 1 (cross-creed).
- [[entities/disciplines/judgment|Judgment]] — `[jud]` — 1 (cross-creed).
- [[entities/disciplines/vengeance|Vengeance]] — `[ven]` — 1 (cross-creed).

## Card counts (src-002 snapshot 2026-04-18)

- Crypt cards printed as Defender: **3**
- Crypt cards carrying Defense: 3 (all of them).
- Library cards referencing "Defender": 2 (name/text hits).

## Notable members

- **Jack "Hannibal137" Harmon** (cap 4, group 4) — `def/jud`.
- **Lupe "Cabbie22" Droin** (cap 4, group 4) — `def/ven`.
- **Xian "DziDzat155" Quan** (cap 4, group 4) — `def/inn`.

## Imbued mechanics (summary)

- Imbued are **mortals with True Faith**, not vampires — vampire-only card effects do not target them [src-002].
- Imbued use **Conviction** and **Power** library card types in combination with virtues, in place of several vampire-discipline card types [src-002].
- No dedicated ruling page for Imbued mechanics (True Faith, Convictions, imbuement, targeting restrictions) exists yet — **gap flag**.

## Query

Reproducible filter:

```
# All Defender crypt cards
jq '.[] | select(.clans[]? == "Defender") | .name' card-db/crypt.json

# Superior virtue frequency on Defender
jq -r '[.[] | select(.clans[]? == "Defender") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({virtue: .[0], count: length}) | sort_by(-.count) | .[] | "\(.virtue) \(.count)"' card-db/crypt.json
```

## Related

- [[entities/disciplines/defense|Defense]] — creed-defining virtue.
- [[entities/disciplines/innocence|Innocence]], [[entities/disciplines/judgment|Judgment]], [[entities/disciplines/vengeance|Vengeance]] — cross-creed virtues.
- [[entities/creeds/avenger|Avenger]], [[entities/creeds/innocent|Innocent]], [[entities/creeds/judge|Judge]], [[entities/creeds/martyr|Martyr]], [[entities/creeds/redeemer|Redeemer]], [[entities/creeds/visionary|Visionary]] — other six creeds.
- **Gap:** no `wiki/rulings/` page for Imbued / True Faith / Convictions mechanics yet.

## Sources

- src-002 — krcg vtes.json snapshot 2026-04-18 (Imbued crypt, virtue frequencies).
