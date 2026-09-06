# F228 candidate — quotient labels expose carry defects, not new common-primary capacity

## Status and novelty boundary

This is a self-audited theorem candidate with three preregistered finite
searches.  It is not a factoring algorithm.

F226 proved that the random remainder-child vector is independent of `N` and
deliberately excluded the multiplier labels and Euclidean quotients.  F228
retains those labels.  The quotient bank is genuinely `N`-dependent and is
recursion-safe under numerical-QP multiplier and shift bounds.  Its exact
common-primary contribution, however, collapses to a public carry defect.
The remaining APR-compatible support obeys an inverse-lift law but has no
proved all-input lower bound.

Throughout,

\[
n=\lceil\log_2(N+1)\rceil,
\qquad B=2^{\lfloor n/2\rfloor},
\]

`N>=3` is odd, `u` is positive and odd, and

\[
uN=Q_uB+R_u,
\qquad 0<R_u<B.
\tag{1}
\]

For an integer shift `c`, put `A_{u,c}=Q_u+c` whenever this integer is
positive.

## Theorem A — recursion-safe quotient children and exact carry words

Let `U(n)` and `C(n)` be fixed numerical-QP bounds.  All children
`A_{u,c}` with

\[
1\le u\le U(n),\qquad |c|\le C(n)
\]

have

\[
\operatorname{bits}(A_{u,c})
\le {n\over2}+(\log n)^{O(1)}.
\tag{2}
\]

The same bound holds for every auxiliary `ell-1` after factoring a child.
Numerical-QP many such calls therefore fit a fixed-ratio recursive factoring
tree of total numerical-QP size, conditional on a correct dispatcher for all
reachable smaller integers.

Writing

\[
N=KB+S,qquad 0<S<B,
\tag{3}
\]

gives the exact carry identities

\[
Q_u=uK+\left\lfloor{uS\over B}\right\rfloor,
\qquad
R_u=uS\bmod B.
\tag{4}
\]

In particular, if `uS<B`, then `Q_u=uK` and `R_u=uS`.  Thus, unlike the
F226 remainder ensemble, quotient banks need not refresh: a whole bounded
multiplier range can collapse to multiples of one public half-size integer.

## Theorem B — direct gcds and common-primary support collapse

For every shift with `A_{u,c}>0`,

\[
\boxed{
\gcd(A_{u,c},N)=\gcd(R_u-cB,N).
}
\tag{5}
\]

Thus a direct factor found by a shifted quotient is already found by its
public half-size carry defect.

More generally, for every odd divisor `d|N-1`,

\[
\boxed{
\gcd(A_{u,c},d)=\gcd(u-R_u+cB,d).
}
\tag{6}
\]

Let

\[
D_N=\gcd_{r\mid N,\ r\ {m prime}}(r-1)
\tag{7}
\]

and let `D_N^odd` be its odd part.  Since `D_N|N-1`, equation (6) gives

\[
\boxed{
\gcd(A_{u,c},D_N^{\rm odd})
=\gcd(u-R_u+cB,D_N^{\rm odd}).
}
\tag{8}
\]

Consequently every odd primary block that a global-return certificate from
the factored exponent `A_{u,c}` could certify as common to all rational
components already divides the public half-size defect `u-R_u+cB`.
Factoring the quotient can still provide a different annihilator/return
event.  Equation (8) concerns support capacity, not the probability of that
return and not the validity of a certificate without a witness.

## Theorem C — inverse-lift characterization of APR-compatible support

Now assume

\[
N=pq,qquad p<q<2p,
\tag{9}
\]

with distinct odd primes.  Put `a=R_u-cB`.  Let `ell` be an odd prime
dividing `A_{u,c}` after the direct gcd screen, and suppose `ell` does not
divide `u`.  Then

\[
\boxed{
N\equiv a u^{-1}\pmod\ell.
}
\tag{10}
\]

For every integer `i>=0`,

\[
\boxed{
p\equiv N^i\pmod\ell
\iff
u^ip\equiv a^i\pmod\ell.
}
\tag{11}
\]

For the other factor, equation (11) is equivalently

\[
uq\equiv a\pmod\ell\quad(i=0),
\tag{12}
\]

or

\[
qa^{i-1}\equiv u^{i-1}\pmod\ell\quad(i\ge1).
\tag{13}
\]

Hence the compatible primes inside one quotient child are exactly prime
divisors of the explicit child that also divide the hidden inverse-lift
integer

\[
u^ip-a^i.
\tag{14}
\]

The primes dividing `u` are bounded by the public multiplier cap and can be
separated into a deterministic small-prime bank.  Equations (10)--(14) do
not certify compatibility.  They identify its exact integer source.

For a fixed exponent `i`, every compatible prime also divides the nonzero
integer `N^i-p`.  Therefore the total squarefree compatible support has
binary logarithm less than

\[
n\max(1,i).
\tag{15}
\]

There is no all-input lower bound in (14) or (15).

## Theorem D — uniform random shifts reduce to harmonic sampling

Fix `u`.  Draw a shift uniformly from any `W` consecutive integers.  For a
fixed prime `ell`,

\[
\Pr(\ell\mid Q_u+c)
\le {1\over\ell}+{1\over W}.
\tag{16}
\]

For `K` independent shifts, let `Z_i(Y)` be the binary logarithm of the
product of captured compatible primes greater than `Y` for exponent `i`.
Then

\[
\mathbb E Z_i(Y)
\le
Kn\max(1,i)\left({1\over Y}+{1\over W}\right).
\tag{17}
\]

Consequently, for `0<=i<T` and `Delta>0`,

\[
\Pr\bigl(\exists i<T:Z_i(Y)\ge\Delta\bigr)
\le
{KnT^2\over\Delta}
\left({1\over Y}+{1\over W}\right).
\tag{18}
\]

Numerical-QP choices of `Y` and `W` can make this tail smaller than any
specified inverse-QP target while every prime at most `Y` is deterministically
enumerable in numerical-QP time.  Thus uniform random shifts do not by
themselves turn the quotient into a useful-heavy source.  This theorem does
not cover an integer-biased multiplier, an adaptive heavy shift, or joint
processing of the complete carry word.

## Finite guidance

The frozen searches used balanced consecutive safe-prime pairs, for which
`gcd(p-1,q-1)=2`.  Hence odd common-primary capacity was absent by
construction.

- D01 used 512 rows at 37--38 input bits.  Under the fixed cap
  `omega(W_u)<=20`, every row had a positive numerator out of 128; the range
  was 17--72 and the total was 22,962.
- D02 used 32 rows at each safe-prime scale `k=22,26,30`.  Its cap-20 totals
  were 524, 92, and 15 out of 4,096, with 0, 4, and 19 capped zero rows.
- D03 removed the cap before measuring source availability.  The exact
  totals were 2,754, 1,514, and 788 out of 4,096, with no oracle-zero row.
  Every trial had at most 29, 31, and 34 distinct odd child primes at the
  three scales, so cap 40 reproduced the no-cap totals exactly.

Thus the D02 zero rows were cap artifacts, not arithmetic-source
counterexamples.  The positive no-cap data is useful guidance, but it does
not supply the missing uniform inverse-QP theorem.  D00 records an accidental
local prelaunch execution; the remote D01 output is the declared evidence.
