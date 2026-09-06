# F266-D04 prelaunch manifest

## Identity

- Experiment: `F266-D04`
- Family: canonical split-quadratic discriminant lifts under public
  `SL_2(Z)` words
- Status: `STATIC_FROZEN; FRESH_HOSTILE_AUDIT_PENDING`
- Search result: none
- Dynamic validation: forbidden before a fresh D04 hostile audit passes

## Immutable predecessors

F266-D01 remains unchanged. Its frozen-manifest SHA-256 is
`1ebfeff0b66cdec024a9612279675f435ad668059289865b581bf4d2b74a70e8`.
Its hostile FAIL audit SHA-256 is
`4880f3467e790519f39e278a78c0c808fd9b350afaafaf22c998823ec5cfc9c2`.

F266-D02 also remains unchanged. Its frozen-manifest SHA-256 is
`723314508048e2a2de692314764ad83ab78ffc84ce10d10cce27b39d759dde2e`.
Its hostile FAIL audit SHA-256 is
`ca1fe923ce674d369aa75c8ef7557515e4ec88fc7acff84357950762fa5f104b`.

F266-D03 also remains unchanged. Its frozen-manifest SHA-256 is
`07257b9e0820b1b1763984d382fcd49e6e6cf3d2d5db5666299813d4cb691984`.
Its hostile FAIL audit SHA-256 is
`a11cea775386f3d1178c46826c5db0b8042b49ad54bf056077ceaebd725bf73a`.

All three audits forbid their exact packets. None authorizes D04.

## Unchanged theory seam

For a public split quadratic

`Q=a(X-rY)(X-sY) (mod N^h)`,

the exact discriminant has the supplied unit root `a(r-s) mod N`. An
integral `SL_2(Z)` change of variables preserves that discriminant exactly.
Canonical coefficient reduction modulo `N` or `N^2` creates an exact public
carry. Its positive discriminant lift is at most `4N^(2h)` and remains a
modular square with the same supplied root.

D04 uses the same eight public base families, five generators, word and
matrix caps, two lift levels, direct screens, carry tickets, singleton and
square-multiple templates, canonical decoys, cohorts, rank tuple, and complete
factor-free P66 decoder as D01. It adds no algebraic family or candidate.

## Inherited D02 repairs

- One public `N^2` gauge triple is chosen once per base before matrix
  selection. Every matrix in that base shares the exact lifted source and
  base discriminant.
- Same-level differences require exact division by `N` or `N^2` as
  applicable. Cross-level differences require exact division by `N`. An
  invariant failure escapes the bank and aborts the process.
- The eight direct-screen stages execute globally in registered order.
- Equal rows keep `EQUAL_ROW_DECOY` and never increment the
  square-multiple-template score.
- Direct, carry, normalized-root, and P66 certificates retain original
  integer tickets and complete row witnesses. Positive gates use only strict
  hits whose certificate survives the 64-per-family cap.
- Every eligible bank writes a residual row map. Every final gcd-free block
  writes its value, sparse exponent vector, exact-square flag, and either
  `EXACT_SQUARE_BLOCK` or `UNKNOWN_OPAQUE_NOT_NEEDED`.
- The principal-digit baseline uses distinct positive integer row values and
  eligible banks only. Any held-out factor prevents a finite-null label.

## Inherited D03 repairs

- The null coverage gate is exactly `exists one selected family` whose every
  held-out size/shape cell has at least 24 eligible banks. All 48
  family/cell coverage rows and all 12 aggregate cell rows are emitted,
  including zero and ineligible counts. Observed singleton counts include
  banks that later become ineligible; baseline mass remains eligible-only.
- Each of the eight direct stages emits `tests`, `unit`, `full`, and `proper`
  counters. Both signed gcds from a normalized-root comparison are counted,
  and each four-way partition is checked exactly.
- Preflight records the measured corpus, bank, family, certificate, and
  opaque-block serialized bytes and their exact sum, in addition to its
  projections.
- Discovery emits the selection and corpus digests only after closing its
  output. The runner captures them directly into read-only shell variables,
  then verifies the exact output bytes and convenience sidecars. Heldout uses
  the captured selection digest; no sidecar is an authority.
- The registered D01 ranking population is restored: the final tie-breaker
  counts rows after coefficient-triple deduplication and before exact-square
  or rational-square-class removal. D04 preregisters this population
  explicitly.
- One remaining-time timeout owns the complete pipefail compression shell.
  `nice 15` applies to that shell and both `tar` and one-thread `zstd`.
- The deadline still begins before compilation. Compile, self-test,
  preflight, production, evidence hashing, and compression use bounded
  remaining time. Every executable phase uses the 4 GiB and one-GiB file
  limits. Aggregate evidence includes logs. Final resource and manifest
  evidence is closed before one-thread compression.

## D04 narrow repair closure

- Each convenience sidecar is parsed as one exact newline-terminated record.
  Its embedded digest must equal the read-only value captured from discovery
  stdout, and its filename must equal the fixed target basename. The runner
  rejects alternate digests, filenames, separators, extra lines, and extra
  bytes. It repeats the checks after discovery, after heldout, and immediately
  before the complete uncompressed manifest.
- A focused runner self-check accepts the canonical sidecar record and rejects
  wrong-digest, wrong-filename, and wrong-separator records.
- The one frozen direct chronology is identical in `ALGEBRA.md`,
  `PREREGISTRATION.md`, `DirectStage`, the TSV schema, and runner verification.
  Stage `source` contains attempted `a,r,s,r-s` and inverse seed `u`. Stage
  `base` contains `A0,B0,C0,Delta0,x` once per retained base/lift level.
- The mandatory source self-test checks the exact stage-name order, sends four
  unit candidates only to `source`, sends exactly five base-form quantities
  only to `base`, and requires all later stage counts to remain zero. The
  runner requires the exact 32 counter columns and every partition identity
  in both production bank files.

## Frozen files

| File | SHA-256 |
|---|---|
| `ALGEBRA.md` | `50ea42b05db7f1817e4cdde0847e4d0eee848ab6b5c6f2ef7d0bf8c368238157` |
| `PREREGISTRATION.md` | `ad937e55474ca8dd04e9c8d67f6406317082402d4f77149ad7e03c784c7dfce2` |
| `search.cpp` | `82e651211d2247d3a34ac39e561bdb908eacb70d1b8a547a25866181a5f54c9a` |
| `remote_run.sh` | `3441213ba996860f4bb87f599a9f0501795b8181314d09d3352d7b3ba74646b4` |

## Static checks completed

- The D04 directory was absent before creation. D01 through D03 bytes and all
  three audits were not edited.
- The source has fixed source, word, matrix, row, pair, decoder, certificate,
  cohort, worker, memory, wall, output, and compression caps.
- The only arithmetic analysis entry point accepts public `N` and a public
  family. Hidden factors label a returned exact divisor only after public
  analysis finishes.
- The shared-lift construction occurs before matrix selection. No word enters
  its seed.
- Canonical discriminant, positive-row, row-bit, projective-root, same-level,
  cross-level, exact-square, normalized-root, decoder reconstruction, and
  kernel assertions are fatal on failure.
- Discovery writes one rank packet and emits its digest into runner-captured
  shell memory. Heldout reads those exact bytes once, verifies their SHA-256,
  reconstructs their ranking, verifies the discovery-corpus SHA-256, and
  generates heldout inputs afterward.
- The runner requires each sidecar's exact digest, two-space separator,
  filename, newline count, and byte count to match its captured digest and
  fixed target. Its focused parser self-check rejects three malformed forms.
- The source implements one-family-across-all-cells coverage and explicit
  family/cell and aggregate-cell evidence. It restores `tested_rows` as the
  registered selection tie-breaker.
- Bank output contains the exact four-way counters for all eight direct
  stages. Preflight output contains every measured serialized-byte component
  and their sum.
- Both theory files use the same exact eight-stage text. The source self-test
  authenticates the source/base allocation. The runner authenticates the 32
  stage/outcome columns and every row partition in both bank files.
- Writers refuse overwrite and account all discovery and held-out evidence,
  including the block stream, under the in-process byte cap.
- The runner refuses existing evidence and same-range production processes,
  gates host capacity, records phase manifests, verifies program manifests,
  closes a complete uncompressed manifest, and compresses only afterward.

These are static source inspections. They are not compiler or runtime claims.

## Pending checks

No D04 source or runner command has executed. This agent did not compile,
self-test, preflight, access the remote host, generate a corpus, or open any
cohort.

Before any dynamic step, an independent hostile audit must authenticate the
new `FROZEN.sha256` root and inspect the exact D04 bytes. A passing audit must
contain these exact lines:

```text
# Verdict: PASS
frozen_manifest_sha256: <SHA-256 of FROZEN.sha256>
```

After that pass, the unchanged packet must:

1. authenticate every frozen file and the audit root line;
2. pass the host-capacity and process-overlap gates;
3. compile under the complete-packet deadline and resource limits;
4. pass the mandatory exact self-tests;
5. pass the fixed one-worker 1/16 preflight and its conservative eight-worker
   wall, RSS, output, and zero-resource-rejection gates;
6. run discovery and authenticated heldout sequentially; and
7. verify all phase manifests before final one-thread compression.

Any failure remains attached to these exact bytes. It must not be edited and
rerun silently.

## Interpretation

All future output is finite guidance. A positive certificate factors its
displayed modulus. A held-out null closes only the frozen grammar and corpus.
Neither result proves an all-input probability law or the top-level factoring
claim.
