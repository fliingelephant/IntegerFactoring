# Selected-fiber guard resource control

The guard pilot uses four balanced scales, two values \(K=2,8\), a matched
base algorithm, and 16 independent trials per case and method. Every
proposal and guard evaluation counts against the same public budget
\[
 B=\min(4096,\operatorname{bitlength}(N)^2).
\]
The estimate is below 10 seconds and 128 MiB. It runs separately from the
larger public scale with its own internal 28-second alarm, external
30-second timeout, and 512 MiB peak-RSS check.

The run completed in 0.902084 seconds at 25,919,488 bytes peak RSS. It
stayed below every limit.
