# F192 self-audit

## Verdict

The local-distinctness lemma, circular cluster lemma, lattice determinant,
factor vector, exact Dirichlet obstruction, and cyclic-order bank count are
elementary and internally consistent. This is a proof-only candidate for a
narrow standard-lattice obstruction. It is not a general ACD, lattice, or
factoring lower bound.

No mathematical computation was run. The frozen candidate requires a fresh
hostile audit. If that passes, it requires a statement-only blind
reconstruction before any durable promotion.

## Attacks checked

1. **Use of P164.** The proof uses only one certified P164 fact: every prime
   in every final local order sees each retained base \(a\) as a unit of
   order above \(K\). It does not infer independent action directions.

2. **Prime versus composite local order.** Equality of two power-word
   entries forces the full local order \(g_S\) to divide an exponent
   difference. Since \(a\) is coprime to every prime divisor of \(g_S\), it
   is coprime to \(g_S\). Any one prime divisor then contradicts the
   order-above-\(K\) condition.

3. **Endpoint \(R=K+1\).** Two indices in \(0,\ldots,K\) differ by at most
   \(K\). This is exactly the range excluded by
   \(\operatorname{ord}_\ell(a)>K\).

4. **Simultaneous distinctness.** The same public word is distinct modulo
   both hidden primes. This makes every chosen difference a unit modulo
   \(N\), not merely nonzero modulo the prime used for clustering.

5. **Circular wrap.** The cluster uses clockwise residues modulo the hidden
   prime. Reduction of the global difference modulo \(N\), followed by
   reduction modulo the hidden prime, gives the same clockwise residue.
   Wraparound therefore does not invalidate the approximate-multiple
   equation.

6. **Cluster size.** Summing all \(R\) arcs of \(m\) consecutive gaps counts
   every gap exactly \(m\) times. One arc has length at most \(mS/R\).
   No randomness or equidistribution is assumed.

7. **Hidden subset.** The theorem does not claim that the cluster indices
   are public. The lattice obstruction grants the correct subset, making it
   stronger than an obstruction caused only by outlier selection.

8. **Hidden error bound.** The exact value
   \(\lceil mP/R\rceil\) is not public without \(P\). The theorem allows any
   granted or public upper bound \(\widehat B\). Under fixed balance, a
   constant-factor public upper bound is available. The proof itself uses
   only (8).

9. **Choice of the larger prime.** Clustering is done modulo \(P\ge Q\).
   The factor-bearing lattice coefficient is therefore the smaller prime
   \(Q\). Every nonzero nonunit integer coefficient has magnitude at least
   \(Q\). This ordering is essential to the exact shortest-vector claim.

10. **Lattice convention.** The displayed rows form a full-rank triangular
    basis. Every lattice vector has the unique coefficient form (3.1), and
    the determinant is exactly \(\widehat B N^m\).

11. **Factor vector.** Multiplying \(z_i=Pt_i+r_i\) by \(Q\) produces
    \(Qz_i=Nt_i+Qr_i\). Thus \(v_Q\) is literally in the lattice; it is not
    only close to it.

12. **Determinant algebra.** Substituting
    \(N=PQ\) and \(\widehat B=\epsilon P\) gives the exact ratio
    \((Q\epsilon^m)^{1/(m+1)}\). No Gaussian or Minkowski heuristic is used.

13. **Dirichlet constant.** The pigeonhole proof uses \(H^m+1\) torus
    points and \(H^m\) boxes. The condition \(A\ge2^m\) gives
    \(H\ge A^{1/m}/2\), hence the factor two.

14. **Integer interval.** The theorem assumes an integer \(A\) in the open
    interval (14). It does not infer one merely from a weak real inequality.
    The asymptotic corollary has an exponential gap, so the interval
    contains an integer.

15. **Euclidean norm.** All \(D=m+1\) coordinates of the Dirichlet vector
    are strictly below \(Q\widehat B/\sqrt D\). Its Euclidean norm is
    therefore strictly below \(Q\widehat B\).

16. **Zero leading coefficient.** A nonzero vector with \(c=0\) has norm at
    least \(N\). Since \(\widehat B<Q\le P\), one has
    \(Q\widehat B<Q^2\le N\), so such a vector cannot be shortest after the
    Dirichlet vector is found.

17. **All factor-bearing coefficients.** Any nonzero \(c\) with
    \(\gcd(c,N)>1\) has \(|c|\ge Q\). Its first coordinate alone has length
    at least \(Q\widehat B\). This excludes every nonunit coefficient, not
    only \(c=Q\).

18. **Coordinate gcds.** For a shortest vector, \(c\), \(\widehat B\), and
    every \(z_i\) are units modulo \(N\). Subtracting \(Nk_i\) does not
    change a residue modulo either hidden prime. Thus every coordinate gcd
    with \(N\) is one.

19. **Polylogarithmic corollary.** Numerical-QP \(R\) has
    \(\log R=(\log n)^{O(1)}\). Multiplying by polylogarithmic \(m\) remains
    polylogarithmic and is \(o(n)\). Fixed balance gives
    \(\log Q=n/2+O(1)\).

20. **Subset-bank count.** A fixed \(s\)-subset is consecutive in a fraction
    \(R/\binom Rs\) of oriented cyclic orders. The union bound gives the
    stated necessary bank size. Independence is not assumed.

21. **Subset-bank scope.** The count concerns a bank that uses no
    information beyond an unknown cyclic label order. It does not prove
    that all cyclic orders are realizable by \(x_{j+1}=x_j^a\bmod N\), and
    it does not obstruct a selector that exploits that recurrence.

22. **No support overclaim.** A short unit coordinate might accidentally be
    divisible by a surviving local-order prime, since those primes are
    coprime to \(N\). F192 claims only that shortness supplies no proved
    support coverage. It does not claim that every short coordinate misses
    every order prime.

23. **No recursion objection.** A one-bit contraction would be enough for a
    single recursive chain. F192 instead shows failure of the named factor
    extraction from the exact shortest vector. It makes no recursion-depth
    claim.

24. **No algorithmic lower bound.** Different lattices, affine targets,
    robust outlier decoding, multivariate polynomial methods, and
    source-aware recurrence methods remain open. A different postprocessor
    of the same shortest vector is also not excluded. No complexity lower
    bound for SVP, ACD, or factoring is asserted.
