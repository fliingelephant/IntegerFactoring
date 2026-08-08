# F103 run manifest

## Authoritative run

The named runner invoked the named Python source with a hard 180-second
timeout. The source received only (N). It imported the pinned audited F98
public arithmetic source and wrote `OUTPUT.json`.

```text
command=/opt/homebrew/bin/python3 public_core_replay.py --modulus 202537109 --output OUTPUT.json
timeout_seconds=180
exit_code=0
elapsed_seconds=60.189580
source_elapsed_seconds=60.144565
```

The run did not call factorization, primality testing, order finding, Sage,
or a factor-aware target selector.

## Failed runs

`FAILED_RUNS.md` records that no failed named run occurred.

## SHA-256

```text
e88a9454cfccbfd9b5796c996be6dc0cbabeb28896379a4797d2cddff09f3c28  DESIGN.md
28a8371d6395321969280b223098d54d675a5330deecc31c5bb821c014a177ef  RESULT.md
5a14eead9fb88e212bbcfb64e8e1425436ccc0d4d9eea2935224943cd4ffe4b0  public_core_replay.py
3c216f9db20231153bd9e7a41bdb8f3459a0ea43a117447bd1a7d4ff6c1a0169  run_with_timeout.py
5a02ad9410219442c818bf77d1c513ad268883d18c5e3c9e04779806d454defd  OUTPUT.json
93329866d34e7ec8d0d31d20016d610d45ee7ed1a93e09c41fa94e79fa5865e5  RUN.log
09220883e9170d5a44db6203b94a13124aa88da044f2b5666569da5a77e63eb7  FAILED_RUNS.md
5fded40920ca52827662ba536f14a49ec9e302b934f6d0967e66be2b18c9ba4b  ../F98_multiseed_presentation_closure_kill/public_factorization_free_replay.py
```
