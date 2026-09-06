# F222 V2 fresh hostile audit

## Verdict

**PASS.**

The frozen V2 theorem packet is mathematically sound in its stated scope. The
two local coefficient bounds, the local-nullity bound, the adaptive fresh-shift
union bound, and the Baker--Harman--Pintz infinite-family construction all
reconstruct independently.

This verdict does not extend to biased shifts, a modulus selected after seeing
the same shift, joint processing of nonzero coefficients, or any all-input
factoring lower bound. F222-D01 is finite consistency evidence only.

## 1. Authentication

I read V2_MANIFEST.md first and SHA-256 hashed every authoritative input
before reading it. Every supplied V2 hash matched exactly.

- V2_STATEMENT.md:
  586d2edd549a8c580aa9d66c9dd2cee7866ee4f0d74ed0956bc3f07772ad6cd9
- V2_PROOF.md:
  e098bb138dd033537436cdc64ed8a46e67b80ba4ae1e0c489c48a8d0c71ff4c1
- V2_SELF_AUDIT.md:
  f7a5b3a852c7e8843fa4727e925f3bdb628d8e3e417ff291d8650a0f2f0dbeb1
- V2_RESULT.md:
  5704609d26498ad842fbf82ef2f04f1faf001720b7c5a001d5fb38c479c5b032
- V2_PROVENANCE.md:
  cfcb1945ece5b0e72af261bcd4b6f15be27ba1d8294cf22578046e77eda17510

The independently recorded manifest hash is

c32f54bcfdf15f9e32b56dfd62dc4478a745559a8cab66c777e41ce2fda7bf8b.

The preserved V1 hashes stated in V2_PROVENANCE.md also match, but V1 was
not used as authority:

- STATEMENT.md:
  e3d860bfb2558a365aa6389fb59460060c11566a6349ff4dc6a613ac4b4c143b
- PROOF.md:
  33780d9494fbadc933ae1a05aa2c779dfeadb0c1e668752e7116aba510b51171
- SELF_AUDIT.md:
  775907003bb1b0ffc97f7d5a95767deb4cf7c6ea02bb82e98e2317b7bcccb0bb
- RESULT.md:
  610d783a7157ef5672ddf20b38666732a32ec0e1966c14e3a4a267c75ca76564

## 2. Local Frobenius identities

Put

\[
h_{m,a}(X)=(X+a)^m-X^m-a^m.
\]

In characteristic \(p\) and \(q\), respectively,

\[
E_a=h_{q,a}(X)^p,
\qquad
E_a=h_{p,a}(X)^q.
\]

These follow by applying the relevant Frobenius map to all three terms.
Because \(\gcd(r,pq)=1\), multiplication of cyclic indices by \(p\) or \(q\)
permutes the \(r\) positions. Thus coefficient zeros are exactly permuted.
For nullity, taking a Frobenius power also preserves the set of common roots
with \(X^r-1\).

## 3. The \(p\)-local coefficient calculation

In characteristic \(p\), \(q=p+d\) gives

\[
h_{q,a}
=X^p\bigl((X+a)^d-X^d\bigr)
 +a\bigl((X+a)^d-a^d\bigr).
\]

Sorting by the power \(a^e\) gives, with every endpoint included,

\[
h_{q,a}(X)=
\sum_{e=1}^{d}a^e
\left(
\binom de X^{q-e}
+\binom d{e-1}X^{d-e+1}
\right).
\]

The two \(X\)-indices paired at a fixed \(e\) differ by

\[
(q-e)-(d-e+1)=p-1.
\]

All displayed binomial coefficients are nonzero modulo \(p\), since their
factorials have arguments below \(p\).

If \(p\not\equiv1\pmod r\), the two terms of a fixed \(a\)-degree enter
different cyclic buckets. Terms from different \(e\) have different
\(a\)-degrees and cannot cancel. The \(d\) consecutive indices in the first
family meet every bucket because \(d>r\).

If \(p\equiv1\pmod r\), the paired terms enter the same bucket and combine as

\[
\binom de+\binom d{e-1}=\binom{d+1}e.
\]

This is nonzero modulo \(p\) because \(d+1<p\). The same \(d>r\) coverage
argument applies. Hence every \(p\)-local cyclic coefficient is a nonzero
polynomial of degree at most \(d\). Root counting and a union over the \(r\)
buckets prove

\[
\Pr(\text{some \(p\)-local coefficient is zero})
\leq \frac{rd}{p-1}.
\]

## 4. The \(q\)-local coefficient clearing

Before cyclic reduction,

\[
h_{p,a}(X)=\sum_{j=1}^{p-1}\binom pj a^{p-j}X^j.
\]

No coefficient vanishes modulo \(q\): every prime divisor of
\(\binom pj\) is at most \(p<q\). Within a cyclic bucket the powers \(a^{p-j}\)
are distinct. Also \(1\leq j\leq p-1\) meets every bucket because
\(p-1>d>r\). Thus every direct cyclic coefficient \(v_k(a)\) is nonzero and
has degree at most \(p-1\).

For a unit \(a\in\mathbb F_q^\times\), multiplication by
\(a^{d-1}(X+a)^d\), with \(p=q-d\), gives

\[
a^{d-1}(X+a)^d h_{p,a}=K_a,
\]

where

\[
K_a=a^{d-1}(X^q+a)
-a^{d-1}X^p(X+a)^d
-(X+a)^d.
\]

The last term is exact because \(a^{d-1}a^p=a^{q-1}=1\). After the two
endpoint cancellations,

\[
K_a=
-\sum_{j=0}^{d-1}\binom dj X^{p+j}a^{2d-1-j}
-\sum_{j=1}^{d}\binom dj X^j a^{d-j}.
\]

This also makes the degree bound \(2d-1\) explicit.

Define

\[
J_a=X^{r-1}-aX^{r-2}+\cdots+(-a)^{r-1},
\qquad
D(a)=1-(-a)^r.
\]

Direct multiplication gives

\[
(X+a)J_a=X^r-(-a)^r=D(a)
\]

in \(\mathbb F_q[X]/(X^r-1)\). Therefore

\[
a^{d-1}D(a)^d h_{p,a}=K_aJ_a^d.
\]

Each cyclic coefficient \(W_k(a)\) on the right has degree at most

\[
(2d-1)+d(r-1)=d(r+1)-1.
\]

Every \(W_k\) is nonzero. If \(W_k\) were the zero polynomial, then for every
unit \(a\) with \(D(a)\ne0\), the corresponding nonzero polynomial \(v_k\)
would vanish. Since \(D\) has at most \(r\) roots, \(v_k\) would have at least

\[
q-1-r>q-d-1=p-1
\]

roots. This contradicts \(\deg v_k\leq p-1\). The strict inequality is
exactly the premise \(d>r\).

The exceptional roots of \(D\) are common to all buckets. Counting that set
once, followed by the roots of all \(r\) nonzero \(W_k\), gives

\[
r+r\bigl(d(r+1)-1\bigr)=rd(r+1).
\]

This proves the \(q\)-side coefficient bound. Counting the exceptional set
once per coefficient would be incorrect; V2 does not do that.

## 5. Proper coefficient gcds

CRT sends a uniform unit modulo \(N\) to independent uniform elements of
\(\mathbb F_p^\times\times\mathbb F_q^\times\). If a global coefficient has
\(1<\gcd(e_k,N)<N\), then it is zero in at least one local field. The converse
need not hold: a coefficient zero in both fields has gcd \(N\). Thus the proper
gcd event is contained in, rather than equal to, the local-zero union. Adding
the two local bounds proves (S4).

## 6. The weakened local-nullity premise

Let \(\xi\) be an \(r\)th root in an algebraic closure of \(\mathbb F_p\).
The coefficients of \(a^d\) and \(a\) in \(h_{q,a}(\xi)\) are

\[
\xi(\xi^{p-1}+d),
\qquad
\xi^d(d\xi^{p-1}+1).
\]

If the polynomial were identically zero, these two coefficients would force
\(d^2=1\pmod p\). Since \(p,q\) are odd, \(d\) is even. The premise gives
\(2\leq d\leq p-2\), so \(d\) is neither \(1\) nor \(-1\) modulo \(p\).
Therefore each of the \(r\) roots accepts at most \(d\) shifts.

For completeness, the abbreviated \(q\)-local step in V2_PROOF.md
reconstructs without using V1. Substitute an \(r\)th root
\(\xi\ne0\) into the displayed expansion of \(K_a\):

\[
K_\xi(a)=
-\sum_{j=0}^{d-1}\binom dj \xi^{p+j}a^{2d-1-j}
-\sum_{j=1}^{d}\binom dj \xi^j a^{d-j}.
\]

The first sum occupies \(a\)-degrees \(d,\ldots,2d-1\); the second occupies
degrees \(0,\ldots,d-1\). Every coefficient is nonzero. In particular,
\(K_\xi\) is a nonzero polynomial of exact degree \(2d-1\). If
\(h_{p,a}(\xi)=0\), then \(K_\xi(a)=0\), including at \(a=-\xi\); no division
or exceptional-shift assumption is needed for this implication. Hence each
\(\xi\) accepts at most \(2d-1<2d\) unit shifts.

Since \(\gcd(r,pq)=1\), \(X^r-1\) has \(r\) distinct local roots. The two
root unions give

\[
\Pr(\nu_p>0\text{ or }\nu_q>0)
\leq \frac{rd}{p-1}+\frac{2rd}{q-1}.
\]

A local resultant vanishes exactly when the two local polynomials share a
root. Therefore a proper gcd of the integer resultant with \(N\) is contained
in this nullity union. Adding it to (S4) gives (S6).

## 7. Primary Baker--Harman--Pintz theorem

I inspected Theorem 1 in the primary paper: R. C. Baker, G. Harman, and
J. Pintz, *The Difference Between Consecutive Primes, II*, Proceedings of
the London Mathematical Society 83 (2001), 532--562,
[DOI 10.1112/plms/83.3.532](https://doi.org/10.1112/plms/83.3.532).
It states that for all sufficiently large \(x\), the interval
\([x-x^{0.525},x]\) contains a prime.

For each unbounded prime \(p\), put

\[
x_p=p+\lfloor p^{3/5}\rfloor.
\]

Because \(3/5>0.525\), the lower endpoint is strictly greater than \(p\) for
all sufficiently large \(p\). A prime \(q\) in the guaranteed interval then
satisfies

\[
p^{3/5}-O(p^{0.525})\leq q-p\leq p^{3/5}.
\]

Thus \(d=q-p=\Theta(p^{3/5})\). Also \(p<q<2p\) and \(d<p-1\) eventually.
As \(p\) runs through unbounded primes, this produces an infinite family, not
merely a finite list of examples.

## 8. Adaptive bank and exponential conversion

Let \(\mathcal F_{i-1}\) be the transcript before trial \(i\). The modulus
\(r_i\) is \(\mathcal F_{i-1}\)-measurable, while the new unit shift is
conditionally uniform. Therefore

\[
\Pr(U_i\mid\mathcal F_{i-1})
\leq d\left(
\frac{2r_i}{p-1}+\frac{r_i(r_i+3)}{q-1}
\right).
\]

No independence between trials is needed. The precise adaptive union bound
is

\[
\Pr\left(\bigcup_i U_i\right)
\leq
\mathbb E\!\left[
d\sum_i\left(
\frac{2r_i}{p-1}+\frac{r_i(r_i+3)}{q-1}
\right)
\right],
\]

or the same expression with a deterministic numerical-QP envelope for the
random sum. This is the rigorous interpretation of (S9).

For \(n=\lceil\log_2 N\rceil\) on the balanced family,

\[
p=2^{n/2+O(1)},
\qquad
\frac d p=p^{-2/5+o(1)}=2^{-n/5+o(n)}.
\]

A fixed numerical-QP trial bound and fixed numerical-QP modulus envelope
make the sum outside \(d\) equal to \(2^{o(n)}\). Such moduli are also
eventually below \(d=2^{3n/10+o(n)}\). Hence the total probability is

\[
2^{-n/5+o(n)}\,2^{o(n)}=2^{-\Omega(n)}.
\]

This conditioning fails if \(r_i\) is selected from the same shift \(a_i\),
and the root counts do not apply to a biased shift law. V2 excludes both
extensions explicitly.

## 9. Finite D01 evidence is nonauthoritative

The D01 run manifest and every hash it supplies also authenticate:

- RUN_MANIFEST_D01.md:
  6a5a042b1b97a96b7706e3c3f29839038d994f07acd2021604f1419dce1e71bf
- PREREGISTRATION_D01.md:
  5af81584198083adbf59cec31b072e438e9671bc93ff8cfe8e2314147c28a569
- scripts/F222_D01_coefficient_search.py:
  d2cc2ce1a39228eecc3d407d40368b536ff8067389eb6974998b9b56e616a31d
- scripts/run_F222_D01_remote.sh:
  9a13859e837994157a46cb801c5f8a79d820e8b2273326099584d021b54a6c51
- output/F222-D01.json:
  cebb7a614c1af895bb820e5e4bfadfae6afd16aa8502ab1829220ff0a275ec32
- logs/F222-D01.log:
  526081803458be4f8fd518ad1b0338d7e287120ca8848c138803b1380faf99c6

An independent filter of the frozen JSON finds exactly 143 rows satisfying
\(r<d<p-1\), with zero violations of (S4). This is consistent with the
theorem. It is not used in any algebraic, probabilistic, or asymptotic step
above and cannot establish the infinite-family claim.

## 10. Nonfatal exposition note

Section 5 of V2_PROOF.md cites the old F222 \(q\)-local nullity argument
instead of displaying it. The expansion in Section 6 of this audit derives
the needed nonzero degree-\((2d-1)\) polynomial directly from the authenticated
V2 formulas. This is an exposition omission, not a mathematical dependency on
the nonauthoritative V1 packet.
