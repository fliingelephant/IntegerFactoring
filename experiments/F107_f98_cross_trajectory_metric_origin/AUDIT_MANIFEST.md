# F107 hostile-audit manifest

## Authoritative independent run

```text
command=/opt/homebrew/bin/python3 audit_independent_verifier.py --candidate-dir . --f98 ../F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json --f100 ../F100_f98_dependency_structure/OUTPUT.json --output AUDIT_ATTEMPT_OUTPUT.json
working_directory=/Users/zhou/autoresearch/IntegerFactoring/experiments/F107_f98_cross_trajectory_metric_origin
timeout_seconds=60
elapsed_seconds=0.500928
timed_out=false
exit_code=0
verifier_status=PASS
candidate_verdict=FAIL
checks=7698
verifier_failures=0
```

`run_F107_hostile_audit_with_timeout.py` enforced the hard timeout. It moves
an unsuccessful output and log to a timestamped `AUDIT_FAILED_*` pair. It
promotes only a successful run to `AUDIT_OUTPUT.json` and `AUDIT_RUN.log`.

The verifier imported and executed neither candidate source file. It used
Python 3.14.5.

SageMath 10.9 separately read the full per-prime supports and checked dense
GF(2) ranks:

```text
all=165
strict_cross=163
strict_base_free=159
strict_no_mixed=141
raw_exposed=165
strict_no_raw=25
```

## Pinned inputs

```text
ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab  ../F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json
9bcf6217f412f837fab8e3d0b832e01c80fbd5afa1d173156ec93df95bd94076  ../F100_f98_dependency_structure/OUTPUT.json
```

These hashes equal the input hashes in the candidate manifest and output.

## Candidate artifacts inspected without modification

```text
70752325390cb6d15885ea66d46a54e1f3941424fb0226132ec9c462b14bca1e  DESIGN.md
bd16a7b6ad07e207e27c06ab6787196732c28c63627cd4a09ca182cf72e5be67  RESULT.md
6c1c1cd5b43a44d87750b71b274afac33778e77abb3e351518bb17c3268bad7d  RUN_MANIFEST.md
c28e667601b9b283044b1bd9afc80954d0459e03d97af544ee69e6bd284f7cda  FAILED_RUNS.md
a5636dcf7d30340a0717bb2712d181ed701e4d5071aa683643ed77da57ef8cac  analyze_metric_origin.py
bd2165b63384de58a44a80c20c36eae82b9626b13f105085db0340a7c6adede3  run_with_timeout.py
5eda5e8053386781a0adb7bbec9ec5a5af89192bc65ea027162e4ee3dd1337f9  OUTPUT.json
0031acc1ba179b71423abf8317b8abf907fce2af90be8f6c7a01dbfbc8bc5a8f  RUN.log
7bc9807fe74293d9da879c865196339c8b948b3d3d71db6f3375027f636a7603  OUTPUT_R01.json
910127b2616c3aceb27f168048660ae1b5210accd238bc196c7850df0419f2b5  RUN_R01.log
```

All ten hashes declared inside the candidate `RUN_MANIFEST.md` match their
targets. Both run logs contain exit code zero and JSON equal to their output
files. Every comparable R01 field matches the independent reconstruction.

## Authoritative audit artifacts

```text
985edf65b3d3030eeba321b2b6e0c6a3e4f5fa8742a163ce0797170f1a088804  AUDIT.md
1bf5c2830675cb5388bcf0083224547e7c202f11657163b20929c8dfd5cd515b  audit_independent_verifier.py
c0d7de621d0d7e0e9b298d89a2938ec38273995c3f96fdc757a55de561a2530d  run_F107_hostile_audit_with_timeout.py
32c7383badfeddfe7d0642e4a1c576b5ee913249b470f008670263e25157392f  AUDIT_OUTPUT.json
9e25dbd8e61e7356fb1a16efebaa8de5a32352d9bddf8f876a6cb9fd7b494702  AUDIT_RUN.log
```

The canonical SHA-256 of the full 230-row classification inside
`AUDIT_OUTPUT.json` is:

```text
efcf562c11bccf1058e261414d5e311adb7effbea887400a0fc796ab1742833d
```

## Preserved failed audit attempts

No verifier attempt failed. No `AUDIT_FAILED_*` artifact exists. The runner is
configured to preserve any future failure rather than overwrite it.
