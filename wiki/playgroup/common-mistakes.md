---
type: playgroup
tags: [playgroup, common-mistakes, combat, sce, aim-cards, damage-rider]
sources: [src-002, src-003]
last_verified: 2026-04-19
status: verified
---

# Common Playgroup Mistakes

Running list of rules errors — ours, and common community ones — we've hit. Each entry deep-links from the related ruling page via `[[common-mistakes#<slug>]]`.

## aim-cards-on-combat-ends-with-damage-rider — Target Vitals on Catatonic Fear [PRE]

**What we were doing:** assuming that Target Vitals does nothing when played on a combat-ends strike, because the strike "does no damage" and the krcg Target Vitals ruling says it "has no effect" on such strikes.

**What's actually correct:** When the combat-ends strike carries a damage rider (superior [Catatonic Fear](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Catatonic%20Fear), superior [Loving Agony](https://codex-of-the-damned.org/en/card-search/library/index.html?card=Loving%20Agony)), the rider damage **is** damage from that strike. If it lands, Target Vitals adds **+2 damage**. Rules Director Ankha and rules coordinator Pascal Bertrand explicitly confirmed this in [PIB 20130319](https://www.vekn.net/forum/rules-questions/46164-catatonic-fear-and-loving-agony) [src-003].

**Numbers at close range, superior [PRE] Catatonic Fear:**
- Alone: 1 unpreventable damage after combat.
- With Target Vitals: 1 + 2 = **3 unpreventable damage** after combat.
- Dodged: 0 — dodge cancels the rider damage on the dodger; combat still ends (combat-ends is not "directed at the dodger") [RTR 20041202] [LSJ 20070124] [src-002].
- Basic [pre] Catatonic Fear (no rider) + Target Vitals: 0 — the krcg "has no effect" ruling correctly applies here.

**First noticed:** 2026-04-18 (caught by kfedya after I gave a wrong answer in chat; corrected after `WebFetch` of the forum thread and `POST api.krcg.org/twda/list` returning 4 tournament-winning decks that pack both cards, one of them literally named *Fearful Vitals*).

**Related rulings:**
- [[strike-effects#combat-ends-with-a-damage-rider]] — general rule for `Strike: End combat and do X`.
- [[wiki/cards/catatonic-fear|catatonic-fear]] — full card page with rulings breakdown.

**Lesson for LLM sessions:** if a krcg ruling reads "has no effect", **check which case it covers** before generalising. The Target Vitals ruling [RTR 19960221] [PIB 20130319] covers strikes that truly inflict no damage (basic-level SCE, dodges) — not SCE with a damage rider. When in doubt, `WebFetch` the referenced forum thread.

## dodge-vs-combat-ends-on-sce — "Dodge defeats the whole SCE strike"

**What we (and many players) say loosely:** "Dodge cancels Catatonic Fear / Majesty / any SCE strike."

**What's actually correct:** Dodge **does not cancel "combat ends"** — combat-ends is not directed at the dodger, so it still resolves and combat ends. Dodge only cancels effects of the opposing strike that are **directed at the dodging minion** — for Catatonic Fear [PRE] that's the 1-unpreventable-damage rider [src-001 p. 33] [LSJ 19980526] [RTR 20041202] [LSJ 20070124] [src-002].

**Verbatim from RTR 20041202** (LSJ, group `WUWh7AdooDU/m/vojisZMCSnsJ` on `groups.google.com/g/rec.games.trading-cards.jyhad`):

> Dodge protects the dodger from the effects of the opposing minion's strike, even if that strike is done at First Strike or even if it is a Combat Ends strike (Combat Ends will still end combat, but any additional effects the strike would have on the dodger, like Catatonic Fear's damage, are dodged).

**Verbatim from LSJ 20070124** (group `5YMceht1KTk/m/LhhbEr_dlU8J`):

> Yes. Well, it avoids the damage (the damage is never applied, rather than being applied and prevented).

**Why this matters in practice:**
- A vampire dodging Catatonic Fear takes 0 damage **and** combat ends — they cannot then act this combat round, fish for press, retain hand, etc. Combat is over.
- Sibling strikes already in flight (e.g. simultaneous normal strike from the dodger) still resolve at the moment combat is ending, but no further rounds.
- **Real cancellers of "combat ends"** are cards that interrupt or restart combat — `Psyche!` [CEL], `Telepathic Tracking` [AUS] — not dodges.

**First noticed:** 2026-04-19 (caught by kfedya pushing back on my answer "dodge cancels combat ends"; corrected after `curl`-ing the raw Google Groups HTML and reading the LSJ replies in context).

**Related rulings:**
- [[strike-effects#dodge]] — general rule that dodge does not cancel combat ends.
- [[strike-effects#combat-ends-with-a-damage-rider]] — SCE rider behaviour.
- [[wiki/cards/catatonic-fear|catatonic-fear]] — full card page.

**Lesson for LLM sessions:** when the user pushes back on a strike-effects ruling, do not paraphrase loosely (e.g. "dodge defeats the whole strike"). Pull the exact forum quote — `card-db/library/<type>.json` already stores the source URL in `rulings[].references[].url`. `curl -sSL <url>` and `grep` for the term; the raw Google Groups HTML preserves the inline text even when the SPA shows a login wall.
