# Commit 6 checklist: pre-match Elo integrity

## Files changed

- `notebooks/world_cup_predictor.ipynb`
- `README.md`
- `docs/CURRENT_SCOPE.md`
- `docs/PROJECT_PLAN.md`

## Files added

- `docs/ELO_FEATURES.md`
- `docs/COMMIT_06_CHECKLIST.md`
- `outputs/elo_validation.csv`
- `outputs/final_elo_ratings.csv`

## Requirements completed

- [x] Keep `match_id` throughout Elo calculation
- [x] Record Elo before each match result is applied
- [x] Use corrected Commit 5 match weights in the Elo K-factor
- [x] Handle same-day repeated teams without arbitrary within-day leakage
- [x] Produce exactly one Elo row per match
- [x] Merge Elo using `match_id`
- [x] Enforce `validate="one_to_one"`
- [x] Remove silent `dropna()` handling from the Elo merge
- [x] Raise explicit errors for missing Elo values or row-count changes
- [x] Save final team ratings and validation outputs
- [x] Clear notebook outputs before commit

## Scope note

The random 80/20 split and original RBF SVM are intentionally retained. Chronological evaluation is the next commit.
