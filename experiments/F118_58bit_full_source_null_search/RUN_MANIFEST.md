# F118 run manifest

## Passing run

- Command: `python3 -B run_with_timeout.py`.
- Named timeout: `F118_58BIT_FULL_SOURCE_NULL_HARD_TIMEOUT`.
- Hard timeout: 1,200 seconds.
- Registered Sage child:
  `/usr/local/bin/sage -python scan_full_source.py --spec CORPUS_SPEC.json --output ATTEMPT_<UTC>.json`.
- Final log: `RUN.log`.
- Final output: `OUTPUT.json`.
- Result: `CAP_COMPLETE_NO_NULL`.
- Scanner time: 293.096697 seconds.
- Wrapper time: 295.204076 seconds.

The runner verified every hash in `REGISTRATION.json` before it started
Sage. The passing run used elevated filesystem access only because Sage writes
its import cache under `~/.sage`.

## Failed environment-only attempt

The first wrapper attempt ran inside the workspace sandbox. Sage failed during
import before candidate generation because it could not write its import
cache under `~/.sage`.

- Log: `RUN_FAILED_20260808T052055Z_EXIT_1.log`.
- Output: `OUTPUT_FAILED_20260808T052055Z_EXIT_1.json`.
- Log SHA-256:
  `6d60ee0b5fc5f41132c73be8d221491fd46b983f8e77dbcc4a497ec13d483174`.
- Output SHA-256:
  `a418d7db9f17dd9548f429a9c671b2871df7db4ebbff70f2cfb8cdb6d0877400`.

No target computation started in this failed attempt. The frozen registration
and sources did not change before the passing rerun.
