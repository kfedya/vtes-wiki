---
type: entity
tags: [discipline, 5e-core, animalism, retainer, combat]
sources: [src-001, src-002]
last_verified: 2026-04-19
status: verified
---

# Animalism

**Code:** `[ani]` basic / `[ANI]` superior

## Overview

Animalism is the discipline of communing with and commanding beasts. In play it fuels animal retainers, swarm-style combat cards that deal environmental damage via summoned creatures, and utility reactions that let the vampire see through animal senses [src-001 p. 53]. It is one of the nine 5E core disciplines.

## In-clan

Primary in-clan discipline for (5E-era printings): **Gangrel**, **Nosferatu**, **Ravnos**, **Tzimisce** (and their antitribu variants).
Also common on: Guruhi, Akunanse.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[ani]` (basic or superior): **73**
- Crypt vampires with `[ani]` or `[ANI]`: **476**

## Typical card roles

- Animal combat swarm — [Aid from Bats](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Aid%20from%20Bats), [Carrion Crows](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Carrion%20Crows).
- Animal retainers — [Raven Spy](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Raven%20Spy), [Owl Companion](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Owl%20Companion).
- Mass-attack actions — [Army of Rats](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Army%20of%20Rats), [Deep Song](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Deep%20Song).
- Intercept reactions via animal senses — [Cats' Guidance](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Cats%27%20Guidance), [Read the Winds](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Read%20the%20Winds).
- Big-beast allies — [Tier of Souls](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Tier%20of%20Souls).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "ani")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "ani")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[retainer]] — retainer rules (many Animalism cards are animal retainers).
- [[damage-resolution]] — environmental damage from animal combat cards.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
