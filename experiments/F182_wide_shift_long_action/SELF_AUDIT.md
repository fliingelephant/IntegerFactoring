# F182 self-audit

## Verdict

The two-menu filter and the double-identity contradiction are internally
consistent. Independent hostile audit and statement-only reconstruction are
required before promotion.

## Kill-first checks

1. **Both menus act on the same state.** The \(\mathcal B\) filter uses the
   original F181-rough unit \(w\), not the result of the \(\mathcal A\)
   filter. Otherwise double identity would not give two certificates for
   each original order prime.
2. **The menu filter is an OR on prime support.** A primary part is deleted
   if it is nonunit or has period at most \(K\) for at least one shift in
   the menu. A surviving primary part is therefore unit and long for every
   shift in that menu.
3. **Every primary multiplicity is removed.** The outer \(n\)-th power is
   sufficient because \(\ell^a\le g_j<N<2^n\) gives \(a<n\).
4. **Partial prime-power gcds are safe.** Every filtered order remains
   coprime to the hidden rational prime. Reduction to the prime field is
   injective on the filtered cyclic subgroup, so identity modulo the prime
   is equivalent to identity modulo the full hidden prime power.
5. **All cross gaps are valid.** The smallest gap is
   \((L+2)-(L-1)=3\), and the largest is \(2L+1\). The two complex unit
   circles are always disjoint.
6. **The case \(L=1\) is included.** The menus become \(\{0\}\) and
   \(\{3\}\), with gap three. No empty menu or zero resultant appears.
7. **Nonunit cases are included in the same proof.** Index zero is the
   linear polynomial \(X+\delta\). Linear/linear and linear/short
   resultants are explicit nonzero integers below \(T\).
8. **The roughness inequality is strict.** Every relevant order prime has
   \(\ell>T\), while every cross resultant has positive absolute value
   strictly below \(T\). Divisibility is impossible.
9. **The cap remains QP.** Although \(L\) is numerical QP, only \(\log L\)
   occurs in \(\log T\). Thus \(T=2^{(\log n)^{O(1)}}\).
10. **The exponent is encoded explicitly.** Its bit length, not only its
    arithmetic-expression size, is
    \(O(nLK^2(n+\log L))\), which is QP. No tetration or compressed unknown
    exponent is used.
11. **No hidden factorization occurs.** The algorithm builds evaluated
    integer factors \(C_\delta\), multiplies them, powers \(w\), and takes
    gcds. Resultants are proof witnesses only and are not factored.
12. **The surviving gate is explicit.** The theorem supplies no method to
    localize a rough order prime whose shifted public actions are all long.
    No all-input factoring conclusion is claimed.

## Computation

No mathematical computation was run. No durable result ledger was edited by
this candidate artifact.
