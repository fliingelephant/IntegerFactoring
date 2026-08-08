# F120 Preserved Failed Proof Routes

## 1. One universe-private row is not a full obstruction

The seed-`2` row is stable against the complete canonical universe. This only
forces the seed column out of every dependency. It does not give private rows
to the other complete-source columns and does not prove kernel zero.

## 2. The infinite `N=2q-1` family is not an infinite semiprime family

Dirichlet gives infinitely many suitable primes `q`, but it gives no required
factorization of `2q-1`. Promoting this family to trial-hard distinct
semiprimes requires the exact `(SPS)` lemma in `RESULT.md`.

The one computed semiprime is a finite falsifier. It does not prove `(SPS)`.

## 3. Exact-value privacy is not raw-residue privacy

Two inverse residues can give duplicate raw columns with the same exact
value. A raw F118-style matrix can therefore show a row twice even when that
row belongs to only one exact value. The F120 theorem applies after global
exact-value projection. Duplicate raw columns generate only a global-root
projection-kernel direction.

## 4. Initial REUSE failure says nothing about the peeled core

A private row removes one forced-zero coordinate from every kernel vector.
The remaining matrix can have zero or positive nullity. F120 did not decode
the remaining source on its finite input.

## 5. No-private-row matrices can still have full column rank

Even `REUSE` would not prove `CLOSE`. For example, the binary matrix

```text
1 1 0
1 0 1
1 1 1
```

has no degree-one row and is invertible over `F_2`. A source-specific closure
proof needs more than row-degree lower bounds.

## 6. CLOSE does not imply ROOT

A nonzero square-class kernel can map entirely to the global signs. The
normalized-root homomorphism must be proved nonzero separately. Neither the
large-prime theorem nor private-row peeling controls this image.

## 7. Carry congruence alone misses endpoint feasibility

For `N=2q-1`, divisibility of `1+kN` by `q` permits two carries in the broad
canonical interval. The second formal carry would require an endpoint
multiple of `q` with a cofactor at least `N`, so it cannot be a canonical
product of two endpoints below `N`.

This is why the endpoint-orbit bound improves the F119 interval bound. A
carry-residue count that ignores endpoint feasibility is not sharp enough.

## 8. Large-prime privacy below the threshold remains source-dependent

For `r <= (N-1)/2`, more than one endpoint multiple of `r` exists. Equation
`degree(r) <= floor((N-1)/r)` does not decide which inverse orbits the fixed
source reaches. Stable privacy below the threshold still requires control of
the self-generated source.

## 9. Smoothness and random matrices remain inadmissible

No distributional claim about factors of `1+kN` proves `(SPS)`, `(LFSP)`,
`CLOSE`, or `ROOT`. F120 uses none.
