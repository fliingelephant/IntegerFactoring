# F53 — noninvertible joint-move obstruction collapses to the direct output gcd

## Status and scope

**Status:** killed framework candidate after hostile audit. The local
restriction lemma survives, but the advertised path obstruction was only the
direct output-gcd decoder in disguise. No computation is used.

**Family:** F23. This directly tests one reopen condition left by P45 and by
F52: a stochastic joint update of both free coordinates.

Let

\[
N=pq,
\qquad
R=\mathbb Z/N\mathbb Z,
\qquad
\Omega_N=\{(k,x)\in R^2:kx=0\},
\]

where \(p\ne q\) are primes. P45 treats low-degree polynomial bijections of
\(\Omega_N\). The present result removes bijectivity. Each realized move may
be noninvertible, may collapse an axis, and may be selected adaptively from
the full past. The only semantic promise is that the realized polynomial map
sends all of \(\Omega_N\) into \(\Omega_N\).

The local lemma does not cover a map that is valid only at the current point,
state-stitched branches whose individual branches do not preserve all of
\(\Omega_N\), characteristic-scale degree, rational or opaque moves, or
auxiliary hidden state. The separate terminal-output decoder has no such
representation restriction.

## 1. One realized joint move

Let

\[
T=(F,G):\Omega_N\longrightarrow\Omega_N
\tag{1.1}
\]

be induced by \(F,G\in R[K,X]\), each of total degree at most \(D\). Assume

\[
2D<\min(p,q).
\tag{1.2}
\]

Form the four public axis restrictions

\[
F_K(Z)=F(Z,0),\quad G_K(Z)=G(Z,0),\quad
F_X(Z)=F(0,Z),\quad G_X(Z)=G(0,Z).
\tag{1.3}
\]

Screen every coefficient \(c\) in these four polynomials by \(\gcd(c,N)\).
There is an exact dichotomy:

1. one coefficient gives a proper factor of \(N\); or
2. on each source axis, both CRT fields choose the same one of three forms:
   the first target axis, the second target axis, or collapse to the origin.

The second case is a statement about which restricted polynomial is formally
zero. The active one-variable polynomial need not be a permutation and can
have roots.

### Proof

Fix \(r\in\{p,q\}\), and reduce all polynomials modulo \(r\). Since (1.1)
maps the first source axis into the local zero-product set,

\[
F_{K,r}(t)G_{K,r}(t)=0
\qquad\text{for every }t\in\mathbb F_r.
\tag{1.4}
\]

To justify the local statement, complete any chosen local axis point by the
origin in the other CRT field and lift the pair to \(\Omega_N\). Its global
image has zero product, so its selected local component has zero product.

The product in (1.4) has degree at most \(2D<r\). It has \(r\) roots, so it
is the zero polynomial. Since \(\mathbb F_r[Z]\) is an integral domain,

\[
F_{K,r}=0\quad\text{or}\quad G_{K,r}=0.
\tag{1.5}
\]

The same proof gives

\[
F_{X,r}=0\quad\text{or}\quad G_{X,r}=0.
\tag{1.6}
\]

Suppose no coefficient screen is proper. For \(N=pq\), every screened
coefficient is then either zero modulo both primes or nonzero modulo both
primes. Therefore each polynomial in (1.3) is formally zero modulo \(p\) if
and only if it is formally zero modulo \(q\). Equations (1.5)--(1.6) now show
that the nonzero-output pattern on each source axis is synchronized across
the two fields. Both restricted outputs can be zero, which is the new
axis-collapse case absent from the bijective theorem. They cannot both be
nonzero. This proves the dichotomy. \(\square\)

## 2. The attempted path invariant is universal

Define the public-axis region

\[
\mathcal A_N=
(R^\times\times\{0\})
\mathbin{\dot\cup}
(\{0\}\times R^\times)
\mathbin{\dot\cup}
\{(0,0)\}.
\tag{2.1}
\]

Put

\[
B_N=\Omega_N\setminus\mathcal A_N.
\]

For every \((k,x)\in\Omega_N\),

\[
(k,x)\in B_N
\quad\Longleftrightarrow\quad
1<\gcd(k,N)<N\ \text{ or }\ 1<\gcd(x,N)<N.
\tag{2.2}
\]

Indeed, if neither coordinate gives a proper gcd, each coordinate is zero or
a unit. Two units cannot have zero product. Thus the pair lies in
\(\mathcal A_N\). The converse follows directly from (2.1).

Consequently, after both output coordinates are screened, every safe output
of **any** \(\Omega_N\)-valued move lies in \(\mathcal A_N\). No polynomial
map, degree bound, coefficient screen, input invariant, or Markov property is
used. The proposed path theorem therefore supplied no low-degree obstruction.

## 3. Universal factor-or-distance consequence

Let \(\pi_N\) be uniform on \(\Omega_N\).

CRT gives

\[
|\Omega_N|=(2p-1)(2q-1),
\qquad
|B_N|=2N-2,
\]

so

\[
\rho_N:=\pi_N(B_N)
=\frac{2N-2}{(2p-1)(2q-1)}
>\frac12.
\tag{3.1}
\]

If \(\mu_N\) is any law on \(\Omega_N\), screen only its terminal pair.
Equation (2.2) gives

\[
\boxed{
\Pr(\text{terminal gcd factors }N)=\mu_N(B_N)
\ge \rho_N-\|\mu_N-\pi_N\|_{\rm TV}.
}
\tag{3.2}
\]

This is the direct zero-product decoder. It applies to polynomial,
non-polynomial, adaptive, opaque, or direct samplers. It does not show that a
noninvertible move fails to construct such a sample.

## 4. Cost boundary

Let \(n=\lceil\log_2(N+1)\rceil\). Require one public polynomial \(P\) with

\[
D_N\le P(n)
\]

for all histories, random seeds, moves, and stopping times. Before running
the chain, scan integers \(2,\ldots,2D_N\) by gcd with \(N\). A hit is a
factor. If there is no hit, then \(2D_N<\min(p,q)\) on every distinct
semiprime input, as required in (1.2).

For a materialized division-free circuit, evaluate each gate after the two
substitutions

\[
(K,X)=(Z,0),\qquad(K,X)=(0,Z)
\]

in \(R[Z]/(Z^{D_N+1})\). Truncated convolution uses
\(O(D_N^2)\) ring operations per multiplication gate and recovers every
coefficient because the promised exact formal output degree is at most
\(D_N\).

Assume a circuit-based process has expected-polynomial bit and fair-bit cost
and expected-polynomial total circuit encoding length. Then the coefficient
monitor for the local lemma also has expected-polynomial cost.

For the universal terminal decoder, fresh independent runs give an
expected-polynomial splitter only when the success gap is uniformly
inverse-polynomial, for example

\[
\rho_N-\|\mu_N-\pi_N\|_{\rm TV}
\ge\frac1{\operatorname{poly}(n)}.
\tag{4.1}
\]

The pointwise condition \(\|\mu_N-\pi_N\|_{\rm TV}<1/2\) is not sufficient,
because its gap below \(1/2\) can be exponentially small. This statement does
not by itself handle prime powers, more than two prime factors, even powers,
recursion, or complete factorization.

The semantic map-into-\(\Omega_N\) promise and the exact formal-degree promise
must be proved by the proposed sampler. The monitor does not certify them.

## 5. Exact surviving open mechanism

Section 1 synchronizes only the **formal zero/nonzero restriction pattern**.
It does not synchronize evaluations at the two hidden primes. Noninvertibility
introduces roots, and one active polynomial can vanish modulo one prime but not
the other at the same public unit.

For example, let \(N=77=7\cdot11\) and

\[
T(K,X)=(K(K-1),0).
\]

This degree-two map sends all of \(R^2\) into \(\Omega_N\). Its coefficients
are \(0,1,-1\), so no coefficient gcd factors \(N\). But

\[
T(8,0)=(56,0),
\qquad
\gcd(56,77)=7.
\]

Thus a factor-asymmetric root can create the desired mixed output without a
factor-bearing coefficient. The output gcd detects success, but F53 gives no
probability bound or bare-\(N\) method for arranging such roots.

## Killed conclusion

The local low-degree classification is correct, but the claimed joint-move
barrier is not. Once output coordinates are screened, the factor-or-distance
statement is true for every zero-product sampler and says nothing about how
the sample was made. The real open question is whether a public
noninvertible process can manufacture factor-asymmetric root evaluations with
inverse-polynomial probability.
