# F14 torus q-factorial reconstruction manifest

**Approach-family ID:** `F14_torus_qfactorial_reconstruct`.

The mathematical computation used one named source, an explicit hard
timeout, a retained log, and a retained JSON output.  The successful source
was not edited after R01.  Python's standard library was the only dependency.
There were no failed runs.

## Proof-blind isolation

This reconstruction used only the bare statement supplied with the task.  It
did not read:

- `experiments/F14_torus_qfactorial_evaluator`;
- `experiments/F14_torus_qfactorial_audit`;
- canonical files; or
- messages or artifacts derived from those sources.

All new files are confined to
`experiments/F14_torus_qfactorial_reconstruct`.

## Run summary

| Run | Status | Coverage | Log | Output |
| --- | --- | --- | --- | --- |
| R01 | exit 0, PASS | Gcd counterexample; prime zero sets; composite divisibility; order witnesses; one-lcm false positive; exact shifted polynomial laws; formal supports; quotient and totient bounds; evaluator-tree counts | `logs/R01.log` | `output/R01.json` |

## Exact invocation

From the repository root:

```sh
bash experiments/F14_torus_qfactorial_reconstruct/run.sh
```

The wrapper ran:

```sh
/opt/homebrew/bin/timeout 180s python3 /Users/zhou/autoresearch/IntegerFactoring/experiments/F14_torus_qfactorial_reconstruct/verify_reconstruction.py --output /Users/zhou/autoresearch/IntegerFactoring/experiments/F14_torus_qfactorial_reconstruct/output/R01.json
```

Standard output and error were retained in
`experiments/F14_torus_qfactorial_reconstruct/logs/R01.log`.  The wrapper
recorded `STARTED`, the 180-second timeout, Python 3.14.5, and `PASS`.

## SHA-256

| Artifact | SHA-256 |
| --- | --- |
| `verify_reconstruction.py` | `2d0ef357d44a809fe56cf6c1757e2af00367ef3e977da053f3b5fb21744a6694` |
| `run.sh` | `8243c3b8d89015f6cabce5e71d46408b54b958b015840b671246c9279b60d23f` |
| `output/R01.json` | `6cb6b6825851a891e8165eb2591cbc2e3757ebafcbf8015ee0989bb2b4a37ed7` |
| `logs/R01.log` | `a56ef7d7dd0062dcf70eb9bda90e2af71baf170b4ef80583c9f6413accbc4d5e` |

The source hash is also embedded in `output/R01.json` and was computed by the
source itself before serialization.
