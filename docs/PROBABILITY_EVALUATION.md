# Probability calibration and evaluation

The tournament simulator needs a full away-win/draw/home-win probability vector, so probability quality is the main selection criterion.

## Equal calibration treatment

Both learned candidates now receive temporal sigmoid calibration.

The Linear SVM contains its scaler and class-balanced classifier inside the calibrated pipeline.

For histogram gradient boosting, balanced training weights are computed inside a small estimator wrapper. This allows the classifier itself to remain class-balanced while the calibration layer is fitted against the natural outcome distribution rather than a reweighted one.

Five expanding folds are built from unique match dates. Every estimator-training period ends before the corresponding calibration period begins.

## Final selection metrics

The model table reports:

- accuracy
- balanced accuracy
- macro F1
- away-win recall
- draw recall
- home-win recall
- multiclass log loss
- multiclass Brier score

The final model is selected by lowest log loss, with Brier score used as a secondary check.

## Why low draw recall does not imply zero draw probability

The selected model rarely makes `Draw` its highest-probability class, so its hard-class draw recall is low. That does not mean it assigns draws negligible probability.

`outputs/draw_probability_diagnostic.csv` compares the observed test draw rate with the model's mean predicted draw probability and the draw calibration bins. The Monte Carlo simulation samples from this full probability vector, not from the argmax class.

The correct interpretation is therefore:

- draw recall describes how often `Draw` is the single highest-probability class
- calibration and log loss describe whether the assigned probabilities are useful for probabilistic simulation

The historical calibration diagnostic does not guarantee a particular draw rate inside the simulated tournament because that tournament contains a different mix of teams and neutral fixtures.

## HGB calibration sensitivity

`outputs/hgb_calibration_sensitivity.csv` records the balanced gradient-boosting model before and after temporal calibration. This check was added because class weighting can alter probability frequencies.

The final comparison is based on the calibrated HGB result, so the selected model is not benefiting from an apples-to-oranges calibration advantage.
