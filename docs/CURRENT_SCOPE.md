# Current implementation scope

The functional modelling pipeline is now complete.

It includes:

- Validated historical match data with deterministic `match_id`
- Leakage-safe rolling form
- Tournament context and neutral-venue features
- Pre-match Elo ratings
- Chronological model evaluation
- Class-balanced classification comparison
- Temporal probability calibration
- Log loss, Brier score, confusion matrices and per-class recall
- Team-specific feature construction
- Neutral-order-symmetric match probabilities
- Configurable 48-team-style tournament simulation
- Monte Carlo stage and champion probabilities

## Current prediction flow

A new fixture looks up both teams in the latest state snapshot, builds the eight model features and passes them to the probability model selected in Commit 9.

Tournament matches use neutral-venue predictions. The simulator then propagates those probabilities through group matches and knockout rounds.

## Remaining work

Commit 11 is the final consolidation pass: remove obsolete notebook sections, clean repeated documentation patterns, align the literature and methodology with the implemented project, prepare final result/poster material and verify a clean end-to-end run.
