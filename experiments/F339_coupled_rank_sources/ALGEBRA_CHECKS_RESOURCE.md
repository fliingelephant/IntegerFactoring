# F339 algebra-check resources

**Family:** route:F31

Status: pre-run estimate.

The preflight at 2026-09-07 20:02 +0800 found load averages 1.88, 1.83, and
1.78. System-wide free memory was 65 percent of 16 GiB. There were zero
throttled pages and zero swap-ins or swap-outs in the current boot counters.
No research numerical worker appeared in the process snapshot. The data volume
had 8.9 GiB free.

One unrelated application held about 3.1 GiB RSS, but the measured free-memory
margin remained ample for the declared 256 MiB ceiling. The F339 coupling
worker had completed its search and was not running a numerical job.

The pilot covers generic identities through N=11, all half-orbit units through
N=51, and the first two source indices of every frozen F337 law at N=209. It
is estimated below two seconds and 128 MiB.

The complete work is split into an identities job and a frozen-source job.
Each uses one thread, a 28-second internal alarm, a 30-second external timeout,
and a 268,435,456-byte measured RSS ceiling. Direct phase prefixes avoid
recomputing deleted counts. The expected sum of actual arithmetic time is
below ten seconds.

## Actual use

The final pilot passed in 0.067 seconds at 81,281,024 bytes peak RSS. The
identity job passed in 2.296 seconds at 41,828,352 bytes. The frozen-source
job passed in 0.576 seconds at 186,712,064 bytes. Aggregation passed in 0.013
seconds at 43,892,736 bytes.

All jobs remained single-threaded and below their time and memory limits. No
split beyond the planned identity/source separation was needed. No timeout,
resource censor, or arithmetic anomaly occurred. All numerical processes were
terminal before report generation.
