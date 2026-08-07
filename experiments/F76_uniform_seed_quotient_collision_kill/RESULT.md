# F76 — uniform inverse seeds do not supply hard large-prime quotient collisions

**Status:** corrected proof-only candidate after a failed first hostile audit.
No research computation was run. This is a source obstruction for the F74
quotient-collision sieve. It does not cover adaptive correlated feedback.

## 1. Setup

Let

\[
n=\lceil\log_2(N+1)\rceil,
\qquad N\ge3.
\]

First run a deterministic polynomial-time primality test. If \(N\) is prime,
stop. Thus the remaining input is composite.

Fix integers \(m,R,B\ge1\), with \(B\ge\max(3,n)\). Trial-divide \(N\) by
all primes at most \(B\). If this gives a proper factor, stop. Otherwise every
prime divisor of the remaining composite \(N\) is greater than \(B\).

For \(1\le i\le m\), let \(U_i\) be uniform on
\((\mathbb Z/N\mathbb Z)^\times\), represented in \(1,\ldots,N-1\). Put

\[
V_i=\iota_N(U_i),
\qquad
A_i=U_iV_i=1+K_iN.
\]

The samples can be independent. The proof below only needs every \(U_i\) to
have the uniform marginal law.

For every target \(1\le r\le R\), put

\[
C_r=1+rN,
\qquad
P=\prod_{i=1}^mA_i,
\qquad
D_r=\gcd(P,C_r).
\]

The event of interest is that some \(D_r\) contains a prime greater than the
public trial-division bound \(B\).

## 2. Large common-prime bound

### Theorem 1

Let

\[
L=n+\lceil\log_2(R+1)\rceil+1.
\]

Then

\[
\boxed{
\Pr\!\left(
\exists r\le R,\ \exists\text{ prime }\ell>B:\ \ell\mid D_r
\right)
\le
\frac{2mRNL}{B\varphi(N)}.
}
\tag{1}
\]

After the declared trial division,

\[
\frac{N}{\varphi(N)}
\le
\exp\!\left(
\frac{n}{B\log_2(B+1)}
\right)
\le e.
\tag{2}
\]

Consequently,

\[
\boxed{
\Pr\!\left(
\exists r\le R,\ \exists\ell>B:\ \ell\mid D_r
\right)
\le
\frac{2e\,mRL}{B}.
}
\tag{3}
\]

### Proof

Fix \(i,r\), and fix a prime \(\ell\mid C_r\). Since \(C_r\equiv1\pmod
N\), one has \(\ell\nmid N\). If \(\ell\mid A_i=U_iV_i\), primality gives

\[
\ell\mid U_i
\quad\text{or}\quad
\ell\mid V_i.
\]

Among the \(\varphi(N)\) unit representatives in \(1,\ldots,N-1\), at most
\(N/\ell\) are divisible by \(\ell\). Inversion permutes the units, so \(V_i\)
has the same uniform law as \(U_i\). Therefore

\[
\Pr(\ell\mid A_i)
\le
\Pr(\ell\mid U_i)+\Pr(\ell\mid V_i)
\le
\frac{2N}{\ell\varphi(N)}.
\tag{4}
\]

The integer \(C_r\) has at most \(\log_2C_r\le L\) distinct prime divisors.
For every one greater than \(B\), \(1/\ell<1/B\). A union bound over its
large prime divisors gives

\[
\Pr\!\left(
\gcd(A_i,C_r)\text{ has a prime divisor greater than }B
\right)
\le
\frac{2NL}{B\varphi(N)}.
\]

If a prime divides \(D_r=\gcd(\prod_iA_i,C_r)\), it divides at least one
\(A_i\). A second union bound over all \(mR\) pairs proves (1). No
independence assumption was used.

It remains to bound \(N/\varphi(N)\). Let \(\omega(N)\) be the number of
distinct prime divisors of \(N\). Every such prime exceeds \(B\), so

\[
\omega(N)\log_2(B+1)\le\log_2N<n.
\]

Also, for every prime \(q>B\),

\[
-\log(1-1/q)\le\frac1{q-1}\le\frac1B.
\]

Hence

\[
\log\frac{N}{\varphi(N)}
=\sum_{q\mid N}-\log(1-1/q)
\le\frac{\omega(N)}B
\le\frac{n}{B\log_2(B+1)}.
\]

Because \(B\ge n\ge2\), the last exponent is at most one. This proves (2)
and (3). \(\square\)

## 3. Asymptotic consequence

Fix constants \(a,b,c\ge1\). If

\[
m\le n^a,
\qquad
R\le n^b,
\qquad
B=n^{a+b+c+3},
\]

then trial division through \(B\) is polynomial in \(n\), and Theorem 1 gives

\[
\Pr\!\left(
\exists r\le R,\ \exists\ell>B:\ \ell\mid D_r
\right)
=O(n^{-c-1}).
\tag{5}
\]

The precise extra power of \(n\) is not important. For every declared
polynomial seed count and target range, one can choose a larger polynomial
trial bound so that a large shared prime occurs with arbitrarily small
inverse-polynomial probability.

On the complementary event, every \(D_r\) is \(B\)-smooth. Trial division
completely factors \(D_r\), and also the full \(B\)-smooth part of every
\(C_r\), in polynomial time. It can likewise remove these public small primes
from every retained endpoint block. Thus the quotient-collision sieve has
not manufactured a hard large common factor. It has supplied an explicit
smooth factor pool, followed by the still-open task of selecting a
factor-bearing product or relation.

## 4. Exact scope

This theorem does **not** prove that \(D_r\le r\), and it does not prove that
a smooth \(D_r\) is useless. A product of many small factors can exceed
\(r\), create a new presentation, or contain a direct separator. The theorem
only shows that the random seeds are not needed to discover those small prime
factors: polynomial trial division of the auxiliary values exposes them.

The theorem applies to fresh uniform inverse samples, even when the target
\(r\) is selected adaptively inside the declared numerical range
\(1,\ldots,R\). It does not apply when the seed states are chosen by an
adaptive canonical-residue or block-feedback process. Such states can be
strongly correlated with the current integer block structure and need not
have uniform marginals.

Therefore the live quotient-feedback route cannot rely on independent
uniform large-quotient seeds. It must obtain its hard overlaps from adaptive
correlation, or use a different progress mechanism. No factoring algorithm
is proved.

The failed first hostile audit is preserved at
`experiments/F76_uniform_seed_quotient_collision_kill_audit/RESULT.md`. It
accepted the probability argument and found one omitted prime-input stop in
the precondition of (2). The corrected version adds that stop and requires a
fresh hostile audit.
