# F272 author self-audit

## Status

This is an author self-audit only. It does not raise the packet above
self-audited proof-only candidate status.

## Checks

1. **Set versus multiset.** \(D\) collapses equal absolute differences.
   The prime-mass proof remains valid after collapse. The output proof uses
   all nonzero ordered pairs, so duplicated values only add output.

2. **Signs.** Divisibility and prime factorization are applied to
   \(|s-t|\). No ordering assumption on \(S,T\) is needed.

3. **Zero.** Pairs with \(s=t\) are excluded. If zero were admitted as a
   witness, every divisor condition would be vacuous. No factorization of
   zero is requested.

4. **Primorial divisibility.** Each prime \(p\leq X\) divides at least one
   member of \(D\). Pairwise coprimality of distinct primes proves that the
   whole primorial divides the product of all distinct \(d\)'s. One cover
   value may carry many primes; this is already charged by its bit length.

5. **Binary length.** If \(d\) has at most \(L\) bits, then \(d<2^L\),
   which gives the strict upper bound in (6). Signed \(B\)-bit magnitudes
   yield differences below \(2^{B+1}\).

6. **QP quantifier.** The contradiction is along every unbounded sequence
   of \(X\). A fixed quasipolynomial in \(n_X=\Theta(\log X)\) is
   \(X^{o(1)}\). The constants cannot depend on \(X\) or the hidden
   factors.

7. **Output model.** An explicit factorization must print every distinct
   prime divisor in binary. Per-pair worst-case time bounds per-pair output
   length. An uncharged shared dictionary or nonuniform prime table is
   expressly outside the uniform explicit-output claim.

8. **Huge succinct values.** Theorem 1 does not apply when only a short
   circuit description is bounded. Theorem 2 still applies if complete
   prime lists must be printed. If both expansion and prime output are
   avoided, neither theorem claims a circuit lower bound.

9. **Prime pairs.** For \(p,q\in[a\sqrt X,b\sqrt X]\) and \(b\leq1\),
   one has \(pq\leq X\). A value \(d\leq H\) contains at most \(h\)
   distinct band primes. Repeated coverage makes the incidence sum larger,
   so (13) has the correct direction.

10. **Exponent bookkeeping.** Prime mass gives
    \(1\leq\alpha+2\beta\). Pair incidence gives
    \(1\leq2\alpha+2\beta\). Explicit output gives
    \(1\leq\gamma+2\beta\). No logarithmic factor changes these exponent
    inequalities.

11. **Rank scope.** The rank-free QP no-go applies when actual bit length or
    explicit prefactor output is QP. At the Umans--Wang one-third scale,
    the inequalities are tight and do not kill ranks two through six.
    He--Sahai is cited only for the cover set itself being one arithmetic
    progression.

12. **Factor-free construction.** The lower bounds do not assume knowledge
    of the factors of any input. They hold even for nonuniform existential
    choices of \(S,T\), so adding uniform construction requirements cannot
    evade them.

13. **Prime separation.** Pairwise separation means distinct divisibility
    codewords. At most one prime can be absent from every \(A_i\). The
    possible missing binary name costs at most \(\log_2X\), giving (21).

14. **Integer-factoring relevance.** The published one-third consequence
    is \(N^{1/6+o(1)}\), not QP in \(\log N\). F272 does not present an
    exponent improvement as progress toward the fixed theorem.

15. **Succinct seam.** The interval-factorial evaluator is stated as an
    exact missing interface, not as a lemma proved here. F197 shows that its
    full interval already exposes a balanced factor. The packet does not
    call the interface easier than factoring.

16. **General factoring reduction.** Section 6 is only a sketch explaining
    why the interface is strong enough and why it is outside the
    obstruction. It is not promoted as a complete all-input algorithm and
    is not needed for Theorems 1--3 or Corollaries 4--5.

## Result

No internal counterexample was found. The highest-risk audit points are the
scope of "explicit" prefactor output, the exact Umans--Wang height
translation, and any accidental reading of the rank-free QP obstruction as
a refutation of the critical higher-rank one-third conjecture.

