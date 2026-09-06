# F281-D01 provenance

## Prior mathematical context

F281-D01 starts from the exact local central-Stirling seam in
`experiments/F277_integer_valued_difference_boundary`. In that packet, the
two F277 scalars are simultaneously saturated at a prime component exactly
when

```text
p divides S(2s+1,s) and S(2s+1,s-1).
```

F281-D01 does not modify F277. It tests the separate conjecture that a common
prime divisor of those two integers cannot exceed `2s+1`.

The root agent supplied these pre-F281 observations:

- local exact checks found no counterexample through `s=3000`;
- the general adjacent-row analogue is false because
  `23 | S(12,3),S(12,2)`; and
- the central slice is therefore an essential hypothesis.

These observations are provenance only. This packet did not rerun them before
freeze. Its own pilot and production outputs must identify their exact tested
cohorts.

## Theory work before packet authoring

The theory-first pass established:

- the complete homogeneous target at degrees `s+1,s+2`;
- the exact complement to `c(s+2h+1,2h)` and
  `c(s+2h+1,2h-1)` for `p=2s+1+2h`;
- the finite-difference endpoint and reflection forms;
- the fixed-divisor prefix-to-tail seam; and
- the failure of the proposed `h_(2h-2),h_(2h-1)` reparameterization.

No proof and no counterexample to the central conjecture was found. No
Lundell or determinantal-divisor theorem was assumed to bridge the two-entry
gcd to the full tail fixed divisor.

## Execution provenance at freeze

The F281-D01 source was authored after theory alignment. Before freeze, it was
not compiled, executed, benchmarked, or transferred. No local resource pilot
and no `ssh seetacloud` command was run for F281-D01. `VALIDATION_PENDING.md`
is the authoritative qualification state.
