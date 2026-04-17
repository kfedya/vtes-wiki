---
type: entity
tags: [clan, legacy, guruhi, laibon]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Guruhi

## Overview

Guruhi is a legacy **Laibon tribe** — one of four African vampire tribes from the Ebony Kingdom / Legacies of Blood era [src-002]. The Guruhi are elder-dominated rulers of the Ebony Kingdom; card-db evidence shows a tight identity around Animalism, Potence, and Presence — the Laibon mirror of Brujah's combat-plus-vote profile. Of 16 Guruhi crypt vampires, `ANI` (13), `PRE` (13), and `POT` (11) dominate superior disciplines (one Guruhi printed at inferior brings ANI appearance to 16/16) [src-002].

## In-clan disciplines (legacy signature)

- [[entities/disciplines/animalism|Animalism]] — `[ani]`
- [[entities/disciplines/potence|Potence]] — `[pot]`
- [[entities/disciplines/presence|Presence]] — `[pre]`

## Sect alignment

Primarily **[[entities/sects/laibon|Laibon]]**. Legacy-only sect, fully legal [src-001 p. 40]. Guruhi crypt includes multiple Laibon **magaji** holders. Four Guruhi carry `Laibon magaji` text (Eze the Demon Prince, Ngozi Ekwensu, Sobayifa, Ugadja). Magaji is non-unique and cannot be contested; 2 votes per ready magaji [src-001 p. 40].

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires: **16**
- Crypt vampires with `[PRE]` at superior: **13**
- Crypt vampires with `[ANI]` at superior: **13**
- Crypt vampires with `[POT]` at superior: **11**
- Library cards referencing "Guruhi" in name or text: see query below.

## Notable members

- **Lucian, the Perfect** (cap 11, group 4) — Guruhi iconic elder; `ANI/AUS/DOM/OBF/POT/PRE`.
- **Eze, The Demon Prince** (cap 11, group 3) — Laibon magaji with unlock-after-action effect; `aus/ANI/NEC/POT/PRE/THA`.
- **Ugadja** (cap 10, group 4) — Laibon magaji; can stealth-transfer blood to a younger Laibon; `dom/for/ABO/ANI/POT/PRE`.
- **Ngozi Ekwensu** (cap 9, group 5) — Laibon magaji; aggravated hand strikes via Orun lock; `cel/ANI/POT/PRE/VIC`.

## Typical deck roles

- **Laibon grinder / combat** — POT hand-strike damage + ANI animal retainers + PRE Majesty; the most Brujah-like Laibon tribe.
- **Magaji vote + combat** — 2-vote magaji titles pair naturally with PRE vote boost (Voter Captivation, Majesty).
- **Guruhi elder swarm** — high-capacity methuselah-tier elders in mixed Laibon crypts.

## Query

Reproducible filters:

```
# All crypt vampires of the tribe
jq '.[] | select(.clans[]? == "Guruhi") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Guruhi") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the tribe by name or text
jq -s '[.[][] | select((.name // "" | test("Guruhi"; "i")) or (.card_text // "" | test("Guruhi"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/sects/laibon|Laibon]] — parent sect; kholo/magaji title rules.
- [[entities/clans/akunanse|Akunanse]], [[entities/clans/ishtarri|Ishtarri]], [[entities/clans/osebo|Osebo]] — the other three Laibon tribes.
- [[entities/disciplines/animalism|Animalism]] — totem/retainer core.
- [[entities/disciplines/potence|Potence]] — hand-strike damage.
- [[entities/disciplines/presence|Presence]] — vote + Majesty.

## Sources

- src-001 — VTES 5E Rulebook (Laibon sect rules, p. 40).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, title text).
