---
type: entity
tags: [clan, 5e-playable, ravnos, independent, anarch]
sources: [src-001, src-002, src-016]
last_verified: 2026-04-18
status: verified
---

# Ravnos

## Overview

Ravnos is a V5-playable clan [src-001 p. 53]. Legacy signature disciplines were Animalism, Chimerstry, and Fortitude; V5 has largely retained Animalism and Presence in the in-clan set while dropping Chimerstry as a printed core (Chimerstry-specific cards remain legal for legacy crypt). Card-db evidence: of 78 Ravnos vampires, `CHI` (40), `ANI` (33), and `FOR` (27) remain the most common superior disciplines, with `PRE` (13) and `OBF` (12) behind [src-002].

## In-clan disciplines (V5)

- [[entities/disciplines/animalism|Animalism]] — `[ani]`
- [[entities/disciplines/chimerstry|Chimerstry]] — `[chi]` (legacy signature; still present on most crypt)
- [[entities/disciplines/presence|Presence]] — `[pre]` (V5 addition)

Also common on crypt: [[entities/disciplines/fortitude|Fortitude]] — `[for]` (27 superior printings).

## Sect alignment

Overwhelmingly **Independent** — 20 of 78 vampires print `Independent.` in full, consistent with the clan's wanderer / itinerant identity [src-002]. **Anarch** (7) and a small **Sabbat** (2) contingent round out the sect distribution.

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **78**
- Crypt vampires with `[CHI]` at superior: **40**
- Crypt vampires with `[ANI]` at superior: **33**
- Crypt vampires with `[FOR]` at superior: **27**
- Crypt vampires with `[PRE]` at superior: **13**
- Library cards referencing "Ravnos" in name or text: **25**

## Notable members

- **Ezmerelda** (cap 11, group 2) — `dom/tha/ANI/CHI/FOR/PRE`.
- **Hazimel** (cap 11, group 4) — `dem/ANI/AUS/CHI/FOR/POT`.
- **Durga Syn** (cap 9, group 4) — `ani/aus/dom/for/CHI/OBF/THA`.
- **Lizette** (cap 10, group 4) — `pot/ANI/CEL/CHI/FOR/PRO`.
- **Ivan Krenyenko** (cap 10, group 2) — `obf/ANI/CHI/FOR/POT`.

## Typical deck archetypes

- **Chimerstry stealth-bleed** — CHI illusion-based stealth modifiers + CHI trickery combat; legacy Ravnos classic.
- **Animal swarm / Raven Spy** — ANI retainer swarm with Raven Spy intercept; fits Independent sect.
- **Fortitude wall** — FOR damage-prevent with ANI reactions; resilient defensive Ravnos.
- [[archetypes/ravnos-bonds|Ravnos Bonds]] — top-tier V5 Ravnos Anarch stealth-and-bleed; Break the Bonds × 16 bleed-and-recruit engine; Memory Rift × 10 OBF stealth; Dabbler × 4 triple-discipline economy [src-016].

## Query

Reproducible filters:

```
# All crypt vampires of the clan
jq '.[] | select(.clans[]? == "Ravnos") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Ravnos") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("Ravnos"; "i")) or (.card_text // "" | test("Ravnos"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/sects/independent]] — primary sect alignment.
- [[entities/sects/anarch]] — secondary; 2 votes per baron.
- [[entities/disciplines/animalism]] — animal retainers + swarm combat.
- [[entities/disciplines/chimerstry]] — legacy signature; illusion-based stealth + combat.
- [[entities/disciplines/presence]] — V5 addition; vote boost.
- [[entities/disciplines/fortitude]] — damage prevention.

## Sources

- src-001 — VTES 5E Rulebook (playable-clan list, p. 53 Quick Reference icons).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
- src-016 — Codex of the Damned — Ravnos Bonds archetype (top-tier V5 Ravnos Anarch stealth-and-bleed; Break the Bonds engine).
