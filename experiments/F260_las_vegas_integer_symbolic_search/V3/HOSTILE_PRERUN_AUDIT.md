# F260-D03 V3 fresh hostile pre-run audit

Verdict: **PASS — CLEARED FOR LAUNCH**
FROZEN_SHA256=303643eaffb5250c147123af3409f588b5acf8636012d2d780203324ce3b20b2

This is a static hostile audit of the exact frozen packet. I did not compile
or execute `search.cpp`. I did not invoke or parse-run `remote_run.sh`. I did
not use a remote host, generate or inspect a cohort, or edit a frozen file or
durable ledger. Target qualification remains mandatory.

## Authentication and predecessor boundaries

The SHA-256 of the exact `FROZEN.sha256` bytes is
`303643eaffb5250c147123af3409f588b5acf8636012d2d780203324ce3b20b2`.
Every record in that file matches the local byte stream:

```text
PASS  ALGEBRA.md                 f94ad4119a2bb6bb4e795da536a7bf29823b6e2d1c509c51e9b42e27a26d490f
PASS  PREREGISTRATION.md         b8cd3e88b77aa2dd84ca655436a8e2dbd1e68100f827c89eb0b64abb006aefcf
PASS  search.cpp                 1359cd6cdec022e01c19d6b704cd6705fdee2cb3db190058386aa3c49debdebc
PASS  remote_run.sh              098b586bb237c821ec47919e6667ff0abe8ccf785e8fc703492636185a9e2699
PASS  PROVENANCE.md              05e1b77d6182350039a24f120e49231894d0367b2b246d65ee05458b9782fc3f
PASS  VALIDATION_PENDING.md       d2dc1ef9e96549304debb34c859b5c7f698e2a9c3b1e4d7a8f62d22353cbcd59
PASS  STATIC_REVIEW.md            64b97371317aab2f15fb5a8e68153a6cb1df07652d62ef25676780abbc156bfd
PASS  AUDIT_REQUEST.md            b7f9b7e1dc6a8329ac1cc1a6ce916452b84d4c310cc0a959d6757b1c6258aa4c
PASS  PRELAUNCH_MANIFEST.md       7fbe8f0ab2befcc1b6f27e8234c166e93316acf73bbbf863356f58780e23d53b
```

The immutable D01 boundary in `PROVENANCE.md` also matches:

```text
PASS  ../ALGEBRA.md              09691b4f5d005a330b85952dd9bfe4a0b93c2e5de7c23832d53572d4db5700a2
PASS  ../PREREGISTRATION.md      3b9c13374e38cba1394e9528fccb5ab623a6164829a3394f434f6b81acf38714
PASS  ../search.cpp              d4263fb8ceef91caecc4480ee3b49d8cd670b6ff34bb0920d8469c47ddf7e44e
PASS  ../remote_run.sh           7215ee1d9e34ee34146ca8ed992e96c582defc0cfd7b40bba39a91b78e98d103
PASS  ../PRELAUNCH_MANIFEST.md    7087694e8019280675f660eae88eec88620f33ffca323d29b180c33100d13d05
PASS  ../HOSTILE_PRERUN_AUDIT.md  9e49fb75f86b5ccdd7b3290053099cd822ab547a06495dbee82f64ff7a5e636d
```

The D01 verdict remains `FAIL — DO NOT LAUNCH`.

The complete D02 boundary also matches:

```text
PASS  ../V2/ALGEBRA.md                       d0ceeddbab866cc9d35f85565ffc0f3282a955fd22603d666e9d00790dd00229
PASS  ../V2/PREREGISTRATION.md               2ebd75dea01d34fe72682d45524abc2e6072618866393d963ba6dccd221059d7
PASS  ../V2/search.cpp                       c6d0f016e471911c115a497311ef05e5682c796df6c3887626ac5cb25bcb3911
PASS  ../V2/remote_run.sh                    6812855a4ef7b87c351cfe1c29d098dae0470788139d9ca27b7c8d94f5de43be
PASS  ../V2/PRELAUNCH_MANIFEST.md            f85d202ea5bf7247a74da99c57b76703ba9d91b6d04430c4cccfda42b09918eb
PASS  ../V2/FROZEN.sha256                    6a87e1dba63d60a9a5d94c08f22960db337bad9ea3eadd3f39868a87d25c0b3e
PASS  ../V2/HOSTILE_PRERUN_AUDIT.md          281945088bf2b9d701c55c0cab6663ad8842daf80a6fe883129a4ea5b22d6a29
PASS  ../V2/HOSTILE_PRERUN_AUDIT.sha256      e8b23b346715fd23964db11496932522228af6a69948ad65c963af75fe82e975
```

Every D02 `FROZEN.sha256` record matches. Its one-record audit sidecar also
verifies. The D02 verdict remains `FAIL — DO NOT LAUNCH`. No predecessor byte
is part of this PASS.

## Decisive D03 regression review

The D03 source enumerates all sequence candidates before fingerprint
grouping. Each fingerprint map retains the lexicographically first complete
syntax. It then applies `(depth,length,syntax)` ordering and the type cap.
The word and factored paths use the same order of operations. No type uses
the D02 length-first representative rule.

Each two-sequence word compares the complete retained sequence names first.
It constructs one canonical `word:left*right` name from that order. The same
name controls the modulo-five admission test and remains on the candidate
through semantic fingerprint grouping, type ordering, global ID assignment,
grammar output, ranking tie-breaks, selection output, and held-out syntax
validation. Thus an index order cannot change the sparse grammar.

The forced D02 `dyadic_carry` collision is repaired by the general map rule.
`seq:dyadic_carry:adj_diff` is lexicographically earlier than
`seq:dyadic_carry:adj_sum`, independent of depth and length. There is no
candidate-specific exception.

Every word row initializes or updates four residual extrema. Worker merging
copies the first populated cell and then takes global minima and maxima.
Aggregate output emits mean, minimum, and maximum for `log2(r_p)` followed
by the same three fields for `log2(r_q)`. It emits zero in all four extrema
fields for non-word rows. The header and row each contain exactly 45 fields.
The runner requires 45 fields in both aggregate files.

A complete source and runner diff against authenticated D02 contains only
these canonicalization and extrema changes, D03 names, the 45-field checks,
the new self-test assertions, and the added D02 conflict needle. The master
seed, score functions, source bases, transforms, grammar admission clauses,
cohort tables, rank functions, literal top-eight selector, lead gates,
worker count, caps, and deadlines are unchanged.

All source output names, digest labels, manifest names, held-out path checks,
process resource tags, error tags, runner status text, and runner manifest
names use D03. The retained `F260D02...` seed literal is the preregistered
unchanged master seed, not an experiment label. The process firewall now
also rejects active F260-D02 production.

## Inherited mathematical and experimental boundaries

The annihilator implementation reconstructs the exact local return-order
law. It computes direct factors, stripping factors, strict growth,
factor-or-growth, and expected log-lcm gain with the registered formulas.
The expected-gain loop has one pass over the relevant primary laws. The D01
product-over-all-other-primaries loop is absent. The final smooth path also
uses public support caching and the registered balanced-factor screen.

The operational states `M=1` and `M=2` are distinct. The hidden gcd state is
stored only as a diagnostic. Each dyadic channel uses capped integer lcm
states, keeps its own exact distribution, and contributes only within its
own maximum channel.

The word score implements P205 with `H`, hard residuals, both residual logs,
and baseline improvement. Sequence values are canonical distinct values.
Collision and pair-Miller denominators therefore contain only ordered pairs
with different indices and different values. Baseline-supported primaries
are removed before captured-log scoring. Direct joint averaging implements
the registered P241 quantity.

Common leaves, transformed values, pair differences, smooth support,
recursive-oracle primaries, and saturation outcomes all have explicit gcd
paths. Proper factors retain the public row, source syntax, and exact factor.
Hypergeometric candidates use identity only. Their endpoints use short
factorial-ratio products. The full central binomial control is not
materialized.

The six recursive factorizations are nonoperational. They receive a separate
diagnostic ranking. Normal selection omits them, the selection parser rejects
them, the restricted grammar checks them again, and the lead gate requires
an operational non-oracle candidate.

Every prime, safe-prime, next-prime, factorization, and cohort loop has a
source cap. The source enforces exact factor bit length, primality, balance,
safe-safe and consecutive structure, the frozen row counts, and global
modulus distinctness across discovery and held-out.

The four discovery orders are complete. The selector takes only the literal
first eight entries from each order, forms their ordered union, and then
fills from order one. Selection and public discovery-corpus bytes have
independent digests. Held-out authenticates and parses those same bytes,
checks all selection identity fields, and uses no discovery score file.

Aggregates remain keyed by program, split, factor size, and cohort. The lead
writer checks all hostile cells at all four held-out sizes, both 40-to-60
loss changes, all four expected-mass cells, operational status, and all
collision-anomaly cells. A null lead is output and does not fail execution.

The runner authenticates the frozen packet and this audit binding before it
creates production state. It refuses overwrite and conflicting production.
It applies resource, compile, self-test, benchmark, projection, worker,
memory, file, live-output, exact-set, row, field, digest, phase-manifest, and
shared production-deadline gates. It rechecks conflicts before and during
each stage and at both split boundaries.

## Qualification boundary

`VALIDATION_PENDING.md` accurately withholds compilation, self-test,
benchmark, runtime, memory, output projection, runner execution, and all
cohort evidence. This static PASS permits only the registered runner path.
The runner must still authenticate these exact bytes and pass every target
gate before discovery can start.
