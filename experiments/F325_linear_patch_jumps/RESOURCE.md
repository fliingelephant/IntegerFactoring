# F325 resource control

**Family:** route:F31

The pilot uses the F324 public pairs at \(N=209,1333\), plus conditional
public \(a=-1\) controls where its Jacobi sign is positive. Three paths are
compared: original micro, modified micro, and modified macro. The cap is
\(\min(3N,8192)\) equivalent calls to \(r\).

Small controls exhaust the modified involution on all states for odd
\(N\leq31\). Every Gurobi first-exit result is separately validated by
an exact linear scan; validation scans are timed but not charged as
algorithm work.

Gurobi 13.0.2 uses a quiet environment, one thread, a one-second limit per
call, zero relative and absolute MIP gaps, and \(10^{-9}\) integer and
feasibility tolerances. Returned integers are rounded and checked exactly.
An unresolved solver call censors its path without a fallback.

A local preflight at approximately 14:05 on 2026-09-07 found a 16 GiB host,
70 percent free memory, zero swap, and load averages 1.93, 1.81, 1.69.
The estimate is below 15 seconds and 256 MiB. Each process has an internal
28-second alarm, external 30-second timeout, and 512 MiB ceiling.

## Actual runs

The pilot completed in 0.422 seconds with peak RSS 62,586,880 bytes. All 18
queries completed. The scale run completed in 0.043 seconds with peak RSS
60,964,864 bytes. All 17 queries completed. Neither run reached a solver,
path, time, or memory censor.

Across both runs, the macro paths used 1,474 actual calls to `r*` to represent
1,959 expanded calls. The 77 Gurobi calls were all resolved and all returned
first exits agreed with exact linear scans. One additional first exit used the
explicit `a=-1` rule without Gurobi. Validation scanned 483 candidate integers
in 0.000083 seconds; this work is recorded separately from algorithm work.

The independent induced-matching control completed in 0.579 seconds with peak
RSS 32,522,240 bytes. It exhaustively checked all 4,016 ordered unit pairs for
odd N through 31. Its 224,970 retained-state comparisons all matched the
explicit ordered-subset matching, and the restricted `r` matching was
invariant on every checked state.
