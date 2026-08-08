# F102 hostile audit

**Verdict: PASS, in the stated finite and factor-assisted scope.**

I found no theorem error, count error, provenance error, or hidden factoring
claim. The result is a lossless compression theorem for one frozen binary
matrix and an exact diagnosis of the pinned F98 data.

## The theorem

Let row `r` have active degree one, with unique incident column `j`. The row
equation forces coordinate `j` to be zero in every kernel vector. Restriction
to the other columns is therefore a kernel isomorphism. Its inverse inserts a
zero at coordinate `j`. One peel preserves nullity and removes one unit of
rank. Repeated peels preserve the full kernel after zero coordinates are
restored.

The final column set is unique. Call a column set stable when every row that
meets it has degree at least two. During any peel order, every stable set is a
subset of the active columns: if a deleted column were in a stable set, its
forcing row would have degree one in that set. The final set is itself stable.
It is therefore the unique largest stable set. This also proves order
independence.

This proof applies only after the batch is frozen. It does not permit a
streaming collector to discard a column. A later column can reuse the row
that was private at the time of deletion.

## Independent finite replay

The independent verifier did not import the candidate source. It regenerated
the F98 first-occurrence stream, deduplicated exact values, factored all 9,414
nonzero values, built the prime-parity matrix, and used a different
highest-pivot rank routine. It peeled once with the smallest forcing prime
first and once with the largest forcing prime first. Both orders returned the
same full and prefix cores.

The replay confirmed all reported summary fields, both complete row-degree
histograms, both core-degree histograms, both core hashes, both component
lists, the factor-count histograms, and all provenance fields.

| Frozen pool | Columns | Rows | Rank | Nullity | Initial degree-one rows | Peeled columns | Core columns | Core rows | Core rank | Core nullity |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Full F98 pool | 9,414 | 11,034 | 8,926 | 488 | 7,884 | 7,633 | 1,781 | 1,299 | 1,293 | 488 |
| First occurrence before raw record 5,616 | 4,293 | 5,658 | 4,291 | 2 | 4,062 | 3,920 | 373 | 387 | 371 | 2 |

The rank losses equal the deleted-column counts:

```text
8926 - 1293 = 7633
4291 - 371 = 3920
```

Each core has one connected component in the prime-support column graph. The
full core hash is
`5e18521931048141bdc4c09f23af1b8b9e7d0b5b95bb70b42b420443c6f2cbc8`.
The prefix core hash is
`9b75bad6177686931cc714931b37bdf4e42823db4d0121b7e8859dff3c1260df`.

All 166 columns of the pinned public certificate are in the full core. The
full core has 3 seed relations and 1,778 feedback relations. The seeds are
2, 11, and 27. The feedback relations cover 8 active-pair families. Their
orientation counts are 1,138 and 640; both orientations occur.

## Scope pressure

- This is a factor-assisted prime matrix. The pinned public gcd-free decoder
  has 11,015 nonsquare block rows, while this diagnostic has 11,034 prime
  rows. Their reported ranks agree at 8,926, but their row presentations are
  not the same. This audit does not claim that the displayed peeled core is
  directly available to the public decoder.
- Connectedness means connectedness in the factor-assisted prime-support
  graph. It does not imply a non-global square root. It does not measure the
  probability that a sampled dependency factors `N`.
- Membership of the 166-column certificate proves that the certificate is
  not outside, or in a separate component from, the large core. It does not
  prove that useful certificates are typical in that core.
- The prefix rank defect shows only that more columns than rows is not needed
  for this finite dependency. It gives no input-uniform density statement.
- No tested statement forces a nonempty core, a rank defect, or a useful root
  for every composite input. No tested statement gives an inverse-polynomial
  success rate. No tested step is a factoring algorithm.

Thus the exact claim that survives is narrow but nontrivial: for this frozen
F98 batch, 7,633 of 9,414 relation columns are provably absent from every
dependency, while the complete 488-dimensional kernel and the known useful
certificate remain in a unique 1,781-column core.

## Evidence pins

Candidate pins include:

```text
62e08b8fb396df3fbc65f527e7df6d687d4e75661f92e8cf98cd98f95e31c20d  RESULT.md
dd39810e627dc6e89725b77e4abd36bcb9fa9b40436a94941921b569eae14c7d  analyze_full_core.sage
6ac7f0e543fadae37ebbfc998bc314aceed02664d023a62506587cfe8a9ab6bc  OUTPUT.json
ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab  ../F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json
```

Independent audit pins:

```text
b25619738a85b495f101118e42c4fcae2d4f43f1ba4933e72dcb6ca20491ed9d  audit_verify_full_core.sage
5697a792997ee1c2cf6af15c90e52d1a5a02f6bbdc56563aafef8a2b8dea9d8e  AUDIT_VERIFY_OUTPUT.json
56f1d9957e26aa69283258f96e7f711f0759a4731af8196d070326a68c8c042e  AUDIT_VERIFY_RUN.log
3297fad24f965cd92b5d77481cd2c3342c6b0e5374eeb6f4002a284db201173e  AUDIT_VERIFY_FAILED_RUN.log
d9b6c1cb725af41304a9c32d0e17fc304ed639ad6f7a5cf3d0975ed72145ba58  AUDIT_RUN_MANIFEST.md
```

The authoritative audit run exited zero under a 180-second hard timeout. It
took 2.14 seconds. The named audit source predates its output and log. The
audit-only failed run is preserved and does not support this verdict.
