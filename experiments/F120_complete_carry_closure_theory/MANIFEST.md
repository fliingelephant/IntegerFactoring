# F120 Manifest

## Boundary

F120 proves a source-independent prime-row degree bound and gives one exact
trial-hard distinct-semiprime counterexample to universal `REUSE`. It does not
prove an infinite semiprime family, `CLOSE`, or `ROOT`.

The mathematical result uses exact integer arguments. The only computation
is the preregistered deterministic search for one finite semiprime falsifier.
It uses proof-enabled Sage primality checks. No smoothness or random-matrix
evidence is used. An exploratory theorem lookup was not used as evidence.

No durable ledger was edited.

## Registered run

```text
named_timeout=F120_SEMIPRIME_PRIVATE_ROW_HARD_TIMEOUT
hard_timeout_seconds=60
registered_pair_cap=10000
accepted_status=FOUND
pairs_tested=23
elapsed_seconds=3.914020
```

The first run failed before candidate generation because Sage could not write
`/Users/zhou/.sage/cache`. After explicit approval, the retry changed only
`DOT_SAGE` to an experiment-local writable cache. The registered source,
candidate order, proof-enabled primality checks, timeout, and evidence
standard were unchanged. The cache was removed after the run because it is
transient and is not evidence.

## SHA-256 pins

Each hash is over the exact file bytes. This manifest has no self-hash.

| Role | File | SHA-256 |
|:---|:---|:---|
| Prior carry result | `../F119_all_pairs_private_row_theory/RESULT.md` | `552a54c8382341709305e53bd535efd9ef0ec0bc7957fa32be8ddc5c061f4575` |
| F116 fixed-source design | `../F116_independent_54bit_all_pairs_stress/DESIGN.md` | `533f92d1e79cf81ef4e3841b48fbddd527571a944b3fced5c131b6148034c803` |
| F118 fixed-source design | `../F118_58bit_full_source_null_search/DESIGN.md` | `3e474dd0bcacda89b6fca863fda59c019066da3664b6ef17312c00ef55da9c2a` |
| Preregistered question | `QUESTION.md` | `d11a55ce9dc747af2c43935fd352f083d483fd478400512bf7e9c01328064ad6` |
| Run registration | `REGISTRATION.json` | `4a014f6d0704d1ba083e53c2e44858838b10938cad0a9d90869cc16e629f09d1` |
| Search source | `find_semiprime_private_row.py` | `04f5abd4140a885f2d3e22f38a597e88e95063aee1479a40d01e9d0c0c178e94` |
| Approved retry runner | `run_with_timeout.py` | `fe383ace9cfbdb39a3398bf69375947219b8902454ccfacde229e1819dcb1be2` |
| Authoritative output | `OUTPUT.json` | `bc84fec9d4b8ab17d4a84c5b9a64b753c0625023f7b963e805f4828ee4d361f9` |
| Authoritative run log | `RUN.log` | `52170ca6a746993fab8a0e03d7c6529d76e8e1527c96948d32f036c992413c5f` |
| Failed environment output | `OUTPUT_FAILED_20260808T054832Z_EXIT_1.json` | `278b311e583cf2e96331aa53dc9037db7f6bcaebb19b41116393caca2275bd48` |
| Failed environment log | `RUN_FAILED_20260808T054832Z_EXIT_1.log` | `0a6aeb91b2adc447c20743029a62dcb2b85bc1efd3227f28be533853334c61a7` |
| Failed-run record | `FAILED_RUNS.md` | `11aae8f244c3ca7256a6b3b73f914ac4b442e5ddafd6523d7c3857a8c66399c4` |
| Preserved proof failures | `FAILED_ROUTES.md` | `a87f6076ff69a9bc1c95976cc95849cd9971d5334a00830adaba3b4ccba20c47` |
| Proof and result | `RESULT.md` | `a8a63cc9a2bfab6acea2ded42e851fe3d6a185e15f9962bbe802a0ecb1866445` |
