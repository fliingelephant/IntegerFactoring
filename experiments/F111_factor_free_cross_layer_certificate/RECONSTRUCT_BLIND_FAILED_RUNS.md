# Proof-blind reconstruction failed runs

The named runner preserves every timeout, nonzero exit, malformed output, and
failed claim under a timestamped `RECONSTRUCT_BLIND_FAILED_*` name.  No failed
attempt existed when this ledger was created.

The first attempt completed in 0.128343 seconds with exit code 0 and status
`PASS`.  A source-only advice-boundary tightening was then applied.  The final
authoritative rerun completed in 0.143313 seconds with exit code 0 and status
`PASS`.  Therefore there are no preserved failed-run files.
