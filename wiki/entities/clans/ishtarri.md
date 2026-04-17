---
type: entity
tags: [clan, legacy, ishtarri, laibon]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Ishtarri

## Overview

Ishtarri is a legacy **Laibon tribe** — one of four African vampire tribes from the Ebony Kingdom / Legacies of Blood era [src-002]. The Ishtarri are hedonists and power-brokers; card-db evidence shows a tight identity around Celerity, Fortitude, and Presence — a fast-but-tanky combat-plus-vote profile. Of 16 Ishtarri crypt vampires, `CEL` (9), `PRE` (9), and `FOR` (9) dominate superior disciplines (all three virtues appear on 15/16 at either basic or superior) [src-002].

## In-clan disciplines (legacy signature)

- [[entities/disciplines/celerity|Celerity]] — `[cel]`
- [[entities/disciplines/fortitude|Fortitude]] — `[for]`
- [[entities/disciplines/presence|Presence]] — `[pre]`

## Sect alignment

Primarily **[[entities/sects/laibon|Laibon]]**. Legacy-only sect, fully legal [src-001 p. 40]. Ishtarri crypt includes Laibon **magaji** holders (Falhu Shibaba, Ubende, Undele). Magaji is non-unique and cannot be contested; 2 votes per ready magaji [src-001 p. 40].

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires: **16**
- Crypt vampires with `[CEL]` at superior: **9**
- Crypt vampires with `[PRE]` at superior: **9**
- Crypt vampires with `[FOR]` at superior: **9**
- Library cards referencing "Ishtarri" in name or text: see query below.

## Notable members

- **Ayo Igoli** (cap 10, group 4) — top-capacity Ishtarri; `obf/tha/AUS/CEL/FOR/PRE`.
- **Undele** (cap 9, group 5) — Laibon magaji; political-action ash-heap recovery; `obf/pre/ser/CEL/FOR`.
- **Jibade el-Bahrawi** (cap 9, group 4) — `aus/CEL/DEM/FOR/PRE`.
- **Luanda Magere** (cap 8, group 4) — `for/CEL/PRE/PRO`.

## Typical deck roles

- **Ishtarri wall + vote** — FOR damage-prevent + PRE vote boost + CEL reactions; Laibon equivalent of a Toreador/Ventrue hybrid wall.
- **Magaji vote core** — 2-vote magaji titles drive PRE-based vote plans.
- **Fast wall** — CEL extra strikes + FOR damage-prevent on mid-capacity crypt.

## Query

Reproducible filters:

```
# All crypt vampires of the tribe
jq '.[] | select(.clans[]? == "Ishtarri") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Ishtarri") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the tribe by name or text
jq -s '[.[][] | select((.name // "" | test("Ishtarri"; "i")) or (.card_text // "" | test("Ishtarri"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/sects/laibon|Laibon]] — parent sect; kholo/magaji title rules.
- [[entities/clans/akunanse|Akunanse]], [[entities/clans/guruhi|Guruhi]], [[entities/clans/osebo|Osebo]] — the other three Laibon tribes.
- [[entities/disciplines/celerity|Celerity]] — extra strikes.
- [[entities/disciplines/fortitude|Fortitude]] — damage-prevent.
- [[entities/disciplines/presence|Presence]] — vote + Majesty.

## Sources

- src-001 — VTES 5E Rulebook (Laibon sect rules, p. 40).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, title text).
