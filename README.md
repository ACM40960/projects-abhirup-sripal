# World Cup Match Outcome Predictor

This repository contains the current prototype for a mathematical modelling project on predicting international football match outcomes and simulating a World Cup tournament.

## Current stage

The repository now contains validated historical match data and leakage-safe rolling team-form features. The form pipeline retains `match_id` for both home and away team perspectives, calculates recent goals scored and conceded from the previous five matches strictly before the current date, and merges the features back with one-to-one identifier joins. This removes the row multiplication present in the original date/team merge.

Later commits will correct match-context features, pre-match Elo, chronological evaluation, model comparison and team-specific tournament simulation.

## Repository structure

```text
.
├── data/          Historical match and supporting datasets
├── notebooks/     Jupyter modelling notebook
├── literature/    Literature review
├── docs/          Project planning and methodology notes
├── outputs/       Generated validation files, metrics, figures and simulations
├── environment.yml
└── requirements.txt
```

## Run with Anaconda

From Anaconda Prompt:

```bat
conda env create -f environment.yml
conda activate worldcup
python -m ipykernel install --user --name worldcup --display-name "Python (World Cup Predictor)"
jupyter lab
```

For an offline Anaconda installation, clone the base environment if the required packages are already available:

```bat
conda create --name worldcup --clone base
conda activate worldcup
python -m ipykernel install --user --name worldcup --display-name "Python (World Cup Predictor)"
jupyter lab
```

Open `notebooks/world_cup_predictor.ipynb` and select the `Python (World Cup Predictor)` kernel.

## Data and generated validation files

The prototype reads `data/results.csv`.

Commit 3 generated:

- `outputs/data_validation_summary.csv`
- `outputs/duplicate_match_keys.csv`

Commit 4 adds:

- `outputs/rolling_form_validation.csv`

The other source datasets are retained for later analysis but are not yet integrated into the predictive model.

## Reproducibility note

The notebook resolves the project path from either the repository root or the `notebooks` folder. Notebook outputs are intentionally cleared before commit so results can be reproduced from a fresh kernel.
