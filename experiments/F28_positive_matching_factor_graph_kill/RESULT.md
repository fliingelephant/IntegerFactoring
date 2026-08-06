# F28 — positive perfect-matching factor graph: conditional sampler and local signature boundary

**Family:** F21.

**Status:** promoted as P38 after corrected hostile audits and a strict
proof-blind reconstruction.

**Classification:** evidence against the exact auxiliary mechanism consisting
of direct single-rail or exactly-one dual-rail positive perfect-matching
gadgets for COPY, AND, full addition, and the natural fused multiplier cell.
It is not a method failure for a closed multiplication-specific graph with a
global matching decoder.

**Computation:** none.  Every claim below is symbolic.

## Outcome

There are two sharply different results.

1. If a uniform factor-free polynomial-size bipartite graph has perfect
   matchings in an efficiently readable, equal-multiplicity correspondence
   with the ordered pairs \((x,y)\) satisfying \(xy=N\), then the
   Jerrum--Sinclair--Vigoda almost-uniform perfect-matching sampler gives a
   complete classical Las Vegas polynomial-bit factoring algorithm.  The
   worst uniform success probability is exactly \(1/3\), attained by a prime
   square.  Total-variation error \(1/12\) leaves success probability at least
   \(1/4\) per independent trial.  Verification and recursion require no
   terminal factor-extracting gcd.

2. An ordinary positive perfect-matching gadget is much more restrictive than
   an arbitrary Boolean tensor.  Its supported terminal-deletion sets have
   fixed parity, have fixed left-minus-right charge when the gadget is
   bipartite, and satisfy symmetric exchange; when the support is nonempty,
   they form an even matching delta-matroid.  Consequently, if an exact
   dual-rail gadget has nonempty support only on codewords selecting exactly
   one of two terminals for each logical bit, its logical relation must be a
   subcube.  Empty support is a separate realizable case.  COPY3, AND3, the
   full-adder relation, and the natural fused
   multiplication/addition cell are not subcubes.

The second result kills the direct local-gadget landing.  It does not constrain
the labels obtained by decoding internal edges of a closed graph, nor does it
exclude off-code support filtered by a global construction, assignment-dependent
auxiliary ports, larger block codes, or a multiplication-specific graph.

## 1. Closest prior route and material difference

The closest prior route is P36/F20.  There, exact contraction of every
prefix-pinned multiplication-witness tensor network would self-reduce to a
factor, while a common-basis ternary COPY--AND matchgate landing fails under
the required transpose-dual actions.

F21 is materially different in three ways.

* It asks for one ordinary nonnegative bipartite graph, not a basis change
  making a planar tensor network Pfaffian.
* It uses polynomial-time approximate sampling of perfect matchings, not exact
  contraction or exact prefix counts.
* It reads a divisor directly from a sampled matching.  Prefix pins and a
  terminal gcd are unnecessary.

The price is an exact positive encoding condition: trivial and nontrivial
factor witnesses must not be separated by cancellations, interpolation, or
uncontrolled matching multiplicities.

## 2. Exact conditional theorem

### 2.1 The graph hypothesis

Let

\[
  \mathcal W_N
  =
  \{(x,y)\in \mathbb Z_{>0}^2:xy=N\},
\]

so \(|\mathcal W_N|=\tau(N)\).  Assume there are uniform algorithms
\(\mathsf Build\) and \(\mathsf Decode\), and fixed polynomials bounding the
following operations for every \(N>1\) of bit length \(n\).

1. \(\mathsf Build(N)\) uses only public information computable from \(N\)
   and returns an unweighted bipartite graph
   \(G_N=(L_N,R_N,E_N)\) with
   \(|L_N|=|R_N|\le n^a\) for one fixed \(a\).  Its complete adjacency
   description has polynomial length and is built in polynomial bit time.
   In particular, the builder receives no factor, factor-dependent advice,
   order-finding oracle, or hidden splitting oracle.
2. Every perfect matching \(M\) of \(G_N\) is decoded in polynomial bit time
   to one member \(\mathsf Decode(N,M)\in\mathcal W_N\).
3. There is an integer \(c_N\ge1\), independent of the witness, such that

   \[
     |\{M: M\text{ is a perfect matching of }G_N,
          \mathsf Decode(N,M)=(x,y)\}|
     =c_N
   \]

   for every \((x,y)\in\mathcal W_N\).  Knowledge of \(c_N\) is not needed
   by the sampler, but the equal-multiplicity assertion must be a proved
   property of the public construction.

The graph is automatically nonempty: it has \(c_N\tau(N)\) perfect
matchings, including preimages of \((1,N)\) and \((N,1)\).

### 2.2 The sampling theorem and pushforward

Jerrum, Sinclair, and Vigoda construct a fully polynomial almost-uniform
sampler for perfect matchings of an arbitrary bipartite graph.  Given a graph
with at least one perfect matching and \(\delta\in(0,1]\), it returns an
actual perfect matching from a distribution \(\mu\) satisfying

\[
  d_{\mathrm{TV}}(\mu,U_G)\le\delta,
\]

where \(U_G\) is uniform on all perfect matchings.  Section 2.1, Figure 1,
Lemma 2, Theorem 4, and the end of Section 3 give the explicit FPAUS and a
number of transitions/arithmetic operations polynomial in the graph order
and \(\log \delta^{-1}\).  The primary preprint and journal article are:

Mark Jerrum, Alistair Sinclair, and Eric Vigoda,
[*A Polynomial-Time Approximation Algorithm for the Permanent of a Matrix
with Nonnegative Entries*](https://eccc.weizmann.ac.il/report/2000/079/),
ECCC TR00-079; J. ACM 51 (2004), 671--697.

The source presents the bound principally in transitions and arithmetic
operations.  The fair-random-bit Turing implementation needed here is given
explicitly in Section 2.4 below; its expected bit and random-bit cost is
polynomial.  A deterministic bipartite-matching algorithm may first find one
perfect matching and supplies the sampler's fallback matching.  On a
composite input the graph hypothesis proves that this search cannot fail.

Let \(D(M)=\mathsf Decode(N,M)\).  Total variation cannot increase under a
deterministic map:

\[
  d_{\mathrm{TV}}(D_*\mu,D_*U_G)\le\delta.
  \tag{2.1}
\]

Equal multiplicity makes \(D_*U_G\) exactly uniform on
\(\mathcal W_N\), since each ordered factor witness has \(c_N\) preimages.
For the event

\[
  A_N=\{(x,y)\in\mathcal W_N:1<x<N\},
\]

equation (2.1) therefore gives

\[
 \Pr_{M\sim\mu}[D(M)\in A_N]
 \ge
 \frac{\tau(N)-2}{\tau(N)}-\delta.
 \tag{2.2}
\]

Every composite has at least three positive divisors: \(1\), \(N\), and
one proper divisor.  Hence \(\tau(N)\ge3\), and

\[
  \frac{\tau(N)-2}{\tau(N)}\ge\frac13.
\]

This includes every exceptional-looking input class:

* for a square, the central ordered pair \((\sqrt N,\sqrt N)\) is counted
  once, exactly as one divisor;
* for \(N=p^e\), \(e\ge2\), success is
  \((e-1)/(e+1)\ge1/3\);
* repeated factors and arbitrarily unbalanced factors do not alter the divisor
  count argument; and
* even composites obey the same bound, with \(N=4\) again attaining
  \(1/3\).

Fix \(\delta=1/12\).  Every fresh sample then has success probability at
least

\[
  \frac13-\frac1{12}=\frac14.
  \tag{2.3}
\]

There is no accumulation of total-variation errors here.  Each invocation is
used only for the one event \(A_N\), for which (2.2) is a complete
per-invocation bound.  Independent fresh coins make the conditional success
probability after any history of rejections at least \(1/4\).

### 2.3 Las Vegas splitter

On an input integer \(M>1\):

1. Run a deterministic polynomial-time primality test.  If \(M\) is prime,
   return it as a leaf and do not invoke a perfect-matching sampler.
2. Build \(G_M\).  Deterministically find one perfect matching.  Under the
   hypothesis this succeeds because composite \(M\) has at least the three
   ordered divisor witnesses described above.
3. Invoke the almost-uniform sampler with \(\delta=1/12\), decode its actual
   perfect matching to \((x,y)\), and verify by ordinary integer arithmetic
   that

   \[
     x>0,\quad y>0,\quad xy=M.
   \]

4. If \(1<x<M\), return \(x\).  Otherwise reject the sample and repeat
   Step 3.

Every returned number is a verified nontrivial divisor.  An implementation may
also reject any malformed decoder output or failed product check; under the
graph hypothesis these extra checks never reject a valid perfect matching.
The two rejected valid witnesses are exactly \((1,M)\) and \((M,1)\).

By (2.3), if \(T_M\) is the number of samples at a composite node, then

\[
  \Pr[T_M>t]\le(3/4)^t,
  \qquad
  \mathbb E[T_M]\le4.
\]

Thus termination is almost sure.  The terminal operation is decoding followed
by exact multiplication/division verification; it is not a
factor-extracting gcd.

Recursively split the two verified factors, run deterministic primality
testing at every node, collect equal prime leaves into exponents, and verify
the powered product against the original input.  Prime powers, repeated
factors, even inputs, and unbalanced recursion branches are thereby handled
without promises.

### 2.4 Fair-random-bit implementation and total complexity

The JSV chain can be instantiated entirely with rational data.  Use the
permitted rational cooling ratio \(3/4\); when another such step would pass
the terminal activity \(1/m!\), set the last activity exactly to
\(1/m!\).  JSV changes one chosen non-edge activity in each phase.  There
are at most \(m^2\) non-edges, and one activity needs at most

\[
\left\lceil\log_{4/3}(m!)\right\rceil=O(m\log m)
\]

steps.  Hence the complete schedule has

\[
P\le m^2\left\lceil\log_{4/3}(m!)\right\rceil
=O(m^3\log m)
\tag{2.4}
\]

phases, not merely the phase count for one non-edge.  With at most
\(m^2\) empirical hole estimates per phase, the failure union bound covers
\(O(m^5\log m)\) estimates.  Let \(E\) be the event that at least one of
these estimates misses its promised multiplicative interval.  Choose the
per-estimate failure probabilities so that the union bound gives
\(\Pr(E)\le\delta/2\), and allocate the remaining \(\delta/2\) to mixing
and final sampling on \(E^c\).

Every activity is a ratio of integers with polynomial bit length.  On a
good empirical update, the hole weight is multiplied by a ratio of two
positive integer sample counts of polynomial size.  If either required count
is zero, retain the preceding positive rational weights and return the known
deterministic perfect matching through the sampler's bounded fallback branch.
Such a zero count is a detectable subevent of \(E\), because the corresponding
true sector has the positive inverse-polynomial stationary mass used by the
empirical-estimation guarantee.  Thus no division by zero and no zero-weight
Metropolis ratio occurs on any random-bit stream.

On \(E\) with all required counts positive, the algorithm may continue with
inaccurate weights, but every stored weight remains a positive rational and
the bounded sampler still returns an actual perfect matching.  Hence the
entire algorithm is defined on every random-bit stream, and its arbitrary
conditional output law on the full event \(E\) contributes at most
\(\Pr(E)\le\delta/2\) to total variation.  On \(E^c\), every empirical
refinement has the required accuracy, the cooling invariant holds at every
phase, and the JSV mixing/final-sampling proof contributes at most the other
\(\delta/2\).  Convexity of total variation gives total error at most
\(\delta\).  No algorithmic test for a positive but inaccurate estimate is
needed.

Across \(P\) updates, unreduced rational numerator and denominator lengths
grow by at most \(O(P\log S)\), where \(S\) is the polynomial sample count
per estimate.  This remains polynomial; fraction-normalizing gcds are not
needed because cross-multiplication suffices.  Thus every Metropolis
acceptance probability and every proposal probability is an exactly
represented positive rational \(a/b\) with
\(\log b=\operatorname{poly}(m,\log\delta^{-1})\).

If \(a=0\) or \(a=b\), reject or accept deterministically with zero random
bits.  For \(0<a<b\), an exact rational coin of bias \(a/b\) uses fair
bits as follows.  Put
\(s=\lceil\log_2 b\rceil\), draw \(s\) fair bits as an integer
\(U\in\{0,\ldots,2^s-1\}\), reject and redraw if \(U\ge b\), and accept
iff \(U<a\).  A round survives with probability
\(b/2^s>1/2\), so the number of rounds has expectation less than two and is
finite almost surely.  The expected fair-bit cost is less than \(2s\), and
the exact comparisons have bit cost polynomial in \(\log b\).  Uniform
finite proposals use the same rejection construction.  Consequently every
specified JSV transition is simulated exactly, the total-variation theorem
is unchanged, and a complete sampler invocation has almost-sure termination
and expected bit and fair-random-bit cost

\[
R_{\rm exp}(m,\ell)
=\operatorname{poly}(m,\ell),
\qquad
\ell=\lceil\log_2\delta^{-1}\rceil.
\tag{2.5}
\]

This is an expected bound, not an unsupported worst-case cap on fair random
bits.  At \(\delta=1/12\), \(\ell=4\) is constant.

Use an independent **complete** sampler invocation on every factor trial.
Let all builder, decoder, primality, matching, verification, and bookkeeping
costs at a \(k\)-bit recursion node be bounded by a fixed polynomial
\(C(k)\).  The cost distribution of a fresh invocation is independent of
the event that all earlier trials were rejected.  Therefore, by conditional
expectation (equivalently Wald's identity), the expected sampling and
arithmetic cost at one composite node is at most

\[
4\bigl(R_{\rm exp}(k^a,4)+C(k)\bigr).
\tag{2.6}
\]

If the prime factorization of the original \(N\) has \(r\) prime leaves
counted with multiplicity, then \(2^r\le N\), so \(r\le n\).  The binary
factor-recursion tree has at most \(2r-1\le2n-1\) total nodes.  Dominating
every node length by \(n\) and applying linearity of expectation gives

\[
  \mathbb E[T(N)]
  \le
  8n\bigl(R_{\rm exp}(n^a,4)+C(n)\bigr)+C'(n),
  \tag{2.7}
\]

for a fixed polynomial \(C'\) covering final sorting, exponent merging, and
product verification.  Equation (2.7) is one fixed polynomial in \(n\),
independent of the unknown factors.  The same argument gives a polynomial
expected fair-random-bit count.  Every rational-coin rejection loop, every
complete sampler invocation, and every geometric factor loop terminates
almost surely; the finite recursion tree therefore terminates almost surely.
Correctness is unconditional for every returned split.

Accordingly, the graph hypothesis is sufficient for the full goal.  It is not
merely a reduction to exact permanent evaluation.

## 3. Universal support constraints for a positive matching gadget

### 3.1 Boundary convention

Let \(H=(V,E)\) be an arbitrary finite graph with a distinguished set
\(B\subseteq V\) of distinct boundary vertices.  Selecting terminal
\(b\in B\) means that an external edge covers \(b\), so the internal
matching problem deletes \(b\).  For \(S\subseteq B\), define

\[
  F_H(S)
  =
  \#\{\text{perfect matchings of }H-S\}.
  \tag{3.1}
\]

Arbitrarily many auxiliary vertices are allowed in \(V\setminus B\).
Nonnegative edge weights give the same support after zero-weight edges are
deleted, so every support statement below applies to positive weighted
gadgets as well.

If the opposite bit convention is used, every terminal bit is complemented.
This replaces the supported family by its twist with \(B\).  Fixed parity is
shifted by a constant, the charge equation is rewritten with a constant, and
the dual-rail subcube conclusion is unchanged because coordinate
complementation maps subcubes to subcubes.

### 3.2 Parity, bipartite charge, and symmetric exchange

If \(F_H(S)>0\), then \(H-S\) has an even number of vertices.  Therefore

\[
  |S|\equiv|V|\pmod2.
  \tag{3.2}
\]

Every supported set has the same parity.  Internal auxiliary vertices only
choose which parity occurs.

If \(H\) is bipartite with sides \(L,R\), a perfect matching of \(H-S\)
also requires equal remaining side sizes:

\[
  |L|-|S\cap L|
  =
  |R|-|S\cap R|.
\]

Equivalently,

\[
  |S\cap L|-|S\cap R|
  =
  |L|-|R|.
  \tag{3.3}
\]

Thus supported terminal sets lie on one exact integral charge hyperplane, a
strict refinement of parity.

There is also a combinatorial exchange constraint.  Let

\[
  \mathcal F_H=\{S\subseteq B:F_H(S)>0\}.
\]

Take \(X,Y\in\mathcal F_H\), choose perfect matchings \(M_X\) of
\(H-X\) and \(M_Y\) of \(H-Y\), and inspect
\(M_X\triangle M_Y\).  Every vertex outside \(X\triangle Y\) has degree
zero or two in this symmetric-difference graph.  Every vertex of
\(X\triangle Y\) has degree one: it is absent from exactly one of the two
matched graphs and matched in the other.  Hence the non-cycle components are
alternating paths whose endpoints pair the elements of
\(X\triangle Y\).

For any \(e\in X\triangle Y\), follow its alternating path to the other
endpoint \(f\in X\triangle Y\).  Toggling \(M_X\) along this path gives a
perfect matching of

\[
  H-\bigl(X\triangle\{e,f\}\bigr).
\]

Therefore

\[
  \forall X,Y\in\mathcal F_H, \forall e\in X\triangle Y,
  \exists f\in X\triangle Y:
  X\triangle\{e,f\}\in\mathcal F_H.
  \tag{3.4}
\]

This is the symmetric-exchange axiom.  When \(\mathcal F_H\ne\varnothing\),
the standard terminology is that \(\mathcal F_H\) is a matching
delta-matroid; together with (3.2), it is even.  Empty support still satisfies
the displayed parity and exchange implications vacuously, but is handled as
a separate realizable case rather than being called a delta-matroid.  The
proof already includes arbitrary internal auxiliary vertices and does not
assume planarity.

Equations (3.2)--(3.4) are necessary support conditions, not a full numerical
characterization of all perfect-matching counts.  In particular, higher
Pfaffian/matchgate identities must not be imposed on a general nonplanar
bipartite graph.

### 3.3 Nonempty exact dual rail is exactly a subcube at support level

Give logical bit \(i\) two boundary terminals
\(b_i^0,b_i^1\).  Encode a logical word \(z\in\{0,1\}^k\) by the
one-hot deletion set

\[
  B_z=\{b_i^{z_i}:1\le i\le k\}.
  \tag{3.5}
\]

Suppose a direct gadget is exact in the strong local sense

\[
  \mathcal F_H=\{B_z:z\in\mathcal R\}
  \tag{3.6}
\]

for some **nonempty** logical relation
\(\mathcal R\subseteq\{0,1\}^k\): there is no support on zero-rail,
two-rail, or other off-code terminal sets.

Every feasible set in (3.6) has cardinality \(k\).  In an equicardinal
delta-matroid, (3.4) becomes ordinary matroid basis exchange.  Indeed, for
\(X,Y\) of size \(k\) and \(e\in X\setminus Y\), the exchanged feasible
set must retain size \(k\), so the second endpoint lies in
\(Y\setminus X\) and has the form \(X-e+f\).

Now take \(z,w\in\mathcal R\) and a coordinate \(i\) where
\(z_i\ne w_i\).  Apply basis exchange to
\(e=b_i^{z_i}\in B_z\setminus B_w\).  Because every feasible set is an
exact one-hot codeword, the only possible exchanged terminal is
\(f=b_i^{w_i}\).  Choosing a terminal from any other block would leave
block \(i\) empty and that other block doubled.  Hence

\[
  z\oplus e_i\in\mathcal R
  \qquad
  \text{whenever }z,w\in\mathcal R\text{ differ at }i.
  \tag{3.7}
\]

Fix \(z^{(0)}\in\mathcal R\), and let \(I\) be the set of coordinates
that vary somewhere in \(\mathcal R\).  For every \(i\in I\), choose a
word \(w^{(i)}\in\mathcal R\) that differs from \(z^{(0)}\) at \(i\).
Induct on \(|J|\) for \(J\subseteq I\).  If
\(z^{(0)}\oplus\mathbf1_J\in\mathcal R\) and \(i\in I\setminus J\),
that current word and \(w^{(i)}\) still differ at \(i\), so (3.7) adds
\(i\).  Thus

\[
  \{z^{(0)}\oplus\mathbf1_J:J\subseteq I\}
  \subseteq\mathcal R.
\]

The reverse inclusion follows from the definition of \(I\).  Therefore
\(\mathcal R\) is exactly a subcube: some coordinates are fixed and all
others vary independently.

The support theorem is also sharp.  For one logical bit, take two boundary
vertices \(b^0,b^1\) on the right and one internal vertex \(u\) on the
left.  Connect \(u\) to both boundary vertices for a free bit, or only to
the boundary vertex that remains after the desired deletion for a fixed bit.
The component has a perfect matching after exactly the allowed one-hot
deletions and after no zero-rail or two-rail deletion.  A disjoint union over
bits realizes every subcube with multiplicity one.

Thus, under the exact direct convention (3.6), a **nonempty** logical
relation has a positive perfect-matching realization if and only if it is a
subcube.  The empty relation is separately realizable, for example by adding
an isolated internal vertex, and is the only exception to the classification
wording.  Common fixed auxiliary boundary bits do not help: they occur in
every feasible set, cancel from every symmetric difference, and leave the
proof unchanged.  Assignment-dependent auxiliary boundary states are
different and remain open.

## 4. Direct gadget kill tests

### 4.1 Single rail

For a single-rail truth-table signature, (3.2) alone requires every satisfying
row to have the same Hamming parity.

* COPY3 has rows \(000\) and \(111\), of opposite parity.
* AND3, in the order \((x,y,z)\) with \(z=xy\), contains
  \(000\) and \(100\), again of opposite parity.
* The full-adder relation

  \[
    a+b+c=s+2d
  \]

  contains \(00000\) and \(11001\) in the order
  \((a,b,c,s,d)\); their weights are zero and three.

Therefore none is the exact terminal signature of an ordinary positive
perfect-matching gadget.

The bipartite charge (3.3) is stronger.  Give terminal \(i\) a sign
\(\sigma_i=+1\) on the left and \(-1\) on the right.  Every supported
row must have one constant value of \(\sum_i\sigma_i b_i\).  AND's rows
\(000\) and \(010\) would force \(\sigma_y=0\), impossible.  COPY's two
rows would require a sum of three signs to be zero, also impossible.
For the full adder, the three one-input rows force
\(\sigma_a=\sigma_b=\sigma_c=-\sigma_s\); a two-input/carry row then
requires \(-2\sigma_s+\sigma_d=0\), impossible for signs.

Pins themselves are not the problem.  A lone boundary vertex realizes the
selected/deleted pin, while a boundary vertex joined to one internal mate
realizes the unselected pin.  Fixing terminals merely shifts the parity and
charge constants.  It cannot turn a mixed-parity residual truth relation into
a direct matching signature.  F21's sampling decoder does not require prefix
pins at all.

### 4.2 Exact one-hot dual rail

Dual rail removes the parity mismatch because every \(k\)-bit codeword
deletes exactly \(k\) terminals.  The subcube theorem replaces it with a
stronger obstruction.

For COPY3 the exact encoded support would be

\[
 \{\{x_0,y_0,z_0\},\{x_1,y_1,z_1\}\}.
\]

It is not a subcube.  Equivalently, basis exchange applied to \(x_0\) in
the first set requires one of the three one-terminal replacements, none of
which is supported.

For AND3 the four encoded codewords are

\[
  B_{000},\quad B_{010},\quad B_{100},\quad B_{111}.
\]

Between \(B_{000}\) and \(B_{111}\), remove \(z_0\).  Replacing it by
\(z_1\) gives the invalid truth row \(001\); replacing it by \(x_1\) or
\(y_1\) violates the exactly-one rail code.  Basis exchange fails.

For the full adder, both logical words \(00000\) and \(11111\) are valid:
\(0=0\) and \(3=1+2\).  Subcube closure would require the one-bit word
\(00001\), which asserts a carry from zero inputs and is invalid.  Hence the
full-adder relation is not an exact dual-rail matching signature.

Bipartiteness adds a useful layout constraint even before exchange.  Let
\(q_i(b)\in\{+1,-1\}\) be the side of rail \(b_i^b\).  Charge equality
on the four AND rows first gives

\[
 q_x(0)=q_x(1),\qquad q_y(0)=q_y(1),
\]

and then \(q_z(0)=q_z(1)\).  Thus both rails of each varying AND port
would have to lie on the same bipartition side.  For a full adder, writing
\(\Delta_i=q_i(1)-q_i(0)\in\{-2,0,2\}\), the one-input rows give

\[
  \Delta_a=\Delta_b=\Delta_c=-\Delta_s,
\]

while a two-input/carry row gives
\(-2\Delta_s+\Delta_d=0\).  The only allowed solution is
\(\Delta_a=\Delta_b=\Delta_c=\Delta_s=\Delta_d=0\), so each rail pair
must again occupy one side.  This condition is compatible with alternating
gadget sides and is therefore a constraint, not a global impossibility.

The exact dual-rail theorem does not cover a gadget with nonzero off-code
entries that are somehow suppressed by the rest of a global graph.  Such a
suppression cannot simply be assumed: a positive construction has no
cancellation, and gluing an independent one-hot filter is itself a
perfect-matching composition whose support and multiplicity must be proved.
Nor does the theorem cover a code in which a logical value occupies a larger
block of terminals or an internal matching pattern rather than one selected
terminal.

### 4.3 The obvious fused multiplier cell

Fusing the AND output into one full-adder does not evade the direct
obstruction.  The natural boundary relation is

\[
  a+c+xy=s+2d
  \tag{4.1}
\]

on \((x,y,a,c,s,d)\), with the partial product \(xy\) internal.

In single rail, \(000000\) and \(100000\) are both valid because
\(x\) is irrelevant when \(y=0\); they have opposite parity.  In exact
dual rail, \(000000\) and \(110010\) are valid, but the subcube between
them would contain \(000010\), which sets \(s=1\) with zero left-hand
side.  Thus (4.1) is not a subcube.

This closes only the most literal fused cell.  A larger cell may expose a
parity flag, use assignment-dependent auxiliary boundary states, encode
several wires as one block, or decode logical values from internal matching
edges.  Fusing an entire multiplier into a closed graph removes terminal
signature constraints altogether.  Those possibilities are not covered.

## 5. Positivity and global multiplicity

Local satisfiability preservation is insufficient for F21.  In a simple
composition of positive gadgets, let \(m_g(r)\) be the number of internal
perfect-matching completions of gadget \(g\) on local truth row \(r\).
For a deterministic circuit assignment \(z\), the matching multiplicity is
typically a product of the form

\[
  \prod_g m_g(r_g(z)),
\]

possibly times further wiring-cycle factors.  Unless this quantity is proved
independent of the factor witness, almost-uniform matching sampling pushes
forward to a biased divisor distribution.  In particular, a large excess of
matchings over the two trivial pairs can swamp every nontrivial factor even
when each satisfying assignment has at least one completion.

Equal local multiplicity is a sufficient design rule but not a necessary one;
a global balancing mechanism could compensate exactly.  A weaker F21 theorem
could also tolerate unequal multiplicities if it proved directly that
nontrivial witnesses carry inverse-polynomial total matching mass on every
composite.  No such bound follows from mere positivity or from the existence
of one matching per factor.

The standard permanent completeness theorem does not supply the missing
positive witness map.  Valiant's original construction first uses a weighted
cycle-cover graph with negative entries and states explicitly that spurious
cycle covers cancel, while each good route contributes a fixed factor.  Its
passage to \(0,1\)-matrices computes congruences modulo several primes,
replaces negative residues by nonnegative integers, and expands integer
weights before reconstructing the desired count arithmetically.  See
L. G. Valiant,
[*The Complexity of Computing the Permanent*](https://www.math.cmu.edu/users/af1p/Teaching/MCC17/Papers/permanent.pdf),
Theoretical Computer Science 8 (1979), especially Lemmas 3.1--3.3.

Thus the resulting unweighted perfect matchings are not presented in a
single, readable constant-to-one correspondence with the original satisfying
assignments.  Negative cancellation, modular recovery, and polynomial
interpolation can prove equality of aggregate counts without giving the
positive per-witness correspondence needed by the sampler.  This observation
is about the exact content of those reductions; it is not an impossibility
argument based on \(#P\)-hardness or on a conjectured separation such as
\(RP\ne NP\).

## 6. Exact boundary of the kill result

The following are closed by the proved local support theorem:

1. direct single-rail positive gadgets for COPY3, AND3, and full addition;
2. direct exactly-one dual-rail gadgets whose complete terminal support is
   precisely the encoded truth relation, even with arbitrary internal
   auxiliary vertices and common fixed boundary pins; and
3. the corresponding single-/dual-rail realization of the natural fused cell
   (4.1).

The following remain open and must not be folded into the negative result:

1. a closed polynomial-size bipartite graph whose internal matching pattern is
   decoded globally into \((x,y)\), with no exposed factor signature;
2. off-code local support that is removed by a proved globally positive
   construction without spoiling multiplicity;
3. assignment-dependent auxiliary boundary states whose projection is the
   desired Boolean relation;
4. larger constant-size or growing block codes, cycle-state encodings, or
   heterogeneous gadgets;
5. fused multiplication blocks substantially different from (4.1);
6. a graph family whose matching multiplicities are unequal locally but
   globally constant, or whose nontrivial matching mass is nevertheless
   inverse-polynomial on every composite;
7. weighted nonnegative matchings with an exact sampling theorem and a proved
   factor-decoding mass bound; and
8. any direct multiplication-specific construction not assembled as the
   excluded local truth-table gadgets.

For a closed graph \(B=\varnothing\), parity, charge, and delta-matroid
constraints reduce to vacuous statements about the one empty boundary set.
They impose no known restriction on an efficient decoder's labels for its
internal perfect matchings.  Therefore a global multiplication-specific
construction remains genuinely open.

## 7. Exact verdict and reopen condition

> **Exact verdict.** A public polynomial-size bipartite graph with a readable
> equal-multiplicity perfect-matching correspondence to ordered factor
> witnesses would yield complete all-input classical Las Vegas factoring in
> expected polynomial bit and fair-random-bit complexity by fixed-bias
> almost-uniform sampling.  However, the direct local route cannot use
> positive single-rail COPY3/AND3/full-adder signatures, and an exact
> nonempty one-hot dual-rail perfect-matching signature can express only a
> subcube, so
> it cannot express those gates or the natural fused multiplier cell.  This is
> a local encoding obstruction, not a perfect-matching or factoring lower
> bound.

A materially new retry must exhibit at least one of the open mechanisms in
Section 6 and prove all of the following simultaneously:

1. uniform factor-free graph construction of size and bit length polynomial
   in \(\log N\);
2. bipartiteness and existence of perfect matchings for every sampled
   composite input;
3. a polynomial-time decoder with exact product verification;
4. one common multiplicity per ordered factor witness, or an explicit
   inverse-polynomial lower bound on nontrivial total matching mass;
5. treatment of squares, prime powers, repeated factors, even and unbalanced
   composites; and
6. polynomial bit and random complexity for construction, sampling,
   verification, repetition, and complete recursion.

Merely citing permanent \(#P\)-completeness, giving a gadget with
row-dependent completion counts, or encoding the aggregate count by
cancellation/interpolation does not meet this reopen condition.
