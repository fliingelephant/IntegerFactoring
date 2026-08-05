# Runbook

All commands are launched from this directory.  No mathematical program is
passed through standard input or an inline `-c` expression.

1. Compile the three named C++ sources with `scripts/build.sh`, retaining the
   compiler log.
2. Run `scripts/prepare_run.sh`.  This hashes the fixed parameters, plan,
   sources, scripts, and executables into `manifests/run_001.inputs.sha256`
   before the finite execution.
3. Run `scripts/run_all.sh`.  It first verifies the pre-run hashes, then invokes
   each named source under the hard timeout in
   `manifests/run_001.plan.json`.  Standard output and error go to distinct
   stage logs.  A timeout or any nonzero exit writes a named failure
   disposition and stops.
4. The runner hashes all primary outputs before running the independent
   artifact parser, then hashes the final artifact set.

The global-vector generator uses the exact characteristic identity

`(X+a)^(pq) = (X^p+a)^q mod p`

and its `p,q`-swapped version, followed by coefficientwise CRT.  CRT is the
canonical isomorphism from the two field coordinates to `Z/NZ`, so this
materializes the global vector exactly.  The complete verifier opens only that
materialized binary, reduces each stored coefficient, and runs the field
checks.  A later spot audit recomputes four vectors by direct exponentiation
modulo the composite `N`, avoiding the generator's Frobenius/CRT route.

