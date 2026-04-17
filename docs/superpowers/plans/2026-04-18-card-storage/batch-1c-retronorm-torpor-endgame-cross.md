# Batch 1c — Retro-normalize card citations: torpor, diablerie, endgame, traits, cross-cutting

**Goal:** audit card citations on torpor/diablerie, endgame, traits, and cross-cutting interaction pages; normalize formatting; bump `last_verified`.

**Depends on:** Batch 0.

**Commit subject:** `chore: retro-norm card citations — torpor, endgame, cross-cutting`

## Scope — pages to audit

- `wiki/rulings/torpor.md`
- `wiki/rulings/diablerie.md`
- `wiki/rulings/blood-hunt.md`
- `wiki/rulings/ending-the-game.md`
- `wiki/rulings/withdraw.md`
- `wiki/rulings/traits.md`
- `wiki/rulings/stealth-modifiers.md`
- `wiki/rulings/target-redirection.md`
- `wiki/rulings/post-combat-effects.md`
- `wiki/rulings/hunting-grounds.md`
- `wiki/rulings/cards-removed-in-5e.md`
- `wiki/rulings/quick-reference.md`

## What to do on each page

Same procedure as batch-1a. See `batch-1a-retronorm-turn-actions.md` §"What to do on each page".

## Commit

```
git add wiki/rulings/torpor.md wiki/rulings/diablerie.md wiki/rulings/blood-hunt.md \
        wiki/rulings/ending-the-game.md wiki/rulings/withdraw.md wiki/rulings/traits.md \
        wiki/rulings/stealth-modifiers.md wiki/rulings/target-redirection.md \
        wiki/rulings/post-combat-effects.md wiki/rulings/hunting-grounds.md \
        wiki/rulings/cards-removed-in-5e.md wiki/rulings/quick-reference.md

git commit -m "chore: retro-norm card citations — torpor, endgame, cross-cutting

Ensures all card-name citations on torpor/diablerie, endgame,
traits, and cross-cutting interaction pages match the schema-v2
linking convention: wikilink for problem-card pages, query-URL
krcg link otherwise.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

## Out of scope

- No new content.
- No structural edits.
- No enrichment from krcg `rulings[]`.
- Do not touch pages outside the list above.
