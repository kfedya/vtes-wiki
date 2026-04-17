---
type: entity
tags: [clan, 5e-playable, tzimisce, sabbat, anarch]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Tzimisce

## Overview

Tzimisce is a V5-playable clan [src-001 p. 53]. Their in-clan disciplines of Animalism, Dominate, and Vicissitude define a fleshcrafting, animal-commanding, will-bending profile — the Sabbat's twisted aristocrats. Card-db evidence: of 67 Tzimisce vampires, `ANI` (39), `VIC` (35), and `AUS` (32) are the most common superior disciplines, with `DOM` (12) behind; note `AUS` leads `DOM` at superior due to many legacy Tzimisce printing Auspex over Dominate [src-002].

## In-clan disciplines (V5)

- [[entities/disciplines/animalism|Animalism]] — `[ani]`
- [[entities/disciplines/dominate|Dominate]] — `[dom]`
- [[entities/disciplines/vicissitude|Vicissitude]] — `[vic]`

Also frequent at superior on legacy crypt: [[entities/disciplines/auspex|Auspex]] — `[aus]` (32 superior printings).

## Sect alignment

Primarily **Sabbat** — 13 of 67 Tzimisce print `Sabbat.` in full [src-002]. The clan is a co-founding pillar of the Sabbat. A modest **Anarch** contingent (4) exists, along with 1 **Laibon** and 1 **Independent** printing.

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **67**
- Crypt vampires with `[ANI]` at superior: **39**
- Crypt vampires with `[VIC]` at superior: **35**
- Crypt vampires with `[AUS]` at superior: **32**
- Crypt vampires with `[DOM]` at superior: **12**
- Library cards referencing "Tzimisce" in name or text: **10**

## Notable members

- **Sha-Ennu** (cap 11, group 4) — Tzimisce regent; `obf/tha/ANI/AUS/CHI/VIC`.
- **The Dracon** (cap 11, group 5) — methuselah-tier; `ANI/AUS/POT/THA/VIC`.
- **Lambach** (cap 10, group 2) — Tzimisce priscus; `pre/ANI/AUS/DOM/VIC`.
- **Count Vladimir Rustovitch** (cap 9, group 4) — voivode template; `dom/pot/pro/ANI/AUS/VIC`.
- **Cyscek** (cap 10, group 4) — `dem/ANI/AUS/OBF/VIC`.

## Typical deck archetypes

- **Tzimisce wall** — ANI + AUS intercept with VIC combat for finishing; extremely resilient.
- **Vicissitude combat / fleshcrafting** — VIC natural-weapon strikes (Chiropteran Marauder, Horrid Form) + ANI retainers.
- **Sabbat dominate bleed** — DOM bleed with VIC combat backup; Sabbat titles (bishop/archbishop).

## Query

Reproducible filters:

```
# All crypt vampires of the clan
jq '.[] | select(.clans[]? == "Tzimisce") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Tzimisce") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("Tzimisce"; "i")) or (.card_text // "" | test("Tzimisce"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/sects/sabbat]] — primary sect alignment.
- [[entities/sects/anarch]] — secondary contingent.
- [[entities/disciplines/animalism]] — animal retainers + swarm combat.
- [[entities/disciplines/dominate]] — bleed increase + Deflection bounce.
- [[entities/disciplines/vicissitude]] — fleshcrafting; natural-weapon combat.
- [[entities/disciplines/auspex]] — intercept; common at superior on legacy crypt.

## Sources

- src-001 — VTES 5E Rulebook (playable-clan list, p. 53 Quick Reference icons).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
