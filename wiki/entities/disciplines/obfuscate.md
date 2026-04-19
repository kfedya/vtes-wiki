---
type: entity
tags: [discipline, 5e-core, obfuscate, stealth, concealment]
sources: [src-001, src-002]
last_verified: 2026-04-19
status: verified
---

# Obfuscate

**Code:** `[obf]` basic / `[OBF]` superior

## Overview

Obfuscate is the discipline of **stealth and concealment** — hiding from sight, clouding minds, going unseen. In game terms it is the premier source of +stealth action modifiers that punch unblockable bleeds and actions through to resolution [src-001 p. 53]. It is one of the nine 5E core disciplines.

## In-clan

Primary in-clan discipline for (5E-era printings): **Nosferatu**, **Malkavian**, **Banu Haqim**, **Ministry** (and their antitribu variants).
Also common on: Baali, Gangrel antitribu.

## Card counts (src-002 snapshot 2026-04-18)

- Library cards requiring `[obf]` (basic or superior): **72**
- Crypt vampires with `[obf]` or `[OBF]`: **607**

## Typical card roles

- +1 stealth action modifier — [Cloak the Gathering](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Cloak%20the%20Gathering), [Faceless Night](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Faceless%20Night), [Lost in Crowds](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Lost%20in%20Crowds).
- +2 stealth / scale stealth — [Swallowed by the Night](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Swallowed%20by%20the%20Night), [Veil the Legions](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Veil%20the%20Legions).
- +2/+3 stealth (non-bleed actions only) — [Forgotten Labyrinth](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Forgotten%20Labyrinth).
- Identity swap / elder-mimicry — [Elder Impersonation](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Elder%20Impersonation).
- Domain / game-action stealth — [Domain of Evernight](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Domain%20of%20Evernight).

## Query

Reproducible filter for all library cards requiring this discipline:

```
jq -s '[.[][] | select(.disciplines[]? | ascii_downcase == "obf")] | length' card-db/library/*.json
```

List names:

```
jq -rs '[.[][] | select(.disciplines[]? | ascii_downcase == "obf")] | .[] | .name' card-db/library/*.json
```

## Related

- [[entities/card-types/library]] — library card mechanics.
- [[stealth-modifiers]] — central ruling page; Obfuscate is the main printed-stealth source.
- [[block-resolution]] — stealth vs intercept comparison.
- [[bleed]] — Obfuscate supplies the stealth side of bleed actions.

## Sources

- src-001 — VTES 5E Rulebook, p. 53 (Quick Reference discipline list).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card counts, clan co-occurrence, role examples).
