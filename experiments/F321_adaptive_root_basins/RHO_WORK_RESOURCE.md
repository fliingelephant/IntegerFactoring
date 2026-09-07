# Work-matched Pollard-rho resource control

The eight public datasets and 32 independent trials per case are identical
to SCALE_REPORT.md. For
\[
 B=\min(4096,\operatorname{bitlength}(N)^2),
\]
each rho trial receives \(W=B(B-1)/2\) modular multiplications, matching the
worst-case multiplication count of an adaptive attempt that accepts a new
root after every H evaluation. Each Floyd iteration uses three
multiplications.

A local preflight at approximately 12:48 on 2026-09-07 found 69 percent
free memory, zero swap, and load averages 1.46, 1.58, 1.70. Expected rho
hits are far below the cap on these offline semiprimes. The estimate is
below 15 seconds and 128 MiB.

The run has its own internal 28-second alarm, external 30-second timeout,
and 512 MiB peak-RSS check. It does not rerun the adaptive trials.

The run completed in 0.325042 seconds at 27,017,216 bytes peak RSS. It
stayed below every limit.
