# F281-D01 preregistration — exact central Stirling search

## 1. Status and decision boundary

F281-D01 is a theory-first, exact search packet. Its frozen question is the
prime-support conjecture in `ALGEBRA.md`.

The packet has no proof and no counterexample at freeze time. Existing local
exact checks through `s=3000` are prior context. They are not output from this
packet. The general adjacent-row analogue is false at
`S(12,3),S(12,2) (mod 23)` and is only a self-test. Centrality is essential.

Every finite PASS is evidence. It does not prove an unbounded statement. A
valid residual witness is an exact disproof even if the residual is not
factored.

## 2. Frozen software and arithmetic

The source is C++17. It requires:

- GMP and GMP C++ for exact integers;
- FLINT `n_is_prime` for deterministic machine-word primality; and
- a 64-bit `unsigned long` target.

There is no alternate Python, Sage, Boost, probabilistic-primality, or
floating arithmetic path. Missing dependencies stop before compilation.

All conjecture tests are exact. Floating arithmetic is used only by the
runner for conservative resource projections. It never selects or validates
a mathematical witness.

## 3. Mandatory self-tests

The frozen binary must pass all of these tests before any pilot:

1. exact small second-kind and first-kind rows;
2. `S(n,k)=h_(n-k)(1,...,k)` on a bounded grid;
3. `h_(s+2)(1,...,s)=B_s+sA_s`;
4. the complement equivalence in equation (3) for small primes;
5. the norm identity (5) below degree `p-1`;
6. the reflection identity (7) and both endpoint identities (6);
7. `s=3,p=43,h=18` as the mandatory negative test for the discarded
   `h_(2h-2),h_(2h-1)` reparameterization;
8. the individual F277 saturations
   `37 | S(9,4)` and `19 | S(10,4)`, while neither registered pair is a
   central joint zero;
9. the noncentral adjacent positive control
   `23 | S(12,3),S(12,2)`;
10. the fixed-divisor diagnostic at `s=73`, where `G/Delta=1679` and the
    ratio does not divide `146`; and
11. a synthetic small-support stripper with residual `13^2` above bound 11.

Any failed identity aborts. A known individual zero is not counted as a joint
zero.

## 4. Lane A — exact all-s recurrence

For every `1 <= s <= S_A`, the source computes

```text
A = S(2s+1,s)
B = S(2s+1,s-1)
g = gcd(A,B)
```

It sieves every rational prime at most `2S_A+1`. For each row, it applies
`mpz_remove` for every prime at most `2s+1`. Removal is to exhaustion.

If the residual is one, the row passes. If the residual `R` is above one,
the source verifies and serializes:

```text
R divides A and B;
gcd(R,lcm(1,...,2s+1)) = 1;
the exact decimal A, B, g, R, and support lcm;
the original second-kind inclusion-exclusion residues modulo R.
```

The lane then stops. It does not try to factor `R`.

The row is stored only through `k=S_A`. This is sufficient because later
Stirling columns never flow into a lower column. For `2s+1 <= S_A` and
`s<=512`, the row is still complete. Those rows also emit non-gating
telemetry for

```text
G = gcd((s-1)! B, s! A)
Delta = gcd(k! S(2s+1,k) : s-1 <= k <= 2s+1)
G/Delta
whether G/Delta divides 2s
the residual after stripping prime support <=2s+1 from G/Delta.
```

The `G/Delta | 2s` column is a refuted diagnostic. It must be false at
`s=73`. No telemetry column can stop a run or change its status.

## 5. Lane B — deterministic near-offset rectangle

The registered rectangle is

```text
1 <= s <= S_B
1 <= h <= H
p = 2s+2h+1 prime.
```

The source computes the exact unsigned first-kind row through degree `2H`.
At `n=s+2h+1`, it tests

```text
c(n,2h) mod p
c(n,2h-1) mod p.
```

Primality for each distinct `p` is cached after one FLINT call. The exact
coefficient recurrence is shared across the whole rectangle. It is not
restarted for each pair.

The deterministic scan order is increasing `n=s+2h+1`, then increasing `h`
within one row. The associated `s` is reconstructed exactly. This order
selects the first serialized witness and does not omit any pair in the
rectangle.

A joint zero serializes `s,h,p,n` and the two exact decimal first-kind
coefficients. It then independently evaluates

```text
S(2s+1,s) mod p
S(2s+1,s-1) mod p
```

by the original inclusion-exclusion formula. Both residues must be zero.
The lane stops after this first exact witness.

## 6. Deterministic pilot and target ladder

The exact same frozen binary and production code paths run these one-worker
geometric pilots:

```text
Lane A pilot S:        512, 1024, 2048
Lane B pilot (S,H):   (2048,64), (4096,64), (8192,64)
```

The only production targets are these predeclared rungs:

| Rung | Lane A `S_A` | Lane B `S_B` | Lane B `H` |
|---:|---:|---:|---:|
| 0 | 4,000 | 25,000 | 32 |
| 1 | 6,000 | 50,000 | 48 |
| 2 | 8,000 | 100,000 | 64 |
| 3 | 10,000 | 150,000 | 64 |
| 4 | 12,000 | 200,000 | 64 |
| 5 | 16,000 | 300,000 | 64 |

No interpolated target is allowed. The runner chooses the highest rung that
passes every projected wall, memory, output, disk, load, and deadline gate.
If rung 0 fails, no production search starts.

For each pilot and each target, define the frozen work proxies

```text
W_A(S)   = S^3 log(S+1)
M_A(S)   = S^2 log(S+1)
W_B(S,H) = H S^2 log(S+1)
M_B(S,H) = H S log(S+1).
```

For wall time, the runner takes the largest observed `seconds/W` across the
three pilots and multiplies the target value by `2.5`. For stored limbs, it
takes the largest observed `limb_bytes/M`, multiplies by the target value and
`2.5`, then adds 256 MiB. These are conservative operational projections,
not asymptotic claims.

The runner reserves 600 seconds for closing checks and manifests. Projected
production must fit the smaller of the remaining packet deadline and 12,600
seconds. Projected peak memory must be at most 3.5 GiB under the 4 GiB hard
cgroup limit. Projected aggregate output, including a worst-case first
witness, must be at most 384 MiB under the 512 MiB live cap.

## 7. Workers and chronology

All self-tests and pilots use one worker. Production is one scientific
process. It uses:

- one worker, with Lane A then Lane B, or
- two internal `std::thread` workers, with the independent lanes concurrent.

The two-worker form is allowed only after pilots, only when at least four
CPUs are visible, and only when the sum of projected lane memory is at most
3.5 GiB. It uses no duplicated shards. The scientific source has no
`fork`, `exec`, subprocess, shell, or external-command path. The hard source
and runner ceiling is eight workers. This packet never selects more than two.

The immutable chronology is:

1. authenticate the frozen packet and fresh hostile audit;
2. verify hard containment and deployment compatibility;
3. record CPU, RAM, disk, load, process, and cgroup state;
4. create one fresh target;
5. compile;
6. self-test;
7. run the six one-worker pilots;
8. write and close the projection table;
9. select one frozen rung and one- or two-worker mode;
10. run production;
11. replay any witness independently;
12. verify exact output sets, sizes, and statuses; and
13. write the final hash manifest.

## 8. Hard resource and compatibility boundary

The whole runner is re-executed under a 14,395-second parent timeout with a
five-second kill grace. The kill grace is inside the four-hour envelope. The
runner also watches the direct scientific PID with its monotonic deadline.
The target is subject to:

```text
single-process RLIMIT_AS soft/hard     = 4,294,967,296 bytes
single-process RLIMIT_CORE soft/hard   = 0
single-process RLIMIT_FSIZE soft/hard <= 536,870,912 bytes
single-process RLIMIT_NOFILE           <= 128
single-process RLIMIT_NPROC            <= 64
projected production peak             <= 3.5 GiB
aggregate target output               <= 536,870,912 bytes
projected aggregate output            <= 402,653,184 bytes
selected production workers           <= 8 (actually 1 or 2)
```

The primary containment model is one scientific process with internal
threads. `RLIMIT_AS` therefore applies to the aggregate address space of both
lanes and every worker thread. The source reads back the soft and hard limits
before allocating its large rows. It also reads back the other registered
limits, sets niceness at least 15, checks its internal output reservation,
and rejects more than eight workers.

This is an address-space boundary. The packet does not silently relabel it as
an RSS, physical-memory, or swap-accounting theorem. Current `MemAvailable`,
measured peak RSS, and any cgroup values are separate resource evidence.

Only these memory-containment deployments are supported:

1. the registered single-process hard RLIMIT set above; or
2. the same RLIMIT set inside a `systemd-run`, scheduler, or container
   cgroup-v2 job whose readable `memory.max` is no larger than 4 GiB.

The runner proves that it can set and read back the complete hard RLIMIT set
before target creation and before compilation. If a cgroup-v2 memory limit at
most 4 GiB is present, it records that additional containment. A larger,
unbounded, or absent cgroup is recorded as RLIMIT-primary and is not
represented as cgroup containment. A host that cannot set the full RLIMIT set
is incompatible. The runner stops. It does not silently substitute per-child
limits, polling, fewer rows, local execution, or another host workflow.

The runner checks current available memory, disk, CPU count, load, and active
related production before every expensive phase. The runner starts exactly
one scientific PID. It watches that PID against a monotonic deadline, sends
`TERM` and then `KILL` directly if needed, and proves termination with
`wait`. It does not put `timeout`, a pipeline, or a second scientific process
between itself and that PID. Polling is an early-stop signal. It is not the
memory-containment mechanism.

## 9. Serialization and fail closure

Every cohort, rung, and iteration order is deterministic. Every phase writes
to a new staging directory. A successful phase is moved atomically to its
final directory. A crash leaves only staging data and cannot create a PASS.

Each lane writes:

```text
summary.tsv
checkpoints.tsv
telemetry.tsv
witness.tsv
DONE
```

Witness files have at most one data row. The runner rejects extra files,
missing headers, multiple witnesses, nonzero commands without a closed phase,
or status/output disagreement. It computes SHA-256 for every frozen input,
binary, log, preflight file, result file, and replay file. The final manifest
records partial state on ordinary failure. A kill that prevents the trap from
running still leaves no final PASS marker.

Output is plain TSV with decimal integers and fixed field order. No locale,
random seed, thread schedule, hash-map iteration, or wall clock changes a
mathematical row or witness.
