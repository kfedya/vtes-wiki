---
type: entity
tags: [clan, legacy, antitribu, brujah, sabbat]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Brujah antitribu

## Overview

Brujah antitribu is the legacy **Sabbat offshoot** of [[entities/clans/brujah|Brujah]] [src-002]. Antitribu are a persistent VTES pattern: the Sabbat-aligned parallel of a mainstream clan, printed under its own `<Clan> antitribu` name but sharing the parent's discipline identity almost exactly. Of 43 Brujah antitribu vampires, `CEL` (25), `POT` (25), and `PRE` (23) dominate superior disciplines — the same CEL/POT/PRE signature as mainstream Brujah [src-002].

## Parent clan relationship

- Parent: [[entities/clans/brujah|Brujah]] (Camarilla + Anarch in V5; 94 crypt).
- Antitribu variant: Sabbat-aligned since the legacy era; 43 crypt.
- Discipline signature: **identical** to parent (CEL / POT / PRE).

## In-clan disciplines

- [[entities/disciplines/celerity|Celerity]] — `[cel]`
- [[entities/disciplines/potence|Potence]] — `[pot]`
- [[entities/disciplines/presence|Presence]] — `[pre]`

## Sect alignment

Primarily **[[entities/sects/sabbat|Sabbat]]** — the defining feature of the antitribu identity.

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires: **43**
- Crypt vampires with `[CEL]` at superior: **25**
- Crypt vampires with `[POT]` at superior: **25**
- Crypt vampires with `[PRE]` at superior: **23**

## Notable members

- **Bela Kardoza** (cap 10, group 4) — `ani/dom/CEL/POT/PRE/VIC`.
- **Bronwen** (cap 10, group 2) — `dom/obt/CEL/POT/PRE`.
- **Armin Brenner** (cap 10, group 4) — `ani/obf/CEL/FOR/POT/PRE`.

## Query

```
jq '.[] | select(.clans[]? == "Brujah antitribu") | .name' card-db/crypt.json
```

## Related

- [[entities/clans/brujah|Brujah]] — parent clan.
- [[entities/sects/sabbat|Sabbat]] — sect.
- [[entities/disciplines/celerity|Celerity]], [[entities/disciplines/potence|Potence]], [[entities/disciplines/presence|Presence]] — shared signature.

## Sources

- src-001 — VTES 5E Rulebook (Sabbat sect rules, p. 40).
- src-002 — krcg vtes.json snapshot 2026-04-18.
