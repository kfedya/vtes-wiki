---
type: entity
tags: [clan, 5e-core, malkavian, camarilla]
sources: [src-001, src-002, src-012]
last_verified: 2026-04-18
status: verified
---

# Malkavian

## Overview

Malkavian is one of the five core 5E clans [src-001 p. 53]. Their in-clan disciplines of Auspex, Dominate, and Obfuscate push the clan toward intercept-plus-bleed and stealth-bleed decks, often flavored by madness-themed cards (derangements, dementia). Card-db evidence: of 86 Malkavian vampires, `AUS` (50), `OBF` (45), and `DOM` (18) are the most common superior disciplines (alongside Dementation `DEM` from legacy printings) [src-002].

## In-clan disciplines (V5)

- [[entities/disciplines/auspex|Auspex]] — `[aus]`
- [[entities/disciplines/dominate|Dominate]] — `[dom]`
- [[entities/disciplines/obfuscate|Obfuscate]] — `[obf]`

## Sect alignment

Primarily **Camarilla** — 24 of 86 Malkavian vampires print the `Camarilla.` text in full, and many more carry Camarilla titles (primogen, prince, justicar). A handful of **Anarch** printings exist (post-V5 barons, standalone Anarch Malkavians), and **Malkavian antitribu** (43 crypt entries) represent the legacy Sabbat offshoot [src-002].

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **86**
- Crypt vampires with `[AUS]` at superior: **50**
- Crypt vampires with `[OBF]` at superior: **45**
- Crypt vampires with `[DOM]` at superior: **18**
- Library cards referencing "Malkavian" in name or text: **22**

## Notable members

- Alexandra (Toreador, not Malkavian — see toreador.md); the comparable Malkavian icon is **Unmada** (cap 10, group 5) — methuselah-tier priscus with `AUS/DEM/OBF/VIC`.
- **Lutz von Hohenzollern** (cap 11, group 4) — Camarilla justicar template; `pot / AUS / DEM / OBF / PRE`.
- **Leandro** (cap 11, group 2) — Camarilla Malkavian Inner Circle; `cel / dom / AUS / OBF / PRE`.
- **Rachel Brandywine** (cap 10, group 3) — `ani / AUS / DEM / OBF / PRO`.
- **Maris Streck** (cap 9, group 3) — Camarilla prince; `ani / dem / dom / AUS / OBF`.
- 5E-era printing: **Alexander Silverson** (cap 8, group 6) — a modern baseline Malkavian.

## Typical deck archetypes

- **Malkavian intercept-bleed** — AUS reactions (intercept) paired with DOM bleed modifiers; the classic Camarilla Malkavian build.
- **Stealth-bleed (MMPA / Malk-stealth-bleed)** — OBF stealth modifiers + DOM or DEM bleed bombs.
- **Dementation / chaos decks** — legacy archetype leveraging `DEM` for "confusion of the eye"-style attack modifiers (legacy-era, fewer printings in V5).
- [[archetypes/malk-22|Malk' 22]] — top-tier V5 Malkavian stealth-and-bleed; descendant of Malk' 94; Govern × 17 ramp into pure bleed-attack with Conditioning × 7 + 30 stealth modifiers; zero combat cards [src-012].

## Query

Reproducible filters:

```
# All crypt vampires of the clan
jq '.[] | select(.clans[]? == "Malkavian") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Malkavian") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("Malkavian"; "i")) or (.card_text // "" | test("Malkavian"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/sects/camarilla]] — primary sect alignment.
- [[entities/disciplines/auspex]] — primary intercept discipline.
- [[entities/disciplines/dominate]] — bleed increase + Deflection bounce.
- [[entities/disciplines/obfuscate]] — stealth modifiers; see also [[stealth-modifiers]].

## Sources

- src-001 — VTES 5E Rulebook (core-5 clan list, p. 53 Quick Reference icons).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
- src-012 — Codex of the Damned — Malk' 22 archetype (top-tier V5 Malkavian stealth-and-bleed; DOM/OBF, no combat).
