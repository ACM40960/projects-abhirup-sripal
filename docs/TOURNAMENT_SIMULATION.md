# Tournament simulation

The simulator accepts 48 unique teams and creates 12 groups of four.

Each group plays a round robin. The top two sides advance together with the eight best third-place teams, producing a 32-team knockout stage.

## Simplifications

The match model predicts outcome class probabilities rather than scorelines, so official goal-difference tiebreaks cannot be reproduced. Group ties use points followed by the pre-tournament Elo snapshot.

The round-of-32 pairing is seeded and avoids same-group opponents where possible. It is not presented as the official FIFA bracket map.

If a knockout match is drawn in regulation, advancement is sampled from the two teams' relative non-draw probabilities.

## Demonstration field

The repository does not contain an authoritative participant list. The bundled simulation therefore uses the top 48 teams in the current Elo snapshot.

This makes the output a reproducible modelling demonstration rather than an official World Cup forecast.

The default run uses 2,000 iterations with seed 42.
