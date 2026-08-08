# F106 run manifest

## Authoritative candidate run R02

```text
command: /opt/homebrew/bin/python3 experiments/F106_f98_carry_origin_diagnosis/run_with_timeout.py
working directory: /Users/zhou/autoresearch/IntegerFactoring
inner command: /opt/homebrew/bin/python3 experiments/F106_f98_carry_origin_diagnosis/analyze_carry_origin.py
hard timeout: 30 seconds
elapsed: 0.029928 seconds
exit code: 0
log: RUN.log
output: OUTPUT.json
```

R02 checks every selected pair in one oriented trajectory for an exact
zero-carry chain. It reads pinned F98 public certificate data and pinned F100
factor-assisted factorizations. It does not factor N or select a new
certificate.

## SHA-256

```text
e5f41ba6be4affcac2da0c283b30c894ef2b10eb8027b38f843c96d78eaea883  DESIGN.md
ba318e99ace6a7f33678b4c7b6d50ea621b2e608aa0ef20820d56715e79fd656  analyze_carry_origin.py
2eb51391866bd410b30abbb85c19d498a8f7c0a196eedb3fe45543752414550b  run_with_timeout.py
6335e3782c5da0d398354b152409538a350769fb590d3d22f3014f5d28893d9e  OUTPUT.json
9ecb3c14294c6e7ec0ebbe264b3e83ad5e0148954c52663bb6c8e401bfc7f802  RUN.log
dfc4f3a257e278fa17cefeee1d21c31e2f724851d487f303dd0de32d90abbfcf  FAILED_RUNS.md
ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab  ../F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json
9bcf6217f412f837fab8e3d0b832e01c80fbd5afa1d173156ec93df95bd94076  ../F100_f98_dependency_structure/OUTPUT.json
```

## Preserved superseded run

R01 counted only adjacent selected exponents. It was too narrow for the
declared question. The valid narrower output and log are preserved and are
not authoritative:

```text
07f77a888509408625e03709c60c702273c60c8e64dfbad45b642b5c9864ea5c  OUTPUT_R01_ADJACENT_ONLY.json
88651d10e60a2c09c2b6b0cf18cbb567abbf2b4c77b60ca17328b5754b2f6ce2  RUN_R01_ADJACENT_ONLY.log
```
