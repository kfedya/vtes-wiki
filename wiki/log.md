# Wiki Log

Append-only chronology of wiki activity. Each entry starts with `## [YYYY-MM-DD] <op> | <short description>` so `grep "^## \[" log.md` yields a clean timeline.

## Operations

- `init` — wiki scaffolded
- `ingest src-NNN` — new source integrated into the wiki
- `query` — significant question answered; may result in a new page
- `lint` — health-check pass

---

## [2026-04-17] init | Wiki scaffolded from brainstorm spec (docs/superpowers/specs/2026-04-17-vtes-wiki-design.md)

## [2026-04-17] ingest src-001 | VTES 5E Rulebook — stage 1 foundations (pp. 1–16) — touched 12 pages

## [2026-04-17] ingest src-001 | VTES 5E Rulebook — stage 2 phases & action resolution (pp. 17–28, FAQ pp. 46–52) — touched 18 pages; renamed card-types/political-action.md → political-action-card.md

## [2026-04-17] ingest src-001 | VTES 5E Rulebook — stage 3 combat, torpor/diablerie, influence/discard, game-end, sects, traits (pp. 29–45, FAQ combat/ouster rulings) — touched 21 pages (19 new + 2 updates)

## [2026-04-17] ingest src-001 | VTES 5E Rulebook — stage 4 FAQ card rulings (pp. 46–52) — touched 22 pages (10 new + 12 updates); rulings grouped by mechanic rather than per-card; backlog item filed about card-storage model

## [2026-04-18] ingest src-001 | VTES 5E Rulebook — stage 5 lore glossary + quick reference (pp. 45, 53) — touched 5 pages (2 new + 3 updates); opens lore/ layer; clan/discipline entity stubs deferred to backlog pending krcg source; src-001 fully ingested

## [2026-04-18] ingest src-002 | krcg vtes.json snapshot — card-db v1 established, schema v2

## [2026-04-18] query | "all equipment that prevent a block at burn-cost" — filed as wiki/mechanics-index/burn-equipment-to-prevent-block.md; first mechanic-index page; validates end-to-end card-db query path (jq + regex + semantic cleanup)

## [2026-04-18] query | "core 5E discipline stubs from card-db" — filed 9 new wiki/entities/disciplines/*.md pages

## [2026-04-18] query | "core 5E clan stubs from card-db" — filed 5 new wiki/entities/clans/*.md pages; closes clan/discipline entity-stub backlog item

## [2026-04-18] query | "legacy vampire disciplines stubs from card-db, part 1" — filed 10 new wiki/entities/disciplines/*.md pages (abombwe, chimerstry, daimoinon, dementation, melpominee, mytherceria, necromancy, obeah, oblivion, obtenebration)

## [2026-04-18] query | "legacy vampire disciplines stubs from card-db, part 2" — filed 10 new wiki/entities/disciplines/*.md pages (protean, quietus, sanguinus, serpentis, spiritus, temporis, thanatosis, valeren, vicissitude, visceratika)

## [2026-04-18] query | "Imbued virtues + discipline-code investigation (str, mal, viz, flight)" — filed 9 new wiki/entities/disciplines/*.md pages (defense, innocence, judgment, martyrdom, redemption, vengeance, vision + combo-code stubs striga, maleficia); updated traits.md with FLIGHT card-db representation; closes the discipline-stub front

## [2026-04-18] query | "V5 + major legacy vampire clan stubs from card-db" — filed 9 new wiki/entities/clans/*.md pages (brujah, gangrel, banu-haqim, lasombra, ministry, ravnos, salubri, tzimisce, hecata)
