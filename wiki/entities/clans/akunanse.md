---
type: entity
tags: [clan, legacy, akunanse, laibon]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Akunanse

## Overview

Akunanse is a legacy **Laibon tribe** — one of four African vampire tribes from the Ebony Kingdom / Legacies of Blood era [src-002]. The Akunanse are known as ancestor-communers and totem-bearers; card-db evidence shows a focused identity around Animalism, Fortitude, and Abombwe. Of 16 Akunanse crypt vampires, `FOR` (11), `ABO` (10), and `ANI` (9) dominate superior disciplines [src-002].

## In-clan disciplines (legacy signature)

- [[entities/disciplines/abombwe|Abombwe]] — `[abo]`
- [[entities/disciplines/animalism|Animalism]] — `[ani]`
- [[entities/disciplines/fortitude|Fortitude]] — `[for]`

## Sect alignment

Primarily **[[entities/sects/laibon|Laibon]]**. The Laibon sect is legacy-only (pre-5E) but remains fully legal [src-001 p. 40]. Akunanse crypt includes Laibon **magaji** holders — magaji is a non-unique Laibon title worth 2 votes [src-001 p. 40]. Three Akunanse carry `Laibon magaji` text (Nkule Galadima, Uchenna, Umdava).

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires: **16**
- Crypt vampires with `[FOR]` at superior: **11**
- Crypt vampires with `[ABO]` at superior: **10**
- Crypt vampires with `[ANI]` at superior: **9**
- Library cards referencing "Akunanse" in name or text: see query below.

## Notable members

- **Kamiri wa Itherero** (cap 10, group 4) — top-capacity Akunanse; `pot/qui/ABO/ANI/FOR/OBF`.
- **Umdava** (cap 9, group 4) — Laibon magaji; `vic/ABO/ANI/FOR/PRE`.
- **Matata** (cap 9, group 3) — `aus/cel/obf/ABO/ANI/FOR`.
- **Nkule Galadima** (cap 8, group 4) — Laibon magaji with anti-Lasombra + Edge-vote effect; `ani/aus/pre/ABO/FOR`.

## Typical deck roles

- **Laibon Abombwe stack** — ABO-based totem + hunt ground cards leveraging the tribe's African-predator flavor.
- **Wall / intercept** — FOR damage-prevent + ANI intercept reactions (Aid from Bats, Cats' Guidance).
- **Magaji vote core** — 2-vote magaji titles enable Kindred Restructure-style vote plans inside mixed Laibon crypts.

## Query

Reproducible filters:

```
# All crypt vampires of the tribe
jq '.[] | select(.clans[]? == "Akunanse") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Akunanse") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the tribe by name or text
jq -s '[.[][] | select((.name // "" | test("Akunanse"; "i")) or (.card_text // "" | test("Akunanse"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/sects/laibon|Laibon]] — parent sect; kholo/magaji title rules.
- [[entities/clans/guruhi|Guruhi]], [[entities/clans/ishtarri|Ishtarri]], [[entities/clans/osebo|Osebo]] — the other three Laibon tribes.
- [[entities/disciplines/abombwe|Abombwe]] — tribe-defining legacy discipline.
- [[entities/disciplines/animalism|Animalism]] — totem/retainer core.
- [[entities/disciplines/fortitude|Fortitude]] — damage-prevent.

## Sources

- src-001 — VTES 5E Rulebook (Laibon sect rules, p. 40).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, title text).
