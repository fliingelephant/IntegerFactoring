# F111 Layer-Interaction Manifest

## Result

```text
A_frozen_contains_non_global_root=false
B_appended_only_contains_non_global_root=false
C_union_contains_non_global_root=true
every_useful_union_dependency_crosses_layers=true
```

The complete exact-value-deduplicated dimensions are:

```text
frozen:            columns=11885 rank=11878 nullity=7
appended alone:    columns=837   rank=837   nullity=0
union appended:    columns=684   rank=684   nullity=0
union:             columns=12569 rank=12551 nullity=18
cross quotient:    dimension=11  normalized-root-map-rank=1
```

## Input policy

- Main replay inputs: `CERTIFICATE.json` fields `N`, `n`, `bound`, and
  `source_stop_relation_count`.
- Public algorithm specification: pinned F98 public-basis source.
- Published 363 dependency indices read by the verifier: no.
- Known factors used by the verifier: no.
- Factorization or primality routine called: no.
- Factor-assisted diagnostic stage: not run.
- F110 and F115 documents: context only, not computational inputs.
- Candidate files edited: none.

## Successful run

```text
command=/opt/homebrew/bin/python3 experiments/F111_factor_free_cross_layer_certificate/LAYER_INTERACTION_run_with_timeout.py
working_directory=/Users/zhou/autoresearch/IntegerFactoring
hard_timeout_seconds=300
outer_elapsed_seconds=162.260575
inner_elapsed_seconds=162.2067346249969
timed_out=false
exit_code=0
status=PASS
verdict=PASS
```

## Computational input SHA-256

| File | SHA-256 |
| --- | --- |
| `CERTIFICATE.json` | `735a8535eb8cd4e8bc5e1c0fbc71d78b3acd79b3e6efa1f865d9084dea67cf6b` |
| `../F98_multiseed_presentation_closure_kill/public_factorization_free_replay.py` | `5fded40920ca52827662ba536f14a49ec9e302b934f6d0967e66be2b18c9ba4b` |

## Context SHA-256

These documents supplied terminology and prior claim boundaries only.

| File | SHA-256 |
| --- | --- |
| `../F110_frozen_batch_seed_pair_rescue/DESIGN.md` | `afe07753f790778bd701c73ad39cc5d1e4c12a56a1ac5844d7f653bde1837f4b` |
| `../F110_frozen_batch_seed_pair_rescue/RESULT.md` | `aa2c010284d5454889ec99163cf7e208806b1716016b41bf91847113b12551de` |
| `../F110_frozen_batch_seed_pair_rescue/AUDIT.md` | `425f15ba95c6609142fa02cbdd134257fb4c91478ad78f6ae0e23857d21a3b94` |
| `../F115_all_pairs_global_corpus_audit/AUDIT.md` | `e0c725521b7307de3c3bb579d1eeee173192f152f6fdae9281ad83ea35e08a6f` |

## Successful evidence SHA-256

| File | SHA-256 |
| --- | --- |
| `LAYER_INTERACTION_independent_verifier.py` | `7c1a12c6489f229e9ea146374b198bd683fbebe6228dcec0c427d2310b394d4c` |
| `LAYER_INTERACTION_run_with_timeout.py` | `7eed85de7e10f7f2de6775f34a430aef790125f8ed657f2ef4df8a73fb5c6082` |
| `LAYER_INTERACTION_OUTPUT.json` | `6b9c66ca97c47d1307212db9ba5fa299df3c66c3312af6ee8f110c9d3e8e52a8` |
| `LAYER_INTERACTION_RUN.log` | `d1db49b4ce80edbb0568953ad6b2738feca7024909ebd019562150eaceddd7b8` |
| `LAYER_INTERACTION_AUDIT.md` | `6133c966d6e14e966314dd43360998289102507d1cb144f5f9a29d158310d95e` |

## Preserved failed attempt

This was an auditor self-check defect. It was not a candidate defect.

| File | SHA-256 |
| --- | --- |
| `LAYER_INTERACTION_FAILED_20260808T034345655510Z_EXIT_1.json` | `01e00b8352a5e099435a13167d44bd45cc24c261fd6c2a88de054b237958f44f` |
| `LAYER_INTERACTION_FAILED_20260808T034345655510Z_EXIT_1.log` | `e45b16da421181ca2779dcb8244bf01dcc3435bf426e786fc9a9b1308e796cc9` |
