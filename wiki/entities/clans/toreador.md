---
type: entity
tags: [clan, 5e-core, toreador, camarilla]
sources: [src-001, src-002, src-022]
last_verified: 2026-04-18
status: verified
---

# Toreador

## Overview

Toreador is one of the five core 5E clans [src-001 p. 53]. Their in-clan disciplines of Auspex, Celerity, and Presence give the clan an unusual breadth — they can intercept, rush, and call referendums from the same crypt. Card-db evidence: of 96 Toreador vampires, `PRE` (51), `AUS` (48), and `CEL` (43) are the most common superior disciplines, confirming the V5 signature set [src-002].

## In-clan disciplines (V5)

- [[entities/disciplines/auspex|Auspex]] — `[aus]`
- [[entities/disciplines/celerity|Celerity]] — `[cel]`
- [[entities/disciplines/presence|Presence]] — `[pre]`

## Sect alignment

Primarily **Camarilla** — 26 of 96 Toreador vampires print `Camarilla.` in full, with numerous Camarilla primogen and prince templates. A handful of explicit **Sabbat** printings exist (2), and **Anarch** Toreador (e.g., Aisha az-Zahra as baron) appear in post-V5 printings. **Toreador antitribu** (45 crypt entries) represent the legacy Sabbat offshoot [src-002].

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **96**
- Crypt vampires with `[PRE]` at superior: **51**
- Crypt vampires with `[AUS]` at superior: **48**
- Crypt vampires with `[CEL]` at superior: **43**
- Library cards referencing "Toreador" in name or text: **23**

## Notable members

- **Alexandra** (cap 11, group 2) — iconic Inner Circle Toreador; `dom / ANI / AUS / CEL / PRE`.
- **Rafael de Corazon** (cap 11, group 4) — Camarilla justicar archetype; `AUS / CEL / DOM / OBF / PRE`.
- **François Villon** (cap 10, group 2) — Camarilla prince of Paris; `chi / obf / pot / AUS / CEL / PRE`.
- **Anneke** (cap 10, group 1) — `dom / AUS / CEL / PRE`.
- **Helena** (cap 10, group 3) — classic high-cap methuselah; `obf / pre / tha / AUS / CEL / DOM`.
- 5E-era printing: **Catalina Vega** (cap 8, group 6).

## Typical deck archetypes

- **Toreador Grand Ball / vote** — PRE vote-push (Voter Captivation, Kindred Restructure Committee) piloted by Camarilla princes/primogens.
- **Toreador combat-wall / intercept** — AUS intercept reactions plus CEL extra strikes; often paired with AUS reactions like Telepathic Misdirection.
- **Toreador rush / celerity rush** — CEL additional strikes on mid-cap combat vampires; complements the PRE vote-backbone.
- [[archetypes/forced-ball|Forced Ball]] — runner-up Toreador Camarilla political/vote; Toreador Grand Ball × 7 makes the host unblockable on political actions; Diana Iadanza bypasses Delaying Tactics; Forced March × 4 chains actions via Fortitude [src-022].

## Query

Reproducible filters:

```
# All crypt vampires of the clan
jq '.[] | select(.clans[]? == "Toreador") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Toreador") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("Toreador"; "i")) or (.card_text // "" | test("Toreador"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/sects/camarilla]] — primary sect alignment.
- [[entities/disciplines/auspex]] — primary intercept discipline.
- [[entities/disciplines/celerity]] — additional strikes + dodge.
- [[entities/disciplines/presence]] — vote boost + Majesty combat-ends.
- [[post-combat-effects]] — Voter Captivation timing; Toreador commonly trigger it.

## Sources

- src-001 — VTES 5E Rulebook (core-5 clan list, p. 53 Quick Reference icons).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
- src-022 — Codex of the Damned — Forced Ball archetype (runner-up Toreador Camarilla political/vote via Toreador Grand Ball).
