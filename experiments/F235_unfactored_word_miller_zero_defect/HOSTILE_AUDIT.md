# F235 focused hostile audit

## Verdict

PASS.  No counterexample or proof gap was found.

## Checks reconstructed

- If the two local two-adic valuations differ, zero defect forces their
  minimum to be at least `floor(n/2)`, and balance then gives `pq>2^n`.
  Thus the valuations are equal.
- The exponent contains the full local two-Sylow exponents.
- `gcd(E,p-1)=2^e D gcd(W,s_p)` is exact valuation by valuation, including
  overlap between `D` and `s_p`.
- Conditional global return restricts only odd coordinates.  Both local
  two-primary coordinates remain independent and uniform.
- The Miller chain splits exactly when their two-order exponents differ,
  giving `mu_e=(2/3)(1-4^(-e))` and the displayed total law.
- The `n`-th child powers saturate every supported residual prime power.
- Product construction, modular powering, the square chain, gcds, and exact
  uniform-unit rejection sampling have the claimed bit complexity.

This audit read the frozen statement and proof but not the self-audit or
provenance.
