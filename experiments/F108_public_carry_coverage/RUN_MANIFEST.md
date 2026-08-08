# F108 run manifest

- Experiment: F108 public carry coverage.
- Source: `analyze_public_carry_coverage.py`.
- Runner: `run_with_timeout.py`.
- Declared hard timeout: 180 seconds.
- Interpreter recorded in `RUN.log`:
  `/opt/homebrew/opt/python@3.14/bin/python3.14`.
- Status: completed with exit code 0.
- Canonical output: `OUTPUT.json`.
- Full log: `RUN.log`.
- Forbidden operations: none.  The source does not factor endpoint or relation
  values and does not use the factor-assisted F100 output.

## Pinned input

```text
ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab  ../F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json
```

## Artifact hashes

```text
0be579050066d9bc79e4bf5192a606989958fef2531420fb83984de925e1e8de  analyze_public_carry_coverage.py
8849a9789e9ebd0920705713b12b52720cd84a74568514fad33200804cbc7948  run_with_timeout.py
2427d36129ecac0de8e735d972f641dbdb2c22d885c28d1502ba0ff9411340c5  OUTPUT.json
50bb788a90ec5135d20ba43ead4df8e53d4744495e632b1cb4cc80814c741c46  RUN.log
```
