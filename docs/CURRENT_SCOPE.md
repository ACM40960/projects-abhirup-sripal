# Final project scope

The implemented pipeline includes:

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
- retrospective 2026 World Cup match-level validation
- bootstrap uncertainty for the 104-match backtest
- actual-field stage-progression validation

The final probability model is selected after calibrating both learned candidates under the same temporal evaluation design.

The post-tournament analysis is isolated from model development: tournament outcomes are used for evaluation only and are not used to retrain, retune or reselect the model.

The remaining limitations are methodological rather than unfinished code. The model does not use bookmaker odds, player-level data, FIFA ratings, geography or climate; it predicts outcomes rather than scorelines; and the tournament mechanics are an approximation rather than an exact FIFA implementation.
