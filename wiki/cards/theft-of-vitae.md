---
type: card
tags: [combat, blood-sorcery, strike, steal-blood, ordering, not-damage]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: draft
---

# Theft of Vitae

> Card text pending krcg.org ingest.

— [krcg.org entry](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Theft%20of%20Vitae)

## Why it has a page
Theft of Vitae pulls rulings from multiple combat-timing axes at once: stealing-blood-is-not-damage, strike:combat-ends ordering, mend ordering with stolen blood, and the simultaneous-steal edge case. The interactions are niche and come up in playgroup disputes regularly.

## Rulings

### Range
- Usable at **close or long range** [src-001 p. 51].

### Not damage
- **Stealing blood does not count as damage:** it cannot be prevented by prevent-damage effects like [Hidden Strength](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Hidden%20Strength) [src-001 p. 51].

### Strike: combat ends resolves first
- A strike: combat ends (e.g., from [Swallowed by the Night](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Swallowed%20by%20the%20Night) at superior) resolves **before** Theft of Vitae. If combat ends early via a strike effect, **you do not steal blood** [src-001 p. 51].

### Mend ordering (the classic edge case)
- Stealing blood **resolves before** burning blood to mend damage [src-001 p. 51].
- **Concrete example:** your empty vampire steals 1 blood from the opposing minion who is simultaneously striking back for 1 damage.
  1. Your vampire gains 1 blood from the steal.
  2. Your vampire burns that 1 blood to mend the 1 incoming damage.
  3. Net result: your vampire is **empty but still ready**, not in torpor.

### Mutual steal is simultaneous
- If **two vampires both steal blood from each other** in the same strike pair, the blood is moved **simultaneously** [src-001 p. 51].
- Neither "does their steal first"; both transfers happen at once.
- krcg clarifies the exact bookkeeping: blood amounts are **adjusted by the total of gain and loss**, and **no blood wears off** in the exchange [src-002, ANK 20200123, LSJ 20041027].

### Can target a minion with insufficient blood/life
- Theft of Vitae is a legal strike even if the target has **less blood or life than the amount stolen** — you simply steal what is available [src-002, RTR 20010711].

## Interactions
- **With [[damage-resolution]]:** classed as blood theft, not damage — no prevent, no aggravated, etc.
- **With [[strike-effects]]:** placed after strike: combat ends in the ordering; resolves with regular strikes otherwise.
- **With [[torpor]]:** empty-vampire-steals-then-mends is the canonical "does my vampire survive a torpor-threshold hit" case.
- **With [[press]]:** the steal resolves in the strike-resolution step; press decisions come later.

## Common Mistakes
- Preventing the stolen blood with Hidden Strength — can't; steal is not damage.
- Letting the steal happen *after* combat ends via strike: CE — no; strike: CE resolves first and you lose the steal.
- Mending damage before applying the stolen blood — wrong order; you gain the blood first, then mend.
- Deciding mutual steals "in order" — they're simultaneous.

## Sources
- src-001 — VTES Fifth Edition Rulebook, p. 51 (Theft of Vitae FAQ).
- src-002 — krcg vtes.json snapshot 2026-04-18 (embedded card-level rulings).
