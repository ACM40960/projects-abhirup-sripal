# Final project scope

The functional pipeline is complete.

Implemented components include:

- completed-match validation with deterministic `match_id`
- leakage-safe recent form
- corrected tournament weighting
- neutral-venue context
- pre-match Elo ratings with same-day batching
- chronological training and testing
- class-balanced Linear SVM and histogram gradient boosting
- expanding temporal probability calibration
- log loss, multiclass Brier score, per-class recall and confusion matrices
- team-specific current-state features
- neutral-order-symmetric match probabilities
- configurable 48-team-style Monte Carlo simulation

The final probability model is selected after calibrating both learned candidates under the same temporal evaluation design.

The remaining limitations are methodological rather than unfinished code: the model does not use bookmaker odds, player-level data, FIFA ratings, geography or climate; it predicts outcome classes rather than scorelines; and the tournament bracket is a transparent approximation rather than the official FIFA competition implementation.
