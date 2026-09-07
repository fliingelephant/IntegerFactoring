# Resource control

The bulk spectrum computation is exact enumerative discovery. It is not a
candidate polynomial-bit evaluator.

The shared preflight supplied by the root reported 70 percent free memory,
zero swap, load averages 1.98, 2.12, 2.20, one requested CPU, and no large
research job. A local recheck at approximately 11:37 on 2026-09-07 reported
a 16 GiB host, 71 percent free memory, zero swap, and load averages 2.58,
2.31, 2.26.

The pilot covers k=8,10,12, plus complete direct controls for M<=128. Its
estimate is below 10 seconds and 256 MiB. Scaling to k=14,16,18 is permitted
only after the measured pilot remains comfortably below the hard limits.
The k=18 polynomial length is R=65,536 and its largest coefficients are
about 40 bits.

Every run uses an internal 28-second alarm, an external 30-second timeout,
and a one-GiB RSS watchdog. Only one Sage process runs at a time.

The pilot completed all k=8,10,12 spectra and the small controls in
0.618024 seconds at 257,392,640 bytes peak RSS. Before scaling, a second
preflight at approximately 11:42 reported 69 percent free memory, zero
swap, and load averages 2.12, 2.19, 2.21. The k=14,16,18 scale run then
completed in 1.636694 seconds at 309,329,920 bytes peak RSS. The k=18
modulus itself used 0.340628 seconds. Both runs stayed below every limit.
