# F112 run manifest

## Authoritative completed counterexample run

```text
command=/opt/homebrew/opt/python@3.14/bin/python3.14 experiments/F112_frozen_two_v_global_root_stress/run_with_timeout.py
inner_workers=4
hard_timeout_seconds=1800
inner_elapsed_seconds=224.40180541599693
inner_exit_code=0
completed_cases=100
factor_cases=86
null_cases=14
claim_status=FAIL
```

The runner intentionally preserves a completed falsifier under failed-claim
names instead of promoting it to `OUTPUT.json`.

## SHA-256 pins

```text
b27316ffe98f84830802abd018ef6a5f0e902d1a7d399d8dd727befeef61fec1  DESIGN.md
3eb11e927f3b376db890fe46a9b528af1b40229b1cbf83185994dc336e9a4acf  stress_frozen_two_v.py
1599eae0247456b13491031c7a2fb338b422da45f73c0e79d0ddcc598db52a20  run_with_timeout.py
1c5bc0c9078f2424134790f410f15b9ed10f2fefc92e87b7e59121096602ee96  OUTPUT_FAILED_20260808T025244Z_CLAIM.json
e94e192901fc46f338b09da8e843bdf4dc313ed4ab01500f3e78c20fb7502fa5  RUN_FAILED_20260808T024838Z_EXIT_1.log
f8db33c5b976d635f8b48bf81f85b4901d9704ef94502c516ac88fa1d964cc49  RUN_FAILED_20260808T025244Z_CLAIM.log
2fa5068fbd8eb724d8f169fbf03be7e019db072c8b4fab2537c2c2e725204131  ../F110_frozen_batch_seed_pair_rescue/test_frozen_batch_rescue.py
```

The first run failed before any case because the sandbox blocked a process
pool system query.  It is excluded from the mathematical result.
