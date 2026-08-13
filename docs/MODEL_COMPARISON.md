# Commit 8 model comparison

## Purpose

The earlier notebook relied on a relatively slow RBF SVM and an MLP experiment without a simple benchmark. Commit 8 introduces a compact, reproducible model comparison using the chronological holdout from Commit 7.

## Models

### Class-prior baseline

`DummyClassifier(strategy="prior")`

This is the minimum benchmark. It predicts according to the training-set class prior and shows whether the learned classifiers improve on a model that ignores the football features.

### Linear SVM

`LinearSVC(class_weight="balanced")`

The linear SVM is substantially cheaper than the previous RBF SVM on this dataset. Class balancing is retained because draws are less common and were poorly detected in the original prototype.

### Histogram gradient boosting

`HistGradientBoostingClassifier`

This model captures nonlinear relationships between Elo, recent form and match context while remaining efficient on the current tabular dataset.

## Shared evaluation design

Every model uses the same chronological split:

- training: before 2023-01-01
- testing: 2023-01-01 onward

The Linear SVM uses a `StandardScaler` fitted only on the training set. Histogram gradient boosting and the dummy baseline use the unscaled features.

## Commit 8 metrics

Commit 8 reports:

- accuracy
- balanced accuracy
- macro F1

Probability calibration, multiclass log loss and probability-focused diagnostics are intentionally reserved for Commit 9.

## Output

`outputs/model_comparison_classification.csv`

The best classification result in this file is provisional. Final model selection should be based on the probability evaluation introduced in the next commit because the tournament simulator requires meaningful probabilities, not only class labels.
