# F261-D01 frozen prelaunch manifest

Frozen on 2026-08-13 before the first compile, benchmark, cohort generation,
or scan.

## Frozen artifact hashes

```text
df27b6557ac2fe2ae29a495241c66741e864f8d667237f04855aa82f499aa67f  ALGEBRA.md
ae0e04eb7b1593795560eae3444c753ed07c4e4c0758c41386562fb72779c7f1  PREREGISTRATION.md
9af35178e041b3d02f4bf33134b451b9fe938cf8235ae450fb8df7f0027b1e6d  search.cpp
07fd9d53c1e2f08b647b24272908f1487ed1ba38657e7aef1a196d4f389137f3  remote_run.sh
```

The source and runner are frozen at these bytes.  Any later repair creates a
new hash set and must be declared before execution.

## Static review completed

- The runner passes `bash -n`.
- The exact prefix congruence, direct `T` interval, signed endpoint formulas,
  quadratic decoder, `Kq=0` endpoint, and one-dimensional inverse map were
  reviewed against `ALGEBRA.md`.
- The runner checks for F258, F259, and F260 before compilation.
- The runner limits the preflight to one hour and the full run to four hours.
  It uses `nice -n 15`, at most eight workers, and a 4 GiB virtual-memory cap.

## Mandatory unexecuted prelaunch gates

F258 was active at freeze time.  The incompatibility rule therefore forbade
compilation and all dynamic checks.  After F258, F259, and F260 are absent,
the runner must do all of these steps on the target in order:

1. inspect load, available RAM, free disk, and incompatible processes;
2. compile the frozen C++17 source with Boost Multiprecision;
3. pass the exact small self-test;
4. pass the frozen public inner-loop benchmark;
5. observe at least one hit in each separate 60-bit cohort generator
   benchmark, including safe-safe;
6. abort if the conservative projected run time exceeds 12,000 seconds;
7. only then generate cohorts and launch F261-D01.

No dynamic correctness or performance claim is made before these gates pass.

## Frozen scale and resource forecast

The cohort scan has 1,368 rows and at most 711,622,656 exact centered-carry
evaluations.  The preflight uses 20,000,000 public synthetic carry evaluations
and 29,000,000 separately labelled generator attempts.  Its factor-three
inner-loop extrapolation covers predictor and exact candidate-bound overhead.

The full result keeps aggregate rows and selected witnesses, not dense traces.
Projected RSS is below 512 MiB even at eight workers.  Projected output is
below 25 MiB.  Both forecasts are well below the frozen 4 GiB RSS and 1 GiB
output caps.  Target runtime is deliberately left unclaimed until the frozen
preflight measures the remote host.
