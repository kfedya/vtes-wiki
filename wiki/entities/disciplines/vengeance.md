---
type: entity
tags: [discipline, imbued-virtue, imbued, vengeance]
sources: [src-002]
last_verified: 2026-04-18
status: draft
---

# Vengeance

**Code:** `[ven]` basic / `[VEN]` superior

## Overview

Vengeance is one of the seven Imbued **virtues** — the "discipline" analogue for Imbued minions (mortals with True Faith, not vampires) [src-002]. Virtues only appear on Imbued crypt cards and on library cards of the `Power` / `Conviction` card types that are playable exclusively by Imbued. Every Imbued carries exactly three virtues; `ven` is the Avenger creed's signature virtue, themed around bleed pressure, weapons, and aggressive monster-hunting strikes.

> Imbued virtues are distinct from vampire disciplines. A vampire cannot have `[ven]`. Imbued-only card types (`Power`, `Conviction`) live in separate shards under `card-db/library/`.

## In-clan

Imbued creeds carrying Vengeance (src-002 snapshot):
- **Avenger** — primary creed for Vengeance.
- **Innocent**, **Judge**, **Defender**, **Redeemer** — scattered cross-creed appearances.

No vampire clan has access to Vengeance.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[ven]` (basic or superior): **4**
- Imbued crypt cards with `[ven]` or `[VEN]`: **6**

## Typical card roles

- Avenger crypt — [Jennifer "Flame61" Vidisania](https://codex-of-the-damned.org/en/card-search/crypt/index.html?card=Jennifer%20%22Flame61%22%20Vidisania), [John "Cop90" O'Malley](https://codex-of-the-damned.org/en/card-search/crypt/index.html?card=John%20%22Cop90%22%20O%27Malley), [Pedro Cortez](https://codex-of-the-damned.org/en/card-search/crypt/index.html?card=Pedro%20Cortez).
- Power cards — [Surge](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Surge).
- Action (muse / weapon-flavour) — [Muse of Flame](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Muse%20of%20Flame).
- Combat — [Cleave](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Cleave), [Smite](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Smite).

## Query

Reproducible filter for all library cards requiring this virtue:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "ven")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "ven")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[entities/disciplines/defense|defense]], [[entities/disciplines/innocence|innocence]], [[entities/disciplines/judgment|judgment]], [[entities/disciplines/martyrdom|martyrdom]], [[entities/disciplines/redemption|redemption]], [[entities/disciplines/vision|vision]] — the other six Imbued virtues.
- No dedicated ruling page for Imbued / Conviction / True Faith yet — gap to fill on a later ingest.

## Sources

- src-002 — krcg vtes.json snapshot 2026-04-18 (virtue codes, card counts, creed co-occurrence, role examples).
