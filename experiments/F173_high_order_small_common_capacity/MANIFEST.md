# F173 manifest

## Approach-family ID

`F173_high_order_small_common_capacity`

## Artifact type

Proof-only candidate. No computation was run.

## Question

Can a Harvey--Hittmeir large-order certificate, combined with bounded
factor-first screens, ordinary and Jacobi-torus quotient fingerprints, and
small known common-order states, force deterministic or Las Vegas QP
factoring?

## Candidate answer

Not from those interface facts alone. There is an infinite unbalanced
trial-hard semiprime family for which all four shifted ambient orders have
exponential prime components, all ordinary and Jacobi-minus-one common
orders have lcm at most twelve, and oracle-supplied primitive witnesses send
every named QP screen to a no-factor capacity branch.

A supplied factored exact global order still factors immediately. The
candidate therefore separates exact order from certified large order and
capacity. It does not claim a Harvey--Hittmeir output law or a factoring
lower bound.

## Files

- `STATEMENT.md`: frozen candidate statement and exact exclusions.
- `PROOF.md`: CRT/Linnik construction and group/order proof.
- `SELF_AUDIT.md`: quantifier, screen, and scope audit.

## Required next checks

1. Fresh hostile proof audit.
2. Fresh statement-only reconstruction.
3. Verify the full signed \(j(N\pm1)\) reductions in both torus
   orientations.
4. Verify that the strengthened CRT conditions preserve every F172 shifted
   gcd exactly.
5. Verify the QP length link and the distinction between the HH theorem
   interface and its instrumented exact-order branch.

No durable proof or failure ledger should be updated before those checks.
