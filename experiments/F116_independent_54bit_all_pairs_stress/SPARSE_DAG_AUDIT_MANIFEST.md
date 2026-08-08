# F116 Sparse-DAG Hostile-Audit Manifest

## Verdict

```text
fixed_advised_factor_free_certificate=PASS
source_generation_through_advised_stop=PASS
residue_first_occurrence_dedup=PASS
all_direct_gcd_screens=PASS
candidate_performs_exact_value_dedup=FAIL
independent_exact_value_projection=PASS
sparse_elimination_and_DAG_mechanics=PASS
online_modular_half_root_invariant=PASS
reported_factor_split=PASS
candidate_factor_free_polynomial_time=FAIL
candidate_constant_or_linear_total_memory=FAIL
full_no_stop_complete_decoder=NOT_RUN
overall=PASS_WITH_CLAIM_BOUNDARIES
```

## Promoted run

```text
command=/opt/homebrew/bin/python3 experiments/F116_independent_54bit_all_pairs_stress/SPARSE_DAG_AUDIT_run_with_timeout.py
child_interpreter=/opt/homebrew/opt/python@3.14/bin/python3.14
hard_timeout_seconds=300
timed_out=false
exit_code=0
status=PASS
verdict=PASS_WITH_CLAIM_BOUNDARIES
outer_elapsed_seconds=4.833909
inner_elapsed_seconds=4.7629732500063255
```

Two preliminary named runs also passed. They took 4.403388 and 4.822484
seconds. They were superseded by stricter coordinate and theorem-boundary
fields. No independent-audit attempt failed.

## Decisive input policy

Before terminal gcd extraction, the verifier used only `N`, `n`, `B`, the
advised retained-record stop, and the advised support. It made no factorization
or primality call. It did not import or execute the candidate. It read the
known factors in the discovery output only after it computed both terminal
gcds.

The discovery run remains factor-assisted. The proof-blind reconstruction and
this hostile audit are factor-free advised certificate replays.

## Exact result

```text
N=12800004879996637
attempted_residues=1336218
duplicate_residues=565136
retained_raw_columns=771082
proper_direct_gcds=0
unit_exact_columns_removed=1
duplicate_exact_columns_removed=148930
unique_nonunit_exact_columns=622151
raw_to_exact_kernel_dimension=148931
raw_support_size=6486
projected_support_size=6486
selected_values_first_occurring_outside_support=0
each_value_first_occurs_at_its_selected_raw_record=true
dedup_column_numbers_equal_selected_raw_indices=false
root_mod_N=5266287723884331
gcd_root_minus_one_N=159999943
gcd_root_plus_one_N=80000059
gcd_product=12800004879996637
```

All unit and duplicate-value projection-kernel directions have root `+1`.
The raw and projected advised supports have the same exact product and the
same non-global root.

## Advice and extension boundary

- The promoted replay needs the stop and 6,486 support indices.
- The sparse candidate discovers its support with endpoint factorization. It
  does not exact-value deduplicate.
- Raw residue-stream append monotonicity preserves the advised raw columns.
- Exact-value append monotonicity preserves the independently projected
  useful dependency.
- The no-stop/no-support corollary is promoted only at the P66
  useful-dependency-existence level.
- The full 1,378-pair source and separate complete factor-free decoder were
  not run.
- No all-input theorem follows.

## Failure accounting

The five recorded discovery failures remain present:

1. `RUN_FAILED_20260808T031223Z_EXIT_1.log` and its checkpoint: sandbox
   process-pool denial.
2. `RUN_FAILED_20260808T034426Z_TIMEOUT.log` and its checkpoint: 1,800-second
   Python endpoint-factorization timeout.
3. `SAGE_RUN_FAILED_20260808T035310Z_EXIT_137.log` and its checkpoint: one
   provisional case, then signal 9.
4. `SINGLE_CASE_RUN_FAILED_20260808T035917Z_EXIT_1.log` and its no-output JSON:
   forbidden Sage cache write.
5. `SINGLE_CASE_RUN_FAILED_20260808T040103Z_EXIT_137.log` and its no-output
   JSON: dense isolated replay killed for memory use.

The sparse discovery, proof-blind reconstruction, and hostile audit had no
preserved failed attempt.

## Write scope

This hostile audit added or updated only:

- `SPARSE_DAG_AUDIT_verifier.py`;
- `SPARSE_DAG_AUDIT_run_with_timeout.py`;
- `SPARSE_DAG_AUDIT_OUTPUT.json`;
- `SPARSE_DAG_AUDIT_RUN.log`;
- `SPARSE_DAG_AUDIT_REPORT.md`;
- this manifest.

It did not edit a candidate file or durable project ledger. The separately
created `RECONSTRUCT_*` artifacts are corroborating evidence, not hostile-audit
writes. Transient `__pycache__` bytecode is not evidence and is not pinned.

## SHA-256 pins

### Registered design and public reconstruction input

| File | SHA-256 |
| --- | --- |
| `DESIGN.md` | `533f92d1e79cf81ef4e3841b48fbddd527571a944b3fced5c131b6148034c803` |
| `FAILED_RUNS.md` | `3b6bfce1f2b6ceae997fd75f3fb21ba7102b9096e2744251da3eca803a4842d2` |
| `RECONSTRUCT_STATEMENT.md` | `f402a39c9d751a72c93a46b28ab593c5a1e8a03ed4c9bdc97655b310c01e8983` |
| `RECONSTRUCT_INPUT.json` | `5194ee596916810edb78fa802c3179341746423c6fb65f2548a600c598b05015` |

### Original candidate sources, runs, and failures

| File | SHA-256 |
| --- | --- |
| `stress_independent_all_pairs.py` | `a247b467f4d9a9a664187e36ed435d88e4935b69ec197444d579935157706431` |
| `run_with_timeout.py` | `e1d3f214802c014f7780c4b38d5dde8450f5473fef103474f1e8e46b09a60328` |
| `OUTPUT_FAILED_20260808T031223Z_EXIT_1.json` | `bd34af75e014177d31d33a792a9b33495b82def8eeada416258a494819e13537` |
| `RUN_FAILED_20260808T031223Z_EXIT_1.log` | `d19c6a395f217799cb40ee6fdb636248b9c956aab370bbd3a591a2bf0bb75b06` |
| `OUTPUT_FAILED_20260808T034426Z_TIMEOUT.json` | `4188e31d6be11cd7a13767eafd6082436ed4fec9926e98366398b968e5c6c6fa` |
| `RUN_FAILED_20260808T034426Z_TIMEOUT.log` | `187f5c9bdd6edef1d85327f6be7030355ed3e1be6ed7d4f53372f0e3538004f8` |
| `stress_independent_all_pairs_sage.py` | `c8c68de07f7034e47ff92f4666d436f849ff49a4a84e01141c91b7a39c1203b5` |
| `run_sage_with_timeout.py` | `55c8d351014ab00c27572235dcab7b791a8caa62d27ec72cf927f2aefce7c13e` |
| `SAGE_RETRY.md` | `1d660c8842f5e062ec7fc26950af4e52bc7f6913efb6e922c256c91bf809c600` |
| `SAGE_OUTPUT_FAILED_20260808T035310Z_EXIT_137.json` | `d8f17ce592d8eb3519f58dbb147b5fb0f1f924397c41c870fe3307d96c07c2f8` |
| `SAGE_RUN_FAILED_20260808T035310Z_EXIT_137.log` | `1a9cbb59c8ceccd3a5f9517318856a996030f0f0e996da1193b210b1fc406704` |
| `replay_first_case_sage.py` | `0b2a6cd8705490821bb12d60667425bbaad275c230c33b556ba233defa81ced7` |
| `run_single_case_with_timeout.py` | `af9c1ff8bbf80b58f39340ffd54c5b2dab0f60a55c5169acc9d4848b9be7c4b1` |
| `SINGLE_CASE_OUTPUT_FAILED_20260808T035917Z_EXIT_1.json` | `a418d7db9f17dd9548f429a9c671b2871df7db4ebbff70f2cfb8cdb6d0877400` |
| `SINGLE_CASE_RUN_FAILED_20260808T035917Z_EXIT_1.log` | `bd659a282e1a696d3e8cd608eaea17b6f722dfff88818556d81d35e1c4201ef7` |
| `SINGLE_CASE_OUTPUT_FAILED_20260808T040103Z_EXIT_137.json` | `a418d7db9f17dd9548f429a9c671b2871df7db4ebbff70f2cfb8cdb6d0877400` |
| `SINGLE_CASE_RUN_FAILED_20260808T040103Z_EXIT_137.log` | `b1af92cdabb75fc8f84d74dee6a3c549aa9693657812e630df125235d8c99b11` |
| `stress_sparse_dag_first_case.py` | `7a65e664d9cdca422da47a5d26bd22432ce2eee5c61f8b3db5541bd348e81b84` |
| `run_sparse_dag_with_timeout.py` | `99b611086dcf73caed37cd65ebea82ff4eb772269b193135ad0fd2fdbc20b17b` |
| `SPARSE_DAG_OUTPUT.json` | `17f909113a0777695adec24c9e5619eaef1fec2327987e7e26c3212d04397671` |
| `SPARSE_DAG_RUN.log` | `6f5542bc618f921ff81129939509a1e47d694dc1c0492a7da050b4cc0885f542` |

### Proof-blind corroboration

| File | SHA-256 |
| --- | --- |
| `RECONSTRUCT_decoder_v1.py` | `9941d108483ab52947168860c33c1e6429d4f95f61da8adeccf42bf750fec187` |
| `RECONSTRUCT_run_with_timeout_v1.py` | `994520fbdf876902d13c5832bd67d665803b1488852d67911aee6ae6919d8bd2` |
| `RECONSTRUCT_OUTPUT.json` | `da4401738fcb1bcc2b2c32b6857f6a1434c1a457edcae860ab7756c262115439` |
| `RECONSTRUCT_RUN_V1.log` | `133447678dc0ceee31df4972750aff6671db6d2787eb60a20759bfb3913641d2` |
| `RECONSTRUCT_REPORT.md` | `6f02b2573997faf9eb723a68bbd20ab9ad25961715dcaf4b94a124310aadd4ee` |
| `RECONSTRUCT_MANIFEST.md` | `8aa4d913759c14ffdde76063b889b74759d58dc10102e1c4c6a8fe0234dc196b` |

### Hostile audit

| File | SHA-256 |
| --- | --- |
| `SPARSE_DAG_AUDIT_verifier.py` | `b874b476fbb4902fbdd90334c73327ed0f6193d56f81ea95ddd0333ef732bc3f` |
| `SPARSE_DAG_AUDIT_run_with_timeout.py` | `80f64306a3e1b0d2efc45208bd0d5c230656110ced87818af40e54864c42cf0e` |
| `SPARSE_DAG_AUDIT_OUTPUT.json` | `e25bbbeb6453230753ea569bba8d9b2d2dc97b59088c37988056c4472768cab4` |
| `SPARSE_DAG_AUDIT_RUN.log` | `e6b23b68b264287beab82ff233b9020bf264dc2da58df5f310e0656e4558921f` |
| `SPARSE_DAG_AUDIT_REPORT.md` | `020b8cc8c9c8c15fb9a42186496ffb20e7302519ffa5ec2319c24ae62b9c1cd6` |

This manifest is not self-hashed.
