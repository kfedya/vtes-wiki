---
type: ruling
tags: [action, torpor, rescue, split-cost]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
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

## Cross-Table Blocks (Directed Rescue)

By base rules, a directed rescue is blockable only by the target Methuselah (the controller of the vampire in torpor). Two cards explicitly break that restriction and let **any** Methuselah intervene:

- [Eagle's Sight](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Eagle%27s%20Sight) at [AUS]
- [Falcon's Eye](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Falcon%27s%20Eye) at [SPI]

Both play as reactions and ignore "the normal prey, predator or target restrictions for blocking actions". Confirmed by VEKN Rules Director (Ankha) and moderator Pascal Bertrand — see [vekn.net/forum/rules-questions/45737-rescue-vampire-from-torpor](https://www.vekn.net/forum/rules-questions/45737-rescue-vampire-from-torpor).

Consequence: rescuing "across the table" (non-adjacent Methuselah's vampire) is **not** insulated from your neighbours. Any opponent with a ready AUS/SPI vampire can still intervene. See [[block-resolution#cards-that-ignore-block-restrictions-cross-table-blocks]] for the full treatment and [[mechanics-index/ignore-block-restrictions|mechanics-index/ignore-block-restrictions]] for the card index.

The target Methuselah also has the option of [Hide the Heart](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Hide%20the%20Heart) at [val] to fail the action outright (unless the acting minion burns 1 blood).

## Common Mistakes
- Treating a blocked rescue like a blocked leave-torpor — rescue **produces combat**, leave-torpor does not.
- Rescuing and expecting the target to be ready-and-unlocked — they retain whatever lock state they had in torpor.
- Forgetting that rescuing a **foreign** vampire (other controller) is directed at 0 stealth — it's much harder to sneak past intercept.
- Assuming that only the target can block a directed rescue — Eagle's Sight / Falcon's Eye open it up to any Methuselah.

## Sources
- src-001 — VTES Fifth Edition Rulebook, p. 23 (Rescue a Vampire from Torpor).
- src-002 — krcg vtes.json snapshot 2026-04-18 (Eagle's Sight, Falcon's Eye, Hide the Heart card text).
