# F206 — a near-size spine can carry fixed-ratio side recursion, but the joint child congruences form an inversion torsor

## Status and scope

**Status:** self-audited, proof-only. It has not had the
required fresh hostile audit or blind reconstruction.

The closest prior routes are P165 and P180. P165 proves the one-child
recurrence for `K=(N-1)/2`. P180 proves the roughly half-size square-gap child
and its standalone orientation boundaries. F206 differs in two ways:

1. it proves the stronger recursion theorem with one near-size spine and
   quasipolynomially weighted fixed-ratio side recursion; and
2. it gives the exact joint local state produced by both factorizations.

This is not a factoring algorithm. The local-state theorem closes only
product, square-discriminant, quadratic-character, and genus-orientation
decoders. It does not close integer size, a nonlinear Archimedean statistic,
nonquadratic class-group navigation, adaptive bases, or an implicit evaluator
of the P179 twisted divisor coefficient.

## Theorem 1: one near-size spine plus fixed-ratio side work is QP

Fix `0<rho<1`. Let `Q` be a nondecreasing numerical quasipolynomial:

\[
1\le Q(n)\le 2^{C(\log_2(n+1))^k}
\]

for fixed `C>0` and integer `k>=1`. Suppose a nonnegative running-time
function satisfies, above a fixed base range,

\[
T(n)\le T(n-1)+Q(n)T(r(n))+Q(n),
\qquad r(n)\le \lceil\rho n\rceil+c,
\]

where `c` is fixed. Then there is a fixed `D` such that

\[
\boxed{T(n)\le 2^{D(\log_2(n+1))^{k+1}}.}
\]

Thus the recurrence is numerical QP. A fixed number of side children of
size at most `rho*n+O(1)` is covered by enlarging `Q`.

For a balanced split `N=pq`, `p<q<2p`, the auxiliary child

\[
K=(N-1)/2
\]

has at most `n-1` bits, while

\[
E=N-\lfloor\sqrt N\rfloor^2,
\qquad p,
\qquad q
\]

all have at most `n/2+O(1)` bits. Therefore a complete recursion which first
factors `K`, also factors `E`, and recursively completes both parent-output
factors is covered by Theorem 1 on the balanced promise, if its postprocessor
is QP.

This accounting does not cover an unbalanced all-input branch where the
auxiliary `K` call and a large parent-output cofactor are two independent
`n-O(1)`-bit children. Such a tree can have recurrence
`T(n)<=2T(n-1)+...`, which this theorem does not bound by QP.

## Theorem 2: exact joint root and inverse-torsor normal form

Let `N` be odd and put

\[
B=\lfloor\sqrt N\rfloor,
\qquad K={N-1\over2},
\qquad E=N-B^2.
\]

If `gcd(E,N)>1`, the square-gap child already gives a proper factor. Assume
from now on that

\[
\gcd(E,N)=1.
\]

Given the complete factorizations of `K` and `E`, put

\[
M=\operatorname{lcm}(K,E).
\]

For each prime power `ell^a || M`, define a local root by

\[
R_\ell\equiv
\begin{cases}
1\pmod{\ell^a},&v_\ell(K)\ge v_\ell(E),\\
B\pmod{\ell^a},&v_\ell(E)>v_\ell(K).
\end{cases}
\]

CRT constructs a public `R mod M` satisfying

\[
\boxed{R^2\equiv N\pmod M.}
\]

Given the two child factorizations, constructing `M` and `R` uses
deterministic polynomial bit complexity in the bit length of `N`.

Every ordered pair of units satisfying `xy=N mod M` is uniquely
parameterized by

\[
\boxed{(x,y)=(Ru,Ru^{-1}),\qquad u\in(\mathbb Z/M\mathbb Z)^\times.}
\]

Consequently there are exactly `phi(M)` locally product-consistent ordered
pairs, and

\[
\varphi(M)\ge \sqrt{M/2}
\ge {\sqrt{N-1}\over2}.
\]

For every such pair,

\[
\boxed{(x+y)^2-4N
\equiv R^2(u-u^{-1})^2\pmod M.}
\]

Thus the product and discriminant-square tests modulo the full joint child
modulus accept the entire inverse torsor.

Factor swap is exactly

\[
(x,y)\longleftrightarrow(y,x),
\qquad u\longleftrightarrow u^{-1}.
\]

Every quadratic character has the same value on `u` and `u^{-1}`. Every
symmetric ring expression in `x,y` is also unchanged by the swap. Hence these
interfaces cannot orient the smaller factor against the larger factor.

## Theorem 3: support-prime Jacobi signs are predetermined

Assume in addition that `N == 3 mod 4`. For every odd prime `ell` dividing
`K*E`, one has

\[
\boxed{\left({\ell\over N}\right)=(-1)^{(\ell-1)/2}=\chi_4(\ell).}
\]

Thus the Jacobi sign of every odd prime supplied by either complete child
factorization is fixed by its public residue modulo 4. It does not reveal
which hidden factor is `1 mod 4`.

In the F202 class-group formulation, the two mixed orientations have classes
`C^2` and `C^{-2}`. Every genus character is quadratic, so it gives `+1` on
both. Composing either orientation with any fixed auxiliary class has the
same genus vector. Factoring `K` therefore does not repair the genus gate by
quadratic characters alone.

## Exact remaining gate

The two child factorizations are complexity-safe on the balanced branch.
Their joint generic local information remains inversion-blind. A successful
postprocessor must use information not covered here, such as:

1. an Archimedean size or exact-division statistic that is not invariant
   under `u <-> u^(-1)`;
2. a nonquadratic full-class-group operation with a QP orientation rule;
3. an adaptive factor-free base/exponent transition not reduced to the fixed
   child-supported character data; or
4. the P179 twisted divisor coefficient or an equivalent integer-specific
   reciprocal-prefix selector.
