# F261-D02 V2 frozen prelaunch manifest and provenance

Frozen on 2026-08-13 before the first V2 compile, self-test, benchmark,
cohort generation, or scan.

## Status

This is an immutable repair candidate. It is not promoted. It has only a
static consistency review. F258 was active at freeze time, so the declared
incompatibility gate prohibited all dynamic validation.

## Frozen V2 artifact hashes

```text
e9894455ae9cfed71a984591c88cc3b45d23a885f3c60216ca0bfdc267792e8d  V2_ALGEBRA.md
0b65705c4135b0e653c5cef0221d7725f1ea354468b897160a75409f916dd68b  V2_PREREGISTRATION.md
ad3827f82e1b350c5887ba2094f5be8d360a2e858090c6a9dd25558b81e1d095  V2_search.cpp
310a4377270408848c2035b88df5bf7166cd5eb1d9f8102bce8ca5df74bf74ae  V2_remote_run.sh
```

These four files are frozen at these bytes. Any repair must use new file
names or a new declared hash set before execution. This manifest cannot
contain its own hash. Its SHA-256 is reported with the handoff.

## V1 immutable provenance

V2 leaves every V1 frozen artifact unchanged:

```text
df27b6557ac2fe2ae29a495241c66741e864f8d667237f04855aa82f499aa67f  ALGEBRA.md
ae0e04eb7b1593795560eae3444c753ed07c4e4c0758c41386562fb72779c7f1  PREREGISTRATION.md
9af35178e041b3d02f4bf33134b451b9fe938cf8235ae450fb8df7f0027b1e6d  search.cpp
07fd9d53c1e2f08b647b24272908f1487ed1ba38657e7aef1a196d4f389137f3  remote_run.sh
110aee72fd78731f354643ccbc9517784e3ee28a8ea5c454069d9e959a6f70e8  PRELAUNCH_MANIFEST.md
```

The existing V1 verification artifacts also remain unchanged:

```text
a2b628035202ae57e9ee2169bc70e4ba329a8057c9cb176a8757ba0c6a2b9558  HOSTILE_AUDIT_THEOREM.md
f05fb46595c6b5ec5b277fba5e0ac938a63a5d1a42fc2d2606b70cf8f91a1a71  FRESH_HOSTILE_AUDIT.md
0ea8459bd471791d11888e4a14b6fadd1c50ed4305b501c660bbb1a80f5f6e22  BLIND_RECONSTRUCTION_THEOREM.md
```

`FRESH_HOSTILE_AUDIT.md` records the V1 packet verdict **FAIL**. V2
preserves that verdict and its exact hash. V2 does not rewrite V1 history.

## Repair provenance

V2 addresses the fresh hostile findings as follows.

1. The no-prefix schedule now defines `R=1` and `a=b=0`. The source returns
   before any inverse call. The self-test observes the branch choice.
2. Predictor selection now uses the lower middle order statistic of raw
   `min |c|`. The preregistration proves that this is exactly order-equivalent
   to the lower median after the strictly increasing `log2(1+x)` transform.
   The self-test includes an even-list witness that distinguishes this rule
   from the V1 arithmetic mean of the two middle raw values.
3. `product_surrogate` now uses
   `floor((u*floor(sqrt(N))+B/2)/B)` in both prose and code. The self-test
   includes `N=11009,B=128,u=19,K0=15`.
4. Preflight receives the actual launch worker count. It divides the
   single-worker scan projection by `0.75*workers`, adds the serial generator
   projection, and rejects totals above 14,400 seconds.
5. Every true-carry cap field is named `oracle_hit_*`. The summary states
   `executes_factor_bank=false`. V2 reports theorem-only bank cost bounds. It
   does not enumerate direct `T`, run a decoder on cohort rows, or claim an
   executed factor-bank hit.

The deterministic edge stream is also described as a modulo-mapped
pseudorandom stream, not as an exactly uniform sampler. The zero-carry
valuation sentinel and raw-rank output convention are now explicit.

## Completed static checks

- Recomputed all five V1 frozen hashes and all three existing verification
  artifact hashes.
- Compared each V2 file with its V1 source and inspected every changed hunk.
- Checked theorem, preregistration, source identifiers, output names, prefix
  formulas, predictor score, product surrogate, and worker flow for literal
  consistency.
- Parsed `V2_remote_run.sh` with `bash -n`.
- Passed `git diff --check` on all four pre-manifest V2 artifacts.
- Confirmed that the runner checks F258, F259, and F260 before compilation.
- Confirmed that the runner passes the same final worker count to preflight
  and the full run.

No C++ compilation or execution occurred. No self-test, benchmark,
generator, cohort, inverse-map study, or output write occurred.

## Mandatory unexecuted target gates

After F258, F259, and F260 are all absent, a target operator must perform
these steps in order:

1. Recompute the four frozen V2 hashes above. Abort on any mismatch.
2. Inspect target load, available RAM, free disk, and incompatible processes.
3. Run `V2_remote_run.sh` from the experiment directory. The runner must
   again confirm that F258, F259, and F260 are absent before compilation.
4. Compile `V2_search.cpp` as C++17 with Boost Multiprecision and the frozen
   warning flags.
5. Pass the exact V2 self-test, including all repair regressions.
6. Pass the public 20,000,000-iteration inner-loop benchmark with the actual
   worker count supplied to the projection.
7. Observe at least one hit in every separately tagged 60-bit generator
   benchmark, including safe-safe.
8. Require the conservative total projection to be at most 14,400 seconds.
9. Only then generate the 1,368 cohorts and start F261-D02.
10. Enforce the four-hour timeout, 4 GiB virtual-memory cap, at most eight
    workers, at least 5 GiB free disk, and the 1 GiB output cap.

Any failed gate aborts V2. It does not authorize a source change, replacement
cohort, relaxed threshold, or alternate workflow under this hash set.

## Frozen scale and interpretation boundary

The cohort scan still has 1,368 rows and at most 711,622,656 exact
centered-carry evaluations. The preflight still has 20,000,000 public
synthetic carry evaluations and 29,000,000 separately tagged generator
attempts. The factor-three inner-loop multiplier covers predictor and exact
candidate-bound overhead before the worker-efficiency adjustment.

The run keeps aggregate rows and selected witnesses. It does not keep dense
traces. Projected RSS remains below 512 MiB at eight workers. Projected output
remains below 25 MiB. These are forecasts, not validated measurements.

Finite oracle hits, predictor improvements, modular-rank anomalies, and
inverse-map samples are diagnostic evidence only. They do not prove an
inverse-QP law, execute the theorem bank, or imply an all-input factoring
algorithm.
