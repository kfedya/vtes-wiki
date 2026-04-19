---
type: ruling
tags: [stealth, action-modifier, cloak, swallowed, block, bonding, perfect-paragon]
sources: [src-001, src-002]
last_verified: 2026-04-19
status: draft
---

# Stealth Modifiers

## Summary
Stealth modifiers are action modifier cards that increase the acting minion's stealth during a non-combat action, so that `stealth > blocker's intercept` and the block fails. They follow the **escalation-when-needed** rule (see [[block-resolution#escalation-windows-critical]]) — you play them in response to a block attempt, not preemptively. A few cards behave oddly because their "stealth" component is conditional or isn't counted as an increase [src-001].

## General Rules
- Stealth can be added to an action only **if a block is currently in progress and the blocker has enough intercept** to block at the current stealth value [src-001 p. 26].
- Modifications persist for the duration of the action, then revert.
- A minion cannot play the **same action modifier card more than once** during a single action — but different vampires can each play a copy.
- Playing an action modifier does **not** require the acting vampire to be unlocked (unlike reaction cards) [src-001 p. 48]. A locked acting vampire can still play them.

## Cloak the Gathering
- **Obfuscate** action modifier, +1 stealth.
- A **locked** acting vampire can play it — action modifiers don't require unlocked state [src-001 p. 48].
- Each vampire can play at most one copy per action, but different vampires in the same action can each play their own copy.

## Swallowed by the Night
- **Basic:** action modifier (+1 stealth) [src-001 p. 51].
- **Superior:** combat card (playable only during combat, not as an action modifier).

Mind the type change — the superior version doesn't add stealth to a non-combat action; it's a different card entirely at that level.

## Perfect Paragon (NOT a stealth modifier — listed here for disambiguation)
[Perfect Paragon](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Perfect%20Paragon) is **Presence-only** and is **not a stealth modifier**. Verbatim card text [src-002]:

> [pre] Only usable during the polling step of a political action. This vampire gets +3 votes.
> [PRE] Allies and younger vampires get -1 intercept.

Basic is a vote modifier for political actions. Superior reduces *blocker* intercept for allies/younger vampires (not a +stealth on the acting minion; it taxes specific would-be blockers instead).

The rulebook FAQ note ([src-001 p. 50]: "At superior, Perfect Paragon does not count as increasing stealth. You can play it even if no one attempts to block to 'cycle' it.") is a **disambiguation**: superior Perfect Paragon's -1 intercept effect is intercept-reduction, not stealth-addition, so it is exempt from the escalation-when-needed rule on stealth modifiers — you can play it with no block attempt in sight.

If a page elsewhere calls Perfect Paragon a stealth modifier, fix it. Card text is cited verbatim above.

## Lost in Crowds
- Obfuscate modifier.
- **Into Thin Air** (referenced in the Lost in Crowds text) is **not** included in Fifth Edition [src-001 p. 49]. Ignore any mention of it in older rulings.

See also [[cards-removed-in-5e]].

## Bonding
- **Dominate-only** action modifier. Verbatim card text [src-002]: `Only usable during a bleed action. [dom] +1 bleed (limited). [DOM] +1 stealth and +1 bleed (limited).`
- The superior stealth clause is **bleed-only** — cannot be used to increase stealth on any non-bleed action [src-002, LSJ 19980824, RTR 19941109].
- **You cannot play the superior effect of Bonding if you do not need stealth** (for instance, if you are not currently being blocked) [src-001 p. 47]. Follows the escalation-when-needed rule strictly — no cycling the superior version.

## Action Cards with "+1 Stealth" Printed
The stealth listed on an action card (e.g., hunt at +1) is the **starting stealth** of *that* action. It cannot be transferred to a different action you play [src-001 p. 46]. Only modifier cards (or effects like The Labyrinth) can increase stealth after announcement.

## Common Mistakes
- Preemptively adding stealth before any block is attempted (not allowed — escalation only when needed).
- Playing Swallowed by the Night at superior as if it were an action modifier — it's a combat card at that level.
- Using Perfect Paragon as a stealth modifier — it isn't one. Basic is +3 votes during polling; superior is -1 intercept vs allies/younger. Don't plan to "sneak by" a block with it.
- Playing the same stealth modifier card twice with the same vampire in one action.

## Related Rulings
- [[block-resolution]] — stealth vs intercept, escalation windows.
- [[bleed]] — bleed-specific modifier limits.
- [[cards-removed-in-5e]] — Into Thin Air is not in 5E.

## Card-Level Rulings (krcg)
Edge cases surfaced from krcg-embedded `rulings[]` [src-002].

### [Bonding](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Bonding) — bleed-only stealth clause
- The Dominate stealth clause of Bonding **cannot be used to increase stealth on a non-bleed action**. The +1 stealth is **bleed-only** — not a generic stealth modifier [src-002, LSJ 19980824, RTR 19941109].

### Cross-reference
- Cloak the Gathering's "multiple copies by different minions on the same action" ruling is surfaced in [[block-resolution#cloak-the-gathering]].

## Sources
- src-001 — VTES Fifth Edition Rulebook, p. 26 (Stealth and Intercept), p. 46 (Stealth FAQ), p. 47 (Bonding), pp. 48–51 (card rulings for Cloak the Gathering, Lost in Crowds, Perfect Paragon, Swallowed by the Night).
- src-002 — krcg vtes.json snapshot 2026-04-18 (embedded card-level rulings).
