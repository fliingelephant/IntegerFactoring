# Proof-blind reconstruction task: frozen-layer completeness

## Isolation rule

Read only RECONSTRUCT_STATEMENT.md, this statement, and
RECONSTRUCT_INPUT.json. Do not read another F111 file or any F98, F109, or
F110 file. You may extend your own independent source from the first
reconstruction task.

Use no general factorization or primality routine. Write only new files whose
names start with RECONSTRUCT_LAYER_. Preserve failed attempts and use a named
hard timeout.

## Objective

Rebuild the complete frozen source specified in RECONSTRUCT_STATEMENT.md,
stopping before the appended \((2,3)\) and \((2,4)\) trajectories. Then use a
complete factor-free decoder to determine whether any frozen-layer integer
square dependency has a non-global root modulo \(N\).

## Exact-value normalization

For each retained frozen record, use its exact relation value \(P=cw\).
Discard \(P=1\). For each other exact integer value, keep only its first
occurrence. This normalization is lossless over \(\mathbb F_2\): an even
number of copies cancels, while an odd number has the same square class and
the same normalized root as one copy.

Give the resulting distinct values zero-based normalized column indices.

## Factor-free parity rows

Apply the deterministic gcd-basis algorithm from RECONSTRUCT_STATEMENT.md to
the list of distinct exact values, treating each value as one endpoint with
its own one-hot integer signature.

The final pairwise-coprime, perfect-power-free blocks reconstruct every exact
value. For each final block, reduce every exponent in its signature modulo
two. Remove a zero row and deduplicate equal nonzero rows. These public rows
give the complete square-class parity matrix:

- every rational prime dividing a block has the same primitive valuation
  signature modulo two;
- every rational prime row occurs as one of these block rows;
- merging equal rows does not change the kernel.

Do not factor a block or an exact relation value.

## Complete decode

Compute a full basis of the binary kernel of the public row matrix. For every
kernel-basis vector:

1. multiply the selected distinct exact relation values;
2. verify that the product is an exact positive square;
3. compute its positive integer root;
4. reduce the root modulo \(N\);
5. compute \(\gcd(R-1,N)\) and \(\gcd(R+1,N)\).

The normalized-root map is a homomorphism from the binary dependency space to
the square roots of one modulo \(N\). Therefore testing a complete kernel
basis is enough. If every basis root is globally \(+1\) or \(-1\), every
frozen-layer dependency is globally signed and none factors \(N\).

## Required report

Report:

1. raw frozen relation count;
2. the number of removed unit values and repeated exact values;
3. distinct normalized column count;
4. distinct nonzero public row count, rank, and kernel dimension;
5. the root residue and both gcds for every kernel-basis vector;
6. whether the complete frozen dependency space contains a proper factor;
7. why the computation is factor-free and complete;
8. the boundary: this is one fixed frozen batch, not an all-input theorem.
