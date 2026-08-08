# Proof-blind reconstruction task: complete cross-layer interaction

## Isolation rule

Read only this statement, `RECONSTRUCT_INTERACTION_INPUT.json`, and
`RECONSTRUCT_STATEMENT.md`. Do not read another F111 file. Do not read any
F98, F109, F110, F115, or F116 file. You may extend code that you wrote for
the earlier frozen-layer reconstruction, but do not read the layer-interaction
auditor's code, output, report, manifest, or logs.

Use no general factorization or primality routine. Write only new files whose
names start with `RECONSTRUCT_INTERACTION_`. Preserve failed attempts. Use a
named hard timeout. Record every input and output hash, the command, the
working directory, and elapsed time.

## Objective

Rebuild the complete ordered source in `RECONSTRUCT_STATEMENT.md`. The frozen
layer contains the initial seed records and all retained frozen-pair trajectory
records. The appended layer contains the records retained after frozen
generation and before the declared public stop.

Determine, without using the published dependency indices, whether a useful
integer-square dependency occurs in:

1. the frozen layer alone;
2. the appended layer alone;
3. the globally deduplicated union.

Also determine whether every useful union dependency must use records from
both layers.

## Exact-value coordinates

For each record, let its exact relation value be `P = c*w`.

For each standalone layer, discard `P = 1` and keep the first occurrence of
each other exact value in that layer. For the union, apply the same rule in
the full source order. Thus an exact value that first occurs in the frozen
layer is a frozen union coordinate, even if it occurs again in the appended
layer.

Report the raw, unit, duplicate, and distinct counts for both layers and the
union. Report the number of exact values shared by the standalone layer sets.

## Complete factor-free decoder

Build a complete binary square-class matrix for all distinct union values by
gcd refinement and exact perfect-power extraction. Do not factor an endpoint,
an exact relation value, or `N`.

It is sufficient to produce pairwise-coprime integer blocks with exact
exponent signatures, reduce those signatures modulo two, remove zero rows,
and deduplicate equal rows. You can use another independently justified
factor-free construction if it produces the complete parity row space.

Restrict or remap the complete union rows to form the frozen, appended-only,
and global-union systems. Compute a complete binary kernel basis for each
system. For every basis vector:

1. multiply its selected exact values;
2. verify that the product is an exact positive square;
3. reduce the positive square root modulo `N`;
4. verify that the residue squares to one modulo `N`;
5. classify the root as `+1`, `-1`, or non-global;
6. compute both terminal gcds.

Testing a complete kernel basis is sufficient because the normalized root map
is a homomorphism from the dependency space to square roots modulo global
sign.

## Cross-layer quotient

Let `M_F` and `M_A` be the frozen and newly appended coordinate parity maps in
the globally deduplicated union. Compute:

```
K_F = kernel(M_F)
K_A = kernel(M_A)
K_U = kernel([M_F M_A]).
```

Independently verify the dimension identity

```
dimension(K_U) - dimension(K_F) - dimension(K_A)
= rank(M_F) + rank(M_A) - rank([M_F M_A]).
```

Construct a complete basis of `K_U/(K_F direct_sum K_A)`. Compute the
normalized root-map rank on this quotient. Use these complete spaces, not one
selected support, to decide whether every useful union dependency crosses the
layer boundary.

## Required boundary

State exactly what the reconstruction proves. It concerns one fixed modulus,
source order, stop, and coordinate convention. It gives no stop selector,
other-input theorem, density law, success probability, or polynomial bit-time
factoring algorithm.
