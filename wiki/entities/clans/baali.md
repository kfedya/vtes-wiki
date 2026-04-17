---
type: entity
tags: [clan, legacy, baali, infernal, independent]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Baali

## Overview

Baali is a legacy **Infernalist bloodline** — demon-touched vampires originally of Middle Eastern antiquity [src-002]. Card-db evidence: of 18 Baali vampires, `DAI` (13), `OBF` (12), and `PRE` (12) dominate superior disciplines — Daimoinon is the clan-signature discipline (near-single-clan), paired with Obfuscate and Presence as the secondary in-clan pair [src-002]. Many Baali carry the **Infernal trait** (1-pool unlock penalty — see [[traits#Infernal]]).

## In-clan disciplines (V5)

Not V5-playable. Legacy signature (from card-db frequency):

- [[entities/disciplines/daimoinon|Daimoinon]] — `[dai]`
- [[entities/disciplines/obfuscate|Obfuscate]] — `[obf]`
- [[entities/disciplines/presence|Presence]] — `[pre]`

## Sect alignment

Printed sect is almost uniformly **Independent** [src-002]. Baali-combo decks lean on Independent-title rules (no clan-sect bonuses; printed votes per vampire). Many Baali print the **Infernal** trait — these vampires do not unlock normally; the controller must burn 1 pool each unlock phase to ready them [src-001 p. 41].

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **18**
- Crypt vampires with `[DAI]` at superior: **13**
- Crypt vampires with `[OBF]` at superior: **12**
- Crypt vampires with `[PRE]` at superior: **12**
- Library cards referencing "Baali" in name or text: **8**

## Notable members

- **Cybele** (cap 10, group 4) — `ANI/DAI/OBF/PRE/SER/THA`; iconic Baali methuselah.
- **Huitzilopochtli** (cap 10, group 2) — `AUS/DAI/DOM/OBF/POT/PRE`.
- **Nergal** (cap 10, group 5) — advanced printing; `AUS/DAI/FOR/OBF/PRE/THA`.
- **The unnamed** (cap 10, group 6) — `CEL/DAI/OBF/PRE/PRO`.
- **Azaneal** (cap 4, group 4) — **Infernal** trait; cheap 4-cap DAI bleeder.

## Typical deck archetypes

- **Baali demonism / curse** — DAI condemnation + curse cards ([[entities/disciplines/maleficia|Maleficia]] combo: Barrenness, Greater Curse) to lock down rivals. OBF stealth-bleed fills the action engine.
- **Baali vote** — PRE votes at superior + Daimoinon combat intercept / debuff. Lean Independent-title vote counts.
- **Infernal-heavy grind** — accept the 1-pool unlock tax to field multiple Infernal Baali with agenda-driving card text.

## Query

Reproducible filters:

```
# All crypt vampires of the clan
jq '.[] | select(.clans[]? == "Baali") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Baali") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("Baali"; "i")) or (.card_text // "" | test("Baali"; "i")))] | length' card-db/library/*.json

# Infernal Baali (by card_text)
jq -r '.[] | select(.clans[]? == "Baali") | select(.card_text // "" | test("Infernal")) | .name' card-db/crypt.json
```

## Related

- [[entities/sects/independent]] — primary sect alignment.
- [[entities/disciplines/daimoinon]] — clan-signature discipline (near-single-clan).
- [[entities/disciplines/obfuscate]] — in-clan; stealth-bleed.
- [[entities/disciplines/presence]] — in-clan; vote + majesty combat-ends.
- [[entities/disciplines/maleficia]] — Daimoinon combo-code; Baali-centric cards.
- [[traits#Infernal]] — 1-pool unlock penalty many Baali carry.

## Sources

- src-001 — VTES 5E Rulebook (clan list, p. 53 Quick Reference icons; Infernal trait p. 41).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
