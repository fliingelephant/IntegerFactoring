# Proof-blind reconstruction manifest

## Isolation

Only these pre-existing files were read:

```text
RECONSTRUCT_STATEMENT.md
RECONSTRUCT_INPUT.json
```

No other F111 file and no F98, F109, or F110 file was read, imported, hashed,
or executed.

## Source files

```text
RECONSTRUCT_BLIND_verify.py
RECONSTRUCT_BLIND_runner.py
```

The verifier uses the standard library only.  It has no factorization,
primality, or external mathematics-library dependency.

## Commands

Syntax validation:

```text
python3 -c 'from pathlib import Path; [compile(path.read_text(), str(path), "exec") for path in map(Path, ("experiments/F111_factor_free_cross_layer_certificate/RECONSTRUCT_BLIND_verify.py", "experiments/F111_factor_free_cross_layer_certificate/RECONSTRUCT_BLIND_runner.py"))]'
exit_code=0
```

Authoritative outer command:

```text
python3 experiments/F111_factor_free_cross_layer_certificate/RECONSTRUCT_BLIND_runner.py
working_directory=/Users/zhou/autoresearch/IntegerFactoring
exit_code=0
```

Exact inner command from the run log:

```text
/opt/homebrew/opt/python@3.14/bin/python3.14 /Users/zhou/autoresearch/IntegerFactoring/experiments/F111_factor_free_cross_layer_certificate/RECONSTRUCT_BLIND_verify.py --output /Users/zhou/autoresearch/IntegerFactoring/experiments/F111_factor_free_cross_layer_certificate/RECONSTRUCT_BLIND_ATTEMPT_OUTPUT.json
working_directory=/Users/zhou/autoresearch/IntegerFactoring/experiments/F111_factor_free_cross_layer_certificate
hard_timeout_seconds=120
elapsed_seconds=0.143313
timed_out=false
exit_code=0
status=PASS
python=3.14.5
```

The runner atomically renamed the successful attempt output and log to their
authoritative names.

## Output and log

```text
RECONSTRUCT_BLIND_OUTPUT.json
RECONSTRUCT_BLIND_RUN.log
```

The JSON output has status `PASS`.  No failed attempt exists.  The failure
policy and first-attempt status are in `RECONSTRUCT_BLIND_FAILED_RUNS.md`.

## SHA-256 pins

Authorized inputs:

```text
e1a573feaceb2465d599df21a41b46372c25c6c30cb15ad7d1b6c56230fe0dae  RECONSTRUCT_STATEMENT.md
8622024473bd602d1d4928fad959099db1ae463e9bd736b7b6ec59fbb99c3f61  RECONSTRUCT_INPUT.json
```

Blind reconstruction artifacts:

```text
01e7d4b8ac3f42385b7fe49c4d174e297bace3cb0552b1f8d213cc43bed85734  RECONSTRUCT_BLIND_verify.py
b79cf2c22fe0ca7aeca6e303caa932a47dfd2184cc495eaf643150276b336fd7  RECONSTRUCT_BLIND_runner.py
7118603de54b6f94e1102907aafc059344e5e936062ae014e7f67d8ac1d40b53  RECONSTRUCT_BLIND_OUTPUT.json
b577ad60198f16344ec51c168b0ed065c114d8cfc24538e7787e13d874ac3c22  RECONSTRUCT_BLIND_RUN.log
ae5efd84c3a50ff0a38779586aa0518d6fc8946887121b2a56e296dfcbc300a8  RECONSTRUCT_BLIND_FAILED_RUNS.md
60fd35b95e367d80fa18442dcc5e0587381f10b018901c621d69ad79c1d00e0f  RECONSTRUCT_BLIND_REPORT.md
```
