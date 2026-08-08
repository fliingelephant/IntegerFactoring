# Proof-blind reconstruction of the fixed cross-layer certificate

## Verdict: PASS

The supplied 363 indices verify one exact cross-layer dependency for
`N=3241632473`.  Its positive square root is non-global modulo `N`.  The two
terminal gcds are 79,043 and 41,011.

This is a fixed-instance verification with external advice.  It is not a
selector, a probability result, or an all-input factoring algorithm.

## Isolation

The reconstruction used only these authorized inputs:

```text
e1a573feaceb2465d599df21a41b46372c25c6c30cb15ad7d1b6c56230fe0dae  RECONSTRUCT_STATEMENT.md
8622024473bd602d1d4928fad959099db1ae463e9bd736b7b6ec59fbb99c3f61  RECONSTRUCT_INPUT.json
```

It did not inspect any other F111 file.  It did not inspect an F98, F109, or
F110 file.  It did not import or execute another implementation.

## Trial screen

The verifier computed all 1,023 gcds for `2 <= t <= 1024`.  Every gcd is one.

## Deterministic seed basis

The 31 seeds produce 62 endpoints.  The ordered stack algorithm gives these 23
blocks:

```text
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
3595103, 12214847, 20010077, 24880951, 58995227,
69463553, 116496167, 287564171, 305094821,
514544837, 736734653, 2992276129
```

The blocks are pairwise coprime.  None is a perfect power.  Their signatures
reconstruct all 62 endpoints exactly.

The operation counts use the definitions in the output file:

| Operation | Count |
|---|---:|
| Initial stack items | 62 |
| Generated stack pushes | 402 |
| Stack pops | 464 |
| Maximum stack size | 66 |
| Unit discards | 69 |
| Perfect-power exponent tests | 3,467 |
| Perfect-power extractions | 19 |
| Extracted exponent sum | 51 |
| Ordered basis gcd tests | 6,234 |
| Overlap events | 186 |
| Identical merges | 114 |
| Nonidentical splits | 72 |
| Basis appends | 209 |
| Final signature entries | 129 |

The resulting frozen-pair list is:

```text
(2,3), (2,3), (2,5), (2,5), (2,3), (2,5),
(2,3), (2,3), (2,5), (2,11), (2,3), (13,2992276129),
(2,5), (2,3), (2,3), (5,17), (2,3), (2,3),
(2,5), (3,7), (2,11), (2,3), (2,3), (2,3),
(2,3), (2,3), (2,5), (2,3), (2,3), (2,31), (2,5)
```

## Ordered trace

The complete frozen layer has:

```text
retained records = 14351
residue attempts = 63581
duplicate residues = 49230
```

The exact public stop has:

```text
retained records = 15383
residue attempts = 67013
duplicate residues = 51630
last pair = (2,4)
last exponent = 690
last orientation = u_times_v_power
last appended-pair index = 1
```

The ordered trace hash is:

```text
63fe6c0bdd1f44a7fe39edb3187cd1e8fd62760660056b27c757c8b4d3f636d4
```

## Direct sign screens

No retained record gives a proper divisor through a direct endpoint screen.

- The minus screen is one on 15,382 records.
- The plus screen is one on all 15,383 records.
- One minus screen is nonunit but improper.

The exceptional record has index 6,166.  It has `c=w=1`.  Therefore
`gcd(c-w,N)=gcd(0,N)=N`.  Its provenance is frozen pair index 11,
`(u,v)=(13,2992276129)`, exponent 1, orientation `u_power_times_v`.

This explains every nonunit direct screen.

## Advised support

The index list has 363 entries.  It is strictly increasing and duplicate-free.
Every index is in range.  Its last index is 15,382, the final retained record.

The selected provenance split is:

```text
frozen_seed_basis_pair = 327
nonadaptive_seed_pair = 36
```

All 36 appended records come from appended-pair index 1, pair `(2,4)`.  Thus
the selected support contains both the frozen and appended layers.  All 363
selected exact relation values are distinct.

## Exact square and terminal gcds

The verifier multiplied the selected exact relation values and used integer
square root.  It did not decompose a selected value.

```text
selected product bit length = 21620
selected product byte length = 2703
selected product SHA-256 = 8064402fc9533bf262ba6442f8d4aea76199ce1f1985be44c25294c0b3ba0f6f
positive root bit length = 10810
positive root byte length = 1352
positive root SHA-256 = 8dcd461e6c415f61efadfc6c333fffb8d0cfe8ecae99c7ff5da65cea4dd833e2
```

The hash encoding is an 8-byte unsigned big-endian payload length followed by
the minimal unsigned big-endian integer payload.

The exact checks give:

```text
product is an exact square = true
product mod N = 1
root mod N = 1058780986
root^2 mod N = 1
root is globally +1 or -1 = false
gcd(root-1,N) = 79043
gcd(root+1,N) = 41011
```

Both gcds are proper divisors.  Their product is `N`.

## Factor-free boundary

The reconstruction used exact integer arithmetic, modular powers, modular
inverse, gcd, exact perfect-power extraction, integer square root, and SHA-256.

It did not use general integer factorization.  It did not factor endpoints or
relation values.  It did not test primality.  It did not use a known divisor of
`N`.  The proper divisors first appear as the two terminal gcd results.

The source trace does not use the advised indices.  The verifier applies them
only after it generates the final retained record.  The advice proves that this
one support exists.  It does not explain how to find such a support from `N`.

## Run status

The named 120-second runner completed without a failed attempt.  The final
authoritative rerun gives:

```text
elapsed_seconds=0.143313
timed_out=false
exit_code=0
status=PASS
```

No failed attempt exists.
