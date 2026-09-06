# F183 self-audit

## Verdict

The wide small-base filter, fully factored extinction branch, and cost bound
are internally consistent. Independent hostile audit and statement-only
reconstruction are required before promotion.

## Kill-first checks

1. **Every \(C_a\) is genuinely small enough to factor.** Its bit length is
   \(O(K^2\log L)=(\log n)^{O(1)}\). Trial division is exponential only in
   that polylogarithmic bit length, hence QP in \(n\).
2. **There are QP many bases.** Multiplying the per-base cost by
   \(L=2^{(\log n)^{O(1)}}\) remains QP.
3. **Duplicate factors are not discarded.** All valuations within and
   across the \(C_a\) are summed. The full factorization of \(P^n\) is
   exact.
4. **The outer exponent removes full primary parts.** Every
   \(\ell^e\parallel g_j\) has \(e<n\), while one occurrence of \(\ell\)
   in \(P\) becomes at least \(n\) occurrences in \(P^n\).
5. **Partial prime-power gcds are safe.** Every filtered order remains
   coprime to the hidden rational prime. Identity modulo that prime is
   equivalent to identity modulo the full hidden prime power.
6. **The global identity uses the original unit.** Factor-first stripping
   recovers the order of \(w\), not the order-one descendant \(z\).
7. **The common order is above the cap.** This follows from F181 roughness:
   every \(g_j\) has a prime divisor above \(T\).
8. **Factor-first synchronization is explicit.** A proper gcd separates.
   If no proper gcd occurs, every retained prime valuation of the final
   annihilator occurs in every local order, so all local orders are equal.
9. **Nonunit bases are covered.** The factor \(a\) in \(C_a\) deletes a
   primary supported on \(\ell\mid a\). On the rough branch this cannot
   occur because \(\ell>T\ge L+1\), but the exact formula includes it.
10. **The exponent is explicit.** It has \(O(nLK^2\log L)\) bits. No
    compressed exponent, unknown order reduction, or tetration is used.
11. **No factorization oracle is hidden.** Trial division is applied only
    to integers with polylogarithmic bit length. It is not applied to
    \(N\), \(N+\delta\), or an \(n\)-bit hard value.
12. **The final gate remains.** A rough order prime can give every small
    public base a long multiplicative order. The theorem does not rule this
    out and does not claim QP factoring.

## Computation

No mathematical computation was run. No durable result ledger was edited by
this candidate artifact.
