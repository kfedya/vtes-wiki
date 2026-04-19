---
type: tournament
tags: [tournament, vekn, scoring, victory-points, game-wins, tie-breakers, withdraw]
sources: [src-032, src-001]
last_verified: 2026-04-19
status: draft
---

# Tournament Scoring

How VEKN-sanctioned tournaments score games, rank players, advance to the final, and decide the tournament winner [src-032 §3.1, §3.7, §3.7.1–§3.7.5].

## The three scoring quantities [src-032 §3.7]

1. **Game Wins (GW)** — awarded once per game to the player who clearly won the game.
2. **Victory Points (VP)** — accumulated for ousts, survival, and (in tournaments) half for withdrawal.
3. **Tournament Points (TP)** — awarded for the player's *table ranking* at the end of each round.

A tournament report tracks all three across rounds. The trio is also the tie-breaker chain (see below).

## Game Wins [src-032 §3.7.1]

A player receives **1 Game Win** at the end of a game if they have:
- **at least 2 Victory Points**, **and**
- strictly **more Victory Points than any other player** at the table.

Both conditions must hold. **No GW is awarded on ties** at the top of the table (even if the tied players each have 2+ VP).

## Victory Points [src-032 §3.7.2]

A player gains:
- **1 VP** each time their **prey is ousted** during the game (or as otherwise indicated by game rules or card text).
- **0.5 VP** for **withdrawing** during a tournament round — this is the **tournament override** of the basic-rules 1 VP for withdraw [src-001 p. 38, overridden by src-032]. See [[withdraw]].
- **0.5 VP** for **surviving the round when the time limit is reached** without being ousted, **unless** the player is the **last surviving Methuselah at the table**, in which case they receive a full **1 VP** (per the basic ending-the-game rule [src-001 p. 38]).

VPs from cards (e.g., political-action wave finishers) follow the wording of the card, not the tournament rule.

## Tournament Points [src-032 §3.7.3]

Awarded by **table ranking** at the end of the round (highest VP = first place, and so on):

| Place | Five-player table | Four-player table |
| ----- | ----------------- | ----------------- |
| 1st   | 60                | 60                |
| 2nd   | 48                | 48                |
| 3rd   | 36                | **bye = 36** (no third place) |
| 4th   | 24                | 24                |
| 5th   | 12                | 12                |

At a four-player table the empty third-place slot is the **table bye** — players are ranked first, second, fourth, fifth (no one sits in third).

When two or more players tie for a particular table place, **average the TP values** of the tied positions and award that average to each tied player (see examples below).

## Worked examples [src-032 §3.7.4]

### Five-player table

Players A and C each oust one prey. Players B and D are ousted by A and C and oust nobody. Player E ousts nobody but survives at time.

- A and C: 1 VP (oust) + 0.5 VP (survive) = **1.5 VP each**.
- E: **0.5 VP** (survive).
- B and D: **0 VP**.

A and C tie for first place at the table. Average the 1st- and 2nd-place TP values: (60 + 48) / 2 = **54 TP each**. Neither hits 2 VP, and they're tied at the top — **no GW awarded**. E sits cleanly in third = **36 TP**. B and D tie for fourth: (24 + 12) / 2 = **18 TP each**.

### Four-player table

Player A ousts one prey and survives. Player B is ousted by A. Players C and D oust nobody but survive.

- A: 1 + 0.5 = **1.5 VP**.
- C and D: **0.5 VP each**.
- B: **0 VP**.

A finishes alone in first = **60 TP**. C and D tie for second (i.e., the second and *fourth*-place slots, since third is the bye): (48 + 24) / 2 = **36 TP each**. B is fifth = **12 TP**.

## Ranking and advancement to the final [src-032 §3.1]

After preliminary rounds, players are ranked using this **tie-breaker chain**:

1. Game Wins
2. Victory Points (cumulative across preliminary rounds)
3. Tournament Points
4. Any remaining ties for one of the **top five** placements are broken by a fair random method (coin toss, die roll).

The **top five** advance to the final round.

## The final round [src-032 §3.1.3 / §3.7.5]

- **Seating** uses an index-card placement procedure. Each finalist shuffles their crypt and presents it to the judge for additional shuffling and cutting; the judge draws **3 random crypt cards from each finalist** and reveals them publicly until everyone is seated. Then, **starting with the lowest qualifier**, each finalist places their named index card either at one of the row's two ends or **inserts it between two cards already placed**. The final left-to-right order is the seating; the judge then **randomly chooses who plays first**.
- **Winner** = the finalist with the **highest VP scored in the final round only** (preliminary VP do not carry over to deciding the winner).
- **Tie-breaker for the win** = the finalists' **preliminary ranking** (the finalist who entered the final ranked higher wins). All other finalists tie for second; **no further tie-breakers** are applied to the rest of the standings.

## Final scoring example (showing the index-card placement) [src-032 §3.1.3]

Player 5 (lowest qualifier) places her card first:

```
5
```

Player 4 (next-lowest qualifier) places to the right end:

```
5  4
```

Player 3 places to the left end:

```
3  5  4
```

Player 2 inserts between 5 and 4:

```
3  5  2  4
```

Player 1 (highest qualifier) inserts between 2 and 4:

```
3  5  2  1  4
```

Final clockwise seating around the table is read left to right.

## Concession, intentional draw, time-out

- **Concede** — a game can be conceded if all but one player agree, **provided it doesn't violate play-to-win**. The game is recorded as if the surviving player ousted each conceding player in sequence. Bribery / coercion to force a concession is a [[play-to-win]] violation [src-032 §3.5].
- **Intentional draw** — players may agree to an intentional draw at any time before results are submitted. Declined offers don't bind anyone. Result is the same as **playing to time** (everyone alive at the end gets 0.5 VP for survival; sole survivor gets 1) [src-032 §3.6].
- **Time** — minimum round length is **2 hours**. When the round is called, the game ends with the **current minion action** (if there is one) or at the end of the **current phase** if the call happens outside the minion phase [src-032 §3.1.1].

## Conflicting Rulings

None on this page. Treat src-032 as authoritative for tournament scoring; treat src-001 as authoritative for non-tournament play. Where they diverge (withdraw VP), src-032 governs sanctioned events.

## Related Pages

- [[index]] — VEKN tournament rules overview and quick-reference table.
- [[banned-cards]] — cards excluded from sanctioned constructed and limited play.
- [[v5-format]] — restricted card pool for the V5 format.
- [[play-to-win]] — sportsmanship + deals + two-player exception + concede / draw context.
- [[../rulings/withdraw]] — basic withdraw mechanic; tournament caps the reward at 0.5 VP.
- [[../rulings/ending-the-game]] — basic-rules ouster + survival VP that the tournament scoring builds on.

## Sources

- src-032 — VEKN Tournament Rules §3.1, §3.7.1–§3.7.5 (Round Structure, Determining a Game Winner, GW / VP / TP scoring, scoring examples, final-round scoring). <https://www.vekn.net/tournament-rules/3-tournament-mechanics>
- src-001 — VTES Fifth Edition Rulebook p. 38 (basic withdraw — 1 VP, overridden by src-032 in tournaments).
