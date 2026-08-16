# World Cup Match Outcome Predictor

This project was completed for **ACM40960 — Projects in Maths Modelling** at University College Dublin.

The aim is to estimate probabilities for international football match outcomes using historical results, recent team form, Elo ratings and match context, then propagate those probabilities through tournament simulations.

## Research question

Can historical international results, Elo ratings and recent team form produce useful match probabilities for forecasting international fixtures and tournament progression?

## Data

The executable modelling pipeline uses `data/results.csv`.

Supporting files (`goalscorers.csv`, `shootouts.csv` and `former_names.csv`) are retained in the repository for reference but are **not inputs to the final model**.

The modelling period begins on 1 January 2000. The validated modern-era table contains **25,157 matches**.

The retrospective World Cup analysis uses separate files:

- `data/world_cup_2026_actual_results.csv`
- `data/world_cup_2026_groups.csv`
- `data/world_cup_2026_team_name_map.csv`

Keeping tournament outcomes separate from `results.csv` preserves the frozen pre-tournament modelling state.

## Final feature set

The probability models use eight inputs:

1. home-team pre-match Elo
2. away-team pre-match Elo
3. home recent goals for
4. home recent goals against
5. away recent goals for
6. away recent goals against
7. tournament importance weight
8. neutral-venue indicator

Rolling form and Elo are calculated without using the current match result. Same-day appearances share the same pre-date state.

## Evaluation design

The historical evaluation is chronological:

- training: 2000-01-04 to 2022-12-30
- test: 2023-01-02 to 2026-03-31
- training matches: 21,712
- test matches: 3,445

Candidate probability models are calibrated with expanding temporal folds. The final model is selected by test-set log loss with multiclass Brier score as a secondary probability metric.

## Final model

The selected model is **Calibrated Linear SVM**.

Historical chronological holdout:

| Metric | Value |
|---|---:|
| Accuracy | 0.596 |
| Log loss | 0.892 |
| Multiclass Brier | 0.525 |

Hard draw recall is low because Draw is rarely the single highest-probability class. The simulator samples from the full probability vector, so log loss, Brier score and calibration are the primary probability diagnostics.

## Tournament simulation

Two tournament uses are kept distinct.

### Generic demonstration

`03_team_prediction_and_tournament.ipynb` uses the top 48 teams in the frozen Elo snapshot and a reproducible 2,000-run simulation.

This is a generic modelling demonstration, not an official World Cup forecast.

### Retrospective actual-field analysis

`04_world_cup_2026_backtest.ipynb` uses the actual 48-team 2026 group field and compares the frozen model with the completed tournament.

Across 104 matches:

| Metric | Value |
|---|---:|
| Accuracy | 0.606 |
| Log loss | 0.884 |
| Multiclass Brier | 0.524 |
| Actual draw rate | 23.1% |
| Mean predicted draw probability | 21.5% |

The World Cup outcomes are evaluation-only and are not used for retraining, retuning or model reselection.

## Notebook structure

Run the notebooks in order:

```text
01_data_and_features.ipynb
        ↓
02_model_training_and_evaluation.ipynb
        ↓
03_team_prediction_and_tournament.ipynb
        ↓
04_world_cup_2026_backtest.ipynb
```

Each notebook reads its required inputs from disk, so later stages do not depend on variables left in an earlier Jupyter kernel. See `notebooks/README.md`.

## Project structure

```text
data/
    results.csv
    goalscorers.csv                 # reference only
    shootouts.csv                   # reference only
    former_names.csv                # reference only
    world_cup_2026_actual_results.csv
    world_cup_2026_groups.csv
    world_cup_2026_team_name_map.csv
docs/
literature/
    Literature_Review.pdf
models/
    selected_probability_model.joblib
    class_prior_baseline.joblib
    model_metadata.json
notebooks/
    01_data_and_features.ipynb
    02_model_training_and_evaluation.ipynb
    03_team_prediction_and_tournament.ipynb
    04_world_cup_2026_backtest.ipynb
    README.md
src/
    worldcup_runtime.py
outputs/
    intermediate/
    figures/
poster/
environment.yml
requirements.txt
```

## Running the project

Create the environment:

```bat
conda env create -f environment.yml
conda activate worldcup
jupyter lab
```

For a complete rebuild, run Notebooks 01 through 04 in order.

Notebook 02 persists the selected model. Once those artefacts exist, the simulation and World Cup backtest notebooks can be rerun without repeating the historical model-training stage.

## Limitations

The final model does not use player injuries, squad availability, bookmaker odds, FIFA ratings, player market values, travel or climate features, and it does not model scorelines directly.

The generic and actual-field tournament simulations use a simplified bracket/tiebreak system. The actual-field simulation also treats simulated tournament matchups as neutral, so host-country venue advantage for Mexico, Canada and the United States is not reproduced.

The frozen World Cup state ends on 31 March 2026, 72 days before the opening match. Later friendlies, qualifiers, final squad choices, injuries and tactical changes are therefore outside the retrospective model state.

## Literature review

The original literature review is retained at `literature/Literature_Review.pdf`. It reflects the methodology as planned earlier in the project and does not exactly match the final implementation.

`docs/LITERATURE_METHOD_ALIGNMENT.md` records which ideas were implemented, which were not, and why the final report should follow the implemented pipeline rather than the earlier proposal language.

## Future work

Useful extensions include player/squad availability, bookmaker probability comparison, an explicit scoreline model, alternative Elo update rules, sequential in-tournament state updating and an exact official tournament bracket/venue implementation.

## Author

**Abhirup and Sripal**  
MSc Data and Computational Science  
University College Dublin
