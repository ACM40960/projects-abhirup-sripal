# World Cup Match Outcome Predictor

This repository contains the final version of a mathematical-modelling project for international football match prediction and tournament simulation.

## Pipeline

The modelling workflow now:

- validates completed international match results
- assigns deterministic match identifiers
- builds leakage-safe five-match form
- calculates pre-match Elo ratings
- adds tournament importance and neutral-venue context
- evaluates on a chronological holdout beginning in 2023
- compares class-balanced linear and nonlinear models
- calibrates the final probability candidates using expanding temporal folds
- constructs current features for named teams
- generates neutral-match outcome probabilities
- propagates those probabilities through a configurable 48-team-style tournament

The fixed demonstration vector from the early prototype has been removed.

## Final model choice

The final probability comparison gives both learned candidates the same temporal calibration treatment. The class-balanced histogram gradient boosting model is calibrated through the same expanding date folds used by the Linear SVM.

Model selection is based on chronological test-set log loss, with multiclass Brier score as a secondary measure. The selected model is recorded in `outputs/selected_probability_model.csv`.

Hard draw recall is reported separately. It is not the selection criterion because the simulator samples from the full probability vector rather than using the argmax class.

## Tournament scope

The tournament code supports 48 teams, 12 groups of four, eight best third-place qualifiers and a 32-team knockout stage.

The bundled run is a modelling demonstration, not an official 2026 forecast. It uses the top 48 teams in the current Elo snapshot because the repository does not contain an authoritative participant list. Group ties use points then Elo, and the knockout pairing is seeded rather than claiming to reproduce the official FIFA bracket.

## Main outputs

Model evaluation:

- `outputs/probability_model_comparison.csv`
- `outputs/draw_probability_diagnostic.csv`
- `outputs/hgb_calibration_sensitivity.csv`
- `outputs/selected_probability_model.csv`
- `outputs/selected_model_calibration.csv`

Prediction and tournament:

- `outputs/team_state_snapshot.csv`
- `outputs/team_specific_prediction_examples.csv`
- `outputs/tournament_group_configuration.csv`
- `outputs/tournament_simulation_results.csv`
- `outputs/tournament_simulation_validation.csv`

Poster-ready figures:

- `outputs/figures/selected_model_calibration.png`
- `outputs/figures/final_log_loss_comparison.png`
- `outputs/figures/classification_draw_recall.png`
- `outputs/figures/champion_probabilities.png`

## Literature review note

The PDF in `literature/` is the original project literature review and reflects an earlier planned methodology. `docs/LITERATURE_METHOD_ALIGNMENT.md` records which ideas were ultimately implemented and which remained literature context rather than model inputs.

## Run

With the project environment active:

```bat
conda activate worldcup
jupyter lab
```

Open `notebooks/world_cup_predictor.ipynb` with the `Python (World Cup Predictor)` kernel and run the notebook from a fresh kernel.
