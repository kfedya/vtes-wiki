---
type: entity
tags: [discipline, legacy, protean, gangrel, shapeshifting]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Protean

**Code:** `[pro]` basic / `[PRO]` superior

## Overview

Protean is the legacy discipline of **bestial transformation** — growing claws, taking animal forms (wolf, bat, mist, cobra), melding with the earth for daytime cover. Mechanically a hybrid action-modifier / combat pool: native-weapon strikes, travel-style +stealth forms, and environmental-damage combat ends. Not a 5E core discipline, but one of the most widely printed legacy disciplines across clans.

## In-clan

Primary in-clan discipline for (legacy printings): **Gangrel** (and Gangrel antitribu).
Also frequent on: Tzimisce, Ministry (Followers of Set), Ahrimane, Nosferatu.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[pro]` (basic or superior): **56**
- Crypt vampires with `[pro]` or `[PRO]`: **285**

## Typical card roles

- Transformation / native weapons — [Form of the Bat](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Form%20of%20the%20Bat), [Form of the Cobra](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Form%20of%20the%20Cobra), [Spirit Claws](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Spirit%27s%20Claws), [Rapid Change](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Rapid%20Change).
- Earth-meld / daytime cover — [Earth Control](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Earth%20Control), [Earth Meld](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Earth%20Meld), [Beast Meld](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Beast%20Meld).
- Combat ends / environmental damage — [Taste of Vitae](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Taste%20of%20Vitae), [Flesh of Marble](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Flesh%20of%20Marble).
- Stealth action modifiers — [Instantaneous Transformation](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Instantaneous%20Transformation), [Mantle of the Bestial Majesty](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Mantle%20of%20the%20Bestial%20Majesty).
- Monstrous bruiser actions — [Monstrous Form](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Monstrous%20Form), [Horrific Countenance](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Horrific%20Countenance).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "pro")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "pro")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[combat]] — Protean native-weapon strikes.
- [[strike-effects]] — many Protean forms grant alternative strikes.
- [[entities/disciplines/animalism|animalism]] — sibling beast-themed discipline for Gangrel.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
