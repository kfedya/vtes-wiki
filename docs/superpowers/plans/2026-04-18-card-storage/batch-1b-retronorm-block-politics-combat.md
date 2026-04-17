# Batch 1b — Retro-normalize card citations: block, politics, combat

**Goal:** audit card citations on block-resolution, politics, and combat rulings; normalize formatting; bump `last_verified`.

**Depends on:** Batch 0.

**Commit subject:** `chore: retro-norm card citations — block, politics, combat`

## Scope — pages to audit

- `wiki/rulings/block-resolution.md`
- `wiki/rulings/politics.md`
- `wiki/rulings/political-action.md`
- `wiki/rulings/referendum.md`
- `wiki/rulings/voting.md`
- `wiki/rulings/combat.md`
- `wiki/rulings/maneuver.md`
- `wiki/rulings/strike.md`
- `wiki/rulings/strike-effects.md`
- `wiki/rulings/damage-resolution.md`
- `wiki/rulings/press.md`

## What to do on each page

Same procedure as batch-1a. See `batch-1a-retronorm-turn-actions.md` §"What to do on each page".

## Commit

```
git add wiki/rulings/block-resolution.md wiki/rulings/politics.md \
        wiki/rulings/political-action.md wiki/rulings/referendum.md \
        wiki/rulings/voting.md wiki/rulings/combat.md wiki/rulings/maneuver.md \
        wiki/rulings/strike.md wiki/rulings/strike-effects.md \
        wiki/rulings/damage-resolution.md wiki/rulings/press.md

git commit -m "chore: retro-norm card citations — block, politics, combat

Ensures all card-name citations on block-resolution, politics,
and combat-family ruling pages match the schema-v2 linking
convention: wikilink for problem-card pages, query-URL krcg
link otherwise.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

## Out of scope

- No new content.
- No structural edits.
- No enrichment from krcg `rulings[]`.
- Do not touch pages outside the list above.
