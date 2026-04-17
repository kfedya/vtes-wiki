---
type: entity
tags: [clan, legacy, antitribu, nosferatu, sabbat]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Nosferatu antitribu

## Overview

Nosferatu antitribu is the legacy **Sabbat offshoot** of [[entities/clans/nosferatu|Nosferatu]] [src-002]. The antitribu branch keeps the parent's ANI/OBF/POT signature intact — unlike Malkavian or Salubri antitribu, Nosferatu antitribu share the full discipline identity of mainstream Nosferatu. Of 44 Nosferatu antitribu vampires, `OBF` (27), `POT` (26), and `ANI` (22) dominate superior disciplines [src-002].

## Parent clan relationship

- Parent: [[entities/clans/nosferatu|Nosferatu]] (Camarilla; ANI/OBF/POT).
- Antitribu variant: Sabbat-aligned since the legacy era; 44 crypt.
- Discipline signature: **identical** to parent.

## In-clan disciplines

- [[entities/disciplines/animalism|Animalism]] — `[ani]`
- [[entities/disciplines/obfuscate|Obfuscate]] — `[obf]`
- [[entities/disciplines/potence|Potence]] — `[pot]`

## Sect alignment

Primarily **[[entities/sects/sabbat|Sabbat]]** — the defining feature of the antitribu identity.

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires: **44**
- Crypt vampires with `[OBF]` at superior: **27**
- Crypt vampires with `[POT]` at superior: **26**
- Crypt vampires with `[ANI]` at superior: **22**

## Notable members

- **Ysador the Foul** (cap 10, group 4) — `obt/ANI/DEM/FOR/OBF/POT`.
- **Servius Marius Pustula** (cap 10, group 4) — `obf/ANI/CHI/DOM/OBT/POT`.
- **Yong-Sun, Harmonist** (cap 10, group 2) — `aus/ANI/OBF/POT/THA`; has an ADV printing.

## Query

```
jq '.[] | select(.clans[]? == "Nosferatu antitribu") | .name' card-db/crypt.json
```

## Related

- [[entities/clans/nosferatu|Nosferatu]] — parent clan.
- [[entities/sects/sabbat|Sabbat]] — sect.
- [[entities/disciplines/animalism|Animalism]], [[entities/disciplines/obfuscate|Obfuscate]], [[entities/disciplines/potence|Potence]] — shared signature.

## Sources

- src-001 — VTES 5E Rulebook (Sabbat sect rules, p. 40).
- src-002 — krcg vtes.json snapshot 2026-04-18.
