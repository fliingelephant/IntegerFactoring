# F193 V2 provenance

## Frozen V1

V1 remains preserved as:

- `STATEMENT.md`
- `PROOF.md`
- `SELF_AUDIT.md`
- `MANIFEST.md`
- `HOSTILE_AUDIT.md`

The fresh hostile audit returned **FAIL**. Its SHA-256 is
`aec0338a71c7bac828a660ff57b432aac91139ecb61309199d1f30644aec8e03`.

## Fatal V1 issue

V1 inferred nonvanishing of `chi(N)` from coprimality of the conductor with
`N`. The principal character modulo `N` is imprimitive with conductor one,
but its extended value at `N` is zero. Therefore V1's exact-rank-one and
universal-recovery statements were false.

## V2 repairs

V2:

1. states twist-bank rank **at most** one;
2. permits public zero rows and requires one nonzero row for recovery;
3. distinguishes a character's defining modulus from its conductor;
4. bounds the total sparse-chain encoding;
5. states the full Fricke partition action;
6. restricts the torsion theorem to auxiliary-prime torsion;
7. proves the CM characteristic polynomial through Tate-module trace and
   determinant.

No V1 file was modified. No mathematical computation was run. No durable
ledger was edited.
