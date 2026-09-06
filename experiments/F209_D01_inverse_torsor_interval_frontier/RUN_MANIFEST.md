# F209-D01 run manifest

## Status

Completed remotely on 2026-08-13.  The frozen runner exited with code zero.
No timeout, representative-cap abort, preflight abort, or integrity abort
occurred.

## Frozen inputs

The local hashes were recomputed before staging and matched the prelaunch
manifest.  The same hashes were recomputed remotely before launch.

| File | SHA-256 |
|---|---|
| `PREREGISTRATION.md` | `09fab369dc9519dfb07c3f73c436e9995e9269696cb9a6bed9d5b446689ddf3d` |
| `scripts/F209_D01_inverse_torsor_frontier.py` | `61b13495b8455b2697b983668602829053c297a8fc68e08188966ea824634d6a` |
| `scripts/run_F209_D01_remote.sh` | `00bbe754566d26d9757af39dbb82791ba955f3ac856266a187e79f187221c03e` |
| `PRELAUNCH_MANIFEST.md` | `f1e6a295c48abb2b27d027496a5ddacf94df7f408542f9717197099cd0363238` |

The runner independently checked the source hash before its preflight.

## Remote identity and exact launch

- SSH alias: `seetacloud`.
- Remote root: `/root/IntegerFactoring_F209/F209-D01`.
- Source used:
  `/root/IntegerFactoring_F209/F209-D01/scripts/F209_D01_inverse_torsor_frontier.py`.
- Runner used:
  `/root/IntegerFactoring_F209/F209-D01/scripts/run_F209_D01_remote.sh`.
- Launch command:

  ```text
  ssh seetacloud bash /root/IntegerFactoring_F209/F209-D01/scripts/run_F209_D01_remote.sh
  ```

The frozen runner invoked one process under `timeout 1800`, imposed
`ulimit -v 8388608`, and used exactly these arguments:

```text
--train-count 256
--holdout-count 64
--small-p-limit 1000
--max-p-representatives 2000000
```

No fallback, changed threshold, changed ordering, changed dataset, restart,
or second run was used.

## Preflight and runtime

The preflight passed with:

- 32 CPUs;
- one-minute load average `56.15`, below the registered limit `64`;
- `385835884` KiB available memory;
- `22588272` KiB free disk at the remote root; and
- no visible CPU-intensive process other than the experiment after launch.

Runtime versions were:

- Python `3.12.3`;
- SymPy `1.14.0`.

The recorded experiment runtime was `243.796` seconds.  During the largest
rows, the process used one CPU and approximately 590 MiB resident memory.

## Dataset identity

The deterministic pair hashes emitted before row evaluation were:

| Cohort | Rows | Identity |
|---|---:|---|
| `paired_train` | 256 | seed `20501`, bits 12--17, 503 attempts, `be10d5184ea0024f3f05ea435da50a4c6f7464ed447a9da534f32ee3bd7edfdf` |
| `paired_holdout` | 64 | seed `20502`, bits 18--23, 119 attempts, `781d8bfba98edf7c95e7c51f6370bc439144846acf4d07fcb3d387e7af1c25aa` |
| `small_exhaustive` | 5,570 | `p<=1000`, `0068c5479b7ca7b1054142d682376c6f001f6fb2fcdc9d582025cdceea2317c3` |
| `frozen_witnesses` | 4 | `61b12793dae6e52ab8b78a252941e6c2857f0cb7079453985b9259c6affc5741` |

These are the registered exact F205-prefix generators, exhaustive loop, and
frozen list.  The total expected row count was 5,894.

## Preserved artifacts

Remote and copied-local hashes matched exactly.

| Artifact | Remote path | Bytes | SHA-256 |
|---|---|---:|---|
| log | `/root/IntegerFactoring_F209/F209-D01/logs/F209-D01.log` | 8,499 | `dddbec6ba76154ab55040f242acef3139a0a0057ac017c2acb08d62ecd3a8f32` |
| summary | `/root/IntegerFactoring_F209/F209-D01/output/F209-D01.json` | 17,153 | `a75121324d320756847945bbbd97f93b914ec8476c99255464837b13d2563a5c` |
| rows | `/root/IntegerFactoring_F209/F209-D01/output/F209-D01.rows.jsonl.gz` | 4,946,916 | `4684356503f785d878a79ace81af1bbf621bb2a0fa55c0b1ea51de25e0fb78b0` |

Local copies are under `logs/` and `output/` in this experiment directory.

## Post-copy verification

The following checks passed:

1. local and remote SHA-256 values agree for all three artifacts;
2. `gzip -t output/F209-D01.rows.jsonl.gz` exits successfully;
3. decompression gives exactly 5,894 JSONL rows;
4. the summary is valid JSON and repeats all four preregistered dataset
   identities;
5. cohort row counts sum to 5,894;
6. 5,858 rows enter the primary F207 torsor and 36 take the public
   `gcd(E,N)` exit;
7. every primary row retains its hidden audit branch, reaches final frontier
   width one, and gives the correct public singleton-product certificate;
8. the summary reports zero integrity failures and no `n^4` exceedance; and
9. the log ends with `classification=strong_finite_geometry_lead` and
   `integrity_failures=0`.

## Staging note

The first copy command also placed redundant byte-identical source and runner
copies in the remote root.  The files under the registered `scripts/` paths
were then copied and hash-verified.  Only those registered `scripts/` files
were executed.  The redundant root copies were not inputs and were not
modified or deleted.

No durable-ledger file was edited by this run owner.
