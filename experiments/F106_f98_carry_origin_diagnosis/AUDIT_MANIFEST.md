# F106 hostile-audit manifest

## Authoritative independent run

```text
command=/opt/homebrew/opt/python@3.14/bin/python3.14 audit_independent_verifier.py --candidate-dir . --f98 ../F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json --f100 ../F100_f98_dependency_structure/OUTPUT.json --output AUDIT_ATTEMPT_OUTPUT.json
working_directory=/Users/zhou/autoresearch/IntegerFactoring/experiments/F106_f98_carry_origin_diagnosis
timeout_seconds=60
elapsed_seconds=0.443200
timed_out=false
exit_code=0
verifier_status=PASS
candidate_verdict=FAIL
checks=32503
verifier_failures=0
```

`run_F106_hostile_audit_with_timeout.py` enforced the hard timeout. It moves
an unsuccessful attempt to a timestamped `AUDIT_FAILED_*` pair. A successful
attempt becomes `AUDIT_OUTPUT.json` and `AUDIT_RUN.log`.

The verifier imported and executed neither candidate source file. It used
Python 3.14.5. A separate SageMath 10.9 dense-matrix check confirmed ranks
165, 71, 145, 72, 165, and 50 for the full, narrow-carry, narrow-no-carry,
mixed-carry, odd-only, and pure-edge matrices.

## Pinned inputs

```text
ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab  ../F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json
9bcf6217f412f837fab8e3d0b832e01c80fbd5afa1d173156ec93df95bd94076  ../F100_f98_dependency_structure/OUTPUT.json
```

These hashes equal the input hashes in the candidate manifest and output.

## Candidate artifacts inspected without modification

```text
e5f41ba6be4affcac2da0c283b30c894ef2b10eb8027b38f843c96d78eaea883  DESIGN.md
71c99a6416ffb4ea8bad337485b7aa3bf2f5a25d09d480e10c3d653244b621ee  RESULT.md
bdb85406431ce17708f63ef29d9348b052fcdd297ac2d9de670c8e1b9969b542  RUN_MANIFEST.md
ba318e99ace6a7f33678b4c7b6d50ea621b2e608aa0ef20820d56715e79fd656  analyze_carry_origin.py
2eb51391866bd410b30abbb85c19d498a8f7c0a196eedb3fe45543752414550b  run_with_timeout.py
6335e3782c5da0d398354b152409538a350769fb590d3d22f3014f5d28893d9e  OUTPUT.json
9ecb3c14294c6e7ec0ebbe264b3e83ad5e0148954c52663bb6c8e401bfc7f802  RUN.log
dfc4f3a257e278fa17cefeee1d21c31e2f724851d487f303dd0de32d90abbfcf  FAILED_RUNS.md
07f77a888509408625e03709c60c702273c60c8e64dfbad45b642b5c9864ea5c  OUTPUT_R01_ADJACENT_ONLY.json
88651d10e60a2c09c2b6b0cf18cbb567abbf2b4c77b60ca17328b5754b2f6ce2  RUN_R01_ADJACENT_ONLY.log
```

All ten hashes declared inside the candidate `RUN_MANIFEST.md` match their
targets. The two run logs contain exit code zero and JSON equal to their
respective output files.

## Authoritative audit artifacts

```text
02b9d0a0ca1c29d86b42d329f650f9b16673048a533027762623d2d13031c834  AUDIT.md
d35381b61cb58e1061785b6fb86e733b2fa5f3d484a93909efdcb1da6603fa97  audit_independent_verifier.py
d5f7117309bc8c40f8cdf2cb6f7641ab45a3de2dabc62ea6058b8234bd2d7c70  run_F106_hostile_audit_with_timeout.py
e30896dd84f8c0f2afb58e74d8a035cc35effd66c560ad6c75f293a07a9d5aae  AUDIT_OUTPUT.json
7f29913739965bc403201549eb8016e7c1265ff009c35224377ddea01d561772  AUDIT_RUN.log
```

## Preserved failed audit attempts

```text
c45adcdf532863dec72d2a35611cd8dc714cdbba9b5168cd4347da0b4e6a1975  AUDIT_FAILED_20260808T014849Z_SCOPE_BUG.json
d19e6336816f31eb0a8587e6c57765e0f7fb4a22c57da87c80ab7f3603ecc343  AUDIT_FAILED_20260808T014849Z_SCOPE_BUG.log
7e51613253c3142690f4207c306925d964f8afd7007025d618f85f071d41680b  AUDIT_FAILED_20260808T015050Z_DUPLICATE_FILTER.json
c31cb190aa8d27093afca51d79d347de03019889149b4f133f566adc056b97f0  AUDIT_FAILED_20260808T015050Z_DUPLICATE_FILTER.log
```

The first attempt used only the eight certificate-represented trajectories
for a scan labelled “full round one.” The second used inconsistent duplicate
filters in the 8- and 54-trajectory scans. Both were audit implementation
failures. Neither changed or executed the candidate.
