# Final results

## Dataset and evaluation

- 49,215 completed matches remain after validation
- 25,157 matches from 2000 onward form the modelling dataset
- 21,712 matches are used for training
- 3,445 matches from 2023 onward form the chronological test set

## Final probability comparison

|   probability_rank | model                                    |   accuracy |   balanced_accuracy |   macro_f1 |   away_win_recall |   draw_recall |   home_win_recall |   log_loss |   multiclass_brier |
|-------------------:|:-----------------------------------------|-----------:|--------------------:|-----------:|------------------:|--------------:|------------------:|-----------:|-------------------:|
|                  1 | Calibrated Linear SVM                    |     0.5962 |              0.5006 |     0.4449 |            0.6236 |        0.0113 |            0.8668 |     0.8917 |             0.5249 |
|                  2 | Calibrated Balanced HistGradientBoosting |     0.5835 |              0.4836 |     0.4290 |            0.5647 |        0.0063 |            0.8798 |     0.9257 |             0.5433 |
|                  3 | Class-prior baseline                     |     0.4685 |              0.3333 |     0.2127 |            0.0000 |        0.0000 |            1.0000 |     1.0557 |             0.6373 |

The selected model is **Calibrated Linear SVM** with chronological test log loss **0.8917** and multiclass Brier score **0.5249**.

Its argmax accuracy is **59.62%** and macro F1 is **0.4449**.

## Draw interpretation

The test set contains draws at a rate of **23.08%**. The selected model's mean predicted draw probability is **22.45%**, while its hard argmax draw recall is only **1.13%**.

These numbers answer different questions. Draw recall asks how often `Draw` is the single highest-probability class. The simulator instead samples from the full probability vector, so calibration and log loss are more relevant to its use case.

Across the ten draw calibration bins, the mean absolute gap between predicted and observed draw frequency is **0.018**.

## HGB calibration check

| variant                            |   accuracy |   macro_f1 |   draw_recall |   log_loss |   multiclass_brier |
|:-----------------------------------|-----------:|-----------:|--------------:|-----------:|-------------------:|
| Balanced HGB raw probabilities     |     0.5585 |     0.5104 |        0.2491 |     0.9143 |             0.5405 |
| Balanced HGB temporally calibrated |     0.5835 |     0.4290 |        0.0063 |     0.9257 |             0.5433 |

The balanced HGB model was explicitly recalibrated under the same expanding temporal design as the SVM. Calibration did not improve its probability metrics enough to overtake the SVM, so the final model choice is robust to the fairness concern raised during review.

## Tournament demonstration

The bundled tournament is a 2,000-iteration, seed-42 demonstration using the top 48 teams in the current Elo snapshot.

| team        |   champion_probability |   final_probability |   sf_probability |
|:------------|-----------------------:|--------------------:|-----------------:|
| Argentina   |                 0.2320 |              0.3225 |           0.4575 |
| Spain       |                 0.2285 |              0.3350 |           0.4675 |
| France      |                 0.1220 |              0.2200 |           0.3475 |
| England     |                 0.0770 |              0.1390 |           0.2555 |
| Netherlands |                 0.0460 |              0.1115 |           0.2155 |
| Japan       |                 0.0400 |              0.0840 |           0.1875 |
| Morocco     |                 0.0390 |              0.0965 |           0.2040 |
| Germany     |                 0.0355 |              0.0955 |           0.2010 |
| Portugal    |                 0.0330 |              0.0845 |           0.1790 |
| Brazil      |                 0.0280 |              0.0645 |           0.1625 |

These are model outputs for the bundled demonstration field, not official World Cup probabilities.


## Retrospective 2026 World Cup backtest

The selected model is frozen before tournament outcomes enter the retrospective analysis. All 104 World Cup matches are evaluated from the same team-state snapshot ending on 31 March 2026.

| Metric | Estimate | 95% bootstrap interval |
|---|---:|---:|
| Accuracy | 0.606 | 0.510–0.702 |
| Log loss | 0.884 | 0.786–0.984 |
| Multiclass Brier | 0.524 | 0.452–0.597 |

The historical class-prior baseline scores **47.1%** accuracy, **1.054** log loss and **0.636** Brier on the same tournament matches.

### Draw interpretation

The tournament draw rate is **23.1%** and the frozen model assigns a mean draw probability of **21.5%**. Draw is never the argmax class in this 104-match sample, so argmax draw recall is **0%**.

That is consistent with the behaviour already identified on the larger chronological holdout: draw recall describes hard classification, while the Monte Carlo system consumes the full probability vector. World Cup probability scoring therefore remains the primary post-tournament diagnostic.

### Group versus knockout performance

| split          |   matches |   accuracy |   log_loss |   multiclass_brier |   actual_draw_rate |   mean_predicted_draw_probability |   argmax_draw_prediction_rate |   argmax_draw_recall |
|:---------------|----------:|-----------:|-----------:|-------------------:|-------------------:|----------------------------------:|------------------------------:|---------------------:|
| Overall        |       104 |     0.6058 |     0.8840 |             0.5236 |             0.2308 |                            0.2150 |                        0.0000 |               0.0000 |
| Group stage    |        72 |     0.5556 |     0.9301 |             0.5589 |             0.2778 |                            0.2085 |                        0.0000 |               0.0000 |
| Knockout stage |        32 |     0.7188 |     0.7801 |             0.4440 |             0.1250 |                            0.2294 |                        0.0000 |               0.0000 |

The stronger knockout-stage point estimate should not be overinterpreted: only 32 knockout matches are available, and the analysis is explicitly presented as a single-tournament stress test rather than a new model-selection set.

### Actual-field tournament comparison

The separate 2,000-run simulation uses the actual 48-team group field while retaining the project's documented approximate knockout mapping.

- Spain: **25.7%** title probability, rank **1**, actual finish **Champion**
- Argentina: **21.2%**, rank **2**, actual finish **Runner-up**
- England: **7.4%**, rank **4**, actual finish **Third**
- France: **12.4%**, rank **3**, actual finish **Fourth**

These retrospective outputs do not replace the main 2023–March 2026 chronological holdout and were not used to retune or reselect the classifier.
