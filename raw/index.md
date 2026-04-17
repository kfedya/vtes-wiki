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

### Rulings
### krcg snapshots
### Articles
### Forums
### Videos
### Discord
### Decks
### Personal notes
