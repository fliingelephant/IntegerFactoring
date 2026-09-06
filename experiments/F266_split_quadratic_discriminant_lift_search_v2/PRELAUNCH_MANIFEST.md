# F266-D02 prelaunch manifest

## Identity

- Experiment: `F266-D02`
- Family: canonical split-quadratic discriminant lifts under public
  `SL_2(Z)` words
- Status: `STATIC_FROZEN; FRESH_HOSTILE_AUDIT_PENDING`
- Search result: none
- Dynamic validation: forbidden before a fresh D02 hostile audit passes

## Immutable predecessor

F266-D01 remains unchanged. Its frozen-manifest SHA-256 is
`1ebfeff0b66cdec024a9612279675f435ad668059289865b581bf4d2b74a70e8`.
Its hostile FAIL audit SHA-256 is
`4880f3467e790519f39e278a78c0c808fd9b350afaafaf22c998823ec5cfc9c2`.
That audit forbids D01 execution and does not authorize D02.

## Unchanged theory seam

For a public split quadratic

`Q=a(X-rY)(X-sY) (mod N^h)`,

the exact discriminant has the supplied unit root `a(r-s) mod N`. An
integral `SL_2(Z)` change of variables preserves that discriminant exactly.
Canonical coefficient reduction modulo `N` or `N^2` creates an exact public
carry. Its positive discriminant lift is at most `4N^(2h)` and remains a
modular square with the same supplied root.

D02 uses the same eight public base families, five generators, word and
matrix caps, two lift levels, direct screens, carry tickets, singleton and
square-multiple templates, canonical decoys, cohorts, rank tuple, and complete
factor-free P66 decoder as D01. It adds no algebraic family or candidate.

## Narrow repair closure

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
- Heldout authenticates exact selection bytes, reconstructs the complete rank
  order from the authenticated metrics, and requires the selected IDs to be
  the first four ranks.
- The deadline begins before compilation. Compile, self-test, preflight,
  production, evidence hashing, and compression use bounded remaining time.
  Every executable phase uses the 4 GiB and one-GiB file limits. Aggregate
  evidence includes logs. Final resource and manifest evidence is closed
  before one-thread compression.

## Frozen files

| File | SHA-256 |
|---|---|
| `ALGEBRA.md` | `0b1d5c0f7dd8843c16834bd8f319ea267cb7431ab4a321bc1f4ab7dec0b7b0dd` |
| `PREREGISTRATION.md` | `8cdec3544e965e8cca433670bf365f5350a702b45916d9fd9580759743e88942` |
| `search.cpp` | `1b53b8026a5ff95592e24d267275bf590d89539bbaf2bcf6b944fb77bd655efd` |
| `remote_run.sh` | `7605b165feb8377dc2131509bd0cd7fe34546f2ce58fe09fc5a54501bc79a8c3` |

## Static checks completed

- The D02 directory was absent before creation. D01 bytes were not edited.
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
- Discovery writes one authenticated rank packet. Heldout reads those bytes
  once, verifies their SHA-256, reconstructs their ranking, verifies the
  discovery-corpus SHA-256, and generates heldout inputs afterward.
- Writers refuse overwrite and account all discovery and held-out evidence,
  including the block stream, under the in-process byte cap.
- The runner refuses existing evidence and same-range production processes,
  gates host capacity, records phase manifests, verifies program manifests,
  closes a complete uncompressed manifest, and compresses only afterward.

These are static source inspections. They are not compiler or runtime claims.

## Pending checks

No D02 source or runner command has executed. This agent did not compile,
self-test, preflight, access the remote host, generate a corpus, or open any
cohort.

Before any dynamic step, an independent hostile audit must authenticate the
new `FROZEN.sha256` root and inspect the exact D02 bytes. A passing audit must
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
