---
type: mechanic-index
tags: [block, intercept, reaction, cross-table, restriction-override]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Ignore Prey/Predator/Target Block Restrictions — Card Index

## Scope

Cards that **let any vampire attempt to block an action**, overriding the rulebook rule that limits blocks to the target Methuselah (directed actions) or the acting Methuselah's prey/predator (undirected actions).

The canonical card text pattern is:

> "…ignoring the normal prey, predator or target restrictions for blocking actions."

Excluded:
- **Wake effects** (On the Qui Vive, Forced Awakening, Wake with Evening's Freshness, Eyes of Argus at superior) — let a locked vampire act as unlocked, but do NOT override whose Methuselah can block. A waked vampire whose Methuselah has no right to block still cannot block.
- **Enablers on the acting side** (e.g., Lord of Serenity — granted to the rescuer, lifts restrictions for blockers of the action). This page is about **reaction** cards played by blockers.
- **Intercept boosters** (Cats' Guidance, Aid from Bats, Telepathic Tracking, etc.) — these add intercept but don't override WHO can block.

## Cards

### Reaction

- [Eagle's Sight](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Eagle%27s%20Sight) — Auspex.
  - `[aus]` basic: +1 intercept (standard use; blocker must already have block rights).
  - `[AUS]` superior: "This vampire attempts to block the current action, **ignoring the normal prey, predator or target restrictions** for blocking actions."
- [Falcon's Eye](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Falcon%27s%20Eye) — Spiritus (Ahrimane).
  - `[ani]` basic: burn 1 blood for +1 intercept.
  - `[spi]` basic: +1 intercept.
  - `[SPI]` superior: "This reacting vampire attempts to block the current action, **ignoring the normal prey, predator or target restrictions** for blocking actions."

### Action (acting side — for completeness)

- [Lord of Serenity](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Lord%20of%20Serenity) — Fortitude + Obeah.
  - `[for]`: "Rescue up to two vampires from torpor. **Vampires can ignore the normal prey, predator or target restrictions for blocking this action.**" — Acts as a *grantor*: when the rescuer plays this card, the rescue becomes blockable by any vampire. Edge case; covers multi-target rescues mixing own and foreign vampires.

## Ruling — cross-table block on directed actions

VEKN Rules Director and moderation confirm that **other Methuselahs can block directed actions via these cards**, even if the action isn't directed at them:

> "Other Methuselahs can also block that (D) action with Eagle's Sight or similar effects." — Pascal Bertrand, moderator
> "Globally yes (he may also cause your action to fail with cards such as Hide the Heart)." — Ankha, Rules Director

Source thread: [vekn.net/forum/rules-questions/45737-rescue-vampire-from-torpor](https://www.vekn.net/forum/rules-questions/45737-rescue-vampire-from-torpor).

## Query used

```
jq '.[] | select(.card_text | test("ignor.*(normal).*(prey|predator|target).*(restrict|block)|ignor.*(prey|predator|target).*(restrict)"; "i")) | {name, card_text}' card-db/library/*.json
```

Returns 3 hits: Eagle's Sight, Falcon's Eye, Lord of Serenity.

## Practical notes

- **Auspex is common** — Tremere, Toreador, Malkavian, Salubri, many cross-clan Aus vampires. Expect Eagle's Sight to be available at most tables.
- **Spiritus is rare** — Ahrimane-only discipline; small playbase. Falcon's Eye rarely appears.
- These cards still require a **ready unlocked** vampire. Combine with wake effects to enable locked minions ([On the Qui Vive](https://codex-of-the-damned.org/en/card-search/library/index.html?card=On%20the%20Qui%20Vive), [Forced Awakening](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Forced%20Awakening)).
- Stealth/intercept still applies. A cross-table block via Eagle's Sight/Falcon's Eye still needs intercept ≥ stealth.

## Related

- [[rulings/block-resolution]] — base rules on who may attempt to block.
- [[rulings/rescue-from-torpor]] — one of the most-affected actions; see the "Cross-Table Blocks" section.
- [[entities/disciplines/auspex]] — primary discipline hosting this capability.
- [[entities/disciplines/spiritus]] — Ahrimane equivalent.

## Sources

- src-001 — VTES 5E Rulebook, p. 25 (Who May Attempt to Block, base rule).
- src-002 — krcg vtes.json snapshot 2026-04-18 (Eagle's Sight, Falcon's Eye, Lord of Serenity card text).
- VEKN forum ruling — [rules-questions/45737](https://www.vekn.net/forum/rules-questions/45737-rescue-vampire-from-torpor), Pascal Bertrand + Ankha.
