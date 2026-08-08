# F116 proof-blind reconstruction manifest

## Isolation

The only supplied files read before reconstruction were
`RECONSTRUCT_STATEMENT.md` and `RECONSTRUCT_INPUT.json`. No other F116
file and no F104, F110, F111, or F115 file was read. Later verification read
only the new `RECONSTRUCT_*` artifacts.

## Execution

Launcher:

```text
python3 experiments/F116_independent_54bit_all_pairs_stress/RECONSTRUCT_run_with_timeout_v1.py
```

Recorded child command:

```text
/opt/homebrew/opt/python@3.14/bin/python3.14 -B /Users/zhou/autoresearch/IntegerFactoring/experiments/F116_independent_54bit_all_pairs_stress/RECONSTRUCT_decoder_v1.py --input /Users/zhou/autoresearch/IntegerFactoring/experiments/F116_independent_54bit_all_pairs_stress/RECONSTRUCT_INPUT.json --output /Users/zhou/autoresearch/IntegerFactoring/experiments/F116_independent_54bit_all_pairs_stress/RECONSTRUCT_OUTPUT.json
```

Working directory:

```text
/Users/zhou/autoresearch/IntegerFactoring/experiments/F116_independent_54bit_all_pairs_stress
```

- Named timeout: `F116_PROOF_BLIND_HARD_TIMEOUT_V1`.
- Hard timeout: 7,200 seconds.
- Runner elapsed time: 4.602976 seconds.
- Decoder elapsed time: 4.494861457991647 seconds.
- Exit code: 0.
- Status: PASS.
- Failed reconstruction attempts: none.

A separate read-only consistency command verified all source partitions,
attempt-minus-duplicate counts, provenance totals, screen totals, advice
properties, seed-basis invariants, selected provenance, root congruence,
terminal gcds, and the terminal gcd product. It printed:

```text
complete F116 reconstruction consistency checks passed
```

## File pins

| File | Bytes | SHA-256 | Role |
|---|---:|---|---|
| `RECONSTRUCT_STATEMENT.md` | 4,107 | `f402a39c9d751a72c93a46b28ab593c5a1e8a03ed4c9bdc97655b310c01e8983` | permitted public specification |
| `RECONSTRUCT_INPUT.json` | 42,884 | `5194ee596916810edb78fa802c3179341746423c6fb65f2548a600c598b05015` | permitted public instance and advice |
| `RECONSTRUCT_decoder_v1.py` | 26,405 | `9941d108483ab52947168860c33c1e6429d4f95f61da8adeccf42bf750fec187` | independent factor-free verifier |
| `RECONSTRUCT_run_with_timeout_v1.py` | 2,689 | `994520fbdf876902d13c5832bd67d665803b1488852d67911aee6ae6919d8bd2` | named hard-timeout runner |
| `RECONSTRUCT_RUN_V1.log` | 1,263 | `133447678dc0ceee31df4972750aff6671db6d2787eb60a20759bfb3913641d2` | successful complete run log |
| `RECONSTRUCT_OUTPUT.json` | 19,018 | `da4401738fcb1bcc2b2c32b6857f6a1434c1a457edcae860ab7756c262115439` | machine-readable exact result |
| `RECONSTRUCT_REPORT.md` | 5,042 | `6f02b2573997faf9eb723a68bbd20ab9ad25961715dcaf4b94a124310aadd4ee` | human-readable result |

This manifest is not self-hashed. Every supplied input, source, output, log,
and report that it indexes is pinned above.

## Bounded internal pins

Integers use an 8-byte length followed by the minimal unsigned big-endian
payload. Sequences end with an 8-byte item count. No hash uses a large decimal
encoding.

| Object | SHA-256 |
|---|---|
| advice index sequence | `5f049b7552d76c1b99c202994565965a0ef11f76230cfdce297937a76a31c0ef` |
| seed block sequence | `4f85a12cda470b937f4f1ed4275c420a165261862db720a00b3b3550e38846b2` |
| retained-record transcript | `d14d9139e6e5d276c1be9a51d7cc7bb32cd0da466fb52a08674437f6ae094199` |
| direct-screen transcript | `00a8712dd0e068fad69c4568c528cfbeaffe48a34a2afffdcb130fd0c2fd801b` |
| selected-record transcript | `8d00cca0af833d0b9c188093df9ba89d3db6fab5c43f79139c8d55eb55de13e6` |
| selected exact values | `4da154587186547ffa06bab9eb37090db0819647588e2be8f330a18bd70ca1a1` |
| selected exact product | `a10c30c2be30d7665f02ab721e7b1e548dd8986c0a4ce6b2050f1e505bfef696` |
| selected positive root | `1c70b587135415eb699cd7032630ee8990162e3d9a459cd5511df34cbaa3ab71` |
