# VTES Card Storage Design

**Date:** 2026-04-18
**Status:** approved for implementation
**Supersedes:** the "card-page storage model" open question in `wiki/meta/backlog.md` (2026-04-17)

## Context

The wiki is an LLM-maintained knowledge base for VTES. VTES has ~4000 unique cards across decades of printing. The LLM reads `wiki/index.md` to select relevant pages when answering a query — index bloat directly degrades retrieval quality. This is not RAG; the LLM reasons over loaded pages, so the ceiling on wiki size is a ceiling on LLM effectiveness.

Current rule of thumb ("only problem cards get a page") is right in direction but ad-hoc. Without a formal model, card pages accumulate organically and the wiki will cross 1000 pages within a year or two.

## Goals

- Keep `wiki/` bounded at ~200 pages long-term so index-reads stay cheap.
- Support card-level lookup ("what does Theft of Vitae do?") without page-per-card.
- Support structured deck-building queries (filter by discipline, type, cost, clan, capacity, group).
- Let accumulated playgroup knowledge compound without forcing a page per card.
- Preserve `raw/`'s immutability rule.

## Non-goals

- Not building a SQL layer or real database.
- Not indexing all cards into markdown pages.
- Not auto-importing krcg's per-card rulings into mechanic pages — those stay curated.
- Not translating card data into Russian.

## Architecture: four layers

Adds one layer to the existing three:

1. **`raw/`** — immutable source documents. LLM reads only.
2. **`card-db/`** — *new.* Structured, derived, regenerable shards. Top-level sibling to `raw/` and `wiki/`.
3. **`wiki/`** — LLM-curated human-readable knowledge.
4. **`docs/`** — design specs (historical).

`card-db/` is not `raw/` (it's derived) and not `wiki/` (not human-curated). A fourth peer is cleaner than stretching either.

## Card-db design

### Source of truth

`https://static.krcg.org/data/vtes.json` — single JSON array, ~7 MB, ~4000 cards. Maintained by krcg.org; updated at errata and new-set releases.

Per-card fields include `id`, `name`, `types[]`, `disciplines[]`, `clans[]`, `card_text`, cost fields (`pool_cost`, `blood_cost`, `conviction_cost`), crypt fields (`capacity`, `group`, `title`, `sect`), `legality`, printing history, and — critically — `rulings[]` with source references (RTR, LSJ, ANK, krcg). Embedded rulings make krcg a one-stop card-level source.

### Storage layout

```
raw/card-db-snapshots/
  vtes-YYYY-MM-DD.json        # immutable raw dumps
  scripts/
    split.py                  # ingest / shard script

card-db/
  crypt.json                  # types[0] in {"Vampire", "Imbued"}
  library/
    action.json
    action-modifier.json
    ally.json
    combat.json
    equipment.json
    event.json
    master.json
    political-action.json
    power.json
    reaction.json
    reflex.json
    retainer.json
  index.json                  # snapshot_date, card counts by type,
                              # multi_type_cards: {id: [type1, type2]}
```

### Shard assignment

- `types[0]` determines the shard.
- Crypt cards route to `crypt.json` regardless of order.
- Multi-type cards (<50 of 4000) are enumerated in `index.json.multi_type_cards` so secondary-type queries can still find them.

### Transformation

None. Full krcg records are stored verbatim in shards. Zero drift vs upstream; `rulings[]` and translations come free. 7 MB total is trivial on disk; queries load only one shard.

## Query paths

### Single-card view

1. Resolve card name → slug → shard (via type).
2. Read shard, find entry.
3. Grep `wiki/` for mentions (card name + variants).
4. If `wiki/cards/<slug>.md` exists, read it.
5. Assemble answer: card text verbatim + embedded `rulings[]` + wiki mentions + krcg link.

### Deck-building / semantic filter

1. Identify the narrowest shard(s) from the structured filter.
2. Apply attribute filter (`types`, `disciplines`, `cost`, `clans`, `capacity`, `group`) via `jq` or in-context.
3. If semantic, apply a coarse regex over `card_text`, then do LLM semantic cleanup on survivors.
4. Return list with card text + krcg links.
5. If reusable, offer to file `wiki/mechanics-index/<slug>.md`.

## Wiki-level changes

### Two new page types

`type: archetype` — deck-building view. Template sections: Core idea · Key disciplines and clans · Signature cards (crypt/library by role) · Support / tech · Common variants · Weaknesses · Related rulings.

`type: mechanic-index` — reverse index from a mechanic to implementing cards. Template sections: Scope · Cards (grouped by card type) · Query used (reproducible filter) · Related.

Both are **not** created preemptively. They're promoted from a concrete query whose result is substantive and likely to recur.

### Problem-card trigger (tightened)

A `wiki/cards/<slug>.md` page exists only when:

1. Conflicting rulings exist across sources — the page hosts `## Conflicting Rulings`, or
2. ≥3 distinct rulings **and** cited from ≥2 ruling pages — consolidation reduces cross-clicking, or
3. User explicitly requests a page.

Default: no page. Card data comes from `card-db`; rulings live on mechanic pages with inline `[Card Name](krcg-url)`.

### Linking convention

- `[[Card Name]]` — only for cards with a `wiki/cards/` page.
- `[Card Name](https://codex-of-the-damned.org/en/card-search/library/<slug>.html)` — library cards without a page.
- `[Card Name](https://codex-of-the-damned.org/en/card-search/crypt/<slug>.html)` — crypt cards.
- Slug = lowercased name, non-alphanumeric stripped (`Theft of Vitae` → `theftofvitae`). card-db includes canonical URLs when uncertain.

### `wiki/index.md` — new sections

- `## Archetypes` (grows from queries)
- `## Mechanics Index` (grows from queries)
- `## Card Database` — single pointer line to `card-db/` + latest snapshot date

## Operations (new entries in CLAUDE.md)

### Card-db snapshot ingest

Trigger: user asks to refresh, or krcg has published a new release.

1. Download `https://static.krcg.org/data/vtes.json` → `raw/card-db-snapshots/vtes-YYYY-MM-DD.json`.
2. Assign next `src-NNN`; add entry to `raw/index.md`.
3. Run `raw/card-db-snapshots/scripts/split.py` → rewrites `card-db/`.
4. Diff vs previous snapshot; summarize card-count delta and notable text/ruling changes.
5. If errata touches existing ruling pages, bump `last_verified` and re-check `status`.
6. Append to `wiki/log.md`: `ingest src-NNN | vtes snapshot YYYY-MM-DD | +X cards / Y text changes`.
7. Commit: `ingest: src-NNN card-db snapshot YYYY-MM-DD`.

### Card view query — see §Query paths.

### Deck-building query — see §Query paths.

## Source authority hierarchy — amendment

Current tiers (VEKN RD → Black Chantry → krcg → community) stand. Clarification: embedded `rulings[]` from the card-db dump are the same tier as krcg.org web pages. References within those rulings (e.g., `RTR 20010711`, `LSJ 20041027`) trace back to higher tiers and should be cited when propagating into wiki pages.

## CLAUDE.md — required updates

1. Intro section: three layers → four layers.
2. Directory rules: add `raw/card-db-snapshots/` and `card-db/` with immutability/regenerability notes.
3. Frontmatter `type` enum: add `archetype`, `mechanic-index`.
4. Source authority: krcg-tier note about embedded rulings.
5. Operations: three new operation entries (snapshot ingest, card view, deck-building).
6. Page templates: two new templates (`archetype`, `mechanic-index`).
7. New subsection "When to create a card page" with the three triggers.
8. "What NOT to do": four new bullets (no edits to `raw/card-db-snapshots/`, no hand-edits to `card-db/`, no card pages without a trigger, no card-text duplication).
9. Linking convention: slug rule + per-kind krcg URL template.
10. `wiki/index.md` new sections: Archetypes, Mechanics Index, Card Database.

## Non-obvious decisions and rationale

- **Why not SQLite?** Binary → no git diff → no review → no errata history. krcg changes are exactly what we want in `git log`.
- **Why keep full krcg records, not a minimal subset?** Zero transform = zero drift. Size is trivial; only one shard is loaded at query time.
- **Why `types[0]` for sharding despite multi-type cards?** <50 cards affected; `index.json.multi_type_cards` covers lookup. Duplicating entries across shards would risk drift on snapshot updates.
- **Why not auto-import krcg rulings into mechanic pages?** Would duplicate data already available via card-db on demand. Mechanic pages stay anchored to rulebook/RD rulings; card-level rulings surface at query time.
- **Why not a flat `all.json`?** Every semantic query would pull 7 MB into context. Shards cap load size at ~400 KB.
- **Why a separate `card-db/` top-level?** `raw/` is immutable; `wiki/` is curated. Derived structured data is neither.

## Rollout

- **Foundation** — single session: write split script, download snapshot, regenerate shards, update CLAUDE.md, wiki/index.md, raw/index.md, wiki/log.md. Commit.
- **Retro-normalization** — optional, batched: audit existing wiki pages for card citations and align to the new linking convention.
- **Enrichment** — optional, batched: selectively surface krcg `rulings[]` that add material edge cases beyond the rulebook, on a per-mechanic-page basis.

Batch structure and agent orchestration are captured in the implementation plan.
