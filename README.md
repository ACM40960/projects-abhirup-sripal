# World Cup Match Outcome Predictor

This repository contains a mathematical-modelling project for predicting international football match outcomes and using those predictions in a World Cup simulation.

## Current stage

The pipeline now includes:

- validated international match results;
- deterministic match identifiers;
- leakage-safe rolling team form;
- corrected tournament context;
- pre-match Elo ratings;
- chronological evaluation using a 2023 holdout;
- a class-prior benchmark;
- a class-balanced Linear SVM;
- histogram gradient boosting.

Commit 8 replaces the active slow RBF-SVM/MLP comparison with a smaller and more reproducible classification benchmark. Every model uses the same chronological test set.

Current classification metrics are:

- accuracy;
- balanced accuracy;
- macro F1.

Probability calibration, log loss and probability-focused model selection are reserved for Commit 9.

## Chronological split

- Training: matches before 1 January 2023
- Testing: matches from 1 January 2023 onward

The Linear SVM scaler is fitted only on the training sample.

## Repository structure

```text
.
├── data/
├── notebooks/
├── literature/
├── docs/
├── outputs/
├── environment.yml
└── requirements.txt
```

## Run with Anaconda

```bat
conda activate worldcup
jupyter lab
```

Open `notebooks/world_cup_predictor.ipynb` and select the `Python (World Cup Predictor)` kernel.

## Commit 8 output

`outputs/model_comparison_classification.csv`

Notebook execution outputs are cleared before commit so results can be reproduced from a fresh kernel.
