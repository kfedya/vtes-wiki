---
type: entity
tags: [creed, imbued]
sources: [src-002]
last_verified: 2026-04-18
status: draft
---

# Innocent

## Overview

Innocent is one of seven Imbued **creeds** — the "clan" analogue for Imbued minions (mortals with True Faith) [src-002]. Innocents embody faith-preserving purity and youth; every Innocent crypt card carries [[entities/disciplines/innocence|Innocence]] as its signature virtue. Imbued are generally not targetable by vampire-only effects and use Convictions + Power library cards rather than several regular library slots; see the gap flag under Related.

## Virtues (card-db signature)

Of 3 Innocent crypt cards, superior virtue frequencies are:

- [[entities/disciplines/innocence|Innocence]] — `[inn]` — **3** (universal on Innocent).
- [[entities/disciplines/redemption|Redemption]] — `[red]` — 1 (cross-creed).
- [[entities/disciplines/vengeance|Vengeance]] — `[ven]` — 1 (cross-creed).

## Card counts (src-002 snapshot 2026-04-18)

- Crypt cards printed as Innocent: **3**
- Crypt cards carrying Innocence: 3 (all of them).
- Library cards referencing "Innocent": 1 (name/text hits).

## Notable members

- **Béatrice "Oracle171" Tremblay** (cap 3, group 4) — `inn/ven`.
- **Inez "Nurse216" Villagrande** (cap 3, group 4) — `inn`.
- **Liz "Ticket312" Thornton** (cap 2, group 4) — `inn/red`.

## Imbued mechanics (summary)

- Imbued are **mortals with True Faith**, not vampires — vampire-only card effects do not target them [src-002].
- Imbued use **Conviction** and **Power** library card types in combination with virtues, in place of several vampire-discipline card types [src-002].
- No dedicated ruling page for Imbued mechanics (True Faith, Convictions, imbuement, targeting restrictions) exists yet — **gap flag**.

## Query

Reproducible filter:

```
# All Innocent crypt cards
jq '.[] | select(.clans[]? == "Innocent") | .name' card-db/crypt.json

# Superior virtue frequency on Innocent
jq -r '[.[] | select(.clans[]? == "Innocent") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({virtue: .[0], count: length}) | sort_by(-.count) | .[] | "\(.virtue) \(.count)"' card-db/crypt.json
```

## Related

- [[entities/disciplines/innocence|Innocence]] — creed-defining virtue.
- [[entities/disciplines/redemption|Redemption]], [[entities/disciplines/vengeance|Vengeance]] — cross-creed virtues.
- [[entities/creeds/avenger|Avenger]], [[entities/creeds/defender|Defender]], [[entities/creeds/judge|Judge]], [[entities/creeds/martyr|Martyr]], [[entities/creeds/redeemer|Redeemer]], [[entities/creeds/visionary|Visionary]] — other six creeds.
- **Gap:** no `wiki/rulings/` page for Imbued / True Faith / Convictions mechanics yet.

## Sources

- src-002 — krcg vtes.json snapshot 2026-04-18 (Imbued crypt, virtue frequencies).
