# F151 V3 candidate — a self-contained large-order and Jacobi-torus boundary

## Status and V3 repair

This is a proof-only candidate. It is not a factoring algorithm.

V2 passed its hostile re-audit. Its statement-only reconstruction verified
the mathematical core but found three missing interfaces. V3 only repairs
those interfaces. It defines the canonical inverse, defines the exact-value
decoder and factor-free refinement, and states the two cited results as
explicit external premises. It does not strengthen a V2 claim.

V1, V2, and their reviews remain frozen. V3 has not passed a fresh hostile
audit or a fresh statement-only reconstruction.

## Parameters and notation

Let \(N\ge3\) be an integer and write

\[
n=\lceil\log_2(N+1)\rceil.
\]

Let \(B\) be an integer with

\[
4\le B<N-1,
\qquad
B=2^{(\log n)^{O(1)}}.
\tag{1}
\]

For an integer \(a\), let \([a]_N\) be the unique integer in
\(\{0,1,\ldots,N-1\}\) congruent to \(a\) modulo \(N\). If
\(c\in\{1,\ldots,N-1\}\) is a unit modulo \(N\), define

\[
\boxed{
\iota_N(c)=[c^{-1}]_N.
}
\tag{2}
\]

Thus \(\iota_N(c)\in\{1,\ldots,N-1\}\) and
\(c\iota_N(c)\equiv1\pmod N\).

For a unit \(u\) modulo \(m\), let \(\operatorname{ord}_m(u)\) be the
least positive integer \(t\) such that \(u^t\equiv1\pmod m\).

Quasipolynomial time means
\(2^{(\log n)^{O(1)}}\) bit operations.

## External premises used in this candidate

The following two results are cited premises. V3 does not prove them.

### HH premise

Harvey and Hittmeir, *Deterministic methods for finding elements of large
multiplicative order*, arXiv:2601.11131v2, Theorem 1.1, state the following.
For integers \(N\ge3\) and \(1\le B<N-1\), a deterministic algorithm returns
either a proper divisor of \(N\), or a unit
\(\alpha\in(\mathbb Z/N\mathbb Z)^\times\) with

\[
\operatorname{ord}_N(\alpha)>B.
\tag{HH}
\]

Its stated bit cost is

\[
O\!\left(
\frac{B^{1/2}\log B}{(\log\log B)^{1/2}}\log N
\right),
\tag{3}
\]

with the cited theorem's harmless small-parameter convention.

### Pilatte premise

Pilatte, *Unconditional correctness of recent quantum algorithms for
factoring and computing discrete logarithms*, arXiv:2404.16450v2,
Corollaries 1.4--1.5 and Theorem 3.18, gives the following consequence used
here. Put

\[
d=\lceil\sqrt{\log N}\rceil,
\qquad
X=d^{1000d}.
\tag{4}
\]

For the stated \(d\) independent random small-prime generators from the
eligible set bounded by \(X\), the full relation lattice has, with high
probability, a basis whose vectors have Euclidean norm

\[
\exp(O(d)).
\tag{P}
\]

V3 uses only this dimension, probability, and norm conclusion. It does not
assume a classical algorithm that finds the basis.

## Exact-value decoder and factor-free refinement

This section defines all decoder language used below.

The decoder input is an ordered finite list of positive integers

\[
P_1,\ldots,P_s,
\qquad
P_i\equiv1\pmod N.
\tag{5}
\]

It applies these steps.

1. Discard every \(P_i=1\). For each other exact integer value, retain only
   its first occurrence. Call the resulting list \(A_1,\ldots,A_m\).
2. By repeated integer gcd splitting, exact division, and exact
   perfect-power extraction, compute pairwise-coprime integers
   \(g_1,\ldots,g_t>1\), none a perfect power, and nonnegative integer
   coordinates \(E_{ji}\) such that

   \[
   A_i=\prod_{j=1}^t g_j^{E_{ji}}.
   \tag{6}
   \]

   This is the **factor-free refinement**. It does not use rational-prime
   factorization.
3. Form the binary parity matrix

   \[
   M=(E_{ji}\bmod2)_{j,i}.
   \tag{7}
   \]

   A nonzero vector \(z\in\ker_{\mathbb F_2}M\) is an **exact-value
   closure**. For such \(z\), compute

   \[
   Q_z=\prod_{i:z_i=1}A_i,
   \qquad
   R_z=\sqrt{Q_z}>0.
   \tag{8}
   \]

4. Compute a complete binary basis of \(\ker M\). For every basis vector,
   test

   \[
   \gcd(R_z-1,N),
   \qquad
   \gcd(R_z+1,N).
   \tag{9}
   \]

The decoder reports progress only when a test in (9) is a proper divisor of
\(N\). It uses the endpoints only to form the exact values \(P_i\). Equal
exact values from different endpoint presentations are therefore handled by
the first-occurrence rule.

Pairwise coprimality and the non-perfect-power condition make (7) exact:

\[
Mz=0
\quad\Longleftrightarrow\quad
Q_z\text{ is an integer square}.
\tag{10}
\]

Also, \(R_z^2\equiv1\pmod N\). The induced root map is a homomorphism.
Therefore testing one complete kernel basis detects a non-global square root
whenever any closure has one. Here non-global means not congruent to \(1\)
or \(-1\) modulo \(N\). These decoder facts are proved in `V3_PROOF.md`.

## Theorem 1 — factor or large order in every prime component

There is a deterministic quasipolynomial procedure that returns a proper
factor of \(N\), or a unit \(\alpha\) such that

\[
\boxed{
\operatorname{ord}_r(\alpha)>B
\quad\text{for every rational prime }r\mid N.
}
\tag{11}
\]

The procedure invokes the HH premise with target \(B\). If that call does
not factor \(N\), it returns a unit with
\(\operatorname{ord}_N(\alpha)>B\). The procedure then tests

\[
\gcd(\alpha^e-1,N),
\qquad
1\le e\le B.
\tag{12}
\]

If no proper gcd occurs, (11) holds. The extra scan is quasipolynomial.

This is stronger than a certified large global order. It rules out a short
order in every hidden prime component. It does not establish or exclude
factor correlation outside the explicit scan (12).

## Theorem 2 — the short power bank has no listed local collision

Assume the no-factor branch of Theorem 1. For

\[
1\le e\le\lfloor B/4\rfloor,
\qquad
c_e=[\alpha^e]_N,
\qquad
w_e=\iota_N(c_e),
\tag{13}
\]

all of the following gcds are one for distinct eligible \(e,f\):

\[
\gcd(c_e-c_f,N),
\quad
\gcd(c_e+c_f,N),
\quad
\gcd(c_ec_f-1,N),
\quad
\gcd(c_ec_f+1,N),
\tag{14}
\]

and

\[
\boxed{
\gcd(c_e-w_e,N)=
\gcd(c_e+w_e,N)=1.
}
\tag{15}
\]

Thus the power positions are distinct and noninverse in every hidden prime
component. Every listed inverse-pair sign screen is null.

The associated exact values are

\[
P_e=c_ew_e=1+\kappa_eN.
\tag{16}
\]

Here \(\kappa_e\) is a positive integer.

Feed the ordered list \((P_e)\) to the exact-value decoder defined in
(5)--(9). The conclusions (14)--(15) do not determine that decoder. The
integers \(P_e\) can share ordinary integer factors or repeat. The refined
matrix can also have a multi-column closure whose root screen factors \(N\).

These residual events occur on certified windows. For example:

- For \(N=143=11\cdot13\), \(B=8\), and \(\alpha=2\), the two local orders
  are \(10\) and \(12\), while \(P_1=P_2=144\) through endpoint pairs
  \((2,72)\) and \((4,36)\).
- For \(N=391=17\cdot23\), \(B=12\), and \(\alpha=37\), the two local
  orders are \(16\) and \(22\). The first two distinct exact values satisfy

  \[
  P_1=37\cdot74=2738,
  \qquad
  P_2=196\cdot2=392,
  \]

  \[
  P_1P_2=1036^2,
  \qquad
  \gcd(1036-1,N)=23,
  \qquad
  \gcd(1036+1,N)=17.
  \tag{17}
  \]

The examples are capability witnesses only. The theorem does not assert a
closure, a useful root, or a factor on every input. It does not exclude
larger exponents, component-order finding beyond \(B\), or another decoder.

## Theorem 3 — Pilatte's norm premise does not give a QP full-ball catalogue

The dimension in the Pilatte premise satisfies

\[
d=\lceil\sqrt{\log N}\rceil=\Theta(\sqrt n).
\tag{18}
\]

Each promised basis vector has a polynomial-size coordinate description.
The norm premise gives no polylogarithmic-support conclusion. A vector under
the norm bound may use all \(d\) coordinates.

For a fixed positive \(C\), a brute-force catalogue of every integer vector
in the Euclidean ball of radius \(R=\exp(Cd)\) has

\[
\exp(\Theta(d^2))=\exp(\Theta(n))
\tag{19}
\]

members. This is not quasipolynomially many.

Therefore the Pilatte premise gives short relations with high probability,
but does not put a promised basis vector in a polylogarithmic-support
catalogue and does not give a quasipolynomial exhaustive search of the full
norm ball. This is not a lower bound. A structured classical sampler could
still find the relations without enumerating the ball.

## Theorem 4 — the direct large-order/Jacobi-torus splice loses the asymmetry

Now restrict to

\[
N=pq
\]

with distinct odd primes. Let \(\Delta\) be a unit with

\[
\left(\frac{\Delta}{N}\right)=-1,
\tag{20}
\]

Call the component modulo \(r\) split when
\(\left(\frac{\Delta}{r}\right)=1\), and nonsplit when it is \(-1\).

and let \(\alpha\) satisfy (11). Put

\[
x=\frac{\alpha+\alpha^{-1}}2\pmod N,
\qquad
b=\Delta^{-1}(x^2-1)\pmod N.
\tag{21}
\]

For each \(r\in\{p,q\}\),

\[
\boxed{
\left(\frac b r\right)
=
\left(\frac\Delta r\right).
}
\tag{22}
\]

Consequently the norm-one equation

\[
x^2-\Delta y^2=1
\tag{23}
\]

has a local \(y\) exactly in the split hidden component. It has no global
solution \(y\) modulo \(N\). The standard map that would place \(\alpha\)
in the split torus needs a local square root of \(\Delta\). It cannot form
one global torus point with this fixed \(x\).

Define the first-kind Chebyshev polynomials by

\[
T_0(X)=1,
\qquad
T_1(X)=X,
\qquad
T_{m+1}(X)=2XT_m(X)-T_{m-1}(X).
\tag{24}
\]

For every integer \(m\ge0\),

\[
T_m(x)=\frac{\alpha^m+\alpha^{-m}}2.
\tag{25}
\]

Equation (25) is independent of \(\Delta\). Thus the direct
fixed-\(x\) Kummer orbit discards the forced split/nonsplit orientation.

This closes only the direct splice of the scalar large-order element into
this fixed Kummer coordinate. It does not close other torus points,
coordinate-specific multi-relation decoders, or a new win--win theorem
inside a torus.

## Exact consequence and exclusions

The two external premises and the elementary deductions give these facts.

1. A deterministic QP source can be made collision-free for the exact
   short-window screens (14)--(15).
2. A short relation basis exists with high probability in a larger
   \(\sqrt n\)-dimensional region, but full-ball enumeration is exponential.
3. The direct scalar-to-fixed-Kummer splice loses the explicit Jacobi
   orientation.

These facts do not supply a factor-correlated sampler. They do not exclude
exact-value closures such as (17), integer carries, larger exponents,
component-order mismatches after \(B\), structured classical relation
sampling, or other torus coordinates. They do not constitute a factoring
algorithm.
