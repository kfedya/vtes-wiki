---
type: entity
tags: [discipline, imbued-virtue, imbued, judgment]
sources: [src-002]
last_verified: 2026-04-18
status: draft
---

# Judgment

**Code:** `[jud]` basic / `[JUD]` superior

## Overview

Judgment is one of the seven Imbued **virtues** — the "discipline" analogue for Imbued minions (mortals with True Faith, not vampires) [src-002]. Virtues only appear on Imbued crypt cards and on library cards of the `Power` / `Conviction` card types that are playable exclusively by Imbued. Every Imbued carries exactly three virtues; `jud` is the Judge creed's signature virtue, themed around monster-hunting combat entry and conviction-recovery.

> Imbued virtues are distinct from vampire disciplines. A vampire cannot have `[jud]`. Imbued-only card types (`Power`, `Conviction`) live in separate shards under `card-db/library/`.

## In-clan

Imbued creeds carrying Judgment (src-002 snapshot):
- **Judge** — primary creed for Judgment.
- **Visionary**, **Defender**, **Redeemer**, **Avenger** — scattered cross-creed appearances.

No vampire clan has access to Judgment.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[jud]` (basic or superior): **4**
- Imbued crypt cards with `[jud]` or `[JUD]`: **7**

## Typical card roles

- Judge crypt — [Erick "Shophet125" Franco](https://codex-of-the-damned.org/en/card-search/crypt/index.html?card=Erick%20%22Shophet125%22%20Franco), [François "Warden" Loehr](https://codex-of-the-damned.org/en/card-search/crypt/index.html?card=Fran%C3%A7ois%20%22Warden%22%20Loehr).
- Power cards — [Discern](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Discern), [Vigilance](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Vigilance).
- Action (monster-hunt) — [Antithesis](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Antithesis).
- Combat — [Imprison](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Imprison).

## Query

Reproducible filter for all library cards requiring this virtue:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "jud")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "jud")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[entities/disciplines/defense|defense]], [[entities/disciplines/innocence|innocence]], [[entities/disciplines/martyrdom|martyrdom]], [[entities/disciplines/redemption|redemption]], [[entities/disciplines/vengeance|vengeance]], [[entities/disciplines/vision|vision]] — the other six Imbued virtues.
- No dedicated ruling page for Imbued / Conviction / True Faith yet — gap to fill on a later ingest.

## Sources

- src-002 — krcg vtes.json snapshot 2026-04-18 (virtue codes, card counts, creed co-occurrence, role examples).
