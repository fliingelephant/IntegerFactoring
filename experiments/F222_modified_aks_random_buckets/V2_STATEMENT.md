# F222 V2 candidate: uniform modified-AKS coefficients are rare on an intermediate-gap family

## Status and scope

This is a proof-only V2 candidate.  It preserves the original F222 files and
adds a stronger, integer-specific obstruction for

\[
E_a(X)=(X+a)^N-X^N-a^N\pmod{X^r-1,N}.
\]

It covers a fresh uniform unit shift, an adaptively chosen numerical-QP
modulus fixed before that shift, every raw coefficient gcd, and the local
nullity/resultant event.  It is not a lower bound against biased shifts,
joint processing of nonzero coefficients, or an `r` chosen after seeing the
same shift.

## Setup

Let

\[
N=pq,\qquad p<q<2p,\qquad d=q-p,
\]

where `p,q` are distinct odd primes.  Let `r>=2`, `gcd(r,N)=1`, and

\[
R_\ell=\mathbb F_\ell[X]/(X^r-1)
\qquad(\ell\in\{p,q\}).
\]

Write `e_(ell,k)(a)` for the coefficient at `X^k` of `E_a` in `R_ell`.
Assume

\[
\boxed{r<d<p-1.}
\tag{S1}
\]

## Theorem A: exact-degree coefficient bound

For every cyclic position `k`, the function

\[
a\longmapsto e_{p,k}(a)
\]

is a nonzero polynomial on `F_p` of degree at most `d`.  Therefore

\[
\Pr_{a_p\in\mathbb F_p^\times}
\bigl(\text{some }e_{p,k}(a_p)=0\bigr)
\le {rd\over p-1}.
\tag{S2}
\]

For every cyclic position `k`, there is a nonzero polynomial `W_k` over
`F_q` of degree at most

\[
d(r+1)-1
\]

such that, outside at most `r` common exceptional shifts,

\[
e_{q,k}(a)=0\Longrightarrow W_k(a)=0.
\]

Consequently,

\[
\Pr_{a_q\in\mathbb F_q^\times}
\bigl(\text{some }e_{q,k}(a_q)=0\bigr)
\le {rd(r+1)\over q-1}.
\tag{S3}
\]

For a uniform unit `a mod N`, CRT makes the two local shifts independent.
If any coefficient has a proper gcd with `N`, at least one local coefficient
is zero.  Hence

\[
\boxed{
\Pr\bigl(\exists k:1<\gcd(e_k(a),N)<N\bigr)
\le {rd\over p-1}+{rd(r+1)\over q-1}.}
\tag{S4}
\]

This bounds the complete coefficient scan, not one preselected coefficient.

## Theorem B: the local-nullity bound needs only `d<p-1`

Let

\[
\nu_\ell(a,r)=\deg\gcd(E_a\bmod\ell,X^r-1).
\]

Then

\[
\boxed{
\Pr(\nu_p(a,r)>0\text{ or }\nu_q(a,r)>0)
\le {rd\over p-1}+{2rd\over q-1}.}
\tag{S5}
\]

The original F222 imposed `p>d^2+1` only to exclude `d^2=1 mod p`.
Under (S1), `d` is an even integer in `[2,p-2]`, which already excludes that
congruence.  Thus (S5) applies in the intermediate-gap regime.

A proper resultant gcd is contained in the event in (S5).  Combining every
raw coefficient gcd with the resultant/nullity channel gives the one-trial
bound

\[
\boxed{
\Pr(\text{either channel is useful})
\le
{2rd\over p-1}+{rd(r+3)\over q-1}.}
\tag{S6}
\]

## Corollary: an infinite exponential obstruction

There is an infinite family of balanced prime pairs satisfying

\[
\boxed{d=\Theta(p^{3/5}).}
\tag{S7}
\]

For that family, let an adaptive bank make a numerical-QP number of trials.
At trial `i`, it fixes a numerical-QP integer `r_i`, coprime to `N`, from the
previous public transcript and then draws a fresh conditionally uniform unit
shift `a_i`.  It may scan every coefficient and the full
resultant/local-nullity event.  Then

\[
\boxed{
\Pr(\text{some trial is useful})=2^{-\Omega(n)},}
\tag{S8}
\]

where `n` is the bit length of `N`.

More precisely, once every `r_i<d`, the conditional union bound is

\[
d\sum_i\left(
{2r_i\over p-1}+{r_i(r_i+3)\over q-1}
\right).
\tag{S9}
\]

For numerical-QP trial count and moduli, the sum outside `d` is
`2^{o(n)}`, while `d/p=p^{-2/5+o(1)}=2^{-\Omega(n)}`.

The family uses Baker--Harman--Pintz, Theorem 1: for every sufficiently large
`x`, `[x-x^0.525,x]` contains a prime.  Applying it at
`x=p+floor(p^(3/5))` for unbounded primes `p` gives (S7).

## Exact remaining scope

The proof uses all of the following integer-specific facts:

- `N=pq` gives the two Frobenius collapses;
- the actual gap `d=q-p` controls the polynomial degrees;
- `a^(q-1)=1` clears the negative exponent on the `q` side; and
- an unconditional short-interval prime theorem constructs the hostile
  balanced family.

It does not cover nonuniform or carry-correlated shifts, fixed shifts with
random evaluation points, joint statistics of typical nonzero coefficients,
multi-shift elimination, or implicit moduli larger than numerical QP.

