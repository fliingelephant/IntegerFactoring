# F112 failed runs

## 2026-08-08 02:48:38Z — sandbox semaphore query

The first run stopped before any case started.  Python's process-pool
constructor called `os.sysconf("SC_SEM_NSEMS_MAX")`, and the sandbox denied
that system query.  The complete environment failure is preserved in
`RUN_FAILED_20260808T024838Z_EXIT_1.log`.  It supplies no mathematical
evidence.  The identical runner is retried with permission for local process
pool use.

## 2026-08-08 02:52:44Z — empirical source claim refuted

The approved retry completed all 100 cases with exit code zero.  The runner
preserved it under the failed-claim names because 14 inputs reached the end of
the complete `(2,v)` menu without a factor.  This is valid negative evidence,
not an implementation failure.  The canonical data and log are
`OUTPUT_FAILED_20260808T025244Z_CLAIM.json` and
`RUN_FAILED_20260808T025244Z_CLAIM.log`.
