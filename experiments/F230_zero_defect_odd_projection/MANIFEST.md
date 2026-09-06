# F230 frozen candidate manifest

## Frozen files

- `STATEMENT.md`
  - `96edf9b0eb183364ce9178385e289e8e7c5dc967d32f74912aaff7548ba5999f`
- `PROOF.md`
  - `2a07b604ac59d3090ed6cc7e46c8c4aed197665ce79db84068b802031a82d407`
- `SELF_AUDIT.md`
  - `902ee4dd3c9a5528c3fcbcc2a2e5860aee1feb51ed0400d7ea77581185c8f8ba`
- `PROVENANCE.md`
  - `290cc0b5a0e670bcd05ea0739feedad1a1c79d54080ee4da9611e72a0ec987ec`

## Candidate claims

1. For odd `1<=u<B`, zero common-primary defect occurs exactly when
   `B|(N-1)` and `c=0`; every such quotient child equals `uH` for the one
   public half-size integer `H=(N-1)/B`.
2. The public projection `x -> x^(2^n)` produces independent uniform odd
   local coordinates and gives the exact return laws (7)--(9), including
   arbitrary primary powers.
3. If one hidden residual odd local order is at most the public
   numerical-QP multiplier cap and the odd common capacity closes the
   beta-two terminal, a complete public multiplier bank has history-wise
   factor-or-growth probability at least `4/9`.
4. A single uniform odd multiplier has inverse-QP progress at the explicit
   rate in (15), and an independent uniform shift bank loses exactly its
   zero-shift atom as in (16).
5. If both residual odd orders are large, the same bounded uniform projected
   source obeys the exact union bound (17) and the sparse laws (18)--(19).

## Required hostile checks

- Reconstruct the zero-defect equivalence, including the `u>=B` extension.
- Check `gcd(H,P)=gcd(H,Q)=D` when `N-1` has cancellation-enhanced odd
  valuations.
- Check the `2^n` projection on every prime-power component.
- Check the exact local return and direct-factor probabilities.
- Audit the stripping loop when the exponent has redundant primary powers.
- Check the favorable cases `(s_p,s_q)!=(1,1)` and `(1,1)` separately.
- Verify that the algorithm never needs to know `D`, `s_p`, `s_q`, `S`, or
  the missing primary, and that it continues after a stale early return.
- Check the conditional drift, beta-two/lcm terminal, numerical-QP bank
  cost, recursive assumption, and exact scope of the sparse upper law.

No computation is part of this packet.

