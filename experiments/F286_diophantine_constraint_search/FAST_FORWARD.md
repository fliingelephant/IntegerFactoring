# F286: exact endpoint maps and a certified block jump

Status: proof candidates, not independently verified or promoted.
No new computational sweep was run. Earlier packets and outputs are unchanged.

## Candidate stated before prior lookup

Study the right endpoint of a surviving arc left of sqrt(N), alternating
the local-minimum cuts for x+y and x+2y. Express a complete pair of updates
as a map on the integer sum threshold. Then ask whether a stable rounded
x-coordinate permits skipping many sum thresholds at once.

After deriving this object, the Rust reader was used to inspect P80 and P168.
P80's quotient fibre concerns products of canonical inverse relations and
the identity gcd(P,K-r). P168 concerns whether a Euclidean remainder retains
hidden prime support. Neither is used here: the present state is an exact
real hyperbola arc with two prescribed integer residue coordinates. No old
relation word or quotient-support source is being renamed.

## Exact maps: one cycle is exactly one sum step

Fix M, a unit u modulo M, and v=N/u modulo M. Write s0=u+v and t0=u+2v,
with congruences always interpreted modulo M. Let C_r(z) be the least integer
congruent to r modulo M that is >=z, and F_r(z) the largest such integer <=z.

After a sum cut the right endpoint has the form

    x(S) = (S - sqrt(S^2-4N))/2,   S == s0 (mod M), S>=2 sqrt(N).

Define

    H(S) = x(S)+2N/x(S) = (3S+sqrt(S^2-4N))/2 = 2S-x(S),
    K(T) = (3T-sqrt(T^2-8N))/4,   T>=3 sqrt(N).

On these branches K is the inverse of H. A cut by x+2y and then x+y gives

    T = C_t0(H(S)),
    S_next = C_s0(K(T)).

If H(S) is already on its residue grid, this is a fixed endpoint and

    x=2S-T,   y=T-S

are positive integers in the prescribed residue classes with xy=N. Verify
the product and nontriviality to extract the factor.

Otherwise S_next=S+M **exactly**. Indeed H'(S)>2 away from the lower endpoint,
so its inverse has derivative between 0 and 1/2. The rounding raises H(S)
by a number strictly between 0 and M. Therefore

    S < K(T) < S+M/2,

and rounding to the S-grid gives S+M. The boundary S=2 sqrt(N) follows by
continuity and strict increase. This is not merely an asymptotic slow-step
estimate: this two-form propagation is a residue-strided sum scan.

Quantities that must remain fixed for this identity are the modulus, the
two residue classes, the smaller-root branch, and the ordered pair of forms.
It applies while the moving right endpoint is not clipped by the left
endpoint or another constraint. It is not a claim about an arbitrary
larger-menu sweep.

## A positive exact jump across one rounded-coordinate cell

Set X=F_u(x(S)) and assume X>0. Since

    T = 2S-X,

the extra integer quantity in the T-update is precisely this rounded x
coordinate. If x(S)=X, the factor point has already been reached. Otherwise

    X < x(S) < X+M.

No x in this open interval has residue u. Since x(S) decreases with S, all
sum thresholds before the crossing x=X can be skipped. The exact safe jump is

    S_jump = C_s0(X+N/X).

Test X for divisibility at this boundary. If X divides N, then N/X has residue
v (because X is a unit modulo M), and X+N/X lies on the S-grid. The boundary
is an exact factor point. If it does not divide N, the jump passes the
crossing, and no skipped S-grid point was a compatible factor point.

The calculation uses rational division, a quadratic root floor to find X,
and residue rounding. Its operand bit lengths are polynomial in the input
and state bit lengths. It skips an arbitrarily long sequence in one step
when the current x-cell corresponds to a long sum interval.

**Exact example.** Take N=47423, M=8, u=7, v=1, and S=1000. The sum grid is
0 modulo 8. On the smaller-root branch,

    47 < x(1000) < 55,

because 47+47423/47=1056>1000 and 55+47423/55<1000. Hence X=47. The rule
jumps directly to S=1056, bypassing the intermediate thresholds
1008,1016,1024,1032,1040,1048. The public boundary division verifies
47423=47*1009. No factor label is needed to compute X or the jump.

## Why repeated cell jumps are not a Euclidean acceleration

Suppose X<=sqrt(N/2), X-M>0, and the divisibility test fails. Put
g(x)=x+N/x. On 0<x<=X, g is decreasing with |g'(x)|>=1. The boundary
rounding changes g(X) by a number strictly between 0 and M. Thus

    X-M < x(S_jump) < X,

and the next rounded coordinate is exactly X-M. In this subdomain, repeated
cell jumps are simply trial division along one residue class, in decreasing
order. The shortcut genuinely batches sum thresholds, but it does not
compress the number of possible divisor coordinates. Near sqrt(N) the sum
coordinate itself is cheaper. Merely choosing between these two coordinates
does not establish an all-input quasipolynomial bound.

This pinpoints the failed fast-forward assumption: a stable floor label
permits one certified jump, but its next label need not be reachable by a
Euclidean quotient contraction. In the stated region it moves by exactly M.

## What a different continued-fraction block certificate must control

A larger x-block [L,U] can be certified with a nearly constant positive form
f(x)=a x+bN/x. Compute its exact minimum m and maximum h on that block. The
only possible factor traces are

    t == a u+b v (mod M),   m<=t<=h.

If h-m<M there is at most one such trace. A square-discriminant test plus
integer-root, residue, interval, and product checks then either finds all
factor points in the block or certifies the entire block empty. This is a
stronger block operation than stepping through local minimum thresholds.

Its exact variation can be controlled without assuming a stable derivative:
for a center c and x=c+d>0,

    f(c+d)-f(c)
      = (a-bN/c^2)d + bN d^2 / (c^2(c+d)).

Thus a proposed block needs both a rational-slope approximation and an
explicit curvature bound. Stability of a continued-fraction prefix alone
does not bound the final term or exclude an intermediate valid trace.

After this derivation, a focused primary-source check found that this
near-constant-linear-form block mechanism is already the Lehman mechanism
described by David Harvey, *Recent progress on deterministic integer
factorisation*, slides 7–11 (25 September 2023). It chooses a rational
approximation to N/c^2, balances linear error and curvature, and obtains
blocks of width on the N^(1/6) scale near sqrt(N). Therefore this final
paragraph supplies a known benchmark, not a novelty claim. Source:
https://web.maths.unsw.edu.au/~davidharvey/talks/rtca2023.pdf

## Concrete next question

Can several already retained congruence cuts certify a long block empty even
when every individual near-constant form admits multiple trace values,
without enumerating their Cartesian product or solving the same conic grid
intersection point by point? A candidate must state a joint block
certificate and its evaluation cost. The present two-form map and its stable
x-cell jump do not supply one.
