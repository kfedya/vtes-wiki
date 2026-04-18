---
type: entity
tags: [clan, legacy, antitribu, malkavian, sabbat, dementation]
sources: [src-001, src-002, src-021]
last_verified: 2026-04-18
status: verified
---

# Malkavian antitribu

## Overview

Malkavian antitribu is the legacy **Sabbat offshoot** of [[entities/clans/malkavian|Malkavian]] [src-002]. Distinct from mainstream Malkavian (AUS/DOM/OBF in V5), the antitribu branch carries **Dementation** in place of Dominate — legacy madness-magic themed after "confusion of the eye" and Malkavian fractures. Of 43 Malkavian antitribu vampires, `AUS` (26), `DEM` (26), and `OBF` (24) dominate superior disciplines [src-002].

## Parent clan relationship

- Parent: [[entities/clans/malkavian|Malkavian]] (Camarilla; AUS/DOM/OBF in V5).
- Antitribu variant: Sabbat-aligned since the legacy era; 43 crypt.
- Discipline signature divergence: **Dementation replaces Dominate** — a distinctive signature shift marking the antitribu as a separately flavored branch. Mainstream Malkavian can still print DEM historically, but the antitribu are the discipline's home base.

## In-clan disciplines (antitribu signature)

- [[entities/disciplines/auspex|Auspex]] — `[aus]`
- [[entities/disciplines/dementation|Dementation]] — `[dem]` (replaces Dominate)
- [[entities/disciplines/obfuscate|Obfuscate]] — `[obf]`

## Sect alignment

Primarily **[[entities/sects/sabbat|Sabbat]]** — the defining feature of the antitribu identity.

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires: **43**
- Crypt vampires with `[AUS]` at superior: **26**
- Crypt vampires with `[DEM]` at superior: **26**
- Crypt vampires with `[OBF]` at superior: **24**

## Typical deck archetypes

- [[archetypes/dementation-bleed|Dementation Bleed]] — runner-up Sabbat Malkavian antitribu stealth-and-bleed; Kindred Spirits × 15 payload + Confusion/Eyes of Chaos bleed amp; Telepathic Misdirection × 10 bounce; Coma × 4 combat deterrent [src-021].

## Notable members

- **Louhi** (cap 10, group 4) — `pro/ANI/AUS/DEM/OBF/THA`.
- **Gravitnir** (cap 10, group 4) — `AUS/CEL/DEM/OBF/VIC`.
- **Hannibal** (cap 10, group 2) — `cel/dom/AUS/DEM/OBF`; has an ADV printing.

## Query

```
jq '.[] | select(.clans[]? == "Malkavian antitribu") | .name' card-db/crypt.json
```

## Related

- [[entities/clans/malkavian|Malkavian]] — parent clan.
- [[entities/sects/sabbat|Sabbat]] — sect.
- [[entities/disciplines/dementation|Dementation]] — antitribu signature (vs parent's Dominate).
- [[entities/disciplines/auspex|Auspex]], [[entities/disciplines/obfuscate|Obfuscate]] — shared with parent.

## Sources

- src-001 — VTES 5E Rulebook (Sabbat sect rules, p. 40).
- src-002 — krcg vtes.json snapshot 2026-04-18.
- src-021 — Codex of the Damned — Dementation Bleed archetype (runner-up Sabbat stealth-and-bleed with DEM Kindred Spirits engine).
