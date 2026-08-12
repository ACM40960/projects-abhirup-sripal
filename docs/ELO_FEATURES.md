# Pre-match Elo feature engineering

## Purpose

The original notebook calculated Elo in chronological order but later merged the result using `(date, home_team, away_team)`. That key is not guaranteed to be unique in the source data, and the following `dropna()` could silently remove rows.

Commit 6 carries the permanent `match_id` through the Elo calculation and merges Elo features with `validate="one_to_one"`.

## Pre-match rule

For each match, `home_elo` and `away_elo` are the ratings available before that match's result is applied. New teams begin at 1500.

The Elo K-factor retains the existing project assumption:

```text
K = 30 × match_weight
```

Tournament weighting itself was corrected and validated in Commit 5.

## Same-day matches

The dataset contains a small number of cases where one team appears more than once on a calendar date. There are no kick-off times to establish a reliable within-day order.

Commit 6 therefore processes Elo in date batches:

1. snapshot all ratings before the date;
2. assign those pre-date ratings to every match on that date;
3. calculate each match's Elo change;
4. sum a team's changes for that date;
5. apply the changes only after all matches on the date have been evaluated.

This prevents an arbitrary row order from allowing one same-day result to affect another same-day feature.

## Merge validation

The notebook raises an error if:

- Elo does not produce one row per modern match;
- `elo_features.match_id` is not unique;
- the Elo identifiers differ from the validated match identifiers;
- the merge produces missing Elo values;
- the merge changes the modelling row count;
- duplicate `match_id` values appear after the merge;
- repeated team/date appearances receive different pre-date Elo ratings.

No `dropna()` is used to conceal failed Elo joins.
