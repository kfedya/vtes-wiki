---
type: entity
tags: [clan, 5e-core, nosferatu, camarilla]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Nosferatu

## Overview

Nosferatu is one of the five core 5E clans [src-001 p. 53]. Their in-clan disciplines of Animalism, Obfuscate, and Potence place them at the intersection of stealth-bleed and combat-grapple. Card-db evidence: of 91 Nosferatu vampires, `OBF` (51), `POT` (45), and `ANI` (37) are the most common superior disciplines, confirming the V5 signature set [src-002].

## In-clan disciplines (V5)

- [[entities/disciplines/animalism|Animalism]] — `[ani]`
- [[entities/disciplines/obfuscate|Obfuscate]] — `[obf]`
- [[entities/disciplines/potence|Potence]] — `[pot]`

## Sect alignment

Primarily **Camarilla** — 21 of 91 Nosferatu vampires print `Camarilla.` in full, with a few Camarilla primogens. **Sabbat** Nosferatu exist (3 explicit printings plus the **Nosferatu antitribu** clan, 44 crypt entries). **Anarch** Nosferatu barons appear in post-V5 printings (e.g., Anarch Baron of Fortaleza, of Versailles) [src-002].

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **91**
- Crypt vampires with `[OBF]` at superior: **51**
- Crypt vampires with `[POT]` at superior: **45**
- Crypt vampires with `[ANI]` at superior: **37**
- Library cards referencing "Nosferatu" in name or text: **22**

## Notable members

- **Baba Yaga, the Iron Hag** (cap 11, group 5) — iconic methuselah; `ANI / AUS / FOR / OBF / POT / THA`.
- **Harrod** (cap 11, group 2) — classic high-cap Nosferatu; `aus / pre / ANI / CEL / OBF / POT`.
- **Josef von Bauren** (cap 11, group 4) — `cel / ANI / DEM / OBF / POT`.
- **Ellison Humboldt** (cap 9, group 3) — Camarilla primogen; `pro / ANI / OBF / POT / PRE`.
- 5E-era printing: **Lenny Burkhead** (cap 6, group 6) — modern baseline Nosferatu.

## Typical deck archetypes

- **Nosferatu stealth-bleed** — OBF stealth modifiers (Cloak the Gathering, etc.) pairing with cheap bleed actions; see [[stealth-modifiers]].
- **Animalism retainer swarm** — ANI retainers (Raven Spy, Homunculus) for intercept and hit-and-hide.
- **Royalty / grapple combat** — POT hand-strikes plus grapple (Immortal Grapple, Torn Signpost in legacy); beefy combat turn.

## Query

Reproducible filters:

```
# All crypt vampires of the clan
jq '.[] | select(.clans[]? == "Nosferatu") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Nosferatu") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("Nosferatu"; "i")) or (.card_text // "" | test("Nosferatu"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/sects/camarilla]] — primary sect alignment.
- [[entities/disciplines/animalism]] — retainer + swarm combat.
- [[entities/disciplines/obfuscate]] — stealth modifiers; see also [[stealth-modifiers]].
- [[entities/disciplines/potence]] — hand-strike damage + grapple.

## Sources

- src-001 — VTES 5E Rulebook (core-5 clan list, p. 53 Quick Reference icons).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
