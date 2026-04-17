---
type: entity
tags: [clan, legacy, osebo, laibon]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Osebo

## Overview

Osebo is a legacy **Laibon tribe** — one of four African vampire tribes from the Ebony Kingdom / Legacies of Blood era [src-002]. The Osebo are leopard-kin hunters and warriors; card-db evidence shows an offensive identity around Celerity, Potence, and Auspex — fast-striking combat paired with intercept rather than vote. Of 16 Osebo crypt vampires, `POT` (9), `AUS` (9), and `CEL` (8) dominate superior disciplines [src-002].

## In-clan disciplines (legacy signature)

- [[entities/disciplines/auspex|Auspex]] — `[aus]`
- [[entities/disciplines/celerity|Celerity]] — `[cel]`
- [[entities/disciplines/potence|Potence]] — `[pot]`

## Sect alignment

Primarily **[[entities/sects/laibon|Laibon]]**. Legacy-only sect, fully legal [src-001 p. 40]. Osebo crypt includes Laibon **magaji** holders (Cesewayo and Cesewayo ADV, Kisha Bhimji, Mamadou Keita). Magaji is non-unique and cannot be contested; 2 votes per ready magaji [src-001 p. 40].

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires: **16**
- Crypt vampires with `[POT]` at superior: **9**
- Crypt vampires with `[AUS]` at superior: **9**
- Crypt vampires with `[CEL]` at superior: **8**
- Library cards referencing "Osebo" in name or text: see query below.

## Notable members

- **Cesewayo** (cap 10, group 4) — Laibon magaji; advanced version gets 2 extra votes; `ani/AUS/CEL/DOM/POT/THA`.
- **Massassi** (cap 9, group 4) — `obf/AUS/CEL/POT/QUI`.
- **Tatu Sawosa** (cap 8, group 4) — `ani/cel/AUS/OBF/POT`.
- **Mamadou Keita** (cap 7, group 4) — Laibon magaji; political-action unpreventable damage; `aus/pot/pre/vic/CEL`.

## Typical deck roles

- **Osebo intercept-rush** — AUS reactions (intercept) + CEL/POT combat; Laibon answer to a Brujah wall archetype.
- **Magaji vote + combat** — 2-vote magaji titles stacked with multi-magaji Laibon crypts.
- **Fast combat finisher** — CEL extra strikes + POT hand-strike damage; mid-to-high capacity elders.

## Query

Reproducible filters:

```
# All crypt vampires of the tribe
jq '.[] | select(.clans[]? == "Osebo") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Osebo") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the tribe by name or text
jq -s '[.[][] | select((.name // "" | test("Osebo"; "i")) or (.card_text // "" | test("Osebo"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/sects/laibon|Laibon]] — parent sect; kholo/magaji title rules.
- [[entities/clans/akunanse|Akunanse]], [[entities/clans/guruhi|Guruhi]], [[entities/clans/ishtarri|Ishtarri]] — the other three Laibon tribes.
- [[entities/disciplines/auspex|Auspex]] — intercept.
- [[entities/disciplines/celerity|Celerity]] — extra strikes.
- [[entities/disciplines/potence|Potence]] — hand-strike damage.

## Sources

- src-001 — VTES 5E Rulebook (Laibon sect rules, p. 40).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, title text).
