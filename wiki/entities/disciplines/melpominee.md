---
type: entity
tags: [discipline, legacy, melpominee, daughters-of-cacophony, voice]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Melpominee

**Code:** `[mel]` basic / `[MEL]` superior

## Overview

Melpominee is the unique song-and-voice discipline of the **Daughters of Cacophony** bloodline — weaponized vocal performance, harmonic resonance, and audience-charming politics [src-002]. Mechanically it is a narrow discipline tightly bound to its home clan: voice-based action modifiers that stack with Presence vote play, crescendo bleed actions, and rare political action cards. Not a 5E core discipline; effectively single-clan.

## In-clan

Primary in-clan discipline for (legacy printings): **Daughter of Cacophony**.
No other crypt cards carry Melpominee in the current snapshot.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[mel]` (basic or superior): **16**
- Crypt vampires with `[mel]` or `[MEL]`: **14**

## Typical card roles

- Voice action modifiers — [Siren's Lure](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Siren%27s%20Lure), [Madrigal](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Madrigal), [Virtuosa](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Virtuosa).
- Crescendo bleed / action — [Shattering Crescendo](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Shattering%20Crescendo), [Persistent Echo](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Persistent%20Echo).
- Audience-charm bleed action — [Blessed Audience](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Blessed%20Audience), [Choir](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Choir).
- Political actions — [Fanfare for Elysium](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Fanfare%20for%20Elysium), [Lily Prelude](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Lily%20Prelude).
- Combat against Toreador / kin — [Toreador's Bane](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Toreador%27s%20Bane), [Death of the Drum](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Death%20of%20the%20Drum).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "mel")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "mel")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[entities/disciplines/presence]] — Melpominee decks typically lean on Presence for vote play.
- [[politics]] — Daughters of Cacophony vote archetype uses Melpominee political-action cards.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
