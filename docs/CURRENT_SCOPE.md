# Current implementation scope

At this repository stage, the project contains:

- reproducible repository and Anaconda environment files;
- required-column validation for `results.csv`;
- consistent date and score parsing;
- removal of incomplete completed-match outcomes;
- exact-duplicate checks and duplicate match-key reporting;
- deterministic unique `match_id` values;
- machine-readable validation outputs;
- the original prototype modelling stages for rolling form, tournament weights, Elo, SVM, MLP and a four-team Monte Carlo demonstration.

## Validation result

- source rows: 49,287;
- missing-score rows removed: 72;
- invalid-date rows: 0;
- exact duplicates removed: 0;
- completed validated matches: 49,215;
- matches from 2000 onward: 25,157.

## Known issues reserved for later commits

- the rolling-feature merge can duplicate modelling observations;
- random train-test splitting is not suitable for forecasting;
- the full RBF SVM is slow;
- simulation inputs are not team-specific;
- the tournament demonstration is not the complete 2026 format;
- the literature review includes features not implemented in the notebook.
