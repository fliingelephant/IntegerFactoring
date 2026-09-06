# F193 V3 blind reconstruction

## Input discipline and verdict

The SHA-256 digest of `V3_STATEMENT.md` was checked before it was read. It is

```text
286ff3962751262c7256e5d78cfb0b510fb9563523765c9c9776e949eaeadc05
```

which is the required digest. This reconstruction uses only `PROMPT.md` and
`V3_STATEMENT.md`.

**Verdict: pass, at the narrow scope stated.** Each of the four mathematical
boundaries can be reconstructed independently. They do not prove the
top-level factoring statement. They also do not give a general lower bound
for any of the represented mathematical objects.

Two interpretations must remain explicit:

1. The rank in Section 3 is rank over a common coefficient overfield after
   compatible embeddings. It is not a claim that the coefficients have
   rational-vector-space rank one.
2. The evaluator corollary in Section 3 uses the ordinary meaning of an exact
   QP evaluator: the character value and the compatible field representation
   support exact arithmetic in time polynomial in their explicit encoding
   lengths. The coefficient identity itself does not need this computational
   convention.

Neither point enlarges the stated result.

## 1. Sparse modular-symbol boundaries

### 1.1 Cusp types at squarefree level

Represent a reduced cusp by a primitive column vector `(a,c)`, with `(1,0)`
for infinity. Let

\[
\gamma=\begin{pmatrix}A&B\\ C&D\end{pmatrix}\in\Gamma_0(N).
\]

For every prime `s` dividing `N`, one has `C = 0 mod s` and
`AD = 1 mod s`. In particular, `D` is nonzero modulo `s`, and the new lower
coordinate satisfies

\[
Ca+Dc\equiv Dc\pmod s.
\]

Thus `s` divides the cusp denominator before the action if and only if it
divides it after the action. Reduction of the resulting fraction cannot alter
this conclusion: the matrix is invertible modulo `s`, so its two output
coordinates cannot both vanish modulo `s`.

The standard elementary classification of cusps for `Gamma_0(N)` refines
the divisor `d = gcd(c,N)` by a residue class modulo
`gcd(d,N/d)`. This follows by applying Bezout row operations subject to the
lower-left congruence modulo `N`; the remaining numerator freedom is exactly
modulo `gcd(d,N/d)`. If `N` is squarefree, then

\[
\gcd(d,N/d)=1
\]

for every divisor `d` of `N`. Hence there is exactly one orbit for each
divisor. For `N=pq`, the four types are `1,p,q,N`. Infinity has type `N`
because `gcd(0,N)=N`.

### 1.2 The boundary dichotomy

For each listed endpoint, compute `gcd(c,N)`. If it is `p` or `q`, it is
immediately a nontrivial divisor of `N`. If this never happens, every endpoint
has type `1` or `N`.

In the free abelian group on cusp orbits,

\[
\partial\{\alpha,\beta\}=[\beta]-[\alpha].
\]

Consequently, if all endpoints have the two global types, then

\[
\partial C=A[c_1]+B[c_N].
\]

Every elementary boundary has coefficient sum zero, so `A+B=0`. Therefore

\[
\partial C=B([c_N]-[c_1]).
\]

This proves only a support statement. It gives no bound on `B` and says
nothing about a chain with zero boundary.

Let `B_enc` be the total input encoding length of the sparse chain. There are
at most `B_enc` listed endpoints, and no integer operated on has more than
`B_enc+n` input bits. Euclidean gcd, rational reduction, coefficient addition,
and comparison use time polynomial in this quantity. If

\[
B_{\rm enc}\le 2^{C(\log_2(n+1))^k},
\]

then any fixed polynomial in `B_enc+n` is again numerical-QP in `n`. This
proves the runtime part of the dichotomy.

### 1.3 Good Hecke branches

A branch of a good Hecke correspondence can be represented by an integral
matrix

\[
M=\begin{pmatrix}u&v\\ Nw&z\end{pmatrix}
\]

whose determinant is coprime to `N`. For each `s | N`, this matrix is upper
triangular and invertible modulo `s`; hence both `u` and `z` are nonzero
modulo `s`. Acting on a primitive cusp vector `(a,c)` gives lower coordinate

\[
Nwa+zc\equiv zc\pmod s.
\]

The same invertibility argument prevents reduction of the output vector from
changing whether this coordinate is divisible by `s`. Each prime divisor of
`N` therefore has unchanged membership in `gcd(c,N)`. Every good branch
preserves cusp type. This applies to composite `m` as long as `gcd(m,N)=1`.

### 1.4 Fricke and selective Atkin--Lehner operators

At squarefree level, a type-`d` cusp can be represented by `1/d`. The
unnormalized Fricke matrix sends

\[
\frac1d\longmapsto -\frac dN=-\frac1{N/d}.
\]

Thus Fricke sends `d` to `N/d`; it swaps `1` with `N` and swaps `p` with
`q`. It preserves the partition into global and factor-local cusp types.

For an exact divisor `Q || N`, a standard unnormalized integral
Atkin--Lehner representative has the form

\[
W_Q=\begin{pmatrix}Qa&b\\ Nc&Qd\end{pmatrix},
\qquad
Qad-\frac NQbc=1.
\]

Its determinant is `Q`. Let `s | N`. If `s` does not divide `Q`, the lower
coordinate modulo `s` is a nonzero scalar multiple of the old lower
coordinate, so membership of `s` in the cusp type is preserved. If `s`
divides `Q`, the displayed Bezout relation makes `b` and `c` units modulo
`s`. A primitive input whose lower coordinate is not divisible by `s` maps
to an output with lower coordinate divisible by `s` and upper coordinate not
divisible by `s`. If the input lower coordinate is divisible by `s`, both
raw output coordinates have a factor `s`, but the raw lower coordinate has
exactly one such factor; cancelling it makes the reduced lower coordinate a
unit modulo `s`. Hence membership of `s` is toggled. This is exactly the
claimed prime-by-prime behavior.

For `N=pq`, the only proper nontrivial exact divisors are `p` and `q`.
Supplying either integer as the public operator label already supplies a
factor. The determinant assertion applies to the integral representative
above, not to a matrix rescaled for analytic normalization.

Good branches preserve the set `{1,N}` and Fricke permutes it. Therefore any
finite composition of these operations preserves global boundary support.
The invariant is stronger than the stated QP-many version. The QP qualifier
matters only when one also claims that an explicit expansion can be processed
within a QP resource bound. It says nothing about a compressed dense object.

## 2. Uniform small-modulus evaluation

### 2.1 Size of the exact coefficient

For distinct primes `p,q`, multiplicativity of the divisor-sum function gives

\[
\sigma_1(pq)=(1+p)(1+q)=N+p+q+1.
\]

Since `p,q` are distinct odd primes, `p+q <= pq=N`. Also, the definition of
`n` gives `N+1 <= 2^n`. Consequently

\[
0<b_N=N+p+q+1\le 2N+1<2(N+1)\le 2^{n+1}.
\tag{2.1}
\]

### 2.2 Enough small auxiliary primes

An elementary Chebyshev bound gives an absolute constant `c>0` such that

\[
\pi(x)\ge c\frac{x}{\log x}
\]

for all sufficiently large `x`. One obtains this bound from the prime
factorization of central binomial coefficients: the inequalities
`2^m <= binom(2m,m) < 4^m`, grouped by prime powers, give linear upper and
lower bounds for the Chebyshev functions, and hence the displayed lower
bound for `pi(x)`. Enlarging constants handles the finite initial range.

Set `x=C n log(n+2)`. For sufficiently large fixed absolute `C`, the bound
above supplies at least `n+2` primes at least `5` below `x`, for every
semiprime input size; the finitely many small sizes are absorbed by the same
choice of `C`. Each such prime has `O(log n)` bits. A deterministic sieve up
to `x` constructs the list in polynomial bit time and polynomial space.

If an intended meaning of "auxiliary" excludes a prime divisor of `N`, first
compute `gcd(ell,N)`. A nontrivial gcd finishes the factorization. Otherwise
the evaluator's promise applies. Thus this convention creates no gap.

Choose `n+2` eligible primes and let their product be `M`. Then

\[
M\ge 5^{n+2}>2^{n+1}>b_N.
\tag{2.2}
\]

### 2.3 CRT recovery and factoring

Call the one uniform evaluator at the chosen primes. The residues determine
a unique integer in `[0,M)`. Equations (2.1)--(2.2) show that this integer is
the exact `b_N`.

If the evaluator instead returns `24b_N mod ell`, use only `ell >= 5` and
multiply each answer by the inverse of `24 mod ell`. The same CRT step then
recovers `b_N`.

Set

\[
s=b_N-N-1=p+q.
\]

The discriminant

\[
\Delta=s^2-4N=(p-q)^2
\]

is a perfect square, and exact integer square root gives

\[
p=\frac{s+\sqrt\Delta}{2},\qquad
q=\frac{s-\sqrt\Delta}{2}
\]

up to order. Multiplication verifies the result.

There are `O(n)` calls. Their combined input length is `n+O(log n)=O(n)`.
Uniformity means that one fixed QP bound applies to all calls; multiplying it
by `O(n)` remains QP. The CRT modulus has `O(n log n)` bits, so sieving, gcds,
CRT, integer square root, and verification all have polynomial bit
complexity. This proves deterministic numerical-QP factoring on the stated
semiprime promise.

The quantifiers are essential. The proof uses a modulus product that grows
past the a priori bound on `b_N`. It gives no conclusion from one fixed
modulus or any fixed finite bank. Conversely, a single uniform evaluator for
the growing bank is enough; separate nonuniform advice for each input length
would not meet the hypothesis.

## 3. A bank of twists of one form

### 3.1 Coefficient identity

The Dirichlet twist is defined coefficientwise:

\[
f\otimes\chi=\sum_{m\ge1}\chi(m)a_f(m)q^m.
\]

Therefore, at the single index `N`,

\[
a_{f\otimes\chi_j}(N)=\chi_j(N)a_f(N)
\]

for every row. Primitivity is not needed for this identity. For an
imprimitive character, the usual extension by zero accounts for indices not
coprime to its defining modulus.

### 3.2 Exact meaning of rank one

Use the specified compatible embeddings to put the coefficient field of `f`
and all character-value fields into a common overfield `K`. Write

\[
x=a_f(N),\qquad c_j=\chi_j(N).
\]

The complete bank is

\[
\Phi(x)=(c_1x,\ldots,c_Lx).
\]

Over `K`, the matrix of `Phi` is the single public column
`(c_1,...,c_L)^T`; its rank is at most one. If some `c_j` is nonzero, the
projection onto row `j` followed by multiplication by `c_j^{-1}` is a left
inverse and recovers `x`. If every `c_j` is zero, `Phi` is the zero map and
the coefficient observations do not depend on `x`.

A nonzero Dirichlet-character value is a root of unity because it lies in the
finite image of the character on the finite unit group. Moreover,

\[
\chi(N)\ne0\quad\Longleftrightarrow\quad
\gcd(N,M)=1
\]

when `M` is its defining modulus. This proves the two stated sufficient
conditions involving a conductor or defining modulus coprime to `N`.

With standard explicit exact-field representations, recovery from a nonzero
row takes one multiplication by a known root of unity inverse and costs only
polynomial time in the represented data. Thus an exact QP evaluator for that
twist yields an exact QP evaluator for the base coefficient.

This argument is solely an identity among coefficient values. It gives no
lower bound on evaluation. It also does not say that character metadata is
factor-free: for example, a public defining modulus can itself have a
nontrivial gcd with `N`. Nor does it relate coefficients of genuinely
different forms or different indices.

## 4. A global endomorphism on prime-to-characteristic torsion

### 4.1 Constancy as a finite etale local system

Because `r` is invertible on `S`, the group scheme `E[r]` is finite etale of
rank `r^2`. Its geometric fibers form a locally constant sheaf of
two-dimensional `F_r`-vector spaces. On a connected arithmetic base, any two
geometric points are joined by an etale path in the fundamental groupoid.
Parallel transport along such a path gives an `F_r`-linear isomorphism

\[
\tau:E_{\bar p}[r]\longrightarrow E_{\bar q}[r].
\]

The restriction of a global morphism `alpha in End_S(E)` to `E[r]` is a
morphism of this local system. Functoriality of parallel transport gives

\[
\tau\alpha_p=\alpha_q\tau,
\]

and hence

\[
\alpha_q=\tau\alpha_p\tau^{-1}.
\]

After independent choices of bases, the two matrices are conjugate in
`Mat_2(F_r)`. Conjugate matrices have the same characteristic polynomial and
the same monic minimal polynomial. If one is invertible, both are, and their
orders in `GL_2(F_r)` agree.

This proof uses the usual locally Noetherian meaning of "arithmetic base."
The characteristic-zero generic point is not needed for the local-system
conjugacy; it is relevant to identifying a CM endomorphism and its trace and
norm.

### 4.2 The CM polynomial

On a characteristic-zero CM elliptic curve, a CM endomorphism `alpha` is an
element of an order in an imaginary quadratic field. Multiplication by
`alpha` on the two-dimensional rational Tate module has the two field
embeddings of `alpha` as its eigenvalues. Its characteristic polynomial is
therefore

\[
(X-\alpha)(X-\bar\alpha)
=X^2-\operatorname{Tr}(\alpha)X+\operatorname{Nm}(\alpha).
\]

The trace and norm are integers for an element of the CM order. The integral
Tate module is stable under `alpha`, so reducing its matrix modulo `r` gives
the action on `E[r]` and reduces this same polynomial modulo `r`. Since the
endomorphism descends over `S`, this is the common polynomial in every good
fiber covered by the theorem. For the scalar endomorphism `[a]`, commutation
with scalar multiplication gives the matrix `a I_2` directly.

### 4.3 Necessity of the exclusions

Each listed exclusion removes a hypothesis used above:

- local Frobenius is attached to one residue fiber and is not generally the
  specialization of one global endomorphism;
- an endomorphism created after reduction is not a morphism of the global
  local system;
- characteristic-primary torsion is not finite etale, so parallel transport
  does not give the argument above;
- on a disconnected base, locally constant data on two components need not
  agree;
- independently CRT-glued local maps need not descend to a single global
  morphism.

Thus no conclusion about their local orders or minimal polynomials follows
from this theorem.

## 5. Scope audit of the surviving interface

The four proofs leave exactly the advertised kinds of openings:

- Section 1 controls only explicit cusp-boundary support. It does not control
  boundary-zero cuspidal classes or an operation whose characteristic-scale
  expansion is never explicitly materialized.
- Section 2 turns a new uniform growing-bank evaluator into a factoring
  algorithm. It does not construct that evaluator and does not analyze a
  fixed bank.
- Section 3 collapses twists of one coefficient to scalar multiples of that
  coefficient. It does not collapse different forms, Rankin convolutions,
  nontwist operations, or different indices.
- Section 4 synchronizes only one endomorphism descending over one connected
  base on torsion of order invertible on that base. It does not synchronize
  local Frobenius, reduction-only endomorphisms, disconnected CRT data, or
  characteristic-primary torsion.

Accordingly, V3 establishes four representation boundaries and nothing
stronger. In particular, it neither supplies nor refutes a classical
quasipolynomial-time factoring algorithm for arbitrary integers.
