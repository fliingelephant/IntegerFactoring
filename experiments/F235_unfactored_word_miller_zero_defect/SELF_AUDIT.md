# F235 self-audit

## Checks

1. The base is a raw uniform unit.  Odd projection would remove the Miller
   signal, so it is not used.
2. The return law includes the full factors `2^e D` in `N-1`; only the
   exclusive residual `s_p,s_q` remains.
3. The proof establishes `v2(p-1)=v2(q-1)` from zero defect and balance.
   The Miller formula would still have a positive variant without equality,
   but the displayed exact formula uses equality.
4. Conditioning on `x^E=1` does not bias the two-primary coordinate because
   `2^e|E`.  The odd and two-primary coordinates are independent in each
   cyclic local unit group.
5. A global return is checked before the Miller chain.  The method never
   assumes an unverified annihilator.
6. Formula (4) counts exclusive returns plus the conditional Miller success
   on the global-return atom.  These events are disjoint.
7. Factorization of `W` is unnecessary.  The route obtains only a direct
   factor, not a P197 common-order certificate.
8. `W_K` has `O(nK^2)` bits, not `O(nK)` bits.
9. Child powers use exponent `n`, which dominates every primary exponent in
   an integer smaller than `N`.
10. The all-input meta-order bound is not claimed.  Long/high meta-orders
    remain a live obstruction.

## Status

Self-audited only.  A fresh hostile audit and a proof-blind reconstruction
are required before promotion.
