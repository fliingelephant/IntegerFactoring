# F338 resource plan

**Family:** route:F31

Status: pre-run estimate.

The preflight at 2026-09-07 18:24 +0800 found load averages 2.12, 1.86, and
1.85. System-wide free memory was 60 percent of 16 GiB. There were zero
throttled pages and zero swap-ins or swap-outs in the current boot counters.
The process snapshot showed no numerical worker in the top CPU list. The data
volume had 8.9 GiB free.

The F337 worker reported no active numerical job and reserved at most one
single-threaded pilot slot. F338 will use at most the other slot and will
notify that worker before scale work. The total number of simultaneous
numerical jobs must remain at most two.

The F336 source corpus occupies 24 compact gzip row artifacts. A 64-index
batch contains 896 rows. F336's slowest corresponding source batch took 1.35
seconds below 38 MiB RSS. Replaying one minimum descent and running one fair
descent per accepted row should keep a batch below 4 seconds and 128 MiB.
The estimated sum over all 24 batches is below 30 seconds. The pilot is
estimated below 2 seconds and 128 MiB.

Every process is single-threaded. It has a 28-second internal alarm, a
30-second external timeout, and a measured 536,870,912-byte RSS ceiling.
Full traces are limited to controls, pilot rows, distinct output witnesses,
and anomalies. Compact rows and deterministic gzip JSONL avoid duplicate
trace storage.

## Actual use

The repaired active F336 DP checks used the reserved F338 process slot. The
N<=51 check passed in 0.0068 seconds at 27,017,216 bytes peak RSS. The N<=301
check passed in 0.524 seconds at 27,607,040 bytes. Under the corrected
both-child charge, fair branches had lower gcd calls per success on 28 of the
86 finite inputs where both policies succeeded.

The F338 pilot passed in 0.075 seconds at 41,058,304 bytes. It retained all
56 transformed source rows and both complete small branch trees. All 24 scale
jobs passed. Their process times sum to 22.854 seconds. The slowest job took
2.633 seconds, and the largest scale-job peak RSS was 150,994,944 bytes. The
aggregate passed in 0.724 seconds at 65,224,704 bytes.

No job reached its internal timeout, external timeout, or memory ceiling. No
resource censor was recorded as an algorithm failure. All F338 numerical
processes were terminal before report generation. Scale outputs, compact rows,
and distinct-output witnesses occupy about 13 MiB in total.
