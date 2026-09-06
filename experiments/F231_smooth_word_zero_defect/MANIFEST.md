# F231 frozen candidate manifest

## Family and status

F231: factored smooth exponent words and child-supported prime words in the
balanced zero-defect quotient state.

Frozen, self-audited, proof-only favorable-state candidate.  **Do not
promote.**  The first pre-freeze hostile audit failed one source-boundary
sentence.  That failure is preserved below and does not verify the repaired
bytes.  No hostile re-audit of the frozen version, statement-only
reconstruction, cross-family audit, human audit, or publication-level
literature review has run.

## Frozen candidate files and SHA-256 hashes

- `STATEMENT.md`
  - `f7503be5f8db21697157bc6f267b5719e656d55b395f8d8d524c5a0661d1dd56`
- `PROOF.md`
  - `02a8c7a863bbec8b4bbd2475b617456a1d4e059c44e693c96526f7ae60c663c5`
- `SELF_AUDIT.md`
  - `a2ae6a640974d396940985c63892fa0263868f8cb1b095dced85439509e4b657`
- `PROVENANCE.md`
  - `608ff1794971bfc2bb69eee64ce511823594372fad9016e4dcfd47a0a5a14331`

## Frozen imported source identities

- `PROMPT.md`
  - `a4a85d0fc0cc540af7d2ab410dc8d7b6e6bf8a72dc2037509cb0999ddc9ee938`
- `experiments/F230_zero_defect_odd_projection/STATEMENT.md`
  - `96edf9b0eb183364ce9178385e289e8e7c5dc967d32f74912aaff7548ba5999f`
- `experiments/F230_zero_defect_odd_projection/PROOF.md`
  - `2a07b604ac59d3090ed6cc7e46c8c4aed197665ce79db84068b802031a82d407`
- `experiments/F181_rough_order_normalization/STATEMENT.md` (P161)
  - `992f84a580a362d7908d9287e186dbae46963044956dae65b7b52540fa15df32`
- `experiments/F220_aggregate_order_carry_las_vegas_terminal/V2_STATEMENT.md`
  (P197)
  - `935ef9a28dff6bfade891ca069eb5d544236977c4c8c20c6d4208ff582b5fe45`

## Frozen claims

1. For every completely factored public word `W`, the projected local
   return probabilities are exactly `1/r_p(W)` and `1/r_q(W)`.
2. Complete factor-first stripping has exact factor-or-growth probability
   equal to the union-of-returns probability minus
   `sum_(d|M) phi(d)^2/(PQ)`.  This last term is exactly the stale atom.
3. The powered word `U_Y=lcm(1,...,Y)^n` absorbs every hidden residual whose
   prime support is at most a numerical-QP `Y`, even when the residual has
   exponential numerical value or arbitrary prime powers.
4. The factorization of the half-size child `H` gives the enriched word
   `Uhat_Y=U_Y product_(ell|H,ell>Y) ell^n` at only `O(n^2)` extra
   logarithmic height.
5. Under either resulting one-residual saturation condition, each fresh
   stage has history-wise factor-or-growth probability at least `2/3`.
   It factors almost surely in at most `3n/2` expected stages, conditional
   on the correct half-size factorization of `H`.
6. The apparent `s_p=s_q=1` exception is impossible in the balanced
   zero-defect state by an exact two-adic valuation contradiction.
7. Factored words aggregate by lcm without reducing total factor-or-growth
   probability.  Common-primary certificates from unrelated projected
   bases aggregate independently by lcm into `M`; no one base needs order
   `M`.
8. The beta-two residue combines with `p=1 mod M` modulo
   `lcm(2^t,M)`.  Reaching the known-residue threshold can terminate before
   the direct factor, but no terminal-capacity assumption is needed.
9. If both residual kernels remain exponential, the declared uniform
   projected source is exponentially sparse.  Roughness alone does not
   imply exponential size.

## Preserved failed pre-freeze audit

`HOSTILE_AUDIT.md` has SHA-256
`6301af75b0cf075819e43040f8e862df6dcd874c21ace8941b621b9fd5cbd138`.
It audited the earlier statement hash
`3da8d99937bc792021f79486d53753c5f8d114cd7544ce73cf0a927253748fd3`
and returned literal FAIL.  Marginal identity mass for a correlated base
can be concentrated entirely on simultaneous stale returns.  The frozen
version instead requires exactly-one-return or nonstale-global-return mass.
The failed audit found no other objection, but it does not count toward the
verification of the repaired hashes.

## Required focused hostile re-audit

1. Authenticate all four frozen candidate hashes before reading them.
2. Recheck the exact stale term and the exhaustive stripping classification.
3. Recheck the full valuation proof excluding `s_p=s_q=1`.
4. Verify the `2/3` constant and `3n/2` almost-sure Las Vegas stage bound
   without a terminal-capacity premise.
5. Verify arbitrary prime powers in `U_Y`, the child-supported enrichment,
   and all logarithmic-height and bit-cost bounds.
6. Check lcm monotonicity separately from direct-factor monotonicity.
7. Confirm that every correlated-source sentence subtracts or excludes the
   stale joint atom.
8. Reject any implicit all-input dispatcher, hidden factor access, or claim
   that P161 roughness supplies residual saturation.

No numerical computation, scripted experiment, remote run, web search, or
finite fit is evidence for this proof-only packet.  No durable ledger was
edited.
