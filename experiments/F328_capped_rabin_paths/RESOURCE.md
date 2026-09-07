# F328 resource plan

Status: pre-run estimate. Actual measurements will be appended after each
retained job.

## Scope

The experiment measures capped random-square attempts. It does not enumerate
the F326 domain and does not call the F326 complete-path routine except in a
few tiny agreement checks. The arithmetic solver retains one current rank and
receives only `N`, `a`, the auxiliary method, and the cap.

The planned scales are 20, 28, 36, 44, 60, and 92 bits. Two independently
generated balanced semiprimes are retained at each scale. The target is 16
outer trials per modulus and one solver path of at most 2,048 F calls per
eligible trial. Results at caps 32, 128, 512, and 2,048 are prefix views of
that one path. Censored prefixes and full-cap censors are retained.

## Limits and estimates

- Every job is single-threaded.
- Every ordinary-Python job has a 25-second internal alarm, a 30-second GNU
  `timeout`, and a 512 MiB measured peak-RSS limit checked after every trial.
- Offline prime generation uses the existing `/usr/local/bin/sage -python`
  runtime with proof-enabled `Integer.next_prime`. It generates only 24 primes,
  of at most 46 bits. Estimated time is below 10 seconds after startup and
  estimated peak RSS is below 512 MiB. Sage startup will be measured before
  generation.
- The tiny agreement check and capped pilot are estimated below 5 seconds and
  128 MiB.
- A full per-modulus job performs at most 16*2,048 = 32,768 F calls. Rank
  selection makes its cost grow with `log N`; the pilot will determine whether
  larger scales need smaller fresh batches. Trial count or cap reductions will
  be recorded before aggregation. No unfinished trial will be discarded.

The offline factors are input labels and validation metadata. They never enter
the arithmetic solver. Hidden roots remain in the outer trial driver and enter
only exact postprocessing after a verified root is returned.

## Preflight and actual runs

Preflight at 2026-09-07 14:54 +0800 found load averages
`1.93, 1.65, 1.59`, 66 percent system-wide free memory, zero throttled pages,
and zero swap-ins or swap-outs in the current boot counters. The process view
showed no sustained CPU saturation. Reading the process table required the
normal read-only sandbox escalation. A direct `sysctl hw.memsize` read was
blocked, but `memory_pressure -Q` reported 17,179,869,184 bytes of physical
memory.

The first sandboxed Sage startup could not write its existing user cache and
therefore did no generation. The authorized rerun completed a proof-enabled
`next_prime` query in 1.55 seconds with peak RSS 256,065,536 bytes and no swaps.
This is below the 512 MiB limit, so the retained prime-generation job may use
the existing Sage runtime.

The tiny F326 agreement job passed in 0.0007 seconds at 27,607,040 bytes peak
RSS. The first retained 20-bit pilot ran two full-protocol trials in 0.049
seconds at 27,459,584 bytes peak RSS; its paths stopped after 963 and 291 F
calls. The retained 92-bit calibration trial reached the 2,048-call cap in
2.256 seconds at 27,639,808 bytes peak RSS, with 6,109,312 floor-sum Euclidean
iterations.

The 92-bit calibration implies that 16 trials in one process would exceed the
25-second internal limit. The scale run will therefore use fresh jobs of at
most four trials at 92 bits. The 60-bit jobs will use at most eight trials as a
margin. Lower scales will use at most one 16-trial job per modulus. The pilot
trials use the exact final protocol and fixed trial indices, so they remain in
the aggregate; those indices will not be rerun.

All 22 retained solver jobs passed. They contain all 192 planned trials. The
sum of their process wall times is 130.504 seconds. The longest one is a
four-trial 92-bit job at 9.870 seconds. Their largest peak RSS is 28,442,624
bytes. The final aggregation took 0.015 seconds and peaked at 31,244,288 bytes.

| Scope | Fresh jobs | Trials | Process seconds per job |
|---|---:|---:|---:|
| 20 bits, including retained pilot | 3 | 32 | 0.049--0.340 |
| 28 bits | 2 | 32 | 1.534--1.879 |
| 36 bits | 2 | 32 | 3.974--4.196 |
| 44 bits | 2 | 32 | 6.500--6.776 |
| 60 bits | 4 | 32 | 6.963--7.545 |
| 92 bits, including retained pilot | 9 | 32 | 2.256--9.870 |

Every scale job was single-threaded and finished below both time limits. No
job crossed the memory limit, failed, or lost an unfinished capped trial.
