# World Cup Match Outcome Predictor

This repository contains the current prototype for a mathematical modelling project on predicting international football match outcomes and simulating a World Cup tournament.

## Current stage

The repository now contains validated historical match data, leakage-safe rolling form, corrected tournament context, deterministic pre-match Elo features and chronological forecast evaluation.

The previous random 80/20 split has been replaced with a fixed date holdout:

- training: matches before 1 January 2023;
- testing: matches from 1 January 2023 onward.

This means later test matches cannot be randomly mixed into the training period. Standardisation is fitted on training data only.

The original SVM and MLP architectures are retained temporarily. Model replacement and broader probability evaluation are scheduled for the next commits.

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

## Commit validation outputs

The `outputs/` directory includes validation artifacts for data cleaning, rolling form, tournament context, Elo integrity and chronological evaluation.

Commit 7 adds:

- `chronological_split_validation.csv`
- `chronological_split_class_distribution.csv`

Notebook outputs are cleared before commit so the pipeline can be reproduced from a fresh kernel.
