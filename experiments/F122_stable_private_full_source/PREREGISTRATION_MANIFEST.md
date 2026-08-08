# F122 Preregistration Manifest

This manifest freezes the finite diagnostic before execution.

## Fixed execution

- Input: `N=2000887089301=1000289*2000309`.
- Source: complete no-stop F116/F118 menu through exponent `1681`.
- Expected attempts: `2,758,520`.
- Parity columns: global canonical-residue first occurrence, then global
  positive-exact-value first occurrence, with `P=1` removed.
- Decoder: factor-assisted hidden prime parity with exact positive half-roots.
- Named timeout: `F122_STABLE_PRIVATE_FULL_SOURCE_HARD_TIMEOUT`.
- Hard timeout: 900 seconds.
- Sage cache: experiment-local `.sage` from the first attempt.

## Registered artifact names

- Registration: `REGISTRATION.json`.
- Authoritative output: `OUTPUT.json`.
- Authoritative log: `RUN.log`.
- Final report: `RESULT.md`.
- Final hash manifest: `MANIFEST.md`.
- Failure ledger: `FAILED_RUNS.md`.
- Failed outputs and logs: timestamped `OUTPUT_FAILED_*` and `RUN_FAILED_*`.

## Pre-run SHA-256

| File | SHA-256 |
|:---|:---|
| `QUESTION.md` | `3bc499bd883e11605adc20e525c3d43e294207126ad0c0bec8ecd19987b04039` |
| `CORPUS.json` | `861bbe2bf9bba9737796e1ad9ba735c6ee3dd3e4dc4494a9c168d7cebb440090` |
| `scan_complete_source.py` | `8782ab9605ef7b133ec7092b30ab94084871c6e668a1d3ce330d825b7b14610a` |
| `run_with_timeout.py` | `35f2ff702b6c52ee0a2f030e267e25bb58cf49616935dd11cdca0a785571a14c` |

This file will not be edited after execution.
