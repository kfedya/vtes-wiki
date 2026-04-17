---
type: entity
tags: [clan, legacy, abomination, niche-bloodline]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Abomination

## Overview

Abomination is a very niche legacy bloodline — **Vampire-Werewolf hybrids** (descended from the Nuwisha-Gangrel crossing in lore) [src-002]. Only 4 crypt entries exist in the snapshot, making this one of the smallest bloodlines in the game. Card-db evidence: of 4 Abomination vampires, `OBF` (3), `PRO` (2), and `POT/PRE/SER` (1 each) dominate superior disciplines — Obfuscate + Protean is the working signature, reflecting the shapeshifter heritage [src-002].

## In-clan disciplines (V5)

Not V5-playable. Legacy signature (from card-db frequency):

- [[entities/disciplines/obfuscate|Obfuscate]] — `[obf]`
- [[entities/disciplines/protean|Protean]] — `[pro]`
- [[entities/disciplines/potence|Potence]] — `[pot]` (on most Abominations)

## Sect alignment

Sect is printed per-vampire — the 4 Abominations split between **Independent** (3) and **Sabbat** (1, Zubeida with Black Hand) [src-002]. Every Abomination prints `Scarce. Sterile.`, reflecting the hybrid origin (cannot sire).

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **4**
- Crypt vampires with `[OBF]` at superior: **3**
- Crypt vampires with `[PRO]` at superior: **2**
- Library cards referencing "Abomination" in name or text: **1**

## Notable members

- **Zubeida** (cap 8, group 5) — Sabbat / Black Hand; `for/ser/OBF/PRE/PRO`; largest Abomination.
- **Allonzo Montoya** (cap 6, group 3) — Independent; `ani/aus/OBF/SER`.
- **Pariah** (cap 6, group 2) — Independent; `pot/pre/OBF/PRO`; +1 strength, cannot take undirected actions other than hunting.
- **Lorrie Dunsirn** (cap 4, group 4) — Independent; `for/nec/POT`; rage-combat profile (additional strike per round, press per combat).

## Typical deck archetypes

- **Hybrid curio / single-minion combat** — Pariah or Lorrie as solo-combat monsters. Cannot block undirected (Allonzo) or press to end (Lorrie), so deck-building must lean into their combat-card economy.
- **Tiny bloodline support** — too few vampires to carry a full crypt; typically seen as a single-slot curiosity inside a Gangrel- or Sabbat-Caitiff shell.

## Query

Reproducible filters:

```
# All crypt vampires of the clan
jq '.[] | select(.clans[]? == "Abomination") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Abomination") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("Abomination"; "i")) or (.card_text // "" | test("Abomination"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/disciplines/obfuscate]] — most common in-clan printing.
- [[entities/disciplines/protean]] — hybrid-shape signature.
- [[entities/clans/gangrel]] — ancestral bloodline.

## Sources

- src-001 — VTES 5E Rulebook (clan list, p. 53 Quick Reference icons).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
