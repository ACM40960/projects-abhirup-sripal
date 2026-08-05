# Current implementation scope

At this repository stage, the notebook contains the original prototype implementation:

- historical international match loading;
- five-match rolling form features;
- tournament importance weights;
- neutral venue flag;
- Elo ratings;
- SVM and MLP classifiers;
- a four-team Monte Carlo demonstration.

Known issues intentionally left for later commits:

- rolling-feature merge can duplicate observations;
- random train-test splitting is not suitable for forecasting;
- the full RBF SVM is slow;
- simulation inputs are not team-specific;
- the tournament demonstration is not the complete 2026 format;
- the literature review includes features not implemented in the notebook.
