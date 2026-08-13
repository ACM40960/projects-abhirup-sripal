# Chronological evaluation

The original prototype used a random 80/20 train-test split. That is a poor fit for forecasting because later matches can enter training while earlier matches appear in testing.

The final pipeline uses a fixed date boundary:

- training matches occur before 1 January 2023
- test matches occur on or after 1 January 2023

For the supplied modern-era modelling data this gives 21,712 training matches and 3,445 test matches.

The notebook checks that the two periods do not overlap and that every modelling row belongs to exactly one side of the split.

## Preprocessing

Scaling is only required by the Linear SVM. It is fitted inside the relevant training pipeline rather than on the full dataset. During temporal calibration, each SVM fold therefore learns its scaler from that fold's historical estimator-training rows.

Tree-based models use the unscaled feature values.

## Why this matters

The reported metrics are intended to approximate a forecasting setting. A model evaluated on randomly mixed historical periods can benefit from information patterns that would not have been available at the time of the earlier test matches.
