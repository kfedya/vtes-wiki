---
type: entity
tags: [discipline, imbued-virtue, imbued, innocence]
sources: [src-002]
last_verified: 2026-04-18
status: draft
---

# Innocence

**Code:** `[inn]` basic / `[INN]` superior

## Overview

Innocence is one of the seven Imbued **virtues** — the "discipline" analogue for Imbued minions (mortals with True Faith, not vampires) [src-002]. Virtues only appear on Imbued crypt cards and on library cards of the `Power` / `Conviction` card types that are playable exclusively by Imbued. Every Imbued carries exactly three virtues; `inn` is the Innocent creed's signature virtue, themed around concealment, bleed support, and conviction-generation.

> Imbued virtues are distinct from vampire disciplines. A vampire cannot have `[inn]`. Imbued-only card types (`Power`, `Conviction`) live in separate shards under `card-db/library/`.

## In-clan

Imbued creeds carrying Innocence (src-002 snapshot):
- **Innocent** — primary creed for Innocence.
- **Judge**, **Visionary**, **Redeemer**, **Martyr**, **Defender** — scattered cross-creed appearances.

No vampire clan has access to Innocence.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[inn]` (basic or superior): **4**
- Imbued crypt cards with `[inn]` or `[INN]`: **8**

## Typical card roles

- Innocent crypt — [Béatrice "Oracle171" Tremblay](https://codex-of-the-damned.org/en/card-search/crypt/index.html?card=B%C3%A9atrice%20%22Oracle171%22%20Tremblay), [Inez "Nurse216" Villagrande](https://codex-of-the-damned.org/en/card-search/crypt/index.html?card=Inez%20%22Nurse216%22%20Villagrande), [Liz "Ticket312" Thornton](https://codex-of-the-damned.org/en/card-search/crypt/index.html?card=Liz%20%22Ticket312%22%20Thornton).
- Power cards — [Hide](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Hide), [Illuminate](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Illuminate), [Inspire](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Inspire).
- Action (Conviction-gated) — [Bond](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Bond).

## Query

Reproducible filter for all library cards requiring this virtue:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "inn")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "inn")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[entities/disciplines/defense|defense]], [[entities/disciplines/judgment|judgment]], [[entities/disciplines/martyrdom|martyrdom]], [[entities/disciplines/redemption|redemption]], [[entities/disciplines/vengeance|vengeance]], [[entities/disciplines/vision|vision]] — the other six Imbued virtues.
- No dedicated ruling page for Imbued / Conviction / True Faith yet — gap to fill on a later ingest.

## Sources

- src-002 — krcg vtes.json snapshot 2026-04-18 (virtue codes, card counts, creed co-occurrence, role examples).
