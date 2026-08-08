# F110 run manifest

## Authoritative run

```text
command=/opt/homebrew/opt/python@3.14/bin/python3.14 experiments/F110_frozen_batch_seed_pair_rescue/run_with_timeout.py
inner_source=experiments/F110_frozen_batch_seed_pair_rescue/test_frozen_batch_rescue.py --case-cap 7
working_directory=/Users/zhou/autoresearch/IntegerFactoring
hard_timeout_seconds=900
inner_elapsed_seconds=6.389679917003377
exit_code=0
status=PASS
```

## SHA-256 pins

```text
afe07753f790778bd701c73ad39cc5d1e4c12a56a1ac5844d7f653bde1837f4b  DESIGN.md
2fa5068fbd8eb724d8f169fbf03be7e019db072c8b4fab2537c2c2e725204131  test_frozen_batch_rescue.py
00315172e6f1b25ea8f46261693475b266becce940cd84e98799518bb6920f2d  run_with_timeout.py
87b339efc536763aac40e04a39878f56cb36a49e64d9af492f3196de9a601458  OUTPUT.json
d7e6f51d9133937139030cec9c470a92a2afeb54a4fb444171349bb3cadc6a1c  RUN.log
faf2bf6e58710401808374e81af6c36d4e4df69dcc6b4d74d3c09d6ca663535b  FAILED_RUNS.md
ce23482d464dee551f3b585dedd803d3af24753592c4b639f5ee796b05d9e356  ../F109_recursive_feedback_rescue/OUTPUT.json
cbf50afc19a387ee58dffa9b0cca9a4ac2e732265c1b841cb535907cce364479  ../F98_multiseed_presentation_closure_kill/search_factor_assisted.py
```

The authoritative run had no failed attempt.  The runner preserves future
timeouts, invalid outputs, and failed claims under timestamped names.
