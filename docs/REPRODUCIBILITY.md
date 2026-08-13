# Reproducibility notes

The final notebook is designed to run from either the repository root or the `notebooks` directory.

## Expected data checks

A fresh run should reproduce:

- 49,215 validated completed matches
- 25,157 modelling matches from 2000 onward
- 21,712 training matches
- 3,445 chronological test matches
- 25,157 unique modern `match_id` values
- zero model rows added or lost by rolling-form and Elo joins
- 248 Copa América matches assigned the corrected 0.8 weight
- 48 teams in the bundled tournament demonstration
- champion probabilities summing to 1.0

The final model name and probability metrics are written to `outputs/selected_probability_model.csv` and `outputs/final_run_validation.csv`.

## Environment

`environment.yml` targets Python 3.11 and lists the required packages. `requirements.txt` provides the equivalent pip package list.

The code includes compatibility handling for the `CalibratedClassifierCV` constructor name used across scikit-learn versions.

## Notebook hygiene

Execution outputs are cleared in the committed notebook. Run all cells from a fresh kernel to regenerate the CSV and figure outputs.

The obsolete `Chapter 1` / `Chapter 2` placeholders, standalone PCA/correlation experiment and redundant pre-Elo scaler have been removed from the final notebook.
