---
type: ruling
tags: [target, redirect, deflection, change-of-target, mirror-walk, block, bleed, stuck]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: draft
---

# Target Redirection

## Summary
Some cards **change the target** of an action mid-resolution. The rules differ sharply between cards that end the current action (Change of Target, Mirror Walk) and cards that merely redirect within the same action (Deflection). In particular: who ends up locked, when the block window reopens, and what happens to the original acting minion [src-001].

## Change of Target (Animalism)
Played by the **blocking** minion during a block attempt.
- The action **ends** before the block resolution — so the blocking minion is **not locked for blocking** [src-001 p. 48].
- If the blocker was already locked and used a wake effect to block, **they remain locked** (wake doesn't unlock; it just grants reaction-capability for that action).
- If the acting vampire was performing a **mandatory** action (e.g., hunting because they had 0 blood), they become **"stuck"** — unlocked but unable to perform any action this turn [src-001 p. 48].

**Practical consequence:** Change of Target is strictly better than a block for the defender in one respect — the blocker doesn't burn a lock — but it terminates the action, so the acting Methuselah doesn't get another swing at the original target.

## Mirror Walk
Played by the **acting** minion to avoid a block.
- Contrary to Change of Target, Mirror Walk **explicitly locks the blocking minion** before ending the action [src-001 p. 50].
- If the card is not replaced, it effectively counts against your hand size: a hand size of 7 → 6 until your discard phase [src-001 p. 50].

**The key contrast with Change of Target:** Mirror Walk does lock the blocker; Change of Target does not.

## Deflection / Telepathic Misdirection (bleed redirect)
Played by the target of a **bleed** to redirect it to another Methuselah.
- You must **first decline to block** before playing Deflection. The acting Methuselah gets one last chance to increase the bleed, whether or not they take it [src-001 p. 46].
- The new target can **block** or **redirect again**.
- If a redirected bleed is redirected **back to you**, the block window **reopens** — you can try to block [src-001 p. 46].
- A **locked** vampire under a wake effect (e.g., [On the Qui Vive](https://codex-of-the-damned.org/en/card-search/library/index.html?card=On%20the%20Qui%20Vive)) can still play Deflection — even at **basic**. Basic Deflection locks the player, but if they're already locked the lock has no further effect [src-001 p. 48].

## Target Change Reopens Blocks (General Rule)
Whenever a card changes the target of an action, the new target gets a fresh block window with the normal rules — regardless of prior decisions by the old target [src-001 p. 26, p. 46]. See [[block-resolution#target-change-reopens-blocks]].

## "Stuck" Minions
A vampire forced off a **mandatory** action (hunt, for example) without completing it is "stuck": unlocked but unable to take another action this turn. This is specific to Change of Target resolution and similar mid-action terminations [src-001 p. 48].

## Creeping Sabotage Loop
[Creeping Sabotage](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Creeping%20Sabotage) is an ally whose text causes recursive interactions with Change of Target:
- **First Creeping Sabotage costs 0 blood** [src-001 p. 48].
- If a minion attempts to burn a Creeping Sabotage and plays **Change of Target**, they **cannot do the same action again** — the action has ended [src-001 p. 48].
- However, **burning a different copy** of Creeping Sabotage is **not** considered the "same action," so a new attempt is permitted against another copy [src-001 p. 48].

This is the rulebook's canonical "what counts as the same action" case for Change of Target.

## Common Mistakes
- Locking the Change-of-Target blocker — they don't lock, because the action ends before block resolution.
- Locking the Mirror Walk acting vampire but not the blocker — Mirror Walk explicitly locks the blocker.
- Playing Deflection before declining to block.
- Forgetting that a redirect-back-to-original-target reopens blocking.
- Assuming a wake-effect vampire loses the ability to play Deflection — they don't; basic Deflection works, even if they're already locked.

## Related Rulings
- [[bleed]] — redirect windows, FAQ.
- [[block-resolution]] — target change reopens blocks; wake mechanics.
- [[hunt]] — mandatory for 0-blood vampires.

## Card-Level Rulings (krcg)
Edge cases surfaced from krcg-embedded `rulings[]` [src-002]. Each entry preserves the original reference label (RTR/LSJ/ANK).

### [Change of Target](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Change%20of%20Target)
- The action **reaches resolution** via Change of Target — therefore it is subject to **NRA (Non-Repeatable Action) rules** [src-002, LSJ 20070709].
- **"Same action" definition** (for NRA and related "can't repeat" checks):
  - Actions **without a card** (provided by the rulebook) are **not the same** as actions provided by **cards (played or in play)** [src-002, LSJ 20060522, LSJ 20060824, LSJ 20080725, LSJ 20090617].
  - Rulebook-provided actions **can be repeated** if they have **different targets**. For "equip from a minion," the targets are the equipments — if **any one** equipment is the same, the action is considered the same [src-002, RTR 19950509, LSJ 20080710, ANK 20200502].
  - Actions provided by **different in-play cards** are **not the same**, even if the cards share a name [src-002, LSJ 20080725].
- **Timing:** played **after** a minion successfully blocks, **before** the blocker is locked and combat begins. **Cannot be used** if the action is ended without a block [src-002, LSJ 19980224, RTR 19991206].
- Effects that trigger **when the action is blocked** (e.g., [Unleash Hell's Fury](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Unleash%20Hell%27s%20Fury), [Truth of Blood](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Truth%20of%20Blood), [Aching Beauty](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Aching%20Beauty)) **still apply** [src-002, RTR 19991206].
- After Change of Target resolves, **no other action modifier or reaction can be played** — the action has ended [src-002, LSJ 20010803-1, RTR 20180719].

### [Mirror Walk](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Mirror%20Walk) [THA]
- The would-be blocker is **locked** even if they benefit from an effect preventing them from locking on a successful block — the lock comes **from Mirror Walk's effect**, not from the block [src-002, ANK 20191204].
- If the action is **blocked**, it **ends unsuccessfully immediately** — no further modifier or reaction can be played (e.g., [Freak Drive](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Freak%20Drive), slave rule, [Sowing Dissension](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Sowing%20Dissension)) [src-002, RTR 20180719, ANK 20200207, ANK 20210627].
- On a blocked action, **all** "successful block" triggered effects (e.g., [Banshee Ironwail](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Banshee%20Ironwail)) **must be applied** (the acting Methuselah orders them). Other effects and modifiers (e.g., [Crypt's Sons](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Crypt%27s%20Sons), Change of Target) can only be used **after** all triggered effects have resolved [src-002, ANK 20220116, ANK 20211207, ANK 20210627].

### Cross-reference
- The leave-torpor "no diablerie opportunity" edge cases for Change of Target and Mirror Walk are surfaced in [[torpor#leave-torpor--blocker-loses-the-diablerie-opportunity]].

## Sources
- src-001 — VTES Fifth Edition Rulebook, p. 26 (target change reopens blocks), p. 46 (Bleed FAQ — Deflection timing, redirect re-block), pp. 48–50 (card rulings — Change of Target, Creeping Sabotage, Deflection, Mirror Walk, On the Qui Vive, Telepathic Misdirection).
- src-002 — krcg vtes.json snapshot 2026-04-18 (embedded card-level rulings).
