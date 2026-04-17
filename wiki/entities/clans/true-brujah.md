---
type: entity
tags: [clan, legacy, true-brujah, brujah-antecedents, tiny-bloodline, single-clan-discipline]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# True Brujah

## Overview

True Brujah is a legacy **tiny antecedent bloodline** — stoic, time-manipulating vampires claiming descent from the original Brujah antediluvian before Troile's diablerie reshaped the clan [src-002]. Card-db evidence: of 10 True Brujah, `TEM` (10), `POT` (8), and `PRE` (7) dominate superior disciplines — Temporis is single-clan to True Brujah and appears on every entry, paired with Potence and Presence [src-002]. At only 10 vampires, True Brujah is one of the smallest bloodlines in the game.

## In-clan disciplines (V5)

Not V5-playable. Legacy signature (from card-db frequency):

- [[entities/disciplines/potence|Potence]] — `[pot]`
- [[entities/disciplines/presence|Presence]] — `[pre]`
- [[entities/disciplines/temporis|Temporis]] — `[tem]`

Some True Brujah also carry Auspex (2 superior printings) as a fourth legacy discipline — the card-db confirms it but it is secondary.

## Sect alignment

Printed sect splits between **Independent** (Al-Muntaquim, Ibn Khaldun, Krassimir, Lydia, Mikael, Nehemiah, Nu, Shalmath, Synesios — most of the bloodline) and **Sabbat** (Al-Muntathir) [src-002]. True Brujah frequently print **Scarce** (3-pool penalty for contested vampires) — see [[traits#Scarce]].

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **10**
- Crypt vampires with `[TEM]` at superior: **10** (every True Brujah has TEM at superior)
- Crypt vampires with `[POT]` at superior: **8**
- Crypt vampires with `[PRE]` at superior: **7**
- Library cards referencing "True Brujah" in name or text: **2**

## Notable members

- **Shalmath** (cap 10, group 6) — Independent; `POT/PRE/TEM`; pure in-clan signature.
- **Lydia, Grand Praetor** (cap 9, group 6) — Independent, 1 vote (titled); `dom/pre/AUS/FOR/POT/TEM`.
- **Nehemiah** (cap 9, group 4) — Independent, 2 votes (titled); `obt/POT/PRE/SER/TEM`.
- **Nu, The Pillar** (cap 9, group 2) — Independent; `ani/aus/pro/POT/PRE/TEM`.
- **Al-Muntaquim, The Avenger** (cap 8, group 4) — Independent; `obf/pre/FOR/POT/TEM`; can burn a Caitiff for +1 bleed buff.

## Typical deck archetypes

- **Temporis stall / action-replay** — TEM cards (Patience of the Norns, Breath of the Dragon) to recur action modifiers and stop actions in their tracks.
- **True Brujah vote** — Independent title votes (Lydia, Nehemiah) + PRE vote-boost for political presence.
- **TEM/POT combat** — rare combination; Temporis cards cancel strikes, Potence supplies hand-strike damage.

## Query

Reproducible filters:

```
# All crypt vampires of the clan
jq '.[] | select(.clans[]? == "True Brujah") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "True Brujah") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("True Brujah"; "i")) or (.card_text // "" | test("True Brujah"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/sects/independent]] — primary sect alignment.
- [[entities/disciplines/temporis]] — single-clan signature; time-manipulation.
- [[entities/disciplines/potence]] — in-clan; hand-strike combat.
- [[entities/disciplines/presence]] — in-clan; vote boost.
- [[entities/clans/brujah]] — sibling clan (Brujah are the Troile-line; True Brujah claim the original lineage).
- [[traits#Scarce]] — 3-pool contested-vampire penalty many True Brujah carry.

## Sources

- src-001 — VTES 5E Rulebook (clan list; Scarce trait p. 41).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
