---
type: entity
tags: [discipline, legacy, dementation, malkavian, madness]
sources: [src-001, src-002]
last_verified: 2026-04-19
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

Verified against card-db snapshot 2026-04-18 [src-002].

- Signature bleed action — [Kindred Spirits](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Kindred%20Spirits) (directed bleed +1 pool on success; +1 bleed at superior).
- Influence-ramp action — [The Call](https://codex-of-the-damned.org/en/card-search/library/index.html?card=The%20Call) (AUS/DEM, +1 stealth; add 2/3 blood to a younger `[dem]` vampire in uncontrolled region).
- Block-ending reactions — [Voice of Madness](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Voice%20of%20Madness) (on block of ally/younger: lock self, end action; superior burns 1 from acting minion), [Shattered Mirror](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Shattered%20Mirror) (on block of ally/younger bleeder: end action + persistent -1 bleed debuff on acting minion).
- Attach-to-minion madness actions — [Lunatic Eruption](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Lunatic%20Eruption) (force attached minion into combat with prey each turn), [Total Insanity](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Total%20Insanity) (-1 stealth + ticking action-lockout on ally/younger).
- Bleed modifiers — [Confusion](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Confusion) ((limited) +1 bleed; +1 stealth + bleed at superior), [Eyes of Chaos](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Eyes%20of%20Chaos) ((limited) +1/+2 bleed).
- Mind-breaking combat — [Coma](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Coma) (strike: send opposing vampire to torpor), [Abandoning the Flesh](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Abandoning%20the%20Flesh) (escape-burn reaction; stays in play as a +1 bleed enabler for other `[dem]` vampires).

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
