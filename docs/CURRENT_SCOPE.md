# Current implementation scope

Completed so far:

- Validated match data with deterministic `match_id`
- Leakage-safe five-match rolling form
- Corrected tournament and neutral-venue context
- Pre-match Elo ratings with same-day batching
- One-to-one Elo joins using `match_id`
- Chronological evaluation using a 2023 holdout
- Class-prior baseline
- Class-balanced Linear SVM
- Histogram gradient boosting trained with balanced sample weights
- Temporal probability calibration for the Linear SVM
- Multiclass log loss and Brier evaluation
- Per-class recall and confusion-matrix diagnostics
- Probability-based provisional model selection

## Current modelling position

Linear SVM gives a lightweight linear benchmark, while histogram gradient boosting can capture nonlinear relationships between Elo, form and match context.

Draw performance is now reported explicitly rather than inferred from macro metrics. This matters because the original prototype and the unweighted gradient-boosting comparison both struggled badly with draws.

Still to do: genuine team-specific prediction, configurable tournament simulation, literature-methodology alignment, poster outputs and final cleanup.
