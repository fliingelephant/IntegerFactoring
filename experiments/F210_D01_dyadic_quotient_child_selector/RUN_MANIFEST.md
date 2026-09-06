# F210-D01 run manifest

## Status

Completed on 2026-08-13. The exact frozen source and runner were used once.
The process exited successfully after 108.76 seconds. There was no retry,
source change, truncation, or alternate workflow.

This is finite discovery and counterexample evidence. It is not an
unbounded factoring theorem or lower bound.

## Frozen inputs

| Artifact | SHA-256 |
|---|---|
| `PREREGISTRATION.md` | `e1c1537ba752ba4bf44eb23d5dcaabdb25b51270addcdc25a296c730443a2349` |
| `scripts/F210_D01_dyadic_quotient_selector.py` | `32d0b4f8ad5141433e7f6d547242620df421f53702ade39d27587ba2079e5648` |
| `scripts/run_F210_D01_remote.sh` | `b35c5b9200784ba0ff9f2029dd2c3d55ec5e7b27e025e57b05d63889bf9d223c` |
| `PRELAUNCH_MANIFEST.md` | `2ca496aae1a51068f9eabbce4f12ba08fd1f3642448aa95cb1d3e9611075a62b` |

All four hashes were checked locally and after remote staging. The runner
independently checked the source hash before its preflight.

## Remote provenance and preflight

- SSH alias: `seetacloud`.
- Remote directory: `/root/IntegerFactoring_F210/F210-D01`.
- Runtime: `/root/miniconda3/bin/python`.
- Python: 3.12.3.
- SymPy: 1.14.0.
- Timeout: 1,800 seconds.
- Concurrency: one Python process and no workers.
- Address-space cap: 8 GiB.

The remote directory was absent before staging. The frozen runner reported:

- 32 logical CPUs;
- one-minute load 57.74, below the frozen `2*cpu_count` abort threshold;
- 385,787,972 KiB available memory; and
- 22,583,356 KiB free disk.

The preflight passed. The process emitted its `complete` event and exited
with status zero.

## Exact invocation

The frozen runner invoked:

```text
timeout 1800 /root/miniconda3/bin/python \
  /root/IntegerFactoring_F210/F210-D01/scripts/F210_D01_dyadic_quotient_selector.py \
  --output /root/IntegerFactoring_F210/F210-D01/output/F210-D01.json \
  --rows /root/IntegerFactoring_F210/F210-D01/output/F210-D01.rows.jsonl.gz \
  --train-count 2000 \
  --holdout-count 1000 \
  --small-p-limit 500
```

The deterministic ordered-pair hashes emitted before child construction
were:

| Cohort | SHA-256 |
|---|---|
| train | `c31c98809eaa286536a67ae03e0bef13c84844e099c06346bb161f647df4c39d` |
| holdout | `3f78983e876a78f00f0f48c0abe126f75971a3cfd6996cba0cf50baaf65f4715` |
| exhaustive-small | `d1329f7c4efe1337b4cf923cb960520ff71bb828fce963d9aa427ebe72c6f05e` |

## Output artifacts and integrity

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `logs/F210-D01.log` | 8,441 | `a6cb772d20a60ed90a0e37f84ee077db1ccd7b36af782e53fe2091e1f9d35ac7` |
| `output/F210-D01.json` | 596,523 | `7e5e62a0d9012ad8ad57ea9ed6f44d4591610e0cb9cff457ecf4f2e1197f0a16` |
| `output/F210-D01.rows.jsonl.gz` | 22,752,107 | `8ad41104ae3873c24c89a2fb9303d54344a197bc6611c04722bb56b64adafabe` |

The remote and local hashes and byte counts agree. Local `gzip -t` passed.
The compressed JSONL contains 24,762 rows:

- 11,357 training stage rows;
- 8,670 holdout stage rows; and
- 4,735 exhaustive-small stage rows.

The recursion-cohort row counts were:

| Split | early unsafe | late safe |
|---|---:|---:|
| train | 6,242 | 5,115 |
| holdout | 4,555 | 4,115 |
| exhaustive-small | 3,047 | 1,688 |

## Leakage and scope checks

- `public_stage` received only `N,t,u`.
- Hidden `p,q` generated the promised prefix and target bit only after the
  public factorization and action transcript existed.
- All stages from one input remained in the same train or holdout split.
- Action exits were removed from selector fitting and scoring by a public
  predicate.
- One rule was selected separately for each preregistered recursion cohort
  on training data before holdout scoring.
- No per-stage rule was selected.
- Early four-child recursion remains diagnostic only. No QP claim is made
  for it.
- The valid one-child decrement recurrence remains outside the null's scope.

No durable ledger was edited as part of result preparation.
