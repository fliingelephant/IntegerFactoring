# F245 V2 manifest

## Status

- V2 is a self-audited proof-only candidate.
- V1 is preserved byte-for-byte.
- V1 hostile review passed the mathematics but its strict statement-only
  reconstruction failed because the P208/P209 interfaces were only named.
- V2 restates those exact interfaces and the Las Vegas truncation argument.
- No computation or durable-ledger edit belongs to this packet.

## V2 frozen SHA-256

- `V2_STATEMENT.md`:
  `ad4ff2a363de6e30c12245a7ecaefa7990dc560893e3ddebb68bfb14d8338440`
- `V2_PROOF.md`:
  `a3da0fcb8a97425f289846e1f824e40f7e227395c230664c95f79c42ed40a92c`
- `V2_SELF_AUDIT.md`:
  `a467c9ac9de50511efc0a638bca79e5b3f8eb5474f7c236258585a9863993ce3`
- `V2_PROVENANCE.md`:
  `a67635a0575becf346cb037355b09350b8675ce4df88213dbb24482646d0e2ce`

## Preserved V1 SHA-256

- `STATEMENT.md`:
  `c12d744be03815b942010c13637225a9d889f7724f1f5c95c4e5dc35d2a05a21`
- `PROOF.md`:
  `4d1580cebb9bdfcd82a6db332a9cc5e146cc2e68b91bd63c6057898c92c8b30a`
- `SELF_AUDIT.md`:
  `e15ac05a5de7f070000299afe6d7f06bf5f988f9ed52834affc8e1a9cb0d2256`
- `PROVENANCE.md`:
  `c0448f5aa54999c0b55086fa890f28dcfc662032186756c15f3d88990b9e2b7f`
- `MANIFEST.md`:
  `3d129d3ed943e93342273ff5ce3db7de97d5259fb7cc0b1bcc314f001851f5fa`
- `HOSTILE_AUDIT.md`:
  `4a628b36faa03ea665a4e6e95ce12379eab8a8e0f4ab7249b3ff9b35329ec561`
- `BLIND_RECONSTRUCTION.md`:
  `c59bce6b5c92d139d65015eedd99e524f1c6e300d5dce5ac090efc9d3ea4b2c4`

## Required V2 hostile checks

1. Authenticate all four V2 files and all seven preserved V1 artifacts.
2. Reconstruct the sequential CRT--Linnik family and input-length link.
3. Check the primitive-order signed-power exclusion.
4. Check the clean and nonclean torus upper bounds.
5. Check the adaptive inverse-quotient bank and expected-time truncation.
6. Check that no conclusion is transferred to nonlinear carries.
