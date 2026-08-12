# Commit 7 checklist: chronological evaluation

## Requirements completed

- [x] Remove random `train_test_split` from the form-only evaluation
- [x] Remove random `train_test_split` from the Elo + form evaluation
- [x] Set a fixed evaluation cutoff of 2023-01-01
- [x] Train only on matches before the cutoff
- [x] Test only on matches on or after the cutoff
- [x] Validate that training and testing dates do not overlap
- [x] Validate that every modelling row belongs to exactly one split
- [x] Fit `StandardScaler` on training data only
- [x] Use the same split for form-only and Elo + form models
- [x] Save machine-readable split validation outputs
- [x] Clear notebook outputs before commit

## Expected split

- Total modelling rows: 25,157
- Training rows: 21,712
- Test rows: 3,445
- Training end: 2022-12-30
- Test start: 2023-01-02
- Date overlap: none

## Scope note

Model architecture replacement, expanded probability metrics, team-specific tournament inputs and tournament simulation remain for later commits.

## Commit message

```bash
git commit -m "fix: replace random split with chronological evaluation"
```
