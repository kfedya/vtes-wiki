---
type: entity
tags: [discipline, legacy, sanguinus, blood-brother, coordination]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Sanguinus

**Code:** `[san]` basic / `[SAN]` superior

## Overview

Sanguinus is the legacy **Blood Brother** discipline of Circle coordination — sharing blood, bodies, and actions between members of a Circle. Mechanically a support pool built around multi-minion combat coordination, body-swap action modifiers, and Circle-gated reactions. A single-clan discipline with one of the smallest card pools in the game.

## In-clan

Primary in-clan discipline for (legacy printings): **Blood Brother** only.
No other clans carry Sanguinus in the current snapshot.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[san]` (basic or superior): **16**
- Crypt vampires with `[san]` or `[SAN]`: **24**

## Typical card roles

- Circle coordination / combat — [Coordinate Attacks](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Coordinate%20Attacks), [Clockwerx](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Clockwerx), [Free Fight](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Free%20Fight), [Octopod](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Octopod).
- Blood-sharing / body-swap — [Brother's Blood](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Brother%27s%20Blood), [Shell Game](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Shell%20Game), [Claiming the Body](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Claiming%20the%20Body).
- Action modifiers / bleed support — [Slake the Thirst](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Slake%20the%20Thirst), [Walk of Caine](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Walk%20of%20Caine), [Hay Ride](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Hay%20Ride).
- Reactions — [Camaraderie](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Camaraderie), [Gestalt](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Gestalt).
- Actions — [Hive Mind](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Hive%20Mind), [Unwholesome Bond](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Unwholesome%20Bond).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "san")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "san")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[traits]] — Circle trait (Blood Brothers share a Circle).
- [[combat]] — multi-minion combat coordination.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
