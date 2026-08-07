# Rolling team-form feature engineering

## Purpose

The original prototype calculated sensible shifted rolling averages, but joined those values back using only `date` and `team`. Because the source contains a small number of cases where a team appears more than once on the same date, that join could multiply rows.

Commit 4 retains the deterministic `match_id` created in Commit 3 throughout the feature-engineering pipeline.

## Team-perspective representation

Each match creates exactly two rows:

- a home-team perspective;
- an away-team perspective.

For 25,157 modern-era matches this produces exactly 50,314 team-perspective rows.

## Leakage rule

Recent form is defined as the average goals scored and conceded across the previous five matches available before the current calendar date.

The current match is never included in its own form. When a team has multiple source matches on the same date, every match on that date receives the same form calculated from dates strictly before it. The day's results are added to history only after all of that day's form values have been assigned.

## Join rule

Home and away form lookups each contain one row per `match_id`. They are joined to the validated match table with pandas `validate='one_to_one'`.

The notebook raises an error if:

- either lookup contains duplicate match identifiers;
- a form value is missing after the join;
- the feature merge changes the number of matches;
- the final modelling table contains duplicate `match_id` values.

## Expected result

- modern-era matches: 25,157;
- team-perspective rows: 50,314;
- same-day team/date groups handled: 7;
- final modelling rows: 25,157;
- unique final `match_id`: 25,157;
- rows added or lost: 0.

This commit changes rolling-form construction only. Later modelling and tournament-simulation issues remain intentionally unchanged.
