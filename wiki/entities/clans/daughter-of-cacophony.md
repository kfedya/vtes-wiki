---
type: entity
tags: [clan, legacy, daughter-of-cacophony, toreador-bloodline, single-clan-discipline]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Daughter of Cacophony

## Overview

Daughter of Cacophony is a legacy **Toreador offshoot** — opera-singing vampires whose voice bends reality [src-002]. Card-db evidence: of 15 Daughters, `MEL` (8), `FOR` (7), and `PRE` (6) dominate superior disciplines — Melpominee is single-clan to Daughters and drives the "song" cards; Fortitude and Presence round out the in-clan trio [src-002].

## In-clan disciplines (V5)

Not V5-playable. Legacy signature (from card-db frequency):

- [[entities/disciplines/fortitude|Fortitude]] — `[for]`
- [[entities/disciplines/melpominee|Melpominee]] — `[mel]`
- [[entities/disciplines/presence|Presence]] — `[pre]`

## Sect alignment

Printed sect is mostly **Independent** (with 1 Camarilla printing, Angela Preston) [src-002]. Daughters frequently have card text interacting with Toreador — reflecting their Toreador origin.

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires (all eras): **15**
- Crypt vampires with `[MEL]` at superior: **8**
- Crypt vampires with `[FOR]` at superior: **7**
- Crypt vampires with `[PRE]` at superior: **6**
- Library cards referencing "Daughter of Cacophony" in name or text: **6**

## Notable members

- **Scout Youngwood** (cap 8, group 6) — `for/qui/MEL/OBF/PRE`; largest Daughter.
- **Sayshila** (cap 7, group 4) — `dem/FOR/MEL/PRE`.
- **Evil Jensen** (cap 6, group 4) — `mel/nec/pot/FOR/PRE`.
- **Gaël Pilet** (cap 6, group 2) — `chi/pre/FOR/MEL`.
- **Yseult** (cap 6, group 3) — `FOR/MEL/PRE`; pure in-clan signature.

## Typical deck archetypes

- **Song-bleed stealth** — stacked Melpominee "song" cards (Phantom of the Opera, The Art of Memory) with PRE for vote/presence support.
- **Daughter wall** — MEL reactions + FOR damage-prevent; intercept with Audience Among the Dead.
- **Mixed Toreador / Daughter crypt** — pair Daughters with Toreador antitribu to share PRE/AUS.

## Query

Reproducible filters:

```
# All crypt vampires of the clan
jq '.[] | select(.clans[]? == "Daughter of Cacophony") | .name' card-db/crypt.json

# Top superior disciplines
jq -r '[.[] | select(.clans[]? == "Daughter of Cacophony") | .disciplines[]? | select(. == (. | ascii_upcase))] | group_by(.) | map({disc: .[0], count: length}) | sort_by(-.count) | .[] | "\(.disc) \(.count)"' card-db/crypt.json

# Library cards referencing the clan by name or text
jq -s '[.[][] | select((.name // "" | test("Daughter of Cacophony"; "i")) or (.card_text // "" | test("Daughter of Cacophony"; "i")))] | length' card-db/library/*.json
```

## Related

- [[entities/disciplines/melpominee]] — single-clan signature; Daughter-only song cards.
- [[entities/disciplines/fortitude]] — in-clan.
- [[entities/disciplines/presence]] — in-clan.
- [[entities/clans/toreador]] — parent clan.

## Sources

- src-001 — VTES 5E Rulebook (clan list, p. 53 Quick Reference icons).
- src-002 — krcg vtes.json snapshot 2026-04-18 (vampire rosters, discipline frequencies, library cross-references).
