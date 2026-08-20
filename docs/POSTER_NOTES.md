# Poster-ready results and talking points

## Suggested title

**Predicting World Cup Outcomes with Elo Ratings and Machine Learning**

## Research question

Can historical international results, Elo ratings and recent team form produce useful match probabilities that can be propagated through a tournament simulation?

## Pipeline for the methods section

Historical results -> validation -> rolling form + Elo -> tournament context -> chronological holdout -> class-balanced models -> temporal calibration -> team-specific probabilities -> Monte Carlo tournament

## Numbers worth putting on the poster

- 25,157 modern-era modelling matches
- 21,712 training matches
- 3,445 chronological test matches
- Final model: Calibrated Linear SVM
- Test log loss: 0.892
- Multiclass Brier score: 0.525
- Test accuracy: 59.62%
- Test draw rate: 23.08%
- Mean predicted draw probability: 22.45%
- Generic simulator demonstration: 2,000 runs, seed 42
- Final actual-field simulation: 2,000 runs, seed 2026

## Draw question likely to come up

The selected probability model has low hard-class draw recall, but that does not mean it assigns zero probability to draws. Draw is rarely the single largest probability, while the average draw probability on the held-out test set remains close to the observed draw frequency. Because the tournament simulator samples from the full probability vector, log loss and calibration are more relevant than argmax draw recall for model selection.

## Final modelling result

Balanced histogram gradient boosting was also temporally calibrated in the final validation pass. It still had worse log loss and Brier score than the calibrated Linear SVM, so the selected model did not depend on giving the SVM a calibration advantage.

## Tournament result caveat

Two Monte Carlo runs are retained in the repository and should not be conflated.

- **Generic demonstration (`03_team_prediction_and_tournament.ipynb`):** top 48 teams in the frozen Elo snapshot, constructed groups, 2,000 runs, seed 42. This is a simulator demonstration rather than an official World Cup forecast.
- **Final actual-field simulation (`04_world_cup_2026_backtest.ipynb`):** actual 48-team 2026 field and actual group allocation, frozen team state ending 31 March 2026, 2,000 runs, seed 2026. This is the run represented by the final poster champion chart.

The actual-field simulation uses no World Cup match outcomes to generate the champion probabilities. Actual results are attached afterwards for retrospective comparison. The knockout bracket remains the project's transparent seeded approximation rather than an exact FIFA reconstruction.

## Recommended visuals

- `outputs/figures/final_log_loss_comparison.png`
- `outputs/figures/selected_model_calibration.png`
- `outputs/figures/classification_draw_recall.png`
- `outputs/figures/champion_probabilities.png`

## Short conclusion

The project shows that a compact feature set based on Elo, recent form and match context can outperform a class-prior baseline and produce calibrated probabilities suitable for simulation. The strongest remaining limitations are the absence of scoreline modelling, richer player/market features and an exact official tournament bracket.


## Post-tournament validation box

**Retrospective 2026 World Cup validation — model frozen before tournament outcomes**

- 104 matches evaluated
- Accuracy: **60.6%** (95% bootstrap CI 51.0%–70.2%)
- Log loss: **0.884** (95% CI 0.786–0.984)
- Brier score: **0.524** (95% CI 0.452–0.597)
- Actual draw rate: **23.1%**
- Mean predicted draw probability: **21.5%**
- Historical-data state ends 31 March 2026, 72 days before the opening match
- World Cup outcomes used for retraining or model reselection: **0**

**Draw explanation:** the model does not make Draw its argmax class in the 104-match backtest, but it still allocates about one-fifth of its probability mass to draws. The poster should therefore keep log loss, Brier score and draw-probability calibration ahead of bare draw recall.

**Actual-field simulation:** the final poster chart uses the frozen actual 48-team field/group configuration, 2,000 runs and seed 2026. Spain receives a **25.7%** title probability and rank **1**, while Argentina receives **21.2%** and rank **2**. Spain's eventual championship result is not an input to these probabilities; it is added afterwards for retrospective comparison.

**Separation from the backtest:** the 2,000-run actual-field simulation is not used to calculate the 104-match accuracy, log loss or Brier score. The backtest scores the frozen model on the 104 completed matches, and 5,000 bootstrap resamples with seed 2026 quantify uncertainty in those metrics.

Recommended new figures:

- `outputs/figures/world_cup_2026_probability_performance.png`
- `outputs/figures/world_cup_2026_draw_calibration.png`
- `outputs/figures/world_cup_2026_expected_vs_actual.png`
