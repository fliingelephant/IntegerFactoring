# F102 run manifest

## Authoritative run

The named Python runner invoked the named Sage source with a hard
180-second timeout. It read the frozen public F98 replay and wrote
`OUTPUT.json`.

```text
command=/usr/local/bin/sage analyze_full_core.sage --input ../F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json --output OUTPUT.json
timeout_seconds=180
exit_code=0
elapsed_seconds=2.464807
DOT_SAGE=/private/tmp/f102_sage
```

The candidate source factors the exact relation values for diagnosis. It is
not a factor-free algorithm. Sage also generated the preparsed
`analyze_full_core.sage.py`; this file is retained but is not the named
source.

## Failed runs

`FAILED_RUNS.md` preserves two failed named runs. The first exposed Sage
pre-parser handling of binary XOR assignment. The second completed the
mathematics but failed JSON key serialization. Neither failed run supports a
claim.

## SHA-256

```text
ac17c66961f4f52f949f78e03384a8b9ae37710d533d1969c0bc0c8e083a5182  DESIGN.md
62e08b8fb396df3fbc65f527e7df6d687d4e75661f92e8cf98cd98f95e31c20d  RESULT.md
dd39810e627dc6e89725b77e4abd36bcb9fa9b40436a94941921b569eae14c7d  analyze_full_core.sage
f3486561e04c5cabb25a951ccca232a772312d7923b48af08490da87854d7e80  analyze_full_core.sage.py
d831af294ec0b3241f10dcb3276905d6ebe01f2dee080b5521ad09d540cb4e29  run_with_timeout.py
6ac7f0e543fadae37ebbfc998bc314aceed02664d023a62506587cfe8a9ab6bc  OUTPUT.json
c18807f11305e1388bcf9f23f1d895685aa389b6b2ac462327adcd353dc2a842  RUN.log
24c75d812fa2c6cf33c322fb480e00f84efd3b00bf019aab5b1ac1e25ad17d53  FAILED_RUNS.md
ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab  ../F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json
```
