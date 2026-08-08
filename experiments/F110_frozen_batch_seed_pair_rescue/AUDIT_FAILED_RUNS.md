# F110 hostile-audit failed runs

The audit runner preserves every timeout, nonzero exit, malformed output, and
failed claim under a timestamped `AUDIT_FAILED_*` name.  No failed audit run
existed when this ledger was created.

- `AUDIT_FAILED_20260808T025519.727234Z_RUN_LOG.log`: both verifiers exited
  during audit-harness checks.  The public basis reconstruction failed to
  discard unit fragments created by gcd splitting.  The run-log comparison
  also added one newline that was not present in the extracted payload.  No
  candidate claim was evaluated by this failed attempt.

- `AUDIT_FAILED_20260808T025645.749694Z_RUN_LOG.log` and its preserved
  `PUBLIC_OUTPUT.json`: the N-only replay passed all seven traces and all six
  exact certificates.  The Sage verifier then rejected a brittle source-text
  count because the provenance label also occurs in the result assertion.
  The check now counts only AST calls to `run_pair` with that label.
