---
type: entity
tags: [clan, 5e-core, tremere, camarilla]
sources: [src-001, src-002, src-013]
last_verified: 2026-04-18
status: verified
---

# Tremere

## Overview

Tremere is one of the five core 5E clans [src-001 p. 53]. Their in-clan disciplines of Auspex, Blood Sorcery, and Dominate pair reactive intercept with aggressive bleed and a combat toolbox built on ranged Blood Sorcery cards. Card-db evidence: of 91 Tremere vampires, `THA` (65), `AUS` (48), and `DOM` (42) are the most common superior disciplines, confirming the V5 signature set (Blood Sorcery still keyed as `tha/THA` in card-db) [src-002].

## In-clan disciplines (V5)

- [[entities/disciplines/auspex|Auspex]] — `[aus]`
- [[entities/disciplines/blood-sorcery|Blood Sorcery]] — `[tha]`
- [[entities/disciplines/dominate|Dominate]] — `[dom]`

## Sect alignment

Primarily **Camarilla** — 24 of 91 Tremere vampires print `Camarilla.` in full, with multiple Camarilla primogens and at least one Camarilla Prince (Addis Ababa). **Anarch** Tremere exist in small numbers (Anarch Baron of Manila, stand-alone Anarch Tremere). **Tremere antitribu** (43 crypt entries) represent the legacy Sabbat offshoot [src-002].

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **91**
- Crypt vampires with `[THA]` at superior: **65**
- Crypt vampires with `[AUS]` at superior: **48**
- Crypt vampires with `[DOM]` at superior: **42**
- Library cards referencing "Tremere" in name or text: **28** (highest of the 5 core clans)

## Notable members

- **Etrius** (cap 11, group 2) — iconic Camarilla justicar / Inner Circle; `pro / AUS / DOM / OBF / THA`.
- **Mistress Fanchon** (cap 11, group 4) — `AUS / CEL / DOM / OBF / THA / VIC`.
- **Lord Tremere** (cap 11, group 5) — clan founder template; `obe / ANI / AUS / DOM / THA / VIC`.
- **Ulugh Beg, The Watcher** (cap 10, group 1) — `cel / for / pot / AUS / DOM / THA`.
- **Karl Schrekt** (cap 10, group 6) — `AUS / DOM / FOR / PRE / THA`.
- 5E-era printing: **Inês Tristão** (cap 6, group 6).

## Typical deck archetypes

- **Tremere wall / intercept-backup** — AUS reactions at base; `THA` cards like Theft of Vitae and Blood Rage plug combat gaps; Deflection (DOM) bounces bleeds.
- **Tremere bleed / govern** — DOM bleed modifiers (Conditioning, Govern the Unaligned) with AUS reactions for defense; extremely resilient.
- **Blood Sorcery combat / ranged** — THA-based ranged combat cards (Theft of Vitae, Apportation, Rego Motus), with AUS reaction backup.
- [[archetypes/mistress|Mistress]] — top-tier Tremere Camarilla vote & bleed; Mistress Fanchon Inner Circle; Alastor/Helicopter combo; 32-master pile; Obedience × 4 + Deflection × 4 defence [src-013].

## Query

Reproducible filters:

```
# All crypt vampires of the clan
jq '.[] | select(.clans[]? == "Tremere") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Tremere") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("Tremere"; "i")) or (.card_text // "" | test("Tremere"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/sects/camarilla]] — primary sect alignment.
- [[entities/disciplines/auspex]] — primary intercept discipline.
- [[entities/disciplines/blood-sorcery]] — ranged combat + blood rituals.
- [[entities/disciplines/dominate]] — bleed increase + Deflection bounce.
- [[wiki/cards/theft-of-vitae|theft-of-vitae]] — signature Blood Sorcery combat card (has a dedicated page).

## Sources

- src-001 — VTES 5E Rulebook (core-5 clan list, p. 53 Quick Reference icons).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
- src-013 — Codex of the Damned — Mistress archetype (top-tier Tremere/multi-clan Camarilla vote & bleed; Mistress Fanchon Inner Circle Alastor/Helicopter combo).
