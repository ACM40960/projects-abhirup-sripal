# Current implementation scope

At this repository stage, the project contains:

- reproducible repository and Anaconda environment files;
- required-column validation for `results.csv`;
- consistent date and score parsing;
- removal of incomplete completed-match outcomes;
- exact-duplicate checks and duplicate match-key reporting;
- deterministic unique `match_id` values;
- machine-readable validation outputs;
- leakage-safe five-match rolling goals-for and goals-against features;
- strict same-date handling so one match on a date cannot inform another match on that date;
- one-to-one home and away feature joins using `match_id`;
- the original later prototype stages for tournament weights, Elo, SVM, MLP and a four-team Monte Carlo demonstration.

## Current validation result

- source rows: 49,287;
- missing-score rows removed: 72;
- completed validated matches: 49,215;
- matches from 2000 onward: 25,157;
- team-perspective rows: 50,314;
- same-day team/date groups handled without leakage: 7;
- final modelling rows after rolling-form joins: 25,157;
- unique modelling `match_id` values: 25,157;
- rows added or lost by the rolling-form merge: 0.

## Known issues reserved for later commits

- tournament importance conditions need explicit, case-normalised logic;
- the Elo merge still needs to be tied directly to `match_id`;
- random train-test splitting is not suitable for forecasting;
- the full RBF SVM is slow;
- draw detection is weak in the original models;
- simulation inputs are not team-specific;
- the tournament demonstration is not the complete 2026 format;
- the literature review includes features not implemented in the notebook.
