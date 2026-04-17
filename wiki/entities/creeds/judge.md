---
type: entity
tags: [creed, imbued]
sources: [src-002]
last_verified: 2026-04-18
status: draft
---

# Judge

## Overview

Judge is one of seven Imbued **creeds** — the "clan" analogue for Imbued minions (mortals with True Faith) [src-002]. Judges embody decisive judgment of monstrosity, meting out punishment where warranted; every Judge crypt card carries [[entities/disciplines/judgment|Judgment]] as its signature virtue. The Judge creed is the smallest of the seven (2 crypt cards) in the current card-db snapshot. Imbued are generally not targetable by vampire-only effects and use Convictions + Power library cards rather than several regular library slots; see the gap flag under Related.

## Virtues (card-db signature)

Of 2 Judge crypt cards, superior virtue frequencies are:

- [[entities/disciplines/judgment|Judgment]] — `[jud]` — **2** (universal on Judge).
- [[entities/disciplines/defense|Defense]] — `[def]` — 1 (cross-creed).
- [[entities/disciplines/innocence|Innocence]] — `[inn]` — 1 (cross-creed).

## Card counts (src-002 snapshot 2026-04-18)

- Crypt cards printed as Judge: **2**
- Crypt cards carrying Judgment: 2 (all of them).
- Library cards referencing "Judge": 1 (name/text hits).

## Notable members

- **Erick "Shophet125" Franco** (cap 4, group 4) — `inn/jud`.
- **François "Warden" Loehr** (cap 3, group 4) — `def/jud`. Also appears on the Defender creed side (dual-virtue crypt).

## Imbued mechanics (summary)

- Imbued are **mortals with True Faith**, not vampires — vampire-only card effects do not target them [src-002].
- Imbued use **Conviction** and **Power** library card types in combination with virtues, in place of several vampire-discipline card types [src-002].
- No dedicated ruling page for Imbued mechanics (True Faith, Convictions, imbuement, targeting restrictions) exists yet — **gap flag**.

## Query

Reproducible filter:

```
# All Judge crypt cards
jq '.[] | select(.clans[]? == "Judge") | .name' card-db/crypt.json

# Superior virtue frequency on Judge
jq -r '[.[] | select(.clans[]? == "Judge") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({virtue: .[0], count: length}) | sort_by(-.count) | .[] | "\(.virtue) \(.count)"' card-db/crypt.json
```

## Related

- [[entities/disciplines/judgment|Judgment]] — creed-defining virtue.
- [[entities/disciplines/defense|Defense]], [[entities/disciplines/innocence|Innocence]] — cross-creed virtues.
- [[entities/creeds/avenger|Avenger]], [[entities/creeds/defender|Defender]], [[entities/creeds/innocent|Innocent]], [[entities/creeds/martyr|Martyr]], [[entities/creeds/redeemer|Redeemer]], [[entities/creeds/visionary|Visionary]] — other six creeds.
- **Gap:** no `wiki/rulings/` page for Imbued / True Faith / Convictions mechanics yet.

## Sources

- src-002 — krcg vtes.json snapshot 2026-04-18 (Imbued crypt, virtue frequencies).
