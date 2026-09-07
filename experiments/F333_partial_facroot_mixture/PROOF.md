# Two sources remove the conditional-square cost requirement

**Family:** route:F31

Status: root-derived proof, pending independent reconstruction. This is a
conditional Las Vegas reduction; no fast partial FacRoot solver is supplied.

## One capped call

Write s>=2 for the number of distinct prime divisors of N. Squaring on the
unit group has kernel size 2^s by CRT, including repeated prime exponents.
The Jacobi symbol is a homomorphism to {+1,-1}, so its positive kernel J has
size at least |U|/2. Every square is in J. Consequently

    rho=|S|/|J| <= 2^(1-s) <= 1/2.

This includes the case where the Jacobi character is principal: no nonsquare
assumption on N is needed here.

Let r_S be the capped root-output probability on uniform a in S. Because a
valid unit root can exist only on S, and the same public procedure is used in
both modes,

    r_J=rho*r_S.

Let delta_S denote its total valid-output probability on S, so delta_S>=r_S.
In J mode the factor probability is f_J. In S mode P02 gives factor probability
at least delta_S/2, including any direct factor outputs. Hence the mixed ideal
attempt has success at least

    f_J/2+delta_S/4
      >= f_J/2+r_J/(4*rho)
      >= (f_J+r_J)/2.

This argument does not assert that a solver which succeeds on J necessarily
succeeds on nonsquares. Root-only success is supplied by the other mode.

## Generation without factors

Draw a uniform nonzero residue using fair-bit rejection. A nonunit is already
a proper divisor because zero was excluded. In J mode, negative-Jacobi units
are the only repeats. At least half of all units have Jacobi +1, so each draw
ends generation with probability at least 1/2. Conditional on reaching A, its
parameter is uniform in J. If generation instead produces a factor, that
immediate success can only increase the lower bound f_J for this mode.

The S mode needs one such nonzero draw. A nonunit is an immediate factor;
conditional on a unit, r is uniform in U and r^2 is uniform in S. A mixture
of immediate success and conditional success at least delta_S/2 is itself at
least delta_S/2. Thus the implemented attempt retains the delta_J/2 bound.
Each bounded residue draw uses fewer than two fair-bit rejection trials in
expectation and O(n) expected bits. Jacobi and gcd costs are polynomial in n.
There is no deterministic worst-case claim for these generation loops.

## Truncation and a uniform expected bound

Put delta=delta_J(N) and tau=tau_J(N). With B=ceil(2Q(n)), Markov's inequality
gives

    Pr_J(call cost>B) <= tau/B <= delta/2.

Therefore the capped J call still returns a valid output with probability at
least delta/2, and the preceding mixture succeeds with probability at least
delta/4. Since tau>=1 and tau/delta<=Q, one also has delta>=1/Q. Each mixed
attempt costs at most B plus expected polynomial generation and final-gcd
work. Independent restart consequently costs

    O((Q(n)+poly(n))/delta)
      = O(Q(n)^2+poly(n)*Q(n)).

No cost over the rare square subset enters this bound; the same explicit cap
is imposed there. Costs within an attempt may correlate with its success.
Only fresh independent attempts are needed for the renewal calculation.

Budget construction is also charged. The displayed capped cost uses a Q
whose budget is evaluable within that cost, such as the standard integer
envelope 2^(c*ceil(log2(n+1))^k) for fixed positive integers c,k. If Q is
merely computable with no evaluation-time bound, use such an efficiently
computable quasipolynomial majorant and state the capped cost in terms of
that majorant, or charge the actual evaluation cost. The uncapped dovetail
below has no such budget-computation requirement.

For arbitrary input, first handle primes, remove powers of two, and detect
proper perfect powers using polynomial-bit routines. A remaining odd composite
has at least two distinct primes and meets the reduction's hypotheses. A
verified split reduces to smaller positive integers. There are at most O(n)
splitting nodes and polynomially many preprocessing operations; replacing Q
by a monotone quasipolynomial upper envelope makes their summed expectation
quasipolynomial. Correctness follows from verified divisions, exact power
identities, and certified primality. Positive success probability and finite
expected restart cost give almost-sure termination at every node.

The reduction thus accepts an average cost/success contract over the dense
Jacobi-positive parameter set for each fixed N. It does not establish such a
contract for F326, the feedback policies, or any other proposed solver.

## Uncapped dovetailing avoids even knowing the envelope

Let f=f_J and r=r_J for uncapped A, so delta=f+r. Write tau_S for the
conditional mean cost on uniform squares. Nonnegative costs and S subset J
give rho*tau_S<=tau_J, even when tau_S is much larger than tau_J. Also
r=rho*r_S, by the same output-law identity as above.

The J retry engine has success at least f and mean attempt cost at most
g+tau_J. Its expected work to a factor is therefore at most (g+tau_J)/f
when f>0. The square retry engine has success at least r_S/2 and mean
attempt cost at most g+tau_S. When r>0, its expected work is at most

    2*(g+tau_S)/r_S
      <= 2*(rho*g+tau_J)/r
      <= 2*(g+tau_J)/r.

Interpret the corresponding bound as infinity if its denominator is zero.
Since f+r=delta>0, at least one engine has finite expected work. If
f>=delta/3, the first bound is at most3*(g+tau_J)/delta. Otherwise
r>2*delta/3 and the second bound is below that same value.

Interleaving one bit operation of each engine costs at most twice the work
that either engine needs by itself. Each engine has persistent machine state
and private random tapes, so a slow call does not prevent the other engine
from progressing. Taking expectations proves the claimed factor6 bound.
This argument does not require cost and success to be independent inside an
attempt. It uses fresh attempts within each engine and the renewal bound.

Because tau_J>=1, the contract tau_J/delta<=Q also implies1/delta<=Q.
The bound is therefore O(poly(n)*Q(n)); the previous all-input reduction and
almost-sure termination arguments apply. The two fixed machines can be
interleaved on a constant-tape bit model with constant per-step overhead.
No oracle for which engine is faster, no supplied envelope Q, and no
worst-case-fast individual attempt is required by this alternative.

## Prior navigation and intended use

Scoped Rust searches for partial FacRoot, FacRoot, and result-level mixtures
found P02, P246, C284 and P247 as the closest records. C284 uses a contract on
random squares. P247 supplies a conditional fixed-input matching law. The
current distinction is the two-mode reduction and truncation of an otherwise
uncontrolled conditional-square cost. This is not a literature-wide novelty
assessment. The useful next mathematical question is whether a solver can
exploit average arithmetic structure on the full Jacobi-positive set.
