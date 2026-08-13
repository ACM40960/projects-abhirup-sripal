# Probability calibration and evaluation

The simulator needs outcome probabilities, not just a winning class. Commit 9 therefore compares probability quality on the same 2023 chronological holdout used for classification.

## Fair treatment of the draw class

The Linear SVM already uses `class_weight="balanced"`. Histogram gradient boosting now receives training sample weights from `compute_sample_weight(class_weight="balanced", ...)`.

Using sample weights avoids depending on a particular scikit-learn version exposing a `class_weight` argument on `HistGradientBoostingClassifier`.

The comparison now records recall separately for away wins, draws and home wins. Confusion matrices are also saved so a model cannot look competitive overall while effectively ignoring one class.

## Temporal calibration

The Linear SVM does not produce probabilities natively. Sigmoid calibration uses five expanding folds built from unique match dates. Every estimator-training period ends before its corresponding calibration period begins.

Scaling sits inside the calibrated pipeline, so each fold fits its scaler only on the historical rows available to that fold.

## Probability metrics

Multiclass log loss is the primary model-selection metric. Lower values mean the model assigned more probability to the outcomes that actually occurred.

The multiclass Brier score is used as a secondary measure. It is the mean summed squared error between the three predicted probabilities and the observed one-hot outcome.

Accuracy, balanced accuracy, macro F1 and per-class recall remain in the output for interpretation.

## Files produced

- `outputs/model_per_class_recall.csv`
- `outputs/model_confusion_matrices.csv`
- `outputs/calibration_fold_validation.csv`
- `outputs/probability_model_comparison.csv`
- `outputs/selected_probability_model.csv`
- `outputs/selected_model_calibration.csv`
- `outputs/figures/selected_model_calibration.png`

Team-specific feature construction is still deferred to Commit 10.
