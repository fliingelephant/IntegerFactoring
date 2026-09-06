# F260-D02 V2 fresh hostile pre-run audit

Verdict: **FAIL — DO NOT LAUNCH**

This was a static hostile audit of the exact frozen packet. I did not compile
or execute `search.cpp`, invoke or parse-run `remote_run.sh`, use a remote
host, generate or inspect a cohort, or edit a frozen file or durable ledger.

## Authentication

The SHA-256 of the exact `FROZEN.sha256` bytes is
`6a87e1dba63d60a9a5d94c08f22960db337bad9ea3eadd3f39868a87d25c0b3e`.
Every record in that file matches the local byte stream:

```text
PASS  ALGEBRA.md                 d0ceeddbab866cc9d35f85565ffc0f3282a955fd22603d666e9d00790dd00229
PASS  PREREGISTRATION.md         2ebd75dea01d34fe72682d45524abc2e6072618866393d963ba6dccd221059d7
PASS  search.cpp                 c6d0f016e471911c115a497311ef05e5682c796df6c3887626ac5cb25bcb3911
PASS  remote_run.sh              6812855a4ef7b87c351cfe1c29d098dae0470788139d9ca27b7c8d94f5de43be
PASS  PROVENANCE.md              b8f019b4e9b78cec7fcd772fb75ca7395c881ae6793db711bc78fe14991d9c59
PASS  VALIDATION_PENDING.md       34baff67c8af30225206e32d8009c3be1dee06d405532bd6857baf82e14a4c6f
PASS  STATIC_REVIEW.md            297f87601eaab098cb18cc6244543bbd7c80c390b2ba575879f80e41f3ec04a3
PASS  AUDIT_REQUEST.md            63ce96dcaa52114b7d18a1e4e516bc63db76cd533089abbbf7389c4fa8f48a54
PASS  PRELAUNCH_MANIFEST.md       f85d202ea5bf7247a74da99c57b76703ba9d91b6d04430c4cccfda42b09918eb
```

The immutable D01 provenance also authenticates exactly. The hashes of the
D01 algebra, preregistration, final source, runner, prelaunch manifest, and
FAIL audit are, respectively,
`09691b4f5d005a330b85952dd9bfe4a0b93c2e5de7c23832d53572d4db5700a2`,
`3b9c13374e38cba1394e9528fccb5ab623a6164829a3394f434f6b81acf38714`,
`d4263fb8ceef91caecc4480ee3b49d8cd670b6ff34bb0920d8469c47ddf7e44e`,
`7215ee1d9e34ee34146ca8ed992e96c582defc0cfd7b40bba39a91b78e98d103`,
`7087694e8019280675f660eae88eec88620f33ffca323d29b180c33100d13d05`,
and
`9e49fb75f86b5ccdd7b3290053099cd822ab547a06495dbee82f64ff7a5e636d`.
The predecessor verdict remains `FAIL — DO NOT LAUNCH`.

## Decisive blocker: the frozen canonical grammar is not implemented

The preregistration requires two distinct ordering rules:

1. a duplicate semantic fingerprint is represented by the lexicographically
   first normalized syntax; and
2. only after normalization, candidates are sorted by
   `(depth, normalized syntax length, normalized syntax)`.

The source instead sorts raw sequence candidates with the second rule and
then keeps the first fingerprint (`search.cpp:952-960`). Those rules are not
equivalent. The mismatch has a forced example in the frozen grammar.

Every `dyadic_carry` value is zero or one. Exact-value canonicalization thus
leaves at most two values. On a one-value sequence, both `adj_diff` and
`adj_sum` are empty. On a two-value sequence, both transforms are the
one-value sequence `[1]`. They therefore have the same 192-bit semantic
fingerprint on every one of the 24 public synthetic inputs. Lexicographic
normalization requires

```text
seq:dyadic_carry:adj_diff
```

as representative. The source's length-first order keeps the shorter

```text
seq:dyadic_carry:adj_sum
```

instead. This is an actual duplicate, not a hypothetical hash collision.

The same ordering defect reaches commutative word syntax. Word children are
emitted in retained sequence-index order (`search.cpp:983-990`). That index
order is `(depth,length,syntax)`, not normalized-syntax order. For example,
the depth-zero `dyadic_carry` identity precedes its depth-one adjacent
transform in the vector, although `adj_*` precedes `id` lexicographically.
The resulting nonnormalized word string is also the input to the frozen
`syntax_hash(name) % 5` admission rule. The defect can therefore change the
sparse word set, normalized names, program IDs, syntax tie-breaks, and the
authenticated 32-row selection. Semantic fingerprints do not repair an
order-dependent grammar after enumeration.

This is a direct regression at the V1 canonical-grammar repair boundary. It
changes frozen discovery semantics, so target validation cannot qualify this
packet.

## Additional frozen-output mismatch

`ALGEBRA.md` says that word evaluation records both residuals through their
logarithms and extrema. The source retains only per-row logarithms and sums
them into `Cell` (`search.cpp:1568,1794-1796,1865-1867`). The only word
output fields are `mean_log_rp` and `mean_log_rq`
(`search.cpp:2068-2069,2094-2096`). There is no residual minimum, maximum, or
per-row word stream from which an extremum can be reconstructed. This does
not alter selection order three, but it removes a frozen diagnostic promised
for symbolic pattern discovery.

## Boundaries that passed static reconstruction

Subject to the failed grammar boundary, the following repairs are present in
the authenticated source:

- The primary return laws, direct and stripping factor probabilities,
  strict growth, factor-or-growth, and expected log-lcm gain match the frozen
  formulas. Expected gain uses one support pass and has no D01
  product-over-all-other-primaries loop.
- Operational `M=1` and `M=2` are separated from the hidden gcd state. The
  three dyadic channels use capped integer lcm states and retain separate
  distributions.
- P205 uses the hard residual after baseline-support removal. Collision and
  pair-Miller denominators use ordered pairs of distinct canonical values.
  The direct joint average implements the registered P241 quantity.
- Common, transformed, pair, smooth-support, recursive-oracle, and saturation
  gcd paths are present. Proper factors retain row identity, source, and
  exact factor. Hypergeometric candidates use identity only, and the full
  central binomial control is not materialized.
- Recursive factorizations remain nonoperational, receive a separate
  discovery ranking, and are rejected by held-out selection parsing.
- Prime, safe-prime, next-prime, factorization, and cohort retries have finite
  source caps. Counts, factor sizes, balance, hostile structure, and
  cross-split modulus distinctness match the frozen tables.
- The selector takes the literal first eight positions of each complete
  order before order-one fill. Selection and discovery-corpus bytes are
  hashed, checked, and parsed from the authenticated buffers before held-out
  generation.
- Aggregates retain factor size. The lead writer checks all four held-out
  sizes, both hostile cohorts, the 40-to-60 upper-median loss change, the
  four expected-mass cells, and all collision-anomaly cells. A null lead does
  not fail the runner.
- The runner authenticates frozen and audit bytes, refuses overwrite and
  incompatible production, applies worker, deadline, memory, file, output,
  exact-set, TSV, digest, manifest, and resource gates, and uses one shared
  production deadline.

## Validation status and disposition

`VALIDATION_PENDING.md` accurately withholds compilation, self-test,
benchmark, runtime, memory, output projection, runner behavior, and all
cohort evidence. This audit makes no claim about any of them.

Do not launch F260-D02. Preserve these frozen bytes as the failed V2 packet.
A repair needs a new experiment freeze with one explicit normalized-syntax
order used for duplicate representatives, commutative children, syntax
hashing, IDs, tie-breaks, and selection. It must also add the promised
residual extrema or remove that promise before freezing.
