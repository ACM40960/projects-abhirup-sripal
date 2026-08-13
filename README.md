# World Cup Match Outcome Predictor

This project predicts international football match outcomes from historical results and propagates those probabilities through a tournament simulation.

## What the current pipeline does

- Validates the historical match dataset
- Builds leakage-safe recent-form features
- Calculates pre-match Elo ratings
- Adds tournament importance and neutral-venue context
- Evaluates models on a chronological 2023 holdout
- Compares class-balanced Linear SVM and histogram gradient boosting models
- Evaluates probability quality with log loss and Brier score
- Builds current state features for named teams
- Produces neutral-venue match probabilities
- Simulates a configurable 48-team-style tournament

The old fixed vector used by the four-team demonstration has been removed.

## Team-specific prediction

`get_match_probabilities(...)` now uses the named teams' current Elo and recent form. Neutral tournament matches are evaluated in both team orderings and averaged, avoiding an arbitrary first-listed-team advantage.

Validation examples are written to:

- `outputs/team_state_snapshot.csv`
- `outputs/team_specific_prediction_examples.csv`
- `outputs/team_prediction_validation.csv`

## Tournament simulation

The bundled demonstration uses 12 groups of four, advances the top two teams plus eight best third-place teams and then runs a 32-team knockout stage.

The repository does not store an authoritative participant list, so the demonstration uses the top 48 teams in the current Elo snapshot. A different 48-team list can be passed to the tournament functions.

The simulator is intentionally transparent about two simplifications: points ties are broken using Elo because the model does not predict scorelines, and the knockout bracket is seeded rather than reproducing an official FIFA draw map.

Outputs include:

- `outputs/tournament_group_configuration.csv`
- `outputs/tournament_simulation_results.csv`
- `outputs/tournament_simulation_validation.csv`
- `outputs/figures/champion_probabilities.png`

## Run with Anaconda

```bat
conda activate worldcup
jupyter lab
```

Open `notebooks/world_cup_predictor.ipynb` with the `Python (World Cup Predictor)` kernel.

Commit 11 is the final cleanup and submission pass.
