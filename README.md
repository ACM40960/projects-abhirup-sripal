# World Cup Match Outcome Predictor

This project predicts international football match outcomes and uses those probabilities as the basis for tournament simulation.

The current pipeline includes:

- Validated historical match results
- Deterministic match identifiers
- Leakage-safe rolling team form
- Tournament context and neutral-venue features
- Pre-match Elo ratings
- A chronological 2023 test holdout
- Class-prior, Linear SVM and histogram gradient boosting benchmarks
- Balanced treatment of the minority draw class for both learned models
- Temporal SVM calibration
- Log loss, Brier score, per-class recall and confusion-matrix diagnostics

## Evaluation

Training uses matches before 1 January 2023. Matches from 1 January 2023 onward form the test set.

Histogram gradient boosting is trained with balanced sample weights. The Linear SVM uses balanced class weights and temporal sigmoid calibration. Model selection for tournament probabilities is based primarily on test-set log loss, not raw accuracy.

Commit 9 produces:

- `outputs/model_per_class_recall.csv`
- `outputs/model_confusion_matrices.csv`
- `outputs/probability_model_comparison.csv`
- `outputs/selected_probability_model.csv`
- `outputs/selected_model_calibration.csv`
- `outputs/figures/selected_model_calibration.png`

The existing four-team simulation is still a placeholder because it does not yet construct features from the named teams. That is the next modelling step.

## Run with Anaconda

```bat
conda activate worldcup
jupyter lab
```

Open `notebooks/world_cup_predictor.ipynb` and use the `Python (World Cup Predictor)` kernel.
