# Source checks

**Family:** route:F31

Questions posed for the focused search: what fixed-denominator mean or tail
bounds already exist for the sum of continued-fraction digits, and what
explicit prime count in [H,2H] suffices to turn the finite cofactor bound
into an infinite balanced-input family? The author digit-count proof was
derived before this lookup. Search date: 2026-09-07.

- Christoph Aistleitner, Bence Borda, and Manuel Hauke,
  [On the distribution of partial quotients of reduced fractions with fixed denominator](https://arxiv.org/html/2210.14095),
  arXiv:2210.14095v2, 2023. Theorem 1 proves concentration near
  (12/pi^2) log N log log N for every fixed denominator; its stated tail
  parameter range is t<=(log N)^C. The introduction records the stronger
  known mean asymptotic (6/pi^2)(log N)^2, and the paper uses reversal in
  its counting argument. Our elementary bound is a reproducible sufficient
  estimate, not a new CF distribution theorem. Its all-cutoff Markov
  consequence is used here instead of importing Theorem 1 outside its
  stated range. The primary HTML and abstract were read; the persistent
  Sol was asked to cache the paper through the unchanged download-ref skill.
- J. Barkley Rosser and Lowell Schoenfeld,
  [Approximate formulas for some functions of prime numbers](https://doi.org/10.1215/ijm/1255631807),
  Illinois Journal of Mathematics 6 (1962), 64--94. Page 69, Corollary 3,
  equation (3.8), gives pi(2x)-pi(x)>3x/(5 log x) for x>=20.5. The frozen
  statement uses the weaker threshold H>=21. The primary paper was read
  in [this PDF scan](https://denisevellachemla.eu/Rosser-Schoenfeld-1962.pdf).
  This prime-count inequality is the sole external theorem in the
  infinite-family conclusion. The finite cofactor bound does not require
  it. The persistent Sol reported that the DOI metadata fetched but its
  helper PDF tiers missed; the required fallback lacked Playwright.
  No alternate cache workflow or helper edit was performed by this worker.

Repository navigation used P248 and P249, plus F330's count-descent design
and unpromoted discrepancy note. Scoped reader queries for dyadic methods,
continued fractions, triangular profiles, rational rotations, and short
rational inputs found no earlier result proving this particular descent
mass bound. That is a limited repository check, not external novelty
evidence. The short-rational profile is author-derived and remains separate
from the frozen mass statement.
