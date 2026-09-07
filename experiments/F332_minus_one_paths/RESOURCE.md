# F332 resource plan

Status: pre-run estimate.

## Scope and limits

The exact control compares frozen F326, direct fine formulas, and the adjacent
P/Q block kernel for every `N=1 mod 4` through 101. It is estimated below one
second and 64 MiB.

The initial public run uses the seven retained F328 moduli with `N=1 mod 4`.
Reflection is capped at 8,192 fine F calls. The compressed adjacent path is
capped at 8,192 block iterations and records its equivalent fine calls. Equal
numeric caps have different path coverage. Censored methods may be rerun in
fresh jobs at cap 262,144 after the pilot.

- Every job is one process and one thread.
- Every job has a 28-second internal alarm, a 30-second GNU `timeout`, and a
  512 MiB measured peak-RSS limit.
- Exact integer lifts stop before exceeding 4,096 bits. The modular traversal
  and letter counters continue without the lift.
- Public algorithms retain only current modular state, counters, and short
  trace prefixes. Estimated peak memory is below 64 MiB.
- At 262,144 iterations, the 92-bit case performs at most approximately
  262,144 inversions for reflection or the block kernel. Estimated time is
  below 15 seconds per method, subject to the initial pilot.

F331 numerical work was confirmed complete before this preflight. At
2026-09-07 16:17 +0800, load averages were `2.14,2.38,2.39`, system-wide free
memory was 52 percent, no pages were throttled, and boot counters showed zero
swap-ins and swap-outs. No experiment worker appeared in the process
table. F332 jobs will run sequentially.

## Actual runs

The exhaustive control passed in 0.003 seconds at 28,295,168 bytes peak RSS.
It completed all 75 frozen-path comparisons.

| Scope | Jobs | Process seconds per job | Largest peak RSS |
|---|---:|---:|---:|
| Initial 8,192-cap runs | 7 | 0.003--0.125 | 28,393,472 bytes |
| Extended 262,144-cap runs | 5 | 0.443--2.193 | 28,344,320 bytes |
| Final aggregation | 1 | 0.006 | 29,802,496 bytes |

The 12 numerical jobs used 6.699 process seconds in total. All jobs were
single-threaded and remained below the time and memory limits. The 4,096-bit
lift guard activated where expected; exact lift arithmetic then stopped while
the public modular path continued. No special-return guard or resource anomaly
occurred.
