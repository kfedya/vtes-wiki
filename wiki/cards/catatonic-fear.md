---
type: card
tags: [combat, presence, combat-ends, damage-rider, aim-interaction, sce]
sources: [src-001, src-002, src-003]
last_verified: 2026-04-18
status: verified
---

# Catatonic Fear

> **[pre] Strike: combat ends.**
> **[PRE] As above, and after combat ends, if the range is close, this vampire inflicts 1 unpreventable damage on the opposing minion.**

— [krcg.org entry](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Catatonic%20Fear)

Combat card. Requires [pre]. Blood cost 1.

## Why it has a page
Six distinct krcg rulings + a counter-intuitive interaction with Aim / damage-boost cards that looks like "no effect" from card-db alone but actually adds damage. The archetype-defining combo **Catatonic Fear + Target Vitals** has its own TWDA deck name ("Fearful Vitals", 2k8dcdbr3) and is called out in Codex of the Damned as a signature Presence SCE module.

## Interaction with damage-boost / Aim cards

### Target Vitals (Aim) — boosts Catatonic Fear when damage lands

Rules Director Ankha and rules coordinator Pascal Bertrand confirmed in [PIB 20130319](https://www.vekn.net/forum/rules-questions/46164-catatonic-fear-and-loving-agony) that **Target Vitals adds +2 damage** to the superior-level 1 unpreventable damage **if that damage is successfully inflicted** [src-003].

Verbatim (Pascal Bertrand):

> Target Vitals can be played on Catatonic Fear's strike. […] Now, if Catatonic Fear / Loving Agony's damage is successfully inflicted, Target Vital would indeed add an extra 2 damage.

Verbatim (Ankha):

> Yes, for an added 2 damage in both case.

**Totals at close range, superior [PRE]:**
- Catatonic Fear alone: 1 damage.
- Catatonic Fear + Target Vitals (damage lands): **1 + 2 = 3 damage**, still unpreventable. Opposing minion also "cannot press this round" (from Target Vitals — moot since combat has ended, but matters if another effect would restart combat).
- Catatonic Fear + Target Vitals, **dodged**: 0 damage. Dodge defeats both strikes' effects.
- **Basic [pre] Catatonic Fear** (no damage rider) + Target Vitals: 0 damage. Here the krcg Target Vitals ruling "Can be played on a strike that does no damage, even a dodge or a combat ends, but has no effect in that case" [RTR 19960221] [PIB 20130319] [src-002] applies — the basic strike inflicts nothing, so Target Vitals' trigger ("if any damage from this strike is successfully inflicted") is never met.

> **Why the krcg "has no effect" ruling is not a contradiction.** That ruling covers strikes that literally inflict no damage: dodges, basic-level combat ends without a damage rider. Superior Catatonic Fear and superior Loving Agony are combat-ends-with-damage-rider strikes — the rider damage *is* "damage from this strike" for Aim purposes, even though it resolves after combat ends.

### Dam the Heart's River — also boosts, different wording

Dam the Heart's River adds +1 "each **strike or damaging effect**" [src-002]. The "damaging effect" clause explicitly catches the after-combat 1 damage from Catatonic Fear [PRE] [ANK 20170111] [PIB 20130319] [src-002]. If both Dam the Heart's River ([qui] basic) and Target Vitals hit, at close range superior [PRE] you get 1 + 1 + 2 = 4 damage.

### Majesty / Dodge — no damage to boost
Target Vitals on Majesty or Dodge has no effect — neither inflicts damage [src-003].

## Interaction with Dawn Operation

**Not aggravated.** Dawn Operation (action modifier) makes damage done **during** the combat aggravated. Catatonic Fear's 1 damage is inflicted **after** combat ends, so Dawn Operation does not reach it [src-003].

Pascal Bertrand: *"Catatonic Fear and Loving Agony's damage is triggered after the end of combat."*

## Interaction with Amaranth

**Cannot be used to diablerize a 0-blood vampire struck by Catatonic Fear.** Amaranth is a combat card — must be played during combat. Catatonic Fear's death-dealing damage is delivered *after* combat ends, so the legal window for Amaranth has already closed [src-003].

Pascal Bertrand: *"All 'Strike: End combat and do X' effects have X happen after the end of combat — the only exception being when 'do X' is untapping one (or two) minion(s)."*

This is a **general rule for combat-ends-with-rider strikes**, surfaced in [[strike-effects#combat-ends-with-a-damage-rider]].

## Other rulings

From krcg's embedded `rulings[]` [src-002]:

- **[PRE] Damage is done by the vampire (not environmental).** [RTR 19970630] [LSJ 19990723] — so "immune to X vampire damage" effects protect; "immune to environmental damage" does not.
- **If the strike is dodged, no damage is done.** [LSJ 19980526] [RTR 20041202] [LSJ 20070124].
- **If combat continues or a new combat begins**, the after-combat effect **does not happen / is not usable** — e.g. after `Psyche!` or `Telepathic Tracking`. [RTR 20020501] [LSJ 19980109] — partial reversal of RTR 20010711.
- **Any blood loss occurs after combat** and will not trigger Anathema or be available for Taste of Vitae, etc. [LSJ 20031123]. Mirror case: damage applied after combat **cannot be prevented by combat cards** (they're out of scope once combat ends) [LSJ 20010205].
- **Is a damage-dealing effect** and can be modified by other effects like Dam the Heart's River. [ANK 20170111] [PIB 20130319].

## Empirical — TWDA appearances

`POST https://api.krcg.org/twda/list` with both "Catatonic Fear" and "Target Vitals" returns 4 decks (as of 2026-04-18):

| id | date | event | name |
|---|---|---|---|
| [`2k8dcdbr3`](https://api.krcg.org/twda/2k8dcdbr3) | 2008-08-31 | DragonCon NAC Qualifier (12p) | **Fearful Vitals** — 10× CF, 9× TV |
| `2k9brisbanecq` | 2009-03-28 | Brisbane CQ | — |
| `2013ebc` | 2013-04-21 | European Championship | Violent Daughters |
| `2019bolbg` | 2019-10-26 | Bol BG | Anson's beautifull Tongue |

## Related
- [[strike-effects]] §Combat Ends — general ordering rules.
- [[playgroup/common-mistakes#aim-cards-on-combat-ends-with-damage-rider]] — playgroup mistake filed from this clarification.
- [Loving Agony](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Loving%20Agony) — sibling `[val]` card with the same combat-ends + 1-unpreventable-damage rider mechanic; same TV / Dawn Operation / Amaranth rulings apply.
- [Majesty](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Majesty) — pure combat-ends without damage rider; TV on Majesty has no effect.

## Sources
- src-001 — VTES 5E Rulebook (dodge, combat-ends ordering, first-strike interactions).
- src-002 — krcg snapshot 2026-04-18 (embedded `rulings[]`).
- src-003 — VEKN forum thread `46164-catatonic-fear-and-loving-agony` (PIB 20130319), Ankha + Pascal Bertrand rulings.
