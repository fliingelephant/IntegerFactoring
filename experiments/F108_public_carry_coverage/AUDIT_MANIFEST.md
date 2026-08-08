# F108 hostile-audit manifest

## Verdict

- Status: PASS.
- Candidate source imported or executed: no.
- Audit truth oracle: Sage factorization of the 166 fixed endpoint pairs.
- Rank oracle: SageMath 10.9 matrices over `GF(2)`.
- Declared hard timeout: 300 seconds.
- Final runner exit code: 0.
- Verifier elapsed time: 0.746 seconds.

## Commands

```text
python3 experiments/F108_public_carry_coverage/run_hostile_audit_with_timeout.py
/usr/local/bin/sage experiments/F108_public_carry_coverage/audit_independent_verifier.sage
```

Sage needed access to its existing cache under `/Users/zhou/.sage`. The
first sandboxed attempt failed before import and is preserved. The successful
run used the identical 300-second runner after cache access was approved.

## Corrected candidate artifacts

```text
db3531a92180c051fac08ba10bdb79ebaf2d2756cac560effa646b6ebc4a62dc  DESIGN.md
623deb83b7695e02e8e36f48dd48d65d9072d7a147a8e58278fa7cd6e30d4135  FAILED_RUNS.md
2427d36129ecac0de8e735d972f641dbdb2c22d885c28d1502ba0ff9411340c5  OUTPUT.json
5c912207a12fb3d561423d5d5e6cd71c4b685a7d6a9f572dc868d29ef8f47dbc  RESULT.md
50bb788a90ec5135d20ba43ead4df8e53d4744495e632b1cb4cc80814c741c46  RUN.log
23b147431833715e293494449bc9d75b931ad3b5108cf686bf67de60aafc0a29  RUN_MANIFEST.md
0be579050066d9bc79e4bf5192a606989958fef2531420fb83984de925e1e8de  analyze_public_carry_coverage.py
8849a9789e9ebd0920705713b12b52720cd84a74568514fad33200804cbc7948  run_with_timeout.py
```

The initial hostile audit read the pre-correction wording at these hashes:

```text
0c1ef45b46a8879df1ec41bc9f25d00f70ef68c4ee0694f8f5db99f502e19620  prior DESIGN.md
e02b88815e04cd60234b5c4aa5353bc82ead596ab881d6004289eec0a8873889  prior RESULT.md
```

## Pinned public input

```text
ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab  ../F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json
```

## Audit artifacts

```text
517c3421b848d36e6b49a7e7682edc1a529abdb1a4ed006fa6b2e2077a700e49  audit_independent_verifier.sage
1e856cd9bafb00de487b804219751cf17c1e46fbef45d0747c41b1acd1a603b0  run_hostile_audit_with_timeout.py
78335beeef175ddb809db105126b2ae8e414853ce28e6046c49d2898abc1c1c3  AUDIT_OUTPUT.json
86d941a6bb98d05fe29beb74339a4b5a15f31c644634255d4351188d2ec60ca7  AUDIT_RUN.log
576ad5c07c2857b1bd64e861dffa4ed1c108ca491364505f756b639ba7176bc8  AUDIT_FAILED_RUNS.md
fb6a16a2e5d102c6accfcb319bbe96c15893c02703f417ee5287614c54833f52  AUDIT_FAILED_20260808T022331Z_SAGE_CACHE.log
144cdec6d515d1eea254d6121288ec7bdc8eb495e03ae23ca48d95a62f55ebf9  AUDIT_FAILED_20260808T022414Z_SAGE_SEED.log
6e17edd24681e003a894943a6e6f37975d2cc1fb8b8d66f87cc54d4804c48a0f  FINAL_REAUDIT.md
```

`AUDIT.md` and this manifest are excluded from their own hash list.
