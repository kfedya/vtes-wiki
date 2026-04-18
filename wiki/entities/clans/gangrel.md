---
type: entity
tags: [clan, 5e-playable, gangrel, independent, anarch, camarilla]
sources: [src-001, src-002, src-005, src-017]
last_verified: 2026-04-18
status: verified
---

# Gangrel

## Overview

Gangrel is a V5-playable clan [src-001 p. 53]. Their in-clan disciplines of Animalism, Fortitude, and Protean define a feral bruiser profile — native-weapon combat, damage prevention, and animal retainers. Card-db evidence: of 95 Gangrel vampires, `PRO` (55), `ANI` (46), and `FOR` (45) are the most common superior disciplines, confirming the V5 signature set [src-002].

## In-clan disciplines (V5)

- [[entities/disciplines/animalism|Animalism]] — `[ani]`
- [[entities/disciplines/fortitude|Fortitude]] — `[for]`
- [[entities/disciplines/protean|Protean]] — `[pro]`

## Sect alignment

Heavily split: **Independent** (13 printed) and **Camarilla** (10) are the leading factions, with an active **Anarch** contingent (8) [src-002]. Legacy lore has Gangrel abandoning the Camarilla in the modern nights, and the 58-vampire **Gangrel antitribu** lineage represents the Sabbat offshoot. V5-era printings trend Anarch / Independent.

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **95**
- Gangrel antitribu crypt vampires: **58**
- Crypt vampires with `[PRO]` at superior: **55**
- Crypt vampires with `[ANI]` at superior: **46**
- Crypt vampires with `[FOR]` at superior: **45**
- Library cards referencing "Gangrel" in name or text: **23**

## Notable members

- **Fakir al Sidi** (cap 11, group 4) — `abo/ANI/FOR/PRE/PRO/THA`.
- **Stanislava** (cap 11, group 2) — `ANI/CEL/DOM/FOR/PRO`.
- **Karsh** (cap 10, group 3) — iconic Gangrel warlord; `ANI/CEL/FOR/POT/PRO`.
- **Angus the Unruled** (cap 10, group 1) — `cel/for/pot/ANI/PRO`.
- **Matasuntha** (cap 10, group 5) — `ANI/AUS/CEL/FOR/PRO`.

## Typical deck archetypes

- **Gangrel wall / weenie-wall** — ANI reactions (On the Qui Vive, Cats' Guidance) + FOR damage-prevent; tanks combat and intercepts bleeds.
- **Protean combat / native weapons** — PRO Flesh of Marble + Form of Mist + native-weapon strikes for resilient slow aggression.
- **Anarch Gangrel swarm** — cheap Anarch Gangrels leveraging animal retainers (Raven Spy) and baron-title politics.
- [[archetypes/gangrel-thing|Gangrel Thing]] — top-tier grind-bleed / intercept wall using Thing × 5 to fan out Anarch Barons; Codex-classified ⭐ Top Dog [src-005].
- [[archetypes/stanislava|Stanislava]] — top-tier Camarilla Gangrel Inner Circle stealth-vote; Stanislava × 5 as the flagship cap-11 bleeder (+2 bleed, allies can't block); Zillah's Valley × 8 ramp + Kine Resources Contested × 6 + Protean stealth-combat stack [src-017].

## Query

Reproducible filters:

```
# All crypt vampires of the clan
jq '.[] | select(.clans[]? == "Gangrel") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Gangrel") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("Gangrel"; "i")) or (.card_text // "" | test("Gangrel"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/sects/independent]] — plurality sect alignment.
- [[entities/sects/anarch]] — 5E-era tilt; 2 votes per baron.
- [[entities/sects/camarilla]] — historical alignment retained by some printings.
- [[entities/disciplines/animalism]] — animal retainers + swarm combat.
- [[entities/disciplines/fortitude]] — damage prevention.
- [[entities/disciplines/protean]] — shapeshifting / native weapons / earth-meld.

## Sources

- src-001 — VTES 5E Rulebook (playable-clan list, p. 53 Quick Reference icons).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
- src-005 — Codex of the Damned — Gangrel Thing archetype (top-tier Anarch Baron wall).
- src-017 — Codex of the Damned — Stanislava archetype (top-tier Camarilla Gangrel Inner Circle stealth-vote/bleed).
