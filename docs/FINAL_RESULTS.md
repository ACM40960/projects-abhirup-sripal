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
