# Raw Sources Index

Catalogue of source documents stored in `raw/`. This file is the source of truth for source IDs. LLM reads; user and LLM both write entries here during ingest.

## Conventions

- Every source gets a three-digit ID: `src-001`, `src-002`, …
- IDs are monotonically increasing across the whole `raw/` tree (not per-subdirectory).
- Files in `raw/` are named `NNN-slug.ext` where `NNN` matches the ID.
- Entries in this file are grouped by category, ordered by ID within a category.

## Entry template

```
## src-NNN — <short title>
- type: rulebook | ruling | krcg-snapshot | article | forum-thread | video-transcript | discord-export | deck-list | personal-note
- date: YYYY-MM-DD (source publication or capture date)
- author_or_channel: <who/where>
- topic: <one-line description>
- url: <source URL if applicable>
- added: YYYY-MM-DD (date added to this wiki)
- pages_touched: [wiki/path/to/page.md, …]
```

## Sources

### Rulebooks

## src-001 — VTES Fifth Edition Rulebook (EN)
- type: rulebook
- date: 2023-10-01
- author_or_channel: Black Chantry Productions
- topic: Official Fifth Edition rulebook v1.1 — components, card types, turn sequence, sects, glossary, FAQ/rulings, quick reference. 56 pages.
- url: https://blackchantry.com/Vampire%20The%20Eternal%20Struggle%20Fifth%20Edition%20rulebook%20ENG.pdf
- added: 2026-04-17
- pages_touched:
  - wiki/rulings/game-overview.md
  - wiki/rulings/unlock-phase.md
  - wiki/rulings/master-phase.md
  - wiki/rulings/minion-phase.md
  - wiki/rulings/influence-phase.md
  - wiki/rulings/discard-phase.md
  - wiki/rulings/bleed.md
  - wiki/rulings/hunt.md
  - wiki/rulings/equip.md
  - wiki/rulings/employ-retainer.md
  - wiki/rulings/recruit-ally.md
  - wiki/rulings/leave-torpor.md
  - wiki/rulings/rescue-from-torpor.md
  - wiki/rulings/diablerise-action.md
  - wiki/rulings/become-anarch.md
  - wiki/rulings/block-resolution.md
  - wiki/rulings/politics.md
  - wiki/rulings/political-action.md
  - wiki/rulings/referendum.md
  - wiki/rulings/voting.md
  - wiki/rulings/combat.md
  - wiki/rulings/maneuver.md
  - wiki/rulings/strike.md
  - wiki/rulings/strike-effects.md
  - wiki/rulings/damage-resolution.md
  - wiki/rulings/press.md
  - wiki/rulings/torpor.md
  - wiki/rulings/diablerie.md
  - wiki/rulings/blood-hunt.md
  - wiki/rulings/ending-the-game.md
  - wiki/rulings/withdraw.md
  - wiki/rulings/traits.md
  - wiki/entities/card-types/crypt.md
  - wiki/entities/card-types/library.md
  - wiki/entities/card-types/master.md
  - wiki/entities/card-types/action.md
  - wiki/entities/card-types/action-modifier.md
  - wiki/entities/card-types/reaction.md
  - wiki/entities/card-types/combat-card.md
  - wiki/entities/card-types/political-action-card.md
  - wiki/entities/card-types/ally.md
  - wiki/entities/card-types/retainer.md
  - wiki/entities/card-types/equipment.md
  - wiki/entities/sects/camarilla.md
  - wiki/entities/sects/sabbat.md
  - wiki/entities/sects/anarch.md
  - wiki/entities/sects/independent.md
  - wiki/entities/sects/laibon.md
  - wiki/rulings/stealth-modifiers.md
  - wiki/rulings/target-redirection.md
  - wiki/rulings/post-combat-effects.md
  - wiki/rulings/hunting-grounds.md
  - wiki/rulings/cards-removed-in-5e.md
  - wiki/cards/pentex-subversion.md
  - wiki/cards/vessel.md
  - wiki/cards/smiling-jack-the-anarch.md
  - wiki/cards/theft-of-vitae.md
  - wiki/meta/backlog.md
  - wiki/lore/wod-glossary.md
  - wiki/rulings/quick-reference.md

### Card databases

## src-002 — krcg vtes.json snapshot 2026-04-18
- type: krcg-snapshot
- date: 2026-04-18
- author_or_channel: krcg.org (Lionel Panhaleux et al.)
- topic: Full VTES card data — names, types, disciplines, costs, card_text, embedded rulings.
- url: https://static.krcg.org/data/vtes.json
- added: 2026-04-18
- pages_touched: [card-db/, CLAUDE.md, wiki/index.md, wiki/log.md, wiki/meta/backlog.md, wiki/rulings/bleed.md, wiki/rulings/combat.md, wiki/cards/theft-of-vitae.md, wiki/rulings/block-resolution.md, wiki/rulings/strike.md, wiki/rulings/strike-effects.md, wiki/rulings/damage-resolution.md, wiki/rulings/referendum.md, wiki/rulings/voting.md, wiki/rulings/diablerie.md, wiki/rulings/torpor.md, wiki/rulings/target-redirection.md, wiki/rulings/stealth-modifiers.md]

### Rulings
### krcg snapshots
### Articles
### Forums

## src-003 — VEKN forum thread: Catatonic Fear and Loving Agony (PIB 20130319)
- type: forum-thread
- date: 2013-03-19
- author_or_channel: vekn.net — wesile (asker), Ankha (Rules Director), Pascal Bertrand (rules coordinator)
- topic: Target Vitals on superior Catatonic Fear / Loving Agony combat-ends strikes adds +2 damage when the rider damage is successfully inflicted; Dawn Operation does not aggravate the after-combat damage; Amaranth cannot be played against a vampire whose death comes from Catatonic Fear (after-combat); general rule: all "Strike: End combat and do X" effects have X happen after combat ends, except untap X.
- url: https://www.vekn.net/forum/rules-questions/46164-catatonic-fear-and-loving-agony
- added: 2026-04-18
- pages_touched:
  - CLAUDE.md
  - wiki/cards/catatonic-fear.md
  - wiki/rulings/strike-effects.md
  - wiki/playgroup/common-mistakes.md
  - wiki/index.md
  - wiki/log.md

### Videos
### Discord
### Decks

## src-004 — Codex of the Damned: Hesha's Emporium (archetype + decklist)
- type: deck-list
- date: 2024-04-17
- author_or_channel: Codex of the Damned (editorial) / Sérgio Louçã Martins (deck player, 2024 Atlantic Cup 3GW13+1 finals 1st seed)
- topic: Hesha Ruhadze (G6) combo powerbleed archetype — Angel Chavarria + Hesha + 27+ unique equipment + Hag's Wrinkles chain; unblockable bleeds (Flaming Candle / Concoction of Vitality / Horrific Countenance) + anti-bounce (Perfect Clarity / I am Legion via Vial/Textbook/Veneficorum/Ritual Goblet) + Nod/Heidelberg equipment transfer.
- url: https://codex-of-the-damned.org/en/archetypes/archive/heshas-emporium.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/heshas-emporium.md
  - wiki/entities/clans/ministry.md
  - wiki/entities/sects/anarch.md
  - wiki/index.md
  - wiki/log.md

## src-005 — Codex of the Damned: Gangrel Thing (top-tier archetype + decklist)
- type: deck-list
- date: 2024-09-27
- author_or_channel: Codex of the Damned (editorial) / Marius Iscru (deck player, 2024 VtES European "Last Chance" Qualifier, TWDA id 11667)
- topic: Gangrel Anarch wall / grind-bleed archetype — 9 Gangrel Anarch Barons, Thing × 5 to fan out 4–6 minions, Organized Resistance × 9 + Deep Ecology × 5 intercept wall, Bait and Switch × 5 bounce, Earth Meld / Form of Mist combat bail, Smiling Jack + Constant Revolution payload, Reckless Agitation / Monkey Wrench lunge; Brutal / Council Propaganda / Renegade variants referenced. Classified by Codex as one of 4 ⭐ "Top Dog" current-meta archetypes.
- url: https://codex-of-the-damned.org/en/archetypes/top-tier/gangrel-thing.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/gangrel-thing.md
  - wiki/entities/clans/gangrel.md
  - wiki/entities/sects/anarch.md
  - wiki/index.md
  - wiki/log.md

## src-006 — Codex of the Damned: Haqim Royalty (top-tier archetype + decklist)
- type: deck-list
- date: 2024-11-03
- author_or_channel: Codex of the Damned (editorial) / Gyula Erdős (deck player, "Beauty challenge" 2024, TWDA id 11674)
- topic: Banu Haqim Camarilla toolbox — Prince/Justicar crypt (Kassandra Tassaki × 3, Kasim Bayar × 2, Oluwafunmilayo × 2) leveraging Second Tradition: Domain × 9 for defence; 38-card THA/CEL combat module (Hunger of Marduk × 9, Pursuit family × 12, Psyche! × 5) doubles as Haqim's Law: Retribution bleed fuel (discard a combat card for +1 bleed). Bloat via Villein × 5, Anathema, Priority Contract × 2. Ashur Tablets × 9 + Infernal Pursuit × 5 rebuild engine. Variants: Biothaumaturgic splash, Alamut/Black Throne politics, Embrace/Progeny swarm. Classified by Codex as one of 4 ⭐ "Top Dog" current-meta archetypes.
- url: https://codex-of-the-damned.org/en/archetypes/top-tier/haqim-royalty.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/haqim-royalty.md
  - wiki/entities/clans/banu-haqim.md
  - wiki/entities/sects/camarilla.md
  - wiki/index.md
  - wiki/log.md

## src-007 — Codex of the Damned: Illegal Brawl (top-tier archetype + decklist)
- type: deck-list
- date: 2024-06-20
- author_or_channel: Codex of the Damned (editorial) / Darby Keeney (deck player, Origins Thursday 2 2024, TWDA id 11440)
- topic: Brujah Anarch Baron toolbox — Illegalism × 9 (Anarch double-threat action: bleed / bleed-at-stealth) + Line Brawl × 10 (POT 3-way-combat action) flex rush↔bleed. Combat package: Immortal Grapple × 6, Dust Up × 9, Target Vitals × 5, Diversion × 4, Bollix × 2, Disarm × 2, Pulled Fangs × 2, Thrown Gate × 4. Power of One × 6 POT stealth-bleed mod. New Carthage × 2 doubles Baron bleed + vote. Bloat Villein × 5 + Blood Doll × 2 + Papillon + Carfax Abbey + Taste of Vitae × 4. Bait and Switch × 6 bounce; Organized Resistance × 2 minimal intercept. Variants: Resistance (max OR + Constant Revolution / Stolen Police Cruiser), Chimerstry splash (Dabbler, stealth-Illegalism), Primogen (Protected District). Classified by Codex as one of 4 ⭐ "Top Dog" current-meta archetypes.
- url: https://codex-of-the-damned.org/en/archetypes/top-tier/illegal-brawl.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/illegal-brawl.md
  - wiki/entities/clans/brujah.md
  - wiki/entities/sects/anarch.md
  - wiki/index.md
  - wiki/log.md

## src-008 — Codex of the Damned: Platinum Revelation (top-tier archetype + decklist)
- type: deck-list
- date: 2023-10-15
- author_or_channel: Codex of the Damned (editorial) / Jonas Ståhle (deck player, EC 2023 Day 2, TWDA id 11032)
- topic: V5 Ministry Anarch stealth-and-bleed — triple-discipline OBF/PRE/PRO build; core is The Platinum Protocol × 10 (Anarch action: +1 stealth + +1 bleed + 1 corruption counter on prey's minion on success). Corruption counters feed Revelation of the Serpent × 7 (bleed amp / counter-burn) and Enchanting Gaze × 4 (permanent block-denial via counter-burn). CrimethInc. × 5 unlocks chained bleeds. Dabbler × 3 Master trifle (blood/unlock after triple-discipline action) out-values Villein in Ministry shell. Defence: Party Out Of Bounds × 2 (triple-mode Anarch reaction), Bait and Switch × 4 bounce, Form of Mist × 4 + Earth Meld × 2 combat, On the Qui Vive × 3. Variants: Apolitical (Kim Nilsson — no Barons, POB-only defence), Political-lunge (Eat The Rich + Reckless Agitation + Propaganda of the Deed), The Unnamed hybrid (Lukáš Simandl, Austrian Open). Classified by Codex as 4th ⭐ "Top Dog" current-meta archetype — closes Batch A.
- url: https://codex-of-the-damned.org/en/archetypes/top-tier/platinum-revelation.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/platinum-revelation.md
  - wiki/entities/clans/ministry.md
  - wiki/entities/sects/anarch.md
  - wiki/index.md
  - wiki/log.md

### Personal notes
