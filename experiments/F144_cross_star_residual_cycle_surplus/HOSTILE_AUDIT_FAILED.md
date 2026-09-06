# F144 hostile audit — failed

## Verdict

**FAIL as frozen.**  The general residual-cycle identity is correct, and the
metric gcd conclusion is correct.  However, the advertised near-\(N\)
cycle-surplus regime in Sections 4--5 is vacuous.  The same hypotheses that
make all its edges wrapped also imply that no directed cycle of length at
most \(K\) can exist.

The frozen inputs were verified before review:

- `STATEMENT.md`:
  `937a41ce493c65f14ad2ab9c826542188e904b2ff1762d38efc380d96e13420d`;
- `PROOF.md`:
  `affcb1bdb8db25da2a81d5e27b827553039c3bf49e0ed9a56358bd8f2e841aa3`.

## 1. Fatal obstruction: every wrapped directed cycle is already long

Consider one directed containment cycle \(C\), without assuming that its
residual product is a square.  Write

\[
A_C=\prod_{e\in C}a_e,
\qquad
T_C=\prod_{e\in C}T_e,
\qquad
Q_C=\prod_{e\in C}q_e=\prod_{e\in C}r_e.
\]

The exact cycle identities give

\[
\prod_{e\in C}U_e=Q_CA_C^2,
\qquad
\prod_{e\in C}c_e=Q_CT_C.
\]

Each \(U_e\equiv c_e\pmod N\), and \(Q_C\) is a unit modulo \(N\).
Therefore

\[
\boxed{N\mid A_C^2-T_C.}
\]

If at least one edge of this cycle is wrapped, then
\(\prod U_e>\prod c_e\), so

\[
A_C^2>T_C.
\]

The two facts combine to give the stronger necessary condition

\[
\boxed{A_C^2\ge N+T_C>N,\qquad A_C>\sqrt N.}
\tag{A}
\]

Section 4 proves that every edge in its near-\(N\) graph is wrapped.  A
cycle of length at most \(K\), with anchors at most \(H\), would instead
satisfy

\[
A_C\le H^K.
\]

But the frozen size condition

\[
2H^{K(R+1)}<N,
\qquad R\ge2,
\]

implies

\[
H^{2K}<N,
\qquad H^K<\sqrt N.
\tag{B}
\]

Equations (A) and (B) contradict each other.  Hence, under the frozen
Section 4 hypotheses, the graph contains **zero** directed cycles of length
at most \(K\).  It cannot contain \(R+1\) such cycles.

Thus implication (19) is logically true only because its antecedent is
impossible.  The residual-parity dimension count never activates.  The
claimed remaining source-side gate is not merely unproved: the stated gate
is excluded by the exact carry identity above.

This is material.  It removes the second advertised positive fact and the
only proposed quasipolynomial forcing regime.  Repair requires a different
regime, not a local wording change.

## 2. The general residual-cycle theorem survives

For an indexed collection of directed cycles, the tail and head products
are equal.  If the combined residual product is \(S^2\), then

\[
\prod_e C_eL_e=(Q\mathcal A S W)^2
\]

and, because
\(W\equiv(QS^2)^{-1}\pmod N\), its root is

\[
Q\mathcal A S W\equiv\mathcal A S^{-1}\pmod N.
\]

The same calculation gives
\(\mathcal A^2\equiv S^2\pmod N\).  If one occurrence wraps, exact product
comparison gives \(\mathcal A>S\).  If also \(2\mathcal A<N\), then

\[
0<\mathcal A-S<\mathcal A+S<N.
\]

Since \(N\mid(\mathcal A-S)(\mathcal A+S)\), neither factor can be a unit
and neither can be divisible by \(N\).  Both displayed gcds are proper.
No distribution assumption is used.  These quantifiers and the exact root
calculation pass.

The new obstruction (A) does not make this general lemma vacuous.  It only
shows that a cycle containing a wrap must have anchor product above
\(\sqrt N\).  The lemma still permits
\(\sqrt N<\mathcal A<N/2\).

### Hand certificate

The supplied hostile certificate checks the surviving general lemma.  Take

\[
N=35,\quad q=13,\quad r=17,\quad a=2,\quad b=3.
\]

Then

\[
[13\cdot2^2]_{35}=17,
\qquad
[17\cdot3^2]_{35}=13.
\]

This is a two-edge directed cycle with residuals \(1,1\), and both edges
wrap.  Its anchor product is \(6\), so \(2\mathcal A=12<35\), and

\[
\gcd(6-1,35)=5,
\qquad
\gcd(6+1,35)=7.
\]

At the actual relation level,

\[
(561)(1716)(351)(4131)=1181466^2,
\qquad
1181466\equiv6\pmod{35}.
\]

The two centers are pairwise-coprime units and the anchors are eligible
primes.  Thus the positions are legal under the theorem if \(13\) and
\(17\) occur together as current named blocks.  This is a conditional
P128-semantic certificate.  It does not prove that the actual P118
transcript for \(N=35\) reaches that frozen basis; preprocessing can already
factor this small input.  It also does not satisfy the Section 4 size
conditions.

## 3. Deduplication and cycle overlap pass

The proof correctly restores actual canonical and lifted values before
deduplication.  Every such value is congruent to \(1\pmod N\).  Removing two
equal occurrences removes an exact square \(P^2\) and divides the positive
root by \(P\equiv1\pmod N\).  It therefore preserves the normalized root.

This also handles a source edge used by several logical cycles and equality
between a canonical value and a lifted value.  If all selected values were
deleted, the remaining root would be \(+1\); the strict metric conclusion
prevents that collapse.  There is no conflict with P129's warning about
deduplicating conceptual bridge columns with different supplied roots,
because F144 performs deletion on the actual P128 values, whose supplied
roots are all one.

The phrase “distinct simple directed cycles” should mean distinct labeled
edge cycles up to cyclic rotation.  This definitional point is not the
fatal issue: even one such short cycle is forbidden by (A)--(B).

## 4. Residual dimension count is correct but unreachable

If \(T_e<R\), every rational-prime row is indexed by a prime below \(R\),
so there are fewer than \(R\) rows.  Any \(R+1\) cycle columns have a
nonzero binary dependency, and that dependency makes the combined residual
product an exact square.  The occurrence and anchor-product bounds are also
correct as formal bounds.

The defect is not this linear algebra.  The defect is that the required
columns cannot exist under (16).

## 5. Cost and parameter scope

Conditional on an explicit graph, the stated enumeration, trial division,
linear algebra, exact products, square root, and gcd work are
quasipolynomial for the frozen polylogarithmic \(R,H,K\).  This cost claim
passes.  It is not a useful detector in the frozen regime because it always
finds fewer than one qualifying cycle.

The parameter statement is unnecessarily narrow.  The same cost analysis
can allow quasipolynomially enumerable \(H\) and \(R\), with
polylogarithmic \(K\), subject to the explicit size inequalities.  In
particular, it can include the P128 anchor cap \(H=n^3\), whereas frozen
Section 5 writes only \(H=(\log n)^{O(1)}\).  This scope loss is not by
itself fatal.  It also does not repair the obstruction: whenever
\(H^K<\sqrt N\), no wrapped cycle of length at most \(K\) exists.  All
standard bounded-support quasipolynomial choices have exactly this problem
asymptotically.

## 6. Determinant and P114 checks pass

For two endpoints, substitution verifies

\[
\Delta=sc-td=qa^2s-rb^2t.
\]

The divisibility \(\gcd(c,d)\mid\Delta\), the strict size bound on
\(|\Delta|\), and the implication from \(hN\ge qr a^2b^2\) are correct.
When \(\Delta=0\), the displayed factorization through \(z\) and
\(Z=z+gN\) gives normalized root \(Z/z\equiv1\pmod N\).  The zero
determinant is therefore a global-root decoy.

The four endpoints in (26) do form the stated P114 multiplicative
rectangle.  This is a correct specialization and makes no new density
claim.

## 7. Novelty and surviving scope

The surviving general lemma is a real extension of P129's exact endpoint
cycle.  It permits non-square residuals on individual containment edges,
closes their product across cycles, and turns wrapping plus a metric bound
into an automatic non-global root.  It is also outside F143's purely formal
endpoint-equality cycle space, so it is a genuine arithmetic-hypercycle
certificate rather than a commutation diamond.

However, F144 does not promote as stated.  Relative to P128/P129/F143, its
new unconditional algorithmic progress was meant to be the short-cycle
surplus regime.  The exact obstruction above proves that regime empty.
What remains is a correct conditional certificate and a sharper negative
boundary:

\[
\boxed{
\text{every directed containment cycle with a wrapped edge has }
\prod a_e>\sqrt N.
}
\]

A revised candidate should lead with this boundary and should not claim
that bounded-anchor, polylogarithmic-length wrapped cycles are the next
source-side gate.

