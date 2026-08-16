# Reproducibility notes

The final analysis is split into four purpose-specific notebooks. Each notebook starts from files on disk rather than depending on variables retained in another Jupyter kernel.

## Execution order

1. `notebooks/01_data_and_features.ipynb`
2. `notebooks/02_model_training_and_evaluation.ipynb`
3. `notebooks/03_team_prediction_and_tournament.ipynb`
4. `notebooks/04_world_cup_2026_backtest.ipynb`

Notebook 01 writes the prepared historical feature table and frozen team-state snapshot.

Notebook 02 writes the selected probability model, baseline model and model metadata to `models/`.

Notebooks 03 and 04 load those artefacts, so they can be rerun without repeating model training once the first two stages have been completed.

## Expected historical checks

A fresh rebuild should reproduce:

- 49,215 validated completed matches
- 25,157 modelling matches from 2000 onward
- 21,712 training matches
- 3,445 chronological test matches
- 25,157 unique modern `match_id` values
- zero rows added or lost by rolling-form and Elo joins
- 248 Copa América matches assigned the corrected 0.8 tournament weight

## Expected retrospective checks

The World Cup backtest should reproduce:

- 104 completed tournament matches
- 48 participants
- zero completed World Cup matches in model-development data
- 5,000 bootstrap resamples with seed 2026
- 2,000 actual-field tournament simulations with seed 2026

Actual tournament outcomes remain separate from `data/results.csv`.

## Persisted models

`models/model_metadata.json` records the feature order, selected model name, training/holdout dates and the scikit-learn version used to serialize the model.

Scikit-learn model files are not guaranteed to be portable across every library version. If loading a tracked `.joblib` artefact fails, rerun Notebook 02 in the active environment before running Notebooks 03 or 04.

## Notebook hygiene

Committed notebook outputs are cleared. CSV and figure outputs are stored under `outputs/`.

The split keeps the longest training/calibration stage isolated from the much faster prediction, simulation and retrospective-analysis stages.

## Runtime validation

The split was also checked as four fresh notebook executions, each with its own Python namespace. Timings are stored in `outputs/notebook_runtime_validation.csv`; they are environment-specific and are included to demonstrate that later analysis no longer requires rerunning the entire monolithic notebook.
