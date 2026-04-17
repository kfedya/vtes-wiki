---
type: entity
tags: [creed, imbued]
sources: [src-002]
last_verified: 2026-04-18
status: draft
---

# Redeemer

## Overview

Redeemer is one of seven Imbued **creeds** — the "clan" analogue for Imbued minions (mortals with True Faith) [src-002]. Redeemers embody the work of redemption: salvaging the damned and restoring virtue; every Redeemer crypt card carries [[entities/disciplines/redemption|Redemption]] as its signature virtue. Imbued are generally not targetable by vampire-only effects and use Convictions + Power library cards rather than several regular library slots; see the gap flag under Related.

## Virtues (card-db signature)

Of 3 Redeemer crypt cards, superior virtue frequencies are:

- [[entities/disciplines/redemption|Redemption]] — `[red]` — **3** (universal on Redeemer).
- [[entities/disciplines/innocence|Innocence]] — `[inn]` — 1 (cross-creed).
- [[entities/disciplines/judgment|Judgment]] — `[jud]` — 1 (cross-creed).
- [[entities/disciplines/vengeance|Vengeance]] — `[ven]` — 1 (cross-creed).
- [[entities/disciplines/vision|Vision]] — `[viz]` — 1 (cross-creed).

## Card counts (src-002 snapshot 2026-04-18)

- Crypt cards printed as Redeemer: **3**
- Crypt cards carrying Redemption: 3 (all of them).
- Library cards referencing "Redeemer": 0 (no name/text hits — Redeemer identity is virtue-gated).

## Notable members

- **Leaf "Potter116" Pankowski** (cap 4, group 4) — `inn/red/viz`.
- **Marion "Teacher193" Perks** (cap 4, group 4) — `red/jud`.
- **Peter "Outback295" Rophail** (cap 4, group 4) — `red/ven`.

## Imbued mechanics (summary)

- Imbued are **mortals with True Faith**, not vampires — vampire-only card effects do not target them [src-002].
- Imbued use **Conviction** and **Power** library card types in combination with virtues, in place of several vampire-discipline card types [src-002].
- No dedicated ruling page for Imbued mechanics (True Faith, Convictions, imbuement, targeting restrictions) exists yet — **gap flag**.

## Query

Reproducible filter:

```
# All Redeemer crypt cards
jq '.[] | select(.clans[]? == "Redeemer") | .name' card-db/crypt.json

# Superior virtue frequency on Redeemer
jq -r '[.[] | select(.clans[]? == "Redeemer") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({virtue: .[0], count: length}) | sort_by(-.count) | .[] | "\(.virtue) \(.count)"' card-db/crypt.json
```

## Related

- [[entities/disciplines/redemption|Redemption]] — creed-defining virtue.
- [[entities/disciplines/innocence|Innocence]], [[entities/disciplines/judgment|Judgment]], [[entities/disciplines/vengeance|Vengeance]], [[entities/disciplines/vision|Vision]] — cross-creed virtues.
- [[entities/creeds/avenger|Avenger]], [[entities/creeds/defender|Defender]], [[entities/creeds/innocent|Innocent]], [[entities/creeds/judge|Judge]], [[entities/creeds/martyr|Martyr]], [[entities/creeds/visionary|Visionary]] — other six creeds.
- **Gap:** no `wiki/rulings/` page for Imbued / True Faith / Convictions mechanics yet.

## Sources

- src-002 — krcg vtes.json snapshot 2026-04-18 (Imbued crypt, virtue frequencies).
