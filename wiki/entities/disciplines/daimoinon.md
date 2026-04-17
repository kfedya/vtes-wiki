---
type: entity
tags: [discipline, legacy, daimoinon, baali, infernal]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Daimoinon

**Code:** `[dai]` basic / `[DAI]` superior

## Overview

Daimoinon is the legacy Baali discipline of infernal power — commanding demons, wielding hellfire, and cursing opponents with lasting Condemnation tokens [src-002]. Mechanically it is a small combat-and-curse pool: aggravated-damage fire combat, persistent Condemnation actions that sit on target minions, and a few infernal action modifiers. Not a 5E core discipline.

## In-clan

Primary in-clan discipline for (legacy printings): **Baali**.
Scattered appearances on: Malkavian, Tremere, Tremere antitribu.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[dai]` (basic or superior): **18**
- Crypt vampires with `[dai]` or `[DAI]`: **24**

## Typical card roles

- Condemnation curses (persistent per-minion tokens) — [Condemnation: Doomed](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Condemnation%3A%20Doomed), [Condemnation: Betrayed](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Condemnation%3A%20Betrayed), [Condemnation: Languid](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Condemnation%3A%20Languid).
- Hellfire combat (aggravated damage) — [Conflagration](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Conflagration), [Flames of the Netherworld](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Flames%20of%20the%20Netherworld).
- Fear combat cards — [Fear of the Void Below](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Fear%20of%20the%20Void%20Below).
- Infernal ally / summon — [Infernal Servitor](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Infernal%20Servitor).
- Action modifiers / aura reading — [Sense the Sin](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Sense%20the%20Sin), [I am Legion](https://codex-of-the-damned.org/en/card-search/library/index.html?card=I%20am%20Legion).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "dai")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "dai")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[traits]] — Infernal trait (1-pool unlock cost) shows up on Baali.
- [[combat]] — hellfire aggravated-damage combat.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
