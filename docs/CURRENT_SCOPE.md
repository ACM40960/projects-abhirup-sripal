# Current implementation scope

At this repository stage, the project contains:

- reproducible repository and Anaconda environment files;
- validated historical match data;
- deterministic unique `match_id` values;
- leakage-safe five-match rolling team-form features;
- strict same-date handling for rolling form;
- one-to-one home/away form joins using `match_id`;
- corrected tournament weighting with case- and accent-normalised matching;
- validation of tournament-weight assignments.

## Commit 5 validation

- modern-era matches: 25,157;
- modern-era Copa América matches: 248;
- Copa América matches assigned weight 0.8: 248;
- Copa América matches assigned weight 0.4: 0.

## Known issues reserved for later commits

- the Elo calculation is still joined back using `(date, home_team, away_team)` rather than `match_id`;
- the Elo merge has no one-to-one validation and is followed by silent `dropna()`;
- random train-test splitting is not suitable for forecasting;
- the full RBF SVM is slow;
- draw detection remains limited in the original models;
- simulation inputs are not yet team-specific;
- the tournament demonstration is not the complete 2026 format;
- the literature review contains features that are not implemented in the current predictor.
