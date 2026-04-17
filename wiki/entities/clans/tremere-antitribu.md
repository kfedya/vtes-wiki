---
type: entity
tags: [clan, legacy, antitribu, tremere, sabbat]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
---

# Tremere antitribu

## Overview

Tremere antitribu is the legacy **Sabbat offshoot** of [[entities/clans/tremere|Tremere]] [src-002]. The antitribu branch keeps the parent's Blood-Sorcery-centric identity (AUS/DOM/THA). Of 43 Tremere antitribu vampires, `THA` (28), `AUS` (24), and `DOM` (22) dominate superior disciplines — identical to mainstream Tremere's signature [src-002].

## Parent clan relationship

- Parent: [[entities/clans/tremere|Tremere]] (Camarilla; AUS/Blood Sorcery/DOM).
- Antitribu variant: Sabbat-aligned since the legacy era; 43 crypt.
- Discipline signature: **identical** to parent. Goratrix (legacy Tremere antitribu founder) is the canonical lore anchor.

## In-clan disciplines

- [[entities/disciplines/auspex|Auspex]] — `[aus]`
- [[entities/disciplines/blood-sorcery|Blood Sorcery]] — `[tha]` (Thaumaturgy in legacy)
- [[entities/disciplines/dominate|Dominate]] — `[dom]`

## Sect alignment

Primarily **[[entities/sects/sabbat|Sabbat]]** — the defining feature of the antitribu identity.

## Card counts (src-002 snapshot 2026-04-18)

- Crypt vampires: **43**
- Crypt vampires with `[THA]` at superior: **28**
- Crypt vampires with `[AUS]` at superior: **24**
- Crypt vampires with `[DOM]` at superior: **22**

## Notable members

- **Goratrix** (cap 10, group 2) — lore founder of the Tremere antitribu; `vic/ANI/AUS/DOM/THA`.
- **Lucubratio** (cap 10, group 4) — `AUS/DOM/POT/PRE/THA`.
- **Lernean** (cap 10, group 4) — `for/pro/AUS/CEL/DOM/THA`.

## Query

```
jq '.[] | select(.clans[]? == "Tremere antitribu") | .name' card-db/crypt.json
```

## Related

- [[entities/clans/tremere|Tremere]] — parent clan.
- [[entities/sects/sabbat|Sabbat]] — sect.
- [[entities/disciplines/auspex|Auspex]], [[entities/disciplines/blood-sorcery|Blood Sorcery]], [[entities/disciplines/dominate|Dominate]] — shared signature.

## Sources

- src-001 — VTES 5E Rulebook (Sabbat sect rules, p. 40).
- src-002 — krcg vtes.json snapshot 2026-04-18.
