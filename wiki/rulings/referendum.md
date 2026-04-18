---
type: ruling
tags: [referendum, politics, polling, blood-hunt]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: draft
---

# Referendum

## Summary
A three-step voting procedure triggered by a successful political action or by a diablerie event (the **blood hunt** referendum). Votes-and-ballots are cast, counted, and the referendum passes if **votes for > votes against** (ties fail) [src-001].

## Step-by-Step Sequence [src-001]

### 1. Choose Terms
The acting Methuselah announces the referendum's specific terms (choices, targets, etc.). Terms are **not** chosen until the political action has resolved successfully — see [[political-action]].

### 2. Polling
Cards marked "during the polling step" but "before votes and ballots are cast" are played at this point.

Then all Methuselahs may cast any votes and ballots they have, in any order. Votes and ballots:
- Are called out freely; no obligation to cast.
- Once cast, **cannot be changed**.
- Each vote/ballot is cast "for", "against", or withheld (abstain).
- A single vampire's or source's votes/ballots must all be cast **in agreement** (all for, or all against).

The polling stage ends only when all Methuselahs are done casting. If a time limit is needed: **15 seconds** after the last cast is a common agreement [src-001].

### 3. Resolve the Referendum
- **More votes for than against:** passes; effects take place.
- **Otherwise (including ties):** fails; no effect.

## Acting Methuselah's Vote
All of the acting Methuselah's votes — including the 1 vote from the political action card used to call the referendum — are normal votes and **can be cast against your own referendum** [src-001 p. 46].

## Blood Hunt Referendum
When a diablerie is committed, a referendum is **automatically** and **immediately** conducted to decide whether to call a blood hunt on the diablerist. If it passes, the diablerist is burned [src-001 p. 35].

- The blood hunt referendum is **not** an action, so it **cannot be blocked**.
- **Action modifiers and reaction cards cannot be played** during the blood hunt referendum.
- Otherwise handled like any other referendum.

Full diablerie resolution arrives in stage-3 ingest; see [[diablerise-action]] for now.

## Votes vs Ballots
The rulebook distinguishes **votes** (default unit) from **ballots** (used inside sub-referendums like the Prisci block). For most purposes they work identically: both count toward the main tally. Prisci-block mechanics are covered in stage-4 (sect ingest).

## Referendum Terms — Card-Specific Rules
- [Kine Resources Contested](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Kine%20Resources%20Contested) — **cannot assign all 4 points to a single Methuselah**. You can assign points to yourself if you wish (or if no other choice exists) [src-001 p. 49].
- [Consanguineous Boon](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Consanguineous%20Boon) — must choose an **existing clan**, even if no vampires of that clan are in play [src-001 p. 48].
- [Ancilla Empowerment](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Ancilla%20Empowerment) — **every Methuselah loses pool, including you** (the referendum's caller) [src-001 p. 47].

## Common Cards Involved — Timing Subtleties
- [Bewitching Oration](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Bewitching%20Oration) — play only after terms have been declared. Gained votes need not be cast immediately; you can wait for others to cast and then choose direction (useful to avoid a Scalpel Tongue) [src-001 p. 47].
- [Scalpel Tongue](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Scalpel%20Tongue) — must wait until a vampire has cast votes before targeting them; abstaining vampires are not valid targets [src-001 p. 50].
- [Voter Captivation](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Voter%20Captivation) — played **after** action resolution. Cannot rescue you from being ousted at 0 pool as a result of the referendum — you must already be ousted by then [src-001 p. 52]. See also [[post-combat-effects#voter-captivation]].
- [Protected District](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Protected%20District) — see Bewitching Oration [src-001 p. 50].

## Common Mistakes
- Passing the 15-second "last cast" threshold and then trying to re-cast — not allowed.
- Splitting a single vampire's votes "for" and "against" — must all go the same way.
- Trying to play action modifiers/reactions during a blood hunt referendum — not allowed.
- Playing Bewitching Oration at action announcement — it must wait for terms to be declared (i.e., after the political action succeeds).

## Card-Level Rulings (krcg)
Edge cases surfaced from krcg-embedded `rulings[]` [src-002]. Each entry preserves the original reference label (RTR/LSJ/ANK/PIB).

### Automatically-passing referendum — shared restriction
The following vote-gaining / vote-manipulating cards **cannot be used during a referendum that is automatically passing** (e.g., via [Delaying Tactics](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Delaying%20Tactics) or similar effects that bypass the polling step):

- [Bewitching Oration](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Bewitching%20Oration)
- [Perfect Paragon](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Perfect%20Paragon)
- [Scalpel Tongue](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Scalpel%20Tongue)

[src-002, PIB 20150105, LSJ 19980107].

### [Voter Captivation](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Voter%20Captivation)
- Is played after resolution, **after all combats (if any)** are handled, but still **during the action**. "After resolution" action modifiers and effects can be played **before or after** Voter Captivation [src-002, PIB 20150915, LSJ 19981028, ANK 20190425].
- **Can** be used after a referendum that is automatically passing — but in that case the vote is considered to have passed by **0 votes** (so VC grants only 1 blood / 1 pool, not more) [src-002, LSJ 19980107, PIB 20150105].

### [Perfect Paragon](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Perfect%20Paragon)
- Can be played **any time during the action before resolution** — a block attempt is **not required** first [src-002, LSJ 20020612].

### Multi-oust referendums — shared rule ([Ancilla Empowerment](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Ancilla%20Empowerment), [Kine Resources Contested](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Kine%20Resources%20Contested), and similar)
- If a referendum outcome ousts **multiple Methuselahs simultaneously**, players whose **prey** gets ousted **still get a victory point** — **even if they themselves are being ousted in the same resolution**.
- **Only surviving** Methuselahs receive the **6 pool** from their prey's oust. Pool is **not** granted from a grand-prey's oust [src-002, LSJ 20000309].

### [Kine Resources Contested](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Kine%20Resources%20Contested)
- Can allocate **more points** than a Methuselah has pool (extra pool loss simply overshoots, contributing to oust resolution) [src-002, LSJ 20020819].

## Sources
- src-001 — VTES Fifth Edition Rulebook, pp. 27–28 (The Political Action — Referendum), p. 35 (Blood Hunt referendum restrictions), p. 46 (voting against own referendum), p. 47 (Ancilla Empowerment, Bewitching Oration), p. 48 (Consanguineous Boon), pp. 49–50 (Kine Resources Contested, Protected District, Scalpel Tongue), p. 52 (Voter Captivation).
- src-002 — krcg vtes.json snapshot 2026-04-18 (embedded card-level rulings).
