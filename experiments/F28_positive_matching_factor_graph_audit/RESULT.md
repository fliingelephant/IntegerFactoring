# Hostile audit of F28 — positive perfect-matching factor graph

**Candidate audited:**
`experiments/F28_positive_matching_factor_graph_kill/RESULT.md`.

**Canonical context checked:** `PROMPT.md`, P36 in `PROVED.md`, X30 in
`FAILED.md`, and F20/F21 in `REGISTRY.md`.

**Computation:** none.  This audit is symbolic.  The cited primary papers
were read directly; no finite experiment is evidence for any conclusion
below.

## Verdict

> **PASS WITH REQUIRED CORRECTIONS.**

The two mathematical cores are sound:

1. the stated equal-multiplicity readable perfect-matching representation,
   together with a genuine almost-uniform sampler, conditionally gives a
   complete all-input classical Las Vegas factoring algorithm; and
2. the support of terminal deletions admitting a perfect matching obeys the
   parity, bipartite-charge, and even-delta-matroid constraints used in the
   report.  Under complete exactly-one dual-rail support, these constraints
   force every nonempty logical relation to be a subcube.  The displayed
   COPY3, AND3, full-adder, and natural fused-cell witnesses therefore do
   rule out exactly the claimed direct local gadgets.

I found no counterexample to either core.  I did find one proof-standard
gap in the invoked sampler's **bit/random-bit interface** and one edge-case
overstatement in the subcube theorem.  Both are repairable without changing
the route's conclusion, but PROMPT's bit-complexity standard makes the first
one substantive rather than cosmetic.

## Required corrections

### R1 — instantiate the sampler in the fair-random-bit Turing model

The candidate says that the Jerrum--Sinclair--Vigoda paper itself supplies a
fixed polynomial **bit-time and random-bit bound** \(R(m,\ell)\), and then
uses that as a worst-case per-invocation bound in (2.4).  The primary paper
does explicitly define and construct the required total-variation sampler,
with dependence polynomial in the graph order and
\(\log \delta^{-1}\).  Its displayed analysis, however, is principally in
Markov-chain transitions/arithmetic operations.  It uses activities and
Metropolis probabilities without spelling out the exact fair-coin rational
implementation or a worst-case bound on the number of fair random bits.
The paper therefore does not, by citation alone, justify the stronger
sentence in the candidate.

The corrected report must do one of the following.

* Give a Turing-model implementation.  A direct repair is available: choose
  a rational cooling step such as \(3/4\), with the last step truncated
  exactly to \(1/m!\).  Every activity and empirical hole-weight estimate is
  then rational and has polynomial bit length over the polynomial number of
  phases.  A Metropolis coin \(a/b\) can be generated exactly by rejection
  from a power-of-two range, using expected \(O(\log b)\) fair bits and
  expected polynomial bit time.  State and prove the polynomial bounds on
  the accumulated numerator/denominator lengths and on this expected coin
  cost.
* Or cite an exact Turing-model FPAUS theorem that already includes these
  facts, while stating its expected-versus-worst-case guarantee accurately.

If the exact rational-coin implementation is used, \(R\) should be an
**expected** polynomial cost, not an unsupported deterministic random-bit
cap.  The outer reduction still has polynomial expectation: use fresh,
independent complete sampler invocations and either apply Wald's identity to
the i.i.d. trial cost/success pairs or condition directly on the trial
history.  Almost-sure termination of the rational rejection coins and of the
geometric factor trials must also be stated.  Alternatively, a finite-
precision, fixed-time simulator may allocate its extra total-variation
error inside the existing \(1/12\) budget.

At the fixed bias \(1/12\), even a sampler polynomial in
\(\delta^{-1}\) would be enough for F28.  Thus this correction does not
threaten the conditional factoring theorem; it is needed only because the
current text claims a stronger bit-model interface than it proves.

### R2 — include the empty-support exception

The sentence saying that an exact one-hot dual-rail relation is a subcube
assumes a base word \(z^{(0)}\in\mathcal R\).  If
\(\mathcal R=\varnothing\), an isolated internal vertex gives a gadget with
empty support, while the empty relation is not normally called a subcube.
The exact support classification is therefore:

> A direct exactly-one dual-rail support is either empty or, if nonempty, a
> subcube; conversely every nonempty subcube has the displayed bipartite
> multiplicity-one realization.  The empty relation is separately
> realizable.

All four killed truth relations are nonempty, so this correction changes no
obstruction.

### R3 — make the primary sampler citation reproducible and no broader than
its statement

The author-hosted Georgia Tech URL in the candidate returned HTTP 403 during
this audit.  The same primary preprint is available as Jerrum--Sinclair--
Vigoda, ECCC Report 79 (2000),
`https://eccc.weizmann.ac.il/report/2000/079/`.  The corrected report should
cite that record or the journal DOI in addition to, or instead of, the dead
PDF URL.  It should continue to identify Section 2.1/Figure 1/Lemma 2 and
the end of Section 3, because the journal's headline theorem is an FPRAS for
the permanent whereas F28 needs the paper's explicitly constructed FPAUS.

This is a source/provenance correction.  It must not be replaced by the
weaker assertion that approximate counting somehow automatically gives the
sampling interface.

## 1. Conditional factorization theorem

### 1.1 Uniform pushforward and total variation

For each divisor \(x\mid N\) there is exactly one positive
\(y=N/x\), so the ordered witness set

\[
  \mathcal W_N=\{(x,y):xy=N\}
\]

has size \(\tau(N)\), not \(2\tau(N)\).  If every witness has exactly
\(c_N>0\) matching preimages and every perfect matching decodes to a
witness, the uniform matching measure pushes forward to the uniform measure
on \(\mathcal W_N\).  The value of \(c_N\) need not be computed by the
algorithm.

For every deterministic decoder \(D\), total variation contracts under
pushforward.  Hence an input matching distribution within \(\delta\) of
uniform assigns the event

\[
  A_N=\{(x,y):1<x<N\}
\]

probability at least

\[
  \frac{\tau(N)-2}{\tau(N)}-\delta.
\]

Every composite has \(\tau(N)\ge3\), with equality exactly for a prime
square.  Thus \(\delta=1/12\) gives per-invocation success at least \(1/4\).
There is no union bound or accumulated-TV requirement: one sampler output is
used for one verified event.  Re-running the **entire** sampler with fresh
coins makes this lower bound valid after every rejection history.  Reusing a
single random preprocessing state would not by itself justify that
conditional claim, so the candidate's fresh-invocation wording is essential.

### 1.2 Existence, edge cases, and correctness

The graph hypothesis gives \(c_N\tau(N)>0\) perfect matchings.  A
deterministic bipartite matching routine can therefore supply the initial and
fallback matching required by the sampler.  Prime nodes are recognized by a
deterministic polynomial-time primality test and never invoke the graph
construction.

The divisor-count argument covers all requested cases.

* \(N=p^e\), \(e\ge2\), has success mass
  \((e-1)/(e+1)\ge1/3\).
* For a square, the central ordered witness is counted once, as it should be.
* \(N=4\) attains the worst uniform success \(1/3\), so even composites are
  included.
* Repeated factors, unbalanced factors, and arbitrary products require no
  distributional promise.

The sampler always returns an actual perfect matching; its fallback is the
deterministically found one.  Decoding plus the checks
\(x,y>0\) and \(xy=M\), followed by \(1<x<M\), ensures that every accepted
split is correct.  A nontrivial accepted \(x\) also forces \(1<y<M\).  No
sampler error can create an incorrect factor.

The terminal factor-producing step is decoding and exact product/division
verification.  It is not a factor-extracting gcd.  This narrow claim does
not forbid standard internal arithmetic in primality or matching routines,
and the candidate does not rely on any such internal gcd to reveal the
factor.

### 1.3 Recursion and expectation

At a composite node the number of independent full sampler invocations is
stochastically dominated by a geometric random variable of parameter
\(1/4\), so it is finite almost surely and has expectation at most four.
Every accepted split strictly decreases both children.  If the final prime
factorization has \(r\) leaves counted with multiplicity, then
\(2^r\le N\), hence \(r\le\log_2N<n\), and the binary recursion tree has at
most \(2r-1<2n\) nodes.

Once R1 supplies a genuine expected polynomial bit/random cost per complete
sampler invocation, conditional expectation over each reached node and the
deterministic \(2n\) node bound give one fixed polynomial upper bound for
the whole computation.  All decoded integers have at most \(n\) bits under
the graph hypothesis; products, divisions, primality tests, sorting,
exponent merging, and final product verification therefore have polynomial
bit cost.  A finite tree of almost-surely terminating nodes terminates almost
surely.

Thus the conditional theorem is valid after R1.  It is a sufficient
construction theorem, not an unconditional factoring result, because F28
does not construct the graph family.

## 2. Audit of the JSV sampler interface

The primary Jerrum--Sinclair--Vigoda preprint says the following.

* Section 2.1 defines a fully polynomial almost-uniform sampler as an
  algorithm that outputs a perfect matching from a distribution at total
  variation distance at most \(\delta\) from uniform and runs in time
  polynomial in the side size and \(\log\delta^{-1}\).
* Figure 1 and Lemma 2 convert the rapidly mixing chain into exactly that
  sampler.  The bounded fallback is an arbitrary known perfect matching, so
  the output is always a genuine perfect matching.
* Theorem 4 supplies the mixing bound.  The end of Section 3 gives, for the
  0--1 case, an initialization cost
  \(O(m^{26}(\log m)^2(\log m+\log\delta^{-1}))\) in the paper's side-size
  notation and an additional polynomial expected sampling cost.  The
  exponents are enormous but fixed.
* The construction assumes at least one perfect matching; F28 explicitly
  supplies one by deterministic search under its graph hypothesis.

Consequently the cited source does supply the **distributional** interface
F28 uses; the route is not merely invoking an FPRAS for a number.  There is
no hidden dependence exponential in the graph order or in
\(\log\delta^{-1}\).  R1 is only the missing translation from the paper's
arithmetic/transition presentation to the exact fair-random-bit accounting
demanded by PROMPT.

## 3. Matching-support delta-matroid

Let \(X,Y\) be supported deletion sets, with perfect matchings
\(M_X\) of \(H-X\) and \(M_Y\) of \(H-Y\).  Regard both matchings as edge
sets on \(V(H)\).  In \(M_X\triangle M_Y\):

* a vertex outside \(X\triangle Y\) has degree zero or two;
* a vertex in \(X\setminus Y\) has its unique incident edge from \(M_Y\);
* a vertex in \(Y\setminus X\) has its unique incident edge from \(M_X\).

Thus every noncycle component is an alternating path with two distinct
endpoints in \(X\triangle Y\).  Starting at any prescribed
\(e\in X\triangle Y\), let \(f\ne e\) be the other endpoint of its path.
Toggling \(M_X\) on that path covers an endpoint formerly deleted from
\(H-X\), uncovers an endpoint formerly present, or does the corresponding
operation at both ends.  In all four endpoint-type combinations it is a
perfect matching of

\[
  H-(X\triangle\{e,f\}).
\]

This proves symmetric exchange and also closes the possible \(f=e\)
loophole: \(f\) is the other endpoint of a nontrivial path.  Since every
feasible \(S\) satisfies
\(|S|\equiv|V(H)|\pmod2\), the set system is even.

The proof does not require connectedness, planarity, simplicity beyond the
usual matching convention, or a unique perfect matching.  Isolated
terminals merely remove some sets from support.  Parallel edges and positive
multiplicities change counts but not support.  Nonnegative weights likewise
reduce to the positive-edge subgraph.  The only definitional qualification
is R2: many definitions require a delta-matroid's feasible family to be
nonempty.

Complementing terminal conventions twists the deletion family by a fixed
subset of the boundary.  Twists preserve symmetric exchange; Hamming parity
changes by a constant; and coordinate complementation preserves the class of
subcubes.  Therefore bit complements and rail relabelings do not evade the
obstruction.

## 4. Bipartite charge

For bipartite \(H=(L,R;E)\), a perfect matching of \(H-S\) requires

\[
 |L|-|S\cap L|=|R|-|S\cap R|,
\]

so every feasible deletion set has the exact charge

\[
 |S\cap L|-|S\cap R|=|L|-|R|.
\]

This uses only side cardinalities and therefore holds for disconnected
graphs, isolated boundary vertices, arbitrary auxiliary vertices, and every
placement of the rails.  Complementing a selected-terminal convention only
changes the affine constant/sign description.

The report's rail consequences are correct.  For AND, comparing \(000\)
with \(100\) and \(010\) forces the two input rail pairs to have equal side
charges, and comparison with \(111\) then forces the output rail pair too.
For the full adder, the one-input rows give
\(\Delta_a=\Delta_b=\Delta_c=-\Delta_s\), while a two-input/carry row gives
\(-2\Delta_s+\Delta_d=0\).  Since every
\(\Delta_i\in\{-2,0,2\}\), all are zero.  The report correctly calls this a
layout constraint, not a global impossibility.

## 5. Exactly-one dual rail

Under the complete-support hypothesis

\[
 \mathcal F_H=\{B_z:z\in\mathcal R\},\qquad
 B_z=\{b_i^{z_i}:1\le i\le k\},
\]

all feasible sets have cardinality \(k\).  Symmetric exchange then becomes
ordinary matroid basis exchange: for
\(e\in X\setminus Y\), cardinality rules out a second deletion from
\(X\setminus Y\), so the exchanged element lies in \(Y\setminus X\).

If \(B_z,B_w\) differ in block \(i\), remove \(b_i^{z_i}\).  Exact one-hot
support makes \(b_i^{w_i}\) the only possible replacement: a rail from any
other block leaves block \(i\) empty and doubles that other block.  Therefore

\[
  z,w\in\mathcal R, z_i\ne w_i
  \quad\Longrightarrow\quad
  z\oplus e_i\in\mathcal R.
\]

Starting from any \(z^{(0)}\in\mathcal R\), this single-coordinate closure
inductively generates all combinations of every coordinate that varies
anywhere in the relation.  No other coordinate can vary by definition.
Hence every **nonempty** relation is a subcube.

The converse star gadget is correct.  Put both rails on one bipartition side
and one internal vertex on the other.  Connecting the internal vertex to
both rails realizes a free coordinate; connecting it only to the rail that
remains after the desired deletion realizes a fixed coordinate.  With zero
or two deleted rails the component has an unmatched vertex, and with an
allowed one-hot deletion it has one unique matching.  Disjoint union realizes
every nonempty subcube with multiplicity one.  Fixed common auxiliary
boundary selections occur in every feasible set and cancel from every
symmetric difference, so they do not affect the proof.

## 6. Gate and fused-cell witnesses

Every displayed witness checks out.

| Relation | Single-rail mixed-parity witnesses | Exactly-one dual-rail non-subcube witnesses |
|---|---|---|
| COPY3 | \(000,111\) | \(000,111\); any one-coordinate intermediate is invalid |
| AND3, \(z=xy\) | \(000,100\) | \(000,111\); flipping only \(z\) gives invalid \(001\) |
| Full adder, \(a+b+c=s+2d\) | \(00000,11001\) | \(00000,11111\); \(00001\) is invalid |
| Fused cell, \(a+c+xy=s+2d\) | \(000000,100000\) | \(000000,110010\); \(000010\) is invalid |

For single rail, complementing any fixed subset of logical coordinates adds
a constant to Hamming parity modulo two, so each mixed-parity obstruction
survives all logical bit complements.  For dual rail, swapping the two rails
of any block is a hypercube coordinate complement, which maps subcubes to
subcubes and non-subcubes to non-subcubes.

The narrower charge contradictions are also correct: AND's \(000/010\)
comparison would require a terminal sign zero; COPY would require three
\(\pm1\) signs to sum to zero; and the full-adder equations would require
\(-2\sigma_s+\sigma_d=0\) with signs in \(\{\pm1\}\).

## 7. Valiant citation

Valiant's 1979 paper supports the candidate's narrow historical statement.
Lemma 3.1 first constructs a matrix with entries in
\(\{-1,0,1,2,3\}\).  The proof groups cycle covers into routes, makes every
spurious route contribute zero by signed cancellation inside the junctions,
and gives each good route a fixed positive contribution.  Proposition 3.4
then evaluates the signed integer permanent modulo several small primes,
replaces negative entries by their nonnegative residues, applies Lemma 3.3
to expand positive integer weights into a 0--1 matrix, and reconstructs the
integer arithmetically.

That proof establishes aggregate permanent identities.  It does not present
one unweighted graph whose every perfect matching has a readable,
constant-to-one association with a satisfying assignment.  Hence it does
not supply F21's missing positive sampler decoder.  This is only a statement
about the cited reduction.  It neither proves that no other positive
construction exists nor invokes \(RP\ne NP\), \(\#P\)-hardness beliefs, or
any complexity separation.  The candidate preserves that scope.

## 8. Scope audit

The negative theorem uses the complete local-support identity
\(\mathcal F_H=\{B_z:z\in\mathcal R\}\).  It therefore does **not** apply to:

* off-code local states removed only after a proved global composition;
* a projection with assignment-dependent auxiliary boundary states;
* block codes, internal-edge/cycle-state codes, or heterogeneous rails;
* a closed graph whose decoder labels complete internal matchings;
* witness-dependent local multiplicities that are exactly balanced only
  globally;
* a merely inverse-polynomial lower bound on total nontrivial matching mass;
* fused blocks other than the explicitly tested relation
  \(a+c+xy=s+2d\); or
* any multiplication-specific construction not decomposed into the excluded
  direct truth-table gadgets.

For \(B=\varnothing\), the terminal support contains only the empty boundary
set when a perfect matching exists, so the local parity/charge/exchange
conditions say nothing about labels assigned to internal matchings.  The
candidate explicitly preserves this global route.  It also correctly notes
that positivity plus existence of one completion per Boolean witness does
not control the pushforward distribution: assignment-dependent products of
local completion counts can concentrate essentially all matching mass on
trivial factor witnesses.

Accordingly, F28 is evidence against the exact named **local encoding
mechanism**, not a perfect-matching lower bound and not a method failure for
F21's closed global graph hypothesis.

## Reconstruction recommendation

After R1--R3 are incorporated and a fresh hostile re-audit confirms the new
Turing-model paragraph, a strict proof-blind reconstruction is warranted.
The reconstruction package should state only:

1. the equal-multiplicity graph hypothesis and the FPAUS interface;
2. the terminal-deletion support theorem;
3. the exactly-one dual-rail support condition; and
4. the four truth relations to test.

The reconstructor should independently recover the all-input Las Vegas
recursion and the alternating-path/subcube proof, including the fair-random-
bit implementation or a precise invoked theorem.  It must not be shown the
candidate or this audit.  Only after that cadence should the result be
promoted.  It remains an auxiliary boundary result, not completion of the
top-level factoring goal.
