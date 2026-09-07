# F334 resource plan

Status: pre-run estimate. Actual pilot and scale measurements will be appended
after the retained jobs.

## Scope

F334 implements the route:F31 count descent from the frozen F330 design. It
uses the frozen F326 floor-sum methods. It does not enumerate a Gauss domain or
walk the full involution graph.

The exact small control covers every odd composite N at most 101 and every
Jacobi-positive unit a. Its fixed and inverse-start rows are exhaustive in a.
Fresh-mode inner parameters use independent reproducible random streams and
remain non-exhaustive.

The scale input is the two retained F328 moduli at each of 20, 28, 36, 44, 60,
and 92 bits. Each modulus receives 256 accepted Jacobi-positive initial
parameters. Fixed, fresh, and inverse-start descents use the same initial a.
Nonunit generation draws are retained as separate earlier factor successes.

The public menu controls use D=8, 32, and 128. Fixed-start menus depend only on
N. Inverse-start menus depend on the public pair (N,a). Candidate sets are
deduplicated within each menu, and every retained candidate is gcd-screened.

## Limits and estimate

- Each job uses one Python process and one thread.
- Each retained numerical job has a 28-second internal alarm and a 30-second
  external timeout.
- Peak RSS must remain at most 536,870,912 bytes.
- The tiny pilot is estimated below 3 seconds and 128 MiB.
- One 256-parameter modulus batch performs at most O(256 log N) exact count
  queries. The D=128 inverse menus dominate raw gcd count. A 92-bit batch is
  estimated below 20 seconds and 256 MiB. The pilot will decide whether it must
  be split.
- Expected retained output is below 100 MiB in total. Full descent traces are
  retained, but duplicate all-gcd-one menu tables are replaced by exact counts
  and candidate-set hashes.

## Preflight

The preflight at 2026-09-07 17:15 +0800 found load averages
1.63, 1.74, and 1.75. System-wide free memory was 62 percent of 16 GiB.
There were zero throttled pages and zero swap-ins or swap-outs in the current
boot counters. The largest visible research-related process was the Codex host
at about 615 MiB RSS; no numerical worker was active. The collaborating F335
worker confirmed that it had no active or planned heavy process during this
window.

The data volume had 9.1 GiB free. This is sufficient for the estimated output.
The first process-table read was blocked by the sandbox. The approved read-only
ps retry supplied the process snapshot. Homebrew timeout is available at
/opt/homebrew/bin/timeout.

## Actual use

The final source hash is
`cb93f160d57b2a3285551cbd268e732917e3062a90eb8ca62df843f581be1e24`.
The retained pilot passed in 0.197 seconds at 33,882,112 bytes peak RSS. It
used eight accepted parameters for N=209 and four for the 92-bit input
`b92_i0`. The exact small job passed in 0.166 seconds at 47,153,152 bytes peak
RSS. It covered 25 odd composite moduli and 547 Jacobi-positive units.

All twelve scale jobs passed. Each job used one process and one thread, and
each retained 256 accepted parameters. Their summed process time was 46.445
seconds. The slowest job was `b92_i0` at 11.467 seconds. The largest scale-job
peak RSS was 124,829,696 bytes. The aggregate job used 131,907,584 bytes. No
job reached either timeout or the memory limit. No attempt was lost or labeled
as a stopping failure because of a resource censor.

| Scale | Per-job wall-time range (seconds) |
|---|---:|
| 20 bits | 0.72--0.74 |
| 28 bits | 1.30--1.32 |
| 36 bits | 1.99--2.01 |
| 44 bits | 2.82--2.88 |
| 60 bits | 4.92--5.00 |
| 92 bits | 11.29--11.47 |

The scale summaries occupy 30,874,471 bytes. Deterministic gzip JSONL keeps
all 3,072 full per-parameter traces in 28,224,321 bytes. This avoids repeating
large validation tables in the readable report.
