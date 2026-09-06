# F174 V2 manifest

## Status

Proof-only repair candidate. No computation was run. The V1 statement,
proof, self-audit, manifest, hostile audit, and blind reconstruction remain
byte-identical.

## Reason for V2

The V1 operational trichotomy survived both reviews. The statement-only
review found two overbroad prose readings:

1. A raw line-13 escape is outside at least one old local subgroup. It is
   outside every old local subgroup only on the later absolute-gcd-one hard
   branch.
2. A general hard branch need not have unequal hidden orders. It certifies
   no exact common quotient order. Unequal orders are forced after the F172
   specialization.

V2 changes only those scope statements and the corresponding proof
clarification. It does not change the algorithm, displayed outcome
conditions, cost, or F172 corollary.

## Frozen V1 hashes

- `STATEMENT.md`: `6f5ff26ad6e5735d60e85bb394b992b44e05698bee7c9d51d902a240205d5908`
- `PROOF.md`: `614dbb1b0bb538353c2c919a5fa5778c8ff885c031992229ab1877db5a29ec98`
- `SELF_AUDIT.md`: `387146e6cfe3dbfeac9a24fb67e6ea4473399c8cafb2316c6f1eb35daae047f6`
- `MANIFEST.md`: `cc415a7d75713e60553489085d7d2eca2ed506571b3b64fd29569e015b6a2eea`
- `HOSTILE_AUDIT.md`: `f6381875873d53c9a72c07bb51633ff60b351b80f6eebeca7be88a4634f6ddbd`
- `BLIND_RECONSTRUCTION.md`: `086610b9fcedea2af55f7f36b81f7b43ddb5b86798e575eafacec31b2f4240d0`

## Frozen V2 inputs

- `V2_STATEMENT.md`: `faca4273e53eb04347c07bde9b0fd2fe429f7b681201bec205916cb49d97cecb`
- `V2_PROOF.md`: `3cf9d9f45a42005d1170203910868d65aca16c1cb5ff61fb04c119c7256277f9`

## Required checks

1. Fresh hostile audit of the complete V2 statement and proof.
2. Fresh statement-only reconstruction from `V2_STATEMENT.md`.
3. No promotion before both checks pass on the frozen hashes.
