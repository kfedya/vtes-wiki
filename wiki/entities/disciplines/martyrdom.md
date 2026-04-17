---
type: entity
tags: [discipline, imbued-virtue, imbued, martyrdom]
sources: [src-002]
last_verified: 2026-04-18
status: draft
---

# Martyrdom

**Code:** `[mar]` basic / `[MAR]` superior

## Overview

Martyrdom is one of the seven Imbued **virtues** — the "discipline" analogue for Imbued minions (mortals with True Faith, not vampires) [src-002]. Virtues only appear on Imbued crypt cards and on library cards of the `Power` / `Conviction` card types that are playable exclusively by Imbued. Every Imbued carries exactly three virtues; `mar` is the Martyr creed's signature virtue, themed around self-sacrifice for others, damage-sharing, and aggressive combat swings.

> Imbued virtues are distinct from vampire disciplines. A vampire cannot have `[mar]`. Imbued-only card types (`Power`, `Conviction`) live in separate shards under `card-db/library/`.

## In-clan

Imbued creeds carrying Martyrdom (src-002 snapshot):
- **Martyr** — primary creed for Martyrdom.
- **Visionary**, **Avenger** — scattered cross-creed appearances.

No vampire clan has access to Martyrdom.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[mar]` (basic or superior): **4**
- Imbued crypt cards with `[mar]` or `[MAR]`: **5**

## Typical card roles

- Martyr crypt — [Anna "Dictatrix11" Suljic](https://codex-of-the-damned.org/en/card-search/crypt/index.html?card=Anna%20%22Dictatrix11%22%20Suljic), [Maman Boumba](https://codex-of-the-damned.org/en/card-search/crypt/index.html?card=Maman%20Boumba), [Travis "Traveler72" Miller](https://codex-of-the-damned.org/en/card-search/crypt/index.html?card=Travis%20%22Traveler72%22%20Miller).
- Power cards — [Donate](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Donate), [Project](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Project).
- Combat — [Expiate](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Expiate), [Inflict](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Inflict).

## Query

Reproducible filter for all library cards requiring this virtue:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "mar")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "mar")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[entities/disciplines/defense|defense]], [[entities/disciplines/innocence|innocence]], [[entities/disciplines/judgment|judgment]], [[entities/disciplines/redemption|redemption]], [[entities/disciplines/vengeance|vengeance]], [[entities/disciplines/vision|vision]] — the other six Imbued virtues.
- No dedicated ruling page for Imbued / Conviction / True Faith yet — gap to fill on a later ingest.

## Sources

- src-002 — krcg vtes.json snapshot 2026-04-18 (virtue codes, card counts, creed co-occurrence, role examples).
