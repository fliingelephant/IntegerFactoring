# F109 run manifest

## Authoritative run R02

```text
command=/opt/homebrew/opt/python@3.14/bin/python3.14 experiments/F109_recursive_feedback_rescue/run_with_timeout.py
inner_source=experiments/F109_recursive_feedback_rescue/test_recursive_rescue.py
working_directory=/Users/zhou/autoresearch/IntegerFactoring
hard_timeout_seconds=600
elapsed_seconds=328.9993519159907
exit_code=0
status=PASS
```

The run imports the pinned F98 factor-assisted discovery source.  It factors
public endpoint values to build the exact prime-parity decoder.  It does not
serve as a factor-free replay.

## SHA-256 pins

```text
1780f158b0a0b53812b12cbca39eddfc3038f28e1b320b88e82f900c76f85ae4  DESIGN.md
a223723f2bfef64a97ff7a14532627927d11870e9965b40a96b05c89f27b612e  test_recursive_rescue.py
05749e3626f600edeac67c6fe50e69dfe3a2a41792a9a2d0f7043bbe48041fb5  run_with_timeout.py
ce23482d464dee551f3b585dedd803d3af24753592c4b639f5ee796b05d9e356  OUTPUT.json
4432bcf455c6f74d018452cdc56255095c47481253bc5bac458c5c64c262aa9d  RUN.log
aaaa7d3f21ff245d7dfcaa0fa79baa2ed7ba1344c9baf5df96b9af7648f09ab2  FAILED_RUNS.md
f0e9d8281b1b07f97d9e2d005f9959461bcbff4f6822b5c20cbc2fbd6c44f0c6  RUN_FAILED_R01_ASSERTED_ISOLATED_SUCCESS.log
cbf50afc19a387ee58dffa9b0cca9a4ac2e732265c1b841cb535907cce364479  ../F98_multiseed_presentation_closure_kill/search_factor_assisted.py
```

## Preserved failed run

R01 asserted that the isolated final pair must succeed.  The first case
refuted that assumption.  Its complete assertion log is preserved and is not
used as evidence for R02.
