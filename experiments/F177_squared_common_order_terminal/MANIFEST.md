# F177 manifest

## Approach-family ID

`F177_squared_common_order_terminal`

## Artifact type

Proof-only positive candidate. No computation was run. No durable ledger was
edited as part of this candidate.

## Question

Can one certified ordinary or oriented quadratic-torus common order be used
more efficiently than direct enumeration of a factor residue class?

## Candidate answer

Yes, on balanced squarefree semiprimes. The ordinary order gives the factor
sum modulo the square of the order. An oriented torus order gives the factor
difference modulo the square of the order. Either reduces an individual
terminal threshold from order \(\sqrt N\), up to QP factors, to order
\(N^{1/4}\), up to QP factors.

This does not supply the common order and does not cover arbitrary factor
patterns.

## Frozen files

- `STATEMENT.md`: `bc1ec03dd8f9ac47e90d7e0108f3188d9639f0bb4f3f36074be047ba37da4944`
- `PROOF.md`: `82ec538a073e22566eb6e7429f03193b86fac119e24a551d144df89a33c73a09`
- `SELF_AUDIT.md`: `62942bd1ebb95d14c02ff2d876026acf660c44efb683c9a7264cde17e2774e26`

## Required checks

1. Fresh hostile proof audit.
2. Fresh statement-only blind reconstruction.
3. Compare precisely with P156/F170 before promotion.
4. Do not infer an all-input QP algorithm from this terminal decoder.
