# F111 Monotone-Extension Audit Manifest

## Verdict

```text
claim_1_exact_value_dependency_existence_is_monotone=PASS
claim_2_full_fixed_trajectory_removes_stop_advice=PASS
claim_3_uniform_complete_factor_free_decoder_factors_fixed_N_in_polynomial_bit_time=PASS
overall=PASS_WITH_EXACT_FINITE_BOUNDARY
```

The basis itself is not monotone. Useful-dependency existence is monotone.
The fixed `(2,3),(2,4)` schedule is post-selected constant program text. No
all-input success statement follows.

## Promoted named run

```text
command=/opt/homebrew/bin/python3 experiments/F111_factor_free_cross_layer_certificate/MONOTONE_EXTENSION_run_with_timeout.py
hard_timeout_seconds=300
timed_out=false
exit_code=0
status=PASS
verdict=PASS
outer_elapsed_seconds=127.876129
inner_total_seconds=127.83969754099962
factor_free_refinement_seconds=127.29557012498844
kernel_and_all_basis_root_tests_seconds=0.3846875830058707
```

The runner used Python 3.14 at
`/opt/homebrew/opt/python@3.14/bin/python3.14`. The exact command, working
directory, timeout, exit status, stdout, and stderr are in
`MONOTONE_EXTENSION_RUN.log`.

No hard-timeout attempt failed. There are no `MONOTONE_EXTENSION_FAILED_*`
artifacts.

## Preliminary computations

The earlier inline diagnostic reported 128.887922709 seconds for refinement
and 0.442452750 seconds for kernel construction and all root tests. It was ad
hoc and had no named source, hard timeout, output, or log. It is unpromoted.

A first named dry run passed in 126.696825 seconds. It is also unpromoted. The
auditor then corrected “fewer than `2n` bits” to “at most `2n` bits” and added
explicit coordinate-stream evidence. The final named run above is the only
promoted run.

## Input and advice policy

```text
N=3241632473
n=32
bound=1024
known_factors_used=false
factorization_calls=false
primality_calls=false
dependency_indices_read=false
generation_fields=N,n,bound
prefix_stop_used_for_generation=false
prefix_stop_used_only_for_post_generation_audit=true
```

The source audit found no prohibited factorization or primality call. The
certificate stop `15383` is used only after full generation to compare the
preserved prefix with the pinned layer output.

## Source, coordinates, and direct gcds

```text
trial_screens=1023
trial_gcd_one=1023
full_source_positions=67681
full_appended_positions=4100
full_retained_records=15884
full_duplicate_residues=51797
prefix_exact=true
prefix_records=15383
prefix_columns=12569
full_columns=12962
prefix_columns_preserved_as_initial_coordinate_block=true
new_columns_after_prefix=393
full_repeated_exact_values_removed=2921
full_unit_values_removed=1
full_direct_screens=31768
full_direct_gcd_one=31767
full_direct_gcd_N=1
full_proper_direct_gcds=0
full_retained_stream_sha256=660b6b8333fd46e3b0d60dc1b72a353371982dc2de3fad490e04dd18b32f2684
full_unique_column_stream_sha256=68afa804f4a4ed6d49dd5127b7f05e972c85efdd9d97b771688a1cf61117594b
```

Pair `(2,3)` made 2,050 attempts and retained no new record. Pair `(2,4)`
made 2,050 attempts and retained 1,533 new records.

## Complete factor-free decoder

```text
columns=12962
parity_rank=12923
kernel_dimension=39
stored_and_tested_basis_vectors=39
basis_roots_plus_one=25
basis_roots_minus_one=4
basis_roots_non_global=10
full_root_image_size=4
full_root_image_rank=2
normalized_root_image_size=2
normalized_root_image_rank=1
gcd_tests=1808779225
refinements=87979
maximum_relation_value_bit_length=64
maximum_tested_basis_product_bit_length=25801
```

One computed basis root gave:

```text
root_mod_N=1058780986
root_squared_mod_N=1
gcd_root_minus_one_N=79043
gcd_root_plus_one_N=41011
gcd_product=3241632473
```

The terminal gcd values are outputs of root extraction. They are not replay
inputs.

## Write scope

- New or updated audit files:
  `MONOTONE_EXTENSION_verifier.py`,
  `MONOTONE_EXTENSION_run_with_timeout.py`,
  `MONOTONE_EXTENSION_OUTPUT.json`,
  `MONOTONE_EXTENSION_RUN.log`,
  `MONOTONE_EXTENSION_AUDIT.md`, and this manifest.
- Candidate files edited: none.
- Non-prefixed files edited: none.

## Frozen SHA-256 values

| File | SHA-256 |
| --- | --- |
| `CERTIFICATE.json` | `735a8535eb8cd4e8bc5e1c0fbc71d78b3acd79b3e6efa1f865d9084dea67cf6b` |
| `../F98_multiseed_presentation_closure_kill/public_factorization_free_replay.py` | `5fded40920ca52827662ba536f14a49ec9e302b934f6d0967e66be2b18c9ba4b` |
| `LAYER_INTERACTION_independent_verifier.py` | `7c1a12c6489f229e9ea146374b198bd683fbebe6228dcec0c427d2310b394d4c` |
| `LAYER_INTERACTION_OUTPUT.json` | `6b9c66ca97c47d1307212db9ba5fa299df3c66c3312af6ee8f110c9d3e8e52a8` |
| `MONOTONE_EXTENSION_verifier.py` | `428b81c6d49bbe7dd93b4063eee4786845ee00f55aedfefe843c708a9b23a78c` |
| `MONOTONE_EXTENSION_run_with_timeout.py` | `428e1031a592b2c493556f494fefa809fff8542492111a7fd4dcb730c2568e97` |
| `MONOTONE_EXTENSION_OUTPUT.json` | `f629bc58e14d3a21877f8642145ac6bab3ef1cf8d85a4589ba321eb219763095` |
| `MONOTONE_EXTENSION_RUN.log` | `bdb8f716db99ae3554aaaa64bb7adacf16ae754bf374537093644127ffce9c43` |
| `MONOTONE_EXTENSION_AUDIT.md` | `55bdaf32d841a47a5ad8ce4cb422eb80c4bb0d0bc6991699fd8eff50f3ab7b95` |

This manifest is not self-hashed.

## Exact boundary

The validated algorithm accepts `N`, derives its public frozen source, runs
the two fixed appended pairs to completion, computes a complete factor-free
square-class kernel, and tests every basis root. Its bit cost is polynomial in
the bit length of `N`. It factors `N=3,241,632,473`.

This does not prove useful-root existence for another input. It gives no
density, probability, expected-time, or all-input factoring theorem. It also
does not remove the historical post-selection of the fixed `(2,4)` trajectory.
