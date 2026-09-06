# F231 provenance

## Prior-route check

The closest prior route is F230.  Its favorable source enumerates every odd
integer `u<=U`, so it needs one hidden residual odd order to have
numerical-QP value.  F231 differs materially because its word
`U_Y=lcm(1,...,Y)^n` has numerical-QP encoded length but may have enormous
value.  It annihilates any hidden residual with small prime support,
including arbitrary prime powers.

P161 is the closest primary-filter theorem.  It proves that the same
powered lcm removes all small-prime primary parts of a fixed local order.
F231 applies this operation after the zero-defect quotient identity and
counts the complete two-coordinate return/stripping law.

P197 is the aggregate-certificate framework used for `M`.  F231 does not
assume a common-order generator.  It counts stale returns directly as pairs
of equal local orders already dividing the aggregate `M`.

P47/F37 studies a different mechanism: Fermat scanning of `kN`.  Its
resolution loss is not used here because F231 uses the factored word as an
exponent and does not search divisor allocations of a multiplied target.

## New claims

1. For any factored word `W`, the local return kernels have exact indices
   `r_p(W),r_q(W)`.
2. The exact no-progress probability is the sum of the neither-return term
   and `sum_(d|M) phi(d)^2/(PQ)`.
3. One `Y`-smooth hidden residual, even of exponential value, gives
   history-wise progress probability at least `2/3`.  A new valuation
   argument proves that `s_p=s_q=1` is impossible in the balanced
   zero-defect domain, so there is no capacity exception.
4. The known prime support of the factored half-size child `H` can be added
   to the word with only `O(n^2)` exponent bits, removing large as well as
   small residual primary parts.
5. Multiple factored words aggregate canonically by lcm, while common-order
   certificates from unrelated elements aggregate independently by lcm.
6. The remaining uniform-source gap is exactly a factored word of QP
   logarithmic height and list size that leaves one residual numerical-QP.
   A correlated source instead needs inverse-QP exactly-one-return or
   nonstale-global-return mass; marginal identity mass does not suffice.

## Preserved failed draft

The pre-freeze hostile audit returned literal FAIL against statement hash
`3da8d99937bc792021f79486d53753c5f8d114cd7544ce73cf0a927253748fd3`.
It rejected only the final claim that one-coordinate inverse-QP identity
mass suffices for a correlated source.  The counterexample is the constant
identity source: all identity mass is a simultaneous stale return.  The
audit SHA-256 is
`6301af75b0cf075819e43040f8e862df6dcd874c21ace8941b621b9fd5cbd138`.
The current version requires exactly-one return or a nonstale global return.
The failed bytes and objection remain in `HOSTILE_AUDIT.md`; they do not
count as verification of this repaired version.

No numerical computation or public web search was used.  The packet is
proof-only and has only self-audited status.
