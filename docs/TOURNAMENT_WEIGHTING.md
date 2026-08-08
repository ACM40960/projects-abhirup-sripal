# Tournament weighting

## Purpose

Commit 5 corrects the tournament-weighting function used by the current predictor. The dataset records the competition as `Copa América` with an accented character, while the earlier function searched for the unaccented string `Copa America`. As a result, the 248 modern-era Copa América matches were previously assigned the generic weight 0.4 rather than the intended major-tournament weight 0.8.

## Weight rules

| Competition type | Weight |
|---|---:|
| FIFA World Cup (non-qualification) | 1.00 |
| Confederations Cup / Copa América / Euro (non-qualification) | 0.80 |
| Qualification competitions | 0.60 |
| Nations League | 0.50 |
| Other competitions | 0.40 |
| Friendly matches | 0.25 |

The function normalises case and removes accents before matching. Therefore `Copa América` and `Copa America` are treated identically. The qualification check is applied to the whole major-final condition rather than relying on Python's `and`/`or` precedence.

## Validation

Using the current `data/results.csv`, the modern-era slice contains exactly **248 Copa América matches**. Commit 5 validates that all 248 receive weight **0.8** and none receive weight 0.4. The full tournament/weight frequency table is saved to `outputs/tournament_weight_validation.csv`.

## Scope boundary

This commit changes tournament-weight assignment and its validation only. The Elo calculation and its `(date, home_team, away_team)` merge remain unchanged and are reserved for Commit 6. Chronological train/test evaluation and team-specific tournament prediction are also reserved for later commits.
