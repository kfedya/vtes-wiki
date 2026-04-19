---
type: ruling
tags: [post-combat, freak-drive, voter-captivation, taste-of-vitae, timing, ordering, premature-combat-end, anesthetic-touch]
sources: [src-001, src-002, src-003]
last_verified: 2026-04-19
status: draft
---

# Post-Combat & Post-Action Effects

## Summary
Several cards are played **after** an action or combat has resolved, which creates ordering puzzles: Freak Drive, Voter Captivation, and Taste of Vitae all sit in the "after resolution" window. The rulebook FAQ fixes the order of operations so stacking stays deterministic [src-001].

## The "After Resolution" Window
When an action resolves (successfully or not), certain cards can fire in the follow-up:
- **Freak Drive** — unlocks the acting vampire for another action.
- **Voter Captivation** — gains pool/blood after a successful referendum.
- **Taste of Vitae** — gains blood from a vampire opponent who lost blood in combat.

These cards are all played **after** the action/combat ends, and their order can matter.

## Freak Drive
- Played **after combat** if the acting vampire was blocked [src-001 p. 49].
- **Can even be played if the vampire is now in torpor**, provided they still have blood to pay the cost [src-001 p. 49]. (Unusual — most abilities require the minion to be ready.)
- Unlocks the acting vampire, letting them take another action this turn.
- A vampire who Freak Drives and unlocks **cannot play the same once-per-turn effect again** — e.g., [Enchant Kindred](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Enchant%20Kindred) and [Govern the Unaligned](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Govern%20the%20Unaligned) cannot be played again this turn by the same vampire, even at a different level [src-001 pp. 48–49].

## Voter Captivation
- Played **after** the referendum's action has resolved [src-001 p. 52].
- **You cannot use Voter Captivation to regain pool and survive** a referendum that leaves you at 0 pool — the action has already resolved by the time Voter Captivation fires [src-001 p. 52].
- **Voter Captivation and Freak Drive can be played in either order** after the action, since both fire in the same window [src-001 p. 52].

## Taste of Vitae
- Played **after combat** against a vampire (not allies) [src-001 p. 51].
- Can be played if the opposing vampire has **not** actually lost any blood — in that case it just cycles [src-001 p. 51].
- **Must be played after you decide to press or not** [src-001 p. 51]. Press decisions come first.
- **Can be played even if the round ended prematurely** (e.g. a `Strike: combat ends` rider fired) [src-002, RTR 20001020, LSJ 20001024, RTR 20030519]. See [Premature Combat End](#premature-combat-end).
- Counts **blood lost**, not damage inflicted. A 1-damage hand strike against a vampire at 0 blood sends them to torpor without burning blood — `Taste of Vitae` cycles for **0** in that case [src-001 p. 51].

## Premature Combat End
The round of combat can end before the normal end-of-round step via a **combat-end strike** ([Majesty](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Majesty), [Catatonic Fear](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Catatonic%20Fear), [Disarm](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Disarm), [Psyche!](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Psyche%21), …) or a **combat-end rider** ([Anesthetic Touch](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Anesthetic%20Touch) [OBE], [Loving Agony](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Loving%20Agony), any `Strike: combat ends. <rider>`).

**Post-combat cards still fire.** The "end of round" window opens once combat has ended, regardless of *how* it ended — the press decision is simply skipped when combat was forced to end [src-002, RTR 20001020, LSJ 20001024, RTR 20030519].

### Worked example — Anesthetic Touch [OBE] + Taste of Vitae
[Anesthetic Touch](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Anesthetic%20Touch) card text (verbatim, [src-002]):

> Only usable at close range.
> [aus] Strike: dodge.
> [obe] Strike: hand strike. Combat ends immediately after the resolution of this strike.
> [OBE] As [obe] above, with first strike.

Key krcg rulings on Anesthetic Touch [src-002]:
- "Does not end combat **as a strike**; it ends combat **after strike resolution**. It is still just a hand strike." [LSJ 20011210-1]
- "Does not end combat until after strike resolution, so the damage **can be prevented or healed as normal**." [LSJ 20011210-3]
- "A dodge won't prevent combat from ending after strike resolution." [LSJ 20011210-2]

Sequence at close range:
| # | Event |
|---|---|
| 1 | Anesthetic Touch declared as [OBE] first strike |
| 2 | First-strike segment: hand strike resolves → damage dealt |
| 3 | Opposing vampire burns blood to mend (or goes to torpor at 0 blood) |
| 4 | "Combat ends immediately after the resolution of this strike" — combat ends here |
| 5 | Press decision — **skipped** (combat ended by rider, not by natural round end) |
| 6 | Post-combat window: `Taste of Vitae`, `Freak Drive`, etc. |

`Taste of Vitae` gains blood equal to the opposing vampire's **blood lost to damage** this round — so it still pays out even though combat ended prematurely.

### What does NOT survive premature combat end
- **In-combat effects** on the rider half of a strike — the rider's damage/effect happens **after** combat has ended, so combat-only defences no longer apply. See [[strike-effects#combat-ends-with-a-damage-rider]] for the general rule and card-specific fallout (Target Vitals boost, Dawn Operation scope, Amaranth timing) [src-002, src-003].
- **Additional strikes** this round — combat ended, no further strikes resolve.
- **Dodge** on the striker's side does not retroactively cancel the combat-end — dodge protects the dodger from the strike's direct effects, not from the rider firing "combat ends" [src-002, LSJ 20011210-2].

## Ordering Cheat-Sheet
When multiple post-action effects fire on the same action/combat:

| Order | Event |
|-------|-------|
| 1 | Action/combat ends (naturally OR prematurely via combat-end strike/rider) |
| 2 | Press decision (if applicable — skipped when combat ended prematurely; Taste of Vitae waits for this when it applies) |
| 3 | Post-combat / post-referendum cards: Freak Drive, Voter Captivation, Taste of Vitae |
| 4 | Next action by a ready minion (if any) |

Step 3 has no enforced internal order — the owning Methuselahs sequence their plays.

## Common Mistakes
- Playing Taste of Vitae while still deliberating whether to press — the press decision comes first.
- Expecting Voter Captivation to save you from a pool-0 ouster via referendum — it fires too late.
- Thinking a vampire in torpor cannot Freak Drive — they can, if they still have blood to pay.
- Re-using a once-per-turn effect (Enchant Kindred, Govern the Unaligned) after a Freak Drive — same vampire can't replay it the same turn.
- Thinking `Taste of Vitae` is dead when combat ended prematurely (Anesthetic Touch [OBE], Majesty, Psyche!) — it **still fires**; the post-combat window always opens [src-002].
- Counting damage instead of **blood lost** for `Taste of Vitae` — a 1-damage strike against a 0-blood vampire = 0 blood lost = 0 gain (card just cycles).

## Related Rulings
- [[press]] — press vs cancel; end-of-round always occurs.
- [[combat]] — round sequence; post-combat window.
- [[strike-effects]] — combat-end strikes and combat-end riders; what does/doesn't survive combat ending.
- [[referendum]] — referendum resolution.
- [[voting]] — voting mechanics.

## Sources
- src-001 — VTES Fifth Edition Rulebook, pp. 48–49 (Enchant Kindred, Freak Drive, Govern the Unaligned), p. 51 (Taste of Vitae), p. 52 (Voter Captivation).
- src-002 — krcg vtes.json snapshot 2026-04-18 (embedded card-level rulings on Anesthetic Touch and Taste of Vitae: LSJ 20011210-1/2/3, RTR 20001020, LSJ 20001024, RTR 20030519).
- src-003 — VEKN forum thread `46164-catatonic-fear-and-loving-agony` (PIB 20130319) — cross-reference via [[strike-effects]] for combat-end rider timing rules.
