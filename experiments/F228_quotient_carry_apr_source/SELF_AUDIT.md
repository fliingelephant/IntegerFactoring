# F228 self-audit

## Verdict

The theorem packet is internally consistent at its stated scope.  The main
positive infrastructure is the fixed-ratio recursion.  The main exact
obstruction is equation (8): quotient-side common-primary capacity is
already in a half-size carry defect.  The APR-compatible branch remains
open because the inverse-lift equations give no lower bound.

## Algebra checks

1. The signs in the two defects differ for a reason:
   `gcd(A,N)` uses `R-cB`, while reduction modulo a divisor of `N-1` uses
   `u-R+cB`.
2. Equation (6) requires `d` odd because `B` must be invertible.  The
   exponent of the common two-primary support need not be public.  It is
   outside the collapse theorem; no claim about it is made.
3. A prime dividing the multiplier `u` cannot be divided out in (10).  The
   statement excludes it and classifies it as public small-prime support.
4. The `i=0` power convention in (11) gives exactly `p=1 mod ell`.
5. The hidden integer `N^i-p` is nonzero at every nonnegative `i`, so the
   logarithmic support bound has no exceptional equality case.
6. A global-return exponent can still matter even when its common block is
   present in the defect.  The packet does not equate support with a valid
   order certificate.

## Complexity checks

The child-size bound is `n/2+polylog(n)`, not literally half size.  Replacing
it by `2n/3` only after a fixed base range is valid because `polylog(n)=o(n)`.
The number of children, prime occurrences, `ell-1` descendants, random bits,
and stored integers is numerical QP.  The theorem proves recursion size,
not an unconditional factorer for arbitrary recursive children.

## Probability checks

The random-shift theorem fixes the multiplier first.  It uses only the count
of one residue class in a consecutive interval and a union bound.  It does
not assume independence between different prime divisibility events.  It
does not cover random multipliers, heavy adaptive shifts, or a joint carry
computation.

## Computation checks and disclosed defect

D00 records the accidental un-timed local execution.  Its output was not
used as D01 evidence.  The remote D01 source hash matched the frozen local
source, and the remote/local output hashes matched.

D02's preregistration said a zero row would obstruct the complete fixed menu
even with hidden compatible-subset knowledge.  That wording was too strong
because a cap-rejected trial was not evaluated.  D03 repaired the evidence
boundary without modifying D02: it measured the no-cap predicate first.
D03 found no oracle-zero row.  The candidate therefore makes no numerical
source-obstruction claim.

The finite evidence is favorable at the tested sizes but decreases across
the fixed-parameter scale ladder.  Neither observation is an asymptotic
claim.

The named local verifier passed all six frozen input hashes, all row counts
and summaries, the rowwise D02/D03 cap-20 equality, the safe-prime cohort
identities, and all 96 D03 selected compatible-support certificates.  Its
stdout SHA-256 is
`6ab95948da2a42e462eb601ae23f5f26a79b0fffb5ec584762fa668b8e34cd06`.

## Remaining exact gap

One of the following is still needed:

- an all-input inverse-QP lower bound for compatible support exposed by an
  integer-biased multiplier/carry law;
- a sound factor transition from APR rejection;
- or a nonuniform annihilator/return source that uses the quotient event and
  is not reduced to uniform local-order sampling.
