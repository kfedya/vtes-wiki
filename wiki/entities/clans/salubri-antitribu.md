---
type: entity
tags: [clan, legacy, antitribu, salubri, sabbat, valeren]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Salubri antitribu

## Overview

Salubri antitribu is the legacy **Sabbat offshoot** of [[entities/clans/salubri|Salubri]] — the **warrior tradition** of Salubri, embracing Valeren where mainstream Salubri carried Obeah [src-002]. This is one of the most distinctive antitribu shifts: the parent-clan's healer tradition is inverted into aggressive aggravated-damage combat. Of 19 Salubri antitribu vampires, `VAL` (13), `AUS` (8), and `FOR` (8) dominate superior disciplines [src-002].

## Parent clan relationship

- Parent: [[entities/clans/salubri|Salubri]] (Independent / near-extinct; AUS/DOM/FOR in V5 with legacy Obeah).
- Antitribu variant: Sabbat-aligned warrior tradition; 19 crypt.
- Discipline signature divergence: **Valeren replaces Obeah/Dominate** — the same discipline "slot" filled by a warrior tradition rather than a healer tradition. AUS/FOR remain shared with the parent.

## In-clan disciplines (antitribu signature)

- [[entities/disciplines/auspex|Auspex]] — `[aus]`
- [[entities/disciplines/fortitude|Fortitude]] — `[for]`
- [[entities/disciplines/valeren|Valeren]] — `[val]` (warrior tradition, antitribu-defining)

## Sect alignment

Primarily **[[entities/sects/sabbat|Sabbat]]** — the defining feature of the antitribu identity.

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires: **19**
- Crypt vampires with `[VAL]` at superior: **13**
- Crypt vampires with `[AUS]` at superior: **8**
- Crypt vampires with `[FOR]` at superior: **8**

## Notable members

- **Qawiyya el-Ghaduba** (cap 9, group 5) — `aus/pre/FOR/POT/VAL`.
- **Nuriel** (cap 8, group 6) — `cel/dom/AUS/FOR/VAL`.
- **Uriel** (cap 8, group 4) — `ani/obe/AUS/FOR/VAL`.

## Query

```
jq '.[] | select(.clans[]? == "Salubri antitribu") | .name' card-db/crypt.json
```

## Related

- [[entities/clans/salubri|Salubri]] — parent clan (healer tradition).
- [[entities/sects/sabbat|Sabbat]] — sect.
- [[entities/disciplines/valeren|Valeren]] — antitribu-defining warrior tradition.
- [[entities/disciplines/obeah|Obeah]] — parent-clan healer tradition (contrast).
- [[entities/disciplines/auspex|Auspex]], [[entities/disciplines/fortitude|Fortitude]] — shared with parent.

## Sources

- src-001 — VTES 5E Rulebook (Sabbat sect rules, p. 40).
- src-002 — krcg vtes.json snapshot 2026-04-18.
