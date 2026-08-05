# Run manifest

This directory is an independent reconstruction.  It does not read or modify
the project's canonical proof/status files or the earlier `F10_autkill` and
`F10_aut_audit` experiment trees.

## Run V1

- Source: `verify.py`
- Runner: `run.sh`
- Command: `./experiments/F10_aut_reconstruct/run.sh`
- Wall-clock timeout: 120 seconds, enforced by
  `/opt/homebrew/bin/timeout`
- Dependencies: Python 3 standard library only
- Primary output: `verification.json`
- Combined stdout/stderr and disposition log: `run.log`
- Expected work: enumerate 42,875 candidate coefficient triples for the
  largest example, plus all monic cubics over four small prime fields

Failure dispositions are explicit:

- exit 0 and `status=PASS`: accept the finite checks recorded in the JSON;
- exit 124 and `status=TIMEOUT`: retain the log, treat the run as providing no
  evidence, and report the timeout rather than extrapolating;
- any other nonzero exit and `status=FAIL`: retain the log and output (if any),
  diagnose the named source, and do not use partial results.

The computations are finite checks only.  The general statements in
`RESULT.md` are proved algebraically rather than inferred from these runs.
