# F115 — hostile audit of the F112/F113/F114 corpus claim

## Verdict

**The six requested bounded propositions pass.  The candidate artifacts fail
one aggregate consistency check.**

An independent SageMath/Pari replay reproduces every per-case F112, F113, and
F114 field used by the claims.  It imports no candidate implementation.

F112's authoritative JSON nevertheless says `direct_factor_cases = 33`.
That field is false.  It subtracts the 67 parity cases from all 100 cases and
therefore counts the 14 nulls as direct factors.  The correct split is:

```text
67 parity factors + 19 direct factors + 14 nulls = 100
19 direct factors = 12 minus-gcd + 7 plus-gcd
```

The prose result gives the corrected count.  Thus the audit verdict is
**FAIL as written, PASS after correcting that aggregate field**.

## Independent method

The verifier:

1. reads every F104 `*OUTPUT.json` file;
2. independently applies the declared corpus predicate and file exclusion;
3. prime-certifies each selected `p,q` with Sage and checks trial hardness and
   the stability equation;
4. reconstructs the initial endpoint-signature blocks with Sage/Pari endpoint
   factors;
5. independently reimplements residue generation, global deduplication,
   direct screens, incremental GF(2) decoding, square roots, and gcd tests;
6. replays all 100 frozen-plus-`(2,v)` cases; and
7. continues all 14 nulls through the full lexicographic all-pair menu.

All candidate pins match.  Every independent per-case projection matches.

## Corpus result and selection boundary

Among completed, non-running F104 output files, the predicate finds 101
qualifying rows and 100 distinct moduli.  The duplicate is the exact and
accelerated observation of `N = 3,241,632,473`.  The F112 case order, source
file, factors, and first-round kernel dimension match exactly.

Every selected case is a distinct stable trial-hard semiprime.  Its reported
first-round kernel is nonzero.  Every reported basis root is `+1`; no selected
basis contains `-1` or a non-global root.

The phrase “all completed F104 cases” needs the declared file-level qualifier.
F112 excludes `PRIME_SCAN_320K_640K_WIDE_OUTPUT.json` because that file has
status `running`.  It nevertheless contains 86 qualifying completed rows.
Twenty-four overlap the 100-case corpus.  Sixty-two are additional distinct
cases.  F112 did not test them.

The exact corpus statement is therefore:

> F112 tests all 100 distinct qualifying rows from completed, non-running F104
> output files, after explicitly excluding the interrupted wide file.

It is not the set of every qualifying completed row present anywhere in the
F104 directory.

## F112 result

The independent replay gives exactly:

| n | cases | `(2,v)` factors | nulls |
|---:|---:|---:|---:|
| 32 | 1 | 1 | 0 |
| 34 | 5 | 5 | 0 |
| 36 | 14 | 14 | 0 |
| 38 | 27 | 27 | 0 |
| 40 | 33 | 33 | 0 |
| 42 | 6 | 6 | 0 |
| 46 | 7 | 0 | 7 |
| 50 | 7 | 0 | 7 |

Thus the fixed frozen-plus-`(2,v)` source factors exactly 86 corpus cases.  Its
14 nulls are exactly the seven 46-bit and seven 50-bit cases later pinned by
F113 and F114.  Each null replay exhausts every `v = 3..n`.  Every emitted
dependency remains global.

The aggregate bug is at
`stress_frozen_two_v.py:189`: `len(completed) - len(parity_cases)` counts both
direct and null outcomes.  This audit does not modify the candidate.

## F113/F114 result

The fixed source is the same frozen layer followed by every unordered seed
pair in lexicographic order.  The independent replay factors all 14 cases at
the same pair, relation prefix, support size, root, and proper gcd as the
candidate.

| N | pair | support | frozen / appended | distinct appended pairs | outside final pair |
|---:|---:|---:|---:|---:|---:|
| 50,000,764,992,341 | `(3,19)` | 2,265 | 1,013 / 1,252 | 41 | 2,247 |
| 50,001,624,955,573 | `(3,20)` | 2,288 | 969 / 1,319 | 49 | 2,283 |
| 50,001,724,887,113 | `(3,20)` | 2,444 | 999 / 1,445 | 48 | 2,443 |
| 50,002,154,865,017 | `(3,19)` | 2,492 | 1,390 / 1,102 | 46 | 2,488 |
| 50,002,584,754,033 | `(3,20)` | 2,405 | 1,213 / 1,192 | 45 | 2,398 |
| 50,002,694,807,489 | `(3,20)` | 2,571 | 1,346 + 1 seed / 1,224 | 44 | 2,524 |
| 50,002,744,708,409 | `(3,17)` | 2,240 | 1,209 / 1,031 | 42 | 2,233 |
| 799,999,779,999,949 | `(4,7)` | 3,696 | 1,653 / 2,043 | 60 | 3,693 |
| 800,000,499,996,757 | `(3,50)` | 3,885 | 1,514 / 2,371 | 66 | 3,870 |
| 800,000,739,995,221 | `(3,46)` | 3,792 | 1,746 + 1 seed / 2,045 | 68 | 3,783 |
| 800,001,099,992,377 | `(3,50)` | 3,740 | 1,617 / 2,123 | 62 | 3,736 |
| 800,002,819,971,857 | `(4,7)` | 3,927 | 1,692 / 2,235 | 76 | 3,922 |
| 800,003,059,967,681 | `(3,50)` | 3,968 | 1,826 + 1 seed / 2,141 | 69 | 3,962 |
| 800,005,299,946,297 | `(3,49)` | 3,870 | 1,772 / 2,098 | 67 | 3,867 |

Every success is a parity dependency.  Every exact support contains both a
first-layer relation and a newly retained all-pair relation.  Each support
uses 54 to 92 distinct actual nonseed pair-menu keys and 41 to 76 distinct
appended pairs.  It contains only 1 to 47 relations from the final successful
pair and 2,233 to 3,962 relations outside it.

Therefore the displayed exact dependencies are genuinely cross-layer.  None
is a single residue, one final pair menu, or one trajectory artifact.

This does not prove that the frozen layer is necessary.  Some frozen residues
could be generated later by the all-pair menu.  It also does not make the last
pair a sole cause.  The precise term is the **trigger pair for the first useful
lexicographic prefix**.

## Source bound

The seed set `2..n` has `n-1` values.  It has

```text
C(n-1,2) = (n-1)(n-2)/2
```

unordered pairs.  Each pair supplies two orientations at every exponent
`0..n^2`, or `2(n^2+1)` positions.  The complete appended menu therefore has

```text
(n-1)(n-2)(n^2+1) = Theta(n^4)
```

residue positions.  The frozen first layer has `n-1` pair menus and
`2(n-1)(n^2+1) = Theta(n^3)` positions.  The stated `O(n^4)` source-cardinality
bound is correct.

This is not an `O(n^4)` bit-runtime proof.  Modular arithmetic adds bit cost,
and the candidate decoder calls integer factorization.

## Factor-assisted, order, duplicate, and finite boundaries

- **Factor assistance:** Sage/Pari in the audit and Pollard-rho in the
  candidate factor endpoint values.  The semiprime factors also certify and
  select the corpus.  No positive is promoted as N-only.
- **Selection:** the corpus is outcome-selected from bounded F104 scans.  The
  running wide file is excluded despite containing 62 additional distinct
  qualifying cases.
- **Order:** the successful pair and support refer to the fixed lexicographic
  prefix, increasing exponents, declared orientation order, and the decoder's
  pivot order.  Other orders were not tested.
- **Duplicates:** one global residue set spans both layers.  First provenance
  wins.  F112 discards 53.7% to 77.0% of attempted positions as duplicates.
  F113/F114 discard 45.9% to 54.8%.  Provenance and trigger labels depend on
  this order.
- **Finite scope:** the corrected statement covers these 100 selected moduli
  and no others.  It gives no all-input theorem, density, probability, or
  asymptotic success law.

## Narrowest valid statement

For the declared 100-case corpus and exact factor-assisted insertion order,
the frozen-plus-`(2,v)` source factors 86 cases and is null on exactly 14.  The
fixed lexicographic all-unordered-seed-pair source factors those 14.  Every
displayed parity support crosses the frozen/appended boundary and uses many
pair menus.  The appended source has `Theta(n^4)` residue positions.

The statement requires the explicit corpus exclusion and the corrected count
of 19 direct factors.  It is only a finite factor-assisted observation.

## Reproducibility

Run:

```text
python3 experiments/F115_all_pairs_global_corpus_audit/run_F115_hostile_audit_with_timeout.py
```

The authoritative run completed with exit code 0 in 276.732454 seconds.  The
inner verifier took 274.735095 seconds.  The hard timeout is 1,800 seconds.
One earlier audit assertion failure is preserved and documented separately.
