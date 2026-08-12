# Current implementation scope

Completed at this stage:

- reproducible project structure and environment files;
- validated completed-match dataset with deterministic `match_id`;
- leakage-safe five-match rolling goals form;
- corrected and validated tournament weights and neutral-venue feature;
- deterministic pre-match Elo calculation;
- same-day Elo batching when kick-off order is unavailable;
- one-to-one Elo merge using `match_id`;
- chronological forecast evaluation with a 2023 holdout;
- training-only standardisation;
- explicit checks that training and testing dates do not overlap.

## Current evaluation split

The modern modelling slice contains 25,157 matches.

- Training: 21,712 matches from 2000-01-04 through 2022-12-30
- Testing: 3,445 matches from 2023-01-02 through 2026-03-31

The existing SVM and MLP models now use this chronological split. Their final replacement/comparison is intentionally reserved for the next commit.

## Known issues reserved for later commits

- the full RBF SVM is slow;
- draw prediction is weak in the original model;
- final model comparison and probability metrics are incomplete;
- simulation inputs are still dummy values rather than team-specific states;
- the tournament demonstration remains hard-coded to four teams;
- literature claims still exceed the implemented feature set;
- placeholder notebook headings remain for later cleanup.
