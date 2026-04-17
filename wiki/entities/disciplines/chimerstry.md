---
type: entity
tags: [discipline, legacy, chimerstry, illusion, ravnos]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Chimerstry

**Code:** `[chi]` basic / `[CHI]` superior

## Overview

Chimerstry is the legacy Ravnos discipline of illusion — conjuring phantasms that can deceive the senses, block actions, or inflict real harm when the victim believes the illusion [src-002]. Mechanically it is a deep library of stealth-bleed action modifiers, bleed-and-pool pressure actions, and illusory combat cards that ignore many defences. Not a 5E core discipline; Ravnos have legacy-era printings.

## In-clan

Primary in-clan discipline for (legacy printings): **Ravnos**.
Scattered appearances on: Giovanni, Ishtarri, Lasombra, Ministry.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[chi]` (basic or superior): **48**
- Crypt vampires with `[chi]` or `[CHI]`: **84**

## Typical card roles

- Bleed / pool-pressure actions — [Illusory Resources](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Illusory%20Resources), [Mass Reality](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Mass%20Reality).
- Stealth action modifiers — [Fata Morgana](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Fata%20Morgana), [Smoke and Mirrors](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Smoke%20and%20Mirrors).
- Illusory combat — [Horrid Reality](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Horrid%20Reality), [Apparition](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Apparition).
- Mind-twisting actions — [Sensory Deprivation](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Sensory%20Deprivation), [Shared Nightmare](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Shared%20Nightmare).
- Card-manipulation trickery — [Sleight of Hand](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Sleight%20of%20Hand), [Mirror's Visage](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Mirror%27s%20Visage).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "chi")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "chi")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[stealth-modifiers]] — Chimerstry contributes many +stealth modifiers.
- [[combat]] — illusory combat cards.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
