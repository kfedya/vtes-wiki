---
type: entity
tags: [discipline, 5e-core, auspex, intercept, reaction]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Auspex

**Code:** `[aus]` basic / `[AUS]` superior

## Overview

Auspex is the discipline of heightened perception — seeing through walls, sensing auras, and reading minds. Mechanically it is the premier **intercept** discipline: most Auspex cards add intercept, scry the top of the library, or cancel concealment on the opposing action [src-001 p. 53]. It is one of the nine 5E core disciplines.

## In-clan

Primary in-clan discipline for (5E-era printings): **Malkavian**, **Toreador**, **Tremere** (and their antitribu variants).
Also common on: Tzimisce, Salubri.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[aus]` (basic or superior): **75**
- Crypt vampires with `[aus]` or `[AUS]`: **752**

## Typical card roles

- Intercept reaction — [Telepathic Misdirection](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Telepathic%20Misdirection), [Eyes of Argus](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Eyes%20of%20Argus).
- Library scrying / card-selection — [Precognition](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Precognition), [Spirit's Touch](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Spirit%27s%20Touch).
- Vote bounce / aura reading — [Sense the Sin](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Sense%20the%20Sin), [Aura Absorption](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Aura%20Absorption).
- Combat fire-support — [Telepathic Tracking](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Telepathic%20Tracking).
- Bleed / action acceleration — [Pulse of the Canaille](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Pulse%20of%20the%20Canaille).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "aus")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "aus")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[entities/card-types/reaction]] — many Auspex cards are reactions (intercept).
- [[block-resolution]] — stealth vs intercept comparison.
- [[stealth-modifiers]] — the other side of the equation.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
