# Verdict: FAIL
frozen_manifest_sha256: 723314508048e2a2de692314764ad83ab78ffc84ce10d10cce27b39d759dde2e

# F266-D02 hostile pre-run audit

**DO NOT COMPILE, SELF-TEST, PREFLIGHT, OR LAUNCH THIS FROZEN PACKET.**

This was a fresh static hostile audit. I did not compile or execute
`search.cpp`, invoke `remote_run.sh`, access the remote host, generate a
corpus, or inspect a discovery or held-out cohort.

## Frozen-artifact authentication

The SHA-256 of `FROZEN.sha256` is the authenticated manifest root shown
above. All five entries in that manifest match the local bytes:

```text
PASS  ALGEBRA.md             0b1d5c0f7dd8843c16834bd8f319ea267cb7431ab4a321bc1f4ab7dec0b7b0dd
PASS  PREREGISTRATION.md     8cdec3544e965e8cca433670bf365f5350a702b45916d9fd9580759743e88942
PASS  search.cpp             1b53b8026a5ff95592e24d267275bf590d89539bbaf2bcf6b944fb77bd655efd
PASS  remote_run.sh          7605b165feb8377dc2131509bd0cd7fe34546f2ce58fe09fc5a54501bc79a8c3
PASS  PRELAUNCH_MANIFEST.md  c1f11236a9f095164e6124e4644b61156dbf9fba46cf0cf6e6318641b7cb1e39
```

The immutable predecessor provenance also authenticates:

```text
PASS  F266-D01/FROZEN.sha256             1ebfeff0b66cdec024a9612279675f435ad668059289865b581bf4d2b74a70e8
PASS  F266-D01/HOSTILE_PRERUN_AUDIT.md   4880f3467e790519f39e278a78c0c808fd9b350afaafaf22c998823ec5cfc9c2
```

All five D01 manifest entries also match their local bytes. D01 remains an
immutable failed packet.

## Decisive blockers

### 1. The finite-null cell gate implements the wrong quantifier

The frozen rule requires at least 24 eligible moduli in every held-out
size/shape cell **for one selected family**. This is

```text
exists family: for every cell, eligible(family,cell) >= 24.
```

The executable instead loops over cells first and accepts if some family
covers each individual cell (`search.cpp:1776-1782`). It implements

```text
for every cell: exists family, eligible(family,cell) >= 24.
```

Different families may therefore cover different cells while no selected
family covers the complete held-out grid. Such a run can receive
`finite_null_signal=1` even though it fails the preregistered coverage rule.

The cell anomaly table has a related evidence defect. A cell row is created
only inside `if (b.eligible)` (`search.cpp:1766-1771`). A cell with no
eligible bank is omitted instead of being reported with zero comparison
mass. Singleton observations from a bank that later becomes a decoder
resource rejection are also omitted, although singleton screens occur before
decoder eligibility is decided. This is not the promised report for every
cell.

### 2. Final compression is not under the whole-packet deadline

The compression pipeline is

```text
timeout REMAINING nice -n 15 tar ... | zstd -q -T1 -3 -o ARCHIVE
```

(`remote_run.sh:256-264`). `timeout` governs only the `tar` process on the
left side of the pipe. It does not govern `zstd` or the enclosing pipeline.
The `zstd` process also does not inherit the `nice -n 15` applied only to
`tar`. Thus compression as a phase has neither the registered remaining-wall
timeout nor the packet's stated niceness. A stalled compressor can exceed the
four-hour packet cap. The later archive hash cannot repair an already
unbounded phase.

### 3. Preflight does not record all serialized evidence bytes

Preflight computes a private `sample_output` sum from five in-memory payloads
and uses it in a projection (`search.cpp:1952-1959`). The emitted preflight
JSON does not contain `sample_output` or the component byte counts
(`search.cpp:1963-1975`). It records only the projected byte count.

The frozen contract explicitly requires preflight to record all serialized
evidence bytes as well as the conservative projection. The omitted measured
quantity cannot be reconstructed from the preflight evidence because the
sample payloads are never written. This makes the output projection
unauthenticated and fails the preflight evidence gate.

### 4. The registered direct-channel counters are not present

The preregistration says that every exact direct-screen result is retained in
counters and that each bank row contains all direct-channel counters. The
bank state and TSV contain counters for projective determinants, resultants,
and carries, but no counters for source, base-coefficient, transformed-
coefficient, base-discriminant, transformed-discriminant, or supplied-root
screens (`search.cpp:600-609,1390-1421`).

For those channels, `record_ticket` retains only the first proper factor
certificate. Unit results, full-gcd decoys, and later proper results are
discarded. Therefore the output cannot authenticate the declared eight-stage
screen population or the claim that every exact result was counted. Correct
source ordering does not cure missing frozen evidence.

### 5. Selection bytes still have no independent discovery-phase anchor

The held-out parser now correctly validates numeric syntax, reconstructs the
rank order, and requires the selected IDs to be its first four rows
(`search.cpp:1662-1719`). That repairs the D01 parser-semantic defect.

The runner, however, still obtains the expected selection digest from the
mutable sidecar in the same output directory after discovery
(`remote_run.sh:177-184`). A coupled replacement of the selection bytes and
sidecar before these lines is accepted. The attacker need only provide a
self-consistent fabricated rank packet; the parser never compares its metrics
with the discovery totals, and the runner does not anchor the digest printed
by the completed discovery process before reading mutable output. The
selection is internally consistent, but it is not authenticated as the
selection actually produced by discovery.

This is the same phase-authentication seam identified in the D01 audit. The
new semantic replay narrows it but does not close it.

### 6. The claimed unchanged ranking implementation drifted

D02 says that the ranking tuple is unchanged. D01 accumulates the ninth
ranking field from `bank.tested_rows`; D02 changes it to
`bank.residual_rows` (`search.cpp:1293`). Exact-square and rational-square-
class removal can make these totals different, so this can change the family
order and the held-out grammar.

The written tuple name, `total retained rows`, does not resolve which of the
two populations is frozen. Because the predecessor implementation and D02
implementation differ while D02 declares no ranking change, the packet does
not authenticate a no-drift claim. The intended population must be stated
unambiguously and then implemented in a new version.

## Narrow repairs that passed static inspection

Subject to the blockers above, these D02 repairs are present and internally
consistent:

- One level-`N^2` gauge triple is derived once per public family/base and
  stored in `BaseSource` before any matrix in that base is evaluated. Word
  syntax does not enter the lift seed. All same-base level-two rows therefore
  share `A0,B0,C0,delta0`.
- Canonical-discriminant, positive-row, row-bit, supplied-root, same-level,
  and cross-level divisibility assertions use fatal `require` calls. The D01
  bank-local exception conversion was removed; worker exceptions are
  rethrown and terminate the process.
- The eight direct screen stages occur in the registered global order:
  source, base, transformed, projective, resultants, carries, singletons, and
  equal/square-class pairs. The singleton loop completes before the pair
  template loop.
- Equal positive rows increment `equal_rows`, retain the
  `EQUAL_ROW_DECOY` label, do not increment `useful_square_multiples`, and do
  not set `strict_square_multiple`. Row-based normalized-root certificates
  serialize the exact root, supplied root, normalized root, both signed gcds,
  original candidate, factor, and complete row witnesses.
- Carry and quotient certificates retain the undivided numerator, exact
  divisor, quotient, and row witnesses. Resultant and other row-based direct
  tickets retain their integer candidate and row witnesses. P66 certificates
  retain every selected residual row and replay the exact product square.
- Only a strict multirow or 48-plus carry hit with an emitted certificate can
  contribute to its positive gate. The 64-per-family cap can cause only a
  false negative for these gates.
- Every eligible bank serializes a residual row map. Every final gcd-free
  block serializes its value, complete sparse exponent vector, exact-square
  flag, and either `EXACT_SQUARE_BLOCK` or the mandatory literal
  `UNKNOWN_OPAQUE_NOT_NEEDED`.
- `baseline_rows` is the number of distinct positive integer row values
  before exact-square and rational-square-class removal. Cell comparison mass
  is accumulated only for eligible banks. `gain_banks==0` correctly forbids a
  finite null after any proper held-out factor in any implemented channel.
- Selection parsing validates all rank fields, reconstructs the exact frozen
  rate comparisons, and enforces the first-four selection semantics. The
  remaining defect is the independent phase anchor described above.
- The source algebra, eight base families, five generators, word caps, two
  lift levels, direct ticket formulas, decoy formulas, cohorts, and P66
  arithmetic otherwise match D01. Hidden `p,q` are used only after
  `analyze_public(N,family)` returns, to label a public exact divisor.
- The runner places compilation, self-test, preflight, discovery, heldout,
  and individual hashing commands under remaining-time checks and global
  4-GiB/one-GiB limits. It counts output, preflight, and log directories in
  the aggregate uncompressed cap, closes final resource/run/uncompressed
  manifests before compression, and writes external archive manifests. These
  partial repairs do not cure the unbounded compressor or missing preflight
  measurement.

## Required disposition

Preserve F266-D02 and this audit as an immutable failed packet. Do not execute
it. Any successor must use a new version and new hashes. At minimum, it must:

1. implement one-family-across-all-cells null coverage and emit every cell;
2. place the complete compression pipeline under the remaining deadline and
   niceness;
3. record the measured preflight evidence-byte total and its components;
4. serialize the frozen direct-channel counters;
5. anchor selection bytes to the completed discovery phase independently of
   a mutable coupled sidecar; and
6. resolve the tested-row versus residual-row ranking population without an
   undeclared grammar change.

Only a fresh hostile audit of a new immutable packet can authorize target
validation or cohort execution.
