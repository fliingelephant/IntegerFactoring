# F326 resource control

**Family:** route:F31

The public pilot uses the eight exact F324 parameter pairs at each of
N=209 and 1333. It also runs exhaustive controls for every odd N through
101 and every unit a<=16. Full construction checks are restricted to
Jacobi-positive a; the all-residue Gauss parity check covers both Jacobi
signs.

The separate Rabin pilot uses 32 trials at each pilot modulus. Hidden-root
and solver-choice random streams have separate derived seeds. Explicit
domain lists are built only to validate the uniform rank/select algorithm,
and their time is recorded separately.

A preflight at approximately 14:32 on 2026-09-07 found 69 percent
system-wide free memory, no throttled pages, and load averages
1.80, 1.69, 1.59. Each pilot is estimated below five seconds and 128 MiB.
Runs are sequential. Each process has an internal 28-second alarm, an
external 30-second timeout, and a 512 MiB ceiling.

## Actual runs

| Run | Wall time | Peak RSS |
|---|---:|---:|
| public pilot plus exhaustive controls | 0.123 seconds | 54,624,256 bytes |
| public scale | 0.339 seconds | 60,981,248 bytes |
| Rabin pilot | 0.038 seconds | 54,984,704 bytes |
| Rabin scale | 0.807 seconds | 61,603,840 bytes |

All four processes passed without a path, time, or memory failure. Explicit
domain validation took 0.0004 seconds in the public pilot, 0.079 seconds in
the public scale, 0.001 seconds in the Rabin pilot, and 0.327 seconds in the
Rabin scale. These times are included in process wall time but excluded from
the pairing operation counts.
