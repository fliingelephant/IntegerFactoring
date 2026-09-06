# F268-D04 independent hostile pre-run audit

# Verdict: PASS

frozen_manifest_sha256: de76f2e3fbb264b917cedb5639fde75c979f272e43841452c6f642b8132cdbf4

## Authentication, D03 failure, and exact repair

- The SHA-256 of the exact `FROZEN.sha256` bytes is the coordinator-supplied
  digest above. All eleven frozen entries authenticate, including
  `PROVENANCE.md`.
- The immutable D03 manifest bytes hash to
  `19e856152caebdddc374c72444acc5f1bbd727a9c722e0e183ee2f6c70cf720f`,
  and every D03 frozen entry authenticates. Its hostile `PASS` bytes hash to
  `23a3e7921fa54ee1c7048ed7fc05b116f61ee76b88af2fb2275d7b13f8bd3a04`.
  Its packaged failed-validation `RESULT.md` and `RUN_MANIFEST.md` hash to,
  respectively,
  `399fcea77a78c26cbfdab214dc00d186474a3ed898acb3ff0ddc2ebf16e6e459`
  and
  `f493a1302f44a9d3b3798156813bde2c3a88e7a1ba5225b3246c841974d295e9`.
- The D03 failure reproduces from the authenticated source and record. Its
  custom table has `0x2748774U` at SHA-256 round constant 46 instead of the
  standard `0x2748774cU`. Both frozen expected family digests and the external
  digest agree, so the custom digest must fail first. The authenticated log
  contains exactly `F268_SEARCH_FATAL family syntax SHA mismatch`.
- The stopped chronology is preserved. The first runner invocation stopped
  before target creation because `/usr/bin/time` was absent. After the standard
  `time` package was installed, the same frozen runner compiled all three C++
  programs, passed the corpus self-test, and failed the search self-test. No
  label self-test, corpus generation, preflight, discovery, heldout, or search
  evidence followed; the packaged preflight directory is empty.
- D04 contains standard constant `0x2748774cU` exactly once and no
  `0x2748774U` token. In `self_test`, the existing `sha256_bytes("abc")`
  known-answer test is the first SHA consumer and precedes
  `authenticate_family_syntax`.
- Direct D03--D04 comparison finds no unauthorized semantic change. Apart
  from that constant repair and test reordering, changes are D04 packet/output
  tokens and frozen provenance, status, audit, and manifest metadata.
  `FAMILY_SYNTAX.tsv` is byte-identical. The seed, grammar, cohorts, screens,
  ranking, caps, projections, and target commands are unchanged.

## Algebra, low-support chronology, and P66 replay

- For odd `N`, canonical unit `a`, and each exponent
  `N-1,N+1,N^2-1,2(N-1),2(N+1)`, the exponent is positive, even, and coprime
  to `N`. Hence `U_E(a)` is a unit in `[1,N^2)`, `Y_E(a)` is a unit in
  `[1,N)`, and `Y_E(a)^2 = U_E(a) (mod N)`.
- Expanding modulo `N^2` gives the displayed multiplication, inverse, power,
  and complement quotient identities. Their numerators are exactly divisible
  by `N`; signs and unit multipliers are correct; and the quotient gcd equals
  the base-carry gcd, while the complement quotient has gcd one. Source checks
  divisibility, congruence, and gcd equality. Only scalar `U` rows enter P66.
- For `g=gcd(u,v)`, write `u=gx`, `v=gy` with `gcd(x,y)=1`. Then `uv` is a
  square exactly when `x` and `y` are squares, and its positive root is `gst`.
  Source and replay classify every singleton and unordered pair and verify
  every exact root and both signed gcds.
- The bank is completed through all stage-1 source gcds before its rows are
  used. Direct stages 2--4 finish without changing it. The complete singleton
  and pair scan follows. Every useful low-support certificate is counted and
  serialized; none enters the decoy span or is relabelled residual. Only
  verified global-sign vectors enter the span. P66 is authenticated next.
  Residual vectors are emitted only on the no-useful branch and have support
  at least three.
- Gcd-free refinement produces pairwise-coprime blocks and reconstructs every
  row from exact exponent vectors. Square blocks add no parity equation.
  Binary elimination constructs the complete kernel. The decoy-basis extension
  checks `low_dim + residual_dim = kernel_dim`; every remainder is independently
  in the kernel. Exact products, positive roots, supplied roots, normalized
  roots, both signed gcds, block data, source rows, quotient representatives,
  and frozen template predicates are reconstructed by replay.
- A later decoder or evidence cap preserves a completed useful singleton or
  pair and the complete low-support record. Such a bank remains
  `RESOURCE_REJECT`, ineligible, and non-null, with no blocks or residuals.
  The dedicated self-test exercises this disposition.

## Seam, syntax, firewall, and cohorts

- The scope is only a finite canonical scalar-section and retrospective
  nonduplicate multirow search. It does not duplicate P211/F247 or P213/F248
  fresh principal-lift results, P212/F245 inverse-quotient/torus results,
  P66/P138 decoder results, F262 polynomial rows, F264 matrix rows, F265
  elliptic-cubic rows, F266 quadratic-form rows, or the F26 canonical-inverse
  endpoint route. It makes no asymptotic factoring claim.
- All twelve discovery families implement 20/24 rows; only four authenticated
  heldout families implement 45/48 rows. Family 10 alone has 20/45 rows. The
  syntax table advertises 45/48 maxima. All twelve template predicates match
  source, and complete low-support testing stays inside every eligible bank.
- Search `Case` contains only public split, shape, factor bits, index, and `N`.
  Source generation uses only `N`, family syntax, the frozen row target, and
  public gcd outcomes. Discovery aggregation and ranking receive arithmetic
  `BankResult` values, never `Case`, factors, markers, or labels. Family syntax
  and exact selection bytes are authenticated; heldout reparses and reranks
  all fields, requires the exact rank prefixes and embedded digests, and reads
  no discovery evidence. Mode-0600 labels enter only through the separate
  post-heldout auditor.
- The constructors enforce deterministic 64-bit primality, exact factor bits,
  distinct balanced factors, global modulus uniqueness, the public neighbor
  skip and nonconsecutiveness, safe-safe factors, all four shifted gcds, four
  distinct marker primes, and all cross primitive-root tests. The label auditor
  independently checks these conditions and exact shortfalls.
- Each registered marker cell requests exactly two rows. Each requested row
  has 4,096 seeded pair attempts, with at most 128 candidates for each of its
  two congruence-class prime requests. Thus the bound is exactly
  `4096*(128+128)=1,048,576` constrained-prime candidate tests per requested
  row. The ordinary 200,000-candidate cap is not substituted.

## Resource, overlap, preflight, and runner gates

- Source attempts, rows, input-row bits, gcd-free steps, blocks, low relations,
  quotient relations, relation bits, evidence bytes, workers, aggregate output,
  memory, disk, load, overlap, and deadline all have explicit stop or rejection
  dispositions. A bank cap produces `RESOURCE_REJECT`, never a null bank.
- `refuse_overlap` rejects every process command containing `F265` or `f265`,
  including packet paths and all named phases. Its `[F]265|[f]265` expression
  does not match the grep process. The gate runs before target creation and in
  every target phase through `capacity_gate` or `run_phase`.
- With all marker rows, the exact staged scale is 3,440 banks, 110,224 row
  powers and singleton tests, 1,942,040 pair bundles, 15,536,320 stage-3 pair
  gcds, and 1,942,040 support-two tests. Also,
  `2369895/3316.220420 = 714.6373581524475...`, matching the compiled
  `714.637358152448` rate.
- Preflight uses the largest real case in each available shape and all twelve
  families, with ordinary heldout 45/48-row layouts. Its timed path includes
  family authentication, public parsing, source grammar, every row power, all
  eight pair gcds, every singleton and pair test, P66, quotienting,
  serialization, and replay. Exact recorded count identities, zero rejects,
  and at least one completed 48-row bank are required.
- The gate takes the maximum of the measured pair-scaled and task-scaled F268
  projections and the twice-safety F265 empirical floor, then adds twice full
  corpus-generation wall time. It gates output, measured RSS, and
  `512 MiB + 4*projected output` against the frozen limits. The runner uses
  C++17 and POSIX tools only; the programs and validation sequence have no
  Python dependency.
- Self-tests cover SHA-256 before artifact authentication, both row tiers,
  unique `(base,exponent)` rows, a useful support-two certificate excluded from
  the decoy quotient and preserved across later rejection, a global singleton
  admitted to it, a clean support-three quotient relation, carry algebra, P66
  decoding, and selection reranking.

No D04 C++ was compiled or executed. No corpus was generated, no remote command
was invoked, and no future output was inspected. This `PASS` authorizes only
the frozen validation sequence after every F265 process has ended. Any failed
compile, self-test, corpus, preflight, replay, digest, resource, output, label,
overlap, or deadline gate stops this exact packet. Any future result is finite
evidence only.
