# Data validation

This commit adds an explicit validation stage before feature engineering.

## Checks performed

- verifies that `results.csv` contains all nine required source columns;
- parses match dates with invalid values converted to missing;
- converts home and away scores to numeric values;
- counts and removes records without a valid date or complete score;
- counts and removes exact duplicate rows;
- reports records sharing the same date, home team and away team for manual review;
- assigns every retained match a deterministic `match_id`;
- writes a machine-readable validation summary to `outputs/data_validation_summary.csv`;
- writes possible duplicate match keys to `outputs/duplicate_match_keys.csv`.

## Current dataset findings

The source contains 49,287 rows. Seventy-two rows have missing home and away scores and are removed from the completed-match dataset. No invalid dates or exact duplicate rows were found. One date/home/away key is repeated across two source rows with different scores, so both rows are retained and reported rather than silently deleted.

After validation, 49,215 completed matches remain. Filtering to matches from 1 January 2000 onward leaves 25,157 modelling records.

## Identifier design

`match_id` is a deterministic SHA-1-derived identifier based on the complete validated source record. SHA-1 is used here only to create stable identifiers, not as a security mechanism.

## Scope boundary

This commit validates the match records but does not yet repair the rolling-form merge. The existing prototype can still duplicate modelling rows when it joins team form by date and team alone. That issue is reserved for the next feature-engineering commit.
