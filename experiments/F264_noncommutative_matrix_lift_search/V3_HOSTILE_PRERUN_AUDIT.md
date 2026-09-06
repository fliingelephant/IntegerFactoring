# F264-D03 V3 fresh hostile pre-run audit

Verdict: **PASS — TARGET VALIDATION ONLY AFTER THE INCOMPATIBILITY AND RESOURCE GATES PASS**

Audit method: fresh static inspection only. I did not compile or execute
`V3_symbolic_search.cpp` or `V3_remote_run.sh`. I did not generate or open a
cohort, inspect prior cohort output, or use the remote host.

## Authentication

I authenticated every entry in `V3_FROZEN.sha256` before inspecting its
contents. I also authenticated every preserved V1 and V2 frozen entry, both
prelaunch manifests, and both hostile FAIL audits. All digests match.

```text
PASS  V3_FROZEN.sha256             1216d1d586295d0e38ae8a91fbe507a74fcd36742720649cebe0400566d81dd7
PASS  V3_ALGEBRA.md                a102c9623b113cd28563a1d4552ed6fd8f05e32c56aa61f972d85a1f79cbdb14
PASS  V3_PREREGISTRATION.md        20b31fe7ddc8b3146cec16b67cceb5ebb66ac540fd3bb7ebfdda3d3f8f552370
PASS  V3_symbolic_search.cpp       b76812ba8966eabceee4a42340910701aab89ca163e5d2a00b74494ad4df9de3
PASS  V3_remote_run.sh             b10db23daa7d2401a3fb006f232a9c1239b2e4acd9cc467608a82320579320b5
PASS  V3_VALIDATION_PENDING.md     cb1bffb63aed35975a32a0baa27b7bc5283aaa10395cbb3c81ee987a5947c7a7
PASS  V3_AUDIT_REQUEST.md          0ea0401d4e42b7ba0d96a6042c4eb8e6405f02ff5846a02df6b1926ecfe8c6f9
PASS  V3_STATIC_VALIDATION.md      1cadb086cca3d73ec72b1f9b85dc2016b70e89cafde12b228c6821f3bda611ba
PASS  V3_PRELAUNCH_MANIFEST.md     74ae2168d9b18288e42b1fa9db12bdafb450d08b409c43df013ce5c9b99d2b99

PASS  FROZEN.sha256                23d7aa6bd72f9cb7cf66b63ea9680fbd3adabcd4b543150929b249d8b0a2bb22
PASS  PRELAUNCH_MANIFEST.md        507ecd4c5c56d44867b0f34ca9262b7df5bb4d6450cd8121791d4912cb39e522
PASS  HOSTILE_PRERUN_AUDIT.md      f00fee9eac5fb71c9403d0f3a39b8cbf0bb0eb5682d6776f5eca1d26e21e3c9c
PASS  V2_FROZEN.sha256             52cb03a726c0ba26c79ad215971b6f72ec72199c50dac22f062f8016356255e0
PASS  V2_PRELAUNCH_MANIFEST.md     e1a2442589ec276d4c6c6c5fd4afd8c4c4522f6bd9f4165eea79b9555c673044
PASS  V2_HOSTILE_PRERUN_AUDIT.md   4206516a9ee14b831db4f3d9c148052f990faf209ffacf2673518f8de9eaf51a
```

## Hostile findings

1. **PASS — the repair is narrow.** The complete V2-to-V3 source diff changes
   only packet identifiers, exhaustive root-proposal accounting, the added
   report fields, and moving that accounting before every order-path return.
   The public seeds, generators, reduced words, sparse scopes, 30 families,
   candidate DAG, cohorts, P205 programs, schedules, thresholds, and held-out
   rules are unchanged. The algebra diff changes only packet identifiers and
   explicitly preserves every V2 formula.

2. **PASS — the order scope has one consistent meaning.** The source selects
   eight main words and one cyclic control in each of two profiles. Both
   schedules run on all 18 matrices. This gives `2*(8+1)*2=36` trials per
   input. The preregistration, source self-test, benchmark description, row
   validator, manifest, and validation gate all use 36. No V3 text retains
   the rejected per-profile `16 main + 2 controls` interpretation.

3. **PASS — all root proposals are evaluated before any order return.**
   `check_split_certificate` constructs the exact ordered seven original-basis
   and seven conjugate-basis proposals, requires length 14, and has no return
   inside its 14-iteration loop. `order_trial` calls it first. Only after the
   complete loop can a retained proper gcd, an initial-return gcd, a failed
   initial return, an order-strip gcd, or a missing split certificate return.
   A unit root never short-circuits later proposals.

4. **PASS — root coverage is reconstructible.** Every trial increments the
   total and the indexed check counter. Every row therefore exposes 504 total
   checks and 36 checks at each of 14 indices. It also exposes square, unit,
   and proper-gcd match totals. The ordered transcript recurrence includes the
   proposal index, proposal residue, square residual, gcd/outcome class, and
   the trial index. The self-test freezes 36 trials, 504 checks, and a
   `36x14` index profile. The report validator independently requires the same
   row and aggregate invariants.

5. **PASS — certificate semantics and precedence remain exact.** A proposal
   becomes a split certificate only after its exact square residual vanishes
   modulo `N` and its gcd with `N` is one. A proper gcd remains an exact factor
   and has precedence even if another proposal supplied a unit root. A
   nonsquare proposal cannot certify splitting. The subsequent smooth-order
   stripping code is byte-for-byte the V2 logic: global return permits prime
   deletion, a proper gcd factors `N`, and gcd one retains the prime. The
   no-factor result is the exact common local order, so a valid split root
   still proves divisibility by every hidden `r-1`.

6. **PASS — TSV and anomaly validation are exact.** The validator reconstructs
   the ordered 2,560-column header from 31 fixed fields, 14 root-index fields,
   20 basis fields, 10 named decoys, 150 family fields, and 2,335 P205 fields.
   It compares the full header and every row width. It also checks the exact
   anomaly header and row shape, split labels, cell sizes and indices,
   primality, balance, safe-prime and consecutive-prime conditions, global
   pair uniqueness, two noncommutative profiles, 36/504 root counts, and all
   14 indexed counts.

7. **PASS — JSON validation uses closed schemas.** The validator compares the
   exact top-level key set and every nested object key set. It checks the ten
   ordered decoy names and positive counts, all 30 ordered family names, exact
   cohort/family/P205 cell order and sizes, the exact candidate count emitted
   by the frozen description, consecutive candidate IDs, and aggregate root
   totals and index counts against the rows.

8. **PASS — every named stage uses one resource envelope.** Authentication,
   compile, self-test, self-test parsing, benchmark and parsing, description
   and parsing, both production splits and validators, compression, manifest
   construction, and the final gate all call `run_monitored`. Each call checks
   the incompatibility and resource gates, inherited remaining four-hour
   deadline, 4 GiB virtual-memory cap, `nice 15`, pre/post owned-byte cap, and
   a two-second overlap/output monitor. The source admits at most eight
   threads and the runner requests eight. Static shell parsing also passes.

9. **PASS — manifest and final-size ordering is closed.** Manifest construction
   is monitored and completes before the final gate starts. The final gate
   requires both summaries and all four compressed TSVs, requires removal of
   their uncompressed forms, and includes its already-created stdout/stderr in
   its own size calculation. `run_monitored` repeats the owned-byte and
   deadline checks after that child exits, so the final gate's completed logs
   are covered. The runner creates no owned file after this return.

10. **PASS — no hidden label controls discovery.** Public profiles, words,
    scopes, root proposals, schedules, families, and candidate evaluations
    depend only on `N` and frozen constants. `process_public` completes before
    `p,q` enter P205 scoring. Discovery output does not alter the held-out
    candidate set or any literal lead predicate. Factor labels only stratify
    or score already-frozen public results.

## Authorization boundary

No static blocker remains. This PASS authorizes only the frozen target
validation workflow. It does not authenticate Boost behavior, runtime,
memory, output size, cohort construction, or numerical results. Do not start
that workflow until every incompatible F258--F263 process is absent and the
live target resource gates pass. Any dynamic failure invalidates these bytes;
it does not authorize an edit or relaxed gate. No durable ledger was edited.
