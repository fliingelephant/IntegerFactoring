# F100 corrected hostile re-audit

## Verdict: **FAIL**

The corrected computation passes. The matrix labels in the design, source,
and JSON output are now accurate. The output explicitly separates five
active-pair families from eight oriented trajectories. The result hash is
pinned, and the prior failed audit is unchanged.

Two local defects remain:

1. The main theorem paragraph in `RESULT.md` still says "odd-prime valuation
   matrix." The computed 230-row matrix includes prime 2. This sentence must
   say "prime-valuation parity matrix."
2. `RUN_MANIFEST.md` reports the old elapsed time, 1.966538 seconds. The
   corrected authoritative `RUN.log` reports 1.998962 seconds.

Neither defect changes the circuit arithmetic. They prevent a strict PASS
because the requested correction was to remove every mislabel and freeze the
corrected run accurately.

## 1. Corrected artifact pins

All expected corrected hashes match:

```text
3cca68e44691bd7e16488ba1073de471bf7dc8bae6ee1d62f87cb41a75b41c48  DESIGN.md
f31721cfeddcbea880719458c6d9c7cc67d9a1d35b3cca2da050725d5a7b9b74  RESULT.md
d997608bca403b9ce9a8a1e10298317fd483fb5d63cf7b546195d8117871ed2f  analyze_dependency.sage
9bcf6217f412f837fab8e3d0b832e01c80fbd5afa1d173156ec93df95bd94076  OUTPUT.json
753dfeaa57cd985a047f7d8a6d5dbccc9da3e838132b9251202f70deada10200  RUN.log
6eba6f30220e6a56ff1bd7f4129092c828303bf257259d239159d61ed7720b4a  FAILED_RUNS.md
88c429719d757cf812719b43630ab7924f333bf1c1c8824a427de3832a9ff817  run_with_timeout.py
```

The corrected manifest hash is:

```text
c27a8d3c169d2f9117491f10961eb27d8e23b68c24cbce37816ebb5a627858b0  RUN_MANIFEST.md
```

I read the corrected design, result, manifest, source, output, run log, and
failed-run note in full. This includes all 6,969 lines of `OUTPUT.json`.

The prior hostile audit remains unchanged:

```text
50bd1b5ac7bce7fbcd153bf6cef80bdcd783d0e65b4341eef48f92e112524ee8  AUDIT.md
```

## 2. Matrix naming correction: partial PASS

The corrected design now requests a "prime-valuation parity matrix." It
calls its rows "parity-prime rows" and defines connectivity through shared
odd-valuation prime support. These terms clearly include prime 2 when its
valuation is odd.

The corrected source follows that definition:

- `odd_supports` became `parity_supports`;
- `odd_primes` became `parity_primes`;
- `odd_prime_row_count` became `parity_prime_row_count`;
- `pairwise_odd_support_intersections` became
  `pairwise_parity_support_intersections`; and
- each factorization now reports `odd_valuation_support`.

The corrected JSON contains only the new keys. It contains no old matrix or
support key.

Most of `RESULT.md` is also correct. It says that the matrix has 230 rows,
explicitly includes prime 2, and uses parity-prime support. However, its
first claim still reads:

> Their odd-prime valuation matrix has rank 165 and nullity one.

Under ordinary mathematical usage, "odd-prime" excludes 2. This is the exact
mislabel that the first audit rejected. The source and output did not compute
an odd-prime-only 230-row matrix.

Required replacement:

> Their prime-valuation parity matrix has rank 165 and nullity one.

## 3. Oriented trajectories: PASS

The correction now distinguishes the two provenance levels.

`RESULT.md` says "five active-pair families spanning eight oriented
trajectories." The source emits both `active_pair_family_counts` and
`oriented_trajectory_counts`. The output gives exactly eight nonzero
oriented trajectories:

```text
index 9,  (11, 36824929),  u_power_times_v:  15
index 11, (13, 124638221), u_power_times_v:  10
index 12, (2, 5),          u_power_times_v:  32
index 12, (2, 5),          u_times_v_power:  22
index 15, (2, 17),         u_power_times_v:  38
index 15, (2, 17),         u_times_v_power:  15
index 25, (3, 17),         u_power_times_v:  15
index 25, (3, 17),         u_times_v_power:  18
```

These counts total 165 feedback relations. Together with one initial seed
relation, they give the 166-value circuit. This prior failure is fully fixed.

## 4. Result pin and failed audit: PASS

The manifest now pins the corrected `RESULT.md` hash:

```text
f31721cfeddcbea880719458c6d9c7cc67d9a1d35b3cca2da050725d5a7b9b74  RESULT.md
```

The old failed `AUDIT.md` retains its exact prior hash. `FAILED_RUNS.md`
also records the additional corrected-source Sage-cache failure. It does not
use that failed run as evidence.

## 5. Authoritative run metadata: FAIL

The corrected source predates `OUTPUT.json` and `RUN.log`. The runner used a
hard 120-second timeout and exited zero. Its corrected log says:

```text
elapsed_seconds=1.998962
exit_code=0
```

The manifest instead says:

```text
elapsed_seconds=1.966538
```

That value came from the prior run. The current manifest pins the corrected
run log but describes a different elapsed time. Replace 1.966538 with
1.998962.

## 6. Fresh corrected-output replay: PASS

I wrote a new corrected-output-aware Sage verifier. It does not import the
candidate source. It independently:

- validated and factored all 166 exact relations;
- rebuilt the 230-row prime-valuation parity matrix;
- reproduced rank 165 and nullity one;
- checked all 166 one-column deletions for circuit minimality;
- reproduced both degree histograms;
- verified connectivity with and without the prime-2 row;
- reproduced five active-pair families and eight oriented trajectories;
- compared every corrected JSON key and every reported factorization; and
- recomputed the square root and the factors 19,727 and 10,267.

The final command was:

```text
/usr/bin/time -p /opt/homebrew/bin/timeout 120 /usr/local/bin/sage \
  reaudit_dependency_verifier.sage \
  --input ../F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json \
  --candidate-output OUTPUT.json \
  --output REAUDIT_VERIFY_OUTPUT.json
```

It exited zero in 2.06 seconds. The source predates its output and log.

```text
522e14ee992d76b20298407edc876df353d00384817a2f37850c04f22c408e3c  reaudit_dependency_verifier.sage
a72eb92e65d0a55eb7be58866c42256e958ee6b09076163c860f6d90004c0555  REAUDIT_VERIFY_OUTPUT.json
0ba288f481c98d2c45e5ec2f7fabb9ea6bd4f39491f824591e7a674e3cb695d0  REAUDIT_VERIFY_RUN.log
```

## 7. Exact mathematical scope

The corrected arithmetic still proves this fixed finite statement:

- the 166 selected exact values are distinct;
- their prime-valuation parity matrix has rank 165 and nullity one;
- the all-column dependency is a binary matroid circuit;
- its parity-support graph is connected;
- it spans five active-pair families and eight oriented trajectories; and
- its exact square root exposes both factors of the fixed modulus.

The circuit is minimal only inside this selected 166-value set. F100 does
not prove minimum support in the full 9,414-value pool, an all-input law, an
inverse-polynomial density, publication-level novelty, or a polynomial-time
factoring algorithm.

## Exact correction required

1. In the main theorem paragraph of `RESULT.md`, replace "odd-prime
   valuation matrix" with "prime-valuation parity matrix."
2. In `RUN_MANIFEST.md`, replace `elapsed_seconds=1.966538` with
   `elapsed_seconds=1.998962`.
3. Update the result hash in the manifest after the first edit.

No source, output, arithmetic, or new factorization run is required for
these two text corrections.

## Final decision

**FAIL.** The corrected computation and the eight-trajectory result pass.
One old matrix label remains in the headline result, and the manifest still
contains the old runtime. After those exact text fixes, the mathematical
candidate is ready for a final frozen re-audit.
