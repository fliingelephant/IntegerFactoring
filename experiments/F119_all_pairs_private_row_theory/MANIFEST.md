# F119 Proof-Only Manifest

## Boundary

F119 is a proof-only investigation of stable private square-class rows in the
complete fixed F116 source. It ran no mathematical computation and used no
external data. It made no durable-ledger edit.

The result is partial. It proves exact carry laws and an infinite
`Theta(n/log n)` cross-pair submatrix construction. It does not prove a
complete-source obstruction or a forced-progress theorem.

## Correction history

The first hostile audit returned `PASS_WITH_CORRECTIONS` on the original
`RESULT.md` hash
`990952a8175733959ef8d7f67429a330c27378ba897426a81c11f536dbd8a500`.
It found that the sign-screen wording could be read as covering a different
earlier residue with the same exact value. The corrected result limits that
claim to each named exponent-two residue and its canonical inverse. The
value-level private-row theorem is unchanged. A separate final re-audit is
required for the corrected hashes below.

## SHA-256 pins

Each hash is over the exact file bytes. This manifest has no self-hash.

| Role | File | SHA-256 |
|:---|:---|:---|
| Prior single-trajectory result | `../F99_canonical_power_trajectory_obstructions/RESULT.md` | `d3a1af9e01f0209d8f06d53c2641bbad2056077bdca4d7966f9e6bdc98e592aa` |
| Complete-source design | `../F116_independent_54bit_all_pairs_stress/DESIGN.md` | `533f92d1e79cf81ef4e3841b48fbddd527571a944b3fced5c131b6148034c803` |
| Preregistered question | `QUESTION.md` | `7dba1e0092302380bd9989d218cc144aa6026c44214ee215145285424f5e9c7f` |
| Proof and result | `RESULT.md` | `552a54c8382341709305e53bd535efd9ef0ec0bc7957fa32be8ddc5c061f4575` |
| Preserved failed routes | `FAILED_ROUTES.md` | `be2afb89c6299e8de5ca0b818796d12994bb51f8a0ba912c020a908066eca563` |

## Run record

- Named computations: none.
- Failed program runs: none.
- Preserved logical failures: seven, in `FAILED_ROUTES.md`.
- External sources: none.
- Files changed outside this directory: none.
