# Third fresh hostile re-audit of F28 — positive perfect-matching factor graph

**Candidate audited:**
`experiments/F28_positive_matching_factor_graph_kill/RESULT.md`.

**Prior audits read in full:**
`experiments/F28_positive_matching_factor_graph_audit/RESULT.md` and
`experiments/F28_positive_matching_factor_graph_reaudit/RESULT.md`.

**Primary sources rechecked:** Jerrum--Sinclair--Vigoda, ECCC TR00-079 / the
STOC preprint and J. ACM 51 (2004), Sections 2--3; and Valiant (1979),
Lemmas 3.1--3.3 and Proposition 3.4.

**Computation:** none.  This audit is symbolic and source-level.

## Verdict

> **PASS WITH ONE REQUIRED CORRECTION.**

C1--C4 from the preceding re-audit are now repaired.  In particular, the
candidate has the right one-nonedge-at-a-time phase count, the right estimate
count, a total positive branch on a zero empirical count, polynomial
unreduced rational bit growth, exact deterministic and nontrivial rational
coins, almost-sure termination, and the nonempty qualifier in its
delta-matroid terminology.

The conditional factoring theorem, the matching-support theorem, every gate
and fused-cell witness, the Valiant paragraph, and the negative theorem's
scope all survive the corrections.

One error remains in the stated total-variation split.  It is a local and
directly repairable proof error, but the current sentence is false: the
complement of the **marked zero-count event** can still contain a positive but
inaccurate empirical estimate.  JSV's good-weight proof does not apply on
that event.  The analysis must charge the full empirical-accuracy failure
event, whether or not the algorithm can detect it.

Strict proof-blind reconstruction must therefore wait for this paragraph to
be corrected and freshly rechecked.

## Required correction C5 — charge every inaccurate estimate, not only a
detectable zero

Section 2.4 correctly begins by allocating at most \(\delta/2\) to the union
of all empirical-estimation failures.  It then defines a detectable fallback
only when a required sample count is zero.  The next two sentences say:

> The marked event has probability at most \(\delta/2\); its arbitrary
> actual-matching output contributes at most that amount to total variation.
> On its complement the JSV proof contributes at most the other
> \(\delta/2\).

The last sentence does not follow.  A ratio of two positive empirical counts
can be outside the required multiplicative window.  Such an outcome belongs
to the union-bounded estimation-failure event but is not marked by the
zero-count guard.  On that outcome the computed weights remain positive and
the algorithm remains operational, but Theorem 4's factor-two hypothesis is
not proved.

The exact repair is to name the full event.  For example, replace the quoted
split by the following argument.

* Let \(E\) be the event that at least one empirical estimate in the whole
  initialization misses its promised multiplicative interval.  The choice of
  per-estimate failure probability and the union bound give
  \(\Pr(E)\le\delta/2\).
* A zero required count implies \(E\), because the corresponding true sector
  has a positive inverse-polynomial stationary mass.  On that detectable
  subevent the algorithm aborts initialization and returns the known perfect
  matching.  On \(E\) with all required counts positive, the algorithm may
  continue with inaccurate weights, but every weight remains a positive
  rational and the bounded sampler still returns an actual matching.
  Therefore the entire algorithm is defined on every stream, and the
  arbitrary conditional law on \(E\) contributes at most \(\Pr(E)\) to
  total variation.
* On \(E^c\), every refinement has the required accuracy, the cooling
  invariant holds at every phase, and the mixing/final-sampling analysis is
  allocated at most \(\delta/2\).  Convexity of total variation then gives
  total error at most \(\delta\).

This change needs no new mechanism, runtime bound, or algorithmic test for
whether a positive estimate is accurate.  It merely distinguishes the
operational zero-count guard from the probabilistic event used in the proof.

## 1. Decisive check of C1--C4

### 1.1 C1: rational one-nonedge cooling and exact counts — repaired

The ECCC/STOC version of the JSV initialization changes one selected
nonedge activity in a phase.  Starting from activity one, multiplying by
\(3/4\), and truncating the last step exactly to \(1/m!\) requires at most

\[
  \left\lceil\log_{4/3}(m!)\right\rceil
  =O(m\log m)
\]

updates for one nonedge.  There are at most \(m^2\) nonedges, so

\[
  P\le
  m^2\left\lceil\log_{4/3}(m!)\right\rceil
  =O(m^3\log m).
\]

This is the complete schedule, not the schedule for one edge.  Each phase
refines at most \(m^2+1=O(m^2)\) sector probabilities, hence the complete
initialization makes \(O(m^5\log m)\) empirical estimates.  The candidate's
failure union bound now uses this quantity.

The rational cooling step is admissible.  Changing one activity by
\(\rho\in[3/4,1]\) changes every matching partition sum by a factor in
\([\rho,1]\), so an ideal hole-weight ratio changes by at most
\(\rho^{-1}\le4/3\).  A refined \(6/5\)-approximation therefore remains
within

\[
  \frac65\frac43=\frac85<2
\]

after the activity update, as required by JSV's mixing theorem.  If an
ordinary \(3/4\) step would cross \(1/m!\), exact truncation has
\(\rho\in(3/4,1)\), so the same proof applies.

The later journal version groups nonedges incident to one vertex and obtains
a faster phase count.  That does not invalidate the candidate's explicitly
chosen, slower ECCC/STOC one-edge schedule.

### 1.2 C2: zero-count totality and positivity — operationally repaired

On a successful empirical refinement, the update multiplies a positive hole
weight by a ratio of two positive integer counts.  If either required count
is zero, the candidate now retains the preceding positive rational weights
and returns the deterministically known perfect matching.  Thus it never
divides by zero, never creates a zero hole weight, and never invokes a
Metropolis ratio with a zero denominator.

If all counts are positive but an estimate is inaccurate, all subsequent
rational operations are still defined and positive; only the distributional
proof can fail.  This observation is exactly why C5 must charge the full
event \(E\), rather than the marked zero-count subevent.  With C5's wording,
the zero-count fallback and the total-variation proof are both complete.

### 1.3 Polynomial unreduced rational bit growth — repaired

Every activity is a rational power of \(3/4\), followed possibly by the
exact rational \(1/m!\), and therefore has polynomial numerator and
denominator length.  A matching uses only \(m\) activities.  If the sample
size per empirical estimate is \(S\), every nonfallback hole-weight update
multiplies its current rational representation by a ratio of integers at
most \(S\).  Without any fraction reduction, after \(P\) phases its two
stored integers grow by at most

\[
  O(P\log S)
\]

bits beyond their initial length.  Both \(P\) and \(S\) are polynomial in
\(m\) and \(\log\delta^{-1}\).  Products, comparisons, and
cross-multiplications therefore have polynomial bit cost.  A
fraction-normalizing gcd is unnecessary.

### 1.4 C3: exact rational coins — repaired

The candidate now separates deterministic probabilities.  If \(a=0\) or
\(a=b\), the transition rejects or accepts with no random bits.  For
\(0<a<b\), put \(s=\lceil\log_2 b\rceil\), sample uniformly from
\(\{0,\ldots,2^s-1\}\), retry values at least \(b\), and accept values
below \(a\).  Because \(b/2^s>1/2\), the number of rounds is finite almost
surely and has expectation below two.  The expected fair-bit use is below
\(2s\), and every comparison has polynomial bit cost.  The same construction
gives exact uniform finite proposals.

Hence the simulated transition kernel is exactly JSV's rational kernel; no
rounding term is added to total variation.  The guarantee is correctly
stated as expected polynomial fair-bit and bit cost, not as a deterministic
cap.

There are deterministically finitely many phases, empirical samples, Markov
steps, and sampler trials.  Each rational-coin rejection loop terminates
almost surely, so a complete invocation terminates almost surely.  The
outer factor loop has conditional success probability at least \(1/4\), so
it too terminates almost surely.  Finally, the factor recursion has a
deterministically finite tree.  The candidate's almost-sure termination
claim is therefore sound once C5 supplies the correct distributional split.

### 1.5 C4: nonempty delta-matroid terminology — repaired

The Outcome says that supported deletion sets satisfy symmetric exchange and
that, **when the support is nonempty**, they form an even matching
delta-matroid.  Section 3.2 repeats the same qualification and handles empty
support separately.  Section 3.3 likewise classifies a nonempty exact
one-hot relation as a subcube and gives a separate realization of the empty
relation.  No definitional overstatement remains.

## 2. Conditional all-input Las Vegas reduction

The conditional theorem is otherwise complete.

1. There is one ordered positive witness \((x,N/x)\) for each divisor
   \(x\mid N\), so \(|\mathcal W_N|=\tau(N)\).
2. If every witness has the same positive matching multiplicity and every
   perfect matching decodes to a witness, uniform matchings push forward to
   the uniform law on \(\mathcal W_N\).  Total variation contracts under
   the deterministic decoder.
3. Exactly two ordered witnesses are trivial.  Every composite has
   \(\tau(N)\ge3\), with equality for a prime square, so the exact uniform
   nontrivial mass is at least \(1/3\).  A sampler at distance \(1/12\)
   leaves success probability at least \(1/4\).
4. Squares count their central witness once.  The same divisor count covers
   prime powers, repeated factors, even composites, unbalanced products, and
   \(N=4\).
5. The sampler always returns an actual perfect matching, including on its
   fallback branch.  Positivity and exact-product checks followed by
   \(1<x<N\) ensure that every accepted split is correct.  No Monte Carlo
   error can produce an incorrect factor.
6. Every retry is a fresh complete sampler invocation.  Therefore the
   conditional success probability after any rejection history remains at
   least \(1/4\), and the expected number of invocations at a composite node
   is at most four.
7. Although an invocation's random cost may correlate with its success, its
   cost is independent of all earlier rejection events.  Summing
   \(\mathbb E[C_i\mathbf 1_{\{T\ge i\}}]\) gives at most four times the
   expected cost of one invocation; no unsupported independence between cost
   and same-trial success is needed.
8. If the final factorization has \(r\) prime leaves with multiplicity, then
   \(2^r\le N\), hence \(r\le n\), and the binary recursion tree has at most
   \(2r-1\le2n-1\) nodes.  Polynomial expected cost per node therefore gives
   one polynomial expected bit and fair-bit bound for the full recursion.

Deterministic primality testing prevents sampler calls on prime leaves.
Decoding followed by exact multiplication/division verification is the
factor-producing terminal operation; the reduction does not end in a
factor-extracting gcd.  This remains a conditional theorem: F28 has not
constructed the hypothesized graph family.

## 3. Primary-source claims

The JSV source does provide the distributional interface used here, not
merely an approximate permanent value.  Section 2.1 defines a
fully-polynomial almost-uniform perfect-matching sampler in total variation.
Figure 1 performs bounded trials and outputs a known perfect matching if the
trials do not reach the valid perfect-matching sector.  The mixing theorem
applies under factor-two approximate hole weights.  The ECCC/STOC
initialization changes one nonedge per phase and records the
\(O(m^3\log m)\) phase and \(O(m^5\log m)\) estimate counts used by the
candidate.  It assigns one part of the requested bias to initialization
failure and the other part to final sampling.

The paper states its main complexity in transitions and arithmetic
operations.  It does not itself spell out an exact fair-coin Turing
implementation.  The candidate's rational schedule, polynomial operand
length proof, and exact rejection coins are therefore necessary; subject to
C5, they now supply that missing translation.

The ECCC record, journal citation, title, and three authors are correctly
identified.  The journal's faster grouped-update schedule is compatible
with, but not needed for, the candidate's preprint-style schedule.

## 4. Matching-support theorem

For supported deletion sets \(X,Y\), choose perfect matchings of \(H-X\)
and \(H-Y\).  Their symmetric difference consists of alternating cycles and
alternating paths.  The path endpoints are precisely \(X\triangle Y\).
Following the path from a prescribed endpoint \(e\) to its distinct other
endpoint \(f\), then toggling the first matching on that path, gives a
perfect matching after deleting
\(X\triangle\{e,f\}\).  This proves symmetric exchange with arbitrary
internal vertices and without planarity, connectedness, or uniqueness.

Every supported deletion set has fixed parity because \(|V(H)-S|\) is even.
For bipartite \(H=(L,R;E)\), equality of remaining side sizes gives the
exact charge

\[
 |S\cap L|-|S\cap R|=|L|-|R|.
\]

Positive edge weights change counts but not support; zero-weight edges may
be deleted.  A fixed terminal complement twists the set system and preserves
the exchange argument.

Under complete exactly-one dual-rail support, every feasible deletion set
has cardinality \(k\).  Symmetric exchange becomes ordinary basis exchange.
If two codewords differ in block \(i\), exchanging the selected rail in that
block can only insert the other rail from the same block; every other choice
would leave one block empty and another doubled.  The logical relation is
therefore closed under every single coordinate that varies anywhere.  From
one base word this generates every combination of the varying coordinates,
so every nonempty relation is a subcube.

The converse star component realizes a free or fixed logical coordinate with
one matching on every allowed one-hot deletion and no off-code support.
Disjoint union realizes every nonempty subcube with multiplicity one.  An
isolated internal vertex separately realizes empty support.  Common fixed
boundary selections cancel from every symmetric difference; genuinely
assignment-dependent auxiliary selections remain outside the theorem.

## 5. Gate, charge, and fused-cell checks

All four obstruction witnesses are correct.

| Relation | Single-rail mixed-parity rows | Dual-rail non-subcube rows |
|---|---|---|
| COPY3 | \(000,111\) | \(000,111\); every one-bit intermediate is invalid |
| AND3 | \(000,100\) | \(000,111\); \(001\) is invalid |
| Full adder | \(00000,11001\) | \(00000,11111\); \(00001\) is invalid |
| \(a+c+xy=s+2d\) | \(000000,100000\) | \(000000,110010\); \(000010\) is invalid |

Fixed bit complements preserve the mixed-parity contradiction, and rail
swaps are coordinate complements that preserve the class of subcubes.

The bipartite charge calculations also check out.  AND forces the two rails
of each varying port onto the same side.  For the full adder, the one-input
rows give
\(\Delta_a=\Delta_b=\Delta_c=-\Delta_s\), while a two-input/carry row gives
\(-2\Delta_s+\Delta_d=0\).  Since every
\(\Delta_i\in\{-2,0,2\}\), all differences vanish.  The candidate correctly
uses this only as a layout constraint.

The multiplicity warning is necessary and correct.  Positive local support
does not make the pushforward distribution useful: products of
assignment-dependent local completion counts can place negligible mass on
all nontrivial factors.  Equal global multiplicity or a direct
inverse-polynomial nontrivial-mass bound remains essential.

## 6. Valiant paragraph

Valiant's Lemma 3.1 uses a signed weighted cycle-cover construction.  Bad
routes have aggregate contribution zero by cancellation, while each good
route contributes one common positive factor and good routes correspond to
satisfying assignments.  Proposition 3.4 evaluates the resulting signed
integer permanent modulo enough small primes, replaces entries by
nonnegative residues, invokes Lemma 3.3 to expand positive integer weights
to a \(0,1\) matrix, and reconstructs the integer arithmetically.

This proves aggregate permanent identities.  It does not present one
unweighted graph in which every perfect matching has a readable
constant-to-one association with a satisfying assignment.  The candidate's
narrow historical conclusion is therefore accurate.  It does not turn this
observation into a lower bound and does not rely on \(RP\ne NP\),
\(\#P\)-hardness beliefs, or any unproved separation.

## 7. Scope and regression audit

The negative theorem still requires a complete direct terminal-support
identity.  It closes direct single-rail COPY3/AND3/full-adder signatures,
complete exactly-one dual-rail versions of those signatures, and the one
displayed fused cell.  It does not close:

* off-code states eliminated by a proved global positive composition;
* projected relations with assignment-dependent auxiliary ports;
* larger block, internal-edge, cycle-state, or heterogeneous encodings;
* globally balanced but locally unequal matching multiplicities;
* a direct inverse-polynomial mass construction without equal multiplicity;
* fused blocks different from \(a+c+xy=s+2d\); or
* a closed multiplication-specific graph whose internal matching is decoded
  globally.

For empty boundary, the support conditions reduce to a statement about at
most the one empty boundary set and impose no restriction on labels assigned
to internal matchings.  The candidate therefore remains a local encoding
obstruction, not a perfect-matching lower bound or a failure of the global
F21 hypothesis.  No scope inflation or other regression was found.

## Reconstruction recommendation

Do **not** begin strict proof-blind reconstruction from the present text.
First make C5's one-paragraph event split explicit and perform a short fresh
check that it says:

1. \(E\) is the union of **all** empirical multiplicative failures;
2. \(\Pr(E)\le\delta/2\);
3. zero counts trigger a total positive fallback, while positive inaccurate
   counts remain operational but are also charged to \(E\); and
4. only on \(E^c\) is the remaining \(\delta/2\) JSV guarantee invoked.

After that correction, no further mathematical issue identified by this
audit blocks strict proof-blind reconstruction.
