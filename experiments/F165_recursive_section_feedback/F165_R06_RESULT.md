# F165-R06 corrected reconstruction and hostile comparison result

Status: completed registered finite workflow. Both sequential stages passed.
The authorized command ran exactly once. It was not rerun.

## Verdict

Finite exact reconstruction: **PASS**.

- R06 reproduced all stated finite counts and certificates.
- All complete D01/R06 candidate sequences match.
- All complete D01/R06 exact-value sequences match.
- All complete D01/R06 block sequences match.
- All complete D01/R06 selected-column sequences match.
- All adjacent decoder summaries now match.
- The comparison found zero mismatches.

Fixed-depth proof hostile audit: **PASS**. The audit found no gap in the stated
fixed-`H` quasipolynomial cost theorem. It found no growing-depth or success
theorem.

This report does not promote a durable claim. The root agent must apply the
repository's verification-cadence and ordering rules.

## Frozen and generated artifact hashes

| Artifact | SHA-256 |
|---|---|
| R06 reconstruction source | `252123931d35856febfd93c07c8e22072564bf6310d75093d5eb169a07f09838` |
| R06 comparison source | `fa2742f2562f2288f7c93114fb4f02d1a6691ab920c46b62fbae23dfd4285c7b` |
| R06 runner | `dd048920430b9003dcdcd498e3de9e2c44026703a9d8b7e026ff712732eacf0f` |
| R06 frozen expected outputs | `f4b066fbb1580a67846538c2381e9b7a377ad00225b9116fa3aaffa709eb1c68` |
| R06 source provenance | `14e0f62f90205f5a26f9215cdc175b3bf5b365e81c3ba45721069b403d0d0589` |
| R06 preregistration | `5f0bc98cf8446a99b2844bd88fb05895309c605803e889dc10302f2525a68829` |
| R06 log | `205cd56cc98c8fdc00dc2bab6f007073eab2117033991924d899a3b0efed0d00` |
| R06 reconstruction output | `95b4ba37651dd5cc3644ad4281be5622e92392448b4b4865214b6c888d14f19c` |
| R06 comparison output | `0cad4cc8c0fc1c4a2af98c9532249a4e6e734cc970c202993d89f1cbfbebb610` |
| Fixed-depth hostile audit | `982c667b7d7fde8b3832ea4db131341835fee26ba734d07d23633622be9c83e4` |

The source, comparison, runner, expectations, provenance, and preregistration
hashes after execution equal their registered pre-run hashes.

Authoritative command:

`python3 /Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r06_timeout_runner.py`

The total registered timeout was 600 seconds. The estimated peak memory was
256 MiB. The reconstruction child exited 0. The comparison child exited 0.
The runner recorded `workflow_status=PASS`.

## Complete comparison coverage

| Check | Count | Mismatches |
|---|---:|---:|
| Inputs | 64 | 0 |
| Base/feedback snapshots | 192 | 0 |
| Candidate entries | 15,644 | 0 |
| Exact-value entries | 3,220 | 0 |
| Block entries | 4,323 | 0 |
| Selected-column entries | 3,089 | 0 |
| D01 feedback candidate digests | 128 | 0 |
| D01 exact-value digests | 192 | 0 |
| D01 block digests | 192 | 0 |
| D01 selected-column digests | 192 | 0 |

The comparison output has `status=PASS`, `mismatch_total=0`, and
`first_mismatch=null`.

## Exact R05 repair

R05 proved that R04 omitted one retained `A=1` zero parity column at every
feedback snapshot. R06 moved the `A>1` filter from complete column construction
to factor-free refinement inputs.

The registered R06 comparison confirmed the complete expected effect:

- 64 base snapshots stayed unchanged from R04;
- 128 feedback snapshots retained the `A=1` zero column;
- columns, nullity, and global-plus count increased by one at each feedback
  snapshot and now equal D01;
- rows, rank, global-minus count, and non-global count stayed unchanged;
- every candidate, exact-value, block, and selected-column sequence stayed
  unchanged from R04.

Thus the repair changes only the previously omitted trivial kernel column. It
does not change feedback generation or any substantive finite factor outcome.

## Sequence certificates

| Sequence | Normalized detailed SHA-256 |
|---|---|
| Candidate | `96972dcb941ca98ed1fd45bda9e75cb5b5b79e27317d6b2f3767d60ba7b60f88` |
| Exact value | `b17a5884e2017f2f47d2e3b268a1220d0aab6c6be2f69df7a2160373cefbd08c` |
| Block | `bda32c2be9c39b5616c168c250ca6a3596f4be6ecda20cee2015c785a17ea1df` |
| Selected column | `23eaa0350432570c030c5648e6bc85401d3402a054482450686df61cf0d632df` |

These are also the R04 detailed aggregate hashes because R06 intentionally
does not change any of the four sequences.

## Fixed-depth theorem audit

The hostile audit independently checked:

- the subset-count recurrence;
- all generated integer and metadata lengths;
- the invariant, termination potential, component count, and bit complexity
  of multiplicity-aware gcd/perfect-power refinement;
- complete Gaussian elimination and kernel decoding;
- exact dependency-product lengths and signed gcd tests;
- time and space induction through fixed `H`;
- the effect of retained zero parity columns;
- the failure of the same argument to give a uniform growing-depth bound.

It returned PASS for the exact fixed-depth theorem. The full argument and two
nonfatal precision notes are in `F165_R04_FIXED_DEPTH_HOSTILE_AUDIT.md`.

## Scope

The finite replay is not a density law, minimum-depth law, all-input success
law, or presentation-complete endpoint grammar. The theorem is only a cost
bound for each fixed number of layers. Neither result supplies a factoring
algorithm or resolves the top-level task.
