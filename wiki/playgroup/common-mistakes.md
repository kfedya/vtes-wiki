---
type: playgroup
tags: [playgroup, common-mistakes, combat, sce, aim-cards, damage-rider]
sources: [src-002, src-003]
last_verified: 2026-04-18
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
- Dodged: 0 (dodge defeats the whole strike).
- Basic [pre] Catatonic Fear (no rider) + Target Vitals: 0 — the krcg "has no effect" ruling correctly applies here.

**First noticed:** 2026-04-18 (caught by kfedya after I gave a wrong answer in chat; corrected after `WebFetch` of the forum thread and `POST api.krcg.org/twda/list` returning 4 tournament-winning decks that pack both cards, one of them literally named *Fearful Vitals*).

**Related rulings:**
- [[strike-effects#combat-ends-with-a-damage-rider]] — general rule for `Strike: End combat and do X`.
- [[wiki/cards/catatonic-fear|catatonic-fear]] — full card page with rulings breakdown.

**Lesson for LLM sessions:** if a krcg ruling reads "has no effect", **check which case it covers** before generalising. The Target Vitals ruling [RTR 19960221] [PIB 20130319] covers strikes that truly inflict no damage (basic-level SCE, dodges) — not SCE with a damage rider. When in doubt, `WebFetch` the referenced forum thread.
