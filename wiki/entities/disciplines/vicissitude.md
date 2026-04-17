---
type: entity
tags: [discipline, legacy, vicissitude, tzimisce, fleshcraft]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Vicissitude

**Code:** `[vic]` basic / `[VIC]` superior

## Overview

Vicissitude is the legacy **Tzimisce** discipline of fleshcrafting — reshaping bone and flesh, growing grotesque combat weapons, and remoulding minions into grotesque constructs. Mechanically a combat-heavy pool: natural-weapon strikes, armour, shape-shifting dodges, and a handful of corrupt action modifiers. Not a 5E core discipline; Tzimisce remain outside the 5E core clans but retain Vicissitude as their signature.

## In-clan

Primary in-clan discipline for (legacy printings): **Tzimisce**.
Also scattered on: Blood Brother, Gangrel antitribu, Malkavian antitribu, Tremere (and antitribu variants).

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[vic]` (basic or superior): **30**
- Crypt vampires with `[vic]` or `[VIC]`: **104**

## Typical card roles

- Fleshcraft combat — [Fleshcraft](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Fleshcraft), [Bonecraft](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Bonecraft), [Body Arsenal](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Body%20Arsenal), [Breath of the Dragon](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Breath%20of%20the%20Dragon), [Chiropteran Marauder](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Chiropteran%20Marauder).
- Shape-shift / body-reform — [Bloodform](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Bloodform), [Blood of Acid](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Blood%20of%20Acid), [Plasmic Form](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Plasmic%20Form), [Reform Body](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Reform%20Body).
- Identity / face-changing action modifiers — [Changeling](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Changeling), [Malleable Visage](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Malleable%20Visage), [Lobotomy](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Lobotomy), [Loose Cannon](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Loose%20Cannon).
- Crafting / transformation actions — [Soul Decoration](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Soul%20Decoration), [Root of Vitality](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Root%20of%20Vitality), [The World's a Canvas](https://codex-of-the-damned.org/en/card-search/library/index.html?card=The%20World%27s%20a%20Canvas), [Bauble](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Bauble).
- Construct allies — [Corrupt Construction](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Corrupt%20Construction).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "vic")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "vic")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[combat]] — Vicissitude fleshcraft combat package.
- [[damage-resolution]] — armour / prevent interactions.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
