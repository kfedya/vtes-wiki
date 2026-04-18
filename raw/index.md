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

## src-009 — Codex of the Damned: Govern Resistance (top-tier archetype + decklist)
- type: deck-list
- date: 2024-06-22
- author_or_channel: Codex of the Damned (editorial) / Bill Troxel (deck player, NAC 2024, TWDA id 11496)
- topic: Tzimisce Anarch Baron toolbox — Govern the Unaligned × 12 oldest-first influence discount + bleed; Organized Resistance × 7 Anarch intercept wall; Deflection × 4 + Bait and Switch × 4 bounce; Delaying Tactics × 3 anti-vote; Conditioning × 4 DOM bleed amp; Deep Song × 3 rush/lock; Earth Meld × 9 + Form of Mist × 7 Protean combat bail; Earth Control × 4 stealth; Eat the Rich × 2 political pool hit. Variants: Claws (Donnybrook + Claws of the Dead), Tap'n Bleed (more Deep Song + Invigorate). Close cousin of Gangrel Thing (Dominate focus vs naked-bleed).
- url: https://codex-of-the-damned.org/en/archetypes/top-tier/govern-resistance.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/govern-resistance.md
  - wiki/entities/clans/tzimisce.md
  - wiki/entities/sects/anarch.md
  - wiki/index.md
  - wiki/log.md

## src-010 — Codex of the Damned: Living Museum (top-tier archetype + decklist)
- type: deck-list
- date: 2025-03-10
- author_or_channel: Codex of the Damned (editorial) / Keith Lim (deck player, 2024 AU/NZ Championship, TWDA id 11686); archetype invented by Darby Keeney ("Darby dance")
- topic: Tzimisce stealth-and-bleed — Living Manse × 7 (VIC equipment-location, +1 bleed, burn-to-end-combat) + The British Museum, London × 5 (after successful non-electronic/non-vehicle/non-weapon equip, the acting minion may unlock once per turn) chain-equip unlock engine. Govern the Unaligned × 8 crypt ramp; Conditioning × 2 DOM amp; Deflection × 6 DOM bounce + Bait and Switch × 4 + Guard Dogs × 4 retainer intercept (J. S. Simmons, Tasha Morgan); Heart of Nizchetus × 2 smoothing; Heidelberg Castle equipment-move double-dip; NRA PAC × 1 end-of-turn re-unlock ("Darby dance"). Combat bail Earth Meld × 4 / Form of Mist × 4 / Obedient Flesh × 2. Variants: Darby Keeney latest (Dominate Kine, Cooler, Palatial Estate, Powerbase: Savannah).
- url: https://codex-of-the-damned.org/en/archetypes/top-tier/living-museum.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/living-museum.md
  - wiki/entities/clans/tzimisce.md
  - wiki/index.md
  - wiki/log.md

## src-011 — Codex of the Damned: Lutz Politics (top-tier archetype + decklist)
- type: deck-list
- date: 2023-06-24
- author_or_channel: Codex of the Damned (editorial) / Kelly Schultz (deck player, NAC 2023, TWDA id 10735)
- topic: Camarilla stealth-vote + political-bleed — multi-clan crypt Lutz von Hohenzollern × 3 (Inner Circle, 3 votes) + Undele × 3 (Malkavian Justicar, 3 votes) + Dmitra Ilyanova × 2 (Brujah Justicar, 3 votes). Zillah's Valley × 5 influence ramp; Minion Tap × 7 legacy bloat + Voter Captivation × 8 vote-bonus-+-pool. Perfect Paragon × 6 + Elder Impersonation × 3 + Bewitching Oration × 2 + Awe × 2 vote stack. Referendum chain: Kine Resources Contested × 6 + Banishment × 3 + Conservative Agitation × 3 + singletons (Political Stranglehold, Ancient Influence, Ancilla Empowerment, Reins of Power, Anarchist Uprising, Honor the Elders, Neonate Breach, Disputed Territory). Stealth for undirected politics: Lost in Crowds × 5 + Forgotten Labyrinth × 3 + Faceless Night × 1. Defence = only Force of Personality × 6. Variants: Auspex (Johnson Gonçalves), Protected Resources (Teemu Sainomaa / Michael Holmström), Petra (Jens Johansson), Maris Lutz (Danilo Torrisi 2016 EC), Helicopter (Fabien Garcia 2014 EC FCQ), AD&D (Otso Saariluoma 2010).
- url: https://codex-of-the-damned.org/en/archetypes/top-tier/lutz-politics.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/lutz-politics.md
  - wiki/entities/sects/camarilla.md
  - wiki/index.md
  - wiki/log.md

## src-012 — Codex of the Damned: Malk' 22 (top-tier archetype + decklist)
- type: deck-list
- date: 2023-03-25
- author_or_channel: Codex of the Damned (editorial) / Arnau Diez Sans (deck player, Nacional VTES España 2023 Sevilla, TWDA id 10419)
- topic: V5 Malkavian stealth-and-bleed (modern descendant of Malk' 94) — Camarilla, DOM/OBF, zero combat cards. Govern the Unaligned × 17 ramp phase (get 4 vampires out); attack phase pure bleed (Conditioning × 7 DOM +1 bleed, Seduction × 4 DOM own-blood bleed, Bonding × 3); 30 stealth modifiers (Spying Mission × 7, Lost in Crowds × 5, Cloak the Gathering × 4, Elder Impersonation × 4, Faceless Night × 3, Swallowed by the Night × 3). Block-denial (Hide the Mind × 3, Misdirection Master, Pentex™ Subversion). Defence: Deflection × 6 + Delaying Tactics × 2 + On the Qui Vive × 3 + singletons (My Enemy's Enemy, Telepathic Misdirection). Bloat-disruption: Wash × 3 "masked bleed". Event: The Bitter and Sweet Story.
- url: https://codex-of-the-damned.org/en/archetypes/top-tier/malk-22.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/malk-22.md
  - wiki/entities/clans/malkavian.md
  - wiki/index.md
  - wiki/log.md

## src-013 — Codex of the Damned: Mistress (top-tier archetype + decklist)
- type: deck-list
- date: 2023-10-14
- author_or_channel: Codex of the Damned (editorial) / Otso Saariluoma (deck player, EC 2023 Day 1, TWDA id 10909)
- topic: Tremere-led Camarilla vote & bleed — Mistress Fanchon × 3 (Tremere Inner Circle) + Orlando Oriundus × 2 (Lasombra Prince) + Gabrielle di Righetti × 2 + fillers. Signature combo: Fanchon's ability puts Alastor with Helicopter on a Red-List vampire for 1 pool; Magic of the Smith × 2 fetches Helicopter. 32-master pile for slow economy (Villein × 7, Ashur Tablets × 6, Zillah's Valley × 3, Parthenon × 3, Information Highway × 2, Dreams × 2). Payload Parity Shift × 3 + Banishment × 3 + singletons (Political Stranglehold, Ancient Influence, Ancilla Empowerment, Reins of Power, Anarchist Uprising, Rumors of Gehenna). Stealth/redirect: Mirror Walk × 6 (THA), Forgotten Labyrinth × 2. Defence: Obedience × 4 (OBT) + Deflection × 4 + Eyes of Argus × 3 + singletons. Event: Scourge of the Enochians × 1 anti-breed. Enkil Cog × 1 unique equipment action-doubler. Variants: Malgorzata (stealth + VIC agg), Possession (Might of the Camarilla accelerator), A&B (more Helicopter/Obedience).
- url: https://codex-of-the-damned.org/en/archetypes/top-tier/mistress.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/mistress.md
  - wiki/entities/clans/tremere.md
  - wiki/entities/sects/camarilla.md
  - wiki/index.md
  - wiki/log.md

## src-014 — Codex of the Damned: Nephandii (top-tier archetype + decklist)
- type: deck-list
- date: 2024-11-09
- author_or_channel: Codex of the Damned (editorial) / Tomasz Kloczko (deck player, English NC 2024, TWDA id 11521)
- topic: Sabbat allies-swarm — Antonio d'Erlette × 6 (Tremere antitribu cap-5 G4) Sabbat-gated ability: use 4 transfers to put a Mage ally from library/hand in play. Library: Nephandus × 10 (Mage ally, 2 life, 1 bleed, strike 1R + 1 press) + Target Vitals × 8 combat rider; Liquidation × 4 crypt-burn pool gain + Ashur Tablets × 9 rebuild + Parthenon × 4 tap + Shard × 2 cost reduction + Dreams × 3; Mirror Walk × 4 THA stealth for allies; Deflection × 7 bleed defence + Delaying Tactics × 2 anti-vote + On the Qui Vive × 4 wake; The Unmasking × 3 + FBI SAD × 1 events; Secure Haven × 2 protects Antonio; Tupdog × 3 crypt blockers/decoy; Carlton Van Wyk anti-diablerie. Variants: Darby Keeney streamlined, Martin Weinmayer Bounce (Auspex).
- url: https://codex-of-the-damned.org/en/archetypes/top-tier/nephandii.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/nephandii.md
  - wiki/entities/clans/tremere-antitribu.md
  - wiki/entities/sects/sabbat.md
  - wiki/index.md
  - wiki/log.md

## src-015 — Codex of the Damned: Princess Toolbox (top-tier archetype + decklist)
- type: deck-list
- date: 2023-07-02
- author_or_channel: Codex of the Damned (editorial) / Marius Iscru (deck player, Swiss NC 2023, TWDA id 10550)
- topic: Tremere Camarilla intercept-wall toolbox — Carna, The Princess Witch × 4 (cap 8, AUS/DOM/THA triple) as host for the densest reaction suite in top-tier play (39 reaction cards: Deflection × 8 + Eyes of Argus × 8 + Enhanced Senses × 4 + Eagle's Sight × 4 + Telepathic Misdirection × 4 + On the Qui Vive × 3 + Forced Awakening × 3 + Delaying Tactics × 3 + My Enemy's Enemy × 2). Magic of the Smith × 6 equipment tutor (Heart of Nizchetus × 2 filter; Sniper Rifle × 2 / .44 Magnum × 2 grind; Ivory Bow, Kevlar Vest, Sawed-Off Shotgun, Sport Bike, Bowl of Convergence). Vessel × 6 + The Rack × 2 + Smiling Jack × 3 bloat/tax. Theft of Vitae × 4 + Rego Motum × 4 ranged combat. Conditioning × 2 + Anonymous Freight × 2 soft finisher. Variants: Toolbox + Govern, Royalty, Infernal (Valerius), V5, Oliver (Thrace anti-Form-of-Mist).
- url: https://codex-of-the-damned.org/en/archetypes/top-tier/princess-toolbox.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/princess-toolbox.md
  - wiki/entities/clans/tremere.md
  - wiki/entities/sects/camarilla.md
  - wiki/index.md
  - wiki/log.md

## src-016 — Codex of the Damned: Ravnos Bonds (top-tier archetype + decklist)
- type: deck-list
- date: 2024-09-28
- author_or_channel: Codex of the Damned (editorial) / Simone Parmeggiani (deck player, EC 2024 Day 1, TWDA id 11668)
- topic: V5 Ravnos Anarch stealth-and-bleed — Break the Bonds × 16 (CHI action: bleed + recruit another Ravnos from hand on success). Crypt wide pool of G6 Ravnos (Sreelekha × 2, Roberto Rivamonte × 2, Gathii × 2, + 6 singletons). Stealth: Memory Rift × 10 (OBF/AUS, doesn't clog hand) + Lost in Crowds × 3 + Faceless Night × 3 + Elder Impersonation × 4 + Spying Mission × 4 + Veil the Legions × 3 + True Love's Face × 2. Bleed amp: Visions of Gehenna × 8 (CHI +1 bleed) + Power of One × 4 (POT splash) + Public Trust × 4 (PRE). Wave finisher: Week of Nightmares × 2 + Club Illusion. Economy: Dabbler × 4 triple-discipline reward (CHI/OBF/PRE). Defence: Visions of Zapathasura × 5 is the ONLY bleed-defence; Delaying Tactics × 2 anti-vote; Narrow Minds event; Wash × 2 anti-intercept-location. Zero combat cards.
- url: https://codex-of-the-damned.org/en/archetypes/top-tier/ravnos-bonds.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/ravnos-bonds.md
  - wiki/entities/clans/ravnos.md
  - wiki/entities/sects/anarch.md
  - wiki/index.md
  - wiki/log.md

## src-017 — Codex of the Damned: Stanislava (top-tier archetype + decklist)
- type: deck-list
- date: 2023-11-25
- author_or_channel: Codex of the Damned (editorial) / Mikey Ferguson (deck player, UK NC 2023, TWDA id 10998); classic archetype piloted through 2010s by Martin Weinmayer
- topic: Camarilla Gangrel-led stealth-vote/bleed — Stanislava × 5 (G2 cap 11 Inner Circle, +2 bleed printed, allies cannot block her, retainers lose abilities vs her in combat) flagship; supporting crypt Hartmut Stover × 2, Xaviar (ADV) × 2, Ingrid Rossler × 2, Mark Decker. Zillah's Valley × 8 + Villein × 6 + Govern × 6 ramp. Political stack: Kine Resources Contested × 6 + 6 singleton finishers (Anarchist Uprising, Ancient Influence, Ancilla Empowerment, Banishment, Political Stranglehold, Reins of Power). Stealth via Protean: Earth Control × 6, Forced March × 3, Instantaneous Transformation × 3, Rapid Change × 2, Scouting Mission × 3. Defence: Deflection × 6 + Second Tradition: Domain × 2 + On the Qui Vive × 2. Protean combat bail Form of Mist × 7 + Earth Meld × 5. Freak Drive × 3 ANI post-action unlock. Enkil Cog action-doubler. Variants: Classic (Martin Weinmayer), Iliana/Caitlin crypt alts, Ashur (Ashur Tablets + Parthenon + Liquidation post-2024 balance).
- url: https://codex-of-the-damned.org/en/archetypes/top-tier/stanislava.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/stanislava.md
  - wiki/entities/clans/gangrel.md
  - wiki/entities/sects/camarilla.md
  - wiki/index.md
  - wiki/log.md

## src-018 — Codex of the Damned: The unnamed (top-tier archetype + decklist)
- type: deck-list
- date: 2024-06-21
- author_or_channel: Codex of the Damned (editorial) / Darby Keeney (deck player, Origins Friday 2 2024, TWDA id 11442)
- topic: Baali Independent stealth-and-bleed / bloat — The unnamed × 5 (G6 cap 10 Infernal: +2 pool after successful bleed) flagship; support crypt The Horde × 3 (non-unique cap-3, lock to give infernal +1 bleed — bypasses bleed-reducers like POB/Visions of Zapathasura) + Xeper, Sultan of Lepers × 2 (+1 vote per ready infernal; steal allies) + Annazir, Arishat. Engine: Enkil Cog × 3 (double action) + Homunculus × 3 (retainer +1 bleed) + Flurry of Action × 6 unlock chain + Instantaneous Transformation × 6 stealth/action. Bloat Tend the Flock × 6 flex (1 pool + influence OR 4 pool). Stealth OBF (Swallowed by the Night × 5, Lost in Crowds × 2, Faceless Night × 2, Elder Impersonation × 2) + I am Legion × 3 (DAI/OBF bounce-cancel + pool). Finisher Unleash Hell's Fury × 3 (DAI/PRE +1 bleed + mode). Infernal allies: Infernal Servitor × 3, Veneficti, Mylan Horseed, D'habi Revenant retainer. Defence: Eluding the Arms of Morpheus × 4, Majesty × 3, Form of the Bat × 2, Sense the Sin × 2. Variants: Anarch (Platinum Protocol hybrid — Lukáš Simandl Austrian Open), Hell Rising, Maleficia, Coven-focused.
- url: https://codex-of-the-damned.org/en/archetypes/top-tier/the-unnamed.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/the-unnamed.md
  - wiki/entities/clans/baali.md
  - wiki/entities/sects/independent.md
  - wiki/index.md
  - wiki/log.md

## src-019 — Codex of the Damned: Tupdogs (top-tier archetype + decklist)
- type: deck-list
- date: 2023-12-09
- author_or_channel: Codex of the Damned (editorial) / Danilo Torrisi (deck player, GP Milan Season 2024, TWDA id 10853)
- topic: Sabbat rush — Tupdog × 21 (cap-1 non-unique Gargoyle Tremere-antitribu-slave; each burns end-of-minion-phase) as disposable rush minions enabled by Tremere antitribu hosts (Antonio d'Erlette, Esoara, Janine, Mosfair, Ember Wright, Keith Moody, Saiz × 1 each). Combat pile 37 cards: Immortal Grapple × 10 + Raking Talons × 9 + Brick by Brick × 8 + Disarm × 6 + Roundhouse × 4. Rock Cat × 10 (cap-4 ally, 3 life 2 strength, ends combat on press) supplementary threats. Graverobbing × 8 (Sabbat action) steals prey's torpored vampires. Autarkis Persecution × 8 political pool-damage/gain. Ashur Tablets × 6 + Info Highway × 3 + Dreams × 3 economy. Deflection × 6 + As the Crow × 6 (ANI bypass of block restrictions for Rock Cat) + Secure Haven + Fame defence. Closes Batch B (11 Top Tier archetypes).
- url: https://codex-of-the-damned.org/en/archetypes/top-tier/tupdogs.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/tupdogs.md
  - wiki/entities/clans/gargoyle.md
  - wiki/entities/clans/tremere-antitribu.md
  - wiki/entities/sects/sabbat.md
  - wiki/index.md
  - wiki/log.md

## src-020 — Codex of the Damned: Capuchin Toolbox (runner-up archetype + decklist)
- type: deck-list
- date: 2025-01-19
- author_or_channel: Codex of the Damned (editorial) / Richard Stefan Utner (deck player, Hungarian NC LC Prep 2025, TWDA id 11991); recent archetype creation, 3 tournament wins to date
- topic: Multi-clan endurance toolbox — The Capuchin × 5 (Harbinger of Skulls G5 cap 11) + Abraham Mellon × 4 (Malkavian G6 cap 8) + Gerald Windham × 3 (Tremere G5 cap 9), all sharing AUS/DOM. Extreme bleed defence (10 bounces: Deflection × 4 + Telepathic Misdirection × 2 + My Enemy's Enemy × 2 + Murmur of the False Will × 2). Heavy intercept (11: Eyes of Argus × 9 + Eagle's Sight × 2). Bleed amp: Bonding × 5 + Under My Skin × 5 + Crocodile's Tongue × 2 penalise blockers. Freak Drive × 4 post-action unlock. Unflinching Persistence × 7 + Theft of Vitae × 4 combat. Hand regularly exceeds 10 cards due to Dreams × 2 + Auspex cycle.
- url: https://codex-of-the-damned.org/en/archetypes/runner-ups/capuchin-toolbox.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/capuchin-toolbox.md
  - wiki/entities/clans/harbinger-of-skulls.md
  - wiki/index.md
  - wiki/log.md

## src-021 — Codex of the Damned: Dementation Bleed (runner-up archetype + decklist)
- type: deck-list
- date: 2024-07-07
- author_or_channel: Codex of the Damned (editorial) / Jonathan da Silva Goudard (deck player, Eternal Vigilance I, TWDA id 11567)
- topic: Malkavian antitribu stealth-and-bleed — Sabbat, DEM/OBF/AUS. Core: Kindred Spirits × 15 (DEM action: bleed + stealth). Bleed amp: Confusion × 8 (DEM), Eyes of Chaos × 8 (DEM). Stealth stack: Cloak the Gathering × 5 + Elder Impersonation × 6 + Faceless Night × 4 + Lost in Crowds × 4 + Spying Mission × 2 + Swallowed by the Night × 2. Defence: Telepathic Misdirection × 10 (AUS bounce — 2/3 crypt has AUS), Eyes of Argus × 4 + On the Qui Vive × 4 + My Enemy's Enemy × 2. Coma × 4 combat deterrent. Wide crypt (Rodolfo/Morel/Midget × 2 each + Persephone/Colonel/Uncle George/Jackie/Marta/Cassandra × 1). Variants: Alessandro Donati 2022 Italian NC lower-cap DEM-only, Louhi-focused.
- url: https://codex-of-the-damned.org/en/archetypes/runner-ups/dementation-bleed.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/dementation-bleed.md
  - wiki/entities/clans/malkavian-antitribu.md
  - wiki/entities/sects/sabbat.md
  - wiki/index.md
  - wiki/log.md

## src-022 — Codex of the Damned: Forced Ball (runner-up archetype + decklist)
- type: deck-list
- date: 2025-01-11
- author_or_channel: Codex of the Damned (editorial) / Filippo Tomov (deck player, Italian Tour Trento 2025, TWDA id 11913)
- topic: Toreador Camarilla political/vote — Toreador Grand Ball × 7 (Master: host unblockable on political actions) primary defence in lieu of stealth. Diana Iadanza × 3 (ability bypasses Delaying Tactics). FOR-based Toreador crypt (Catalina Vega × 2, Flávio Gonçalves × 2, Mkhokheli × 2, + singletons) enables Forced March × 4 action-chain. Referendum chain: Kine Resources Contested × 6 + Parity Shift × 4 + Conservative Agitation × 2 + Consanguineous Boon × 2 + Camarilla's Iron Fist × 2 + Banishment + Anarchist Uprising. Vote-amp: Voter Captivation × 5 + Perfect Paragon × 4 + Scalpel Tongue × 4 + Bewitching Oration × 3 + Awe × 2. Bloat: Villein × 6 + Ashur Tablets × 6 + Parthenon × 2 + Protected Resources × 2 + Art Museum + Papillon. Defence: Telepathic Misdirection × 6 + Second Tradition: Domain × 2 + Majesty × 6. Sargon Fragment + Heart of Nizchetus.
- url: https://codex-of-the-damned.org/en/archetypes/runner-ups/forced-ball.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/forced-ball.md
  - wiki/entities/clans/toreador.md
  - wiki/entities/sects/camarilla.md
  - wiki/index.md
  - wiki/log.md

## src-023 — Codex of the Damned: Infernal Barons (runner-up archetype + decklist)
- type: deck-list
- date: 2021-11-06
- author_or_channel: Codex of the Damned (editorial) / Ke Carlton (deck player, AUSNZ Continental 2022, TWDA id 10276)
- topic: Anarch Baali/Ministry vote — Arishat × 4 (Baali Baron Infernal) + Xeper × 2 (Baali +1 vote per infernal) + Ministry splash (Vivian VI × 2) + Elisha Tucker × 2 + Jacques Rouge + Atiena. Core: Condemnation: Mute × 5 strip opposing vote capacity, Kine Resources Contested × 11 referendum chain, Reckless Agitation × 3, Eat the Rich × 3, Anarchist Uprising, Ancilla Empowerment. Vote amp: Voter Captivation × 4 + Bewitching Oration × 2 + Monkey Wrench × 2. Stealth: Forgotten Labyrinth × 5 + Lost in Crowds × 5 + Faceless Night × 2. Bloat: Villein × 6 + Info Highway × 3 + Wider View × 2 + Garibaldi-Meucci Museum × 2. Defence Bait and Switch × 4 + Organized Resistance × 2 + Majesty × 4. Utility: Unleash Hell's Fury × 3. Variants: no-Xeper (Entrancement sub), Dominica (rush defence swap).
- url: https://codex-of-the-damned.org/en/archetypes/runner-ups/infernal-barons.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/infernal-barons.md
  - wiki/entities/clans/baali.md
  - wiki/entities/sects/anarch.md
  - wiki/index.md
  - wiki/log.md

## src-024 — Codex of the Damned: Lasombra Nocturn (runner-up archetype + decklist)
- type: deck-list
- date: 2023-11-26
- author_or_channel: Codex of the Damned (editorial) / Eduardo García (deck player, Mexican NC 2023, TWDA id 11066)
- topic: Lasombra stealth-and-bleed — Govern × 12 ramp; Nocturn × 12 OBL ally (dual-purpose: boost bleed or protect from combat); DOM bleed amp (Conditioning × 4 + Empowering the Puppet King × 4 + Command of the Beast × 4 + Foreshadowing Destruction × 2); OBL stealth (Shadow Play × 6 + Shroud of Absence × 4 + Tenebrous Form × 2); Deflection × 8 DOM bounce + On the Qui Vive × 6 + Redirection × 2 OBL redirect + Pulling Strings + Delaying Tactics; combat Oubliette × 4 + Entombment × 2 + Shadow Body × 2; Vessel × 2 + Blood Doll × 2 + Path of Night × 2 economy. Can deliver 7-damage bleeds by prioritising bleed amp over stealth volume. Variants: Brutal (Arms of the Abyss + Entombment), Black Hand (G3/G4 support), Kiasyd (related Lasombra-Fae bloodline).
- url: https://codex-of-the-damned.org/en/archetypes/runner-ups/lasombra-nocturn.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/lasombra-nocturn.md
  - wiki/entities/clans/lasombra.md
  - wiki/index.md
  - wiki/log.md

## src-025 — Codex of the Damned: Protean Barons (runner-up archetype + decklist)
- type: deck-list
- date: 2024-10-19
- author_or_channel: Codex of the Damned (editorial) / Vincent Ripoll — Ankha, current VEKN Rules Director (deck player, French NC 2024, TWDA id 11754)
- topic: Multi-clan Anarch Baron toolbox — wide 1-of Anarch Baron crypt (Gangrel/Ministry/Tzimisce/Ravnos/Brujah mix). Protean × 6 (Master: grants `[pro]` inferior to bearer) lets any Baron access Earth Meld × 8 + Earth Control × 4 + Form of the Bat × 4 + Donnybrook × 6 aggravated. Childe of the Revolution × 8 swarm-growth. 16-copy Organized Resistance wall + Bait and Switch × 6 + Protection Racket × 2. Bloat Villein × 6 + Anarch package (Anarch Free Press, Carfax Abbey × 2, Papillon, Garibaldi-Meucci Museum × 2). Light votes: Revolutionary Council, Eat the Rich, Constant Revolution. Closes Runner-up batch. Variants: Simo Tiippana original, Tommi Hakomaa Death Star (Ashur + Form of Mist + Revolutionary Council), Diego Rodrigues Rush (Bum's Rush + Open War).
- url: https://codex-of-the-damned.org/en/archetypes/runner-ups/protean-barons.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/protean-barons.md
  - wiki/entities/sects/anarch.md
  - wiki/index.md
  - wiki/log.md

## src-026 — Codex of the Damned: Baron Debate (new-kid archetype + decklist)
- type: deck-list
- date: 2024-09-24
- author_or_channel: Codex of the Damned (editorial) / Jorge Delgado (deck player, Week of Nightmares 2024 Day 1, TWDA id 11663)
- topic: Brujah Anarch Baron wall — Brujah Debate × 8 Master stacks on the highest-cap Baron (Aline Gädeke × 2 key vampire) for strength/maneuvers, but locks the Debate host during the stack. Crypt: Aline Gädeke × 2 + Valeriya Zinovieva × 2 + Atiena × 2 + Leumeah × 2 + singletons. Childe of the Revolution × 4 swarm; Constant Revolution × 4 naked-bleed amp; Open War × 1 game-changer. 18-copy Organized Resistance wall + Bait and Switch × 4 + On the Qui Vive × 2 + Protection Racket × 2. Combat Dust Up × 6 + Immortal Grapple × 4 + Taste of Vitae × 4. Bloat Villein × 4 + Smiling Jack × 2 + Parthenon × 2 + Anarch package. The Parthenon × 2 + Rumors of Gehenna × 1 pile Brujah Debate faster via multi-master-phase actions. Fresh archetype — few winners yet.
- url: https://codex-of-the-damned.org/en/archetypes/new-kids/baron-debate.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/baron-debate.md
  - wiki/entities/clans/brujah.md
  - wiki/entities/sects/anarch.md
  - wiki/index.md
  - wiki/log.md

## src-027 — Codex of the Damned: Kalinda (new-kid archetype + decklist)
- type: deck-list
- date: 2025-01-12
- author_or_channel: Codex of the Damned (editorial) / Bram Van Stappen (deck player, New Years Blood 2025, TWDA id 11997)
- topic: Banu Haqim Camarilla stealth-and-bleed — Kalinda (G6) × 4 ability bleed-then-unlock; Protected District × 7 defensive block-reaction; Haqim's Law: Retribution × 6 Master (discard combat card for +1 bleed). OBF stealth: Lost in Crowds × 7 + Faceless Night × 3 + Cloak the Gathering × 2 + Elder Impersonation × 2 + Spying Mission × 2 + Domain of Evernight. Swallowed by the Night × 9 + Resist Earth's Grasp × 2 dual stealth/combat-feed for Retribution. Combat Hunger of Marduk × 5 + Pursuit × 4 + Infernal Pursuit × 2. Political: Camarilla's Iron Fist × 3 + Banu Haqim Justicar. Economy: Villein × 4 + Ashur Tablets × 6 + Wider View × 2 + Alamut + Coven. Metagame angle: looks like Haqim Royalty so opponents fear combat. Variants: more Alamut, Web of Knives Recruit splash.
- url: https://codex-of-the-damned.org/en/archetypes/new-kids/kalinda.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/kalinda.md
  - wiki/entities/clans/banu-haqim.md
  - wiki/entities/sects/camarilla.md
  - wiki/index.md
  - wiki/log.md

## src-028 — Codex of the Damned: Malkarishat (new-kid archetype + decklist)
- type: deck-list
- date: 2024-09-29
- author_or_channel: Codex of the Damned (editorial) / Danilo Torrisi (deck player, EC 2024 Day 2, TWDA id 11669)
- topic: Malkavian Justicar + Baali Baron vote hybrid — portmanteau of Malkavian + Arishat. Juliet Parr × 4 (G7 Camarilla Malkavian Justicar, cap 9, 3 votes, post-pass +2 hand size, 1 optional maneuver/combat) + Arishat × 4 (Baali Baron Infernal polling-abstention). Support: Alexander Silverson × 2 + Gilbert Duane G6 + Andi Liu. Govern × 8 ramp. Referendum chain: Kine Resources Contested × 6 + Parity Shift × 6 + My Kin Against the World × 2 + Anarchist Uprising + Ancilla Empowerment. Vote-strip: Condemnation: Mute × 4 + Unleash Hell's Fury × 2. Stealth for undirected politics: Forgotten Labyrinth × 7 + Lost in Crowds × 7 + Elder Impersonation × 2. Defence: Deflection × 8 + Obedience × 6 (no wake effects — proactive unlock management). Economy: Ashur Tablets × 6 + Villein × 2 + Dreams × 2 + Info Highway × 2 + Wider View × 2.
- url: https://codex-of-the-damned.org/en/archetypes/new-kids/malkarishat.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/malkarishat.md
  - wiki/entities/clans/malkavian.md
  - wiki/entities/clans/baali.md
  - wiki/index.md
  - wiki/log.md

## src-029 — Codex of the Damned: Piper War Ghoul '24 (new-kid archetype + decklist)
- type: deck-list
- date: 2024-09-15
- author_or_channel: Codex of the Damned (editorial) / Alessandro Donati (deck player, Italian Tour Bologna 2024, TWDA id 11590)
- topic: Tzimisce Anarch rush / ally-combat — Piper × 7 (Master enables low-cap Tzimisce to recruit War Ghoul) + Jake Washington × 7 (Master ally fodder) + War Ghoul × 6 primary threat; big allies Ossian, Vozhd of Sofia, Asanbonsam Ghoul, Carlton Van Wyk, Vagabond Mystic. Retainer pack: J.S. Simmons + Jackie Therman + Mr. Winthrop + Tasha Morgan. Crypt low-cap Tzimisce + Anarch Convert (Susie Kano × 3 + Marialena × 2 + singletons). Combat Donnybrook × 3 + Trap × 3 + Fake Out × 2. Defence Deflection × 6 + Deep Ecology × 3 + On the Qui Vive × 3 + One With the Land × 3 (scales to 4 intercept). Events Dragonbound + The Unmasking × 2. 60-card library — unusually small.
- url: https://codex-of-the-damned.org/en/archetypes/new-kids/piper-war-ghoul-24.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/piper-war-ghoul-24.md
  - wiki/entities/clans/tzimisce.md
  - wiki/entities/sects/anarch.md
  - wiki/index.md
  - wiki/log.md

## src-030 — Codex of the Damned: Salubri Powerbleed (new-kid archetype + decklist)
- type: deck-list
- date: 2024-03-02
- author_or_channel: Codex of the Damned (editorial) / Pasi Karjalainen (deck player, Fee Stake: Jyväskylä 4 2024, TWDA id 11271)
- topic: V5 Salubri Camarilla powerbleed — crypt Abaddon × 2 + Seraphina × 2 + Ilonka × 2 + Aniel × 2 + Malachi × 2 + Opikun + Yael. Core: Feast of the Soul's Secrets × 6 (DOM powerbleed action) + Govern × 5 + Scouting Mission × 4. Block-denial stack: Seduction × 6 + Forced Confessional × 6 + Misdirection × 2 + Pentex × 2 + Anarch Troublemaker × 2 + Unleashing the Bestial Soul × 2 (beats wake-and-bounce). Freak Drive × 5 (ANI) action-chain via Salubri Fortitude. Bonding × 3 + Conditioning × 2 + Threats × 2 bleed amp. Defence Deflection × 4 + Eyes of Argus × 3 + Murmur of the False Will × 2 + singletons. FOR combat wall Rolling with the Punches × 4 + Indomitability × 3 + Hidden Strength × 3. Saulot's Guiding Wisdom, Sight Beyond Sight, Meditative Grove. Noted as achievement in competitive Finnish meta.
- url: https://codex-of-the-damned.org/en/archetypes/new-kids/salubri-powerbleed.html
- added: 2026-04-18
- pages_touched:
  - wiki/archetypes/salubri-powerbleed.md
  - wiki/entities/clans/salubri.md
  - wiki/entities/sects/camarilla.md
  - wiki/index.md
  - wiki/log.md

### Personal notes
