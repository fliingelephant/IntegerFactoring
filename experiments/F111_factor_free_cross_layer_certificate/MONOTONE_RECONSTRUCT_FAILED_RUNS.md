# Monotone reconstruction failed runs

The named 900-second runner preserves every timeout, nonzero exit, malformed
output, and failed claim under a timestamped `MONOTONE_RECONSTRUCT_FAILED_*`
name.  No failed attempt existed when this ledger was created.

The first complete run passed in 11.986073 seconds.  The verifier then gained
an explicit polynomial-time early branch for nonunit trial screens.  The final
run for that source passed in 12.020008 seconds.  A proof audit then corrected
the symbolic relation-value bound from less than `2n` bits to at most `2n`
bits.  The final authoritative run passed in 12.185525 seconds.  No run timed
out or failed, so there is no preserved failed-run file.
