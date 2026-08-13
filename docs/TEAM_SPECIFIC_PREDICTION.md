# Team-specific prediction

Future or hypothetical fixtures are built from the named teams rather than a fixed demonstration vector.

Each current team state contains:

- latest Elo after the most recent completed match
- mean goals scored across the five most recent completed matches
- mean goals conceded across the same window
- number of matches used for form
- latest recorded match date

Historical training rows still use pre-match Elo and pre-match form. The current snapshot is only used when predicting a new fixture.

For neutral matches, the model evaluates both team orderings and averages the equivalent outcomes. Swapping the order of two teams therefore swaps their win probabilities while preserving the draw probability.

Unknown team names fail explicitly and provide close-name suggestions where possible.
