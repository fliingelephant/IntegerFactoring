# Fresh hostile re-audit of corrected F28 — positive perfect-matching factor graph

**Candidate re-audited:** `experiments/F28_positive_matching_factor_graph_kill/RESULT.md`.

**Prior audit checked in full:** `experiments/F28_positive_matching_factor_graph_audit/RESULT.md`.

**Primary sources rechecked:** Jerrum--Sinclair--Vigoda, ECCC
TR00-079, especially Section 2.1, Figure 1, Lemma 2, Theorem 4,
Figure 3, and the end of Section 3; and Valiant (1979), Lemmas
3.1--3.3 and Proposition 3.4.

**Computation:** none.  This is a symbolic and source-level audit.

## Verdict

> **PASS WITH REQUIRED CORRECTIONS.**

The corrected candidate preserves both substantive cores:

1. its equal-multiplicity readable-graph hypothesis plus a genuine FPAUS
   conditionally gives complete all-input Las Vegas factoring in expected
   polynomial bit and fair-random-bit cost; and
2. the parity, bipartite-charge, alternating-path exchange, and nonempty
   exactly-one dual-rail subcube arguments still kill exactly the named
   direct local gadgets.

The proposed rational `3/4` cooling replacement is admissible in the JSV
proof, including an exact terminal truncation to `1/m!`.  Exact rational
coins also preserve the intended transition kernel and hence the
total-variation proof.

However, R1 is not fully repaired.  Section 2.4 undercounts the number of
cooling phases by a factor of up to `m^2`, and it does not define the
empirical-weight update on zero-count outcomes.  The latter outcomes have
small probability but nonzero probability, so omitting them leaves the
purported exact sampler undefined on some random-bit streams.  There are
also two small exactness qualifications: deterministic rational coins need
a separate one-line case, and the term “delta-matroid” conventionally
requires nonempty support.

These defects do not threaten the route's conclusion.  They have direct
polynomial-cost repairs, but PROMPT's exact bit-model and almost-sure
termination standards require the repairs and another fresh re-audit before
proof-blind reconstruction.

## Required corrections

### C1 — count all cooling phases, not the phases for one non-edge

The candidate currently says:

> There are `O(log(m!))=O(m log m)` phases.

JSV's Figure 3 changes the activity of **one chosen non-edge** in a phase.
There can be `m^2` non-edges.  With rational ratio `3/4`, the number of
steps for one non-edge is

\[
  \left\lceil \log_{4/3}(m!) \right\rceil
  = O(m\log m),
\]

so the total number of phases is

\[
  P
  \le m^2\left\lceil \log_{4/3}(m!) \right\rceil
  = O(m^3\log m).
\]

The correction must explicitly say that activities are updated one at a
time.  Simultaneously scaling all non-edge activities is not justified by
the JSV stability estimate: changing many activities at once can change an
ideal hole weight by much more than a constant factor.

The bit-length conclusion remains polynomial after the correction.  The
failure union bound must likewise use `P` phases and `m^2` hole estimates
per phase, i.e. `O(m^5 log m)` estimated quantities, as the primary paper
does.

### C2 — make empirical zero-count branches total and positive

The empirical update for a hole pair is of the form

\[
  w'(u,v)
  =
  w(u,v)\frac{C_{\mathcal M}}{C_{u,v}},
\]

where the two `C`'s are integer sample counts.  On the good Chernoff event
both counts are positive.  Off that event, either count can be zero with
nonzero probability.  The displayed ratio is then undefined or zero, and a
later Metropolis ratio need not be defined.

Specify an operational branch such as:

* if every required count is positive, perform the rational update;
* otherwise retain the previous positive rational weights (or use another
  fixed positive rational fallback) for that phase.

The bad branch is already charged to the initialization-failure event in
JSV's total-variation budget.  Its output need not be accurate, but the
algorithm must remain defined, all activities and hole weights must remain
positive, and Figure 1's bounded trials plus its known-perfect-matching
fallback must still return an actual perfect matching.  With this guard,
every path has polynomially bounded rational operand lengths and every
complete invocation terminates almost surely.

### C3 — state the deterministic rational-coin case

For `0<a<b`, the candidate's power-of-two rejection construction has
expected fewer than two rounds and expected fewer than
`2 ceil(log_2 b)` fair bits.  For `a=0` or `a=b`, decide
deterministically with zero bits.  This avoids the literal false strict
inequality “expected cost is less than `2s`” when `b=1` and `s=0`.
No complexity or distributional claim changes.

### C4 — qualify the delta-matroid name when support is empty

The corrected Section 3.3 now gives the right exact classification:
empty support is separately realizable, while every nonempty exact
one-hot dual-rail relation is a subcube.  Thus the mathematical repair
requested by R2 is present.

But the Outcome and Section 3.2 still say without qualification that
`mathcal F_H` “is a matching delta-matroid.”  Under the standard definition,
a delta-matroid has a nonempty feasible family.  Say instead:

> The support satisfies parity and symmetric exchange; when nonempty, it is
> an even matching delta-matroid.

This is terminological only.  All killed relations are nonempty.

## 1. Re-audit of R1: rational JSV implementation

### 1.1 The primary citation is accessible and says what F28 needs

The ECCC landing page and primary PDF were accessible at
`https://eccc.weizmann.ac.il/report/2000/079/` and its download link.
The PDF is the Jerrum--Sinclair--Vigoda preprint named by the candidate.

The relevant statements were verified directly:

* Section 2.1 defines a fully polynomial almost-uniform sampler as outputting
  a perfect matching within requested total variation `delta` of uniform in
  time polynomial in the side size and `log delta^{-1}`.
* Figure 1 uses finitely many complete Markov-chain simulations and returns
  an arbitrary known perfect matching if none lands in the perfect-matching
  sector.
* Lemma 2 proves the resulting output distribution has the requested total
  variation bias.
* Theorem 4 supplies the mixing bound under the factor-two hole-weight
  condition.
* Figure 3 changes one non-edge activity in each phase.
* The end of Section 3 gives `O(m^3 log m)` phases in side-size notation,
  `O(m^5 log m)` estimated values over all phases, polynomial initialization
  cost, and polynomial additional sampling cost.

Thus R3 is cleanly repaired: the citation is reproducible, is a primary
source, and the candidate invokes the paper's explicit FPAUS rather than
claiming that an FPRAS automatically implies the needed sampler.

### 1.2 Why rational `3/4` cooling is valid

The source updates one activity from `lambda(e)` to `lambda'(e)` under

\[
 e^{-1/2}\lambda(e)
 \le \lambda'(e)
 \le e^{1/2}\lambda(e).
\]

An ordinary rational step `lambda'=3lambda/4` lies in this interval.
Changing one activity by a factor `rho in [3/4,1]` changes each partition
sum by a factor in `[rho,1]`, so their ratio

\[
  w^*(u,v)
  =
  \frac{\lambda(\mathcal M)}
       {\lambda(\mathcal M(u,v))}
\]

changes by at most `rho^{-1} le 4/3`.  The refined estimate is within
`6/5` before the update, and

\[
  \frac65\cdot\frac43
  =
  \frac85
  <2.
\]

Therefore the factor-two invariant required by Theorem 4 survives.

Suppose the current activity is above `1/m!` but another multiplication by
`3/4` would pass below it.  Setting the next value exactly to `1/m!` uses
a factor `rho in (3/4,1)`, so the same argument applies.  The exact target
is therefore permitted; no irrational value is required.

### 1.3 Rational numerator and denominator growth

After C1, the schedule has `P=O(m^3 log m)` phases.  Each activity is a
power of `3/4` until its final value `1/m!`, so an unreduced numerator and
denominator need only `O(m log m)` bits.  A matching contains `m` edges;
products of its activities still have polynomial bit length.

At a phase, each empirical count is at most the polynomial sample count
`S`.  A non-fallback update multiplies the prior hole weight by a ratio of
two such integers.  Even without fraction reduction, after `P` updates its
numerator and denominator have at most their prior length plus
`O(P log S)` bits.  The JSV choice of per-estimate failure probability uses
`log epsilon^{-1}=O(log m+log delta^{-1})` beyond fixed constants, so
`log S` is polynomially bounded.  All hole weights, stationary weights,
proposal probabilities, and Metropolis ratios consequently have polynomial
bit length.

This validates the candidate's intended bit-growth conclusion, but only
with the corrected total phase count and the positive zero-count guard.
No fraction-normalizing gcd is necessary: unreduced rational pairs and
cross-multiplication suffice.

### 1.4 Exact fair-coin simulation

Every primitive random choice is rational:

* the lazy step has probability `1/2`;
* the proposed edge is uniform among a finite public set;
* empirical samples use repeated instances of the same rational chain; and
* Metropolis acceptance is the minimum of one and a ratio of positive
  rational weights.

For `0<a<b`, rejection from `2^s` points with
`s=ceil(log_2 b)` produces an exact uniform integer in
`{0,...,b-1}`.  Its survival probability is `b/2^s>1/2`.  It terminates
almost surely, uses fewer than two rounds in expectation, and has expected
`O(log b)` bit and fair-bit cost.  C3 handles deterministic probabilities.

Exact simulation therefore produces exactly the transition kernel analyzed
by JSV.  It introduces no discretization error and consumes none of the
total-variation budget.

### 1.5 Expected, not worst-case, resource bounds

The rejection coin has no deterministic fair-bit cap.  The candidate now
correctly calls `R_exp` an expected polynomial bound.  With C2, every bad
empirical branch remains a finite, positive-rational computation; Figure 1
has bounded trials and an actual perfect-matching fallback.

Each factor trial invokes the **entire** sampler from scratch with fresh
coins.  Let `C_i` be its random cost and let `T` be the first successful
factor trial.  Although `C_i` may correlate with success on trial `i`, it is
independent of the preceding rejection history.  Thus

\[
  \mathbb E\left[\sum_{i=1}^{T}C_i\right]
  =
  \sum_{i\ge1}
  \mathbb E[C_i\mathbf1_{\{T\ge i\}}]
  =
  \mathbb E[C_1]
  \sum_{i\ge1}\Pr(T\ge i)
  \le4\mathbb E[C_1].
\]

This is the direct conditional-expectation form of the candidate's Wald
claim and does not assume independence between cost and success inside one
invocation.  Rational rejection loops terminate almost surely, and a
geometric factor loop with conditional success at least `1/4` terminates
almost surely.  A deterministic finite recursion-tree bound then gives
almost-sure total termination and expected polynomial bit and fair-bit cost.

### 1.6 Total variation remains correct

On the event that every initialization estimate meets its promised
multiplicative accuracy, Theorem 4 and Lemma 2 give the allocated
near-uniform output guarantee.  There are
`O(m^5 log m)` estimates after C1, so assigning a sufficiently small
per-estimate failure budget makes the union of initialization failures use,
for example, at most half of the requested `delta`.  On a bad-estimate
event, C2 and Figure 1 still return some actual matching; an event of
probability at most `delta/2` can add at most `delta/2` to total variation.
The chain-mixing/output part uses the remaining budget.

Replacing irrational cooling by the permitted rational schedule changes
neither the invariant nor these event counts asymptotically.  Exact rational
coins reproduce the intended law, so no further TV term appears.

## 2. Re-audit of the conditional factoring theorem

The conditional reduction has no regression.

* The ordered positive witness set has exactly `tau(N)` members: one
  witness `(x,N/x)` for each positive divisor `x`.
* Equal positive multiplicity makes the uniform-matching pushforward
  exactly uniform on those witnesses.
* Total variation contracts under deterministic decoding.
* Every composite has `tau(N)ge3`, so its exact uniform nontrivial mass is
  at least `1/3`; bias `1/12` leaves at least `1/4`.
* Squares count the central witness once.  Prime powers, repeated factors,
  even composites, unbalanced factors, and `N=4` are all covered.
* The sampler always returns an actual matching.  Decoding, positivity,
  exact-product verification, and `1<x<N` ensure every accepted split is
  correct.
* Fresh full sampler invocations preserve the conditional success bound
  after every history; there is no accumulated-TV union bound across factor
  trials.
* If there are `r` prime leaves counted with multiplicity, then
  `2^r le N` and the recursion tree has at most `2r-1<2n` nodes.
* The factor-producing operation is decoding plus exact product/division
  verification, not a terminal factor-extracting gcd.

Subject to C1--C3, this remains a complete all-input classical Las Vegas
polynomial-bit factoring theorem **conditional on** the graph hypothesis.
F28 still does not construct that graph family.

## 3. Re-audit of matching support

### 3.1 Parity, charge, and alternating paths

For every supported deletion set `S`, `|V(H)-S|` is even, giving fixed
`|S| mod 2`.  In a bipartite graph, equality of the remaining side sizes
gives

\[
 |S\cap L|-|S\cap R|=|L|-|R|.
\]

Both statements survive arbitrary auxiliary vertices and disconnected
components.

For supported `X,Y`, perfect matchings of `H-X` and `H-Y` have symmetric
difference consisting of alternating cycles and paths.  The endpoints of
the paths are exactly `X triangle Y`.  Following the path from any prescribed
endpoint `e` reaches a distinct endpoint `f`; toggling the first matching
on that path proves support of
`X triangle {e,f}`.  This proves symmetric exchange without planarity,
uniqueness, or connectedness.  C4 is the only definitional qualification.

Positive weights alter counts but not support after zero-weight edges are
deleted.  Fixed bit complements twist the support and preserve exchange;
hypercube coordinate complements preserve subcubes.

### 3.2 Exact one-hot dual rail

Under complete exactly-one support, all feasible deletion sets have size
`k`.  Symmetric exchange therefore becomes ordinary basis exchange.  If
two codewords differ in block `i`, exact one-hot support forces the
replacement for `b_i^{z_i}` to be the other rail in the same block;
an exchange with another block would leave one block empty and another
doubled.  The logical relation is consequently closed under every single
coordinate that varies anywhere.  From a base word, induction yields all
combinations of the varying coordinates, hence a subcube.

The disjoint star construction realizes every nonempty subcube with
multiplicity one and with no off-code support.  An isolated internal vertex
realizes empty support.  The candidate's repaired nonempty/empty
classification is mathematically exact; only C4's global terminology
remains.

## 4. Gate, fused-cell, charge, and multiplicity checks

All displayed witnesses remain valid.

| Relation | Single-rail parity obstruction | Dual-rail subcube obstruction |
|---|---|---|
| COPY3 | `000,111` | `000,111`; every one-bit intermediate is invalid |
| AND3 | `000,100` | `000,111`; `001` is invalid |
| Full adder | `00000,11001` | `00000,11111`; `00001` is invalid |
| `a+c+xy=s+2d` | `000000,100000` | `000000,110010`; `000010` is invalid |

The AND rail-charge comparisons force equal side placement within each rail
pair.  The full-adder equations
`Delta_a=Delta_b=Delta_c=-Delta_s` and
`-2Delta_s+Delta_d=0` with
`Delta_i in {-2,0,2}` force every `Delta_i=0`.  The candidate correctly
uses these only as layout constraints.

The product-of-local-completion-counts warning is also correct.  Positivity
and one completion per Boolean assignment do not imply an inverse-polynomial
nontrivial matching mass; equal global multiplicity or a direct mass lower
bound is still required.

## 5. Valiant and scope

Valiant's primary paper confirms the candidate's narrow historical claim.
Lemma 3.1 uses a signed weighted cycle-cover construction: spurious routes
have aggregate contribution zero, while good routes correspond to satisfying
assignments and contribute a common positive amount.  Proposition 3.4
reduces signed integer permanents modulo several small primes; residues are
nonnegative, and Lemma 3.3 expands positive integer weights into a
`0,1` matrix before arithmetic reconstruction.

This proves aggregate permanent identities.  It does not exhibit one
unweighted graph whose every perfect matching has a readable constant-to-one
map to satisfying assignments.  The candidate therefore correctly says
that this classical proof does not itself supply F21's positive sampling
decoder.  It does not infer a lower bound or use an unproved complexity
separation.

The negative result remains confined to complete direct single-rail or
exactly-one dual-rail local signatures and the one displayed fused cell.
It does not cover off-code states removed globally, assignment-dependent
auxiliary ports, larger block codes, internal-edge encodings, heterogeneous
gadgets, globally balanced multiplicities, or a closed
multiplication-specific graph with a decoder.  For empty boundary, the
support constraints impose no restriction on labels assigned to internal
matchings.  No scope inflation or regression was found.

## Reconstruction recommendation

Do **not** start strict proof-blind reconstruction from this version.
First repair C1--C4, then perform another fresh hostile re-audit of the
sampler paragraph.  A clean pass should explicitly confirm:

1. one-edge-at-a-time `O(m^3 log m)` cooling and the
   `O(m^5 log m)` failure-event count;
2. positive rational behavior on zero empirical counts;
3. exact rational coins with expected, not worst-case, fair-bit bounds;
4. preservation of JSV's total-variation allocation; and
5. the nonempty qualifier for delta-matroid terminology.

After that clean pass, the prior audit's proposed proof-blind package remains
appropriate.
