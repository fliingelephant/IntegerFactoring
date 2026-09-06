# F231 self-audit

## Mathematical checks

1. The exact useful probability is computed after conditioning on a unit.
   Sampling from `1,...,N-1` first can only add a proper-factor event.
2. The no-progress classification is exhaustive for the declared decoder.
   If neither local order divides `A`, no divisor of `A` can return locally.
   If both divide `A`, complete factor-first stripping factors exactly when
   their primary valuations differ and otherwise returns their common exact
   order.
3. The stale count uses `phi(d)^2`, not `phi(d)`.  The CRT coordinates are
   independent, and each cyclic group contains `phi(d)` elements of exact
   order `d`.
4. Every `d|M` divides `A` because `M|D|H`.  Thus every pair counted in the
   stale term is genuinely a global return.
5. `D` and `s_p` need not be coprime.  The valuation proof of (P1) handles
   a prime that occurs both in `D` and in one residual quotient.
   In contrast, `r_p` and `r_q` are coprime because they divide the coprime
   integers `s_p` and `s_q`.
6. The powered word `Lambda_Y^n` is necessary for arbitrary small-prime
   powers.  The unpowered lcm only contains prime powers at most `Y` and
   would not annihilate every `Y`-smooth integer below `N`.
7. The favorable theorem assumes only prime support at most `Y`; the hidden
   residual may have exponential numerical value.  The algorithm never
   enumerates values up to that residual.
8. If one return kernel is full, every sample has at least one local return.
   The only no-progress outcome is therefore the exact stale event.  This is
   why the stronger `2/3` bound replaces F230's `4/9` missing-primary bound.
9. The apparent `s_p=s_q=1` branch is impossible here.  The proof derives
   `f=e+1`, computes `v_2(N-1)=e`, and contradicts
   `floor(n/2)>=e+1`.  No terminal-capacity premise is needed.
10. When `M=D` and `s_ps_q>1`, a nonstale global return must factor.  A new
    common primary cannot exceed `D`.
11. Different words contribute only through their lcm.  Different bases,
    not the words, supply the independent common-order certificates.
12. The upper law (22) is only for the declared uniform odd projection and
    return/puncture decoder.  It is not a lower bound against a
    carry-correlated base or another decoder.
13. The child-supported enrichment uses only the public prime list from the
    assumed factorization of `H`.  Raising those primes to exponent `n`
    costs at most `n log_2 H=O(n^2)` bits and does not assume knowledge of
    which of them also divide a hidden residual.
14. Replacing separate words by their lcm can reduce the direct mismatch
    mass, but it increases the union-of-returns mass.  The exact useful law
    is that union mass minus a word-independent stale term.  Therefore the
    total factor-or-growth probability is monotone even though the direct
    factor subevent alone need not be.
15. One-coordinate identity mass for a correlated source is not claimed
    sufficient.  The mass can be concentrated on simultaneous stale
    returns, for example at the identity element.  The repaired source
    boundary explicitly subtracts or excludes that atom.

## Complexity and scope checks

1. `Y` is bounded in numerical value by a fixed numerical-QP function.
   This makes the sieve through `Y` numerical-QP.
2. The exponent value is enormous, but modular powering depends on its bit
   length.  Inequality (17) bounds that bit length by a numerical-QP value.
   The word-aggregation claim likewise assumes QP total logarithmic height;
   it does not count a huge prime exponent only by the short binary encoding
   of that exponent.
3. The complete factorization of `H` is an explicit half-size recursive
   assumption.  F231 does not provide the all-input dispatcher.
4. The theorem is restricted to the balanced, distinct-prime zero-defect
   state imported from F230.  It makes no claim for prime powers, arbitrary
   composites, or nonzero quotient defects.
5. The first draft received one hostile FAIL.  It found that
   one-coordinate identity mass does not exclude joint stale returns.  The
   present version removes that claim and preserves the exact objection in
   `HOSTILE_AUDIT.md`.  No numerical experiment, web search, blind
   reconstruction, cross-family audit, human audit, or literature claim is
   used.

## Closest routes

- F230 is the closest route.  It enumerates odd multipliers of bounded
  numerical value and succeeds when one residual itself is numerically
  small.  F231 instead uses one factored QP-bit exponent word and covers a
  hidden residual of exponential value when its prime support is small.
- P161 uses the same powered-lcm primary filter on a fixed element order.
  F231 applies it to the hidden quotient of the entire projected local
  group and derives the exact two-coordinate stale probability.
- P197 supplies the lcm certificate potential.  F231 supplies a constant
  favorable-state source without requiring one element of exact aggregate
  order.
- P47/F37 concerns Fermat scans of the multiplied target `kN`.  F231 uses a
  multiplier only as a modular exponent.  P47's divisor-cloud obstruction
  does not apply to this detector.
