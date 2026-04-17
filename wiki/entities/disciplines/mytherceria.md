---
type: entity
tags: [discipline, legacy, mytherceria, kiasyd, faerie]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Mytherceria

**Code:** `[myt]` basic / `[MYT]` superior

## Overview

Mytherceria is the unique faerie-tainted discipline of the **Kiasyd** bloodline — a hybrid of fae trickery, cold iron lore, and mind-theft [src-002]. Mechanically it is a narrow clan-exclusive toolbox: a few intercept / blocking reactions, mind-control actions, and combat options that pair tightly with the Kiasyd's other primary discipline, Obtenebration. Not a 5E core discipline; effectively single-clan.

## In-clan

Primary in-clan discipline for (legacy printings): **Kiasyd**.
No other crypt cards carry Mytherceria in the current snapshot.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[myt]` (basic or superior): **16**
- Crypt vampires with `[myt]` or `[MYT]`: **16**

## Typical card roles

- Faerie reaction / blocking — [Faerie Wards](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Faerie%20Wards), [Folderol](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Folderol).
- Mind-theft actions — [Steal the Mind](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Steal%20the%20Mind), [Pandora's Whisper](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Pandora%27s%20Whisper).
- Gremlin / goblin havoc — [Gremlins](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Gremlins), [Goblinism](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Goblinism).
- Fae combat — [Darkling Trickery](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Darkling%20Trickery), [Basilisk's Touch](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Basilisk%27s%20Touch), [Earth Swords](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Earth%20Swords).
- Unique retainer / equipment — [Redcap Wilder](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Redcap%20Wilder), [Tinglestripe](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Tinglestripe).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "myt")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "myt")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[entities/disciplines/obtenebration]] — Kiasyd's other clan discipline; Mytherceria decks lean on it for shadow combat.
- [[combat]] — most Mytherceria cards are combat or reaction cards.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
