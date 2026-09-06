# F259-D02 static validation

Status: **PASS for static preparation; target execution pending.**

No C++ binary or cohort was executed. The checks below are source-level or
shell-parse checks.

## Preservation

The V1 hashes were reauthenticated after V2 preparation:

```text
PREREGISTRATION.md       0b162d3f0b8c653483a3b92e5106b2b60b7066fa464366e9654163182198a014
ALGEBRA.md                7f5c1679816eb57e9810ce112f93c97ed0edef136f710f22d91596287e0cefb8
symbolic_search.cpp       2b8c941782cfa10aeb3598a558c6a9008a9a98534933ca58c4e94d628be9a145
remote_run.sh             77be4b41f8d414819bc0137f723309804e63fc193556f0e5c1520b7b7fd83e45
FROZEN.sha256             f876baafab99508e900b3fea8d65a5416118e756eb9dd5987d79786f1d101ead
HOSTILE_PRERUN_AUDIT.md   ef242ae9fb611f7d47fd3fb599f6ce07c34171fc4bc07d96c362ae16a153cb75
```

## Repair trace

- Family 20 inserts the exact formula `D*c*(2*z+c*N)`. It inserts zero when
  `c=0`.
- Family 22 evaluates the displayed cubic or quintic core directly for every
  admitted composition. The checked identity is `E=4*D*c^2*core`; no division
  by `c` occurs. Both target-15 routes are present whenever `15*j` is in the
  window.
- Identity columns are exactly the six real plus six imaginary additive
  cocycle terms. The source ranks the 96-by-12 matrix and enumerates all
  `3^12` ternary vectors with explicit zero rejection and sign normalization.
- All four public source screens call the same certificate recorder. The
  first cleanup certificate has priority over any earlier grammar certificate.
  The source aborts if `cleanup_events>0` but the first certificate is empty
  or lacks the cleanup prefix. The pending self-test includes an explicit
  grammar-certificate-to-cleanup-certificate priority control.
- Every prime, safe-prime, and cohort retry path has an explicit bound.
- The 22-family and 255-word formulas and sparse edge/triple caps are
  unchanged except for the frozen V2 semantic repairs.
- The TSV schema has `14 + 22*5 + 255*2 = 634` columns.
- Family summaries have `7*3*22 = 462` rows. Word summaries have
  `7*3*255 = 5,355` rows.
- The predicted uncompressed output is 494,927,872 bytes, below 1 GiB.
- The exact largest-input static insertion bound remains 176,384, and the
  exact production word-score count remains 1,795,200.

## Runner checks

`bash -n remote_run.sh` passes. The runner requires a fresh PASS audit,
authenticates frozen hashes before work, and refuses nonempty output or log
directories. It checks command line,
working directory, and executable path for every
F258/F260/F261/F263/F264 process. It applies those checks before, during, and
after compile, self-test, benchmark, describe, production, and compression.
Report and compression validation use the same monitor. All monitored modes
use `nice 15`, a 4 GiB virtual-memory limit, and a timeout. Production report
validation and compression share the four-hour deadline.
Output and log bytes are monitored below 1 GiB, with 1 MiB reserved for the
final manifest. TSV validation independently checks cleanup-certificate,
cleanup-free, direct-hit, and strict-row consistency before compression.

## Deferred checks

The local Mac has no Boost Multiprecision header. F258 is active on the target,
and F259-D02 declares it incompatible. Therefore C++ compilation, self-test,
benchmark, and every cohort remain unopened. The first target action must be a
fresh-audit-approved invocation of the frozen runner after F258 ends.
