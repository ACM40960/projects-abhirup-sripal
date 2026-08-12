# Current implementation scope

Completed at this stage:

- reproducible project structure and environment files;
- validated completed-match dataset with deterministic `match_id`;
- leakage-safe five-match rolling goals form;
- corrected and validated tournament weights and neutral-venue feature;
- deterministic chronological pre-match Elo calculation;
- same-day Elo batching when kick-off order is unavailable;
- one-to-one Elo merge using `match_id`;
- explicit checks for missing Elo values, duplicate identifiers and row-count changes;
- final team Elo ratings and machine-readable Elo validation outputs.

## Current integrity result

The modern modelling slice contains 25,157 matches. Elo produces exactly 25,157 feature rows and preserves exactly one final modelling row per `match_id`. No Elo values are silently dropped.

## Known issues reserved for later commits

- random train/test splitting is not suitable for forecast evaluation;
- the full RBF SVM is slow;
- draw prediction is weak in the original model;
- simulation inputs are still dummy values rather than team-specific states;
- the tournament demonstration remains hard-coded to four teams;
- literature claims still exceed the implemented feature set;
- placeholder notebook headings remain for later cleanup.
