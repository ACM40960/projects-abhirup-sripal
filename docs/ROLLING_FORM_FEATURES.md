# Rolling team-form feature engineering

The rolling-form pipeline uses the deterministic `match_id` introduced in the data-validation stage. Each match creates one home and one away team-perspective row. Recent form is based on the previous five matches and excludes the current result.

When a team has multiple matches on the same calendar date, all matches on that date receive the same form calculated before that date. This avoids using one same-day result to predict another same-day match.

Home and away form are joined back to the match table by `match_id` with one-to-one merge validation. The feature stage must preserve exactly one modelling row per match.

Commit 4 validation results carried into Commit 5:

- modern-era matches: 25,157;
- team-perspective rows: 50,314;
- same-day team/date groups handled: 7;
- final modelling rows: 25,157;
- unique modelling match IDs: 25,157;
- duplicate modelling match IDs: 0;
- rows added or lost by the form merge: 0.

The rolling-form logic is unchanged by Commit 5.
