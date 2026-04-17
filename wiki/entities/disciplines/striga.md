---
type: entity
tags: [discipline, combo-code, striga, not-a-discipline]
sources: [src-002]
last_verified: 2026-04-18
status: draft
---

# Striga (`str`)

**Code:** `[str]` basic / `[STR]` superior — **explicitly labelled "not a Discipline" on every card** [src-002].

## Overview

`str` is a library-only combo marker that appears on a small cluster of Gehenna-era Gargoyle-servitor library cards. It looks like a discipline in `card-db` entries but every card that uses it contains the explicit disclaimer text **"[str] is not a Discipline"** in its card text [src-002]. It therefore cannot be acquired via a master: Discipline card or satisfied by Discipline-based requirements — it is resolved purely through card-text conditions.

## Combo / special

Every `str` library card also lists a real second discipline (obf / cel / dai / pre), and the `str` clause is the alternate-effect line on that combo card. The pattern mirrors how `FLIGHT` is used on Gargoyle cards: a marker that gates a card's secondary effect without being a true discipline.

- [Masca](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Masca) — Action Modifier, combos with `[obf]`.
- [Fractura](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Fractura) — Combat, combos with `[cel]`.
- [Hexe](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Hexe) — Combat, combos with `[dai]`.
- [Scobax](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Scobax) — Reaction, combos with `[pre]`.
- [Strix](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Strix) — Reaction, solo `[str]` effect.

All five are named after Latin / Roman-lore Gargoyle-servitor creatures (masca, fractura, hexe, scobax, strix-screech-owl), suggesting a thematic Gargoyle/infernal-servitor cluster.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards using `[str]` (basic or superior): **5**
- Crypt vampires with `[str]` or `[STR]`: **0** — no vampire in the snapshot carries Striga.

## Open question

The canonical name for this code is not attested in the card-db snapshot; rulebook src-001's Quick Reference does not list `[str]`. Based on the card cluster (named after Strix / Hexe / etc.) the working label is **"Striga"**, but this is a conjecture — the cards themselves only ever refer to the code as `[str]` and tell the player it is not a discipline [src-002]. A later source (e.g. Black Chantry FAQ, VEKN ruling, or the Gehenna rulebook) is needed to fix the canonical name.

## Query

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "str")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[entities/disciplines/visceratika|visceratika]] — Gargoyle's actual in-clan discipline; the `str` cluster rides alongside the Gargoyle-servitor theme.
- [[entities/disciplines/daimoinon|daimoinon]] — combo partner on [Hexe](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Hexe).
- [[traits]] — see `Flight` section; `[str]` parallels `[FLIGHT]` as a non-discipline code used on Gargoyle-themed cards.

## Sources

- src-002 — krcg vtes.json snapshot 2026-04-18 (card listings and the explicit "[str] is not a Discipline" card-text clauses).
