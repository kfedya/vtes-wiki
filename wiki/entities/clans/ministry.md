---
type: entity
tags: [clan, 5e-playable, ministry, followers-of-set, v5-rebrand, independent, anarch]
sources: [src-001, src-002, src-004, src-008]
last_verified: 2026-04-18
status: verified
---

# Ministry

## Overview

Ministry is the V5 rebrand of the legacy **Followers of Set** clan, and is V5-playable [src-001 p. 53]. The V5 signature disciplines are Obfuscate, Presence, and Protean — temptation, seduction, and serpent-form. Card-db evidence: of 81 Ministry vampires (the snapshot has renamed the legacy Followers of Set roster under this name), `PRE` (44), `SER` (42, legacy Serpentis), and `OBF` (39) dominate superior disciplines [src-002].

## V5 rebrand

The card-db has consolidated all former "Follower of Set" / "Serpents of the Light" crypt entries under "Ministry" (0 crypt entries remain under the legacy names). The V5-era in-clan is **Obfuscate / Presence / Protean**, dropping legacy **Serpentis** from the signature trio — though `SER` remains the most-printed legacy discipline on crypt and on ~22 library cards. Legacy cards referencing "Follower of Set" / "Followers of Set" remain legal; ~22 library cards match.

## In-clan disciplines (V5)

- [[entities/disciplines/obfuscate|Obfuscate]] — `[obf]`
- [[entities/disciplines/presence|Presence]] — `[pre]`
- [[entities/disciplines/protean|Protean]] — `[pro]`

Legacy signature (on most pre-V5 crypt): [[entities/disciplines/serpentis|Serpentis]] — `[ser]`.

## Sect alignment

Overwhelmingly **Independent** — 22 of 81 vampires print `Independent.` in full [src-002]. Legacy lore keeps the clan aloof from sect politics; V5 printings bring an **Anarch** contingent (8) and a small **Sabbat** legacy faction (3).

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras, all renamed under Ministry): **81**
- Crypt vampires with `[PRE]` at superior: **44**
- Crypt vampires with `[SER]` at superior (legacy signature): **42**
- Crypt vampires with `[OBF]` at superior: **39**
- Crypt vampires with `[PRO]` at superior (V5 signature): **10**
- Library cards referencing "Ministry" in name or text: **1**
- Library cards referencing "Follower of Set" / "Followers of Set" in name or text (legacy, still legal): **22**

## Notable members

- **Nakhthorheb** (cap 10, group 4) — `OBF/PRE/SER`; methuselah-tier.
- **Kemintiri** (cap 10, group 2) — Antediluvian-tier; `aus/dom/OBF/PRE/SER/THA`.
- **Nefertiti** (cap 10, group 2) — `cel/pot/DOM/OBF/PRE/SER`.
- **Nehsi** (cap 10, group 2) — `aus/for/OBF/PRE/PRO/SER`.
- **Agnieszka, Tempter of Legions** (cap 10, group 6) — V5-era printing; `for/pot/AUS/OBF/PRE/PRO`.

## Typical deck archetypes

- **Stealth-bleed** — OBF stealth modifiers + PRE vote/bleed pressure; classic Ministry.
- **Temptation / corruption** — legacy SER combat + temptation action cards; long-game manipulation.
- **V5 Ministry (Anarch)** — PRO + OBF + PRE as Anarch baron; vote + stealth-bleed hybrid.
- **[[archetypes/heshas-emporium|Hesha's Emporium]]** — combo powerbleed around Hesha Ruhadze G6 (+1 bleed per unique equipment). Angel Chavarria setup → equip pile → 20+ bleeds turn 3. 2024 Atlantic Cup winner.
- **[[archetypes/platinum-revelation|Platinum Revelation]]** — top-tier V5 Ministry Anarch stealth-and-bleed; The Platinum Protocol × 10 triple-discipline bleed + corruption-counter engine (Revelation of the Serpent / Enchanting Gaze); Dabbler × 3 economy. EC 2023 Day 2 (Jonas Ståhle, TWDA id 11032) [src-008].

## Query

Reproducible filters:

```
# All crypt vampires of the clan
jq '.[] | select(.clans[]? == "Ministry") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Ministry") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing legacy Followers of Set
jq -s '[.[][] | select((.name // "" | test("Follower of Set|Followers of Set"; "i")) or (.card_text // "" | test("Follower of Set|Followers of Set"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/sects/independent]] — primary sect alignment.
- [[entities/sects/anarch]] — V5-era contingent; 2 votes per baron.
- [[entities/disciplines/obfuscate]] — V5 signature; stealth modifiers.
- [[entities/disciplines/presence]] — V5 signature; vote boost + Majesty.
- [[entities/disciplines/protean]] — V5 signature; shapeshifting.
- [[entities/disciplines/serpentis]] — legacy signature; largely superseded in V5 printings.

## Sources

- src-001 — VTES 5E Rulebook (playable-clan list, p. 53 Quick Reference icons).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
- src-004 — Codex of the Damned — Hesha's Emporium archetype page (Hesha G6 +1 bleed per unique equipment; V5 Ministry combo archetype).
- src-008 — Codex of the Damned — Platinum Revelation archetype (V5 Ministry Anarch stealth-bleed; Platinum Protocol OBF/PRE/PRO triple-discipline action + corruption-counter engine).
