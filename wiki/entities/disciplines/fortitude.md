---
type: entity
tags: [discipline, 5e-core, fortitude, damage-prevention, combat]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Fortitude

**Code:** `[for]` basic / `[FOR]` superior

## Overview

Fortitude is the discipline of physical resilience. Its bread-and-butter is **damage prevention** in combat, plus a smaller set of action-modifier staples that give aggressive decks extra tempo (sun-cover and post-combat re-unlock) [src-001 p. 53]. It is one of the nine 5E core disciplines.

## In-clan

Primary in-clan discipline for (5E-era printings): **Ventrue**, **Gangrel** (and their antitribu variants).
Also common on: Ravnos, Harbinger of Skulls, Salubri, Akunanse.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[for]` (basic or superior): **64**
- Crypt vampires with `[for]` or `[FOR]`: **635**

## Typical card roles

- Damage prevention — [Skin of Steel](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Skin%20of%20Steel), [Skin of Rock](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Skin%20of%20Rock), [Superior Mettle](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Superior%20Mettle).
- Post-combat unlock — [Freak Drive](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Freak%20Drive).
- Extra actions from sun-cover — [Day Operation](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Day%20Operation), [Dawn Operation](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Dawn%20Operation), [Daring the Dawn](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Daring%20the%20Dawn).
- Action-speed ramp — [Forced March](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Forced%20March) (shared with Celerity).
- Anti-Anarch tempo — [Ni Dieu ni Maître](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Ni%20Dieu%20ni%20Ma%C3%AEtre).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "for")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "for")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[damage-resolution]] — prevent/mend rules; Fortitude is the main prevent source.
- [[post-combat-effects]] — Freak Drive timing after combat.
- [[entities/card-types/combat-card]] — most Fortitude cards are combat cards.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
