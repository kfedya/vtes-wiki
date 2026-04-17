---
type: entity
tags: [clan, legacy, antitribu, gangrel, sabbat]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Gangrel antitribu

## Overview

Gangrel antitribu is the legacy **Sabbat offshoot** of [[entities/clans/gangrel|Gangrel]] [src-002]. The antitribu variant diverges slightly from its parent: where mainstream Gangrel runs ANI/FOR/PRO, the Sabbat offshoot leans PRO + CEL + OBF — trading Fortitude/Animalism dominance for Celerity and Obfuscate. Of 58 Gangrel antitribu vampires, `PRO` (34), `CEL` (18), and `OBF` (18) dominate superior disciplines [src-002].

## Parent clan relationship

- Parent: [[entities/clans/gangrel|Gangrel]] (Independent/Anarch/Camarilla; ANI/FOR/PRO signature).
- Antitribu variant: Sabbat-aligned since the legacy era; 58 crypt.
- Discipline signature divergence: keeps Protean as the anchor but trades ANI/FOR for CEL/OBF — a measurable shift vs the parent.

## In-clan disciplines (antitribu signature)

- [[entities/disciplines/protean|Protean]] — `[pro]`
- [[entities/disciplines/celerity|Celerity]] — `[cel]`
- [[entities/disciplines/obfuscate|Obfuscate]] — `[obf]`

(Animalism and Fortitude remain common on individual printings but are not the top-3 superior signature.)

## Sect alignment

Primarily **[[entities/sects/sabbat|Sabbat]]** — the defining feature of the antitribu identity.

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires: **58**
- Crypt vampires with `[PRO]` at superior: **34**
- Crypt vampires with `[CEL]` at superior: **18**
- Crypt vampires with `[OBF]` at superior: **18**
- Crypt vampires with `[ANI]` at superior: 15
- Crypt vampires with `[FOR]` at superior: 11

## Notable members

- **Enkidu, The Noah** (cap 11, group 4) — iconic Sabbat Gangrel antitribu; `for/ANI/CEL/OBF/POT/PRO`.
- **Mimir** (cap 10, group 5) — `dom/ANI/FOR/PRO/THA`.
- **Hukros** (cap 10, group 4) — `abo/cel/ANI/OBF/PRO/VIC`.

## Query

```
jq '.[] | select(.clans[]? == "Gangrel antitribu") | .name' card-db/crypt.json
```

## Related

- [[entities/clans/gangrel|Gangrel]] — parent clan.
- [[entities/sects/sabbat|Sabbat]] — sect.
- [[entities/disciplines/protean|Protean]] — shared anchor discipline.
- [[entities/disciplines/celerity|Celerity]], [[entities/disciplines/obfuscate|Obfuscate]] — antitribu-shifted emphasis.

## Sources

- src-001 — VTES 5E Rulebook (Sabbat sect rules, p. 40).
- src-002 — krcg vtes.json snapshot 2026-04-18.
