---
type: entity
tags: [discipline, legacy, temporis, true-brujah, time]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Temporis

**Code:** `[tem]` basic / `[TEM]` superior

## Overview

Temporis is the legacy **True Brujah** discipline of time manipulation — stopping the clock, replaying actions, and peering into the future. Mechanically a tempo pool built around action-replay modifiers, recurring reactions, and combat cards that alter sequencing. A small, single-clan discipline with one of the most distinctive effect suites in the game.

## In-clan

Primary in-clan discipline for (legacy printings): **True Brujah**.
Almost exclusively a True Brujah discipline in the current snapshot.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[tem]` (basic or superior): **17**
- Crypt vampires with `[tem]` or `[TEM]`: **11**

## Typical card roles

- Action replay / recurring modifiers — [Recurring Contemplation](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Recurring%20Contemplation), [Quicksilver Contemplation](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Quicksilver%20Contemplation), [Pocket Out of Time](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Pocket%20Out%20of%20Time).
- Time-stop reactions — [Rewind Time](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Rewind%20Time), [Internal Recursion](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Internal%20Recursion).
- Fate / history actions — [Clio's Kiss](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Clio%27s%20Kiss), [Clotho's Gift](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Clotho%27s%20Gift), [Cheat the Fates](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Cheat%20the%20Fates), [Hourglass of the Mind](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Hourglass%20of%20the%20Mind), [Summon History](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Summon%20History).
- Combat sequencing — [Outside the Hourglass](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Outside%20the%20Hourglass), [Lapse](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Lapse).
- Domain effects — [Domain of Evernight](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Domain%20of%20Evernight), [Hall of Hades' Court](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Hall%20of%20Hades%27%20Court), [Tangle Atropos' Hand](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Tangle%20Atropos%27%20Hand).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "tem")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "tem")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[game-overview]] — sequencing rules that Temporis disrupts.
- [[combat]] — Temporis combat-sequencing cards.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
