---
type: ruling
tags: [block, stealth, intercept, reaction, wake, directed, undirected, redirect]
sources: [src-001]
last_verified: 2026-04-18
status: draft
---

# Block Resolution

## Summary
After an action is announced, target Methuselah(s) may try to block it with ready unlocked minions. A block succeeds when the blocking minion's **intercept** ≥ the acting minion's **stealth**. Successful block locks the blocker and triggers combat (unless the action is leave-torpor — see [[leave-torpor]]). This page documents the window, attempt mechanics, and stealth/intercept modifiers [src-001].

## Who May Attempt to Block

### Directed Actions
Actions targeting one or more Methuselahs (or things they control) are **directed**. Card text is marked with `{}` as a reminder [src-001].

- Only the **targeted** Methuselah(s) may attempt to block with their ready unlocked minions.
- Multiple targets: block attempts proceed in **clockwise** order.

### Undirected Actions
Actions not directed at another Methuselah (or targeting the acting Methuselah's own things) are **undirected** [src-001].

- The acting Methuselah's **prey** gets first opportunity to block.
- Then the **predator**.

Political actions are **always undirected** [src-001 p. 26].

## Retrying and Declining
- A minion can attempt to block as many times as they wish **as long as another minion is not already blocking**.
- If one attempt fails, another can be made, as often as the blocking Methuselah wishes.
- Once a Methuselah **declines** further attempts, the decision is final **for this action** — unless the target changes.

## Target Change Reopens Blocks
If the target of the action changes (e.g., a bleed is redirected by Deflection), **the block window reopens** and the normal rules restart with the new target [src-001 p. 26, p. 46].

## Stealth and Intercept

### Default Values
- Vampires have **0 stealth** and **0 intercept** by default [src-001 p. 26].
- Some actions have inherent stealth (e.g., hunt: +1, bleed: 0).

### Comparison
A block succeeds when `blocker's intercept ≥ acting minion's stealth`.

### Escalation Windows (Critical)
Stealth and intercept can only be added **when needed** [src-001 p. 26]:
- Acting minion can add stealth **only if** a block is currently in progress and the blocker has enough intercept.
- Blocking minion can add intercept **only if** the acting minion's stealth currently exceeds the blocker's intercept.

Modifications persist **for the duration of the action**, then return to normal when the action resolves.

### Stealth Listed on Action Cards Is Not Transferable
> Can I use the "+1 stealth" listed on an action card to increase the stealth of another action I play?
> No. The stealth listed on an action card indicates the starting stealth of that action. Only action modifiers and similar effects (such as The Labyrinth) can be used to increase the stealth after the action has been announced. [src-001 p. 46]

## Detailed Course of an Action (Advanced)
The rulebook formalises three states [src-001 p. 27]:

### A. No Current Block Attempt
1. Normal sequencing applies.
2. Anyone who can play effects during an action may do so; any eligible Methuselah can declare a block attempt → switch to state **B**.
3. If a Methuselah **passes**, they cannot declare a block attempt again for this action **unless the target changes**.
4. Once every Methuselah has passed, switch to state **C**.

### B. Ongoing Block Attempt
1. Normal sequencing applies.
2. The **target of the action cannot be changed** while a block is in progress.
3. The Methuselah with the ongoing block can use effects that force the currently blocking minion to attempt to block (no other minion can try while this attempt is being resolved).
4. When all Methuselahs pass, resolve the attempt:
   - **Successful:** the action is blocked; blocker locks and combat begins (unless prohibited, e.g., leave-torpor).
   - **Unsuccessful:** switch back to state **A**.

### C. Blocks Declined by All
1. Normal sequencing applies.
2. If the target changes, switch back to state **A**.
3. When all Methuselahs pass, the action is **successful** and resolves: cost paid, effect applied.

## Faceless Night / Retroactive Lock
A minion who attempts to block and **fails** is **not locked**. They can still play reaction cards (Deflection etc.). They only lock if the block eventually **succeeds** or as part of the action's final resolution per [Faceless Night](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Faceless%20Night) [src-001 p. 49].

Faceless Night does **not** retroactively lock minions who previously attempted to block.

## "Replace First, Then Decide" — Optional-Block Cards
Some reaction/wake-like cards present their effect **before** the block decision, and the rule is consistent: **replace the card first**, then decide [src-001 p. 50]:
- [On the Qui Vive](https://codex-of-the-damned.org/en/card-search/library/index.html?card=On%20the%20Qui%20Vive) — if you wake, nothing forces you to block. Replace before deciding.
- [Guard Dogs](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Guard%20Dogs) — nothing forces you to block with the vampire playing Guard Dogs. Replace first [src-001 p. 49].

## Action Directed Against the Playing Methuselah (Master Cards)
A master card is **controlled by the Methuselah who played it**, not by the bearer's controller. Consequence: an action to burn a master card (e.g., [Haven Uncovered](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Haven%20Uncovered), [[wiki/cards/pentex-subversion|Pentex™ Subversion]]) is **directed against the Methuselah who played the master** — blocks come from *their* minions, not the bearer's controller's minions [src-001 pp. 49–50].

## Wake Effects
A **wake** effect lets a locked vampire act as though unlocked **for the duration of the current action** — they can attempt to block and/or play reaction cards [src-001 glossary p. 44].

- Wake effects can be played in the "as a card is played" window, specifically to enable playing other reaction cards that must be played in that window.
- A reaction card that **unlocks** (but does not **wake**) a vampire is not a wake effect and cannot be played in the "as a card is played" window.
- A minion who wakes is **not** unlocked. They are simply treated as unlocked for reaction/block purposes.

## Wake Edge Cases from FAQ [src-001 pp. 48–51]
- **Cats' Guidance:** if your blocking minion ends up in torpor after combat, you cannot play Cats' Guidance afterward — only ready minions can play reaction cards.
- **Eyes of Argus:** cannot play at superior to wake, then at basic for intercept with the same vampire — same reaction card cannot be played twice during a single action.
- **Second Tradition: Domain:** not a wake effect. A locked vampire can play it but must be able to actually block; cannot be used purely to "get a reaction in" if the vampire cannot block the action (e.g., action not directed at you, or unblockable via Daring the Dawn / Toreador Grand Ball).
- **Cloak the Gathering:** an action modifier — a **locked** acting vampire *can* play it at superior, because action modifiers don't require unlocked state like reaction cards do.

## Common Cards Involved
- [On the Qui Vive](https://codex-of-the-damned.org/en/card-search/library/index.html?card=On%20the%20Qui%20Vive) — wake; nothing forces you to block after waking, replace card first [src-001 p. 50].
- [Wake with Evening's Freshness](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Wake%20with%20Evening%27s%20Freshness) — see On the Qui Vive [src-001 p. 52].
- [Eyes of Argus](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Eyes%20of%20Argus) — intercept / wake-at-superior; see above caveat [src-001 p. 49].
- [Cats' Guidance](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Cats%27%20Guidance) — intercept; caveat about post-combat torpor above [src-001 p. 48].
- [Faceless Night](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Faceless%20Night) — lock-on-declare mechanic [src-001 p. 49].
- [Daring the Dawn](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Daring%20the%20Dawn) — makes action unblockable; playable before or during block attempts [src-001 p. 48].
- [Second Tradition: Domain](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Second%20Tradition:%20Domain) — locked-vampire forced-block; caveats above [src-001 p. 50].
- [Guard Dogs](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Guard%20Dogs) — retainer; "replace first, then decide" [src-001 p. 49].
- [Haven Uncovered](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Haven%20Uncovered) — master; burn-action directed against playing Methuselah [src-001 p. 49].
- [[wiki/cards/pentex-subversion|Pentex™ Subversion]] — master; bearer can still play reactions even though they cannot block [src-001 p. 50].

## Common Mistakes
- Locking a blocker the instant they declare a block, before resolution — they only lock if the block succeeds.
- Trying to add stealth/intercept pre-emptively before any block attempt exists — escalation is only allowed "when needed".
- Playing a Deflection **without** declining to block first — you must decline before redirecting (see [[bleed#FAQ]]).
- Using an action card's printed stealth value to "pool" stealth into another action — you can't; printed stealth is the starting value for that action only.
- Assuming a wake effect unlocks the vampire — it doesn't; they just act as though unlocked for this action.

## Sources
- src-001 — VTES Fifth Edition Rulebook, pp. 25–27 (Resolve Any Block Attempts, Detailed Course of an Action), p. 46 (Stealth FAQ), pp. 48–52 (card rulings — Cats' Guidance, Cloak the Gathering, Daring the Dawn, Eyes of Argus, Faceless Night, Guard Dogs, Haven Uncovered, On the Qui Vive, Pentex Subversion, Second Tradition: Domain, Wake with Evening's Freshness), p. 44 (Wake glossary entry).
