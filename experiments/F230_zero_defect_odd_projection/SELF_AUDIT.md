# F230 self-audit

## Claim audit

1. The equivalence `E=0 iff B|(N-1) and c=0` is restricted to odd
   `1<=u<B`.  The separate formula for `u=v+kB` records the exact larger
   range and its shifted value `c=-k`.
2. The favorable condition `min(s_p,s_q)<=U` is hidden.  The algorithm does
   not discover `s_p` or `s_q`; it enumerates the public multiplier bank.
   The theorem is a favorable-state result, not an all-input algorithm.
   The full residual annihilator `S=s_ps_q` is also hidden and can be
   exponential.  It is used only to explain the local order structure, not
   as an algorithmic input or a cost bound.
3. The complete factorization of `H` is an explicit recursive assumption.
   The theorem proves that this call is half-size and that no further
   factoring call is needed for `uH`.  It does not supply the all-input
   recursive dispatcher.
4. Raising to `2^n` deliberately deletes the two-primary local orders.  The
   target certificate `D`, the accumulated `M`, and the favorable residuals
   are all odd.  The beta-two modulus already supplies the public power of
   two in the terminal.
5. The projection handles prime powers.  It is an automorphism on every odd
   primary component, not only on squarefree orders.
6. The bank does not stop at the earliest global return when its stripped
   block is stale.  It continues.  Stopping at an unproductive earlier
   return would invalidate the proof that the hidden useful entry is
   reached.
7. In the `(1,1)` residual case, the proof chooses a hidden missing primary
   only for analysis.  The stripping algorithm processes every public prime
   factor of `H`.  It does not know `D` or the chosen primary.
8. The exact probability in (13) concerns the order of a fresh uniform
   projected unit.  A nonunit sample gives a factor first, so it cannot
   reduce the unconditional success bound.
9. The terminal-capacity hypothesis is necessary.  If `M` already contains
   all of `D` and `lcm(2^t,D)<J`, the zero branch can be saturated without
   reaching the terminal.
10. A numerical-QP multiplier bound means the value `U`, and therefore the
    size of the enumerated bank, is numerical-QP.  A bound only on the bit
    length of `U` would not justify full enumeration.
11. The sparse upper law covers only fresh uniform odd projections and the
    factored-exponent return/puncture decoder.  It does not cover biased
    integer witnesses, quotient/carry correlations, or APR-compatible
    residue accumulation.
12. No numerical experiment, web search, literature claim, cross-family
    audit, hostile audit, blind reconstruction, or human audit supports this
    packet yet.

## Edge cases

- If a multiplier shares a factor with `N`, the direct gcd factors first.
  The bank explicitly performs this screen, and the sparse upper law is
  stated after it.
- Every residual `s_p,s_q` is odd.  Therefore a nonunit residual greater
  than one is at least three, which gives the `2/3` constant.
- If `s_p=s_q=1`, both odd local group orders equal `D`; this is the only
  branch that uses the missing-primary probability rather than a direct
  return mismatch.
- Extra odd valuation in `H` caused by cancellation in `N-1` is harmless.
  Equation `gcd(H,P)=D` controls its intersection with each local group, and
  stripping removes every redundant exponent power.
- The random-shift corollary requires a consecutive shift set that contains
  zero.  It counts only the one zero-defect atom.
