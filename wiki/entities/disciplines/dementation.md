---
type: entity
tags: [discipline, legacy, dementation, malkavian, madness]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Dementation

**Code:** `[dem]` basic / `[DEM]` superior

## Overview

Dementation is the legacy Malkavian madness discipline — warping sanity, inflicting chaos on opponents, and bleeding through sheer derangement [src-002]. Mechanically it hosts the iconic Malkavian bleed actions, bounce-bleed reactions, and action-modifier chaos. In 5E, Malkavians returned to Auspex/Dominate/Obfuscate as their clan triad and Dementation is no longer a 5E core discipline, but it remains rich with legacy printings that are still fully legal.

## In-clan

Primary in-clan discipline for (legacy printings): **Malkavian**, **Malkavian antitribu**.
Scattered appearances on: Ravnos, Ishtarri, Baali.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[dem]` (basic or superior): **36**
- Crypt vampires with `[dem]` or `[DEM]`: **119**

## Typical card roles

- Signature bleed actions — [Kindred Spirits](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Kindred%20Spirits), [The Call](https://codex-of-the-damned.org/en/card-search/library/index.html?card=The%20Call).
- Bounce / bleed-redirect reactions — [Voice of Madness](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Voice%20of%20Madness), [Shattered Mirror](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Shattered%20Mirror).
- Madness-themed actions — [Lunatic Eruption](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Lunatic%20Eruption), [Total Insanity](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Total%20Insanity).
- Chaos action modifiers — [Confusion](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Confusion), [Eyes of Chaos](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Eyes%20of%20Chaos).
- Mind-breaking combat — [Coma](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Coma), [Abandoning the Flesh](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Abandoning%20the%20Flesh).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "dem")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "dem")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[entities/clans/malkavian]] — home clan for Dementation (legacy).
- [[target-redirection]] — Dementation bounce reactions participate in bleed-redirect chains.
- [[bleed]] — Dementation is a strong bleed discipline.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
