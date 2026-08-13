# Commit 9 checklist: probability calibration and evaluation

- [x] Keep the 2023 chronological test holdout
- [x] Keep class balancing for the Linear SVM
- [x] Add balanced sample weights to histogram gradient boosting
- [x] Report recall for away wins, draws and home wins
- [x] Save confusion matrices for every classification model
- [x] Build SVM calibration folds from unique dates
- [x] Keep estimator dates strictly before calibration dates
- [x] Fit scaling inside the calibrated SVM pipeline
- [x] Evaluate class-prior baseline probabilities
- [x] Evaluate calibrated Linear SVM probabilities
- [x] Evaluate balanced histogram gradient boosting probabilities
- [x] Add multiclass log loss and Brier score
- [x] Select the provisional probability model by lowest log loss
- [x] Save class-wise calibration diagnostics
- [x] Leave team-specific prediction for Commit 10
- [x] Clear notebook outputs before commit
