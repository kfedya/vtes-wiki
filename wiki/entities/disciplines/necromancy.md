---
type: entity
tags: [discipline, legacy, necromancy, giovanni, harbinger-of-skulls, nagaraja, death]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Necromancy

**Code:** `[nec]` basic / `[NEC]` superior

## Overview

Necromancy is the legacy discipline of death magic — commanding ghosts, animating corpses, stealing souls, and summoning wraiths to do the vampire's bidding [src-002]. Mechanically it is one of the deepest legacy pools: stealth bleed/draining actions, ghost combat, and a signature bleed-bounce reaction ([Call of the Hungry Dead](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Call%20of%20the%20Hungry%20Dead)). In 5E it is no longer a 5E core discipline — the Hecata clan uses the consolidated [[entities/disciplines/oblivion|Oblivion]] discipline, which partly supersedes Necromancy. Giovanni, Harbinger of Skulls, and Nagaraja legacy printings still use `[nec]`.

## In-clan

Primary in-clan discipline for (legacy printings): **Giovanni**, **Harbinger of Skulls**, **Nagaraja**, **Samedi**.
Scattered appearances on: Ministry.

## V5 / legacy relationship

- Legacy Necromancy is partly absorbed into V5 **Oblivion** (shared with legacy Obtenebration).
- Legacy `[nec]` cards are still fully legal and coexist with new `[obl]` printings. A Hecata deck can run both pools concurrently.
- See [[entities/disciplines/oblivion]] for the V5 consolidated discipline.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[nec]` (basic or superior): **44**
- Crypt vampires with `[nec]` or `[NEC]`: **142**

## Typical card roles

- Bleed-bounce / bleed redirect reaction — [Call of the Hungry Dead](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Call%20of%20the%20Hungry%20Dead).
- Ghost / soul stealth actions — [Soul Feasting](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Soul%20Feasting), [Possession](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Possession), [Daemonic Possession](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Daemonic%20Possession).
- Stealth / void action modifiers — [Shroudsight](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Shroudsight), [Inevitability of the Void](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Inevitability%20of%20the%20Void).
- Wraith / undead allies — [Shambling Hordes](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Shambling%20Hordes), [Puppeteer](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Puppeteer).
- Ghost combat — [Dead Hand](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Dead%20Hand), [Torment the Soul](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Torment%20the%20Soul), [Heaven's Gate](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Heaven%27s%20Gate).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "nec")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "nec")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[entities/disciplines/oblivion]] — V5 consolidation that partly supersedes Necromancy.
- [[target-redirection]] — Call of the Hungry Dead is a Necromancy bleed-bounce.
- [[bleed]] — Necromancy supports stealth-bleed archetypes.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
