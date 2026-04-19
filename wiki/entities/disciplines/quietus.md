---
type: entity
tags: [discipline, legacy, quietus, banu-haqim, assamite, silent-death]
sources: [src-001, src-002]
last_verified: 2026-04-19
status: verified
---

# Quietus

**Code:** `[qui]` basic / `[QUI]` superior

## Overview

Quietus is the legacy **Assamite** (now Banu Haqim) discipline of the Silent Death — blood-based poisons, silencing strikes, and assassination tools. Mechanically a targeted-combat pool with unique blood-curse / blood-tempering actions that punish the prey's minions and pool. In V5 the shard has been **largely superseded by Blood Sorcery** for Banu Haqim; legacy Quietus cards are still legal where the clan card base carries `[qui]`, but new Banu Haqim crypt printings favor `[tha]` over `[qui]`.

## In-clan

Primary in-clan discipline for (legacy printings): **Banu Haqim** (Assamite).
Scattered across clans but concentrated almost exclusively on Banu Haqim crypt cards.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[qui]` (basic or superior): **42**
- Crypt vampires with `[qui]` or `[QUI]`: **90**

## Typical card roles

- Master-hate / hunting-ground attack — [Poison the Well of Life](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Poison%20the%20Well%20of%20Life) (burn a hunting ground; burn ALL hunting grounds at superior), [Blood Clots](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Blood%20Clots), [Erosion](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Erosion).
- Hunt-assist / blood-curse modifiers — [Succulent Vitae](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Succulent%20Vitae) (during hunt; stores on vampire to reduce cost of future `[qui]` cards), [Draught of the Soul](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Draught%20of%20the%20Soul).
- Silent / ranged combat — [Baal's Bloody Talons](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Baal%27s%20Bloody%20Talons), [Blood Agony](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Blood%20Agony), [Steely Tenacity](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Steely%20Tenacity).
- Action-chain / stealth-bleed — [Retain the Quick Blood](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Retain%20the%20Quick%20Blood) (unlock after action), [Truth of Blood](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Truth%20of%20Blood) (stealth-bleed action with discard-on-block punishment).
- Reactions / wake — [Blood Awakening](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Blood%20Awakening).

## Relationship to Blood Sorcery (V5)

In V5 Banu Haqim were redesigned around Blood Sorcery (`[tha]`). New Banu Haqim crypt cards typically list `[tha]` as an in-clan discipline, and many Quietus-themed spell effects were re-imagined as Blood Sorcery cards. Existing Quietus cards remain legal and retain their printed discipline cost — there is no errata consolidation.

See [[entities/disciplines/blood-sorcery|blood-sorcery]] for the V5 successor.

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "qui")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "qui")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[entities/disciplines/blood-sorcery|blood-sorcery]] — V5 successor for Banu Haqim.
- [[combat]] — Quietus combat package.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
