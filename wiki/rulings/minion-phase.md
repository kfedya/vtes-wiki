---
type: ruling
tags: [phase, minion, actions, sequencing, mandatory, stuck]
sources: [src-001]
last_verified: 2026-04-17
status: draft
---

# Minion Phase

## Summary
The longest and most consequential phase. The acting Methuselah's **ready unlocked** minions may perform actions one at a time. Taking an action **locks** the minion. Each action must resolve (successful or blocked) before another action is begun [src-001].

## Who Can Act
- Only **ready unlocked** minions (see [[game-overview#Play Area]]).
- If a minion unlocks mid-phase (e.g., Freak Drive), they **can** act again — subject to per-card/per-minion action limits (see below).

## Mandatory Actions
Some actions are **mandatory** and must be performed before any non-mandatory actions [src-001].

- A **ready vampire with no blood must hunt** as a mandatory action.
- A minion required to take a mandatory action cannot perform any other action while the mandatory one is pending.
- Multiple minions with mandatory actions: you choose the order among them.

### "Stuck" Minions
If a minion has two or more different mandatory actions, or a mandatory action they cannot take (e.g., hunt is disallowed), they are **stuck** and cannot act at all this turn. This does not prevent your *other* minions from acting [src-001].

A minion can also become stuck mid-action: e.g., a vampire forced to hunt because they had no blood who is then hit by [Change of Target](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Change%20of%20Target) — the action ends, the vampire remains unlocked, but cannot act [src-001 p. 48].

## Per-Card / Per-Minion Limits
Even if a minion unlocks and re-acts, these limits persist for the turn [src-001]:

- **Same action card:** a minion cannot play the same named action card from hand or in play more than once per turn.
- **Same copy of a card:** a minion cannot perform an action via the same copy of a card in play (including their own crypt card text) more than once per turn.
- **Bleed:** a minion cannot perform more than one bleed action per turn. See [[bleed]].
- **Political action:** a vampire cannot perform more than one political action per turn. See [[politics]].
- **Same action modifier / reaction card:** a minion cannot play the same action modifier or reaction card more than once *per action*. Different vampires can each play their own copy.

## Default (Non-Card) Actions
Any ready vampire may, without playing an action card, attempt one of [src-001]:
- **Bleed** the prey — see [[bleed]].
- **Hunt** — see [[hunt]].

Any ready ally may attempt only:
- **Bleed**.

Other default actions (see list below) exist but are situational.

## Complete Action Catalog
Listed in the rulebook at pp. 20–24. Each has its own ruling page:

- [[bleed]] — reduce target Methuselah's pool; default 0 stealth; directed at prey.
- [[hunt]] — vampire-only; +1 stealth; undirected; gain blood.
- [[equip]] — from hand or from another of your minions; +1 stealth when from hand.
- [[employ-retainer]] — +1 stealth; undirected.
- [[recruit-ally]] — +1 stealth; undirected.
- [[political-action]] — vampire-only; +1 stealth; undirected; calls a referendum.
- [[leave-torpor]] — torpor-vampire only; +1 stealth; undirected.
- [[rescue-from-torpor]] — stealth and directed-ness depend on whether the torpor vampire is yours.
- [[diablerise-action]] — ready vampire vs vampire in torpor; stealth/directed-ness same rule as rescue.
- [[become-anarch]] — untitled non-Anarch vampire only; +1 stealth; undirected.
- **Action card** — play any action card matching the minion's requirements.

## Summary of the Course of an Action
Adapted from the rulebook summary at p. 24 [src-001]:

1. **Announce** the action. Play the card (if any) face-up, temporarily out of play. Lock the acting minion. Cards marked "as the action is announced" are played before regular action modifiers or reaction cards.
2. **Block window.** Target Methuselah(s) may attempt to block with ready unlocked minions. See [[block-resolution]]. Failed attempts can be retried until the defender declines further attempts.
3. **Resolution.** If unblocked and no more effects are being played, the action succeeds: cost is paid, effect applies. If blocked, the action card (if any) is burned, the blocker is locked, and combat begins (see future `[[combat]]` — stage 3).

Action modifiers and reaction cards can be played throughout, with the acting Methuselah having first **impulse** (see [[game-overview#Sequencing]]). Effects last for the duration of the current action; the same minion cannot play the same modifier/reaction more than once per action.

## Action Cost Timing
- **Cost of the action itself:** paid only on success. Not paid if blocked [src-001 p. 27].
- **Cost of action modifiers and reaction cards:** paid **when the card is played**, regardless of whether the action ultimately succeeds.

## Common Mistakes
- Letting a vampire with 0 blood skip hunting to do something else — they can't, hunt is mandatory.
- Playing a second copy of the same action card with the same vampire after a Freak Drive — not allowed; same-card limit is per-minion-per-turn, not per-action.
- Assuming a blocker auto-locks when declaring a block — they only lock if the block **succeeds** (see [[block-resolution]] and Faceless Night FAQ on p. 49).

## Sources
- src-001 — VTES Fifth Edition Rulebook, pp. 18–20 (Minion Phase, Types of Actions), p. 24 (Summary of an Action), p. 27 (cost timing), pp. 48–49 (FAQ — Change of Target, Faceless Night).
