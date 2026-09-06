# F238 self-audit

## Checks

1. The base is a raw uniform unit.  Odd projection would erase the Miller
   signal and is not used.
2. The identity `gcd(N-1,p-1)=gcd(q-1,p-1)` is exact and does not use
   balance or zero defect.
3. The residuals `s_p,s_q` are coprime but need not both be odd.  The
   statement does not call them odd residuals.
4. When the local two-adic valuations differ, conditioning leaves a
   uniform element of a possibly proper two-primary kernel.  The proof
   uses `h_i=min(v2(p_i-1),v2(E))`, not the full local two-Sylow exponent.
5. Both `h_i` are at least one because `N-1` and each `p_i-1` are even.
6. The exact unequal-kernel formula was derived from the full order-exponent
   distributions.  It specializes to the F235 equal-kernel formula.
7. The Miller chain tests both signs at every displayed square.  Its
   success event is exactly inequality of the local two-order exponents.
8. Formula (3) counts disjoint exclusive-return and global-return atoms.
   It is exact only in the squarefree semiprime theorem.
9. The bound `S>=mu max(alpha_p,alpha_q)` handles the negative-coefficient
   case in (P10) by reversing the inequality correctly.
10. Repeated prime powers can make the first gcd proper even when every
    reduction modulo `p_i` returns.  The multi-support extension therefore
    states a lower bound, not an exact total formula.
11. The theorem does not require the algorithm to know any hidden residual,
    local valuation, or success probability.  They are analysis variables.
12. No factorization of `W` is used.  Complexity depends on its binary
    length, not on the number or sizes of its prime factors.
13. Unit sampling is implementable by gcd rejection.  Encountering a
    nontrivial nonunit already factors `N`.
14. The result is still conditional.  It does not construct a QP-bit word
    that reduces one hidden residual on every input.
15. Randomness amplifies certified word progress.  It does not make a
    uniformly random QP-bit integer likely to contain a large hidden prime.

## Status

Self-audited only.  A fresh hostile audit and a strict statement-only
reconstruction are required before promotion.
