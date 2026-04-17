---
type: entity
tags: [discipline, legacy, obeah, salubri, healing]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Obeah

**Code:** `[obe]` basic / `[OBE]` superior

## Overview

Obeah is the legacy discipline of the **Salubri** healer tradition — laying-on-of-hands that restores blood, cures derangements, and can even return a vampire from torpor [src-002]. Mechanically it is a defensive / support pool: blood-return actions, stasis-style action modifiers, and damage-prevent combat cards. Not a 5E core discipline; rare outside the Salubri bloodline.

## In-clan

Primary in-clan discipline for (legacy printings): **Salubri** (healer tradition).
No other crypt cards carry Obeah in the current snapshot.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[obe]` (basic or superior): **20**
- Crypt vampires with `[obe]` or `[OBE]`: **13**

## Typical card roles

- Healing / blood-return actions — [Healing Touch](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Healing%20Touch), [Renewed Vigor](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Renewed%20Vigor), [Panacea](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Panacea).
- Torpor-rescue / cleanse — [Resurrection](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Resurrection), [Cleansing Ritual](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Cleansing%20Ritual).
- Damage-prevent combat — [Anesthetic Touch](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Anesthetic%20Touch), [Vitae Block](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Vitae%20Block).
- Defensive action modifiers — [Neutral Guard](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Neutral%20Guard), [Safe Passage](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Safe%20Passage), [Repulsion](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Repulsion).
- Truth / reaction — [Glare of Lies](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Glare%20of%20Lies), [Peacemaker](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Peacemaker).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "obe")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "obe")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[damage-resolution]] — many Obeah combat cards are damage-prevention.
- [[rescue-from-torpor]] — Obeah has torpor-recovery actions.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
