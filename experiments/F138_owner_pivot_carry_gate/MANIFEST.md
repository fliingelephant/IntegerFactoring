# F138 manifest

## Outcome

The proposed universal max-digit owner-pivot cancellation claim is false.
The strongest registered certificate puts a universe-private prime row at
the largest declared F133 integer anchor `a=E` and digit `A=E-1`. Its
canonical residue `2E` lies beyond the initial seed bank. A separate exact
four-column certificate has no degree-one row but has zero binary kernel.
The same `2E` residue is already an F130 support-one word, so this refutes
universal owner-pivot cancellation, not a narrower new-F133-value claim.

The result also gives the exact cross-star carry condition

\[
k_b+bA\equiv k_d+dB\pmod r.
\]

This is not a complete-source failure theorem. Other source positions can
still factor the registered inputs or create a useful kernel.

## Main hashes

| File | SHA-256 |
|---|---|
| `RESULT.md` | `f6ac31e00bbf81b67f4cc64137f108fbe2224b3c5ba629e32bbabab58f0832be` |
| `PREREGISTRATION_QPOLY_MAX_DIGIT.md` | `10c1fbf6193f53f978c0f3f0132d5cb02839d2af3e9244155f099de5f1a9dc1f` |
| `PRE_RUN_PINS_QPOLY_MAX_DIGIT.md` | `f51e51948f39f832eba058bed9ca82049221d3d876643c1281e20726e5568243` |
| `verify_qpoly_max_digit.sage` | `6e5b5d9f5e0e537ba5ba9205f92ca1555cfda8a28131343e534d3ba8e8d8a578` |
| `OUTPUT_QPOLY_MAX_DIGIT.json` | `87c522e6cb7c99ee1e07461ffd3bd1d282cf770f51b8b35e0da6d9ced75c057d` |

## Supporting hashes

| File | SHA-256 |
|---|---|
| `PREREGISTRATION.md` | `ecef6d34c431c14fb0b8283af705e7d25cea75c68d546f39613e61f287a87607` |
| `PRE_RUN_PINS.md` | `fa6d3a695d70541eeb3e74f62c9a014934ff1f9402f79e98092c2b4bd972dd8b` |
| `verify.sage` | `eba2c33af941e64d069e4567fdf2ea24bb868966d0ae9d9c3c5a62bc5df517ef` |
| `OUTPUT.json` | `900aec82966ab9d082095f038e3dff3aabef560fd1d1641bb1a434e02aac0462` |
| `UNREGISTERED_SYNTAX_CHECK_OUTPUT.json` | `900aec82966ab9d082095f038e3dff3aabef560fd1d1641bb1a434e02aac0462` |
| `FAILED_RUNS.md` | `860bca2ef8183d15308979342771ecc0e890b5f0a92d47a24821c64fc78ca238` |
| `PREREGISTRATION_NONZERO_ARM.md` | `0f8957ed7db8ab839aa439ab8270e200ad7a0f85867f15593ce456cb1e74dd50` |
| `PRE_RUN_PINS_NONZERO_ARM.md` | `a02839405cc928c9fb7083a788aff04fc9b29d94857a3a9bc481447a06b9b66c` |
| `REVISION_NONZERO_ARM_1.md` | `e2bbb483cd385201f36984e560194e1de1df56c975b503025e8095ee48e6f7f3` |
| `PRE_RUN_PINS_NONZERO_ARM_REVISION_1.md` | `1eb0d4a73640e840abb758d0314d42bc610c777ccb950bd9bcf7d41566e4065e` |
| `verify_nonzero_arm.sage` | `0916d04b9397e1c8202004cc08ec5a7522e1045392071cdfe6f4e77bab8ea6c9` |
| `OUTPUT_NONZERO_ARM.json` | `4674189fb15db499cf68b82041d65afbd5819f78f4037417538c0947488f16db` |
| `FAILED_NONZERO_ARM_RUNS.md` | `d16a12bd7b26742fea039f5336b8901a602fbd5f9fc1f1b3489f61b44a3d1088` |
| `HOSTILE_AUDIT.md` | `16c70c0b6602bcfb94bf241dd1d475613436ae8e61e7f6b7ffbcbc648015b514` |
| `BLIND_RECONSTRUCTION.md` | `0238ffed30d9d370f4f3902f1072b8d5386042382114334aa79f9cbb5ff38545` |
| `RUN_QPOLY_MAX_DIGIT_SANDBOX_FAILED.md` | `28b057bdb19e3af06ff6ed37c7ac2e9b24b9355e9f61454a7ff539d5adcba406` |

The accidental syntax-check execution and the first nonzero-arm reporting
failure are preserved. Neither is used as authoritative evidence. The local
maximum-digit replay first failed because Sage's default state directory was
not writable in the workspace sandbox. That environment failure and its hash
are preserved in `RUN_QPOLY_MAX_DIGIT_SANDBOX_FAILED.md`.

Sage-generated `.sage.py` files are execution by-products. They are not
evidence and are not pinned.

## Audit status

The frozen result passed a full artifact hostile audit and an independent
result-only blind reconstruction. The hostile audit reran all registered
verifiers and reproduced their pinned JSON files. The blind reconstruction
used independent proof-mode Sage checks but did not inspect the source
implementations. The result is eligible for narrow promotion. No cross-family
audit, human audit, or publication-level literature review has run.
