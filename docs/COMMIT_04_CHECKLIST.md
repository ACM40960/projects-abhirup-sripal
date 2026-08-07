# Commit 4 checklist: leakage-safe rolling team form

## Files changed

- `notebooks/world_cup_predictor.ipynb`
- `README.md`
- `docs/CURRENT_SCOPE.md`
- `docs/PROJECT_PLAN.md`

## Files added

- `docs/ROLLING_FORM_FEATURES.md`
- `docs/COMMIT_04_CHECKLIST.md`
- `outputs/rolling_form_validation.csv`

## Requirements completed

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
- [x] Clear notebook outputs before commit

## Expected results

- Modern-era matches: 25,157
- Team-perspective rows: 50,314
- Same-day team/date groups handled: 7
- Final feature-matrix rows: 25,157
- Unique model match IDs: 25,157
- Duplicate model match IDs: 0
- Rows added or lost: 0
- Missing form values: 0

## Scope note

Tournament-weight logic, Elo joins, chronological evaluation, model replacement and team-specific tournament prediction are intentionally left for later commits.

## Commit message

```bash
git commit -m "feat: add leakage-safe rolling team form features"
```
