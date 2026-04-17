---
type: entity
tags: [discipline, combo-code, maleficia, baali, not-a-discipline]
sources: [src-002]
last_verified: 2026-04-18
status: draft
---

# Maleficia (`mal`)

**Code:** `[mal]` basic / `[MAL]` superior — **explicitly labelled "not a Discipline" on every card** [src-002].

## Overview

`mal` is a library-only combo marker that appears on a small cluster of infernal / Baali-themed library cards — mostly curse actions and a hybrid combat/reaction. It looks like a discipline in `card-db` entries but every card that uses it contains the explicit disclaimer text **"[mal] is not a Discipline"** in its card text [src-002]. It therefore cannot be acquired via a master: Discipline card or satisfied by standard discipline requirements — the effect is gated purely by the card-text clauses on each individual card.

## Combo / special

Each `mal` card either stands alone or pairs with a real second discipline, where the `[mal]` clause is the alternate-effect line:

- [Psalm of the Damned](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Psalm%20of%20the%20Damned) — Action Modifier, combos with `[pre]`.
- [Barrenness](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Barrenness) — Action, solo `[mal]`. Applies Sterile trait and reduces target's capacity.
- [Greater Curse](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Greater%20Curse) — Action, combos with `[dai]`. Taxes the cursed minion's bleed/combat cards.
- [Minor Curse](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Minor%20Curse) — Action, solo `[mal]`. Suppresses card replacement.
- [Evil Eye](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Evil%20Eye) — Combat/Reaction hybrid, solo `[mal]`. Cancels strikes / action cards.

All five are infernal-flavoured curses, suggesting the name **"Maleficia"** (Latin for evil deeds / witchcraft) — consistent with Baali-theme Daimoinon combos. Note that `[dai]` (Daimoinon) is a real discipline; `[mal]` is the curse-effect alternate.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards using `[mal]` (basic or superior): **5**
- Crypt vampires with `[mal]` or `[MAL]`: **0** — no vampire in the snapshot carries Maleficia.

## Open question

The canonical name for this code is not attested in the card-db snapshot; rulebook src-001's Quick Reference does not list `[mal]`. Based on the card cluster (persistent curses with Baali/Daimoinon combo partners) the working label is **"Maleficia"**, but this is a conjecture — the cards themselves only ever refer to the code as `[mal]` and tell the player it is not a discipline [src-002]. A later source (e.g. Black Chantry FAQ, VEKN ruling, or the original Gehenna / Nights of Reckoning set text) is needed to fix the canonical name.

## Query

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "mal")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[entities/disciplines/daimoinon|daimoinon]] — Baali real discipline; natural combo partner (see [Greater Curse](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Greater%20Curse)).
- [[traits]] — Infernal trait (1-pool unlock cost on some curse targets); Sterile trait applied by [Barrenness](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Barrenness).

## Sources

- src-002 — krcg vtes.json snapshot 2026-04-18 (card listings and the explicit "[mal] is not a Discipline" card-text clauses).
