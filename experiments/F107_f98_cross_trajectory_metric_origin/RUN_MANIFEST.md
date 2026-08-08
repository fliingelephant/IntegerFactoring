# F107 run manifest

## Authoritative candidate run R02

```text
command: /opt/homebrew/bin/python3 experiments/F107_f98_cross_trajectory_metric_origin/run_with_timeout.py
working directory: /Users/zhou/autoresearch/IntegerFactoring
inner command: /opt/homebrew/bin/python3 experiments/F107_f98_cross_trajectory_metric_origin/analyze_metric_origin.py
hard timeout: 30 seconds
elapsed: 0.030280 seconds
exit code: 0
log: RUN.log
output: OUTPUT.json
```

The run reads the pinned F98 public certificate and pinned F100
factor-assisted factorizations. It does not factor N or select a new
dependency.

## SHA-256

```text
70752325390cb6d15885ea66d46a54e1f3941424fb0226132ec9c462b14bca1e  DESIGN.md
a5636dcf7d30340a0717bb2712d181ed701e4d5071aa683643ed77da57ef8cac  analyze_metric_origin.py
bd2165b63384de58a44a80c20c36eae82b9626b13f105085db0340a7c6adede3  run_with_timeout.py
5eda5e8053386781a0adb7bbec9ec5a5af89192bc65ea027162e4ee3dd1337f9  OUTPUT.json
0031acc1ba179b71423abf8317b8abf907fce2af90be8f6c7a01dbfbc8bc5a8f  RUN.log
c28e667601b9b283044b1bd9afc80954d0459e03d97af544ee69e6bd284f7cda  FAILED_RUNS.md
ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab  ../F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json
9bcf6217f412f837fab8e3d0b832e01c80fbd5afa1d173156ec93df95bd94076  ../F100_f98_dependency_structure/OUTPUT.json
```

## Preserved preliminary run

R01 omitted two reported category intersections but did not use a different
classification. Its valid preliminary artifacts are preserved:

```text
7bc9807fe74293d9da879c865196339c8b948b3d3d71db6f3375027f636a7603  OUTPUT_R01.json
910127b2616c3aceb27f168048660ae1b5210accd238bc196c7850df0419f2b5  RUN_R01.log
```
