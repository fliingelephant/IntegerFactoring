# F04 full column-matroid run manifest

Approach-family ID: `F04_full_column_matroid_kill`.

## Permitted inputs

Before discovery, the agent read `AGENTS.md`, the computation rules in
`PROMPT.md`, and only `experiments/F04_joint_matroid_kill/RESULT.md` plus its
`RUN_MANIFEST.md` for prior experimental context.  Work and new outputs were
confined to this fresh directory.  No canonical file was edited and no commit
was created.

## Runs

Every mathematical run used a named source fixed in a pre-run SHA-256
manifest, a hard timeout, a combined log, retained outputs, and a failure
policy.

| Run | Hard timeout | Purpose | Outcome | Combined log |
| --- | ---: | --- | --- | --- |
| 001 | 1,800 s computation; 600 s audit | Directly form all global rows, solve both local systems, scan all entries and all `2x2` minors, directly certify the first mismatch, then parse/audit artifacts | exit 0; total computation 41.053 s; two mismatches | `logs/run_001_combined.log` |
| 002 | 600 s certification; 120 s audit | Directly compute both local exchanged determinants for every mismatch, CRT, gcd, and independently audit the table | exit 0; both certificates give `199999991` | `logs/run_002_combined.log` |
| 003 | 180 s | Independent complete `2x2` rescan with a different enumeration order and byte comparison | exit 0; exact agreement | `logs/run_003_combined.log` |
| 004 | 120 s | Optional final artifact packaging | exit 1; malformed shell redirection, failure preserved; no mathematical artifact affected | `logs/run_004_combined.log` |
| 005 | 120 s | Corrected self-excluding final artifact manifest | exit 0; all immutable manifests and final artifacts verified | `logs/run_005_combined.log` |
| 006 | 120 s | Refresh the self-excluding final hash after explicitly adding the run-004 disclosure to `RESULT.md` | exit 0; earlier hashed evidence unchanged | `logs/run_006_combined.log` |

Run 001 timings were: 29.3528 seconds for direct global formation, 3.82151
and 3.73816 seconds for the two local solve-and-check stages, and 0.196863
seconds for the parallel exhaustive `2x2` scan.  Its exact counts and
certificate are in `outputs/summary.json`; `outputs/audit.json` passed.

## Hash and output locations

* `manifests/run_001.inputs.sha256` fixes the primary source, scripts, plan,
  parameters, and executable before execution.
* `manifests/run_001.primary_outputs.sha256` fixes the global matrix, both `C`
  matrices, both zero-pattern tables, and summary before the audit.
* `manifests/run_002.inputs.sha256` and `run_002.outputs.sha256` fix the
  all-certificate reconstruction.
* `manifests/run_003.inputs.sha256` and `run_003.outputs.sha256` fix the
  independent exhaustive rescan.
* `manifests/final_artifacts.sha256` is the corrected, self-excluding final
  artifact list refreshed by run 006.  It excludes itself and the active
  run-006 log/failure paths, whose contents cannot be stable while the manifest
  is being generated; it includes the preserved run-004 log and failure file.
* `outputs/global_matrix.bin`, `C_p.bin`, and `C_q.bin` retain the exact dense
  inputs to the scans.
* `outputs/two_by_two_zeros.csv` is the complete union of both local zero
  patterns; `two_by_two_zeros_rescan.csv` is its independent identical copy.
* `outputs/all_exchange_certificates.csv` retains both exact global
  certificates.

There were no failed mathematical runs and no timeout dispositions.  Run 004's
optional packaging stage failed because `256>` was parsed as a file-descriptor
redirection, leaving `shasum -a` to parse `FAILURE_DISPOSITIONS.md` as the
numeric option.  Its plan, combined log, and failure file are retained and are
not mathematical evidence; run 005 corrected only that shell spacing under a
new input manifest.  Run 006 only refreshed the self-excluding final hash after
this disclosure was added to the result.  Separately, one
pre-manifest compilation of the run-002 certificate source failed because a
single `auto` declaration mixed vector types; the compiler log is retained as
`logs/build_run_002.log`.  The source was corrected, successfully rebuilt in
`logs/build_run_002_attempt_002.log`, and only then frozen in the run-002 input
manifest.  It did not affect any mathematical output.

## Evidence status and limitations

The scan and certificates are self-audited exact finite evidence.  The
zero-pattern completeness was recomputed by a separate source and loop order,
and every reported exchange determinant was directly evaluated over both
fields.  This has not received a fresh hostile-agent, different-model-family,
or human audit.  The factor-free Berkowitz procedure is proved as the global
evaluation route but was not executed at dimension 2,942; the retained numeric
certificates were computed with the known factors and CRT, as stated in
`RESULT.md`.
