# Commit 3 checklist: data validation

## Files changed

- `notebooks/world_cup_predictor.ipynb`
- `README.md`
- `docs/CURRENT_SCOPE.md`
- `docs/PROJECT_PLAN.md`

## Files added

- `docs/DATA_VALIDATION.md`
- `outputs/data_validation_summary.csv`
- `outputs/duplicate_match_keys.csv`

## Validation requirements completed

- [x] Required-column checks
- [x] Consistent date parsing
- [x] Numeric score parsing
- [x] Missing-score removal
- [x] Exact-duplicate reporting and removal
- [x] Duplicate date/home/away key reporting
- [x] Deterministic unique `match_id`
- [x] Machine-readable dataset summary output
- [x] Notebook paths tested from repository root
- [x] Notebook paths tested from `notebooks/`
- [x] Notebook outputs cleared before commit

## Expected validation results

- Source rows: 49,287
- Missing-score rows removed: 72
- Invalid date rows: 0
- Exact duplicate rows removed: 0
- Validated completed matches: 49,215
- Modern-era matches from 2000 onward: 25,157
- Unique modern-era match IDs: 25,157

## Scope note

The feature-engineering merge still produces 25,171 modelling rows from 25,157 modern-era matches. This known issue is intentionally left for the next commit, which will rebuild rolling team form using `match_id`.

## Commit message

```bash
git commit -m "feat: validate match data and assign unique identifiers"
```
