# F102 independent audit run manifest

## Authoritative audit run

The audit used a separate Sage source. It did not import the candidate
source. It rebuilt the F98 stream, factored every distinct nonzero relation,
recomputed both matrices, and ran two opposite degree-one peel orders.

```text
command=env DOT_SAGE=/private/tmp/f102_audit_sage /usr/bin/time -p /opt/homebrew/bin/timeout 180 /usr/local/bin/sage audit_verify_full_core.sage --input ../F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json --candidate-output OUTPUT.json --output AUDIT_VERIFY_OUTPUT.json
timeout_seconds=180
exit_code=0
elapsed_seconds=2.14
DOT_SAGE=/private/tmp/f102_audit_sage
```

The named source existed before the authoritative output and log.

## Preserved failed audit run

`AUDIT_VERIFY_FAILED_RUN.log` records one audit-only failure. All
mathematical assertions had passed. JSON serialization then rejected Sage
integer keys in two histograms. The source was changed only to convert those
keys to Python integers. The failed run does not support the verdict.

## Pinned candidate and input SHA-256

```text
ac17c66961f4f52f949f78e03384a8b9ae37710d533d1969c0bc0c8e083a5182  DESIGN.md
62e08b8fb396df3fbc65f527e7df6d687d4e75661f92e8cf98cd98f95e31c20d  RESULT.md
c593a88425e6918ae22af5918316dde4c6e2ecf4c3e67a44fe62fd62c1d0a51d  RUN_MANIFEST.md
dd39810e627dc6e89725b77e4abd36bcb9fa9b40436a94941921b569eae14c7d  analyze_full_core.sage
f3486561e04c5cabb25a951ccca232a772312d7923b48af08490da87854d7e80  analyze_full_core.sage.py
d831af294ec0b3241f10dcb3276905d6ebe01f2dee080b5521ad09d540cb4e29  run_with_timeout.py
6ac7f0e543fadae37ebbfc998bc314aceed02664d023a62506587cfe8a9ab6bc  OUTPUT.json
c18807f11305e1388bcf9f23f1d895685aa389b6b2ac462327adcd353dc2a842  RUN.log
24c75d812fa2c6cf33c322fb480e00f84efd3b00bf019aab5b1ac1e25ad17d53  FAILED_RUNS.md
ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab  ../F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json
5fded40920ca52827662ba536f14a49ec9e302b934f6d0967e66be2b18c9ba4b  ../F98_multiseed_presentation_closure_kill/public_replay.py
```

## Independent audit artifact SHA-256

```text
b25619738a85b495f101118e42c4fcae2d4f43f1ba4933e72dcb6ca20491ed9d  audit_verify_full_core.sage
5697a792997ee1c2cf6af15c90e52d1a5a02f6bbdc56563aafef8a2b8dea9d8e  AUDIT_VERIFY_OUTPUT.json
56f1d9957e26aa69283258f96e7f711f0759a4731af8196d070326a68c8c042e  AUDIT_VERIFY_RUN.log
3297fad24f965cd92b5d77481cd2c3342c6b0e5374eeb6f4002a284db201173e  AUDIT_VERIFY_FAILED_RUN.log
```
