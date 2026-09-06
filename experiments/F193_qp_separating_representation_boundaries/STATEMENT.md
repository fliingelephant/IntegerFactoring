# F193 candidate — narrow QP boundaries for separating representations

## Status and exact scope

This is a proof-only candidate. No mathematical computation is used.

It records four independent, narrow boundaries for Inspiration B5:

1. explicit sparse cusp-boundary constructions in modular symbols for
   squarefree level;
2. uniform small-modulus evaluation of P29's Eisenstein coefficient;
3. Dirichlet-twist banks of one fixed modular form at one index;
4. elliptic-torsion endomorphisms that descend from one globally defined
   endomorphism.

None of the four statements is a general obstruction to modular symbols,
cusp forms, modular forms, elliptic torsion, finite etale algebras, or
low-dimensional representations. In particular, this candidate does not
rule out a boundary-zero cuspidal quotient, a compressed dense modular-symbol
presentation, genuinely different eigenforms, a new coefficient evaluator,
local Frobenius, or a reduction-only endomorphism.

Throughout the first three sections, let

\[
N=pq
\]

for distinct odd primes, and put

\[
n=\left\lceil\log _2(N+1)\right\rceil.
\]

## 1. Explicit sparse modular-symbol cusp boundary

Write a rational cusp in reduced form as \(a/c\), with \(c=0\) allowed for
\(\infty\), and define

\[
d(a/c)=\gcd(c,N).
\tag{1.1}
\]

For squarefree \(N\), the \(\Gamma _0(N)\)-orbit of a cusp is determined by
\(d(a/c)\). Thus the four cusps for \(N=pq\) have types

\[
1,p,q,N.
\tag{1.2}
\]

Consider an explicitly represented sparse modular-symbol chain

\[
C=\sum_{i=1}^{L}u_i\{\alpha_i,\beta_i\},
\tag{1.3}
\]

where the list length and the bit lengths of every integer in every reduced
rational endpoint are numerical-QP in \(n\). Then one of the following
happens in numerical-QP time:

1. an endpoint denominator has gcd \(p\) or \(q\) with \(N\), and this gcd
   factors \(N\);
2. every endpoint has type \(1\) or \(N\), and

   \[
   \partial C\in
   \mathbb Z\bigl([c_N]-[c_1]\bigr).
   \tag{1.4}
   \]

Thus an explicit sparse chain cannot obtain factor-local **boundary support**
at the hidden cusps without an endpoint gcd already exposing a factor. This
does not restrict the integer coefficient multiplying the global line in
(1.4); that coefficient could itself contain metric information.

The standard public operators obey the same support boundary:

- every good-prime Hecke correspondence \(T_m\), with \(\gcd(m,N)=1\),
  preserves the type (1.1) on every branch;
- the Fricke involution \(W_N\) sends type \(d\) to type \(N/d\), so it only
  swaps the two global types \(1,N\);
- for an exact divisor \(Q\parallel N\), the standard Atkin--Lehner operator
  \(W_Q\) toggles the primes in \(Q\). If \(Q=p\) or \(q\), it reaches the
  factor-local cusps, but its exact-divisor label, and the determinant of a
  standard integral representative, is the factor \(Q\).

For a semiprime, the standard proper Atkin--Lehner labels are exactly \(p\)
and \(q\). Hence QP-many explicitly listed endpoints, good-prime Hecke
branches, and applications of \(W_N\) do not create a hidden-cusp support
direction. Introducing \(W_p\) or \(W_q\) explicitly already supplies a
factor.

## 2. Uniform small-modulus CRT amplification of P29

Let

\[
b_N=\sigma _1(N)=N+p+q+1
\tag{2.1}
\]

be P29's level-two Eisenstein coefficient on the distinct-odd-semiprime
promise.

Suppose one uniform classical algorithm takes \((N,\ell)\), where \(\ell\)
is any auxiliary prime of \(O(\log n)\) bits, and returns

\[
b_N\bmod\ell
\tag{2.2}
\]

in numerical-QP time in \(n+\log\ell\). It is enough to grant this algorithm
only for all primes up to \(C n\log(n+2)\), for one sufficiently large
absolute constant \(C\).

Then every promised \(N\) can be factored in deterministic numerical-QP
time. The same conclusion holds if the output is \(24b_N\bmod\ell\) for all
auxiliary primes \(\ell\ge5\) in that range.

The proof uses \(O(n)\) different \(O(\log n)\)-bit moduli, not one large
oracle modulus. Consequently, P29's open fixed-small-modulus interface is
pointwise only:

- one fixed modulus, or one fixed finite set of moduli, is not covered;
- one uniform evaluator over a growing QP-constructible bank whose product
  exceeds the coefficient bound is already a factoring interface.

## 3. A Dirichlet-twist bank has rank one at the index \(N\)

Let

\[
f=\sum_{m\ge1}a_f(m)q^m
\]

be one fixed normalized modular eigenform. Let \(\chi_1,\ldots,\chi_L\) be
any explicitly represented Dirichlet characters whose conductors are
coprime to \(N\). The bank can be QP-large and the characters can have
different conductors and coefficient fields. At the single index \(N\),

\[
a_{f\otimes\chi_j}(N)=\chi_j(N)a_f(N)
\qquad(1\le j\le L).
\tag{3.1}
\]

Every multiplier \(\chi_j(N)\) is public and nonzero. Hence the full twist
bank is determined by the one unknown \(a_f(N)\). Conversely, any one twist
value recovers \(a_f(N)\) after multiplication by the public inverse of
\(\chi_j(N)\). In this precise sense, the bank has information rank one.

This does not say that evaluating the twisted and untwisted forms has the
same implementation cost. If one twist has a new QP evaluator, (3.1) makes
that evaluator a QP evaluator of the base coefficient. The theorem also says
nothing about banks of genuinely different eigenforms, nontwist operations,
several unrelated indices, Rankin convolutions, or coefficient combinations
that are not scalar twists.

## 4. Globally defined elliptic-torsion endomorphisms are synchronized

Let \(S\) be a connected characteristic-zero base on which an elliptic curve
\(E\), an endomorphism

\[
\alpha\in\operatorname{End}_S(E),
\]

and the integer \(m\ge2\) are defined, with \(m\) invertible on \(S\). Let
\(p\) and \(q\) be two good residue characteristics represented by geometric
points of \(S\). Then the actions

\[
\alpha_p:E_p[m]\longrightarrow E_p[m],
\qquad
\alpha_q:E_q[m]\longrightarrow E_q[m]
\tag{4.1}
\]

are conjugate after choosing geometric \((\mathbb Z/m\mathbb Z)^2\)-bases.
In particular, they have the same characteristic polynomial, minimal
polynomial, and, when invertible, order.

For a globally defined CM endomorphism this common characteristic polynomial
is

\[
X^2-\operatorname{Tr}(\alpha)X+operatorname{Nm}(\alpha)pmod m,
\tag{4.2}
\]

and for a scalar endomorphism \([a]\) it is \((X-a)^2\). These invariants are
independent of whether the good fiber has characteristic \(p\) or \(q\).

Therefore fixed CM endomorphisms, scalar maps, and other endomorphisms that
descend from one global endomorphism cannot supply the B5 local-order or
minimal-polynomial mismatch on fixed torsion.

This statement does not cover:

- local Frobenius \(\pi_p\) and \(\pi_q\);
- endomorphisms that exist only after reduction, including extra
  supersingular endomorphisms;
- a CRT-glued endomorphism over \(\mathbb Z/N\mathbb Z\) that does not descend
  from one endomorphism on a connected base;
- an isogeny whose kernel or section is already oriented differently in the
  two components.

Those excluded objects are exactly where characteristic-dependent or
factor-local information can enter. The theorem does not assert that they
cannot be computed without factoring.

## 5. Combined consequence and surviving interface

The four results do not combine into a general lower bound. They remove four
standard repackagings:

1. naming hidden modular cusps through explicit rational endpoints;
2. treating a uniform bank of small modular coefficient outputs as low
   information;
3. treating twists of one coefficient as independent views;
4. expecting fixed global torsion endomorphisms to acquire different local
   orders after good reduction.

A materially new B5 route can still use a boundary-zero cuspidal quotient, a
compressed characteristic-scale modular-symbol operation, genuinely
different forms, a direct uniform small-modulus evaluator (which would be a
positive factoring bridge by Section 2), local Frobenius, or a new
reduction-only endomorphism with a factor-free construction.
