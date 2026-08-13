# Literature review and final implementation alignment

The PDF in `literature/25200786_Literature_Review.pdf` is retained as the original literature-review submission. It describes several methods and data sources that were considered during project planning but were not all implemented in the final notebook.

This note separates literature context from the final model.

## Implemented from the literature direction

The final project uses:

- historical international match results
- Elo ratings
- recent team form
- match context through tournament importance and neutral venue
- probabilistic model evaluation
- calibration diagnostics
- Monte Carlo tournament simulation
- a 48-team-style tournament structure

These elements remain consistent with the review's broad motivation around dynamic team strength, calibration and tournament-level uncertainty.

## Planned ideas that are not final model inputs

The original review also discusses or describes:

- FIFA ratings
- bookmaker odds
- player-level squad ratings
- Transfermarkt market values
- host/geographic advantage scores
- climate similarity
- travel distance
- GDP and other macroeconomic indicators
- XGBoost as the project classifier

Those items are not used by the final implementation.

The final feature vector contains Elo, five-match goals-for and goals-against form, tournament weight and neutral-venue status. The final learned candidates are a Linear SVM and histogram gradient boosting, with the probability model selected after temporal calibration.

## Historical range

The raw results file contains matches back to the nineteenth century, but the final modelling period begins in 2000. This keeps the training data closer to contemporary international football while preserving the full source dataset in the repository.

## Tournament claim

The simulator follows a 48-team-style structure with 12 groups and a 32-team knockout stage, but it does not reproduce every official FIFA tiebreak, participant-selection or bracket rule. The default demonstration field is the top 48 teams in the current Elo snapshot.

For the final report and poster, implementation claims should follow this alignment note rather than the earlier planned-method wording in the original literature-review PDF.
