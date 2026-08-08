# F114 failed runs

## 2026-08-08 02:55:29Z — dynamic import was not picklable

The first process-pool launch stopped before a case completed.  The submitted
function belonged to a dynamically named imported module, so Python could not
find that module while serializing the worker task.  The exact log is
`RUN_FAILED_20260808T025529Z_EXIT_1.log`.  It supplies no mathematical
evidence.  R02 adds only a top-level wrapper in the F114 source.
