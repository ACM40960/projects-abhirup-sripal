# Notebook execution order

The final analysis is split into four notebooks so each stage has a clear responsibility and can be executed independently from disk artefacts.

1. `01_data_and_features.ipynb`
   - validates historical matches
   - builds rolling form, match context and pre-match Elo
   - writes `outputs/intermediate/model_features.csv`
   - writes the frozen team-state snapshot

2. `02_model_training_and_evaluation.ipynb`
   - trains and evaluates the candidate models
   - performs temporal probability calibration
   - saves the selected probability model and class-prior baseline in `models/`

3. `03_team_prediction_and_tournament.ipynb`
   - loads the selected model
   - validates team-specific probabilities
   - runs the generic top-48-Elo tournament demonstration

4. `04_world_cup_2026_backtest.ipynb`
   - loads the frozen selected model
   - evaluates all 104 completed World Cup matches
   - estimates metric uncertainty with 5,000 bootstrap resamples, seed 2026
   - separately runs the actual-field 48-team tournament simulation for 2,000 iterations, seed 2026

Each notebook starts from files on disk rather than depending on variables left in another notebook's kernel.

For a complete rebuild, run 01 -> 02 -> 03 -> 04. If the prepared model artefacts already exist, notebooks 03 and 04 can be rerun without repeating model training.

## Verified split runtime

A clean sequential validation of the split notebooks in the release build completed each notebook independently in under 10 seconds in the validation environment. Exact timings are stored in `outputs/notebook_runtime_validation.csv`. Runtime will vary by machine.
