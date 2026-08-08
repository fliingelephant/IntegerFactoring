# F109 failed runs

## R01 — asserted isolated-pair success

The first formal run completed the recursive replay for the first case and
then failed an assertion that its final active pair must factor in isolation.
This was a false test assumption, not a timeout or evidence against the
recursive run.  The exact log is preserved as
`RUN_FAILED_R01_ASSERTED_ISOLATED_SUCCESS.log`.  R02 records isolated-pair
failure as an admissible and informative outcome.
