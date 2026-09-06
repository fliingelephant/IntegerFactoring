# F226-D04 preregistration — exact local-log performance repair

F226-D03 did not complete within the orchestration call.  It searched a
local exponent by a linear walk of length `ord_ell(N)` for every auxiliary
prime.  D04 replaces this with the exact subgroup test `p^h=1 mod ell`
followed, only on acceptance, by Sage's exact discrete-log routine with known
order `h`.  It also computes `ceil(N^(1/4))` by exact integer root instead of
a real power.  The cohort, recorded quantities, exhaustive subset cap, and
300-second process limit remain unchanged.  Output is `D04_OUTPUT.json` and
the log is `logs/F226-D04.log`.

