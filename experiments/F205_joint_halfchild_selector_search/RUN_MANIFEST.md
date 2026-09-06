# F205-D01 run manifest

## Status

Completed on 2026-08-13. The run used the preregistered source and runner
without a post-launch change. It finished in 146.672 seconds under the
declared 900-second timeout.

This is finite discovery and counterexample evidence. It is not a proof of
an unbounded factoring or hardness claim.

## Frozen inputs

| Artifact | SHA-256 |
|---|---|
| `PREREGISTRATION.md` | `4c04fe00a485413c13549e1940933b79caa13c71a2b0983548a729f46eb73a85` |
| `scripts/F205_D01_joint_selector.py` | `9828866096689fc4025b3c0c251d961ccf261873e42590b0e9930217f614a993` |
| `scripts/run_F205_D01_remote.sh` | `6964b80501102fd33c298f1bba33ea2bbfd943cfa2ac82c578a69196d70f96a9` |

The launch command printed the same two source hashes from the remote copy
before it started the runner.

## Remote provenance and resource check

- SSH alias: `seetacloud`.
- Resolved host from the local SSH configuration:
  `connect.westc.seetacloud.com`, port `27673`.
- Remote work directory: `/root/IntegerFactoring_F205/F205-D01`.
- Runtime: `/root/miniconda3/bin/python`.
- Python: 3.12.3.
- SymPy: 1.14.0.
- NumPy: 2.4.6.
- Concurrency: one Python process. No worker process was used.
- Timeout: 900 seconds.

The prelaunch read-only check reported 32 logical CPUs, a load average near
56, 503 GiB total RAM, 367 GiB available RAM, and 22 GiB free disk. The
visible container had no CPU-intensive user process. The declared process
budget was below 1 GiB RAM.

## Exact command path

The local frozen source and runner were copied to

`/root/IntegerFactoring_F205/F205-D01/scripts/`.

The remote command was:

```text
cd /root/IntegerFactoring_F205/F205-D01
sha256sum scripts/F205_D01_joint_selector.py scripts/run_F205_D01_remote.sh
bash scripts/run_F205_D01_remote.sh
```

The runner invoked exactly:

```text
timeout 900 /root/miniconda3/bin/python \
  /root/IntegerFactoring_F205/F205-D01/scripts/F205_D01_joint_selector.py \
  --output /root/IntegerFactoring_F205/F205-D01/output/F205-D01.json \
  --rows /root/IntegerFactoring_F205/F205-D01/output/F205-D01.rows.jsonl.gz \
  --train-count 5000 \
  --holdout-count 2500 \
  --small-p-limit 1000
```

The runner used `set -euo pipefail`. The source emitted its `complete` event.
No failure, retry, or alternate workflow occurred.

## Output artifacts

| Artifact | Remote path | Local path | Bytes | SHA-256 |
|---|---|---|---:|---|
| log | `/root/IntegerFactoring_F205/F205-D01/logs/F205-D01.log` | `logs/F205-D01.log` | 6,217 | `edec0b6fa3ef8a7981bbf491b0b425a2f28a834dc2b474866cd012df0eca5e4f` |
| result | `/root/IntegerFactoring_F205/F205-D01/output/F205-D01.json` | `output/F205-D01.json` | 119,293 | `e9f2e4573631a1d40380bc329f3dcc2537689464471f4828dd6709d76515ad4d` |
| rows | `/root/IntegerFactoring_F205/F205-D01/output/F205-D01.rows.jsonl.gz` | `output/F205-D01.rows.jsonl.gz` | 16,795,245 | `2dbbcea5e9f66e45f77b7ba78f4dc059d489ce74e3151a8d8cbc19642bff2abe` |

The remote and local hashes agree. `gzip -t` passed. The compressed JSONL
contains 13,071 rows: 5,000 training, 2,500 holdout, 5,570 exhaustive-small,
and one separately repeated frozen F202 witness.

## Cohort and leakage checks

- Training uses smaller-factor bit lengths 12 through 17 and seed `20501`.
- Holdout uses smaller-factor bit lengths 18 through 23 and seed `20502`.
- The two factor-bit ranges are disjoint. Thus their input sets are disjoint.
- The exhaustive-small cohort has `p<=1000`, so it is disjoint from both
  random cohorts.
- The frozen `2627=37*71` row intentionally repeats its exhaustive-small row.
  It is not used to train or select a rule.
- `public_record` accepts only `N`. It constructs `B,K,E`, both child
  factorizations, every feature, every public transition, and the mixed-norm
  scan before `hidden_labels` receives `p,q`.
- Hidden factors are used only to label and verify outcomes.
- The training phase fixes the rule, orientation, and numeric threshold.
  Holdout labels are read only when the frozen rule is scored.
- The primary selector cohort excludes only public easy branches:
  `gcd(E,N)>1` and a proper factor from the fixed public transition bank.
  There were no `gcd(E,N)>1` cases in either random cohort.

The source records 10,092 raw generation attempts for 5,000 accepted training
inputs and 4,817 attempts for 2,500 accepted holdout inputs. Acceptance uses
only the declared balanced-semiprime promise and `N mod 4 == 3`.

