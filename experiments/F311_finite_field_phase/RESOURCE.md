# Resource record

Initial estimate: one Python process, under 30 seconds and 128 MiB. All three
sources install a 30-second alarm. Initial preflight at 10:05 local time on
2026-09-07 reported 69% available memory and load 2.49,2.49,2.33.

The main pilot uses truth tables of at most 4096 bits, field fitting only
through 256 elements, and packed binary linear algebra. It took 1.027856 seconds
and 20,365,312 peak RSS bytes on macOS.

Before the bounded nonlinear-pullback continuation, preflight at 10:15
reported 67% available memory and load 3.58,2.46,2.30. The process remained
small: the final run took 0.149828 seconds and 22,773,760 peak RSS bytes. The later certificate check
used less than 0.1 seconds and 24 MiB, with no concurrent process from this worker.

Commands:

    python3 experiments/F311_finite_field_phase/pilot.py > experiments/F311_finite_field_phase/run.log 2>&1
    python3 experiments/F311_finite_field_phase/QUADRATIC_PULLBACK.py > experiments/F311_finite_field_phase/QUADRATIC_PULLBACK_run.log 2>&1
    python3 experiments/F311_finite_field_phase/CERTIFICATES.py > experiments/F311_finite_field_phase/CERTIFICATES_run.log 2>&1

Outputs retain seeds, original N/M values, complete truth tables, field
polynomials, successful coefficient witnesses, nonmembership certificates,
and exact checks. The certificate run was repeated after adding an independent
enumeration of its 16-element genus-two curve; the final log includes that
verification. No floating-point acceptance test is used.

The pullback run was repeated after correcting its metadata to list only
visited centers when a successful fit stops the search. Mathematical
outcomes were unchanged.
