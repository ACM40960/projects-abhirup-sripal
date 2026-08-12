# Tournament weighting and match context

## Commit 5 purpose

Commit 5 corrects the tournament-name matching used to create `match_weight` and validates the neutral-venue flag. It intentionally does not modify Elo merging or train/test splitting.

## Active bug fixed

The source dataset uses the accented tournament label `Copa América`. The earlier function searched for the unaccented string `Copa America`, so modern Copa América finals fell into the generic 0.4 bucket instead of the intended 0.8 major-tournament bucket.

The corrected implementation case-folds and Unicode-normalizes names before matching. In the supplied 2000+ data, 248 Copa América matches are now assigned 0.8.

## Boolean-precedence fix

The earlier condition combined `or` and `and` without grouping, so the qualification exclusion applied only to the final `Euro` clause. The corrected function first defines explicit major-final names and then applies the qualification exclusion to the whole group.

## False-positive cleanup

The old substring check for `Euro` also classified `CONIFA European Football Cup` as a major UEFA final. Explicit matching against `UEFA Euro` prevents this. In the current modern-era data, 49 such matches return to the generic 0.4 bucket.

## Validation outputs

- `outputs/tournament_weight_validation.csv` lists tournament-level counts and original/corrected weights.
- `outputs/match_context_validation.csv` records aggregate checks, including Copa América coverage and weight-category counts.

## Scope boundary

The Elo stage still joins on date/home-team/away-team in the original later notebook cells. That is reserved for Commit 6.
