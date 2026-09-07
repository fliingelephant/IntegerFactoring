# F338 sources

**Family:** route:F31

No web source or external dataset was used.

| File | SHA256 | Use |
|---|---|---|
| experiments/F338_fair_count_branches/DESIGN.md | d5879d6b995e85ce8d95d702b848f6c3c2dda13dc7aa24cd888c39fad66e4acb | Frozen F338 execution design |
| experiments/F336_biased_rational_inputs/FAIR_BRANCH.md | ce8c57e5c3dbbb8cedcfa6ad6b1001cffde5ec305d6bec29d63295ca5f58f507 | Active fair-branch definition with both-child screening |
| experiments/F336_biased_rational_inputs/fair_branch_checks.py | 46ad21c1911c516ad760fa61262895499b6ebb0ca9c97943585c619be4dfcd4e | Active exact small DP comparator |
| experiments/F336_biased_rational_inputs/fair_branch_scale.json | cdcf9f098a8f3a9bcb05ece97e7e61f3c195b2c7607a3824e9aed9beb443e94e | Repaired N<=301 DP output used for the two pilot witnesses |
| experiments/F336_biased_rational_inputs/biased_rational_inputs.py | b660db8da032e3f514dfdfc5a4183defb5392b22d4cf8bcfa4ab9eaec57c5256 | Frozen source-law implementation |
| experiments/F336_biased_rational_inputs/aggregate_output.json | afca015f15169be06a080b1e000d02409251d73d8c5df59cbd0b269ac18b3801 | Frozen catalog of all 24 source-row artifacts |
| experiments/F334_count_descent/count_descent.py | cb93f160d57b2a3285551cbd268e732917e3062a90eb8ca62df843f581be1e24 | CountOracle, charged gcd, and minimum-child replay |
| experiments/F328_capped_rabin_paths/moduli.json | acf09b285c57c39cfcb93d3cd77addce909498e224955fd0ec9d2e4d86ee0428 | Public moduli and offline output labels |

The initial FAIR_BRANCH and DP version used an early-return child-gcd cost.
During F338 implementation, comparison with the frozen F336 solver exposed
that F336 actually charges both positive child screens. The root retained the
old files under experiments/F336_biased_rational_inputs/prior_early_return and
repaired the active definition and DP. F338 uses only the active hashes above.
The repair changes gcd costs, not branch success probabilities or query counts.

Every F336 row artifact is checked against the hash stored in the frozen
aggregate before transformation. The F338 branch seed uses a separate
33820260907 domain and the exact frozen row ID. Offline factors are attached
only after a public gcd has already returned.
