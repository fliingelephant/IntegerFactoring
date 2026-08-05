# F22 — real-quadratic infrastructure metric kill-first analysis

**Status:** self-audited symbolic result. No computation was run, so there is
no computation-ledger entry or run manifest.

## Outcome

The route does **not** currently give a factoring algorithm.  It does give a
materially new and exact boundary:

1. Real infrastructure arithmetic really does retain a metric coordinate and
   supports long composition jumps.  Exact arithmetic and distance precision
   are not, by themselves, the obstruction.
2. The bare principal cycle need not contain any proper SQUFOF square, even if
   one traverses the whole cycle.  There is an infinite explicit composite
   family for which the cycle has only two reduced forms and every individual
   form coefficient is coprime to the input.
3. Class-group composition alone forgets the metric coordinate; retaining the
   infrastructure coordinate changes the problem into locating a marked point
   on a circle of unknown circumference.  The standard exact regulator and
   equivalence algorithms pay a square-root-in-the-regulator search cost.
4. Racing multipliers and treating proper-square occurrences as memoryless
   lucky events has only heuristic/average support.  A polynomial-time retry
   proof needs a new uniform multiplier theorem or a joint decoder that extracts
   information before any individual proper-square hit.

This closes the literal “build the principal infrastructure, jump to a
square/ambiguous form, and apply the standard single-form extraction”
mechanism.  It does not close
multiplier-changing constructions, arithmetic decoders combining many
non-square forms, or arbitrary real-quadratic methods.

## Prior-route check

The closest prior route is **X21/P27 (family F16)**, exact-iid ambiguity hunting
in imaginary quadratic class groups.  The material difference is that a real
quadratic class contains an ordered cycle of reduced representatives with an
injective distance coordinate in a circle of circumference the regulator.
Composition and reduction can therefore make metric giant steps between
representatives which collapse to the same ordinary ideal class.  P27's finite
class-group occupancy calculation does not apply to this ordered
infrastructure.

The closest metric route is **F15/P26/P29**, but those results concern additive
approximations to the factor trace and an Eisenstein divisor-sum coefficient.
The present observable is the continued-fraction/infrastructure distance and
its marked reduced representatives; it is neither a computation in
\(\mathbb Z/N\mathbb Z\) nor a final-gcd polynomial invariant.

## 1. Exact setup and what composition really preserves

Let \(\mathcal O_\Delta\) be a real quadratic order of positive nonsquare
discriminant \(\Delta\), let \(R=\log\varepsilon\) be its regulator, and let
\(\mathcal R_\Delta\cap\mathcal P\) denote the reduced principal fractional
ideals.  If \(\mathfrak a=(\alpha)\), its infrastructure distance is

\[
d(\mathcal O_\Delta,\mathfrak a)
 = \frac12\log\left|\frac{\sigma(\alpha)}{\alpha}\right|\pmod {R}.
\]

The distance map is injective on the reduced principal ideals, while all of
those ideals are the identity in the ordinary ideal class group.  Therefore:

- ordinary class-group arithmetic erases all positions in the principal cycle;
- ideal multiplication followed by reduction can retain the positions because
  infrastructure distances add modulo \(R\);
- repeated squaring really can double a known distance.  It is incorrect to
  dismiss the route merely by saying that reduction destroys every distance.

For adjacent reduced ideals, the standard exact bounds are

\[
 \frac1{\sqrt\Delta}<d_i<\frac12\log\Delta,
 \qquad d_i+d_{i+1}>\log2. \tag{1}
\]

Thus \(O(\log\Delta)\) bits of separation suffice to distinguish neighboring
positions.  Moreover, exact algorithms avoid expanding a fundamental unit:
they retain reduced ideals and a power-product representation of the relative
generator.  Each ideal multiplication/reduction has polynomial bit cost in
\(\log\Delta\).  Buchmann and Vollmer's exact Terr algorithm has the proved
time and space bound

\[
 O\!\left((\log\Delta+\sqrt R)(\log\Delta)^2\right). \tag{2}
\]

Consequently, uncontrolled floating-point precision and immediate coefficient
blowup are **not** valid kill claims for a polynomial number of infrastructure
operations.  The standard exact way to learn the circumference or solve an
equivalence/logarithm problem instead pays the \(\sqrt R\) search term in (2).
Equation (2) is an upper bound for that specified algorithm, not a lower bound
against every possible real-quadratic algorithm.

## 2. An infinite principal-cycle counterfamily

### Theorem 1 (complete two-form cycle with no proper square)

For every integer \(t\ge1\), put

\[
a=6t+1,
\qquad N=a^2+2=3(12t^2+4t+1).
\]

Then \(N\) is an odd composite with \(N\equiv3\pmod4\), and

\[
 \sqrt N=[a;\overline{a,2a}]. \tag{3}
\]

The principal cycle of forms of discriminant \(4N\) therefore has length two.
With the sign convention of the cited SQUFOF recurrence, its two forms are

\[
 F_+=(1,2a,-2),\qquad F_-=(-2,2a,1).
\]

In the standard continued-fraction notation its complete denominators alternate

\[
 Q_0=1,\quad Q_1=2,\quad Q_2=1,\quad Q_3=2,\ldots. \tag{4}
\]

and the noninitial complete numerators are all \(P_i=a\).  Hence:

1. the only square complete denominator is \(1\), which gives an improper
   square form and only a trivial factorization;
2. no proper square form occurs anywhere in the principal cycle;
3. every coefficient of every form in the cycle, up to sign, belongs to
   \(\{1,2,2a\}\), so every individual coefficient has gcd one with \(N\);
4. arbitrary form composition followed by reduction, as long as it stays in
   the principal class of this same discriminant, can only return one of these
   two reduced forms and cannot repair (1)--(3).

The smallest squarefree certificate in the family is

\[
 t=1,\quad a=7,\quad N=51=3\cdot17,\quad \Delta=204. \tag{5}
\]

### Proof

Because \(a^2<N<(a+1)^2\), the integer part of \(\sqrt N\) is \(a\).  Apply
the exact continued-fraction recurrence

\[
P_{i+1}=q_iQ_i-P_i,
\qquad
Q_{i+1}=\frac{N-P_{i+1}^2}{Q_i},
\qquad
q_{i+1}=\left\lfloor\frac{a+P_{i+1}}{Q_{i+1}}\right\rfloor
\]

from \((P_0,Q_0,q_0)=(0,1,a)\).  It gives

\[
(P_1,Q_1,q_1)=(a,2,a),
\qquad
(P_2,Q_2,q_2)=(a,1,2a),
\]

and the first state then repeats.  This proves (3) and (4).  The forms in the
principal cycle have, up to the conventional signs,

\[
 F_i=(\mathord{\pm}Q_{i-1},2P_i,\mathord{\pm}Q_i),
\]

so their coefficients have the asserted values.  Since \(a\) and \(N\) are
odd and

\[
\gcd(a,N)=\gcd(a,a^2+2)=\gcd(a,2)=1,
\]

each coordinate gcd is trivial.  SQUFOF tests the appropriate \(Q_i\) for
squareness; \(2\) is not a square and \(Q_i=1\) yields the trivial square root,
so no proper square exists.  Finally, composition preserves the proper ideal
class, and reduction chooses a reduced representative in that class.  The
principal class has exactly the displayed two-form cycle, proving the last
claim. \(\square\)

### Scope of the counterexample

This theorem refutes the auxiliary claims that every composite input has a
proper square, or an ambiguous representative useful to the standard
single-form extraction, in its bare principal cycle, or that sufficiently
clever binary jumping within that cycle must find one.  It is stronger than a
polynomial-query miss: full traversal does not help.

It is **not** a factoring lower bound.  The displayed family itself has the
small factor \(3\), and an algorithm may use arithmetic combinations of several
forms rather than a single coefficient or proper-square trigger.  Changing the
discriminant with a multiplier also leaves the theorem's scope.

### Two priority hostile-audit targets

1. **Cycle convention.**  Recheck that period length two in (3), together with
   the exact \(F_i\)-formula used above, gives the complete reduced principal
   form cycle \(F_+,F_-\) for discriminant \(4N\) under the stated signs and
   proper-equivalence convention.  The recurrence proves the periodic data;
   this convention bridge is the first place an indexing or orientation error
   could narrow Theorem 1.
2. **Intermediate transcript.**  Item 4 of Theorem 1 concerns the *reduced
   endpoint* and the standard proper-square/single-reduced-form trigger only.
   It does not analyze unreduced composition coefficients, reduction quotients,
   relative generators, power-product data, or relations among several such
   intermediate objects.  A decoder using that richer transcript would evade
   the individual-reduced-coefficient scope and remains open.

## 3. SQUFOF does not supply the required probability theorem

For squarefree \(N\equiv2,3\pmod4\), standard SQUFOF uses the principal cycle
of discriminant \(4N\), searches for a reduced square form, takes an inverse
square root under composition, and follows the resulting cycle to an ambiguous
form.  Once the symmetry condition is reached, the exact recurrence gives

\[
 N=S_m\left(S_{m-1}+S_m\frac{t_m^2}{4}\right), \tag{6}
\]

so a claimed factor is checked by integer division.  With a multiplier \(k\),
the extracted divisor may belong partly or wholly to \(k\), so the safe output
rule is

\[
 g=\gcd(d,N),\qquad\text{return only if }1<g<N. \tag{7}
\]

This makes every returned output certifiable; it does not prove that an output
will occur quickly.

The standard binary-form description permits \(4\lfloor\Delta^{1/4}\rfloor\)
forward reductions before giving up.  A reduction uses only
\(O(\log\Delta)\)-bit coefficients, but \(\Delta^{1/4}\) reductions are
exponential in the binary input length.  More importantly, the published
average \(\Theta(N^{1/4})\) analysis explicitly:

- omits inputs whose principal cycle has no proper square;
- assumes an average spacing law for square forms;
- assumes a square root lands uniformly among ambiguous forms;
- assumes an average queue-density law;
- treats racing multipliers through an experimentally motivated exponential,
  memoryless model.

Those assumptions are useful descriptions of SQUFOF, but none is a per-input
inverse-polynomial success bound.  Replacing a sequential walk by
baby-step/giant-step reduces a cycle/order search to a square-root-scale search;
it does not by itself turn it into \(\operatorname{poly}(\log N)\) work.

## 4. What “amortize many lucky relations” must add

The following elementary lemma isolates the difference between merely pooling
rare hits and a genuine joint decoder.

### Lemma 2 (generic shifted-marker union bound)

Let \(C=\mathbb Z/L\mathbb Z\), let \(M\subset C\) have \(|M|=s\), and hide
the translated marked set \(M+\tau\) with uniform \(\tau\in C\).  An adaptive
algorithm may perform arbitrary \(\tau\)-independent group arithmetic and make
at most \(T\) membership tests of positions of its choice.  It learns a factor
only upon a positive membership test.  Then

\[
 \Pr(\text{success})\le \min\!\left(1,\frac{Ts}{L}\right). \tag{8}
\]

If \(K\) sampled positions generate at most \(T\le K^2\) explicitly tested
sums, differences, or pair relations, their total success is at most
\(K^2s/L\).

**Proof.**  Fix the algorithm's random coins and follow its all-negative
transcript.  This fixes all queried positions \(x_1,\ldots,x_T\).  A first
positive answer can occur only when

\[
 \tau\in\bigcup_{i=1}^T(x_i-M),
\]

a set of size at most \(Ts\).  Divide by \(L\), then average over the coins.
\(\square\)

This is a theorem about the stated generic model, **not** a lower bound for
actual quadratic infrastructures: actual form coefficients may leak structured
information about the untranslated target.  Its consequence is narrower and
decisive for retry design.  Accumulating many independently sparse
proper-square tests, or all pairwise tests among them, is still a union of lucky
events.  A materially new amortized mechanism must specify an arithmetic joint
decoder whose transcript from *unmarked* forms narrows the factor or target
distance.

## 5. Exact multiplier/restart criterion

A multiplier-based Las Vegas retry would have to specify, from bare \(N\), a
distribution over multipliers \(k\) and query/composition plans satisfying all
of the following uniformly for every unresolved composite \(N\):

1. \(\log k\), every reduced-form coefficient, every stored distance
   representation, and the number of infrastructure operations are bounded by
   one fixed polynomial in \(n=\lceil\log_2(N+1)\rceil\);
2. compute \(\gcd(k,N)\) first and immediately verify any factor it gives;
3. use (7) and divisibility to verify every factor extracted from \(kN\);
4. prove either a per-restart success probability at least \(1/P(n)\) for one
   fixed polynomial \(P\), or an equivalent direct expected-work bound;
5. prove the bound without assuming independence between multiplier cycles,
   uniform square-form locations, a known regulator, a smooth regulator/period,
   or a supplied factorization of the discriminant beyond the public
   multiplier.

No such bound follows from SQUFOF's multiplier heuristics or from the generic
ability to make infrastructure giant steps.  This is the exact missing lemma,
and at present it is as strong as the proposed factor-localization task rather
than a completed reduction.

## 6. Classification and precise retry boundary

**Classification:** method failure for the bare principal-cycle
proper-square/ambiguous-hit mechanism, ordinary sequential SQUFOF as a
polylogarithmic algorithm, exact regulator BSGS as a claimed polylogarithmic
subroutine without an additional regulator bound, and multiplier racing whose
success proof is only the standard memoryless heuristic.  Theorem 1 is
evidence against the exact auxiliary claim that the unmultiplied principal
cycle always contains a useful target.  It is not evidence against arbitrary
real-quadratic algorithms.

**A retry is materially new only if it supplies at least one of:**

- a factor-free multiplier distribution or deterministic list with a proved
  per-input inverse-polynomial useful-target probability;
- a computable target distance or interval of inverse-polynomial relative
  measure that does not assume the regulator, period, factorization, or an
  equivalent oracle;
- a joint decoder combining polynomially many non-square forms so that negative
  and unmarked transcripts accumulate factor information, rather than merely
  creating polynomially many additional lucky-hit tests;
- a factor-revealing composition/reduction failure outside the principal class;
- a proof that a different real-quadratic observable (not just proper square or
  ambiguity) has inverse-polynomial factor-bearing mass and polynomial bit cost.

## Sources used

- Johannes Buchmann and Ulrich Vollmer, [“A Terr algorithm for computations in
  the infrastructure of real-quadratic number
  fields”](https://doi.org/10.5802/jtnb.558), *Journal de théorie des nombres de
  Bordeaux* 18 (2006), 559--572.  Used for the exact distance map, neighbor-gap
  bounds, power-product representation, and the
  \(O((\log\Delta+\sqrt R)(\log\Delta)^2)\) exact bit bound.
- Jason E. Gower and Samuel S. Wagstaff, Jr., [“Square Form
  Factorization”](https://homes.cerias.purdue.edu/~ssw/squfof.pdf), *Mathematics
  of Computation* 77 (2008), 551--588.  Used for the exact SQUFOF recurrence,
  square-root/ambiguous-form extraction, multiplier handling, and—critically—the
  paper's explicit scope exclusions and heuristic assumptions.
- S. McMath, F. Crabbe, and D. Joyner, [“Continued fractions and Parallel
  SQUFOF”](https://arxiv.org/abs/math/0601263), for the two-sided-cycle and
  infrastructure-distance background.  No complexity claim in this report
  depends on its parallel-performance discussion.
