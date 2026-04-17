---
type: ruling
tags: [overview, setup, turn-sequence, golden-rule, glossary]
sources: [src-001]
last_verified: 2026-04-18
status: draft
---

# Game Overview

## Summary
VTES is a multiplayer (4–5) customisable card game where each player is an ancient vampire (a **Methuselah**) commanding younger vampires and allies to destroy the **influence** of rival Methuselahs. Influence is tracked by **pool counters**; a player runs out of pool, they are ousted and award a victory point to the Methuselah who ousted them [src-001].

## Object of the Game
- Accumulate the most **victory points (VP)** by ousting rival Methuselahs [src-001].
- A Methuselah is ousted when their pool hits 0.
- When your prey is ousted, the next Methuselah to your left becomes your new prey.
- Winner at game end is the Methuselah with the most VPs.

## Table Positions
- Seating is arbitrary. One Methuselah is randomly chosen to act first.
- The Methuselah to your left is your **prey** — the one you want to oust.
- The Methuselah to your right is your **predator** — the one trying to oust you.

## Turn Sequence (five phases, clockwise) [src-001]
1. **Unlock Phase** — unlock all your cards; resolve contests; if you hold the Edge, gain 1 pool from the blood bank.
2. **Master Phase** — play regular master cards as master phase actions.
3. **Minion Phase** — your minions take actions (bleed, block-and-combat, etc.). Usually the longest phase.
4. **Influence Phase** — move pool/transfers to bring uncontrolled vampires into the ready region.
5. **Discard Phase** — one discard-phase action (discard one card / draw one, or in advanced play, play an event).

See `[[card-types/library#Drawing Cards]]` for replacement draws. Full phase mechanics arrive in later ingest stages.

## Play Area
Each Methuselah's area is divided into:
- **Uncontrolled region** — face-down crypt cards waiting to be influenced.
- **Controlled region**, split into:
  - **Ready region** — face-up, usable minions.
  - **Torpor region** — wounded vampires (blood=0 or sent there by damage).

Central area holds the **blood bank** and the **Edge token**.

## Components [src-001]
- The rulebook itself.
- 5 preconstructed decks (Malkavian, Nosferatu, Toreador, Tremere, Ventrue), each 89 cards = 12 crypt + 77 library.
- 180 pool counters.
- 1 Edge token.
- 5 help sheets.

### Counters = Pool / Blood / Life
Physically identical, but named by location [src-001]:
- On a Methuselah: **pool** (main currency).
- On a vampire: **blood**.
- On an ally: **life**.
Moving a counter changes its name: pool→vampire = pool becomes blood; blood→ally = blood becomes life.

When a counter is **burned**, **paid**, or **spent**, it returns to the blood bank. When you **gain** 1, you take from the bank. Blood added to a vampire always comes from the bank.

Dice are discouraged — counters move around constantly.

### The Edge
A small physical token (figurine, trinket). Starts uncontrolled in the central area. Whoever holds the Edge gains 1 pool at the start of their unlock phase [src-001].

## Deck Construction
- **Crypt:** at least 12 cards. No upper bound. All vampires must belong to a single group or two consecutive groups (Advanced Rules) [src-001].
- **Library:** 60–90 cards.
- Any number of copies of any card is allowed within those totals.

## Game Setup [src-001]
1. Determine seating and first player.
2. Each Methuselah takes 30 pool counters; rest go to the central blood bank.
3. Place the Edge uncontrolled in the center.
4. Separate crypt from library. Shuffle each. Let your predator cut both.
5. Draw 7 library cards → your hand (starting hand size = 7).
6. Deal 4 crypt cards face-down into your uncontrolled region.

You may look at cards in your hand and uncontrolled region at any time.

## Important Terms
- **Burn** — send a card to its owner's **ash heap** (discard pile). Counters go back to the blood bank. Cards/counters on a burned card are burned with it. Ash heap is public.
- **Remove from game** — unlike burn, these cards cannot be retrieved by any effect.
- **Control** — the Methuselah who put the card in play controls it (with exceptions for minion cards, which are controlled by the controller of the minion they are on).
- **Ownership** — cards you started the game with are yours and return to you at game end. Ownership never transfers.
- **Locking / Unlocking** — turn a card sideways 90° to lock it (once used). Only **unlocked** minions can act or block.

## The Golden Rule for Cards
> Whenever the cards contradict the rules, the cards take precedence. [src-001]

This is why ruling pages exist: cards create exceptions that need documenting.

## Wording Templates
- **"During X, do Y"** — you may do Y only once per X with this card. E.g., Vessel moves 1 blood per unlock phase, not more.
- **"Lock X to do Y"** — requires X to be unlocked; locked minions cannot pay this cost.
- **"Search your library/crypt"** — you do not have to announce the card; you may fail to find it; you must shuffle after searching.
- **"Cancel a card"** (Advanced) — the cancelled card is still considered played:
  - Cancelled **action card** → the minion does not lock and can play another action card.
  - Cancelled **non-action card** → cost is still paid as normal.
  - Cancelled **combat strike card** → the striker must choose another strike (may come from a different strike card).

## Sequencing (advanced)
When multiple Methuselahs want to play cards/effects at the same point, the **acting Methuselah** always has first **impulse**. After they pass, impulse passes to:
- **Combat or directed action against one Methuselah:** defender first.
- **Action against a set of Methuselahs:** those Methuselahs clockwise.
- **Undirected action:** prey first, then predator.

Then every remaining Methuselah gets a turn clockwise. Any time someone actually plays a card, impulse returns to the acting Methuselah [src-001].

## Sources
- src-001 — VTES Fifth Edition Rulebook, Black Chantry, October 2023. Pages 1–16 (Introduction, Object, Components, Playing the Game, Important Terms).
