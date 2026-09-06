# F181 self-audit

## Verdict

The rough-order normalization and the nonunit-free shift corollary are
internally consistent. Independent hostile audit and statement-only
reconstruction are required before promotion.

## Kill-first checks

1. **Large prime power is not the same as large prime support.** The new
   exponent is \(\Lambda_T^n\), not \(\Lambda_T\). Its \(n\)-th power
   supplies enough valuation to remove a primary part such as \(2^a>T\).
2. **The outer exponent is sufficient.** Every \(\ell^a\parallel f_j\)
   satisfies \(a<n\), including orders modulo repeated prime powers.
3. **The identity branch uses the original unit.** When \(w=1\), the
   returned state is \((y,m)\). Returning \(w\) would give order one.
4. **The annihilator is fully factored.** The sieve gives the complete
   factorization of \(\Lambda_T^n\). No unfactored value such as
   \(N^k-1\) is passed to exact-order stripping.
5. **Factor-first synchronization is explicit.** A proper gcd separates.
   If every divisor test is zero or global, the final retained valuation of
   each prime occurs in every local order, so all local orders equal the
   final \(m\).
6. **The common order is large.** This uses the inherited P160 premise
   \(\sigma(f_j)>T\). Without that premise, the exact common order on the
   identity branch need not exceed \(T\).
7. **The rough branch is nontrivial componentwise.** If only some local
   rough parts vanished, \(\gcd(w-1,N)\) would be proper. The branch
   \(H=1\) makes every \(g_j\) nontrivial.
8. **Prime-power gcd behavior is safe.** Since each \(g_j\) is coprime to
   the hidden rational prime, reduction to the prime field is injective on
   \(\langle w\rangle\). Identity modulo the rational prime is equivalent
   to identity modulo the full hidden prime power.
9. **The cost is in the input length.** The exponent has
   \(O(nT\log T)\) bits, and the number of stripping tests is polynomial in
   \(n,T,\log T\). A fixed numerical QP value of \(T\) preserves QP cost.
10. **The shift-three nonunit case is deleted, not reclassified.** The
    explicit factor \(N+3\) in \(B_3\) removes every primary part whose
    supporting prime divides \(N+3\).
11. **Double identity still has a factored closure.** A nonunit supporting
    prime divides one small \(S_k\). A unit supporting prime divides one
    nonzero F180 resultant. The outer \(n\)-th power restores all
    multiplicities.
12. **The remaining gate is still stated.** Neither theorem forces a
    long-action rough primary part to disappear. No QP factoring theorem is
    claimed.

## Computation

No mathematical computation was run. No durable result ledger was edited by
this candidate artifact.
