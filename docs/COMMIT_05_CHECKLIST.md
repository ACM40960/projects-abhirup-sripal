# Commit 5 checklist: tournament weighting correction

- [x] Normalise tournament names for case and accents.
- [x] Recognise `Copa América` as `Copa America`.
- [x] Correct Copa América weight from the previous fallback 0.4 to 0.8.
- [x] Apply the qualification exclusion to the complete major-final condition.
- [x] Preserve the intended weights for World Cup, major finals, qualifications, Nations League, friendlies and other competitions.
- [x] Validate the 248 modern-era Copa América matches.
- [x] Confirm zero Copa América matches retain weight 0.4.
- [x] Write a machine-readable tournament-weight validation table.
- [x] Keep the Commit 4 rolling-form pipeline unchanged.
- [x] Do not modify the Elo merge; it is Commit 6 scope.

## Commit message

```bash
git commit -m "fix: correct tournament weighting and match context features"
```
