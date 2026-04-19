---
type: entity
tags: [discipline, 5e-core, celerity, combat, speed]
sources: [src-001, src-002]
last_verified: 2026-04-19
status: verified
---

# Celerity

**Code:** `[cel]` basic / `[CEL]` superior

## Overview

Celerity is the discipline of supernatural speed. It lets vampires take **additional strikes** in combat, add maneuvers, and act faster than normal [src-001 p. 53]. Celerity cards are overwhelmingly combat-oriented, with a small set of action modifiers (extra actions, haste-style tempo). It is one of the nine 5E core disciplines.

## In-clan

Primary in-clan discipline for (5E-era printings): **Brujah**, **Toreador**, **Banu Haqim** (and their antitribu variants).
Also common on: Ishtarri, Osebo, Gangrel antitribu.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[cel]` (basic or superior): **67**
- Crypt vampires with `[cel]` or `[CEL]`: **570**

## Typical card roles

Verified against card-db snapshot 2026-04-18 [src-002].

- Additional strikes — [Blur](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Blur), [Lightning Reflexes](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Lightning%20Reflexes), [Pursuit](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Pursuit) (superior), [Quickness](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Quickness).
- Press / combat-continuation — [Psyche!](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Psyche%21), [Flash](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Flash) (maneuver or press).
- Dodge / evasion — [Sideslip](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Sideslip), [Swift Cover](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Swift%20Cover) (dual CEL/OBF, dodge basic / +1 stealth superior), [Sanguine Entrapment](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Sanguine%20Entrapment).
- Maneuver / range control — [Flash](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Flash), [Mercury's Arrow](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Mercury%27s%20Arrow), [Scourge of Alecto](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Scourge%20of%20Alecto).
- Post-action unlock — [Forced March](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Forced%20March), [Instantaneous Transformation](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Instantaneous%20Transformation), [Zephyr](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Zephyr).
- Stealth modifier (action) — [Alacrity](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Alacrity) (+1 stealth + block-contingent maneuver), [The Missing Voice](https://codex-of-the-damned.org/en/card-search/library/index.html?card=The%20Missing%20Voice), [Relentlessness](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Relentlessness).
- Evasive multi-role — [Resist Earth's Grasp](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Resist%20Earth%27s%20Grasp) (maneuver + stealth + press, depending on mode).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "cel")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "cel")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[entities/card-types/combat-card]] — most Celerity cards are combat cards.
- [[strike]] — additional strike rules.
- [[maneuver]] — Celerity frequently adds maneuvers.
- [[press]] — Celerity helps get extra rounds.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
