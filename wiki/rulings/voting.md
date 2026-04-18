---
type: ruling
tags: [politics, votes, titles, edge, primogen, prince, justicar, inner-circle]
sources: [src-001, src-002]
last_verified: 2026-04-18
status: draft
---

# Gaining Votes

## Summary
Methuselahs have **no inherent votes or ballots**. Votes must be gained. Sources include titled vampires, political action cards, the Edge, and card effects [src-001].

## Sources of Votes

### Political Action Cards
Each political action card used to call a referendum grants the acting vampire's controller **1 vote** (the card's "1 vote" text).

Political action cards can also be **burned from hand** for **1 vote** by any Methuselah during a referendum — but **only once per Methuselah per referendum**. The vote goes to the **Methuselah**, not a vampire [src-001 pp. 28, 46].

Restriction [src-001 p. 46]:
> Can I burn a political action card from my hand for 1 vote during a referendum I called?
> You cannot if the referendum was called with a political action card, since it already provides 1 vote. However, some referendums are called without a political action card (e.g., blood hunt); in that case, every Methuselah can discard a political action from their hand to gain 1 vote.

### Camarilla Titles [src-001]
Only **Camarilla** vampires hold Camarilla titles. Each ready titled vampire grants:
- **1 vote** per ready **primogen**
- **2 votes** per ready **prince** or **baron** (baron = Anarch title; see sect notes below)
- **3 votes** per ready **justicar**
- **4 votes** per ready **Inner Circle** member

**Unique titles** (contested per [[unlock-phase#Contested Titles]]): prince (per city), justicar (per clan), Inner Circle member (per clan), regent (Sabbat), archbishop (per city).
**Non-unique titles:** primogen, baron (each baron is city-specific and contested only if another claims any title to that city), Sabbat bishop, Sabbat priscus, Sabbat cardinal, Laibon magaji, Anarch baron.

### Sabbat Titles (Legacy) [src-001 p. 40]
Only **Sabbat** vampires hold:
- **1 vote** per ready **bishop**
- **2 votes** per ready **archbishop**
- **3 votes** per ready **cardinal**
- **4 votes** for the ready **regent**

The **Prisci Block**: prisci-as-a-group have 3 votes cast by a sub-referendum of ballots. Each ready priscus contributes 1 ballot; the side with more ballots wins the 3 votes; tied = abstain. Votes cannot be used in the sub-referendum. See stage-4 sect ingest for the full mechanic.

### Laibon Titles (Legacy) [src-001 p. 40]
Only **Laibon** hold:
- **2 votes** per ready **kholo** or **magaji**

### Other Titles
- Other minions (non-standard titles) may be worth votes/ballots as listed on card text, without being titled in the standard sense (see stage-4 sect ingest for Legacy sets).
- Some minions have special abilities granting votes/ballots without a title.

### Locked Vampires Still Vote
> A minion's votes and ballots can be used only when the minion is **ready**. Whether or not a minion is locked or unlocked does not have any impact on their ability to vote. [src-001 p. 28]

Vampires **in torpor** cannot cast votes — they must abstain [src-001 p. 34].

### The Edge
The Methuselah holding the Edge can **burn it** (return it uncontrolled to the center) to gain **1 vote** [src-001 p. 28].

> When I burn a political action card for a vote, is that vote coming from the acting vampire?
> No. You (as a Methuselah) gain that vote. Burning the Edge for 1 vote works the same way. [src-001 p. 46]

### Card Effects
Action modifiers, reaction cards, and cards in play that grant additional votes/ballots — subject to normal play rules:
- Only the **acting minion** can play action modifiers during an action.
- Only **ready unlocked minions controlled by other Methuselahs** can play reaction cards.
- [Ventrue Headquarters](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Ventrue%20Headquarters) — **you** gain the votes (Methuselah), not the vampire [src-001 p. 51].

## Vote FAQ [src-001 p. 46]

**Can I play action modifiers to gain votes even if they are not needed?**
Yes. Votes can only be gained during the polling step, but there is no "only if needed" restriction.

**Can I vote against a referendum I called?**
Yes. All your votes (including the 1 from the political action card) can be cast against.

## Title Change Implications [src-001 p. 39]
A vampire can have at most **one title**. If a titled vampire gains a new title, they **lose the first** (even if the new one is a "demotion"). A vampire with a **contested** title immediately yields the contested title when they gain a new one.

A vampire whose clan or sect changes to one inappropriate for their title **loses the benefit** of the title until their clan/sect realigns. If they gain a new title or their title is contested before then, they immediately yield the old title.

### Title-Granting Cards Overwrite Prior Titles
- [Toreador Justicar](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Toreador%20Justicar) — can target a Toreador who is **already titled**. In that case they lose the previous title and become justicar [src-001 p. 51]. The general "one title at a time" rule handles the replacement automatically.

## Common Mistakes
- Letting a vampire **in torpor** cast votes — they cannot.
- Letting a Methuselah burn two separate political action cards from hand during the same referendum — only one per Methuselah per referendum.
- Forgetting that a Methuselah can burn a political action card from hand for +1 vote during a blood-hunt referendum (which has no political action card of its own).
- Thinking locked vampires cannot vote — they can; only torpor prevents voting.
- Treating vote gains from the Edge or political action cards as belonging to the acting vampire — they belong to the **Methuselah**.

## Card-Level Rulings (krcg)
Edge cases surfaced from krcg-embedded `rulings[]` [src-002].

### [Toreador Justicar](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Toreador%20Justicar)
- Only a **Camarilla** vampire can be chosen as the target. The card **cannot be played without a valid target** — i.e., you cannot call the referendum just to fish for votes if no Camarilla Toreador exists in play [src-002, LSJ 20041026].

## Sources
- src-001 — VTES Fifth Edition Rulebook, p. 28 (Gaining Votes), pp. 39–40 (Sects and titles), p. 34 (torpor — abstain), p. 46 (FAQ), pp. 51 (Toreador Justicar, Ventrue Headquarters).
- src-002 — krcg vtes.json snapshot 2026-04-18 (embedded card-level rulings).
