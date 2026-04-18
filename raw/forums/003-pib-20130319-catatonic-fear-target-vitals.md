# src-003 — VEKN forum thread: Catatonic Fear and Loving Agony (2013-03-19)

- URL: https://www.vekn.net/forum/rules-questions/46164-catatonic-fear-and-loving-agony
- Captured: 2026-04-18
- Ruling labels in krcg: `[PIB 20130319]`
- Participants: **wesile** (original asker), **Ankha** (Rules Director, Vincent Ripoll), **Pascal Bertrand** (rules coordinator)

This thread is the origin of the `[PIB 20130319]` ruling cited in krcg's `rulings[]` for:
- `Catatonic Fear` — "Is a damage dealing effect and can be modified by other effects like Dam the Heart's River."
- `Target Vitals` — "Can be played on a strike that does no damage, even a dodge or a combat ends, but has no effect in that case."
- (Related) `Loving Agony`, `Majesty`, `Dawn Operation`, `Amaranth`.

The two krcg rulings **are not contradictory** — they apply to different cases. This thread clarifies:

> A combat-ends strike with a damage rider (superior Catatonic Fear, superior Loving Agony) **is** a damage-inflicting strike for the purposes of Aim / damage-boost cards like Target Vitals. The krcg "has no effect in that case" note on Target Vitals applies to strikes that truly inflict no damage (basic-level combat ends with no rider, or a dodge).

## Thread dump (verbatim)

### Post 1 — wesile, 2013-03-19 13:02

> Clarifying...
> Please validate:
>
> You can use TV with Catatonic as well as with Loving Agony.
> You can dodge both strikes.
>
> You can use Dawn operation with CF and LA.
>
> I think that you can also use Amaranth...
>
> Amaranth, Combat, U
>
> Only usable by a vampire who can commit diablerie. Only usable when the opposing vampire should go to torpor. Diablerize the opposing vampire instead. Not usable by a vampire going to torpor.

### Post 2 — Ankha (Rules Director), 2013-03-19 13:18

> > You can use TV with Catatonic as well as with Loving Agony.
>
> Yes, for an added 2 damage in both case.
>
> > You can dodge both strikes.
>
> Yes, taking no damage in both case.
>
> > You can use Dawn operation with CF and LA.
>
> You can play Dawn Operation before the combat and it affects only damage dealt during the combat. Damage from CF and LA won't be aggravated since inflicted after the combat.
>
> > I think that you can also use Amaranth...
>
> No, Amaranth is a combat card. You must play it during the combat. If the vampire goes to torpor after the combat, you can't play Amaranth.

### Post 3 — wesile, 2013-03-19 13:26

> Thanks, that was the clarification that I was looking for.

### Post 4 — Pascal Bertrand, 2013-03-19 13:29

> I'm not sure what "use" means. I'm also not sure what the question is, so I'll have to guess.
>
> Target Vitals can be played on Catatonic Fear's strike. Target Vitals can be played on Loving Agony's strike. Also note that Target Vitals could also be played on Dodge or Majesty.
>
> Now, if Catatonic Fear / Loving Agony's damage is successfully inflicted, Target Vital would indeed add an extra 2 damage.
>
> Both Catatonic Fear and Loving Agony can be dodged. Even Majesty can be dodged.
>
> Now, if I Dodge Catatonic Fear / Loving Agony, is there damage inflicted? No, in both cases.
>
> Dawn Operation can be played before Catatonic Fear or before Loving Agony (it is an action modifier, thus is played before combat).
>
> Now, is Catatonic Fear / Loving Agony's damage aggravated if Dawn Operation was played previously during the blocked action? No, due to Dawn Operation's cardtext. Catatonic Fear and Loving Agony's damage is triggered after the end of combat.
>
> Can you use Amaranth? Well, if the opposing minion is going to torpor at the end of the round, yes, you can.
>
> Now, is Catatonic Fear / Loving Agony's damage applied before the end of combat? No. All "Strike: End combat and do X" effects have X happen after the end of combat - the only exception being when "do X" is untapping one (or two) minion(s). So, no, you cannot play Amaranth when striking with Catatonic Fear against a vampire with 0 blood.

## Key rulings extracted

1. **Target Vitals on Catatonic Fear / Loving Agony** — if the superior-level 1-unpreventable-damage is successfully inflicted, Target Vitals **adds +2 damage** to that damage. (Ankha, Pascal Bertrand)
2. **Target Vitals scope** — can be played on any strike, including Dodge and Majesty, but only has an effect when the strike successfully inflicts damage. (Pascal Bertrand)
3. **Dawn Operation scope** — aggravates damage *during* combat only. Catatonic Fear / Loving Agony 1-damage is inflicted *after* combat, so it is **not aggravated** by Dawn Operation. (Ankha, Pascal Bertrand)
4. **Amaranth on a 0-blood vampire struck by Catatonic Fear** — **not legal**. Amaranth is a combat card and must be played during combat; Catatonic Fear's damage applies after combat, so at the moment the opponent would die, combat has already ended. (Pascal Bertrand)
5. **General rule (Pascal Bertrand)** — *"All 'Strike: End combat and do X' effects have X happen after the end of combat — the only exception being when 'do X' is untapping one (or two) minion(s)."*

## Empirical corroboration — TWDA (krcg API)

Query: `POST https://api.krcg.org/twda/list` with `{"cards": ["Catatonic Fear", "Target Vitals"]}`.

Result (4 tournament-winning decks contain both cards):

| id | date | event | name |
|---|---|---|---|
| `2k8dcdbr3` | 2008-08-31 | DragonCon NAC Qualifier | **Fearful Vitals** |
| `2k9brisbanecq` | 2009-03-28 | Brisbane CQ | — |
| `2013ebc` | 2013-04-21 | European Championship | Violent Daughters |
| `2019bolbg` | 2019-10-26 | Bol BG | Anson's beautifull Tongue |

Sample deck — `2k8dcdbr3` "Fearful Vitals" (DragonCon NAC Qualifier, 12 players):
- **10× Catatonic Fear** + **9× Target Vitals** in the same library.

The archetype name itself is built around the combo. Fetched via `GET https://api.krcg.org/twda/2k8dcdbr3`.

## Referenced by

- Codex of the Damned, *Combat Modules* article, Presence defensive section: *"the nasty combination of Catatonic Fear with Target Vitals if you want your SCE to be more punishing."* — https://codex-of-the-damned.org/en/strategy/articles/advanced/combat-modules.html
