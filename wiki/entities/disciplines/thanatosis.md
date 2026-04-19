---
type: entity
tags: [discipline, legacy, thanatosis, samedi, decay]
sources: [src-001, src-002]
last_verified: 2026-04-19
status: verified
---

# Thanatosis

**Code:** `[thn]` basic / `[THN]` superior

## Overview

Thanatosis is the legacy **Samedi** discipline of decay and necrosis — rotting flesh, releasing plague, and animating corpses. Mechanically a combat-heavy pool: disease and putrefaction combat cards that cause unpreventable damage or corrupt the opposing minion, plus a handful of bleed-focused action modifiers. A small, mostly single-clan discipline.

## In-clan

Primary in-clan discipline for (legacy printings): **Samedi**.
Scattered on a few Harbingers of Skulls and Giovanni in the snapshot.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[thn]` (basic or superior): **18**
- Crypt vampires with `[thn]` or `[THN]`: **27**

## Typical card roles

Verified against card-db snapshot 2026-04-18 [src-002].

- Decay / disease combat — [Necrosis](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Necrosis), [Putrefaction](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Putrefaction), [Infection](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Infection), [Creeping Infection](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Creeping%20Infection), [Withering](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Withering), [Groaning Corpse](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Groaning%20Corpse) (environmental damage per round at close range).
- Ash / dust transformations — [Ashes to Ashes](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Ashes%20to%20Ashes), [Dust to Dust](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Dust%20to%20Dust), [Rigor Mortis](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Rigor%20Mortis).
- Corpse allies / retainers — [Reanimated Corpse](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Reanimated%20Corpse), [Relentless Reaper](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Relentless%20Reaper).
- Debuff / stealth-tax curse actions — [Decompose](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Decompose) (+1 stealth action; puts -1 stealth curse on target minion, blocks additional strikes).
- Zombie / retainer take-over actions — [Pressing Flesh](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Pressing%20Flesh) (+1 stealth; revive burned ally as a zombie), [Putrescent Servitude](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Putrescent%20Servitude) (+1 stealth; move mortal/ghoul retainer or attach to ally).
- Action modifiers — [Transfusion](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Transfusion), [Hag's Wrinkles](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Hag%27s%20Wrinkles), [Under My Skin](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Under%20My%20Skin).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "thn")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "thn")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[combat]] — Thanatosis combat package.
- [[damage-resolution]] — disease / aggravated damage rules.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
