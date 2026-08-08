# F103 hostile-audit manifest

## Authoritative independent run

```text
command=/opt/homebrew/opt/python@3.14/bin/python3.14 AUDIT_VERIFY.py --candidate-dir . --f98-source ../F98_multiseed_presentation_closure_kill/public_factorization_free_replay.py --f102-output ../F102_f98_full_parity_core/OUTPUT.json --output AUDIT_OUTPUT.json
timeout_seconds=240
elapsed_seconds=67.885393
timed_out=false
exit_code=0
strict_status=PASS
checks=122
failures=0
```

`AUDIT_RUNNER.py` enforced the subprocess timeout. `AUDIT_VERIFY.py` imported
neither the F103 candidate nor the pinned F98 source.

## Preserved failed audit run

The first verifier run exited with code one after an independent-verifier
seed-refinement bug. It is preserved in:

```text
AUDIT_FAILED_20260808T092223.json
AUDIT_FAILED_20260808T092223.log
```

This was not a candidate run or candidate failure.

## Candidate and comparison inputs

```text
e88a9454cfccbfd9b5796c996be6dc0cbabeb28896379a4797d2cddff09f3c28  DESIGN.md
28a8371d6395321969280b223098d54d675a5330deecc31c5bb821c014a177ef  RESULT.md
fbf5010b203e20176d45292fee3f437518c07b7fbe843047bd152ea1dcb44a16  RUN_MANIFEST.md
5a14eead9fb88e212bbcfb64e8e1425436ccc0d4d9eea2935224943cd4ffe4b0  public_core_replay.py
5a02ad9410219442c818bf77d1c513ad268883d18c5e3c9e04779806d454defd  OUTPUT.json
93329866d34e7ec8d0d31d20016d610d45ee7ed1a93e09c41fa94e79fa5865e5  RUN.log
5fded40920ca52827662ba536f14a49ec9e302b934f6d0967e66be2b18c9ba4b  ../F98_multiseed_presentation_closure_kill/public_factorization_free_replay.py
62e08b8fb396df3fbc65f527e7df6d687d4e75661f92e8cf98cd98f95e31c20d  ../F102_f98_full_parity_core/RESULT.md
6ac7f0e543fadae37ebbfc998bc314aceed02664d023a62506587cfe8a9ab6bc  ../F102_f98_full_parity_core/OUTPUT.json
```

Every hash declared inside the candidate `RUN_MANIFEST.md` also matched its
target. The verifier records those claimed and actual values separately in
`AUDIT_OUTPUT.json`.

## Independent audit artifacts

```text
fa7aabfeb33f90658a94cbf2517448a0942a2c1101552267e9a1f3206aed8402  AUDIT.md
5f0a419fe8d53f58891bdcf98cfdf7bf3162f81d9a1deb1bc96312dd3752eab9  AUDIT_VERIFY.py
1ba740ea2253ccca98ce27ecad20af4111f16685c7e54e97cae4b5130373f375  AUDIT_RUNNER.py
3a81c17af14e945d28a45f7fe1fd139c23deb9634402ef5faaec8c494bd21055  AUDIT_OUTPUT.json
dc62874b6149450d4965bfb45086faa6abbff3b5315398b8368b25b0279dd0e7  AUDIT_RUN.log
cdbf54fb69fce3a033644d9f4747c5ac0929a9c5b71a39b86f3f817b2409e603  AUDIT_FAILED_20260808T092223.json
dc9305028a9876f7c50b2ec401c4b593c4cca26b11b9fff92421b51fcd886d8d  AUDIT_FAILED_20260808T092223.log
```
