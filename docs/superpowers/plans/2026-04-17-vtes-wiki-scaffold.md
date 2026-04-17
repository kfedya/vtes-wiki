# VTES Wiki Scaffold Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Scaffold the initial file structure of the VTES wiki (directory skeleton, schema file, empty index/log files, gitignore) so that ingest/query/lint operations can start on day one.

**Architecture:** Three-layer LLM-Wiki pattern — `raw/` (immutable sources), `wiki/` (LLM-managed pages), `CLAUDE.md` (schema). Git-tracked from day one. No empty directories beyond the three top-level ones; sub-directories appear only when the first page inside them is created via real ingest.

**Tech Stack:** Plain markdown + YAML frontmatter. Obsidian as the reading IDE (optional). Git for versioning. No build system, no code.

**Reference spec:** `/Users/kfedya/Desktop/VTES/docs/superpowers/specs/2026-04-17-vtes-wiki-design.md`

**Pre-state:** Git repo is already initialized at `/Users/kfedya/Desktop/VTES/` with one commit (the spec). `docs/superpowers/specs/` and `docs/superpowers/plans/` already exist. Everything else still needs to be created.

---

### Task 1: Top-level directory skeleton and `.gitignore`

**Files:**
- Create: `/Users/kfedya/Desktop/VTES/raw/` (empty dir)
- Create: `/Users/kfedya/Desktop/VTES/wiki/` (empty dir)
- Create: `/Users/kfedya/Desktop/VTES/.gitignore`

Only the two top-level content dirs (`raw/` and `wiki/`) are created now. All sub-directories (e.g. `raw/rulebooks/`, `wiki/rulings/`) will be created later, organically, when the first file inside them is written. This enforces the "no empty scaffolding" rule from the spec.

- [ ] **Step 1: Create the two top-level directories**

Run:
```bash
mkdir -p /Users/kfedya/Desktop/VTES/raw /Users/kfedya/Desktop/VTES/wiki
```
Expected: no output; both directories exist.

- [ ] **Step 2: Create `.gitignore`**

Write `/Users/kfedya/Desktop/VTES/.gitignore` with exactly this content:

```gitignore
# macOS
.DS_Store

# Obsidian vault user state (keep vault-level config, drop user-local state)
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/workspace.json.bak

# Editor caches
.idea/
.vscode/
*.swp
```

- [ ] **Step 3: Verify the structure**

Run:
```bash
ls -la /Users/kfedya/Desktop/VTES/
```
Expected output includes: `.git/`, `.gitignore`, `docs/`, `raw/`, `wiki/`.

Empty directories won't appear in `git status` on their own — they'll be picked up once they contain files (Tasks 2 and 3).

- [ ] **Step 4: Commit**

Run:
```bash
cd /Users/kfedya/Desktop/VTES
git add .gitignore
git commit -m "$(cat <<'EOF'
chore: add .gitignore and create top-level layout

Scaffolds raw/ and wiki/ directories (currently empty — content
appears in subsequent tasks).

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

Expected: one commit added. Run `git log --oneline` — should show 2 commits (the spec + this one).

---

### Task 2: Create index files (`raw/index.md`, `wiki/index.md`, `wiki/log.md`)

**Files:**
- Create: `/Users/kfedya/Desktop/VTES/raw/index.md`
- Create: `/Users/kfedya/Desktop/VTES/wiki/index.md`
- Create: `/Users/kfedya/Desktop/VTES/wiki/log.md`

These three files are the navigational backbone. They start essentially empty but with the exact structure the LLM will append to on every ingest/query/lint.

- [ ] **Step 1: Write `raw/index.md`**

Write `/Users/kfedya/Desktop/VTES/raw/index.md` with exactly this content (outer fence uses 4 backticks so the inner 3-backtick template block nests correctly):

````markdown
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

_(No sources ingested yet. First entry will be appended here.)_

### Rulebooks
### Rulings
### krcg snapshots
### Articles
### Forums
### Videos
### Discord
### Decks
### Personal notes
````

- [ ] **Step 2: Write `wiki/index.md`**

Write `/Users/kfedya/Desktop/VTES/wiki/index.md` with exactly this content:

```markdown
# VTES Wiki Index

Last updated: 2026-04-17 | Pages: 0 | Sources: 0

Catalogue of every page in the wiki. LLM reads this first when answering a query to locate relevant pages, and updates it on every ingest.

## Conventions

- Entries are grouped by category (matching the folder structure).
- Each entry is one line: `- [[page-name]] — one-line summary (<150 chars)`.
- Keep summaries specific; they drive relevance decisions during retrieval.

## Rulings (primary)

_(no pages yet)_

## Playgroup

_(no pages yet)_

## Entities

### Clans
_(no pages yet)_

### Disciplines
_(no pages yet)_

### Sects
_(no pages yet)_

### Card types
_(no pages yet)_

### Sets
_(no pages yet)_

## Cards (problem cards only)

_(no pages yet)_

## Archetypes

_(no pages yet)_

## Lore

_(no pages yet)_

## Meta

_(no pages yet)_

## Collection

_(no pages yet)_
```

- [ ] **Step 3: Write `wiki/log.md`**

Write `/Users/kfedya/Desktop/VTES/wiki/log.md` with exactly this content:

```markdown
# Wiki Log

Append-only chronology of wiki activity. Each entry starts with `## [YYYY-MM-DD] <op> | <short description>` so `grep "^## \[" log.md` yields a clean timeline.

## Operations

- `init` — wiki scaffolded
- `ingest src-NNN` — new source integrated into the wiki
- `query` — significant question answered; may result in a new page
- `lint` — health-check pass

---

## [2026-04-17] init | Wiki scaffolded from brainstorm spec (docs/superpowers/specs/2026-04-17-vtes-wiki-design.md)
```

- [ ] **Step 4: Verify file contents**

Run:
```bash
ls /Users/kfedya/Desktop/VTES/raw/ /Users/kfedya/Desktop/VTES/wiki/
head -5 /Users/kfedya/Desktop/VTES/raw/index.md
head -5 /Users/kfedya/Desktop/VTES/wiki/index.md
tail -3 /Users/kfedya/Desktop/VTES/wiki/log.md
```
Expected: `index.md` visible in `raw/`; `index.md` and `log.md` visible in `wiki/`; heads show the first few lines of each file; tail of `log.md` ends with the `[2026-04-17] init` line.

- [ ] **Step 5: Commit**

Run:
```bash
cd /Users/kfedya/Desktop/VTES
git add raw/index.md wiki/index.md wiki/log.md
git commit -m "$(cat <<'EOF'
feat: add wiki and raw index files, initialize log

- raw/index.md: empty source catalogue with entry template
- wiki/index.md: empty page catalogue with category headers
- wiki/log.md: append-only activity log, first entry is init

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

Expected: 3 files added in one commit. `git log --oneline` now shows 3 commits.

---

### Task 3: Write `CLAUDE.md` schema (root of the vault)

**Files:**
- Create: `/Users/kfedya/Desktop/VTES/CLAUDE.md`

`CLAUDE.md` is the schema — the single file that tells any LLM assistant how to read and write this wiki. It is the most important file in the repo after the sources themselves. It must be precise and complete; vagueness here turns into inconsistency across dozens of wiki pages later.

- [ ] **Step 1: Write the full schema**

Write `/Users/kfedya/Desktop/VTES/CLAUDE.md` with exactly this content:

````markdown
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

- `type` — must match the top-level category the page lives in.
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
````

- [ ] **Step 2: Verify the schema**

Run:
```bash
wc -l /Users/kfedya/Desktop/VTES/CLAUDE.md
head -5 /Users/kfedya/Desktop/VTES/CLAUDE.md
```
Expected: a non-zero line count (~200 lines); first line is `# VTES Wiki — LLM Schema`.

- [ ] **Step 3: Commit**

Run:
```bash
cd /Users/kfedya/Desktop/VTES
git add CLAUDE.md
git commit -m "$(cat <<'EOF'
feat: add CLAUDE.md schema

Defines how any LLM assistant should operate on this wiki — three
layers, file naming, frontmatter, source-authority hierarchy, and
the ingest/query/lint workflows.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

Expected: `git log --oneline` now shows 4 commits.

---

### Task 4: Smoke-test the scaffold end-to-end

No new files. This task verifies the scaffold is usable: git tree matches the spec, structure is what we expect, and a trivial dry-run ingest/query would have somewhere to land.

- [ ] **Step 1: Verify the tree**

Run:
```bash
cd /Users/kfedya/Desktop/VTES
find . -type f -not -path './.git/*' | sort
```
Expected output (exact):
```
./.gitignore
./CLAUDE.md
./docs/superpowers/plans/2026-04-17-vtes-wiki-scaffold.md
./docs/superpowers/specs/2026-04-17-vtes-wiki-design.md
./raw/index.md
./wiki/index.md
./wiki/log.md
```

If any file is missing or extra, fix it before continuing.

- [ ] **Step 2: Verify git is clean**

Run:
```bash
cd /Users/kfedya/Desktop/VTES
git status
git log --oneline
```
Expected: `git status` shows a clean working tree. `git log --oneline` shows 4 commits (spec, gitignore, index files, CLAUDE.md).

Note: the plan file itself (`docs/superpowers/plans/2026-04-17-vtes-wiki-scaffold.md`) was created before task execution started and may be untracked. If so, commit it in Step 4 below.

- [ ] **Step 3: Sanity-check the index files**

Run:
```bash
grep -c "^## " /Users/kfedya/Desktop/VTES/wiki/index.md
grep -c "^## " /Users/kfedya/Desktop/VTES/raw/index.md
tail -1 /Users/kfedya/Desktop/VTES/wiki/log.md
```
Expected:
- `wiki/index.md` has several `## ` headers (categories: Rulings, Playgroup, Entities, Cards, Archetypes, Lore, Meta, Collection — expect ≥ 8 matches, plus sub-headers bump the count higher).
- `raw/index.md` has several `## ` headers (category buckets — expect ≥ 2 matches from "Conventions", "Entry template", "Sources" and sub-sections).
- `wiki/log.md` tail shows the `[2026-04-17] init` line.

- [ ] **Step 4: Commit the plan file if still untracked**

Run:
```bash
cd /Users/kfedya/Desktop/VTES
git status --short docs/superpowers/plans/
```

If the plan file is untracked (`?? docs/superpowers/plans/...`), commit it:
```bash
git add docs/superpowers/plans/2026-04-17-vtes-wiki-scaffold.md
git commit -m "$(cat <<'EOF'
docs: add wiki scaffold implementation plan

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

If it is already tracked, skip.

- [ ] **Step 5: Final report to user**

Print (in chat, Russian):
```
Scaffold готов. 
Файлы: CLAUDE.md, .gitignore, raw/index.md, wiki/index.md, wiki/log.md.
Git: <N> коммитов (см. git log --oneline).
Следующий шаг: кинь первый источник в raw/ и скажи «ingest» — запустим первый реальный цикл.
```

Fill `<N>` with the actual commit count.

---

## Definition of done

- `/Users/kfedya/Desktop/VTES/` contains exactly the 7 files listed in Task 4 Step 1.
- `git status` is clean.
- `git log --oneline` shows 4–5 commits (depending on whether the plan file needed a final commit).
- `CLAUDE.md` fully defines the ingest / query / lint workflows, source authority hierarchy, frontmatter conventions, and "what not to do" rules.
- `wiki/index.md` has category headers but no page entries yet.
- `raw/index.md` has the entry template and empty category buckets.
- `wiki/log.md` has exactly one entry: the `init` line.

No wiki pages about actual VTES content exist yet — those come from real ingests, not from scaffolding.
