---
type: entity
tags: [discipline, v5, oblivion, hecata, lasombra, shadow, death]
sources: [src-001, src-002]
last_verified: 2026-04-19
status: verified
---

# Oblivion

**Code:** `[obl]` basic / `[OBL]` superior

## Overview

Oblivion is the V5 consolidated discipline of shadow-and-death magic — the void between worlds, drawn on by both Lasombra (formerly Obtenebration) and Hecata (formerly Necromancy) in modern V5 lore [src-002]. Mechanically it spans summoned-shadow allies, shadow combat, stealth-void action modifiers, and a handful of ghostly actions. Introduced alongside V5; partly supersedes legacy [[entities/disciplines/obtenebration|Obtenebration]] and [[entities/disciplines/necromancy|Necromancy]] without replacing their card pools — legacy cards remain fully legal.

## In-clan

Primary in-clan discipline for (V5-era printings): **Hecata**, **Lasombra**.
Scattered appearances on: Tremere (V5 Banu Haqim / Hecata crossover printings).

## V5 / legacy relationship

- Oblivion is the V5-era consolidation introduced for Lasombra (joining the Camarilla in V5) and the Hecata clan.
- It **does not errata or replace** legacy [[entities/disciplines/obtenebration|Obtenebration]] `[obt]` or [[entities/disciplines/necromancy|Necromancy]] `[nec]` cards. Old and new cards coexist.
- A V5 Lasombra with `[OBL]` can typically also play legacy `[obt]` cards if they have the corresponding legacy discipline on their crypt card. Many V5 Lasombra carry both.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[obl]` (basic or superior): **22**
- Crypt vampires with `[obl]` or `[OBL]`: **39**

## Typical card roles

- Shadow-summoned allies — [Rotting Behemoth](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Rotting%20Behemoth), [Bone Shambler](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Bone%20Shambler), [Spectral Servitor](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Spectral%20Servitor).
- Shadow combat — [Arms of Ahriman](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Arms%20of%20Ahriman), [Touch of Oblivion](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Touch%20of%20Oblivion), [Shadow Cast](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Shadow%20Cast).
- Stealth / void action modifiers — [Shadow Cloak](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Shadow%20Cloak), [Stygian Shroud](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Stygian%20Shroud), [Where the Veil Thins](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Where%20the%20Veil%20Thins).
- Stealth rush action — [Umbrous Clutch](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Umbrous%20Clutch) (+1 stealth; enter combat; maneuver at superior).
- Bleed / attrition action — [Shroud of Decay](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Shroud%20of%20Decay) (basic = bleed +1 with discard-on-success; superior = remove 7 from prey's ash heap to burn 3 pool).
- Reactions — [Shadow Sentinel](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Shadow%20Sentinel), [Truth in Darkness](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Truth%20in%20Darkness).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "obl")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "obl")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[entities/disciplines/obtenebration]] — legacy predecessor for Lasombra Oblivion.
- [[entities/disciplines/necromancy]] — legacy predecessor for Hecata Oblivion.
- [[combat]] — shadow combat cards.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
