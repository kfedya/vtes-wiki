---
type: entity
tags: [discipline, legacy, serpentis, ministry, followers-of-set, temptation]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Serpentis

**Code:** `[ser]` basic / `[SER]` superior

## Overview

Serpentis is the legacy **Followers of Set** (now Ministry) discipline of temptation and serpentine transformation — cobra forms, corruption bleeds, and heart-of-darkness soul manipulation. Mechanically a stealth-bleed / corruption pool: action modifiers that bait redirects, snake-form combat, and Condemnation / Mark-of-Damnation curse actions. Not a 5E core discipline; the Ministry in V5 retain Serpentis as a secondary discipline alongside new tools.

## In-clan

Primary in-clan discipline for (legacy printings): **Ministry** / **Followers of Set**.
Scattered across clans but heavily concentrated on Ministry crypt cards.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[ser]` (basic or superior): **47**
- Crypt vampires with `[ser]` or `[SER]`: **89**

## Typical card roles

- Transformation / snake forms — [Form of the Serpent](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Form%20of%20the%20Serpent), [Eyes of the Serpent](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Eyes%20of%20the%20Serpent), [Form of Corruption](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Form%20of%20Corruption).
- Temptation / corruption actions — [Enticement](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Enticement), [Lure of the Serpent](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Lure%20of%20the%20Serpent), [Revelation of Desire](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Revelation%20of%20Desire), [Truth of a Thousand Lies](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Truth%20of%20a%20Thousand%20Lies).
- Curse / soul-mark actions — [Condemnation: Betrayed](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Condemnation%3A%20Betrayed), [Mark of Damnation](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Mark%20of%20Damnation), [Heart of Darkness](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Heart%20of%20Darkness).
- Venom / stealth modifiers — [Venenation](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Venenation), [Divine Image](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Divine%20Image), [Velvet Tongue](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Velvet%20Tongue).
- Diablerie-like soul actions — [Consignment to Duat](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Consignment%20to%20Duat), [Dismemberment of Osiris](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Dismemberment%20of%20Osiris).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "ser")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "ser")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[bleed]] — many Serpentis action modifiers boost bleed.
- [[target-redirection]] — temptation-style redirect interactions.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
