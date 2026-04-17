---
type: entity
tags: [discipline, imbued-virtue, imbued, redemption]
sources: [src-002]
last_verified: 2026-04-18
status: draft
---

# Redemption

**Code:** `[red]` basic / `[RED]` superior

## Overview

Redemption is one of the seven Imbued **virtues** — the "discipline" analogue for Imbued minions (mortals with True Faith, not vampires) [src-002]. Virtues only appear on Imbued crypt cards and on library cards of the `Power` / `Conviction` card types that are playable exclusively by Imbued. Every Imbued carries exactly three virtues; `red` is the Redeemer creed's signature virtue, themed around recovery, conviction-search, and blunting enemy threats.

> Imbued virtues are distinct from vampire disciplines. A vampire cannot have `[red]`. Imbued-only card types (`Power`, `Conviction`) live in separate shards under `card-db/library/`.

## In-clan

Imbued creeds carrying Redemption (src-002 snapshot):
- **Redeemer** — primary creed for Redemption.
- **Martyr**, **Innocent** — scattered cross-creed appearances.

No vampire clan has access to Redemption.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[red]` (basic or superior): **4**
- Imbued crypt cards with `[red]` or `[RED]`: **5**

## Typical card roles

- Redeemer crypt — [Leaf "Potter116" Pankowski](https://codex-of-the-damned.org/en/card-search/crypt/index.html?card=Leaf%20%22Potter116%22%20Pankowski), [Marion "Teacher193" Perks](https://codex-of-the-damned.org/en/card-search/crypt/index.html?card=Marion%20%22Teacher193%22%20Perks), [Peter "Outback295" Rophail](https://codex-of-the-damned.org/en/card-search/crypt/index.html?card=Peter%20%22Outback295%22%20Rophail).
- Power cards — [Abjure](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Abjure), [Respire](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Respire), [Shame](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Shame).
- Action / Combat hybrid — [Punish](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Punish).

## Query

Reproducible filter for all library cards requiring this virtue:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "red")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "red")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[entities/disciplines/defense|defense]], [[entities/disciplines/innocence|innocence]], [[entities/disciplines/judgment|judgment]], [[entities/disciplines/martyrdom|martyrdom]], [[entities/disciplines/vengeance|vengeance]], [[entities/disciplines/vision|vision]] — the other six Imbued virtues.
- No dedicated ruling page for Imbued / Conviction / True Faith yet — gap to fill on a later ingest.

## Sources

- src-002 — krcg vtes.json snapshot 2026-04-18 (virtue codes, card counts, creed co-occurrence, role examples).
