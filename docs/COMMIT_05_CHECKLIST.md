# Commit 5 checklist: tournament weighting and match context

## Requirements completed

- [x] Case-normalize tournament labels
- [x] Unicode-normalize accented labels
- [x] Correct `Copa América` weighting
- [x] Apply qualification exclusion to the full major-final condition
- [x] Avoid broad `Euro` substring false positives
- [x] Preserve the one-row-per-match model table
- [x] Validate neutral venue as a binary feature
- [x] Write tournament-level validation output
- [x] Write aggregate match-context validation output
- [x] Clear notebook outputs before commit

## Expected supplied-data checks

- Modern-era matches: 25,157
- Copa América finals: 248
- Copa América finals assigned 0.8: 248
- Rows changed versus original tournament-weight logic: 297
  - 248 Copa América rows corrected from 0.4 to 0.8
  - 49 CONIFA European Football Cup rows corrected from 0.8 to 0.4

## Scope intentionally left unchanged

- Elo feature join
- chronological train/test evaluation
- model replacement
- team-specific tournament prediction

## Commit message

```bash
git commit -m "fix: correct tournament weighting and match context features"
```
