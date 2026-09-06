# Verdict: FAIL
frozen_manifest_sha256: 07257b9e0820b1b1763984d382fcd49e6e6cf3d2d5db5666299813d4cb691984

# F266-D03 hostile pre-run audit

**DO NOT COMPILE, SELF-TEST, PREFLIGHT, OR LAUNCH THIS FROZEN PACKET.**

This was a fresh static hostile audit. I did not compile or execute
`search.cpp`, invoke `remote_run.sh`, access the remote host, generate or open
a corpus, or inspect a discovery or held-out cohort.

## Frozen-artifact authentication

The SHA-256 of `FROZEN.sha256` is the authenticated manifest root shown above.
All five manifest entries match the local D03 bytes:

```text
PASS  ALGEBRA.md             7f2608c91fd102941b5e282390b7e4aeb0f0049eafab4d28b957de42fc888515
PASS  PREREGISTRATION.md     81cc58f1018a7d466a19d8909f44eab6722e0c66ab922a96ab18767b45264ffe
PASS  search.cpp             7ce9f0af137990df48550980ea97f0c41dff409e0aafc3c3ebeb7ad9df25a1eb
PASS  remote_run.sh          72518275d0ca283e09788359ad5e6b5941b2016b1c60ceeff23c521de6979bd7
PASS  PRELAUNCH_MANIFEST.md  839e72da463cf19a678045a4f7b237100f61ad12b2bf0ea6b5d28a86c4ef8335
```

The immutable predecessor provenance also authenticates:

```text
PASS  F266-D01/FROZEN.sha256             1ebfeff0b66cdec024a9612279675f435ad668059289865b581bf4d2b74a70e8
PASS  F266-D01/HOSTILE_PRERUN_AUDIT.md   4880f3467e790519f39e278a78c0c808fd9b350afaafaf22c998823ec5cfc9c2
PASS  F266-D02/FROZEN.sha256             723314508048e2a2de692314764ad83ab78ffc84ce10d10cce27b39d759dde2e
PASS  F266-D02/HOSTILE_PRERUN_AUDIT.md   ca1fe923ce674d369aa75c8ef7557515e4ec88fc7acff84357950762fa5f104b
```

Every entry in both predecessor manifests also matches its local file. Both
predecessor audits begin with `# Verdict: FAIL`. D01 and D02 remain immutable
failed packets.

## Decisive blocker

### The convenience sidecars are not bound to the captured discovery digests

The discovery process correctly closes its files and then emits the corpus
and selection digests (`search.cpp:1943-1956`). The runner captures those
tokens from process stdout and makes the shell variables read-only before it
reads either sidecar (`remote_run.sh:168-183`). It also directly hashes the
fixed selection and corpus files and compares those hashes with the captured
values (`remote_run.sh:194-199`). Those parts repair the central D02 selection
anchor defect, and heldout receives the captured values rather than sidecar
values (`remote_run.sh:206-214`).

The runner does not, however, require either sidecar's digest and filename
fields to equal the captured digest and its fixed output filename. Lines
188-192 only run `sha256sum -c` on whatever record each mutable sidecar
contains. A changed sidecar can therefore authenticate a different existing
file. The independently anchored fixed-file checks on lines 194-199 do not
link that sidecar record back to the captured value.

The discovery program manifest does not close the seam. Its digest is not
emitted or otherwise anchored by the completed discovery process. The runner
only checks the manifest against current directory bytes (`remote_run.sh:63-80,
193`) and then hashes that current manifest into later evidence
(`remote_run.sh:200-203`). Thus a coupled post-discovery replacement of the
sidecars and the program manifest is accepted.

For example, without changing either anchored data file, replace the corpus
sidecar with a valid record for the selection file, replace the selection
sidecar with a valid record for the corpus file, and update the two sidecar
hash rows in `F266-D03.discovery.manifest.tsv`. Both `sha256sum -c` commands,
the program-manifest verification, both direct fixed-file hash comparisons,
heldout, and all later manifests pass. The archived convenience sidecars no
longer state the discovery values captured in read-only shell memory.

This directly contradicts the frozen requirement that both convenience
sidecars match the captured discovery values (`PREREGISTRATION.md:210-218`).
It also falsifies the prelaunch claim that the sidecars are verified against
the immutable discovery-process output. The sidecars are not an authority for
heldout, which protects cohort selection, but incomplete authentication is
still a frozen evidence-gate failure.

## Additional frozen-document contradiction

The new per-stage counters do not have one consistent frozen stage assignment.
`ALGEBRA.md:270-277` puts the supplied discriminant-root gcd in stage 1 and
puts base coefficients and the base discriminant in stage 2.
`PREREGISTRATION.md:112-119` instead puts the supplied-root gcd in stage 2 and
does not list the base-coefficient gcds there. The executable counts source
`a,r,s,r-s` tests in `DIRECT_SOURCE` (`search.cpp:679-739`) and counts
`A0,B0,C0,delta0,root` in `DIRECT_BASE` once per base and lift level
(`search.cpp:1021-1030`).

The implementation's four-way partitions are internally exact, but a
reported source-stage or base-stage count cannot satisfy both frozen stage
definitions. This ambiguity was less visible before D03 added stage-specific
evidence. D03 must state one exact assignment and implement it consistently.

## D02 repairs that passed static inspection

Subject to the blockers above, the six requested D03 repairs are otherwise
present:

- `find_coverage_family` implements `exists family: for every cell`, not the
  reversed quantifiers. The lead output loops over four selected families,
  four sizes, and three shapes, so it emits all 48 coverage rows. A separate
  fixed four-by-three loop emits all 12 aggregate rows. Intended, eligible,
  and ineligible counts are explicit even at zero. Singleton observations are
  accumulated before eligibility filtering, while only eligible banks add
  `2*k/N` baseline mass (`search.cpp:1792-1883`).
- The complete `tar | zstd` pipeline is inside one pipefail-enabled shell
  owned by the remaining-time `timeout`. Niceness and the 4-GiB and one-GiB
  limits are inherited by both children, and `zstd` is fixed at `-T1 -3`
  (`remote_run.sh:271-281`).
- Preflight materializes the corpus, bank, family, certificate, and opaque
  payloads, records each measured byte count, and records their exact sum.
  Its wall, RSS, output, and zero-resource-rejection gates remain present
  (`search.cpp:2009-2068`).
- Each bank serializes `tests`, `unit`, `full`, and `proper` for an eight-entry
  direct-stage array and requires each partition identity before output.
  Rejected source candidates flow through the source counter. Singleton and
  equal/square-class comparisons send both signed candidates through the
  applicable counter (`search.cpp:580-685,1021-1188,1432-1474`). The remaining
  defect is the frozen stage-assignment contradiction above.
- The discovery-process stdout capture, read-only digest variables, direct
  fixed-file hashes, heldout arguments, one-read selection parser, rank replay,
  and corpus-before-heldout firewall are implemented. Only the sidecar binding
  remains defective.
- Discovery ranking again accumulates `bank.tested_rows`, which is set after
  coefficient-triple deduplication and before exact-square or rational-square-
  class removal (`search.cpp:1233-1247,1317-1336`). The preregistration now
  states this D01 population explicitly.

## Broader static checks that passed

- The shared level-`N^2` gauge triple is selected once per public family/base
  before matrix evaluation. No word enters its seed. Same-base, same-level
  rows therefore share the exact source discriminant.
- The split discriminant congruence, integral `SL_2(Z)` invariance, canonical
  carry identity, positive-row bound, projective-root identity, resultant
  formula, same-level division, and cross-level division are algebraically
  sound. Their exact assertions escape worker analysis and abort the process.
- The eight bank-local direct stages execute in frozen order. Equal rows keep
  `EQUAL_ROW_DECOY`. Exact squares and rational square classes are screened
  before residual removal.
- Direct, carry, singleton, square-class, and P66 certificates retain the
  original integer ticket and the row witnesses needed by their replay
  assertions. Only retained strict certificates contribute to positive
  multirow and carry gates.
- The gcd-free refinement is bounded and factor-free. It reconstructs every
  row, checks final pairwise coprimality and kernel parity, writes residual row
  maps, and writes every final block with its sparse exponent vector, square
  flag, and required status.
- The only arithmetic analysis entry point accepts public `N` and a public
  family. Hidden `p,q` are used after it returns only to label a public exact
  divisor. They do not affect source generation, family ranking, selection,
  eligibility, or lead gates.
- Prime, safe-prime, neighbor, pair-retry, source-attempt, word, matrix, row,
  pair, decoder, certificate, worker, memory, output, and wall loops have
  finite caps. Corpus construction enforces exact bit sizes, primality,
  balance, and modulus distinctness across discovery and heldout.
- Writers refuse overwrite and close before digest emission. The runner gates
  host capacity and overlap, limits each executable phase, includes logs in
  the aggregate uncompressed cap, closes final resource and uncompressed
  manifests before compression, and writes external archive evidence.

## Required disposition

Preserve F266-D03 and this audit as an immutable failed packet. Do not execute
it. A successor must use a new version and new hashes. At minimum, it must
parse each convenience sidecar and require its digest and filename fields to
equal the captured discovery digest and fixed target, independently of the
mutable program manifest. It must also reconcile the frozen source/base direct
stage definitions with the counter assignment.

Only a fresh hostile audit of that new immutable packet can authorize dynamic
validation or cohort execution.
