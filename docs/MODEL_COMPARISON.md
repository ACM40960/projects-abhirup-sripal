# Model comparison

The final project keeps one transparent probability baseline and two learned candidates.

## Models compared

### Class-prior baseline

`DummyClassifier(strategy="prior")` ignores the football features and provides a lower benchmark based on the training outcome distribution.

### Linear SVM

The Linear SVM uses balanced class weights and standardised features. It is computationally much lighter than the original RBF SVM.

### Histogram gradient boosting

Histogram gradient boosting captures nonlinear relationships between Elo, form and match context. Balanced sample weights are calculated inside the estimator so the minority draw class is not effectively ignored.

## Two views of performance

Classification diagnostics report accuracy, balanced accuracy, macro F1, per-class recall and confusion matrices.

Probability evaluation is separate. The Linear SVM and balanced gradient-boosting model are both calibrated with the same expanding temporal folds before log loss and multiclass Brier score are compared.

This distinction matters because the tournament simulator samples from probabilities rather than taking the single highest-probability class.
