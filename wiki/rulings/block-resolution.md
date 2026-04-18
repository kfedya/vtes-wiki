---
type: ruling
tags: [block, stealth, intercept, reaction, wake, directed, undirected, redirect]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: verified
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

## Cards That Ignore Block Restrictions (Cross-Table Blocks)

The rulebook rule ("only target blocks directed actions, only prey/predator block undirected") has an important exception: specific cards let any vampire block any action, regardless of whose Methuselah controls them. The cards carry the canonical phrase:

> "…ignoring the normal prey, predator or target restrictions for blocking actions."

Known cards with this effect (src-002 snapshot):
- [Eagle's Sight](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Eagle%27s%20Sight) at **[AUS]** superior — Auspex reaction; any vampire with AUS attempts to block.
- [Falcon's Eye](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Falcon%27s%20Eye) at **[SPI]** superior — Spiritus equivalent; Ahrimanes.

Practical effect: on a directed action (e.g., bleed, directed rescue-from-torpor, steal-equipment), **any Methuselah with a ready unlocked AUS/SPI-superior vampire can intervene**, not just the target. This is confirmed by VEKN Rules Director and moderation:

> "Other Methuselahs can also block that (D) action with Eagle's Sight or similar effects." — Pascal Bertrand (moderator)
> "Globally yes." — Ankha (Rules Director)

Source: [vekn.net/forum/rules-questions/45737-rescue-vampire-from-torpor](https://www.vekn.net/forum/rules-questions/45737-rescue-vampire-from-torpor).

A full card list lives at [[mechanics-index/ignore-block-restrictions|ignore-block-restrictions]].

**Not a wake effect** — these cards still require a ready unlocked vampire. To override the lock requirement too, combine with a wake effect (e.g., [On the Qui Vive](https://codex-of-the-damned.org/en/card-search/library/index.html?card=On%20the%20Qui%20Vive), [Forced Awakening](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Forced%20Awakening)).

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

## Card-Level Rulings (krcg)
Edge cases surfaced from krcg-embedded `rulings[]` [src-002]. Each entry preserves the original reference label (RTR/LSJ/ANK/PIB/TOM).

### [Cloak the Gathering](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Cloak%20the%20Gathering)
- **Multiple copies** can be played by **different minions** on the same action — stealth stacks [src-002, ANK 20200515].

### [Daring the Dawn](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Daring%20the%20Dawn)
- If the action is **blocked**, the self-damage is applied **after combat** resolves [src-002, RTR 19980623].
- The damage **is** applied whenever the action **reaches resolution** — even if the action ends before combat (e.g., via [Mirror Walk](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Mirror%20Walk), [Change of Target](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Change%20of%20Target), [Red Herring](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Red%20Herring)) or has no effect (e.g., because the cost cannot be paid) [src-002, ANK 20220331, ANK 20210124, LSJ 20020927, LSJ 20021115, ANK 20221011-2].
- The damage is **not** applied if the action is **cancelled before resolution** (e.g., by [Tangle Atropos' Hand](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Tangle%20Atropos%27%20Hand), [The Kiss of Ra](https://codex-of-the-damned.org/en/card-search/library/index.html?card=The%20Kiss%20of%20Ra)) [src-002, ANK 20220401, ANK 20211015, ANK 20210124].

### [Faceless Night](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Faceless%20Night)
- A minion who was **already attempting to block** when Faceless Night is played **cannot back out** of the attempt [src-002, LSJ 20081202].
- The aspirant blocker is locked **at resolution**. Before the lock, they can still play [Deflection](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Deflection) (and even re-attempt to block if deflected back), and they can play [Guard Dogs](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Guard%20Dogs) — **before the lock, not after** [src-002, ANK 20171017, ANK 20230305].

### [Cats' Guidance](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Cats%27%20Guidance)
- Is played **after all combats** on the action have been handled [src-002, RTR 19980623, LSJ 20040219, ANK 20221130].

### [Eagle's Sight](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Eagle%27s%20Sight) / [Falcon's Eye](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Falcon%27s%20Eye) (cross-table block enablers)
- These cards **only** override the "who may block" restriction. Every **other** requirement to block still applies. In particular, [Blood Bond](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Blood%20Bond), [Day Operation](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Day%20Operation), [Seduction](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Seduction), and a **prior decision not to block** are **not** circumvented [src-002, RTR 19950413, RTR 20020501].
- Apply to **one block attempt only**. If the action later continues as if unblocked (e.g., via [Form of Mist](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Form%20of%20Mist)), a **new copy** is needed [src-002, LSJ 20030227].

### Wake-family ([On the Qui Vive](https://codex-of-the-damned.org/en/card-search/library/index.html?card=On%20the%20Qui%20Vive), [Wake with Evening's Freshness](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Wake%20with%20Evening%27s%20Freshness), [Eyes of Argus](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Eyes%20of%20Argus), [Forced Awakening](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Forced%20Awakening))
Shared rulings across the wake/permanent-wake family:
- Can be played or used **after action resolution** — e.g., to play a reaction like [Fast Reaction](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Fast%20Reaction) after combat [src-002, LSJ 20091123].
- Can be played in the **"as a card is played" window**, **except** during combat or when there is no action [src-002, ANK 20210819].

### Wake with Evening's Freshness (specific)
- Is **replaced before unlocking cards** resolve. Other unlock effects **cannot be ordered before** Wake [src-002, ANK 20200129, LSJ 20091208, RTR 19951017].

### [Forced Awakening](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Forced%20Awakening) (specific)
- If the vampire **fails to block**, the 1-blood cost is paid **only when the action begins to resolve** (success or not). The vampire can play and pay for reactions **after declining to block, before burning the blood** [src-002, LSJ 19990421].
- If the vampire **successfully blocks**, the blood cost is **not paid** — even if the action continues as if unblocked afterward (e.g., Form of Mist) [src-002, LSJ 20070417].
- Forced Awakening **does not consider blocks made before it was played** (relevant when the action has been continued, e.g., via Form of Mist) [src-002, ANK 20230319].

### [Guard Dogs](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Guard%20Dogs)
- The maneuver works **only in the combat from the successful block**, and does **not carry over** to a follow-up combat (e.g., from [Psyche!](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Psyche%21)) [src-002, LSJ 20010813, LSJ 20010819-2].
- The maneuver is **provided again** if a **second block** happens on the same action (e.g., after Form of Mist reopens blocks) [src-002, LSJ 20010814-2].

### [Second Tradition: Domain](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Second%20Tradition:%20Domain)
- The burn-blood cost is **not** reduced by card-cost-reduction effects (e.g., [Adana de Sforza](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Adana%20de%20Sforza)) [src-002, ANK 20210226].
- Cannot be played if the vampire **cannot afford to burn the blood** [src-002, ANK 20210226].
- If unlocking the vampire **removes the action's target** (e.g., [Ambush](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Ambush)), the **block attempt still happens** — and the combat on successful block still happens [src-002, LSJ 20090514].
- Can be used by a vampire **already attempting to block** [src-002, ANK 20181122-2].
- **Does NOT** override the prey/predator/target restrictions — contrast with Eagle's Sight / Falcon's Eye [src-002, ANK 20180623].

## Sources
- src-001 — VTES Fifth Edition Rulebook, pp. 25–27 (Resolve Any Block Attempts, Detailed Course of an Action), p. 46 (Stealth FAQ), pp. 48–52 (card rulings — Cats' Guidance, Cloak the Gathering, Daring the Dawn, Eyes of Argus, Faceless Night, Guard Dogs, Haven Uncovered, On the Qui Vive, Pentex Subversion, Second Tradition: Domain, Wake with Evening's Freshness), p. 44 (Wake glossary entry).
- src-002 — krcg vtes.json snapshot 2026-04-18 (embedded card-level rulings).
