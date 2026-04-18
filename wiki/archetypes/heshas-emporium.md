---
type: archetype
tags: [archetype, combo, powerbleed, ministry, anarch, equipment, hesha-ruhadze, death-star, twda]
sources: [src-004]
last_verified: 2026-04-18
status: draft
---

# Hesha's Emporium (Trinket Emporium)

Ministry combo powerbleed deck built around **Hesha Ruhadze (G6)** and his ability *"Anarch: Hesha gets +1 bleed for each unique equipment attached to him."* Pile ~20 unique equipments on Hesha, bleed for 20+ per action, oust table in 3–5 turns. Descendant of Matt Morgan's classic **Death Star** archetype.

Notable tournament result: **Sérgio Louçã Martins** brought "Hesha's trinket emporium" to the 2024 Atlantic Cup finals as 1st seed with a **3GW13+1** score [src-004].

## Core idea

1. **Angel Chavarria** (cap 4 Ministry, Anarch via [[wiki/cards/the-red-question|The Red Question]] flavor) is influenced first and serves as the *setup minion*.
2. Angel chains **Hag's Wrinkles** (29 copies) during repeated **equip actions**. Hag's Wrinkles is the engine:
   - `[obf]` +2 stealth on the equip action.
   - `[thn]` unlock this vampire after the action resolves if successful (→ infinite equip chain).
   - `[THN]` as `[thn]` + another +1 stealth.
   - Source of `[thn]` is **Vial of Elder Vitae** (+1 level of any Discipline) and **The Textbook Damnation**.
3. **Learjet** (×6) is grabbed early so Angel can plow through the library during the equip chain and fetch the combo pieces.
4. **Kaymakli Fragment** (×2) + **The Textbook Damnation** (×2) help bring **Hesha Ruhadze (G6)** into play the turn after Angel's setup.
5. Turn 3–4: **Nod** (trifle, rearranges equipment on all ready minions) or **Heidelberg Castle, Germany** (lock to move blood/equipment/retainers between two of your ready vampires) moves the full equipment pile from Angel onto Hesha in one action.
6. Hesha bleeds for ~20 using **unblockable** bleed-enablers: [[wiki/cards/flaming-candle|Flaming Candle]], [[wiki/cards/concoction-of-vitality|Concoction of Vitality]], [[wiki/cards/horrific-countenance|Horrific Countenance]].

## Key disciplines and clans

- **Clan:** Ministry (both Angel and Hesha).
- **Disciplines (Hesha G6, cap 7):** `ani`, `aus`, `obf`, `[PRE]`, `[PRO]`.
- **Disciplines borrowed via equipment:**
  - `[THA]` (Blood Sorcery) — via **Vial of Elder Vitae**, **The Textbook Damnation**, **Veneficorum Artum Sanguis**, **Ritual Goblet** — enables **Perfect Clarity** (cancels DOM/PRE reactions, i.e. bounce).
  - `[obf]` → `[OBF]` — via **Vial of Elder Vitae** — enables **I am Legion** (`[DAI][OBF]`) and heavy stealth.
- **Sect:** Anarch — required by **The Red Question** activation on Angel, and by Hesha's own *"Anarch: ..."* trigger.

## Signature cards

### Crypt (12)
- **Hesha Ruhadze (G6)** ×6 — cap 7 Ministry, Anarch, `ani/aus/obf/PRE/PRO`. *"Anarch: Hesha gets +1 bleed for each unique equipment attached to him."*
- **Angel Chavarria** ×6 — cap 4 Ministry setup vampire; enables the Hag's Wrinkles equip chain via the 1st-turn influence cycle.

### Library (79)
- **Master (3):** Direct Intervention ×1, Heidelberg Castle Germany ×1, Nod ×1 — the *minimum* master pile; the deck cannot afford any more because it races to oust.
- **Action (1):** Revelations ×1 — emergency anti-bounce.
- **Equipment (35):** 27 distinct *unique* equipment cards + 2× Kaymakli Fragment + 2× The Textbook Damnation + 2× Vial of Elder Vitae + 6× Learjet. Every unique card on Hesha = +1 bleed. Highlights:
  - **Learjet ×6** — electronic, +1 bleed AND enables super-cycling during equip chain.
  - **Kaymakli Fragment ×2** — brings Hesha into play faster.
  - **Codex of the Edenic Groundskeepers** — +3 bleed vs empty prey (with −2 stealth trade).
  - **Seal of Veddartha** — gives Hesha `[dom]` access after 1 counter (see #considerations).
  - **Flaming Candle / Concoction of Vitality** — unblockable *by vampires only*.
  - **Blood Tears of Kephran** — burn for 2 blood or 2 damage prevention.
  - **Monocle of Clarity** — check for a bounce/Archon before committing the lunge.
  - **Body Bag** — fail any rush attempt at Hesha.
- **Action Modifier (38):** **Hag's Wrinkles ×29**, Perfect Clarity ×2, I am Legion ×2, Under My Skin ×2, Approximation of Loyalty, Horrific Countenance, The Red Question.
- **Action Modifier/Combat (2):** Force of Personality, Hide the Mind.

Full decklist: `raw/decks/004-heshas-trinket-emporium.html` (CotD archive; the `<meta property="decklist">` tag carries the canonical JSON).

## Support / tech

### Anti-bounce stack
1. **Monocle of Clarity** — pre-action check for the bounce.
2. **Perfect Clarity** `[tha]` — the prey's bounce (Deflection / Telepathic Misdirection requires `[dom]` or `[pre]`) has no effect.
3. **I am Legion** `[dai][obf]` — cancels `[aus]` reactions (most intercept).
4. **Hide the Mind** `[obf]` — cancels `[aus]` reactions as action modifier or combat card.
5. **Approximation of Loyalty** + **Revelations** — last-resort anti-bounce chain when Perfect Clarity can't fire.

### Anti-rush
- **Body Bag** — prevents combat when rushed.
- **Sire's Index Finger** — frenzy immunity.

### Block denial (for the *finishing* bleed)
- **Horrific Countenance** `[pro]` — triggered after a block, makes the action truly unblockable (vs. allies too — see #considerations).
- **Flaming Candle** — unblockable by *vampires only*.
- **Concoction of Vitality** — unblockable by *vampires only*.

## Variants

- **Classic "Death Star"** (Matt Morgan) — pre-G6 Hesha. Same equipment-stacking spine; built on **Hesha Ruhadze (G2)** or other cap-7+ vampires with DOM/PRE bleed support. TWDA has 21+ Hesha decks, most using G2. The G6 printing (Fifth Edition: Anarch, 2021) triggered the modern Emporium build.
- **Setite Death Star 2023** (Karl Schaefer) — G2 Hesha + Ezekiel, Lord of Montreal + Samat Ramal-Ra political variant; Origins 2023 TWDA id `10733`.
- **V5 Setite/Ministry Tempt-stack** — older Hesha G2 "Tempt me plox" / "Vem para mim…" shells use Temptation + Waters of Duat (Ministry action) instead of equipment stacking.

## Weaknesses

1. **Ally-heavy preys (Hecata, Lasombra allies, hunter decks).** Both **Flaming Candle** and **Concoction of Vitality** specify *"vampires cannot block"* — **allies block them as normal**. Only **Horrific Countenance** is truly unblockable once triggered, but there is only 1 copy in the original build. See [Considerations → ally weakness].
2. **Bait And Switch.** `[aus]` bounce that doesn't require `[dom]/[pre]` → **Perfect Clarity** and **I am Legion** don't cancel it. Only Approximation of Loyalty + Revelations can pay, and both are 1-of.
3. **Blood economy.** The base list runs **zero blood-gain masters**. Hesha burns 1 blood per bleed with Codex of the Edenic Groundskeepers, 1 blood + the card for Flaming Candle, 1 blood for Under My Skin persistence. Over the full oust chain of 2 preys (5–7 turns), Hesha runs dry without support.
4. **Precision execution.** Wrong Learjet discard order loses the combo turn. The Sargon Fragment partially mitigates but the deck is fragile.
5. **Card availability.** Hag's Wrinkles is an unreprinted rare — collecting 29 copies is physically difficult.

## Considerations

### Ally weakness — anti-ally options to add
These close the Hekata / ally-swarm matchup without significantly bloating the master pile. See [[wiki/rulings/bleed|bleed]] and the block-denial rulings.

| Card | Type | Cost | Req | Effect |
|------|------|------|-----|--------|
| Libertas | Master | 1 pool | Anarch | Put on an Anarch. *Allies cannot block this Anarch.* Also: `[dom]`/`[pre]` cards cost other minions +1 blood against this Anarch. One copy closes the matchup. |
| Invigorate | Action Mod | free | Anarch, `[dom]` | `[dom]`: this Anarch cannot be blocked by allies this action. Hesha gets `[dom]` from **Seal of Veddartha** after 1 counter. |
| Horrific Countenance ×2 more | Action Mod | free | `[pro]` | First block → action becomes truly unblockable. Deck runs only 1; 3 copies total gives per-turn coverage. |
| Into Thin Air | Action Mod | free | `[obf]` | `[obf]` +1 stealth + burn 1 blood → ally/younger vampire −1 intercept. Incompatible with Lost in Crowds in same action. |

### Blood economy — sustain options
Tempo-aware additions (deck plays 5–7 turns across the full oust chain, not 3 — the initial Turn-3 kill only covers prey #1):

| Card | Type | Cost | Req | Effect |
|------|------|------|-----|--------|
| Cooler | Equipment | 1 pool | — | 4 blood counters, 1/unlock to vampire. Also counts as unique equipment → +1 bleed to Hesha. Double duty. |
| Blood Doll | Master | free | — | 1 blood per master phase, flexible direction. 2 copies: one on Angel (cap 4), one on Hesha. |
| Spoils of War | Action Mod | free | — | After successful directed action: +1 blood to vampire, +1 pool to you. Pure refund on bleed. |
| Giant's Blood | Master | free | 1/game | Full refill to capacity. Single emergency slot for the finishing turn. |

### Why the base list cannot accept generic "obvious" improvements
- **Villein ×3** — classic bleed-deck master, but it takes blood *from* the vampire to your pool. Wrong direction for Hesha.
- **Heavy master package** — 10+ masters brick in hand because even in the full oust chain, the deck only plays 5–7 master phases.
- **Adding more unique equipment** (beyond ~25) — diminishing returns. Hesha's starting pool of 7 blood + action economy caps the bleed size anyway.

## Related rulings

- [[wiki/rulings/bleed|bleed]] — base bleed action; +bleed modifiers.
- [[wiki/rulings/equip|equip]] — equip action profile; Pier 13 exception for unblockable equip.
- [[wiki/rulings/block-resolution|block-resolution]] — who may block, stealth/intercept resolution.
- [[wiki/mechanics-index/burn-equipment-to-prevent-block|burn-equipment-to-prevent-block]] — index that covers Concoction of Vitality + Flaming Candle.
- [[wiki/entities/clans/ministry|ministry]] — clan context.
- [[wiki/entities/sects/anarch|anarch]] — sect context for Hesha's trigger.

## Sources

- src-004 — Codex of the Damned — *Hesha's Emporium* archetype page (includes canonical decklist JSON in `<meta property="decklist">`). Captured 2026-04-18.
