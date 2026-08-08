# F98 proof-blind reconstruction

## Verdict: PASS

The factor-free public replay reproduces every declared count and both declared
166-value witnesses. The separate factor-aware audit also passes. No file other
than `RECONSTRUCTION_STATEMENT.md` supplied the mathematical construction.

## Artifacts and execution

Public artifacts:

- `RECONSTRUCT_public.py`: N-only, factor-free source.
- `RECONSTRUCT_public.log`: complete run log.
- `RECONSTRUCT_public.json`: structured result and strict claim checks.
- `RECONSTRUCT_FREEZE.sha256`: freeze manifest made before the factor-aware
  audit source was created.

The public command was:

```text
python3 RECONSTRUCT_public.py \
  --output RECONSTRUCT_public.json \
  --log RECONSTRUCT_public.log \
  --timeout-seconds 1800
```

`RECONSTRUCT_public.py` installs an operating-system wall-clock timer with
`setitimer(ITIMER_REAL, 1800)`. A timeout exits with status 124. The successful
run exited with status 0 in 9.778 seconds.

The frozen SHA-256 values are:

```text
a4349609c99a12b12a5ebcf29aba2939eb9d38ba08353ff28048dbc3db6d4482  RECONSTRUCT_public.py
573b614605f45d5449a25bb73367afdb9d541404942da61685d56c428683e184  RECONSTRUCT_public.json
96a02cc899d9a4075b3b84bb2dbbb673c52614ee840f57a1859d127baf17ef26  RECONSTRUCT_public.log
```

The separate audit artifacts are `RECONSTRUCT_audit.py`,
`RECONSTRUCT_audit.log`, and `RECONSTRUCT_audit.json`. The audit first checks
all frozen hashes. Only then does it use the two factors returned by the public
gcds. It has its own 60-second hard timeout. It exited with status 0.

## Reconstructed algorithm

The replay implements the seven public steps literally. One grammatical point
is important in step 4. “Nonzero modulo two” decides whether a seed column is
eligible. The following unqualified “support” is the support of its full
integer exponent column. Thus a block with positive even exponent can be one
of the two smallest supported blocks. This interpretation gives the declared
trajectory count without a target residue, target class, or factor data.

The gcd basis is a deterministic refinement DAG.

1. Each positive endpoint starts as one node.
2. If two active nodes have gcd `g > 1`, each node is replaced by the exact
   product of `g` and its quotient as needed.
3. New children are refined again. The active leaves therefore remain
   pairwise coprime.
4. A seed leaf which is an exact perfect power is replaced by repeated copies
   of its maximal exact integer root. Exact roots use integer binary search.
5. Every endpoint retains a DAG path to the final leaves. Expanding that path
   recovers its complete exponent vector, including multiplicity.

No factorization, primality test, order, discrete logarithm, or preselected
dependency occurs in the public source. The public arithmetic decomposition
uses only integer gcd, exact roots, multiplication, modular multiplication,
and modular inversion.

The decoder assigns a row to each nonsquare final gcd-basis block. It omits an
exact-square block. Columns and kernel combinations are Python integer bitsets.
Columns arrive in the prescribed seed/trajectory order. Online elimination
uses the lowest numbered nonzero row as pivot. Every dependent column gives
one kernel vector. The unique latest column in each such vector proves that
these vectors are independent. Their number is `columns - rank`, so they form
a full kernel basis.

## Public numerical evidence

| Check | Result |
|---|---:|
| `N`, `n`, `B` | 202,537,109; 28; 784 |
| Trial-screen proper gcds | 0 |
| Retained seed relations | 27 |
| Seed sign-screen proper gcds | 0 |
| New first-occurrence trajectory relations | 12,522 |
| Total processed retained residues | 12,549 |
| Trajectory sign-screen proper gcds | 0 |
| Removed `P = 1` values | 1 |
| Removed repeated exact `P` values | 3,134 |
| Distinct nonzero decoder columns | 9,414 |
| Final pairwise-coprime blocks | 11,015 |
| Exact-square blocks omitted | 0 |
| Nonsquare matrix rows | 11,015 |
| Matrix rank | 8,926 |
| Kernel dimension | 488 |
| Kernel basis vectors tested | 488 |
| Useful kernel basis vectors | 258 |

The seed basis reconstructed all 54 distinct seed endpoints and passed a
pairwise-coprime check. The decoder basis reconstructed all 18,828 distinct
decoder endpoints and passed the same check. The latter refinement performed
63,198,989 exact gcd tests.

Kernel-basis vector 392 is the declared main witness:

```text
distinct relation values = 166
exact-root decimal digits = 1283
exact-root SHA-256        = cdcedafc174e4f3eb4b39033f59c40874d4cdc049887a70059af121337393a62
R mod N                   = 132013085
gcd(R - 1, N)             = 19727
gcd(R + 1, N)             = 10267
```

The source multiplies the 166 exact relation values, computes `isqrt`, and
requires `R*R` to equal that product before it records the residue or gcds.
It does the same exact-square check for all 488 kernel-basis vectors.

## Diagnostic evidence

The independent online eliminator processes the first 5,616 retained
relations, including repetitions, in public order. When a combination repeats
an exact relation value twice, the diagnostic removes the pair. This removes a
square factor `P^2`; its root factor is `P`, and every relation has
`P congruent to 1 modulo N`. Therefore normalization preserves the root residue
and both sign gcds.

The first useful online dependency is:

```text
ordinal                     = 5616
occurrence support          = 166
distinct exact-value support= 166
exact-root decimal digits   = 1291
exact-root SHA-256          = 9b9c8626e515aa4867d953e474ff2eaf1d0c79e505d8ec106b943e1105ca7a83
R mod N                     = 70524024
gcd(R - 1, N)               = 10267
gcd(R + 1, N)               = 19727
```

There are 4,293 distinct nonunit exact values in this prefix. The exhaustive
small-support check uses the exact factor-free signatures:

- Support 1 requires a zero signature.
- Support 2 requires two equal signatures.
- Support 3 requires `signature[i] xor signature[j] = signature[k]`.

The replay exhausts all three cases. It finds zero square dependencies of
support 1, 2, or 3. This is stronger than finding zero useful dependencies in
those support sizes. It does not test or claim global minimality from support
4 through 165.

## Correctness argument

For every retained presentation `(c,w)`, exact modular inversion gives

```text
c*w congruent to 1 modulo N.
```

Its relation value is the positive integer `P = c*w`. Before retention, the
replay computes both `gcd(c-w,N)` and `gcd(c+w,N)`. A proper result is already
a factor. The public run gets no proper result at this stage.

Every gcd-basis split is an exact identity. Expanding a refinement DAG node
therefore reconstructs its original endpoint. Strictly smaller children make
the process terminate. When insertion finishes, a new active leaf is coprime
to every prior active leaf. Splitting a prior leaf and reinserting all children
preserves that invariant. The final prefix-product gcd check independently
verifies pairwise coprimality.

Let the final active blocks be `b_j`, and write relation `P_i` as

```text
P_i = product_j b_j ** a[j,i].
```

Distinct blocks are pairwise coprime. If `b_j` is a square, any power of it is
a square and it needs no parity row. If `b_j` is not a square, it has a prime
with odd valuation. That prime occurs in no other block. Hence a product of
relation values is a square exactly when every nonsquare-block exponent sum is
even. This is exactly the binary column-kernel condition.

For a kernel vector `x`, the implementation computes the exact positive root

```text
R = sqrt(product of selected P_i).
```

Since each selected `P_i` is 1 modulo `N`, `R^2` is 1 modulo `N`. Therefore
`N` divides `(R-1)(R+1)`. If `R` is not globally `+1` or `-1` across the prime
divisors of `N`, one or both sign gcds are proper. Testing every vector in a
full kernel basis is therefore sound. The public vector 392 gives the two
proper gcds above.

The factor-aware audit verifies

```text
202537109 = 10267 * 19727,
```

and proves both factors prime by trial division. It also verifies the mixed CRT
signs:

```text
132013085 mod 10267 = -1; 132013085 mod 19727 = +1
 70524024 mod 10267 = +1;  70524024 mod 19727 = -1
```

Both residues square to 1 modulo `N`.

## Polynomial bit complexity

Let `n = bitlength(N)`, `B = n^2`, and let `M(k)` denote the bit cost of a
`k`-bit multiplication. The bounds below are conservative.

- The trial screen performs `O(n^2)` gcds on `O(n)`-bit integers.
- There are `O(n)` seed inversions and sign tests.
- At most `n` seed pairs generate `2(B+1)n = O(n^3)` candidate positions.
  Each position uses `O(n)`-bit modular arithmetic, one inverse, and two gcds.
- There are therefore `C = O(n^3)` retained relation occurrences and decoder
  columns. Every relation value has fewer than `2n` bits.
- There are `K = 2C = O(n^3)` decoder endpoints. An endpoint below `N` has at
  most `n` terminal block occurrences because every occurrence is at least 2.
  Thus the number of active blocks and strict refinement events is
  `O(Kn) = O(n^4)`.
- The deterministic insertion can scan all active blocks. A conservative bound
  is `O(n^8)` gcd tests on `O(n)`-bit values. Exact-root loops and all DAG
  expansions also have polynomial bit cost.
- The parity matrix has `C = O(n^3)` columns and at most `O(n^4)` rows. Online
  bitset elimination costs at most
  `O(C^2 (C + rows)) = O(n^10)` bit operations under this representation.
- There are at most `C` kernel vectors. Each selected-product integer has
  `O(Cn) = O(n^4)` bits. Multiplication, exact square root, and the two final
  gcds are polynomial in that bit length.
- The diagnostic has at most `O(n^3)` distinct values. Its exhaustive
  support-at-most-three enumeration has at most cubic many reported triples,
  still polynomial. Online elimination has the matrix bound above.

Thus the declared bounded rule has polynomial bit complexity in `n`. The hard
timeout is an execution guard and is not part of this asymptotic proof.

## Scope

This PASS proves one finite mechanism witness for `N = 202,537,109`. It proves
that this execution reaches a factor only after joint retained-relation
decoding, and that no individual canonical-inverse sign screen reaches one.

It does not prove an all-input success law, inverse-polynomial success density,
abstract-subgroup expansion, publication novelty, global support minimality, or
a polynomial-time factoring algorithm for arbitrary integers.
