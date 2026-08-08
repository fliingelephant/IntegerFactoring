# Reconstruction manifest

## Input pin

- `RECONSTRUCT_STATEMENT.md`
- SHA-256:
  `4a4aaf43119609e7745b5f88623a3ea9fb3c72aac7d15b16062d1aef0e692986`
- Hash verification: pass.

## Output pins

- `RECONSTRUCT_PROOF.md`
- SHA-256:
  `e8aa7a5f4c10bb24d99b766b1fe774912d939e9db16f565de035d92d4442db46`

- `RECONSTRUCT_FAILED_ROUTES.md`
- SHA-256:
  `fc940f621003fa5c447feb9bd530b680364d0371767e948636b9b20063c64d72`

- `RECONSTRUCT_REPORT.md`
- SHA-256:
  `5f9c9dae4ff42ad4c8685dcd3c0a39a95931c792f0fe8973b9b79749450ba5ef`

## Method

- Proof-only reconstruction.
- No computation.
- Named external results used: prime number theorem, Chinese remainder
  theorem, and Linnik's theorem.
- No other F119 file read.
- No durable ledger read.
- No project proof search.
- No durable ledger edit.

## Verdict

Claims A–C reconstruct exactly. Claim B is an infinite selected-submatrix
independence theorem. It is not a complete-source obstruction. The named
residue screen proof is not transferred to a different earlier residue that
has the same exact integer value.
