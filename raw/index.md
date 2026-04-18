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

### Personal notes
