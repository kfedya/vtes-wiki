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
