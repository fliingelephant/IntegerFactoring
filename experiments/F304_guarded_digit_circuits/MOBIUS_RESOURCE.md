# Continuation resource record

Estimate: each pilot under 30 seconds and 128 MiB, one process at a time.
Both sources install a 30-second alarm. The moment pilot requests degree
three; its coefficient and exact-power arrays have polynomially bounded
small dimensions. Only its external audit enumerates canonical points.

Preflight at 08:19 local time on 2026-09-07: 72% memory available and
load averages 2.16, 2.14, 2.13. This worker launched no concurrent math job.

Commands:

    python3 experiments/F304_guarded_digit_circuits/MOBIUS_BANK.py > experiments/F304_guarded_digit_circuits/MOBIUS_BANK_run.log 2>&1
    python3 experiments/F304_guarded_digit_circuits/MOBIUS_BRANCHES.py > experiments/F304_guarded_digit_circuits/MOBIUS_BRANCHES_run.log 2>&1
    python3 experiments/F304_guarded_digit_circuits/MOBIUS_BANK_GROWTH.py > experiments/F304_guarded_digit_circuits/MOBIUS_BANK_GROWTH_run.log 2>&1

MOBIUS_BANK measured 0.019572 seconds and 17,694,720 peak RSS bytes.
MOBIUS_BRANCHES records its measured runtime and RSS in its output and log.
The degree-two bank-growth follow-up measured 0.010664 seconds and
18,137,088 peak RSS bytes. It ran after the other processes completed,
under the same 30-second alarm and 128 MiB estimate.
All mathematical checks use exact integers. No floating-point acceptance
criterion is used.
