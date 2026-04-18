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
- pages_touched: [card-db/, CLAUDE.md, wiki/index.md, wiki/log.md, wiki/meta/backlog.md, wiki/rulings/bleed.md, wiki/rulings/combat.md, wiki/cards/theft-of-vitae.md, wiki/rulings/block-resolution.md, wiki/rulings/strike.md, wiki/rulings/strike-effects.md, wiki/rulings/damage-resolution.md, wiki/rulings/referendum.md, wiki/rulings/voting.md, wiki/rulings/diablerie.md]

### Rulings
### krcg snapshots
### Articles
### Forums
### Videos
### Discord
### Decks
### Personal notes
