# Current implementation scope

Completed at this stage:

- reproducible project structure and environment files;
- validated completed-match dataset with deterministic `match_id`;
- leakage-safe five-match rolling goals form;
- corrected tournament weights and neutral-venue context;
- deterministic pre-match Elo calculation with same-day batching;
- one-to-one Elo integration using `match_id`;
- chronological forecast evaluation using a 2023 holdout;
- training-only standardisation;
- class-prior baseline;
- class-balanced Linear SVM;
- histogram gradient boosting;
- shared classification comparison using accuracy, balanced accuracy and macro F1.

## Current model evaluation

All active models are evaluated on exactly the same chronological test period. The class-prior dummy classifier provides the minimum benchmark. The Linear SVM provides an efficient linear decision model and histogram gradient boosting provides a nonlinear tabular model.

The old RBF SVM and MLP are no longer part of the active comparison path.

## Still reserved for later commits

- probability calibration;
- multiclass log loss and probability-quality diagnostics;
- final probability-based model selection;
- team-specific prediction states;
- configurable tournament simulation;
- literature-methodology alignment;
- poster/final result generation;
- final clean reproducibility release.
