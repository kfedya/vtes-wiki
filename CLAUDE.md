# VTES Wiki — LLM Schema

This file tells any LLM assistant how to operate on this wiki. Read it fully before any ingest, query, or lint operation.

## What this repo is

A personal, LLM-maintained knowledge base for **Vampire: The Eternal Struggle** (VTES). Primary purpose: quick reference for rulings and edge cases during local playgroup games. Secondary: deck-building, lore, tournament meta, personal collection.

Built on the "LLM Wiki" pattern — three layers (raw sources, wiki pages, schema), LLM does maintenance, human curates sources and asks questions.

Full design: `docs/superpowers/specs/2026-04-17-vtes-wiki-design.md`.

## Language

- **Wiki content is in English.** Official card text and rulings exist in English only; translating them risks subtle errors that break the whole point of this reference.
- **Conversation with the user is in Russian** by default. Explanations in chat can be in Russian; the wiki stays English.

## Three layers

1. **`raw/`** — immutable source documents (PDFs, markdown clips, Discord exports, card-database snapshots). LLM **reads only**; never writes or modifies. This is the source of truth.
2. **`wiki/`** — LLM-managed markdown pages. User reads; LLM creates and updates.
3. **`CLAUDE.md`** (this file) — the schema. Co-evolved. Either party proposes changes; the other confirms before the schema changes.

## Directory rules

- The three top-level directories (`raw/`, `wiki/`, `docs/`) always exist.
- All sub-directories (`raw/rulebooks/`, `wiki/rulings/`, `wiki/entities/clans/`, …) are created **only when the first file inside them is written**. No empty scaffolding.

## File naming

- kebab-case, English, no spaces.
- Wiki pages: `<descriptive-slug>.md`.
- Card pages: `<card-name-slug>.md` in `wiki/cards/`. Example: `wake-with-evenings-freshness.md`.
- Clan / discipline / sect pages: lowercase bare name. Example: `wiki/entities/clans/tremere.md`, `wiki/entities/disciplines/auspex.md`.
- Source files: `NNN-slug.ext` in the matching `raw/<category>/`. IDs grow monotonically across the whole `raw/` — not per-category.

## Page frontmatter (required on every `wiki/` page)

```yaml
---
type: ruling | entity | card | archetype | playgroup | lore | meta | collection
tags: [kebab-case, tags, here]
sources: [src-NNN, src-NNN]
last_verified: YYYY-MM-DD
status: draft | verified | disputed
---
```

- `type` — must match the top-level `wiki/` category the page lives under. Pages nested inside `wiki/entities/*/` (clans, disciplines, sects, card-types, sets) all use `type: entity`.
- `tags` — free-form, kebab-case. Re-use existing tags where possible; check `wiki/index.md` before inventing new ones.
- `sources` — list of source IDs backing the page's claims. Every ruling-layer statement needs at least one source.
- `last_verified` — date the LLM last cross-checked the page against its sources. Bump on every substantive update.
- `status`:
  - `draft` — new page, not yet cross-checked.
  - `verified` — passed a lint pass; sources still current.
  - `disputed` — contains a `## Conflicting Rulings` section awaiting resolution.

## Cross-links

- Internal links use Obsidian wikilinks: `[[page-name]]` or `[[page-name|display text]]`.
- Card references: `[[Card Name]]` **only if** the card has its own page in `wiki/cards/`. Otherwise use an inline markdown link to its krcg.org page: `[Card Name](https://codex-of-the-damned.org/en/card-search/library/...)`.
- External links always include a visible URL and source context.

## Source citations

Every factual statement in `wiki/rulings/` must carry at least one source ID in brackets, e.g.:

```
> Stealth is applied separately to each bleed action [src-007].
```

Source IDs resolve via `raw/index.md`.

Card text is quoted **verbatim** from the official English wording in a blockquote, followed by a link to the krcg.org page. Never paraphrase card text.

## Source authority hierarchy

When two sources conflict, use this order from most to least authoritative:

1. **Rules Director rulings** (VEKN — vekn.net)
2. **Black Chantry Productions** official FAQ and rulebook
3. **krcg.org** (Codex of the Damned) card-level rulings
4. **Community discussion** (Discord, reddit, BGG, forum threads) — treat as informational, not authoritative on their own.

**Never silently resolve a conflict.** When a new source contradicts an existing claim:
1. Do not delete the old claim.
2. Add a `## Conflicting Rulings` section to the page.
3. Record both claims with their source IDs and dates.
4. Set the page's `status` to `disputed`.
5. Flag for resolution on the next lint pass.

## Operations

### Ingest

**Trigger:** user drops a file into `raw/<category>/` and asks to ingest, or provides a URL to fetch.

**Workflow:**
1. Assign the next source ID. Scan `raw/index.md` for the current highest `src-NNN` and increment.
2. Read the source fully. For non-text (PDFs, images) convert or OCR as needed.
3. Discuss the key takeaways with the user in chat (Russian). Confirm what to emphasize, what conflicts existing claims, and what's genuinely new.
4. Propose which wiki pages to create or update. User confirms.
5. Apply:
   - Create or update pages with proper frontmatter and inline source citations.
   - Add a one-line entry to the relevant section of `wiki/index.md`.
   - Add an entry to `raw/index.md` under the matching category, filling every template field including `pages_touched`.
   - Append to `wiki/log.md`: `## [YYYY-MM-DD] ingest src-NNN | <short title> — touched <N> pages`.
6. Commit. One source = one commit. Commit message: `ingest: src-NNN <short title>`.

A single ingest typically touches 3–10 wiki pages.

### Query

**Trigger:** user asks a question in chat.

**Workflow:**
1. Read `wiki/index.md` first to locate relevant pages.
2. Drill into the identified pages.
3. If the answer requires information not in the wiki, say so and suggest ingesting sources that would cover it. Do not invent.
4. Answer with inline source citations when quoting ruling-layer statements.
5. If the answer is genuinely novel — a comparison, a synthesis, or a new connection — offer to file it as a new page so the knowledge compounds.
6. For significant queries (ones that involved more than a simple page lookup), append to `wiki/log.md`: `## [YYYY-MM-DD] query | "<question>" — filed as <path> §<section>` (or `— no page filed` if nothing new).

### Lint

**Trigger:** user runs "lint wiki".

**Workflow:**
1. Scan all pages for contradictions (same claim, different conclusions across pages).
2. Flag pages where `last_verified` is more than 6 months old.
3. Identify orphan pages (no inbound wikilinks from any other page and not linked from `wiki/index.md`).
4. Suggest missing cross-links (terms that match existing page names but aren't linked).
5. Suggest new questions or sources to close visible gaps.
6. Present findings as a report. **Apply fixes only after user confirmation** per finding type.
7. Append to `wiki/log.md`: `## [YYYY-MM-DD] lint | <N> contradictions, <M> orphans, <K> stale`.

## Page templates

### Ruling page (`wiki/rulings/<mechanic>.md`)

```markdown
---
type: ruling
tags: [...]
sources: [src-NNN]
last_verified: YYYY-MM-DD
status: draft
---

# <Mechanic Name>

## Summary
<2–3 sentences.>

## Step-by-Step Sequence
1. ...
2. ...

## Common Cards Involved
- [[Card Name]] — how it interacts.
- [Card Name](https://codex-of-the-damned.org/...) — ...

## Common Mistakes
- See [[common-mistakes#<anchor>]].

## Conflicting Rulings
<Only if applicable.>

## Sources
- src-NNN — <title>, <date>.
```

### Card page (`wiki/cards/<slug>.md`)

```markdown
---
type: card
tags: [...]
sources: [src-NNN]
last_verified: YYYY-MM-DD
status: draft
---

# <Card Name>

> <Verbatim card text in a blockquote.>

— [krcg.org entry](https://codex-of-the-damned.org/...)

## Why it has a page
<One sentence: disputed ruling / archetype-defining / complex interaction.>

## Rulings
- ...

## Sources
- src-NNN — ...
```

## What NOT to do

- Do not modify or delete files in `raw/`.
- Do not paraphrase card text.
- Do not silently resolve conflicts. Always use `## Conflicting Rulings`.
- Do not create empty sub-directories.
- Do not commit wiki changes without updating `wiki/log.md`.
- Do not translate rulings into Russian inside wiki files. Chat explanations can be Russian; the wiki stays English.
- Do not write to `docs/superpowers/specs/` in normal operation — those are historical design documents.
