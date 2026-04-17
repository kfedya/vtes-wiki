---
type: entity
tags: [discipline, imbued-virtue, imbued, vision]
sources: [src-002]
last_verified: 2026-04-18
status: draft
---

# Vision

**Code:** `[viz]` basic / `[VIZ]` superior

## Overview

Vision is one of the seven Imbued **virtues** — the "discipline" analogue for Imbued minions (mortals with True Faith, not vampires) [src-002]. Virtues only appear on Imbued crypt cards and on library cards of the `Power` / `Conviction` card types that are playable exclusively by Imbued. Every Imbued carries exactly three virtues; `viz` is the Visionary creed's signature virtue, themed around library-scrying, conviction flow, and foresight reactions.

> **Code clarification:** Vision uses `[viz]`, not `[vis]`. The three-letter code `vis` is **Visceratika** (the Gargoyle vampire discipline — see [[entities/disciplines/visceratika|visceratika]]). The two shards never overlap: `[vis]` cards appear only on Gargoyle library/crypt cards, while `[viz]` cards appear only on Imbued cards [src-002]. Do not conflate the two when querying card-db.

## In-clan

Imbued creeds carrying Vision (src-002 snapshot):
- **Visionary** — primary creed for Vision.
- **Martyr**, **Redeemer**, **Avenger** — scattered cross-creed appearances.

No vampire clan has access to Vision.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[viz]` (basic or superior): **3**
- Imbued crypt cards with `[viz]` or `[VIZ]`: **6**

## Typical card roles

- Visionary crypt — [Earl "Shaka74" Deams](https://codex-of-the-damned.org/en/card-search/crypt/index.html?card=Earl%20%22Shaka74%22%20Deams), [Jennie "Cassie247" Orne](https://codex-of-the-damned.org/en/card-search/crypt/index.html?card=Jennie%20%22Cassie247%22%20Orne), [Paul "Sixofswords29" Moreton](https://codex-of-the-damned.org/en/card-search/crypt/index.html?card=Paul%20%22Sixofswords29%22%20Moreton).
- Action — [Augur](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Augur).
- Power cards — [Foresee](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Foresee).
- Reaction — [Determine](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Determine).

## Query

Reproducible filter for all library cards requiring this virtue:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "viz")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "viz")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[entities/disciplines/visceratika|visceratika]] — disambiguation: `vis` ≠ `viz`.
- [[entities/disciplines/defense|defense]], [[entities/disciplines/innocence|innocence]], [[entities/disciplines/judgment|judgment]], [[entities/disciplines/martyrdom|martyrdom]], [[entities/disciplines/redemption|redemption]], [[entities/disciplines/vengeance|vengeance]] — the other six Imbued virtues.
- No dedicated ruling page for Imbued / Conviction / True Faith yet — gap to fill on a later ingest.

## Sources

- src-002 — krcg vtes.json snapshot 2026-04-18 (virtue codes, card counts, creed co-occurrence, role examples).
