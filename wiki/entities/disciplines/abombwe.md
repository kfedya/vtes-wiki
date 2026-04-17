---
type: entity
tags: [discipline, legacy, laibon, abombwe, combat]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Abombwe

**Code:** `[abo]` basic / `[ABO]` superior

## Overview

Abombwe is a legacy Laibon discipline representing mastery of the predator's totem spirit. Mechanically it is a small pool: a handful of combat tricks that shift the vampire into beast-form body parts, plus a predator-themed reaction / action-modifier sub-set [src-002]. It is not part of the 5E core nine.

## In-clan

Primary in-clan discipline for (legacy printings): **Akunanse** (Laibon).
Scattered appearances on: Gangrel, Guruhi.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[abo]` (basic or superior): **14**
- Crypt vampires with `[abo]` or `[ABO]`: **25**

## Typical card roles

- Beast-form combat (transforming body parts) — [Devil-Channel: Throat](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Devil-Channel%3A%20Throat), [Devil-Channel: Hands](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Devil-Channel%3A%20Hands), [Devil-Channel: Feet](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Devil-Channel%3A%20Feet).
- Predator action modifiers — [Predator's Mastery](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Predator%27s%20Mastery), [Predator's Transformation](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Predator%27s%20Transformation).
- Reactions / intercept via beast senses — [Predator's Communion](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Predator%27s%20Communion).
- Beast-invocation combat — [Invoking the Beast](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Invoking%20the%20Beast), [Taming the Beast](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Taming%20the%20Beast).
- Skin-taking shapeshift toolbox — [Taking the Skin: Minion](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Taking%20the%20Skin%3A%20Minion), [Taking the Skin: Vulture](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Taking%20the%20Skin%3A%20Vulture).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "abo")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "abo")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[entities/sects/laibon]] — Abombwe is a Laibon-era discipline.
- [[combat]] — most Abombwe cards are combat cards.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
