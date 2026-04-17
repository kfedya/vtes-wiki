---
type: entity
tags: [discipline, imbued-virtue, imbued, defense]
sources: [src-002]
last_verified: 2026-04-18
status: draft
---

# Defense

**Code:** `[def]` basic / `[DEF]` superior

## Overview

Defense is one of the seven Imbued **virtues** — the "discipline" analogue for Imbued minions (mortals with True Faith, not vampires) [src-002]. Virtues only appear on Imbued crypt cards and on library cards of the `Power` / `Conviction` card types that are playable exclusively by Imbued. Every Imbued carries exactly three virtues; the `def` code marks a minion as a Defender-aligned protector focused on shielding allies and tanking directed actions.

> Imbued virtues are distinct from vampire disciplines. A vampire cannot have `[def]`, and a Defense power card cannot be played by a vampire even via Discipline master cards [src-002]. Imbued-only card types (`Power`, `Conviction`) live in separate shards under `card-db/library/`.

## In-clan

Imbued creeds carrying Defense (src-002 snapshot):
- **Defender** — primary creed for Defense (`def` is a creed-defining virtue).
- **Judge**, **Martyr**, **Visionary** — scattered Defender-virtue crossovers.

No vampire clan has access to Defense.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[def]` (basic or superior): **3**
- Imbued crypt cards with `[def]` or `[DEF]`: **6**

## Typical card roles

- Defender crypt — [François "Warden" Loehr](https://codex-of-the-damned.org/en/card-search/crypt/index.html?card=Fran%C3%A7ois%20%22Warden%22%20Loehr), [Jack "Hannibal137" Harmon](https://codex-of-the-damned.org/en/card-search/crypt/index.html?card=Jack%20%22Hannibal137%22%20Harmon), [Lupe "Cabbie22" Droin](https://codex-of-the-damned.org/en/card-search/crypt/index.html?card=Lupe%20%22Cabbie22%22%20Droin), [Xian "DziDzat155" Quan](https://codex-of-the-damned.org/en/card-search/crypt/index.html?card=Xian%20%22DziDzat155%22%20Quan).
- Power cards — [Champion](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Champion), [Rejuvenate](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Rejuvenate).
- Action (Conviction-gated) — [Lock](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Lock).

## Query

Reproducible filter for all library cards requiring this virtue:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "def")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "def")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[entities/disciplines/innocence|innocence]], [[entities/disciplines/judgment|judgment]], [[entities/disciplines/martyrdom|martyrdom]], [[entities/disciplines/redemption|redemption]], [[entities/disciplines/vengeance|vengeance]], [[entities/disciplines/vision|vision]] — the other six Imbued virtues.
- No dedicated ruling page for Imbued / Conviction / True Faith yet — gap to fill on a later ingest.

## Sources

- src-002 — krcg vtes.json snapshot 2026-04-18 (virtue codes, card counts, creed co-occurrence, role examples).
