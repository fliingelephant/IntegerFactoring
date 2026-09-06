# F260-D02 V2 validation pending

Status: **STATIC PACKET ONLY — DO NOT GENERATE A CORPUS**

F258-D01 was active when this packet was frozen. The registered incompatibility
firewall prohibits compiling or executing D02 during that run. Packet
preparation therefore did not compile `search.cpp`, execute any binary, invoke
`remote_run.sh`, use a remote host, generate a tiny or full corpus, inspect a
cohort, or modify a durable ledger.

These checks remain mandatory on the authenticated final source:

1. a fresh independent hostile static audit and exact audit sidecar;
2. target C++17 compilation with Boost Multiprecision under the runner caps;
3. the final-source self-test;
4. the full-grammar 32-bit row and conservative 32-program 60-bit row
   benchmark;
5. a runtime projection no larger than four hours;
6. a projected peak no larger than 4 GiB and projected output no larger than
   1 GiB; and
7. every conflict, resource, output, row-count, digest, manifest, and shared
   deadline gate in `remote_run.sh`.

The runner must stop before discovery if any check fails. Discovery and
held-out share one four-hour production deadline. A finite null result is
valid. Validation must not weaken a frozen score, cohort, selection, or gate.
