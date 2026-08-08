# Monotone full-source reconstruction report

## Result

**PASS.** The isolated full source completed under the named 900-second hard
timeout. The authoritative runner elapsed time was 12.185525 seconds. The
verifier elapsed time was 12.071118292 seconds. All 39 vectors in the complete
binary kernel basis were tested. Eleven basis vectors had a nonzero normalized
root class. Each of those vectors exposed a proper divisor at a terminal gcd.

This is a result for the supplied integer only. The constant pairs `(2,3)` and
`(2,4)` were historically chosen after experiments. They are now fixed program
text. This report does not claim success for all inputs. It does not give a
probability law. It does not give a factoring algorithm for arbitrary integers.

## Isolation and inputs

Before construction, only the following supplied files were read:

- `MONOTONE_RECONSTRUCT_STATEMENT.md`, SHA-256
  `1cdea0d4292e3f80a54551a3cc5f4c1160cfdf4af2e4ed6a110f35fbeef8936b`.
- `MONOTONE_RECONSTRUCT_INPUT.json`, SHA-256
  `4b1615f7eb4fbb5cb820d51c10c8ce317c919adc0738046db8367ec0398bfa79`.

The public input was `N=3241632473`, `n=32`, and `B=1024=n^2`. The input had
no factor, primality advice, retained-record stop, or dependency index. No
other F111 file and no F98, F109, F110, F115, or F116 file was read. The
implementation used exact integer arithmetic, exact division, modular
arithmetic, gcd, exact perfect-power tests, integer square root, binary bitset
linear algebra, and SHA-256. It did not use integer factorization or a
primality test.

## Exact-value extension theorem

Let the old first-occurrence, nonunit exact values be
`P_1,...,P_m`. Append more ordered records. First-occurrence exact-value
deduplication cannot remove an old value. A new record that equals an old value
is removed. Each new distinct value follows the old values. Thus the old
values are the initial coordinate block of the extended matrix.

Let `x` be in the old exact square-class kernel. Extend it to `x'=(x,0)` by
adding one zero for each new coordinate. The selected exact product does not
change. Therefore it is still a square. Its positive integer root does not
change. Hence `x'` is in the extended kernel and has the same normalized root
class. Appending records cannot destroy this dependency.

It remains to prove the complete-basis claim. For two kernel vectors `x` and
`y`, let `C` be the coordinates selected by both. Binary addition selects the
symmetric difference. Positivity and exact squareness give

```text
R(x) R(y) = R(x+y) * product(P_i for i in C).
```

Every `P_i` is congruent to 1 modulo `N`. Therefore
`R(x+y) = R(x)R(y) (mod N)`. The root map is a homomorphism from the binary
kernel to the group of square roots of 1 modulo `N`. Quotienting its image by
the global subgroup `{+1,-1}` gives the normalized root-class homomorphism.

Suppose an extended dependency has a nonzero normalized class. If every vector
in a complete binary kernel basis had zero class, linearity would give zero
class for every vector in their span. That span is the complete kernel. This
contradicts the assumed dependency. Thus every complete kernel basis contains
at least one vector with nonzero normalized class. The theorem does not say
that a particular kernel-basis vector persists.

## Factor-free decoder correctness

### Seed gcd basis

An item `(x,s)` means that the block `x` contributes with signature `s` to the
seed endpoints. Each transformation preserves exact endpoint products:

- If `x=r^k` is the maximal exact perfect power, replace `x` by `r` and
  multiply every signature multiplicity by `k`.
- If two overlapping values are equal, merge their signatures.
- If unequal values `x` and `y` overlap at `d=gcd(x,y)`, replace them by
  `(d,s)`, `(x/d,s)`, `(d,t)`, and `(y/d,t)`.
- Discard a unit block.

The implementation always processes the last work item and the first ordered
basis overlap. It then sorts the final blocks. The verifier checked that every
final block is perfect-power-free, that the blocks are pairwise coprime, and
that their signatures reconstruct all seed endpoints exactly.

### Exact square-class rows

For each distinct relation column `j`, the decoder starts with `(c_j,e_j)` and
`(w_j,e_j)`. Here `e_j` is the one-bit column mask. An entry `(x,A)` means that
`x` occurs in every column selected by `A`.

For an overlap `d=gcd(x,y)>1`, the decoder replaces

```text
(x,A), (y,B)
```

with

```text
(d,A xor B), (x/d,A), (y/d,B).
```

Fix one column and let its bits in `A,B` be `a,b`. The old contribution is
`x^a y^b`. The new contribution is
`d^(a xor b) (x/d)^a (y/d)^b`. Their quotient is 1 in the cases `00`, `10`,
and `01`. It is `d^2` in the case `11`. Thus each replacement preserves every
column product modulo exact integer squares.

The stable terminal values are pairwise coprime. A selected product is a square
exactly when the mask of each nonsquare terminal value has even intersection
with the selection. Pairwise coprimality is essential here: each nonsquare
terminal value has an odd prime exponent that occurs in no other terminal
value. A square terminal value gives no constraint. Therefore the emitted
binary rows describe the exact square-class kernel. No factorization is needed
to construct them.

The row reduction installs one pivot for each independent row. It then creates
one solution for every free column. It verifies every solution against every
row. Hence the returned vectors form a complete binary kernel basis.

## Fixed-input source audit

The trial screen tested all 1,023 integers from 2 through 1,024. Every gcd was
1.

The deterministic seed basis ended with these 23 blocks:

```text
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 3595103, 12214847,
20010077, 24880951, 58995227, 69463553, 116496167, 287564171,
305094821, 514544837, 736734653, 2992276129
```

It processed 62 initial endpoint items and 464 work pops. It made 3,467 exact
perfect-power exponent tests, 19 perfect-power extractions, 6,234 basis gcd
tests, 186 overlap transformations, 114 equal merges, and 72 unequal splits.
It produced 129 final signature entries. Exact reconstruction passed.

The complete source attempted

```text
(n-1) + 2*(n+1)*(B+1) = 67,681
```

positions. The 31 frozen pairs accounted for 63,581 attempts, 14,351 retained
residues, and 49,230 duplicate residues. The appended pair `(2,3)` accounted
for 2,050 attempts and no new residue. The appended pair `(2,4)` accounted for
2,050 attempts, 1,533 new residues, and 517 duplicate residues. The complete
source retained 15,884 residues and saw 51,797 duplicates. The maximum endpoint
bit length was 32. The maximum exact relation-value bit length was 64. The
record trace SHA-256 was
`be3fcdfbfd61bb87797023c3b93a020d74e01d9988fd5d7c69abf383351b5279`.

Every newly retained residue received both sign screens. No direct screen gave
a proper divisor. The minus screen had 15,883 unit results and one improper
result equal to `N`. The plus screen had 15,884 unit results. The sole improper
case was raw record 6,166, with `c=w=1`, from frozen pair index 11,
`(13,2992276129)`, exponent 1, orientation `u_power_times_v`. This is the
required `gcd(c-w,N)=N` identity case, not a factor.

Exact-value first-occurrence deduplication removed one `P=1` record and 2,921
repeated exact values. It left 12,962 distinct nonunit columns. Their value
sequence SHA-256 was
`580feb2987b1bf5ddeaadd06682d9887b2279f44fc8cc752a38b972d89b2fcce`.
The first-occurrence raw-index sequence SHA-256 was
`bcd2f277c883b9c0f6c8462a2bb7a51a210bb2a0cf02fbcccc1fc0ef2e22cbb1`.

The factor-free parity refinement started with 25,924 endpoint entries. It
performed 87,979 refinements and 289,861 work pops. It made 78,898,114 block
gcd tests and 2,180,491 ordered leaf gcd tests. The stable store used 105,078
slots. It ended with 17,099 pairwise-coprime terminal blocks. All were
nonsquares. The decoder emitted 17,099 row masks, of which 14,269 were
distinct. The row sequence SHA-256 was
`13bf60d3a534d6cd549655da09e46821a879e87a8300227281f3eb05d5f66481`.

Binary elimination on the 12,962 columns gave rank 12,923 and nullity 39. It
used 147,091 row-reduction XORs and 7,132 kernel-solve XORs. The complete basis
sequence SHA-256 was
`0d2d7fe80460c2fcc7aaabdbce77b5b723e25d8647409a4dfb1421df05da6d0d`.

## Every kernel-basis root

For every basis vector, the verifier multiplied the selected exact relation
values, tested the exact positive integer square root, reduced that root modulo
`N`, checked that its square was 1 modulo `N`, and computed both terminal gcds.
All 39 exact products were squares. All 39 modular roots squared to 1.

| Basis | Support | Root modulo `N` | `gcd(root-1,N)` | `gcd(root+1,N)` | Class |
|---:|---:|---:|---:|---:|:---|
| 0 | 341 | 2182851487 | 41011 | 79043 | nonzero |
| 1 | 310 | 2182851487 | 41011 | 79043 | nonzero |
| 2 | 364 | 1058780986 | 79043 | 41011 | nonzero |
| 3 | 340 | 3241632472 | 1 | 3241632473 | -1 |
| 4 | 330 | 1058780986 | 79043 | 41011 | nonzero |
| 5 | 386 | 3241632472 | 1 | 3241632473 | -1 |
| 6 | 368 | 3241632472 | 1 | 3241632473 | -1 |
| 7 | 393 | 1 | 3241632473 | 1 | +1 |
| 8 | 374 | 3241632472 | 1 | 3241632473 | -1 |
| 9 | 329 | 1058780986 | 79043 | 41011 | nonzero |
| 10 | 347 | 2182851487 | 41011 | 79043 | nonzero |
| 11 | 395 | 1058780986 | 79043 | 41011 | nonzero |
| 12 | 353 | 1 | 3241632473 | 1 | +1 |
| 13 | 337 | 1 | 3241632473 | 1 | +1 |
| 14 | 354 | 1 | 3241632473 | 1 | +1 |
| 15 | 299 | 1058780986 | 79043 | 41011 | nonzero |
| 16 | 328 | 3241632472 | 1 | 3241632473 | -1 |
| 17 | 375 | 2182851487 | 41011 | 79043 | nonzero |
| 18 | 335 | 2182851487 | 41011 | 79043 | nonzero |
| 19 | 381 | 1058780986 | 79043 | 41011 | nonzero |
| 20 | 6 | 1 | 3241632473 | 1 | +1 |
| 21 | 6 | 1 | 3241632473 | 1 | +1 |
| 22 | 8 | 1 | 3241632473 | 1 | +1 |
| 23 | 6 | 1 | 3241632473 | 1 | +1 |
| 24 | 6 | 1 | 3241632473 | 1 | +1 |
| 25 | 6 | 1 | 3241632473 | 1 | +1 |
| 26 | 6 | 1 | 3241632473 | 1 | +1 |
| 27 | 8 | 1 | 3241632473 | 1 | +1 |
| 28 | 12 | 1 | 3241632473 | 1 | +1 |
| 29 | 6 | 1 | 3241632473 | 1 | +1 |
| 30 | 6 | 1 | 3241632473 | 1 | +1 |
| 31 | 6 | 1 | 3241632473 | 1 | +1 |
| 32 | 6 | 1 | 3241632473 | 1 | +1 |
| 33 | 6 | 1 | 3241632473 | 1 | +1 |
| 34 | 8 | 1 | 3241632473 | 1 | +1 |
| 35 | 6 | 1 | 3241632473 | 1 | +1 |
| 36 | 8 | 1 | 3241632473 | 1 | +1 |
| 37 | 10 | 1 | 3241632473 | 1 | +1 |
| 38 | 6 | 1 | 3241632473 | 1 | +1 |

There were 23 global `+1` roots, five global `-1` roots, and eleven nonzero
normalized root classes. The nonzero roots were `1058780986` and its negative
`2182851487` modulo `N`. Their terminal gcds gave the proper divisors 41,011
and 79,043. This terminal result was derived from every basis-root test. It was
not supplied as input.

## Uniform polynomial-bit-time bound

Let `n` be the bit length of the input odd integer and let `B=n^2`.

The source has

```text
S = (n-1) + 2(n+1)(n^2+1) = O(n^3)
```

positions. Modular exponentiation, inversion, and gcd operate on `O(n)`-bit
integers and polynomial-size exponents. Every endpoint is less than `N`, so it
has at most `n` bits. Every exact relation value is less than `N^2`, so it has
at most `2n` bits. The number `m` of distinct nonunit relation columns is at
most `S=O(n^3)`.

Invertibility is also uniform. If the initial trial branch continues, every
integer from 2 through `B` is a unit modulo `N`. This includes the seeds and
the constant-pair entries. Every seed inverse is a unit. Every final seed block
divides a seed endpoint, so every frozen-pair entry is a unit. Powers and
products of these entries remain units. Thus every requested inverse exists
after the trial branch.

For the seed basis, there are `E_0=2(n-1)` endpoint items. Use prime factors
only as abstract tokens in this complexity proof. The algorithm never computes
them. The number of prime-factor tokens, with multiplicity, is at most
`E_0 n=O(n^2)`.

Define the cohabitation potential of an item `(x,s)` as

```text
sum_j s_j * binomial(Omega(x),2),
```

where `Omega(x)` is the abstract number of prime factors with multiplicity.
Sum this over all work and basis items. The initial potential is `O(n^3)`.
Perfect-power extraction cannot increase it. An equal merge leaves it
unchanged because it adds signatures. Every unequal gcd split strictly lowers
it: at least one of `x` or `y` is split into two nonunit factors, and the
cross-factor token pairs cease to cohabit. Thus there are `O(n^3)` unequal
splits. Each unequal split raises the item count by at most two. Each equal
merge lowers it by one. Therefore equal merges and all work pops are also
`O(n^3)`. A direct ordered scan has `O(n^3)` live items, so even the coarse
bound is `O(n^6)` seed-basis gcd tests. Exact perfect-power testing scans at
most `O(n)` exponents on `O(n)`-bit values. The complete seed-basis stage is
polynomial bit time.

For exact square-class refinement, start with `E=2m=O(n^3)` endpoint entries.
Their total input bit length is

```text
L <= 2mn = O(n^4).
```

For one overlap, the product of the two replaced values changes from `xy` to
`xy/d`, where `d>=2`. Hence the product of all active integer values decreases
by a factor of at least two. There are at most `L` refinements. The work and
stable stores therefore use `O(E+L)=O(n^4)` slots. A full ordered overlap scan
would use `O((E+L)^2)=O(n^8)` gcd queries. The implemented 128-entry
block-product scan has the same polynomial worst-case bound. All values and
fixed-size block products have `O(n)` bits. Each mask has `m=O(n^3)` bits.

There are at most `O(n^4)` terminal rows and `O(n^3)` columns. A coarse bitset
Gaussian-elimination bound is `O(r m^2)=O(n^10)` bit operations for `r` rows,
plus `O(m^3)` for a complete kernel basis. The basis has at most `m=O(n^3)`
vectors.

One dependency selects at most `m` relation values. Its exact product has less
than `2nm=O(n^4)` bits. The verifier performs at most `m` exact products,
integer square roots, modular reductions, and two gcd tests on integers of
polynomial bit length. Therefore the full source, complete decoder, and every
basis-root test form one uniform polynomial-bit-time computation from `N`,
`n`, and `B`.

## Exact boundary

The computation is complete for the stated source. It uses every prescribed
source position. It uses one global first-residue rule. It deduplicates exact
values only after the source ends. It computes a complete factor-free kernel
basis. It tests every basis vector. It uses no certificate stop and no supplied
dependency support.

The success claim is only this: for the supplied `N`, this fixed complete
source and decoder contain a nonzero normalized root and expose proper terminal
divisors. The extension theorem is general, but it only says that later source
records preserve an already existing nonzero class and that a complete basis
must reveal one. It does not show that such a class exists for every input.
