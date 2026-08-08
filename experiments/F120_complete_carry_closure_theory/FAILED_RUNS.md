# F120 Failed Runs

## 2026-08-08T05:48:32Z — environment failure

The first registered run failed before it tested a candidate. Sage 10.9 tried
to create its lazy-import cache under `/Users/zhou/.sage/cache`, which is not
writable in this workspace. Python raised `PermissionError` during
`from sage.all import ZZ`.

Preserved artifacts:

- `RUN_FAILED_20260808T054832Z_EXIT_1.log`;
- `OUTPUT_FAILED_20260808T054832Z_EXIT_1.json`.

The failed output has status `NO_OUTPUT`. It contains no mathematical
evidence.

The retry was explicitly approved. It changed only `DOT_SAGE`, which now
points to the experiment-local `.sage` cache. The registered corpus, search
source, proof-enabled Sage primality checks, 60-second timeout, and evidence
standard did not change. The retry passed and produced `OUTPUT.json` and
`RUN.log`.
