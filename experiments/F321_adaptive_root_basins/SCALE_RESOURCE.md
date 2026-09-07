# Larger public-trial resource control

The original F321 sources, outputs, logs, and hashes remain unchanged.

The root requested six balanced scales with \(p\) near
\(2^{18},\ldots,2^{28}\), two unbalanced scales, and 32 independent trials
for each of three public methods. Every trial uses
\[
 B=\min(4096,\operatorname{bitlength}(N)^2).
\]
The observed smaller pilot and the proposed \(p^{1/3}\) stage scale suggest
about ten million adaptive modular multiplications in the high cases. This
is a sizing hypothesis only. The estimate is below 15 seconds and 256 MiB,
so one batch is used.

A local preflight at approximately 12:43 on 2026-09-07 found 69 percent
free memory, zero swap, and load averages 2.11, 1.67, 1.77. The run has an
internal 28-second alarm, an external 30-second timeout, and a 512 MiB
peak-RSS check.

The run completed in 2.208405 seconds at 26,755,072 bytes peak RSS. It
stayed below every limit.
