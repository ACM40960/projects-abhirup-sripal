# Tournament simulation

Commit 10 replaces the four-team hard-coded demonstration with a configurable 48-team-style Monte Carlo tournament.

## Format implemented

The simulator expects 48 unique teams and creates 12 groups of four.

Each group plays a round robin. A win is worth three points and a draw one point. The top two teams in every group advance, followed by the eight best third-place teams, producing a 32-team knockout field.

The knockout stage then runs:

- Round of 32
- Round of 16
- Quarter-finals
- Semi-finals
- Final

## Modelling assumptions

This is a tournament model, not a complete implementation of FIFA competition regulations.

The match model predicts away win, draw and home win rather than a scoreline, so official goal-difference tiebreaks cannot be reproduced. Group ties are resolved by points and then the pre-tournament Elo snapshot.

The round-of-32 bracket is built from tournament seeding and avoids same-group pairings where possible. It does not claim to reproduce an official FIFA bracket mapping.

If a knockout match is drawn in regulation, the simulator uses the two teams' relative non-draw probabilities to choose who advances through the extra-time/penalty stage.

## Default demonstration

The repository does not contain an authoritative World Cup participant list. The bundled demonstration therefore uses the top 48 teams in the current Elo snapshot.

`build_seeded_groups(...)` and `run_monte_carlo_tournament(...)` accept a different 48-team list, so an official participant list can be supplied without changing the prediction model.

## Reproducibility

The bundled run uses 2,000 iterations with seed 42.

Outputs:

- `outputs/tournament_group_configuration.csv`
- `outputs/tournament_simulation_results.csv`
- `outputs/tournament_simulation_validation.csv`
- `outputs/figures/champion_probabilities.png`
