# Tournament weighting and match context

Tournament labels are Unicode-normalised and case-folded before matching.

The correction matters for `Copa América`: the original code searched for the unaccented text `Copa America`, so those matches fell into the generic weight bucket. In the supplied modern-era data, 248 Copa América matches now receive the intended major-tournament weight of 0.8.

The revised logic also avoids the earlier boolean-precedence ambiguity around qualification matches and stops broad `Euro` substring matching from treating `CONIFA European Football Cup` as a UEFA Euro final.

Validation outputs record the tournament-level counts, old and corrected weights, and the neutral-match totals.
