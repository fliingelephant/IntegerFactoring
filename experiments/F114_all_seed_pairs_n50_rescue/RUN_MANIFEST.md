# F114 run manifest

```text
command=/opt/homebrew/opt/python@3.14/bin/python3.14 experiments/F114_all_seed_pairs_n50_rescue/run_with_timeout.py
inner_workers=4
hard_timeout_seconds=1800
elapsed_seconds=183.3219162089954
exit_code=0
completed_cases=7
factor_cases=7
```

## SHA-256 pins

```text
9c269e4e72473956e7fbacef0dd27632354cf54cdff4c1694a1e584e042912e1  DESIGN.md
4ff3be00160bd2a7a7d1a3b5e1245c118b6a8f2219f9b1b63401265b50f25cb5  test_all_seed_pairs_n50.py
3c3ce288bd6c37f1655f6484c9af0f09bae1060862acae6d222db3ee6b1f8eb9  run_with_timeout.py
e63cd04be683e2f64ad2c49e1ffe2bcb7c8094aa9520a4a299e9def968f6f4f6  OUTPUT.json
6266bfda2cadd379dba1821c7b70d635dd574536a6a25cf341fec7fd19df3f7d  RUN.log
dd69c3396c420aa387260cb706ce51f2a518b4a0f0dc4cfcbe91f959a1c28d5c  FAILED_RUNS.md
4ad9522199e5c4e6b7227aa7e3fca9282363d4ed17a40194a6936d71b5689516  RUN_FAILED_20260808T025529Z_EXIT_1.log
c254ba6ec5b8bcc1ce816b60865ae0bce0cd9725aee2bdee1144acd03df290ab  ../F113_all_seed_pairs_n46_rescue/test_all_seed_pairs.py
```

The first launch failed before it completed a case because its dynamically
imported worker was not picklable. The failed log is preserved. The corrected
run adds only a top-level wrapper and supplies the mathematical output above.
