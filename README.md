# World Cup Match Outcome Predictor

This repository contains the current prototype for a mathematical modelling project on predicting international football match outcomes and simulating a World Cup tournament.

## Current stage

The repository has been reorganised from the original flat project archive into a reproducible structure. The modelling logic remains the original prototype at this stage. Later commits will address data validation, leakage-safe feature engineering, chronological evaluation, model comparison and team-specific tournament simulation.

## Repository structure

```text
.
├── data/          Historical match and supporting datasets
├── notebooks/     Jupyter modelling notebook
├── literature/    Literature review
├── docs/          Project planning and methodology notes
├── outputs/       Generated metrics, figures and simulation results
├── environment.yml
└── requirements.txt
```

## Run with Anaconda

From Anaconda Prompt, open the repository folder and create the environment:

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

## Data

The prototype currently reads `data/results.csv`. The other datasets are retained for later analysis but are not yet integrated into the model.

## Reproducibility note

The notebook now resolves the project data path from either the repository root or the `notebooks` folder. Generated notebook outputs have been cleared so that results can be reproduced from a fresh kernel.
