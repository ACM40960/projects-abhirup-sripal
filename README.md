# World Cup Match Outcome Predictor

This repository contains the current prototype for a mathematical modelling project on predicting international football match outcomes and simulating a World Cup tournament.

## Current stage

The repository now contains validated historical match data, leakage-safe rolling form, corrected tournament context, and deterministic pre-match Elo features. Elo is carried by `match_id`, joined one-to-one, and validated so no rows are silently duplicated or dropped. Teams with multiple source matches on the same calendar date receive the same pre-date Elo because no kick-off times are available.

Random train/test splitting and the original model/simulation choices are retained temporarily and are scheduled for later commits.

## Repository structure

```text
.
├── data/          Historical match and supporting datasets
├── notebooks/     Jupyter modelling notebook
├── literature/    Literature review
├── docs/          Project planning and methodology notes
├── outputs/       Generated validation files, ratings, metrics and figures
├── environment.yml
└── requirements.txt
```

## Run with Anaconda

From Anaconda Prompt:

```bat
conda activate worldcup
jupyter lab
```

Open `notebooks/world_cup_predictor.ipynb` and select the `Python (World Cup Predictor)` kernel.

## Commit validation outputs

The `outputs/` directory now includes:

- `data_validation_summary.csv`
- `duplicate_match_keys.csv`
- `rolling_form_validation.csv`
- `tournament_weight_validation.csv`
- `match_context_validation.csv`
- `elo_validation.csv`
- `final_elo_ratings.csv`

Notebook outputs are cleared before commit so the pipeline can be reproduced from a fresh kernel.
