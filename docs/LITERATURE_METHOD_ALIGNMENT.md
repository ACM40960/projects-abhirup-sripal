# Literature review and final implementation alignment

The original literature review is retained at `literature/Literature_Review.pdf`.

It was written before the final modelling pipeline was fixed, so it includes proposed data sources and methods that were not all implemented. The final report, notebook interpretation and poster should follow the implementation documented in this repository.

## Implemented ideas

The final project uses:

- historical international match results
- Elo ratings
- recent five-match form
- tournament importance and neutral-venue context
- chronological evaluation
- probabilistic model comparison
- temporal calibration diagnostics
- Monte Carlo tournament simulation
- a 48-team-style tournament structure
- retrospective evaluation on the completed 2026 World Cup

These elements remain consistent with the review's broader motivation around dynamic team strength, probabilistic forecasting and tournament uncertainty.

## Discussed or proposed but not implemented

The final model does **not** use:

- FIFA ratings
- bookmaker odds
- player-level squad ratings
- Transfermarkt market values
- geographic advantage scores
- climate similarity
- travel distance
- GDP or other macroeconomic indicators
- XGBoost
- Poisson or hybrid scoreline modelling
- a separate Elo-only probabilistic baseline
- sequential in-tournament Elo/form updating

The implemented learned candidates are a class-balanced Linear SVM and histogram gradient boosting. After temporal calibration, the Calibrated Linear SVM is selected by chronological test-set log loss.

## Historical range

The raw source file extends back to the nineteenth century, but the final modelling period begins in 2000. The earlier records remain in the repository but are not used for model fitting.

## Tournament implementation

The project contains two tournament analyses:

- a generic top-48-Elo demonstration
- a retrospective simulation using the actual 48-team 2026 group field

Neither claims to reproduce every FIFA rule. Group ties use points followed by frozen Elo, the knockout mapping is a transparent approximation, and simulated tournament matchups are treated as neutral.

## Post-tournament validation

The completed 2026 World Cup is used only after model development.

The final selected model and March 2026 team state are frozen before actual tournament outcomes are introduced. This is a retrospective backtest, not a claim that the predictions were timestamped and published prospectively.

## Literature chronology

The original PDF is preserved rather than silently rewritten to match the final code. Additional academic references used during later model evaluation and poster preparation are listed in the README/poster material and were incorporated after the original literature-review stage.
