# F116 remaining registered corpus manifest

## Boundary

This run completes the five preregistered cases not completed by the first
sparse-DAG run. It uses the exact pinned sparse candidate with only `P`, `Q`,
`N`, and the registered ordinal changed.

The result is factor-assisted discovery. Sage factors relation endpoints to
find a parity dependency. Each process then replays its advised support by
exact integer multiplication, square root, and gcd without endpoint
factorization. No independent hostile audit or proof-blind reconstruction has
checked these five supports. They are finite control evidence only.

## Result

The named command was:

```text
/opt/homebrew/bin/python3 experiments/F116_independent_54bit_all_pairs_stress/run_sparse_dag_remaining_with_timeout.py
```

Each child had a 600-second hard timeout. The complete run passed in
153.925440 seconds.

| Ordinal | N | Successful pair | Retained relations | Support | Child seconds |
| ---: | ---: | --- | ---: | ---: | ---: |
| 4 | 12,800,006,319,995,929 | (5, 32) | 800,203 | 7,826 | 31.130055 |
| 6 | 12,800,006,479,991,909 | (5, 32) | 802,610 | 7,062 | 31.013200 |
| 7 | 12,800,009,679,988,789 | (5, 31) | 776,374 | 7,130 | 30.248240 |
| 9 | 12,800,014,959,981,793 | (5, 28) | 780,808 | 7,245 | 30.689683 |
| 13 | 12,800,024,559,934,753 | (5, 28) | 793,994 | 7,013 | 30.837732 |

Together with the audited ordinal-3 case, the registered 54-bit corpus is
6/6 positive. All six frozen layers have dependencies but only global roots.
Every successful joint dependency uses both the frozen and appended source.
This does not show that recursive feedback is necessary. The appended source
is a fixed nonadaptive all-seed-pair menu.

## Preserved failure

The first named run failed before source generation because Sage tried to use
a non-writable cache. All five per-case failures, the combined checkpoint,
and the combined log remain present. The retry changed only `DOT_SAGE` to an
experiment-local writable path. The cache itself is transient and is not
evidence.

## SHA-256 pins

| File | SHA-256 |
| --- | --- |
| `stress_sparse_dag_first_case.py` | `7a65e664d9cdca422da47a5d26bd22432ce2eee5c61f8b3db5541bd348e81b84` |
| `stress_sparse_dag_registered_case.py` | `bfc1207c13237925a13e23304a6ac234d23b132831971fb1eeb13c5523d7dd55` |
| `run_sparse_dag_remaining_with_timeout.py` | `40ae4d40b56e0fdb1f1ba12f98466efe0f79211aefd994061267392c69dd54e4` |
| `SPARSE_DAG_REMAINING_OUTPUT.json` | `35191f511593dc8d01a4d5bfb146be6c919df66b9a51e8eb90d48540d954761b` |
| `SPARSE_DAG_REMAINING_RUN.log` | `b6ef16f49c0c3685eab846c535f3e414095890268d452a4ec479d8ec58ac331f` |
| `SPARSE_DAG_CASE_04_OUTPUT.json` | `d01c27d9d947a1d5fdac0a5c1765d45d42937f1be3bfdd3f2ad71d2a8bd23aa5` |
| `SPARSE_DAG_CASE_06_OUTPUT.json` | `bdb4270e16bcfdab6c5a46b631a1d805a05af80f22206489e2bf14e0f2ff5ec3` |
| `SPARSE_DAG_CASE_07_OUTPUT.json` | `b6d88b26a83c2cb82b1e82a29fd8326bff37625d6f1f60fdc3f5c6a88ce3404c` |
| `SPARSE_DAG_CASE_09_OUTPUT.json` | `6c47931f567cc8a96d6a4b1f92bf4844db46693298beec0628c57db48b99f6c2` |
| `SPARSE_DAG_CASE_13_OUTPUT.json` | `9d6755a5c88ed563ac8059109531f492a07ab2da1f55e43201582ebdafbbf721` |
| `SPARSE_DAG_REMAINING_OUTPUT_FAILED_20260808T045242Z_ENV.json` | `6517dfe762ceb15da2feaf6ea11864a32f74a68c2fd05278bcdf855e2368dc0d` |
| `SPARSE_DAG_REMAINING_RUN_FAILED_20260808T045242Z_ENV.log` | `54f03c6d3edb290756d9ffca9b53bad081db136a39af87849e31ca1e5d4d5e9f` |

Each of the five empty per-case environment-failure checkpoints has SHA-256
`a418d7db9f17dd9548f429a9c671b2871df7db4ebbff70f2cfb8cdb6d0877400`.
