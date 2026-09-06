# F146 V2 hostile re-audit — PASS

## Frozen inputs and method

I audited only the corrected V2 candidate. The frozen hashes matched:

- `V2_STATEMENT.md`:
  `886ca7aafa5d5cd42514fa4fbd6223a9e7ca12a368820a8c53b9731b3553ac57`;
- `V2_PROOF.md`:
  `d4836162de32274bf253461b3f712c8e6d5662127ac2a907dc723d7c028a093c`.

I also read the preserved V1 failure audit to test each stated repair. I did
not modify either frozen V2 file. I used no research computation.

## Verdict

**PASS.** V2 repairs both defects in V1. I found no false theorem, missing
hypothesis, or complexity overclaim in the corrected candidate.

This is a boundary theorem for the local exchange-minor route. It is not an
AKS counterexample and it is not a factoring algorithm. Its positive part is
conditional on a common unit base and on either a small success radius or a
polylogarithmic tail. Its negative construction concerns general
CRT-representable matrices, not the special AKS coefficient matrix.

## 1. The arbitrary-composite repair is exact

For an exchange indexed by equal-size sets (I,J), factoring out (B) and
expanding along the retained identity columns gives

\[
\det E_{I,J}
=\varepsilon(I,J)\det(B)\det C[I,J].
\]

The factor \(\varepsilon(I,J)\det B\) is a unit modulo (N). Multiplying a
residue by a unit preserves its gcd with (N). Thus the scan succeeds on an
arbitrary composite exactly when one of the scanned determinants satisfies

\[
1<\gcd(\det C[I,J],N)<N.
\]

This is precisely the V2 definition of \(\gamma_B\), so scan success is
equivalent to \(\gamma_B\le s\) without a squarefreeness assumption.

If a determinant is zero modulo one prime divisor of (N) and nonzero
modulo another, its gcd contains the first prime and omits the second. The
gcd is therefore nontrivial and proper. Hence

\[
\gamma_B\le\delta_B
\]

for every composite (N), including prime powers under the usual convention
that \(\delta_B=\infty\) when no two distinct local zero statuses exist.

When (N) is squarefree, a determinant has gcd 1 exactly when it is nonzero
in every residue field, and gcd (N) exactly when it is zero in every
residue field. A proper gcd is therefore equivalent to a nonconstant local
zero pattern. This proves the corrected equality

\[
\gamma_B=\delta_B
\]

on squarefree inputs.

The V1 counterexample is now handled correctly. For (N=45) and determinant
15, the gcd is 15 although the determinant is zero modulo both 3 and 5. It
gives \(\gamma_B=1<\delta_B=\infty\). V2 explicitly classifies this as a
valuation-only success and makes no false converse claim.

## 2. The count and the empty-tail repair pass

At support (k), the removed base set and inserted tail set are chosen in
exactly

\[
\binom Ak\binom tk
\]

ways. Therefore the displayed sum for (Q_s(A,t)) is exact. If (At\ge1),
each summand is at most \((At)^s\). If (t=0), only the support-zero base
occurs. Both cases satisfy

\[
Q_s(A,t)\le(s+1)\max\{1,At\}^{s}.
\]

This fixes the V1 endpoint failure. It also covers (s=0).

For polynomial (A,r) and polylogarithmic (s), the base-two logarithm of
the scan count is

\[
O(s\log n)=O((\log(n+1))^{d+1}).
\]

Computing (C=B^{-1}T) is polynomial on the unit-determinant branch.
Adjugate or division-free methods do not require a field pivot. Every tested
determinant has size at most (s); modular arithmetic keeps its entries at
(O(n)) bits, and the final gcd is polynomial. Multiplying by the exact scan
count gives the claimed quasipolynomial bit bound.

If the tail has (t\le s) columns, every maximal column set uses at most
(t) tail columns and is scanned. The common unit base gives rank (A) in
every residue field, so maximal bases determine each full column matroid.
Thus every local matroid mismatch is found. On squarefree inputs, the
\(\gamma_B=\delta_B\) result makes the full-scan if-and-only-if exact. On
non-squarefree inputs, valuation-only successes can occur in addition.

## 3. The near-threshold estimate passes

With (x=\sqrt{r-1}) and (u=r-1-L^2>0), where (L=\log_2N),

\[
r-\lfloor Lx\rfloor
<x(x-L)+2
=\frac{x}{x+L}u+2
<u+2.
\]

Therefore a polylogarithmic positive excess above (L^2) gives a
polylogarithmic tail and a complete quasipolynomial scan. V2 correctly keeps
this conditional. It does not claim that a suitable prime modulus, a common
unit base, or a mismatch exists for every input.

## 4. The delayed-disagreement construction passes

Fix (s\ge1) and put (d=s+1). For

\[
U_{ih}=i^h,\qquad V_{hj}=j^h,\qquad 0\le h\le s-1,
\]

every square minor of (U), and every corresponding transposed minor of
(V), is a positive generalized Vandermonde determinant. Cauchy--Binet then
gives, for all \(|I|=|J|=k\le s\),

\[
\det(UV)[I,J]
=\sum_{|K|=k}\det U[I,K]\det V[K,J]>0.
\]

There is no sign cancellation. Since (U) is injective and (V) is
surjective over \(\mathbb Q\), (D=UV) has rank exactly (s). Hence every
proper square minor used by an exchange is positive, while \(\det D=0\).

For (E_{ij}=i^{j-1}), every square minor, including the full determinant,
is a positive generalized Vandermonde determinant. The common bound

\[
H_s=d!\bigl(s d^{2s}\bigr)^d
\]

dominates the absolute value of every minor of (D) and (E). Choosing
primes (H_s<q<2H_s) and (q<p<2q) therefore preserves every positive
minor in its assigned field. Entrywise CRT produces one (C\pmod{pq}) with

\[
C\equiv E\pmod p,\qquad C\equiv D\pmod q.
\]

All exchanges through support (s) are bases in both fields. The full
support-(s+1) exchange is a basis modulo (p) and dependent modulo (q).
Thus the first local disagreement is exactly (s+1). Because (N=pq) is
squarefree, this is also the first proper-gcd exchange.

Finally,

\[
\log H_s=\Theta(s^2\log(s+1)),\qquad
n=\Theta(s^2\log(s+1)).
\]

Thus (s>(\log(n+1))^D) for every fixed exponent (D) on all sufficiently
large members. The quantifier needed to defeat every fixed polylogarithmic
exchange radius is valid.

## 5. Padding preserves the claimed property

Set (A=n^2), place the old (d\)-by-(d) tail in the first (d) rows, and
fill later tail rows with zero. A minor using a padded row is zero in both
fields. A minor using only old rows has its old status. Hence all local zero
patterns still agree through support (s), and the old support-(s+1)
mismatch remains.

The padded construction does **not** retain the stronger unpadded statement
that every small exchange is a basis: padded-row exchanges are dependent in
both fields. V2 claims only that the first disagreement is preserved, so
there is no scope error. The dimensions satisfy

\[
A=n^2,\qquad r=A+s+1,\qquad r/A\to1.
\]

V2 also states explicitly that this near-square matrix is not an AKS error
matrix.

## 6. P11 calibration and scope pass

The promoted P24 artifacts give the stated values

\[
A=2942,\qquad t=11,\qquad
\binom A2\binom t2=237{,}941{,}605,
\]

with zero and two singular two-tail minors in the two local fields, and no
one-tail mismatch. For a uniform (2\)-by-(2) matrix over
\(\mathbb F_\ell\),

\[
\Pr(\text{singular})
=1-(1-\ell^{-1})(1-\ell^{-2})
=\ell^{-1}+\ell^{-2}-\ell^{-3}.
\]

The stated expectations follow from this comparison model and the retained
family sizes. V2 does not assert that AKS minors are independent or random.
It uses the comparison only to show that the finite P11 hit is at an
ordinary exact-zero scale.

The final union-bound warning is also correctly conditional. On balanced
semiprimes, quasipolynomially many residues with uniform-scalar divisibility
still have total hit probability

\[
2^{(\log n)^{O(1)}}(p^{-1}+q^{-1})
=2^{-\Theta(n)+o(n)}.
\]

## Residual risk

The theorem does not settle the AKS route. The CRT/Vandermonde family only
blocks a forcing theorem based on generic representable-matroid structure,
a common base, dimensions, and a bounded exchange radius. An AKS-specific
identity could still force a polylogarithmic mismatch. A proof-blind
reconstruction is still required before promotion under the project
protocol.
