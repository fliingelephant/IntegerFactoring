# Hostile audit of F26 — holographic factor-witness contraction

**Audited family:** F20.

**Audited artifact:** `experiments/F26_holographic_factor_network/RESULT.md`.

**Method:** symbolic hostile audit only.  No computation was run.

**Sources and prior state read:** `PROMPT.md` in full; P10, P19, and P29 in
`PROVED.md`; the corresponding F06/F11/F15 closures in `FAILED.md`; F20 in
`REGISTRY.md`; and the candidate in full.  The cited primary source was also
checked directly: Sergey Bravyi, [*Contraction of matchgate tensor networks on
non-planar graphs*](https://arxiv.org/abs/0801.2989), equation (1) and the
sentence immediately following it.

## Executive verdict

The conditional pinned-count reduction to complete factorization is correct,
including repeated factors, prime powers, unbalanced composites, recursion,
verification, and polynomial bit lengths.  The COPY classification is also
correct as a classification of \(T^{\otimes3}E\), and the AND parity
contradiction is algebraically correct for the column-ratio hypothesis used in
Section 5.

The current version nevertheless has one substantive convention error.  For
ordinary tensor contraction, transforming the COPY endpoint of an edge by
\(T\) requires transforming the opposite endpoint by

\[
  S=(T^{-1})^{\mathsf T},
\]

not by \(T^{-1}\).  Equations (3.2) and (4.4), and the sentence claiming that
the opposite convention follows merely by replacing \(T\) by its inverse,
therefore do not describe a contraction-preserving holographic
transformation as written.

This error is repairable and does **not** overturn the local no-go theorem.
For both COPY normal forms, the correct dual matrix \(S\) still has, at
transformed coordinate \(b\), an original-one/original-zero column ratio
\(r(-1)^b\) with \(r\ne0\).  Consequently Section 5 applies verbatim after
that corrected derivation, and the arbitrary output basis remains arbitrary.

The exact current version is not a strict pass.  It should be corrected and
then freshly re-audited, because the correction changes the mathematical
transformation, not merely prose.

## 1. Conditional exact contraction really would factor

### 1.1 Witness network and uniqueness

A uniform polynomial-size Boolean multiplication circuit can be closed with
the public output bits of \(N\) pinned and represented as a constant-arity
\({0,1}\)-tensor network.  Given the \(n\)-bit strings \(x,y\), every
partial product, sum bit, and carry is the output of a deterministic Boolean
gate.  Copy constraints also have a unique consistent assignment.  Thus:

1. every satisfying assignment gives one ordered pair of nonnegative
   integers with \(xy=N\);
2. every ordered positive divisor pair \((x,N/x)\) supplies exactly one
   satisfying internal assignment; and
3. leading zeroes are fixed positions in one \(n\)-bit encoding, not multiple
   encodings of an integer.

Since \(N>0\), zero cannot occur in a witness.  Therefore the unpinned count is
exactly \(\tau(N)\), and every prefix count is the number of divisors whose
unique \(n\)-bit encoding extends that prefix.

### 1.2 Subtracting the trivial witnesses is exact

For a prefix \(P\), define

\[
 Z_*(P)=Z(P)
 -\mathbf1_{\{1\text{ extends }P\}}
 -\mathbf1_{\{N\text{ extends }P\}}.
\]

Both indicators are public and obey the same binary partition identity as the
witness count.  Hence

\[
 Z_*(P)=Z_*(P0)+Z_*(P1)
\]

exactly, and \(Z_*(P)\ge0\) for every prefix.  If \(N\) is composite, then
\(\tau(N)-2>0\), including when \(N\) is a prime power or a square.  Choosing
a positive child at every level therefore reaches a unique \(n\)-bit integer
\(x\) with \(1<x<N\) and \(x\mid N\).  Exact division checks the result and
gives the complementary factor.

The self-reduction needs at most two exact pinned contractions per bit; it
does not assume that one unpinned scalar count exposes a witness.  Prefix
pinning is therefore an essential part of the conditional hypothesis.

### 1.3 Complete factorization and bit complexity

Run a deterministic polynomial-time primality test before attempting a split
at each recursion node.  A composite node is split by the preceding
self-reduction, and its two strictly smaller verified factors are recursed
upon.  If prime factors are counted with multiplicity, their number is at
most \(\log_2N\); consequently the binary factorization tree has
\(O(n)\) nodes.

At a node of bit length \(m\le n\), the network has polynomial size and the
conditional contraction routine is assumed uniform polynomial time in
\(m\).  There are \(O(m)\) pinned calls at that node and \(O(n)\) nodes, so a
fixed \(O(m^c)\) contraction bound gives, for example,
\(O(n^{c+2})\) total contraction time, plus polynomial-time primality,
subtraction, comparison, exact division, and output handling.

The candidate's \(2n+1\)-bit bound on counts is safe: there are at most
\(2^{2n}\) assignments to \((x,y)\), and deterministic internal wires add no
multiplicity.  In fact the closed multiplication count is only
\(\tau(N)\le N\), but the weaker bound suffices.

This is a deterministic conditional reduction, stronger than the requested
Las Vegas conclusion.  Its factor extraction uses no terminal gcd.  The
sentence “does not use a gcd” should be understood as referring to the
self-reduction; if it is intended to forbid even internal gcd arithmetic in a
chosen primality implementation, that stronger claim should either be
withdrawn or an explicitly gcd-free implementation should be named.  Nothing
in the research claim requires that stronger prohibition.

## 2. Matchgate source statement

The Bravyi paper defines matchgate tensors by the quadratic identities in
equation (1), then states explicitly that a tensor of rank/arity \(1,2,\) or
\(3\) is a matchgate if and only if it is even or odd.  Its footnote defines
“even” as vanishing on odd Hamming weights and “odd” as vanishing on even
Hamming weights.  Thus the candidate uses an accurate necessary condition;
for arity three it is also sufficient.  The audit needs only necessity.

The paper also makes clear that planar matchgate contraction is the
FKT/Pfaffian regime, while nonplanar cost depends on topology.  It does not
justify ignoring crossings or genus.  The candidate correctly leaves those
issues open.

## 3. COPY\(_3\) basis classification

Let

\[
 T=\begin{pmatrix}a&b\\c&d\end{pmatrix},
 \qquad
 T^{\otimes3}E=u^{\otimes3}+v^{\otimes3},
 \qquad
 u=(a,c)^{\mathsf T},\ v=(b,d)^{\mathsf T}.
\]

Because the tensor is symmetric, one equation represents every component of a
fixed weight.

### 3.1 Even COPY

Even parity requires the weight-one and weight-three components to vanish:

\[
 a^2c+b^2d=0,
 \qquad c^3+d^3=0.
\]

The zero-coordinate cases do not yield an invertible exception.  If \(c=0\),
the second equation gives \(d=0\), making the second row zero.  If \(a=0\),
invertibility initially forces \(b,c\ne0\); the first equation gives \(d=0\)
and the second then gives \(c=0\), a contradiction.

Hence \(a,c\ne0\).  With \(\rho=d/c\) and \(t=b/a\),

\[
 \rho^3=-1,
 \qquad t^2=-\rho^{-1}=\rho^2.
\]

Over \(\mathbb C\), \(t=\pm\rho\).  The choice \(t=\rho\) makes the two
columns proportional, so invertibility forces \(t=-\rho\).  Therefore

\[
 T=\operatorname{diag}(a,c)
 \begin{pmatrix}1&-\rho\\1&\rho\end{pmatrix},
 \qquad \rho^3=-1.
\]

Conversely this form has all odd-weight entries zero and nonzero determinant,
so the classification is exact.

### 3.2 Odd COPY

Odd parity requires weights zero and two to vanish:

\[
 a^3+b^3=0,
 \qquad ac^2+bd^2=0.
\]

Again \(a,c\ne0\): \(a=0\) forces \(b=0\), while \(c=0\), together with
invertibility, makes the second equation force \(b=0\) and the first force
\(a=0\).  The same normalization now gives

\[
 T=\operatorname{diag}(a,c)
 \begin{pmatrix}1&\rho\\1&-\rho\end{pmatrix},
 \qquad \rho^3=-1.
\]

Thus Section 4's two normal forms and its exclusion of zero coordinates are
correct.

## 4. The mandatory transpose correction

### 4.1 Why \(T^{-1}\) is wrong here

Consider one ordinary contracted edge with endpoint vectors \(f,g\), paired
by

\[
 \langle f,g\rangle=f^{\mathsf T}g.
\]

If the first endpoint is transformed to \(Tf\), the second must be transformed
to \(Sg\) with

\[
 (Tf)^{\mathsf T}(Sg)
 =f^{\mathsf T}T^{\mathsf T}Sg
 =f^{\mathsf T}g
\]

for all \(f,g\).  Therefore

\[
 S=(T^{\mathsf T})^{-1}=(T^{-1})^{\mathsf T}.
 \tag{4.1}
\]

Using \(S=T^{-1}\) instead would require
\(T^{\mathsf T}T^{-1}=I\), which is false for a general classified basis.
This is not repaired by replacing \(T\) by \(T^{-1}\): inverse and
inverse-transpose are different operations.

One may equivalently call one endpoint a covector and write a right action by
\(T^{-1}\).  Once both signatures are represented as column component arrays,
as they are in equations (3.1)--(4.4), that right action is represented by
\((T^{-1})^{\mathsf T}\), not by \(T^{-1}\).

### 4.2 Corrected column-ratio lemma

Set \(S=(T^{-1})^{\mathsf T}\).

For the even-COPY normal form,

\[
 T=\begin{pmatrix}a&-a\rho\\c&c\rho\end{pmatrix},
\]

direct inversion gives

\[
 Se_0=
 \begin{pmatrix}(2a)^{-1}\\(2c)^{-1}\end{pmatrix},
 \qquad
 Se_1=
 \begin{pmatrix}-(2\rho a)^{-1}\\(2\rho c)^{-1}\end{pmatrix}.
\]

Both coordinates of \(Se_0\) are nonzero.  At transformed coordinate
\(b\in\{0,1\}\),

\[
 \frac{(Se_1)_b}{(Se_0)_b}
 =r(-1)^b,
 \qquad r=-\rho^{-1}\ne0.
 \tag{4.2}
\]

For the odd-COPY normal form,

\[
 T=\begin{pmatrix}a&a\rho\\c&-c\rho\end{pmatrix},
\]

one obtains

\[
 Se_0=
 \begin{pmatrix}(2a)^{-1}\\(2c)^{-1}\end{pmatrix},
 \qquad
 Se_1=
 \begin{pmatrix}(2\rho a)^{-1}\\-(2\rho c)^{-1}\end{pmatrix},
\]

and hence

\[
 \frac{(Se_1)_b}{(Se_0)_b}
 =r(-1)^b,
 \qquad r=\rho^{-1}\ne0.
 \tag{4.3}
\]

Equations (4.2)--(4.3), rather than candidate equation (4.4), are the needed
input statement for the AND proof.  They are actually simpler: the row
scalings \(a,c\) cancel.

On the AND-output edge, \(S_3=(T_3^{-1})^{\mathsf T}\) is still a completely
arbitrary invertible matrix because \(T_3\mapsto S_3\) is a bijection of
\(\operatorname{GL}_2(\mathbb C)\).  Thus writing
\(u=S_3e_0\) and \(v=S_3e_1\) loses no generality.

## 5. Re-audit of the AND contradiction after correction

Let \(S_j=(T_j^{-1})^{\mathsf T}\) on the two factor-input edges, and let
\(r_j\ne0\) be supplied by (4.2) or (4.3).  Fix transformed bits
\(b_1,b_2\) and put

\[
 s=(-1)^{b_1},\quad t=(-1)^{b_2},
 \quad x=r_1,\quad y=r_2.
\]

After dividing by the nonzero original-zero coordinate factors, the AND
output slice is exactly

\[
 W_{s,t}=u(1+xs+yt)+vxy\,st.
 \tag{5.1}
\]

The thin space in \(xy\,st\) above denotes ordinary multiplication; equivalently
the last term is \(vxy st\).  No COPY parity, cube-root choice, or row scaling
has been dropped: all of them are absorbed into the nonzero \(x,y\).

If the transformed AND tensor were even, its output-zero components with
\(b_1+b_2\) odd would give

\[
 u_0(1-x+y)-v_0xy=0,
 \qquad
 u_0(1+x-y)-v_0xy=0,
 \tag{5.2}
\]

while its output-one components with \(b_1+b_2\) even would give

\[
 u_1(1+x+y)+v_1xy=0,
 \qquad
 u_1(1-x-y)+v_1xy=0.
 \tag{5.3}
\]

If \(u_0=0\), invertibility of the two-column matrix \((u,v)\) forces
\(v_0\ne0\), so (5.2) forces \(xy=0\), impossible.  The same argument with
(5.3) excludes \(u_1=0\).  Subtracting the two equations in (5.2) gives
\(x=y\); subtracting those in (5.3) gives \(x=-y\).  Characteristic zero and
\(x,y\ne0\) yield a contradiction.

If the transformed AND tensor were odd, the even-total-weight components give

\[
 u_0(1+x+y)+v_0xy=0,
 \qquad
 u_0(1-x-y)+v_0xy=0,
 \tag{5.4}
\]

and

\[
 u_1(1-x+y)-v_1xy=0,
 \qquad
 u_1(1+x-y)-v_1xy=0.
 \tag{5.5}
\]

The identical zero-coordinate argument applies.  Subtraction in (5.4) gives
\(x=-y\), while subtraction in (5.5) gives \(x=y\), again impossible.

Therefore the corrected contraction-preserving transform cannot make AND
either even or odd.  By the arity-three matchgate criterion it cannot make AND
a matchgate.  This conclusion permits:

1. independent bases on the two copied factor-input roles;
2. either parity for each transformed COPY tensor;
3. every cube root \(\rho_j^3=-1\);
4. all nonzero basis scalings; and
5. a completely arbitrary invertible output-edge basis.

The central local obstruction is therefore true after the transpose
correction.

## 6. Network, pin, and topology scope

### 6.1 What the local theorem does prove

The corrected theorem rules out a contraction-preserving common-basis scheme
whenever a ternary COPY tensor on one side of a bipartite signature graph is
directly paired with an AND tensor on the other side on each factor-input
role.  Since the AND output basis was arbitrary, no assumption about the
neighboring partial-product consumer is needed for this local contradiction.
Full adders need not be tested in that named realization.

Prefix pins do not rescue the unpinned local pair.  Conversely, a proposed
pinned matchgate algorithm would also have to show that transformed boundary
pin tensors or their absorbed versions remain matchgate-realizable.  The
candidate makes no unsupported claim that this is automatic; its conditional
factoring premise explicitly asks for every pinned network.

### 6.2 Fanout-tree wording needs tightening

A tree made from ternary COPY tensors has COPY--COPY internal edges.  It is
not enough to say only that “the fanout trees contain ternary copy nodes” and
then assign \(T\) to every COPY and \(T^{-1}\) to every other constraint:
opposite endpoints of every ordinary edge must receive transpose-dual
actions.  In a bipartite realization, COPY nodes at alternating depths receive
opposite dual actions.  The local theorem still applies if the realization is
chosen so that every leaf COPY adjacent to an AND lies in the COPY
bipartition, but this construction/orientation should be stated explicitly.

Alternatively, if one retains one high-arity equality tensor for each factor
bit, the present arity-three classification by itself is not a proof about
that high-arity tensor.  A separate high-arity matchgate analysis would be
needed.  Likewise, placing COPY and AND on the same bipartition with an
intervening equality signature is not literally the local scheme proved
here.

Accordingly the global conclusion should be phrased as a no-go for the
explicit direct-adjacency bipartite ternary realization, not for every
possible way of representing fanout.  This is consistent with the candidate's
existing list of open fused cells, edge-dependent gauges, and alternative gate
sets, but the current Section 6 should make the realization exact.

### 6.3 Planarity and FKT

The local incompatibility occurs before planarity matters.  It proves neither
that a multiplier incidence graph is nonplanar nor that crossings cannot be
realized by matchgate gadgets.  Even if every local tensor were a matchgate,
an FKT conclusion would still require a planar embedding with compatible
cyclic index orders, or a separately bounded topological overhead.

The candidate correctly does not claim any of:

- a tensor-contraction hardness theorem;
- a lower bound against fused or larger signatures;
- an obstruction to edge-dependent gauges;
- an obstruction to another Pfaffian/sub-Pfaffian identity;
- a bound against non-Pfaffian exact contraction; or
- a polynomial contraction for a generic nonplanar multiplier.

The final sentence “does not acquire an FKT/Pfaffian contraction through that
transformation” is sound only after “that transformation” is corrected to the
transpose-dual action and tied to the explicit local direct-adjacency
realization.

## 7. Exact-arithmetic complexity scope

For a polynomial-size planar matchgate network over exact rational or
efficiently represented algebraic weights, a polynomial-size Pfaffian gives
polynomially many field operations.  A bit-complexity conclusion additionally
needs polynomial degree/representation size for the common field and
polynomial growth of numerators, denominators, or algebraic-coordinate
heights.  The candidate states these conditions rather than assuming them, so
it does not inflate arithmetic-operation count into bit complexity.

The local obstruction itself is fixed-size algebra and makes no factoring
algorithm.  The conditional count-to-factor reduction has polynomial bit
complexity for every input only because its hypothesis postulates a uniform
polynomial-bit contraction algorithm for all pinned instances.  This
conditional statement does not meet the top-level PROMPT success criterion,
and the candidate correctly says so.

## 8. Hostile counterexample checks

The following possible escapes were tested symbolically against the exact
claim:

1. **Zero coordinates in the COPY basis.**  They force singularity or
   contradiction; no basis is missed.
2. **Different COPY parities.**  Both even and odd normal forms give the
   alternating ratio under the correct dual transform.
3. **Different cube roots and scalings.**  The AND contradiction requires
   only \(x,y\ne0\), so all survive the reduction.
4. **Independent factor-role bases.**  Section 5 never equates the two bases;
   it permits independent \(x,y\).
5. **Arbitrary AND-output basis.**  The proof uses only linear independence of
   \(u,v\), including all cases where one coordinate of \(u\) is zero.
6. **Switching AND parity.**  Both parity systems are inconsistent.
7. **Pins.**  Pinning is required by the conditional decoder but cannot repair
   the already non-matchgate unpinned local AND; transformed pins may create
   additional obstructions.
8. **Crossings or nonplanarity.**  They are not used in the local proof and are
   not claimed to be solved.
9. **Avoiding explicit COPY.**  A high-arity equality, fused multiplier cell,
   different fanout realization, or edge-dependent gauge is outside the exact
   local theorem and remains a valid reopen direction.

No counterexample to the corrected local algebra was found.

## 9. Required corrections before re-audit

The next candidate version should make all of the following exact:

1. Replace equation (3.2) by

   \[
   A'=
   ((T_1^{-1})^{\mathsf T}
   \otimes(T_2^{-1})^{\mathsf T}
   \otimes(T_3^{-1})^{\mathsf T})A
   \]

   when COPY endpoints are transformed by \(T_j\).
2. Replace candidate equation (4.4) by the coordinate-ratio lemma
   (4.2)--(4.3) above.  Do not retain the false inverse-column
   parametrization.
3. Define \(u,v\) as the columns of the correct dual output matrix.  Note that
   this matrix remains arbitrary invertible.
4. Replace the “opposite convention = replace by inverse” sentence by the
   correct transpose-dual statement.
5. State a concrete bipartite ternary fanout realization in which the COPY
   node used by the local proof is directly opposite the AND node, or narrow
   the network verdict explicitly to such a local realization.  Do not infer
   the claim for an unanalysed high-arity equality or for COPY--COPY edges
   receiving the same action.
6. Prefer “factor extraction uses no terminal gcd” over an unqualified claim
   that every invoked subroutine is gcd-free.

After items 1--5, the displayed parity proof establishes the stated narrow
obstruction.  Item 6 is a scope clarification.

## Final verdict

**PASS WITH CORRECTIONS.**

The conditional all-input count-to-factor reduction is correct, the cited
arity-three matchgate criterion is accurate, the COPY normal forms are
complete, and the AND parity obstruction survives the proper holographic
dual action.  The current version's use of \(T^{-1}\) instead of
\((T^{-1})^{\mathsf T}\) is nevertheless a substantive mathematical error,
and its fanout-tree/global-basis wording must be made explicit.  The corrected
artifact requires a fresh hostile re-audit before this audit stage can count
as passed.  Even after that, the result remains a narrow method failure and
not a top-level factoring algorithm.
