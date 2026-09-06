# F222 candidate: random modified-AKS buckets separate sparsity from annihilation

## Status and closest prior work

This is a self-audited proof-only boundary for

\[
E_a(X)=(X+a)^N-X^N-a^N
\pmod{X^r-1,N}.
\]

It is not a factoring algorithm. The closest prior results are P11, P14,
P18, and P24. Those results use the standard error with constant term
`-a`, the standard minimal AKS modulus, and fixed coefficient, nullity,
principal-subresultant, or joint-minor scans. F222 differs materially by
using the homogeneous constant `-a^N`, arbitrary nonstandard QP-size
moduli `r`, and a uniform random integer shift `a`. It gives an exact
probability law and an infinite-family bound.

## Setup

Let

\[
N=pq,\qquad p<q<2p,\qquad d=q-p,
\]

where \(p,q\) are distinct odd primes. Let \(r\ge2\) satisfy
\(\gcd(r,N)=1\). Put

\[
R_N=(\mathbb Z/N\mathbb Z)[X]/(X^r-1)
\]

and let \(\overline E_a\) be the canonical coefficient vector of \(E_a\)
in \(R_N\). For a prime \(\ell\mid N\), let

\[
\nu_\ell(a,r)
=\deg\gcd(E_a\bmod\ell,X^r-1)
\]

over \(\mathbb F_\ell[X]\). This is the nullity of multiplication by
\(E_a\) in the local quotient.

## Theorem A: Frobenius and homogeneity normal form

For

\[
h_{m,a}(X)=(X+a)^m-X^m-a^m,
\]

one has

\[
E_a\equiv h_{q,a}(X)^p\pmod p,
\qquad
E_a\equiv h_{p,a}(X)^q\pmod q.
\]

Since \(p,q\) are coprime to \(r\), the two Frobenius powers permute the
\(r\) coefficient positions and preserve local nullity. For a unit shift,

\[
\boxed{h_{m,a}(X)=a^m h_{m,1}(X/a).}
\]

Thus randomizing \(a\) does not create a new error polynomial. It replaces
the cyclotomic equation \(Y^r=1\) for \(h_{m,1}(Y)\) by
\(Y^r=a^{-r}\).

More precisely, let

\[
S_{\ell,m,r}
=\{y^r\in\mathbb F_\ell^\times:
 y\in\overline{\mathbb F}_\ell^\times,
 h_{m,1}(y)=0\}.
\]

If \(a\) is uniform in \(\mathbb F_\ell^\times\), then

\[
\boxed{
\Pr(\nu_\ell(a,r)>0)
=\frac{g_\ell}{\ell-1}
\left|S_{\ell,m,r}\cap(\mathbb F_\ell^\times)^r\right|,
\qquad
g_\ell=\gcd(r,\ell-1),}
\]

where \(m=N/\ell\).

For a uniform unit \(a\bmod N\), the two local shifts are independent. If
the displayed probabilities are \(\alpha_p,\alpha_q\), a resultant gcd is
proper with exact probability

\[
\boxed{\alpha_p(1-\alpha_q)+\alpha_q(1-\alpha_p),}
\]

and both local quotients are annihilated with exact probability
\(\alpha_p\alpha_q\).

## Theorem B: bounded gaps kill the random-annihilation law

Assume

\[
p>d^2+1.
\]

For a uniform unit shift modulo \(N\),

\[
\boxed{
\Pr\bigl(\nu_p(a,r)>0\text{ or }\nu_q(a,r)>0\bigr)
\le
\frac{rd}{p-1}+\frac{2rd}{q-1}.}
\]

Consequently the probability of either a proper resultant gcd or a common
annihilated quotient is bounded by the same expression.

P165 invokes a proved bounded-prime-gap theorem. By pigeonhole over the
finite set of even gaps, it supplies an infinite balanced family with one
fixed gap \(d=d_0\). On that family, any randomized bank with fresh uniform
unit shifts and

\[
\sum_i r_i=\operatorname{QP}(n)
\]

has total modified-AKS annihilation probability

\[
\boxed{2^{-\Omega(n)}.}
\]

The choice of each \(r_i\) may depend on the previous transcript, provided
the next shift is fresh and uniform after \(r_i\) is fixed. This closes the
uniform random-shift resultant/nullity route even for nonstandard QP moduli.
It does not cover a shift distribution biased by integer information or an
\(r\) chosen after seeing the same shift.

## Theorem C: coefficient buckets have a different exact dichotomy

For every unit or nonunit shift \(a\), the support of the coefficient vector
\(E_a\bmod p\) has size at most

\[
\boxed{2d.}
\]

Therefore, if \(r>2d\), scanning the \(r\) global coefficients gives
exactly one of the following outcomes:

1. some coefficient has a proper gcd with \(N\), which factors \(N\); or
2. the two local coefficient supports are identical and have size at most
   \(2d\).

Thus the coefficient route is not covered by Theorem B. It can be
deterministically strong on close-factor inputs. But the proved dichotomy
requires \(r>2d\). If \(r\) is numerical QP, then \(d\) is already
numerical QP, and ordinary Fermat factorization takes QP time because its
scan distance is

\[
O(d^2/\sqrt N)+O(1).
\]

On the live branch \(d\ge r/2\), the support bound becomes vacuous and no
inverse-QP coefficient-mismatch probability follows.

The sparse no-factor outcome is not an order certificate, a fully factored
annihilator, or a smaller recursive child. Turning it into one remains an
explicit missing step.

## Scope

F222 proves a scoped kill for uniform random local annihilation and a
sparse-or-factor theorem for raw coefficients. It leaves open:

- integer-biased or carry-biased shifts;
- nonuniform joint choices of \((a,r)\);
- adaptive minors or elimination transcripts using several shifts;
- the full column-matroid channel preserved by P24;
- large \(r\) represented implicitly;
- a decoder that turns the synchronized sparse outcome into a certified
  primary contribution;
- all-input factoring.
