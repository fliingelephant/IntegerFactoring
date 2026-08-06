# Fresh hostile re-audit of corrected F26 — holographic factor-witness contraction

**Audited family:** F20.

**Audited artifact:** `experiments/F26_holographic_factor_network/RESULT.md`,
after its substantive transpose-dual and fanout correction.

**Prior audit consulted:** `experiments/F26_holographic_factor_network_audit/RESULT.md`.
Its verdict was not assumed; every mathematical step below was rederived from
the corrected artifact.

**Method:** symbolic hostile audit. No computation was run.

**Sources read in full:** `PROMPT.md`, the corrected candidate, and the first
hostile audit. The cited primary source, Sergey Bravyi,
[*Contraction of matchgate tensor networks on non-planar
graphs*](https://arxiv.org/abs/0801.2989), was checked for the rank-at-most-three
matchgate criterion and the topology scope.

## Executive verdict

**PASS.**

The corrected candidate is sound in its stated narrow scope.

1. The ordinary-contraction action is exactly transpose-dual:
   \(S=(T^{-1})^{\mathsf T}\). Both COPY parity normal forms give the claimed
   alternating nonzero coordinate ratio under this action.
2. The transformed AND slice and all eight parity equations are correct.
   Every possible zero coordinate of \(u\) is explicitly contradictory, and
   the remaining equations force simultaneously \(x=y\) and \(x=-y\).
3. The complete ternary fanout construction supplies a literal bipartite
   leaf-COPY-to-AND pair. Root and padding unaries, a dummy depth, and binary
   equality subdivisions all preserve every witness with weight one and add
   no multiplicity.
4. Exact prefix-pinned witness counts conditionally give a deterministic,
   all-input polynomial-bit factoring algorithm. Prime powers, repeated
   factors, unbalanced composites, even inputs, prime leaves, recursion,
   verification, and aggregation of repeated prime leaves are covered.
5. The conclusion is only a method failure for one common-role-basis,
   separated COPY\(_3\)--AND\(_3\) realization. The candidate correctly leaves
   high-arity equality, fused cells, edge-dependent gauges, other gate sets,
   other Pfaffian identities, and non-Pfaffian contractions open. Its claim is
   only that factor extraction needs no terminal factor-extracting gcd.

This result is not a factoring algorithm and does not meet the top-level
success criterion in `PROMPT.md`. It certifies one local obstruction and one
conditional count-to-factor reduction.

## 1. Ordinary contraction forces the transpose-dual action

For one contracted binary edge, write the endpoint component columns as
\(f,g\in\mathbb C^2\). Their contraction is \(f^{\mathsf T}g\). If the first
endpoint receives \(T\) and the second receives \(S\), preservation for all
\(f,g\) requires

\[
  (Tf)^{\mathsf T}(Sg)
  =
  f^{\mathsf T}T^{\mathsf T}Sg
  =
  f^{\mathsf T}g.
\]

Therefore

\[
  T^{\mathsf T}S=I,
  \qquad
  S=(T^{\mathsf T})^{-1}=(T^{-1})^{\mathsf T}.
  \tag{1.1}
\]

This applies independently on every leg. Hence, when a COPY endpoint receives
\(T_j\), the adjacent AND endpoint receives
\(S_j=(T_j^{-1})^{\mathsf T}\), and the corrected equation

\[
  A'=(S_1\otimes S_2\otimes S_3)A
\]

is contraction-preserving. The transpose cannot generally be omitted.

## 2. Independent reconstruction of the COPY classification

Let

\[
  E=e_0^{\otimes3}+e_1^{\otimes3},
  \qquad
  T=
  \begin{pmatrix}a&b\\c&d\end{pmatrix}.
\]

Then

\[
  T^{\otimes3}E
  =
  (a,c)^{\mathsf T\otimes3}
  +(b,d)^{\mathsf T\otimes3}.
\]

Because this tensor is symmetric, one equation represents each Hamming
weight.

### 2.1 Even COPY

Even parity requires its weight-one and weight-three components to vanish:

\[
  a^2c+b^2d=0,
  \qquad
  c^3+d^3=0.
  \tag{2.1}
\]

There is no invertible zero-coordinate escape. If \(c=0\), then \(d=0\), so
the second row vanishes. If \(a=0\), invertibility first gives \(b,c\ne0\);
the first equation then gives \(d=0\), and the second gives \(c=0\), a
contradiction. Thus \(a,c\ne0\).

Put \(\rho=d/c\) and \(t=b/a\). Equation (2.1) gives

\[
  \rho^3=-1,
  \qquad
  t^2=-\rho^{-1}=\rho^2.
\]

Thus \(t=\pm\rho\). The choice \(t=\rho\) makes the two columns proportional,
so invertibility forces \(t=-\rho\). Exactly the even solutions are

\[
  T=
  \operatorname{diag}(a,c)
  \begin{pmatrix}1&-\rho\\1&\rho\end{pmatrix},
  \qquad
  ac\rho\ne0,
  \quad \rho^3=-1.
  \tag{2.2}
\]

### 2.2 Odd COPY

Odd parity requires the weight-zero and weight-two components to vanish:

\[
  a^3+b^3=0,
  \qquad
  ac^2+bd^2=0.
  \tag{2.3}
\]

Again \(a,c\ne0\). If \(a=0\), then \(b=0\); if \(c=0\), invertibility gives
\(a,d\ne0\), after which the second equation gives \(b=0\) and the first
gives \(a=0\), a contradiction.

With \(t=b/a\) and \(q=d/c\), (2.3) says
\(t^3=-1\) and \(q^2=t^2\). The choice \(q=t\) is singular, so \(q=-t\).
Writing \(\rho=t\), exactly the odd solutions are

\[
  T=
  \operatorname{diag}(a,c)
  \begin{pmatrix}1&\rho\\1&-\rho\end{pmatrix},
  \qquad
  ac\rho\ne0,
  \quad \rho^3=-1.
  \tag{2.4}
\]

### 2.3 Correct dual columns

For the even form (2.2), direct inversion and transposition give

\[
  Se_0=
  \begin{pmatrix}(2a)^{-1}\\(2c)^{-1}\end{pmatrix},
  \qquad
  Se_1=
  \begin{pmatrix}-(2\rho a)^{-1}\\(2\rho c)^{-1}\end{pmatrix}.
  \tag{2.5}
\]

For the odd form (2.4), they give

\[
  Se_0=
  \begin{pmatrix}(2a)^{-1}\\(2c)^{-1}\end{pmatrix},
  \qquad
  Se_1=
  \begin{pmatrix}(2\rho a)^{-1}\\-(2\rho c)^{-1}\end{pmatrix}.
  \tag{2.6}
\]

Thus in both cases there are nonzero \(\lambda_0,\lambda_1,r\) with

\[
  Se_0=
  \begin{pmatrix}\lambda_0\\\lambda_1\end{pmatrix},
  \qquad
  Se_1=
  r\begin{pmatrix}\lambda_0\\-\lambda_1\end{pmatrix};
\]

\(r=-\rho^{-1}\) in the even case and \(r=\rho^{-1}\) in the odd case.
At transformed coordinate \(b\), the original-one/original-zero ratio is
exactly

\[
  \frac{(Se_1)_b}{(Se_0)_b}=r(-1)^b,
  \qquad r\ne0.
  \tag{2.7}
\]

This independently confirms every formula used by the corrected AND proof.

## 3. Complete hostile check of the AND parity equations

The AND relation is

\[
  A
  =
  e_0e_0e_0+e_0e_1e_0+e_1e_0e_0+e_1e_1e_1,
\]

where juxtaposition denotes tensor product. For the two copied input roles,
let (2.7) supply independent \(x=r_1\ne0\) and \(y=r_2\ne0\). At transformed
input coordinates \(b_1,b_2\), put

\[
  s=(-1)^{b_1},
  \qquad
  t=(-1)^{b_2}.
\]

After factoring out the two nonzero \(e_0\)-column coordinates, the four AND
terms give, respectively,

\[
  u,\qquad yt\,u,\qquad xs\,u,\qquad xy\,st\,v,
\]

where \(u=S_3e_0\), \(v=S_3e_1\). Since \(S_3\) is arbitrary invertible,
\(u,v\) are arbitrary linearly independent columns. Therefore the output
slice is exactly

\[
  W_{s,t}=u(1+xs+yt)+vxy\,st.
  \tag{3.1}
\]

No scaling, COPY parity, or cube-root choice is omitted.

### 3.1 Even parity is impossible

If \(A'\) were even, its odd-total-weight entries would vanish. For output
coordinate zero and \(b_1+b_2\) odd, (3.1) gives

\[
  u_0(1-x+y)-v_0xy=0,
  \qquad
  u_0(1+x-y)-v_0xy=0.
  \tag{3.2}
\]

For output coordinate one and \(b_1+b_2\) even, it gives

\[
  u_1(1+x+y)+v_1xy=0,
  \qquad
  u_1(1-x-y)+v_1xy=0.
  \tag{3.3}
\]

All zero-coordinate cases are covered. If \(u_0=0\), linear independence
forces \(v_0\ne0\), and either equation (3.2) forces \(xy=0\). If \(u_1=0\),
the same argument in (3.3) forces \(xy=0\). Hence \(u_0u_1\ne0\).

Subtracting the two equations in (3.2) now gives \(x=y\); subtracting those
in (3.3) gives \(x=-y\). Over \(\mathbb C\), these imply \(x=y=0\), contrary
to (2.7). Values \(v_0=0\) or \(v_1=0\) create no further case because the
subtractions do not divide by either coordinate of \(v\).

### 3.2 Odd parity is impossible

If \(A'\) were odd, its even-total-weight entries would vanish. For output
coordinate zero and \(b_1+b_2\) even,

\[
  u_0(1+x+y)+v_0xy=0,
  \qquad
  u_0(1-x-y)+v_0xy=0.
  \tag{3.4}
\]

For output coordinate one and \(b_1+b_2\) odd,

\[
  u_1(1-x+y)-v_1xy=0,
  \qquad
  u_1(1+x-y)-v_1xy=0.
  \tag{3.5}
\]

The identical zero-coordinate argument forces \(u_0u_1\ne0\). Subtracting
(3.4) gives \(x=-y\), while subtracting (3.5) gives \(x=y\), again impossible
for nonzero \(x,y\).

The eight components required by the two parity hypotheses have therefore
all been checked. The transformed AND is neither even nor odd. Bravyi's
rank-at-most-three criterion states that a ternary tensor is a matchgate if
and only if it is parity-pure, so the AND tensor is not a matchgate.

## 4. The explicit fanout realization is literal and count-preserving

This was the other substantive issue in the first audit. The corrected
construction resolves it.

### 4.1 Ternary tree and neutral legs

For one factor bit with \(m\) uses, take a rooted complete binary tree whose
vertices are ternary equality tensors

\[
  E_{abc}=\mathbf1_{{a=b=c}}.
\]

Regard one leg of each vertex as its parent leg and two as child legs. Attach
the spare parent leg of the root to the unary all-ones tensor
\(\mathbf1=(1,1)\). Choose a depth with at least \(m\) dangling child legs,
connect \(m\) of them directly to the required AND inputs, and attach every
unused child leg to another copy of \(\mathbf1\).

For any assignment of the used legs, the tree contributes zero unless all
used values agree. If they agree, every internal edge, spare root index, and
unused child index is uniquely forced to that common bit. Every all-ones
unary then contributes the scalar one. Thus the tree realizes one free
Boolean variable copied to all (m) uses, with exactly one internal
extension per value. In particular, neither the root unary nor unused padding
legs introduce a factor of two.

### 4.2 Dummy depth

If a leaf-depth parity must be flipped, add one complete vertex level. On
each formerly dangling child leg, insert a new ternary equality vertex,
reconnect the formerly used external edge to one child leg, and terminate the
other child leg with (\mathbf1). Formerly unused legs may instead terminate
both new child legs with (\mathbf1).

Given the parent value, both new child values are uniquely forced and all
new unary weights equal one. Hence a dummy level preserves the relation and
the exact witness count while flipping the bipartition color of every leaf
COPY vertex. Applying this where necessary puts all leaf COPY vertices for
both factor-input roles on one chosen side.

### 4.3 Bipartition and equality subdivisions

Color those leaf COPY vertices left and every adjacent AND right. Tree
vertices alternate colors by depth. Give every remaining old tensor an
arbitrary provisional color. Whenever an old edge has endpoints of the same
color, replace it by a two-edge path through the binary equality
(\Delta_{ij}=\mathbf1_{{i=j}}), colored oppositely. Edges with opposite
endpoint colors remain unchanged. The resulting graph is bipartite.

The replacement preserves contraction exactly:

\[
  \sum_i F_iG_i
  =
  \sum_{i,j}F_i\Delta_{ij}G_j.
  \tag{4.1}
\]

It also preserves Boolean witnesses one-for-one because the inserted index is
uniquely equal to the old wire value. Thus the bipartization introduces no
extra satisfying assignments.

### 4.4 The local obstruction now applies without a global inference

Under a common basis for one copied role, every leg incident to a chosen leaf
COPY receives the same \(T_j\): its parent leg and its used or neutral child
legs all carry that same Boolean role. Every opposite endpoint receives
\(S_j=(T_j^{-1})^{\mathsf T}\). In particular, each AND factor input is
directly opposite a leaf COPY and receives the dual action used in Section 3.

Suppose all local tensors in this explicit realization became matchgates.
Each of the two leaf COPY tensors neighboring any AND would then be
parity-pure, so Section 2 classifies its common role basis. Section 3 then
proves that the same AND cannot be a matchgate, a contradiction.

Nothing about internal COPY tensors, root or padding unaries, inserted binary
equalities, adders, planarity, or crossings is needed for this implication.
Those tensors could only add further obstructions. The argument uses the
literal directly adjacent pair and no unsupported high-arity inference.

## 5. Conditional exact-count reduction covers every input

### 5.1 Exact witness multiplicity

For an \(m\)-bit integer \(M>1\), use \(m\)-bit inputs \(x,y\), a deterministic
Boolean multiplication circuit, and pin all \(2m\) product bits to the binary
encoding of \(M\), including leading zeroes. Given \(x,y\), every partial
product, sum bit, carry, copy-tree index, and inserted equality index is
uniquely determined. Conversely, every satisfying assignment has \(xy=M\).
Since \(M>0\), neither input is zero.

Therefore there is exactly one witness for each ordered positive divisor
pair \((x,M/x)\), and the unpinned count is \(\tau(M)\). Prefix pins on the
\(x\)-encoding retain exactly the divisors extending that prefix. Leading
zeroes are fixed bit positions and create no duplicate encoding.

### 5.2 Self-reduction after removing the two public witnesses

For a prefix \(P\), let \(Z(P)\) be the exact pinned count and define

\[
  Z_*(P)
  =
  Z(P)
  -\mathbf1_{{1\text{ extends }P}}
  -\mathbf1_{{M\text{ extends }P}}.
  \tag{5.1}
\]

The subtracted indicators refer to two actual distinct witnesses because
\(M>1\). Hence \(Z_*(P)\ge0\), and both the witness sets and the two
indicators partition by the next bit:

\[
  Z_*(P)=Z_*(P0)+Z_*(P1).
  \tag{5.2}
\]

If \(M\) is composite, \(\tau(M)-2>0\). This remains true for squares and
prime powers. Starting at the empty prefix and repeatedly choosing a child
with positive adjusted count reaches after \(m\) bits an integer

\[
  1<x<M,
  \qquad
  x\mid M.
\]

No distributional, independence, or smoothness assumption occurs. Exact
integer division verifies the divisor and returns \(M/x\). The bit string
\(x\) itself is the factor; there is no terminal factor-extracting gcd.

### 5.3 Prime, repeated, unbalanced, and even cases

Run a deterministic polynomial-time primality test before splitting a
recursion node. A prime input, including \(M=2\), is returned as a leaf and
never enters the positive-count search. A composite input always has a
nontrivial divisor, regardless of balance or parity. Prime powers are split
by the same count search, and repeated prime factors simply appear as
multiple recursion leaves.

Recursing on the two verified strict factors terminates because both are
smaller than the parent. Sort the prime leaves and aggregate equal values to
obtain distinct primes with their exponents. This covers arbitrary
composites, even inputs, prime powers, repeated factors, and unbalanced
factors.

### 5.4 Uniform bit complexity

Assume the conditional contraction algorithm is uniform and has a fixed
bound \(P(m)\le C(m+1)^c\) on the original and every prefix-pinned \(m\)-bit
network. At a node, at most two counts per one of \(m\) prefix bits suffice.
There are at most \(2m+1\) bits in a count: only \(2^{2m}\) input pairs exist,
and deterministic internal wires add no multiplicity.

The number of prime leaves with multiplicity is at most
\(\log_2M\le n\), so the binary recursion tree has \(O(n)\) nodes. Every node
has bit length at most \(n\). A deliberately loose uniform bound for all
contractions is therefore

\[
  O\bigl(n^2P(n)\bigr)=O(n^{c+2}).
\]

Deterministic primality testing, exact division, comparison, subtraction,
sorting, aggregation, and output all have polynomial bit complexity on
\(O(n)\)-bit integers and \(O(n)\) nodes. Thus the conditional algorithm is a
deterministic worst-case polynomial-time complete factorization algorithm,
which is stronger than the requested Las Vegas guarantee. The missing
ingredient is precisely the hypothesized exact pinned contraction routine.

## 6. Scope and attempted escapes

The following adversarial escapes were checked against the exact theorem:

1. **A zero entry in a COPY basis.** The parity equations force singularity;
   Sections 2.1--2.2 omit no invertible case.
2. **Different COPY parities or cube roots.** Both normal forms, every cube
   root of \(-1\), and every nonzero row scaling yield (2.7).
3. **Independent factor-role bases.** The AND proof treats \(x\) and \(y\)
   as unrelated nonzero complex numbers.
4. **An arbitrary output basis.** The proof assumes only that \(u,v\) are
   linearly independent; the dual-output map ranges over all invertible
   matrices.
5. **Zero coordinates in \(u\) or \(v\).** A zero coordinate in \(u\) forces
   \(xy=0\); zero coordinates in \(v\) do not affect the subtraction
   contradiction.
6. **Switching AND parity.** Both even and odd systems were checked
   separately.
7. **Padding or bipartization multiplicity.** Equality indices are uniquely
   forced and every all-ones unary contributes one.
8. **Prime powers, repeated factors, squares, even or unbalanced inputs.**
   None changes the positive adjusted divisor count or recursion proof.
9. **Pins.** Pins are explicitly part of the conditional contraction
   hypothesis. They do not repair the already non-matchgate unpinned local
   pair.
10. **Planarity or crossings.** The local contradiction occurs before either
    is used; no planar embedding is claimed.

The theorem does **not** cover, and the corrected candidate does not claim to
cover:

- high-arity equality without this ternary realization;
- fused multiplier cells;
- edge-dependent or vertex-dependent gauges;
- alternative Boolean gate sets or higher-domain encodings;
- Pfaffian or sub-Pfaffian identities not obtained by making these displayed
  local tensors matchgates;
- cancellations specialized to public output pins;
- bounded-genus constructions with proved polynomial overhead; or
- non-Pfaffian exact contractions exploiting multiplier structure.

It is also not a tensor-contraction lower bound and not evidence that factoring
requires a gcd.

## Final verdict

**PASS.**

The corrected F26 artifact has repaired both substantive defects identified
by the first hostile audit. The transpose-dual formulas, COPY classification,
AND contradiction, explicit direct-adjacency fanout realization, exact
witness preservation, conditional all-input factorization reduction, and
scope statements all withstand the fresh hostile check. The audit stage may
now count as passed for this corrected version.

The claim remains a narrow auxiliary method failure, not a solution to the
integer-factoring goal. It still requires the PROMPT-mandated independent
proof-blind reconstruction before it can become verifier-backed.
