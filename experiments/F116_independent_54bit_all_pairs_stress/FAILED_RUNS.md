# F116 failed runs

## 2026-08-08 03:12:23Z — sandbox denied the process-pool system query

The registered source selected all six cases, then stopped before launching a
batch worker. Python's process-pool constructor called
os.sysconf("SC_SEM_NSEMS_MAX"), and the sandbox returned
PermissionError: [Errno 1] Operation not permitted.

The exact log and last checkpoint are:

- RUN_FAILED_20260808T031223Z_EXIT_1.log;
- OUTPUT_FAILED_20260808T031223Z_EXIT_1.json.

They contain no all-pairs mathematical result. The retry uses the identical
source, selected corpus rule, worker count, and timeout outside this sandbox
restriction.

## 2026-08-08 03:44:26Z — Python endpoint factorization timed out

The identical retry completed the registered selection in 263.20 seconds and
selected all six cases. It then spent the rest of the 1,800-second hard
timeout inside the three factor-assisted batch workers. No worker completed a
case, so this run gives no all-pairs result.

The exact log and last checkpoint are:

- RUN_FAILED_20260808T034426Z_TIMEOUT.log;
- OUTPUT_FAILED_20260808T034426Z_TIMEOUT.json.

The next attempt keeps the corpus rule, source order, decoder, and timeout.
It replaces the candidate's pure-Python Pollard factorizer with the Sage/Pari
endpoint factorizer that the independent F115 audit already used. This is a
new named source and run, not a reinterpretation of the timeout.

## 2026-08-08 03:53:10Z — Sage retry was killed after one completed case

The Sage/Pari retry completed the registered selection and one full batch.
For the first selected modulus, it provisionally found a cross-layer parity
dependency after 177 public pair-menu entries. The dependency used 6,486
relations and gave the factor 159,999,943. The parent process was then killed
with signal 9 before a second case completed. The overall run therefore
failed and the provisional case is not promoted.

The exact checkpoint and log are:

- SAGE_OUTPUT_FAILED_20260808T035310Z_EXIT_137.json;
- SAGE_RUN_FAILED_20260808T035310Z_EXIT_137.log.

The next retry must isolate one modulus in one process. It must export the
exact dependency support. A separate factor-free replay must verify that
support before the case can count as mathematical evidence.

## 2026-08-08 03:59:17Z — isolated Sage replay hit the sandbox cache rule

The first isolated retry stopped during Sage import. Sage tried to write its
lazy-import cache under `.sage`, outside the workspace write boundary. The
run produced no candidate output. Its files are:

- SINGLE_CASE_OUTPUT_FAILED_20260808T035917Z_EXIT_1.json;
- SINGLE_CASE_RUN_FAILED_20260808T035917Z_EXIT_1.log.

## 2026-08-08 04:01:03Z — isolated Sage replay was killed for memory use

The same isolated source ran outside the sandbox but was killed with signal 9
after 57.12 seconds. It produced no support export. This is consistent with
the dense online decoder's large combination state. It is an implementation
failure, not a null mathematical result. Its files are:

- SINGLE_CASE_OUTPUT_FAILED_20260808T040103Z_EXIT_137.json;
- SINGLE_CASE_RUN_FAILED_20260808T040103Z_EXIT_137.log.

Do not retry this dense implementation while the independent F111 decoders
are active. A retry must either run with memory available or replace dense
combination masks with a memory-bounded exact representation.

## 2026-08-08 04:52:42Z — five registered-case wrappers hit the Sage cache rule

The first remaining-corpus run launched all five cases in sequence. Every
case stopped during Sage import because Sage tried to write its lazy-import
cache under the non-writable user cache directory. No source relation was
generated. This is one repeated environment failure, not five mathematical
nulls.

The combined checkpoint and log are:

- SPARSE_DAG_REMAINING_OUTPUT_FAILED_20260808T045242Z_ENV.json;
- SPARSE_DAG_REMAINING_RUN_FAILED_20260808T045242Z_ENV.log.

The five empty per-case checkpoints are also preserved with names of the form
`SPARSE_DAG_CASE_*_FAILED_20260808T*_EXIT_1.json`. The corrected retry changed
only `DOT_SAGE`, which now points to a writable experiment-local cache. It
kept the same corpus, candidate, order, and 600-second per-case timeout.
