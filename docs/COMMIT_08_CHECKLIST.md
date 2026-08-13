# Commit 8 checklist: baseline and efficient comparison models

- [x] Preserve the chronological 2023 holdout
- [x] Preserve leakage-safe Elo, form and match-context features
- [x] Add a class-prior dummy baseline
- [x] Replace active RBF-SVM training with a class-balanced Linear SVM
- [x] Add histogram gradient boosting
- [x] Fit the Linear SVM scaler on training data only
- [x] Evaluate every model on the same test rows
- [x] Report accuracy, balanced accuracy and macro F1
- [x] Save a machine-readable classification comparison
- [x] Remove the MLP from the active model-comparison path
- [x] Keep probability calibration for Commit 9
- [x] Keep team-specific prediction and tournament restructuring for later commits
- [x] Clear notebook outputs before commit

## Commit message

```bash
git commit -m "feat: add baseline and efficient classification models"
```
