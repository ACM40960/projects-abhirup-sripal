# Post-tournament validation of the 2026 World Cup

The retrospective evaluation layer runs after the completed tournament and does not modify the selected classifier, calibration procedure or model-selection rule.

## Freeze rules

The backtest enforces the following constraints:

- final probability model remains the selected Calibrated Linear SVM
- classifier training remains on matches before 1 January 2023
- the existing chronological holdout remains unchanged
- the Elo/form state uses completed project data only through 31 March 2026
- World Cup outcomes are never used for retraining, retuning or model reselection
- every World Cup fixture is predicted from the same frozen pre-tournament state

This is a retrospective backtest of a frozen project snapshot, not a prospective forecast archive.

## Probability-first evaluation

The historical holdout already showed that Draw is rarely the model's argmax class even when the assigned draw probability is meaningful.

The World Cup analysis therefore leads with multiclass log loss, multiclass Brier score, draw-rate versus mean predicted draw probability, and bootstrap uncertainty. Accuracy and the confusion matrix remain secondary diagnostics.

## Small-sample uncertainty

A World Cup contains only 104 matches. The analysis uses 5,000 bootstrap resamples with seed 2026 and reports 95% percentile intervals for accuracy, log loss and Brier score.

These are descriptive uncertainty intervals, not a new model-selection exercise.

## Stage-progression retrospective comparison

Aggregate stage reach rates are not used as evidence of calibration. In a fixed 48-team tournament, exactly 32 teams reach the Round of 32, 16 reach the Round of 16, eight reach the quarter-finals, four reach the semi-finals, two reach the final and one becomes champion. By construction, the mean simulated reach probability across all 48 teams is therefore tied to those same fractions for any model.

Tournament-level validation instead uses:

- **per-team stage Brier score**, which penalises probability assigned to the wrong teams
- **top-k capture rate**, which measures how many actual stage participants appear among the model's highest-probability teams for the same number of available places

`outputs/world_cup_2026_stage_validation.csv` contains these team-level diagnostics.

## Actual-field tournament comparison

A separate **2,000-run Monte Carlo tournament simulation with seed 2026** uses the actual 48-team field and actual group allocation while retaining the frozen pre-tournament model state.

This Monte Carlo analysis is a sibling of the 104-match backtest, not a step inside it. It is not used to calculate backtest accuracy, log loss, Brier score or bootstrap intervals.

The original project tournament assumptions remain:

- group ties use points followed by frozen Elo because the model does not predict scorelines
- the knockout stage uses the project's transparent seeded pairing heuristic
- knockout draws use relative non-draw probabilities for advancement

The output is an actual-field retrospective comparison of the model's tournament expectations, not a reconstruction of every official FIFA bracket and tiebreak rule.

## Feature freshness

The pre-tournament state ends on 31 March 2026 and the World Cup began on 11 June 2026, a 72-day gap.

Later friendlies, qualifiers, final squad selections, injuries and tactical changes are deliberately excluded to preserve the frozen-state design.

## Result convention

Penalty-shootout matches remain Draw for the three-way outcome score, while the advancing team is recorded separately. Spain's 1-0 extra-time victory over Argentina in the final is recorded as a Spain win.

## Data provenance

Structured match ground truth is adapted from the WC2026-Agents benchmark metadata released under CC BY 4.0:

Ding, Jiacheng; Guo, Cong; Xu, Jason (2026), *FIFA World Cup 2026 as a Contamination-Free Benchmark for LLM Forecasting Agents: Four Models, a Bookmaker, and 104 Matches*, arXiv:2607.17765.

Repository: `graphuofm/FIFA2026LLM`

The schedule and key knockout outcomes were cross-checked against FIFA's official 2026 World Cup fixtures/results pages and final tournament standings.

The historical `data/results.csv` file remains unchanged. Actual tournament outcomes live only in `data/world_cup_2026_actual_results.csv`.


## Venue assumption in tournament simulation

The match-level backtest uses the recorded `neutral` flag for each actual fixture. The separate Monte Carlo tournament simulation treats simulated matchups as neutral, so it does not reproduce host-country venue advantage for Mexico, Canada or the United States.
