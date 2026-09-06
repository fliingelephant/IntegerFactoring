# F259-D02 fresh hostile pre-run audit request

Status: **UNOPENED — PASS required before any target invocation.**

Audit the frozen F259-D02 V2 packet independently and from first principles.
Use static inspection only. Do not compile or execute `symbolic_search.cpp`.
Do not invoke `remote_run.sh`, access the remote host, generate inputs, or open
any discovery or held-out cohort.

First authenticate the observed SHA-256 of `FROZEN.sha256` supplied with the
audit assignment. Then authenticate every entry in that file. Also confirm
that the following V1 bytes and its FAIL audit remain unchanged:

```text
PREREGISTRATION.md       0b162d3f0b8c653483a3b92e5106b2b60b7066fa464366e9654163182198a014
ALGEBRA.md                7f5c1679816eb57e9810ce112f93c97ed0edef136f710f22d91596287e0cefb8
symbolic_search.cpp       2b8c941782cfa10aeb3598a558c6a9008a9a98534933ca58c4e94d628be9a145
remote_run.sh             77be4b41f8d414819bc0137f723309804e63fc193556f0e5c1520b7b7fd83e45
FROZEN.sha256             f876baafab99508e900b3fea8d65a5416118e756eb9dd5987d79786f1d101ead
HOSTILE_PRERUN_AUDIT.md   ef242ae9fb611f7d47fd3fb599f6ce07c34171fc4bc07d96c362ae16a153cb75
```

Audit at least these V2 surfaces:

1. the Pell quotient, tangent, multiplication-carry, determinant, resultant,
   same-discriminant factorization, and both second-curvature identities;
2. exact divisibility assertions and exact public common-`N` stripping;
3. all 22 hard-coded family constructors, especially exact `c=0` behavior
   for families 20--22 and both target-15 core routes;
4. all sparse row, pair, cross-discriminant, triple, and composition scopes,
   their deduplication, window tests, caps, and static insertion projection;
5. the exact 12-term cocycle matrix, modular rank calculation, exhaustive
   ternary enumeration, sign normalization, four expected decoys, two
   primitive controls, and 64 exact disjoint holdouts;
6. the 255 non-adaptive word shapes, normalized syntax descriptions, exact
   modular exponentiation and residual gcd scores, and discovery/held-out
   firewall;
7. all four public cleanup screens, cleanup-certificate priority and scope,
   grammar certificates on cleanup-free direct hits, strict-row semantics,
   and per-family zero/unit/stripped-power/direct counts;
8. deterministic prime, safe-prime, consecutive-prime, cohort retry bounds,
   bit lengths, balance, global per-size distinctness, exact cohort counts,
   labels, and the total of 7,040 inputs;
9. family and word aggregation, split labels, quantiles, anomaly thresholds,
   exact TSV/JSON dimensions, stream-close checks, validation, compression,
   and final manifest preservation;
10. absolute F258/F260/F261/F263/F264 checks through command line, working
    directory, and executable path before, during, and after every monitored
    mode;
11. CPU, memory, disk, load, niceness, virtual-memory, timeout, shared
    deadline, projected-runtime, live-output, final-output, and failure-status
    gates.

Treat `STATIC_VALIDATION.md` as a claim to verify, not as audit evidence.
Target compilation, self-test, benchmark, and production are intentionally
pending because F258 is active. Their pending state is not a PASS substitute.

Write only `HOSTILE_PRERUN_AUDIT.md` in this V2 directory. After any Markdown
heading, make its first substantive line `Verdict: PASS` or `Verdict: FAIL`.
List authenticated hashes and decisive findings. After the file is closed,
send its SHA-256 to the audit coordinator. Do not repair any artifact. Do not edit V1,
any frozen V2 input, or any durable ledger.
