---
type: ruling
tags: [action, torpor, rescue, split-cost]
sources: [src-001]
last_verified: 2026-04-17
status: draft
---

# Rescue a Vampire from Torpor

## Summary
Action by a ready vampire to move a vampire **out of torpor** into the ready region. The default cost is 2 blood, which can be paid by either vampire or **split** between them — an explicit exception to the "pay from your own resources" rule [src-001].

## Action Profile [src-001]
- **Who can rescue:** any ready vampire.
- **Default cost:** 2 blood, paid by the acting vampire, or the rescued vampire, or split.
- **Default target:** a vampire in torpor.
- **Directed-ness:**
  - **Undirected** if the two vampires share the same controller.
  - **Directed** if controllers differ.
- **Default stealth:**
  - **+1** if the two vampires share the same controller.
  - **0** if controllers differ.

## Effect
- On success: the vampire in torpor moves to the ready region. The rescued vampire does **not lock or unlock** as a result of the rescue — they keep whatever state they were in. They are **no longer wounded** after being rescued.
- On block: the acting vampire and blocking minion enter combat **as normal** (contrast with [[leave-torpor]], where blocked actions do not produce combat).

## Split Cost
The 2-blood cost is unusual: it can come from the acting vampire, the vampire in torpor, or both in combination. Announce the split at resolution time, per normal cost-payment-on-success rules [src-001].

## Common Mistakes
- Treating a blocked rescue like a blocked leave-torpor — rescue **produces combat**, leave-torpor does not.
- Rescuing and expecting the target to be ready-and-unlocked — they retain whatever lock state they had in torpor.
- Forgetting that rescuing a **foreign** vampire (other controller) is directed at 0 stealth — it's much harder to sneak past intercept.

## Sources
- src-001 — VTES Fifth Edition Rulebook, p. 23 (Rescue a Vampire from Torpor).
