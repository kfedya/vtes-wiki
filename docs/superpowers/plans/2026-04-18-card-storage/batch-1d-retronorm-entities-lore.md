# Batch 1d — Retro-normalize card citations: entities, lore, existing card pages

**Goal:** audit card citations on sect/card-type entities, lore, and existing `wiki/cards/` pages; normalize formatting; bump `last_verified`.

**Depends on:** Batch 0.

**Commit subject:** `chore: retro-norm card citations — entities, lore, cards`

## Scope — pages to audit

Sects:
- `wiki/entities/sects/camarilla.md`
- `wiki/entities/sects/sabbat.md`
- `wiki/entities/sects/anarch.md`
- `wiki/entities/sects/independent.md`
- `wiki/entities/sects/laibon.md`

Card types:
- `wiki/entities/card-types/crypt.md`
- `wiki/entities/card-types/library.md`
- `wiki/entities/card-types/master.md`
- `wiki/entities/card-types/action.md`
- `wiki/entities/card-types/action-modifier.md`
- `wiki/entities/card-types/reaction.md`
- `wiki/entities/card-types/combat-card.md`
- `wiki/entities/card-types/political-action-card.md`
- `wiki/entities/card-types/ally.md`
- `wiki/entities/card-types/retainer.md`
- `wiki/entities/card-types/equipment.md`

Lore:
- `wiki/lore/wod-glossary.md`

Existing problem cards (sanity pass — ensure internal references still follow convention after schema v2):
- `wiki/cards/pentex-subversion.md`
- `wiki/cards/vessel.md`
- `wiki/cards/smiling-jack-the-anarch.md`
- `wiki/cards/theft-of-vitae.md`

Playgroup/meta — skip for this batch (no card citations expected).

## What to do on each page

Same procedure as batch-1a. See `batch-1a-retronorm-turn-actions.md` §"What to do on each page".

Additional note for `wiki/cards/<slug>.md` pages: references to the page's own card should use the plain card name (the page IS that card); references to OTHER cards follow the usual convention.

## Commit

```
git add wiki/entities/sects/ wiki/entities/card-types/ \
        wiki/lore/wod-glossary.md wiki/cards/

git commit -m "chore: retro-norm card citations — entities, lore, cards

Ensures all card-name citations on sect, card-type, lore, and
existing problem-card pages match the schema-v2 linking
convention: wikilink for problem-card pages, query-URL krcg
link otherwise.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

## Out of scope

- No new content.
- No structural edits.
- No enrichment from krcg `rulings[]`.
- Do not create new card pages.
- Do not touch pages outside the list above.
