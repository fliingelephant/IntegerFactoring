# F162 manifest

- Date: 2026-08-12
- Type: proof-only batch-decoder candidate
- Computation: none
- Finite evidence: read-only regrouping of the frozen F157 `OUTPUT.json`
- Durable ledgers: not edited
- Closest evaluator result: P34 composite-ring product/remainder-tree
  multipoint evaluation
- Closest source results: P143/F156 and P147/F157
- Material difference: detect all signed inverse pairs in one public value
  list by one product polynomial, with derivative deflation of exact global
  partners and deterministic factor localization
- Fixed-input consequence: the F157 positive witness has 28 empty-intersection
  hits, so one public near-linear batch finds a factor without the exhaustive
  70,490,001-pair scan
- Structural compression: 65 serialized hit occurrences collapse to eight
  distinct public `(q,z,w)` triples
- Shared-block extension: a batch for each public block subset `T` detects
  every F156 pair whose full intersection equals `T`
- Complexity: soft-linear in the total normalized owner-list incidence;
  quasipolynomial for a quasipolynomial explicit source and polylogarithmic
  intersection cap
- Exact nonclaim: no collision density, all-input progress law, complete
  F156 intersection compression, or factoring algorithm is proved
- Frozen statement SHA-256:
  `0cbc91e95b6068674f04d96b7af281b5cb9a28505bbcede043f284a15f3ca89e`
- Frozen proof SHA-256:
  `a4f1767cf71d1eeeec8334ae6e293143e8c4ed886b828d99e90d07ee3134dbc9`
- Review status: candidate; fresh hostile audit and independent
  statement-only reconstruction are required before promotion
