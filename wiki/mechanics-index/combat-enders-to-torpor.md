---
type: mechanic-index
tags: [combat, torpor, combat-ends, strike, master-out-of-turn, reaction, finisher]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: draft
---

# Combat-Enders That Send a Vampire to Torpor — Card Index

## Scope

Cards whose effect both **ends combat** and **sends a vampire (opposing or self) to torpor**.

The underlying mechanic: per rulebook p. 30, "if during any step either combatant is no longer ready... the round and combat end immediately." Therefore a card that sends a combatant to torpor mid-combat **implicitly** ends combat — explicit "combat ends" text is redundant but sometimes present.

Not included:
- Strikes that inflict damage and incidentally cause torpor by damage threshold (ordinary damage-to-torpor is covered by [[rulings/damage-resolution]] / [[rulings/torpor]]).
- Cards that **track or reward** torpor-sending without doing it themselves (Code of Samiel, Sociopath, The Path of Lilith).
- Cards that **replace** torpor with another outcome (burn-instead, diablerize-instead) — listed separately under "Redirectors" for cross-reference.

## Cards by category

### Strikes that send the opposing vampire to torpor (combat ends as consequence)

These are the **cleanest combat-enders**: the strike directly places the opposing vampire in torpor, which ends combat automatically.

- [Coma](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Coma) — Dementation.
  - `[dem]`: "Strike: send the opposing vampire to torpor."
  - `[DEM]`: as above, and the opposing vampire **does not unlock** as normal during their next unlock phase.
- [Entombment](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Entombment) — Obtenebration.
  - `[obt]`: "Strike: burn the opposing ally."
  - `[OBT]`: "Strike: send the opposing vampire to torpor."
- [Touch of Oblivion](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Touch%20of%20Oblivion) — Oblivion.
  - `[OBL]`: "Strike: send the opposing vampire to torpor or burn the opposing ally."

### Conditional: strike damage triggers torpor

- [Basilisk's Touch](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Basilisk%27s%20Touch) — Mytherceria (+ Potence at inferior for strength).
  - `[myt]`: "Only usable in combat with an ally or younger vampire. If any damage is successfully inflicted from this vampire's hand strikes this round, send the opposing vampire to torpor or burn the opposing ally."
  - Restricted to **ally or younger vampire** combats. Combat ends on hand-strike damage → torpor trigger.

### Master: out-of-turn

- [Rötschreck](https://codex-of-the-damned.org/en/card-search/library/index.html?card=R%C3%B6tschreck) — Master: out-of-turn. Frenzy.
  - "Put this card on a vampire when an opposing minion attempts to inflict aggravated damage on him or her... Combat ends. This vampire is locked and sent to torpor. This vampire does not unlock as normal. During this vampire's next unlock phase, burn this card."
  - **Target:** the vampire receiving the aggravated damage — per krcg ruling `[RTR 19980623]`, "is played on the vampire that would receive the aggravated damage." No "your vampire" restriction — **can be played on ANY vampire**, including an opposing one about to eat an aggravated strike from your vampire.
  - **Offensive combo:** your vampire announces an aggravated-damage strike → you play Rötschreck on the opposing target → combat ends, opposing vampire locked + torpor.
  - Additional krcg rulings worth keeping in mind:
    - Only after strike declaration, before resolution `[LSJ 19990217, RTR 20041202, LSJ 20100119]`.
    - Cannot be played if the aggravated damage comes from a **non-strike** effect (e.g., Outside the Hourglass + Domain of Evernight) `[ANK 20220114]`.
    - Cannot be played if the damage is **not effective at the current range** `[RTR 19980928, ANK 20211102]`.
    - Works even if the opponent announced **Strike: Dodge** or **Strike: Combat Ends** `[LSJ 20011005, ANK 20211102]`.
    - Works even if the opponent treats aggravated as normal `[ANK 20200130-1]`.
    - Ends combat immediately; strikes are not resolved, damage prevention cannot be played, and a **second Rötschreck cannot be played** `[LSJ 19990217, LSJ 20020715, LSJ 20060803]`.
    - **Key edge case:** "Ends combat with both minions still **ready**, so cards and effects usable 'when the opposing vampire is going to torpor / should go into torpor / is not ready' **cannot be used**" `[LSJ 20070709-2, LSJ 20020402]`. This means you **cannot chain** [Decapitate](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Decapitate), [Amaranth](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Amaranth), [Ahriman's Demesne](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Ahriman%27s%20Demesne), or [Tortured Confession](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Tortured%20Confession) off a Rötschreck-induced torpor.
    - If the combat continues or a new combat begins, the card is put on the vampire, but they are **not** locked and do **not** go to torpor. They still do not unlock as normal `[RTR 20020501, LSJ 20071009]`.

### Reaction: title-sacrifice trigger

- [Legacy of Power](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Legacy%20of%20Power) — Reaction. Requires a ready prince, justicar or Inner Circle member.
  - "Only usable when another vampire you control enters combat. Lock this reacting vampire and **end combat**. **Each of the vampires involved in that combat goes to torpor.**"
  - Both-combatants-to-torpor with a title-holder tax. Last-ditch break-the-engagement card.

### Self-torpor + combat ends (for completeness)

Cards where the acting minion voluntarily goes to torpor to end combat. Not the "torpor-your-opponent" use case, but share the "combat ends + torpor" pattern:

- [Mummify](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Mummify) — Serpentis. "Strike: combat ends. This vampire unlocks and goes into torpor."
- [Ashes to Ashes](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Ashes%20to%20Ashes) — Thanatosis + Fortitude. At `[thn]` and `[THN]`: prevent all damage, this vampire unlocks and goes to torpor (ending combat).
- [Undead Persistence](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Undead%20Persistence) / [Undying Tenacity](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Undying%20Tenacity) — Fortitude. Delay torpor until combat ends (defer, not trigger).

### Related: Redirectors (replace the torpor outcome)

Cards that convert an imminent "going to torpor" into something else — they don't send-to-torpor themselves but interact with the torpor-causing strikes above:

- [Decapitate](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Decapitate) `[POT]`: "Only usable when the opposing vampire is going into torpor... Burn the opposing vampire instead."
- [Amaranth](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Amaranth): "Only usable when the opposing vampire should go to torpor. Diablerize the opposing vampire instead."
- [Ahriman's Demesne](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Ahriman%27s%20Demesne) `[OBT]`: "If the opposing vampire would go to torpor during the resolution of this strike, instead they are burned."

**Reminder:** Rötschreck does **not** allow these redirectors because it ends combat with both combatants still ready (see Rötschreck section above) `[LSJ 20070709-2]`.

### Related: end-of-round / post-combat torpor-senders

These do not end combat (combat concludes naturally by its own rules), but are listed here so a reader looking for "how do I torpor my opponent" doesn't miss them:

- [Disarm](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Disarm) `[pot]` — end of round, if you inflicted more damage; attaches + torpors opposing.
- [Cobra Fangs](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Cobra%20Fangs) `[SER]` — if hand-strike damage landed, opposing goes to torpor **next unlock phase**.
- [Pulled Fangs](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Pulled%20Fangs) — attaches, forces-hunt → torpor.
- [Blade Clot](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Blade%20Clot) — diablerie aftermath. Clot counters → torpor/burn in unlock phase (allies cannot go to torpor — they burn) `[LSJ 20080612-3]`.
- [Cardinal Sin: Insubordination](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Cardinal%20Sin:%20Insubordination) — Reaction after combat vs a non-titled Sabbat vampire; opposing goes to torpor (combat already ended).
- [Tortured Confession](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Tortured%20Confession) — combat card "only usable when the opposing vampire goes into torpor"; combat ends + peek opposing hand. This is a **response** to torpor, not the cause.

## Query used

Reproducible — re-run on snapshot update.

```
# Broad pass: all library shards
jq -r '.[] | select((.card_text // "" | ascii_downcase) | test("torpor")) |
               select((.card_text // "" | ascii_downcase) | test("combat ends|end.*combat|into torpor")) |
               {name, types, card_text}' card-db/library/*.json
```

Then manual semantic cleanup: discard self-torpor-only cards, torpor-tracking masters, and damage-to-torpor natural consequences. The candidates above are what remains.

## Practical notes

- **Combat ends before strike resolution** (rulebook p. 33). But Rötschreck is a master out-of-turn whose "combat ends" text fires *before* strike resolution as well — both bypass the strike entirely.
- Rötschreck is a **unique table-level combo** because it sends opposing to torpor **without requiring a successful strike** (only the strike declaration).
- Combining Coma/Entombment/Touch of Oblivion with [Decapitate](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Decapitate) (POT) on the same vampire is the canonical "torpor → burn" finisher chain.
- Legacy of Power costs a titled vampire's action — use it as a **survivability tool** when a key vampire is in a lethal combat, not as an offensive finisher.

## Related

- [[rulings/combat]] — combat sequence and impulse.
- [[rulings/strike-effects]] — combat ends resolves first; dodge does not cancel combat ends.
- [[rulings/torpor]] — torpor mechanics, "fizzle" on leave-torpor.
- [[rulings/damage-resolution]] — aggravated → wounded → torpor pathway.
- [[entities/disciplines/dementation]] — hosts Coma.
- [[entities/disciplines/obtenebration]] — hosts Entombment.
- [[entities/disciplines/oblivion]] — hosts Touch of Oblivion.

## Sources

- src-001 — VTES 5E Rulebook, p. 30 (combatant no longer ready → combat ends), p. 33 (combat ends resolution order).
- src-002 — krcg vtes.json snapshot 2026-04-18 (card text + embedded `rulings[]` for Rötschreck, Coma, Entombment, Touch of Oblivion, Legacy of Power, Basilisk's Touch, Mummify, Ashes to Ashes, and related).
