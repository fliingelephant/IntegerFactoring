# F229 self-audit

## Result

The packet is internally consistent after the checks below. Its status
remains **candidate**. No hostile audit, blind reconstruction, cross-family
audit, or human audit has run.

## Quantifier checks

1. The gap \(d\) is fixed once for the whole infinite family. It does not
   depend on \(p\), \(q\), \(N\), a history, or a sampler.
2. The bounded-gap theorem gives infinitely many gaps at most one absolute
   constant. Pigeonhole over the finitely many even gaps gives one fixed
   \(d\) attained infinitely often.
3. Every numerical-QP height and bank bound has logarithm \(o(n)\). Since
   \(d\) is fixed, \(H^d<p\) eventually.
4. The interval theorem is uniform over every integer \(H\ge2\), including
   history-dependent and extremely large \(H\). The history must choose
   \(H\) before the fresh conditional uniform sample.
5. The subgroup theorem grants exact uniformity. It does not claim that a
   QP random walk reaches that law.

## Algebra checks

1. Modulo \(p-1\), \(pq-1\equiv q-1=d\), not \(q\).
2. Modulo \(q-1\), \(pq-1\equiv p-1=-d\), not \(d\).
3. The negative exponent modulo \(q\) is legal only after the unit screen.
   Multiplication by \(-X^{-d}\) proves equality of the zero conditions.
4. Equality of the two gcds uses squarefreeness of \(N=pq\). No
   prime-power version is claimed.
5. A certified \(\ell^e\parallel A\) block on a global return forces both
   local order valuations to equal \(e\). Since the local orders divide
   \(d\), the block divides \(d\).
6. The cases \(X=0\), \(X=1\), a proper initial gcd, and the full initial
   gcd are separated explicitly.

## Probability checks

1. For a uniform interval, direct nonunit hits and roots of \(T^d-1\) are
   union-bounded separately. Overlap only reduces the true probability.
2. A degree-\(d\) polynomial over either prime field has at most \(d\)
   roots. No assumption about order independence is present.
3. If \(H^d<p\), the event is exactly absent. Otherwise
   \(H\ge p^{1/d}\), so the endpoint error \(1/H\) is still exponentially
   small because \(d\) is fixed.
4. A uniform finite-group element projects uniformly under a surjective
   homomorphism. The two CRT projections need not be independent.
5. The exact local subgroup return probability is
   \(\gcd(d,|G_r|)/|G_r|\).
6. Every \(B\)-smooth integer below the hidden prime gives a distinct
   element of the projected small-prime subgroup. This proves a lower bound
   on group size without assuming multiplicative independence of the small
   rational primes.
7. Numerical-QP union bounds preserve both exponential estimates because
   their logarithmic cost is \(o(n)\).

## Scope attacks

The following stronger readings are false or unsupported and are excluded.

1. **All small-prime words fail.** Not proved. A long nonuniform word can
   wrap modulo the hidden primes and may be biased toward the union of the
   local \(d\)-torsion sets.
2. **Uniform subgroup sampling is implementable in QP time.** Not claimed.
   It is granted as an idealized endpoint obstruction.
3. **A QP-length random walk is close to uniform.** Not claimed. No
   spectral gap or mixing theorem is used.
4. **Local small-prime orders are independent.** Not assumed. The subgroup
   proof uses only projection, cyclic root counts, and smooth-number
   density.
5. **The theorem handles arbitrary composites or prime powers.** It treats
   one infinite family of distinct balanced semiprimes, which is sufficient
   to refute universality of the named sampling laws.
6. **The theorem blocks other annihilators.** It is specific to
   \(A=N-1\) and its sound primary stripping stage.
7. **The fixed lcm ceiling alone is new.** P197 already gives
   \(D_N\mid q-p\) on bounded-gap pairs. F229's new content is the exact
   integer exponent collapse, deterministic height zero, uniform-interval
   law, and smooth-generated-subgroup law.
8. **Crossing the word-height threshold is progress.** It is only necessary.
   A useful source must additionally produce a selective divisibility event.

## Highest-risk points for hostile audit

1. Reconstruct both exponent reductions and the equality of gcds.
2. Check that every P197 primary block from a global return divides \(d\).
3. Check constants in the all-height interval bound, especially the
   transition at \(H^d=p\).
4. Verify the exact hypotheses and range of the P172 smooth-number estimate.
5. Check that \(\Psi(p,B)\) injects into the generated subgroup, including
   the endpoint \(p\).
6. Keep intermediate nonuniform word laws outside the theorem.

## Evidence

No computation, web search, remote run, random experiment, or numerical fit
was used. The proof uses the bounded-prime-gap theorem and the same
smooth-number estimate already imported and promoted in P165/P172.
