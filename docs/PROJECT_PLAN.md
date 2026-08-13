# Project development plan

Completed:

1. [x] Reorganise the project and add reproducible environment files
2. [x] Validate match data and assign deterministic identifiers
3. [x] Rebuild rolling team form without duplicate joins or current-match leakage
4. [x] Correct tournament weighting and match-context features
5. [x] Calculate and join pre-match Elo features using `match_id`
6. [x] Replace random splitting with chronological evaluation
7. [x] Add a class-prior baseline and efficient classification models
8. [x] Add class-balanced probability calibration and expanded evaluation
9. [x] Replace dummy prediction inputs with team-specific states and add tournament simulation

Final consolidation:

10. [ ] Align literature and methodology with the implementation
11. [ ] Produce final result and poster-ready outputs
12. [ ] Remove notebook leftovers and redundant preprocessing
13. [ ] Clean repeated documentation patterns
14. [ ] Verify a fresh end-to-end run and prepare the final release

These final items are intentionally grouped into Commit 11 rather than split into separate Git commits.
