---
type: entity
tags: [clan, legacy, antitribu, toreador, sabbat]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Toreador antitribu

## Overview

Toreador antitribu is the legacy **Sabbat offshoot** of [[entities/clans/toreador|Toreador]] [src-002]. The antitribu branch keeps the parent's AUS/CEL/PRE signature intact. Of 45 Toreador antitribu vampires, `PRE` (29), `AUS` (26), and `CEL` (24) dominate superior disciplines — mirroring mainstream Toreador almost exactly [src-002].

## Parent clan relationship

- Parent: [[entities/clans/toreador|Toreador]] (Camarilla; AUS/CEL/PRE).
- Antitribu variant: Sabbat-aligned since the legacy era; 45 crypt.
- Discipline signature: **identical** to parent.

## In-clan disciplines

- [[entities/disciplines/auspex|Auspex]] — `[aus]`
- [[entities/disciplines/celerity|Celerity]] — `[cel]`
- [[entities/disciplines/presence|Presence]] — `[pre]`

## Sect alignment

Primarily **[[entities/sects/sabbat|Sabbat]]** — the defining feature of the antitribu identity. Toreador antitribu include prominent Sabbat leaders (Melinda Galbraith is the iconic example).

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires: **45**
- Crypt vampires with `[PRE]` at superior: **29**
- Crypt vampires with `[AUS]` at superior: **26**
- Crypt vampires with `[CEL]` at superior: **24**

## Notable members

- **Melinda Galbraith** (cap 10, group 4 ADV) — iconic Sabbat regent; `obt/AUS/CEL/DOM/POT/PRE`.
- **Marthe Dizier** (cap 10, group 3) — `pro/AUS/CEL/OBF/PRE`.
- **Matteus, Flesh Sculptor** (cap 10, group 2) — `AUS/CEL/PRE/VIC`.

## Query

```
jq '.[] | select(.clans[]? == "Toreador antitribu") | .name' card-db/crypt.json
```

## Related

- [[entities/clans/toreador|Toreador]] — parent clan.
- [[entities/sects/sabbat|Sabbat]] — sect.
- [[entities/disciplines/auspex|Auspex]], [[entities/disciplines/celerity|Celerity]], [[entities/disciplines/presence|Presence]] — shared signature.

## Sources

- src-001 — VTES 5E Rulebook (Sabbat sect rules, p. 40).
- src-002 — krcg vtes.json snapshot 2026-04-18.
