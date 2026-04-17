---
type: entity
tags: [discipline, 5e-core, dominate, bleed, mind-control]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Dominate

**Code:** `[dom]` basic / `[DOM]` superior

## Overview

Dominate is the discipline of mind control — direct psychic command over mortals and other vampires. Mechanically it is the signature **bleed-increase** discipline: most Dominate action modifiers raise bleed strength, and its defining reaction ([Deflection](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Deflection)) redirects a bleed back up the table [src-001 p. 53]. It is one of the nine 5E core disciplines.

## In-clan

Primary in-clan discipline for (5E-era printings): **Ventrue**, **Tremere**, **Lasombra**, **Giovanni**, **Malkavian** (and their antitribu variants).
Also common on: Tzimisce.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[dom]` (basic or superior): **58**
- Crypt vampires with `[dom]` or `[DOM]`: **593**

## Typical card roles

- Bleed increase — [Conditioning](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Conditioning), [Command of the Beast](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Command%20of%20the%20Beast).
- Bleed bounce — [Deflection](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Deflection).
- Pool-theft actions — [Govern the Unaligned](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Govern%20the%20Unaligned), [Graverobbing](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Graverobbing).
- Permanent mind-lock — [Bonding](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Bonding).
- Action-hijacking — [Mouthpiece](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Mouthpiece), [Foreshadowing Destruction](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Foreshadowing%20Destruction).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "dom")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "dom")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[bleed]] — bleed action; Dominate is the main bleed-boost discipline.
- [[target-redirection]] — Deflection is the classic Dominate redirect.
- [[stealth-modifiers]] — Bonding is listed among transfer-stealth cases.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
