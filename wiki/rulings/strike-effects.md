---
type: ruling
tags: [combat, strike-effects, hand-strike, dodge, combat-ends, damage-rider, sce, first-strike, steal-blood, destroy-equipment, steal-equipment]
sources: [src-001, src-002, src-003]
last_verified: 2026-04-19
status: verified
---

# Strike Effects

## Summary
Strikes come in several flavours. Each has its own range, interaction, and ordering. The most important effects are **hand strike**, **dodge**, **combat ends**, **steal blood**, **destroy/steal equipment**, and **first strike** [src-001 pp. 33–34].

## Hand Strike
The default strike when a minion doesn't play a strike card or weapon. At close range, it deals damage equal to the minion's **strength** to the opposing minion. Vampires have a default strength of 1 [src-001 p. 33].

- Hand strike is a **close**-range strike.
- [Roundhouse](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Roundhouse) is a hand strike — it still works when the round is restricted by [Immortal Grapple](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Immortal%20Grapple) [src-001 p. 50].

## Dodge
A defensive strike dealing **no** damage but protecting the dodging minion and their possessions from the effects of the opposing strike. Details [src-001 p. 33]:
- **Effective at any range.**
- Protects **even from first strike**.
- A dodge is a strike (it fills that pair slot).
- **Does NOT protect retainers** — the retainer is still exposed to the attack.
- **Does NOT cancel combat ends** — combat ends only cancels effects directed at the dodging minion.
- **Does NOT protect from environmental damage** — dodge only protects from the **opponent's strike**. So Carrion Crows' damage, which is environmental, cannot be dodged [src-001 p. 48].

## Combat Ends
Immediately ends combat. Resolution order:
- Combat ends is **first to resolve**, even before first strike [src-001 p. 33].
- Ends combat **before other strikes or strike-resolution effects** are resolved.
- Effective **at any range**.
- **Not affected by a dodge** (dodge only cancels effects directed at the dodging minion).
- **A strike: combat ends ends combat before Carrion Crows damage is inflicted** [src-001 p. 48].

### Combat Ends with a damage rider

Several strike cards read `Strike: combat ends, AND <X>` — e.g. [Catatonic Fear](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Catatonic%20Fear) [PRE] (1 unpreventable damage after combat ends at close), [Loving Agony](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Loving%20Agony) [val] (same pattern), [Majesty](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Majesty) (no damage, pure SCE).

**General rule, per Pascal Bertrand** [src-003]:
> *"All 'Strike: End combat and do X' effects have X happen **after** the end of combat — the only exception being when 'do X' is untapping one (or two) minion(s)."*

Consequences:
- **The rider X is NOT protected by being part of combat resolution.** Combat-card prevention, `Taste of Vitae`, and other in-combat effects are out of scope once combat ends [LSJ 20010205] [LSJ 20031123] [src-002].
- **Dodge cancels the rider damage, but combat still ends** [LSJ 19980526] [RTR 20041202] [LSJ 20070124] [src-002]. Dodge protects the dodging minion from effects of the opposing strike directed at the dodger; "combat ends" is not directed at the dodger so it still resolves. Verbatim from RTR 20041202 (LSJ): *"Combat Ends will still end combat, but any additional effects the strike would have on the dodger, like Catatonic Fear's damage, are dodged."* Verbatim from LSJ 20070124: *"Yes. Well, it avoids the damage (the damage is never applied, rather than being applied and prevented)."* Source URLs in `card-db/library/combat.json` under Catatonic Fear's `rulings[].references[].url`.
- **If combat continues** (e.g. `Psyche!`, `Telepathic Tracking` restart combat), the after-combat rider **does not happen / is not usable** [RTR 20020501] [src-002].
- **Aim / damage-boost cards can boost the rider** when the rider damage successfully lands. [Target Vitals](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Target%20Vitals) adds **+2 damage** to Catatonic Fear [PRE] or Loving Agony [val] rider damage if it is inflicted [PIB 20130319] [src-003]. `Dam the Heart's River` adds +1 via its "strike OR damaging effect" clause [ANK 20170111] [src-002]. The general krcg Target Vitals ruling "has no effect on a strike that does no damage" [RTR 19960221] covers basic-level SCE without a rider (and dodges), **not** SCE strikes that carry a damage rider.
- **Damage-aggravating effects DO NOT reach the rider** if they scope to "during combat". [Dawn Operation](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Dawn%20Operation) only aggravates damage dealt during combat, so Catatonic Fear / Loving Agony rider damage **is not aggravated** by a pre-combat Dawn Operation [src-003].
- **Combat-only cards cannot be used on the rider outcome.** [Amaranth](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Amaranth) is a combat card — so you cannot Amaranth a vampire who dies from Catatonic Fear's after-combat damage; combat has already ended when that death happens [src-003]. Same logic for any combat-only effect that would trigger on the rider result.
- **Exception — untap riders** (`Strike: combat ends, this vampire unlocks` and similar) resolve before combat ends so they happen inside combat [src-003].

Full breakdown on the card page: [[wiki/cards/catatonic-fear|Catatonic Fear]]. Common mistake entry: [[playgroup/common-mistakes#aim-cards-on-combat-ends-with-damage-rider]].

## Steal Blood
Moves blood counters (or life counters) from the target to the striking minion. Details [src-001 p. 33]:
- **Not damage** — therefore **cannot be prevented** by damage-prevention effects.
- Resolves **before** the mend-damage step, so stolen blood can be used to mend damage inflicted simultaneously.
- If stolen blood would exceed the striking vampire's **capacity**, the excess drains immediately.
- If two vampires steal blood from each other, the blood is moved **simultaneously** [src-001 p. 51 — [[wiki/cards/theft-of-vitae|Theft of Vitae]]].
- A **strike: combat ends** resolves **before** [[wiki/cards/theft-of-vitae|Theft of Vitae]] — you do **not** steal blood in that case [src-001 p. 51].

## Destroy Equipment / Destroy Weapon
Burns a piece of equipment (or a weapon) of the opposing minion. The striking minion picks which piece. The equipment can still be used **up to the point the destroy-equipment strike resolves** [src-001 p. 34].

## Steal Equipment
Like destroy equipment, but the equipment is **moved** to the striking minion instead of burned. The stolen equipment may **not** be used by the new bearer during the current round of combat. It is kept after combat ends [src-001 p. 34].

## First Strike
An offensive strike done faster than normal. Details [src-001 p. 34]:
- Resolves **before** a normal strike.
- If the opposing minion is burned or sent to torpor by the first-strike, **their normal strike is not resolved at all**.
- If the opposing minion was striking with a weapon that is **stolen or destroyed** by first strike, that minion simply **loses their strike altogether**.
- If **both** minions strike with first strike, the strikes resolve **simultaneously**.
- A first-strike does **not** resolve before a **combat ends** (combat ends is still first).
- **A dodge still works against first strike.**

## Ordering Summary (cheat-sheet)
1. **Combat ends** — before everything.
2. **First strike** — before normal.
3. **Normal strikes** — simultaneous.
4. **Steal blood** — resolves before mend (not damage).
5. **Damage resolution** — prevent, then mend. See [[damage-resolution]].
6. **Additional strikes** — then repeat 4–5 for each additional.

## Example — Steal Blood (from rulebook)
Chrysanthemum (capacity 5, 4 blood) fights an Underbridge Stray ally (2 life). At close range Chrysanthemum strikes to steal 2 blood. The ally strikes for 1 damage. Simultaneously: 2 life counters move to Chrysanthemum (excess over capacity 5 — 1 blood drains off), then she burns 1 blood to mend the incoming damage. Final: Chrysanthemum 4 blood, ally burned (0 life) [src-001 p. 33].

## Edge Cases & Card-Specific Rulings
- **Carrion Crows** — environmental, cannot be dodged; combat ends beats it [src-001 p. 48].
- **Murder of Crows** — retainer environmental damage; works like Carrion Crows [src-001 p. 49].
- **Hidden Strength** — can only be played if there is damage to prevent; cannot be used solely to cycle into a press [src-001 p. 49].
- **Swallowed by the Night** — action modifier at basic, combat card at superior [src-001 p. 51].
- [[wiki/cards/theft-of-vitae|Theft of Vitae]] — see Steal Blood section above [src-001 p. 51].
- **Taste of Vitae** — cannot be used during combat against an ally; can be played if opposing vampire hasn't lost blood this combat to "cycle"; must be played **after** decision to press or not [src-001 p. 51].

## Common Mistakes
- Assuming dodge protects retainers or from environmental damage — it doesn't.
- Assuming a dodge cancels combat ends — it doesn't.
- Preventing stolen blood with a damage-prevention card — can't; steal blood isn't damage.
- Ordering first strike before combat ends.
- Forgetting that a destroyed weapon may still be used up to the instant the strike resolves.

## Card-Level Rulings (krcg)
Edge cases surfaced from krcg-embedded `rulings[]` [src-002]. Each entry preserves the original reference label (RTR/LSJ/ANK/PIB).

### [Taste of Vitae](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Taste%20of%20Vitae)
- Must be played **after the press step** is handled, and **can** be played **even if the round ended prematurely** [src-002, RTR 20001020, LSJ 20001024, RTR 20030519].
- Can be played **before or after** end-of-round effects and "when the combat would end" effects (e.g., [Telepathic Tracking](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Telepathic%20Tracking)). Can be played **after [Psyche!](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Psyche%21)** [src-002, LSJ 20021113, ANK 20191219, ANK 20180910-1].
- Can be played **even if the opposing minion was burned** during combat [src-002, LSJ 20031201-2].

### Cross-reference
- Hidden Strength's "X can be higher than strictly needed (prevents up to X+1)" ruling is surfaced in [[combat#hidden-strength]].

## Sources
- src-001 — VTES Fifth Edition Rulebook, pp. 33–34 (Strike Effects sidebar, First Strike, Destroy/Steal Equipment, Steal Blood), p. 48 (Carrion Crows), p. 49 (Murder of Crows, Hidden Strength), p. 50 (Roundhouse), p. 51 (Swallowed by the Night, Taste of Vitae, Theft of Vitae).
- src-002 — krcg vtes.json snapshot 2026-04-18 (embedded card-level rulings).
- src-003 — VEKN forum thread `46164-catatonic-fear-and-loving-agony` (PIB 20130319) — general rule for "Strike: End combat and do X" effects (X happens after combat, except untap X), Target Vitals +2 on SCE rider damage, Dawn Operation scope, Amaranth timing.
