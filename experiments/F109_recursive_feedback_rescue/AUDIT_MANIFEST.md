# F109 hostile audit manifest

## Authoritative audit run

```text
command=python3 experiments/F109_recursive_feedback_rescue/run_F109_hostile_audit_with_timeout.py
inner_command=/usr/local/bin/sage -python experiments/F109_recursive_feedback_rescue/audit_independent_verifier.py
working_directory=/Users/zhou/autoresearch/IntegerFactoring
hard_timeout_seconds=900
elapsed_seconds=10.057435833005002
inner_elapsed_seconds=7.088140209001722
exit_code=0
status=PASS
sage_version=10.9
```

The verifier does not import F109 code or the pinned F98 factor-assisted code.
SageMath/Pari factors public endpoint values.  The verifier independently
implements endpoint-signature grouping, FIFO recursion, GF(2) elimination,
root tests, isolated controls, and a second row-rank calculation.

No hostile-audit attempt failed.  The candidate's preserved R01 failure is
part of the frozen candidate evidence and was not modified.

## Frozen candidate SHA-256 pins

```text
1780f158b0a0b53812b12cbca39eddfc3038f28e1b320b88e82f900c76f85ae4  DESIGN.md
aaaa7d3f21ff245d7dfcaa0fa79baa2ed7ba1344c9baf5df96b9af7648f09ab2  FAILED_RUNS.md
ce23482d464dee551f3b585dedd803d3af24753592c4b639f5ee796b05d9e356  OUTPUT.json
e19e656156fbd170ccdc1209516d513abdc486b27df52bdfe023303f64c82d7b  RESULT.md
4432bcf455c6f74d018452cdc56255095c47481253bc5bac458c5c64c262aa9d  RUN.log
f0e9d8281b1b07f97d9e2d005f9959461bcbff4f6822b5c20cbc2fbd6c44f0c6  RUN_FAILED_R01_ASSERTED_ISOLATED_SUCCESS.log
76e3fc6d6a25d89b7ad67825a5ade79a2a7c05702603d972ef0d5beb6984b08b  RUN_MANIFEST.md
05749e3626f600edeac67c6fe50e69dfe3a2a41792a9a2d0f7043bbe48041fb5  run_with_timeout.py
a223723f2bfef64a97ff7a14532627927d11870e9965b40a96b05c89f27b612e  test_recursive_rescue.py
cbf50afc19a387ee58dffa9b0cca9a4ac2e732265c1b841cb535907cce364479  ../F98_multiseed_presentation_closure_kill/search_factor_assisted.py
```

## Audit artifact SHA-256 pins

```text
f95d15bb1b7acd5ae667f547c1ea1497c65927d0936600a253f79926be8e7ee0  AUDIT.md
74946e8bae3b4b3461c162e012261ea321399f1e00ed76b6487d510828000f27  audit_independent_verifier.py
c85e6c320a001c50973f8a3cf2f8b328b1b5794d875ef20af56ad1c72c8038a1  run_F109_hostile_audit_with_timeout.py
d597319cd550c735342aaa3306829ac99ee8f9f310e5c76347805e7e6ca4f7e4  AUDIT_OUTPUT.json
17a8852849b434a0be4b72b551cc3c7efb2c8eccd4b545dde256c3e16ce716c7  AUDIT_RUN.log
```

`AUDIT_MANIFEST.md` is not self-hashed.
