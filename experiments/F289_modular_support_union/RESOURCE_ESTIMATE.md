# F289 resource estimate

This experiment uses one Python process and a 60-second source alarm.

Before the run, the 16 GB host reported load averages 2.51, 2.43, and 2.18,
73% free memory, no swap activity, and no other numerical job. One macOS
suggestion service used approximately one CPU core. The pilot does not need
all cores.

The largest planned scale is \(B=2^{16}\). Its public cutoff \(K\) is expected
to be below \(10^5\). At most \(O(K)\) exact integer points are live for one
case. Cases run sequentially. The estimated peak memory is below 128 MB. The
initial \(B=2^8\) scale runs first. Extension through \(B=2^{16}\) occurs only
when the initial scales finish in less than 20 seconds.
