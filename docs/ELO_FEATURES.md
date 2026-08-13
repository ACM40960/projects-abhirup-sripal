# Pre-match Elo feature engineering

Elo is carried through the pipeline with the permanent `match_id`, avoiding the earlier fixture-key merge on date and team names.

For each historical match, `home_elo` and `away_elo` are the ratings available before that result is applied. New teams begin at 1500.

The update size follows the project assumption:

```text
K = 30 x match_weight
```

Tournament importance is defined in `TOURNAMENT_WEIGHTING.md`.

## Same-day matches

A few teams appear more than once on the same calendar date, while the dataset does not provide reliable kick-off ordering. The Elo calculation therefore works in date batches:

1. snapshot ratings before the date
2. assign those ratings to every match on that date
3. calculate each match's rating change
4. accumulate changes by team
5. apply them after all matches on the date have been evaluated

This prevents arbitrary CSV row order from leaking one same-day result into another match's pre-match rating.

## Integrity checks

The notebook verifies one Elo row per modern match, unique identifiers, no missing values after the one-to-one merge, unchanged model row counts and consistent pre-date ratings for repeated same-day appearances.
