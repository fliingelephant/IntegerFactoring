# F233 frozen hostile audit

## Verdict

**PASS.**  All frozen hashes matched `MANIFEST.md`.  The reviewer edited no
candidate input and ran no computation.

## Checks that survived

1. The two gap signs follow separately from `p=1 mod ell` and
   `q=1 mod ell`.  Symmetric nonzero shifts identify the two ratio covers.
2. Overlap between `D` and `s_p` or `s_q` causes no residual error.  Such a
   prime divides `H`, so `W_0` saturates it.  Every exposed residual power is
   saturated because its valuation is less than `n`.
3. The P202 formula imports correctly.  The word is completely factored,
   the projected unit is fresh and uniform, `M|D`, and deterministic bank
   screening does not condition that sample.
4. The circular-gap proof returns an index difference `1<=u<=U` and a
   nonzero signed gap of size at most `floor(ell/(U+1))`.
5. The ratio set has at most `2CU` elements.  The avoidance and uniform-model
   bounds follow.
6. Projective uniqueness is valid in the stated residual scope
   `ell` not dividing `H`.
7. Even multipliers are valid because only `0<u<B` is needed for the
   Euclidean remainder.  Positivity follows from `C<H`.
8. The smooth-cutoff conclusion is explicitly limited to universal,
   residue-independent coverage.  It does not claim an actual gap-ratio
   distribution.
9. The contraction and numerical-QP accounting remain explicitly
   conditional on the external all-input dispatcher.

## Audited hashes

```text
STATEMENT.md
779fc3dafec72264ed0ae6bb0fee8835d2500cb70cfb2bcfea936d059841b510

PROOF.md
58f35d1037d37143da61d1296b2df3bac4279546bf1c2792cd4479402a003bbc

SELF_AUDIT.md
07b5f356b4a71646f8a3cc0f446422912da35ce9dd5ae83e2bd3950e01bf4bd4

PROVENANCE.md
5a4b896a185e16534c1e37ae4b26794e33be035ddb4349af240a71140e6b90ea
```

