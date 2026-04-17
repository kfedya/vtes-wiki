# Batch 0 — Foundation

**Goal:** working `card-db/`, updated CLAUDE.md schema, committed snapshot as `src-002`.

**Depends on:** nothing.

**Commit subject:** `ingest: src-002 card-db snapshot 2026-04-18 + schema v2`

## Preconditions

- Repo at `/Users/kfedya/Desktop/VTES`, branch `master`, clean working tree.
- Internet access for downloading `https://static.krcg.org/data/vtes.json`.
- Python 3 available (`python3 --version`).

## Steps

### 1. Create directory layout

```
mkdir -p raw/card-db-snapshots/scripts
mkdir -p card-db/library
```

### 2. Write the split script

Create `raw/card-db-snapshots/scripts/split.py`:

```python
#!/usr/bin/env python3
"""Split a krcg vtes.json snapshot into per-type shards under card-db/.

Usage:
    python3 split.py <snapshot.json>

Reads the snapshot (JSON array of card objects) and writes:
    card-db/crypt.json           — cards with "Vampire" or "Imbued" in types
    card-db/library/<type>.json  — other cards, sharded by types[0] lowercased, kebab-cased
    card-db/index.json           — metadata: snapshot file, date, counts, multi-type cards
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
CARD_DB = REPO_ROOT / "card-db"
LIBRARY_DIR = CARD_DB / "library"

CRYPT_TYPES = {"Vampire", "Imbued"}


def slugify_type(t: str) -> str:
    """'Political Action' -> 'political-action'."""
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def main(snapshot_path: str) -> None:
    snapshot = Path(snapshot_path)
    cards = json.loads(snapshot.read_text(encoding="utf-8"))
    if not isinstance(cards, list):
        sys.exit(f"Expected JSON array at top level, got {type(cards).__name__}")

    CARD_DB.mkdir(parents=True, exist_ok=True)
    LIBRARY_DIR.mkdir(parents=True, exist_ok=True)

    shards: dict[str, list] = defaultdict(list)
    multi_type: dict[int, list[str]] = {}
    counts: dict[str, int] = defaultdict(int)

    for card in cards:
        types = card.get("types") or []
        if not types:
            sys.exit(f"Card {card.get('id')} has no types; aborting.")

        is_crypt = any(t in CRYPT_TYPES for t in types)
        primary = "crypt" if is_crypt else slugify_type(types[0])
        shards[primary].append(card)
        counts[primary] += 1
        if len(types) > 1:
            multi_type[card["id"]] = list(types)

    # Sort each shard by name for stable diffs.
    for bucket in shards.values():
        bucket.sort(key=lambda c: (c.get("name") or "").lower())

    # Write crypt + library shards.
    for shard, entries in shards.items():
        if shard == "crypt":
            out = CARD_DB / "crypt.json"
        else:
            out = LIBRARY_DIR / f"{shard}.json"
        out.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Write index.
    index = {
        "snapshot_file": snapshot.name,
        "snapshot_date": date.today().isoformat(),
        "total_cards": len(cards),
        "counts_by_shard": dict(sorted(counts.items())),
        "multi_type_cards": {str(k): v for k, v in sorted(multi_type.items())},
    }
    (CARD_DB / "index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    print(f"Wrote {len(cards)} cards across {len(shards)} shards.")
    for k, v in sorted(counts.items()):
        print(f"  {k}: {v}")
    print(f"Multi-type cards: {len(multi_type)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: split.py <snapshot.json>")
    main(sys.argv[1])
```

Make it executable: `chmod +x raw/card-db-snapshots/scripts/split.py`

### 3. Download snapshot

```
curl -sfL https://static.krcg.org/data/vtes.json \
  -o raw/card-db-snapshots/vtes-2026-04-18.json
```

Verify it's a non-empty JSON array:

```
python3 -c "import json, sys; d = json.load(open('raw/card-db-snapshots/vtes-2026-04-18.json')); assert isinstance(d, list) and len(d) > 1000, 'bad snapshot'; print(f'OK: {len(d)} cards')"
```

### 4. Run split script

```
python3 raw/card-db-snapshots/scripts/split.py raw/card-db-snapshots/vtes-2026-04-18.json
```

Expected output: ~4000 cards across 13 shards.

### 5. Update CLAUDE.md

Apply all 10 schema changes per the spec §"CLAUDE.md — required updates". Specifically:

1. **Intro — Three layers → Four layers.** Replace the `## Three layers` section with a four-layer version; add `card-db/` between `raw/` and `wiki/`. Full text:

    ```markdown
    ## Four layers

    1. **`raw/`** — immutable source documents (PDFs, markdown clips, Discord exports, card-database snapshots). LLM **reads only**; never writes or modifies. This is the source of truth.
    2. **`card-db/`** — structured data shards derived deterministically from the latest snapshot in `raw/card-db-snapshots/` via `raw/card-db-snapshots/scripts/split.py`. Not human-curated; regenerated on snapshot ingest. LLM reads for card-text and attribute queries; only the ingest script rewrites these files.
    3. **`wiki/`** — LLM-managed markdown pages. User reads; LLM creates and updates.
    4. **`CLAUDE.md`** (this file) — the schema. Co-evolved.
    ```

2. **Directory rules — add entries.** Add after the existing rules:

    ```
    - `raw/card-db-snapshots/*.json` are immutable — never modify.
    - `card-db/*.json` are regenerated by `raw/card-db-snapshots/scripts/split.py` — never hand-edit. Re-run the script to update.
    ```

3. **Frontmatter `type` enum.** Change the enum line to:

    ```
    type: ruling | entity | card | archetype | mechanic-index | playgroup | lore | meta | collection
    ```

    Keep the rest of the frontmatter block unchanged.

4. **Source authority hierarchy — append clarification.** After the existing tier list, add a paragraph:

    > krcg.org data (`static.krcg.org/data/vtes.json`) includes embedded per-card `rulings[]` with source labels (RTR, LSJ, ANK, krcg). Treat these as krcg-tier. When propagating a ruling into a wiki page, cite both the card-db source (`src-NNN`) and the original reference label quoted by krcg.

5. **Operations — add three entries.** After the existing Lint operation, add:

    5a. `### Card-db snapshot ingest` — the 7-step workflow from the spec §"Operations > Card-db snapshot ingest".

    5b. `### Card view query` — the 5-step single-card assembly workflow from the spec §"Query paths > Single-card view".

    5c. `### Deck-building query` — the 5-step filter workflow from the spec §"Query paths > Deck-building / semantic filter".

6. **Page templates — add two.** After the existing templates, add:

    6a. `### Archetype page (`wiki/archetypes/<slug>.md`)` with the template from the brainstorm (Core idea / Key disciplines and clans / Signature cards / Support / Common variants / Weaknesses / Related rulings / Sources).

    6b. `### Mechanic-index page (`wiki/mechanics-index/<slug>.md`)` with the template (Scope / Cards by type / Query used / Related / Sources).

7. **New subsection "When to create a card page".** Insert before the existing Card page template. Content:

    ```markdown
    ### When to create a card page

    A `wiki/cards/<slug>.md` page is created only when at least one of:

    1. Conflicting rulings exist across sources — the page hosts `## Conflicting Rulings`.
    2. ≥3 distinct rulings AND cited from ≥2 ruling pages — consolidation reduces cross-clicking.
    3. The user explicitly requests a page.

    Default: no page. Card data comes from `card-db`; rulings live on mechanic pages with inline `[Card Name](krcg-url)`.
    ```

8. **"What NOT to do" — add 4 bullets:**

    ```
    - Do not modify files under `raw/card-db-snapshots/`.
    - Do not hand-edit files under `card-db/` — regenerate via the split script.
    - Do not create a `wiki/cards/` page unless one of the three problem-card triggers is met.
    - Do not duplicate card text into wiki pages — cite via card-db + krcg link.
    ```

9. **Cross-links — clarify existing convention.** After the existing "Card references" bullet, add:

    > For card references without a dedicated wiki page, link to krcg using the query-URL form already used in existing pages: `[Card Name](https://codex-of-the-damned.org/en/card-search/library/index.html?card=<URL-encoded-Name>)` for library cards, `/crypt/index.html?card=...` for crypt. URL-encode spaces as `%20`. Example: `[Theft of Vitae](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Theft%20of%20Vitae)`. `card-db` entries include the krcg image URL and can be used to confirm card name spelling when ambiguous.

10. (Intentionally empty — item 10 is `wiki/index.md`, handled in step 7 below.)

### 6. Update `raw/index.md`

Add under `### Rulebooks` (or create a new `### Card databases` section if preferred — new section is cleaner):

```markdown
### Card databases

## src-002 — krcg vtes.json snapshot 2026-04-18
- type: krcg-snapshot
- date: 2026-04-18
- author_or_channel: krcg.org (Lionel Panhaleux et al.)
- topic: Full VTES card data — names, types, disciplines, costs, card_text, embedded rulings.
- url: https://static.krcg.org/data/vtes.json
- added: 2026-04-18
- pages_touched: [card-db/, CLAUDE.md, wiki/index.md, wiki/log.md, wiki/meta/backlog.md]
```

### 7. Update `wiki/index.md`

Under `## Archetypes` (currently empty): leave `_(no pages yet)_` — archetype pages aren't created in this batch.

Add new section `## Mechanics Index` near the bottom:

```markdown
## Mechanics Index

_(no pages yet)_
```

Add new section `## Card Database` at the bottom:

```markdown
## Card Database

Structured card data lives outside `wiki/` — see `card-db/` (derived from src-002 snapshot 2026-04-18). Query via the card-view and deck-building operations in CLAUDE.md.
```

Bump the top line: `Last updated: 2026-04-18 | Pages: 60 | Sources: 2`.

### 8. Update `wiki/log.md`

Append:

```
## [2026-04-18] ingest src-002 | krcg vtes.json snapshot — card-db v1 established, schema v2
```

### 9. Resolve backlog item

In `wiki/meta/backlog.md`, move the "[2026-04-17] Card-page storage model" entry from `## Open questions` to `## Resolved items` with a resolution line:

```markdown
### [2026-04-17→2026-04-18] Card-page storage model — RESOLVED
See `docs/superpowers/specs/2026-04-18-card-storage-design.md`. Rolled out as src-002 (card-db snapshot) + schema v2 (four-layer arch, tightened problem-card trigger, new archetype/mechanic-index types).
```

Bump `last_verified`.

### 10. Commit

```
git add raw/card-db-snapshots/ card-db/ CLAUDE.md raw/index.md wiki/index.md wiki/log.md wiki/meta/backlog.md
git commit -m "ingest: src-002 card-db snapshot 2026-04-18 + schema v2

Establishes card-db/ as a derived fourth layer sourced from
static.krcg.org/data/vtes.json, sharded by card type. Adds
archetype and mechanic-index page types. Tightens problem-card
page trigger to three explicit conditions.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

## Postconditions

- `card-db/crypt.json` exists with ~1500 entries.
- `card-db/library/` contains 10–12 shard files.
- `card-db/index.json` shows correct counts and lists multi-type cards.
- `CLAUDE.md` has all 10 changes applied.
- `git log -1` subject matches the expected commit message.
- `git status` is clean.

## Verification

Run these and confirm expected results:

```
jq '. | length' card-db/crypt.json              # > 1000
ls card-db/library/*.json | wc -l               # 10-12
jq '.total_cards' card-db/index.json            # > 3000
grep -c 'Four layers' CLAUDE.md                 # >= 1
grep -c 'archetype | mechanic-index' CLAUDE.md  # 1
git log -1 --format=%s                          # starts with "ingest: src-002"
git status --porcelain                          # empty
```
