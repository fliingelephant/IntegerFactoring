# F268-D03 independent hostile pre-run audit

# Verdict: PASS

frozen_manifest_sha256: 19e856152caebdddc374c72444acc5f1bbd727a9c722e0e183ee2f6c70cf720f

## Authentication and frozen ancestry

- The SHA-256 of the exact `FROZEN.sha256` bytes is the coordinator-supplied
  digest above. All eleven frozen entries authenticate, including
  `PROVENANCE.md`.
- The immutable D02 manifest bytes hash to
  `31e05f0f310ff6f0b37421ccf68634bf57bce65cb708074408dec96b7801561b`,
  and every D02 frozen entry authenticates. Its post-freeze hostile failure
  record hashes to
  `1b2c37510ec4680d0c8996d3654108e8727e9a44e92acf8523c550b79735a7b0`.
- The D02 directory contains only its frozen packet and hostile audit. It has
  no corpus, binary, log, preflight, selection, evidence, label-audit, or
  result artifact.
- D02's first failure reproduces exactly: its prose assigned 200,000
  candidates to every prime request, while both constrained marker-prime calls
  supplied an explicit cap of 128. Its second failure also reproduces: its
  overlap expression covered selected search/runner names, not every F265
  process command.
- Static comparison shows that D03 changes the marker-cap alignment, the
  conservative all-token F265 overlap rule, packet/output version strings, the
  corrected D03 template-version sentence, and frozen provenance/status/audit
  metadata. `FAMILY_SYNTAX.tsv` is byte-identical. I found no other semantic
  source, algebra, cohort, screen, rank, cap, projection, or command change.

## Algebra, chronology, and decoder

- For odd `N`, a canonical unit `a`, and each frozen exponent
  `N-1,N+1,N^2-1,2(N-1),2(N+1)`, the exponent is positive, even, and coprime
  to `N`. Thus `U_E(a)` is a unit in `[1,N^2)`, `Y_E(a)` is a unit in
  `[1,N)`, and `Y_E(a)^2 = U_E(a) (mod N)`.
- Direct expansion modulo `N^2` gives the frozen multiplication, inverse,
  power, and complement quotient identities with the displayed signs. The
  numerators are exactly divisible by `N`; each stated multiplier is a unit;
  and the quotient/base-carry gcd equalities follow. The implementation checks
  divisibility, congruence, and gcd equality. Only scalar `U` rows enter P66.
- If `u=gx`, `v=gy`, and `g=gcd(u,v)`, then `gcd(x,y)=1`. Hence `uv` is a
  square exactly when both `x` and `y` are squares, with positive root `gst`.
  Every singleton and unordered pair is tested and every actual relation is
  certified before P66.
- Source construction completes the full bank through stage-1 gcds, then
  freezes its rows. Stages 2--4 finish before the complete low-support scan.
  Every useful singleton or pair is retained and ends only the residual
  branch. Only verified global-sign relations enter the decoy span. P66 is
  still authenticated, and residual representatives are emitted only on the
  no-useful branch with support at least three. A later decoder or evidence
  rejection preserves complete useful low-support evidence while leaving the
  bank `RESOURCE_REJECT`, neither eligible nor null.
- Gcd-free splitting preserves every row's exact exponent vector and produces
  pairwise-coprime blocks. Exact-square blocks contribute no parity equation;
  nonsquare blocks do. Binary elimination constructs the full kernel. The
  global-decoy span and its extension satisfy the kernel quotient-dimension
  identity. Product roots, supplied roots, normalized roots, both signed gcds,
  opaque blocks, source rows, quotient representatives, and all frozen
  template predicates are independently reconstructed by replay.

## Scope, firewall, cohorts, and resources

- The seam is a finite canonical scalar-section, retrospective nonduplicate
  multirow search. It does not duplicate the fresh principal-lift results
  P211/F247 or P213/F248, the inverse-quotient/torus result P212/F245, the
  decoder-only P66/P138 results, the polynomial, matrix, elliptic-cubic, or
  quadratic-form sources F262/F264/F265/F266, or the F26 canonical-inverse
  endpoint route. It makes no asymptotic factoring claim.
- All twelve families implement the advertised 20/24 discovery and 45/48
  heldout tiers. Family 10 alone uses 20 and 45 rows. The frozen syntax table
  advertises the actual 45/48 maxima. Complete low-support classification is
  inside every eligible bank.
- Search `Case` has only public fields. Bank construction uses `N`, the frozen
  tier/family syntax, and public arithmetic outcomes. Discovery aggregation
  and ranking consume arithmetic `BankResult` statistics and never receive
  `Case`, shape, factor bits, factors, markers, or labels. Family syntax and
  exact selection bytes are authenticated. Heldout reparses every metric,
  reruns both ranking comparators, requires both rank prefixes and the embedded
  digests, and rereads no discovery evidence. Labels remain mode 0600 and are
  used only by the separate post-heldout auditor.
- The ordinary and marker constructors statically enforce deterministic
  64-bit primality, exact factor bits, distinct balanced primes, global modulus
  uniqueness, nonconsecutive neighbors, safe-safe factors, the four shifted
  gcd conditions, four distinct marker primes, cross primitive-root tests,
  bounded attempts, and explicit shortfalls. Each registered marker cell asks
  for exactly two rows. Each requested row has 4,096 seeded pair attempts; each
  constrained prime request has a 128-candidate cap. Therefore one requested
  row performs at most `4096*(128+128)=1,048,576` constrained-prime candidate
  tests, not the ordinary 200,000-candidate law. Post-run label checks verify
  all accepted-row conditions and exact cell shortfalls.
- Source, row, row-bit, gcd-free-step, block, low-relation,
  quotient-relation, relation-bit, bank-evidence, worker, aggregate-output,
  memory, disk, load, overlap, and deadline caps have explicit rejecting
  dispositions. A bank-cap crossing is `RESOURCE_REJECT`. The runner's
  `refuse_overlap` matches every command containing `F265` or `f265`; its
  bracketed expressions do not match the grep process. The gate runs before
  target creation and through every target phase.
- With all marker rows, the scale is 3,440 banks, 110,224 row powers and
  singleton tests, 1,942,040 unordered row-pair bundles, 15,536,320 stage-3
  pair gcds, and 1,942,040 support-two tests. Also,
  `2369895/3316.220420 = 714.6373581524475...`, consistent with the compiled
  `714.637358152448`; the twice-safety floor is about 5,435.036324 seconds.
  The gate takes the maximum of both measured F268 projections and that floor,
  adds twice complete corpus-generation wall time, uses real largest-shape
  45/48-row banks, and applies the stated wall, RSS, live-memory, output,
  zero-reject, and completed-48-row requirements. The timed preflight executes
  source construction, row powers, all eight pair gcds, every singleton and
  pair test, P66, the quotient, serialization, and replay, and checks the exact
  count identities.
- The frozen self-tests cover SHA-256, both tiers, unique row keys, exclusion
  and preservation of a useful pair, admission of a global singleton, a clean
  support-three quotient relation, carry algebra, P66 decoding, and selection
  reranking. Static inspection finds C++17/POSIX interfaces and no Python
  dependency in the runner or validators.

No C++ was compiled or executed. No corpus was generated, no remote command
was invoked, and no future output was inspected. This `PASS` authorizes only
the frozen validation sequence after every F265 process has ended. Any failed
compile, self-test, corpus, preflight, replay, digest, resource, output, label,
or deadline gate stops this exact packet. Any future result is finite evidence
only.
