# Tournament simulation

The simulator expects 48 unique teams and models 12 groups of four followed by a 32-team knockout stage.

Each group plays a round robin. The top two sides advance together with the eight best third-place teams.

## Generic demonstration

The generic simulation in `03_team_prediction_and_tournament.ipynb` uses the top 48 teams in the frozen Elo snapshot.

This output is retained as a reproducible modelling demonstration rather than an official World Cup forecast.

The default run uses 2,000 iterations with seed 42.

## Actual-field retrospective simulation

The post-tournament analysis in `04_world_cup_2026_backtest.ipynb` uses the actual 48-team 2026 group field and compares simulated progression with the completed tournament.

This is still an approximate tournament model rather than an exact FIFA reconstruction.

## Simplifications

The match model predicts outcome probabilities rather than scorelines, so official goal-difference tiebreaks cannot be reproduced. Group ties use points followed by the frozen Elo snapshot.

The round-of-32 pairing is seeded and avoids same-group opponents where possible. It is not presented as the official FIFA bracket map.

If a knockout match is drawn in regulation, advancement is sampled from the two teams' relative non-draw probabilities.

Simulated tournament matchups are treated as neutral. The actual-field Monte Carlo comparison therefore does not reproduce host-country venue advantage for Mexico, Canada or the United States.
