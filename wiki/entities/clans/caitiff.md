---
type: entity
tags: [clan, legacy, caitiff, clanless]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Caitiff

## Overview

Caitiff are **clanless** vampires — Kindred of no known lineage [src-002]. They have **no in-clan disciplines**: every discipline a Caitiff carries is played at out-of-clan cost. Card-db evidence: of 36 Caitiff vampires, superior disciplines are scattered (`AUS` 2, `PRE` 2, then `CEL/FOR/QUI/THA` at 1 each), reflecting exactly that lack of a signature set — Caitiff are printed with whatever mix the designer chose for that particular character [src-002].

## In-clan disciplines (V5)

**N/A — clanless.** Caitiff have no in-clan disciplines; every discipline on a Caitiff crypt card is paid at out-of-clan cost for library play. Deck-building uses Caitiff as flexible crypt slots constrained only by group, capacity, and the discipline spread printed on each vampire.

## Sect alignment

Caitiff have **no clan sect bias** — sect is printed per-vampire. The card-db snapshot shows a mix of **Camarilla**, **Anarch**, and untitled Caitiff printings. [Anarch Convert](https://codex-of-the-damned.org/en/card-search/crypt/index.html?card=Anarch%20Convert) is the best-known Caitiff (1-cap, any group, printed as Anarch) and sees heavy play as a starting-crypt filler for Anarch builds.

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **36**
- Crypt vampires with any superior discipline: scattered; no single superior appears on more than 2 Caitiff.
- Library cards referencing "Caitiff" in name or text: **3**

## Notable members

- **Mukhtar Bey** (cap 7, group 4) — largest Caitiff; `obf/pot/FOR/PRE/QUI`.
- **Anarch Convert** (cap 1, any group) — iconic 1-cap Anarch starter; can be removed from game to pull another Anarch into the uncontrolled region.
- **Maldavis** (cap 4, group 3) — advanced printing available; `for/pre/AUS`.
- **Gabriel Tremblay** (cap 4, group 6) — Anarch Caitiff; `aus/pot/pro`.
- **Count Zaroff** (cap 4, group 5) — Camarilla Caitiff; `cel/obf`.

## Typical deck archetypes

- **Anarch grinder / starter** — Anarch Convert as a cheap 1-cap pool-sink / crypt-engine piece.
- **Off-clan utility** — slot a small Caitiff into a crypt that needs a particular discipline spread without paying clan-signature-card restrictions. Everything is out-of-clan for them, so library choice drives the archetype rather than the crypt.

## Query

Reproducible filters:

```
# All crypt vampires of the clan
jq '.[] | select(.clans[]? == "Caitiff") | .name' card-db/crypt.json

# Top superior disciplines (expected: flat distribution — no signature)
jq -r '[.[] | select(.clans[]? == "Caitiff") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("Caitiff"; "i")) or (.card_text // "" | test("Caitiff"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/clans/pander]] — Sabbat-aligned Caitiff offshoot; similar "clanless" mechanics.
- [[entities/sects/anarch]] — many Caitiff are printed Anarch (Anarch Convert).
- [[entities/sects/camarilla]] — a handful of Caitiff are printed Camarilla.

## Sources

- src-001 — VTES 5E Rulebook (clan list, p. 53 Quick Reference icons).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
