# F153 manifest

- Candidate: Jacobi-torus orientation is one character, but it does not
  determine a decorated section.
- Type: proof-only kill-first candidate.
- Runtime experiment: none.
- Durable ledgers edited by the candidate and reviewers: none.
- Promotion status: V3 passed fresh hostile audit and fresh independent
  statement-only reconstruction. V3 is the promoted version.
- V1 hostile audit: failed on one section-uniqueness inference.
- V2 repair: preserves the exact identities, removes that inference, and
  states the remaining kernel freedom explicitly.
- V2 hostile re-audit: passed.
- V2 statement-only reconstruction: reconstructed every mathematical
  identity, but found four literal quotient and scope defects.
- V3 repair: uses the literal section quotient, qualifies the split-side
  coordinate isomorphism, leaves an unspecified `t(alpha)` map unclassified,
  and makes no minimality claim for the biquadratic algebra.
- Required V3 checks: complete.

## Closest prior results

- P55: exact signed factor-gap relation in Jacobi-minus-one Lucas tori.
- P57: exact Dickson trace aliases and coherent mixed-root boundary.
- F151 V2: large-order preprocessing and failure of the direct Kummer splice.
- F152: unpromoted decorated-squareclass split-or-section framework. F153
  uses only the form repaired by squareclass independence and supplied-root
  comparison before deduplication.

## New exact content

1. Every multiplicative discriminant-word orientation is the restriction of
   the single hidden character `(./p)`. This fixes the base character but
   does not uniquely fix an F152 decorated section.
2. The P55 signed-gap identity has one universal synchronized exponent
   halving and no direct uniform second halving.
3. Cayley halving is exactly square-root selection for `1-Dt^2`; opposite
   global branches differ by global `-1`, while a mixed branch already
   factors `N`.
4. A product of two Jacobi-minus-one discriminants has the exact sum-type
   torus relation in Statement (14). It is a direct specialization of P55's
   local-order formula; its split branch overlaps P57, while its explicit
   all-nonsplit branch was not previously recorded there.
5. A conjugation-preserving cross-discriminant isomorphism needs a square
   root of the discriminant ratio, and the three direct biquadratic relative
   norms return only `U^2`, `V^2`, or `1`.
6. Any homomorphism from the ordinary local unit group to a nonsplit local
   norm-one torus has image of order at most two. Ordinary large order cannot
   transfer through that interface.

## Frozen hashes

```text
f38c3a1558b7f2509a8fadfc7518ace67ef6fcb7522be003961c690ab0723419  STATEMENT.md
c6b612da25b716c44fc1844141509769d83c26f7e342047a29bfb90617de6ff6  PROOF.md
```

These V1 files remain frozen byte-identically. The failed hostile audit is:

```text
34961e89fad39f9006e2c4c7ae9836ca1ffdf5f3b0f11265fd6ba8cea2e6810a  HOSTILE_AUDIT_FAILED.md
```

## Frozen V2 hashes

```text
6bba6be5b6f8dd9f2a4810f7182fbc400029cc5026b55224809835a186123b3a  V2_STATEMENT.md
9fa532e12483b38497987fa798711ae69e356938c75c93836d5cf41a538c451d  V2_PROOF.md
```

The V2 statement and proof remain frozen byte-identically. Their completed
reviews are:

```text
71f0bb3878ac2815f6f41add4c1e96b5f88d9109e6730a8dfccf917bf865b9d6  V2_HOSTILE_REAUDIT.md
e439879cb5fec3733f662f1e416f9e18c5be7ddf800afe371e9570b46b075155  V2_BLIND_RECONSTRUCTION.md
```

## Frozen V3 hashes

```text
91886c70c39496dc0519ab4928f7234a263539eb235a863c7ac8bbe21c50d8a0  V3_STATEMENT.md
f86807ae0bff8b4557f24da18c17b6729e4cb78895b22f6987f8a77efc17447d  V3_PROOF.md
```

The V3 statement and proof are frozen at these hashes for fresh review. The
four repairs do not alter an exponent, algebra identity, factor certificate,
or algorithmic conclusion. They do change the literal statement and proof,
so they received a fresh hostile audit and a fresh statement-only
reconstruction:

```text
176a12902893b11fdbda5c86ff113cea50978bac070cdfb2e55dfd4b4dbcb645  V3_HOSTILE_AUDIT.md
67b772502c1dd8341d4b0c4ae26ff7eb1248a29b82b61342e5b0f673cc29b595  V3_BLIND_RECONSTRUCTION.md
```
