# F04 reconstruction run manifest

Approach-family ID: `F04_reconstruct`.

All evidentiary runs used a named source, an external timeout, a dedicated log,
and a dedicated output path.  Sage used `DOT_SAGE=/tmp/f04_reconstruct_sage`
because the sandbox does not permit writes to the default Sage cache directory.

## Evidentiary and diagnostic runs

| ID | completed (Asia/Hong_Kong) | named source | timeout | output | log | exit | disposition |
|---|---|---|---:|---|---|---:|---|
| B1 | 2026-08-05 23:59:56 | `benchmark_direct.sage` (initial revision) | 180 s | `output/benchmark_q_local.json` (empty) | `logs/benchmark_q_local.log` | 1 | Polynomial computation completed, but JSON serialization of Sage integer `a` failed; rejected as evidence. |
| B2 | 2026-08-06 00:00:17 | `benchmark_direct.sage` (second revision) | 180 s | `output/benchmark_q_local_attempt2.json` (empty) | `logs/benchmark_q_local_attempt2.log` | 1 | `r` and `zero_count` were converted, but Sage integer `a` still failed serialization; rejected as evidence. |
| B3 | 2026-08-06 00:00:38 | `benchmark_direct.sage` (current revision) | 180 s | `output/benchmark_q_local_attempt3.json` | `logs/benchmark_q_local_attempt3.log` | 0 | Successful one-shift timing probe; diagnostic only. |
| F1 | 2026-08-06 00:04:22 | `reconstruct_f04.sage` (pre-encoder-fix revision) | 900 s | `output/full_attempt1/` | `logs/full_run_attempt1.log` | 1 | Complete order table was written, then first coefficient row failed JSON serialization; partial artifacts preserved, rejected as full evidence. |
| F2 | 2026-08-06 00:06:15 | `reconstruct_f04.sage` (pre-status-vocabulary revision; recorded SHA-256 `b67070f75d5c89a80b54db254610db93c9da23e5a02a18b016102669493b5de5`) | 900 s | `output/full_attempt2/` | `logs/full_run_attempt2.log` | 0 | Successful exhaustive run, but the source was subsequently edited to replace the non-vocabulary metadata value `verified`; retained as reproducibility evidence, not presented as reproduced by the current source. |
| A1 | 2026-08-06 00:07:40 | `audit_artifacts.py` (pre-status-vocabulary revision) | 60 s | `output/artifact_audit.json` | `logs/artifact_audit.log` | 0 | Successful structural/hash audit of F2 artifacts. |
| F3 | 2026-08-06 00:11:46 | `reconstruct_f04.sage` (current revision) | 900 s | `output/full_attempt3/` | `logs/full_run_attempt3.log` | 0 | Clean end-to-end rerun after the metadata fix; authoritative primary evidence. Its deterministic order and coefficient artifacts exactly match F2. |
| A2 | 2026-08-06 00:11:50 | `audit_artifacts.py` (current revision) | 60 s | `output/artifact_audit_attempt2.json` | `logs/artifact_audit_attempt2.log` | 0 | Successful structural/hash audit of authoritative F3 artifacts. |

The exact commands were:

```text
DOT_SAGE=/tmp/f04_reconstruct_sage timeout 180 sage experiments/F04_reconstruct/benchmark_direct.sage 199999991 100000007 > experiments/F04_reconstruct/output/benchmark_q_local.json 2> experiments/F04_reconstruct/logs/benchmark_q_local.log

DOT_SAGE=/tmp/f04_reconstruct_sage timeout 180 sage experiments/F04_reconstruct/benchmark_direct.sage 199999991 100000007 > experiments/F04_reconstruct/output/benchmark_q_local_attempt2.json 2> experiments/F04_reconstruct/logs/benchmark_q_local_attempt2.log

DOT_SAGE=/tmp/f04_reconstruct_sage timeout 180 sage experiments/F04_reconstruct/benchmark_direct.sage 199999991 100000007 > experiments/F04_reconstruct/output/benchmark_q_local_attempt3.json 2> experiments/F04_reconstruct/logs/benchmark_q_local_attempt3.log

DOT_SAGE=/tmp/f04_reconstruct_sage timeout 900 sage experiments/F04_reconstruct/reconstruct_f04.sage --output-dir experiments/F04_reconstruct/output > experiments/F04_reconstruct/output/full_run_stdout.jsonl 2> experiments/F04_reconstruct/logs/full_run.log

DOT_SAGE=/tmp/f04_reconstruct_sage timeout 900 sage experiments/F04_reconstruct/reconstruct_f04.sage --output-dir experiments/F04_reconstruct/output/full_attempt2 > experiments/F04_reconstruct/output/full_attempt2/run_stdout.jsonl 2> experiments/F04_reconstruct/logs/full_run_attempt2.log

timeout 60 python3 experiments/F04_reconstruct/audit_artifacts.py experiments/F04_reconstruct/output/full_attempt2 > experiments/F04_reconstruct/output/artifact_audit.json 2> experiments/F04_reconstruct/logs/artifact_audit.log

DOT_SAGE=/tmp/f04_reconstruct_sage timeout 900 sage experiments/F04_reconstruct/reconstruct_f04.sage --output-dir experiments/F04_reconstruct/output/full_attempt3 > experiments/F04_reconstruct/output/full_attempt3/run_stdout.jsonl 2> experiments/F04_reconstruct/logs/full_run_attempt3.log

timeout 60 python3 experiments/F04_reconstruct/audit_artifacts.py experiments/F04_reconstruct/output/full_attempt3 > experiments/F04_reconstruct/output/artifact_audit_attempt2.json 2> experiments/F04_reconstruct/logs/artifact_audit_attempt2.log
```

After F1 failed, its output files were moved without modification into
`output/full_attempt1/`, and its log was renamed `logs/full_run_attempt1.log`, so
F2 could not overwrite them.

Current source hashes:

- `reconstruct_f04.sage`:
  `4c57ce69108de5df3da98428a624e086d817c5d0cabd7c0bb3daa8d99889d3ed`;
- `benchmark_direct.sage`:
  `e709a3b6d7e8d09141da5d8c02da5d4fab9d9824227c36d425ba7f16c2e78bcf`;
- `audit_artifacts.py`:
  `7428e1308656302460f6dd9b67be4793cac608e2580f33f88c2184706c7b58d2`.

Primary F3 hashes:

- `output/full_attempt3/summary.json`:
  `24cfd12c03d28e01b75338f896a87084f17c0d709a825928a0dcd10a4c7511d4`;
- `logs/full_run_attempt3.log`:
  `07c3a94239463cec8bb64f89e078610dbc678c7a7d40bb04df86ba05d9a27dba`;
- `output/full_attempt3/orders_2_through_2953.csv`:
  `e52e0742358504d94a34024f643b83e3334dff252425fe15a3f1f6833430b07d`;
- `output/full_attempt3/local_coefficients_mod_p.jsonl`:
  `0ea82a9efa81cf1e8b1e19224c2c51cbd8320cee5bd0be670ad95744193a8df0`;
- `output/full_attempt3/local_coefficients_mod_q.jsonl`:
  `18962035991d6e81f3c08218f9559cd998bd39689888b7349870373499883672`.

The F2 and F3 order-table SHA-256 values are identical, as are both local row-file
SHA-256 values and both full coefficient-stream SHA-256 values.  This is the
reproducibility check across the pre- and post-metadata-fix runs.

## Disqualified pre-source probes

Before the named sources were created, two small inline Python probes were issued:
one printed the proposed product and floating-point parameter estimates; the
other attempted to import unavailable `sympy` and failed immediately.  They had
no timeout wrapper and no preserved output/log files, so they did not comply with
the computation rule and are disqualified.  No result in `RECONSTRUCTION.md`
depends on either probe; every claimed value was recomputed by F3 from the named
source under timeout.  They are recorded here rather than silently omitted.

Their exact command forms were `python3 -c '<product and floating-point probe>'`
and `python3 - <<'PY' <sympy order probe> PY`; the second terminated at import.
Because neither had a named source or file output, no source/log/output path is
claimed for them.

After A2, `audit_artifacts.py output/full_attempt3` was also invoked once directly
as an interactive display check, without the external timeout and redirection.
Although it printed the same passing audit, that invocation is disqualified and
is not evidence.  A2 is the preserved, timeout-bounded execution of the identical
current source and supplies the claimed output and log.
