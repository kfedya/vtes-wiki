---
type: entity
tags: [clan, legacy, pander, caitiff, sabbat]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Pander

## Overview

Pander are the **Sabbat-aligned Caitiff** — clanless vampires recognized as a semi-clan within Sabbat lore after being championed by Joseph Pander [src-002]. Mechanically they function like [[entities/clans/caitiff|Caitiff]]: **no in-clan disciplines**, every printed discipline paid at out-of-clan cost. Card-db evidence: of 22 Pander vampires, superior disciplines are flat (`PRE` 2, `THA` 2, `AUS/CEL/OBF/OBT/POT` 1 each), the same flat spread as Caitiff — sect alignment is the differentiator, not a discipline signature [src-002].

## In-clan disciplines (V5)

**N/A — clanless.** Pander inherit the Caitiff treatment: no in-clan disciplines; all disciplines paid at out-of-clan cost. Deck-building uses Pander as flexible Sabbat-aligned crypt slots.

## Sect alignment

Printed sect is almost uniformly **Sabbat** — every Pander in the snapshot prints `Sabbat:` or `Sabbat.` in their text box [src-002]. Panders play the Sabbat role (bishops, priscus references, Black Hand text) while retaining the clanless discipline-spread of Caitiff.

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **22**
- Crypt vampires with any superior discipline: scattered; no single superior appears on more than 2 Panders.
- Library cards referencing "Pander" in name or text: **4**

## Notable members

- **Alfred Benezri** (cap 7 advanced, group 3) — Sabbat bishop; `aus/dom/PRE/THA`.
- **Matthew Romans** (cap 7, group 4) — Sabbat; `pot/AUS/OBF/OBT`.
- **Jimmy Dunn** (cap 4, group 2) — Sabbat; `for/CEL/POT`; cannot be contested.
- **Caroline Bishops** (cap 3, group 4) — Sabbat; `cel/for/pot`.
- **Lena Rowe** (cap 3, group 2) — Sabbat; `aus/obf/pre`; cannot receive any title.

## Typical deck archetypes

- **Sabbat Pander utility** — off-clan Sabbat filler with whatever discipline the individual vampire carries; works as secondary crypt in bigger Sabbat clan decks.
- **Small-cap Sabbat rush** — cheap Panders (Jimmy Dunn, Caroline Bishops) as supporting bleeders alongside a Sabbat main clan.

## Query

Reproducible filters:

```
# All crypt vampires of the clan
jq '.[] | select(.clans[]? == "Pander") | .name' card-db/crypt.json

# Top superior disciplines (expected: flat — no signature)
jq -r '[.[] | select(.clans[]? == "Pander") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("Pander"; "i")) or (.card_text // "" | test("Pander"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/clans/caitiff]] — parent/sibling clanless designation; same mechanical treatment.
- [[entities/sects/sabbat]] — primary sect alignment.

## Sources

- src-001 — VTES 5E Rulebook (clan list, p. 53 Quick Reference icons).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
