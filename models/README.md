# Persisted model artefacts

`02_model_training_and_evaluation.ipynb` writes:

- `selected_probability_model.joblib`
- `class_prior_baseline.joblib`
- `model_metadata.json`

The metadata records the selected model name, feature order, training/holdout dates and the scikit-learn version used to serialize the model.

If a different scikit-learn environment cannot load a tracked `.joblib` file, rerun Notebook 02 in that environment to regenerate the model artefacts before running Notebooks 03 or 04.
