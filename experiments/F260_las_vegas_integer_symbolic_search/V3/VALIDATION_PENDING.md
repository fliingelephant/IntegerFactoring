# F260-D03 V3 validation pending

Status: **STATIC PACKET ONLY — DO NOT GENERATE A CORPUS**

D03 has not been compiled or executed. Preparation did not invoke the runner,
use a remote host, generate a tiny or full corpus, inspect a cohort, or edit a
durable ledger.

These checks remain mandatory on the authenticated final source:

1. a fresh independent hostile static audit and exact audit sidecar;
2. target C++17 compilation with Boost Multiprecision under the runner caps;
3. the final-source self-test, including normalized word-child ordering and
   residual-extrema aggregation;
4. the full-grammar 32-bit row and conservative 32-program 60-bit row
   benchmark;
5. a runtime projection no larger than four hours;
6. a projected peak no larger than 4 GiB and projected output no larger than
   1 GiB; and
7. every conflict, resource, output, 45-field aggregate, row-count, digest,
   manifest, audit-binding, and shared-deadline gate in `remote_run.sh`.

The runner must stop before discovery if any check fails. Discovery and
held-out share one four-hour production deadline. A finite null result is
valid. Validation must not weaken a frozen syntax, score, cohort, selection,
or gate.

