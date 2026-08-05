# Run manifest

## Scope

This directory is a proof-blind reconstruction from the supplied bare target
statement.  No contents were read from `FAILED.md`, `PROVED.md`, `REGISTRY.md`,
`notes/Progress.md`, `experiments/F09_phasekill`, or
`experiments/F09_phase_audit`.  No canonical file was edited.

## Sources and artifacts

| File | Role |
|---|---|
| `verify_phase_reconstruction.py` | Dependency-free finite verifier and counterexample search |
| `run_verification.py` | Subprocess runner enforcing the hard timeout and recording all streams/status |
| `certificate_output.json` | Complete deterministic standard output from the verifier |
| `run.log` | Command, UTC timestamps, elapsed time, timeout, exit code, and complete standard error |
| `timeout_status.txt` | Minimal machine-readable timeout and exit status |
| `RESULT.md` | Self-contained proofs, limits, counterexamples, and finite certificate |

## Reproduction

Run from the repository root:

```sh
python3 experiments/F09_phase_reconstruct/run_verification.py
```

The runner executes:

```text
/opt/homebrew/opt/python@3.14/bin/python3.14 /Users/zhou/autoresearch/IntegerFactoring/experiments/F09_phase_reconstruct/verify_phase_reconstruction.py --prime-bound 2000
```

The child-process timeout is 60 seconds.  The recorded run started at
`2026-08-05T17:00:01.007654+00:00`, finished at
`2026-08-05T17:00:01.464544+00:00`, and took 0.456890 seconds.  It did not time
out, returned exit code 0, and produced no standard error.

## Environment

- Python: `Python 3.14.5`
- OS: `Darwin 25.6.0`, arm64
- Third-party Python packages: none

## Checked search space

- Character classification: exhaustive for `ell = 2, 3, 5, 7, 11`.
- Swap transcript counterexamples: enumerated at `ell = 5`.
- Cyclotomic product: every odd prime `ell < 32`, every prime `p < 2000`
  satisfying `p = 1 mod ell`, and every nonzero residue `a mod p`.
- Cyclotomic totals: 386 `(ell,p)` pairs, 357,334 values of `a`, and
  2,783,012 individual residue-symbol evaluations; no counterexample.
- `ell=3, N=91`: the three requested phases under every global root, all 72
  units, all ordered phase-pair fibers, all scalar-sum fibers, all
  unordered-multiset fibers, every root of `Phi_3`, and every pairwise
  root-difference gcd.

## SHA-256

```text
be53dca7c4abe2c4ccac4d58468c7c10975e34d685e579ecd70ffbbb1719706e  verify_phase_reconstruction.py
cbeedbc97bc94e4c24ddd62bfd97948ca73cd8a403c8aacfa0606a6cfbd3e1c0  run_verification.py
4207ab7ad7ad95716d93767d3438d38072a6a84c7a785178f1f4f6e44b2968eb  certificate_output.json
31970128ae91924ffc66f8eb2937242115d6e3d3c47c1e2c2438b37f62d8cf58  run.log
9bde2dbc606ece170c0dae84935aa719aba79381627dd058d24bbd67d8d6e02f  timeout_status.txt
ca7f7a8df075ea34e6bbac332cdc7356e4d6409ab0c567b80cb06160deab4451  RESULT.md
```

`certificate_output.json` is deterministic for a fixed source and prime bound.
The log hash changes on a rerun because UTC timestamps are recorded.
