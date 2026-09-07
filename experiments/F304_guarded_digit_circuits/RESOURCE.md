# Resource record

Initial estimate: one Python process, under 30 seconds and 128 MiB.
The source installs a 30-second alarm. Enumeration has at most 512 graph
points per case. Exact Taylor jets have at most 17 rational coefficients.

Preflight at 08:00 local time on 2026-09-07: 71% memory available, load
averages 2.56, 2.36, 2.17. This worker launched no parallel math process.

Command:

    python3 experiments/F304_guarded_digit_circuits/pilot.py > experiments/F304_guarded_digit_circuits/run.log 2>&1

Measured runtime 0.035923 seconds; peak RSS 17,563,648 bytes on macOS.
The retained seed is 30420260907. All checks use integers or exact rational
numbers. No floating-point mathematical acceptance test is used.
