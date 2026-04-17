# Batch 1a — Retro-normalize card citations: turn structure + actions

**Goal:** audit card citations on turn-structure and action rulings; normalize formatting; bump `last_verified`.

**Depends on:** Batch 0 (card-db must exist for verifying card names).

**Commit subject:** `chore: retro-norm card citations — turn structure + actions`

## Scope — pages to audit

- `wiki/rulings/game-overview.md`
- `wiki/rulings/unlock-phase.md`
- `wiki/rulings/master-phase.md`
- `wiki/rulings/minion-phase.md`
- `wiki/rulings/influence-phase.md`
- `wiki/rulings/discard-phase.md`
- `wiki/rulings/bleed.md`
- `wiki/rulings/hunt.md`
- `wiki/rulings/equip.md`
- `wiki/rulings/employ-retainer.md`
- `wiki/rulings/recruit-ally.md`
- `wiki/rulings/leave-torpor.md`
- `wiki/rulings/rescue-from-torpor.md`
- `wiki/rulings/diablerise-action.md`
- `wiki/rulings/become-anarch.md`

## What to do on each page

1. Read the page fully.
2. Find every card name mention (look for capitalized proper-noun card names — often in bold, italic, or already linked).
3. For each mention, classify:
   - **Problem card** (has `wiki/cards/<slug>.md`): ensure written as `[[Card Name]]`. Current problem cards: `pentex-subversion`, `vessel`, `smiling-jack-the-anarch`, `theft-of-vitae`.
   - **Other card**: ensure written as `[Card Name](https://codex-of-the-damned.org/en/card-search/library/index.html?card=<URL-encoded-Name>)` for library, `/crypt/index.html?card=...` for crypt. Use `%20` for spaces.
   - **Flavor mention** (e.g., paraphrased in a rule sentence, not a citation): leave as-is.
4. If a card is cited but you're unsure if it's crypt or library, verify by searching `card-db/crypt.json` vs `card-db/library/*.json` for the exact name.
5. Card-db can also confirm spelling: search by name with a simple grep.
6. Do NOT add new card citations the original text didn't have.
7. Do NOT rewrite or restructure page content — this is a link-formatting pass only.
8. After editing the page, bump the `last_verified` frontmatter to `2026-04-18`.

## Verification commands (per page)

```bash
# Find unlinked card names (heuristic: capitalized multi-word phrases outside links).
# Not perfect — use judgment. Good for a spot-check.
grep -oE '\*\*[A-Z][a-zA-Z ]+\*\*' wiki/rulings/<page>.md

# Confirm card name exists in card-db.
jq -r '.[] | select(.name == "Theft of Vitae") | .name' card-db/library/combat.json
```

## Commit

Stage only the files in scope, commit with the declared subject.

```
git add wiki/rulings/game-overview.md wiki/rulings/unlock-phase.md \
        wiki/rulings/master-phase.md wiki/rulings/minion-phase.md \
        wiki/rulings/influence-phase.md wiki/rulings/discard-phase.md \
        wiki/rulings/bleed.md wiki/rulings/hunt.md wiki/rulings/equip.md \
        wiki/rulings/employ-retainer.md wiki/rulings/recruit-ally.md \
        wiki/rulings/leave-torpor.md wiki/rulings/rescue-from-torpor.md \
        wiki/rulings/diablerise-action.md wiki/rulings/become-anarch.md

git commit -m "chore: retro-norm card citations — turn structure + actions

Ensures all card-name citations on turn-structure and action
ruling pages match the schema-v2 linking convention: wikilink
for problem-card pages, query-URL krcg link otherwise.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

## Out of scope

- No new content.
- No structural edits.
- No enrichment from krcg `rulings[]` — that's batch 2.
- Do not touch pages outside the list above.
