# F164 V2 manifest

## Candidate

- ID: `F164 V2`
- Name: quotient-fingerprint rank–capacity updater
- Type: narrow statement-and-proof repair
- Computation: none
- Durable-ledger edits: none
- Self-audit: none

## Preserved V1 artifacts

The V2 repair does not modify these files:

- `STATEMENT.md`
  - SHA-256: `b45b07e7f97aad53d4a3fa15ce795db4a7bdf659f371bb70857668dae816af83`
- `PROOF.md`
  - SHA-256: `ccfe1f918bb4bba86ffefe72a4678ef18785e54788cff5cb49946d2186696187`
- `MANIFEST.md`
  - SHA-256: `8003d58aba572fd48078b5631fa89f6901bfd2c472d56deec2666072773b4f02`
- `HOSTILE_AUDIT.md`
  - SHA-256: `ed03dd70d27531c1df8ed07f292d483fda4c18ab88181e247defc02a52117988`
- `verify_audit.py`
  - SHA-256: `b166dc147077b012af3e36266a2162ad08c32e7ac34fa06b90edb086b26aaad1`
- `BLIND_RECONSTRUCTION.md`
  - SHA-256: `4dae6da74c74dc796bd146a01d4e61049ceab09e7d0c8ac6091a68c8c5bfeb2b`

## V2 artifacts

- `V2_STATEMENT.md`
  - SHA-256: `8e47a9e249ff7f6fd7996664daddbbd53ace7dafd1e85b159ad20502a6d6fa19`
- `V2_PROOF.md`
  - SHA-256: `53488652f65c7138412389a584e6a4dd7fa5a9367191c8d5bbc1558f7a4bf2bb`

## Exact repair scope

V2 makes four changes only:

1. It calls the three Section 8 progress conditions alternatives. It does
   not call them equivalent.
2. It places the quasipolynomial cap on the full encoded transcript. The cap
   includes named blocks, the explicit bank, retained relations, complete
   provenance, and all exponent and coefficient bits. It states that a cap
   on `kappa` or bank cardinality alone is insufficient.
3. It defines the `N=341` legal provenance inside the statement and proof.
   The construction starts from the two displayed canonical-inverse endpoint
   identities and applies complete joint gcd-free refinement with occurrence
   and multiplicity provenance.
4. It sets the next F161 scan cap to

   \[
   B'=\max(B,\kappa),
   \]

   so the cap contains every prime factor of `D=M*kappa`.

V2 does not strengthen the success claims or change the remaining
mathematics. It requires independent review before any durable promotion.
