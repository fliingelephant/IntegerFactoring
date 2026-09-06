# F203 provenance

F203 was derived from the promoted P175 reciprocal-prefix target and P177's
arithmetic-progression cell boundary. The user explicitly corrected the
recursion criterion: one strictly descending recursive child can lose only
one bit and still preserve numerical quasipolynomial time. The quotient
section keeps that correction exact.

The closest prior promoted interfaces are:

- P29 and P170, where the untwisted divisor sum
  \(\sigma_1(N)=N+p+q+1\) is already a factoring coefficient;
- P165, where recursively factoring \((N-1)/2\) is a valid one-child
  preprocessing step but independent uniform-base return remains rare;
- P166/F189, where a segment-Jacobi zero oracle conditionally isolates a
  factor but ordinary reciprocity leaves the non-coprime correction
  unevaluated;
- P175, where a quarter-minus-polylog prefix of \(p^{-1}\) is terminal; and
- P177, where the missing prefix cell is one power-of-two arithmetic
  progression and the surviving opening is a nonlocal integer statistic.

F203 differs from the segment-product gate. Its selector is the exact
coefficient of a periodic weighted divisor sum. The factor weights \(d\)
retain the Archimedean ordering information that an ordinary product of
quadratic signs loses. At modulus two, the periodic weight becomes
\(\chi_4\), but the needed coefficient is weighted by the divisor itself.

The Lambert-series identity, the sibling relation, and the quotient
coalescence are proved directly from finite integer algebra. No external
source is needed for the mathematical claims. No numerical experiment was
run.

The artifact intentionally makes no literature-priority claim and no claim
that a modular-form, theta-series, reciprocity, factorial, or recursive
algorithm evaluates the coefficient in numerical QP time.

