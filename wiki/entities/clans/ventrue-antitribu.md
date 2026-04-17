---
type: entity
tags: [clan, legacy, antitribu, ventrue, sabbat]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Ventrue antitribu

## Overview

Ventrue antitribu is the legacy **Sabbat offshoot** of [[entities/clans/ventrue|Ventrue]] [src-002]. Unlike mainstream Ventrue (DOM/FOR/PRE), the antitribu branch carries **Auspex in place of Presence** — trading vote boost for intercept. Of 43 Ventrue antitribu vampires, `AUS` (24), `DOM` (23), and `FOR` (21) dominate superior disciplines [src-002].

## Parent clan relationship

- Parent: [[entities/clans/ventrue|Ventrue]] (Camarilla; DOM/FOR/PRE).
- Antitribu variant: Sabbat-aligned since the legacy era; 43 crypt.
- Discipline signature divergence: **Auspex replaces Presence** — a notable shift, moving the clan's identity from Ventrue-vote-grinder toward Ventrue-antitribu-wall.

## In-clan disciplines (antitribu signature)

- [[entities/disciplines/auspex|Auspex]] — `[aus]` (replaces Presence)
- [[entities/disciplines/dominate|Dominate]] — `[dom]`
- [[entities/disciplines/fortitude|Fortitude]] — `[for]`

## Sect alignment

Primarily **[[entities/sects/sabbat|Sabbat]]** — the defining feature of the antitribu identity.

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires: **43**
- Crypt vampires with `[AUS]` at superior: **24**
- Crypt vampires with `[DOM]` at superior: **23**
- Crypt vampires with `[FOR]` at superior: **21**

## Notable members

- **Elimelech the Twice-Damned** (cap 11, group 5) — `pro/AUS/DEM/DOM/FOR/OBF`.
- **Laszlo Mirac** (cap 10, group 4) — `cel/obf/vic/AUS/DOM/FOR`.
- **Bruce de Guy** (cap 10, group 4) — `AUS/DOM/FOR/OBT`.

## Query

```
jq '.[] | select(.clans[]? == "Ventrue antitribu") | .name' card-db/crypt.json
```

## Related

- [[entities/clans/ventrue|Ventrue]] — parent clan.
- [[entities/sects/sabbat|Sabbat]] — sect.
- [[entities/disciplines/auspex|Auspex]] — antitribu signature (vs parent's Presence).
- [[entities/disciplines/dominate|Dominate]], [[entities/disciplines/fortitude|Fortitude]] — shared with parent.

## Sources

- src-001 — VTES 5E Rulebook (Sabbat sect rules, p. 40).
- src-002 — krcg vtes.json snapshot 2026-04-18.
