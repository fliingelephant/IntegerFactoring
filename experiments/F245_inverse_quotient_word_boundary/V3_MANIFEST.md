# F245 V3 manifest

## Status

- V3 is a frozen self-audited proof-only candidate.
- V1 and V2 are preserved byte-for-byte with both generations of audit
  records.
- V2 hostile review passed its mathematical reading, but the strict V2
  statement-only reconstruction failed because the algorithmic grammar and
  its exhaustive factor exits were not defined.
- V3 defines that grammar.  It adds no numerical or empirical claim.
- No computation or durable-ledger edit belongs to this packet.

## V3 frozen SHA-256

- `V3_STATEMENT.md`:
  `2120f53ec1762cd6b90236eb165d59368f9e0aad4750dcb3a5afadf3508d2c8b`
- `V3_PROOF.md`:
  `52e7b9391d8d4f36d4653b016f58805776655f732d3a398f9e753c9f14205e7d`
- `V3_SELF_AUDIT.md`:
  `ca19b956247c986fe30f69633b71f37b90894133c1fd83bf617dfa89d9376f3f`
- `V3_PROVENANCE.md`:
  `b15f8b84842dbf5c663162b1e7793ff29ae9a5e138071665e8f98fd06d865981`

## Preserved V2 SHA-256

- `V2_STATEMENT.md`:
  `ad4ff2a363de6e30c12245a7ecaefa7990dc560893e3ddebb68bfb14d8338440`
- `V2_PROOF.md`:
  `a3da0fcb8a97425f289846e1f824e40f7e227395c230664c95f79c42ed40a92c`
- `V2_SELF_AUDIT.md`:
  `a467c9ac9de50511efc0a638bca79e5b3f8eb5474f7c236258585a9863993ce3`
- `V2_PROVENANCE.md`:
  `a67635a0575becf346cb037355b09350b8675ce4df88213dbb24482646d0e2ce`
- `V2_MANIFEST.md`:
  `66e8b484a93ae425994dba4e968c5ba4de29b84506388ac44ddd2286b305bf35`
- `V2_HOSTILE_REAUDIT.md`:
  `742fee39bcf02d6006165d3cabb76a25eb5734872b01164f470eae0da964a462`
- `V2_BLIND_RECONSTRUCTION.md`:
  `74a29858458cb25354baf945795a6907c92fa86fa61239ed46a367ffc39ddb65`

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

## Required fresh V3 hostile checks

1. Authenticate the four frozen V3 inputs and every preserved V1/V2
   artifact before reading them.
2. Treat `V3_STATEMENT.md` as the exact theorem.  Do not silently expand the
   grammar.
3. Reconstruct the filtration and verify that each exponent is fixed before
   its fresh torus point.
4. Check the complete nonclean branch: unit, discriminant, coefficient, and
   norm gcd exits, including raw rejection tails.
5. Check the endpoint screen, global-return gate, two-primary chain, signed
   identity screens, and local-return containment.
6. Check that the six-prime bank event covers every legal direct word gcd.
7. Check the sequential CRT--Linnik family, signed-power exclusion, and
   common-order lcm bound.
8. Check that equation (38) is pathwise exhaustive and that Markov
   truncation uses the correct quantifier order.
9. Reject any conclusion for nonlinear carries, current-point feedback,
   biased sources, or an unrestricted transcript decoder.
