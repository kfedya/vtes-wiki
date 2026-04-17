# VTES Wiki — Design Spec

**Date:** 2026-04-17
**Status:** Approved for implementation
**Location:** `/Users/kfedya/Desktop/VTES/`

## Purpose

A personal LLM-maintained knowledge base for Vampire: The Eternal Struggle (VTES), implementing the "LLM Wiki" pattern (three-layer: raw sources, wiki, schema).

**Primary use case:** quick reference for rulings and edge cases — resolving rules disputes in a local 2-year-old playgroup that regularly discovers rules mistakes.

**Secondary use cases (ranked):**
- Deck-building (cards, archetypes, combos, meta)
- Tournament prep (current meta, top decks, results)
- World of Darkness lore supporting VTES cards and factions
- Personal collection tracking

**User profile:** plays ~2 years in a Russian-speaking local playgroup; regularly finds they've been playing rules wrong; wants an authoritative reference to settle disputes.

**Language:** wiki content in English (official card/rules text is English-only; avoids translation errors). LLM conversation about the wiki in Russian.

## Architecture

Three-layer structure following the LLM Wiki pattern.

```
/Users/kfedya/Desktop/VTES/
├── CLAUDE.md              # schema: how LLM operates on the wiki
├── raw/                   # immutable sources (LLM reads, never writes)
├── wiki/                  # LLM-managed pages (user reads, LLM writes)
│   ├── index.md
│   └── log.md
├── docs/superpowers/      # design specs and plans (this file lives here)
├── .gitignore
└── .git/                  # git repo from day one
```

**Layer responsibilities:**
- `raw/` — user-curated sources. LLM reads only.
- `wiki/` — LLM-owned. User reads; LLM creates/updates.
- `CLAUDE.md` — co-evolved schema. Either party proposes changes; both confirm.

## `wiki/` directory structure

Rules-first architecture — primary layer is mechanics; entities and cards are supporting.

```
wiki/
├── index.md                      # catalog of all pages with one-line summaries
├── log.md                        # append-only chronology
│
├── rulings/                      # PRIMARY — by game mechanic
│   ├── bleed-sequence.md
│   ├── combat-sequence.md
│   ├── strike-resolution.md
│   ├── damage-prevention.md
│   ├── influence-phase.md
│   ├── untap-phase.md
│   ├── master-phase.md
│   ├── minion-phase.md
│   ├── stealth-intercept.md
│   ├── reaction-timing.md
│   ├── blood-and-pool.md
│   ├── oust-conditions.md
│   ├── torpor-and-diablerie.md
│   ├── replacement-vs-modifier.md
│   └── ...                       # grow organically via ingest
│
├── playgroup/                    # dedicated layer for user's local reality
│   ├── common-mistakes.md        # running list of rules errors in user's games
│   └── disputes-log.md           # resolved disputes with dates and sources
│
├── entities/                     # SECONDARY
│   ├── clans/                    # brujah.md, tremere.md, …
│   ├── disciplines/              # auspex.md, dominate.md, …
│   ├── sects/                    # camarilla.md, sabbat.md, …
│   ├── card-types/               # action, reaction, combat, equipment, ally, retainer, master, modifier, political, event
│   └── sets/                     # fifth-edition.md, heirs-to-the-blood.md, …
│
├── cards/                        # TERTIARY — only "problem" cards (disputed, complex, archetype-defining)
│   └── <card-slug>.md
│
├── archetypes/                   # for deck-building use case
│   └── <archetype>.md
│
├── lore/                         # for WoD lore use case
│
├── meta/                         # for tournament prep
│   ├── current-meta.md
│   └── tournaments/
│
└── collection/                   # for personal collection tracking
    └── my-inventory.md
```

**Rules:**
- Directories are created only when the first page inside them exists (no empty scaffolding).
- File names are kebab-case, English.
- `rulings/` and `playgroup/` are the heart of the system.

## Page format conventions

**YAML frontmatter (required on every page):**

```yaml
---
type: ruling | entity | card | archetype | playgroup | lore | meta | collection
tags: [bleed, stealth-intercept, camarilla, …]
sources: [src-001, src-003, src-012]       # IDs referencing raw/index.md
last_verified: 2026-04-17                  # date LLM last cross-checked with sources
status: draft | verified | disputed
---
```

**Cross-linking:** Obsidian-style wikilinks `[[page-name]]` for all internal links (enables graph view). For cards: `[[Wake with Evening's Freshness]]` if the card has its own page, otherwise inline link to the card's krcg.org page.

**Source citations:** every ruling-layer statement must carry a source ID: `> Stealth acts on each bleed separately [src-007]`. Source IDs resolve via `raw/index.md`.

**Card text quotes:** verbatim English text in a blockquote with a link to krcg.org. Never paraphrase card text.

**Conflicting rulings:** when a new source contradicts an existing page, the LLM does NOT delete the old claim. Instead it adds a `## Conflicting Rulings` section with dates and source weights. Authority hierarchy: Rules Director > Black Chantry FAQ > krcg.org rulings > community/BGG.

**Ruling page template:**
```
# <Mechanic Name>
## Summary                       — 2–3 sentences
## Step-by-Step Sequence         — numbered steps
## Common Cards Involved         — links to cards/krcg
## Common Mistakes               — links to playgroup/common-mistakes.md
## Conflicting Rulings           — if any
## Sources                       — list with dates
```

## `raw/` organization and ingestion

**Directory layout:**

```
raw/
├── index.md                      # source catalog: ID, type, date, annotation
├── rulebooks/                    # official PDFs + markdown conversions
├── rulings/                      # VEKN / Rules Director rulings
├── krcg/                         # archived krcg.org snapshots
├── articles/                     # blog posts, articles
├── forums/                       # reddit/BGG threads
├── videos/                       # stream/podcast transcripts
├── discord/                      # Discord conversation exports
├── decks/                        # deck lists from Amaranth/tournaments
└── personal/                     # user's own notes, questions from games
```

**Source ID scheme:** `NNN-slug.ext`. IDs grow monotonically. `raw/index.md` is the source of truth.

**`raw/index.md` entry format:**
```markdown
## src-020 — Discord #rulings-2026-04-15
- type: discord-export
- date: 2026-04-15
- channel: VTES Official / #rulings
- topic: Ironclad's Pride + Telepathic Counter interaction
- added: 2026-04-16
- pages_touched: [wiki/rulings/stealth-intercept.md, wiki/playgroup/common-mistakes.md]
```

**Ingestion workflow:**
1. User drops file into `raw/<category>/` (or provides a URL for LLM to fetch).
2. User invokes ingest: "ingest src-020" or describes the source.
3. LLM reads, discusses key takeaways with user, proposes which wiki pages to touch.
4. User confirms → LLM creates/updates pages, updates `raw/index.md` entry, appends to `wiki/log.md`.
5. A single source typically touches 3–10 wiki pages.

**Discord-specific ingestion:** user copies the relevant conversation into a markdown file with a header (channel, date, participants). Or exports via DiscordChatExporter — LLM parses.

## Special files

**`wiki/index.md`** — catalog, updated on every ingest. Grouped by type:

```markdown
# VTES Wiki Index
Last updated: 2026-04-17 | Pages: 42 | Sources: 12

## Rulings (primary)
- [[bleed-sequence]] — full bleed phase with modifiers, reactions, and replacement cards
…

## Playgroup
- [[common-mistakes]] — running list of rules errors in our games
…
```

**`wiki/log.md`** — append-only, parseable with `grep "^## \[" log.md`:

```markdown
## [2026-04-17] init | Wiki scaffolded from VTES brainstorm
## [2026-04-18] ingest src-001 | Fifth Edition rulebook — touched 8 pages
## [2026-04-18] query | "how does press work after stealth bleed" — filed as rulings/stealth-intercept.md §Press
## [2026-04-19] lint | 3 orphan pages, 2 conflicts flagged
```

**`CLAUDE.md` (schema file at repo root)** — contains:
- Three-layer architecture description
- File naming, frontmatter, and cross-link conventions
- Workflows for the three operations (ingest / query / lint)
- Source authority hierarchy (Rules Director > BCP FAQ > krcg > community)
- Instruction: read `wiki/index.md` first when answering any query

## Operations

**Ingest** — user supplies a source; LLM summarizes, proposes page changes, applies after confirmation. See Ingestion workflow above.

**Query** — user asks a question. LLM reads `wiki/index.md`, identifies relevant pages, reads them, answers with citations. If the answer is genuinely novel (a comparison, analysis, or new connection), LLM offers to file it as a new page so knowledge compounds.

**Lint** — on command "lint wiki", LLM:
- Finds contradictions across pages
- Flags stale pages (old `last_verified`)
- Identifies orphan pages (no inbound links)
- Proposes missing cross-links
- Suggests new questions/sources to close gaps

## Tooling

**Obsidian** — open `/Users/kfedya/Desktop/VTES/` as a vault. Recommended plugins:
- Dataview — queries over frontmatter
- Graph view — built-in, shows page connectivity
- Outliner
- Marp (optional) — markdown-based slide decks
- Web Clipper (optional) — saves web articles into `raw/` as markdown

**Git** — repo from day one; every ingest/lint can be a commit. Free version history and branching.

## Success criteria

The wiki is successful when:
1. During a playgroup dispute, user opens the vault, types the mechanic name, and has a cited answer within 60 seconds.
2. Every ruling statement in `wiki/rulings/` traces back to at least one entry in `raw/index.md`.
3. `wiki/playgroup/common-mistakes.md` grows over time with real examples, each linking to the relevant ruling page.
4. Lint passes monthly: no unresolved contradictions, no stale pages > 6 months without re-verification.

## Out of scope (YAGNI)

- No full card database — we defer to krcg.org. Individual card pages only for "problem" cards.
- No original-text rule translations — English quotes verbatim.
- No search engine tooling in phase 1 — `wiki/index.md` suffices until the wiki outgrows it.
- No automated Discord ingestion — user manually curates exports.
- No frontend beyond Obsidian.

## Next step

Invoke the writing-plans skill to produce an implementation plan for scaffolding the wiki (directory creation, `CLAUDE.md` schema, initial `index.md` / `log.md`, `.gitignore`, initial git commit).
