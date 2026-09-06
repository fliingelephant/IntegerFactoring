# Proof of the F156 sparse-section feedback source

## 1. Base factor-free coordinates

Every base exact value \(A_i\) is congruent to \(1\) modulo \(N\), so it is
a unit. Complete gcd-free refinement expresses the distinct values in
pairwise-coprime blocks. Maximal perfect-power extraction makes every block
a nonsquare. A block dividing a unit value is itself a unit modulo \(N\).

Separating every exponent into its even part and parity gives the exact
factorization

\[
A_i=t_i^2Q(v_i).
\]

The supplied modular root of a canonical inverse exact value is \(1\).
Therefore

\[
(t_i^{-1})^2\equiv Q(v_i)\pmod N,
\]

and (3) is its public decorated lift.

The P138 online test either returns a non-global root or gives a consistent
quotient section over the base parity span. The source construction below
uses only actual basis lifts, so it is defined on either branch before the
return and requires no hidden CRT choice.

## 2. Sparse actual lifts are public

The decorated group is an abelian group of exponent two. Because the
\(b_i\) form a binary basis, every set \(S\) in (5) gives the unambiguous
actual lift

\[
e_S=\mathop{\star}_{i\in S}e_i=(v_S,z_S).
\]

All star-products use public modular multiplication and inversion. The
second coordinate is a unit and satisfies

\[
z_S^2\equiv Q(v_S)\pmod N.
\tag{14}
\]

The least positive inverse \(w_S\) exists and is public. Both endpoints lie
in \(\{1,\ldots,N-1\}\), so their exact product satisfies

\[
1\le F_S<N^2,
\qquad
F_S\equiv1\pmod N.
\]

For nonempty \(S\), parity-basis independence gives \(v_S\ne0\), so
\(z_S\) is well-defined without using the identity candidate.

## 3. Exact screen identity

Multiplication by the unit \(z_S\) preserves gcd with \(N\). Since
\(z_Sw_S\equiv1\pmod N\),

\[
\gcd(z_S-w_S,N)
=
\gcd(z_S^2-1,N).
\]

Equation (14) gives the minus case of (9). The same calculation with a plus
sign gives

\[
\gcd(z_S+w_S,N)
=
\gcd(z_S^2+1,N)
=
\gcd(Q(v_S)+1,N).
\]

The equality uses congruence modulo \(N\), not exact equality of the dense
integer \(Q(v_S)\). Thus modular evaluation through \(z_S^2\) is sufficient.

## 4. Endpoint and exact-value semantics

Every endpoint presentation is inserted before exact-value deletion. This
preserves every possible split of an old named block. Equal residues give
the same canonical endpoint pair. Equal exact values can add only duplicate
binary directions with positive root congruent to the exact value, hence
\(+1\) modulo \(N\). Deleting their algebraic copies after exposure does not
change the normalized-root image.

The feedback exact values are retained for the final decoder but are
excluded from every future section basis. Therefore a section scan can
change a later named basis only by splitting an old named block. It cannot
recursively amplify its own relation rank inside the source grammar.

Probe-only cofactors are discarded only from the named grammar. Their exact
relation occurrences remain in the final decoder input, as in P118.

## 5. Number of named stages

Let \(A_0\) be the fixed P118 initial named endpoint product. Every later
named block is a divisor descendant of \(A_0\), because only factors that
occur in an old named block survive as future generators.

Complete multiplicity-aware refinement makes every strict stage replace one
old block by at least two pairwise-coprime descendants. Thus the number of
strict stages is bounded by the total number of prime factors of \(A_0\)
with multiplicity, and hence by its bit length \(\Lambda_0\). P118 gives
\(\Lambda_0=2^{O(L^2)}\).

If neither the ordinary word batch nor the section batch splits an old
block, the named basis is unchanged and the declared source stops. Hence
the algorithm terminates within the stated stage bound.

## 6. Source and bit complexity

P118 gives at most \(2^{O(L^4)}\) base records over all named stages.
Global exact-value deletion can only decrease this number. The binary rank
\(r\) of the base parity matrix is therefore at most

\[
R_0=2^{O(L^4)}.
\]

The elementary bound

\[
\sum_{j=1}^{D}\binom rj
\le(D+1)\max\{1,r\}^{D}
\]

and \(D=L^2\) give \(2^{O(L^6)}\) candidates per stage. Multiplication by
the \(2^{O(L^2)}\) stage bound does not change the \(O(L^6)\) exponent.

Every star operation and canonical inverse uses \(O(n)\)-bit modular
integers. Every feedback value is below \(N^2\). Basis provenance,
factor-free coordinates, endpoint batches, and all retained records have
total length \(2^{O(L^6)}\).

Gcd-free refinement, perfect-power extraction, binary elimination, exact
root construction in compact factor-free coordinates, modular root-image
evaluation, and gcd testing are polynomial in this explicit length. A
polynomial in \(2^{O(L^6)}\) is still \(2^{O(L^6)}\), proving (13).

## 7. Dense-provenance distinction and scope

The coordinates \(v_i\) belong to the global factor-free block basis of the
base ledger. Their support is not bounded by \(D\). The xor of at most
\(D\) such vectors can therefore have support much larger than \(D\).
The corresponding \(Q(v_S)\) is a dense squareclass word even though its
relation-basis description is sparse.

No algebraic theorem here says that the resulting residue \(z_S\) is new
relative to every old modular word. The proven difference is the declared
grammar and its cost.

When \(r\le D\), every vector in the base parity span is a subset of the
basis of size at most \(D\). Hence the scan exposes every \(z_v\) and its
canonical inverse from F154. F154 proves that these inverse representatives
can refine a named state, but not that they must.

The final three-way success condition in the statement is therefore an open
source law, not a consequence of this proof.
