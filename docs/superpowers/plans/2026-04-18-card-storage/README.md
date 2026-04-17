# Card storage rollout — orchestration plan

Implements `docs/superpowers/specs/2026-04-18-card-storage-design.md`.

## Batches

Batches are designed to run in independent fresh-context sessions. A batch is self-contained: reads its own file, makes all edits, commits, reports. One commit per batch.

| # | File | Scope | Depends on | Optional |
|---|---|---|---|---|
| 0 | `batch-0-foundation.md` | split script, snapshot download, shards, CLAUDE.md, indexes, logs | — | no |
| 1a | `batch-1a-retronorm-turn-actions.md` | card-citation audit in turn-structure + action rulings | 0 | yes |
| 1b | `batch-1b-retronorm-block-politics-combat.md` | block, politics, combat family | 0 | yes |
| 1c | `batch-1c-retronorm-torpor-endgame-cross.md` | torpor, diablerie, endgame, traits, cross-cutting | 0 | yes |
| 1d | `batch-1d-retronorm-entities-lore.md` | sects, card-types, lore, existing problem cards | 0 | yes |
| 2 | `batch-2-enrichment.md` | selective krcg-ruling surfacing into mechanic pages | 0, 1a–d | yes, interactive |

Batches 1a–1d are independent of each other and can run in any order, but all require batch 0.

Batch 2 is interactive (requires user judgment on which krcg rulings to surface) and should NOT be run by an unattended orchestrator.

## Orchestration contract

An orchestrator agent executes batches 0 → 1a → 1b → 1c → 1d sequentially. For each batch:

1. Spawn a fresh worker subagent with the absolute path to the batch file.
2. Worker reads the file, executes all steps, commits, reports back.
3. Orchestrator verifies: new commit landed on master, no uncommitted changes, `git log -1` subject matches the batch's expected commit prefix.
4. If verification fails, HALT and surface status to the user.
5. If OK, move to the next batch.

On completion, orchestrator reports: batches completed, commit SHAs, any warnings.

## Worker agent contract

Each worker is a general-purpose subagent invoked with:

> "Execute the plan at `/absolute/path/to/batch-N.md`. Read the file fully. Follow all steps. Commit as specified. Do NOT modify files outside the scope listed. Report: commit SHA, files touched, any deviations."

Workers MUST NOT:
- skip commits
- modify files outside their declared scope
- run `git push`, `git reset --hard`, or any destructive op
- create new wiki pages beyond what the batch specifies

## Stop conditions

The orchestrator halts on:
- any worker reports failure
- `git status` shows unexpected uncommitted files after a batch
- a commit lands on an unexpected branch

User intervenes, fixes, resumes by re-launching the orchestrator at the next pending batch.

## Re-entry

Re-launch is safe: the orchestrator first checks which batches have already landed (by inspecting `git log` for expected commit subjects) and skips them.
