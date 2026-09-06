# Proof of the F156 sparse-section feedback source V2

## 1. Stage order and base factor-free coordinates

At each frozen named stage, first complete the ordinary P118 word scan and
append its exact values to the base ledger. Only then form the base section
used by the feedback scan. Apply one joint named refinement after both scans
are complete.

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

For nonempty \(S\), parity-basis independence gives \(v_S\ne0\), so the
scan enumerates only nonzero section vectors.

The omitted empty set is the identity lift. It has

\[
v_0=0,
\qquad
z_0=w_0=1,
\qquad
F_0=1.
\tag{15}
\]

Its two screens are \(N\) and \(1\) on the surviving odd-input branch. If
\(N\) is even, the elementary factor \(2\) is returned before this source.
The endpoint \(1\) has no nontrivial gcd with a named block. The exact value
\(1\) has zero parity and supplied root \(1\). It adds no decoder direction.
Therefore omitting the identity changes no direct screen, named refinement,
or exact-value retention outcome.

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

The identity case (15) is stronger: it supplies only endpoint \(1\) and exact
value \(1\), so there is no endpoint or algebraic occurrence to retain for a
nontrivial outcome.

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

The ordinary word batch is completed first. The section batch is then
completed from that stage's updated base ledger. Only after both batches are
complete is their joint endpoint refinement applied. If neither batch splits
an old block, the named basis is unchanged and the declared source stops.
Hence the algorithm terminates within the stated stage bound.

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

The identity is not a candidate, so the count is unchanged. Adding it would
add only one inert occurrence and would also leave the bound unchanged.

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

When \(r\le D\), every nonzero vector in the base parity span is represented
by one nonempty basis subset of size at most \(D\). Hence the scan exposes
every nontrivial \(z_v\) and its canonical inverse from F154. The only omitted
section vector is \(v=0\). It has

\[
s_0=1,
\qquad
P_0=s_0^2Q(0)=1.
\]

It cannot refine a named block and adds no nontrivial relation. Therefore the
nonempty scan captures the complete F154 refinement opportunity even though
it enumerates the nonzero section vectors rather than the literal whole
section. F154 proves that the nontrivial inverse representatives can refine a
named state, but not that they must.

The final three-way success condition in the statement is therefore an open
source law, not a consequence of this proof.
