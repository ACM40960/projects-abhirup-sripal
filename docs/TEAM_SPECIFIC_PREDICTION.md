# Team-specific match prediction

The original tournament demonstration accepted team names but ignored them when constructing the model input. Every fixture was evaluated with the same fixed feature vector.

Commit 10 removes that placeholder.

## Current team state

Each team now has a state snapshot containing:

- Post-match Elo after its latest completed match in the dataset
- Mean goals scored across its five most recent completed matches
- Mean goals conceded across the same window
- Number of matches available in that form window
- Date of its latest recorded match

The snapshot is written to `outputs/team_state_snapshot.csv`.

Historical training rows still use pre-match form and pre-match Elo. The current snapshot is only used when constructing a new future or hypothetical fixture.

## Building a fixture

`build_match_features(home_team, away_team, ...)` creates the exact eight-column feature row used by the selected probability model.

For a neutral tournament match, `get_match_probabilities(...)` evaluates both team orderings and averages the equivalent outcomes. That prevents a team from gaining an artificial advantage because it happened to be passed as the first argument.

Unknown team names raise an error and return close matches when possible.

## Model use

The simulator uses the probability model selected in Commit 9. It is not silently replaced by another classifier in this stage.

Examples are saved in `outputs/team_specific_prediction_examples.csv`, with an additional neutral-order symmetry check in `outputs/team_prediction_validation.csv`.
