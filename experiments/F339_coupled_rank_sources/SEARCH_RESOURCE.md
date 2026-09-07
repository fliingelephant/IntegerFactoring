# F339 coupling-search resources

**Family:** route:F31

The independent return-map check passed before this search was allowed to run.
Its full output SHA-256 is
`66107520aa0305b227bfe2bf8a1520eb84200a93f3234e3747a6bcfd42b92fee`.

The 2026-09-07 preflight reported 60 percent system-wide free memory and load
averages 2.68, 2.11, and 1.86. The identity-check worker reported that its
numerical process had ended. No other local numerical job was active in this
support thread.

The search uses one Python process and one thread. It enforces a 28-second
internal alarm, a 30-second external timeout, and a 256 MiB peak-RSS ceiling.
The `N=209` pilot uses only source indices 0 and 1. Full jobs are split by
`N=209,1333,10807`.

The largest retained rank array has 5,404 entries. Rank maps and deleted-visit
prefixes are rebuilt only as offline validation. The six fixed-rule menus have
10,968, 66,228, and 494,628 raw candidates over all cells at the three inputs;
only counts, hashes, costs, and factor rows are serialized. The estimated
runtime is below 20 seconds and peak RSS below 256 MiB for each job. Offline
factor labels never choose a source record, jump rule, endpoint, or menu.

The `N=209` pilot passed in 0.059 seconds at 54,837,248 bytes peak RSS. The
full `N=209`, `N=1333`, and `N=10807` jobs passed in 0.200, 0.757, and 6.666
seconds, with respective peaks 62,783,488, 63,963,136, and 80,609,280 bytes.
Aggregation passed in 0.129 seconds and peaked at 168,099,840 bytes while
loading the three retained outputs. No job reached a resource limit or
reported an anomaly. No numerical process remains.
