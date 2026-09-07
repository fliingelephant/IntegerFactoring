# F339 return-map check resources

**Family:** route:F31

## Preflight and estimate

The preflight at 2026-09-07 19:17 +0800 found load averages 1.65, 1.66, and
1.70. System-wide free memory was 60 percent of 16 GiB. There were zero
throttled pages and zero swap-ins or swap-outs in the current boot counters.
The process snapshot showed no research numerical worker. One system FSEvents
process was briefly active; it did not create memory pressure.

The coupling-search worker reported no active numerical job and waited for
these checks. The plan therefore used one numerical process and stayed below
the two-job shared limit.

The pilot was estimated below one second and 64 MiB. The full direct
enumeration was estimated below eight seconds and 64 MiB. Each job used one
thread, an 8-second internal alarm, a 10-second external timeout, and a
67,108,864-byte measured RSS ceiling.

## Actual use

The retained pilot covered generic odd N<=11 and engineered odd N<=51. It
passed in 0.0229 seconds at 25,853,952 bytes peak RSS.

The retained full job covered generic odd N<=31 and engineered odd N<=511. It
passed in 3.4397 seconds at 25,640,960 bytes peak RSS. No split was needed.
Neither job reached a timeout or the memory ceiling. No resource censor was
reported as a mathematical failure.

The direct oracle stores only one small sorted orbit, rank map, deleted prefix,
and rank-pair counter at a time. The largest generic rotation length was 31.
The largest engineered rotation length was 45. No hidden factor table or
large retained trace was needed.
