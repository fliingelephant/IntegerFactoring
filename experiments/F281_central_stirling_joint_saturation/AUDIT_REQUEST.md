# F281-D01 fresh hostile pre-run audit request

Audit the exact frozen F281-D01 bytes from first principles. This is a static
hostile audit before any compilation or execution.

## Authentication boundary

Use `FROZEN.sha256` as the complete frozen boundary. Check every record. Then
compute and report the lowercase SHA-256 of the exact `FROZEN.sha256` bytes.

The later audit files are not frozen inputs. Write only:

```text
HOSTILE_PRERUN_AUDIT.md
HOSTILE_PRERUN_AUDIT.sha256
```

Do not edit a frozen byte. Do not compile or preprocess `search.cpp`. Do not
invoke, parse-run, or syntax-run `remote_run.sh`. Do not execute a self-test,
pilot, replay, local search, or remote command. Do not connect to
`seetacloud`. Do not edit a proof, failure, registry, or progress ledger.

## Mandatory algebra audit

Reconstruct all of these points independently.

1. Verify `S(n,k)=h_(n-k)(1,...,k)`.
2. Verify that the central pair is equivalent to
   `h_(s+1)(1,...,s)=h_(s+2)(1,...,s)=0`.
3. For `p=2s+1+2h`, verify the complement and every sign and index in
   `c(s+2h+1,2h),c(s+2h+1,2h-1)`.
4. Check both coefficient-degree conventions with and without the leading
   factor `x`.
5. Verify the finite-difference endpoint and reflection identities.
6. Confirm that no fixed-divisor or Eulerian-gamma observation is presented
   as a proof.
7. Confirm the negative control `s=3,p=43,h=18`, including residues
   `A=0`, `B=20`, `h_34=13`, and `h_35=36` modulo 43.
8. Confirm that the valid norm identity does not imply the discarded target.
9. Independently check the `s=73` fixed-divisor telemetry statement
   `G/Delta=1679` and that `1679` does not divide `146`.

Any off-by-one, sign error, false equivalence, or unproved bridge is a FAIL.

## Mandatory source audit

Audit `search.cpp` line by line for these boundaries.

1. Lane A uses the exact second-kind recurrence, covers every registered
   `s`, and does not lose a lower column when truncating the row.
2. Every prime at most `2s+1` is removed to exhaustion. The residual witness
   checks divisibility and gcd one against the exact support lcm.
3. The exact witness replay uses the original second-kind
   inclusion-exclusion formula modulo the composite residual. Check why both
   factorials are invertible.
4. Lane B shares one exact low-degree first-kind recurrence across the whole
   deterministic rectangle. It tests the two literal `c(n,k)` indices from
   the algebra.
5. Each distinct machine-word prime candidate receives deterministic FLINT
   primality. There is no probable-prime or GMP-only fallback.
6. A Lane B witness is independently replayed with original second-kind
   inclusion-exclusion, not accepted from the complement recurrence alone.
7. Each lane stops after its first exact witness. Every output loop and exact
   decimal reservation is bounded.
8. Fixed-divisor telemetry exists only where the stored row is complete. It
   cannot change status or stop a run. Its stronger divisibility boolean is
   required to fail at `s=73`.
9. Reconstruct all mandatory self-tests, including both individual F277
   saturations, the noncentral adjacent positive control, reflection, the
   false-reduction negative test, and the synthetic residual detector.
10. Verify every registered pilot and production rung in source against
    `PREREGISTRATION.md`.
11. Verify one-process production, one or two internal `std::thread` lanes,
    the hard eight-worker rejection, deterministic serialization, and the
    absence of `fork`, `exec`, `system`, shell, subprocess, or random paths in
    the scientific source.
12. Check GMP aliasing, unsigned loop termination, field counts, exact parsing,
    modular addition and subtraction, factorial handling, exception flow, and
    thread-safe disjoint output ownership.

Any route that can miss a registered pair, accept a false witness, turn a
resource rejection into a null, or make thread scheduling change the tested
cohort is a FAIL.

## Mandatory runner and resource audit

Audit `remote_run.sh` without executing it.

1. It authenticates the frozen packet and a fresh audit before target
   creation. It refuses an existing or broad target.
2. FLINT and GMP pkg-config gates are exact. Compilation has no substitute
   source, dependency, language, or host path.
3. The outer timeout, inner monotonic accounting, replay reserve, and direct
   scientific-PID watchdog keep the full packet inside four hours. Check
   `TERM`, `KILL`, `wait`, signal traps, and partial-manifest semantics.
4. The scientific process receives soft and hard `RLIMIT_AS=4 GiB`, core zero,
   bounded file size, descriptor count, and process count. The source reads
   them back. The runner launches no pipeline or `timeout` process between
   itself and the scientific PID.
5. Confirm that one PID with internal threads makes RLIMIT_AS an aggregate
   address-space limit. Confirm that the packet does not call it an RSS or
   swap-accounting guarantee.
6. Check optional cgroup-v2 detection. An absent, unbounded, or larger-than-4
   GiB cgroup must be recorded as RLIMIT-primary, not falsely reported as
   cgroup containment.
7. CPU, available memory, disk, load, active related processes, exact output
   bytes, and resource snapshots are checked before every expensive phase.
8. All six one-worker pilots use the same binary and production kernels.
   Recompute the work proxies, 2.5 multiplier, target-rung choice, one- versus
   two-worker rule, memory aggregation, output bound, and deadline gates.
9. No target outside the six frozen rungs can reach production. Rung 0 failure
   stops production.
10. A preflight witness is replayed and closes as a counterexample. A
    production witness is replayed before exact-counterexample status.
11. Staging-to-final moves, fixed output sets, header/status checks, witness
    line counts, RSS projection readback, 512 MiB live cap, and SHA-256 final
    manifest all fail closed.
12. Confirm that no prior `s<=3000` evidence is mislabeled as F281 output and
    no finite null is called a proof.

Any silent fallback, per-process-tree memory approximation, unbounded
scientific child, partial PASS, projection bypass, overwrite, stale audit, or
evidence/proof overclaim is a FAIL.

## Verdict format

If and only if no blocker remains, include these exact standalone lines:

```text
Verdict: **PASS — CLEARED FOR LAUNCH**
FROZEN_SHA256=<lowercase SHA-256 of the exact FROZEN.sha256 bytes>
```

The sidecar must contain one standard `sha256sum` record for
`HOSTILE_PRERUN_AUDIT.md`. A failure must use an explicit FAIL verdict and
must not contain the PASS line. Because target validation is pending, the
audit must not claim compile, self-test, runtime, memory, benchmark, witness,
or cohort evidence.
