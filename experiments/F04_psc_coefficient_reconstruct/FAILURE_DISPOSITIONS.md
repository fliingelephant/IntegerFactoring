# Failure dispositions

The fixed policy for `run_001` is recorded before execution in
`manifests/run_001.plan.json`:

* exit status zero is required at every stage;
* timeout status or any other nonzero status creates
  `outputs/run_001_<stage>.failure.txt`;
* the runner stops immediately, preserves the failed artifacts and input
  manifest, and does not infer any unverified remainder degree or determinant
  status;
* any source correction requires a new immutable run manifest rather than
  relabeling the failed run.

Stage outcomes and any actual dispositions are recorded in `AUDIT.md` after
execution.

