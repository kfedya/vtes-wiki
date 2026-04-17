---
type: entity
tags: [creed, imbued]
sources: [src-002]
last_verified: 2026-04-18
status: draft
---

# Avenger

## Overview

Avenger is one of seven Imbued **creeds** — the "clan" analogue for Imbued minions (mortals with True Faith), who are a distinct minion type from vampires [src-002]. Avengers embody wrath and retribution against the undead; every Avenger crypt card carries [[entities/disciplines/vengeance|Vengeance]] as its signature virtue. Imbued are generally not targetable by vampire-only effects and use Convictions + Power library cards rather than several regular library slots; see the gap flag under Related.

## Virtues (card-db signature)

Of 3 Avenger crypt cards, superior virtue frequencies are:

- [[entities/disciplines/vengeance|Vengeance]] — `[ven]` — **3** (universal on Avenger).
- [[entities/disciplines/judgment|Judgment]] — `[jud]` — 1 (cross-creed).
- [[entities/disciplines/martyrdom|Martyrdom]] — `[mar]` — 1 (cross-creed).
- [[entities/disciplines/vision|Vision]] — `[viz]` — 1 (cross-creed).

## Card counts (src-002 snapshot 2026-04-18)

- Crypt cards printed as Avenger: **3**
- Crypt cards carrying Vengeance: 3 (all of them).
- Library cards referencing "Avenger": 0 (no direct name/text hits — Avenger identity is virtue-gated, not name-gated).

## Notable members

- **Jennifer "Flame61" Vidisania** (cap 4, group 4) — `ven/viz`.
- **John "Cop90" O'Malley** (cap 4, group 4) — `jud/ven`.
- **Pedro Cortez** (cap 4, group 4) — `mar/ven`.

## Imbued mechanics (summary)

- Imbued are **mortals with True Faith**, not vampires — vampire-only card effects do not target them [src-002].
- Imbued use **Conviction** and **Power** library card types in combination with virtues, in place of several vampire-discipline card types [src-002].
- No dedicated ruling page for Imbued mechanics (True Faith, Convictions, imbuement, targeting restrictions) exists yet — **gap flag**.

## Query

Reproducible filter:

```
# All Avenger crypt cards
jq '.[] | select(.clans[]? == "Avenger") | .name' card-db/crypt.json

# Superior virtue frequency on Avenger
jq -r '[.[] | select(.clans[]? == "Avenger") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({virtue: .[0], count: length}) | sort_by(-.count) | .[] | "\(.virtue) \(.count)"' card-db/crypt.json
```

## Related

- [[entities/disciplines/vengeance|Vengeance]] — creed-defining virtue.
- [[entities/disciplines/judgment|Judgment]], [[entities/disciplines/martyrdom|Martyrdom]], [[entities/disciplines/vision|Vision]] — cross-creed virtues.
- [[entities/creeds/judge|Judge]], [[entities/creeds/defender|Defender]], [[entities/creeds/innocent|Innocent]], [[entities/creeds/martyr|Martyr]], [[entities/creeds/redeemer|Redeemer]], [[entities/creeds/visionary|Visionary]] — other six creeds.
- **Gap:** no `wiki/rulings/` page for Imbued / True Faith / Convictions mechanics yet.

## Sources

- src-002 — krcg vtes.json snapshot 2026-04-18 (Imbued crypt, virtue frequencies).
