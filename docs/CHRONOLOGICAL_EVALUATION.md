# Chronological evaluation

## Purpose

The original prototype used a random 80/20 train-test split. International football data are chronological, so a random split can place later matches in the training set while earlier matches appear in the test set. That does not reflect the intended forecasting task.

Commit 7 replaces random splitting with a fixed time-based holdout.

## Split definition

- Training: matches before 1 January 2023
- Testing: matches on or after 1 January 2023

With the supplied validated modern-era dataset:

- total modelling matches: 25,157
- training matches: 21,712
- testing matches: 3,445
- training period: 2000-01-04 to 2022-12-30
- testing period: 2023-01-02 to 2026-03-31

The notebook explicitly raises an error if the latest training date overlaps the earliest testing date.

## Scaling rule

`StandardScaler` is fitted only on the training subset. The test subset is transformed with the fitted training scaler. This prevents test-set statistics from being used during preprocessing.

## Model scope

Commit 7 changes evaluation design only. The existing RBF SVM and MLP are retained temporarily so the effect of changing the evaluation protocol remains isolated. More efficient comparison models are planned for Commit 8.

## Generated outputs

- `outputs/chronological_split_validation.csv`
- `outputs/chronological_split_class_distribution.csv`
