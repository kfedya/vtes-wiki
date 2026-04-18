---
type: ruling
tags: [torpor, wounded, vulnerable, diablerie, leave-torpor, rescue]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: draft
---

# Torpor

## Summary
When a vampire cannot mend their wounds, they enter **torpor** — a deep sleep that leaves them vulnerable. A vampire in torpor can take almost no action, cannot block, cannot play reactions, and can be diablerised. They remain controlled by their Methuselah and unlock as normal each turn, but remain in the torpor region until rescued or until they leave on their own [src-001 p. 34].

## Where Torpor Vampires Sit
Vampires in torpor are placed in an area to one side of the uncontrolled region [src-001 p. 34]. Any retainers, equipment, and other cards on the vampire **stay with** the vampire when they go into torpor.

## What a Vampire in Torpor Can Do
- Perform **no action except the "leave torpor" action** — see [[leave-torpor]].
- **Cannot block.**
- **Cannot play reaction cards.**
- **Can** play action modifiers during their actions (i.e., during the leave-torpor attempt).
- **Cannot cast any votes or ballots** — they must abstain [src-001 p. 34].

## Control & Ready State
- Still considered **controlled** by their Methuselah.
- **Not ready.**
- **They still unlock at the start of the unlock phase** [src-001 p. 34].

## Getting Out of Torpor
- **[[leave-torpor]]** — self-initiated; 2 blood, +1 stealth, undirected. If blocked by a vampire, the blocker gets a **diablerie opportunity** — no combat either way.
- **[[rescue-from-torpor]]** — initiated by another minion; stealth/directness depends on whether the rescuer and the torpor vampire share a controller.

## Vulnerability: Diablerie
A vampire in torpor is vulnerable to **diablerie** — another ready vampire may drink their blood to send them to final death. See [[diablerie]] for full resolution [src-001 p. 34].

## Targeting Rule
Vampires in the **torpor region** are eligible targets by default for cards and effects that target vampires in play. Vampires in the uncontrolled region and contested cards are **not** eligible targets by default [src-001 p. 44 — Target glossary].

## "Wounded" Terminology
A **wounded** vampire is one that has received damage they have not mended, or one in torpor or on their way to torpor [src-001 p. 44]. Aggravated damage interacts with wounded state — see [[damage-resolution#aggravated-damage]].

## Goes Directly to Ash Heap (Not Torpor First)
- If aggravated damage **burns** a wounded vampire, they go straight to the ash heap — they do **not** pass through torpor first [src-001 p. 32].
- Consequence: [Fame](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Fame) does **not** cost 3 pool when a Fame-bearer is aggravated-burned outright, because they did not go to torpor [src-001 p. 49].

## Related Edge Cases
- **Cats' Guidance** — a blocking minion sent to torpor during combat cannot play Cats' Guidance afterward, since only ready minions can play reaction cards [src-001 p. 48].
- **Freak Drive** — can still be played on a vampire now in torpor, provided they have blood to pay the cost [src-001 p. 49].

## Common Cards Involved
- [Fame](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Fame) — 3-pool penalty when bearer goes to torpor [src-001 p. 49].
- [Cats' Guidance](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Cats%27%20Guidance) — unplayable once blocker is in torpor [src-001 p. 48].
- [Freak Drive](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Freak%20Drive) — playable on torpor vampire with blood [src-001 p. 49].

## Common Mistakes
- Letting a torpor vampire block, react, or vote.
- Skipping unlock for torpor vampires in the unlock phase — they still unlock.
- Treating torpor as an intermediate stop for aggravated-burned wounded vampires.
- Forgetting that equipment and retainers stay on a torpor vampire.

## Card-Level Rulings (krcg)
Edge cases surfaced from krcg-embedded `rulings[]` [src-002]. Each entry preserves the original reference label (RTR/LSJ/ANK/PIB/RBK).

### Shared rule — "fizzle" on rescue-from-torpor when target left torpor
If a rescue/heal-from-torpor action is **unblocked at resolution** but the **target is no longer in torpor**, the action **"fizzles"**: cost (if any) is paid, the action is considered **successful**, but **has no effect** [src-002, ANK 20210124, LSJ 20070411, LSJ 20090514].

Applies to: [Cloak of Blood](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Cloak%20of%20Blood), [Dismemberment of Osiris](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Dismemberment%20of%20Osiris), [Fire on the Mountain](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Fire%20on%20the%20Mountain), [Graverobbing](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Graverobbing), [Healing Touch](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Healing%20Touch), [Lord of Serenity](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Lord%20of%20Serenity), [Raw Recruit](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Raw%20Recruit), [Renewed Vigor](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Renewed%20Vigor), [Resume the Coil](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Resume%20the%20Coil), [Root of Vitality](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Root%20of%20Vitality), [Sacrificial Lamb](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Sacrificial%20Lamb), [Siphon](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Siphon), [Stealing Years](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Stealing%20Years), [Warding the Beast](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Warding%20the%20Beast).

### Shared rule — "fizzle" when the acting vampire leaves torpor before resolution
If the acting vampire **leaves torpor before the action resolves** (e.g., via [Warsaw Station](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Warsaw%20Station)), the action **"fizzles"** immediately — cost paid, considered successful, no effect [src-002, ANK 20220218].

Applies to leave-torpor action cards: [Movement of the Slow Body](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Movement%20of%20the%20Slow%20Body), [Rapid Healing](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Rapid%20Healing), [Recure of the Homeland](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Recure%20of%20the%20Homeland), [Regeneration](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Regeneration), [Resume the Coil](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Resume%20the%20Coil).

### Non-default leave-torpor actions — no blood paid
Rapid Healing, Recure of the Homeland, and Resume the Coil are **"leave torpor" actions** but **not the default action** — **no blood is paid** to leave torpor when using them [src-002, ANK 20181017, LSJ 19980126].

### Leave-torpor — blocker loses the diablerie opportunity
Normally, a blocker of a leave-torpor action gets a diablerie opportunity (no combat). These cards break that:
- [Change of Target](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Change%20of%20Target) while leaving torpor — blocker **does not** get diablerie [src-002, LSJ 20050105-2].
- [Mirror Walk](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Mirror%20Walk) [THA] while leaving torpor — blocker **does not** get diablerie [src-002, PIB 20121216].
- [The Kiss of Ra](https://codex-of-the-damned.org/en/card-search/library/index.html?card=The%20Kiss%20of%20Ra) when used by an acting vampire **in torpor** — the action is ended without a successful block, so **no diablerie** opportunity [src-002, RBK leave-torpor, LSJ 19970325].
- [Blood Brother Ambush](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Blood%20Brother%20Ambush) — a Brujah Antitribu can use it while taking an action from torpor; the blocker **loses the diablerie opportunity** [src-002, RTR 20010710].

### "Can be played from torpor"
The following reactions are played **after all combats** and **may be played from torpor** [src-002, LSJ 20030103, ANK 20181219, ANK 20180906]:
- [Dusk Work](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Dusk%20Work)
- [Momentary Delay](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Momentary%20Delay)
- [Seraph's Second](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Seraph%27s%20Second)
- [Zephyr](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Zephyr)

### Torpor restrictions
- [Make an Example](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Make%20an%20Example) — **cannot** be used by a vampire in torpor [src-002, PIB 20150720, RTR 19970306].
- [Hidden Lurker](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Hidden%20Lurker) — cannot be used to enter combat with a vampire **on his way to torpor** [src-002, LSJ 20100604-1].
- [Gather](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Gather) — only moves from **uncontrolled** region to ready; **cannot rescue** from torpor [src-002, LSJ 20030520-1].

### Misc torpor edge cases
- [Blade Clot](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Blade%20Clot) — controller of a vampire with a clot counter in torpor chooses whether the vampire **stays or burns**. Allies **cannot go to torpor** — they must burn [src-002, LSJ 20080612-3].
- [Puppet Master](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Puppet%20Master) / [Spirit Marionette](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Spirit%20Marionette) / [Temptation](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Temptation) — a stolen minion **returns to their previous controller** even if in **torpor/incapacitated**, but **remains in that state** [src-002, LSJ 20010119].
- [Dual Form](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Dual%20Form) [PRO] — if more than one form would go to torpor simultaneously (e.g., [Edged Illusion](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Edged%20Illusion)), the controller chooses **which one to keep** [src-002, LSJ 20050805].

## Sources
- src-001 — VTES Fifth Edition Rulebook, p. 34 (Torpor), p. 32 (aggravated skipping torpor), p. 44 (Target, Wounded, Torpor Region glossary), p. 48 (Cats' Guidance), p. 49 (Fame, Freak Drive).
- src-002 — krcg vtes.json snapshot 2026-04-18 (embedded card-level rulings).
