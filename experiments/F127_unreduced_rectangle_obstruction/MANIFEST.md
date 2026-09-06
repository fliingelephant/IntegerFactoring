# F127 proof-artifact manifest

F127 is proof-only. It used no research computation.

## Verification history

- V1 failed hostile audit. Its exact endpoint counterexample is preserved.
- Corrected V2 passed a fresh hostile audit.
- The first V2 proof-blind reconstruction failed because the statement was
  under-specified. That failure is preserved.
- The expanded V2 statement passed a fresh proof-blind reconstruction. The
  reader requested only the explicit assumption \(Q\ge1\), which the final
  statement now states.

## SHA-256

- `V1_FAILED_AUDIT.md`:
  `b74a82e25233542aba170733ccd9f154e2985926e5e29f4a4acd0a2c91a13aca`
- `V2_STATEMENT.md`:
  `56ecc3f749381b36743117df3405182ae25e035d7a1bcfc47446390665a7acb9`
- `V2_PROOF.md`:
  `1c6fbe2f1ff0ecd7123d975f6728604635143f71ac3113c1ac54b19701dbaa0d`
- `V2_HOSTILE_AUDIT.md`:
  `81a3325a19c8cdd395880f9aeb3226e7b10ef438ea598a51d3c51a8a9d75060d`
- `V2_BLIND_RECONSTRUCTION_FAILED.md`:
  `7731df34afbf69aa2b22d2c601cb5d150d10aa4f18bab4ae7f75863381b1b54c`
- `V2_BLIND_RECONSTRUCTION.md`:
  `3fca5432c837080ea0eafffb478ed02204b1795de86be0e5b608d24c359be2e6`

No different-model-family or human audit has run.
