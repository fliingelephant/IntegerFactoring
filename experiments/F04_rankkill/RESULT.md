# F04 rank-separator kill result (candidate)

## Exact claim refuted

Let

\[
H_a=(X+a)^N-X^N-a\in (\mathbb Z/N\mathbb Z)[X]/(X^r-1).
\]

For the standard minimal AKS modulus `r` and every standard AKS shift `a`,
it is **not** true that the kernel dimensions of multiplication by `H_a`
must differ over two unknown prime components.  The explicit counterexample
is

\[
N=79403=271\cdot293,\qquad r=269,
\]

for which both local kernel dimensions are zero for every `1 <= a <= 266`.
They remain zero at the adjacent ceiling-convention shift `a=267`.

This closes only the universal standard-parameter rank-separation premise.
It does not rule out nonstandard `r`, other group-algebra elements, or an
asymptotic randomized distribution on shifts.

## Standard AKS parameters

The factors 271 and 293 are prime by trial division through their square
roots.  The exact inequalities

\[
79403^4>2^{65},\qquad 79403^{61}<2^{993}
\]

give

\[
264<(\log_2N)^2<265.
\]

For every `s <= 265`, `ord_s(N) <= phi(s) <= s-1 <= 264`.  Moreover
`phi(266)=108`, `phi(267)=176`, and `phi(268)=132`, so none of 266, 267,
or 268 qualifies.  Modulo 269,

\[
N\equiv48,\qquad 48^{134}\equiv-1,\qquad48^4\equiv239\pmod {269}.
\]

Since `268=4*67`, these two proper-divisor tests prove
`ord_269(N)=268`.  Thus 269 is the minimal standard AKS modulus.

Here `phi(269)=268`, and the same logarithmic bounds imply

\[
266<\sqrt{268}\log_2N<267.
\]

Indeed the lower square is greater than
`268*(65/4)^2=70768.75>266^2`, while the upper square is less than
`268*265=71020<267^2`.  Hence the standard floor shift bound is 266.
Both prime factors exceed 269, so the preceding AKS gcd scan through `r`
does not already split this input.  The input is not a perfect power.

## Local algebra and nullity

For `N=pq`, put

\[
h_{m,a}(Y)=(Y+a)^m-Y^m-a.
\]

Reduction modulo `p` gives

\[
H_a=h_{q,a}(X^p),
\]

and symmetrically modulo `q`.  Because `gcd(p,269)=gcd(q,269)=1`, the
substitutions `X -> X^p` and `X -> X^q` are automorphisms of the respective
quotient algebras.  Also `Y^269-1` is squarefree in both characteristics.
Consequently the two local nullities are exactly

\[
\nu_p(a)=\deg\gcd(h_{q,a},Y^{269}-1),\qquad
\nu_q(a)=\deg\gcd(h_{p,a},Y^{269}-1).
\]

The nontrivial cyclotomic factor degrees are particularly simple.
Modulo 269, `p=271` is 2, whose order is 268: Euler's criterion gives
`2^134=-1` because `269=5 (mod 8)`, and `2^4 != 1`.  Also `q=293` is 24,
whose order is 67, as the exact chain

\[
24^2=38,\ 24^4=99,\ 24^8=117,\ 24^{16}=239,\
24^{32}=93,\ 24^{64}=41,\ 24^{67}=1\pmod {269}
\]

shows (67 is prime and `24 != 1`).  Therefore

- over `F_271`, `Y^269-1` has factor degrees `1,268`;
- over `F_293`, it has factor degrees `1,67,67,67,67`.

For a nontrivial 269th root `zeta`, define

\[
G_a(Y)=(Y^2+a)(Y+a)^{22}-Y^{24}-a.
\]

In characteristic 271, Frobenius and `293=271+22` give
`h_(293,a)(zeta)=G_a(zeta)`.  In characteristic 293, if
`h_(271,a)(zeta)=0`, then `zeta+a != 0` (the nontrivial roots are not in
the base field), and `271=293-22` gives the equivalent equation
`G_a(zeta)=0`.

The `Y^24` leading terms in `G_a` cancel, and its `Y^23` coefficient is
`22a`.  Thus for every nonzero `a`, `G_a` is a nonzero polynomial of degree
23.  It cannot be divisible by any of the nontrivial factors above, whose
degrees are at least 67.  Only `Y-1` can remain.

At `Y=1`, writing `b=1+a`, the root condition is `b^293=b` in `F_271`
and `b^271=b` in `F_293`.  Since

\[
\gcd(22,270)=\gcd(270,292)=2,
\]

the only possibilities are `b=0,+1,-1`, or `a=-1,0,-2`.  At `a=0`, the
whole error polynomial is zero and the local nullity is 269; at `a=-1,-2`
the nullity is exactly 1; all other local shifts have nullity zero.

Hence the full local distributions are

\[
\begin{array}{c|ccc}
&\nu=0&\nu=1&\nu=269\\\hline
\mathbb F_{271}&268&2&1\\
\mathbb F_{293}&290&2&1.
\end{array}
\]

The standard shifts `1,...,266` (and also 267) avoid all exceptional
residues in both fields.  Therefore `nu_271(a)=nu_293(a)=0` throughout the
entire standard scan.  Multiplication by every `H_a` is invertible in both
local algebras, so unequal-degree subresultants cannot extract a factor.

For context only, a uniform shift modulo `N` has unequal local ranks on
exactly

\[
79403-(268\cdot290+2\cdot2+1\cdot1)=1678
\]

CRT pairs.  These exceptional local residues are precisely the shifted-gcd
hits `a=0,-1,-2`; this finite probability is not an asymptotic lower- or
upper-bound theorem.

## Complexity and zero-divisor scope

The proposed rank computation itself is implementable without field
division: compute `H_a` by binary powering in the cyclic quotient, form its
`r`-dimensional multiplication matrix (or the polynomial subresultants),
and use division-free determinant/subresultant algorithms.  For the standard
AKS polynomial bounds on `r` and the number of shifts, this has polynomial
bit cost.  Over `Z/NZ`, a Euclidean gcd is not justified because of zero
divisors; the local argument above is only a counterexample certificate.
On this input both local ranks are full, so the division-free rank pattern
contains no separator.

## Computation certificates

- `R03_full_1_2943.json` separately confirms the same zero/zero pattern
  on the prior 55-bit hard input through every standard shift and the
  adjacent ceiling shift.
- `R04_small_search_1000.json` found `79403` after three smaller hard-regime
  candidates with actual mismatches.
- `R05_verify_79403.json` directly verifies the small certificate and the
  factor-degree patterns.
- `R07_all_local_residues_79403.json` exhausts both full local fields and
  gives the exact distributions above.

All run provenance and the failed/superseded attempts R01 and R06 are in
`RUN_MANIFEST.md`.
