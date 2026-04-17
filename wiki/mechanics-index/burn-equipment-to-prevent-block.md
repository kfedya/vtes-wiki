---
type: mechanic-index
tags: [equipment, stealth, block-prevention, burn-cost]
sources: [src-002]
last_verified: 2026-04-18
status: verified
---

# Burn Equipment to Prevent Block — Card Index

## Scope

Equipment cards whose printed effect **prevents or sidesteps a block on an action the bearer is performing**, with a `burn this equipment` cost.

Excluded:
- Equipment that bars specific clans/types from blocking as a passive effect (no burn cost) — e.g., Cloak of the Abalone, The Signet of King Saul.
- Equipment that cancels **combat** after a block has already happened but does not roll the action back — that's a different mechanic (see Related → Canopic Jar).
- Equipment that burns **on** being blocked without preventing the block — e.g., Unlicensed Taxicab.

## Cards by type

### Equipment

- [Concoction of Vitality](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Concoction%20of%20Vitality) — burn at action announcement to make the action unblockable by vampires; bearer loses discipline-card access for the action. Unique.
- [Flaming Candle](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Flaming%20Candle) — burn the equipment **and** 1 blood at action announcement to make the action unblockable by vampires. One per game total across all Methuselahs.
- [Ambulance](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Ambulance) — vehicle; after a combat with the blocker, lock Ambulance to continue the action as if unblocked. If blocked again, Ambulance burns. Soft version — doesn't cancel the block itself, resets consequences.

## Query used

Reproducible against the current snapshot in `card-db/`:

```
jq '.[] | select(
    (.card_text | test("burn.*block|unblockable|cannot.*block|block.*cancel|cancel.*block|prevent.*block|continue.*unblocked|as if unblocked"; "i"))
    and
    (.card_text | test("burn"; "i"))
  ) | {name, text: .card_text}' card-db/library/equipment.json
```

Raw filter returns 5 hits (Ambulance, Canopic Jar, Concoction of Vitality, Flaming Candle, Polaris Coach). Manual semantic pass drops **Polaris Coach** (false positive: `burn` and `cannot block` refer to the bearer's own blocking, not block prevention) and **Canopic Jar** (prevents combat from the blocker's side — listed under Related instead).

## Related

- [Canopic Jar](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Canopic%20Jar) — opposite direction. Equipped on the **blocker**; burn before block resolution to cancel combat and unlock. Serpentis-gated.
- [[stealth-modifiers]] — core rules for stealth-vs-intercept and block-window mechanics.
- [[block-resolution]] — when a block can be prevented vs cancelled.

## Sources

- src-002 — krcg vtes.json snapshot 2026-04-18 (embedded card data).
