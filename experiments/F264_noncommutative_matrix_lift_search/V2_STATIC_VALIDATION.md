# F264-D02 independent static validation

These checks occurred before the final V2 hash freeze. They are not a C++
compile, self-test, benchmark, or cohort run.

## Exact combinatorial unranking

An independent Python integer model exhaustively compared the V2 pair and
triple unranking formulas against lexicographic combinations for every
`3 <= n <= 79`. It returned

```text
UNRANK_EXHAUSTIVE_PASS n=3..79
```

This checks the formulas and boundaries. The C++ self-test separately freezes
collision-free samples. Target C++ validation remains mandatory.

## Nullspace controls

An independent exact-integer model reproduced the frozen SplitMix64 samples,
matrix products, section carries, all five feature matrices, modular RREF, and
the complete normalized ternary enumeration. It returned

```text
IDENTITY_CONTROL_PASS ranks=5/6,5/6,1/2,2/3,1/2 nulls=1,1,1,1,1
```

The five normalized vectors were exactly

```text
(1,-1,-1,-1,1,1)
(1,1,1,-1,-1,-1)
(1,-1)
(1,-1,1)
(1,-1)
```

This catches the V1 zero-vector and four-column associator failures without
opening any semiprime cohort. It does not authenticate C++ compilation,
Boost behavior, source-to-model transcription, the full public input pipeline,
runtime, memory, or output. The frozen runner must still pass all target gates
after a fresh hostile audit and after F258--F263 are absent.
