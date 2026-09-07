# Resource budget

The integer-only pilot is expected to use under 5 seconds and 64 MiB.
It has a 30-second signal alarm and an outer 35-second timeout. Small
graphs are enumerated only as reference data. No hidden factor selects a
public action in the P237 reduction.

Preflight: 71 percent available memory; no swapins or swapouts; load
2.19/2.14/2.13. The process inventory showed no competing numerical job.
Two macOS indexing services used approximately 156 percent combined CPU.
The load query needed the same read-only command outside the sandbox;
that query was approved and succeeded. The bounded pilot was retained.

Source: pilot.py. Expected artifacts: output.json, run.log, and status.json.
The output records runtime, peak RSS, check counts and the exact witness.
