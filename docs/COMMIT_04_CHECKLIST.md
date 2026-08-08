# Commit 4 checklist: leakage-safe rolling team form

- [x] Retain `match_id` in home and away team perspectives
- [x] Create exactly two team-perspective rows per match
- [x] Use previous five matches only
- [x] Exclude current-match result from its own form
- [x] Prevent same-day match leakage
- [x] Join home form by `match_id`
- [x] Join away form by `match_id`
- [x] Enforce one-to-one merge validation
- [x] Preserve exactly one modelling row per match
- [x] Write machine-readable validation output

Commit 4 result: 25,157 final modelling rows from 25,157 validated modern-era matches, with zero duplicate match IDs and zero rows added or lost.
