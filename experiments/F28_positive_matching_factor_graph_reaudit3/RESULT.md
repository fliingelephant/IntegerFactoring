# Post-C5 hostile re-audit of F28 — positive perfect-matching factor graph

**Candidate audited:**
`experiments/F28_positive_matching_factor_graph_kill/RESULT.md`.

**Prior audits read:**
`experiments/F28_positive_matching_factor_graph_audit/RESULT.md`,
`experiments/F28_positive_matching_factor_graph_reaudit/RESULT.md`, and
`experiments/F28_positive_matching_factor_graph_reaudit2/RESULT.md`.

**Scope of this pass:** the C5 repair and any regression it exposes in the
empirical-initialization event, the zero-count fallback, positive inaccurate
updates, total variation, totality, exact fair-coin simulation, and the
expected full-recursion cost.

**Computation:** none.  This audit is symbolic.

## Verdict

> **CLEAN PASS.**

C5 is repaired correctly.  The candidate now charges the union of **all**
empirical multiplicative-estimation failures to one event \(E\), including
positive inaccurate estimates that the implementation cannot detect.  The
zero-count branch is only an operational guard and is correctly treated as a
subevent of \(E\), not as the whole bad event.  On \(E^c\), the JSV invariant
and the allocated mixing/final-sampling error apply; on \(E\), positivity and
the bounded fallback guarantee an actual perfect matching but no useful
distribution.  The resulting convexity calculation gives the claimed total
variation bound.

The bad event does not create a hidden runtime problem.  Every positive
inaccurate count ratio still has polynomial bit length, every transition
probability remains an exactly represented rational, and the number of
specified transitions is polynomial.  Exact rational coins terminate almost
surely with uniformly polynomial expected bit cost.  Fresh complete
invocations then give the stated geometric success and expected-cost bounds
without requiring cost to be independent of success within the same trial.

No newly exposed mathematical or complexity flaw was found.  The candidate
is ready for strict proof-blind reconstruction.

## 1. The full empirical failure event is now the right event

Let the empirical estimates, in their actual adaptive order, be
\(Z_1,\ldots,Z_K\), where

\[
  K=O(m^5\log m).
\]

For each executed estimate, “good” means that it lies in the multiplicative
interval required by the JSV refinement argument.  The candidate now defines

\[
  E=\{\text{at least one executed estimate is not good}\}.
\]

This is a mathematical analysis event; the algorithm need not recognize it.
The empirical sample sizes are chosen so that, conditional on all preceding
estimates being good, the probability that the next estimate is the first
failure is at most the assigned per-estimate budget.  Therefore the standard
first-failure union bound gives

\[
  \Pr(E)
  =\sum_{j\le K}\Pr(Z_j\text{ is the first failure})
  \le \delta/2.
  \tag{1.1}
\]

This remains valid even though, after a previous bad estimate, later weights
need not satisfy the inverse-polynomial sector-mass invariant.  Once a
previous failure has occurred, the run is already in \(E\), so no later
conditional concentration bound is needed.  This is the precise adaptive
reading of the candidate's union-bound sentence.

The C5 flaw in the previous version was that it substituted the detectable
zero-count event for \(E\).  The corrected text no longer does that.  A pair
of positive empirical counts may yield an inaccurate ratio; that path is now
explicitly included in \(E\), despite being operationally indistinguishable
from a good path.

## 2. Zero counts are a safe detectable subevent

Suppose a required empirical count is zero.

* If all earlier estimates were good, the relevant true sector has the
  positive mass supplied by the current JSV invariant.  Zero is outside its
  promised positive multiplicative interval, so the current estimate is a
  failure and \(E\) occurs.
* If an earlier estimate was already bad, then \(E\) has already occurred.

Thus every zero-count branch lies inside \(E\), including in the adaptive
execution.  The candidate's response is total and positivity preserving: it
does not form the ratio, retains the preceding positive rational weights,
and returns the deterministically known perfect matching through the bounded
fallback.  There is no division by zero, no zero denominator in a later
Metropolis ratio, and no malformed output.

The known fallback is available because the splitter deterministically finds
a perfect matching before invoking the sampler.  Under the graph hypothesis,
such a matching exists on every composite node.  Returning this matching on
a bad initialization path may be maximally biased, but it remains a valid
perfect matching and is fully charged to \(E\).

## 3. Positive inaccurate paths are operationally harmless

On \(E\), it is also possible that every required empirical count is
positive.  The implementation then continues because it cannot test whether
the ratio is accurate.  This does not compromise correctness or complexity.

1. Every update multiplier is a ratio \(c_1/c_2\) with
   \(1\le c_1,c_2\le S\), where \(S\) is the fixed polynomial sample count.
   Multiplication by that ratio preserves strict positivity.
2. After at most \(P=O(m^3\log m)\) updates, each unreduced stored numerator
   and denominator has gained at most \(O(P\log S)\) bits.  Accuracy is not
   used in this operand-length bound.
3. Products, sums, comparisons, and Metropolis minima formed from these
   rationals therefore still have polynomial bit length.  Fraction-reducing
   gcds are unnecessary.
4. The bounded JSV wrapper performs a polynomially prescribed number of
   trials and returns either a perfect matching reached by the chain or the
   known fallback perfect matching.  Bad weights can spoil the output law,
   but they cannot make the wrapper output a nonmatching.

Hence all-positive inaccurate paths have an arbitrary but valid output law
and polynomial expected execution cost.  No accuracy detector is missing
from the algorithm.

## 4. The total-variation split is now rigorous

Let \(U\) be the uniform law on the perfect matchings of the input graph,
let \(p=\Pr(E)\), and let \(\mu_0,\mu_1\) be the output laws conditional on
\(E^c\) and \(E\), respectively.  Future sampling coins can be taken fresh
after the empirical initialization.  For every good realized sequence of
weights, the cooling invariant holds at every phase and the configured JSV
mixing/final-sampling analysis gives

\[
  d_{\mathrm{TV}}(\mu_0,U)\le\delta/2.
  \tag{4.1}
\]

This remains true after mixing over all good realized weight sequences,
because total variation is convex.  No bound is assumed for \(\mu_1\) beyond
the universal \(d_{\mathrm{TV}}(\mu_1,U)\le1\).  Since

\[
  \mu=(1-p)\mu_0+p\mu_1,
\]

another application of convexity and (1.1) yields

\[
\begin{aligned}
  d_{\mathrm{TV}}(\mu,U)
  &\le (1-p)d_{\mathrm{TV}}(\mu_0,U)
       +p d_{\mathrm{TV}}(\mu_1,U)\\
  &\le (1-p)\frac{\delta}{2}+p\\
  &\le \frac{\delta}{2}+\Pr(E)\\
  &\le\delta.
\end{aligned}
  \tag{4.2}
\]

This is exactly the split that C5 required.  In particular, (4.2) charges
positive inaccurate estimates even though the implementation continues on
them.

## 5. Exact fair coins and total invocation cost

The rational implementation remains sound on good and bad empirical paths.
All activities are positive rationals with polynomial bit length.  Section 3
above gives the same pathwise bit-length bound for every retained hole
weight.  Consequently every primitive probability has a representation
\(a/b\) with polynomially many bits.

The deterministic cases \(a=0\) and \(a=b\) use no random bits.  For
\(0<a<b\), rejection from the next power-of-two range accepts a proposal
round with probability \(b/2^{\lceil\log_2b\rceil}>1/2\).  Therefore the
coin has the exact requested bias, terminates almost surely, and uses fewer
than two rounds in expectation.  Its expected fair-bit and arithmetic cost
is polynomial in \(\log b\).  The same reasoning handles exact uniform
finite proposals.

There are only polynomially many prescribed empirical samples and Markov
transitions in one complete invocation.  A conditional-expectation sum over
those primitive calls gives one polynomial expected bit and fair-bit bound

\[
  R_{\rm exp}(m,\ell)=\operatorname{poly}(m,\ell)
\]

uniformly over good, zero-count, and all-positive inaccurate paths.  A finite
collection of almost-surely terminating rational-coin loops terminates
almost surely.  Thus a complete invocation terminates almost surely.

The candidate's phrase that the algorithm is “defined on every random-bit
stream” is correctly read as absence of an undefined arithmetic branch.  An
exceptional infinite rejection stream may fail to halt, as any rejection
sampler can, and the report accurately claims almost-sure rather than
worst-case termination.  There is no contradiction or missing Las Vegas
condition here.

## 6. Fresh invocation and full Las Vegas recursion

At \(\delta=1/12\), (4.2), contraction under the decoder, and equal witness
multiplicity leave nontrivial-factor probability at least

\[
  \frac13-\frac1{12}=\frac14
\]

for every complete invocation at a composite node.  Every invocation uses
fresh coins and reruns the whole initialization, so after any history of
rejected trivial witnesses the next conditional success probability is
still at least \(1/4\).

Let \(C_i\) be the random cost of invocation \(i\), and let \(T\) be the
first successful invocation.  The event \(\{T\ge i\}\) depends only on
earlier invocations and is independent of the fresh cost \(C_i\).  Cost may
be correlated with success in invocation \(i\); no independence of those
two same-trial quantities is needed.  Hence

\[
\begin{aligned}
  \mathbb E\!\left[\sum_{i=1}^{T} C_i\right]
  &=\sum_{i\ge1}\mathbb E[C_i\mathbf1_{\{T\ge i\}}]\\
  &\le R_{\rm exp}\sum_{i\ge1}(3/4)^{i-1}\\
  &=4R_{\rm exp}.
\end{aligned}
  \tag{6.1}
\]

This validates the candidate's conditional-expectation/Wald statement.
Verification makes every accepted split correct, irrespective of the
sampler's internal bad event.  The number of prime leaves, with
multiplicity, is at most the input bit length, so the recursion tree has a
deterministic \(O(n)\) node bound.  Linearity of expectation then gives the
claimed polynomial expected bit and fair-random-bit complexity for the full
all-input recursion, and the finite tree terminates almost surely.

## 7. Regression and reconstruction recommendation

The C5 edit is confined to the sampler's analysis.  It does not alter the
equal-multiplicity graph hypothesis, the divisor-mass calculation, the
matching-support/delta-matroid theorem, the direct gadget witnesses, the
Valiant scope statement, or the listed open global mechanisms.  The earlier
C1--C4 repairs remain present.

No further correction is required.  A strict proof-blind reconstruction may
now test whether the conditional factoring reduction and the local support
boundary can be recovered independently.
